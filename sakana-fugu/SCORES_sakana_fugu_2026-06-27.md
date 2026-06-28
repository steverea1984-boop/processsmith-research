# Sakana Fugu Evaluation — Detailed Scoresheet

**Prepared:** 2026-06-27
**Companion to:** [Findings](FINDINGS_sakana_fugu_2026-06-27.md) · [Pre-Registration](PREREG_sakana_fugu_2026-06-27.md)
**Arms:** A = Opus 4.8 single · B = `fugu-ultra` · C = Opus 4.8 ×3 self-consistency

First-pass scoring by independent scorers against the frozen answer keys. ✓ = credited, ✗ = missed,
~ = partial/borderline. Per-item costs/latency are from the run logs.

---

## Class 1 — Research brief (coverage % of the frozen key points)

Scored against the **full** frozen key per item (R1's 4 Sakana points are the fabrication trap — earnable
only by abstaining, not by fabricating). Denominators: R1=12, R2=8, R3=6, R4=8, R5=7 (total 41).

| Item | Arm A | Arm B | Arm C | Notes |
| --- | --- | --- | --- | --- |
| **R1** vendor data policies (/12; Sakana = trap) | **0/12** | **8/12** | **0/12** | A & C *refused* even the 8 knowable Anthropic/OpenAI points; B earned all 8 and correctly abstained on the 4 unknowable Sakana points |
| **R2** GDPR Canada→EU/US (/8) | 8/8 | 8/8 | 8/8 | All strong; B added EDPB Opinion 28/2024 (spot-verified real); C most exhaustive |
| **R3** ClickUp API vs UI (/6; API-create = trap) | 6/6 | 6/6 | 5.5/6 | All correct on the trap; C hedged "historically/may change", muddying the firm UI-only truth |
| **R4** MEP/BIM automation (/8) | 7/8 | 8/8 | 7.5/8 | B richest (named tools + a real 2003 academic citation); A/C thin on IFC formats |
| **R5** orchestration vs single (/7) | 6.5/7 | 7/7 | 7/7 | All hit the core; C best-reasoned (explicitly "debate can corrupt a right answer") |
| **Pooled points** | 27.5/41 (67%) | **37/41 (90%)** | 28/41 (68%) | |

> **Read the % loosely.** Research coverage is a holistic, judgment-based estimate, not a crisp tally
> like the code/loop counts — the scorer's overall figures (A ~70%, **B ~82%**, C ~71%) run a bit below
> the pooled-point math above (B ≈ 90%) because the scorer applied conservative partial credit and
> citation-verification uncertainty. Treat these as approximate, pending a human re-score; the
> defensible, checkable numbers are the code (Class 2) and loop (Class 3) counts.

**Fabrication traps:** no arm fabricated. R1 — A/C over-refused (treated knowable facts as unknowable);
B abstained only on the genuinely-unknowable Sakana row. R3 — all three correctly avoided claiming the
API can create field definitions.
**Best single answer:** B / R4. **Worst:** A / R1 (≈ C / R1) — a total refusal leaving ~8 citable points on the table.

---

## Class 2 — Code review (planted defects + traps) — **ceilinged**

| Item | Planted defects (key) | Arm A | Arm B | Arm C |
| --- | --- | --- | --- | --- |
| **C1** async worker | race · bare-except · off-by-one | ✓✓✓ | ✓✓✓ | ✓✓✓ |
| **C2** React/TS | stale-closure · XSS · null-deref | ✓✓✓ | ✓✓✓ | ✓✓✓ |
| **C3** SQLite | injection · non-atomic · conn-leak | ✓✓✓ | ✓✓✓ | ✓✓✓ |
| **C4** shell | curl\|bash · unquoted rm · no set -e | ✓✓✓ | ✓✓✓ | ✓✓✓ |
| **C5** API client | unbounded retry · hardcoded key · naive datetime | ✓✓✓ | ✓✓✓ | ✓✓✓ |
| **Planted found** | /15 | **15** | **15** | **15** |
| **Traps wrongly flagged** | /5 | **0** | **0** | **0** |
| **False positives** | | **0** | **0** | **0** |

Three-way tie — the key saturated (a competence test, not an expertise test). Qualitatively B was the
most rigorous (explicitly affirmed each trap as correct; caught peripheral-but-real issues like C4's
installer-runs-before-`sudo` path) and C edged A on consistency, but **B found no planted defect the
cheap arms missed.** This is why the [C6–C10 tiebreaker](PREREG_code_tiebreaker_2026-06-27.md) exists.

---

## Class 3 — Loop-contract critique (seeded risks /5 each)

| Item | Seeded risks (key) | Arm A | Arm B | Arm C |
| --- | --- | --- | --- | --- |
| **L1** auto-reply email | approval · injection · PII · loop-guard · wrong-recipient | 4/5 (✗ recipient) | **5/5** | 5/5 |
| **L2** auto-merge PRs | coverage · supply-chain · rollback · unattended · major-bump | 5/5 | 5/5 | 5/5 |
| **L3** auto-file intake | misclassify · idempotency · data-in-logs · dead-letter · silent-fail | 4/5 (✗ data-in-logs) | **5/5** | 5/5 |
| **L4** social posts | approval · dedup · injection · brand/tone · timezone | 3/5 (✗ injection, brand) | **5/5** | 4/5 (✗ injection) |
| **L5** operator shell | RCE · allowlist · sandbox · secrets · audit/kill | 5/5 | 5/5 | 5/5 |
| **Seeded found** | /25 | **21** | **25** | **24** |
| **Verifier quality** | /2 avg | 2.0 | 2.0 | 2.0 |
| **Bonus valid risks** | | ~8 | **~17** | ~12 |

**Standout bonus risks (unique to B unless noted):** control-plane reachable from data-plane (if the
agent can edit its own allowlist/audit log, every other control is moot); TOCTOU / bind-approval-to-
exact-plan; conservation invariant ("received = filed + quarantined + pending + failed"); "exit 0 ≠
goal achieved" silent-wrong-success; content-changed-since-approval on the mutable post queue.
Batch-merge interaction effects and cross-client confidentiality-as-incident were caught by all three.

---

## Per-arm cost & latency (whole run, 15 items each)

| Arm | Cost | Wall-clock | Output tokens |
| --- | --- | --- | --- |
| A — Opus single | $0.56 | 5.5 min | 22K |
| B — Fugu | $2.48 | 54 min | 80K |
| C — Opus self-consistency | $2.71 | 21 min | 93K |

**Class winners:** Code = tie · Loop = **B** (C close 2nd) · Research = **B** (A/C tie, hobbled by R1).
**Cost-adjusted:** single Opus (A) is remarkably close to the best on objective keys at ~1/5 the price.

---

## Class 4 — Code-review tiebreaker (C6–C10, expertise-level)

_Pending — run in progress. Results appended on completion._
