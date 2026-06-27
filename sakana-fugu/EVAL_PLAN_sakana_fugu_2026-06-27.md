# Sakana Fugu — Narrow Evaluation Plan

**Prepared:** 2026-06-27
**For:** ProcessSmith
**Status:** Evaluation design (pre-registration)
**Companion to:** [Sakana Fugu Research Brief](REPORT_sakana_fugu_2026-06-27.md)

---

## Purpose

Decide one thing with evidence, not vibes: **does `fugu-ultra` produce materially
better accepted output on hard tasks than the stack we already run — and is it worth
the added cost, latency, and review burden?**

This is deliberately a small, pre-registered experiment. We write down the arms,
tasks, rubrics, and pass criteria *before* running anything, so the result can't be
talked into the answer we hoped for.

### Why this design (and why it reuses Debate-Harness)

This is the same question the [Debate-Harness](../../Debate-Harness/POSTMORTEM.md)
project asked — *does multi-model orchestration beat one strong model?* — and it
concluded **no** for hand-rolled debate/build scaffolds. Fugu is the *vendor's*
version of that hypothesis: orchestration learned end-to-end instead of scaffolded by
us. So the honest move is a rematch on the same terms, reusing the measurement
discipline that postmortem paid for in two retracted headlines:

- Score **rubric coverage** and **verifiable correctness**, never a subjective
  "which answer is better?" LLM judge — that judge is noisy and **rewards length**,
  and nearly produced a false "debate wins" result.
- Build rubrics **before** seeing any output.
- **Validate every answer is on-topic before scoring** — one contaminated baseline
  once inflated a whole result.
- **Control confounds:** length (the loser often just lost on brevity) and
  synthesizer (different models writing the final answer).
- **Beware ceiling effects** — if the single model already scores ~100%, you learn
  nothing. Pick high-headroom tasks.
- Judge **blind** to which arm produced which answer, in randomized order.

---

## The arms

The point of the postmortem's §7 is that the bar isn't "single pass" — it's "one
strong model + a good prompt + *maybe self-consistency*." So we test three arms, not
two:

| Arm | What it is | Role |
| --- | --- | --- |
| **A — Single** | Claude Opus 4.8, one pass, our normal prompt | Reigning champion; the baseline to beat |
| **B — Fugu** | `fugu-ultra` via Sakana OpenAI-compatible API, one pass | The candidate under test |
| **C — Self-consistency** | Claude Opus 4.8 sampled ×3, best/merged | The *cheap* bar Fugu must clear to justify itself |

If Fugu can't beat Arm C, it isn't earning its premium — Arm C is far cheaper and
stays entirely inside our existing trust boundary.

---

## Task classes

Three classes, each chosen because acceptance is **objectively scorable** and each
maps to real ProcessSmith work. Target **n = 5 items per class** (15 items × 3 arms =
45 runs). Small, but enough to get past the single-datapoint noise that swung the
Debate-Harness headline twice. This is signal, not proof.

### 1. Research brief

Same question, same source requirements, all three arms.

- **Scoring:** rubric coverage % against a rubric written before runs, **plus
  citation validity** — every cited URL must resolve *and* actually support the
  claim (the exact check performed on the Fugu brief itself in PR #2 — we dogfood it).
- **Source items:** reuse high-headroom research questions where a single pass leaves
  real gaps (avoid topics Opus already nails cold).

### 2. Code review

Same PR to all three arms. Use PRs with a **known, planted defect set** (a mix of a
real correctness bug, a security issue, a broken contract, and one tempting
false-positive trap).

- **Scoring:** true defects found ÷ planted defects; count false positives; count
  missed defects; record review wall-clock. Objective because the defect set is known
  in advance.
- **Compare against** our existing reviewer / `/code-review` output on the same PRs.

### 3. Loop-contract critique

Same automation proposal to all three arms — an OpenClaw loop spec with **known
missing verifiers and known risks** seeded in.

- **Scoring:** risks identified ÷ seeded risks; quality of proposed verifier design
  against a pre-built rubric; false-alarm count.

---

## Metrics

| Metric | Definition |
| --- | --- |
| **Quality** | Rubric coverage % and/or verifiable-correctness rate, per task class |
| **Citation/defect integrity** | Cited sources that resolve + support; planted defects caught; false positives |
| **Accepted-output cost** | Model spend **+** runtime **+** retries **+** human review minutes — per *accepted* artifact, not per token |
| **Latency** | Wall-clock to a usable answer (Fugu Ultra needs longer client timeouts) |

We score **cost per accepted output**, not cost per token. A cheaper token that needs
more review minutes is not cheaper.

---

## Pass criteria (pre-registered)

Fugu earns a named provider lane only if **all** hold:

1. It finds materially useful issues or synthesis that **both** Arm A and Arm C miss.
2. The added latency, cost, and verification burden don't wipe out that benefit
   (positive on **accepted-output cost**, not just raw quality).
3. Outputs stay **auditable and source-grounded**.
4. The data-handling posture is acceptable for the task class.

**Decision rule:** consistently clears all four → promote to a named optional lane
("hard-research backstop" / "secondary code-review judge"). Mainly produces longer
answers without higher acceptance → keep as a niche comparison model or drop. (The
Debate-Harness §4 lesson: a subjective judge rewards length — don't let verbosity
read as quality.)

---

## Data-governance gates (hard pre-conditions)

None of these is optional, and all precede any run:

- [ ] Dedicated **scoped Sakana API key**, smallest plan or pay-as-you-go.
- [ ] **Training-data use disabled** in the Sakana console before anything beyond
      public examples.
- [ ] A **separate Codex profile / API harness** — never the live operator path
      (Jimmy/Max), per the brief's installer caution. Do **not** pipe
      `curl … | bash` into the operator environment; reproduce the minimal provider
      block by hand.
- [ ] **No client-confidential data, financials, or personal data.** Public research,
      public-code review, and synthetic seeded tasks only.
- [ ] **EU/EEA note:** Sakana is not yet available there (working toward GDPR
      compliance). We're in Canada, so local testing is fine; any EU/EEA client data
      stays out regardless of how this eval lands.

---

## Runbook

1. **Pre-register** — freeze this doc: the 15 items, the three rubrics, and the pass
   criteria, before generating any output. (Rubrics-before-outputs is non-negotiable.)
2. **Provision** — scoped key, training opt-out, separate Codex profile (gates above).
3. **Generate** — run all 15 items through Arms A, B, C. Capture full transcripts,
   token counts, retries, and wall-clock per run.
4. **Validate inputs** — confirm every answer is on-topic before scoring; discard and
   re-run any contaminated/off-topic output (don't let it into the numbers).
5. **Blind score** — anonymize arm labels, randomize order, score against the frozen
   rubrics. Log review minutes per artifact as you go.
6. **Tally** — quality, integrity, accepted-output cost, latency per arm per class.
7. **Decide** — apply the pass criteria and decision rule. Write `findings.md` next to
   this plan (mirroring the Debate-Harness `docs/*/findings.md` pattern), with every
   claim auditable back to a transcript.

---

## Cost envelope (rough)

Fugu Ultra pay-as-you-go is $5 / $30 per 1M input/output tokens (≤272K context).
Forty-five runs of bounded research/review prompts is plausibly **single-digit to low
tens of dollars** of Fugu spend, plus the Opus spend for Arms A and C. The dominant
real cost is **human review minutes** — which is exactly why we measure them.

The Debate-Harness experiments cost ~$1.33 on value models for dozens of runs; this is
a comparable-scale experiment, not an open-ended one.

---

## What this plan deliberately does *not* do

- No client data, no production loop, no default-agent routing — those are out until
  (and unless) Fugu earns a lane *and* a separate data-governance review clears them.
- No verdict on Fugu's vendor-resiliency pitch — that's a strategic question this
  small eval can't answer and isn't trying to.
- No claim that this n proves anything. It's a go/no-go signal for whether a larger,
  task-specific evaluation is worth funding.
