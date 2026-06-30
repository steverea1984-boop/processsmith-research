# Research Brief: OpenClaw Business Architecture

## Purpose

Steve wants to understand whether OpenClaw can be the foundation for safe, practical business AI systems, or whether ProcessSmith should rely more heavily on enterprise model platforms, managed agent services, or SDK-first implementations.

The attached Damian F. article is the seed source because it describes a mature internal deployment pattern: Slack-first assistant, OpenClaw gateways, isolated runtimes, web control plane, short-lived credentials, model routing, controlled tool wrappers, and auditability.

## Primary Question

What is the best and safest architecture for ProcessSmith to build business-facing AI agent systems: OpenClaw-first, enterprise-platform-first, SDK-first, or a hybrid of these?

## Comparison Axes

- Identity model: requester, actor, persona, delegated user auth, bot auth, fallback modes.
- Credential handling: OAuth vaults, short-lived tokens, service accounts, workload identity, static secret avoidance.
- Runtime safety: isolated pods, gVisor/container sandboxing, network policy, read-only mounts, controlled tool wrappers.
- Governance: skill review, department-aware capability exposure, human confirmation, approval gates.
- Auditability: session logs, tool invocation records, actor attribution, SIEM/export readiness.
- Model strategy: managed models, self-hosted models, local inference, routing by cost/risk/task.
- Developer surface: OpenClaw skills/tools/sessions versus provider SDKs and managed agent frameworks.
- Client fit: what can be offered to small and mid-size businesses without excessive platform burden.

## Seed Source Claims To Verify

- OpenClaw is useful as a gateway/runtime layer because it centralizes routing, tools, sessions, isolation, and model selection.
- Business agents need explicit identity architecture; prompt-only guardrails are insufficient.
- Long-lived credentials should stay outside agent runtimes.
- Tool use should happen through constrained wrappers, not broad CLIs or raw APIs.
- Shared personas require stricter actor policy than personal agents.
- Read-only identity/instruction/skill mounts reduce self-modification risk.
- GKE, Istio, mTLS, SPIFFE, gVisor, Kubernetes NetworkPolicies, and Workload Identity can form a strong enterprise deployment substrate.
- A hybrid model strategy can combine managed platforms such as Vertex AI with self-hosted or smaller local models.

## Expected Output

The final report should include:

- An architecture recommendation for ProcessSmith.
- A risk-ranked control checklist.
- A build/buy/hybrid comparison.
- A small-business-friendly MVP architecture.
- An enterprise-grade target architecture.
- Open questions and security review items.

