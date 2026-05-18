# DM Thermal Average + Sommerfeld Argument Normalization — Named Non-Derivation Import

**Date:** 2026-05-17
**Claim type:** bounded_theorem
**Status:** bounded named-import wrapper for the textbook
Maxwell-Boltzmann thermal-velocity average on the freeze-out slice
`x_f = 25` and the standard Sommerfeld-enhancement argument
normalization used by the same-surface thermal continuum integral.
**Status authority:** independent audit lane only.

## Purpose

This wrapper note documents the textbook ingredients consumed by the
same-surface DM thermal closure layer as named non-derivation imports
so downstream rows (notably
[DM_FULL_CLOSURE_SAME_SURFACE_THERMAL_INTEGRAL_REPRESENTATION_THEOREM_NOTE_2026-04-16.md](DM_FULL_CLOSURE_SAME_SURFACE_THERMAL_INTEGRAL_REPRESENTATION_THEOREM_NOTE_2026-04-16.md))
can register a one-hop dependency rather than carry the textbook
ingredients as unattributed constants.

## Ingredients covered

This wrapper bundles three textbook DM-relic-abundance ingredients:

### 1. Maxwell-Boltzmann thermal-velocity average

For a non-relativistic species `chi` of mass `m_chi` in thermal
equilibrium at temperature `T`, the velocity distribution is the
Maxwell-Boltzmann distribution

```
f_MB(v)  ~  v^2  exp( - m_chi v^2 / (2 T) ).
```

The thermal average of a velocity-dependent cross section
`sigma v(v)` is

```
< sigma v >(T)  =  int dv  f_MB(v)  sigma v(v)  /  int dv  f_MB(v).
```

This is the standard Gondolo-Gelmini thermal-average formula
(Gondolo & Gelmini 1991) and is textbook DM relic-abundance machinery.

### 2. Freeze-out slice `x_f = 25`

The dimensionless temperature ratio `x := m_chi / T` parameterizes the
expansion of the radiation-dominated era. Standard relic-abundance
analysis on the s-wave or generic-perturbative annihilation channels
gives a numerical freeze-out solution

```
x_f  =  m_chi / T_f  ~~  25
```

for weak-scale DM masses and generic relic-density target. This value
is a textbook benchmark, recovered repeatedly in standard treatments
(Kolb-Turner Ch. 5; Bertone-Hooper-Silk *Phys. Rept.* 2005).

For the same-surface DM thermal closure layer, `x_f = 25` is used as
the canonical freeze-out slice on which the framework's Sommerfeld
average is evaluated.

### 3. Sommerfeld argument normalization

The Sommerfeld enhancement factor `S(z)` for an attractive Coulombic
exchange of effective coupling `alpha_eff` is a standard textbook
result (Sommerfeld 1931; Hisano-Matsumoto-Nojiri *Phys. Rev. D* 2003;
Iengo *JHEP* 2009):

```
S(z)  :=  enhancement factor at relative velocity v_rel,
z      :=  alpha_eff / v_rel    (dimensionless Sommerfeld argument).
```

For the same-surface integral representation, the load-bearing
substitution is the Maxwell-Boltzmann variable change
`v -> sqrt(2 T / m_chi) sqrt(t)` which puts the thermal average in
canonical Gaussian form:

```
< S >  =  (2 / sqrt(pi))  int_0^infinity  S( alpha_eff sqrt(a) / sqrt(t) )  sqrt(t)  exp(-t)  dt,
```

with `a := x_f / 4 = 25 / 4` on the canonical freeze-out slice. The
two low-order moments

```
< 1 / v >    =  2 sqrt(a) / sqrt(pi)   =  5 / sqrt(pi),
< 1 / v^2 >  =  2 a                    =  25 / 2,
```

are exact consequences of the Maxwell-Boltzmann normalization on this
slice.

## What this note does NOT claim

- This is NOT a derivation of the Maxwell-Boltzmann distribution from
  `Cl(3)` on `Z^3` axioms.
- This is NOT a derivation of the value `x_f = 25` from the framework.
- This is NOT a derivation of the Sommerfeld enhancement factor from
  `Cl(3)` on `Z^3` axioms.
- The bounded scope is the named non-derivation import only.

## Standard textbook references

- Kolb & Turner, *The Early Universe* (Addison-Wesley 1990), Ch. 5
  (relic abundance, freeze-out, thermal average).
- Gondolo & Gelmini, "Cosmic Abundances of Stable Particles: Improved
  Analysis," *Nucl. Phys. B* **360**, 145 (1991).
- Bertone, Hooper & Silk, "Particle Dark Matter: Evidence, Candidates
  and Constraints," *Phys. Rept.* **405**, 279 (2005).
- Sommerfeld, *Ann. Phys.* **403**, 257 (1931); Hisano, Matsumoto &
  Nojiri, *Phys. Rev. D* **67**, 075014 (2003); Iengo, *JHEP* **05**,
  024 (2009).

## Downstream usage

This wrapper is consumed by:

- [DM_FULL_CLOSURE_SAME_SURFACE_THERMAL_INTEGRAL_REPRESENTATION_THEOREM_NOTE_2026-04-16.md](DM_FULL_CLOSURE_SAME_SURFACE_THERMAL_INTEGRAL_REPRESENTATION_THEOREM_NOTE_2026-04-16.md) — the continuum integral form `<S> = (2/sqrt(pi)) ∫_0^∞ S(alpha_eff*sqrt(a)/sqrt(t)) sqrt(t) e^{-t} dt`, the slice `a = x_f / 4 = 25 / 4`, and the moment data `<1/v> = 5/sqrt(pi)`, `<1/v^2> = 25/2`.
- [DM_FULL_CLOSURE_SAME_SURFACE_THERMAL_MONOTONICITY_THEOREM_NOTE_2026-04-17.md](DM_FULL_CLOSURE_SAME_SURFACE_THERMAL_MONOTONICITY_THEOREM_NOTE_2026-04-17.md) — uses the same thermal-average machinery as a downstream consumer.
- [DM_FULL_CLOSURE_SAME_SURFACE_THERMAL_SERIES_TAIL_SUPPORT_NOTE_2026-04-17.md](DM_FULL_CLOSURE_SAME_SURFACE_THERMAL_SERIES_TAIL_SUPPORT_NOTE_2026-04-17.md) — uses the same Maxwell-Boltzmann normalization.

## Boundary

This wrapper note is a named-import-only bounded theorem covering the
three textbook ingredients above. It does not claim:

- a framework derivation of any of the imported textbook ingredients;
- closure of any downstream DM-leptogenesis or DM-thermal theorem;
- a tighter audit-tier status for the consumers.

Its only function is to provide a citeable one-hop authority for the
Maxwell-Boltzmann thermal-velocity average, the freeze-out slice value
`x_f = 25`, and the Sommerfeld argument normalization so downstream
notes register the imports cleanly instead of carrying them as
unattributed constants.
