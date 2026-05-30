# DM Leptogenesis `H_rad(T)` Radiation Branch Boundary

**Claim type:** open_gate
**Status:** open - radiation flat-Friedmann authority requires a retained
GR/pressure-source bridge; arithmetic below is conditional on that input.
**Date:** 2026-04-16 (2026-05-28: dependency-chain repair after the
Newton-Poisson wrapper was narrowed to dust only).
**Script:** `scripts/frontier_dm_leptogenesis_hrad_theorem.py`  
**Framework convention:** "axiom" means only `Cl(3)` on `Z^3`.

## 2026-05-28 Dependency-Chain Repair

The historical row used the Newton-Poisson flat-Friedmann wrapper as the
authority for the radiation-era expansion law. That is no longer a valid
dependency after
`NEWTON_POISSON_FLAT_FRIEDMANN_TEXTBOOK_IMPORT_NOTE_2026-05-17.md` was
narrowed to the pressureless dust first integral. The radiation law needs a
separate retained GR/pressure-source authority, because the Newtonian
rho-only acceleration gives half the radiation coefficient unless the
active-gravitational-mass term `rho + 3p` (or an equivalent GR `G_00`
authority) is supplied.

This source row is therefore an **open gate**: it keeps the exact conditional
arithmetic for `H_rad(T)` and the normalized transport profile, but it does
not claim that the radiation flat-Friedmann law is theorem-native from the
current dependency packet.

## Conditional Arithmetic

The exact chain is:

1. the axiom geometry `Z^3` is intrinsically flat
2. the homogeneous/isotropic spatial slice therefore has exact `k = 0`
3. a retained GR/pressure-source authority supplies the flat radiation
   Friedmann law `H^2 = (8 pi G / 3) rho_rad` (**open input; not supplied by
   the dust Newton-Poisson wrapper**)
4. the exact radiation density gives

   `rho_rad(T) = (pi^2/30) g_* T^4`

5. therefore

   `H_rad(T) = sqrt(4*pi^3*g_*/45) * T^2 / M_Pl`

with exact normalized transport profile

`E_H(z) = z^2 H(M1/z)/H(M1) = 1`.

## Why `k = 0` is no longer bounded

The old bounded lane treated `k = 0` as an external flatness assumption.
That spatial-flatness input is supported by the cubic-Regge dependency below.
This does **not** close the missing radiation Friedmann/pressure-source input.

On the cubic spatial tessellation of `Z^3`, each edge has four incident
square plaquettes with dihedral angle `pi/2`, so the Regge deficit is

`delta_e = 2*pi - 4*(pi/2) = 0`.

Hence the coarse-grained homogeneous/isotropic spatial curvature is exactly
zero on the axiom geometry.

## Conditional transport consequences

Conditional on the missing retained radiation Friedmann/pressure-source
authority, the following arithmetic objects are fixed:

- `H_rad(T)` itself
- `m_* = 8*pi*v^2*H_rad(T)/T^2`
- `K = m_tilde / m_*`

Numerically on the refreshed branch:

- `m_* = 0.0021417091151373236 eV`
- `K = 47.23597962989829`

They are not promoted by this row; they remain conditional on the open
radiation Friedmann authority.

## Main consequence for the closure path

The current direct transport solver was already using the normalized branch
`E_H(z) = 1`. This note records the conditional arithmetic for that branch.
The old final exact boundary on `H_rad(T)` is **not** removed until a retained
GR/pressure-source authority lands and audits clean.

## Upstream authority

- [CUBIC_COXETER_REGGE_DEFICIT_VANISHING_NARROW_THEOREM_NOTE_2026-05-10.md](CUBIC_COXETER_REGGE_DEFICIT_VANISHING_NARROW_THEOREM_NOTE_2026-05-10.md) — narrow theorem proving the cubic-Coxeter Regge deficit vanishes identically on `Z^3` (interior edges of every class), used here as the framework-side authority for the `k = 0` spatial-flatness input formerly carried as a bounded sub-assumption in step (2) of the chain.
- [SM_RELATIVISTIC_DOF_COUNT_IMPORT_NOTE_2026-05-17.md](SM_RELATIVISTIC_DOF_COUNT_IMPORT_NOTE_2026-05-17.md) — finite declared-inventory arithmetic certificate for the SM relativistic degrees-of-freedom count `g_* = 28 + (7/8) * 90 = 106.75` used in step (4) and propagated through step (5).
- [AXIOM_FIRST_STEFAN_BOLTZMANN_THEOREM_NOTE_2026-05-01.md](AXIOM_FIRST_STEFAN_BOLTZMANN_THEOREM_NOTE_2026-05-01.md) — framework-side Stefan-Boltzmann derivation for the `(pi^2 / 30)` per-DOF prefactor in the relativistic energy density `rho_rad(T) = (pi^2 / 30) g_* T^4` used in step (4).

Open input, deliberately not a markdown dependency until supplied:

- retained GR/pressure-source authority for the flat radiation Friedmann law
  `H^2 = (8 pi G / 3) rho_rad`.
