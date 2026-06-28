# Code-Review Tiebreaker — Pre-Registration (Hard Set C6–C10)

**Prepared:** 2026-06-27
**Status:** FROZEN before any model output
**Why:** In the main eval, the code-review class (C1–C5) ceilinged — all three arms found 15/15 planted
defects, so it couldn't discriminate. Those snippets tested *competence* (SQL injection, hardcoded
key, XSS). This set tests *expertise*: plausible-looking code whose defects strong models genuinely
diverge on. Same scoring as before — planted-defect recall, false positives, and a false-positive trap.

Snippets live in `eval-assets/code/c6–c10`; run via `run_eval.py --items-file items_hard.json`.

---

## C6 — `c6_webhook_verify.py` (Python, security)
**Planted (2):**
- (a) **Signature verified over `json.dumps(payload)`, not the raw `body`.** Re-serializing the parsed
  JSON changes bytes (key order, whitespace, unicode escaping) — legitimate signatures won't match,
  and an attacker can craft a different raw body that re-serializes identically (signature confusion).
- (b) **`received == expected` is not constant-time** → timing side-channel on the signature.

**Trap:** the `try/except ValueError: return False` on malformed JSON is correct, defensive code — not
an error-swallowing bug.

## C7 — `c7_rate_limit.py` (Python, correctness + efficiency)
**Planted (2):**
- (a) **Boundary off-by-one: `history[0] < cutoff`** keeps an entry exactly `window` seconds old
  (should be `<=`), letting `limit + 1` requests through at the window edge.
- (b) **`history.pop(0)` in a loop is O(n)** → O(n²) under load on a hot path (use a deque).

**Trap:** mutating `history` in place is documented and intentional — not a hidden side-effect bug.

## C8 — `c8_proxy.js` (Node, security)
**Planted (2):**
- (a) **Allow-list bypass: `u.hostname.endsWith(host)`** matches `evilapi.partner.com` (and any
  `*api.partner.com` an attacker can register) — needs an exact or leading-dot match.
- (b) **No request timeout** on `https.get` → a slow/malicious allowed host hangs the call forever
  (resource exhaustion / DoS).

**Trap:** the hand-rolled Promise wrapper around the callback API is clunky but correct.

## C9 — `c9_invoice.py` (Python, money / domain)
**Planted (2):**
- (a) **`split_total` loses or gains pennies:** `[share] * n` doesn't sum back to `total` — the
  remainder cents aren't distributed (classic allocation bug; uses `Decimal`, so "don't use float"
  is *not* the finding).
- (b) **`line_tax` rounds each line then sums** instead of summing then rounding — off-by-a-cent vs a
  single tax computation, an order-of-rounding error that matters for invoicing/compliance.

**Trap:** `ROUND_HALF_UP` is a deliberate, correct currency choice — not a rounding-mode bug.

## C10 — `c10_cache.py` (Python, concurrency)
**Planted (2):**
- (a) **`async with asyncio.Lock()` creates a new lock every call** → it never serializes; concurrent
  misses all run `fetch()` (cache stampede / thundering herd). Looks like locking; isn't.
- (b) **No re-check inside the lock** — even with a shared lock, waiters don't re-read the cache after
  acquiring, so the first N all re-fetch (double-checked-locking missing the second check).

**Trap:** `time.monotonic()` for expiry is the correct clock choice — not a `time.time()` bug.

---

## Scoring (unchanged from the main pre-registration)
Per (item, arm): recall = planted found ÷ 2; trap_flagged (bad); extra false positives (judge
conservatively — legitimate nits don't count). Discrimination expected: these are subtle enough that a
single pass may miss one, so the arms can separate. Same n caveat (5 items) — signal, not proof.
