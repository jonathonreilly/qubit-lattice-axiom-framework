# Dynamics Coupling Residual Classifier

**Date:** 2026-06-06
**Claim type:** no-go / exact-support boundary
**Status:** branch-local source note awaiting independent audit handling.
**Primary runner:**
[`scripts/frontier_dynamics_coupling_residual_classifier_2026_06_06.py`](../scripts/frontier_dynamics_coupling_residual_classifier_2026_06_06.py)
with cached output
[`logs/runner-cache/frontier_dynamics_coupling_residual_classifier_2026_06_06.txt`](../logs/runner-cache/frontier_dynamics_coupling_residual_classifier_2026_06_06.txt).

## Result

Record/gauge preservation can constrain a dynamics form-class. It does not fix:

- coupling magnitude;
- coefficient ratios between independently allowed invariant terms;
- nonzero dynamics;
- clock-rate normalization.

This is the finite algebra version of the residual already visible in the
record-preservation dynamics stack: preserving the record algebra can put `H`
inside a commutant or gauge-invariant-local class, but all scalar coefficients
inside that class remain additional dynamics data unless a separate action,
normalization, minimality, variational, or clock premise is supplied.

## Exact Checks

For a two-atom record algebra with atom projectors `P0, P1`, the Hamiltonian

```text
H(g) = g P1
```

commutes with both record atoms for arbitrary real `g`. Therefore the
record-preservation equations do not determine `g`.

The zero Hamiltonian `H=0` also preserves all records, so nontriviality is not
forced.

The transfer

```text
T = exp(-a H(g))
```

depends on the product `a g`. Thus the same transfer can arise from
`(g=1,a=2)` and `(g=2,a=1)`. A rate/coupling split needs an extra clock or
normalization premise.

For a four-atom algebra, two independent diagonal invariant terms `A` and `B`
commute with all record atoms:

```text
H(x,y) = x A + y B.
```

The ratio `x/y` remains free under record preservation.

## Connection To Open Coupling Gates

This block is relevant to coupling-status gates such as the active
`g_bare` parent-retention gate: a preservation/class theorem may support an
allowed dynamics class, but it does not by itself supply a numeric coupling,
rate, or parent promotion. Any coupling closure still needs its own audited
dependency chain.

## Boundaries

- Does not derive or reject a specific `g_bare` value.
- Does not derive an action, variational principle, minimal truncation, or
  clock metric.
- Does not update repo-wide authority surfaces.
- Does not claim that record preservation is useless; it isolates what it can
  and cannot determine.

## Runner Summary

Expected scorecard:

```text
PASS=18 FAIL=0
```
