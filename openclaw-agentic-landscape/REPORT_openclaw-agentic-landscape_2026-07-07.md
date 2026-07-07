# OpenClaw & Business Agentic Architectures: State of Play

**Date:** 2026-07-07
**Method:** Deep-research workflow (103 agents): 5 search angles, 21 sources fetched, 105 claims extracted, top 25 adversarially verified with 3 independent votes each. Result: 21 confirmed, 4 killed, 0 unverified.
**Evidence:** Full claim-level verification record (findings F1-F14 with votes and quotes, killed claims K1-K4, 21-source register with access dates, caveats, open questions) in [EVIDENCE_openclaw-agentic-landscape_2026-07-07.md](EVIDENCE_openclaw-agentic-landscape_2026-07-07.md). Section citations below reference those finding IDs.
**Status:** Baseline report. Intended to be re-run in lighter form on a recurring cadence (see "Next run" at the bottom).
**Scope:** (1) OpenClaw architecture, business vs. personal use, May-July 2026 releases, security posture. (2) Consensus business agent architectures as of mid-2026. (3) What this means for ProcessSmith's own systems (Jimmy, Max, client offers).

---

## Part 1: OpenClaw

### 1.1 How it works

OpenClaw is one self-hosted program, the **Gateway**, run on your own machine or server. Everything flows through it:

- **Channels** plug into the Gateway and connect it to chat apps: Telegram, WhatsApp, Slack, Discord, iMessage, Signal, Matrix, Google Chat, Teams, Feishu, Mattermost, and more. The chat app is the entire user interface.
- **The agent runtime** sits behind the Gateway. Messages are routed to agent sessions; the agent uses whichever AI model is configured and can use tools (files, shell, browser, APIs).
- **Skills** are add-on instruction packs. **Sandboxing** (Docker or a VM) is optional but strongly recommended.
- **Multi-agent:** one Gateway can host several agents with isolated workspaces, state directories, and session stores, routed by deterministic bindings (chat X goes to agent A, channel Y to agent B). Caveat: direct chats collapse to the agent's main session key by default, so true per-sender isolation needs explicit configuration.

Sources: https://docs.openclaw.ai/ and https://docs.openclaw.ai/concepts/multi-agent (accessed 2026-07-07). Verified 3-0 (evidence F1).

### 1.2 Personal vs. business use

Same software, different deployment posture. The distinction is now visible in the product itself:

| Dimension | Personal | Business / managed |
|---|---|---|
| Gateways | One | Multiple, or a routed fleet |
| Slack | Direct connection | **Slack Router Relay Mode** (v2026.6.11): a central router owns the Socket Mode connection and forwards mentions/threads to the right gateway |
| Cost control | One API key | **ClawRouter plugin** (July betas): model routing, credential-scoped discovery, per-budget usage reporting |
| Security | Defaults, low stakes | Layered defenses are the documented consensus requirement |

The project is visibly moving from hobbyist tool toward managed business fleets. That is the cutting edge as of July 2026.

### 1.3 Releases in the window (May-July 2026)

Near-weekly cadence; three releases in the first week of July alone.

- **v2026.6.8 (June 16, stable):** gateway auth hardening. Admin privileges required for HTTP session/model override endpoints; managed SecretRef auth for model credentials.
- **v2026.6.11 (June 30, stable):** delivery-reliability release. Fewer dropped, duplicated, or misrouted messages across Telegram, WhatsApp, Matrix, Google Chat, iMessage, Feishu, Mattermost. Slack Router Relay Mode. Control UI vulnerability patched (GHSA-cmwh-pvxp-8882, DOMPurify update). Package sourcing rejects lookalike sibling paths.
- **v2026.7.1-beta.1 / beta.2 (July 2 / July 5):**
  - GPT-5.6 model support; `openclaw attach` for external harnesses.
  - **ClawRouter** bundled provider plugin: model routing + budget reporting (PR #99658). Not the third-party BlockRunAI "ClawRouter" crypto project; same name, unrelated.
  - **Capability profiles:** groundwork for per-conversation tool/access boundaries (PR #98536). Wording is "prepare... boundaries": scaffolding, not finished enforcement.
  - Bounds checking on oversized/malformed provider responses; **Windows execution-path allowlisting** with case-insensitive path normalization.
  - Telegram: `/login` Codex pairing, `/steer` for active Codex runs. iMessage: native polls.

Beta-only as of 2026-07-07: ClawRouter, capability profiles, Telegram Codex features. Stable deployments (2026.6.11) do not have them.

Sources: https://docs.openclaw.ai/releases/2026.6.11 and https://github.com/openclaw/openclaw/releases (accessed 2026-07-07); ClawRouter: https://github.com/openclaw/clawrouter. Verified 3-0 (evidence F2-F6).

### 1.4 Security posture

1. **ClawJacked (CVE-2026-32025, CVSS 8.8, patched Feb 2026 in v2026.2.25).** Any malicious website could hijack a locally running agent with zero clicks: the gateway relaxed security for localhost, exempted loopback from rate limiting (brute-force at hundreds of guesses/second, unlogged), and auto-approved device pairing from localhost, yielding shell execution. Patched within 24 hours of Oasis Security's disclosure. Pre-window, but it defines the threat model current hardening responds to. (Primary: https://oasis.security/blog/openclaw-vulnerability; corroboration: Dark Reading, The Hacker News, SC Media. Verified 3-0, evidence F7.)
2. **ClawHub malicious skills.** Koi Security found 824+ malicious skills of ~10,700 by mid-February (up from 341 weeks earlier); Trend Micro documented 39 skills across ClawHub and SkillsMP distributing the Atomic macOS info stealer; Antiy Labs later counted 1,184 historically. Operational rule: treat third-party skills as untrusted code; install only vetted, pinned skills. (Koi Security ClawHavoc audit + Trend Micro AMOS report via https://www.darkreading.com/application-security/critical-openclaw-vulnerability-ai-agent-risks. Verified 3-0, evidence F8.)
3. **CVE volume.** ~543 CVEs tracked as of 2026-07-07; 75 published in May, 61 in June (down from peaks of 198 in March, 174 in April). ~92% (500/543) were assigned by third-party researchers via VulnCheck as CNA, not project-confirmed, so raw counts reflect an external research wave more than confirmed severity. Trend solid; exact numbers medium confidence, and a finer severity breakdown from the same source family was refuted in verification. (https://github.com/jgamblin/OpenClawCVEs/, accessed 2026-07-07, + independent snapshots. Evidence F9, killed claim K3.)
4. **Consensus posture** (Microsoft Security Blog, Backslash Security, OpenClaw's own security docs): built-in safeguards (auth, connection limits, tool controls, optional sandboxing) do not eliminate risk because the agent runs with broad access to files, credentials, and connected systems. Assume compromise is possible; limit blast radius: container/VM isolation, scoped credentials, loopback-only binding with token auth, rate limiting, minimum tool surface per agent. (Microsoft Security Blog, Backslash Security, https://docs.openclaw.ai/gateway/security. Verified 3-0, evidence F10.)

---

## Part 2: Business agentic architectures (consensus, mid-2026)

Google Cloud and Microsoft Azure architecture guidance (both updated May 2026) independently converge on the same ladder:

1. **Many jobs need no agent.** Predictable/structured work is better served by a deterministic workflow or a single model call. Google states this against its own commercial interest; Anthropic's "Building effective agents" says the same.
2. **Default to a single agent with tools.** Microsoft: "often the right default for enterprise use cases"; "use the lowest level of complexity that reliably meets your requirements." Multi-agent adds coordination overhead, latency, new failure modes, and multiplied model cost.
3. **Multi-agent only on demonstrated failure** of a single agent: prompt complexity, tool overload (behavior degrades as toolsets grow), or required security boundaries.

When multi-agent is justified, the named production patterns:

- **Sequential** (pipeline of specialists), **concurrent** (fan-out/fan-in), **group chat** (maker-checker, debate), **handoff** (triage routes to specialists), **magentic** (manager agent with a dynamic task ledger). Google's catalog adds hierarchical/coordinator, swarm, ReAct, human-in-the-loop.
- **Human-in-the-loop** approval is the standard safety valve for critical actions (payments, irreversible changes).
- **MCP (Model Context Protocol)** is named in Microsoft's guidance as the standardizing way agents discover and invoke tools. Build a tool connection once, any agent can use it.

Caveat: both docs target enterprises; applying them to small business is inference, but a safe one since SMB workloads sit at the simple end of the complexity spectrum.

Sources: https://docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system (last reviewed 2026-05-28) and https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns (updated 2026-05-12), both accessed 2026-07-07. Verified 3-0 (evidence F11-F14).

### The ProcessSmith client ladder

Cheapest and most reliable first:

1. Deterministic workflow, no AI.
2. Workflow with one AI step (classify, draft, extract).
3. One agent with a small scoped toolset (MCP where possible), human approval on anything irreversible.
4. Multi-agent, only with a demonstrated reason, using a named pattern.

This matches the official guidance and is defensible in client conversations: complexity is a cost to justify, not a selling point.

---

## Part 3: Applying this to ProcessSmith's own systems

### Jimmy (production OpenClaw on VM)

- **Version audit first.** Confirm Jimmy is on >= v2026.6.11 stable. The delivery-reliability fixes directly affect the ClickUp/Telegram handoff lanes; v2026.6.8's auth hardening (admin-only session/model override endpoints) matters for any exposed HTTP surface.
- **Verify ClawJacked-class posture even though patched:** gateway bound to loopback or private interface, token auth on, no public exposure without firewall + token.
- **Skill audit.** Inventory installed skills, remove anything unvetted, pin versions. ClawHub numbers justify a hard "no unvetted third-party skills" rule in the security framework.
- **Watch the betas, do not run them in production.** Capability profiles (per-conversation tool boundaries) map directly onto the 5-layer security framework's least-privilege layer; adopt when stable. ClawRouter budgets could give per-client cost tracking for the retainer offer; adopt when stable.

### Max (Dockerized OpenClaw in WSL2)

- Docker sandbox is the consensus-stronger posture; keep it. Finish the pending Telegram ID/allowlist step before widening access.
- Telegram `/steer` and `/login` Codex pairing (beta) are relevant to Max's operator role later; note for when they reach stable.

### Operating cadence

- Weekly releases + constant CVE flow means **patching is a recurring operations task, not setup**. A monthly (or biweekly) "OpenClaw patch & security review" pass covers: current stable version, release notes since last pass, new CVEs/GHSAs, skill inventory diff.
- The same pass is a productizable retainer line item for client deployments.

### Client positioning

- The vendor guidance is credibility ammunition: Google and Microsoft both say start simple. ProcessSmith's Audit -> Build -> Retainer ladder aligns with the official architecture ladder; proposals can cite it.

---

## Next run (recurring research template)

Lighter scope than this baseline. Suggested cadence: monthly. Check:

1. OpenClaw releases since last run (stable + beta): what went stable, especially **capability profiles**, **ClawRouter**, Telegram Codex features.
2. CVE/GHSA trend since last run (jgamblin tracker + GitHub advisories); any new critical disclosures.
3. ClawHub/skill-marketplace security developments.
4. Changes to Google/Microsoft/Anthropic agent-architecture guidance; MCP adoption milestones.
5. Anything new in managed/fleet OpenClaw deployment patterns (business-use edge).

Output: an `UPDATE_<date>.md` in this folder diffing against this baseline, plus edits here only if the baseline itself becomes wrong.

---

## Sources

Full source register with quality ratings, search angles, and access dates: [EVIDENCE_openclaw-agentic-landscape_2026-07-07.md](EVIDENCE_openclaw-agentic-landscape_2026-07-07.md), section 3. All sources accessed 2026-07-06/07.

Primary: https://docs.openclaw.ai/ (home, concepts/multi-agent, gateway/security, channels/slack, releases/2026.6.11), https://github.com/openclaw/openclaw/releases, https://github.com/openclaw/clawrouter, https://oasis.security/blog/openclaw-vulnerability, https://docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system, https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns.
Secondary: https://www.darkreading.com/application-security/critical-openclaw-vulnerability-ai-agent-risks (fetch 403'd; verified via excerpts + the primary researchers Oasis/Koi/Trend Micro), https://github.com/jgamblin/OpenClawCVEs/, https://releasebot.io/updates/openclaw, plus corroborating coverage listed in the evidence file.

## Caveats & limits

- Beta features (ClawRouter, capability profiles, Telegram Codex pairing) are not in any stable release as of 2026-07-07; capability profiles are scaffolding, not enforced boundaries (a stronger claim was killed in verification, K4).
- Precise OpenClaw counts (CVEs, channels, malicious skills) are dated snapshots; two count claims were killed (K1, K3).
- The small-business conclusion is inference from enterprise-oriented vendor guidance.
- No claims ranking named commercial platforms (n8n, Zapier, CrewAI, LangGraph, etc.) survived verification, so this report is strong on architecture patterns and deliberately silent on product comparisons. Flagged as the top open question for the next run.
