# Assumptions And Imports

## Used

- The stacked row-bucketing companion in PR #2835.
- Current audit ledger read-only.
- Conservative keyword sub-bucketing over selector/dial rows.

## Not imported

- No audit verdict authority.
- No audit data writes.
- No row promotion.
- No forced generation/Koide dial value.
- No measure, prior, normalization, or Born bridge from Record.

## Important limitation

Sub-buckets are dispatch hints, not final judgments. Any individual row still
needs source-specific review before audit-loop action.
