# Assumptions And Imports

## Used

- The stacked evidence-ladder interface in PR #2834.
- Current `docs/audit/data/audit_ledger.json` read-only.
- Existing bounded/conditional scope logic from the Record typing unlock map.
- Conservative keyword bucketing over row metadata and source text.

## Not imported

- No audit verdict authority.
- No audit data writes.
- No row promotion.
- No probability or concentration theorem from Record.
- No simulation calibration without a certificate.
- No dial selection.

## Important limitation

The buckets are triage, not final audit judgments. A later reviewer should
inspect any row before using the bucket as dispatch input.
