# Assumptions And Imports

## Used

- The current audit ledger snapshot is read-only input.
- The upstream selector/dial subdivision runner supplies:
  `scoped(row)`, `ladder_bucket(row)`, `selector_subbucket(row)`, and
  `haystack(row)`.
- The upstream selector/dial subdivision bucket
  `stability_or_dynamics_selector` contains 64 rows on this snapshot.
- Keyword rules are dispatch rules only. They do not certify row truth,
  physical selection, or audit status.

## Open Imports

- Row-specific review is still required after keyword dispatch.
- Flow/thermal rows need supplied local maps, flows, thermal principles,
  fixed-point statements, separatrix statements, or stability certificates
  before they can support a stable setting.
- Arrow/dynamics rows need a physical arrow, Hamiltonian, transfer, kernel,
  instrument, decoherence, measurement, clock, or rate bridge before selector
  claims can be calibrated.
- Independent audit remains required before repo-wide status changes.

## Forbidden Imports

- No observed target value is used as a proof input.
- No fitted selector is used as a proof input.
- No generation or Koide value is selected by this block.
- No stable setting is converted into a selected dial.
- No physical arrow is derived from Record.
- No audit verdict is applied or predicted.
