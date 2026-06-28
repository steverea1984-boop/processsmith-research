#!/usr/bin/env python3
"""Sakana Fugu evaluation harness — generation pass for Arms A / B / C.

Runs the 15 frozen pre-registration items through:
  Arm A — Opus 4.8, single pass          (Anthropic API)
  Arm B — fugu-ultra                      (Sakana, OpenAI-compatible API)
  Arm C — Opus 4.8 x3 self-consistency    (Anthropic API + a synthesis pass)

For each run it records: output text, token usage, wall-clock latency, and the
number of retries. This is a STANDALONE, ISOLATED generator — it talks only to
the two model APIs and the frozen item set. Do not run it inside the live
operator (Jimmy/Max) environment, and never feed it the pre-registration doc or
the planted-defect keys.

Environment:
  ANTHROPIC_API_KEY   required for Arms A and C
  SAKANA_API_KEY      required for Arm B

Examples:
  python run_eval.py --arms A C                 # Opus arms only (no Sakana key needed)
  python run_eval.py --arms A B C               # full run
  python run_eval.py --arms B --items R1 C3 L5  # a subset
  python run_eval.py --arms A B C --blind        # also emit an anonymized scoring packet
"""
from __future__ import annotations

import argparse
import json
import os
import random
import time
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
ASSETS = HERE.parent                 # sakana-fugu/eval-assets
CODE_DIR = ASSETS / "code"
ITEMS_PATH = HERE / "items.json"
RESULTS = HERE / "results"

OPUS_MODEL = "claude-opus-4-8"
FUGU_MODEL = "fugu-ultra"
SAKANA_BASE_URL = "https://api.sakana.ai/v1"

# USD per 1M tokens (input, output). Opus 4.8 = $5/$25; Fugu Ultra = $5/$30
# (<=272K-context tier, per the brief). "Output" includes thinking tokens.
PRICES = {
    OPUS_MODEL: {"in": 5.0, "out": 25.0},
    FUGU_MODEL: {"in": 5.0, "out": 30.0},
}

SELF_CONSISTENCY_N = 3
MERGE_METHOD = "synthesis"   # recorded in every Arm-C result
MAX_RETRIES = 4
MAX_TOKENS = 16000           # room for adaptive thinking + answer without truncation
FUGU_TIMEOUT_S = 600         # Fugu Ultra can be slow; give it room


# --------------------------------------------------------------------------- #
# Provider calls. Each returns (text, {"in": int, "out": int}).
# --------------------------------------------------------------------------- #

def _anthropic_client():
    import anthropic
    return anthropic.Anthropic()  # reads ANTHROPIC_API_KEY


def _sakana_client():
    from openai import OpenAI
    key = os.environ.get("SAKANA_API_KEY")
    if not key:
        raise RuntimeError("SAKANA_API_KEY is not set (required for Arm B).")
    return OpenAI(base_url=SAKANA_BASE_URL, api_key=key)


def _opus_call(client, prompt):
    # Opus 4.8 rejects temperature/top_p/top_k (400). Diversity for Arm C comes
    # from inherent sampling variation across repeated calls, not a temperature knob.
    def _do():
        resp = client.messages.create(
            model=OPUS_MODEL,
            max_tokens=MAX_TOKENS,
            thinking={"type": "adaptive"},
            output_config={"effort": "high"},
            messages=[{"role": "user", "content": prompt}],
        )
        text = "".join(b.text for b in resp.content if getattr(b, "type", None) == "text")
        return text, {"in": resp.usage.input_tokens, "out": resp.usage.output_tokens}
    return _do


def _fugu_call(client, prompt):
    def _do():
        resp = client.chat.completions.create(
            model=FUGU_MODEL,
            messages=[{"role": "user", "content": prompt}],
            timeout=FUGU_TIMEOUT_S,
        )
        usage = resp.usage
        return resp.choices[0].message.content, {
            "in": usage.prompt_tokens,
            "out": usage.completion_tokens,
        }
    return _do


def _timed_retry(thunk):
    """Run thunk with retries+backoff. Returns (text, usage, retries, latency_s)."""
    start = time.perf_counter()
    last = None
    for attempt in range(MAX_RETRIES + 1):
        try:
            text, usage = thunk()
            return text, usage, attempt, time.perf_counter() - start
        except Exception as exc:  # noqa: BLE001 - transient API errors get a retry
            last = exc
            if attempt < MAX_RETRIES:
                time.sleep(2 ** attempt)
    raise last


# --------------------------------------------------------------------------- #
# Item / cost helpers
# --------------------------------------------------------------------------- #

def build_prompt(item):
    if item["kind"] == "code":
        source = (CODE_DIR / item["file"]).read_text(encoding="utf-8")
        lang = item["file"].rsplit(".", 1)[-1]
        return f"{item['prompt']}\n\n```{lang}\n{source}\n```"
    if item["kind"] == "loop":
        return (
            "Critique this automation proposal for safety and reliability gaps, "
            "and propose the verifiers/controls it needs before it ships:\n\n"
            f"{item['prompt']}"
        )
    return item["prompt"]


def cost_usd(model, usage):
    p = PRICES.get(model, {})
    if p.get("in") is None or p.get("out") is None:
        return None
    return round(usage["in"] / 1e6 * p["in"] + usage["out"] / 1e6 * p["out"], 4)


def _now():
    return datetime.now(timezone.utc).isoformat()


# --------------------------------------------------------------------------- #
# Arms
# --------------------------------------------------------------------------- #

def run_arm_a(item, prompt, anth):
    text, usage, retries, latency = _timed_retry(_opus_call(anth, prompt))
    return {
        "arm": "A", "model": OPUS_MODEL, "method": "single",
        "output": text, "usage": usage, "retries": retries,
        "latency_s": round(latency, 2), "cost_usd": cost_usd(OPUS_MODEL, usage),
    }


def run_arm_b(item, prompt, sak):
    text, usage, retries, latency = _timed_retry(_fugu_call(sak, prompt))
    return {
        "arm": "B", "model": FUGU_MODEL, "method": "single",
        "output": text, "usage": usage, "retries": retries,
        "latency_s": round(latency, 2), "cost_usd": cost_usd(FUGU_MODEL, usage),
    }


def run_arm_c(item, prompt, anth):
    samples, tin, tout, retries, latency = [], 0, 0, 0, 0.0
    for _ in range(SELF_CONSISTENCY_N):
        text, usage, r, lat = _timed_retry(_opus_call(anth, prompt))
        samples.append(text)
        tin += usage["in"]; tout += usage["out"]; retries += r; latency += lat

    joined = "\n\n".join(f"=== Answer {i + 1} ===\n{s}" for i, s in enumerate(samples))
    synth_prompt = (
        "You independently produced the answers below to one task. Synthesize the "
        "single best final answer: keep the strongest, most correct elements of each "
        "and discard anything wrong or unsupported. Return only the final answer.\n\n"
        f"TASK:\n{prompt}\n\n{joined}"
    )
    merged, usage, r, lat = _timed_retry(_opus_call(anth, synth_prompt))
    tin += usage["in"]; tout += usage["out"]; retries += r; latency += lat
    total = {"in": tin, "out": tout}
    return {
        "arm": "C", "model": OPUS_MODEL, "method": f"self_consistency_n{SELF_CONSISTENCY_N}",
        "merge_method": MERGE_METHOD, "samples": samples, "output": merged,
        "usage": total, "retries": retries, "latency_s": round(latency, 2),
        "cost_usd": cost_usd(OPUS_MODEL, total),
    }


ARMS = {"A": run_arm_a, "B": run_arm_b, "C": run_arm_c}


# --------------------------------------------------------------------------- #
# Blind scoring packet
# --------------------------------------------------------------------------- #

def emit_blind_packet(records, seed):
    """Write anonymized answer files + a separate key, for blind scoring."""
    blind_dir = RESULTS / "blind"
    blind_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(seed)
    shuffled = records[:]
    rng.shuffle(shuffled)
    key = {}
    for i, rec in enumerate(shuffled):
        token = f"{i:03d}-{rng.randrange(16**4):04x}"
        (blind_dir / f"{token}.txt").write_text(rec["output"], encoding="utf-8")
        key[token] = {"item": rec["item"], "arm": rec["arm"]}
    (RESULTS / "blind_key.json").write_text(json.dumps(key, indent=2), encoding="utf-8")
    print(f"  blind packet: {len(shuffled)} answers in {blind_dir} (key: blind_key.json)")


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #

def _load_dotenv():
    """Populate os.environ from a local .env (harness dir) without overriding the shell."""
    env_path = HERE / ".env"
    if not env_path.exists():
        return
    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, val = line.partition("=")
        os.environ.setdefault(key.strip(), val.strip().strip('"').strip("'"))


def main():
    _load_dotenv()
    ap = argparse.ArgumentParser(description="Sakana Fugu eval generation pass (Arms A/B/C).")
    ap.add_argument("--arms", nargs="+", default=["A", "B", "C"], choices=list(ARMS))
    ap.add_argument("--items", nargs="+", default=None, help="Item ids to run (default: all).")
    ap.add_argument("--items-file", default=None, help="Items JSON to load (default: items.json).")
    ap.add_argument("--blind", action="store_true", help="Also emit an anonymized scoring packet.")
    ap.add_argument("--seed", type=int, default=0, help="Seed for blind-packet shuffling.")
    args = ap.parse_args()

    items_path = (HERE / args.items_file) if args.items_file else ITEMS_PATH
    items = json.loads(items_path.read_text(encoding="utf-8"))
    if args.items:
        wanted = set(args.items)
        items = [it for it in items if it["id"] in wanted]
        if not items:
            raise SystemExit(f"No items matched {sorted(wanted)}")

    anth = _anthropic_client() if ({"A", "C"} & set(args.arms)) else None
    sak = _sakana_client() if "B" in args.arms else None

    RESULTS.mkdir(parents=True, exist_ok=True)
    records = []
    for item in items:
        prompt = build_prompt(item)
        for arm in args.arms:
            client = sak if arm == "B" else anth
            label = f"{item['id']}/{arm}"
            print(f"running {label} ...", flush=True)
            try:
                rec = ARMS[arm](item, prompt, client)
            except Exception as exc:  # noqa: BLE001 - record the failure, keep going
                rec = {"arm": arm, "error": repr(exc)}
                print(f"  ! {label} failed: {exc!r}")
            rec.update({"item": item["id"], "kind": item["kind"], "ts": _now()})
            out_path = RESULTS / f"{item['id']}__{arm}.json"
            out_path.write_text(json.dumps(rec, indent=2, ensure_ascii=False), encoding="utf-8")
            if "output" in rec:
                cost = rec.get("cost_usd")
                cost_s = f"${cost}" if cost is not None else "$?"
                print(f"  ok  {label}  {rec['usage']}  {rec['latency_s']}s  {cost_s}")
            records.append(rec)

    ok = [r for r in records if "output" in r]
    print(f"\nwrote {len(records)} records ({len(ok)} ok) to {RESULTS}")
    if args.blind and ok:
        emit_blind_packet(ok, args.seed)


if __name__ == "__main__":
    main()
