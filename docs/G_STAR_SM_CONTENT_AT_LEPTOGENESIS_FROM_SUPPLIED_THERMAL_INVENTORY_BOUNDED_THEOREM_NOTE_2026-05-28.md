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

Given the locally supplied inventory P1-P5 below and the conditional thermal
integral R6, exact arithmetic gives

```text
g_*(T) = N_bosons + (7/8) N_fermions = 28 + (7/8) * 90 = 427/4 = 106.75.
```

This is a conditional ideal ultrarelativistic count, not an exact value at
every temperature above a fixed threshold. It does not add a new axiom or
establish framework particle content, equilibrium, or retained physical support.
The parent `SM_RELATIVISTIC_DOF_COUNT_IMPORT_NOTE_2026-05-17.md` records a
literature-conditioned inventory; it does not register a retained P1-P5 packet.
The labels P1-P5 in this note are local supplied premises.

## Supplied counts and conditional bridge (R1-R6)

R1 supplies n_gen=3; R2 supplies N_c=3 and the eight color-vector states;
R3 supplies the listed one-generation matter multiplets; R4 supplies the
Dirac/Weyl state-count convention; R5 supplies the Bose/Fermi equilibrium
occupation choice. None is established as physical content by this proof-walk.
They are included explicitly in P1-P5 rather than inferred from the context
citations below. Conditional on those occupation functions, zero chemical
potential and massless continuum dispersion, R6 is the checked integral
I_F/I_B = eta(4)/zeta(4) = 7/8, carried by
[`GSTAR_THERMAL_SEVEN_EIGHTHS_STEFAN_BOLTZMANN_BRIDGE_NARROW_THEOREM_NOTE_2026-06-06.md`](GSTAR_THERMAL_SEVEN_EIGHTHS_STEFAN_BOLTZMANN_BRIDGE_NARROW_THEOREM_NOTE_2026-06-06.md).
This does not derive the physical occupation choice or particle inventory.

## Local supplied premise packet (P1-P5)

P1-P5 are declared locally here, not imported as retained authority from the
parent inventory note. They are assumptions for the following arithmetic,
not framework derivations or new physical primitives.

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
- **P5 Ideal ultrarelativistic thermal conditions.** Supply restored electroweak
  bookkeeping, equilibrium ideal-gas distributions at a common temperature,
  negligible chemical potentials, and effectively massless listed states.
  Exclude finite-mass, interaction, threshold, decoupling and additional-species
  corrections. No particular inequality such as T > 250 GeV proves these
  exact ideal conditions.

P1 supplies the particle inventory including three generations and three
colors. P2 supplies the two-transverse-polarization state count; P3 the four
real scalar components; P4 supplies the Dirac/Weyl thermal state-count convention;
P5 supplies the ideal thermal regime. R6 supplies only the conditional integral.

## Proof-walk

Each row is conditional arithmetic on the local supplied inventory.
The "Load-bearing input" column names the local premise or conditional integral; the "Lattice-action input?" column shows
that no lattice-action quantity (plaquette, staggered phase, link unitary,
`u_0`, Monte-Carlo measurement, fitted comparator) enters the proof-walk.

| Step | Statement | Load-bearing input | Lattice-action input? |
|---|---|---|---|
| (B1) | Gluon DOF count `8 (color) * 2 (transverse) = 16` | P1 (eight color-vector states) + P2 | no |
| (B2) | SU(2)_L gauge boson DOF count `3 (W^a, a=1,2,3) * 2 = 6` | P1 (three `W^a`) + P2 | no |
| (B3) | U(1)_Y gauge boson DOF count `1 (B) * 2 = 2` | P1 (single B) + P2 | no |
| (B4) | Higgs doublet DOF count `4 (real scalar components)` | P1 + P3 | no |
| (B5) | Bosonic total `N_bosons = 16 + 6 + 2 + 4 = 28` | (B1)+(B2)+(B3)+(B4) | no |
| (B6) | Quark DOF count `n_gen * (n_up + n_down) * N_c * 4 = 3 * 2 * 3 * 4 = 72` | P1 (n_gen=3, N_c=3, quark multiplets) + P4 | no |
| (B7) | Charged lepton DOF count `n_gen * 4 = 3 * 4 = 12` | P1 (`e_R`) + P4 | no |
| (B8) | Active neutrino DOF count `n_gen * 2 = 3 * 2 = 6` | P1 (no `nu_R` in thermal inventory) + P4 | no |
| (B9) | Fermionic total `N_fermions = 72 + 12 + 6 = 90` | (B6)+(B7)+(B8) | no |
| (B10) | Thermal weight `7/8` for fermions | P5 occupation choice + R6 conditional integral | no |
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

## Dependencies and historical context

The local P1-P5 assumptions supply the inventory. The current parent
[`SM_RELATIVISTIC_DOF_COUNT_IMPORT_NOTE_2026-05-17.md`](SM_RELATIVISTIC_DOF_COUNT_IMPORT_NOTE_2026-05-17.md)
is literature-conditioned context for its totals 28/90, not a retained packet.
R6 is the conditional thermal-integral bridge named above. The following
former R1-R5 and parallel references are preserved as historical context only;
existence or citation does not establish their physical applicability or status:

- [`THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md`](THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md)
- [`THREE_GENERATION_OBSERVABLE_M3C_BURNSIDE_NARROW_THEOREM_NOTE_2026-05-10.md`](THREE_GENERATION_OBSERVABLE_M3C_BURNSIDE_NARROW_THEOREM_NOTE_2026-05-10.md)
- [`CL3_COLOR_AUTOMORPHISM_THEOREM.md`](CL3_COLOR_AUTOMORPHISM_THEOREM.md)
- [`ONE_GENERATION_ANOMALY_SINGLET_COMPLETION_NARROW_THEOREM_NOTE_2026-05-10.md`](ONE_GENERATION_ANOMALY_SINGLET_COMPLETION_NARROW_THEOREM_NOTE_2026-05-10.md)
- [`SM_HYPERCHARGE_UNIQUENESS_ALGEBRAIC_SOLUTION_ENUMERATION_NARROW_THEOREM_NOTE_2026-05-10.md`](SM_HYPERCHARGE_UNIQUENESS_ALGEBRAIC_SOLUTION_ENUMERATION_NARROW_THEOREM_NOTE_2026-05-10.md)
- [`PER_SITE_SU2_SPIN_HALF_THEOREM_NOTE_2026-05-02.md`](PER_SITE_SU2_SPIN_HALF_THEOREM_NOTE_2026-05-02.md)
- [`SPIN_STATISTICS_CARDINALITY_PAULI_EXCLUSION_NARROW_THEOREM_NOTE_2026-05-10.md`](SPIN_STATISTICS_CARDINALITY_PAULI_EXCLUSION_NARROW_THEOREM_NOTE_2026-05-10.md)
- [`SPIN_STATISTICS_BEREZIN_DETERMINANT_NARROW_THEOREM_NOTE_2026-05-10.md`](SPIN_STATISTICS_BEREZIN_DETERMINANT_NARROW_THEOREM_NOTE_2026-05-10.md)
- [`HIERARCHY_SEVEN_EIGHTHS_RIEMANN_DIRICHLET_DIMENSIONAL_ANCHOR_NARROW_THEOREM_NOTE_2026-05-10.md`](HIERARCHY_SEVEN_EIGHTHS_RIEMANN_DIRICHLET_DIMENSIONAL_ANCHOR_NARROW_THEOREM_NOTE_2026-05-10.md)

The runner checks documentary alignment and exact local arithmetic, not audit
status or derivations in these context notes. No downstream cosmology or DM
consumer receives physical premise closure from this proof-walk.

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
- the ideal ultrarelativistic thermal conditions (P5);
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
locally supplied P1-P5 inventory plus conditional R6 integral by exact
rational arithmetic.
```
