# Assumptions And Imports

## Allowed premises

- The current `origin/main` parent note and runner for the Higgs lattice
  eigenvalue ratio row.
- Existing companion bridge notes and runners on `origin/main`:
  `HIGGS_LATTICE_TASTE_COUNT_AND_WJ_FORM_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05`
  and `HIGGS_MEAN_FIELD_DETERMINANT_APBC_TASTE_BRIDGE_NOTE_2026-06-06`.
- Runner-cache freshness is checked by SHA against the current runner source.

## Retired hidden imports

- The parent runner no longer relies on the bridge packet being known by repo
  context alone. It now checks the parent note links, source markers, source
  sizes, cache runner names, runner SHAs, clean exits, and expected output
  markers for both bridge runners.

## Remaining imports

- Independent audit must decide whether the bridge packet itself is retained
  enough to satisfy the one-hop bridge requirement.
- The PR does not introduce a physical Higgs-mass identification, a numerical
  `u_0`, an observed value, a fitted selector, or a new axiom.
