# Assumptions And Imports

## Current-Surface Premises Used

- The affected files are under `archive_unlanded/`.
- Each primary Shapiro note already has an audit-failed retraction banner.
- The current audit ledger identifies the rows as `audited_failed` /
  `retained_no_go`.

## Imports Not Retired Here

- Causal phase-lag derivation.
- Diamond/NV phase-ramp and absolute-unit bridge inputs.
- Complex-action selector construction on the same surface as the phase lag.
- Raw recomputation of source-strength, impact-parameter, and drive-scale
  Shapiro sweeps.

## Import Discipline

No textbook/literature import is used. No new axiom is introduced. The PR only
narrows archived prose and adds a guard script.
