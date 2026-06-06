# Assumptions And Imports

## Allowed Repo Inputs

- `docs/audit/data/audit_ledger.json` as read-only input.
- `docs/POST_RECORD_AUDIT_EVIDENCE_LADDER_ROW_BUCKETING_2026-06-06.md`.
- `docs/POST_RECORD_CONDITIONAL_AUDIT_EVIDENCE_LADDER_2026-06-06.md`.
- `docs/RECORD_TYPING_AUDIT_UNLOCK_MAP_2026-06-05.md`.
- `docs/RECORD_HISTORY_COUNT_AUDIT_UNLOCK_SCAN_2026-06-05.md`.

## Imports Retired

- Retires the stale exact-ledger-total guard `len(rows) == 2825`.
- Retires the stale assumption that append/count or record-type buckets must be nonempty after the latest post-Record evidence ladder row renaming.

## Load-Bearing Premises

- The runner reads but does not write `docs/audit/data/audit_ledger.json`.
- Each scoped row must land in exactly one known bucket.
- Touched post-Record ladder buckets remain nonempty where the current classifier has live evidence categories.

## Still Not Claimed

- No audit verdict is applied.
- No row status is predicted or promoted.
- No probability, concentration, simulation calibration, production dynamics, selector, or dial is derived from Record.
