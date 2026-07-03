# Fifth Family Complex Boundary Note

**Date:** 2026-04-06 (originally); 2026-05-03 (review-loop runner repair); 2026-06-09 (sampled-row gate repair)
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

That repaired the import failure but did not compute the Born proxy on every
sampled row. The older note therefore overstated the seed-singleton part of
the boundary: `drift = 0.20`, `seed = 1` also has the `TOWARD -> AWAY`
crossover and had not been given the same Born/F~M gate.

The 2026-06-08 live-source repair also adds an explicit assertion gate to the
runner. The 2026-06-09 sampled-row repair supersedes that seed-singleton
assertion: the runner now computes Born/F~M gates for all six sampled rows and
fails unless the sampled complex-companion set is exactly the drift-0.20 pair
`{(0.20, 0), (0.20, 1)}`.

## Artifact Chain

- [`scripts/FIFTH_FAMILY_COMPLEX_TARGETED.py`](../scripts/FIFTH_FAMILY_COMPLEX_TARGETED.py)
- [`logs/runner-cache/FIFTH_FAMILY_COMPLEX_TARGETED.txt`](../logs/runner-cache/FIFTH_FAMILY_COMPLEX_TARGETED.txt)
- [`logs/2026-04-06-fifth-family-complex-targeted.txt`](../logs/2026-04-06-fifth-family-complex-targeted.txt) (legacy log)
- [`logs/2026-05-03-fifth-family-complex-targeted.txt`](../logs/2026-05-03-fifth-family-complex-targeted.txt) (post-repair log)
- [`archive_unlanded/fifth-family-stale-runners-2026-04-30/FIFTH_FAMILY_COMPLEX_NOTE.md`](../archive_unlanded/fifth-family-stale-runners-2026-04-30/FIFTH_FAMILY_COMPLEX_NOTE.md)

## Boundary Rows

The repaired runner computes the Born proxy, F~M gates, and crossover gate on
every sampled row:

| drift | seed | Born gate | F~M gate | crossover | role |
| --- | ---: | --- | --- | --- | --- |
| 0.05 | 0 | pass | pass | no | outer control; response stays away |
| 0.05 | 1 | pass | pass | no | outer control; response stays toward |
| 0.20 | 0 | pass | pass | yes | sampled complex companion |
| 0.20 | 1 | pass | pass | yes | sampled complex companion; former missing-gate row |
| 0.30 | 0 | pass | pass | no | outer control; response stays away |
| 0.30 | 1 | pass | pass | no | outer control; response stays away |

## Safe Read

- the radial-shell fifth-family slice carries a complex companion on both sampled `drift = 0.20` seeds
- the older seed-singleton claim is not retained by the repaired computation
- the companion is drift-selective on this sampled grid, not family-wide
- the outer sampled rows show a clear response-sign boundary, not a control leak

## Final Verdict

**diagnosed drift-selectivity boundary**
