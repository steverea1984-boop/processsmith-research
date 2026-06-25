# Researcher Agent — Best-Practice Setup vs. Our Current Setup
**Prepared:** 2026-06-21 · **For:** ProcessSmith
**Research engine:** Perplexity Sonar (`sonar-reasoning-pro`, two passes) via the newly-added `research.mjs` skill path
**Sources:** 20+ cited 2026 references (full list in the appendix files)

---

## 0. TL;DR

Our researcher agent is **already strong on doctrine** — it has the three-mode separation, output contracts, and citation discipline that 2026 best-practice guides recommend. The gaps are in **enforcement and tooling**, not philosophy:

1. **(DONE today)** Perplexity was only wired to the raw `/search` snippet API. I added a proper `research.mjs` that calls the **Sonar answer models** (`sonar-pro`, `sonar-reasoning-pro`, `sonar-deep-research`) with citations + recency filtering — the actual "research" capability.
2. **(DONE today)** Fixed a silent secret-sync gap (the live key the agent reads was stale) and added `sync_secret.sh`.
3. **Biggest open gap:** our modes and citation rules are **prompt contracts the model is asked to follow**, not **enforced** state transitions / automated checks. The best-practice guidance is explicit: enforce, don't request.

---

## 1. What "best setup" looks like in 2026 (from the research)

The research converged on treating a researcher agent as a **software system**, not a prompt chain:

- **Architecture:** a stateful graph of roles (Planner → Researcher → Analyst → Fact-checker → Editor) with deterministic state transitions (LangGraph-style), strict tool contracts, budgets, and continuous evals.
- **Model strategy:** one strong frontier generalist as the "brain" for planning/synthesis/final drafting; an optional reasoning-specialized model used **only as an internal planner/critic**; cheap small models for routing/summarization. Start with one model, split only when profiling justifies it.
- **Retrieval, layered by purpose:**
  - Web search APIs → breadth & freshness
  - **Perplexity Sonar deep-research → high-recall multi-hop synthesis** (use early for hypotheses/sources, and late as a contradiction sanity-check — *never as the final oracle*)
  - Agentic browsing (Playwright/Puppeteer) → deep reading of specific pages/PDFs, returning **structured text chunks**, treating page content as untrusted
- **Modes as distinct graph branches** (not prompt flags): fast-critique (minimal/no search), deep-research (full pipeline, 20–40 calls), fact-check (per-claim verdicts with structured JSON).
- **Source discipline via data structures:** an explicit `sources[]` model with stable IDs; the model may only **reference existing IDs, never invent URLs**; ≥2 independent sources for important claims; surface disagreements explicitly.
- **Memory ≠ vector DB:** layered memory (working / summaries / artifacts / long-term prefs) + RAG over your own corpus + optional knowledge graph for entities/relationships.
- **Output + QA:** enforce a JSON schema (auto-repair invalid output); a Reviewer pass; a **Fact-Checker agent** that re-queries and a **programmatic citation check** (verify each quote is substring-present in the cited source chunk); trajectory evals + tracing + cost/step metrics.
- **Failure modes & guardrails:** frozen "mission object" + scope-watchdog (scope drift); retrieval-tool-issued IDs + reject unmatched citations (hallucinated citations); strict step budgets + reflection checkpoints (tool loops); treat all tool content as data-only (prompt injection).

---

## 2. What we have today (OpenClaw researcher)

Source: `docs/agents/RESEARCHER.md`, `docs/agent-audits/RESEARCHER_CAPABILITY_AUDIT.md`, the `perplexity` skill.

| Capability | Current state |
|---|---|
| **Operating modes** | ✅ Three documented modes — Council/Critique, Research, Verification — with per-mode allowed/forbidden tools and stop conditions |
| **Output contract** | ✅ Strong: Key Finding / Evidence / Confidence / Action; confidence labels required |
| **Citation discipline** | ✅ Strong doctrine: no tool-name citations, normalize discovery tools to primary sources; partial automated lint (`lint_research_bundle.py`, `research_bundle_qc.py` reject "Perplexity snippet" etc.) |
| **Search/retrieval** | ⚠️ `aisa-tavily`, `perplexity`, `agent-browser`, `web_fetch`, `youtube-watcher`. **Perplexity was snippet-search only** until today |
| **Memory/RAG/KG** | ✅ `memory_search` + `ontology` (knowledge graph) + `MEMORY.md`; layered-ish |
| **Model "brain"** | ⚠️ Researcher runs **on Perplexity (Sonar) as its model**, rather than a frontier generalist orchestrating Sonar as a tool |
| **Mode enforcement** | ❌ Modes are prompt contracts, not enforced transitions. The capability audit itself flagged "too few enforced mode contracts" |
| **Citation verification** | ❌ No programmatic quote→source substring check |
| **Tool-loop / step budgets** | ❌ Not enforced; audit lists "tool loops" and "scope drift" as observed pain points |
| **Evals / tracing / metrics** | ❌ Not present |
| **Prompt-injection guardrail** | ⚠️ Implicit; no explicit "tool content is untrusted data" rule for `agent-browser` |

---

## 3. Gap analysis

**Where we already match best practice:** mode separation, output contract, citation doctrine, layered memory + knowledge graph, peer-review/fact-check *as doctrine*. This is genuinely ahead of most setups — the audit's instinct ("the problem isn't too many tools, it's too few enforced contracts") matches the research exactly.

**Where we fall short — all about enforcement & tooling:**
1. Perplexity was retrieval-only (snippets), not synthesis — **closed today**.
2. Modes/citations are *requested*, not *enforced*.
3. No automated citation-verification or step budgets, despite both being named pain points.
4. The reasoning "brain" is the search model itself, blurring the research best-practice of "frontier brain + Sonar as a tool, never the final oracle."
5. No evals/observability loop to catch regressions.

---

## 4. Recommendations (prioritized — my recommendations)

### Done today
- **R0a — Sonar answer models.** Added `skills/perplexity/scripts/research.mjs`: `sonar-pro` (default), `sonar-reasoning-pro` (analysis), `sonar-deep-research` (exhaustive), with citations, `--recency`, and `--max-tokens`. Verified working on the new key.
- **R0b — Secret-sync fix.** The live agent reads `gateway.systemd.env`, which held a **stale** Perplexity key; synced it + restarted the gateway. Added `team/scripts/sync_secret.sh` to push any secret to `.env` + `gateway.systemd.env` + Supabase in one no-echo step.

### P1 — high value, low effort
- **R1 — Use the new models in doctrine.** Update `RESEARCHER.md`: Research Mode should call `research.mjs` (`sonar-deep-research` for deep dives, `sonar-pro` for fast grounded answers), and keep `search.mjs` only for raw link discovery. Keep the "never cite the tool; never treat Sonar as the final oracle" rule.
- **R2 — Programmatic citation verification.** Extend `lint_research_bundle.py` into a checker that, for each claim, confirms the quoted text is substring-present in the cited source chunk; fail the bundle on mismatch. This directly kills hallucinated/misattributed citations.
- **R3 — Step & cost budgets + reflection checkpoint.** Cap tool calls per task by mode (e.g., critique ≤3, research ≤40); every K steps ask "is the mission satisfied?"; force a coherent partial answer at the limit. Targets the audited "tool loops."

### P2 — higher effort, strong payoff
- **R4 — Enforce modes as routing, not prose.** A lightweight classifier (or explicit `mode=` parameter) selects a mode and **hard-restricts the toolset** for that mode, instead of relying on the model to self-police.
- **R5 — Frozen mission object + scope-watchdog.** Pass a structured brief (goal / in-scope / out-of-scope / success criteria) on every step; refuse actions outside scope. Targets the audited "scope drift."
- **R6 — Separate the reasoning brain from the search tool.** Let a frontier generalist orchestrate; call Sonar as a typed tool. Reduces "search model is also the judge" risk.
- **R7 — Structured JSON output + auto-repair**, rendered into the human report template (exec summary / evidence table / next actions).
- **R8 — Explicit prompt-injection guardrail** for `agent-browser`/`web_fetch`: wrap fetched content as UNTRUSTED data, never instructions.
- **R9 — Evals + tracing.** Small eval set ("no claim without evidence," max step count, ≥2 sources for high confidence) + per-task metrics (sources/claim, fact-check disagreement rate, tool-calls, token cost).

---

## 5. Suggested sequencing
1. **This week:** R1 (wire new models into doctrine), R2 (citation checker). Both build on assets we already have.
2. **Next:** R3 budgets, R5 mission object — directly close the two audited pain points (tool loops, scope drift).
3. **Then:** R4 enforced routing, R6 brain/tool split, R9 evals — the structural upgrades.

---

## Appendix — artifacts
- `research/researcher-agent-best-setup/reasoning_pro.md` — full Sonar pass 1 (architecture, models, retrieval, modes, sources, memory)
- `research/researcher-agent-best-setup/reasoning_pro_part2.md` — full Sonar pass 2 (output/QA schema, failure modes & guardrails table)
- `research/researcher-agent-best-setup/perplexity_deep_research_raw.md` — `sonar-deep-research` source list

*Note on method: `sonar-deep-research` returned a strong source set but an empty synthesized body on this run (a known long-response flakiness); `sonar-reasoning-pro` was used for the synthesis in two passes. All model knowledge of specific frontier model names is as of early 2026.*
