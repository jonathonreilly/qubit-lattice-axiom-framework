# Edge Deletion Boundary: TOWARD Stability on the 3D Valley-Linear Family

**Date:** 2026-04-04 (table refreshed 2026-05-23)
**Status:** bounded - bounded or caveated result note
**Primary runner:** `scripts/edge_deletion_boundary_sweep.py`

## Scope

Bounded edge-retention sweep on the tested 3D valley-linear lattice family with
`h=0.5`, `W=8`, `L=12`, `max_d=3`, keep fractions `1.00, 0.95, 0.90, 0.85, 0.80, 0.75`,
and seeds `20260404..20260415` (12 seeds). One representative `100%` and `80%` Born /
`k=0` / no-field control per row.

## Result

| Keep fraction | TOWARD | Mean delta | Std delta |
|---:|---:|---:|---:|
| 1.00 | 12/12 (100%) | +3.473338e-05 | 6.776264e-21 |
| 0.95 | 12/12 (100%) | +4.884894e-05 | 1.693359e-05 |
| 0.90 | 12/12 (100%) | +5.446079e-05 | 2.384982e-05 |
| 0.85 | 12/12 (100%) | +5.815760e-05 | 2.112014e-05 |
| 0.80 | 12/12 (100%) | +7.655170e-05 | 2.621961e-05 |
| 0.75 | 12/12 (100%) | +6.004755e-05 | 2.016072e-05 |

Representative controls (seed `20260404`):

- `100%`: Born `2.35e-15`, `k=0` delta `+0.000e+00`, no-field delta `+0.000e+00`
- `80%`:  Born `2.42e-15`, `k=0` delta `+0.000e+00`, no-field delta `+0.000e+00`

## Honest read

On this family, in this swept retention range, the gravity sign stays TOWARD at
every tested keep fraction and every tested seed. The mean delta stays positive
across `1.00 -> 0.75` retention and does not flip in this range.

## Correction of earlier framing

An earlier version of this note reported a sign flip between 90% and 80%
retention, an 80% coin-flip row, and AWAY-dominated behavior below ~85%. The
current completed sweep does **not** reproduce any of those features: the
runner shows TOWARD 12/12 with positive mean delta at every listed keep
fraction from 1.00 down to 0.75. The sign-flip / coin-flip / AWAY-dominated
language has been removed and is not supported by this runner.

## Safe wording

"On the tested 3D ordered-lattice family with valley-linear action, the
gravity sign stays TOWARD across the swept retention range `1.00 -> 0.75`
on 12 seeds. This run does not exhibit a sign-flip boundary in that range
and is not a universal graph theorem; harsher damage regimes, other families,
or other observables are not addressed."
