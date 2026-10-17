---
claim_id: site_localizable_stabilizer_code_fermion_cannot_carry_the_spin_half_class_direction_shell_bounded_theorem_note_2026-10-17
claim_type: bounded_theorem
claim_scope: "Supplied setting: a commuting Pauli Hamiltonian on qubits at the sites of Z^3 whose terms generate the full stabilizer group with no nontrivial local logical operators, a site v, and a group H of proper cube rotations about v realized linearly (or as a stated extension) by unitaries that map the set of Hamiltonian terms onto itself and preserve the vacuum sector; an anyon a with a x a = 1. Statement (conditional on the standard symmetry-localization ansatz used in the companion notes): if a is carried by an H-invariant violated-term pattern supported near v (the load-bearing hypothesis, to be verified per realization), and a one-dimensional localized sector with a fusion-compatible Z2 factor system is supplied, then the fractionalization class eta_a restricted to H lies in the kernel of H^2(H; Z2) -> H^2(H; U(1)). Finite group conclusions (exact independent algebra for the kernel/subgroup results; primary reconstruction and character tables use floating-point arithmetic): for H = O this kernel is {0, w1^2}, so the restriction of the spin-1/2 class w2 is excluded; w2 needs a local dimension of at least two exactly for H in {D2 (both classes), D4, T, O}, while cyclic groups and D3 admit a one-dimensional spin-1/2 local state; on the axis D2 the one-dimensional classes are the involution-square patterns with an even number of -1. An O-orbit of positions has odd size only for stabilizers O and D4. Shells: the induced representations of the binary octahedral group 2O on the orbit of the six directions are A1 + E + T1 (k = 0), T1 + T2 (k = 2, 6), A2 + E + T2 (k = 4) for the linear characters and E1/2 + G3/2 (k = 1, 7) or E5/2 + G3/2 (k = 3, 5) for the spinorial ones (k labels the character on the Z8 generator with trace +sqrt 2); the eight octants give A1 + A2 + T1 + T2 (linear k = 0) and E1/2 + E5/2 + G3/2 or 2 G3/2 (spinorial); the twelve face diagonals give spinorial shells containing E1/2. Application (exact algebra, checked independently): in the half-edge realization the on-site Clifford maps V_R P_R send every generator near v to plus a generator of the same type, so B_v gives an invariant pattern; the kernel implication additionally requires construction of the stated one-dimensional localized sector with fusion-compatible Z2 action (also required in the Majorana-per-direction application). For the bare permutation, B_v is fixed but the term set is not: the clean single-fermion pattern acquires plaquette violations near v (all 12 axis C2 of the order-4 codes), so the hypothesis fails and the theorem does not apply there; this is a concrete candidate for the failing assumption behind the order-4 tension. Not claimed: a proof that the order-4 tension is resolved this way, a model realizing w2, dynamics, energetics of the shells, or any physical identification."
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
**Status:** bounded support, unaudited. The group-theoretic kernel and subgroup conclusions have exact independent algebraic checks; the primary reconstructs group matrices and characters numerically. The physical implication assumes a one-dimensional localized sector and fusion-compatible symmetry localization. Nothing is adopted.

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
   - **Local-sector hypothesis.** Assume the chosen invariant syndrome has a one-dimensional localized sector on which H acts. A fixed syndrome alone need not fix global logical data or establish symmetry localization. The absence of local logical operators is not substituted for an explicit localized-sector construction.
   - **Step two.** By symmetry localization, the localized operators of H
     act on that space as phases u(h). They satisfy
     u(g) u(h) = eta_a(g, h) u(gh).
   - **Conclusion.** Assume a fusion-compatible localization convention with Z2-valued eta_a; a x a = 1 alone does not specify every allowed rephasing. The displayed equation makes eta_a a U(1) coboundary. Its class lies in
     the kernel of H^2(H; Z2) -> H^2(H; U(1)).
2. **The kernels (finite group conclusions).**
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
4. **Shells (character formulas, numerically reconstructed by the primary).** Let a sit at one point of an O-orbit, with a
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
   - **On-site Clifford realizations: the invariant-pattern condition holds.**
     - The maps of the half-edge note are V_R P_R, with V_R a network of CZ
       gates, diagonal in Z.
     - They send every generator near v to plus a generator of the same
       type. The independent check found 0 failures in 13,608 checks, and
       V_R P_R A_e = +A_{Re} analytically.
     - So the single-site pattern "B_v violated" is invariant. If a one-dimensional localized charge sector and fusion-compatible Z2 localization are also constructed, item 1 gives the kernel conclusion. Invariance of the syndrome alone does not establish those hypotheses. The same qualification applies to the Majorana-per-direction realization, including its extension and local-dressing caveats.
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
       order-4 tension (axis D2, pattern (−,−,−)): the tested clean single-B patterns and orderings are not invariant. This does not exclude every dressed invariant pattern or prove that the tension is resolved.
6. **The spinful code escapes by a different route.** Its rotations mix the
   two matter-parity terms P_up and P_dn, so the action does not map the
   set of terms onto itself. Its doublet is two degenerate violated-term
   patterns mixed by the symmetry. That escape is legitimate, but there the
   matter carried 2O already.

## How this bears on the lane (interpretation, not a claim)

- **Conditional design constraint.** An invariant one-dimensional localized charge sector with fusion-compatible Z2 symmetry localization cannot carry the U(1)-nontrivial restriction of w2 on O. A site-centered charge term or invariant syndrome by itself is not excluded. A construction may avoid the invariant localized sector, use a degenerate sector, or fail another localization hypothesis; mixing degenerate terms is one possible route, not an exhaustive dichotomy. Odd support-orbit counting remains a separate combinatorial statement.

- **Retired six-direction code route.** Exact prior lane evidence is in `archive/six_direction_qubit_lane_2026_10_17/MANIFEST.json`. The induced six-direction representation and its 2+4 spinorial decomposition remain useful group theory. They do not construct a fermion code or establish a minimal allowed physical shell. A C4-fixed point alone is not an obstruction: the binary lift has eighth-root characters. A restriction to fourth-root phases must be proved for the specified realization, not assumed for all Clifford or PSG actions. The corner model is a separate supplied construction.

## Historical author check

The following records the submitted check history, not a new certification of exact arithmetic in the primary.

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
  - The six-direction induced-character calculation and its 2 + 4 decomposition; the minimal-code interpretation is retired.

## No-Go Discipline Gate

- **N1 — routes around the claim.**
  - Actions that do not map terms to terms (the spinful code).
  - Non-stabilizer Hamiltonians with symmetric degeneracies.
  - Charge terms with no O- or D4-invariant support.

  None is excluded.
- **N2/N3 — scope.** Commuting Pauli Hamiltonians, rotations about a site.
- **N4 — inputs.** The primary reconstructs the 48-element group with floating-point matrices and tolerance/rounding operations; it is not an exact arithmetic certificate. Independent rational/quadratic-field calculations corroborate the kernel and subgroup conclusions. The physical implication additionally assumes the stated localized sector and fusion-compatible symmetry localization.
- **N5 — wording.** "Spin-1/2 class" means w2 restricted to the rotation
  group. Nothing about physical spin is claimed.
- **N6/N7 — strongest objection.** Symmetry localization for point-group
  actions on lattice codes is an ansatz. The order-4 BKSF codes show that,
  for some realization, either it or lambda = theta eta fails.
- **N8 — earlier claims.**
  - Generalizes the single-state remark of the spinful-code note.
  - Explains the spinless results of the cube-invariant realizations.
  - Reformulates, without resolving, the order-4 tension.

## Landing evidence boundary

Independent exact controls reconstruct H^2(O,Z2) using normalized GF(2) cocycles and construct binary extensions over Q(sqrt(2)); they corroborate the kernel, 30 subgroups/11 conjugacy classes and odd-orbit counts. Character-table reconstruction in the primary remains numerical. The conditional theorem is the elementary implication u(g)u(h)=eta(g,h)u(gh) on an explicitly supplied one-dimensional local sector, not a theorem that every invariant syndrome supplies that sector.

Supplementary exact source and captured results: `outputs/campaign_c16_c18_landing_2026_10_17/independent_controls/exact-controls.py.txt` and `outputs/campaign_c16_c18_landing_2026_10_17/independent_controls/exact-controls.json`. These independent controls cover the named kernel/subgroup statements, not every shell-character or physical-localization claim.

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
