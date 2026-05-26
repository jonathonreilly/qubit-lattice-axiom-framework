# DM Thermal Average + Sommerfeld Argument Normalization — Named Non-Derivation Import

**Date:** 2026-05-17
**Claim type:** bounded_theorem
**Status:** bounded normalization packet for the Maxwell-Boltzmann
thermal-velocity average at the explicit benchmark slice `x_f = 25` and for
the Sommerfeld argument change of variables used by the same-surface thermal
continuum integral.
**Status authority:** independent audit lane only.
**Primary runner:** [`scripts/dm_thermal_average_sommerfeld_normalization.py`](../scripts/dm_thermal_average_sommerfeld_normalization.py)
**Runner cache:** [`logs/runner-cache/dm_thermal_average_sommerfeld_normalization.txt`](../logs/runner-cache/dm_thermal_average_sommerfeld_normalization.txt)

## Purpose

This wrapper note documents the finite normalization algebra consumed by the
same-surface DM thermal closure layer so downstream rows (notably
`DM_FULL_CLOSURE_SAME_SURFACE_THERMAL_INTEGRAL_REPRESENTATION_THEOREM_NOTE_2026-04-16.md`)
can register a one-hop dependency rather than carry the normalization
constants as unattributed inputs.

The repair narrows the previous textbook-import scope. The packet now proves
the Maxwell-Boltzmann variable change and low-order moments at the explicit
benchmark `x_f = 25`; it does not prove freeze-out physics, derive the
Maxwell-Boltzmann distribution from framework axioms, or derive the
Sommerfeld enhancement law.

## Ingredients covered

This wrapper bundles three bounded inputs:

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

The primary runner verifies the normalization denominator and the `t = a v^2`
change of variables used below.

### 2. Freeze-out slice `x_f = 25`

The dimensionless temperature ratio `x := m_chi / T` parameterizes the
thermal slice. This packet takes

```
x_f  =  m_chi / T_f  :=  25
```

as an explicit benchmark slice. The value `25` is not derived here and is not
promoted to framework authority; the auditable claim is the normalization
algebra conditional on evaluating at that benchmark.

### 3. Sommerfeld argument normalization

The Sommerfeld enhancement factor `S(z)` itself is not derived in this note.
The bounded packet only fixes the dimensionless argument convention:

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

## Runner-backed certificate

The primary runner checks the following finite algebraic facts:

- `int_0^infinity v^2 exp(-a v^2) dv = sqrt(pi)/(4 a^(3/2))`;
- `<1/v> = 2 sqrt(a)/sqrt(pi)`, giving `5/sqrt(pi)` at `x_f=25`;
- `<1/v^2> = 2a`, giving `25/2` at `x_f=25`;
- with `t = a v^2`, the Sommerfeld argument transforms as
  `alpha_eff/v = alpha_eff sqrt(a/t)`;
- the normalized thermal-average `t`-measure carries prefactor
  `1/Gamma(3/2) = 2/sqrt(pi)`.

This is a direct normalization certificate. It is not a literature authority
for freeze-out dynamics.

## What this note does NOT claim

- This is NOT a derivation of the Maxwell-Boltzmann distribution from
  `Cl(3)` on `Z^3` axioms.
- This is NOT a derivation of the value `x_f = 25` from the framework.
- This is NOT a derivation of the Sommerfeld enhancement factor from
  `Cl(3)` on `Z^3` axioms.
- The bounded scope is the normalization algebra at the explicit benchmark
  slice.

## Context references

The following references are context for the named physics conventions; the
load-bearing audit packet is the runner-backed normalization certificate
above.

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

This wrapper is consumed by (see-also pointers; backticked to break
cycle-0009 / cycle-0010 / cycle-0011 / cycle-0012 / cycle-0013 in the
citation graph — the load-bearing direction is downstream-theorem ->
this textbook import, not the reverse):

- `DM_FULL_CLOSURE_SAME_SURFACE_THERMAL_INTEGRAL_REPRESENTATION_THEOREM_NOTE_2026-04-16.md` — the continuum integral form `<S> = (2/sqrt(pi)) ∫_0^∞ S(alpha_eff*sqrt(a)/sqrt(t)) sqrt(t) e^{-t} dt`, the slice `a = x_f / 4 = 25 / 4`, and the moment data `<1/v> = 5/sqrt(pi)`, `<1/v^2> = 25/2`.
- `DM_FULL_CLOSURE_SAME_SURFACE_THERMAL_MONOTONICITY_THEOREM_NOTE_2026-04-17.md` — uses the same thermal-average machinery as a downstream consumer.
- `DM_FULL_CLOSURE_SAME_SURFACE_THERMAL_SERIES_TAIL_SUPPORT_NOTE_2026-04-17.md` — uses the same Maxwell-Boltzmann normalization.

## Boundary

This wrapper note is a bounded normalization theorem covering the finite
algebra above. It does not claim:

- a framework derivation of any of the imported textbook ingredients;
- closure of any downstream DM-leptogenesis or DM-thermal theorem;
- a tighter audit-tier status for the consumers.

Its only function is to provide a citeable one-hop authority for the
Maxwell-Boltzmann thermal-velocity normalization, the declared benchmark
evaluation `x_f = 25`, and the Sommerfeld argument variable change so
downstream notes register the finite normalization inputs cleanly instead of
carrying them as unattributed constants.
