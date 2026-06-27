# AI Loop Engineering for ProcessSmith and OpenClaw

**Prepared:** 2026-06-26  
**For:** ProcessSmith  
**Status:** Public-safe research brief  

---

## Executive Summary

AI loops are useful when a repeated task has a durable objective, a reliable verifier, remembered state, a bounded action surface, and an explicit stop condition. Without those elements, "keep going" behavior mostly converts uncertainty into hidden cost, drift, and review burden.

The strongest current pattern is not a broad autonomous assistant. It is a narrow loop contract: a recurring trigger, scoped actions, objective evidence, budget limits, and escalation when the agent cannot prove completion. Claude Code's `/goal` documentation makes this explicit by tying continued work to a measurable completion condition, proof surfaced in the transcript, and optional turn/time bounds. Anthropic's agent guidance makes the same tradeoff at the architecture level: agentic systems can improve task performance, but they trade latency and cost for that performance and should be used only when the added complexity is warranted.

For ProcessSmith and OpenClaw, the gap is not overall philosophy. The current operating model already has many of the right components: orchestrator and specialist separation, skills/playbooks, cron/heartbeat patterns, programmer/reviewer separation, execution profile discipline, verification evidence, and gated external action. The next step is packaging loops as explicit products and measuring them as business systems.

The recommended metric is:

```text
cost per accepted change =
  (agent/model/tool/runtime cost
   + CI/runtime cost
   + human review time
   + failed attempt cost)
  / accepted fixes, PRs, or artifacts
```

This keeps rejected work, review time, retries, and runtime overhead inside the ROI calculation instead of treating the agent's successful final answer as the whole cost.

---

## Loop Eligibility Gate

Do not promote a task into a loop unless all four checks pass.

| Gate | Question | Pass signal |
| --- | --- | --- |
| Recurrence | Does this repeat at least weekly? | Same trigger, same kind of work, recurring business value. |
| Verifier | Is there an automatic or objective verifier? | Tests, lint, checks, published artifact, reconciled ledger, empty queue, human approval state, or another auditable done signal. |
| End-to-end agency | Can the agent complete the work without open-ended product judgment? | The agent can gather inputs, act, verify, and produce evidence within bounded permissions. |
| Objective done state | Can a reviewer tell whether the loop finished? | Done is not "seems better"; it is a named state with evidence. |

If any gate fails, keep the work manual, one-shot, or human-led until one reliable manual run proves the pattern.

---

## Loop Contract Template

Every production loop should have a short contract before it is scheduled or given elevated permissions.

```yaml
name:
owner:
objective:
trigger_or_cadence:
input_sources:
allowed_actions:
disallowed_actions:
verifier:
evidence_artifact:
token_budget:
time_budget:
max_iterations:
stop_states:
  success:
  needs_human:
  budget_exhausted:
  unsafe_input:
escalation_path:
reviewer:
rollback_or_repair:
audit_log_location:
```

Contract quality matters more than contract length. A good loop contract lets a reviewer answer four questions quickly:

1. What is the loop trying to accomplish?
2. What can it touch?
3. How does it prove it is done?
4. When does it stop and ask for help?

---

## Cost Model

Loops should be priced and evaluated by accepted output, not raw task completions.

```text
cost per accepted change =
  (agent/model/tool/runtime cost
   + CI/runtime cost
   + human review time
   + failed attempt cost)
  / accepted fixes, PRs, or artifacts
```

### What to Include

- **Agent/model/tool/runtime cost:** model tokens, hosted runtime, browser sessions, search APIs, execution sandboxes, storage, queue workers, and logs.
- **CI/runtime cost:** test minutes, build minutes, staging environments, retries, and cleanup.
- **Human review time:** triage, prompt correction, diff review, source verification, client approval, merge decisions, and incident response.
- **Failed attempts:** abandoned runs, rejected PRs, bad artifacts, duplicate work, hallucinated citations, or changes that need full human rewrite.

### Useful Secondary Metrics

| Metric | Why it matters |
| --- | --- |
| Accepted output rate | Separates visible activity from useful work. |
| Human minutes per accepted output | Shows whether the loop reduces or shifts labor. |
| Retry count per accepted output | Catches brittle verifiers and unclear contracts. |
| Escalation rate | Reveals tasks that should stay human-led or need narrower scope. |
| Cost variance | Finds loops that sometimes spike due to bad inputs or missing stop states. |

---

## Current ProcessSmith/OpenClaw Comparison

| Loop engineering need | Current alignment | Gap |
| --- | --- | --- |
| Durable goal | Orchestrator/specialist tasks usually start from a concrete objective. | Goals are not always persisted as reusable loop contracts. |
| Verifier/gate | Programmer/reviewer separation, checks, diffs, and evidence summaries are already part of the process. | Verifier quality varies by task type, especially for research and client-facing artifacts. |
| State | Skills, playbooks, workspace docs, cron, and session history provide state. | Loop state is not yet consistently packaged as input/output artifacts. |
| Stop condition | Many tasks use explicit deliverables and approval gates. | Scheduled or recurring loops need formal budget and stop-state fields. |
| Bounded scope | Execution profiles and external-action gates already limit blast radius. | Tool permission surfaces should be reviewed per loop, not inherited from broad agent roles. |
| Acceptable retry cost | Manual specialist workflow makes retry cost visible. | Accepted-output metrics are not yet tracked across loops. |

The process already points in the right direction. The immediate opportunity is to turn recurring work into named, measurable loop products rather than relying on bespoke orchestration each time.

---

## Adoption Recommendations

1. **Start with one reliable manual run.** Do not schedule a loop until a human-led or agent-assisted run has produced the expected evidence artifact once.
2. **Package the loop contract before automation.** The contract should define the trigger, allowed actions, verifier, budgets, stop states, and escalation path.
3. **Prefer objective verifiers.** Tests, lint, link checks, published artifacts, reconciliations, and explicit reviewer approval are stronger than the agent judging its own work.
4. **Use specialist separation for risky loops.** Keep builder and reviewer roles separate for code, money, email, client work, and public publishing.
5. **Track accepted-output cost from day one.** Include review time and failed attempts in the denominator, or ROI will look better than it is.
6. **Keep broad chat interfaces as intake, not authority.** Telegram, email, and web content can start a task, but untrusted content should not directly grant permissions or change the loop contract.
7. **Make loops easy to retire.** A loop that needs frequent human rescue should be narrowed, downgraded to one-shot, or removed.

---

## Do Not Adopt

- Unbounded "keep going" loops without max iterations, time budgets, or stop states.
- Self-verification as the only gate for code, money, email, client deliverables, or public publishing.
- Broad chat agents with powerful permissions, weak audit trails, and unclear ownership.
- Scheduled loops before one reliable manual run.
- ROI claims that ignore rejected work, human review time, failed attempts, and runtime overhead.
- Loops over untrusted web, chat, or email content without prompt-injection controls and narrow allowed actions.

---

## Risks and Cautions

### Prompt Injection and Tool-Content Risk

Loops that consume web pages, email, support tickets, chat messages, or documents must treat that content as untrusted input. OWASP's GenAI Security Project highlights agentic app security, memory/context poisoning, data security, and red teaming as active concern areas for autonomous AI systems. This matters directly for loops because repeated execution can amplify one bad instruction.

### Vendor and Marketplace Claims

Vendor pages and app listings can be useful signals, but they are not neutral evidence. For example, the OpenRouter listing for Mira describes it as a Telegram-native AI assistant and reports usage/ranking metadata; that is useful for understanding the market category, not enough to validate a ProcessSmith production loop. Similarly, Telegram automation toolkits demonstrate integration feasibility, not business ROI.

### Cost Visibility

Agent loops can look cheap when only model tokens are counted. They become more expensive when review time, failed attempts, runtime maintenance, CI, queue failures, and incident response are included.

### Governance Drift

NIST's AI Risk Management Framework is intended to help organizations manage AI risks and incorporate trustworthiness considerations into AI system design, development, use, and evaluation. A loop contract is the practical ProcessSmith version of that: define the system, measure it, govern its permissions, and manage failures.

---

## Source Notes

The sources below were used for the public-safe synthesis. Private Telegram metadata, internal session identifiers, and non-public task details were intentionally excluded.

- Anthropic, ["Building effective agents"](https://www.anthropic.com/engineering/building-effective-agents). Used for the complexity/cost tradeoff and the workflow-versus-agent distinction.
- Claude Code docs, ["Keep Claude working toward a goal"](https://code.claude.com/docs/en/goal). Used for the completion-condition, verifier, and bounded goal pattern.
- Claude Code docs, ["Automate with hooks"](https://code.claude.com/docs/en/hooks). Used as a reference point for deterministic or model-evaluated automation hooks.
- Claude Code docs, ["Extend Claude with skills"](https://code.claude.com/docs/en/skills). Used as a reference point for packaging repeatable procedures.
- Claude Code docs, ["Create custom subagents"](https://code.claude.com/docs/en/sub-agents). Used as a reference point for role separation and specialized agents.
- OpenAI Codex docs, ["Codex cloud"](https://developers.openai.com/codex/cloud). Used as a reference point for scoped delegated coding tasks.
- OpenAI Codex docs, ["Codex code review in GitHub"](https://developers.openai.com/codex/integrations/github). Used for the reviewer/gated PR pattern.
- OpenAI Codex docs, ["Hooks"](https://developers.openai.com/codex/hooks). Used as a reference point for automation hooks around agent runs.
- OpenAI Codex docs, ["Subagents"](https://developers.openai.com/codex/subagents). Used for the parallel specialist-agent pattern and token-cost caution.
- MyClaw, ["Best AI Agent for Coding in 2026: Top Tools Compared"](https://myclaw.ai/blog/best-ai-agent-for-coding). Used for workflow-fit framing, persistent OpenClaw-style workflows, and real-cost considerations.
- OWASP GenAI Security Project, [home/resources](https://genai.owasp.org/). Used for security categories relevant to agentic systems.
- NIST, ["AI Risk Management Framework"](https://www.nist.gov/itl/ai-risk-management-framework). Used for governance framing.
- OpenRouter, ["Mira is the leading AI agent inside Telegram"](https://openrouter.ai/apps/mira). Used only as a vendor/marketplace signal about Telegram-native agents.
- Composio, ["Telegram MCP Integration with Mastra AI"](https://composio.dev/toolkits/telegram/framework/mastra-ai). Used only as an integration-feasibility signal for Telegram automation.
