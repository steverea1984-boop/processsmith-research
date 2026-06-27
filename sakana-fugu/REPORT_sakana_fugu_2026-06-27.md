# Sakana Fugu Research Brief for ProcessSmith and OpenClaw

**Prepared:** 2026-06-27  
**For:** ProcessSmith  
**Status:** Public-safe research brief  

---

## Executive Summary

Sakana Fugu is available now as a hosted model API. It is not an open-weight model to self-host. The useful framing is "multi-agent orchestration behind one model endpoint": ProcessSmith could call `fugu` or `fugu-ultra` through an OpenAI-compatible API while Sakana handles model routing, delegation, verification, and answer synthesis behind the scenes.

The practical answer is yes, we could use it, but only as a vendor-backed model provider in controlled experiments first. It is most interesting for difficult research, coding review, multi-step analysis, and resiliency against single-provider dependency. It is less compelling for cheap routine automation, privacy-sensitive client data, or workflows where we need to know exactly which underlying model handled the request.

Recommended next step: run a narrow evaluation with non-sensitive tasks that already have objective review signals, such as research briefs, code review comparison, and loop-contract evaluation. Do not route client-confidential data through Fugu until data-use, provider-pool, logging, and regional availability requirements are reviewed.

---

## What It Is

Sakana describes Fugu as a family of language models trained to orchestrate teams of frontier LLM workers. From the caller's perspective, it behaves like a model API. Internally, it can select workers, assign roles or instructions, coordinate intermediate work, and synthesize the final answer.

There are two product variants:

| Model | Intended use | Tradeoff |
| --- | --- | --- |
| `fugu` | Everyday coding, review, chat, research, and latency-sensitive work | Faster, lower-latency default; supports custom provider/model-pool opt-outs. |
| `fugu-ultra` | Hard, multi-step reasoning, research, code review, cybersecurity, paper reproduction, patent/literature work | Higher answer-quality target; slower; fixed full agent pool. |

The key product claim is not just benchmark performance. The more strategic claim is that learned orchestration becomes another scaling axis: instead of relying on one giant model, Fugu attempts to combine the strengths of multiple models and agent scaffolds behind a single API.

---

## Availability

Fugu appears commercially available as of Sakana's June 22, 2026 launch.

Current availability signals:

- Sakana's product page and console documentation expose `fugu` and `fugu-ultra` through the Sakana API.
- The API base is `https://api.sakana.ai`, with OpenAI-compatible `v1` endpoints.
- Sakana documents both Chat Completions and Responses API support.
- Subscription plans start at Standard, Pro, and Max tiers; pay-as-you-go is also described.
- Fugu Ultra pricing is listed as `fugu-ultra-20260615` at $5 per 1M input tokens, $30 per 1M output tokens, and $0.50 cached input, with higher rates for context above 272K tokens.
- Sakana says every plan includes both Fugu and Fugu Ultra.

Important restrictions and caveats:

- It is a hosted service, not a local deployment path.
- Sakana says it is not yet available in the EU/EEA while it works toward GDPR and EU-specific compliance.
- Access elsewhere can still depend on network conditions and local regulations.
- Underlying routing and exact model selection are proprietary and not exposed per query.
- Fugu can opt out of specific providers/models through a custom model pool; Fugu Ultra's pool is fixed.
- Usage data may be used to improve Fugu unless the customer opts out in the console.

---

## How We Could Use It

### 1. Codex Provider Experiment

Sakana publishes Codex setup instructions and a one-line installer:

```bash
curl -fsSL https://sakana.ai/fugu/install | bash
```

The documented manual provider block uses:

```toml
[model_providers.sakana]
name = "Sakana API"
base_url = "https://api.sakana.ai/v1"
env_key = "SAKANA_API_KEY"
wire_api = "responses"
stream_idle_timeout_ms = 7200000
stream_max_retries = 5
request_max_retries = 4
```

For ProcessSmith, the safer path is not to run the installer blindly inside the live operator environment. Instead, inspect the published repository or reproduce the minimal provider block in a test Codex profile with a scoped `SAKANA_API_KEY`.

### 2. Custom Workflow API Calls

The console docs show standard OpenAI SDK compatibility:

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://api.sakana.ai/v1",
    api_key="YOUR_API_KEY",
)

response = client.responses.create(
    model="fugu-ultra",
    input="Write a concise explanation of how TLS works",
    timeout=120.0,
)

print(response.output_text)
```

That means ProcessSmith could wire Fugu into evaluation harnesses, research pipelines, or coding-review experiments without changing the rest of the orchestration layer much.

### 3. Research and Review Backstop

Best near-term uses:

- Deep research synthesis where we can verify citations independently.
- Code review comparison against existing reviewer/Codex workflow.
- Complex workflow design critiques.
- Agent-loop contract evaluation.
- Literature, patent, vendor, and technical report reviews.

Poor first uses:

- Client data or confidential project files.
- Cheap recurring jobs where a smaller model already works.
- Workflows that require provider transparency per query.
- Anything that needs deterministic behavior or direct control over the internal agent plan.

---

## Fit for ProcessSmith and OpenClaw

| Need | Fit | Notes |
| --- | --- | --- |
| Research synthesis | Strong trial candidate | Use only with independent source verification. |
| Code review | Strong trial candidate | Compare against existing reviewer and Codex outputs on the same PRs. |
| Long-running coding tasks | Possible | Higher timeout and retry settings matter; still needs normal tests and review. |
| Client automation | Not yet | Needs privacy, terms, data-retention, and provider-pool review first. |
| Local/offline operations | Poor | Fugu is hosted; no self-host path identified. |
| Vendor resiliency | Interesting | It can reduce dependency on a single model provider, but creates dependency on Sakana's orchestrator and opaque routing. |
| Cost control | Mixed | Fugu avoids stacked multi-agent fees, but premium output-token pricing and review time still matter. |

The immediate value is evaluation, not wholesale replacement. Fugu is a candidate "hard task" provider behind the same ProcessSmith controls: bounded prompts, source capture, objective verification, separate review, and no unreviewed external actions.

---

## Recommended Evaluation Plan

1. Create a dedicated Sakana API key with the smallest practical plan or pay-as-you-go controls.
2. Disable training-data use in the Sakana console before testing anything beyond public examples.
3. Configure a separate Codex profile or API harness, not the default production agent path.
4. Run three comparison sets:
   - Research brief: same question, same source requirements, compare citation quality and synthesis.
   - Code review: same PR, compare findings, false positives, missed defects, and review time.
   - Loop contract critique: same automation proposal, compare risk identification and verifier design.
5. Track accepted-output cost, including model spend, runtime, retries, and human review minutes.
6. Decide whether Fugu deserves a named provider lane, such as "hard-research backstop" or "secondary code-review judge."

Pass criteria:

- It finds materially useful issues or synthesis that our existing stack misses.
- It does not add enough latency, cost, or verification burden to wipe out the benefit.
- Outputs remain auditable and source-grounded.
- The data-handling posture is acceptable for the task class.

---

## Risks and Open Questions

### Opaque Routing

Sakana explicitly says the specific underlying model selections and coordination details are proprietary and not exposed. That is acceptable for public research trials, but a problem for regulated, client-confidential, or provider-restricted work.

### Data Governance

Sakana says training-data use can be opted out in the console. Before using Fugu for anything sensitive, we need the actual current terms, retention policy, enterprise controls, and provider-pool behavior reviewed.

### Regional Availability

Sakana says it is not yet available in the EU/EEA while it works toward GDPR compliance. Steve and ProcessSmith are in Canada, so this does not appear to block local testing, but client work involving EU/EEA users or data needs caution.

### Benchmark Claims

The published benchmark numbers are Sakana-reported. Treat them as a reason to test, not proof of production superiority.

### Cost and Latency

Fugu Ultra is designed for harder tasks and may need longer client-side timeouts. It is not the right default for every task.

### Vendor Dependency

Fugu may reduce dependence on one model provider, but it introduces dependence on Sakana's orchestrator, billing, policies, availability, and undisclosed routing layer.

---

## Recommendation

Use Sakana Fugu as an experimental provider for hard research and review tasks, not as a default ProcessSmith runtime yet.

Initial policy:

- Allowed: public research, public-code review, synthetic tests, benchmark comparisons, non-sensitive workflow critique.
- Not allowed yet: client-confidential data, private business financials, personal data, external sends, production automation loops, or default-agent routing.
- Required: source verification, human review, cost tracking, and a separate scoped API key.

If Fugu consistently improves accepted output per review minute, promote it to a named optional provider lane. If it mainly produces longer answers without higher acceptance, keep it as a niche comparison model or drop it.

---

## Source Notes

Public sources used for this synthesis:

- Sakana AI, ["Sakana Fugu: One Model to Command Them All"](https://sakana.ai/fugu-release/), June 22, 2026. Used for launch framing, product claims, and the orchestration-model positioning.
- Sakana AI, ["Sakana Fugu - Multi-Agent System as a Model"](https://sakana.ai/fugu/), accessed 2026-06-27. Used for model variants, pricing, benchmark claims, opt-out behavior, regional restrictions, and FAQ caveats.
- Sakana AI Console, ["Get Started"](https://console.sakana.ai/get-started), accessed 2026-06-27. Used for API base URL, Chat Completions and Responses support, Codex setup path, model IDs, timeout notes, and provider configuration.
- Sakana AI et al., ["Sakana Fugu Technical Report"](https://arxiv.org/html/2606.21228v1), arXiv:2606.21228v1. Used for the technical framing of Fugu as learned orchestration over frontier LLM worker teams.
- MarkTechPost, ["Sakana AI Launches Sakana Fugu"](https://www.marktechpost.com/2026/06/22/sakana-ai-launches-sakana-fugu-an-orchestration-model-that-routes-tasks-across-a-swappable-pool-of-frontier-llms/), June 22, 2026. Used only as a secondary public summary and cautionary framing around proprietary routing.
