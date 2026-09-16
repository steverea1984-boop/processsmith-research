# Building an internal CRM from existing work and open-source examples

## Recommendation

An internal CRM with contact history, Gmail conversations, Google Calendar booking and a useful assistant is a reasonable project. The best starting point is the existing ProcessSmith OS prototype, subject to a short verification of its current branch and storage. Atomic CRM is the strongest alternative foundation from the source studies. HighLevel provides a useful workflow reference, while Relaticle provides an approval pattern to learn from. SeldonFrame demonstrates why a convincing feature list needs source and runtime checks.[^1][^2][^3]

Opinion [medium]: Assess extending ProcessSmith OS before starting a separate CRM. Its current source already contains company, contact, opportunity and task persistence. Atomic would introduce a different backend while still requiring Gmail synchronization, booking and the embedded assistant. Reusing the existing work is likely to reduce disruption.

Flip fact: The existing CRM branch cannot pass its baseline checks, its workflow is a poor fit, or preserving it requires more change than an isolated Atomic pilot. Those findings would favor Atomic with its intended Supabase backend. A decision to remove Supabase while transplanting Atomic's whole interface would lose much of that advantage.

This recommendation is about the next implementation candidate. No application was installed, executed, connected to Google or proved production ready during this study. Implementation belongs in a later task. The [handoff](handoff.md) supplies its starting context, staged tasks and verification gates.

## The first product

The confirmed audience is Steve's own business. Google Workspace and Gmail are the first provider. HighLevel is being studied through public documentation and visual examples, without a trial or account inspection. A commercial platform for multiple client businesses is outside the first release.

The first complete journey should be easy to demonstrate:

1. Add a person and company, with one deal and a next task.
2. See the relevant Gmail conversation on that person's record and compose a reply.
3. Offer a public booking link that respects selected Google calendars.
4. Book, move or cancel the appointment, with the actual result visible in both systems.
5. Create the appropriate next task or proposed follow-up and explain why it exists.
6. Ask the assistant for a grounded account summary or a proposed action, then review any controlled action before it runs.

A small set of fixed follow-up rules is sufficient to test this journey. A drag-and-drop automation designer, campaign sending, SMS, voice, funnels, payments, memberships, client subaccounts and resale can wait. Those are separate products and operating commitments, not necessary scaffolding for a working internal CRM.

ClickUp remains an existing source of truth for tasks and pipeline under the local collaboration standard. The pilot must not silently replace it or start writing back. The first task should map the prototype's local records and imported hierarchy, then record whether the eventual CRM is a view, a selective integration or an intended replacement. A migration needs a separate decision and recovery plan.[^4]

## What the source studies establish

| Reference | Useful contribution | What must still be built or verified |
|---|---|---|
| ProcessSmith OS | Existing company cockpit, CRM and task persistence, local API and tests | Actual baseline on the current CRM branch; owner authentication; live data for the external agent connection; Gmail, booking and a real model-backed assistant |
| Atomic CRM | MIT source, contacts/companies/deals/tasks, configurable screens, import/export and responsive patterns | Default backend depends on Supabase Auth, data API, storage and functions. Its inbound Postmark capture is not Gmail sync. Demo identity/storage is unsuitable for business use |
| HighLevel | Contact-linked communications, booking in context, separate conflict calendars, appointment-triggered follow-up and execution history | Public docs are not a tested account. Some rescheduling instructions conflict. The first product needs its own explicit behavior contract |
| Relaticle | Stored pending actions, review/edit, current permission checks and transactional local CRM writes | A reviewed-version check and reliable external-effect handling are still needed. Its external MCP write tools bypass the chat proposal route |
| SeldonFrame | Shared booking concepts, slot rules and typed agent tools | Native Google sync is disabled in the inspected code. A separate Composio path has uncertain fallbacks. Public rescheduling and strong approval boundaries are incomplete in the inspected paths |

These findings are pinned to the following source revisions. They are not claims about every future release.[^1][^2][^3]

| Project | Revision inspected |
|---|---|
| ProcessSmith OS | `3a4f79e538af1dc0c7ec648ae2364c27509d9d48`, local `codex/4-crm-core` branch |
| Atomic CRM | `7186af64d4cf18cbc928cdf57d2390e4d67fd65c` |
| SeldonFrame | `3f386a221849843a1a535f442e210bf9d293fff9` |
| Relaticle | `4f19fbc297ee91ae32ca29ad50723b21d55fd11d` |

The existing prototype's shared browser token and local agent-policy declarations do not establish separate user and agent authorization. Its current source also defaults the API listener to all interfaces. These are reasons to keep the foundation trial isolated and to establish the intended security boundary before live mailbox data or public booking. Runtime configuration was not inspected.[^1]

The broader comparison remains in the original [market report](../../../../../03_Learning/Research/projects/open-source-agent-crm/report.md). It covers Twenty, EspoCRM, Frappe/ERPNext, Relaticle, Atomic, Krayin, Odoo, SeldonFrame, DenchClaw and complementary booking/messaging tools. It also records the Simple Tech Skills offer, licensing, platform restrictions and alternatives. Repeating that entire comparison here would obscure the narrower implementation decision.

## Lessons from real HighLevel

HighLevel's Gmail integration is a contact-linked conversation bridge. Its documentation distinguishes individual Gmail sends from workflow/bulk email sent through the account's sending provider, and says old mail is not backfilled. Building a full Gmail replacement is therefore unnecessary to reproduce the relevant CRM experience.[^5]

Calendar connection has several meanings. A booking calendar describes an appointment offering. A destination calendar receives the appointment. Conflict calendars supply unavailable time. HighLevel's default mode can import external events as busy blocks; its two-way mode can create appointment records, attendee contacts and workflows. The distinction belongs in plain-language settings, not a single ambiguous sync switch.[^6]

The visually inspected official appointment example puts booking beside an active conversation and groups calendar/contact selection in the appointment editor. That information arrangement is worth adapting. It preserves the context that led to the meeting. The screenshots are official examples, with some older pictured dates; they do not prove the current appearance or behavior of an authenticated account.[^7]

HighLevel's workflow history also supplies a practical design target. A person investigating a message can follow it to the relevant execution, action, time zone and result. Our assistant and scheduled work should be equally explainable. A message saying an action succeeded is not a substitute for a saved result.[^8]

The source study records a material documentation conflict around rescheduling, status names and re-entry. Our implementation should use a stable appointment ID and an explicit version, invalidating reminders tied to the old version. That is a proposed engineering rule, not a claim to reproduce undocumented HighLevel internals.[^9]

## Gmail and Google Calendar are the main integration work

OAuth authorization is an early feasibility check. A business-internal app can qualify for a different verification route from a public app, but Workspace membership alone does not make every Cloud project internal. The project must belong to the relevant organization. Consumer Gmail uses the external route. External apps left in Testing with Gmail/Calendar permissions have short-lived authorization, so a successful first connection is not sufficient evidence of a durable setup.[^10]

The proposed pilot requests only what its functions need. Read selected conversations and send reviewed replies, without adding mailbox deletion or administration. Keep drafts in the CRM initially. Calendar busy-time access and permission to write bookings should be chosen separately. Exact scopes, account ownership, administrator restrictions and consent are an execution gate before a real account is connected.[^10]

Sync must recover from missing notifications, expired cursors and restarts. Gmail can require an initial re-sync after a history error; Calendar has its own token-expiry recovery. These operations rebuild provider caches, not the CRM's customer records or audit history. Historical imports must not accidentally start new outreach.[^11]

Replies need the provider's thread ID and reply headers. Sends need an explicit uncertain state when the request may have succeeded but the response was lost. Calendar writes need saved event identity and checks against changes made in another client. The detailed protocol resources and focused failure tests are in the [Google synchronization study](raw/google-sync-study.md).[^12]

Opinion [high]: Build direct Google integrations for this first provider, with a small application-owned interface around them. Adding a general connector platform now introduces another authorization, data-handling and failure boundary without removing the need to understand Gmail and booking correctness.

Flip fact: The project needs several additional providers immediately, and a connector demonstrably handles the required sync, scopes, retention, recovery and cost requirements. It can then be evaluated against the same acceptance tests.

## What a reliable booking means

Showing an apparently free slot is only the beginning. The server must check the same duration, hours, notice, buffers, exceptions and conflict calendars when the visitor commits. All booking entry points should call the same operation. A selected calendar returning an error is not evidence that the owner is free.[^13]

Two visitors using this application must not both reserve the same host interval. That requires a database-backed reservation or serialized scheduling operation. A saved provider action then creates or updates the Google event. Failures stay visible as pending, failed or uncertain. The application must not silently confirm a local booking after Google failed.

There is no shared transaction between our database and Google Calendar. Another client can still add an overlapping event at the same time. Our requirement is local race prevention plus external conflict detection and recovery. An absolute promise that nothing anywhere can double-book the calendar would be unsupported.

Rescheduling should keep the original appointment identity and history. A failed update must show the still-confirmed time and the requested change. Cancellation or a newer version invalidates obsolete reminders. Public management links should apply to one appointment, expire and be revocable. Existing recurring and all-day Google events must block time correctly even if our public offering initially creates only single meetings.[^11][^13]

## The assistant must work through the application

The assistant's initial job is to summarize selected account history, identify the next task, draft a reply and propose a small set of CRM actions. It should cite the records or messages it used. It should not have a shell, a general-purpose HTTP client, database administration, mailbox administration or the raw Google credentials.

Relaticle shows a useful separation. The model proposes stored work, the owner reviews it, and a server service rechecks permission before applying a local mutation. For our version, approval also binds to the exact reviewed payload and record version. Another tab editing the draft or a new customer reply makes that review stale.[^3]

External writes add another boundary. Approval records a decision; the executor records what actually happened. A crash after a provider accepted a request is different from a request never sent. Model-written `confirmed: true`, a green toast or a changed draft status cannot establish an independent human approval or successful delivery.[^3][^12]

The local Agent Security Standard requires explicit job scope, narrow tools, external-input handling, outward-action approval, audit, stop controls and a pre-release injection test. It currently requires a human approval for each outward agent action. The first follow-up rules therefore create tasks or proposals. Unattended agent-generated email is not a default. Deterministic transactional booking notifications also need an explicit operating policy before activation; the research does not grant blanket sending authority.[^14]

Google permits relevant productivity and CRM uses, but transferring Workspace data to an AI provider requires disclosed, user-consented use for the visible feature. Raw or derived Workspace data must not enter generalized model training or improvement. Verify provider retention, logging, human-access and no-training terms before using live email. A model being available through an existing agent does not establish permission to send business mail to it. Filtering to CRM conversations also does not narrow the underlying mailbox-wide Gmail read grant.[^10]

## Architecture and operating cost

The minimum initial architecture is one application with a persistent database, a background worker using durable jobs, a Google adapter and a narrow assistant service. Keep the worker in the same project initially. A separate queue service, vector database, generic plugin framework and workflow canvas are not prerequisites.

The default foundation trial should keep ProcessSmith OS's existing stack and SQLite, while testing the transaction and scheduling needs. Do not migrate to Postgres merely because another CRM uses it. Before hosting, verify the chosen platform supports a persistent local database and the desired process model. A platform requiring stateless or multiple writers may justify a managed Postgres decision at that point. Atomic's intended Supabase stack remains the alternative, not a partly transplanted hybrid.[^1][^2]

Public booking needs an available server while customers use it. A local laptop demonstration does not provide an always-available appointment service. Hosting, database recovery, OAuth maintenance, model use and operator time remain costs even if the application code is free.

The execution task should fill this cost worksheet from the selected providers' then-current pricing before deployment:

| Cost | How to estimate |
|---|---|
| Application and worker | Monthly baseline plus compute, storage and traffic; persistent disk requirements |
| Database and recovery | Storage, backups, restore tests and retention |
| Google operations | Existing Workspace plan, API quotas, any Pub/Sub usage and administrative setup |
| Assistant | Input/output usage, model choice, maximum requests and a hard spending cap |
| Email delivery | Reviewed personal Gmail use initially; a separate sending provider only if approved requirements justify it |
| Maintenance | Dependency updates, token reconnection, failed jobs, data correction and periodic recovery checks |

No dollar estimate is presented as a quote. The earlier $97 template price is a purchase price, not a tested total operating cost or a measure of the effort needed to own this system.

## Execution readiness and remaining decisions

The research is sufficient to start a bounded foundation trial. It is not sufficient to connect business data or launch public booking without configuration and verification.

| Decision | Recommended default | When it must be settled |
|---|---|---|
| Extend existing prototype or separate app | Assess ProcessSmith OS first, Atomic as fallback | First task, after branch and baseline verification |
| Existing ClickUp relationship | Preserve it; synthetic CRM pilot | Before real import, write-back or replacement |
| First mailbox and conflict calendars | One mailbox, one booking destination, explicitly selected busy calendars | Before OAuth consent |
| Email inclusion and history | Known contacts and manually included threads; bounded backfill | Before initial import |
| Owner/team access | One owner first, no shared browser secret as production authentication | Before live data or external access |
| Assistant provider and data handling | Unselected; synthetic content until approved | Before real email enters a model |
| Sending policy | Review per outward agent action; fixed rules create proposals | Before any automated delivery |
| Hosting and public URL | Local trial first | Before public booking or always-on sync |

The final handoff uses outcome-based tasks and a small failure-focused verification set. A successful result must prove persistence after restart, correct contact/thread identity, consistent booking policy, safe recovery and visible action results. Screenshots alone cannot satisfy those checks.

## Sources

The [resource register](sources.md) is the entry point for all research materials, including the earlier market report, official HighLevel documents, pinned source files, Google references and local project evidence. Each detailed study records publisher, access date, claim and inspection depth. Discovered but unexecuted tests and unavailable resources are marked separately.

[^1]: ProcessSmith, [current prototype source study](raw/processsmith-os-source-study.md), local source inspected 2026-09-08. Runtime not tested.
[^2]: Marmelab, [Atomic pinned source study](../../../../../03_Learning/Research/projects/open-source-agent-crm/raw/atomic-source-study.md), accessed 2026-09-08. MIT license and backend/file map linked there.
[^3]: SeldonFrame and Relaticle, [booking and approval source study](../../../../../03_Learning/Research/projects/open-source-agent-crm/raw/booking-agent-source-study.md), accessed 2026-09-08. Exact code permalinks and inspection scope included.
[^4]: ProcessSmith, [Collaboration and filing standard](../../../../Code%20%26%20Automation/shared-agent-kb/agent-kb/wiki/collaboration-standard.md).
[^5]: HighLevel, [Gmail two-way email sync](https://help.gohighlevel.com/support/solutions/articles/48001235216), accessed 2026-09-08.
[^6]: HighLevel, [linked and conflict calendars](https://help.gohighlevel.com/support/solutions/articles/155000002374), modified 2026-07-08, accessed 2026-09-08.
[^7]: HighLevel, [manual appointment booking](https://help.gohighlevel.com/support/solutions/articles/48001209829-manually-booking-calendar-appointments), modified 2026-05-08. [Visual observations](../../../../../03_Learning/Research/projects/open-source-agent-crm/raw/highlevel-ui-observations.md).
[^8]: HighLevel, [execution logs and enrollment history](https://help.gohighlevel.com/support/solutions/articles/155000003992-execution-logs-enrolment-history-enhancements), modified 2026-04-15, accessed 2026-09-08.
[^9]: HighLevel, [14-document workflow study](../../../../../03_Learning/Research/projects/open-source-agent-crm/raw/highlevel-workflow-study.md), especially sources H8, H10 and H11.
[^10]: Google, [authorization and data-use study](raw/google-authorization-study.md). Official consent, verification, scopes and policy sources linked there, accessed 2026-09-08.
[^11]: Google, [Gmail sync](https://developers.google.com/workspace/gmail/api/guides/sync), [Calendar sync](https://developers.google.com/workspace/calendar/api/guides/sync) and [Calendar notifications](https://developers.google.com/workspace/calendar/api/guides/push), accessed 2026-09-08.
[^12]: Google, [threading](https://developers.google.com/workspace/gmail/api/guides/threads), [send/error contract](https://developers.google.com/workspace/gmail/api/guides/handle-errors) and [Calendar versions](https://developers.google.com/workspace/calendar/api/guides/version-resources), accessed 2026-09-08. Further sources in [sync study](raw/google-sync-study.md).
[^13]: Google, [FreeBusy](https://developers.google.com/workspace/calendar/api/v3/reference/freebusy/query) and [event creation](https://developers.google.com/workspace/calendar/api/v3/reference/events/insert), accessed 2026-09-08. Application transaction/recovery rules are engineering recommendations.
[^14]: ProcessSmith, [Agent Security Standard](../../processsmith-systems/docs/security/agent-security-standard.md), v1 draft dated 2026-07-03, read 2026-09-08.
