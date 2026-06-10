# `g_*` Thermal `7/8` Stefan-Boltzmann Integral Bridge

**Date:** 2026-06-06
**Claim type:** bounded_theorem
**Status authority:** source-note proposal only; audit verdict and effective
status are set by the independent audit lane.
**Primary runner:**
[`scripts/audit_companion_gstar_thermal_seven_eighths_bridge_2026_06_06.py`](../scripts/audit_companion_gstar_thermal_seven_eighths_bridge_2026_06_06.py)
**Cached log:**
[`logs/runner-cache/audit_companion_gstar_thermal_seven_eighths_bridge_2026_06_06.txt`](../logs/runner-cache/audit_companion_gstar_thermal_seven_eighths_bridge_2026_06_06.txt)

## Claim

For a relativistic, effectively massless thermal degree of freedom at zero
chemical potential in `3+1` dimensions, the Fermi-Dirac energy-density integral
is exactly `7/8` of the Bose-Einstein energy-density integral:

```text
I_B = int_0^infty x^3/(e^x - 1) dx = Gamma(4) zeta(4) = pi^4/15,
I_F = int_0^infty x^3/(e^x + 1) dx = Gamma(4) eta(4)  = 7 pi^4/120,
I_F / I_B = eta(4)/zeta(4) = 7/8.
```

Therefore, per internal relativistic degree of freedom in natural units,

```text
rho_B,per-dof = (1/(2 pi^2)) T^4 I_B = (pi^2/30) T^4,
rho_F,per-dof = (1/(2 pi^2)) T^4 I_F = (7/8) (pi^2/30) T^4.
```

This supplies the direct Stefan-Boltzmann / thermal-integral bridge for the
fermion weight in
`G_STAR_SM_CONTENT_AT_LEPTOGENESIS_FROM_SUPPLIED_THERMAL_INVENTORY_BOUNDED_THEOREM_NOTE_2026-05-28.md`.

## Hypotheses

This theorem uses only the standard thermal integral hypotheses needed by the
`g_*` bookkeeping:

- relativistic/massless dispersion in the thermal regime being counted;
- zero chemical potential for the inventory count;
- natural units `k_B = hbar = c = 1`;
- one internal degree of freedom at a time, so all spin/color/flavor/gauge
  multiplicities are counted separately by the parent inventory note.

It does not derive the Standard Model particle inventory, thermal equilibrium,
or which species are relativistic at the chosen temperature.

## Proof

For `s > 1`, expand the Bose and Fermi factors as absolutely convergent
exponential series under the integral:

```text
1/(e^x - 1) = sum_{n>=1} e^{-nx},
1/(e^x + 1) = sum_{n>=1} (-1)^(n-1) e^{-nx}.
```

The elementary Gamma integral gives

```text
int_0^infty x^3 e^{-nx} dx = Gamma(4)/n^4 = 6/n^4.
```

Thus

```text
I_B = sum_{n>=1} 6/n^4 = 6 zeta(4) = pi^4/15,
I_F = sum_{n>=1} 6 (-1)^(n-1)/n^4 = 6 eta(4).
```

Using `eta(s) = (1 - 2^(1-s)) zeta(s)` at `s=4`,

```text
eta(4) = (1 - 2^(-3)) zeta(4) = (7/8) zeta(4),
I_F = (7/8) I_B = 7 pi^4/120.
```

Multiplying by the common phase-space prefactor `(1/(2 pi^2)) T^4` gives the
per-degree coefficients in the claim. This is the standard
Stefan-Boltzmann thermal-integral origin of the `7/8` fermion factor used in
`g_* = N_bosons + (7/8) N_fermions`.

## What This Supplies

- A direct thermal-integral authority for the `7/8` fermion weight in the
  supplied Standard Model inventory proof-walk.
- A source-local bridge parallel to, but distinct from,
  [`HIERARCHY_SEVEN_EIGHTHS_RIEMANN_DIRICHLET_DIMENSIONAL_ANCHOR_NARROW_THEOREM_NOTE_2026-05-10.md`](HIERARCHY_SEVEN_EIGHTHS_RIEMANN_DIRICHLET_DIMENSIONAL_ANCHOR_NARROW_THEOREM_NOTE_2026-05-10.md).
  The hierarchy note proves a `d=4` eta/zeta arithmetic coincidence; this note
  proves the thermodynamic Stefan-Boltzmann ratio actually consumed by `g_*`.

## Boundaries

This note does not close:

- the Standard Model particle inventory;
- the two-transverse-polarization premise for massless gauge bosons;
- the four-real-component premise for the Higgs doublet;
- the Dirac/Weyl state-counting premises;
- thermal-equilibrium dynamics or decoupling thresholds;
- downstream cosmology claims consuming `g_*`.

No new axiom, fitted number, observed comparator, lattice Monte Carlo input,
`g_bare`, `beta=6`, or action-level premise is introduced.

## Verification

```bash
python3 scripts/audit_companion_gstar_thermal_seven_eighths_bridge_2026_06_06.py
```

Expected result: all checks pass, including exact symbolic identities for
`I_B`, `I_F`, the `7/8` ratio, and the `g_* = 427/4` weighted arithmetic when
combined with the parent inventory counts `N_bosons=28` and `N_fermions=90`.
