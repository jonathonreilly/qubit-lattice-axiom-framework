# Quark Route-2 Source-Action Primitive Boundary

**Date:** 2026-06-22
**Type:** open gate / exact support plus scoped no-go
**Claim type:** open_gate
**Actual current-surface status:** exact-support
**Status authority:** independent audit lane only. This source note does not
set, predict, or apply an audit verdict.
**Primary runner:** [scripts/frontier_quark_route2_source_action_primitive_boundary_2026_06_22.py](../scripts/frontier_quark_route2_source_action_primitive_boundary_2026_06_22.py)
**Runner output:** [outputs/frontier_quark_route2_source_action_primitive_boundary_2026_06_22.txt](../outputs/frontier_quark_route2_source_action_primitive_boundary_2026_06_22.txt)

## Scope

Block110 proved the exact positive bridge:

```text
regular multiplicative-to-additive source action
+ Hessian-row readout in the positive weight coordinate w
=> q_E = 15/8, rho_E = 21/4, c_TE = -8/9.
```

This block attacks the missing physical primitive more directly. It asks
whether the log-action cocycle semantics, by itself, selects the Hessian row.

It does not. A regular positive-ray cocycle selects the logarithmic source
action, but it does not select the finite-jet order by which the source row
reads that action. First derivative, second derivative, and higher derivative
rows are all local exact finite-jet readings of the same log action. They give
different Route-2 endpoint ratios.

The block also records the strongest positive narrowing found in this
first-principles attempt: if the Route-2 source action is physically defined
only up to affine Hessian-gauge terms in `w`, and if the source row is the
lowest nonzero constant-coefficient local finite-jet readout invariant under
that affine gauge, then the row is a Hessian row. That premise would recover
Block110. The current surface does not derive that affine-gauge/minimal
curvature premise or the constant source-unit/no-scale coefficient needed to
avoid a weight-dependent Hessian prefactor.

## A_min And Forbidden Imports

Allowed in this block:

- the exact Route-2 endpoint algebra and S3 blocker;
- the O_h weights `w_E=1/3`, `w_T=1/2`;
- supplied T-side values `q_T=5/6` and `s_TE=-2` as conditional stretch
  inputs;
- Block110's regular positive-ray cocycle-to-log theorem;
- local finite-jet calculus in the physical `w` coordinate;
- exact rational arithmetic.

Forbidden proof inputs:

- observed masses;
- fitted endpoint values;
- nearest-rational selection;
- live endpoint measurements;
- literature values;
- assuming `q_E=15/8`, `rho_E=21/4`, or `c_TE=-8/9`;
- assuming from the start that the physical source row is a Hessian row.

The target fractions appear only as exact consequences or comparison values.

## One-Hop Authorities

| Authority | Role used here |
| --- | --- |
| [QUARK_ROUTE2_LOG_ACTION_COCYCLE_HESSIAN_BOUNDARY_NOTE_2026-06-22.md](QUARK_ROUTE2_LOG_ACTION_COCYCLE_HESSIAN_BOUNDARY_NOTE_2026-06-22.md) | Direct parent: log-action cocycle plus Hessian row is sufficient for the endpoint. |
| [QUARK_ROUTE2_LOG_WEIGHT_SECOND_VARIATION_ROW_BOUNDARY_NOTE_2026-06-22.md](QUARK_ROUTE2_LOG_WEIGHT_SECOND_VARIATION_ROW_BOUNDARY_NOTE_2026-06-22.md) | Direct parent: second variation in `w` is sufficient for degree `d=-2`. |
| [QUARK_ROUTE2_RECORD_ADDITIVE_SECOND_VARIATION_NO_GO_NOTE_2026-06-22.md](QUARK_ROUTE2_RECORD_ADDITIVE_SECOND_VARIATION_NO_GO_NOTE_2026-06-22.md) | Prior no-go: scalar Record additivity does not supply a nonzero Hessian. |
| [QUARK_ROUTE2_INFORMATION_METRIC_DEGREE_BOUNDARY_NOTE_2026-06-22.md](QUARK_ROUTE2_INFORMATION_METRIC_DEGREE_BOUNDARY_NOTE_2026-06-22.md) | Prior no-go: standard Fisher/KL/Shannon metrics give degree `-1`, not `-2`. |
| [QUARK_ROUTE2_HESSIAN_COUNTERTERM_EXCLUSION_BOUNDARY_NOTE_2026-06-22.md](QUARK_ROUTE2_HESSIAN_COUNTERTERM_EXCLUSION_BOUNDARY_NOTE_2026-06-22.md) | Prior boundary: positivity does not exclude extra Hessian counterterms. |
| [S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md) | Downstream open gate and endpoint-triple blocker. |
| [QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md) | Restricted readout map and missing E-channel map entry. |
| [MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md) | Framework boundary: no source-row derivative order or physical readout primitive is supplied. |

## Cocycle Fixes The Action, Not The Row

Let `A(w)` be a regular scalar source action on `w>0` satisfying

```text
A(a b) = A(a) + A(b),       A(1)=0.
```

As in Block110, write `u=log w` and `B(u)=A(exp u)`. Then

```text
B(u+v)=B(u)+B(v),
```

so regularity gives

```text
A(w)=K log w.
```

This selects the action coordinate. It does not select which local response
functional is the physical source row. For the signed log representative

```text
Phi(w) = -C log w,
```

the local finite-jet readings have the exact shape

```text
(-1)^k Phi^(k)(w) proportional to w^-k       for k >= 1.
```

Thus the derivative order `k` sets the row degree `d=-k`.

Using the Route-2 weights,

```text
w_E = 1/3,       w_T = 1/2,
```

the E/T row ratio for derivative order `k` is

```text
R_k = (w_T/w_E)^k = (3/2)^k.
```

The endpoint target requires

```text
R_k = 9/4,
```

which selects `k=2` after `k` is known to be an integer derivative order. But
the cocycle premise itself does not select `k`.

## Exact Counter-Witnesses

With supplied `q_T=5/6` and `s_TE=-2`, the derivative-order family gives

```text
q_E(k) = (5/6) R_k,
rho_E(k) = 6(q_E(k)-1),
c_TE(k) = (-2)(5/6)/q_E(k).
```

The target derivative order is:

| Readout | `R_k` | `q_E` | `rho_E` | `c_TE` |
| --- | ---: | ---: | ---: | ---: |
| second derivative `k=2` | `9/4` | `15/8` | `21/4` | `-8/9` |

But the same log action also admits local derivative rows that miss:

| Readout | `R_k` | `q_E` | `rho_E` | `c_TE` |
| --- | ---: | ---: | ---: | ---: |
| first derivative `k=1` | `3/2` | `5/4` | `3/2` | `-4/3` |
| third derivative `k=3` | `27/8` | `45/16` | `87/8` | `-16/27` |
| fourth derivative `k=4` | `81/16` | `135/32` | `309/16` | `-32/81` |

These are not proposed alternatives. They are counter-witnesses to the
overread:

```text
log-action cocycle semantics alone => Hessian source row.
```

The missing datum is derivative order or an equivalent physical response
principle.

## Affine-Gauge Minimal-Curvature Support

There is a sharper positive criterion.

Suppose the source action representative is physically meaningful only modulo
affine Hessian-gauge terms:

```text
Phi(w) ~ Phi(w) + A_0 + A_1 w.
```

Consider a constant-coefficient local linear finite-jet readout through order
2:

```text
L[Phi](w) = a_0 Phi(w) + a_1 Phi'(w) + a_2 Phi''(w).
```

Gauge invariance demands

```text
L[A_0 + A_1 w](w) = 0
```

for every `A_0`, `A_1`, and `w`. This forces:

```text
a_0 = 0,       a_1 = 0.
```

The lowest nonzero such readout is therefore

```text
L[Phi](w) = a_2 Phi''(w).
```

For the log-action representative, this is exactly the Hessian row:

```text
Phi''(w) = C/w^2.
```

So a future theorem can replace the imported phrase "Hessian row readout" by
the more primitive phrase:

```text
affine-gauge-invariant lowest-order local curvature response in w,
with constant source unit / no weight-dependent prefactor.
```

That would be a real first-principles bridge into Block110.

## What Still Does Not Follow

The current surface does not derive the affine-gauge/minimal-curvature
premise.

Two walls remain:

1. The Route-2 source action must be shown to be a physical positive-ray
   log-action cocycle, not merely an available mathematical coordinate.
2. The Route-2 source row must be shown to be the affine-gauge-invariant
   lowest-order local curvature response in the physical `w` coordinate, with
   no weight-dependent coefficient multiplying `Phi''(w)`.

The second condition matters. Even after affine gauge removes value and first
derivative rows, a prefactor family

```text
g(w) Phi''(w)
```

is still affine-gauge-invariant. If `g(w)=w`, the degree becomes `-1`; if
`g(w)=w^2`, the degree becomes `0`. Therefore affine gauge alone is not enough
unless the source-unit/no-scale coefficient is also derived.

## Current-Surface Boundary

This block narrows the remaining source/readout theorem target to:

```text
Route-2 E/T source action is a regular positive-ray log-action cocycle,
and its physical readout row is the no-scale affine-gauge-invariant
lowest-order local curvature response in w.
```

It does not assert that target as current framework content.

## No-Go Discipline

N1 alternative routes:

| Route | Result |
| --- | --- |
| Log-action cocycle alone | Selects `A(w)=K log w`, but not derivative order. |
| First derivative of log action | Exact local finite jet; gives degree `-1`, not endpoint. |
| Second derivative of log action | Gives degree `-2`; sufficient if physically selected. |
| Higher derivative of log action | Exact local finite jets; miss endpoint for `k != 2`. |
| Affine-gauge minimal constant finite jet | Supports Hessian row, but the premise is not derived here. |
| Affine-gauge readout with weight-dependent prefactor | Still underselects the endpoint. |

N2 wall independence:

The remaining wall is not endpoint arithmetic. It is source/readout semantics:
the physical derivative order, physical coordinate, and source-unit/no-scale
coefficient.

N3 hidden-wall scan:

No observed masses, fitted endpoint values, nearest-rational selector,
literature value, or live endpoint measurement is used.

N4 residual matching:

The residual matches the S3/Route-2 blocker: the endpoint triple is not derived
because the E-channel map entry is not selected by a physical readout
primitive.

N5 rhetoric audit:

"Affine-gauge minimal curvature response" names a future theorem premise. It
is not asserted as current Route-2 framework content.

## Validation

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_source_action_primitive_boundary_2026_06_22.py
```

Expected final line:

```text
TOTAL: PASS=51, FAIL=0
```
