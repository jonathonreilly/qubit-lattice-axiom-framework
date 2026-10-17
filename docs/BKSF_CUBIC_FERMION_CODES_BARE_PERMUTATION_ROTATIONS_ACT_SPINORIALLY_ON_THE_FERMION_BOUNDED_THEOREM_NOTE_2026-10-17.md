---
claim_id: bksf_cubic_fermion_codes_bare_permutation_rotations_act_spinorially_on_the_fermion_bounded_theorem_note_2026-10-17
claim_type: bounded_theorem
claim_scope: "Supplied model: the 60 translation-invariant BKSF stabilizer codes on the cubic lattice (one qubit per edge of Z^3, one ordering of the six edge directions at every vertex) of the companion orbit note, with signed plaquette generators, one sign per plaquette orientation (8 translation-invariant sign sectors). Exact (Pauli algebra with phases, L = 4 torus): all 8 sectors of all 60 codes are valid; in two sectors the hop product of a fixed ordering's edge operators around every plaquette is plus, respectively minus, the signed generator (flux 0 and flux pi; this labels the sectors); every rotation in each code's stabilizer maps the signed group of those two sectors to itself as a bare qubit permutation P_R, while in each of the 6 mixed sectors 44 codes have a stabilizing rotation that needs a sign correction. Pair test, exact (L = 8 torus): for every one of the 108 (code, C2) pairs, in both sectors, a state with fermions at x and Rx (solved so that its excitations are R-symmetric and confined near x and Rx) has P_R-eigenvalue +1 relative to the vacuum (controls: +1 for the toric-code boson; -1 for the toric-code boson in pi flux under a plaquette-centred C2). Conditional on the stated lambda=theta_f eta_f localization relation, exchange sign -1 gives eta_f(C2, C2) = -1 for every C2 of every code under P_R. For 72 pairs the creators are clean hop strings; for the other 36 they need local flux dressing, and lambda = +1 holds on the entire space of admissible dressed creators (exact quadratic-form argument, independent check). Conditional on that localization relation, group cohomology gives, for the D3 and single-C2 codes, that the fermion's class for the whole rotation stabilizer under P_R equals the restriction of the spin-1/2 class w2 of SO(3); for the order-4 codes the data (-1 for all three C2) match w2 on D2 in sign pattern, but a nondegenerate fermion cannot carry an odd-minus pattern on D2 in a one-dimensional local action, so these codes signal either a localization obstruction of the bare D2 action or a failure of lambda = theta*eta there (open). Twisting by W = prod_v exp(-i pi B_v / 4) (a function of the stabilizers, constant on the code space) on the elements where a Z2 character is -1 gives a valid realization that flips those C2: the trivial class for D3 and single-C2 codes, but not for the order-4 codes, whose reachable twisted patterns flip exactly two of the three C2. So the class belongs to the realization, not to the code alone. Not claimed: C3-only statements (no Z2 class), sign patterns that are not translation-invariant, the mixed sectors, other encodings, dynamics, the continuum limit, or any physical identification (electron, spin)."
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
   - **Robustness.**
     - For those 72 pairs, the pair creators are clean: hop strings that
       create nothing but the two charges.
     - For the other 36, no ordering's plaquettes are permuted by P_R. A
       clean creator then has a non-clean image, so S must be allowed local
       flux excitations near the endpoints.
     - The independent check showed that λ does not depend on that
       dressing. Over the whole space of admissible dressed creators
       (dimension 327 to 1140), λ is a GF(2) quadratic function whose
       values on a basis are +1 and whose off-diagonal pairing vanishes.
       So λ = +1 on the entire space, for all 108 pairs: at L = 10, and for
       the 36 uncovered pairs again at L = 12.
     - The reason is that in BKSF the product of all B_v is the identity,
       so no local operator flips an odd number of charges. A dressing
       cannot change what the endpoints are.
   - **Controls.** The toric-code boson gives +1. The toric-code boson in
     pi flux gives -1 under a C2 about a plaquette-centred axis (the
     Aharonov–Bohm phase) and +1 under the vertex C2. So the test can
     return -1.
5. **Spinorial action and the spin-1/2 class.**
   - **The relation.** For a pair swapped by C2,
     lambda = theta_f eta_f(C2, C2).
     - Derivation: if the rotation sends c_x^dagger to a c_{Rx}^dagger and
       c_{Rx}^dagger to b c_x^dagger, then the pair c_x^dagger
       c_{Rx}^dagger goes to ab c_{Rx}^dagger c_x^dagger
       = theta_f ab c_x^dagger c_{Rx}^dagger. So lambda = theta_f ab,
       and eta_f(C2, C2) = ab.
     - The independent check also calibrated it numerically: the boson
       cases above, and a scalar fermion with c_v -> c_{Rv}, which gives
       -1.
   - **Pair-derived involution signs.** Assuming lambda = theta_f eta_f
     applies, each tested C2 gives eta_f = -1. This does not establish a
     consistent D2 localization.
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
   - **Conclusion.**
     - For the 12 D3 codes and the 36 single-C2 codes, under P_R the
       fermion's fractionalization class for the code's whole rotation
       stabilizer equals the restriction of w2, the class of a spin-1/2
       particle.
     - For the 12 order-4 codes the pair-test data are -1 for all three C2,
       the sign pattern of w2 on D2 (the quaternion class). But assembling
       these into a class is in tension with the fermion being
       nondegenerate, and is left open.
       - Here a fixed syndrome determines the excitation, so a single
         fermion has one local state.
       - A one-dimensional local action with fermion parity acting as -1
         exists only for the abelian extensions of D2. Those are the sign
         patterns with an even number of -1.
       - The patterns (-,-,-) (quaternion) and the one-minus patterns
         (dihedral) need a degenerate, Kramers-like fermion.
       - So either the bare D2 action of these codes cannot be
         consistently localized on the fermion (an anomaly-type
         obstruction), or λ = θ_f η_f fails for some of these C2.
       - The W-twists of item 6 flip two of the three signs at a time.
         They preserve the odd count, so they do not remove the tension.
       - Exploratory evidence (loop pack, c14):
         - For these codes, P_R turns a bare hop into a hop times a
           flux-creating factor, so no scalar fermion map exists in an
           ordering's convention.
         - None of 12 x 4096 corner-dressed flux conventions is
           D2-invariant, whereas D3 codes have such conventions.
         - This is consistent with a localization obstruction but does not
           prove one.
       - The group-theory steps were checked independently by explicit
         SU(2) computation (22/22; loop pack, c8 independent_check/
         grouptheory).
     - This does not affect D3 or Z2: there every class is compatible with
       a nondegenerate fermion, since H^2(D3; U(1)) = 0.
6. **The class belongs to the realization.**
   - Let W = prod_v exp(-i pi B_v / 4). It is a function of the
     stabilizers, so it is constant on the code space. On a state with
     n fermions it contributes a relative phase e^{i pi n / 2}.
   - Dressing one involution R by W flips its λ.
   - **The group law limits which elements can be dressed** (found by the
     independent check). Write V_g = P_g W^{n(g)}. Since W commutes with
     P_g and leaves a two-fermion state with phase -1, the V_g form an
     action up to fermion parity exactly when n is a homomorphism from the
     stabilizer to Z2.
     - **D3 and single-C2 codes:** n is the sign character (dress the C2,
       not the C3). This flips every C2 and gives the trivial class.
     - **Order-4 codes (D2):** each nontrivial character flips exactly two
       of the three C2. The reachable patterns are (+,+,-), (+,-,+) and
       (-,+,+). The trivial class is not reachable by such a twist.
   - Within one realization, dressing by stabilizer products cannot change
     the class: f x f = 1 fixes the gauge freedom to nu_f = +-1, and
     (F P_R)^2 is constant for a Pauli dressing F that respects the group
     law.

## How this bears on the lane (interpretation, not a claim)

- **Finite pair data and conditional class inference.** The finite pair
  data, conditional on the stated localization relation, give the restricted
  w2 inference for D3 and single-C2 stabilizers. This does not establish an
  electron identification or consistent D2 localization.
- **The four-species stack, with spin.** The orbit note's covariant stack
  of four D3 codes carries one species per body diagonal.
  - Conditional on the same localization premise, under the bare action
    each species has the spinorial D3 character:
    the C2 lift goes to +-i and the C3 lift to -1.
  - Suppose couplings made the four species degenerate partners of one
    multiplet. By Frobenius reciprocity, the binary octahedral group 2O
    would act on the multiplet by the induced representation, which is the
    four-dimensional spinor irrep G_{3/2}. The species form a spin-3/2-like
    quartet, not 1 + 3.
  - This is representation theory under a hypothetical coupling. It is
    not computed.
- **Two caveats.**
  - The twisted realizations of item 6 change the answer. Which one is
    physical depends on the dynamics.
    - The bare permutation is not a symmetry of Majorana hopping
      sum t_e A_e built from one ordering's edge operators; P_R W is, for
      each R separately.
    - With number-conserving hopping both are symmetries, and they differ
      by e^{i pi N / 2}.
    - Exactly: in BKSF, B_v is the encoded fermion parity at v, so the
      occupation is n_v = (1 - B_v)/2. Then
      W = prod_v exp(-i pi B_v / 4) = e^{-i pi L^3 / 4} e^{i pi N / 2}.
      The twist of item 6 is a quarter-turn of the fermion-number U(1),
      applied to the odd elements.
    - So with charge conservation, "spin-1/2 under rotations" and "charge
      rotation by pi/2" are interchangeable. This is the lattice form of a
      spin-charge relation. A prediction needs the framework to fix both
      the rotation action and the charge.
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
- **Second round: confirmed.** The agent wrote its own general pair test
  using R-invariant path windows, with random nullspace sampling.
  - It confirmed lambda = +1 for all 108 pairs in both sectors, including
    separations 1 and 2 and axis C2's at L = 10.
  - It confirmed the toric controls.
  - It confirmed the cohomology step by exact GF(2) computation:
    - H^2(D2; Z2) = Z2^3, with classes in bijection with the sign patterns
      of the squares;
    - H^2(D3; Z2) = Z2.
  - It also argued why the "same syndrome" condition fixes lambda: two
    valid solutions differ only by separated local clusters and
    stabilizers.
- **Third round (run from the C12 check): two results.**
  - **Dressing independence.** It proved λ = +1 on the entire space of
    admissible dressed creators for all 108 pairs (item 4).
  - **A correction to item 6.** Dressing every element by W violates the
    group law; only twists along a Z2 character are consistent.

Files: `.claude/science/physics-loops/toe-campaign-20261017/c8_rotation_action/independent_check/` and
`.claude/science/physics-loops/toe-campaign-20261017/c12_majorana_per_direction/independent_check/` (`REPORT2.txt`, `pairspace.py`).

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
  - Conditional on the stated localization relation, the spin-1/2 class
    on D3 and single-C2 stabilizers and its trivialization by a consistent
    W-character twist. D2 localization remains open; those twists cannot
    trivialize its odd-minus sign pattern.

## No-Go Discipline Gate

- **N1 — routes around the claim.** Not covered:
  - realizations other than P_R and its character twists by W;
  - sign patterns that are not translation-invariant;
  - the mixed sectors;
  - other encodings;
  - stacks.
- **N2/N3 — scope.** One family, two sectors. The fractionalization class
  for D3 and single-C2 stabilizers is conditional on the stated localization
  relation; D2 has pair-derived signs with localization still open.
- **N4 — inputs.** Exact Pauli algebra with phases.
  - The covered-pair test runs on the L = 4 torus, with paths inside a box
    of side 2.
  - The general pair test runs on the L = 8 torus, with unwrapped windows
    of side at most 7 and x, Rx separated by at least 3.
    - For an axis C2 the separation is even, so this means 4, half the
      torus.
    - The independent check repeated the axis-C2 cases at L = 10.
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
