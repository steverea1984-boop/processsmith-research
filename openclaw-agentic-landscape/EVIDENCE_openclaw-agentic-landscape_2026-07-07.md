# Evidence & Verification Record

Companion to `REPORT_openclaw-agentic-landscape_2026-07-07.md`.

**Method:** Deep-research workflow (103 agent calls). 5 search angles -> 21 sources fetched -> 105 candidate claims extracted -> top 25 claims adversarially verified, each by 3 independent verifier agents prompted to refute (a claim dies on 2/3 refute votes). Outcome: 21 confirmed, 4 refuted (killed), 0 unverified. Confirmed claims were then merged into 14 synthesized findings.
**All sources accessed:** 2026-07-06 to 2026-07-07.

---

## 1. Confirmed findings (14, merged from 21 confirmed claims)

| # | Finding (abridged) | Vote | Confidence | Sources |
|---|---|---|---|---|
| F1 | Single self-hosted Gateway bridges chat apps to agents; multi-agent routing with isolated per-agent workspace/state/sessions; channel layer spans 7+ platforms. Direct chats collapse to the agent's main session key by default. | 3-0 (merged claims 0, 1, 6) | High | docs.openclaw.ai/ ; docs.openclaw.ai/concepts/multi-agent ; docs.openclaw.ai/releases/2026.6.11 |
| F2 | Release cadence: stable v2026.6.11 on 2026-06-30; v2026.7.1-beta.1 on 2026-07-02; v2026.7.1-beta.2 on 2026-07-05. | 3-0 (merged 4, 19) | High | docs.openclaw.ai/releases/2026.6.11 ; github.com/openclaw/openclaw/releases ; releasebot.io/updates/openclaw |
| F3 | v2026.6.11 = delivery-reliability release (routing, reply attachment, duplicate prevention across Telegram/WhatsApp/Matrix/Google Chat/iMessage/Feishu/Mattermost) + Slack Router Relay Mode for managed multi-gateway fleets. | 3-0 (merged 5, 6) | High | docs.openclaw.ai/releases/2026.6.11 ; github.com/openclaw/openclaw/releases/tag/v2026.6.11 ; docs.openclaw.ai/channels/slack |
| F4 | July betas bundle the ClawRouter provider plugin: credential-scoped dynamic model discovery, OpenAI-compatible + native Anthropic/Gemini transports, managed budget reporting (PR #99658). Beta-only as of 2026-07-07. Distinct from the unrelated BlockRunAI "ClawRouter" crypto project. | 3-0 (claim 2) | High | github.com/openclaw/openclaw/releases ; github.com/openclaw/clawrouter |
| F5 | July betas: capability profiles that *prepare* per-conversation tool/access boundaries (PR #98536, scaffolding wording); bounds checking on oversized/malformed provider responses (PRs #96502, #96322, #96644, #97693); Windows execution-path allowlisting with case-insensitive normalization (PRs #98260, #98093, #97630). | 3-0 (claim 3) | High | github.com/openclaw/openclaw/releases |
| F6 | Channel features: Telegram /login Codex pairing + /steer for active runs (betas; /steer first in v2026.5.20); iMessage native polls (betas; PRs #98421, #92657, #92877); WhatsApp group-context reliability fixes (~v2026.6.11). | 3-0 (claim 20) | High | github.com/openclaw/openclaw/releases ; releasebot.io/updates/openclaw |
| F7 | ClawJacked (CVE-2026-32025, CVSS 8.8, disclosed late Feb 2026): malicious website could hijack a local agent zero-click via relaxed localhost trust + loopback rate-limit exemption (unlogged brute force) + auto-approved localhost device pairing -> shell execution. Patched in v2026.2.25 within 24h. Oasis blog says High/8.8; its press release and some outlets said Critical. | 3-0 (merged 13, 14) | High | oasis.security/blog/openclaw-vulnerability (primary discoverer) ; darkreading.com/application-security/critical-openclaw-vulnerability-ai-agent-risks |
| F8 | ClawHub malicious skills: Koi Security found 824+ of ~10,700 by mid-Feb 2026 (earlier baseline 341, correcting Dark Reading's "324"); Trend Micro: 39 skills across ClawHub + SkillsMP distributing Atomic macOS stealer; Antiy Labs: 1,184 historical. | 3-0 (claim 15) | High | darkreading.com article, corroborated by Koi Security ClawHavoc audit, Trend Micro AMOS report, The Hacker News, Unit 42, eSecurity Planet |
| F9 | CVE load: 543 tracked as of 2026-07-07; 75 in May, 61 in June (peaks: 198 Mar, 174 Apr). ~92% (500/543) assigned via VulnCheck as CNA, not project-confirmed. | 3-0 (merged 17, 18) | **Medium** (secondary aggregators; a related severity-breakdown claim was refuted, see K3) | github.com/jgamblin/OpenClawCVEs/ ; corroborated by flyingpenguin.com snapshot (376/413 via VulnCheck in May) and OpenCVE/days-since-openclaw-cve.com (~512 by June 12) |
| F10 | Security consensus: built-in safeguards insufficient because the agent has broad local access; layered defenses required (scoped credentials, sandboxing, rate limiting, monitoring, runtime isolation). Held independently by Microsoft Security Blog, Backslash Security, and OpenClaw's own security docs. | 3-0 (claim 16) | High | darkreading.com article ; docs.openclaw.ai/gateway/security ; Microsoft Security Blog "Running OpenClaw safely" |
| F11 | Google (reviewed 2026-05-28) and Microsoft (updated 2026-05-12) both say single agent with tools is the right default; multi-agent only when a single agent can't reliably handle the task (prompt complexity, tool overload, security boundaries). "Use the lowest level of complexity that reliably meets your requirements." | 3-0 (merged 7, 10) | High | docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system ; learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns |
| F12 | Google: predictable/structured workloads may not need agents at all; a plain workflow or single model call can be more cost effective. Convergent with Anthropic's "Building effective agents." | 3-0 (claim 8) | High | docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system |
| F13 | Pattern catalogs: Google lists coordinator (orchestrator/subagent), sequential, parallel, hierarchical, swarm, ReAct, human-in-the-loop; Microsoft defines five fundamental orchestration patterns: sequential (pipeline), concurrent (fan-out/fan-in), group chat (roundtable/maker-checker), handoff (routing/triage), magentic (dynamic task ledger). | 3-0 (merged 9, 11) | High | Same two vendor docs as F11 |
| F14 | Microsoft names MCP as the standardizing protocol for agent tool discovery/invocation ("protocols like Model Context Protocol standardize how agents discover and invoke tools"); tool overload is an explicit stated trigger for splitting one agent into several. | 3-0 (claim 12) | High | learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns |

## 2. Refuted (killed) claims (4)

These appeared in sources but died under adversarial verification. Recorded so future runs don't resurrect them.

| # | Killed claim | Vote | Source that carried it |
|---|---|---|---|
| K1 | OpenClaw natively supports "at least eleven" chat channels with Nostr and Twitch as plugins (specific count/tiering wrong as stated). | 0-3 | docs.openclaw.ai/ (misread of channel list) |
| K2 | A specific framing of the release train mapping (beta.1 July 2 / beta.2 July 5 details as stated in this phrasing did not fully survive re-verification; dates confirmed separately in F2). | 1-2 | github.com/openclaw/openclaw/releases |
| K3 | CVE severity breakdown "1 Critical, 90 High, 53 Medium, 13 Low (+106 awaiting)" at 543 total. Numbers did not check out; only the total and monthly trend survived (F9, downgraded to medium). | 0-3 | github.com/jgamblin/OpenClawCVEs/ |
| K4 | "Recent releases added per-conversation security boundaries: scoped capability profiles that limit which tools a conversation can use" — overstated. What shipped is *preparatory scaffolding* in betas (F5), not enforced boundaries. | 0-3 | releasebot.io/updates/openclaw |

## 3. Source register (21 fetched)

| URL | Quality | Search angle |
|---|---|---|
| https://docs.openclaw.ai/ | Primary | OpenClaw architecture & serious deployments |
| https://github.com/openclaw/openclaw/releases | Primary | OpenClaw architecture & serious deployments |
| https://docs.openclaw.ai/releases/2026.6.11 | Primary | OpenClaw recent updates & security posture |
| https://docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system | Primary | Production agent architecture patterns |
| https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns | Primary | Production agent architecture patterns |
| https://www.darkreading.com/application-security/critical-openclaw-vulnerability-ai-agent-risks | Secondary | OpenClaw recent updates & security posture (direct fetch 403'd; verified via search excerpts + primary researchers Oasis/Koi/Trend Micro) |
| https://github.com/jgamblin/OpenClawCVEs/ | Secondary | OpenClaw recent updates & security posture |
| https://releasebot.io/updates/openclaw | Secondary | OpenClaw recent updates & security posture |
| https://www.mintmcp.com/blog/openclaw-works-architecture-skills-security | Blog | OpenClaw architecture |
| https://vallettasoftware.com/blog/post/openclaw-security-2026-best-practices-risks-hardening-guide | Blog | OpenClaw architecture |
| https://nebius.com/blog/posts/openclaw-security | Blog | OpenClaw architecture |
| https://ppaolo.substack.com/p/openclaw-system-architecture-overview | Blog | OpenClaw architecture |
| https://www.penligent.ai/hackinglabs/openclaw-2026-2-23-brings-security-hardening-and-new-ai-features-but-the-real-story-is-the-security-boundary/ | Blog | OpenClaw updates & security |
| https://www.contextstudios.ai/guides/ai-agents-business-automation-2026 | Blog | Production agent patterns |
| https://www.augmentcode.com/guides/agentic-ai-architecture-patterns | Blog | Production agent patterns |
| https://www.aimagicx.com/blog/best-open-source-ai-agent-frameworks-2026 | Blog | Platform landscape & MCP |
| https://alicelabs.ai/en/insights/best-ai-agent-frameworks-2026 | Blog | Platform landscape & MCP |
| https://lushbinary.com/blog/latest-ai-trends-2026-agentic-mcp-small-models-guide/ | Blog | Platform landscape & MCP |
| https://umesh-malik.com/blog/autonomous-ai-agents-production-gap-2026 | Blog | Small-business automation |
| https://kaizenaiconsulting.com/ai-agents-small-business-2026-what-works/ | Blog | Small-business automation |
| https://machinelearningmastery.com/5-production-scaling-challenges-for-agentic-ai-in-2026/ | Blog | Small-business automation |

Supporting sources cited inside verification evidence (not fetched as full pages): oasis.security/blog/openclaw-vulnerability, github.com/openclaw/clawrouter, docs.openclaw.ai/concepts/multi-agent, docs.openclaw.ai/channels/slack, docs.openclaw.ai/gateway/security, Microsoft Security Blog, The Hacker News, SC Media, SecurityWeek, Security Affairs, Koi Security, Trend Micro, Unit 42, eSecurity Planet, flyingpenguin.com, OpenCVE.

## 4. Caveats (from synthesis)

- July beta features (ClawRouter, capability profiles, Telegram Codex pairing, iMessage polls) exist only in v2026.7.1-beta.1/beta.2 as of 2026-07-07; capability profiles are scaffolding, not enforcement (see K4).
- CVE and ClawHub counts are moving targets from secondary aggregators; treat every precise OpenClaw count as a dated snapshot (see K1, K3).
- The Dark Reading article was verified via search excerpts (direct fetch returned 403), but its key facts trace to the primary researchers (Oasis, Koi, Trend Micro).
- "Best for small business" is an inference from enterprise-oriented Google/Microsoft guidance; neither vendor addresses SMB explicitly.
- No claims about named commercial agent platforms (n8n, Zapier, CrewAI, LangGraph, etc.) survived verification, so the report is strong on architecture patterns and thin on product comparisons.

## 5. Open questions (for the next run)

1. Which commercial platforms actually lead small-business agent automation? (Unanswered; no platform-ranking claims survived verification.)
2. When do ClawRouter and capability profiles reach stable, and do capability profiles ship as enforced boundaries or stay scaffolding?
3. Has ClawHub added vetting/scanning/signing since the February malicious-skill wave?
4. For ProcessSmith specifically: is consolidating Jimmy and Max behind one Gateway safer or riskier than separate hosts, given the Gateway's localhost-trust history?
