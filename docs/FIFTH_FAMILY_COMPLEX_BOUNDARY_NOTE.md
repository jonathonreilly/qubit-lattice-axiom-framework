# Fifth Family Complex Boundary Note

**Date:** 2026-04-06 (originally); 2026-05-03 (review-loop runner repair)
**Status:** support - structural or confirmatory support note

**Primary runner:** [`scripts/FIFTH_FAMILY_COMPLEX_TARGETED.py`](../scripts/FIFTH_FAMILY_COMPLEX_TARGETED.py)

## Review-loop repair (2026-05-03)

The 2026-05-03 audit flagged the runner as failing at import. Root cause:
[`scripts/FIFTH_FAMILY_COMPLEX_TARGETED.py`](../scripts/FIFTH_FAMILY_COMPLEX_TARGETED.py)
imported `_field_from_sources` (and the helper constants) from
`CONNECTIVITY_FAMILY_V2_QUADRANT_SWEEP`, but that module re-exports its
peer module via `from CONNECTIVITY_FAMILY_V2_ELLIPTICAL_SWEEP import *`,
and `import *` does **not** propagate underscore-prefixed names. The
repair points the import directly at `CONNECTIVITY_FAMILY_V2_ELLIPTICAL_SWEEP`,
which is where `_field_from_sources` is actually defined.

Fresh runner log:
[`logs/2026-05-03-fifth-family-complex-targeted.txt`](../logs/2026-05-03-fifth-family-complex-targeted.txt)

The fresh log confirms every boundary-row statement in this note: exactly one
anchor row passes the Born/F~M gates and the `TOWARD -> AWAY` crossover gate:
`drift = 0.20`, `seed = 0`. The runner prints sampled outer rows as controls;
they are not promoted to a family-wide companion claim.

The 2026-06-08 live-source repair also adds an explicit assertion gate to the
runner: it now fails unless the anchor and companion row set is exactly
`{(0.20, 0)}` and the Born/F~M thresholds hold.

## Artifact Chain

- [`scripts/FIFTH_FAMILY_COMPLEX_TARGETED.py`](../scripts/FIFTH_FAMILY_COMPLEX_TARGETED.py)
- [`logs/2026-04-06-fifth-family-complex-targeted.txt`](../logs/2026-04-06-fifth-family-complex-targeted.txt) (legacy log)
- [`logs/2026-05-03-fifth-family-complex-targeted.txt`](../logs/2026-05-03-fifth-family-complex-targeted.txt) (post-repair log)
- [`archive_unlanded/fifth-family-stale-runners-2026-04-30/FIFTH_FAMILY_COMPLEX_NOTE.md`](../archive_unlanded/fifth-family-stale-runners-2026-04-30/FIFTH_FAMILY_COMPLEX_NOTE.md)

## Boundary Rows

The sampled outer rows do not retain the same directional companion cleanly:

- `drift = 0.05`, `seed = 0`
  - exact controls remain clean
  - `gamma = 0` is already negative in the detector shift
  - `TOWARD -> AWAY` does not appear
- `drift = 0.30`, `seed = 1`
  - exact controls remain clean
  - the response stays on the same side of the crossover
  - `TOWARD -> AWAY` does not appear

## Safe Read

- the radial-shell fifth-family slice really does carry a complex companion on the anchor row
- the companion is selective, not family-wide
- the outer sampled rows show a clear response-sign boundary, not a control leak

## Final Verdict

**diagnosed selectivity boundary**
