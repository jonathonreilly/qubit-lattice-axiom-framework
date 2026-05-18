# Newton-Poisson → Flat First Friedmann Law — Named Non-Derivation Import

**Date:** 2026-05-17
**Claim type:** bounded_theorem
**Status:** bounded named-import wrapper. The flat first Friedmann law

```
H^2 = (8 pi G / 3) rho
```

on a spatially flat (k = 0) homogeneous-isotropic slice is a textbook
Newton-Poisson reduction (Milne 1934, McCrea & Milne 1934), recovered
in the appropriate symmetric limit of General Relativity. This note
records that reduction as a named non-derivation import so downstream
rows that consume the flat first Friedmann law can register this
wrapper as their one-hop dependency.
**Status authority:** independent audit lane only.

## Purpose

This wrapper note documents the Newton-Poisson reduction to the flat
first Friedmann law as a named import so downstream rows (notably
`dm_leptogenesis_hrad`) can register a one-hop dependency rather than
carry the reduction as an unattributed step.

## The reduction

Hypotheses:

- Spatial flatness `k = 0` on the homogeneous-isotropic spatial slice.
- Newtonian gravitational potential `Phi` satisfying the Poisson
  equation `nabla^2 Phi = 4 pi G rho` in the symmetric limit, with `G`
  the Newton constant and `rho` the homogeneous energy density.
- Pressureless dust or radiation fluid on the slice, with continuity
  equation `dot rho + 3 H (1 + w) rho = 0` for equation-of-state `w`
  (equivalently `rho a^(3(1+w)) = constant` when `w` is constant).

Conclusion (textbook Milne / McCrea-Milne):

```
H^2 = (8 pi G / 3) rho                                                (F1)
```

with `H := a' / a` the Hubble rate. Equation `(F1)` is the flat first
Friedmann law.

The standard Milne-McCrea Newtonian derivation considers a uniform
expanding ball of radius `R(t) = a(t) R_0` containing total mass
`M = (4 pi / 3) rho R^3`. Newton's shell theorem gives the
gravitational acceleration of a surface element as `R'' = - G M / R^2`,
which on substituting `R = a R_0` and simplifying gives the second
Friedmann acceleration equation `a'' / a = - (4 pi G / 3) rho`. The
first Friedmann law `(F1)` then follows from a first integral of this
second-order equation, with integration constant fixed to zero by the
flatness assumption `k = 0`.

The same `(F1)` is recovered as the symmetric limit of the
`G_{0 0}` Einstein equation on a flat FRW slice in General Relativity
(textbook General-Relativistic cosmology).

## What this note does NOT claim

- This is NOT a derivation of `(F1)` from `Cl(3)` on `Z^3` axioms.
- This is NOT a derivation of the Newton-Poisson equation itself or
  the Newton constant `G`; those are separately documented (see e.g.
  [GRAVITY_CLEAN_DERIVATION_NOTE.md](GRAVITY_CLEAN_DERIVATION_NOTE.md)
  and the
  [G_NEWTON_MASS_LINEAR_POISSON_COMPOSITION_BOUNDED_THEOREM_NOTE_2026-05-10.md](G_NEWTON_MASS_LINEAR_POISSON_COMPOSITION_BOUNDED_THEOREM_NOTE_2026-05-10.md)
  Born-source composition wrapper).
- This wrapper does NOT close `k = 0` from `Cl(3)` on `Z^3`; the
  flatness premise is recorded as the separate
  [CUBIC_COXETER_REGGE_DEFICIT_VANISHING_NARROW_THEOREM_NOTE_2026-05-10.md](CUBIC_COXETER_REGGE_DEFICIT_VANISHING_NARROW_THEOREM_NOTE_2026-05-10.md)
  narrow theorem (Regge deficit = 0 ⇒ flat coarse-grained spatial slice).
- The bounded scope is the named non-derivation import only.

## Standard textbook references

- E. A. Milne, "A Newtonian expanding universe," *Quart. J. Math.*
  **5**, 64–72 (1934).
- W. H. McCrea & E. A. Milne, "Newtonian universes and the curvature of
  space," *Quart. J. Math.* **5**, 73–80 (1934).
- Weinberg, *Cosmology* (Oxford 2008), §1.5.
- Mukhanov, *Physical Foundations of Cosmology* (Cambridge 2005),
  Ch. 1.
- Kolb & Turner, *The Early Universe* (Addison-Wesley 1990), §3.2.

## Downstream usage

This wrapper is consumed by:

- [DM_LEPTOGENESIS_HRAD_THEOREM_NOTE_2026-04-16.md](DM_LEPTOGENESIS_HRAD_THEOREM_NOTE_2026-04-16.md) — combines `(F1)` with the radiation density `rho_rad(T) = (pi^2 / 30) g_* T^4` to obtain `H_rad(T) = sqrt(4 pi^3 g_* / 45) T^2 / M_Pl` on the flat FRW slice.

## Boundary

This wrapper note is a named-import-only bounded theorem. It does not
claim:

- a framework derivation of the Newton-Poisson equation;
- a framework derivation of General Relativity on `Z^3`;
- closure of any downstream DM-leptogenesis theorem.

Its only function is to provide a citeable one-hop authority for the
Newton-Poisson → flat first Friedmann reduction so downstream notes
register the import cleanly instead of carrying it as an unattributed
textbook step.
