# Review History

## 2026-05-27

- Read the active audited conditional row for `assumption_derivation_ledger`.
- Confirmed its only direct dependency is `rconn_derived_note`.
- Confirmed `rconn_derived_note` is audit-clean only for the narrowed no-go:
  exact `F_adj = 8/9` remains support, while physical `R_conn`/`K_EW=9/8`
  requires a selector.
- Repaired the source by narrowing to that exact authority slice.
- Ran the upstream R_conn runner and full audit pipeline.
