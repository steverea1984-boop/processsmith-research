# Sakana Fugu Evaluation — Pre-Registration

**Prepared:** 2026-06-27
**For:** ProcessSmith
**Status:** Pre-registration — **FROZEN 2026-06-27** (no edits past the first run)
**Companion to:** [Evaluation Plan](EVAL_PLAN_sakana_fugu_2026-06-27.md) · [Research Brief](REPORT_sakana_fugu_2026-06-27.md)

---

## Freeze statement

This document fixes the **15 task items**, the **3 scoring rubrics**, and the **answer keys**
*before* any output from Arm A (Opus 4.8 single), Arm B (`fugu-ultra`), or Arm C (Opus 4.8
×3 self-consistency) is generated. Per the [Debate-Harness postmortem](../../Debate-Harness/POSTMORTEM.md)
§4 ("measure the right thing"; "rubrics before outputs"), nothing below may be edited once a
single run has happened. If an item turns out to be broken (ambiguous, ceilinged, or
contaminated), it is **dropped whole and logged** — never silently rescored.

Each item was chosen to be **high-headroom** (a single strong pass is expected to leave real
gaps or make real errors) and **objectively scorable** (a fixed key, not a "which reads
better?" judgment).

---

## Scoring protocol (applies to all classes)

1. **Blind.** Arm labels are stripped; the three answers per item are shuffled and scored
   without knowing which arm produced which.
2. **Length-controlled.** Coverage is scored against a fixed key, so a longer answer earns
   nothing for length alone. Where two arms tie on coverage, the **shorter** answer wins the
   tiebreak (guards the §4 "judge rewards length" failure).
3. **On-topic gate first.** Any answer that is off-topic or contaminated is discarded and the
   run repeated before scoring; contamination never enters the numbers.
4. **Two scorers where feasible.** Steve scores; a second pass (independent agent or re-score
   on a later day) checks the high-variance items. Disagreements are reconciled against the key.
5. **Accepted-output cost** is logged per item per arm: model spend + wall-clock + retries +
   **human review minutes**.

Fabricated citations / invented defects / hallucinated risks are **net-negative**: they cost
more points than a miss, because a confident wrong answer is worse than an honest gap.

---

## Class 1 — Research brief (5 items)

Each arm gets the question + the source rule. **Source rule (all items):** every factual claim
must carry a resolvable citation; a cited URL that 404s or does not support the claim scores as
a fabrication. Coverage is scored against the **key points** below (the answer key); each key
point is hit / partial / miss.

### R1 — LLM provider data-governance comparison
**Prompt:** "As of mid-2026, compare the enterprise-tier data-retention and training-data-use
policies of Anthropic (Claude API), OpenAI, and Sakana (Fugu). For each: default training-use,
how to opt out, retention window, and any region restriction. Cite primary sources."
**Why high-headroom:** details are specific, change often, and are easy to conflate across vendors.
**Key points (12):** per-vendor {training-use default, opt-out path, retention window, region
restriction} × 3 vendors. (We already hold ground truth on the Sakana row from the brief — Fugu:
training-use on by default, console opt-out, not-yet-EU/EEA — so that row is a fabrication trap.)

### R2 — Canadian SaaS → EU/EEA via US-hosted LLM
**Prompt:** "A Canadian SaaS wants to serve EU/EEA end-users while routing their data through a
US-hosted LLM API. What are the concrete GDPR obstacles and the available legal mitigations?
Cite the mechanisms by name."
**Why high-headroom:** mixes legal mechanisms a single pass tends to name vaguely or get stale.
**Key points (8):** lawful-basis/consent · data-transfer mechanism (SCCs) · EU-US Data Privacy
Framework status · data-residency / EU region option · DPA with subprocessor · right-to-erasure
vs model training · Canada adequacy (PIPEDA) interaction · DPIA trigger.

### R3 — ClickUp custom-field automation limits
**Prompt:** "What can and cannot be done to ClickUp custom fields via the public API/MCP vs the
web UI? Cover: creating field definitions, setting values, dropdown option management, the native
GitHub integration, and field scoping. Cite docs."
**Why high-headroom:** the API/UI split is subtle and under-documented.
**Ground-truth key (we verified this session) (6):** field *creation* is UI-only · setting
values IS API-writable (`custom_fields:[{id,value}]`) · dropdown value = option UUID · native
GitHub integration column is NOT API-writable · existing workspace fields reusable via "Add
existing" · a field's scope is fixed to its creation location. An arm claiming the API can
create fields scores a fabrication.

### R4 — MEP/BIM automation tooling landscape
**Prompt:** "Summarize the current automation options for MEP coordination in BIM workflows
(Revit-centric): native APIs, Dynamo, and third-party tools. What is genuinely automatable
today vs vendor-promised? Cite sources."
**Why high-headroom:** vendor marketing vs reality is exactly where single passes overclaim.
**Key points (8):** Revit API surface · Dynamo scope/limits · ≥2 named third-party tools with
what each actually does · clash-detection automation reality · data-exchange formats (IFC) ·
one explicit "promised-not-real" caveat.

### R5 — Multi-agent orchestration vs single strong model
**Prompt:** "Does multi-model orchestration (debate, ensemble, learned routing) beat one strong
model + good prompt + self-consistency on hard reasoning/knowledge tasks? Summarize the evidence
and cite it."
**Why high-headroom:** the honest answer is nuanced; marketing-trained priors overstate
orchestration. **Ground truth held:** the [Debate-Harness postmortem](../../Debate-Harness/POSTMORTEM.md)
§1 (single ≥ debate/build every time; self-consistency is the cheaper bar) is the scoring anchor.
**Key points (7):** single ≥ orchestration on knowable-answer tasks · debate can *corrupt* a
right answer · ceiling effect · self-consistency as cheap baseline · cost/latency tax of
orchestration · the narrow case where it might help (frontier-hard) · cites ≥1 real source.

> **Calibration vs discrimination.** R3 (ClickUp API) and R5 (orchestration vs single) use
> ground truth we already hold, so all three arms may *ceiling* on them — they function as
> **integrity / fabrication checks** (catching a confident-wrong answer), not as items expected
> to separate the arms. Discriminating power is meant to come from Classes 2 and 3 plus
> R1/R2/R4, which have real headroom. Score R3/R5 as pass/fail integrity, not coverage deltas.

---

## Class 2 — Code review (5 items)

Each item is a self-contained snippet (40–80 lines) with a **planted defect set** (the answer
key) and at least one **false-positive trap** (something that looks wrong but is correct/benign).
The literal snippet files are authored from these specs as the final freeze step and stored
under `sakana-fugu/eval-assets/code/` (not committed until the eval runs, to avoid leaking the
key into a public diff early). **Score:** recall = real defects found ÷ planted; precision =
real ÷ all flagged; **trap penalty** if the false-positive is reported as a bug; severity-weighted
(security > correctness > style).

### C1 — Python async worker
**Planted (3):** (a) shared dict mutated from concurrent tasks without a lock (race); (b) bare
`except: pass` swallowing cancellation; (c) off-by-one in a batch slice dropping the last item.
**Trap:** a `# TODO: optimize` comment over correct code.

### C2 — React/TypeScript component
**Planted (3):** (a) `useEffect` missing a dependency → stale closure; (b)
`dangerouslySetInnerHTML` fed unsanitized user input (XSS); (c) `obj.user.name` with no null
guard on an optional prop. **Trap:** an `any` cast that is locally justified and harmless.

### C3 — Python + SQL data layer
**Planted (3):** (a) SQL built via f-string interpolation of user input (injection); (b)
multi-statement write with no transaction/rollback; (c) DB connection opened in a loop and never
closed (leak). **Trap:** a raw SQL string that is actually parameterized correctly.

### C4 — Shell setup script
**Planted (3):** (a) `curl -fsSL <url> | bash` of a remote script with no checksum/pin (the
exact Fugu-installer pattern from the brief); (b) unquoted `$VAR` in a path used with `rm`; (c)
no `set -euo pipefail`, so failures continue silently. **Trap:** a `sudo` call that is
appropriate and correctly scoped.

### C5 — Python API client
**Planted (3):** (a) retry loop with no max attempts and no backoff (infinite-retry / hammer);
(b) hardcoded API key string literal; (c) naive `datetime.now()` without tz → UTC/local bug.
**Trap:** a broad `except Exception` that *does* re-raise after logging (correct).

---

## Class 3 — Loop-contract critique (5 items)

Each item is a one-paragraph automation/agent-loop proposal with **seeded missing verifiers and
risks** (the answer key). The arm is asked: "Critique this automation for safety and reliability
gaps; propose the verifiers it needs." **Score:** risks identified ÷ seeded; verifier-design
quality 0–2 per proposed control; false-alarm count.

### L1 — Auto-reply to inbound client emails
**Seeded risks (5):** no human-approval gate before send · prompt-injection from email body ·
PII handling/retention · no rate limit / loop guard on threads · wrong-recipient / reply-all.

### L2 — Nightly auto-merge of dependency PRs when tests pass
**Seeded risks (5):** "tests pass ≠ safe" (coverage gaps) · supply-chain / malicious update ·
no rollback path · runs unattended overnight (the Debate-Harness "machine sleeps / job dies"
lesson, inverted: unattended *writes*) · no human gate on major-version bumps.

### L3 — Auto-file ClickUp intake into engagements
**Seeded risks (5):** misclassification routing client to wrong engagement · no idempotency →
duplicate tasks on retry · client-confidential data written to logs/description · no dead-letter
for unparseable intake · silent failure (Zapier "claims success, does nothing" pattern).

### L4 — Scheduled social posts from a content queue
**Seeded risks (5):** no approval before publish (irreversible/public) · no dedup → repost ·
injection from the queue source · brand/tone drift unreviewed · timezone/scheduling error.

### L5 — Operator agent runs shell commands from a task description
**Seeded risks (5):** arbitrary code execution from untrusted task text · no command allowlist ·
no sandbox/isolation · secrets/env exposure · no audit log or kill switch.

---

## Pass criteria (restated, frozen)

Fugu earns a named lane only if **all** hold across the 15 items:
1. It surfaces materially useful coverage/defects/risks that **both** Arm A and Arm C miss.
2. Net-positive on **accepted-output cost** (incl. review minutes), not just raw quality.
3. Outputs stay auditable and source-grounded (no fabrication-trap failures).
4. Data-handling posture acceptable for the class.

**Decision field** ([ClickUp task 86bamrnvm](https://app.clickup.com/t/86bamrnvm)) is set only
after `findings.md` is written: **Adopt** (named lane) / **Trial** (niche comparison, revisit) /
**Hold** (inconclusive, re-run larger) / **Drop**.

---

## What is deliberately NOT frozen here

- The literal code snippets for Class 2 (authored from the specs as the final freeze step;
  the *defect keys* above are what's frozen).
- Arm C's merge method (best-of-3 vs synthesis) — pick one and apply it uniformly before runs;
  log which.
- Sample expansion: if results are within noise at n=5, the plan allows a second tranche — but
  only after the first is scored and logged (no peeking-and-extending).
