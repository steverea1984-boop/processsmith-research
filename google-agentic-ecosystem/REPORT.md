# Google Agentic Ecosystem and "Model Eats the Harness" Research

Date: 2026-07-08
Status: PROVISIONAL

## Source

Primary episode:
- Apple Podcasts: "Google DeepMind's Logan Kilpatrick: Why the Model Eats the Harness", Training Data, Sequoia Capital, published June 11, 2026.
- Apple page: https://podcasts.apple.com/ca/podcast/google-deepminds-logan-kilpatrick-why-the-model-eats/id1750736528?i=1000772185230
- Matching YouTube video: https://www.youtube.com/watch?v=cMAs8z2dehs
- Local transcript from YouTube captions: `source/cMAs8z2dehs.transcript.md`
- Caption source file: `source/cMAs8z2dehs.en.vtt`

Note: This report supersedes the first provisional pass, which was based on the wrong local podcast transcript candidate.

## Executive Read

This episode is not mainly about Google Workspace assistants. It is about Google's agent strategy from the perspective of Logan Kilpatrick, who runs Google AI Studio and the Gemini API.

The central thesis is: **the model will eat the harness.** In other words, the scaffolding that developers currently build around models - tool loops, agent harnesses, search, code execution, containers, managed runtime, and workflow glue - tends to start outside the model, then move upstream into the model/provider system as capability improves.

That does not mean application builders are dead. It means the durable value moves away from generic harness plumbing and toward:

- workflow-specific product taste
- distribution and trust
- domain data and evaluation
- business process ownership
- safe human-control surfaces
- integration into real work

For ProcessSmith, this is a useful warning. Do not build the company around being "the agent harness installer." Build around business workflow architecture, implementation, governance, and vertical operating systems for contractors and small businesses.

## Episode Topic Map

### 1. Antigravity as Google's Agent Harness

Transcript claim:
- Google sees the "agentic Gemini era" as a new through-line across Google products.
- Antigravity is described as more than an IDE: it includes an IDE, web-first agent experience, CLI, SDK, and managed agent path through the Gemini API.
- The same harness is described as powering agent features across Search, the Gemini app, Cloud, and AI Studio.

Research:
- Google's public docs currently expose adjacent pieces rather than one simple "Antigravity" product page: Gemini CLI, Gemini Code Assist, Gemini API, ADK, Agent Platform, and Gemini Enterprise.
- Gemini CLI is documented as an open-source terminal agent using a ReAct loop with built-in tools and MCP servers.
- ADK is Google's open-source framework for building, debugging, evaluating, and deploying agents.

ProcessSmith read:
- Treat "Antigravity" as Google's internal/shared agent-harness direction, not yet as a clean product SKU.
- The strategic point is bigger than the name: Google wants one agent substrate to spread across coding, search, Gemini app, Cloud, and AI Studio.
- ProcessSmith should avoid overinvesting in generic agent infrastructure that a provider may absorb.

Sources:
- Transcript: `source/cMAs8z2dehs.transcript.md`
- https://developers.google.com/gemini-code-assist/docs/gemini-cli
- https://adk.dev/
- https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/adk
- https://ai.google.dev/gemini-api/docs/function-calling

Confidence: Medium-High. The transcript is explicit on the strategic claim; public product naming is still fragmented.

### 2. The Model Eats the Harness

Transcript claim:
- Kilpatrick argues that what people call "the model" is no longer just weights.
- Model products now include hosted tools, search, code execution, containers, tool calling, and agent harness behavior.
- Scaffolding often leads the model by a few steps, then gets absorbed into the native model/provider system.
- The current agent harness may stop being the alpha within roughly 12 months.

Research:
- Gemini API already includes function calling and Google Search grounding.
- Google's Agent Platform and ADK provide agent construction, runtime, and deployment pieces.
- OpenAI and Anthropic show the same broad industry direction: models ship with more built-in tools, code execution, browsing/search, computer use, and agent runtimes.

ProcessSmith read:
- Generic harness work is a wasting asset unless it creates learning, distribution, or a reusable client-control layer.
- Durable ProcessSmith value is not "we know how to wire tools to an LLM." It is "we know which work should be automated, which should be approved, how to prove what happened, and how to make it fit the business."
- Keep ProcessSmith architecture provider-portable, but do not rebuild provider features for ideology.

Sources:
- Transcript: `source/cMAs8z2dehs.transcript.md`
- https://ai.google.dev/gemini-api/docs/function-calling
- https://ai.google.dev/gemini-api/docs/google-search
- https://docs.cloud.google.com/gemini-enterprise-agent-platform

Confidence: High for the conceptual trend; Medium for the 12-month timing.

### 3. Agentic AI May Increase Usage, Not Just Cannibalize It

Transcript claim:
- The host asks whether agents reduce human time in products such as Gmail/Search.
- Kilpatrick argues Google has seen AI be positive-sum for Search: people search more, while agents also search more.
- He says Google's goal should be maximizing outcomes for users, not maximizing eyeball time.

Research:
- Google has publicly positioned Gemini and AI Mode as ways to help users ask more complex questions and take action, not just as a replacement for classic search.
- Gemini Enterprise similarly positions agents as ways to find information and complete work across business systems.

ProcessSmith read:
- The right business metric is not "chat volume" or "agent turns." It is completed useful work with evidence.
- For clients, sell outcome loops: fewer missed follow-ups, faster RFIs, cleaner handoffs, faster estimates, better document retrieval, fewer status meetings.

Sources:
- Transcript: `source/cMAs8z2dehs.transcript.md`
- https://cloud.google.com/gemini-enterprise
- https://workspace.google.com/solutions/ai/

Confidence: Medium. Google's claim is plausible and internally consistent, but exact usage metrics were not provided in the episode.

### 4. Coding Agents Are the First Working Agent Category

Transcript claim:
- Enterprises often say coding agents are the only agents they have really seen work.
- Kilpatrick partially agrees, depending on the definition of "work."
- He expects non-coding enterprise use cases to improve quickly.
- Long-horizon agents matter, and coding agents are especially important because better coding accelerates every other part of the business.

Research:
- Gemini CLI, Gemini Code Assist, Jules, Codex, Claude Code, Cursor, and similar tools show the coding-agent category is already operational.
- Coding works early because it has strong feedback loops: tests, compilers, diffs, logs, type checks, review, and deploy gates.

ProcessSmith read:
- Construction/business workflows need the same structure coding has: testable artifacts, acceptance criteria, logs, review gates, and rollback.
- The more a workflow can be made "code-like" - structured inputs, explicit outputs, checks, and approvals - the more agentic execution becomes practical.

Sources:
- Transcript: `source/cMAs8z2dehs.transcript.md`
- https://developers.google.com/gemini-code-assist/docs/gemini-cli
- https://developers.google.com/gemini-code-assist/docs/overview
- https://jules.google/

Confidence: High.

### 5. Dogfooding and Feedback Flywheels

Transcript claim:
- Kilpatrick says it is healthy for DeepMind/Google teams to use competing models to understand the ecosystem.
- He also says Gemini must be used internally because the feedback flywheel from 100k+ Google engineers should be a competitive advantage.
- He cites internal product teams using Antigravity to build mobile/Mac apps faster than normal.

Research:
- This maps to a broader platform pattern: the organizations with the most real internal usage get the best eval traces, bug reports, and product feedback.

ProcessSmith read:
- ProcessSmith should dogfood its own operator system on real internal work before packaging it for clients.
- Every pilot should generate reusable traces: prompt, tools used, human edits, approvals, rejected actions, artifact diffs, and failure modes.

Sources:
- Transcript: `source/cMAs8z2dehs.transcript.md`

Confidence: Medium-High. The dogfooding claim is direct from the episode; exact internal metrics are not independently verified.

### 6. Narrow and Jagged Superintelligence

Transcript claim:
- Coding may already feel like narrow superintelligence.
- Kilpatrick expects "jagged" vertical superintelligence before broad AGI.
- He names verifiable domains such as math, finance, and science as likely early winners.

Research:
- This aligns with the pattern that AI improves fastest where outputs can be checked: code tests, math proofs, scientific simulations, financial calculations, structured data validation.

ProcessSmith read:
- Pick early service lines where agent output is verifiable.
- Avoid fully autonomous judgment-heavy workflows early.
- Good ProcessSmith candidates: document retrieval with source links, meeting/action extraction, RFI/submittal draft generation, estimate checklist QA, recurring status summaries, file/package validation.

Sources:
- Transcript: `source/cMAs8z2dehs.transcript.md`

Confidence: Medium. The direction is credible; "superintelligence" framing is more opinion than measurable product claim.

### 7. World Models, Omni, and Generative Media

Transcript claim:
- Kilpatrick describes Omni as a single model for text, audio, music, image, and video-style outputs, rather than routing across many separate models.
- He frames Omni as world-model-like because it has richer world understanding, though not necessarily a traditional real-time action-conditioned video model.
- He says video/game generation still needs scaffolding: game engines, sprite generation, orchestration, reliability, and product taste.

Research:
- Google has separate public products for Gemini, Veo, Imagen, Lyria, Gemma, and other media/model capabilities, while the episode describes an internal direction toward a true omni model.
- The game-making discussion reinforces the "harness/scaffolding" thesis: even strong generative models need product systems around them.

ProcessSmith read:
- For ProcessSmith, media generation is secondary. The useful lesson is that powerful models still need business scaffolding.
- In business workflows, "world model" value may show up as richer document/site/video understanding, not just flashy content generation.

Sources:
- Transcript: `source/cMAs8z2dehs.transcript.md`
- https://ai.google.dev/gemini-api/docs/models
- https://ai.google.dev/gemma/docs

Confidence: Medium. The transcript is clear, but public Omni details may lag or differ from internal framing.

### 8. AI Studio and Personal Software

Transcript claim:
- The episode discusses AI Studio as a builder surface and references large numbers of Android apps/prototypes created through AI Studio.
- The broader implication is that personal software creation is becoming accessible: users can make one-off apps, games, tools, and automations.

Research:
- Google AI Studio and Gemini API are positioned as builder tools for developers and technically curious users.
- Firebase AI Logic extends Gemini into web/mobile apps.

ProcessSmith read:
- The market will not pay much for "we can make small apps with AI" by itself.
- Clients will pay for useful software connected to their work, data, approvals, and operating rhythm.
- ProcessSmith should package "personal software for businesses": small internal tools that solve annoying workflow gaps.

Sources:
- Transcript: `source/cMAs8z2dehs.transcript.md`
- https://ai.google.dev/
- https://firebase.google.com/products/firebase-ai-logic

Confidence: Medium.

## Google's Ecosystem, Separately

### Gemini App / Workspace Gemini

Role:
- User-facing assistant across Gmail, Docs, Sheets, Meet, Drive, and Gemini surfaces.

ProcessSmith fit:
- Good for Google Workspace clients that need everyday productivity assistance.
- Not enough by itself for custom workflow automation or client-specific operating surfaces.

Sources:
- https://workspace.google.com/solutions/ai/
- https://knowledge.workspace.google.com/admin/generative-ai/workspace-with-gemini/google-workspace-with-gemini

### Gemini Enterprise

Role:
- Employee-facing enterprise search, assistant, and agentic platform across company knowledge and connected systems.

ProcessSmith fit:
- Strong for larger clients already bought into Google Cloud/Workspace.
- Likely overkill for early SMB contractor pilots unless the client is already Google-heavy.

Sources:
- https://cloud.google.com/gemini-enterprise
- https://docs.cloud.google.com/gemini/enterprise/docs

### Gemini Enterprise Agent Platform / Vertex AI Successor Lane

Role:
- Build, deploy, scale, govern, and optimize production agents.

ProcessSmith fit:
- Use for serious production agent hosting where Google Cloud governance and runtime are worth the weight.
- Do not start here for every small-client pilot.

Sources:
- https://docs.cloud.google.com/gemini-enterprise-agent-platform
- https://cloud.google.com/products/gemini-enterprise-agent-platform
- https://cloud.google.com/blog/products/ai-machine-learning/introducing-gemini-enterprise-agent-platform

### ADK and A2A

Role:
- ADK: agent development framework.
- A2A: agent-to-agent interoperability protocol.
- MCP: tool/data/app integration layer.

ProcessSmith fit:
- ADK is worth watching or piloting for Google-native builds.
- A2A matters strategically if ProcessSmith coordinates multiple agents across providers.
- MCP remains the most immediate tool-connection standard.

Sources:
- https://adk.dev/
- https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/adk
- https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/
- https://developers.googleblog.com/developers-guide-to-ai-agent-protocols/

### Gemini API / AI Studio

Role:
- Model and builder layer: function calling, search grounding, file/search/code tools, Live API, app prototyping.

ProcessSmith fit:
- Best near-term Google path for custom ProcessSmith prototypes.
- Pair with ProcessSmith-owned workflow controls rather than relying on raw model behavior.

Sources:
- https://ai.google.dev/
- https://ai.google.dev/gemini-api/docs/function-calling
- https://ai.google.dev/gemini-api/docs/google-search
- https://ai.google.dev/gemini-api/docs/live-api

### Gemini CLI, Code Assist, and Jules

Role:
- Developer-agent layer for terminal, IDE, and async coding workflows.

ProcessSmith fit:
- Useful internally for implementation and prototyping.
- Client-facing use should remain behind repo, test, review, and deployment gates.

Sources:
- https://developers.google.com/gemini-code-assist/docs/gemini-cli
- https://developers.google.com/gemini-code-assist/docs/overview
- https://jules.google/

### Firebase AI Logic

Role:
- Gemini features embedded into web/mobile apps through Firebase.

ProcessSmith fit:
- Good for lightweight client apps and mobile/web prototypes.
- Less relevant for back-office agents unless the front-end app is the product.

Source:
- https://firebase.google.com/products/firebase-ai-logic

### BigQuery Data Agents / Data Canvas

Role:
- Natural-language and agentic analysis over structured business data.

ProcessSmith fit:
- Strong for analytics-heavy clients.
- Most contractors will need data cleanup and schema discipline before this pays off.

Sources:
- https://docs.cloud.google.com/bigquery/docs/data-canvas
- https://docs.cloud.google.com/bigquery/docs/create-data-agents

### Gemma / AI Edge

Role:
- Google's local/on-device/open-model lane.

ProcessSmith fit:
- Useful for privacy-sensitive, edge, or cost-constrained workflows.
- Not a replacement for governance.

Sources:
- https://ai.google.dev/gemma/docs
- https://developers.google.com/edge

## Architecture Recommendation for ProcessSmith

### Best Mental Model

Use Google as a managed substrate when it fits. Use ProcessSmith as the business workflow layer. Use OpenClaw/Open WebUI/local stacks as internal prototyping and flexible orchestration tools.

### What Not To Build

- Do not build a generic "agent harness" as the product.
- Do not compete with Google/OpenAI/Anthropic on raw model tooling.
- Do not sell agent autonomy without evidence, approvals, and clear authority boundaries.

### What To Build

1. Workflow-specific operator surfaces.
2. Client-safe approval and audit systems.
3. Source-grounded research/document workflows.
4. Vertical playbooks for contractors and SMBs.
5. Provider-portable tool wrappers and action policies.
6. Internal eval traces from every ProcessSmith workflow.

### Strong First Pilots

- Google Workspace workflow audit: map Drive/Gmail/Calendar/Docs pain points and identify agent candidates.
- Contractor document assistant: source-linked answers across controlled folders.
- Meeting/action extraction: transcript to task list, with human approval before sending.
- RFI/submittal draft assistant: draft-only, citation-backed, no autonomous send.
- Weekly project status generator: pulls from docs/tasks/calendar/email exports into an approval card.

## Bottom Line

The episode makes OpenClaw-style questions sharper, not weaker. If provider models are going to absorb more harness behavior, ProcessSmith should not differentiate on generic orchestration plumbing. It should differentiate on knowing which business workflows matter, making agent work visible and reviewable, and turning messy SMB operations into structured systems that agents can safely help with.

Most useful positioning line:

> The harness may get eaten. The workflow, trust layer, and business operating model are still ours to design.

## Source Index

Episode:
- https://podcasts.apple.com/ca/podcast/google-deepminds-logan-kilpatrick-why-the-model-eats/id1750736528?i=1000772185230
- https://sequoiacap.com/podcast/google-deepminds-logan-kilpatrick-why-the-model-eats-the-harness/
- https://www.youtube.com/watch?v=cMAs8z2dehs
- https://spoken.md/episode/google-deepminds-logan-kilpatrick-why-the-model-eats-1000772185230

Google:
- https://ai.google.dev/
- https://ai.google.dev/gemini-api/docs/function-calling
- https://ai.google.dev/gemini-api/docs/google-search
- https://ai.google.dev/gemini-api/docs/live-api
- https://adk.dev/
- https://docs.cloud.google.com/gemini-enterprise-agent-platform
- https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/adk
- https://cloud.google.com/gemini-enterprise
- https://cloud.google.com/products/gemini-enterprise-agent-platform
- https://workspace.google.com/solutions/ai/
- https://developers.google.com/gemini-code-assist/docs/gemini-cli
- https://developers.google.com/gemini-code-assist/docs/overview
- https://jules.google/
- https://firebase.google.com/products/firebase-ai-logic
- https://docs.cloud.google.com/bigquery/docs/data-canvas
- https://docs.cloud.google.com/bigquery/docs/create-data-agents
- https://ai.google.dev/gemma/docs
- https://developers.google.com/edge

