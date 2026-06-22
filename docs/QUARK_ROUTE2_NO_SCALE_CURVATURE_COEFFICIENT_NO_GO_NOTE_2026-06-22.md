# Quark Route-2 No-Scale Curvature Coefficient No-Go

**Date:** 2026-06-22
**Type:** exact negative boundary / no-go
**Claim type:** no_go
**Actual current-surface status:** no-go
**Status authority:** independent audit lane only. This source note does not
set, predict, or apply an audit verdict.
**Primary runner:** [scripts/frontier_quark_route2_no_scale_curvature_coefficient_no_go_2026_06_22.py](../scripts/frontier_quark_route2_no_scale_curvature_coefficient_no_go_2026_06_22.py)
**Runner output:** [outputs/frontier_quark_route2_no_scale_curvature_coefficient_no_go_2026_06_22.txt](../outputs/frontier_quark_route2_no_scale_curvature_coefficient_no_go_2026_06_22.txt)

## Scope

Block111 narrowed the Route-2 source/readout primitive to:

```text
log-action cocycle
+ affine-gauge-invariant lowest-order local curvature response in w
+ constant source unit / no weight-dependent prefactor.
```

This block attacks the last clause. It asks whether the current weak premises
exclude a coefficient prefactor

```text
R_g(w) = g(w) Phi''(w)
```

after the Hessian row has already been selected by affine gauge.

They do not. Affine gauge kills value and first-derivative rows, but every
smooth coefficient `g(w)` multiplying `Phi''(w)` is still affine-gauge
invariant. Positivity and channel-uniform functional form also do not force
`g` to be constant.

The exact positive support is equally sharp: if a future theorem proves the
coefficient itself is no-scale under positive rescaling,

```text
g(a w) = g(w)       for every a > 0 and w > 0,
```

then `g` is constant and the Block110/111 Hessian row gives the endpoint. The
current surface does not derive that coefficient no-scale premise.

## A_min And Forbidden Imports

Allowed in this block:

- the exact Route-2 endpoint algebra and S3 blocker;
- the O_h weights `w_E=1/3`, `w_T=1/2`;
- supplied T-side values `q_T=5/6` and `s_TE=-2` as conditional stretch
  inputs;
- Block111's affine-gauge finite-jet boundary;
- Block100's dilation-covariant Hessian support theorem;
- Block101's positive counterterm no-go;
- exact rational arithmetic over coefficient ratios.

Forbidden proof inputs:

- observed masses;
- fitted endpoint values;
- nearest-rational selection;
- live endpoint measurements;
- literature values;
- assuming `q_E=15/8`, `rho_E=21/4`, or `c_TE=-8/9`;
- assuming from the start that `g(w)` is constant or no-scale.

The target fractions appear only as exact consequences or comparison values.

## One-Hop Authorities

| Authority | Role used here |
| --- | --- |
| [QUARK_ROUTE2_SOURCE_ACTION_PRIMITIVE_BOUNDARY_NOTE_2026-06-22.md](QUARK_ROUTE2_SOURCE_ACTION_PRIMITIVE_BOUNDARY_NOTE_2026-06-22.md) | Direct parent: affine-gauge minimal curvature selects Hessian but leaves `g(w) Phi''(w)` open. |
| [QUARK_ROUTE2_DILATION_COVARIANT_HESSIAN_SOURCE_BOUNDARY_NOTE_2026-06-22.md](QUARK_ROUTE2_DILATION_COVARIANT_HESSIAN_SOURCE_BOUNDARY_NOTE_2026-06-22.md) | Positive support: scale covariance of the Hessian coefficient gives inverse-square law. |
| [QUARK_ROUTE2_HESSIAN_COUNTERTERM_EXCLUSION_BOUNDARY_NOTE_2026-06-22.md](QUARK_ROUTE2_HESSIAN_COUNTERTERM_EXCLUSION_BOUNDARY_NOTE_2026-06-22.md) | Prior no-go: positivity does not exclude Hessian counterterms. |
| [QUARK_ROUTE2_LOG_ACTION_COCYCLE_HESSIAN_BOUNDARY_NOTE_2026-06-22.md](QUARK_ROUTE2_LOG_ACTION_COCYCLE_HESSIAN_BOUNDARY_NOTE_2026-06-22.md) | Parent endpoint support under log-action plus Hessian row. |
| [S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md) | Downstream open gate and endpoint-triple blocker. |
| [QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md) | Restricted readout map and missing E-channel map entry. |
| [MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md) | Framework boundary: no coefficient no-scale law or source-unit selector is supplied. |

## Exact Prefactor Compression

For the log-action Hessian representative,

```text
Phi''(w) = C/w^2.
```

Allow a positive coefficient prefactor:

```text
R_g(w) = g(w) C/w^2.
```

Then the Route-2 E/T row ratio is

```text
R_g(E/T) = (g(w_E)/g(w_T)) (w_T/w_E)^2.
```

Using

```text
w_E = 1/3,       w_T = 1/2,
```

this becomes

```text
R_g(E/T) = (9/4) (g_E/g_T).
```

The target endpoint ratio `9/4` is therefore equivalent, inside this prefactor
family, to the exact no-scale two-point condition:

```text
g_E/g_T = 1.
```

This is a compression of the remaining wall, not a derivation of it.

## Counter-Witnesses

The weak premises admit many nonconstant positive prefactors.

### Homogeneous prefactors

For

```text
g_m(w) = w^m,
```

the row degree becomes

```text
d = m - 2.
```

The endpoint is hit only at `m=0`. Other homogeneous, positive,
channel-uniform prefactors miss:

| `m` | `g_E/g_T` | `R_g(E/T)` | `q_E` | `rho_E` | `c_TE` |
| ---: | ---: | ---: | ---: | ---: | ---: |
| `-1` | `3/2` | `27/8` | `45/16` | `87/8` | `-16/27` |
| `0` | `1` | `9/4` | `15/8` | `21/4` | `-8/9` |
| `1` | `2/3` | `3/2` | `5/4` | `3/2` | `-4/3` |
| `2` | `4/9` | `1` | `5/6` | `-1` | `-2` |

Thus affine-gauge Hessian readout plus homogeneous coefficient form still does
not select the no-scale coefficient.

### Smooth two-point-flat prefactors

Endpoint matching is also not a proof of constant `g`. The smooth positive
coefficient

```text
g_flat(w) = 1 + (w - w_E)(w - w_T)
```

is nonconstant, but it satisfies

```text
g_flat(w_E) = g_flat(w_T) = 1.
```

So it hits the E/T endpoint ratio while not being a no-scale coefficient on
the positive ray. The endpoint ratio can test `g_E/g_T`; it cannot prove a
global source-unit theorem by itself.

## No-Scale Support Theorem

If a future physical theorem supplies

```text
g(a w) = g(w)
```

for every `a>0` and `w>0`, then setting `w=1` gives

```text
g(a) = g(1).
```

Renaming `a` to `w` gives

```text
g(w) = g(1),
```

so `g` is constant. Then

```text
R_g(E/T) = 9/4,
q_E = 15/8,
rho_E = 21/4,
c_TE = -8/9.
```

This exactly recovers the Block110 endpoint consequence. It remains a support
theorem, not a current-surface derivation of the Route-2 coefficient law.

## Current-Surface Boundary

The actual current surface remains open.

Block112 proves a scoped no-go:

```text
affine-gauge Hessian readout
+ positivity
+ smooth coefficient
+ channel-uniform functional form
+ homogeneous prefactor family
does not force g(w) to be no-scale.
```

A future positive route must prove one of:

1. the coefficient no-scale law `g(a w)=g(w)`;
2. an equivalent dilation-covariant source-unit theorem;
3. a variational or quotient principle that removes all weight-dependent
   prefactors;
4. a direct E-center theorem deriving `q_E=15/8` without the Hessian chain.

## No-Go Discipline

N1 alternative routes:

| Route | Result |
| --- | --- |
| Affine-gauge Hessian alone | Leaves `g(w) Phi''(w)` open. |
| Positive smooth coefficient | Allows nonconstant prefactors. |
| Homogeneous coefficient `w^m` | Misses endpoint for `m != 0`. |
| Endpoint equality `g_E/g_T=1` | Only a two-point condition; does not prove global no-scale. |
| Full scale invariance `g(a w)=g(w)` | Sufficient for constant `g`, but not derived. |

N2 wall independence:

The no-scale coefficient wall is independent of endpoint arithmetic,
affine-gauge derivative-order selection, and the log functional equation.
Those tell us what would work, not why `g` must be constant.

N3 hidden-wall scan:

No observed masses, fitted endpoint values, nearest-rational selector,
literature value, or live endpoint measurement is used.

N4 residual matching:

The residual matches the S3/Route-2 blocker: the E-channel map entry remains
unselected because the physical source/readout primitive remains underived.

N5 rhetoric audit:

"No-scale coefficient" names a future theorem premise. It is not asserted as
current Route-2 framework content.

## Validation

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_no_scale_curvature_coefficient_no_go_2026_06_22.py
```

Expected final line:

```text
TOTAL: PASS=59, FAIL=0
```
