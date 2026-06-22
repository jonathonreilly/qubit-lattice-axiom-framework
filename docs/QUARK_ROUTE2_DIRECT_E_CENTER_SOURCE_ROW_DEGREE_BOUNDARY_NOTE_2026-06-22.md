# Quark Route-2 Direct E-Center Source-Row Degree Boundary

**Date:** 2026-06-22
**Type:** open gate / exact support
**Claim type:** open_gate
**Actual current-surface status:** exact-support
**Status authority:** independent audit lane only. This source note does not
set, predict, or apply an audit verdict.
**Primary runner:** [scripts/frontier_quark_route2_direct_e_center_source_row_degree_boundary_2026_06_22.py](../scripts/frontier_quark_route2_direct_e_center_source_row_degree_boundary_2026_06_22.py)
**Runner output:** [outputs/frontier_quark_route2_direct_e_center_source_row_degree_boundary_2026_06_22.txt](../outputs/frontier_quark_route2_direct_e_center_source_row_degree_boundary_2026_06_22.txt)

## Scope

This block attacks the direct E-center/source-readout row target from the
row side rather than from the Hessian-coordinate side.

The parent `S3`/Route-2 gate reduces the endpoint obstruction to

```text
(beta_T/alpha_T, alpha_T/alpha_E, beta_E/alpha_E)
  = (-1, -2, 21/4).
```

After the T-side candidates are supplied, the remaining entry is

```text
rho_E := beta_E/alpha_E = 21/4,
q_E = 1 + rho_E/6 = 15/8.
```

Prior no-go notes show that endpoint-only naturality, E-center-blind
constraints, registration/positivity, and the measured finite-box calibration
do not derive the missing value. Block104 gives a sufficient Hessian-coordinate
route: a homogeneous physical coordinate pulls a no-scale Hessian back to an
inverse-square law. This note records the same algebraic target from the row side:

```text
homogeneous direct source row with degree d=-2
  <=> q_E/q_T = 9/4
  <=> q_E = 15/8
  <=> rho_E = 21/4
  <=> c_TE = -8/9
```

under the supplied T-side values. The useful new boundary is uniqueness:
inside the homogeneous source-row class over the cited O_h weights
`w_E=1/3`, `w_T=1/2`, the target endpoint is obtained exactly at homogeneous
source-row degree `d=-2`, and the scanned neighboring degrees fail.

The current surface still does not derive `d=-2`. A direct row theorem must therefore derive the degree, not merely choose it.

In short: the homogeneous source-row degree `d=-2` is the exact row-side
fingerprint of the endpoint target, but the current branch only isolates it.

## One-Hop Authorities

| Authority | Role used here |
| --- | --- |
| [S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md) | Downstream open gate and endpoint-triple blocker. |
| [QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md) | Restricted readout map, endpoint columns, and smallest missing E-map entry. |
| [QUARK_ROUTE2_E_CENTER_LIFT_DERIVATION_ATTEMPT_BOUNDED_NOTE_2026-06-12.md](QUARK_ROUTE2_E_CENTER_LIFT_DERIVATION_ATTEMPT_BOUNDED_NOTE_2026-06-12.md) | Current-bank derivation attempt and named obstruction. |
| [QUARK_ROUTE2_E_CENTER_BLINDNESS_NO_GO_NOTE_2026-06-17.md](QUARK_ROUTE2_E_CENTER_BLINDNESS_NO_GO_NOTE_2026-06-17.md) | Shows E-center-blind repairs cannot derive the value; positive repair must see E-center. |
| [QUARK_ROUTE2_POWER_LAW_COORDINATE_BRIDGE_BOUNDARY_NOTE_2026-06-22.md](QUARK_ROUTE2_POWER_LAW_COORDINATE_BRIDGE_BOUNDARY_NOTE_2026-06-22.md) | Coordinate-side support theorem that also lands on the inverse-square degree. |
| [MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md) | Axiom boundary: no readout context, source-row degree, weighting rule, or selector is supplied. |

## Direct Homogeneous Source-Row Class

Let `w` denote the cited O_h projector-weight coordinate used by the
Route-2 source/readout support line. The relevant channel weights are

```text
w_E = 1/3,
w_T = 1/2.
```

Consider a direct E-center source-row response whose relative channel lift is
homogeneous of degree `d` in this weight coordinate:

```text
R_d(E/T) = (w_E/w_T)^d.
```

This is not a new physical premise. It is a row-side test class: if a direct
source theorem claims to derive the endpoint by a homogeneous weight law, this
is the exact degree it must supply.

Since

```text
w_E/w_T = (1/3)/(1/2) = 2/3,
```

the degree `d=-2` gives

```text
R_{-2}(E/T) = (2/3)^(-2) = (3/2)^2 = 9/4.
```

With the supplied T-side value

```text
q_T = 5/6,
```

the E-center lift becomes

```text
q_E = q_T R_{-2}(E/T)
    = (5/6)(9/4)
    = 15/8.
```

The exact readout-map relation then gives

```text
rho_E = beta_E/alpha_E = 6(q_E - 1) = 21/4.
```

Together with the supplied shell ratio `s_TE=-2`, the center ratio is

```text
c_TE = s_TE q_T/q_E
     = (-2)(5/6)/(15/8)
     = -8/9.
```

Thus the homogeneous degree `d=-2` is exactly the direct row-side fingerprint
of the missing endpoint.

## Uniqueness And Falsifiers

For the positive base `w_E/w_T=2/3`, the equation

```text
(2/3)^d = 9/4
```

has the unique real solution `d=-2`, because `9/4=(2/3)^(-2)` and the
positive-base exponential is injective.

The exact integer-degree falsifiers illustrate the boundary:

| Degree `d` | `q_E/q_T` | `q_E` | `rho_E` | `c_TE` with `s_TE=-2` |
| --- | ---: | ---: | ---: | ---: |
| `-2` | `9/4` | `15/8` | `21/4` | `-8/9` |
| `-1` | `3/2` | `5/4` | `3/2` | `-4/3` |
| `0` | `1` | `5/6` | `-1` | `-2` |
| `1` | `2/3` | `5/9` | `-8/3` | `-3` |
| `2` | `4/9` | `10/27` | `-34/9` | `-9/2` |

So this is not a generic "homogeneity gives the target" result. The target
selects the inverse-square degree. A direct row theorem must therefore derive
that degree from current source/readout structure, or supply an equivalent
E-center lift primitive.

## Relationship To Block104

Block104 says that if the physical source coordinate is multiplicatively
homogeneous and the source Hessian is no-scale in that coordinate, the pulled
back response is inverse-square in `w`. This block says the same target from
the direct row side: any homogeneous source-row law must have degree `-2` to
land on `q_E=15/8`.

The two views are compatible but not identical:

- Block104 is a sufficient coordinate/Hessian bridge.
- This block is a direct row-degree boundary and uniqueness test.
- Neither block derives the missing physical source-row degree selector.

## Current-Surface Boundary

The actual current surface remains open.

- The exact endpoint algebra is closed once the degree is supplied.
- The degree `d=-2` is necessary and sufficient inside the homogeneous
  source-row class.
- The minimal axioms do not supply a physical source-row degree selector,
  readout context, weighting rule, or E-center lift primitive.
- The current source bank does not derive `d=-2`.

This block therefore gives exact support and a sharper theorem target, not
closure of the `S3`/Route-2 endpoint blocker.

## No-Go Discipline

N1 alternative routes:

| Route | Result |
| --- | --- |
| Endpoint-only naturality | Prior no-go leaves `rho_E` free. |
| E-center-blind constraints | Prior no-go leaves all E-center lifts invisible. |
| Registration/positivity | Prior no-go fixes norm or bounds, not direction. |
| Measured finite-box calibration | Prior scan closes the bulk-limit hatch for that functional. |
| Coordinate/Hessian bridge | Block104 gives exact support if homogeneous coordinate/no-scale Hessian is derived. |
| Direct homogeneous source row | This note proves degree `-2` is the exact row-side target. |

N2 wall independence:

The wall is the missing physical degree-selection theorem. The row algebra,
endpoint arithmetic, and O_h weights are not the wall.

N3 hidden-wall scan:

No observed masses, fitted endpoint values, nearest-rational selector,
literature value, or live endpoint measurement is used. The target rationals appear only as exact comparison values inside the theorem target.

N4 residual matching:

This matches the parent residual in `S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md`:
the unresolved entry is still `beta_E/alpha_E=21/4`. The present block says
that a direct homogeneous source-row proof must derive degree `-2`.

N5 rhetoric audit:

The note does not supply a physical source-row degree selector and does not
claim the endpoint triple is derived. It records an exact support/open boundary.

## Validation

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_direct_e_center_source_row_degree_boundary_2026_06_22.py
```

Expected final line:

```text
TOTAL: PASS=37, FAIL=0
```
