# Scalar Quadratic Majorant Lemma For KMS-Style Context

**Date:** 2026-05-11; scope repair 2026-05-27
**Claim type:** bounded_theorem
**Type:** bounded_theorem
**Scope:** external fermionic-RG majorant theorem from Kroschinsky-Marchetti-Salmhofer arXiv:2404.06099 (2024), cited as rigorous-RG context for the fermionic Polchinski equation. No framework substitution, hierarchy formula, or physical scale closure is claimed.
**Status authority:** independent audit lane only.
**Runner:** `scripts/frontier_kms_fermionic_brydges_majorant_external_narrow.py`
**Cache:** `logs/runner-cache/frontier_kms_fermionic_brydges_majorant_external_narrow.txt`

## 2026-05-28 Audit Repair (conditional core; missing upstream admitted)

The 2026-05-28 audit verdict was `audited_conditional`:

> *"The scalar ODE consequences close algebraically once the KMS majorant inequality is assumed. The restricted packet does not provide the KMS paper or any retained-grade upstream authority proving that inequality, so the load-bearing external"*

with repair: *"missing_dependency_edge: include the KMS arXiv:2404.06099 theorem statement/proof excerpt or a retained upstream authority row establishing the BBF majorant inequality and hypotheses."*

Supplying the named upstream authority is substantive new work, out of scope.
This revision narrows via the **admission path**:

- **Load-bearing (in scope):** The scalar majorant ODE `dy/dl = a y^2 + b y` closes algebraically and numerically — small-data integrability, monotonicity, scale-chaining, and the fixed-point structure are all verified by the runner GIVEN the KMS per-scale bound as input.
- **NON-load-bearing (admitted / unsupplied):** The KMS arXiv:2404.06099 Theorem 1 majorant inequality itself — specifically, that the BBF polymer norm satisfies `d/dl ||V_l||_h <= a(l) ||V_l||_h^2 + b(l) ||V_l||_h` with `a(l), b(l)` non-negative and integrable — is admitted as an unsupplied external input; the row does not certify it and no retained upstream authority row for it is present in the restricted packet.

No new axiom, import, or retained bridge is introduced. The conditional core is
the load-bearing content; the named upstream stays admitted until a retained
authority/runner for it lands.

## Scope Repair

The prior version tried to register the Kroschinsky-Marchetti-Salmhofer (KMS)
fermionic Polchinski/BBF majorant theorem as a load-bearing external theorem.
Audit correctly rejected that restricted packet because it did not include or
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
- It does not apply an audit verdict.

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
TOTAL: PASS=18, FAIL=0
```
