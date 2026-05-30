# DM Leptogenesis Expansion Boundary

**Date:** 2026-04-16
**Claim type:** bounded_theorem
**Primary runner:** `scripts/frontier_dm_leptogenesis_expansion_axiom_boundary.py`
**Framework baseline:** one-qubit operator algebra / physical `Cl(3)` local
algebra on the `Z^3` spatial substrate; this row does not add or restate a
repo-wide axiom.

## Scope Repair

The runner no longer asserts the load-bearing boundary collapse with
hard-coded `True` checks. It now computes
`eta[H]` from the exact package, equilibrium factors, and direct Boltzmann
transport solve for a supplied normalized expansion profile `E_H(z)`. It
checks that the same supplied profile gives the same `eta`, that a different
normalized profile changes `eta`, and that the radiation-branch output agrees
with the transport-decomposition theorem's recorded radiation-branch readout.

## Result

Given the following source/transport components as inputs:

- the source package
- the transfer coefficients
- the projection law
- the coherent kernel
- the equilibrium conversion factors
- the direct transport integral

the single remaining non-framework-baseline input is now:

- `H_rad(T)`

equivalently:

- the normalized expansion profile `E_H(z)` together with its normalization at
  `z = 1`

This is sharper than the older boundary

- `T_rad(K) = 7.04 * C_sph * d_th * kappa_fit(K)`

because the bookkeeping factors and the fit are no longer part of the
authority path.

## Why the boundary remains

The current source packet still does not carry a strict theorem-grade
radiation-era expansion law from the framework baseline alone. The older
`H(T)` lane still uses a bounded `k = 0` sub-assumption, so full theorem
closure cannot yet be claimed.

Given `H_rad(T)`, however, the transport package now recomputes `eta`
deterministically from the supplied expansion profile.

## Executable Repair Of The Boundary Claim

The repaired runner proves the boundary statement in the restricted,
executable sense:

```text
eta[H] = (s/n_gamma) * C_sph * d_N * epsilon_1 * kappa_axiom[H],
```

where `kappa_axiom[H]` is obtained by solving the normalized heavy-basis
Boltzmann transport ODE on the supplied expansion profile. The result is not a
fit and not a printed benchmark: `eta[H]` is recomputed from the ODE output.

The runner performs three checks that replace the former asserted boundary:

1. running the same `E_H(z)=1` branch twice gives the same `eta[H_rad]`;
2. replacing it with a positive normalized nonconstant profile with `E_H(1)=1`
   changes the computed `eta`;
3. the radiation-branch value agrees with the transport-decomposition theorem
   readout `eta[H_rad]/eta_obs = 0.188785929502`. This is a consistency
   comparator against the already-recorded transport readout, not a fitted or
   observational match claim.

This proves that the remaining datum for this boundary row is the supplied
expansion profile and its normalization, not an additional hidden fit factor.

## One-Hop Repair Links

- [DM_LEPTOGENESIS_TRANSPORT_DECOMPOSITION_THEOREM_NOTE_2026-04-16.md](DM_LEPTOGENESIS_TRANSPORT_DECOMPOSITION_THEOREM_NOTE_2026-04-16.md)
  derives the factorization of `eta[H]` and identifies `kappa_axiom[H]` as
  the unique remaining transport functional.
- [DM_LEPTOGENESIS_TRANSPORT_INTEGRAL_THEOREM_NOTE_2026-04-16.md](DM_LEPTOGENESIS_TRANSPORT_INTEGRAL_THEOREM_NOTE_2026-04-16.md)
  derives the direct ODE/formal-integral equivalence used to compute
  `kappa_axiom[H]`.
- [DM_LEPTOGENESIS_HRAD_THEOREM_NOTE_2026-04-16.md](DM_LEPTOGENESIS_HRAD_THEOREM_NOTE_2026-04-16.md)
  supplies the candidate radiation-branch profile `E_H(z)=1`. This row does
  not require that candidate profile to be accepted before it can check the
  narrower conditional boundary: if `E_H` is supplied, `eta[H]` is fixed by
  the direct transport solve.

## What This Does Not Close

- It does not by itself derive or accept the radiation-expansion theorem.
- It does not close the DM flagship lane or any right-sensitive microscopic
  selector law.
- It does not convert `eta[H_rad]/eta_obs = 0.188785929502` into an observed
  match; that value is a radiation-branch readout, not a fit target.
