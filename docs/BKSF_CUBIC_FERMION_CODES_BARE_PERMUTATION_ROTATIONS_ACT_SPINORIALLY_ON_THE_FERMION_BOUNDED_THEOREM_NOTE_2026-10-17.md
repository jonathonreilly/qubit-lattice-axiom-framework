---
claim_id: bksf_cubic_fermion_codes_bare_permutation_rotations_act_spinorially_on_the_fermion_bounded_theorem_note_2026-10-17
claim_type: bounded_theorem
claim_scope: "Supplied model: the 60 translation-invariant BKSF stabilizer codes on the cubic lattice (one qubit per edge of Z^3, one ordering of the six edge directions at every vertex) of the companion orbit note, with signed plaquette generators, one sign per plaquette orientation (8 translation-invariant sign sectors). Exact (Pauli algebra with phases, L = 4 torus): all 8 sectors of all 60 codes are valid; in two sectors the hop product of a fixed ordering's edge operators around every plaquette is plus, respectively minus, the signed generator (flux 0 and flux pi; this labels the sectors); every rotation in each code's stabilizer maps the signed group of those two sectors to itself as a bare qubit permutation P_R, while in each of the 6 mixed sectors 44 codes have a stabilizing rotation that needs a sign correction. Pair test, exact (L = 8 torus): for every one of the 108 (code, C2) pairs, in both sectors, a state with fermions at x and Rx (solved so that its excitations are R-symmetric and confined near x and Rx) has P_R-eigenvalue +1 relative to the vacuum (controls: +1 for the toric-code boson; -1 for the toric-code boson in pi flux under a plaquette-centred C2). With exchange sign -1 this gives eta_f(C2, C2) = -1 for every C2 of every code under P_R. Group cohomology then gives, for every code, that the fermion's fractionalization class for its whole rotation stabilizer (D3, D2 or Z2) under P_R equals the restriction of the spin-1/2 class w2 of SO(3). The realization P_R W with W = prod_v exp(-i pi B_v / 4) (a function of the stabilizers, constant on the code space) gives the trivial class instead, so the class belongs to the realization, not to the code alone. Not claimed: C3-only statements (no Z2 class), sign patterns that are not translation-invariant, the mixed sectors, other encodings, dynamics, the continuum limit, or any physical identification (electron, spin).""
upstream_dependencies:
  - bksf_cubic_fermion_codes_are_not_rotation_invariant_minimal_orbit_four_bounded_theorem_note_2026-10-17
runner: scripts/bksf_cubic_fermion_codes_rotations_act_by_bare_permutation_2026_10_17.py
---

# BKSF cubic fermion codes: bare-permutation rotations act spinorially on the fermion (spin-1/2 class)

**Date:** 2026-10-17
**Type:** bounded_theorem
**Status:** bounded support, unaudited. Exact on the L = 4 and L = 8 tori for the
stated family; an independent check reproduced items 1-4 at L = 6 and the
pair test for 72 pairs. Nothing is
adopted.

## Question

The companion orbit note showed two things about the translation-invariant
BKSF codes:
- each carries a fermionic point charge;
- each is fixed by a subgroup of the cubic rotations: D3, a group of order
  4, or a single C2.

An electron is a spin-1/2 fermion: a 2 pi rotation acts on it as -1. The
lattice version of this question is symmetry fractionalization. For a C2 in
the code's stabilizer, is eta_f(C2, C2) = -1, i.e. does C2^2 act on the
fermion as fermion parity?

The answer depends on how the rotation is realized on the qubits. The
framework's Lattice axiom lets rotations act by moving sites, so the natural
realization is the bare qubit permutation P_R. This note asks the question
for P_R.

## Result

1. **Sign sectors (exact).** Give the plaquette generator normal to axis c
   the sign (-1)^{s_c}. All 8 translation-invariant sectors of all 60 codes
   are valid stabilizer groups.
2. **Flux labels.** For a fixed ordering, the hop product
   A(v,b) A(v+b,a) A(v+a,b) A(v,a) around a plaquette is plus or minus the
   generator. So one uniform sector is the flux-0 sector and one is the
   flux-pi sector; this is a labelling, true by construction.
3. **Bare permutations (exact).** In the flux-0 and flux-pi sectors, every
   rotation in each code's stabilizer maps the signed group to itself as a
   bare qubit permutation P_R, with no sign correction.
   - As a control, in each of the 6 mixed sectors, 44 codes have a
     stabilizing rotation whose bare permutation needs a correction.
   - The independent check gives the reason: P_R A^o_e P_R^-1 = A^{Ro}_{Re}
     exactly, and the two uniform signed groups do not depend on which
     ordering in the class is used.
4. **Pair test (exact).** Let R be a C2 in the code's stabilizer and x an
   off-axis vertex.
   - Solve over GF(2), in a window around x and Rx, for a Pauli S with
     three properties:
     - it flips exactly the vertex generators at x and Rx;
     - it creates no other excitation farther than distance 1 from x or Rx;
     - S and S^R = P_R S P_R^-1 have the same syndrome.
   - Then S^dagger S^R is plus or minus an element of the signed group,
     and lambda is that sign. It is the P_R-eigenvalue of the pair state
     S|vac> relative to the vacuum.
   - Results (L = 8 torus, both sectors, two x with |x - Rx| >= 3):
     lambda = +1 for all 108 (code, C2) pairs, i.e. every edge or axis C2
     in the stabilizer of every code.
   - A simpler version, with the hops of an ordering whose plaquette span
     P_R preserves, covers 72 of the pairs at L = 4 and agrees.
   - **Controls.** The toric-code boson gives +1. The toric-code boson in
     pi flux gives -1 under a C2 about a plaquette-centred axis (the
     Aharonov–Bohm phase) and +1 under the vertex C2. So the test can
     return -1.
5. **Spinorial action and the spin-1/2 class.**
   - **The relation.** For a pair swapped by C2,
     lambda = theta_f eta_f(C2, C2). The independent check calibrated it:
     the boson cases above, and a scalar fermion with c_v -> c_{Rv}, which
     gives -1.
   - **Every C2 is spinorial.** With theta_f = -1, eta_f(C2, C2) = -1 for
     every C2 of every code under P_R: C2^2 acts on the emergent fermion as
     (-1)^F.
   - **Majorana form.** The independent check also derived this, for 72
     pairs, from the Majorana form: P_R maps A_e to plus or minus
     A_{Re} B_tail B_head (times plaquettes), so c_v -> -i s_v c_{Rv}.
   - **Group cohomology (standard facts).** The class of a central Z2
     extension is determined by how the lifts of the C2 elements square:
     - H^2(D3; Z2) = Z2, detected by any C2;
     - H^2(Z2; Z2) = Z2;
     - for D2 = Z2 x Z2, H^2 = Z2^3, and the 8 classes correspond
       one-to-one to the 8 sign patterns of the squares of the three
       involutions' lifts.
   - **The spin-1/2 class.** In SU(2) every lift of a pi rotation squares
     to -1. So the restriction of w2 is:
     - the nontrivial class on D3 (the binary dihedral group of order 12);
     - the class with all three squares -1 on the order-4 groups, whose
       three C2 axes are mutually orthogonal (the quaternion group);
     - the nontrivial class on Z2.
   - **Conclusion.** For every one of the 60 codes, the fermion's
     fractionalization class for the code's whole rotation stabilizer,
     under P_R, equals the restriction of w2: the class of a spin-1/2
     particle.
6. **The class belongs to the realization.**
   - Let W = prod_v exp(-i pi B_v / 4). It is a function of the
     stabilizers, so it is constant on the code space. On a state with
     n fermions it contributes a relative phase e^{i pi n / 2}.
   - P_R W is therefore also a realization of R, and it flips lambda, so
     eta_f = +1. It is the scalar rotation c_v -> c_{Rv}.
   - Within one realization, dressing by stabilizer products cannot change
     the class: f x f = 1 fixes the gauge freedom to nu_f = +-1, and
     (F P_R)^2 is constant for a Pauli dressing F that respects the group
     law.

## How this bears on the lane (interpretation, not a claim)

- **Spin from moving sites.** If the framework's rotations act on the
  qubits by moving them, with no extra local unitary, then in these codes
  the emergent fermion is spinorial. A half-turn applied twice gives the
  fermion parity, as for a spin-1/2 particle. Here the lattice supplies the
  "electron spin" sign without any spin degree of freedom being put in.
  For every code in the family, the sign pattern is exactly the one a
  spin-1/2 particle shows under the code's rotation symmetry.
- **Two caveats.**
  - The dressed realization P_R W gives the scalar answer. Which one is
    physical depends on the dynamics.
    - The bare permutation is not a symmetry of Majorana hopping
      sum t_e A_e built from one ordering's edge operators; P_R W is.
    - With number-conserving hopping both are symmetries, and they differ
      by e^{i pi N / 2}.
    - So the spinorial answer is tied to the bare-permutation reading of
      the Lattice axiom, not forced by the code.
  - The hop system of a fixed ordering is less symmetric than the code.
    - For every ordering of a D3 code, P_R preserves span(S^o) only for the
      identity and one edge C2.
    - Even there, P_R maps a hop to a hop times the endpoint vertex terms.
    - A follow-up search (loop pack, c9) finds D3-invariant flux
      conventions of the form S^o_p times corner vertex terms.
    - For two of them, local clean hops exist (L = 6), giving a
      D3-symmetric clean hop system for a D3 code. This is an exploratory
      result, not part of the claim.
- **Pi-flux sector.** For complex (number-conserving) hopping with pi flux
  per plaquette, the low-energy theory is the Kogut–Susskind staggered
  fermion: two four-component Dirac tastes. The independent check confirms
  2 nodes, each with 4 linearly crossing bands. For the Majorana hopping
  sum A_e, the two nodes are particle-hole partners: one Dirac fermion.

## Independent check

A fresh-context agent (same model family) wrote its own code without
reading the runner. Its verdicts:
- **Items 1–4: confirmed**, at L = 4 and L = 6.
- **Earlier wording: refuted, and corrected here.** It refuted the earlier
  version of this note, which claimed eta_f(C2, C2) = +1 under P_R by
  restricting P_R to a region around the fixed vertex. That restriction
  breaks the generators straddling the region's boundary, so it is not a
  valid localization of the symmetry.
- **The current claim.** Its pair test (with calibrations), its Majorana
  derivation and the W-dressing result are the basis of items 4–6.
  - It covered 72 pairs and left 36 open.
  - This note's runner reproduces the 72 with independent code.
  - The runner closes the remaining 36 with the general method of item 4,
    which does not need a symmetric hop system.

Files: `.claude/science/physics-loops/toe-campaign-20261017/c8_rotation_action/independent_check/`.

## Premises

- **Axioms used.** Lattice (Z^3, proper cubic rotations about a vertex).
- **Supplied model.** The BKSF codes of the companion orbit note, with
  signed plaquette generators. The qubits sit on edges, not on sites.
- **Declared choices.**
  - Translation-invariant signs.
  - The bare-permutation realization of the rotations.
  - The relation lambda = theta_f eta_f, calibrated as above.

## Relation to prior work

- BKSF: Bravyi and Kitaev, Ann. Phys. 298, 210 (2002). Statistics: Levin and
  Wen, PRB 67, 245316 (2003).
- Symmetry fractionalization and its gauge freedom: Barkeshli, Bonderson,
  Cheng and Wang, PRB 100, 115147 (2019). This is a 2+1D framework, used here
  for point particles.
- Staggered fermions: Kogut and Susskind, PRD 11, 395 (1975); Susskind,
  PRD 16, 3031 (1977); Golterman and Smit, Nucl. Phys. B245, 61 (1984);
  Golterman, lecture notes arXiv:2406.02906. Symmetries of Hamiltonian
  staggered fermions, including a twisted rotation group: Catterall,
  Pradhan and Samlodia, PRD 113, 014504 (2026), arXiv:2501.10862.
- Emergent fermions from string nets: Wen, PRD 68, 065003 (2003).
- **New here.**
  - The sign-sector and pair-test analysis of the bare-permutation rotation
    action in the cubic BKSF family.
  - The finding that this action is spinorial, with the spin-1/2 class on
    every code's rotation stabilizer, while a stabilizer-function dressing
    makes it scalar.

## No-Go Discipline Gate

- **N1 — routes around the claim.** Not covered:
  - realizations other than P_R and P_R W;
  - sign patterns that are not translation-invariant;
  - the mixed sectors;
  - other encodings;
  - stacks.
- **N2/N3 — scope.** One family, two sectors. The fractionalization class
  for each code's rotation stabilizer, computed from all its C2 elements.
- **N4 — inputs.** Exact Pauli algebra with phases.
  - The covered-pair test runs on the L = 4 torus, with paths inside a box
    of side 2.
  - The general pair test runs on the L = 8 torus, with windows of side at
    most 7 and x, Rx separated by at least 3.
  - In both, S^dagger S^R is local and contractible.
  - The group-cohomology facts used in item 5 are standard. The relation lambda = theta_f eta_f is an
  input, calibrated by the independent check.
- **N5 — wording.** "Spinorial" means eta_f(C2, C2) = -1 for the stated
  realization. It does not mean an emergent SU(2) spin.
- **N6/N7 — strongest objection.** The class depends on the realization.
  This is stated in item 6, and the interpretation does not treat the
  spinorial answer as forced.
- **N8 — earlier claims.** This replaces this note's own first version,
  which had the opposite sign. It is consistent with the orbit note.

## Verification

```bash
python3 scripts/bksf_cubic_fermion_codes_rotations_act_by_bare_permutation_2026_10_17.py
```

Expected: `TOTAL: PASS=9 FAIL=0` (about 3.5 minutes).

## Load-bearing sources

- [BKSF orbit note](BKSF_CUBIC_FERMION_CODES_ARE_NOT_ROTATION_INVARIANT_MINIMAL_ORBIT_FOUR_BOUNDED_THEOREM_NOTE_2026-10-17.md)
- [Axioms](MINIMAL_AXIOMS_2026-06-29.md)
