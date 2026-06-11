# `g_*` SM-Content Proof-Walk From Supplied Thermal Inventory Bounded Note

**Date:** 2026-05-28
**Claim type:** bounded_theorem
**Status authority:** source-note proposal only; audit verdict and
effective status are set by the independent audit lane.
**Primary runner:** [`scripts/frontier_g_star_sm_content_from_supplied_thermal_inventory.py`](../scripts/frontier_g_star_sm_content_from_supplied_thermal_inventory.py)
**Thermal `7/8` bridge:** [`GSTAR_THERMAL_SEVEN_EIGHTHS_STEFAN_BOLTZMANN_BRIDGE_NARROW_THEOREM_NOTE_2026-06-06.md`](GSTAR_THERMAL_SEVEN_EIGHTHS_STEFAN_BOLTZMANN_BRIDGE_NARROW_THEOREM_NOTE_2026-06-06.md),
with runner
[`scripts/audit_companion_gstar_thermal_seven_eighths_bridge_2026_06_06.py`](../scripts/audit_companion_gstar_thermal_seven_eighths_bridge_2026_06_06.py)
and cache
[`logs/runner-cache/audit_companion_gstar_thermal_seven_eighths_bridge_2026_06_06.txt`](../logs/runner-cache/audit_companion_gstar_thermal_seven_eighths_bridge_2026_06_06.txt).

## Claim

Given the registered Standard Model thermal-inventory premise packet P1-P5
from
[`SM_RELATIVISTIC_DOF_COUNT_IMPORT_NOTE_2026-05-17.md`](SM_RELATIVISTIC_DOF_COUNT_IMPORT_NOTE_2026-05-17.md),
with support for the generation count, color count, one-generation
singlet-completion structure, and fermion thermal weight where cited below,
the relativistic effective degrees-of-freedom count

```text
g_*(T) = N_bosons + (7/8) N_fermions = 28 + (7/8) * 90 = 427/4 = 106.75
```

evaluated for the unbroken-Standard-Model thermal inventory at temperatures
`T` above the electroweak crossover (so that the listed Standard Model
particles are relativistic), is a bounded proof-walk on:

- a small set of named group-theoretic / structural / thermal support inputs
  (the **support packet** R1-R6 below);
- the retained-bounded declared-inventory premise packet
  (P1-P5 below) registered in `SM_RELATIVISTIC_DOF_COUNT_IMPORT_NOTE_2026-05-17.md`.

This is a bounded proof-walk of the `g_* = 106.75` arithmetic. It does not
add a new axiom, a new repo-wide theory class, or a retained-status claim.
The Standard Model thermal inventory itself remains a declared physical
inventory premise, not a framework derivation of which particles nature
contains. The repair here is that the premise packet is no longer anonymous:
it is routed through the retained-bounded finite declared-inventory arithmetic
certificate.

## Support packet (R1-R6)

The following authorities and source bridges support the framework-side pieces
consumed by the proof-walk. The independent audit lane owns all final status
classification.

- **R1 Three generations** (three flavour copies for each fermion species).
  Supplied by
  [`THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md`](THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md)
  (`retained_bounded`) and
  [`THREE_GENERATION_OBSERVABLE_M3C_BURNSIDE_NARROW_THEOREM_NOTE_2026-05-10.md`](THREE_GENERATION_OBSERVABLE_M3C_BURNSIDE_NARROW_THEOREM_NOTE_2026-05-10.md)
  (`retained`), supplying the integer count `n_gen = 3` for the proof-walk.
- **R2 SU(3)_c color count `N_c = 3` and adjoint dimension
  `dim adj(SU(3)) = N_c^2 - 1 = 8`.**
  Supplied by
  [`CL3_COLOR_AUTOMORPHISM_THEOREM.md`](CL3_COLOR_AUTOMORPHISM_THEOREM.md)
  (`retained`) for `N_c = 3` and by the elementary Lie-algebra identity
  `dim su(N) = N^2 - 1` for the adjoint count.
- **R3 Right-handed singlet completion at one generation.**
  Supplied by
  [`ONE_GENERATION_ANOMALY_SINGLET_COMPLETION_NARROW_THEOREM_NOTE_2026-05-10.md`](ONE_GENERATION_ANOMALY_SINGLET_COMPLETION_NARROW_THEOREM_NOTE_2026-05-10.md)
  (`retained_bounded`) and the parametric hypercharge enumeration
  [`SM_HYPERCHARGE_UNIQUENESS_ALGEBRAIC_SOLUTION_ENUMERATION_NARROW_THEOREM_NOTE_2026-05-10.md`](SM_HYPERCHARGE_UNIQUENESS_ALGEBRAIC_SOLUTION_ENUMERATION_NARROW_THEOREM_NOTE_2026-05-10.md)
  (`retained_bounded`), enumerating the per-generation right-handed
  multiplet structure used in P1.
- **R4 Per-site `j = 1/2` SU(2) carrier.**
  Supplied by
  [`PER_SITE_SU2_SPIN_HALF_THEOREM_NOTE_2026-05-02.md`](PER_SITE_SU2_SPIN_HALF_THEOREM_NOTE_2026-05-02.md)
  (`retained`), giving the per-site spin-`1/2` carrier for the fermion
  spin-count factor in P4.
- **R5 Spin-statistics cardinality.**
  Supplied by
  [`SPIN_STATISTICS_CARDINALITY_PAULI_EXCLUSION_NARROW_THEOREM_NOTE_2026-05-10.md`](SPIN_STATISTICS_CARDINALITY_PAULI_EXCLUSION_NARROW_THEOREM_NOTE_2026-05-10.md)
  (`retained`) and
  [`SPIN_STATISTICS_BEREZIN_DETERMINANT_NARROW_THEOREM_NOTE_2026-05-10.md`](SPIN_STATISTICS_BEREZIN_DETERMINANT_NARROW_THEOREM_NOTE_2026-05-10.md)
  (`retained_bounded`), supplying the Fermi-Dirac versus Bose-Einstein
  occupation distinction consumed by R6.
- **R6 Fermion-to-boson thermal weight `7/8` at `d = 4`.**
  Supplied directly by
  [`GSTAR_THERMAL_SEVEN_EIGHTHS_STEFAN_BOLTZMANN_BRIDGE_NARROW_THEOREM_NOTE_2026-06-06.md`](GSTAR_THERMAL_SEVEN_EIGHTHS_STEFAN_BOLTZMANN_BRIDGE_NARROW_THEOREM_NOTE_2026-06-06.md),
  which derives the per-fermion-degree-of-freedom Stefan-Boltzmann
  weight from the Bose/Fermi thermal integrals
  `I_F/I_B = η(4)/ζ(4) = 7/8`. The older
  [`HIERARCHY_SEVEN_EIGHTHS_RIEMANN_DIRICHLET_DIMENSIONAL_ANCHOR_NARROW_THEOREM_NOTE_2026-05-10.md`](HIERARCHY_SEVEN_EIGHTHS_RIEMANN_DIRICHLET_DIMENSIONAL_ANCHOR_NARROW_THEOREM_NOTE_2026-05-10.md)
  remains a parallel `d=4` eta/zeta arithmetic identity, not the
  thermal-integral authority consumed by this `g_*` row.

The parent inventory note
`SM_RELATIVISTIC_DOF_COUNT_IMPORT_NOTE_2026-05-17.md` is the existing
finite declared-inventory arithmetic certificate this proof-walk traces as
the registered P1-P5 premise packet. It is now a load-bearing dependency for
this row: the local proof-walk repeats the arithmetic directly, while the
parent note supplies the retained-bounded declared-inventory boundary.

## Registered premise packet (P1-P5)

The following premise packet supplies the Standard Model thermal inventory.
P1-P5 are declared explicitly in the retained-bounded finite inventory wrapper
[`SM_RELATIVISTIC_DOF_COUNT_IMPORT_NOTE_2026-05-17.md`](SM_RELATIVISTIC_DOF_COUNT_IMPORT_NOTE_2026-05-17.md)
and repeated here so this row is self-contained. They are not derived from
the framework here and are not promoted to axioms.

- **P1 Declared Standard Model particle inventory.** The relativistic
  particle content at the leptogenesis-scale temperature is the unbroken
  Standard Model content: `8` gluons; `3` SU(2)_L gauge bosons
  (`W^1, W^2, W^3`); `1` U(1)_Y gauge boson (`B`); one complex
  scalar SU(2)_L Higgs doublet; per generation, one quark SU(2)_L doublet
  `Q_L` in the `(3,2)_{1/3}` representation, one up-type singlet `u_R` in
  `(3,1)_{4/3}`, one down-type singlet `d_R` in `(3,1)_{-2/3}`, one lepton
  SU(2)_L doublet `L_L` in `(1,2)_{-1}`, one charged-lepton singlet `e_R`
  in `(1,1)_{-2}`, and one left-handed (Weyl) active neutrino as part of
  `L_L`. The right-handed neutrino is not counted in the relativistic
  thermal inventory at this temperature.
- **P2 Two transverse polarizations per massless vector.** Each of the
  `8 + 3 + 1 = 12` gauge bosons contributes `2` transverse
  polarization states in the unbroken-phase relativistic accounting.
- **P3 Four real scalar degrees-of-freedom per complex doublet.** The
  Standard Model complex scalar SU(2)_L Higgs doublet has
  `2 (complex components) * 2 (real per complex) = 4` real scalar
  degrees of freedom.
- **P4 Dirac four-dof per charged fermion flavour-colour state.** Each
  Dirac fermion state contributes `2 (spin) * 2 (particle-antiparticle)
  = 4` thermal degrees of freedom. The active neutrino is a single
  Weyl fermion per generation, contributing `2 (helicity-antiparticle)`
  states.
- **P5 Temperature above the electroweak crossover.** The thermal
  accounting is performed at `T > 250 GeV`, so all listed Standard
  Model particles are relativistic and contribute to `g_*`. The
  Higgs scalar is treated in the unbroken-phase bookkeeping with four
  real components.

P1 names the particle inventory; P2-P4 name the per-particle relativistic
state counts used in the proof-walk arithmetic; P5 names the temperature
regime in which the relativistic count is the appropriate accounting.

**Counting premise discipline.** P1-P5 are declared explicitly and are the
load-bearing source for the Standard Model state-count conventions not
otherwise derived here. In particular, P1 supplies the listed gauge and
matter multiplets, P2 supplies the two-transverse-polarization state count
for massless vector bosons, P3 supplies the four-real-component Higgs-doublet
count, P4 supplies the Dirac/Weyl thermal state-count convention for
fermions, and P5 supplies the relativistic-temperature regime. The retained
support packet checks framework-side consistency where cited, while the
retained-bounded inventory wrapper registers the finite SM inventory premise
packet as the physical input boundary.

## Proof-walk

Each row of the table is a step in the parent inventory note's arithmetic.
The "Load-bearing input" column names the smallest retained support
authority or supplied premise consumed; the "Lattice-action input?" column shows
that no lattice-action quantity (plaquette, staggered phase, link unitary,
`u_0`, Monte-Carlo measurement, fitted comparator) enters the proof-walk.

| Step | Statement | Load-bearing input | Lattice-action input? |
|---|---|---|---|
| (B1) | Gluon DOF count `8 (color) * 2 (transverse) = 16` | R2 (`dim adj(SU(3)) = 8`) + P2 | no |
| (B2) | SU(2)_L gauge boson DOF count `3 (W^a, a=1,2,3) * 2 = 6` | P1 (three `W^a`) + P2 | no |
| (B3) | U(1)_Y gauge boson DOF count `1 (B) * 2 = 2` | P1 (single B) + P2 | no |
| (B4) | Higgs doublet DOF count `4 (real scalar components)` | P1 + P3 | no |
| (B5) | Bosonic total `N_bosons = 16 + 6 + 2 + 4 = 28` | (B1)+(B2)+(B3)+(B4) | no |
| (B6) | Quark DOF count `n_gen * (n_up + n_down) * N_c * 4 = 3 * 2 * 3 * 4 = 72` | R1 (`n_gen = 3`) + R2 (`N_c = 3`) + P1 (quark multiplets) + P4 | no |
| (B7) | Charged lepton DOF count `n_gen * 4 = 3 * 4 = 12` | R1 + P1 (`e_R`) + P4 | no |
| (B8) | Active neutrino DOF count `n_gen * 2 = 3 * 2 = 6` | R1 + P1 (no `nu_R` in thermal inventory) + P4 | no |
| (B9) | Fermionic total `N_fermions = 72 + 12 + 6 = 90` | (B6)+(B7)+(B8) | no |
| (B10) | Thermal weight `7/8` for fermions | R5 + R6 | no |
| (B11) | `g_* = N_bosons + (7/8) N_fermions = 28 + (7/8) * 90 = 28 + 78.75 = 106.75` | exact rational arithmetic | no |
| (B12) | Exact rational `g_* = 28 + (7/8) * 90 = (28 * 8 + 7 * 90) / 8 = (224 + 630) / 8 = 854 / 8 = 427 / 4` | exact rational arithmetic | no |
| (B13) | Decimal `g_* = 427/4 = 106.75` | exact rational arithmetic | no |

The proof-walk does not cite the Wilson plaquette action, staggered phases,
Brillouin-zone labels, link unitaries, the lattice scale `u_0`, a Monte
Carlo measurement, or a fitted observational value.

## Exact arithmetic check

The bosonic count factorises as

```text
N_bosons = (N_c^2 - 1) * 2  +  3 * 2  +  1 * 2  +  4
         = 8 * 2  +  6  +  2  +  4
         = 16  +  6  +  2  +  4
         = 28.
```

The fermionic count factorises as

```text
N_fermions = n_gen * [ N_c * (n_up + n_down) * 4 (Dirac)
                       + (n_charged_lepton) * 4 (Dirac)
                       + (n_neutrino_weyl) * 2 (Weyl) ]
           = 3 * [ 3 * 2 * 4  +  1 * 4  +  1 * 2 ]
           = 3 * [ 24  +  4  +  2 ]
           = 3 * 30
           = 90.
```

With the supplied fermion thermal weight bridge `7/8`,

```text
g_*  =  N_bosons  +  (7/8) * N_fermions
     =  28  +  (7/8) * 90
     =  28  +  630/8
     =  224/8  +  630/8
     =  854/8
     =  427/4
     =  106.75.
```

The runner repeats this calculation with `fractions.Fraction` for the
factorised bosonic and fermionic sums and checks each substep against the
parent inventory note's totals `28` and `90`.

## Dependencies

Load-bearing support dependencies for this proof-walk:

- [`SM_RELATIVISTIC_DOF_COUNT_IMPORT_NOTE_2026-05-17.md`](SM_RELATIVISTIC_DOF_COUNT_IMPORT_NOTE_2026-05-17.md)
  retained-bounded finite declared-inventory arithmetic certificate for P1-P5:
  the unbroken Standard Model thermal inventory, vector/scalar/Dirac/Weyl
  state-count conventions, and the `T`-regime premise. This is a registered
  physical-inventory premise wrapper, not a framework derivation of the SM
  particle list.
- [`THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md`](THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md)
  retained three-generation observable algebra (`retained_bounded`).
- [`THREE_GENERATION_OBSERVABLE_M3C_BURNSIDE_NARROW_THEOREM_NOTE_2026-05-10.md`](THREE_GENERATION_OBSERVABLE_M3C_BURNSIDE_NARROW_THEOREM_NOTE_2026-05-10.md)
  retained narrow three-generation `M_3(C)` carrier (`retained`).
- [`CL3_COLOR_AUTOMORPHISM_THEOREM.md`](CL3_COLOR_AUTOMORPHISM_THEOREM.md)
  retained `N_c = 3` color theorem (`retained`).
- [`ONE_GENERATION_ANOMALY_SINGLET_COMPLETION_NARROW_THEOREM_NOTE_2026-05-10.md`](ONE_GENERATION_ANOMALY_SINGLET_COMPLETION_NARROW_THEOREM_NOTE_2026-05-10.md)
  retained right-handed singlet completion at one generation
  (`retained_bounded`).
- [`SM_HYPERCHARGE_UNIQUENESS_ALGEBRAIC_SOLUTION_ENUMERATION_NARROW_THEOREM_NOTE_2026-05-10.md`](SM_HYPERCHARGE_UNIQUENESS_ALGEBRAIC_SOLUTION_ENUMERATION_NARROW_THEOREM_NOTE_2026-05-10.md)
  retained parametric hypercharge enumeration (`retained_bounded`).
- [`PER_SITE_SU2_SPIN_HALF_THEOREM_NOTE_2026-05-02.md`](PER_SITE_SU2_SPIN_HALF_THEOREM_NOTE_2026-05-02.md)
  retained per-site `j = 1/2` SU(2) carrier (`retained`).
- [`SPIN_STATISTICS_CARDINALITY_PAULI_EXCLUSION_NARROW_THEOREM_NOTE_2026-05-10.md`](SPIN_STATISTICS_CARDINALITY_PAULI_EXCLUSION_NARROW_THEOREM_NOTE_2026-05-10.md)
  retained spin-statistics cardinality (`retained`).
- [`SPIN_STATISTICS_BEREZIN_DETERMINANT_NARROW_THEOREM_NOTE_2026-05-10.md`](SPIN_STATISTICS_BEREZIN_DETERMINANT_NARROW_THEOREM_NOTE_2026-05-10.md)
  retained spin-statistics Berezin route (`retained_bounded`).
- [`GSTAR_THERMAL_SEVEN_EIGHTHS_STEFAN_BOLTZMANN_BRIDGE_NARROW_THEOREM_NOTE_2026-06-06.md`](GSTAR_THERMAL_SEVEN_EIGHTHS_STEFAN_BOLTZMANN_BRIDGE_NARROW_THEOREM_NOTE_2026-06-06.md)
  direct Stefan-Boltzmann / thermal-integral derivation of the
  fermion-to-boson `7/8` weight.
- [`HIERARCHY_SEVEN_EIGHTHS_RIEMANN_DIRICHLET_DIMENSIONAL_ANCHOR_NARROW_THEOREM_NOTE_2026-05-10.md`](HIERARCHY_SEVEN_EIGHTHS_RIEMANN_DIRICHLET_DIMENSIONAL_ANCHOR_NARROW_THEOREM_NOTE_2026-05-10.md)
  parallel `d=4` eta/zeta arithmetic identity; context for the same
  rational value, not the thermal-integral bridge.

These are support authorities and bridges for a bounded theorem. The row
remains unaudited until the independent audit lane reviews this note, its
dependencies, the registered P1-P5 premise packet, and the runner. The
Standard Model thermal inventory still comes from P1-P5 and the finite
declared-inventory wrapper, not from the framework-side support authorities
alone.

Non-load-bearing context:

- `DM_ETA_FREEZEOUT_BYPASS_QUANTITATIVE_THEOREM_NOTE_2026-04-25.md` is the
  downstream physics consumer that uses `g_*(EW) = 106.75` as a thermal
  input on the freeze-out-bypass cosmology lane. This proof-walk supplies
  the conditional arithmetic for that consumer's `sqrt(g_*)` appearance;
  it does not promote the consumer's row.
- `AXIOM_FIRST_STEFAN_BOLTZMANN_THEOREM_NOTE_2026-05-01.md` records the
  bosonic Stefan-Boltzmann constant on the framework substrate;
  context-only here.
- `SM_RELATIVISTIC_DOF_COUNT_IMPORT_NOTE_2026-05-17.md` is load-bearing for
  P1-P5 above. It is no longer context-only for this row.

## Boundaries

This proof-walk does not close:

- derivation of the Standard Model gauge group `SU(3)_c x SU(2)_L x U(1)_Y`
  as the physical thermal gauge content (premise P1);
- derivation of the SM particle inventory list itself (premise P1, including
  the single complex Higgs doublet and the absence of an additional
  thermally active scalar sector);
- derivation of the two-transverse-polarization count for massless vector
  bosons (premise P2);
- derivation of the four-real-scalar count for the complex Higgs doublet
  (premise P3);
- derivation of the Dirac four-dof / Weyl two-dof state count per fermion
  species (premise P4);
- the `T > 250 GeV` relativistic-content premise (P5);
- thermal-equilibrium dynamics, chemical-potential assumptions, or
  decoupling thresholds beyond the supplied P1-P5 thermal-inventory
  premise packet; the one-particle Bose/Fermi integral ratio used for
  the `7/8` weight is supplied by R6;
- any downstream cosmology or DM-leptogenesis claim that consumes `g_*`;
- any parent theorem/status promotion (the proof-walk records the
  factorised arithmetic as a separate bounded identity; the parent
  inventory note's status remains pipeline-owned).

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_g_star_sm_content_from_supplied_thermal_inventory.py
```

Expected:

```text
TOTAL: PASS=<n> FAIL=0
VERDICT: bounded proof-walk passes; g_* = 106.75 follows from the
support packet R1-R6 plus supplied premise packet P1-P5 by exact
rational arithmetic.
```
