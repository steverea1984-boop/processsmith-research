# ProcessSmith OS: read-only source study

Accessed: 2026-09-08. Publisher/owner: ProcessSmith, existing local repository. Scope: source and test inspection for an own-business Gmail CRM handoff. No app, tests, dependency installation, remote fetch, mailbox connection, or database was run. No environment files, runtime data, seed records, customer records, or secrets were opened. Only this research note was written; the prototype and its handoff remain untouched.

## Revision and decision

- Canonical inspected checkout: `F:/02_Work/ProcessSmith/repos/processsmith-os`.
- Branch: `codex/4-crm-core`.
- HEAD: `3a4f79e538af1dc0c7ec648ae2364c27509d9d48`.
- `git status --short` and `git diff --stat` returned no changes. This is a clean working-tree observation, not proof that a PR has merged or that the branch is the current approved baseline. Only this local branch appeared in the local branch listing.
- The newest entries in `CLAUDE_HANDOFF.md` say Task 3 CRM is PR 22, awaiting Steve's review/merge, and Task 2b PR 21 was merged. Current remote/PR state was not checked. Older entries in the same document describe superseded branches and test counts.

Opinion [medium]: extending this repository should be the first feasibility candidate if Steve wants CRM inside his existing task/work hub. It already contains working persistence paths for the entities Atomic would otherwise replace, plus company-linked task hierarchy that Atomic does not supply in the same form. Gmail, booking and a real embedded assistant still need to be added to either foundation.

Flip fact: prefer a shallow Atomic fork if Steve wants a separate sales-focused application, accepts the Supabase service model, and an isolated comparison shows that Atomic's contacts/deals UI and authentication save more work than preserving the existing task hub. Runtime quality and the unmerged-branch question can also change the decision. This study does not settle Steve's application preference.

## What the source actually implements

| Area | Confirmed source behavior | Limit for the requested CRM |
| --- | --- | --- |
| CRM storage | Express CRUD for companies, contacts and opportunities uses prepared SQLite statements. Company tags serialize as JSON; names, optional text/numbers and company relationships are validated. | This is real storage code, not seed-only React state. It has not been executed during this study. |
| Relationship integrity | Contacts/opportunities require an existing company. Active opportunity must belong to that company. Deleting/moving an opportunity clears the active pointer. Deleting a company cascades CRM children and sets related tasks' company link to null. | Company ownership here means a data relationship, not a user's access rights. The company-first contact model needs a decision for inbound leads whose employer is unknown. |
| Task/hierarchy storage | Spaces, folders, lists, tasks and statuses have real API routes and SQLite tables. A subtask is a full task row with a parent reference and same-list/cycle checks. Tasks can link to a company. | Tasks currently have no contact or opportunity foreign key. Contact-specific follow-ups need a deliberate extension, not a second task system. |
| CRM UI | `useCompanyData` loads the three CRM collections through `apiClient`; normalizers adapt database names to UI names. `CompanyCockpit` provides create/edit/delete dialogs, company summary, contact and opportunity panels, active opportunity selection, and related task display. | No pipeline board or email conversation inbox was found. Opportunity stage is free text, value has no currency field, and contact email is a single optional string. |
| Client recovery | Confirmed writes are applied to local state before reconciliation GETs. Older load responses are ignored; API failures have visible state. Company deletion also reconciles task links. | This is useful existing work to preserve. Loading whole collections and refreshing them after writes is not yet a large mailbox synchronization design. |
| Notes/activity/files | Contact `notes` is a persisted text field. Tables exist for task comments, checklists and attachment metadata. | Company Files & Notes, Activity, calls, users and agents still come from seed imports. Table presence does not mean API/UI/upload implementation. No persisted communication timeline or actual file upload route was found. |
| Google/email/calendar | Searches of application source, server routes, schema and package manifest found no Gmail/Google OAuth client, provider sync, calendar events, availability, public booking or email send implementation. | Contact email text, last-touch date, due dates and references to email approval are not integrations. New provider data, durable sync state and booking logic are required. |

The README and the historical July 5 context in `CLAUDE.md`/spec still describe seed-only data and no tests. Those statements are superseded for current task/hierarchy/CRM code. The current handoff and inspected files agree on that progress. The shelved Supabase draft is not the active database.

## Authentication, assistant and automation boundaries

**Authentication:** `server/index.js` mounts one `requireOpenClawToken` gate ahead of all current `/api` routers, with `GET /api/health` as the exception. No token configured yields 503; a wrong/missing token yields 401. `src/lib/apiClient.js` places `VITE_OPENCLAW_TOKEN` into browser requests. There is no user login/session identity, per-user authorization, or tenant isolation in this implementation.

The approved v1 spec explicitly accepts this shared token for local single-user work and requires revisiting it before remote/phone access. This note does not undo that decision. Source does reveal a configuration distinction worth checking before any future trial: Vite defaults to loopback, but `server/lib/env.js` defaults `API_HOST` to all interfaces. Actual configured binding/exposure was not inspected. Do not describe the API as loopback-only based on the README.

`src/lib/supabaseClient.js` can construct a client if two frontend environment settings exist, but no Supabase query or auth method use was found. Its `dataMode` badge can say “Supabase connected” based on client construction alone. It is not evidence of live Supabase persistence or authentication.

**Browser assistant:** `App.jsx` passes live task/hierarchy/CRM collections together with remaining seeded feature data into `ChatPanel`. `sendPrompt` directly calls `buildChiefOfStaffReply`; that function checks prompt keywords and returns preset summaries/navigation actions. Browser messages live in React state and reset when their context/data changes. There is no model request, streaming response, durable conversation, or action-execution tool loop on this path.

**External agent bridge:** the OpenClaw context, company and message endpoints use `server/lib/context.js`, which still imports seed arrays into `osData`. They do not query the new SQLite CRM. A company created through live CRM CRUD will therefore not become available to these context/message routes through that creation alone. The message endpoint also calls the same deterministic reply builder. An external OpenClaw agent can exist outside this app; that does not make this endpoint an embedded model.

`POST /api/openclaw/proposed-actions` accepts six proposal types and stores events marked `pending_review`. `store.js` reads and rewrites a JSON array, keeping the newest 250. No approve/reject/execute endpoint or corresponding browser event consumption was found. This is a proposal record, not a durable automation engine or immutable audit history; concurrent read-modify-write operations are also a known future concern in the spec.

The health/context responses list `delete_record` as blocked or approval-required, but current task/CRM DELETE endpoints accept the same shared token. Likewise, task `requires_review` is explicitly enforced by agent convention, not a server-verifiable caller distinction. These informational lists must not be treated as authorization controls when an LLM begins reading inbound mail. A future assistant needs server-enforced action permissions, approval records and audit evidence before it gains external write tools.

Task goal fields are accepted by the current CRUD API. Dependency and flag columns/tables exist, but `/tasks/unblocked`, dependency editing, flag/unflag, custom-field approval and an execution loop are not implemented in the inspected route set. The plan schedules them later. Do not mistake the larger approved v1 spec for completed functionality.

## Storage and extension seams

1. **Database:** `server/lib/db.js` opens `better-sqlite3`, enables foreign keys and executes `server/db/schema.sql` at module load. `PROCESSSMITH_OS_DATA_DIR` selects a separate data directory; default schema/data paths depend on the process working directory. No migration framework or schema-version history is present. Existing `CREATE TABLE IF NOT EXISTS` statements will not upgrade old tables when new columns are added. A tested migration/backup approach is needed before durable mail or calendar state is introduced.
2. **CRM adapter:** add supported CRM fields through `server/routes/companies.js`, SQL schema/migrations, `features/companies/normalize.js`, and `CompanyCockpit`. Preserve its current relationship checks and confirmed-write/reload behavior. CRM records currently lack general created/updated timestamps and revision checks, email identity constraints and external provider IDs. Plan mail identity and deduplication before auto-creating contacts.
3. **Tasks:** reuse `features/tasks/useWorkspaceData.js`, normalizers and the existing task API for follow-up tasks. Preserve status semantics, company unlinking and subtask rules. The existing queue serializes client task edits; it does not provide cross-client or worker idempotency/concurrency control.
4. **Provider boundary:** add a server-side Google connector and durable provider account/message/thread/event/sync-state tables behind the existing API pattern. Do not put provider refresh credentials in Vite variables, store messages as contact notes, or have a browser carry out sync. Exact Google scopes and sync recovery belong to the separate Google integration study.
5. **Assistant boundary:** `ChatPanel` is a usable UI seam, not an agent runtime. Replace the deterministic transport deliberately and wire `context.js` to canonical records. Keep model access behind validated server operations. The old JSON event store and client policy text are insufficient for action approval/audit/idempotency.
6. **Booking boundary:** no implementation exists to extend. Decide whether a public booking surface is a separate narrow service/page or part of a properly authenticated hosted deployment. Publishing the current internal API/client would change its approved local-only assumption.

`App.jsx` still has more than 2,200 lines and mixes working features with prototype views. Existing guidance is to extract a feature as it is changed, not undertake a wholesale rewrite. Atomic patterns can inform a contact timeline or pipeline view without replacing the current data layer.

## Tests and what their evidence means

Static inventory found **129 top-level `test(...)` declarations across 18 test files**, including 33 API tests. This agrees with the most recent historical handoff total. **No current pass claim is made: tests and build were not run.**

- `server/test/api.test.js` uses a temporary data directory and fixture token before dynamically importing the server; it checks representative token gating, hierarchy/task CRUD, parent cycles/list rules, CRM validation/CRUD, active opportunity integrity, and company deletion preserving tasks.
- `server/test/crm-persistence.test.js` really spawns the API, creates a company/contact/opportunity and active pointer, stops the process, restarts it on the same temporary database, and reads the values back. Its second test checks cleanup after server-start timeout. This is substantive persistence-test code, not a mocked storage assertion.
- CRM normalizer/state tests cover null fields, request allowlists, company/task unlinking, pointer cleanup and selection reconciliation. Task tests cover status semantics, drafts, queues, errors/retries, hierarchy moves and nested task trees.
- `modalUtils.test.js` includes a headless Chromium DOM test. `TaskDetailDialog.test.js` loads JSX through Vite and renders static markup. Consequently `node --test` is not entirely a dependency-free pure unit suite; a later task should check the existing local toolchain/browser availability without installing anything silently.

No tests for Gmail, OAuth, calendar, booking, model tools or real authorization exist in the inspected source. Their absence follows the missing implementations, not a claimed test failure.

## First bounded feasibility check for the execution task

1. Read the current repo instructions/handoff and check live PR 22/default-branch state, active work and worktrees. Preserve the shared canonical checkout. If independent code work is appropriate, use a managed sibling Git worktree under the filing standard, not an unmanaged folder copy. Do not merge the CRM branch automatically; this repo reserves merging to Steve.
2. Confirm the intended foundation and the coexistence boundary with the existing ClickUp source of truth. The present research does not authorize replacing ClickUp, migrating live data, publishing the app or connecting real mail.
3. Review the existing test bootstrap and environment lookup before running. Use a temporary, synthetic-only data directory and explicit loopback binding from the correct working directory; avoid the real database, seed import command and production credentials. Run existing tests/build and a focused browser check, recording the checked revision and actual result.
4. In that isolated check, create/edit/reload a company, contact, opportunity and related task; restart the API; verify values survive. Delete only synthetic CRM records and confirm active-pointer/task-unlink behavior. Exercise CRM refresh failure without duplicating a successful write. Confirm missing/wrong token rejection, while describing it as the existing local guard.
5. Demonstrate the current chat/bridge distinction using synthetic context. Before any assistant milestone is accepted, a newly saved CRM record must be visible through the agent's canonical read path, and no seeded customer record should leak into the test context.
6. Write the smallest revised spec/plan for identity, schema migrations, Gmail read/sync, calendar/booking and assistant actions. Run one synthetic message-to-contact-to-follow-up slice before committing to a broad interface refactor. Set up real Google OAuth only as its separately authorized integration step.

Open questions: whether Steve wants one combined app; current merge/CI state; available local dependencies; real runtime binding; data migration/backup needs; email ownership/aliases and contact matching; desired CRM pipeline and currency; deployment/public booking topology; and auth/approval design. These are bounded execution decisions, not reasons to discard the existing source sight unseen.

## Source register

All entries below were read from the local checkout on **2026-09-08**, publisher **ProcessSmith**, at the HEAD above. Paths link directly to source; no mutable remote branch claims are required.

| Source | Supports |
| --- | --- |
| [AGENTS.md](../../../processsmith-os/AGENTS.md), [CLAUDE_HANDOFF.md](../../../processsmith-os/CLAUDE_HANDOFF.md), [CLAUDE.md](../../../processsmith-os/CLAUDE.md), [README.md](../../../processsmith-os/README.md) | Workflow, current/historical state conflicts, Steve-only merge rule and previous verification claims. |
| [Intent](../../../processsmith-os/docs/intent.md), [v1 spec](../../../processsmith-os/docs/v1-core/spec.md), [plan](../../../processsmith-os/docs/v1-core/plan.md) | Own-business task hub, accepted local token tradeoff, deferred features and build order. Design intentions are distinguished above from working code. |
| [package.json](../../../processsmith-os/package.json), [vite.config.js](../../../processsmith-os/vite.config.js) | Actual runtime/dependency/scripts and frontend binding. |
| [server/index.js](../../../processsmith-os/server/index.js), [env.js](../../../processsmith-os/server/lib/env.js), [apiClient.js](../../../processsmith-os/src/lib/apiClient.js) | Route mount/gate, browser token, binding default, bridge behavior and API calls. |
| [db.js](../../../processsmith-os/server/lib/db.js), [paths.js](../../../processsmith-os/server/lib/paths.js), [schema.sql](../../../processsmith-os/server/db/schema.sql) | SQLite bootstrap, isolation variable, actual relationships and currently available fields. |
| [companies.js](../../../processsmith-os/server/routes/companies.js), [tasks.js](../../../processsmith-os/server/routes/tasks.js) | CRUD, validation, transactions, goal fields and implemented endpoint limits. |
| [useCompanyData.js](../../../processsmith-os/src/features/companies/useCompanyData.js), [normalize.js](../../../processsmith-os/src/features/companies/normalize.js), [CompanyCockpit.jsx](../../../processsmith-os/src/features/companies/CompanyCockpit.jsx) | Live CRM adapter/UI and recovery seams. |
| [App.jsx](../../../processsmith-os/src/App.jsx), [chiefOfStaff.js](../../../processsmith-os/src/lib/chiefOfStaff.js), [supabaseClient.js](../../../processsmith-os/src/lib/supabaseClient.js) | Live/seed UI mixture, deterministic chat and inert Supabase readiness distinction. |
| [context.js](../../../processsmith-os/server/lib/context.js), [store.js](../../../processsmith-os/server/lib/store.js), [OpenClaw guide](../../../processsmith-os/docs/OPENCLAW_AGENT.md) | Seed-backed bridge, capped JSON event store and stated proposal policy. No configuration values or source customer examples are retained here. |
| [API tests](../../../processsmith-os/server/test/api.test.js), [CRM restart tests](../../../processsmith-os/server/test/crm-persistence.test.js) | Existing isolated API and real-process persistence test structure. |
| [CRM state tests](../../../processsmith-os/src/features/companies/companyState.test.js), [TaskDetailDialog test](../../../processsmith-os/src/features/tasks/TaskDetailDialog.test.js), [modal tests](../../../processsmith-os/src/components/modalUtils.test.js) | Representative reconciliation and browser/JSX test requirements; remaining test files inventoried by name/declaration. |

Additional comparator: [pinned Atomic source study](../../../../../../03_Learning/Research/projects/open-source-agent-crm/raw/atomic-source-study.md), Marmelab primary code at `7186af64d4cf18cbc928cdf57d2390e4d67fd65c`, accessed 2026-09-08. Atomic is MIT with a provider seam; its default usable backend includes Supabase Auth, PostgREST, Storage, views and Edge Functions. Its FakeRest demo is not production authentication or persistence. Preserve Atomic's MIT notice for copied code and review separate dependency licenses; no Atomic code was copied into ProcessSmith OS.

Applicable filing source: [Collaboration & Filing Standard](<F:/02_Work/Code & Automation/shared-agent-kb/agent-kb/wiki/collaboration-standard.md>), ProcessSmith shared-agent-kb, read 2026-09-08. It preserves canonical paths/shared checkout, requires managed worktrees for second checkouts and keeps ClickUp as task/pipeline source of truth. The research-only scope overrides the prototype's routine instruction to update its handoff after code work.
