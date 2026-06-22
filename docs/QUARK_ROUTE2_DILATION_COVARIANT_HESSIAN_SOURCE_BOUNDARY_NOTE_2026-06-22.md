# Quark Route-2 Dilation-Covariant Hessian Source Boundary

**Date:** 2026-06-22
**Type:** open gate / exact support
**Claim type:** open_gate
**Actual current-surface status:** exact-support
**Status authority:** independent audit lane only. This source note does not
set, predict, or apply an audit verdict.
**Primary runner:** [scripts/frontier_quark_route2_dilation_covariant_hessian_source_boundary_2026_06_22.py](../scripts/frontier_quark_route2_dilation_covariant_hessian_source_boundary_2026_06_22.py)
**Runner output:** [outputs/frontier_quark_route2_dilation_covariant_hessian_source_boundary_2026_06_22.txt](../outputs/frontier_quark_route2_dilation_covariant_hessian_source_boundary_2026_06_22.txt)

## Scope

This block attacks the remaining Route-2/S3 readout endpoint primitive from
the source-functional side. The direct consumer remains
[S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md),
whose blocker is that the readout-map endpoint triple

```text
(beta_T/alpha_T, alpha_T/alpha_E, beta_E/alpha_E)
  = (-1, -2, 21/4)
```

is not derived.

Block99 isolated the exact sufficient primitive:

```text
q_X w_X^2 = 5/24
```

on the Route-2 E/T center-lift channels, with seven-site star weights
`w_E = 1/3` and `w_T = 1/2`. This note proves the next exact reduction:

```text
A separable Hessian source density H(w) is dilation-covariant
with weight -2, H(a w) = a^-2 H(w),
iff H(w) = C / w^2.
```

Therefore, if the Route-2 E/T source/readout primitive is a positive
separable Hessian density on the channel weights and is covariant under
positive rescaling of those weights, then the inverse-square center-lift law
follows exactly.

This note does not derive that dilation-covariant Hessian premise on the
actual current surface. It records exact support and the remaining boundary.

## One-Hop Authorities

| Authority | Role used here |
| --- | --- |
| [QUARK_ROUTE2_TYPED_METRIC_SOURCE_INVERSE_SQUARE_BOUNDARY_NOTE_2026-06-22.md](QUARK_ROUTE2_TYPED_METRIC_SOURCE_INVERSE_SQUARE_BOUNDARY_NOTE_2026-06-22.md) | Direct upstream Block99 packet: inverse-square center-lift law suffices for the endpoint triple. |
| [S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md) | Direct downstream consumer and source of the endpoint-triple blocker. |
| [QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md) | Restricted readout map, endpoint algebra, and missing E-channel map entry. |
| [OH_SEVEN_SITE_STAR_SHELL_LEVERAGE_POSITIVE_THEOREM_NOTE_2026-06-10.md](OH_SEVEN_SITE_STAR_SHELL_LEVERAGE_POSITIVE_THEOREM_NOTE_2026-06-10.md) | Exact weights `w_E = 1/3`, `w_T = 1/2`, and kappa `3/2`. |
| [QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md](QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md) | Current Schur/quadratic no-go and inverse-square characterization. |
| [QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md](QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md) | Current typed source-domain bridge boundary. |
| [MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md) | Minimal Lattice/Quantum/Record boundary; Record supplies no weighting, normalization, probability, dynamics, or readout context. |

## Exact Dilation-Covariant Hessian Theorem

Let `H(w)` be the positive Hessian coefficient used by a separable
source-functional channel at positive channel weight `w`.

Assume the source coefficient is covariant under positive rescaling of the
weight coordinate:

```text
H(a w) = a^-2 H(w)       for every a > 0 and w > 0.
```

Setting `w = 1` gives:

```text
H(a) = a^-2 H(1).
```

Renaming `a` to `w` gives:

```text
H(w) = C / w^2,     C := H(1).
```

Conversely, every `H(w) = C/w^2` satisfies the covariance law exactly:

```text
H(a w) = C/(a w)^2 = a^-2 H(w).
```

Thus the inverse-square Hessian density is equivalent to the dilation
covariance premise.

When `H` is the second derivative of a separable potential `Phi`, this is the
log-barrier potential up to affine terms:

```text
Phi''(w) = C/w^2
=> Phi(w) = -C log(w) + A w + B.
```

The affine terms do not change the Hessian. The load-bearing content is the
scale-covariant Hessian density, not the name "log barrier".

## Endpoint Consequence

Normalize the source lift by the T channel:

```text
q_X = q_T H(w_X)/H(w_T).
```

Using the Route-2 T-side value from the endpoint algebra,

```text
q_T = 5/6,
w_T = 1/2,
w_E = 1/3,
```

the dilation-covariant Hessian gives

```text
H(w_E)/H(w_T) = (w_T/w_E)^2 = (3/2)^2 = 9/4.
```

So

```text
q_E = (5/6)(9/4) = 15/8,
rho_E = 6(q_E - 1) = 21/4.
```

With `alpha_T/alpha_E = -2`, the center ratio is

```text
c_TE = (-2)(5/6)/(15/8) = -8/9.
```

This exactly recovers the endpoint triple:

```text
(-1, -2, 21/4).
```

## Counterterm And Coordinate Boundary

The covariance premise is not supplied by current named surfaces.

First, convex counterterms preserve positivity but break the needed
covariance. For example,

```text
H_epsilon(w) = C/w^2 + epsilon
```

is positive for `C > 0` and `epsilon >= 0`. It gives the target only at
`epsilon = 0`. With `C = 1` and `epsilon = 1`,

```text
H(1/3)/H(1/2) = (9 + 1)/(4 + 1) = 2,
q_E = (5/6)(2) = 5/3,
rho_E = 4,
```

not `21/4`. Thus positivity, convexity, and a finite two-channel Hessian
reading do not force the endpoint.

Second, the Hessian is coordinate-sensitive. The same log expression gives
an inverse-square second derivative in the `w` coordinate, but a different
second-derivative statement in `u = log(w)`. A positive route must prove that
Route-2 channel weights are the physical Hessian coordinates, or provide an
equivalent invariant rule that reduces to `H(w) proportional to w^-2`.

## Current-Surface Boundary

The current surfaces do not derive the dilation-covariant Hessian premise:

- Minimal Record supplies finite scalar additivity in a supplied readout
  context, but no readout context, sector-generation rule, weighting,
  normalization, probability, dynamics, time metric, or within-sector data.
- The O_h seven-site theorem supplies exact weights and `kappa = 3/2`, but
  does not supply a source-functional Hessian.
- The Schur/quadratic no-go records that equivariant quadratic forms leave
  the E:T ratio free and that no named functional supplies the
  inverse-square center lift.
- The source-domain bridge no-go records that current typed source edges do
  not connect the known source/color quantities to the Route-2 center ratio.
- Block99 shows the inverse-square law is sufficient, but not derived.

Therefore the honest current status is exact support/open boundary. The next
closure theorem must prove one of:

1. Route-2 E/T channel weights are the physical positive coordinates of a
   dilation-covariant separable Hessian source density;
2. an equivalent invariant source/readout rule forces `H(w_E)/H(w_T)=9/4`;
3. a direct E-center theorem derives `q_E=15/8` or `rho_E=21/4` without
   importing the endpoint target.

## No-Go Discipline

N1 alternative routes:

| Route | Result |
| --- | --- |
| Constant Hessian | Gives `H_E/H_T = 1`, not `9/4`. |
| Linear or direct-weight Hessian | Gives `2/3`, not `9/4`. |
| Quadratic-weight Hessian | Gives `4/9`, not `9/4`. |
| Single inverse Hessian | Gives `3/2`, not `9/4`. |
| Dilation-covariant Hessian density | Gives `9/4`, but this premise is not supplied by the current surface. |
| Positive counterterm `C/w^2 + epsilon` | Misses the endpoint for `epsilon != 0`. |
| Coordinate reparametrization without a bridge | Does not select the physical Hessian coordinate. |

N2 wall independence:

The dilation-covariant Hessian premise is independent of T-side row
selection, shell normalization, O_h equivariance, Record finite additivity,
and endpoint algebra. Closing any one of those does not derive
`H(a w)=a^-2 H(w)`.

N3 hidden-wall scan:

The exact endpoint fractions are used as symbolic comparison targets in the
readout algebra. No observed masses, fitted endpoint values, nearest-rational
selector, or literature value is used.

N4 residual matching:

The residual matches the exact blocker in the S3 time note: the readout-map
endpoint triple is not yet derived. This note moves the source-functional
route by reducing the missing inverse-square primitive to a scale-covariant
Hessian premise.

N5 rhetoric audit:

"Dilation-covariant Hessian" names a future theorem target. It is not
asserted as current framework content.

N6 partial-closure path:

Any later proof that the Route-2 E/T source density is a positive
dilation-covariant Hessian in the channel-weight coordinate can use this note
and Block99 to derive the endpoint triple exactly.

## Validation

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_dilation_covariant_hessian_source_boundary_2026_06_22.py
```

Expected final line:

```text
TOTAL: PASS=36, FAIL=0
```
