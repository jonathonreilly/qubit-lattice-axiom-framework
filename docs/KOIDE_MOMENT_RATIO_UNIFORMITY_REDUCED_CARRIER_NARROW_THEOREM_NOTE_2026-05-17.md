# Koide MRU Reduced-Carrier Formal Corollary

**Date:** 2026-05-17; formal-scope repair 2026-05-27
**Type:** bounded_theorem
**Status authority:** independent audit lane only.
**Primary runner:** [`scripts/audit_companion_koide_mru_reduced_carrier_post_quotient_algebra.py`](../scripts/audit_companion_koide_mru_reduced_carrier_post_quotient_algebra.py)

## Claim Scope

This row is a formal two-variable corollary of two retained bounded algebra
surfaces:

- the formal reduced two-slot log-volume identity in
  [`KOIDE_MOMENT_RATIO_UNIFORMITY_THEOREM_NOTE_2026-04-19.md`](KOIDE_MOMENT_RATIO_UNIFORMITY_THEOREM_NOTE_2026-04-19.md);
- the block-total Frobenius identities in
  [`KOIDE_KAPPA_BLOCK_TOTAL_FROBENIUS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md`](KOIDE_KAPPA_BLOCK_TOTAL_FROBENIUS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md).

No physical SO(2) frame quotient, charged-lepton scalar-lane reduction,
operator-side readout, mass identification, or Standard Model matching is
part of the binding claim.

## Statement

Let `rho_+ > 0`, `rho_perp > 0`, and `E_tot > 0` be formal variables with

```text
rho_+^2 + rho_perp^2 = E_tot.
```

The retained reduced log-volume identity gives the unique interior
critical point of

```text
S_rho = log rho_+ + log rho_perp
```

on this positive two-slot carrier:

```text
rho_+^2 = rho_perp^2 = E_tot / 2.                         (P1)
```

Now introduce formal Frobenius coordinates `E_+` and `E_perp` by the
positive change of variables

```text
E_+ = rho_+^2,
E_perp = rho_perp^2.
```

Using the retained block-total Frobenius identities for
`H = a I + b C + bbar C^2 in Herm_circ(3)`,

```text
E_+(H) = 3 a^2,
E_perp(H) = 6 |b|^2,
```

the formal reduced-carrier critical point is equivalent to

```text
E_+ = E_perp = E_tot / 2,                                  (P2)
```

and therefore

```text
3 a^2 = 6 |b|^2,
a^2 = 2 |b|^2,
kappa := a^2 / |b|^2 = 2.                                  (P3)
```

The change of variables is monotone on the positive quadrant, and

```text
S_E(E_+, E_perp) := log E_+ + log E_perp = 2 S_rho.
```

Thus the formal reduced-carrier extremum and the formal Frobenius-carrier
extremum have the same critical point after `E_i = rho_i^2`.

## Proof

The Lagrangian for the formal reduced-carrier problem is

```text
L = log rho_+ + log rho_perp
    - lambda (rho_+^2 + rho_perp^2 - E_tot).
```

Stationarity gives

```text
1 / rho_+ = 2 lambda rho_+,
1 / rho_perp = 2 lambda rho_perp.
```

Since both variables are positive, `rho_+^2 = rho_perp^2`; the constraint
then gives `(P1)`. The Hessian of `S_rho` is

```text
diag(-1/rho_+^2, -1/rho_perp^2),
```

so the critical point is the unique strict maximum on the positive
constraint arc.

Substituting `E_i = rho_i^2` gives `(P2)`. Substituting the retained
Frobenius identities `E_+ = 3 a^2` and `E_perp = 6 |b|^2` into `(P2)`
gives `(P3)`.

Finally,

```text
log E_+ + log E_perp
  = log rho_+^2 + log rho_perp^2
  = 2 (log rho_+ + log rho_perp),
```

so the two formal extremum problems are equivalent up to multiplication of
the objective by the positive constant `2`.

## What This Claims

- The formal reduced-carrier log-volume extremum is equivalent to the
  retained formal Frobenius-carrier extremum after `E_i = rho_i^2`.
- At that formal critical point, the retained Frobenius identities imply
  `a^2 = 2 |b|^2` and `kappa = 2`.
- The runner checks the Lagrange equations, concavity, reparametrization
  equivalence, corollaries, and counterfactual tilts at exact symbolic
  precision.

## What This Does Not Claim

- It does not derive a physical SO(2) quotient.
- It does not assert that charged-lepton scalar observables factor through
  `(rho_+, rho_perp)`.
- It does not identify `(rho_+, rho_perp)`, `(E_+, E_perp)`, or `(a, b)`
  with physical charged-lepton masses or amplitudes.
- It does not close the parent physical charged-lepton Koide lane.
- It does not consume observed lepton masses, fitted selectors, or a new
  axiom.

The physical bridge from this formal two-variable corollary to the
charged-lepton scalar lane remains open.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/audit_companion_koide_mru_reduced_carrier_post_quotient_algebra.py
```

Expected result:

```text
TOTAL: PASS=35  FAIL=0
```
