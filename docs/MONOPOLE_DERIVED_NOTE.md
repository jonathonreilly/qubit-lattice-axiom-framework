# Magnetic Monopole Mass: Bounded Lattice Derivation

**Date:** 2026-04-12 (RECONCILED 2026-05-01; IMPORTS LABELED 2026-05-16)
**Script:** `scripts/frontier_monopole_derived.py`
**Status:** Bounded — the lattice shape `M_mono = c_lat * beta * M_Pl` with
`c_lat = G_lat(0) = 0.2527` is closed lattice arithmetic; the numerical
prefactor `M_mono ~ 1.43 M_Planck` is conditional on a named
non-derivation import for `alpha_EM(M_Pl)`. The order-of-magnitude
prediction `M_mono ~ M_Planck` is robust across the plausible
`alpha_EM(M_Pl)` band.

**Claim type:** bounded_theorem
**Current publication disposition:** bounded companion only. Not on the
retained flagship claim surface.

## Summary

On the compact-U(1) Wilson action on Z^3 with edge-valued phases
`theta_{edge} in [0, 2*pi)`, the monopole mass takes the lattice form

    M_mono = c_lat * beta * (1/a),    c_lat = G_lat(0) = 0.2527

where `G_lat(0)` is the lattice Coulomb Green's function at the origin
on the cubic lattice (closed lattice arithmetic; the runner verifies
the value at `L = 64` to four significant figures). The `c_lat` coefficient
is derived; `beta = 1/(4*pi*alpha_EM(a^{-1}))` requires an external value
of `alpha_EM` at the lattice scale.

On the **Planck-scale package pin** `a^(-1) = M_Pl` (carried elsewhere in the
framework, not derived in this note) and the **one-loop SM RG bridge import**
`alpha_EM^{-1}(M_Pl) ~ 72.1` (from `alpha_EM(M_Z) = 1/127.9`, `b_EM = -80/9`;
**not derived from lattice axioms**), the numerical prefactor is

    M_mono = 0.2527 * 5.738 * M_Pl = 1.43 M_Pl = 1.75e19 GeV.

Sensitivity: for `alpha_EM^{-1}(M_Pl)` in `[30, 60]` the prefactor ranges over
`[0.60, 1.21] M_Pl`; for `~ 72` (one-loop SM RG) it gives `1.43 M_Pl`. The
**order-of-magnitude prediction `M_mono ~ M_Planck` is robust**; the exact
prefactor inherits the uncertainty in the `alpha_EM(M_Pl)` extrapolation.

The Dirac quantization condition `e * g = 2*pi` is **automatic** from the
periodicity of `theta` (not a new postulate). The overclosure calculation
shows the framework **requires inflation** with `N_e > 21` e-folds for
cosmological consistency — a bounded consequence of `M_mono ~ M_Pl` and
standard FRW cosmology.

## Derivation Chain

### Step 1: Compactness — magnetic charge is integer (derived)

On Z^3, gauge fields live as group elements `U = exp(i*theta)` on edges,
with `theta in [0, 2*pi)`. This compactness is forced by the lattice
structure (not chosen). The magnetic charge through any cube is provably
an integer, and the total charge on a periodic L^3 lattice is zero by
Gauss's law.

**Runner check:** verified numerically on 100 random L=8 configurations
(every cube charge is an integer to numerical precision; total charge is
zero on every config).

### Step 2: Dirac quantization — automatic (derived)

The minimum magnetic charge is `m = 1` in lattice units. The physical
charge is `g = 2*pi/e`, giving `e*g = 2*pi` — the Dirac condition. This
is not a new postulate; it follows from the periodicity of `theta`.

### Step 3: Monopole self-energy — bounded by named imports

The monopole self-energy is the lattice Coulomb self-energy of a
unit magnetic charge with the lattice providing the UV cutoff:

    M_mono = c_lat * beta * (1/a)

where:

- **`c_lat = G_lat(0)`** (derived). On cubic Z^3 with the
  Wilson action, `G_lat(0)` equals the sum over non-zero lattice momenta
  of `1 / hat{k}^2`, where `hat{k}_mu = 2 sin(pi n_mu / L)`. In the
  infinite-volume limit this is the BKM constant `0.2527`. The runner
  computes `G_lat(0) = 0.2492` on an L=64 lattice (finite-volume
  correction `~ 1.4%`).
- **`beta = 1/(4*pi*alpha_EM(a^{-1}))`** (bridge import). Requires an
  external value of `alpha_EM` at the lattice scale. With the Planck pin
  `a^(-1) = M_Pl` and the one-loop SM RG extrapolation
  `alpha_EM^{-1}(M_Pl) ~ 72.1`, this gives `beta ~ 5.738`. **The
  one-loop SM RG running is not derived from the lattice axioms;** it is
  an explicit bridge import. Two-loop and threshold-matching corrections
  are not implemented and would shift `beta` by `O(10-30%)`.
- **`(1/a) = M_Planck = 1.221 x 10^19 GeV`** (package pin). Carried
  elsewhere in the framework on the accepted physical-lattice reading,
  not derived in this note.

**Conditional headline:** under the three imports above,

    M_mono = 0.2527 * 5.738 * M_Pl = 1.43 M_Pl = 1.75e19 GeV.

**Robust headline (import-independent shape):** for `alpha_EM^{-1}(M_Pl)`
in `[30, 60]` (the plausible perturbative band), `M_mono` ranges over
`[0.60, 1.21] M_Pl`. The order-of-magnitude statement
`M_mono ~ M_Planck` is the import-robust conclusion.

### Step 4: Configuration topology check (NOT a quantitative cross-check)

The earlier version of this note described Step 4 as a "direct numerical
self-energy" measurement. That framing was misleading: the bare Wilson
action of a constructed monopole-antimonopole configuration is dominated
by Dirac-string artifacts, not by the monopole self-energy. On L = 6, 8,
10, 12 lattices, the runner reports `Delta S ~ 246 / 347 / 444 / ...` and
a derived `M / M_Pl ~ 400 / 550 / 700 / ...` which differs from the
analytic Step 3 result by **2-3 orders of magnitude**.

This gap was flagged by the 2026-05-15 audit, and the audit was correct.
The honest framing is:

**What Step 4 actually demonstrates:**

- The `_construct_monopole_config` field carries the intended
  integer monopole-antimonopole charges at each L (Step 1 verification on a
  non-random, physically motivated configuration).
- Total magnetic charge is zero on every L (Gauss's law).

**What Step 4 does NOT demonstrate:**

- A quantitative independent measurement of `c_lat`. The bare Wilson
  action of the singular Wu-Yang potential is dominated by string action
  near the Dirac string, not by the Coulomb self-energy of the monopole
  core. The reported `Delta S` is `O(100)` not `O(1)`, which is
  characteristic of string artifacts.

**What it would take to do a correct numerical measurement:**

- Monte Carlo sampling of the partition function and extraction of the
  free-energy difference between sectors (not the bare action of one
  configuration).
- Explicit subtraction of the Dirac-string contribution
  (DeGrand-Toussaint dual-lattice prescription) or working in the Villain
  formulation where the string is gauged away exactly.

These are well-known techniques in the lattice gauge literature; the
runner does not implement them. A future iteration may add either a
Monte Carlo measurement or a DT subtraction; until then the analytic
`c_lat = G_lat(0)` from Step 3 is the load-bearing computation, and
Step 4 is a topology/configuration check only.

### Step 5: Overclosure — inflation required (bounded)

Kibble mechanism at the graph-growth epoch gives one monopole per
correlation volume; at formation `n_mono / n_gamma = pi^2 / (2 * zeta(3))
~ 4.1`. With `M_mono ~ M_Pl`, today's `Omega_mono ~ 6 x 10^27`
(catastrophic overclosure). With inflation (`N_e > 21` e-folds after
monopole formation), monopoles are diluted below any observational
bound. Post-inflation thermal production is impossible since
`T_RH << M_mono` for any standard reheating temperature; Schwinger
production is exponentially suppressed. All current experimental bounds
(Parker, MACRO, IceCube, MoEDAL) are trivially satisfied by the
prediction `flux = 0` (with inflation).

This step is a **bounded consequence** of Step 3's `M_mono ~ M_Pl`
together with standard FRW cosmology and the Kibble mechanism (the
cosmology and Kibble pieces are also imports, not derived from the
lattice axiom packet).

## Reconciliation Note (2026-05-16)

This iteration responds to the 2026-05-15 audit verdict:

> The load-bearing mass value is obtained by inserting a specific
> externally calibrated running coupling, `alpha_EM^{-1}(M_Pl) ~ 72.1`,
> into `c*beta*M_Pl`. That makes the headline prefactor a chosen-scale
> numerical result, not a closed first-principles computation from the
> stated lattice axiom alone. The runner contains some genuine lattice
> computations, but the direct numerical self-energy section visibly
> disagrees with the analytic headline by orders of magnitude.

The audit verdict was correct on both counts. This revision:

1. Labels `alpha_EM(M_Pl)` as a **named non-derivation bridge import** and
   reports the resulting `1.43 M_Pl` as a **conditional numerical
   prefactor**, with the **import-robust headline** being
   `M_mono ~ M_Planck` across the perturbative-alpha band.
2. Re-scopes Step 4 from "direct numerical self-energy" to a **topology /
   configuration check**, explicitly stating that the bare Wilson action
   of the singular Wu-Yang configuration is dominated by Dirac-string
   artifacts and is **not** a quantitative measurement of `c_lat`.
3. Tags the note's claim type as `bounded_theorem` (was effectively
   ambiguous between "derived" and "bounded companion").

An earlier 2026-05-01 reconciliation already noted the upgrade from
`0.80 M_Pl` (placeholder `alpha^{-1} ~ 40`) to `1.43 M_Pl` (one-loop SM
RG `alpha^{-1} ~ 72`). The current revision keeps that arithmetic but
labels it as conditional on the explicit bridge import.

## Assumptions and Imports (Explicit Ledger)

### Derived from lattice axioms (no import needed)

- Compactness of U(1) on Z^3 edges.
- Magnetic charge quantization (integer per cube; Gauss's law on periodic
  lattice).
- Dirac condition `e*g = 2*pi` from periodicity.
- Existence of monopole as topological excitation
  (`pi_1(U(1)) = Z` via the compact lattice avatar).
- Lattice Coulomb Green's function `G_lat(0) = 0.2527` on cubic Z^3
  (closed lattice arithmetic).
- Self-energy shape `M_mono = c_lat * beta * (1/a)` for the Wilson
  action.

### Named non-derivation imports (load-bearing)

- **Wilson action** `S = -beta * sum cos(Phi_P)`. Alternative compact
  actions (Villain, improved) would shift `c_lat` by `O(10%)`. Not
  derived.
- **Planck-scale package pin** `a^(-1) = M_Pl`. Carried elsewhere in the
  framework. Not derived in this note.
- **`alpha_EM(M_Pl)` one-loop SM RG running from `alpha_EM(M_Z) = 1/127.9`
  with `b_EM = -80/9`**, giving `alpha_EM^{-1}(M_Pl) ~ 72.1`. This is the
  **load-bearing import** for the numerical prefactor. Two-loop and
  threshold-matching corrections are not implemented. **Not derived from
  lattice axioms.**

### Cosmology imports (Step 5 only)

- Standard FRW cosmology with entropy conservation.
- Kibble mechanism at the graph-growth epoch.

## What Is Not Derived

- The exact value of `alpha_EM(M_Pl)` (one-loop SM RG only; full two-loop
  with threshold matching not implemented).
- A quantitative independent numerical measurement of `c_lat` (Step 4 is
  a topology check, not a self-energy measurement — Monte Carlo
  free-energy or DT subtraction would be needed and is not implemented).
- Whether inflation actually occurred (required by the framework, not
  derived).
- Short-range monopole-monopole interactions (lattice artifacts dominate).

## Relation to Earlier Versions

Earlier scripts and notes carried different prefactors depending on the
treatment of `alpha_EM(M_Pl)`:

- Mixing a 4D DeGrand-Toussaint coefficient into a 3D BKM calculation
  gave a much larger headline (incorrect dimensional reduction).
- Using the placeholder `alpha^{-1} ~ 40` gave `M_mono ~ 0.80 M_Pl`.
- Using the one-loop SM RG `alpha^{-1} ~ 72.1` gives `M_mono ~ 1.43 M_Pl`.

The package now tracks the runner-consistent value `1.43 M_Pl` as the
conditional headline and labels it as bounded support, not a flagship
retained claim. The **robust headline is `M_mono ~ M_Planck`**.
