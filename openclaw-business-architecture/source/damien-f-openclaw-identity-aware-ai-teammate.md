0 notifications total

Skip to searchSkip to main content

Keyboard shortcutsClose jump menu

![](openclaw-business-architecture/source/media/image1.wmf)

- 

new feed updates notifications

Home

- 

**1**1 new network update notification

My Network

- 

Jobs

- 

Messaging

- 

**25**25 new notifications

Notifications

- <img src="openclaw-business-architecture/source/media/image2.jpeg" style="width:0.25in;height:0.25in" alt="Steven Rea" />Me

- For Business

- [Reactivate Premium](javascript:void(0))

<img src="openclaw-business-architecture/source/media/image3.jpeg" style="width:7.625in;height:4.29167in" alt="https://media.licdn.com/dms/image/v2/D5612AQHjag-CPTt_RA/article-cover_image-shrink_720_1280/B56Z8FTjJ9KgAQ-/0/1782500439048?e=1784160000&amp;v=beta&amp;t=6RztWXM2v7GAndNlsWFIMsGd9hWlJb44COrDl8JAfUA" />

**Building an Identity-Aware AI Teammate for Real Work Using OpenClaw**

[<img src="openclaw-business-architecture/source/media/image4.jpeg" style="width:1.04167in;height:1.04167in" alt="Damian F." />](https://www.linkedin.com/in/damianfinol/)

[**<u>Damian F.</u>**](https://www.linkedin.com/in/damianfinol/)

VP of Engineering \| Scaling DevOps, SecOps, AI (Agents & claws), IT & QA Teams \| Kubernetes/GKE, Terraform & GCP Leader \| AI, MLOps & Fintech Infrastructure.

June 26, 2026

Work inside a modern company rarely lives in one place.

A single engineering or operations task might start in Slack, require context from GitHub, touch a Google Doc, reference a ClickUp ticket, pull details from Notion, check PagerDuty, inspect New Relic, and eventually trigger something inside an internal system.

That is annoying when humans are doing the work manually. It becomes a security problem when an AI system is allowed to help.

At Felix Pago, we built an internal AI work bot to solve this problem. Internally, we call it **Maestro**. It started as a Slack-first teammate: something you could ask for help in a DM, a project channel, or an incident room. Over time, the same architecture has started to power other internal surfaces too, including employee profile assistants that help people understand who owns what, where work lives, and how to route requests.

Under the hood, Maestro is built on **OpenClaw**, the agent gateway and runtime layer that gives us a consistent way to run agents across the company. OpenClaw handles the parts we did not want to reinvent for every workflow: routing requests, isolating agent runtimes, exposing tools, managing sessions, and choosing model backends.

That last piece matters more than it might sound. Not every agent needs the same model. Some workflows justify a managed model through **Google Vertex AI**. Others are better served by smaller models or self-hosted instances on our own GPU machines. OpenClaw lets us make that a runtime decision instead of a one-way door. The result is better cost control without turning model choice into a separate architecture problem.

Still, the important part is not that Maestro can chat. The important part is that it is designed as a secure, identity-aware runtime for delegated work. Once an assistant can do more than answer questions, it needs real architecture around permissions, auditability, and human control.

**Why a Chatbot Is Not Enough**

A simple chatbot can summarize a thread, draft a response, or explain a document. That is useful, and usually low risk.

The risk changes when the bot can act.

Once an AI system can open a pull request, update a ticket, page someone, query production telemetry, comment in a customer workflow, or trigger an internal tool, the architecture has to answer harder questions:

- Who asked the agent to do this?

- Whose credentials should be used?

- Which permissions apply?

- What system actually performed the action?

- Can we audit it later?

- Should the action require confirmation?

- What happens if the agent is running in a shared channel?

For an internal AI agent, these questions are core product requirements. Prompt design alone is not enough. Secure AI tool use is systems design.

**A Slack-First Teammate With a Control Plane**

We wanted Maestro to live where work already happens, which for us means Slack. People should be able to ask for help in direct messages, project channels, team channels, and incident channels without switching context.

Slack is only one surface, though. Behind it is a web control plane we built where users and administrators manage agents, personas, OAuth connections, permissions, and policy. The control plane exists because Maestro is not only answering questions. It is making decisions about when software is allowed to act, which identity it should use, and what needs to be recorded afterward.

The same web surface is also becoming our agentic intranet. One example is an employee profile assistant: a small assistant on an intranet employee profile page that answers from context the profile owner chose to publish. It can explain what someone works on, where their OKRs live, what they can help with, and how best to reach them. It represents their published work context, not their private authority.

The pieces are deliberately boring:

- A familiar Slack interface.

- A web control plane for configuration, governance, and operations.

- OpenClaw gateways with isolated agent runtimes.

- Model routing across Google Vertex AI and self-hosted GPU-backed models.

- Branded agent identity, instructions, and skills managed by the control plane.

- Controlled tool wrappers around external CLIs and APIs.

- Short-lived credentials for tool calls.

- Workload identity, mTLS, and audit logs.

**High-Level Architecture**

The architecture is easier to explain by function than by internal service name.

A **Slack ingress service** receives Slack events, verifies them, understands where the request came from, and routes the work to the right agent.

An **OpenClaw agent gateway** sits in front of the agent runtime. It connects Slack requests, web requests, and tool calls to the right isolated environment, while enforcing the platform's rules around sessions, tools, and outputs.

An **isolated agent runtime** is where the agent actually runs. Each user or shared persona can have its own environment, which keeps blast radius small and makes tool access easier to reason about.

A **web control plane** gives users and administrators a place to manage agents, OAuth connections, shared personas, policy, and operational settings. It also gives platform operators visibility into fleet health and lets them take targeted actions on OpenClaw gateways, such as resetting unhealthy sessions.

A **Kubernetes provisioner** manages the lifecycle of the agent runtimes and supporting infrastructure.

A **branding and skills layer** defines how an agent should present itself, what instructions it receives, and which reusable skills it can access. These artifacts are managed from the web control plane and mounted into the Kubernetes pod as read-only files. In our case, that includes files such as [**<u>AGENTS.md</u>**](http://agents.md/), [**<u>SOUL.md</u>**](http://soul.md/), and [**<u>IDENTITY.md</u>**](http://identity.md/). The point is simple: the gateway and the agent can read their identity and instructions, but they cannot rewrite them at runtime.

Skills are governed the same way. We maintain a centralized skill library that is curated and reviewed with security in mind. Employees and teams can submit new skills for review; once approved, users can add or remove available skills from their profile settings. The selected skills are then mounted read-only into that user's Kubernetes pod. We are also working on department-aware skill exposure, so sensitive or specialized skills can be made available only to the teams that should use them, such as engineering-only operational skills.

A **model routing layer** lets different agents use different model backends. Higher-stakes reasoning tasks can use managed models through Google Vertex AI. Simpler or higher-volume workflows can run on smaller models, including self-hosted Ollama models on GPU machines.

A **token minting service** issues narrowly scoped, short-lived credentials when an agent invokes a tool.

An **OAuth vault** stores and protects user and bot OAuth grants. Long-lived grants stay in the vault; they are not copied into the agent runtime.

**Controlled tool wrappers** sit between the agent and provider tools. Instead of handing an agent broad access to CLIs or APIs, Maestro exposes constrained wrappers around tools like GitHub, Google Workspace, ClickUp, Notion, PagerDuty, New Relic, and internal systems.

The platform runs on **Google Kubernetes Engine (GKE)** with Istio, mTLS, and SPIFFE-based workload identity, so internal services can prove who they are before exchanging sensitive requests. Today, Maestro runs at meaningful internal scale: more than 500 pods across gateways, runtimes, and supporting services.

<img src="openclaw-business-architecture/source/media/image5.png" style="width:7.83333in;height:6.75407in" alt="Article content" />

**Operating the Agent Fleet**

Once every employee, team channel, and workflow can have an assistant, the operational problem stops looking like "run a bot" and starts looking like "run a fleet."

That is why the web control plane is not just an admin settings page. It is where we inspect fleet health, see which OpenClaw gateways are running, spot unhealthy sessions, and take narrow operational actions without disrupting the broader system.

Agent reliability is user trust. If an incident assistant is stuck, or a personal agent has a stale session, the platform team needs to see it quickly and fix it safely. Kubernetes gives us the scheduling and isolation primitives; the control plane gives us the product-level operations view.

The same fleet view helps with cost. Because OpenClaw can route agents to different model backends, we can reserve larger managed models for work that needs them and move routine or high-volume tasks to cheaper models. In practice, that means using Google Vertex AI when managed quality and operations are the right tradeoff, and using self-hosted Ollama models on GPU machines when local inference is a better fit.

**Personal Agents, Shared Personas, and Profiles**

Three interaction patterns have mattered most so far.

A **personal agent** is the one you use directly. It can act with your permissions, subject to policy, confirmation requirements, and the tools you have connected. If you ask it to draft a pull request, search your documents, or inspect something you can access, it operates as your delegated assistant.

A **shared channel persona** is an agent identity designed for a team, channel, or workflow. An incident channel might have an incident assistant. A support channel might have a customer operations assistant. A platform channel might have a deployment helper.

Shared personas are powerful because they create a consistent team assistant. They are also more sensitive because many people can invoke them. That makes actor policy explicit and important.

A **profile assistant** is attached to an employee's internal profile. It helps colleagues learn what that person works on, where relevant docs or goals live, what they can help with, and how to contact them.

The security boundary is important. A profile assistant represents owner-published context, not the profile owner's private credentials. If Alice asks Damian's profile assistant, "Where are Damian's OKRs?", it can answer from information Damian chose to publish. If it later follows a link into Google Drive or Notion, it should do so as Alice, not as Damian. Alice should only see what Alice is already allowed to see.

**Requester, Actor, and Persona**

Maestro separates three concepts that simpler bots often blur.

The **requester** is the human who asked for something. If Alice asks the agent to investigate a failing deployment, Alice is the requester.

The **actor** is the identity whose credentials are used to perform the action. Sometimes this is the requester. Sometimes it is a bot identity. Sometimes policy determines that the agent can try the requester first and fall back to a bot identity.

The **persona** is the agent identity that responded. In a direct message, that might be a personal agent. In a channel, it might be a shared incident-response persona. On an employee profile page, it might be that employee's profile assistant.

This distinction matters because "the bot did it" is not good enough for real operations. We need to know who requested the action, which agent handled it, and whose authority was used.

A profile assistant makes the distinction concrete. If Alice asks Damian's profile assistant a question, the requester is Alice, the persona is Damian's profile assistant, and the actor is Alice whenever external tool access is needed. The assistant may represent Damian's published profile, but it does not inherit Damian's private authority.

**The actAs Model**

We use explicit actAs modes to decide which credentials an agent may use.

The actAs model is not a new cryptographic primitive. It is a policy layer over familiar enterprise identity patterns: delegated OAuth, service accounts, token exchange, and impersonation. Its purpose is to make AI agent authority explicit. A prompt should not decide whose credentials get used; the platform should.

**invoker**

In invoker mode, the agent acts using the requester's credentials.

This is the cleanest model for user delegation. If you ask the agent to do something, it can only do what you can do. The audit trail can attribute the action back to you as the requester and actor.

This mode works well for personal productivity tasks, user-scoped GitHub actions, document retrieval, and workflows where individual authorization matters.

It is also the right default for profile assistants. When one employee asks another employee's assistant a question, tool access should happen with the asker's permissions. That keeps profile assistants useful without turning them into a way to borrow someone else's access.

**maestro-bot**

In maestro-bot mode, the agent acts using a managed bot identity.

This is useful for team workflows where the action should come from a stable service account rather than a specific person. For example, a shared channel assistant might update a team-owned queue, post a standardized status update, or run a workflow owned by the platform team.

Because this mode uses shared authority, it requires clear policy and auditability.

**invoker-with-bot-fallback**

In invoker-with-bot-fallback mode, the agent first attempts to act as the requester. If the requester lacks the required access, the system may fall back to the managed bot identity when policy allows it.

This mode is useful for workflows where the user should normally be the actor, but a team-owned bot can complete specific approved actions. It gives teams flexibility without silently turning every action into broad bot authority.

Only Admins can create personas and bind them to channels. This way we explicitly understand the risk profile of each deployment and restrict and mitigate as needed before deploy.

**Security Model**

The security model starts with a simple rule: the agent runtime should not be where long-lived credentials live.

Agents can reason, plan, and invoke tools, but they do not hold durable secrets. When a tool needs credentials, the platform mints them just in time.

**No Long-Lived Credentials in Agent Runtimes**

Isolated runtimes reduce blast radius, but isolation is not a reason to store permanent secrets inside them.

OAuth grants live in a vault. When an agent needs to call a tool, it goes through a controlled wrapper that requests a short-lived credential from the token minting service. Once the tool finishes and exits, the temporary credential is gone from the sandbox.

This reduces the impact of runtime compromise and makes credential use easier to monitor.

The same idea applies to model calls. We patched OpenClaw so Google Vertex AI calls can use GKE Workload Identity Federation from inside the cluster, instead of requiring a GOOGLE_APPLICATION_CREDENTIALS file in the pod. That removes another static secret from the agent runtime and lets Google Cloud IAM handle workload-to-service authorization.

**Short-Lived Token Minting**

Credentials are minted for specific tool invocations.

The token request includes context: requester, actor, persona, tool, intended action, and policy constraints. That context allows the platform to enforce least privilege and produce useful audit logs.

The goal is not merely to check whether the agent has "access." The goal is to know why access was granted, for whom, and for what action.

This is particularly important for profile assistants. The platform needs to distinguish "Alice asked Damian's assistant" from "Damian asked his own assistant" because those turns may have the same persona but different actors and different access rights.

**Controlled Tool Wrappers**

Many company tools already have CLIs or APIs. Giving an agent unrestricted access to those interfaces is risky.

Controlled wrappers provide a safer boundary. A wrapper can validate arguments, enforce policy, request the right token, redact sensitive output, require confirmation, and emit structured audit events.

This changes the mental model from "the agent can run a command" to "the platform exposes a governed capability."

**gVisor Runtime Sandboxing**

Kubernetes pod isolation is necessary, but it is not sufficient when the workload inside the pod can run arbitrary code, invoke tools, and execute shell commands on behalf of users.

Agent runtimes on GKE run under **gVisor**, Google's application kernel sandbox. Instead of giving each pod direct access to the host kernel, gVisor intercepts syscalls at a user-space boundary. That gives us a stronger containment layer around code we do not fully control: model-driven tool use, third-party skills, and anything an agent might attempt at runtime.

The sandbox also gives us observability we would not get from a normal container alone. Because syscalls pass through the gVisor boundary, we can analyze syscall patterns for behavior that looks suspicious: unexpected file access, process spawning, network activity outside approved paths, or attempts to probe the environment. Those signals become another input for security review, incident response, and ongoing tuning of what agent runtimes are allowed to do.

gVisor is not a substitute for network policy, short-lived credentials, or read-only mounts. It is the layer that limits what a compromised or misbehaving agent can do on the node itself, while giving us a clearer view of what it tried to do.

**Read-Only Guardrails**

We do not assume agents are trustworthy just because we gave them a good prompt.

The control plane owns the agent's branding, identity, baseline instructions, skills, and gateway configuration. Those artifacts are mounted into the Kubernetes pod as read-only files and PVC mounts. The agent and gateway can use them, but they cannot edit them.

This gives us deterministic guardrails outside the model's control. If an agent is instructed to ignore its identity, rewrite its own policy, or mutate its tool configuration, it should not be able to do that by changing the files that define its behavior. Prompts still matter, but the durable rules live in platform-managed, read-only state.

The same principle applies to skills. A skill is not just a prompt snippet someone copied into a chat. It is a reviewed capability from a central library, selected through profile settings, and mounted into the runtime in a way the agent cannot modify. Over time, department-aware access will let us narrow the skill catalog further, so a support workflow, finance workflow, and engineering workflow do not all see the same set of capabilities by default.

**Network Layer Policies**

Security does not stop at authentication. We also restrict which pods are allowed to talk to each other at the network layer.

On GKE, we use **Istio authorization policies** and **Kubernetes NetworkPolicies** together. Istio policies govern service-to-service traffic inside the mesh: which workloads can reach the token minting service, the OAuth vault, or an OpenClaw gateway. Kubernetes NetworkPolicies provide a complementary baseline at the pod level, limiting east-west traffic so a compromised runtime cannot freely probe the cluster.

The default posture is deny-by-exception. An isolated agent runtime should be able to reach its gateway, the model backend it is configured to use, and the controlled tool wrappers it needs — not every other pod in the fleet. The provisioner, vault, and minting services should accept connections only from the identities that legitimately depend on them.

This matters at our scale. With more than 500 pods across gateways, runtimes, and supporting services, unrestricted inter-pod connectivity would make lateral movement too easy. Network segmentation does not replace mTLS or short-lived credentials, but it reduces blast radius when something goes wrong.

**Mesh Identity and Signed Requests**

Service-to-service communication runs through Istio as our service mesh, with mTLS and SPIFFE identity. Internal services can prove who they are before exchanging sensitive requests.

For example, if Damian asks Maestro to perform a GitHub action, the token request should originate from the pod that carries Damian's expected SPIFFE workload identity. A request for Damian's GitHub access coming from another pod should be rejected, even if it has a plausible-looking payload.

For important authorization flows, the platform also uses signed claims, such as JWS payloads, to preserve request context across service boundaries. This helps prevent confused-deputy problems, where one service accidentally performs an action on behalf of the wrong identity.

**Audit Logs and Attribution**

Every meaningful action needs an audit trail.

The system records the requester, actor, persona, tool, action, and relevant decision context. That makes it possible to answer questions later:

- Who asked the agent to do this?

- Which persona responded?

- Which credentials were used?

- Was a fallback identity involved?

- Did the user confirm the action?

- Which system received the request?

Admins also need a way to inspect what happened after the fact. We collect session data from OpenClaw gateways through Kubernetes cronjobs that poll gateway state and write it into databases for analysis. From the control plane, admins can search across sessions, tool invocations, suspicious messages, and other operational signals.

That turns audit data into something useful during both security review and day-to-day operations. If a tool call looks unusual, or a message appears to be probing for secrets, the team should be able to find the relevant session, see which identity was used, and understand what the agent did next. We are also working on SIEM integration so those signals can flow into the same detection and response workflows as the rest of our infrastructure.

For internal AI agents, auditability is not a compliance afterthought. It is part of the product.

**Confirmation for Risky Actions**

Some actions should not happen automatically.

The agent can require human confirmation before performing risky operations, such as writing to production systems, changing access, sending external messages, or triggering incident workflows.

The confirmation step is not just a UX pattern. It is a control point where the system can restate the intended action, actor, and target before proceeding.

We also have policy-driven step-up confirmation in the backlog. For higher-risk actions, policy could require the user to validate the request through a configured second channel, such as WhatsApp, Signal, or SMS, before the tool invocation is allowed to proceed.

**Practical Use Cases**

The architecture is designed for the work people already do.

In engineering, an agent can investigate CI failures, summarize pull requests, draft code changes, inspect deployment state, search internal documentation, and coordinate reviews.

During incidents, it can summarize Slack threads, pull context from PagerDuty and New Relic, find recent deploys, gather runbook steps, and keep the channel updated.

For support and customer operations, it can connect customer context, internal notes, product behavior, and follow-up tasks while respecting access boundaries. The goal is not to replace the operator's judgment. It is to compress the time spent gathering context. If troubleshooting that used to require jumping across tools can be summarized in minutes, customer operations teams can validate the recommendation and move directly to the fix.

For knowledge work, it can search across documents, tickets, and discussions, then synthesize answers with links back to sources.

For teams, shared channel personas become specialized assistants: a platform helper, an incident coordinator, a support triage assistant, or a project memory bot. In engineering operations, the same pattern can reduce mean time to resolution. An assistant can gather logs, recent deploys, alerts, related pull requests, and likely causes, then post a concise investigation for engineers to validate and act on.

For the internal directory, profile assistants make the company easier to navigate. Instead of asking around for who owns a system, where a person's OKRs live, or what someone can help with, employees can ask the person's profile assistant. The assistant answers from published profile context and, when connected to other tools, only uses the asker's own access.

The common thread is that the assistant meets people where the work already is, while the platform handles identity, credentials, policy, and audit.

**Lessons Learned**

The biggest lesson from building Maestro is that AI agents need identity, not just prompts.

A prompt can describe what an agent should do. It cannot safely decide whose authority the agent should use, how credentials should be minted, whether a shared persona can perform an action, or how the result should be audited.

Secure tool use is a platform problem. It requires runtime isolation, service identity, short-lived credentials, controlled tool boundaries, and policy enforcement. OpenClaw makes that practical for us by giving the agent layer a consistent runtime and gateway model instead of forcing every workflow to reinvent how agents run, call tools, choose models, and manage sessions.

Agent instructions should not be self-modifying. Branding, identity, skills, and gateway configuration belong in control-plane-managed, read-only mounts. Skills also need governance: a central library, security review, profile-level selection, and policy about which departments can use which capabilities. We still use prompts, but we do not trust prompts as the only boundary.

Shared and profile-based agents need explicit actor policy. A channel assistant is not the same thing as a personal assistant, and a profile assistant is not a proxy for the profile owner's private credentials. The system must make those distinctions clear.

Auditability has to be built in from day one. Once agents start taking action across company systems, logs are not just debugging output. They are the record of delegated work.

**Key Takeaways**

- Maestro is the name we use internally, but the bigger idea is secure delegation across company tools.

- OpenClaw provides the gateway and runtime foundation for creating a consistent AI layer across Slack, web profiles, and other internal surfaces.

- OpenClaw also helps control cost by letting different agents use different model backends, including Google Vertex AI and self-hosted Ollama models on GPU machines.

- The architecture separates requester, actor, and persona so actions can be attributed correctly.

- The actAs model applies established delegation and impersonation patterns to AI agent tool use.

- Profile assistants extend the same model beyond Slack: employees can interact through published personal assistants without inheriting each other's access.

- Agent runtimes do not store long-lived credentials; tools receive short-lived tokens at invocation time.

- Branding, identity, skills, and gateway configuration are mounted read-only so agents cannot rewrite their own guardrails.

- Skills come from a centralized reviewed library, can be selected from profile settings, and are moving toward department-aware access controls.

- Controlled tool wrappers create policy boundaries around powerful provider CLIs and APIs.

- Fleet operations matter: at 500+ Kubernetes pods, the web control plane needs to expose health and safe operational actions for OpenClaw gateways.

- Shared channel assistants and profile assistants require explicit policies for whose authority they use.

- Internal AI agents become trustworthy when identity, least privilege, confirmation, and auditability are built into the system from the beginning.
