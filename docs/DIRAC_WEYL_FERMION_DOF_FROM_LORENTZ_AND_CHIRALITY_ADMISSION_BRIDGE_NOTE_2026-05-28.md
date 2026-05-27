# Dirac / Weyl Fermion DOF From Lorentz and Chirality Admission Bridge Note

**Date:** 2026-05-28
**Claim type:** bounded_theorem
**Status authority:** source-note proposal only; audit verdict and
effective status are set by the independent audit lane.
**Primary runner:** [`scripts/audit_companion_dirac_weyl_fermion_dof_from_lorentz_and_chirality_2026_05_28.py`](../scripts/audit_companion_dirac_weyl_fermion_dof_from_lorentz_and_chirality_2026_05_28.py)

## Claim

Given the supplied Cl(3,1) Lorentzian-signature signature-extension
admission packet (Q1-Q2 below), and the retained framework packet
(R1-R4 below), the Standard Model fermion thermal degree-of-freedom
counts named in premise P4 of
`G_STAR_SM_CONTENT_AT_LEPTOGENESIS_FROM_RETAINED_FRAMEWORK_CONTENT_BOUNDED_THEOREM_NOTE_2026-05-28.md`,

```text
Dirac thermal dof per flavour-colour state = 2 (spin) * 2 (particle-antiparticle) = 4,
Weyl thermal dof per flavour-colour state  = 2 (helicity-antiparticle),
```

reduce to exact rational arithmetic on the algebraic content of the named
inputs. The factor `2` for spin comes from R1 (per-site `j = 1/2`); the
factor `2` for particle-antiparticle comes from R3 (CPT exact); the
factor `2` halving from Dirac to Weyl comes from R2 (chirality operator
`gamma_5` existence at even total Clifford generator count). The
Cl(3,1) signature extension supplying the `n = 4` even-generator count
itself is admitted in Q1 (the Wick-rotation sign-`ε` admission P2 of
`HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md`); the on-shell
thermal-counting convention (`2 spin * 2 particle-antiparticle = 4`
rather than the naive 8 real off-shell components of the four-component
spinor) is admitted in Q2.

This is a bounded admission bridge. It does **not** add a new axiom, a
new repo-wide theory class, or a retained-status claim. The Cl(3,1)
signature extension remains an external admission named in Q1; the
on-shell thermal-counting convention remains an external admission
named in Q2.

## Retained framework packet (R1-R4)

The following retained framework authorities supply the load-bearing
algebraic multiplicities consumed by the bridge. Each is currently
`retained` or `retained_bounded` on the live audit ledger as of
2026-05-28.

- **R1 Per-site `j = 1/2` SU(2) spin carrier (factor of 2 spin states).**
  Supplied by
  [`PER_SITE_SU2_SPIN_HALF_THEOREM_NOTE_2026-05-02.md`](PER_SITE_SU2_SPIN_HALF_THEOREM_NOTE_2026-05-02.md)
  (`retained`). On every framework site, the per-site Hilbert space
  carries exactly the `j = 1/2` irreducible representation of su(2);
  the diagonal generator `S_3 = sigma_3 / 2` has eigenvalues
  `m in {-1/2, +1/2}`, supplying the `2 (spin)` factor consumed by the
  proof-walk.

- **R2 Chirality operator `gamma_5` exists iff `n` (total Clifford
  generator count) is even.** Supplied by
  [`CLIFFORD_VOLUME_CHIRALITY_EVEN_DIMENSION_NARROW_THEOREM_NOTE_2026-05-10.md`](CLIFFORD_VOLUME_CHIRALITY_EVEN_DIMENSION_NARROW_THEOREM_NOTE_2026-05-10.md)
  (`retained`). An element `gamma_5` of `Cl_C(p, q)` satisfying
  `gamma_5^2 = +I` and `{gamma_5, gamma_mu} = 0` for every generator
  exists iff `n = p + q` is even. With `n = 4` supplied by Q1, this
  retained existence gives the chirality projectors
  `P_L = (I - gamma_5) / 2` and `P_R = (I + gamma_5) / 2`, supplying
  the factor-of-`1/2` chirality halving consumed by the proof-walk.

- **R3 CPT exact preservation (factor of 2 particle-antiparticle).**
  Supplied by
  [`CPT_EXACT_NOTE.md`](CPT_EXACT_NOTE.md)
  (`retained`, positive_theorem) and its decoration
  [`CPT_PARTICLE_ANTIPARTICLE_MASS_EQUALITY_THEOREM_NOTE_2026-05-02.md`](CPT_PARTICLE_ANTIPARTICLE_MASS_EQUALITY_THEOREM_NOTE_2026-05-02.md)
  (`decoration_under_cpt_exact_note`). Exact CPT preservation pairs
  each particle with a distinct antiparticle state of equal mass,
  supplying the `2 (particle-antiparticle)` factor consumed by the
  proof-walk.

- **R4 Fermionic CAR irreducible single-mode carrier dim 2.** Supplied
  by
  [`SPIN_STATISTICS_CARDINALITY_PAULI_EXCLUSION_NARROW_THEOREM_NOTE_2026-05-10.md`](SPIN_STATISTICS_CARDINALITY_PAULI_EXCLUSION_NARROW_THEOREM_NOTE_2026-05-10.md)
  (`retained`) and
  [`SPIN_STATISTICS_BEREZIN_DETERMINANT_NARROW_THEOREM_NOTE_2026-05-10.md`](SPIN_STATISTICS_BEREZIN_DETERMINANT_NARROW_THEOREM_NOTE_2026-05-10.md)
  (`retained_bounded`). The fermionic CAR algebra has a 2-dim
  irreducible single-mode realisation, and the squared creation
  operator vanishes (`(a^†)^2 = 0`), giving single-mode occupation
  `n in {0, 1}`. R4 supplies the per-mode finite Grassmann / Berezin
  algebraic framing in which spin and particle-antiparticle labels are
  the two independent binary occupation indices on a Dirac state.

The per-site `Cl(3, 0)` algebra supporting R1 is supplied by the
retained Cl(3) backbone
[`CL3_COMPLEXIFICATION_SPLIT_NARROW_THEOREM_NOTE_2026-05-10.md`](CL3_COMPLEXIFICATION_SPLIT_NARROW_THEOREM_NOTE_2026-05-10.md)
(`retained`) and
[`CL3_PAULI_IRREP_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10.md`](CL3_PAULI_IRREP_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10.md)
(`retained`); these are framework-baseline citations and not
load-bearing for the dof arithmetic.

## Supplied admission packet (Q1-Q2, not framework-retained)

The following admission packet supplies the Lorentzian-signature
spinor-space dimension and the on-shell thermal-counting convention.
Q1-Q2 are declared explicitly for this bridge; they are not derived
from the framework here and are not promoted to axioms.

- **Q1 Cl(3,1) Lorentzian signature extension (`n = 4` even generator
  count; `Cl(3, 1) cong M_4(R)`).** The framework's per-site `Cl(3, 0)`
  algebra is extended by one additional anticommuting generator `e_4`
  with `e_4^2 = -I` (the Lorentzian-signature timelike sign). The
  resulting algebra is `Cl(3, 1) cong M_4(R)`, whose unique faithful
  irreducible real module is the standard `R^4` action of `M_4(R)`, of
  real dimension 4. The narrow Cartan-Bott classification is recorded
  in
  `CL3_TO_CL31_SPINOR_EXTENSION_NARROW_THEOREM_NOTE_2026-05-27.md`
  (currently `unaudited`); the sign-`ε = -1` choice itself is the
  Wick-rotation admission **P2** of
  [`HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md`](HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md).
  Q1 is admitted, not derived, on this bridge.

- **Q2 On-shell relativistic thermal-counting convention (factor of
  `1/2` from off-shell to on-shell).** A four-component complex Dirac
  spinor `psi` has `4 * 2 = 8` real off-shell components. After
  imposing the Dirac equation `(i gamma^mu partial_mu - m) psi = 0` as
  a first-order on-shell constraint, the on-shell relativistic state
  count is `8 / 2 = 4` real on-shell components per spacetime point
  (Peskin & Schroeder, *An Introduction to Quantum Field Theory*,
  §3.3; Weinberg, *The Quantum Theory of Fields*, Vol. I, §5.5). Q2
  is the standard textbook on-shell convention; it is admitted here as
  external bookkeeping infrastructure, not derived on the framework
  surface.

Q1 names the algebraic extension to `n = 4` Clifford generators; Q2
names the on-shell vs off-shell relativistic-counting convention used
by the parent thermal-inventory note.

## Proof-walk

Each row of the table is a step in the parent inventory note's
fermion-side arithmetic. The "Load-bearing input" column names the
smallest framework-retained authority or admitted premise consumed;
the "Lattice-action input?" column shows that no lattice-action
quantity (plaquette, staggered phase, link unitary, `u_0`,
Monte-Carlo measurement, fitted comparator) enters the proof-walk.

| Step | Statement | Load-bearing input | Lattice-action input? |
|---|---|---|---|
| (F1) | Cl(3,1) Lorentzian extension at `n = 4` total generator count | Q1 | no |
| (F2) | Volume-element chirality: `gamma_5` exists iff `n` even; with `n = 4`, `gamma_5` exists | R2 + (F1) | no |
| (F3) | Chirality projectors `P_L = (I - gamma_5)/2`, `P_R = (I + gamma_5)/2` are well-defined orthogonal projectors with `P_L + P_R = I`, `P_L P_R = 0` | R2 | no |
| (F4) | Faithful real irrep of `Cl(3, 1) cong M_4(R)` has real dimension 4 | Q1 | no |
| (F5) | Spin label per Dirac state: `m_s in {-1/2, +1/2}` gives factor 2 from per-site `j = 1/2` | R1 | no |
| (F6) | Particle-antiparticle label per Dirac state: CPT pairs `psi <-> psi^c` of equal mass, factor 2 | R3 | no |
| (F7) | Naive off-shell real-component count of a four-component complex Dirac spinor: `4 (complex) * 2 (real per complex) = 8` | (F4) + Q2 (admission) | no |
| (F8) | On-shell Dirac equation constraint halves naive 8 to 4: `8 / 2 = 4` | Q2 | no |
| (F9) | Equivalent thermal factorisation: Dirac on-shell dof = `2 (spin) * 2 (particle-antiparticle) = 4` | R1 (spin factor) + R3 (particle-antiparticle factor) | no |
| (F10) | Chirality halving for Weyl: `P_L psi` projects out half of the four spinor components, so Weyl on-shell dof = `4 / 2 = 2` | R2 + (F8) | no |
| (F11) | Equivalent thermal factorisation: Weyl on-shell dof = `2 (helicity-antiparticle)` | R3 + (F10) (one chirality projected, helicity-antiparticle is the surviving doublet) | no |
| (F12) | Active neutrino is single Weyl per generation (no `nu_R` in the relativistic thermal inventory, by P1 of the parent note) | P1 of parent note + (F11) | no |

The proof-walk does not cite the Wilson plaquette action, staggered
phases, Brillouin-zone labels, link unitaries, the lattice scale
`u_0`, a Monte Carlo measurement, or a fitted observational value.

## Exact arithmetic check

The Dirac on-shell thermal dof factorises as

```text
dof_Dirac (on-shell)  =  2  (spin, m_s in {-1/2, +1/2}, from R1)
                      *  2  (particle-antiparticle, from R3 CPT)
                      =  4.
```

Equivalently, from the spinor-space dimension and Q2 on-shell halving,

```text
dof_Dirac (on-shell)  =  dim_R V_(3,1)  *  2  /  2
                      =  4  *  2  /  2
                      =  4,
```

where `dim_R V_(3,1) = 4` is the real dimension of the faithful real
irreducible module of `Cl(3, 1) cong M_4(R)` (Q1), the `* 2` is the
real-vs-complex doubling for a complex Dirac spinor (4 complex
components -> 8 real components), and the `/ 2` is the Q2 on-shell
halving from the first-order Dirac equation.

The Weyl on-shell thermal dof factorises as

```text
dof_Weyl (on-shell)  =  dof_Dirac (on-shell)  /  2
                     =  4  /  2
                     =  2,
```

where the `/ 2` is the chirality projection `P_L` (or `P_R`) supplied
by R2 (existence of `gamma_5` at even `n = 4`).

Equivalently, from the spin / particle-antiparticle factorisation,

```text
dof_Weyl (on-shell)  =  2  (helicity-antiparticle)
                     =  2,
```

where the surviving Weyl doublet labels two independent on-shell
states; the two-particle/antiparticle states of a Dirac fermion
collapse to a single "helicity-antiparticle" pair after chirality
projection, matching the parent note's `2 (helicity-antiparticle)`
wording.

The runner repeats both factorisations with `fractions.Fraction` (no
floating-point arithmetic) and checks all twelve substeps against
the named retained / admitted inputs.

## Mapping to the parent note's P4 premise

The parent note's P4 premise reads:

> Each Dirac fermion state contributes `2 (spin) * 2 (particle-antiparticle)
> = 4` thermal degrees of freedom. The active neutrino is a single
> Weyl fermion per generation, contributing `2 (helicity-antiparticle)`
> states.

This bridge supplies the algebraic content of P4 in two parts:

- **The two integer factors `2 * 2 = 4` of the Dirac side** are
  framework-retained (R1 supplies spin = 2, R3 supplies
  particle-antiparticle = 2). After this bridge lands, the parent
  note's P4 premise can be restated as:
  
  > Each Dirac fermion state contributes `2 (spin, from R1) * 2
  > (particle-antiparticle, from R3) = 4` thermal degrees of freedom,
  > with the on-shell convention from Q2 and the four-component
  > spinor space from Q1.
  
  The two `2`s are no longer premise content; only the admissions
  Q1 (Cl(3,1) signature extension) and Q2 (on-shell counting
  convention) remain in the supplied premise packet for the parent
  note.

- **The Weyl `2 (helicity-antiparticle)` factor** is also
  framework-retained on the chirality-halving side: R2 supplies the
  existence of the `gamma_5` projector at the even-`n` Clifford
  algebra cell, which halves the Dirac state count to the Weyl state
  count. The remaining factor `2` is the surviving
  helicity-antiparticle doublet after chirality projection, supplied
  jointly by R1 (helicity replaces spin under chirality projection)
  and R3 (antiparticle pairing for the single chirality).

P4 of the parent note can therefore be **retired from the named-premise
packet** to the framework-retained side, with the residual admission
content explicitly relocated to Q1 (signature extension) and Q2
(on-shell counting). This is the operational purpose of the present
bridge note.

## Dependencies

Load-bearing retained dependencies for this bridge:

- [`PER_SITE_SU2_SPIN_HALF_THEOREM_NOTE_2026-05-02.md`](PER_SITE_SU2_SPIN_HALF_THEOREM_NOTE_2026-05-02.md)
  retained per-site `j = 1/2` SU(2) carrier (`retained`).
- [`CLIFFORD_VOLUME_CHIRALITY_EVEN_DIMENSION_NARROW_THEOREM_NOTE_2026-05-10.md`](CLIFFORD_VOLUME_CHIRALITY_EVEN_DIMENSION_NARROW_THEOREM_NOTE_2026-05-10.md)
  retained `gamma_5` exists iff `n` even (`retained`).
- [`CPT_EXACT_NOTE.md`](CPT_EXACT_NOTE.md)
  retained CPT exact preservation (`retained`, positive_theorem).
- [`CPT_PARTICLE_ANTIPARTICLE_MASS_EQUALITY_THEOREM_NOTE_2026-05-02.md`](CPT_PARTICLE_ANTIPARTICLE_MASS_EQUALITY_THEOREM_NOTE_2026-05-02.md)
  retained particle-antiparticle equal-mass decoration
  (`decoration_under_cpt_exact_note`).
- [`SPIN_STATISTICS_CARDINALITY_PAULI_EXCLUSION_NARROW_THEOREM_NOTE_2026-05-10.md`](SPIN_STATISTICS_CARDINALITY_PAULI_EXCLUSION_NARROW_THEOREM_NOTE_2026-05-10.md)
  retained fermionic CAR cardinality (`retained`).
- [`SPIN_STATISTICS_BEREZIN_DETERMINANT_NARROW_THEOREM_NOTE_2026-05-10.md`](SPIN_STATISTICS_BEREZIN_DETERMINANT_NARROW_THEOREM_NOTE_2026-05-10.md)
  retained Berezin-determinant identity (`retained_bounded`).
- `G_STAR_SM_CONTENT_AT_LEPTOGENESIS_FROM_RETAINED_FRAMEWORK_CONTENT_BOUNDED_THEOREM_NOTE_2026-05-28.md`
  parent thermal-inventory proof-walk whose P4 premise this bridge
  retires.

Admitted (not framework-retained) load-bearing inputs:

- `CL3_TO_CL31_SPINOR_EXTENSION_NARROW_THEOREM_NOTE_2026-05-27.md`
  Cartan-Bott classification cell `Cl(3, 1) cong M_4(R)` (currently
  `unaudited`); supplies the algebraic content of Q1 conditional on
  the sign-`ε = -1` Wick-rotation choice (P2 of the hierarchy honest-
  status note).
- [`HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md`](HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md)
  parent honest-status note naming the Wick-rotation `Z^3 -> Z^4`
  admission (P2). Q1 of the present bridge is exactly the algebraic
  content of P2 expressed in Clifford-algebra language.

Non-load-bearing context:

- `CL3_COMPLEXIFICATION_SPLIT_NARROW_THEOREM_NOTE_2026-05-10.md`
  retained `Cl(3, 0) tensor_R C cong M_2(C) + M_2(C)` chirality-pair
  structure at signature `(3, 0)`. Framework-baseline backbone for
  the per-site `Cl(3, 0)` algebra; not load-bearing for the dof
  arithmetic.
- `CL3_PAULI_IRREP_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10.md`
  retained Pauli-irrep uniqueness at `Cl(3, 0)` over `C`.
  Framework-baseline backbone; not load-bearing for the dof
  arithmetic.
- `MINIMAL_AXIOMS_2026-05-20.md` framework-baseline two-axiom
  packet; context only.

These are imported authorities for a bounded admission bridge. The
row remains unaudited until the independent audit lane reviews this
note, its dependencies, the supplied admission packet, and the runner.

## Boundaries

This bridge does not close:

- derivation of the Cl(3,1) Lorentzian signature itself (the Q1
  admission; equivalent to P2 of `HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md`);
- derivation of the on-shell relativistic-counting convention (Q2;
  textbook Peskin-Schroeder / Weinberg infrastructure consumed
  externally);
- derivation of the Lorentz group `SO(3, 1)` or its spin cover
  `SL(2, C)`;
- derivation of the spin-statistics theorem (R4 supplies the CAR
  cardinality core but does not derive the spin-statistics theorem
  proper);
- derivation of the Dirac equation `(i gamma^mu partial_mu - m) psi
  = 0` itself;
- the staggered-Dirac realization gate (still open);
- closure of the parent note `G_STAR_SM_CONTENT_AT_LEPTOGENESIS_FROM_RETAINED_FRAMEWORK_CONTENT_BOUNDED_THEOREM_NOTE_2026-05-28.md`
  (the parent inventory note retains P1, P2, P3, P5 as admitted
  premises; this bridge retires only P4 to the retained side and
  exposes its residual admission content as Q1 + Q2);
- any downstream cosmology, leptogenesis, or DM claim;
- promotion of `cl3_to_cl31_spinor_extension_narrow_theorem_note_2026-05-27`
  from `unaudited` (the present bridge does not alter the audit
  status of cited authorities);
- any parent theorem/status promotion.

## What this claims and does not claim

- The bridge **claims** that the four-factor decomposition `dof_Dirac
  = 2 (spin) * 2 (particle-antiparticle) = 4` follows from R1 + R3 as
  exact integer arithmetic, given the Q1 + Q2 admission packet, and
  that the Weyl halving `dof_Weyl = dof_Dirac / 2 = 2` follows from
  R2 (chirality operator at even `n`).
- The bridge **does not claim** that the Cl(3,1) signature extension
  is forced by any retained framework primitive. The sign-`ε = -1`
  choice is the open content of P2 of
  `HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md`.
- The bridge **does not claim** that the on-shell vs off-shell
  reduction `/ 2` is a framework derivation; it is a textbook
  on-shell convention named explicitly in Q2.
- The bridge **does not claim** parent-note status promotion. The
  parent note `G_STAR_SM_CONTENT_AT_LEPTOGENESIS_FROM_RETAINED_FRAMEWORK_CONTENT_BOUNDED_THEOREM_NOTE_2026-05-28.md`
  retains the remaining premises P1 (declared SM particle inventory),
  P2 (two transverse polarizations per massless vector), P3 (four
  real scalar dof in complex Higgs doublet), and P5 (temperature
  regime). Only P4 is shifted to the retained side, with its residual
  admission content named as Q1 + Q2 of the present bridge.
- The bridge **does not claim** that the framework's per-site Hilbert
  space becomes `R^4`-valued under Wick rotation. The framework's
  per-site site module is `C^2`-valued per
  `cl3_per_site_hilbert_dim_two_theorem_note_2026-05-02`; the
  `Cl(3, 1) cong M_4(R)` action lives on the abstract real
  Clifford algebra at the extended `n = 4` signature `(3, 1)`, not
  on the per-site site module.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/audit_companion_dirac_weyl_fermion_dof_from_lorentz_and_chirality_2026_05_28.py
```

Expected:

```text
TOTAL: PASS=<n> FAIL=0
VERDICT: bounded admission bridge passes; Dirac dof = 4 and Weyl
dof = 2 follow from the retained-framework packet R1-R4 plus
supplied admission packet Q1-Q2 by exact rational arithmetic.
```
