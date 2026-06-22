# Quark Route-2 Log-Action Cocycle Hessian Boundary

**Date:** 2026-06-22
**Type:** open gate / exact support
**Claim type:** open_gate
**Actual current-surface status:** exact-support
**Status authority:** independent audit lane only. This source note does not
set, predict, or apply an audit verdict.
**Primary runner:** [scripts/frontier_quark_route2_log_action_cocycle_hessian_boundary_2026_06_22.py](../scripts/frontier_quark_route2_log_action_cocycle_hessian_boundary_2026_06_22.py)
**Runner output:** [outputs/frontier_quark_route2_log_action_cocycle_hessian_boundary_2026_06_22.txt](../outputs/frontier_quark_route2_log_action_cocycle_hessian_boundary_2026_06_22.txt)

## Scope

Blocks107-109 isolated the live Route-2 source/readout wall:

- Block107: a scale-shift-invariant second variation in the positive weight
  coordinate `w` is sufficient for source-row degree `d=-2`.
- Block108: finite scalar Record additivity alone does not supply that
  nonzero Hessian.
- Block109: standard Fisher/KL/Shannon information metrics give degree `-1`,
  not `-2`.

This block tests the remaining positive source-action shape:

```text
the physical source action is a multiplicative-to-additive cocycle on the
positive weight ray, and the Route-2 source row reads its Hessian in w.
```

Under that premise, the source action must be logarithmic up to scale and
affine Hessian-gauge terms. Its Hessian in `w` is inverse-square, hence it
supplies the Block107 second-variation row.

This block does not derive that the Route-2 source/readout primitive has this
log-action cocycle semantics on the actual current surface. It gives the exact
positive bridge to try next and separates it from the already-pruned Record
additivity and standard information-metric routes.

## A_min And Forbidden Imports

Allowed in this block:

- the exact Route-2 endpoint algebra and S3 blocker;
- the O_h weights `w_E=1/3`, `w_T=1/2`;
- supplied T-side values `q_T=5/6` and `s_TE=-2` as conditional stretch
  inputs;
- the product/log-selection algebra from existing source-measure and log-det
  boundary notes as analogy and support;
- exact rational arithmetic;
- the candidate log-action cocycle plus Hessian-readout premise as the tested
  premise.

Forbidden proof inputs:

- observed masses;
- fitted endpoint values;
- nearest-rational selection;
- live endpoint measurements;
- literature values;
- assuming `q_E=15/8`, `rho_E=21/4`, or `c_TE=-8/9`.

The target fractions appear only as exact consequences or comparison values.

## One-Hop Authorities

| Authority | Role used here |
| --- | --- |
| [QUARK_ROUTE2_LOG_WEIGHT_SECOND_VARIATION_ROW_BOUNDARY_NOTE_2026-06-22.md](QUARK_ROUTE2_LOG_WEIGHT_SECOND_VARIATION_ROW_BOUNDARY_NOTE_2026-06-22.md) | Direct parent: second variation in `w` is sufficient for degree `d=-2`. |
| [QUARK_ROUTE2_RECORD_ADDITIVE_SECOND_VARIATION_NO_GO_NOTE_2026-06-22.md](QUARK_ROUTE2_RECORD_ADDITIVE_SECOND_VARIATION_NO_GO_NOTE_2026-06-22.md) | Direct parent: scalar Record additivity does not supply the nonzero Hessian. |
| [QUARK_ROUTE2_INFORMATION_METRIC_DEGREE_BOUNDARY_NOTE_2026-06-22.md](QUARK_ROUTE2_INFORMATION_METRIC_DEGREE_BOUNDARY_NOTE_2026-06-22.md) | Direct parent: standard information metrics have degree `-1`, not `-2`. |
| [SOURCE_MEASURE_LOG_SELECTION_BOUNDARY_THEOREM_NOTE_2026-05-30.md](SOURCE_MEASURE_LOG_SELECTION_BOUNDARY_THEOREM_NOTE_2026-05-30.md) | Existing source-measure boundary: product composition selects logarithmic coordinate up to scale but not the physical source unit. |
| [REAL_DIAGONAL_SOURCE_DET_POSITIVITY_AND_LOG_READOUT_LEMMA_NOTE_2026-06-08.md](REAL_DIAGONAL_SOURCE_DET_POSITIVITY_AND_LOG_READOUT_LEMMA_NOTE_2026-06-08.md) | Existing log-readout lemma: multiplicative-to-additive Cauchy equation gives log under explicit regularity, with conventions separated. |
| [FLAVOR_LOGDET_FORM_UNDER_RECORD_AXIOM_2026-06-04.md](FLAVOR_LOGDET_FORM_UNDER_RECORD_AXIOM_2026-06-04.md) | Existing firewall: Record additivity only acts after a multiplicative character/readout domain is supplied. |
| [S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md) | Downstream open gate and endpoint-triple blocker. |

## Cocycle-To-Log Theorem

Let `A(w)` be a differentiable scalar source action on the positive ray
`w>0`. Suppose the action is an additive character of multiplicative ray
composition:

```text
A(a b) = A(a) + A(b),       A(1)=0.
```

Equivalently, in log coordinate `u=log w`, define

```text
B(u) = A(exp(u)).
```

Then the equation becomes ordinary additivity:

```text
B(u+v) = B(u) + B(v).
```

With differentiability or the finite-block regularity used by the existing
log-selection notes, the solutions are

```text
B(u) = K u,
A(w) = K log(w).
```

If the source row reads the Hessian of the signed log-barrier representative

```text
Phi(w) = -C log(w) + A_1 w + A_0,
```

then

```text
Phi''(w) = C/w^2.
```

The affine terms are Hessian-gauge terms and do not change the source row.
Thus the premise

```text
multiplicative source-action cocycle + Hessian row readout in w
```

implies the Block107 second-variation row.

## Endpoint Consequence

Using

```text
w_E = 1/3,
w_T = 1/2,
```

the log-action Hessian gives

```text
Phi''(w_E)/Phi''(w_T) = (w_T/w_E)^2 = (3/2)^2 = 9/4.
```

With supplied `q_T=5/6`,

```text
q_E = (5/6)(9/4) = 15/8,
rho_E = 6(q_E - 1) = 21/4.
```

With supplied shell ratio `s_TE=-2`,

```text
c_TE = (-2)(5/6)/(15/8) = -8/9.
```

So the log-action cocycle plus Hessian-readout premise is sufficient for the
endpoint triple:

```text
(-1, -2, 21/4).
```

## Falsifiers And Route Separation

The load-bearing premise is not merely "log appears" and not merely
"multiplicative composition appears."

| Candidate | Row degree | Result |
| --- | ---: | --- |
| direct additive scalar weight `w` | `+1` | misses endpoint |
| standard Fisher/KL/Shannon information metric `1/w` | `-1` | Block109 first-variation miss |
| log-action first derivative `1/w` | `-1` | Block107 first-variation miss |
| log-action Hessian `1/w^2` | `-2` | sufficient for endpoint |
| generic homogeneous row | free | Block106 no-go |

Thus a future positive theorem must prove both parts:

1. the physical source action is the multiplicative-to-additive log cocycle;
2. the Route-2 source row reads the second variation/Hessian in the `w`
   coordinate, not the first derivative or standard information metric.

## Current-Surface Boundary

The actual current surface remains open.

Existing log-selection notes show how a logarithmic coordinate follows after a
multiplicative character/product source domain is supplied. They also state
that Record additivity alone does not supply that source domain, source unit,
or physical source-action bridge.

For Route-2, the missing theorem is now sharper:

```text
derive that the Route-2 E/T source/readout primitive is a positive-ray
log-action cocycle whose physical row is the Hessian in w.
```

This block does not assert that premise as current framework content.

## No-Go Discipline

N1 alternative routes:

| Route | Result |
| --- | --- |
| Record additivity alone | Block108: no nonzero Hessian. |
| Standard information metric | Block109: degree `-1`. |
| Multiplicative log cocycle, first derivative | degree `-1`, misses. |
| Multiplicative log cocycle, Hessian row | this note: degree `-2`, sufficient. |
| Generic homogeneous row | Block106: degree remains free. |

N2 wall independence:

The remaining wall is the physical source-action/readout identification, not
the endpoint arithmetic, O_h weights, or the log functional equation once its
premise is supplied.

N3 hidden-wall scan:

No observed masses, fitted endpoint values, nearest-rational selector,
literature value, or live endpoint measurement is used.

N4 residual matching:

The residual matches the parent S3/Route-2 blocker: the endpoint triple is not
derived because the source/readout primitive selecting the E-center row is not
derived.

N5 rhetoric audit:

"Log-action cocycle" names a future theorem premise. It is not asserted as
current Route-2 framework content.

## Validation

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_log_action_cocycle_hessian_boundary_2026_06_22.py
```

Expected final line:

```text
TOTAL: PASS=40, FAIL=0
```
