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
export ANTHROPIC_API_KEY=...        # Arms A and C
export SAKANA_API_KEY=...           # Arm B only
```

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

## Before trusting the numbers
- **Fill in Opus pricing** in `PRICES` in `run_eval.py` (token counts are always recorded;
  dollar figures are null until you set the rate). Fugu's rate is pre-filled from the brief.
- Arm C's merge method is **synthesis** (logged in every record). Change `MERGE_METHOD` /
  `run_arm_c` if you want best-of-N instead — but pick one and keep it uniform.
- Sakana also exposes the Responses API and reasoning-effort levels (`high`/`xhigh`/`max`);
  this harness uses plain Chat Completions for clean token accounting. Adjust `_fugu_call`
  if you want to exercise those.

The code-review snippets are fed from `../code/` with a neutral prompt — the harness never
sends the planted-defect keys to the model.
