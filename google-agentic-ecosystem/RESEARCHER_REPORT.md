# Researcher Report: Google Agentic Ecosystem and "Model Eats the Harness"

Prepared: 2026-07-09 UTC / 2026-07-08 PDT  
Primary episode: Training Data, "Google DeepMind's Logan Kilpatrick: Why the Model Eats the Harness"  
Local transcript: `source/cMAs8z2dehs.transcript.md`

## Note on the Provisional `REPORT.md`

I agree with the provisional report's core conclusion: this episode is mostly about Google's agent substrate, not just Workspace assistants, and ProcessSmith should avoid differentiating on generic harness plumbing. I disagree with one important emphasis: Antigravity is no longer only a vague/internal direction in the public source trail. Google's current official docs describe Antigravity Agent, Managed Agents in the Gemini API, AI Studio Build mode, and Agent Platform hooks in concrete terms. The provisional report also underweights Workspace Studio and Gemini Enterprise as Google's business-user and IT-control planes.

Confidence: High.

## Executive Summary

Logan Kilpatrick's central claim is that "the model" is becoming a larger system than weights: it now includes tool calling, hosted tools, search, code execution, containers, file systems, browsing, and managed agent runtime. In the transcript he says the old token-in/token-out model frame has become an "expanding sprawling system" around the weights, and that scaffolding often moves into the native model/provider system over time (`source/cMAs8z2dehs.transcript.md:3780`, `:3801`, `:3840`, `:3855`, `:3861`, `:3870`, `:3888`). He expects today's agent harness alpha to move upstream within roughly 12 months (`:3930`, `:3942`, `:3951`, `:3960`).

Google's agentic strategy appears to have four layers:

1. **Model/tool layer:** Gemini API, Gemini 3, built-in tools, grounding, function calling, File Search, URL Context, Code Execution, and Managed Agents.
2. **Agent harness layer:** Antigravity Agent/Harness exposed through Antigravity, Gemini API, AI Studio, and Agent Platform.
3. **Business control layer:** Gemini Enterprise Agent Platform, Gemini Enterprise app, Agent Designer, Workspace Studio, governance, identity, auditing, A2A/MCP.
4. **End-user surfaces:** Search, Gemini app, Workspace apps, AI Studio Build mode, Gemini CLI/Code Assist/Jules, Android/app generation, data agents.

For ProcessSmith, the strategic lesson is not "copy Google's harness." It is: make messy business workflows structured enough for agents to operate safely; own approvals, evidence, audit trails, domain playbooks, and client-specific integration. The durable opportunity is in workflow architecture and trust, not in a generic agent loop.

Confidence: High.

## Topic-by-Topic Breakdown

### 1. Antigravity as Google's Shared Agent Harness

Transcript grounding: Kilpatrick says the "agentic Gemini era" is now becoming real and that the agentic layer is powered by the Antigravity agent harness (`:156-216`). He describes Antigravity as an ecosystem with a core IDE, web agent-first experience, CLI, SDK, and a Gemini API path for managed agents (`:279-333`). He also says the same harness is powering agent work in Search, the Gemini app, Cloud, and AI Studio (`:339-363`).

Separate research: Google's I/O developer highlights describe Antigravity SDK as programmatic access to the same agent harness powering Google's products and introduce Managed Agents in the Gemini API. The Antigravity Agent docs say a single API call gives a general-purpose managed agent that reasons, executes code, manages files, and browses inside a secure Linux sandbox, powered by Gemini 3.5 Flash and the same harness as the Antigravity IDE.

ProcessSmith implication: Treat Antigravity as Google's attempt to make agent runtime a platform primitive. ProcessSmith should use this kind of substrate when it helps, but its own product value should be workflow-specific controls, not a parallel generic harness.

Confidence: High.

Sources:
- https://blog.google/innovation-and-ai/technology/developers-tools/google-io-2026-developer-highlights/
- https://ai.google.dev/gemini-api/docs/antigravity-agent
- https://ai.google.dev/gemini-api/docs/agents
- https://ai.google.dev/gemini-api/docs/custom-agents

### 2. "The Model Eats the Harness"

Transcript grounding: Kilpatrick says the model is no longer just weights; it includes hosted tools, search, code execution, containers, and an agent harness (`:3780-3874`). He says scaffolding can be ahead of the model, then gets "eaten" and becomes part of the native model system (`:3876-3894`). He also argues that lock-in concerns may fade as models become better at using other harnesses and calls for something like a "harness bench" to measure model adaptability across harnesses (`:3972-4074`).

Separate research: Gemini API docs already show the trend: managed agents, built-in tools, Google Search grounding, URL Context, Code Execution, File Search, and function calling are provider-level features. Gemini 3 docs say built-in tools can be combined with function calling. The Antigravity Agent also supports custom functions and remote MCP servers.

ProcessSmith implication: Harness plumbing is a wasting asset unless it produces proprietary domain traces, client trust, or reusable workflow governance. Build provider-portable policy, permissions, review, and evidence layers, but avoid rebuilding native managed agents just for architectural purity.

Confidence: High for direction, Medium for the 12-month timing.

Sources:
- https://ai.google.dev/gemini-api/docs/tools
- https://ai.google.dev/gemini-api/docs/gemini-3
- https://ai.google.dev/gemini-api/docs/function-calling
- https://ai.google.dev/gemini-api/docs/google-search
- https://ai.google.dev/gemini-api/docs/file-search
- https://ai.google.dev/gemini-api/docs/antigravity-agent

### 3. Positive-Sum Usage and Outcome Metrics

Transcript grounding: The host asks whether agents will cannibalize Gmail/Search eyeball time (`:520-552`). Kilpatrick says AI has been positive-sum for Search: people search more and agents also search more (`:555-615`). He says product success should maximize outcomes for customers, not eyeballs (`:657-708`).

Separate research: Google Workspace and Gemini Enterprise positioning is consistent with this: AI is embedded in Gmail, Docs, Sheets, Meet, Drive, and Chat, while Workspace Studio automates flows and Gemini Enterprise puts agents in an employee-facing app.

ProcessSmith implication: Do not measure "agent activity" as the primary value. Measure completed work: fewer missed emails, faster quote turnaround, source-grounded answers, cleaner handoffs, shorter admin cycles, and auditable approvals.

Confidence: Medium. The claim is explicit in the episode, but usage metrics are not independently supplied.

Sources:
- https://workspace.google.com/solutions/ai/
- https://knowledge.workspace.google.com/admin/generative-ai/workspace-with-gemini/google-workspace-with-gemini
- https://workspace.google.com/studio/
- https://cloud.google.com/blog/products/ai-machine-learning/the-new-gemini-enterprise-one-platform-for-agent-development

### 4. Crawl/Walk/Run: Google Is Still Cautious in Billion-User Products

Transcript grounding: Kilpatrick rates most Google product agenticness as "crawl" because Google has stewardship responsibility for billion-user products and users still want to be in the driver's seat (`:813-915`). He says the Gemini app is closer to "walk" because a 24/7 always-on agent doing actions is a frontier use case; Antigravity is another advanced case with autonomous coding agents spending tokens and money on a user's behalf (`:918-980`).

Separate research: Workspace Studio's privacy and access-control language is consistent with this cautious rollout: customer data remains the customer's property, data is not used for advertising, Workspace access controls are respected, and DLP is not overridden. Gemini Enterprise docs emphasize governed sharing and registration of employee-made and custom agents.

ProcessSmith implication: SMBs will also need crawl/walk/run deployment. Start with draft-only and approval-gated workflows; move to autonomous execution only where risk, permissions, rollback, and logs are clear.

Confidence: High.

Sources:
- https://workspace.google.com/studio/
- https://docs.cloud.google.com/gemini/enterprise/docs/agents-overview
- https://cloud.google.com/blog/products/ai-machine-learning/whats-new-in-gemini-enterprise

### 5. Coding Agents as the First Robust Agent Category

Transcript grounding: The host says enterprises mostly see agents working in coding; Kilpatrick says it depends on the bar for "working," but coding is clearly strong and long-horizon agents matter (`:1173-1332`, `:1335-1389`). He says great coding models accelerate every other part of the business (`:1371-1383`). He later says coding feels like narrow superintelligence and increases human ambition/agency rather than simply replacing developers (`:2020-2199`).

Separate research: Gemini CLI is an open-source terminal agent using a ReAct loop with built-in tools and MCP servers. Gemini Code Assist agent mode exposes a subset of Gemini CLI in VS Code. Jules is Google's asynchronous coding agent that clones repositories in a cloud VM, develops a plan, verifies work, and integrates with GitHub/CLI workflows.

ProcessSmith implication: Copy the operating discipline of coding agents into business workflows: acceptance criteria, artifacts, tests/checks, diffs, logs, plan approval, and review gates. A contractor document or RFI workflow should behave more like a pull request than a loose chat.

Confidence: High.

Sources:
- https://developers.google.com/gemini-code-assist/docs/gemini-cli
- https://developers.google.com/gemini-code-assist/docs/use-agentic-chat-pair-programmer
- https://jules.google/
- https://blog.google/innovation-and-ai/models-and-research/google-labs/jules/
- https://developers.googleblog.com/en/meet-jules-tools-a-command-line-companion-for-googles-async-coding-agent/

### 6. Dogfooding and Feedback Flywheels

Transcript grounding: Kilpatrick says Google/DeepMind people should use competing models to understand the ecosystem, but also "definitely" need to use Gemini because the feedback flywheel from 100,000+ Google engineers should be a competitive advantage (`:1770-1872`). He cites teams building mobile apps and the Gemini Mac app unusually fast because of agentic coding (`:1950-1989`).

Separate research: Google's public product surfaces line up around this flywheel: Gemini CLI/Code Assist/Jules for developers, AI Studio Build mode for app creation, Antigravity managed agents for API/runtime, and Agent Platform for enterprise governance.

ProcessSmith implication: ProcessSmith should dogfood every workflow internally before selling it. Each pilot should generate durable traces: user request, plan, tools used, documents retrieved, human edits, approvals, failed actions, and output deltas. These traces become evals and sales proof.

Confidence: Medium-High. Internal scale claims are from the transcript; product surfaces are public.

Sources:
- https://ai.google.dev/gemini-api/docs/aistudio-build-mode
- https://developers.google.com/gemini-code-assist/docs/gemini-cli
- https://ai.google.dev/gemini-api/docs/antigravity-agent

### 7. AI Studio, Android Apps, and Personal Software

Transcript grounding: Kilpatrick says AI Studio's strategy is to expose builders to other parts of the Google ecosystem without sending them through many Google UIs (`:3483-3531`). He says AI Studio enabled people who would not otherwise build Android apps and cites 350,000 Android apps built since the prior week (`:3540-3649`). He frames personal software for personal problems as "very real" (`:3651-3678`).

Separate research: AI Studio Build mode generates Android Kotlin/Jetpack Compose projects, can preview them in a browser emulator, install to a device, and publish for testing. The Antigravity Agent manages multi-file project changes inside Build mode.

ProcessSmith implication: The market will not pay much for "we can make apps with AI." It will pay for small, connected internal tools that solve annoying business gaps and fit existing data/approval rhythms. Package "personal software for a business process," not generic app generation.

Confidence: Medium-High. The 350,000 figure is transcript-only; the AI Studio Build mode capabilities are documented.

Sources:
- https://ai.google.dev/gemini-api/docs/aistudio-build-mode
- https://ai.google.dev/

### 8. Workspace Studio, Gemini Enterprise, and Business Automation

Transcript grounding: The episode mentions agent work across Search, Gemini app, Cloud, and AI Studio (`:345-363`), plus the tension between many Google products and a unified AI/agent through-line (`:225-258`, `:3483-3529`). The business-user automation layer is not deeply discussed, but it is central to how Google's agent ecosystem reaches companies.

Separate research: Workspace Studio is a no-code Workspace automation product for flows/agents across Gmail, Docs, Drive, Chat, and third-party apps. Gemini Enterprise is positioned as an employee front door for AI, with no-code Agent Designer, partner agents, governed sharing, and a central inbox for long-running agents. Gemini Enterprise Agent Platform is the developer/IT layer for building, scaling, governing, and optimizing enterprise agents.

ProcessSmith implication: For Google-heavy clients, first evaluate whether Workspace Studio or Gemini Enterprise can cover the need. ProcessSmith's value is selecting, configuring, governing, and extending the right layer, plus building outside-Google workflow glue when Workspace/Enterprise are not enough.

Confidence: High.

Sources:
- https://workspace.google.com/studio/
- https://cloud.google.com/blog/products/ai-machine-learning/the-new-gemini-enterprise-one-platform-for-agent-development
- https://cloud.google.com/products/gemini-enterprise-agent-platform
- https://docs.cloud.google.com/gemini/enterprise/docs/agents-overview

### 9. ADK, A2A, MCP, and Interoperability

Transcript grounding: Kilpatrick says a generalized model should be able to use another harness, and the ecosystem needs benchmarks for adapting to different harnesses (`:3996-4056`). This maps to interoperability pressures in the agent ecosystem.

Separate research: ADK is Google's open-source framework for building, debugging, and deploying agents at enterprise scale. A2A is Google's agent-to-agent interoperability protocol, contributed to the Linux Foundation, for discovery, collaboration, and secure delegation between agents. Google positions MCP as the tool/data connection layer and A2A as an enterprise agent collaboration layer; Gemini Enterprise supports registering ADK and A2A agents.

ProcessSmith implication: Use MCP for tools and data access now. Watch A2A for multi-agent delegation across vendors. Use ADK selectively for Google-native builds, but keep ProcessSmith's workflow policy/evidence model independent of any single framework.

Confidence: High.

Sources:
- https://adk.dev/
- https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/adk
- https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/
- https://github.com/a2aproject/A2A
- https://cloud.google.com/blog/topics/developers-practitioners/building-connected-agents-with-mcp-and-a2a
- https://docs.cloud.google.com/gemini/enterprise/docs/agents-overview

### 10. Data Agents, File Search, and Grounded Business Knowledge

Transcript grounding: The episode's strongest business lesson is verifiability: Kilpatrick says domains with better verifiability, such as math, finance, and science, should improve fastest (`:2256-2289`). For business agents, retrieval and structured data checks are the analog.

Separate research: Gemini API File Search provides managed RAG over imported files. BigQuery data agents let users ask natural-language questions over selected BigQuery tables/views/UDFs with metadata and instructions. BigQuery Data Canvas lets users find, transform, query, and visualize data with natural language and a graphic interface.

ProcessSmith implication: Many SMB workflows need data cleanup before "agents" help. Start with source-linked document assistants, folder hygiene, named data sources, verified queries, and human-approved summaries before moving to action-taking.

Confidence: High.

Sources:
- https://ai.google.dev/gemini-api/docs/file-search
- https://docs.cloud.google.com/bigquery/docs/create-data-agents
- https://docs.cloud.google.com/bigquery/docs/data-canvas

### 11. World Models, Omni, and Media Generation

Transcript grounding: Kilpatrick says definitions of world models are blurring (`:2754-2784`). He says practical world-model uses still need scaffolding, especially for recurring use cases like games (`:2802-2880`). He describes Omni as a "single model" rather than routing across separate text/audio/music/image/video systems, initially strongest for video editing (`:2892-3171`). He frames a nuanced generated video example as evidence of world understanding (`:3189-3217`).

Separate research: The I/O developer highlights and Gemini docs support the broader pattern: Gemini is expanding multimodal and tool capabilities, while the media/model ecosystem includes Gemini, Veo, Imagen/Nano Banana, Lyria, and model/tool APIs. The specific "true Omni" claims are best treated as episode claims unless directly matched in public technical docs.

ProcessSmith implication: Media generation is not the main ProcessSmith lane. The transferable lesson is that even powerful "world understanding" needs product scaffolding and recurring-use workflow design. In business, the near-term "world model" value is richer understanding of documents, photos, videos, site conditions, and context.

Confidence: Medium.

Sources:
- https://blog.google/innovation-and-ai/technology/developers-tools/google-io-2026-developer-highlights/
- https://ai.google.dev/gemini-api/docs/gemini-3
- https://ai.google.dev/gemini-api/docs

### 12. Application Layer Survival and Startup Opportunity

Transcript grounding: When asked where independent companies survive if models eat the harness, Kilpatrick says both things are true: models do more, but there has never been more opportunity. He says verticalized domains with customer/ecosystem expertise can out-focus big labs, and coding helps startups close the gap with larger companies (`:4077-4294`).

Separate research: Google's own ecosystem reinforces this split: Google is absorbing horizontal substrate, while leaving many vertical workflows to builders via AI Studio, Antigravity SDK/API, ADK, Workspace Studio connectors, Agent Platform, and partner/custom agents.

ProcessSmith implication: The best ProcessSmith positioning is vertical workflow systems for contractor/SMB operations: not "AI agents," but quote-to-cash support, project document control, RFI/submittal assistance, meeting/action follow-through, sales/admin follow-up, and evidence-backed executive reporting.

Confidence: High.

Sources:
- https://ai.google.dev/gemini-api/docs/antigravity-agent
- https://workspace.google.com/studio/
- https://cloud.google.com/products/gemini-enterprise-agent-platform

## Google Ecosystem Map

| Layer | Google pieces | What they do | ProcessSmith read | Confidence |
|---|---|---|---|---|
| Foundation models | Gemini 3/3.5, Gemini API, Gemma | Multimodal models, open models, API access | Use best-fit model; stay provider-portable | High |
| Built-in tools | Google Search grounding, URL Context, Code Execution, File Search, Function Calling | Provider-managed access to web, files, code, APIs | Do not rebuild generic tools unless client policy requires it | High |
| Managed agent runtime | Antigravity Agent, Managed Agents, Interactions API | Hosted agent harness with Linux sandbox, files, tools, browsing, MCP/custom functions | Useful substrate for prototypes and production experiments | High |
| Developer surfaces | Antigravity IDE/CLI/SDK, Gemini CLI, Code Assist, Jules, AI Studio Build mode | Coding agents, app generation, async repo work | Strong internal ProcessSmith acceleration lane | High |
| Agent framework/protocols | ADK, A2A, MCP | Build agents, connect tools, coordinate agents | MCP now; ADK/A2A when Google-native or multi-agent needs justify it | High |
| Enterprise platform | Gemini Enterprise Agent Platform | Build, deploy, govern, optimize enterprise agents | Use for larger Google Cloud clients | High |
| Business user app | Gemini Enterprise app, Agent Designer, agent inbox | Employee-facing assistant and no-code/low-code agents | Good for governed employee workflows | High |
| Workspace automation | Workspace Studio, Gemini in Workspace | Native Gmail/Docs/Drive/Meet/Chat assistance and flows | Best first scan for Google Workspace SMBs | High |
| Data/analytics | BigQuery Data Canvas, BigQuery data agents | Natural-language analysis over business data | Valuable after data cleanup/schema work | High |
| Consumer/search surfaces | Search, Gemini app/Spark | Outcome-oriented consumer agents and search | Strategic signal: Google will own broad user entry points | Medium |
| Media/world models | Omni, Veo, Imagen/Nano Banana, Lyria | Multimodal creation and video/image/audio generation | Secondary for ProcessSmith; useful for richer context understanding | Medium |

## ProcessSmith Implications

1. **Do not sell "agent harness installation" as the durable product.** The model providers are absorbing more of that layer.
2. **Sell workflow control.** ProcessSmith should own intake, scoping, approvals, audit trail, source evidence, authority boundaries, and exception handling.
3. **Make business workflows code-like.** Use plans, diffs, checks, test cases, artifacts, and human review, especially for contractor workflows.
4. **Start with verifiable workflows.** Good early candidates: source-linked document Q&A, meeting/action extraction, estimate checklist QA, RFI/submittal draft support, weekly status reports, file package validation, CRM/email follow-up drafts.
5. **Use Google-native tools when the client lives in Google.** Workspace Studio and Gemini in Workspace may solve simple flows; Gemini Enterprise/Agent Platform may fit larger clients; Gemini API/Antigravity Agent may fit custom builds.
6. **Keep a ProcessSmith evidence layer outside the provider.** Store prompts, sources, plans, tool calls, human edits, approvals, and final artifacts in a client-readable audit trail.
7. **Dogfood aggressively.** Every internal ProcessSmith workflow should become an eval trace and reusable playbook.
8. **Design for crawl/walk/run.** Draft-only first, then approval-gated actions, then narrow autonomy only after measured reliability.

Confidence: High.

## Open Questions

- How much of "Antigravity powering Search/Gemini app/Cloud/AI Studio" is the exact same runtime versus shared design/code patterns?
- What are the security, pricing, and data retention details for Antigravity managed agents in production environments?
- How mature are Workspace Studio connectors for the contractor/SMB systems ProcessSmith cares about: Procore, Buildertrend, QuickBooks, HubSpot, Gmail, Drive, ClickUp, and local file stores?
- Does Gemini Enterprise make economic sense for SMB clients, or is it mainly a mid-market/enterprise play?
- How will A2A adoption compare with MCP in real-world SMB workflows?
- What benchmarks can ProcessSmith use for non-coding workflows analogous to SWE-bench: RFI accuracy, document retrieval precision, meeting action recall, estimate completeness, or follow-up latency?
- Which provider features should ProcessSmith standardize on now, and which should remain abstracted until the market settles?

## Source Index

Primary episode and transcript:
- Apple Podcasts episode: https://podcasts.apple.com/ca/podcast/google-deepminds-logan-kilpatrick-why-the-model-eats/id1750736528?i=1000772185230
- Sequoia transcript/page: https://sequoiacap.com/podcast/google-deepminds-logan-kilpatrick-why-the-model-eats-the-harness/
- YouTube source: https://www.youtube.com/watch?v=cMAs8z2dehs
- Local transcript: `external/processsmith-research/google-agentic-ecosystem/source/cMAs8z2dehs.transcript.md`

Google agent/model substrate:
- Google I/O 2026 developer highlights: https://blog.google/innovation-and-ai/technology/developers-tools/google-io-2026-developer-highlights/
- Gemini API docs: https://ai.google.dev/gemini-api/docs
- Antigravity Agent: https://ai.google.dev/gemini-api/docs/antigravity-agent
- Agents Overview: https://ai.google.dev/gemini-api/docs/agents
- Building Managed Agents: https://ai.google.dev/gemini-api/docs/custom-agents
- Gemini 3 developer guide: https://ai.google.dev/gemini-api/docs/gemini-3
- Tools: https://ai.google.dev/gemini-api/docs/tools
- Function calling: https://ai.google.dev/gemini-api/docs/function-calling
- Google Search grounding: https://ai.google.dev/gemini-api/docs/google-search
- File Search: https://ai.google.dev/gemini-api/docs/file-search
- AI Studio Build mode: https://ai.google.dev/gemini-api/docs/aistudio-build-mode

Google developer/coding agents:
- Gemini CLI: https://developers.google.com/gemini-code-assist/docs/gemini-cli
- Gemini Code Assist agent mode: https://developers.google.com/gemini-code-assist/docs/use-agentic-chat-pair-programmer
- Jules: https://jules.google/
- Jules public beta: https://blog.google/innovation-and-ai/models-and-research/google-labs/jules/
- Jules CLI companion: https://developers.googleblog.com/en/meet-jules-tools-a-command-line-companion-for-googles-async-coding-agent/

Enterprise/business ecosystem:
- Gemini Enterprise Agent Platform: https://cloud.google.com/products/gemini-enterprise-agent-platform
- Gemini Enterprise platform blog: https://cloud.google.com/blog/products/ai-machine-learning/the-new-gemini-enterprise-one-platform-for-agent-development
- Gemini Enterprise agents overview: https://docs.cloud.google.com/gemini/enterprise/docs/agents-overview
- Gemini Enterprise trust/governance blog: https://cloud.google.com/blog/products/ai-machine-learning/whats-new-in-gemini-enterprise
- Workspace AI: https://workspace.google.com/solutions/ai/
- Workspace Gemini admin overview: https://knowledge.workspace.google.com/admin/generative-ai/workspace-with-gemini/google-workspace-with-gemini
- Workspace Studio: https://workspace.google.com/studio/

Frameworks, protocols, data agents:
- ADK: https://adk.dev/
- ADK on Google Cloud: https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/adk
- A2A announcement: https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/
- A2A GitHub/Linux Foundation project: https://github.com/a2aproject/A2A
- MCP/A2A Google Cloud patterns: https://cloud.google.com/blog/topics/developers-practitioners/building-connected-agents-with-mcp-and-a2a
- BigQuery data agents: https://docs.cloud.google.com/bigquery/docs/create-data-agents
- BigQuery Data Canvas: https://docs.cloud.google.com/bigquery/docs/data-canvas

