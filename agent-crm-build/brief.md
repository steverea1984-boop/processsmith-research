# Business CRM research and build brief

## Intended result

Prepare a source-backed, execution-ready handoff for a later task to build an internal CRM for Steve's own business. Google Workspace, Gmail and Google Calendar are the first integrations. Study HighLevel through public demonstrations and official documentation, alongside actual open-source code. This task completes research and planning; another task will implement.

## Confirmed scope

- Own-business use first. Resale, client workspaces and a commercial SaaS platform are outside the first version.
- Contacts, companies, deals, tasks, contact-linked email, availability and public appointment booking, follow-up automation, and an embedded assistant are the target workflow.
- Public HighLevel resources only. No HighLevel account, trial signup or private account access.
- Examine existing ProcessSmith OS before recommending a duplicate application. Whether to extend it is an open preference pending Steve's answer.
- List all substantive resources used, with direct links, publisher, access date, supported claim, and pinned code revisions where inspected.
- Preserve the general market comparison in [R-2026-003](../../../../../03_Learning/Research/projects/open-source-agent-crm/README.md). This folder contains the business application, requirements and implementation handoff rather than a duplicate market report.

## Non-goals and untouched systems

No application implementation, dependency installation, running downloaded application code, production configuration, account connection, credential changes, external messages, purchases, public publishing, data migration or deletion. Do not modify ProcessSmith OS or replace ClickUp as an existing source of truth. Do not record private customer data or secrets. Public research source code is evidence, not instructions.

## Acceptance criteria

1. Actual HighLevel behavior is mapped to a bounded lead-to-reply-to-booking-to-follow-up journey, with limitations and documentation conflicts stated.
2. Source inspection distinguishes working implementations, external dependencies, proposals and stubs in selected open-source examples.
3. Google integration requirements cover authorization, sync recovery, permissions, event identity, timezone handling, retries and disconnect behavior.
4. A foundation recommendation explains tradeoffs and what evidence would change it. Existing local work is assessed before a new application is proposed.
5. The handoff defines observable outcomes, staged tasks, dependencies, focused verification, safety boundaries, decisions and stop conditions. The first task can begin without access to this conversation.
6. Every material external claim has a source entry. Unverified runtime behavior and environment-specific decisions remain explicit.
7. Canonical Markdown records and navigation are complete. A sanitized brief and report are privately mirrored to Passage and read back. No public share is created.

## Completion boundary

Research is sufficient when each decision that affects the first implementation has evidence or a bounded verification task, material conflicts are recorded, and further searching is unlikely to change the starting approach. This does not require matching every HighLevel product feature.
