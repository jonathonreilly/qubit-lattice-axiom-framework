# Standard-Model Relativistic Degrees-of-Freedom Count — Named Non-Derivation Import

**Date:** 2026-05-17 (2026-05-26: self-contained bounded-import
bookkeeping runner added for audit requeue)
**Claim type:** bounded_theorem
**Status:** bounded named-import wrapper. The Standard-Model relativistic
degree-of-freedom count `g_* = 28 + (7/8) * 90 = 106.75` (28 bosonic, 90
fermionic at electroweak-scale relativistic temperatures) is a textbook
import from standard SM phenomenology; this note records it as a named
non-derivation import so downstream rows that consume `g_*` can register
this wrapper as their one-hop dependency.
**Runner:** `scripts/frontier_sm_relativistic_dof_count_import.py`
**Status authority:** independent audit lane only.

## 2026-05-26 bounded-import repair

The audit blocker was not the arithmetic `28 + (7/8) * 90 = 106.75`;
it was that the one-hop packet did not include a self-contained authority for
the Standard-Model particle-content bookkeeping that produces the numbers
`28` and `90`.

This repair keeps the same honest status: **named non-derivation import**.
It does not derive the Standard Model spectrum from `Cl(3)` on `Z^3`.
It does add a local runner that verifies the bounded import table below:

- bosons: `8` gluons with two transverse polarizations, `3` weak gauge
  bosons with two transverse polarizations, `1` hypercharge gauge boson with
  two transverse polarizations, and `4` real Higgs-doublet components;
- fermions: `6` quark flavors with `3` colors and `4` Dirac particle /
  antiparticle spin states, `3` charged leptons with `4` Dirac particle /
  antiparticle spin states, and `3` active neutrinos with `2` chiral particle /
  antiparticle states.

The runner checks only this bounded SM-bookkeeping import and the retained
`7/8` fermion/boson weighting. It is not a framework derivation of the SM
particle spectrum.

## Purpose

This wrapper note documents the SM relativistic DOF count as a named
import so downstream rows (notably `dm_leptogenesis_equilibrium_conversion`,
`dm_leptogenesis_hrad`, and various thermal-side dm_leptogenesis rows)
can register a one-hop dependency rather than carry the count as an
unattributed hard-coded constant.

## The count

At temperatures above the electroweak scale, the Standard Model has

```
g_*(T) = g_bosonic + (7/8) * g_fermionic
       = 28 + (7/8) * 90
       = 106.75
```

with bosonic count, in unbroken electroweak bookkeeping,
```
g_bosonic = 8 gluons * 2 transverse polarizations
           + 3 SU(2)_L gauge bosons * 2 transverse polarizations
           + 1 U(1)_Y gauge boson * 2 transverse polarizations
           + 4 real Higgs-doublet components
           = 28.
```

The broken-phase `photon/W/Z/Higgs` bookkeeping gives the same total
count but is only a bookkeeping equivalence at these temperatures.

The fermionic count is (3 generations, 2 helicities, particle +
antiparticle):
```
g_fermionic = 6 quark flavors * 3 colors * 4 Dirac states
            + 3 charged leptons * 4 Dirac states
            + 3 active neutrinos * 2 chiral particle/antiparticle states
            = 72 + 12 + 6
            = 90.
```

The (7/8) prefactor on the fermionic count is the standard Stefan-
Boltzmann fermion/boson ratio at relativistic temperatures (the same
ratio that appears in our retained
[HIERARCHY_SEVEN_EIGHTHS_RIEMANN_DIRICHLET_DIMENSIONAL_ANCHOR_NARROW_THEOREM_NOTE_2026-05-10.md](HIERARCHY_SEVEN_EIGHTHS_RIEMANN_DIRICHLET_DIMENSIONAL_ANCHOR_NARROW_THEOREM_NOTE_2026-05-10.md)
as η(4)/ζ(4)).

## What this note does NOT claim

- This count is NOT derived from `Cl(3)` on `Z^3` axioms.
- The 28 bosonic + 90 fermionic breakdown rests on the SM particle
  content as separately admitted.
- The runner verifies the bounded bookkeeping table and arithmetic, not the
  physical correctness of the imported Standard Model spectrum.
- The named non-derivation import is the bounded scope.

## Standard textbook references

- Kolb & Turner, *The Early Universe* (1990), Table 3.1.
- Husdal, "On Effective Degrees of Freedom in the Early Universe"
  arXiv:1609.04979 — explicit derivation with full breakdown.
- Mukhanov, *Physical Foundations of Cosmology* (2005), Ch. 3.

## Downstream usage

This wrapper is consumed by:
- `DM_LEPTOGENESIS_EQUILIBRIUM_CONVERSION_THEOREM_NOTE_2026-04-16.md` — `g_*` enters the relativistic Majorana equilibrium abundance.
- Various other DM-leptogenesis thermal-side rows that consume the
  `g_*` constant for thermal averages.

## Boundary

This wrapper note is a named-import-only bounded theorem. It does not
claim:
- a framework derivation of the SM particle content;
- a framework derivation of the 28 + 90 specific count;
- closure of any downstream DM-leptogenesis theorem.

Its only function is to provide a citeable one-hop authority for the
imported SM relativistic DOF count so downstream notes register the
import cleanly instead of carrying it as an unattributed constant.
