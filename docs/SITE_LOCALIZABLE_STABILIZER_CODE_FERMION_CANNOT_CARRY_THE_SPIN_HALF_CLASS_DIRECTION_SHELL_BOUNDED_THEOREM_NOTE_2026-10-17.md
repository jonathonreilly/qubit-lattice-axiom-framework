---
claim_id: site_localizable_stabilizer_code_fermion_cannot_carry_the_spin_half_class_direction_shell_bounded_theorem_note_2026-10-17
claim_type: bounded_theorem
claim_scope: "Supplied setting: a commuting Pauli Hamiltonian on qubits at the sites of Z^3 whose terms generate the full stabilizer group with no nontrivial local logical operators, a site v, and a group H of proper cube rotations about v realized linearly (or as a stated extension) by unitaries that map the set of Hamiltonian terms onto itself and preserve the vacuum sector; an anyon a with a x a = 1. Statement (conditional on the standard symmetry-localization ansatz used in the companion notes): if a is carried by an H-invariant violated-term pattern supported near v (the load-bearing hypothesis, to be verified per realization), the local action of H on a at v is one-dimensional, so the fractionalization class eta_a restricted to H lies in the kernel of H^2(H; Z2) -> H^2(H; U(1)). Exact finite group theory (runner): for H = O this kernel is {0, w1^2}, so the restriction of the spin-1/2 class w2 is excluded; w2 needs a local dimension of at least two exactly for H in {D2 (both classes), D4, T, O}, while cyclic groups and D3 admit a one-dimensional spin-1/2 local state; on the axis D2 the one-dimensional classes are the involution-square patterns with an even number of -1. An O-orbit of positions has odd size only for stabilizers O and D4. Shells: the induced representations of the binary octahedral group 2O on the orbit of the six directions are A1 + E + T1 (k = 0), T1 + T2 (k = 2, 6), A2 + E + T2 (k = 4) for the linear characters and E1/2 + G3/2 (k = 1, 7) or E5/2 + G3/2 (k = 3, 5) for the spinorial ones (k labels the character on the Z8 generator with trace +sqrt 2); the eight octants give A1 + A2 + T1 + T2 (linear k = 0) and E1/2 + E5/2 + G3/2 or 2 G3/2 (spinorial); the twelve face diagonals give spinorial shells containing E1/2. Application (exact algebra, checked independently): in the half-edge realization the on-site Clifford maps V_R P_R send every generator near v to plus a generator of the same type, so the single-site charge term B_v gives an invariant pattern and the fermion's class lies in the kernel, never w2 on O (likewise for the Majorana-per-direction realization). For the bare permutation, B_v is fixed but the term set is not: the clean single-fermion pattern acquires plaquette violations near v (all 12 axis C2 of the order-4 codes), so the hypothesis fails and the theorem does not apply there; this is a concrete candidate for the failing assumption behind the order-4 tension. Not claimed: a proof that the order-4 tension is resolved this way, a model realizing w2, dynamics, energetics of the shells, or any physical identification."
upstream_dependencies:
  - bksf_cubic_fermion_codes_bare_permutation_rotations_act_spinorially_on_the_fermion_bounded_theorem_note_2026-10-17
  - bksf_cubic_fermion_codes_site_local_realization_with_six_direction_qubits_per_site_bounded_theorem_note_2026-10-17
  - majorana_per_direction_cubic_fermion_code_has_one_species_covariant_under_all_cubic_rotations_bounded_theorem_note_2026-10-17
  - spinful_majorana_per_direction_cubic_code_emergent_fermion_doublet_carries_spin_half_class_on_all_cubic_rotations_bounded_theorem_note_2026-10-17
runner: scripts/site_localizable_fermion_cannot_carry_spin_half_class_direction_shell_2026_10_17.py
---

# A site-localizable stabilizer-code fermion cannot carry the spin-1/2 class; the six-direction shell

**Date:** 2026-10-17
**Type:** bounded_theorem
**Status:** bounded support, unaudited. The group theory is exact; the
physical statement is conditional on symmetry localization. Nothing is
adopted.

## Question

Under cube-invariant realizations, the campaign's emergent fermions came out
spinless (the Majorana-per-direction code, and the on-site Clifford action of
the half-edge code). The spinful code's doublet had a spin-1/2 sign, but only
because its matter already transformed under the binary octahedral group
2O.

The sharpened target is a code with a genuine action of the cube rotation
group O whose fermion carries the spin-1/2 class w2. Is there a general
reason the codes built so far could not reach it? If so, what must change?

## Result

1. **The obstruction (conditional on symmetry localization).**
   - **Setting.** A commuting Pauli Hamiltonian whose terms generate the
     full stabilizer group, with no nontrivial local logical operators. A
     group H of rotations about a site v, realized linearly (or as a
     stated extension, such as the fermion-parity extension of the
     Majorana-per-direction note) by unitaries that map the set of
     Hamiltonian terms onto itself and preserve the vacuum sector. An
     anyon a with a x a = 1.
   - **Hypothesis (load-bearing, to verify per realization).** a is carried
     by a pattern of violated terms near v that H maps to itself.
   - **Step one.** In a stabilizer code the violated-term pattern fixes the
     local state. So the states with a at v form a one-dimensional local
     space, and H acts on it.
   - **Step two.** By symmetry localization, the localized operators of H
     act on that space as phases u(h). They satisfy
     u(g) u(h) = eta_a(g, h) u(gh).
   - **Conclusion.** So eta_a, a Z2-valued cocycle (because a x a = 1 fixes
     the gauge freedom to signs), is a U(1) coboundary. Its class lies in
     the kernel of H^2(H; Z2) -> H^2(H; U(1)).
2. **The kernels (exact, runner).**
   - **O.** We built the four classes of H^2(O; Z2) as explicit cocycles
     and formed each central extension.
     - −1 is not a commutator for the classes 0 and w1^2. Here w1 is the
       sign of the permutation of the six directions.
     - −1 is a commutator for w2 and w2 + w1^2.
     - So the kernel is {0, w1^2}, and w2 is excluded.
   - **Every subgroup** (11 conjugacy classes). The restriction of w2 needs
     a local dimension of at least two exactly for:
     - D2, both conjugacy classes;
     - D4, T and O.

     The cyclic groups and D3 admit a one-dimensional spin-1/2 local state.
   - **Axis D2.** All eight involution-square patterns occur. The
     one-dimensional ones have an even number of −1, so (−,−,−) is
     excluded.
3. **Odd orbits (exact).** An O-orbit has odd size only when its
   stabilizer is O (size 1, the site) or D4 (size 3, such as the three
   coordinate axes).
   - Suppose the a-charge of a pattern is the parity of its violated charge
     terms, as for the Z2 charge here.
   - Then an O-invariant pattern with odd charge needs a charge term whose
     support has stabilizer O or D4.
4. **Shells (exact, runner).** Let a sit at one point of an O-orbit, with a
   one-dimensional local state on which its stabilizer acts by a
   character. Then the orbit carries the induced representation of 2O.
   The runner decomposes these into 2O irreps.

   | orbit (stabilizer lift) | linear characters | spinorial characters |
   |---|---|---|
   | six directions (Z8) | A1 + E + T1 (k = 0); T1 + T2; A2 + E + T2 | E1/2 + G3/2 (k = 1, 7); E5/2 + G3/2 (k = 3, 5) |
   | eight octants (Z6) | A1 + A2 + T1 + T2 (k = 0); T1 + T2 + E | E1/2 + E5/2 + G3/2; 2 G3/2 |
   | twelve face diagonals (Z4) | A1 + E + T1 + 2 T2; A2 + E + 2 T1 + T2 | E1/2 + E5/2 + 2 G3/2 |

   - **Convention.** On the six directions, k labels the character's value
     on the Z8 generator with trace +sqrt 2. Using its negative swaps
     k = 1 with 5 and 3 with 7.
   - On the six directions, every spinorial shell is a doublet plus a
     quartet: 6 = 2 + 4.
5. **Application to the campaign's codes (exact algebra, checked
   independently).**
   - In the BKSF edge codes, their half-edge realization and the
     Majorana-per-direction code, the fermion has a single-site charge
     term: B_v, the product of Z over v's qubits (equivalently, of all of
     v's local Majoranas).
   - **On-site Clifford realizations: the hypothesis holds.**
     - The maps of the half-edge note are V_R P_R, with V_R a network of CZ
       gates, diagonal in Z.
     - They send every generator near v to plus a generator of the same
       type. The independent check found 0 failures in 13,608 checks, and
       V_R P_R A_e = +A_{Re} analytically.
     - So the single-site pattern "B_v violated" is invariant, item 1
       applies, and the class lies in the kernel: never w2 on O. The same
       holds for the Majorana-per-direction realization.
     - Their pair tests gave −1 for all nine C2. Under lambda = theta eta,
       that is the class-0 pattern. The w1^2 pattern of that note's
       W-twist is also in the kernel.
   - **Bare permutation: the hypothesis fails.**
     - The bare permutation fixes B_v but maps the term set of an ordering
       to a different term set.
     - At L = 8 the clean single-fermion pattern acquires plaquette
       violations within distance 2 of v under:
       - all 12 axis C2 of the order-4 codes;
       - 19 of 24 of their edge C2;
       - all D3 C3;
       - 24 of 36 D3 edge C2.
     - So item 1 does not apply to the bare action. This is consistent with
       the spin-1/2 restrictions found there for D3 and single-C2 codes.
     - It is a concrete candidate for the failing assumption behind the
       order-4 tension (axis D2, pattern (−,−,−)): no invariant
       single-fermion pattern exists there. It does not prove that this
       resolves the tension.
6. **The spinful code escapes by a different route.** Its rotations mix the
   two matter-parity terms P_up and P_dn, so the action does not map the
   set of terms onto itself. Its doublet is two degenerate violated-term
   patterns mixed by the symmetry. That escape is legitimate, but there the
   matter carried 2O already.

## How this bears on the lane (interpretation, not a claim)

- **A design rule for the sharpened target.** A stabilizer code with a
  genuine O action that maps terms to terms, whose fermion carries w2,
  must have no realizable O-invariant violated-term pattern of odd charge
  about any site. In particular it cannot have a site-centred charge term
  like B_v. By item 3, such a pattern needs a charge term whose support has
  stabilizer O or D4. So avoiding those supports suffices, but it is not
  required.

  Otherwise the action must mix degenerate terms, as in the spinful code.
- **One qubit per connecting direction.** The six directions are the
  smallest even orbit of single positions at a site. Orbits of extended
  supports can be smaller: a tetrahedron of octants has orbit 2. A charge carried by the six direction
  qubits, with no site term, is the minimal shell allowed by the rule.
  - If its class is w2, the six states form a doublet plus a quartet,
    2 + 4. The doublet is E1/2 or E5/2.
  - If its class is trivial and the stabilizer character is trivial
    (k = 0), they form A1 + E + T1.
  - This is the familiar p-shell count: three orbitals times two spin
    states splits as j = 1/2 plus j = 3/2. Here it arises from six
    positions, with no spin degree of freedom put in.
- **Not shown.** A code with a direction-carried charge and class w2. Nor
  that the doublet is the lowest state, which depends on the sign of
  hopping around the shell.

## Independent check

A fresh-context agent (same model family) wrote its own code before
comparing with the runner.
- **Items 2–4: confirmed exactly.**
  - H^2(O;Z2) = Z2^2, with kernel {0, w1^2}.
  - All 11 subgroup classes match.
  - All eight explicit irreps match, and so does every shell entry. It
    asked for the k convention to be stated.
- **Item 1: confirmed, with three hypotheses to make explicit.** No local
  logical operators, a linear (or stated extension) action, and the
  invariant pattern as the condition to verify.
- **Item 5: corrected.** It confirmed the on-site Clifford realizations.
  It refuted the earlier claim that the bare permutation satisfies the
  hypothesis, which gave the order-4 candidate above.

Files: `.claude/science/physics-loops/toe-campaign-20261017/c16_site_localizable_obstruction/independent_check/`.

## Premises

- **Axioms used.** Lattice (Z^3, proper cubic rotations about sites).
- **Supplied.** The commuting Pauli Hamiltonians of the companion notes;
  the standard symmetry-localization ansatz for point-group fractionalization
  (the same one under which those notes read lambda = theta eta).
- **Standard facts used.** H^2(H; Z2) classifies central Z2 extensions. A
  one-dimensional projective representation exists exactly when the class
  is a U(1) coboundary.

## Relation to prior work

- **Projective representations at fixed points force degeneracy.** The
  general fact that an anyon at a symmetry-fixed point carries a
  projective representation of the stabilizer is standard. So is the
  conclusion that a U(1)-nontrivial class forces degeneracy, as with
  Kramers doublets. See symmetry-enriched topological order (Barkeshli,
  Bonderson, Cheng and Wang, PRB 100, 115147 (2019)) and point-group
  fractionalization (Qi and Fu; Thorngren and Else, PRX 8, 011040 (2018)).
- **Textbook facts.** Double-group character tables and induced
  representations of 2O (Bethe; Koster et al.) are textbook.
- **New here.**
  - The stabilizer-code corollary for the campaign's codes.
  - The subgroup table of when w2 forces degeneracy.
  - The odd-orbit design rule.
  - The identification of the six-direction shell as the minimal allowed
    one, with its 2 + 4 decomposition.

## No-Go Discipline Gate

- **N1 — routes around the claim.**
  - Actions that do not map terms to terms (the spinful code).
  - Non-stabilizer Hamiltonians with symmetric degeneracies.
  - Charge terms with no O- or D4-invariant support.

  None is excluded.
- **N2/N3 — scope.** Commuting Pauli Hamiltonians, rotations about a site.
- **N4 — inputs.** The group theory is exact finite computation: cocycles,
  commutator subgroups and characters, over 48 elements. The physical
  statement assumes symmetry localization.
- **N5 — wording.** "Spin-1/2 class" means w2 restricted to the rotation
  group. Nothing about physical spin is claimed.
- **N6/N7 — strongest objection.** Symmetry localization for point-group
  actions on lattice codes is an ansatz. The order-4 BKSF codes show that,
  for some realization, either it or lambda = theta eta fails.
- **N8 — earlier claims.**
  - Generalizes the single-state remark of the spinful-code note.
  - Explains the spinless results of the cube-invariant realizations.
  - Reformulates, without resolving, the order-4 tension.

## Verification

```bash
python3 scripts/site_localizable_fermion_cannot_carry_spin_half_class_direction_shell_2026_10_17.py
```

Expected: `TOTAL: PASS=11 FAIL=0` (a few seconds).

## Load-bearing sources

- [Bare-permutation note](BKSF_CUBIC_FERMION_CODES_BARE_PERMUTATION_ROTATIONS_ACT_SPINORIALLY_ON_THE_FERMION_BOUNDED_THEOREM_NOTE_2026-10-17.md)
- [Half-edge note](BKSF_CUBIC_FERMION_CODES_SITE_LOCAL_REALIZATION_WITH_SIX_DIRECTION_QUBITS_PER_SITE_BOUNDED_THEOREM_NOTE_2026-10-17.md)
- [Majorana-per-direction note](MAJORANA_PER_DIRECTION_CUBIC_FERMION_CODE_HAS_ONE_SPECIES_COVARIANT_UNDER_ALL_CUBIC_ROTATIONS_BOUNDED_THEOREM_NOTE_2026-10-17.md)
- [Spinful-code note](SPINFUL_MAJORANA_PER_DIRECTION_CUBIC_CODE_EMERGENT_FERMION_DOUBLET_CARRIES_SPIN_HALF_CLASS_ON_ALL_CUBIC_ROTATIONS_BOUNDED_THEOREM_NOTE_2026-10-17.md)
- [Axioms](MINIMAL_AXIOMS_2026-06-29.md)
