# Koide MRU Reduced Two-Slot Log-Volume Identity

**Date:** 2026-04-19; reduced-log-volume repair 2026-05-25
**Status:** bounded-support formal reduced-carrier algebra. No physical SO(2)-quotient, scalar charged-lepton lane, or operator-side kappa closure is part of the binding theorem.
**Status authority:** independent audit lane only.
**Claim type:** bounded_theorem
**Primary runner:** `scripts/frontier_koide_mru_reduced_log_volume_repair.py`

## Actual claim

Let `rho_plus > 0` and `rho_perp > 0` be two positive formal coordinates, and fix:

```text
rho_plus^2 + rho_perp^2 = E_tot > 0.
```

On this explicitly reduced two-slot carrier, the log-volume functional

```text
L = log(rho_plus) + log(rho_perp)
```

has its unique interior constrained extremum at:

```text
rho_plus^2 = rho_perp^2 = E_tot / 2.
```

If one defines:

```text
kappa := 2 rho_plus^2 / rho_perp^2,
```

then the extremum gives:

```text
kappa = 2.
```

That formal reduced-carrier identity is the entire repaired theorem.

## Why this repair is narrow

The prior audit verdict accepted the post-quotient algebra but marked the row conditional because the physical step was an admitted bridge:

- charged-lepton scalar observables were assumed to factor through an SO(2) doublet-radius quotient;
- the row then applied the reduced log-volume law to that quotient.

This repair withdraws the physical quotient from the binding claim. It proves only the formal two-variable constrained extremum and the resulting `kappa = 2` identity under the explicit definition above.

## Theorem

**Theorem.** On the positive quadrant with fixed `E_tot > 0`, the constrained extremum of

```text
L(rho_plus, rho_perp) = log(rho_plus) + log(rho_perp)
```

subject to

```text
rho_plus^2 + rho_perp^2 = E_tot
```

occurs uniquely at `rho_plus = rho_perp = sqrt(E_tot / 2)`. With
`kappa := 2 rho_plus^2 / rho_perp^2`, the extremal value is `kappa = 2`.

**Proof.** Use a Lagrange multiplier:

```text
F = log(rho_plus) + log(rho_perp)
    - lambda (rho_plus^2 + rho_perp^2 - E_tot).
```

Stationarity gives:

```text
1/rho_plus = 2 lambda rho_plus,
1/rho_perp = 2 lambda rho_perp.
```

Since both variables are positive, the equations imply
`1/rho_plus^2 = 1/rho_perp^2`, hence:

```text
rho_plus^2 = rho_perp^2.
```

The constraint gives `rho_plus^2 = rho_perp^2 = E_tot/2`. On the closure of the fixed-energy arc, the log-volume tends to `-infinity` at the boundary endpoints, so the interior stationary point is the unique maximum. Therefore:

```text
kappa = 2 (E_tot/2) / (E_tot/2) = 2.
```

QED.

## What this row does not claim

- It does not derive the physical SO(2)-quotient.
- It does not show that charged-lepton scalar observables factor through `rho_perp`.
- It does not derive operator-side `kappa = 2` in the framework.
- It does not use charged-lepton masses or observational matching.
- It does not add an axiom or apply an audit verdict.

The physical bridge from this formal reduced-carrier identity to the charged-lepton scalar lane remains a separate open science problem.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_koide_mru_reduced_log_volume_repair.py
```

Expected result:

```text
Koide MRU reduced log-volume repair
TOTAL: PASS=23 FAIL=0
```
