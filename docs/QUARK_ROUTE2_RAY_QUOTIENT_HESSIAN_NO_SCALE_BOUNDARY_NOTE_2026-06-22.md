# Quark Route-2 Ray-Quotient Hessian No-Scale Boundary

**Date:** 2026-06-22
**Type:** open gate / exact support
**Claim type:** open_gate
**Actual current-surface status:** exact-support
**Status authority:** independent audit lane only. This source note does not
set, predict, or apply an audit verdict.
**Primary runner:** [scripts/frontier_quark_route2_ray_quotient_hessian_no_scale_boundary_2026_06_22.py](../scripts/frontier_quark_route2_ray_quotient_hessian_no_scale_boundary_2026_06_22.py)
**Runner output:** [outputs/frontier_quark_route2_ray_quotient_hessian_no_scale_boundary_2026_06_22.txt](../outputs/frontier_quark_route2_ray_quotient_hessian_no_scale_boundary_2026_06_22.txt)

## Scope

Block99 isolated the sufficient inverse-square source law for the Route-2
E/T center lifts. Block100 showed that a dilation-covariant separable Hessian
source density is exactly that inverse-square law. Block101 then showed the
missing counterterm wall:

```text
H_epsilon(w) = C/w^2 + epsilon
```

is still positive and separable for `epsilon >= 0`, but only `epsilon=0`
recovers the target endpoint ratio.

This block records the exact no-scale quotient theorem that would kill the
counterterm. If the channel weight is a positive ray coordinate and the
source Hessian is a two-form on that ray, then pullback-invariance under
uniform ray rescaling forces

```text
H(a w) = a^-2 H(w).
```

Equivalently, the Hessian coefficient is homogeneous of degree `-2`, so
`H(w)=C/w^2`. In the Block101 counterterm family this condition forces
`epsilon=0`.

This is exact support for the next theorem target, not endpoint closure on
the actual current surface. The current surface still does not prove that the
Route-2 channel weights are the physical ray-quotient Hessian coordinates,
nor that the source/readout primitive must be such a no-scale two-form.

## One-Hop Authorities

| Authority | Role used here |
| --- | --- |
| [QUARK_ROUTE2_HESSIAN_COUNTERTERM_EXCLUSION_BOUNDARY_NOTE_2026-06-22.md](QUARK_ROUTE2_HESSIAN_COUNTERTERM_EXCLUSION_BOUNDARY_NOTE_2026-06-22.md) | Direct parent: positive separable counterterms remain allowed by weak premises and only `epsilon=0` hits the endpoint. |
| [QUARK_ROUTE2_DILATION_COVARIANT_HESSIAN_SOURCE_BOUNDARY_NOTE_2026-06-22.md](QUARK_ROUTE2_DILATION_COVARIANT_HESSIAN_SOURCE_BOUNDARY_NOTE_2026-06-22.md) | Direct support: dilation-covariant Hessian density is equivalent to inverse-square source law. |
| [QUARK_ROUTE2_TYPED_METRIC_SOURCE_INVERSE_SQUARE_BOUNDARY_NOTE_2026-06-22.md](QUARK_ROUTE2_TYPED_METRIC_SOURCE_INVERSE_SQUARE_BOUNDARY_NOTE_2026-06-22.md) | Block99: inverse-square center lift suffices for the endpoint triple. |
| [S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md) | Direct downstream consumer and source of the endpoint-triple blocker. |
| [QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md) | Restricted readout map and missing E-channel map entry. |
| [QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md](QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md) | Current no-go that equivariant/quadratic routes do not force the inverse-square lift. |
| [MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md) | Record axiom boundary: no weighting, normalization, probability, dynamics, readout context, or source two-form is supplied. |

## Exact Ray-Quotient Hessian Theorem

Let `w > 0` be a positive channel-weight coordinate and let the separable
source Hessian be the one-dimensional two-form

```text
g = H(w) dw tensor dw.
```

Uniform ray rescaling sends `w` to `a w`, with `a > 0`. Pulling back the
two-form gives

```text
(S_a)^* g = H(a w) d(a w) tensor d(a w)
          = a^2 H(a w) dw tensor dw.
```

Thus the Hessian two-form is invariant under ray rescaling exactly when

```text
a^2 H(a w) = H(w),
```

or equivalently

```text
H(a w) = a^-2 H(w).
```

Setting `w=1` gives `H(a)=a^-2 H(1)`, so

```text
H(w) = C/w^2.
```

Conversely, every `H(w)=C/w^2` satisfies the pullback equation exactly. This
is the ray-quotient/no-scale version of the Block100 functional equation.

The infinitesimal form is the Euler equation

```text
(w d/dw + 2) H(w) = 0.
```

For the Block101 family,

```text
H_epsilon(w) = C/w^2 + epsilon,
```

the Euler residual is

```text
(w d/dw + 2) H_epsilon(w) = 2 epsilon.
```

Equivalently, the finite pullback residual is

```text
a^2 H_epsilon(a w) - H_epsilon(w) = epsilon (a^2 - 1).
```

For any nontrivial scale `a != 1`, ray-quotient invariance therefore forces
`epsilon=0`.

## Endpoint Consequence

With the Route-2 E/T weights

```text
w_E = 1/3,
w_T = 1/2,
```

the no-scale Hessian gives

```text
H(w_E)/H(w_T) = (w_T/w_E)^2 = (3/2)^2 = 9/4.
```

Using the Block99 T normalization `q_T=5/6`,

```text
q_E = (5/6)(9/4) = 15/8,
rho_E = 6(q_E - 1) = 21/4.
```

With `alpha_T/alpha_E=-2`, the center ratio is

```text
c_TE = (-2)(5/6)/(15/8) = -8/9.
```

So a proved Route-2 ray-quotient Hessian source primitive would supply the
same inverse-square law used by Block99 and recover the endpoint triple.

## Variational And Max-Leverage Boundary

The same calculation gives a useful extremal formulation. With `C=1`, the
Block101 counterterm ratio is

```text
R(epsilon) = H_epsilon(1/3)/H_epsilon(1/2)
           = (9 + epsilon)/(4 + epsilon).
```

For `epsilon >= 0`,

```text
dR/depsilon = -5/(4 + epsilon)^2 < 0.
```

Thus the inverse-square source is the unique maximum-leverage endpoint inside
the positive additive-counterterm family. A future variational theorem could
close this route if it proves that the Route-2 source selects the maximal
E/T Hessian leverage, or equivalently a zero intrinsic Hessian floor. The
current surface does not supply that variational premise, and choosing the
maximum because it matches the target would be circular.

## Current-Surface Boundary

This packet exposes a precise positive premise:

```text
Route-2 E/T channel source = ray-quotient Hessian two-form on positive weights.
```

The current surface does not derive that premise.

- Minimal Record supplies finite scalar additivity only after a readout
  context is supplied. It does not supply weights, a source functional, a
  quotient by global scale, or a Hessian two-form.
- The O_h seven-site theorem supplies exact weights and `kappa=3/2`, but not
  a source/readout Hessian.
- The Schur/quadratic no-go leaves the E:T ratio free for quadratic
  invariant forms and names the inverse-square lift as the missing bridge.
- Block101 proves that positivity, convexity, separability, and finite
  additivity alone do not remove the additive counterterm.
- A coordinate bridge remains open: the statement above is a tensorial rule
  for the positive weight coordinate `w`. Reparametrizing to `u=log(w)`
  changes ordinary second derivatives unless the physical Hessian coordinate
  is specified.

Therefore the honest status is exact support/open boundary. A later theorem
must derive the ray quotient, max-leverage, zero-floor, or equivalent
no-scale source rule from retained primitives before this can close the
readout-map endpoint blocker.

## No-Go Discipline

N1 alternative routes:

| Route | Result |
| --- | --- |
| Ray-quotient Hessian two-form | Forces `epsilon=0` and gives the inverse-square law. |
| Positive additive counterterm | Violates ray pullback invariance by `epsilon(a^2-1)`. |
| Infinitesimal Euler no-scale equation | Equivalent to `epsilon=0` in the counterterm family. |
| Max-leverage selection | Would force `epsilon=0`, but is not currently derived. |
| Positivity/separability alone | Allows every `epsilon >= 0`. |
| Coordinate reparametrization without bridge | Does not identify the physical Hessian coordinate. |

N2 wall independence:

The remaining wall is not endpoint arithmetic, O_h weights, Block99
conditional algebra, or Block100's functional equation. It is the physical
source/readout rule that would make the Route-2 Hessian a no-scale
ray-quotient two-form on the positive channel weights.

N3 hidden-wall scan:

The target rationals are used as exact algebraic comparison targets. No
observed masses, fitted endpoint values, nearest-rational selector, or
literature value is used.

N4 residual matching:

The residual matches the S3-time blocker: the readout-map endpoint triple is
not derived. This block gives a sharper sufficient premise for one source-side
route to that endpoint.

N5 rhetoric audit:

"No-scale" and "ray-quotient" name future theorem premises. They are not
asserted as current framework content.

N6 partial-closure path:

If a later retained theorem derives the ray-quotient Hessian source primitive,
then Block102 plus Block100 and Block99 give a direct route to the endpoint
triple.

## Validation

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_ray_quotient_hessian_no_scale_boundary_2026_06_22.py
```

Expected final line:

```text
TOTAL: PASS=38, FAIL=0
```
