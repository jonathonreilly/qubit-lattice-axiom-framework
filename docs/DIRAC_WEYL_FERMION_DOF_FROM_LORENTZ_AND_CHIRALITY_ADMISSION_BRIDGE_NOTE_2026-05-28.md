# Dirac / Weyl Fermion DOF From Lorentz and Chirality Admission Bridge Note

**Date:** 2026-05-28
**Claim type:** bounded_theorem
**Status authority:** source-note proposal only; audit verdict and
effective status are set by the independent audit lane.
**Primary runner:** [`scripts/audit_companion_dirac_weyl_fermion_dof_from_lorentz_and_chirality_2026_05_28.py`](../scripts/audit_companion_dirac_weyl_fermion_dof_from_lorentz_and_chirality_2026_05_28.py)

## 2026-06-07 source-packet repair

The audit blocker named two residual inputs: Q1 (`Cl(3,1)` signature
extension) and Q2 (on-shell thermal counting). On current `main`, Q1's finite
Clifford-algebra content is now audit-retained by
[`CL3_TO_CL31_SPINOR_EXTENSION_NARROW_THEOREM_NOTE_2026-05-27.md`](CL3_TO_CL31_SPINOR_EXTENSION_NARROW_THEOREM_NOTE_2026-05-27.md).
This repair updates the row accordingly:

- Q1 is retired as an unsupported algebraic admission for this dof bridge.
- Q2 is repaired as a textbook-counting import: the on-shell halving is now a
  source-local finite-rank statement for the Dirac mass-shell operator on
  `C^4`.
- The row still does not claim physical Wick rotation, spacetime dynamics, or
  forced Lorentzian-sign selection.
- The row still does not derive the Dirac equation or the physical thermal
  inventory; it proves the counting once that first-order mass-shell equation
  is the active free-particle equation.
- This is not a ledger retag; independent audit owns any effective-status
  change.

## 2026-06-08 label-semantics safe-narrow

The refreshed audit agrees that the finite algebra checks close, but flags a
remaining physical-label bridge: CPT exactness does not by itself derive that
the thermal inventory has a distinct particle-antiparticle species label, and
the per-site `SU(2)` doublet does not by itself derive the physical
spin/helicity label used in P4.

This note is therefore narrowed. It proves the finite on-shell rank,
chirality-halving, and integer label arithmetic **conditional on the supplied
physical label semantics**. It does not replace P4 of the parent thermal
inventory by itself. A future retained bridge must still identify the
framework `SU(2)` doublet with the physical spin/helicity label and the CPT
pairing with the distinct thermal particle-antiparticle label.

## Claim

Given the retained Cl(3,1) finite Clifford-algebra source packet (Q1
below), the source-local on-shell rank certificate (Q2 below), and the
existing framework authority packet (R1-R4 below), the finite label-counting
arithmetic used by the Standard Model fermion thermal degree-of-freedom counts
named in premise P4 of the parent thermal-inventory proof-walk
`G_STAR_SM_CONTENT_AT_LEPTOGENESIS_FROM_SUPPLIED_THERMAL_INVENTORY_BOUNDED_THEOREM_NOTE_2026-05-28.md`,

```text
Dirac thermal dof per flavour-colour state = 2 (spin) * 2 (particle-antiparticle) = 4,
Weyl thermal dof per flavour-colour state  = 2 (helicity-antiparticle),
```

reduce to exact rational arithmetic once the physical label semantics are
supplied. The factor `2` for the `SU(2)` doublet is checked from R1
(per-site `j = 1/2`); the factor `2` for the paired label is checked from R3
(CPT exact) after a particle/antiparticle thermal-label interpretation is
supplied; the factor `2` halving from Dirac to Weyl comes from R2 (chirality
operator `gamma_5` existence at even total Clifford generator count). The
Cl(3,1) algebra-cell fact supplying the `n = 4` even-generator count is
now sourced by the retained Q1 authority
`CL3_TO_CL31_SPINOR_EXTENSION_NARROW_THEOREM_NOTE_2026-05-27.md`.
The on-shell halving is no longer imported as a textbook convention:
Q2 now proves, by explicit Dirac-operator rank, that imposing
`(gamma^mu p_mu - m) psi = 0` on an on-shell momentum leaves a
two-complex-dimensional particle solution space per energy branch.

This is a Q1/Q2-counting-repaired bounded bridge. It does **not** add a new
axiom, a new repo-wide theory class, or a retained-status claim. Q1 is retired
only as the finite Clifford-algebra cell `Cl(3,1) ~= M_4(R)` with a
four-real-dimensional faithful module; it does **not** claim the
framework has derived Wick rotation, spacetime dynamics, or physical
selection of the Lorentzian sign. Q2 is retired only as the finite
linear-algebra count for an already-supplied Dirac mass-shell equation;
this bridge does **not** derive that equation, the free-field dynamics,
or the physical thermal inventory itself.
Parent-note replacement of P4 remains blocked on the separate physical-label
bridge; this source note supplies only the finite algebraic count and
source-local on-shell rank certificate.

## Framework authority packet (R1-R4)

The following existing framework authorities supply the load-bearing
algebraic multiplicities consumed by the bridge. Their effective
statuses are checked by the audit pipeline and are not asserted by this
source note.

- **R1 Per-site `j = 1/2` SU(2) doublet (factor of 2 label states).**
  Supplied by
  [`PER_SITE_SU2_SPIN_HALF_THEOREM_NOTE_2026-05-02.md`](PER_SITE_SU2_SPIN_HALF_THEOREM_NOTE_2026-05-02.md)
  as an existing audit-ledger authority. On every framework site, the
  per-site Hilbert space carries exactly the `j = 1/2` irreducible
  representation of su(2); the diagonal generator `S_3 = sigma_3 / 2`
  has eigenvalues
  `m in {-1/2, +1/2}`, supplying a two-label algebraic doublet. This row does
  not by itself derive that this doublet is the physical thermal spin/helicity
  label.

- **R2 Chirality operator `gamma_5` exists iff `n` (total Clifford
  generator count) is even.** Supplied by
  [`CLIFFORD_VOLUME_CHIRALITY_EVEN_DIMENSION_NARROW_THEOREM_NOTE_2026-05-10.md`](CLIFFORD_VOLUME_CHIRALITY_EVEN_DIMENSION_NARROW_THEOREM_NOTE_2026-05-10.md)
  as an existing audit-ledger authority. An element `gamma_5` of
  `Cl_C(p, q)` satisfying `gamma_5^2 = +I` and
  `{gamma_5, gamma_mu} = 0` for every generator exists iff
  `n = p + q` is even. With `n = 4` supplied by Q1, this theorem gives
  the chirality projectors
  `P_L = (I - gamma_5) / 2` and `P_R = (I + gamma_5) / 2`, supplying
  the factor-of-`1/2` chirality halving consumed by the proof-walk.

- **R3 CPT exact preservation (paired-label factor of 2 after physical-label
  interpretation).**
  Supplied by
  [`CPT_EXACT_NOTE.md`](CPT_EXACT_NOTE.md)
  as an existing audit-ledger authority. Exact CPT preservation supplies the
  pairing symmetry used by the two-label arithmetic once a physical
  particle-antiparticle thermal-label interpretation is supplied. This row
  does not derive that distinct thermal species label from CPT alone. The
  mass-equality decoration
  `CPT_PARTICLE_ANTIPARTICLE_MASS_EQUALITY_THEOREM_NOTE_2026-05-02.md`
  is reader context only; it is not load-bearing for this integer
  count.

- **R4 Fermionic CAR irreducible single-mode carrier dim 2.** Supplied
  by
  [`SPIN_STATISTICS_CARDINALITY_PAULI_EXCLUSION_NARROW_THEOREM_NOTE_2026-05-10.md`](SPIN_STATISTICS_CARDINALITY_PAULI_EXCLUSION_NARROW_THEOREM_NOTE_2026-05-10.md)
  and
  [`SPIN_STATISTICS_BEREZIN_DETERMINANT_NARROW_THEOREM_NOTE_2026-05-10.md`](SPIN_STATISTICS_BEREZIN_DETERMINANT_NARROW_THEOREM_NOTE_2026-05-10.md)
  as existing audit-ledger authorities. The fermionic CAR algebra has a 2-dim
  irreducible single-mode realisation, and the squared creation
  operator vanishes (`(a^†)^2 = 0`), giving single-mode occupation
  `n in {0, 1}`. R4 supplies the per-mode finite Grassmann / Berezin
  algebraic framing in which spin and particle-antiparticle labels are
  the two independent binary occupation indices on a Dirac state.

The per-site `Cl(3, 0)` algebra supporting R1 is supplied by the
Cl(3) backbone
`CL3_COMPLEXIFICATION_SPLIT_NARROW_THEOREM_NOTE_2026-05-10.md` and
`CL3_PAULI_IRREP_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10.md`; these
are framework-baseline context pointers and not load-bearing for the
dof arithmetic.

## Retained source plus source-local counting packet (Q1-Q2)

The following packet supplies the Lorentzian-signature spinor-space
dimension and the on-shell thermal-counting count. Q1 is now a retained
finite Clifford-algebra authority on the current ledger; Q2 is repaired
inside this packet as a finite rank calculation. Neither is promoted to
an axiom.

- **Q1 Cl(3,1) finite Clifford-algebra source (`n = 4` even generator
  count; `Cl(3, 1) ≅ M_4(R)`).** This is now supplied by the retained
  source
  [`CL3_TO_CL31_SPINOR_EXTENSION_NARROW_THEOREM_NOTE_2026-05-27.md`](CL3_TO_CL31_SPINOR_EXTENSION_NARROW_THEOREM_NOTE_2026-05-27.md).
  That theorem proves the two one-generator real-Clifford extensions of
  the framework `Cl(3,0)` cell, identifies the `ε = -1` branch as
  `Cl(3,1) ≅ M_4(R)`, and gives the faithful real `R^4` module used
  here. Q1 is therefore retired as an unsupported admission for this
  local algebraic dof bridge. Boundary: the retained theorem does not
  derive Wick rotation, physical spacetime, dynamics, or why the
  framework must select the Lorentzian sign; any downstream use that
  requires those physical claims must still carry that separate
  bounded premise.

- **Q2 On-shell finite-rank counting certificate (factor of `1/2`
  from off-shell spinor space to one energy-branch solution space).**
  Let the retained Q1 `Cl(3,1)` cell be represented by gamma matrices
  satisfying `{gamma^mu, gamma^nu} = 2 eta^{mu nu} I_4` with
  `eta = diag(+,-,-,-)` after the standard real/complex presentation
  change used by the runner. For a momentum satisfying the mass-shell
  relation `p_0^2 - |p|^2 = m^2`, the Dirac operator
  `D(p) = gamma^mu p_mu - m I_4` obeys `D(p)(gamma^mu p_mu + m I_4)=0`
  on shell. In the explicit Q1 gamma representation the runner checks
  that `rank D(p) = 2` and therefore `dim_C ker D(p) = 2` for:

  ```text
  p = (m, 0, 0, 0)        rest branch,
  p = (5, 0, 0, 4), m=3   nonzero-momentum branch,
  p = (-5, 0, 0, 4), m=3  antiparticle/negative-energy branch.
  ```

  Thus the "on-shell halving" is not an imported textbook counting
  convention in this row: it is the finite linear-algebra fact
  `C^4 -> ker D(p)` with nullity `2` per energy branch. The real
  off-shell phrase `8 -> 4` is the same statement after multiplying
  complex dimensions by `2`. Boundary: Q2 does not derive the Dirac
  equation, does not derive the physical free-field dynamics, and does
  not by itself prove that the high-temperature thermal inventory must
  use this free Dirac mass-shell surface.

Q1 names the retained algebraic extension to `n = 4` Clifford
generators; Q2 supplies the source-local on-shell rank count used by
the parent thermal-inventory note.

## Proof-walk

Each row of the table is a step in the parent inventory note's
fermion-side arithmetic. The "Load-bearing input" column names the
smallest framework authority or admitted premise consumed;
the "Lattice-action input?" column shows that no lattice-action
quantity (plaquette, staggered phase, link unitary, `u_0`,
Monte-Carlo measurement, fitted comparator) enters the proof-walk.

| Step | Statement | Load-bearing input | Lattice-action input? |
|---|---|---|---|
| (F1) | Cl(3,1) Lorentzian extension at `n = 4` total generator count | Q1 | no |
| (F2) | Volume-element chirality: `gamma_5` exists iff `n` even; with `n = 4`, `gamma_5` exists | R2 + (F1) | no |
| (F3) | Chirality projectors `P_L = (I - gamma_5)/2`, `P_R = (I + gamma_5)/2` are well-defined orthogonal projectors with `P_L + P_R = I`, `P_L P_R = 0` | R2 | no |
| (F4) | Faithful real irrep of `Cl(3, 1) ≅ M_4(R)` has real dimension 4 | Q1 | no |
| (F5) | Algebraic `SU(2)` doublet label: `m_s in {-1/2, +1/2}` gives a factor 2; physical spin/helicity interpretation remains a separate bridge | R1 + supplied label semantics | no |
| (F6) | Paired label per Dirac state: CPT pairs `psi <-> psi^c` of equal mass, factor 2 after the physical particle-antiparticle thermal-label interpretation is supplied | R3 + supplied label semantics | no |
| (F7) | Naive off-shell real-component count of a four-component complex Dirac spinor: `4 (complex) * 2 (real per complex) = 8` | (F4) + complexification bookkeeping | no |
| (F8) | On-shell Dirac equation constraint halves naive 8 to 4: `rank(gamma.p - m)=2`, so `dim_C ker=2` per energy branch | Q2 finite-rank certificate | no |
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

Equivalently, from the spinor-space dimension and Q2 finite-rank
on-shell halving,

```text
dof_Dirac (on-shell)  =  dim_R V_(3,1)  *  2  /  2
                      =  4  *  2  /  2
                      =  4,
```

where `dim_R V_(3,1) = 4` is the real dimension of the faithful real
irreducible module of `Cl(3, 1) ≅ M_4(R)` (Q1), the `* 2` is the
real-vs-complex doubling for a complex Dirac spinor (4 complex
components -> 8 real components), and the `/ 2` is the Q2 finite-rank
halving from the first-order Dirac mass-shell operator.

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
floating-point arithmetic) and checks all twelve substeps against the named
framework-authority inputs plus the explicitly supplied physical-label
semantics.

## Mapping to the parent note's P4 premise

The parent note's P4 premise reads:

> Each Dirac fermion state contributes `2 (spin) * 2 (particle-antiparticle)
> = 4` thermal degrees of freedom. The active neutrino is a single
> Weyl fermion per generation, contributing `2 (helicity-antiparticle)`
> states.

This bridge supplies the algebraic counting support used by P4 in two parts,
but it does **not** replace P4 by itself:

- **The two integer factors `2 * 2 = 4` of the Dirac side** are
  supplied by existing framework authorities plus the still-open physical
  label semantics (R1 supplies the algebraic doublet, R3 supplies the exact
  pairing symmetry). After this bridge is independently audited, the parent
  note's P4 premise still needs a separate physical-label bridge before it can
  be restated as:
  
  > Each Dirac fermion state contributes `2 (spin, from R1) * 2
  > (particle-antiparticle, from R3) = 4` thermal degrees of freedom,
  > with the source-local on-shell rank count from Q2 and the
  > four-component spinor space from Q1.
  
  The two `2`s are then no longer unattributed arithmetic content. Q1
  (finite `Cl(3,1)` algebra cell) is retained-sourced, and Q2's
  textbook on-shell-counting import is replaced by this source-local
  rank certificate. The residual boundary is narrower and explicit: the
  bridge does not derive the Dirac equation/free-field mass-shell input, the
  physical thermal-inventory use of that input, the physical spin/helicity
  label, or the distinct particle-antiparticle thermal label.

- **The Weyl `2 (helicity-antiparticle)` factor** is also
  supported on the chirality-halving side: R2 supplies the existence of
  the `gamma_5` projector at the even-`n` Clifford algebra cell, which
  halves the Dirac state count to the Weyl state count. The remaining
  factor `2` is the surviving doublet after chirality projection,
  conditional on the physical helicity-antiparticle label bridge that is
  still open.

P4 of the parent note therefore cannot be replaced by this bounded row alone.
The operational purpose of this source note is to retire the textbook
on-shell-counting import and isolate the remaining physical-label bridge.

## Dependencies

Load-bearing framework dependencies for this bridge:

- [`PER_SITE_SU2_SPIN_HALF_THEOREM_NOTE_2026-05-02.md`](PER_SITE_SU2_SPIN_HALF_THEOREM_NOTE_2026-05-02.md)
  per-site `j = 1/2` SU(2) carrier.
- [`CLIFFORD_VOLUME_CHIRALITY_EVEN_DIMENSION_NARROW_THEOREM_NOTE_2026-05-10.md`](CLIFFORD_VOLUME_CHIRALITY_EVEN_DIMENSION_NARROW_THEOREM_NOTE_2026-05-10.md)
  `gamma_5` exists iff `n` even.
- [`CPT_EXACT_NOTE.md`](CPT_EXACT_NOTE.md)
  CPT exact preservation.
- [`SPIN_STATISTICS_CARDINALITY_PAULI_EXCLUSION_NARROW_THEOREM_NOTE_2026-05-10.md`](SPIN_STATISTICS_CARDINALITY_PAULI_EXCLUSION_NARROW_THEOREM_NOTE_2026-05-10.md)
  fermionic CAR cardinality.
- [`SPIN_STATISTICS_BEREZIN_DETERMINANT_NARROW_THEOREM_NOTE_2026-05-10.md`](SPIN_STATISTICS_BEREZIN_DETERMINANT_NARROW_THEOREM_NOTE_2026-05-10.md)
  Berezin-determinant identity.

Retained / bounded source inputs:

- [`CL3_TO_CL31_SPINOR_EXTENSION_NARROW_THEOREM_NOTE_2026-05-27.md`](CL3_TO_CL31_SPINOR_EXTENSION_NARROW_THEOREM_NOTE_2026-05-27.md)
  is now the retained Q1 source for the Cartan-Bott classification cell
  `Cl(3, 1) ≅ M_4(R)` and its four-real-dimensional faithful module.
- Q2 finite-rank on-shell counting is source-local to this note and runner:
  explicit gamma matrices verify `rank(gamma.p - m)=2` on mass shell and
  chirality projectors split the massless branch.
- `HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md`
  parent honest-status note naming the Wick-rotation `Z^3 -> Z^4`
  admission (P2). This bridge does not claim to close that physical
  Wick-rotation premise; it only uses the retained finite
  Clifford-algebra Q1 cell.

Non-load-bearing context:

- `CL3_COMPLEXIFICATION_SPLIT_NARROW_THEOREM_NOTE_2026-05-10.md`
  `Cl(3, 0) tensor_R C ≅ M_2(C) + M_2(C)` chirality-pair
  structure at signature `(3, 0)`. Framework-baseline backbone for
  the per-site `Cl(3, 0)` algebra; not load-bearing for the dof
  arithmetic.
- `CL3_PAULI_IRREP_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10.md`
  Pauli-irrep uniqueness at `Cl(3, 0)` over `C`. Framework-baseline
  backbone; not load-bearing for the dof arithmetic.
- `MINIMAL_AXIOMS_2026-05-20.md` framework-baseline two-axiom
  packet; context only.

These are imported authorities for a bounded Q1/Q2-counting-repaired bridge. The row
remains under independent audit authority until the audit lane reviews
this note, its dependencies, the source-local Q2 rank certificate, and
the runner.

## Boundaries

This bridge does not close:

- physical derivation of Wick rotation, spacetime dynamics, or forced
  Lorentzian-sign selection. Q1 retires only the finite algebraic
  `Cl(3,1) ~= M_4(R)` cell used for the spinor module;
- derivation of the Dirac equation/free-field dynamics themselves. Q2
  proves the finite count once the first-order Dirac mass-shell equation
  is the active equation;
- derivation of the Lorentz group `SO(3, 1)` or its spin cover
  `SL(2, C)`;
- derivation of the spin-statistics theorem (R4 supplies the CAR
  cardinality core but does not derive the spin-statistics theorem
  proper);
- the staggered-Dirac realization gate (still open);
- closure of the parent note
  `G_STAR_SM_CONTENT_AT_LEPTOGENESIS_FROM_SUPPLIED_THERMAL_INVENTORY_BOUNDED_THEOREM_NOTE_2026-05-28.md`
  (the parent inventory note still has P1, P2, P3, P5 as admitted
  premises; this bridge only supports the finite arithmetic component of
  P4);
- physical derivation that the framework `SU(2)` doublet is the thermal
  spin/helicity label;
- physical derivation that CPT exactness supplies the distinct thermal
  particle-antiparticle species label;
- any downstream cosmology, leptogenesis, or DM claim;
- promotion of `cl3_to_cl31_spinor_extension_narrow_theorem_note_2026-05-27`
  (the present bridge does not alter the audit status of cited
  authorities);
- any parent theorem/status promotion.

## What this claims and does not claim

- The bridge **claims** that the four-factor decomposition `dof_Dirac
  = 2 * 2 = 4` is exact integer arithmetic, given retained Q1 plus the Q2
  finite-rank on-shell count and the supplied physical-label semantics, and
  that the Weyl halving `dof_Weyl = dof_Dirac / 2 = 2` follows from R2
  (chirality operator at even `n`).
- The bridge **does not claim** that R1 and R3 alone derive the physical
  spin/helicity and particle-antiparticle thermal labels. Those label
  semantics remain the open bridge named by the audit.
- The bridge **does not claim** that the Lorentzian sign is physically
  forced by the framework. The retained Q1 theorem supplies the finite
  algebraic cell; physical sign selection remains outside this bridge.
- The bridge **does not claim** that the Dirac equation/free-field
  mass-shell surface is derived by this row. It only removes the
  textbook import for the on-shell dimension count once that equation
  is supplied.
- The bridge **does not claim** parent-note status promotion. The
  parent note
  `G_STAR_SM_CONTENT_AT_LEPTOGENESIS_FROM_SUPPLIED_THERMAL_INVENTORY_BOUNDED_THEOREM_NOTE_2026-05-28.md`
  retains the remaining premises P1 (declared SM particle inventory),
  P2 (two transverse polarizations per massless vector), P3 (four
  real scalar dof in complex Higgs doublet), and P5 (temperature
  regime). P4 can only be replaced after this bounded bridge is
  independently audited and the separate physical-label bridge is supplied,
  with any separate downstream premise that tries to use Q1 as a physical
  Wick-rotation/sign-selection theorem kept outside this row.
- The bridge **does not claim** that the framework's per-site Hilbert
  space becomes `R^4`-valued under Wick rotation. The framework's
  per-site site module is `C^2`-valued per
  `cl3_per_site_hilbert_dim_two_theorem_note_2026-05-02`; the
  `Cl(3, 1) ≅ M_4(R)` action lives on the abstract real
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
VERDICT: bounded counting bridge passes; Dirac dof = 4 and Weyl
dof = 2 follow by exact rational arithmetic from retained Q1,
source-local Q2 rank counting, and the supplied physical-label semantics.
```
