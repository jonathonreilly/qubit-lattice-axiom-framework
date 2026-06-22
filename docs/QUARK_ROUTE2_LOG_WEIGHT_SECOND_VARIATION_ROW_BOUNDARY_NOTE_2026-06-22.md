# Quark Route-2 Log-Weight Second-Variation Row Boundary

**Date:** 2026-06-22
**Type:** open gate / exact support
**Claim type:** open_gate
**Actual current-surface status:** exact-support
**Status authority:** independent audit lane only. This source note does not
set, predict, or apply an audit verdict.
**Primary runner:** [scripts/frontier_quark_route2_log_weight_second_variation_row_boundary_2026_06_22.py](../scripts/frontier_quark_route2_log_weight_second_variation_row_boundary_2026_06_22.py)
**Runner output:** [outputs/frontier_quark_route2_log_weight_second_variation_row_boundary_2026_06_22.txt](../outputs/frontier_quark_route2_log_weight_second_variation_row_boundary_2026_06_22.txt)

## Scope

Block105 isolated the direct row-side target: a homogeneous source-row degree
`d=-2` is exactly equivalent to the missing E-center endpoint value after the
T-side entries are supplied. Block106 then proved that generic homogeneity,
T normalization, scale covariance, and positivity do not select that degree.

This block is the hard positive stretch: add one specific physical source-row
candidate and test whether it supplies the missing selector.

The candidate is:

```text
the Route-2 source row is a scale-shift-invariant second variation
in the positive channel-weight coordinate w.
```

Equivalently, the source row is a Hessian two-form on the positive weight ray
whose scalar potential changes under `w -> a w` only by terms invisible to
second variation. This premise forces the Hessian coefficient to have degree
`-2`, hence supplies the Block105 degree.

This block does not derive that the Route-2 source row is such a second variation
on the actual current surface. It gives exact support and a falsifiable
physical theorem target, not an endpoint closure.

## A_min And Forbidden Imports

Allowed in this block:

- the current Route-2 endpoint algebra and S3 blocker;
- the O_h weights `w_E=1/3`, `w_T=1/2`;
- supplied T-side values `q_T=5/6` and `s_TE=-2` as conditional stretch inputs;
- exact rational arithmetic;
- the candidate second-variation/log-weight row primitive as the tested
  premise.

Forbidden proof inputs:

- observed masses;
- fitted endpoint values;
- nearest-rational selection;
- live endpoint measurements;
- literature values;
- assuming `q_E=15/8`, `rho_E=21/4`, or `c_TE=-8/9`.

The target rationals appear only as exact consequences or comparison values.

## One-Hop Authorities

| Authority | Role used here |
| --- | --- |
| [QUARK_ROUTE2_SOURCE_ROW_DEGREE_SELECTOR_NO_GO_NOTE_2026-06-22.md](QUARK_ROUTE2_SOURCE_ROW_DEGREE_SELECTOR_NO_GO_NOTE_2026-06-22.md) | Direct parent: generic homogeneous row constraints do not select `d=-2`. |
| [QUARK_ROUTE2_DIRECT_E_CENTER_SOURCE_ROW_DEGREE_BOUNDARY_NOTE_2026-06-22.md](QUARK_ROUTE2_DIRECT_E_CENTER_SOURCE_ROW_DEGREE_BOUNDARY_NOTE_2026-06-22.md) | Identifies `d=-2` as the exact row-side target. |
| [QUARK_ROUTE2_POWER_LAW_COORDINATE_BRIDGE_BOUNDARY_NOTE_2026-06-22.md](QUARK_ROUTE2_POWER_LAW_COORDINATE_BRIDGE_BOUNDARY_NOTE_2026-06-22.md) | Coordinate-side support theorem and homogeneity bridge boundary. |
| [QUARK_ROUTE2_RAY_QUOTIENT_HESSIAN_NO_SCALE_BOUNDARY_NOTE_2026-06-22.md](QUARK_ROUTE2_RAY_QUOTIENT_HESSIAN_NO_SCALE_BOUNDARY_NOTE_2026-06-22.md) | Ray-Hessian no-scale support theorem; supplies the two-form functional equation. |
| [S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md) | Downstream open gate and endpoint-triple blocker. |
| [MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md) | Axiom boundary: no readout context, source-row primitive, weighting rule, or Hessian semantics is supplied. |

## Theorem

Let `w>0` be the Route-2 positive channel-weight coordinate. Suppose a direct
source row is represented by a Hessian coefficient

```text
H(w) = d^2 Phi / dw^2
```

and the corresponding Hessian two-form

```text
g = H(w) dw tensor dw
```

is invariant under common positive scale shifts of the weight ray. Under
`S_a(w)=a w`,

```text
(S_a)^* g = a^2 H(a w) dw tensor dw.
```

Scale-shift invisibility to second variation therefore requires

```text
a^2 H(a w) = H(w),
```

or

```text
H(a w) = a^-2 H(w).
```

Setting `w=1` gives

```text
H(w) = C/w^2.
```

This is the direct row-side route from a physical second-variation primitive
to the Block105 degree:

```text
H(w) proportional to w^-2
  => source-row degree d=-2.
```

Equivalently, a log-weight source potential

```text
Phi(w) = -C log(w) + A w + B
```

has

```text
Phi''(w) = C/w^2,
```

and the affine terms are invisible to the second variation.

## Endpoint Consequence

Use

```text
w_E = 1/3,
w_T = 1/2.
```

The second-variation row gives

```text
H(w_E)/H(w_T) = (w_T/w_E)^2 = (3/2)^2 = 9/4.
```

With supplied `q_T=5/6`,

```text
q_E = (5/6)(9/4) = 15/8,
rho_E = 6(q_E - 1) = 21/4.
```

With supplied shell ratio `s_TE=-2`,

```text
c_TE = s_TE q_T/q_E
     = (-2)(5/6)/(15/8)
     = -8/9.
```

So the candidate primitive is sufficient for the endpoint triple:

```text
(-1, -2, 21/4).
```

## Derivative-Order Falsifiers

The load-bearing selector is second variation, not generic log language.

The ordinary `n`-th derivative of `log(w)` is proportional to `w^-n`. Thus
its E/T ratio is `(3/2)^n`.

In particular, first variation gives degree `-1`, second variation gives
degree `-2`, and third variation gives degree `-3`.

| Row source | degree | `q_E/q_T` | `q_E` | `rho_E` | `c_TE` |
| --- | ---: | ---: | ---: | ---: | ---: |
| first variation | `-1` | `3/2` | `5/4` | `3/2` | `-4/3` |
| second variation | `-2` | `9/4` | `15/8` | `21/4` | `-8/9` |
| third variation | `-3` | `27/8` | `45/16` | `87/8` | `-16/27` |
| fourth variation | `-4` | `81/16` | `135/32` | `309/16` | `-32/81` |

Therefore a proof that the row is merely "log-like" or "homogeneous" is not
enough. The source/readout primitive must specifically identify the row as a
second variation or an equivalent Hessian two-form.

## Relationship To Blocks104-106

- Block104 shows that a multiplicatively homogeneous coordinate bridge keeps
  a no-scale Hessian inverse-square in `w`.
- Block105 shows that direct row degree `d=-2` is exactly the endpoint target.
- Block106 shows generic homogeneity and positivity do not select that degree.
- This block gives the positive row-side selector: scale-shift-invariant
  second variation implies `d=-2`.

The remaining import is physical, not algebraic: the second-variation primitive is the remaining import.

## Current-Surface Boundary

The actual current surface remains open.

Minimal Record supplies no readout context, source-row primitive, weighting
rule, source potential, or Hessian semantics. The O_h weights supply exact
channel weights but not a rule saying that the Route-2 source row is a
scale-shift-invariant second variation in those weights.

Thus this block is exact support for a concrete positive theorem target. It is
not an endpoint closure.

## No-Go Discipline

N1 alternative routes:

| Route | Result |
| --- | --- |
| Generic homogeneous row | Block106: insufficient; degree remains free. |
| First variation of log weight | Misses with degree `-1`. |
| Scale-shift-invariant second variation | This note: sufficient; gives degree `-2`. |
| Third variation of log weight | Misses with degree `-3`. |
| Coordinate/Hessian bridge | Block104: compatible route if physical coordinate homogeneity is derived. |

N2 wall independence:

The remaining wall is the physical source/readout statement that the row is a
second variation in the positive weight coordinate. This is independent of the
endpoint arithmetic and of generic homogeneity.

N3 hidden-wall scan:

No observed masses, fitted endpoint values, nearest-rational selector,
literature value, or live endpoint measurement is used.

N4 residual matching:

The residual matches the parent S3/Route-2 blocker: the endpoint triple is not
derived because the source/readout primitive selecting the E-center row is not
derived.

N5 rhetoric audit:

"Scale-shift-invariant second variation" names a future theorem premise. It
is not asserted as current framework content.

## Validation

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_log_weight_second_variation_row_boundary_2026_06_22.py
```

Expected final line:

```text
TOTAL: PASS=45, FAIL=0
```
