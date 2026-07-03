# Free-Scalar Point-Split Ward Seagull Diagnostic

**Date:** 2026-06-08
**Claim type:** bounded_theorem / finite lattice Ward diagnostic
**Status authority:** independent audit lane only. This source note writes no
audit verdict and does not retag any ledger row.
**Primary runner:** [`scripts/free_scalar_point_split_ward_seagull_diagnostic_2026_06_08.py`](../scripts/free_scalar_point_split_ward_seagull_diagnostic_2026_06_08.py)
**Runner cache:** [`logs/runner-cache/free_scalar_point_split_ward_seagull_diagnostic_2026_06_08.txt`](../logs/runner-cache/free_scalar_point_split_ward_seagull_diagnostic_2026_06_08.txt)

## Summary

This note narrows the R2 stress-conservation branch to a concrete finite
diagnostic. For the free nearest-neighbor scalar lattice inverse propagator

```text
G^-1(p) = m^2 + sum_mu (2 sin(p_mu/2))^2,
```

the point-split vertex

```text
V^mu(p,q) = 2 sin(p_mu + q_mu/2)
```

satisfies the exact lattice Ward identity

```text
qhat_mu V^mu(p,q) = G^-1(p+q) - G^-1(p),
qhat_mu = 2 sin(q_mu/2).
```

The same computation shows that the naive local vertex `2 sin(p_mu)` fails this
identity, and that the failure is exactly minus the point-split-minus-naive
seagull term. This is useful evidence that a contact term in a lattice Ward
calculation can be the required point-splitting seagull rather than a genuine
non-conservation.

## Theorem (Bounded Finite Diagnostic)

- **T1:** for 20,000 random momenta in the runner's `d=4` free scalar lattice
  model, the point-split vertex satisfies the displayed Ward identity to
  machine precision.
- **T2:** for 5,000 random momenta, the naive local vertex has nonzero Ward
  residual and that residual equals `-qhat dot (V_point_split - V_naive)` to
  machine precision.
- **T3:** the source note carries explicit guardrails preventing this diagnostic
  from being read as the full framework stress-tensor, cubic-seagull,
  Belinfante, diffeomorphism, or gravity-sign closure.

`TOTAL: PASS=3 FAIL=0`.

## What This Establishes

The row establishes an exact algebraic identity in a free scalar lattice model:
the point-split current satisfies the lattice Ward identity, while the naive
current's failure is exactly accounted for by the point-split seagull.

That is the durable science worth preserving from the branch. It is a concrete
model for how a lattice contact term can be required by a conserved
point-split current.

## What Remains Open

- Framework-native stress tensor conservation for the actual interacting
  Dirac/qubit matter sector.
- The explicit cubic three-point Noether seagull matching the prior cubic-Ward
  contact.
- Belinfante symmetrization or emergent rotation invariance.
- Spin-2 gauge invariance, diffeomorphism closure, `lambda=1`, or the gravity
  sign.
- Any statement that exact `Z^3` lattice structure alone supplies a conserved
  stress tensor for arbitrary downstream actions.

## Relation to Inventory

This note is a bounded diagnostic for the R2 route. It may guide a later
framework-native cubic seagull construction, but it does not close that
construction and does not promote neighboring universal-GR rows.

## Honest Auditor Read

Audit this as a free-scalar lattice Ward identity and seagull diagnostic. The
runner genuinely checks the algebra over random momenta and verifies the
guardrail text. It should not be read as proof that the framework's full stress
tensor is conserved, that the prior cubic contact has been matched, or that the
spin-2/diffeomorphism/gravity-sign chain closes.
