# Code-review eval inputs (Class 2)

These five snippets are the inputs for the **code review** class of the
[Fugu evaluation](../../PREREG_sakana_fugu_2026-06-27.md). Each has a frozen
**planted defect set** and one **false-positive trap** (see the pre-registration for the keys).

**Run rule — do not leak the key:** feed each arm **only the single snippet's source**, with a
neutral prompt (e.g. *"Review this code for correctness, security, and reliability issues."*).
Never feed the arm the pre-registration doc, this README, the filenames, or the planted-defect
list. The whole point is that the arm finds the defects cold.

| File | Scenario | Planted | Trap |
| --- | --- | --- | --- |
| `c1_async_worker.py` | async batch aggregation | race · swallowed except · off-by-one | `# TODO` over correct code |
| `c2_user_card.tsx` | React profile card | stale-closure effect · XSS · null deref | justified `any` cast |
| `c3_data_layer.py` | SQLite data access | SQL injection · non-atomic transfer · conn leak | correctly parameterized query |
| `c4_setup.sh` | provisioning script | `curl\|bash` · unquoted `rm` var · no `set -euo pipefail` | appropriate `sudo` |
| `c5_api_client.py` | HTTP API client | unbounded retry · hardcoded key · naive `datetime` | broad `except` that re-raises |
