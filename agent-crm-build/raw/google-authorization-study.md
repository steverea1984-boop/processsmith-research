# Google authorization and assistant data boundaries

Access date: 2026-09-08. Publisher for every source below: Google. Scope: an internal ProcessSmith CRM using its operator's Gmail and Google Calendar. Public documentation only; no accounts inspected, grants created, API calls against user data, or settings changed. Sync protocols and booking recovery are covered separately in `google-sync-study.md`.

## Audience and verification

**Fact:** Internal is an OAuth audience restriction, not a synonym for a privately hosted app. It requires a Cloud project associated with a Google Cloud Organization and limits authorization to that organization's members. Outside accounts receive `org_internal`. Workspace administrators can impose additional access controls. Consumer Gmail accounts require the External route. [G1, G2]

**Fact:** External apps in Testing have up to 100 listed testers. Gmail/Calendar test authorizations, including offline refresh tokens, expire seven days after consent. The exception for basic sign-in scopes does not cover Gmail or Calendar. Publishing status and verification are separate: an External app can be In production while still displaying an unverified warning and remaining subject to the applicable cap. [G1, G3]

**Fact:** Google documents verification exceptions for personal use, development/testing and internal use. Internal requires organization ownership and Internal audience, and may require administrator approval. When no exception applies, restricted-scope server access ordinarily brings independent security assessment and recurring reassessment. Do not extend an own-organization exception to customers in other organizations. Domain-wide installation is not a general sensitive/restricted verification bypass. [G2]

**Boundary:** Google explicitly exempts own-domain/organization apps from certain additional scope requirements. That is not a waiver of the general obligation to protect data in transit and at rest, disclose actual handling, or follow OAuth rules. Avoid claiming either that every internal CRM needs a paid annual assessment or that an internal CRM has no Google security duties. [G4]

**Operational decision proposed:** use an organization-owned Internal project for Workspace-only operation after confirming eligibility. If a consumer account is needed, document the External/personal-use route separately. Do not leave the durable working connection in External Testing and describe repeated weekly expiry as a sync bug. Publishing settings are a later authorized configuration task.

## Minimum scope options

Scope names below omit the common prefix `https://www.googleapis.com/auth/` except the full-mail scope.

| Feature | Candidate scope | Consequence |
| --- | --- | --- |
| Read messages for CRM history and assistant context | `gmail.readonly` | Restricted; reads messages/settings but grants no mailbox mutation. |
| Send operator-approved mail | `gmail.send` | Sensitive; send capability without mailbox reading. Pair with readonly when both features are needed. |
| Archive, change read state, or manipulate messages | `gmail.modify` | Restricted; wider read/compose/send and mailbox mutation. Does not allow immediate permanent deletion bypassing Trash. |
| Keep drafts inside Gmail | `gmail.compose` | Restricted; draft management and sending. A draft stored only in the CRM does not need this capability. |
| Header-only integration | `gmail.metadata` | Restricted and excludes message bodies; insufficient for full-text summaries. |
| Full mailbox authority | `https://mail.google.com/` | Includes immediate permanent deletion. Unnecessary for the proposed MVP. |

Gmail classification and permissions: [G5]. **Inference:** start with readonly plus send; add modify only when a selected feature requires it. This reduces powers but does not remove the restricted-data category. A CRM-side filter to selected contacts does not reduce what a readonly OAuth credential can access.

| Calendar requirement | Candidate scope | Limit |
| --- | --- | --- |
| Check own availability | `calendar.freebusy` | Availability, rather than event contents. |
| Check availability on accessible calendars | `calendar.events.freebusy` | Useful when conflict calendars include shared calendars. |
| Write bookings to calendars the operator owns | `calendar.events.owned` | Can read/change/delete events across owned calendars. |
| Write to accessible shared calendars too | `calendar.events` | Broader event access across calendars; select only if needed. |
| Isolate bookings in a calendar created by the CRM | `calendar.app.created` | Creates secondary calendars and manages their events. Does not grant existing primary-calendar event access. |
| Offer a calendar selector | `calendar.calendarlist.readonly` | Lists subscribed calendars; separate from event content/write access. |

Scope meanings: [G6]. `freebusy.query` accepts either freebusy scope and returns busy intervals; it does not require full calendar access. [G7] `events.insert` accepts events.owned or app.created as alternatives to events/full calendar; `primary` can identify the operator's primary calendar without a calendar-list lookup. [G8]

**Opinion [medium]:** test an app-created secondary booking calendar plus freebusy access as the least-privilege starting option. Flip fact: Steve needs appointments written directly into an existing primary/shared calendar, or the secondary-calendar invitation/Meet behavior fails the selected workflow. Then choose events.owned or events as justified. Calendar selection in our UI must still be enforced by the server; an events.owned/events grant is not cryptographically restricted to the one selected calendar. Avoid full `calendar`, calendar sharing, and deletion-of-calendar powers for this MVP.

## Embedded assistant: permitted purpose and provider transfer

**Fact:** Google's Workspace policy lists CRM email productivity and generative summaries among approved Gmail uses. It limits use to visible application features. Transfers for those features require user consent; developer/provider human access has narrowly defined exceptions. The policy also requires transparency about collection/use/sharing and makes the developer responsible for agents and contractors. It calls for user confirmation in the context of agentic behavior. [G9]

**Fact:** Google's AI guidance prohibits raw, aggregated, anonymized, or derived Workspace data from training or improving foundational/generalized models. Personalized-model use has a bounded exception; it is not permission to contribute messages or summaries to a provider's general training pipeline. The guidance also requests an affirmative Limited Use compliance statement. [G10]

**Inference:** third-party inference for an explicit summary/draft feature can fit the permitted transfer route; neither “AI” nor “API” makes every provider arrangement acceptable. Apply these restrictions as the project baseline even where an internal exception removes an assessment requirement. No general-model training, cross-customer improvement, or unrelated evaluation corpus is needed for this CRM.

**Operational decisions proposed:** disclose the selected provider and material data categories before enabling assistant processing; send only selected relevant thread/context; keep OAuth tokens out of model input; use a reviewed provider configuration that excludes generalized training/improvement; keep email sending behind a reviewable approval step. Approval must bind recipient, content and current thread state. External email text is untrusted input, not authority to call tools. Workspace policy identifies prompt-injection protection among its restricted-scope security measures. [G9]

**Status: needs verification:** the provider/product/contract is not selected. Verify its exact training, human review, retention, abuse logging, deletion and subprocessors terms before real mail leaves the CRM. “No training” alone does not establish those other properties. A local model avoids this third-party inference transfer but still needs secure local handling and authorization.

## Operational acceptance conditions

These are proposed implementation requirements, not claims of work already tested.

1. Record actual granted scopes and turn off unavailable features. Denying send must leave reading usable; denying Calendar must not break contact management. Request later scopes only when the operator selects the corresponding feature. Google requires correct partial-consent handling. [G11]
2. Store refresh tokens encrypted at rest; use an approved secret store for client credentials. No tokens in repository, browser local storage, assistant prompts or application logs. Google requires secure token handling and revocation/deletion when access is no longer needed. [G11]
3. Use the supported browser OAuth flow and a client type matching the application, with controlled HTTPS redirects. Do not implement Google login inside an app-controlled embedded webview. [G11]
4. Test expiry/revocation, password change involving Gmail scopes, and administrator restriction. Refresh tokens can fail after those events; production status does not make them permanent. A six-month-unused token can expire, and repeated issuance can invalidate old tokens. Show reconnect state and pause dependent actions. [G3]
5. Test read-only plus send without label/archive/draft-write powers; test app-created calendar scope against a deliberately unrelated calendar. Expected outcome: unnecessary writes are impossible with the granted scopes, not merely hidden in the UI.
6. Verify a denied assistant disclosure causes no model request, and a stale approved draft cannot silently send after recipient/content/context changes. Verify retrieved mail cannot authorize a new recipient, export, deletion or arbitrary tool call. These are our product controls.

## Remaining decisions and source register

**Status: needs verification:** Workspace organization ownership/admin access versus consumer account; booking destination and shared conflict calendars; final requested scopes in the Google console; model provider configuration; data retention/export/deletion rules. Do not inspect private account settings as part of this documentation-only task.

**Retention caution:** Terms section 5(e) limits permanent copies/caching unless permitted by the content owner or applicable law; section 5(d) addresses export. This does not establish a universal CRM email retention period. Record the intended content authorization and retention/deletion behavior before implementing an indefinite mailbox replica. [G12]

All sources accessed **2026-09-08**, publisher **Google**. Source descriptions identify the supporting claims; no vendor implementation has been tested.

| ID | Direct source | Supports |
| --- | --- | --- |
| G1 | [Manage App Audience](https://support.google.com/cloud/answer/15549945?hl=en) | Internal/External, Testing expiry, publishing status and caps. |
| G2 | [Restricted scope verification](https://developers.google.com/identity/protocols/oauth2/production-readiness/restricted-scope-verification) | Verification exceptions, organization prerequisites, assessment route. Updated 2026-08-19. |
| G3 | [OAuth 2.0 overview: refresh token expiration](https://developers.google.com/identity/protocols/oauth2#expiration) | Seven-day External Testing tokens; other expiry/revocation causes. Updated 2026-05-26. |
| G4 | [Google API Services User Data Policy](https://developers.google.com/terms/api-services-user-data-policy) | General secure environment and own-domain additional-requirement exception. |
| G5 | [Choose Gmail API scopes](https://developers.google.com/workspace/gmail/api/auth/scopes) | Scope permissions and sensitivity. Updated 2026-07-22. |
| G6 | [Choose Google Calendar API scopes](https://developers.google.com/workspace/calendar/api/auth) | Narrow Calendar scope meanings. Updated 2026-08-27. |
| G7 | [Freebusy: query](https://developers.google.com/workspace/calendar/api/v3/reference/freebusy/query) | Availability endpoint authorization and response. Updated 2026-05-12. |
| G8 | [Events: insert](https://developers.google.com/workspace/calendar/api/v3/reference/events/insert) | Accepted narrower write scopes and primary calendar identifier. |
| G9 | [Google Workspace user data and developer policy](https://developers.google.com/workspace/workspace-api-user-data-developer-policy) | CRM/summary use, feature transfer, consent, contractors, agentic and security boundaries. Updated 2026-07-22. |
| G10 | [Application Use Cases: AI/ML](https://support.google.com/cloud/answer/13805798?hl=en) | Generalized model-training prohibition includes derived/anonymized data. |
| G11 | [OAuth 2.0 Policies](https://developers.google.com/identity/protocols/oauth2/policies) | Partial consent, token security, appropriate client, browser and redirect rules. Modified 2026-08-05. |
| G12 | [Google APIs Terms of Service](https://developers.google.com/terms) | Sections 5(d) portability and 5(e) content-copy/caching conditions. Modified 2021-11-09. |
