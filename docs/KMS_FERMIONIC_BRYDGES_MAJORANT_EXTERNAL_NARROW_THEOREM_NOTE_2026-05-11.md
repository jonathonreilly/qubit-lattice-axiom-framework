# Scalar Quadratic Majorant Lemma For KMS-Style Context

**Date:** 2026-05-11; scope repair 2026-05-27
**Claim type:** bounded_theorem
**Type:** bounded_theorem
**Scope:** scalar quadratic majorant ODE algebra. The KMS fermionic
Polchinski/BBF paper is context only and is not a load-bearing authority for
this row.
**Primary runner:** `scripts/frontier_kms_fermionic_brydges_majorant_external_narrow.py`
**Cache:** `logs/runner-cache/frontier_kms_fermionic_brydges_majorant_external_narrow.txt`

## Source Boundary

This row proves only scalar ODE consequences that are written below and checked
by the paired runner. It does not import the KMS theorem as a premise, does not
claim that any framework action satisfies a KMS majorant inequality, and does
not add a new framework axiom or framework bridge.

## Scope Repair

Prior versions tried to register the Kroschinsky-Marchetti-Salmhofer (KMS)
fermionic Polchinski/BBF majorant theorem as a load-bearing external theorem.
That is too strong for this source row because the row does not include or
derive the published polymer-norm inequality and hypotheses.

This repair removes the KMS theorem from the binding claim. The row now states
only the scalar quadratic majorant ODE lemma that the runner proves directly.

KMS remains context only: if a later row supplies the actual BBF/Polchinski
inequality and its hypotheses, this scalar lemma is the algebraic step that
turns that inequality into a small-data bound.

## Lemma

Let `a(l) >= 0` and `b(l) >= 0` be scale-integrable coefficient functions on a
finite scale interval. Let `y(l) >= 0` satisfy the scalar differential
inequality

```text
dy/dl <= a(l) y(l)^2 + b(l) y(l).
```

Then comparison with the scalar equality gives the usual small-data control.
In the constant `b=0` case,

```text
y(l) = y0 / (1 - a l y0)
```

for the equality problem, so the threshold `a l y0 < 1` is sharp for finite
positive evolution on that interval. With `a=0`, the linear factor composes
multiplicatively across scale slices. Piecewise nonnegative coefficients chain
by applying the same comparison step on each slice.

The zero action `y=0` is a fixed point of the scalar majorant.

## What This Claims

- Exact scalar majorant ODE algebra.
- Small-data threshold behavior for the quadratic equality model.
- Composition of per-scale linear factors.
- Componentwise finite-dimensional diagonal toy checks under the same scalar
  comparison form.
- Nonnegativity of a finite weighted absolute-value norm surrogate.

## What This Does Not Claim

- It does not derive the KMS BBF polymer-norm inequality.
- It does not prove the fermionic Polchinski equation hypotheses.
- It does not construct a Gram covariance decomposition.
- It does not identify any framework effective action with a KMS `V_l`.
- It does not verify that any framework surface is in a KMS small-data regime.
- It does not close hierarchy, BBS, staggered-blocking, or physical-scale
  bridges.

## KMS Context Only

The external paper

```text
A. Kroschinsky, D. Marchetti, M. Salmhofer,
"A Brydges-Battle-Federbush representation for the fermionic Polchinski
equation", arXiv:2404.06099 (2024).
```

is not a load-bearing authority for this repaired row. It is mentioned only as
the context in which a scalar inequality of this form may arise.

Any future framework use must separately supply the BBF/Polchinski inequality,
its hypotheses, and the framework-substrate identification.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_kms_fermionic_brydges_majorant_external_narrow.py
```

Expected:

```text
TOTAL: PASS=19, FAIL=0
```
