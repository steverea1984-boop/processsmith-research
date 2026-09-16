# Google synchronization and booking study

Publisher: Google unless stated otherwise. Accessed 2026-09-08. Documentation inspection only. No API calls to an account, live messages or calendar mutations. The recommendations below are proposed application behavior, not guarantees from Google.

## Gmail facts

Gmail clients start with an initial bounded retrieval, then use a saved history cursor for changes. An expired history cursor returns 404 and requires a new initial sync. History retention is variable. Save the new cursor only after all pages and changes have been durably applied. [G1]

Implementation requirement: capture a valid starting history watermark before initial paging and replay subsequent history after the initial import. Do not fetch a newer cursor at the end and skip intervening changes. Serialize updates per connection, or use a checked cursor version, so overlapping workers cannot advance past unfinished work. History IDs are opaque identifiers, not consecutive event counts.

Server notifications use Cloud Pub/Sub and carry a mailbox/history reference, not the complete message. Watches must renew within seven days, with daily renewal recommended. Notifications can be delayed or dropped, so reconciliation remains necessary. Google's guide recommends polling for user-owned installed devices. [G2]

To add a reply to a Gmail thread, supply the thread ID, compliant References/In-Reply-To headers and a matching subject. A UI grouping messages under one contact does not establish provider threading. [G3]

The send endpoint returns a Message resource and sends to the To, Cc and Bcc recipients. Its reference does not document a general idempotency-key parameter. Treat the absence as a limitation of the inspected contract, not proof of every possible provider behavior. [G4]

Gmail documents refresh/re-authorization for invalid credentials, reason-specific handling of permission and quota errors, and increasing retry delays. Sending limits are shared across the user's clients. It explicitly cautions that an HTTP 200 alone does not prove successful sending when quota enforcement is delayed. Accepted, observed in Sent, failed and delivered must not be collapsed into one status. [G5]

Message listing supports pagination and search, including RFC message ID queries in the reference. That can help reconcile an uncertain send; it does not promise deduplication or immediate search visibility. Gmail's API search does not expand aliases in the same way as Gmail's interface. [G6][G7]

## Proposed Gmail contract

- One connected mailbox for the pilot. Persist provider message/thread IDs scoped to the connection. Preserve MIME reply headers and sender identity. Treat contact association as a separate relation from a provider thread.
- Start with known CRM contacts and explicitly included threads. Show the chosen backfill window before first import. This is an application filter; Gmail read permission itself is broader. Do not claim that the OAuth grant is restricted to selected contacts.
- Keep drafts in the CRM initially, avoiding extra Gmail draft/write permissions where unnecessary. The first version need not change Gmail read/unread, archive or labels. Make clear which read state belongs to the CRM.
- Use a durable action record before requesting a send. Record recipient set, sender, content fingerprint and intended action ID. A known successful action cannot be reissued on worker restart.
- A timeout after a send becomes `uncertain`, then reconciles against provider evidence. Do not automatically resend because a search has not found it yet. Escalate ambiguity for review. Stable RFC Message-ID is correlation evidence, not an exactly-once switch.
- A reconnect or initial re-sync rebuilds only provider cache, preserving CRM contacts, notes, action logs and approval records. Do not rerun historical automations merely because old messages were reloaded.
- Sanitize HTML, block remote tracking content by default, and keep attachments out of agent context unless selected. MIME handling, recipient display and downloads need explicit size/type boundaries.

## Calendar facts

FreeBusy reports time ranges per calendar and can return errors for individual calendars. Busy intervals use an inclusive start and exclusive end. A successful top-level response therefore does not establish that every requested conflict calendar was checked. [G8]

Event creation accepts a client-supplied ID with defined format and uniqueness requirements. Google cautions that distributed ID collisions are not guaranteed to be caught at creation. Store calendar ID and event ID together; iCalUID has different semantics. Guest notification behavior is controlled separately. Google warns that suppressing notifications with `sendUpdates=none` can cause external-calendar problems. [G9]

Calendar incremental sync uses a sync token with a consistent supported query, paginates until a new token arrives, and returns 410 when a full cache rebuild is needed. The events-list reference prohibits combining syncToken with filters including timeMin, timeMax, q and extended-property filters. Use the documented initial/incremental transition rather than blindly replaying all initial filters. A cache rebuild must not erase the CRM's own booking records. [G10][G16]

Calendar notification channels expire and require replacement. Renewal may overlap channels; notifications are not fully reliable. The receiver must fetch current provider state rather than trusting a notification as a complete event. [G11]

Calendar supports version checks through etags and If-Match. A stale modification can fail with 412, allowing the application to fetch and review changed state. This helps prevent overwriting an appointment edited from another client. [G12]

Calendar has date-only all-day events, timed events and recurring instances. It uses IANA timezone identifiers. An instance's original start helps identify it even after it moves. Appointments cannot be represented safely by an unqualified local date/time string or a fixed UTC offset alone. [G13][G14]

Calendar's error documentation distinguishes retryable quota/backend conditions from authorization, duplicate-ID and stale-version problems. A generic retry-everything handler would be incorrect. [G15]

## Proposed booking commit and recovery contract

Public slot display is advisory until commit. One server operation recomputes the requested interval, checks booking rules and fresh conflict data, then reserves the host interval durably. Use an overlap constraint or serialized host operation in the selected database. Every client route, including manual and assistant-assisted booking, calls that operation.

Record a durable provider-create job in the same local transaction as the reservation. The job uses one previously assigned provider event ID and saves its result. If Google creation is uncertain, retain the pending reservation and bound the automatic retry/review period. Expiry must escalate for reconciliation, not silently release capacity while a provider event might exist. A Calendar 404 can also mean lost access, so it is not automatically proof of absence. Never silently turn provider failure into a confirmed local-only appointment. The public page may show pending confirmation with a reference and a support path. [G15]

Only the local database is transactional with itself. Google and the application do not offer a shared transaction or a global lock against every other calendar writer. We can prevent two visitors to this application from winning the same slot. We cannot promise that another person or app will never insert an overlapping Google event at the same moment. Recheck and reconcile, surface an external conflict, and require a deliberate resolution. Do not delete someone else's event to hide a race.

For a confirmed booking, keep one appointment identity and a separate version. Rescheduling changes the version, preserves history, updates Google with a version check and invalidates previous reminder jobs. Hold the old confirmed interval while reserving the proposed interval. Serialize external operations per appointment, and prevent stale jobs from undoing a later requested change. Release an interval only after its relevant provider outcome is reconciled. If the update fails, display the actual confirmed provider time and the pending requested change. Canceling follows the same explicit result handling. Do not announce a new time as confirmed while the provider still has the old time.

Selected external calendars contribute busy intervals only. App-created Google events map back to their CRM appointment so external edits and cancellations can update it. Unknown Google attendees do not become CRM contacts automatically. Existing recurring busy events must block correctly even though creating recurring appointment series is deferred.

## Small verification set for the build task

1. Gmail import pages repeat and arrive out of order, and a new message arrives during initial paging. One provider message remains, the cursor advances only after persistence and replay, and a crash or concurrent worker loses no later message.
2. Reply from CRM, then Gmail, then reconnect. Both replies stay in the original provider thread. Explicitly include alias and multiple-recipient cases in the supported/deferred behavior.
3. Gmail accepts a send but the response is lost. Recovery shows uncertain until reconciliation and never blindly emits a second copy.
4. Gmail history 404 and Calendar sync 410 rebuild caches while contacts, notes and action history survive.
5. Two simultaneous app booking requests for overlapping intervals yield only one confirmed appointment. Repeating either request does not create another provider event.
6. A selected conflict calendar returns an embedded error, the provider is unavailable, or token renewal fails. Public booking does not treat this as free time.
7. A concurrent external Google event appears. Reconciliation exposes the conflict without falsely asserting global exclusion.
8. Reschedule/cancel occurs before a reminder runs. Old-version reminders cannot execute; a failed provider update remains visible.
9. Test Vancouver and another IANA zone on dates around each zone's transitions using current timezone data. Include date-only closing dates, timed tasks and all-day busy intervals. Do not hard-code a daylight-saving policy from memory.
10. Revoking access or disabling automation prevents new dispatches and invalidates queued jobs through a checked connection/automation generation. An already accepted or in-flight provider request cannot be recalled by a pause switch; record its late outcome and reconcile it. Repeated webhook hints cannot recreate stopped jobs or bypass authorization.

## Resource register

All were accessed 2026-09-08. Dates are the current page when visible; recheck API details during implementation.

| ID | Direct resource | Supports |
|---|---|---|
| G1 | [Synchronize clients with Gmail](https://developers.google.com/workspace/gmail/api/guides/sync) | Initial and partial sync, history retention, 404 recovery. Updated 2026-07-22. |
| G2 | [Configure Gmail push notifications](https://developers.google.com/workspace/gmail/api/guides/push) | Pub/Sub, payload, renewal, dropped notifications and device polling. Updated 2026-07-22. |
| G3 | [Manage Gmail threads](https://developers.google.com/workspace/gmail/api/guides/threads) | Provider threading requirements. |
| G4 | [Gmail messages.send](https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.messages/send) | Recipient headers, Message result and documented request contract. Updated 2026-04-15. |
| G5 | [Resolve Gmail errors](https://developers.google.com/workspace/gmail/api/guides/handle-errors) | Credential, quota, send-result and retry caveats. |
| G6 | [Gmail messages.list](https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.messages/list) | Pagination and RFC message ID search. |
| G7 | [Search and filter Gmail messages](https://developers.google.com/workspace/gmail/api/guides/filtering) | API versus UI alias/search differences. |
| G8 | [Calendar FreeBusy query](https://developers.google.com/workspace/calendar/api/v3/reference/freebusy/query) | Busy intervals and per-calendar errors. Updated 2026-05-12. |
| G9 | [Calendar events.insert](https://developers.google.com/workspace/calendar/api/v3/reference/events/insert) | Event identity, creation contract, guest notifications and accepted scopes. |
| G10 | [Synchronize Calendar resources](https://developers.google.com/workspace/calendar/api/guides/sync) | Tokens, pagination, query restrictions and 410 recovery. Updated 2026-08-27. |
| G11 | [Calendar push notifications](https://developers.google.com/workspace/calendar/api/guides/push) | Watch channels, renewal overlap and missed notifications. Updated 2026-08-27. |
| G12 | [Calendar resource versions](https://developers.google.com/workspace/calendar/api/guides/version-resources) | Etags, If-Match and 412 stale-write handling. |
| G13 | [Calendars and events](https://developers.google.com/workspace/calendar/api/concepts/events-calendars) | IANA zones, all-day/recurring event semantics. Updated 2026-08-27. |
| G14 | [Calendar Events resource](https://developers.google.com/workspace/calendar/api/v3/reference/events) | Event fields, recurrence-instance identity and date versus dateTime. |
| G15 | [Handle Calendar API errors](https://developers.google.com/workspace/calendar/api/guides/errors) | Error categories and recovery distinctions. |
| G16 | [Calendar events.list](https://developers.google.com/workspace/calendar/api/v3/reference/events/list) | Filters incompatible with syncToken and incremental query contract. |

The attempted `/calendar/api/guides/conditional-modification` URL returned no usable page. G12 is the verified replacement. Search results for example code and client libraries were discovery aids; no downloaded Google sample was executed or copied.
