# Sakana Fugu Evaluation — Findings

**Prepared:** 2026-06-27
**For:** ProcessSmith
**Status:** Complete — first-pass scoring against the frozen pre-registration
**Companion to:** [Pre-Registration](PREREG_sakana_fugu_2026-06-27.md) · [Eval Plan](EVAL_PLAN_sakana_fugu_2026-06-27.md) · [Brief](REPORT_sakana_fugu_2026-06-27.md)

---

## Decision: **Trial** (niche backstop, re-evaluate) — not a default runtime

Fugu Ultra produced **materially better, source-grounded output that both Opus arms missed** in two of
three task classes (research breadth and risk-critique depth), and — contrary to the n=1 smoke-test
worry — showed **no "no live citations" failure**: it cited real, verifiable sources and abstained
honestly on the fabrication trap. But it costs **~4–5× single Opus and ran ~10× slower** (54 min vs
5.5 min for the same 15 items), and on the one fully-objective key (planted code defects) it tied —
finding nothing the cheap arms missed. That profile is a **niche backstop for hard research/critique
where breadth justifies the cost**, not a default. It does **not** cleanly clear the pre-registered
"net-positive on accepted-output cost" bar, which is why this is Trial, not Adopt.

---

## The three arms, as run

| Arm | What | Cost | Wall-clock (15 items) |
| --- | --- | --- | --- |
| **A** | Opus 4.8, single pass | $0.56 | 5.5 min |
| **B** | `fugu-ultra` | $2.48 | **54 min** |
| **C** | Opus 4.8 ×3 + synthesis (self-consistency) | $2.71 | 21 min |

All 45 runs completed clean (15/15 per arm). Total spend **$5.75**. Opus arms used adaptive thinking at
high effort, so Arm A is a genuinely strong baseline — which matters for the result below.

---

## Results by class

### Code review (planted defects + traps) — **three-way tie (ceiling effect)**
Every arm found **15/15 planted defects**, flagged **0/5 traps** as bugs, and logged **0 false positives**.
The objective key saturated — exactly the ceiling effect the pre-registration flagged as a risk for
fully-knowable keys. Qualitatively Fugu was the most *rigorous* reviewer (explicitly affirmed each trap
as correct; caught peripheral-but-real issues like C4's installer-runs-before-`sudo` privilege path),
and Arm C edged Arm A on consistency — **but Fugu found no planted defect the cheap arms missed.** On
this class, the 5× cost and 10× latency bought rigor, not recall.

### Loop-contract critique (seeded risks) — **Fugu clearly best**
| Arm | Seeded risks (/25) | Verifier quality | Bonus risks |
| --- | --- | --- | --- |
| A | 21 | 2.0 | ~8 |
| **B** | **25** | 2.0 | **~17** |
| C | 24 | 2.0 | ~12 |

Fugu hit every seeded risk and surfaced the richest set of *valid* extras — several of them genuinely
sharp and **unique to it**: control-plane-reachable-from-data-plane (if the agent can edit its own
allowlist/audit log, every other control is moot), TOCTOU/approval-binding, a conservation-invariant
reframing of "nothing sits unsorted" (received = filed + quarantined + pending + failed), and the
"exit 0 ≠ goal achieved" silent-wrong-success framing. **Arm C (self-consistency) closed most of the
gap to Fugu and beat single Opus** — the synthesis pass recovered risks a single pass dropped.

### Research brief (coverage + citation validity) — **Fugu best; the Opus arms self-sabotaged on R1**
| Arm | Avg coverage | Notable |
| --- | --- | --- |
| A | ~70% | Strong R2–R5; **refused R1 entirely** |
| **B** | **~82%** | Best breadth; real citations throughout |
| C | ~71% | Matches A; also refused R1 |

The decisive item was **R1** (compare Anthropic/OpenAI/Sakana data policies). **Both Opus arms refused
to state stable, knowable facts** (Anthropic/OpenAI default-no-train, retention windows) — treating the
whole question as unanswerable. Fugu answered the two knowable vendors fully with real source URLs and
**correctly abstained on the Sakana row** (the fabrication trap). Critically for the citation-honesty
concern: a scorer spot-verified Fugu's most unusual citation (**EDPB Opinion 28/2024**) as real and
accurately described. **No arm fabricated.** The only confidence error in the whole set ran the *other*
way — Opus A/C wrongly disclaiming knowable facts.

---

## Pass criteria (from the frozen pre-registration)

| Criterion | Verdict |
| --- | --- |
| Surfaces useful output **both A and C miss** | **Yes** — loop-critique bonus risks + R1 coverage. (No, on code review.) |
| **Net-positive on accepted-output cost** (incl. latency/review) | **No / borderline** — ~5× cost, ~10× latency for a real-but-modest quality edge |
| **Auditable and source-grounded** | **Yes** — real citations, no fabrication, honest abstention |
| **Data posture acceptable** for the class | **Yes** for public/non-sensitive with training opt-out |

Three of four hold; the cost/latency criterion is the one it fails — which is the whole reason it lands
at Trial rather than Adopt.

---

## A second, unexpected finding: self-consistency barely earns its keep either

Arm C (the "cheap bar" Fugu had to beat) **edged single Opus on every class but never beat Fugu**, and
it cost **~5× Arm A** (4 calls + 4× synthesis input) for that modest edge. So the cheapest arm — a
single Opus pass with adaptive thinking — was remarkably close to the best on the objective keys.
**Single strong model + good prompt remains hard to beat on cost-adjusted quality** — the same lesson
the Debate-Harness postmortem reached, now reconfirmed with a vendor's learned orchestration on one
side and self-consistency on the other.

---

## Recommended use (the Trial lane)

- **Use Fugu for:** hard, breadth-sensitive research synthesis and adversarial risk-critique where
  surfacing the one risk everyone else missed is worth minutes and a few cents — i.e. a **"second
  opinion / hard-research backstop,"** run *alongside* the Opus path, not as the default.
- **Don't use Fugu for:** anything latency-sensitive (54 min/15 items is disqualifying for interactive
  work), routine tasks (single Opus is ~5× cheaper and nearly as good), client-confidential data
  (unchanged from the brief), or code-defect detection (no edge over the cheap arms here).
- **Default runtime stays Opus single-pass.** Reserve self-consistency for the specific cases where its
  small, measured edge matters.

---

## Caveats (don't over-read this)

- **n = 5 per class.** This is a go/no-go signal, not proof. The headline differences (loop-critique
  breadth, R1 coverage) are clear; the code-review tie is uninformative because the key ceilinged.
- **First-pass scoring** was done by independent scorers against the frozen answer keys. A human
  second pass is recommended per the pre-registration — especially on research coverage and exhaustive
  citation-URL verification (only the most load-bearing URLs were spot-checked).
- **Same-author caveat:** the eval items and the model outputs were generated by the same family on the
  Opus arms; scoring was against objective frozen keys to mitigate, but a fully independent re-score
  would strengthen confidence.
- **Fugu's citation honesty is the most decision-relevant surprise** and most deserves the human
  re-check — it directly contradicts the smoke-test read, so confirm it before relying on it.
