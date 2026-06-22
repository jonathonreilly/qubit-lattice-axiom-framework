# Quark Route-2 Power-Law Coordinate Bridge Boundary

**Date:** 2026-06-22
**Type:** open gate / exact support
**Claim type:** open_gate
**Actual current-surface status:** exact-support
**Status authority:** independent audit lane only. This source note does not
set, predict, or apply an audit verdict.
**Primary runner:** [scripts/frontier_quark_route2_power_law_coordinate_bridge_boundary_2026_06_22.py](../scripts/frontier_quark_route2_power_law_coordinate_bridge_boundary_2026_06_22.py)
**Runner output:** [outputs/frontier_quark_route2_power_law_coordinate_bridge_boundary_2026_06_22.txt](../outputs/frontier_quark_route2_power_law_coordinate_bridge_boundary_2026_06_22.txt)

## Scope

Block102 proved that a no-scale Hessian two-form in the Route-2 positive
weight coordinate `w` gives the inverse-square source law. Block103 then
proved that no-scale form in an arbitrary positive coordinate is too weak:
the coordinate warp `y_b=w exp(bw)` misses the endpoint for `b>0`.

This block records the exact sufficient coordinate bridge that survives that
no-go:

```text
y = K w^a,      K > 0, a != 0.
```

Equivalently,

```text
d log y / d log w = a
```

is constant. A no-scale Hessian in the `y` coordinate pulls back to

```text
C (d log y/dw)^2 dw tensor dw
  = C a^2 dw tensor dw / w^2.
```

The constant `C a^2` cancels in the E/T ratio, so every nonzero power-law
coordinate gives the same Route-2 inverse-square lift:

```text
H_E/H_T = (w_T/w_E)^2 = 9/4.
```

Thus a future positive theorem does not need to prove that the physical
coordinate is exactly `w`; it is enough to prove a multiplicatively
homogeneous coordinate bridge, or equivalently a constant log-elasticity
bridge. The current surface still does not derive that bridge.

## One-Hop Authorities

| Authority | Role used here |
| --- | --- |
| [QUARK_ROUTE2_HESSIAN_COORDINATE_WARP_NO_GO_NOTE_2026-06-22.md](QUARK_ROUTE2_HESSIAN_COORDINATE_WARP_NO_GO_NOTE_2026-06-22.md) | Direct parent: arbitrary positive coordinate no-scale is too weak; positive warps miss the endpoint. |
| [QUARK_ROUTE2_RAY_QUOTIENT_HESSIAN_NO_SCALE_BOUNDARY_NOTE_2026-06-22.md](QUARK_ROUTE2_RAY_QUOTIENT_HESSIAN_NO_SCALE_BOUNDARY_NOTE_2026-06-22.md) | No-scale Hessian in `w` gives inverse-square source law. |
| [QUARK_ROUTE2_HESSIAN_COUNTERTERM_EXCLUSION_BOUNDARY_NOTE_2026-06-22.md](QUARK_ROUTE2_HESSIAN_COUNTERTERM_EXCLUSION_BOUNDARY_NOTE_2026-06-22.md) | Additive counterterm boundary and zero-counterterm target. |
| [QUARK_ROUTE2_TYPED_METRIC_SOURCE_INVERSE_SQUARE_BOUNDARY_NOTE_2026-06-22.md](QUARK_ROUTE2_TYPED_METRIC_SOURCE_INVERSE_SQUARE_BOUNDARY_NOTE_2026-06-22.md) | Inverse-square center-lift conditional endpoint theorem. |
| [S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md) | Downstream consumer and endpoint-triple blocker. |
| [MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md) | Axiom boundary: no source coordinate, homogeneity rule, or Hessian two-form is supplied. |

## Exact Power-Law Bridge Theorem

Let `w>0` be the Route-2 E/T projector-weight coordinate and let

```text
y(w) = K w^a,       K>0, a != 0.
```

A no-scale Hessian two-form in `y` is

```text
g = C dy tensor dy / y^2.
```

Pulling back to `w`,

```text
g = C (d log y/dw)^2 dw tensor dw.
```

For `y=K w^a`,

```text
d log y/dw = a/w,
```

so

```text
g = C a^2 dw tensor dw / w^2.
```

The coefficient is inverse-square in `w`. The prefactor `C a^2` is
channel-uniform and cancels in the E/T ratio.

Using the Route-2 weights

```text
w_E = 1/3,
w_T = 1/2,
```

gives

```text
H(w_E)/H(w_T) = (w_T/w_E)^2 = 9/4.
```

With `q_T=5/6`, this gives

```text
q_E = 15/8,
rho_E = 21/4.
```

Therefore the sufficient coordinate bridge is not "`y=w`"; it is the weaker
homogeneity condition:

```text
y(lambda w) = lambda^a y(w)
```

for a nonzero channel-uniform exponent `a`.

## Boundary Against Block103 Warps

The Block103 coordinate warp

```text
y_b = w exp(bw)
```

has log-elasticity

```text
d log y_b / d log w = 1 + b w.
```

For `b>0`, this is not constant across `w_E=1/3` and `w_T=1/2`.
It therefore lies outside the sufficient power-law bridge class, and its
pulled-back E/T ratio is

```text
((3+b)/(2+b))^2,
```

not `9/4`.

This separates the positive route from the no-go: arbitrary positive
coordinates are too broad, but homogeneous positive coordinates are sufficient.

## Current-Surface Boundary

The current surface does not derive a homogeneous physical source coordinate.

- Minimal Record supplies no readout context, source coordinate, weighting
  rule, homogeneity principle, or Hessian two-form.
- O_h projector weights supply exact `w_E` and `w_T`, not a physical
  coordinate transformation law for the source/readout Hessian.
- Block103 shows that monotonic positivity alone cannot exclude non-power
  coordinate warps.
- The present block shows a weaker positive target: prove constant
  log-elasticity, not exact identity with `w`.

The honest status is exact support/open boundary. A later theorem must derive
the multiplicatively homogeneous source-coordinate bridge from retained
primitives before this route can close the S3/Route-2 endpoint blocker.

## No-Go Discipline

N1 alternative routes:

| Route | Result |
| --- | --- |
| Exact `y=w` ray coordinate | Sufficient but stronger than needed. |
| Power-law coordinate `y=K w^a` | Sufficient; still gives inverse-square source law. |
| Arbitrary positive coordinate | Too weak; Block103 gives counter-witnesses. |
| Additive counterterm | Excluded by no-scale only after a coordinate bridge is supplied. |

N2 wall independence:

The remaining wall is the physical coordinate homogeneity theorem, not the
endpoint arithmetic, the E/T weights, or the inverse-square consequence.

N3 hidden-wall scan:

No observed masses, fitted endpoint values, nearest-rational selector, or
literature value is used. The target rationals appear only as exact algebraic
comparison values downstream of the supplied premise.

N4 residual matching:

The residual remains the S3-time readout-map endpoint triple. This note
narrows one source-side positive route by weakening the required coordinate
bridge from exact identity to multiplicative homogeneity.

N5 rhetoric audit:

"Power-law coordinate bridge" names a future theorem target. This block does
not assert that the bridge is current framework content.

## Validation

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_power_law_coordinate_bridge_boundary_2026_06_22.py
```

Expected final line:

```text
TOTAL: PASS=37, FAIL=0
```
