# OpenClaw Business Architecture for ProcessSmith

Status: Draft scaffold. Source collection and independent verification in progress.

## Executive Recommendation

TBD after source verification.

Working hypothesis: ProcessSmith should treat OpenClaw as the orchestration, identity, tool-governance, and runtime layer, while using enterprise model platforms and SDKs selectively for model access, evals, observability, policy integrations, and client-specific compliance needs.

## Why This Matters

Agentic business systems stop being low-risk once they can act across Slack/Teams, email, Drive, ClickUp, GitHub, accounting, CRM, project systems, or client data. The core question is not only which model is smartest. It is whose authority the system uses, how credentials are handled, what tools are exposed, what gets audited, and how humans can stop or approve risky actions.

## Architecture Options To Compare

1. OpenClaw-first runtime and gateway.
2. Enterprise-platform-first agent architecture.
3. SDK-first custom application architecture.
4. Hybrid OpenClaw plus enterprise model/platform services.

## Control Checklist

- Requester, actor, and persona are explicit.
- Long-lived credentials do not live inside agent runtimes.
- Tool access goes through controlled wrappers.
- Risky actions require confirmation or step-up approval.
- Identity, instructions, and approved skills are managed outside the model's control.
- Runtime isolation and network boundaries are enforced.
- Tool calls and outputs are audit logged with actor attribution.
- Model routing is governed by task sensitivity, quality needs, cost, and data policy.

## ProcessSmith Fit

TBD.

## Sources

- Damian F., "Building an Identity-Aware AI Teammate for Real Work Using OpenClaw", June 26, 2026. Local source: [source markdown](source/damien-f-openclaw-identity-aware-ai-teammate.md).

