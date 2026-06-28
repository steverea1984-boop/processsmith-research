# Fugu evaluation harness

Standalone generator for the [frozen pre-registration](../../PREREG_sakana_fugu_2026-06-27.md)
items across the three arms. It only calls the model APIs and reads the frozen item set —
**run it in isolation, never inside the live operator (Jimmy/Max) environment.**

## Arms
- **A** — Opus 4.8, single pass (Anthropic)
- **B** — `fugu-ultra` (Sakana, OpenAI-compatible)
- **C** — Opus 4.8 ×3 self-consistency + a synthesis pass (Anthropic)

## Setup
```bash
python -m venv .venv && . .venv/Scripts/activate   # Windows; use .venv/bin/activate on *nix
pip install -r requirements.txt
```

**Keys** — put them in a `.env` file in *this folder* (it's gitignored; the harness loads it
automatically). Copy `.env.example` to `.env` and fill in:
```
SAKANA_API_KEY=sk-...     # Arm B only
ANTHROPIC_API_KEY=sk-...  # Arms A and C
```
Shell-exported vars (`export SAKANA_API_KEY=...` / PowerShell `$env:SAKANA_API_KEY="..."`) work
too and take precedence over `.env`.

## Run
```bash
python run_eval.py --arms A C                  # Opus arms now (no Sakana key needed yet)
python run_eval.py --arms A B C --blind        # full run + anonymized scoring packet
python run_eval.py --arms B --items R1 C3 L5   # a subset
```

Results land in `results/` (git-ignored): one `<item>__<arm>.json` per run with output,
token usage, latency, retries, and cost. `--blind` also writes `results/blind/*.txt`
(answers only, shuffled) plus a separate `blind_key.json`, so scoring against the frozen
rubrics can be done without seeing which arm produced which answer.

## Model settings & caveats
- **Opus arms** run with adaptive thinking at `effort: "high"` and no sampling params (Opus 4.8
  rejects `temperature`/`top_p`/`top_k`). "Output" token counts and cost therefore include
  thinking tokens.
- **Arm C diversity** comes from inherent sampling variation across the 3 repeated calls — there
  is no temperature knob to widen it on Opus 4.8. Merge method is **synthesis** (logged in every
  record); change `MERGE_METHOD` / `run_arm_c` for best-of-N, but keep it uniform.
- **Prices** in `PRICES` are current as of 2026-06-27 (Opus 4.8 $5/$25, Fugu $5/$30). Re-check
  before trusting dollar figures; token counts are always recorded regardless.
- Rough spend for a full 3-arm, 15-item run: **~$10–15** (Arm C dominates at ~4 Opus calls/item);
  Opus-only A+C is **~$6–10**.
- Sakana also exposes the Responses API and reasoning-effort levels (`high`/`xhigh`/`max`);
  this harness uses plain Chat Completions for clean token accounting. Adjust `_fugu_call`
  if you want to exercise those.

The code-review snippets are fed from `../code/` with a neutral prompt — the harness never
sends the planted-defect keys to the model.
