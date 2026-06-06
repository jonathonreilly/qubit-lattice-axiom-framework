# Assumptions And Imports

- No new axiom is introduced.
- The current audit ledger is read as input only.
- The classifier is unchanged; only stale snapshot expectations are repaired.
- The current source surface has 2920 ledger rows, 1357 bounded/conditional
  scoped rows, and 280 ladder-touched rows.
- The current classifier has zero rows in `append_count_ready` and
  `record_type_support_only`; the branch records that honestly instead of
  requiring a nonempty bucket.
