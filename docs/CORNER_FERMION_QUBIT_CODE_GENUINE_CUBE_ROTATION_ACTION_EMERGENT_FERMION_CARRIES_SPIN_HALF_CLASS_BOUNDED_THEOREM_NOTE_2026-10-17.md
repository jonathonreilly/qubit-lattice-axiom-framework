---
claim_id: corner_fermion_qubit_code_genuine_cube_rotation_action_emergent_fermion_carries_spin_half_class_bounded_theorem_note_2026-10-17
claim_type: bounded_theorem
claim_scope: "Supplied model: BKSF on the corner graph of Z^3 (vertices = the 12 perpendicular direction pairs at each site; edges = the cuboctahedron edges at a site and the plaquette links between neighbouring sites), with each cross-site link qubit split into two Z-repetition halves, one at each end site: 48 qubits per site, all on sites. Stabilizers: corner charges B_q, repetition terms R, and signed loop operators i^n F prod A on squares (around the C4 axes), triangles (around the octants), plaquettes and edge tubes, with uniform flux F per type; default square = plaquette = pi, triangle = tube = 0. Exact (Pauli algebra with phases, L = 4 torus): commuting group with no -I and log2 code dimension 3; the corner charge has T-junction sign -1; each cube rotation about a site is realized by the site permutation, an on-site CZ network, single-qubit Z fixes and a product of repetition stabilizers, it maps every hop exactly to the rotated hop and every stabilizer to plus a stabilizer, and the 24 operators satisfy U_a U_b = U_ab exactly on all single-qubit Paulis (all 576 pairs) and fix |0...0>, so they form a genuine linear representation of O on the whole qubit Hilbert space. Pair test restricted to the explicit unwrapped creator family in the box [-2,2]^3, projected to the L=4 torus (two corner charges, no repetition defects; contractible comparison loop): lambda = +1 for the three axis C2 and -1 for the six edge C2; with the twist W = prod exp(-i pi B/4) prod exp(-i pi R/4) on the w1-odd elements, which is again an exact O action because W^2 = (-i)^(24L^3) prod B prod R = I and W commutes with rotations, lambda = +1 for all nine C2. Conditional on the localization relation lambda = theta eta used in the companion notes, the fermion's class is w2 + w1^2 under U and w2 (the spin-1/2 class) under the twisted action. Fermion level (L = 4; GF(2) solves exact, lift/character/spectral reconstruction numerical): for all 16 uniform flux patterns the projective symmetry group exists; square flux pi gives axis C2^2 = -1, edge C2^2 = +1, C4^4 = -1; with the twist the 12-corner site representation lifts to a linear representation of 2O and decomposes as E1/2 + E5/2 + 2 G3/2; real on-site hopping never isolates a doublet, and an O-invariant chiral term on the triangles gives an isolated two-dimensional spinorial cluster ground level with gap 2.54 (E1/2 for the i^{w1} twist, E5/2 for the opposite twist; H = -t1 sum u c^dag c + i lambda sum over oriented triangles, t1 = -1, lambda = -0.5). The statements concern rotations about a site; the full space-group fractionalization differs from that of a spin-1/2 particle (C4 conjugation of a translation gives -1 on the fermion, and bond-centred axis C2 give lambda = -1). The historical qubit runner reported 18/18 for tube flux pi (flux argument 1011); this predates the strict creator-coverage repair and is not a current execution certificate. Not claimed here: the mobile doublet (the companion long-wavelength note finds, for tube flux pi, a numerical candidate for an isolated isotropic spinorial band minimum at the affine-fixed momentum k*; an earlier scan of Gamma and R only had suggested otherwise), which realization dynamics selects (the twist requires number-conserving dynamics), gap stability, a framework derivation of the corner structure, the fluxes or the qubit count, or any physical identification."
upstream_dependencies:
  - site_localizable_stabilizer_code_fermion_cannot_carry_the_spin_half_class_direction_shell_bounded_theorem_note_2026-10-17
  - bksf_cubic_fermion_codes_site_local_realization_with_six_direction_qubits_per_site_bounded_theorem_note_2026-10-17
  - bksf_cubic_fermion_codes_bare_permutation_rotations_act_spinorially_on_the_fermion_bounded_theorem_note_2026-10-17
runner: scripts/corner_fermion_qubit_code_genuine_cube_rotation_action_spin_half_class_2026_10_17.py
---

# A corner-fermion qubit code: a genuine cube-rotation action; the emergent fermion carries w2 + w1^2, and the spin-1/2 class under a U(1)-twisted action

**Date:** 2026-10-17
**Type:** bounded_theorem
**Status:** bounded support, unaudited. Exact for the supplied model at L = 4, with an historical pre-coverage-repair L = 6 run preserved as context, not a current certificate. The class identification is conditional on the localization relation used in the companion notes. Nothing is adopted.

## Question

The companion note on site-localizable fermions showed when a code cannot reach the spin-1/2 class. Its exclusion applies only to a one-dimensional invariant localized charge sector with the stated fusion-compatible symmetry-localization structure; a single-site charge term alone does not establish those hypotheses.

One proposed route is to avoid a single invariant site-centered charge sector. Corner positions still have a C2 stabilizer; they are not fixed by no rotation. Can a qubit code on the framework's sites do this? It must also have a genuine (linear) action of the cube rotation group, and its emergent fermion must carry w2.

## Historical motivation for corners (not an exclusion theorem)

- **Restricted fourth-root hypothesis.** If a specified emergent-fermion action has only phases {±1, ±i}, a C4-fixed vertex has u^4=+1. This restriction must be established for that realization; Clifford action on physical Paulis alone does not prove it for every emergent or PSG action.
- **Spin-1/2 needs eighth-root phases there.** The spin-1/2 class needs u^4 = −1, that is, an eighth root of unity.
- **Which positions avoid the C4 axes.**
  - Direction positions (half-edges) lie on C4 axes, and so do sites and edges.
  - The 12 corners (v; d, d') of a site, the pairs of perpendicular directions, lie only on edge-C2 axes.
  - So the corners are the smallest site-local orbit lying only on C2 axes. The eight octant positions v + (±1,±1,±1)/4 lie only on C3 axes. C3 carries no Z2 class, so they also avoid the C4 obstruction. They are not treated here.
- **Scope of this step.** It motivates the model. It is not part of the claim.

## Result

1. **The code (exact, L = 4).**
   - **Graph.** BKSF on the corner graph. Each corner has six hops:
     - four on-site, along the cuboctahedron edges at its site;
     - two plaquette links to the neighbouring sites.
   - **Qubits.** One qubit per hop.
     - Each link qubit is split into two repetition halves, one at each end site.
     - This gives 48 qubits per site, all of them on sites.
   - **Stabilizers.**
     - B_q, the corner charges;
     - R = ZZ, the repetition terms;
     - signed loop operators i^n F ∏A on squares, triangles, plaquettes and tubes. The default flux is square = plaquette = π, triangle = tube = 0.
   - **Checks.**
     - The stabilizer group commutes and contains no −I.
     - log2 code dimension = 3.
     - The hops anticommute exactly when they share one vertex.
     - The corner charge has T-junction sign −1, so it is a fermion.
2. **A genuine linear action of O (exact).**
   - **The rotation operator U_R** has four factors:
     - the site permutation, which permutes the 48 local qubits as labels;
     - an on-site CZ network, on the pairs of hops whose order changes;
     - single-qubit Z fixes, which give each hop its exact sign;
     - a product of repetition stabilizers.
   - **It preserves the code.** It maps every hop exactly to the rotated hop, and every stabilizer to plus a stabilizer.
   - **Without the last factor, the group law fails.** Composites differ by products of R.
     - That leftover is a 2-cocycle valued in the link permutation module.
     - No rotation fixes a link. A link midpoint has one quarter-integer and one half-odd coordinate. On the torus this needs L even; for odd L some links are fixed by a C2.
     - So all 32 link orbits are free, and the cocycle is a coboundary. It is solved orbit by orbit.
   - **The group law becomes exact.** After the correction, U_a U_b = U_ab on all 2 × 3072 single-qubit Paulis, for all 576 pairs.
     - The operators fix |0…0⟩, so the identity holds with no phase.
     - So the 24 operators form a linear representation of O on the whole qubit Hilbert space. Local states therefore carry ordinary representations.
3. **Pair test (exact; class conditional on λ = θη).**
   - **The creators.** Each is a clean hop string from the explicitly tested unwrapped box [-2,2]^3, then projected to the torus. Arbitrary periodic shortest strings are excluded: four of those give noncontractible logical comparison loops, not scalar pair eigenvalues. It flips exactly the two end charges B_q, B_Rq and no repetition term.
   - **Under U.** λ = +1 for the three axis C2 and λ = −1 for the six edge C2. With θ = −1 this is the class w2 + w1^2.
   - **Under the twisted action.**
     - Twist by W = ∏_q exp(−iπB_q/4) ∏_links exp(−iπR/4) on the w1-odd elements, which here are the edge C2 and the C4.
     - ∏B ∏R = I and there are 24L³ factors, so W² = (-i)^(24L³)∏B∏R = I exactly. W is rotation-invariant because the B and R sets are permuted. Thus V_g = U_g W^{w1(g)} is an exact O action.
     - W multiplies a two-charge state by −1. So the twisted action gives λ = +1 for all nine C2: the spin-1/2 class w2.
4. **The fermion-level structure (L = 4; exact GF(2) solves and numerical lift/character/spectral reconstruction in the second runner).**
   - **The PSG.** For all 16 uniform flux patterns, the projective symmetry group of a spinless fermion on the corners exists, for O and for translations.
     - Square flux π gives axis C2^2 = −1, edge C2^2 = +1 and C4^4 = −1. These are the same signs as in item 3.
     - Translations commute exactly when the square and plaquette fluxes agree.
   - **With the twist i^{w1}.** The action on the 12 corners of a site lifts to a linear representation of 2O. It decomposes as E1/2 + E5/2 + 2 G3/2, matching the face-diagonal shell of the companion note.
   - **Real hopping.** Real on-site hopping is time-reversal symmetric, and gives E1/2 + E5/2 or a G3/2 quartet as the lowest level.
   - **Why real hopping cannot do better.** Complex conjugation exchanges the twists i^{w1} and (−i)^{w1}, and so exchanges E1/2 and E5/2. A real Hamiltonian therefore cannot isolate one of them.
   - **Chiral hopping.** The cluster Hamiltonian is H = −t1 Σ u c†c + iλ Σ over the oriented triangles (counterclockwise about the outward body diagonal), with gauge signs u. Here flipping t1 is equivalent to flipping the triangle flux.
     - The O-invariant chiral term splits the pair.
     - The cluster ground level is then an isolated two-dimensional spinorial irrep, with gap 2.54 at t1 = −1, λ = −0.5. It is E1/2 for the i^{w1} twist and E5/2 for the opposite twist, which is equally exact.
     - Reversing the sign of λ exchanges the two labels.

## Primary coverage and algebraic argument

The Pauli group-law and coboundary tests are exact finite checks. The primary's covariance samples are corroboration of the following BKSF identity, not an exhaustive scan: the site permutation pushes each endpoint edge ordering; CZ gates on the inverted pairs restore its prefix-Z strings, and the diagonal Z orientation correction restores the signed A operator. B and R are permuted. The uniform cycle flux is invariant, giving loop covariance; the repetition correction commutes with the encoded A/B operators. These statements apply to the supplied construction and the stated finite realization, not every encoding.

For each of the nine C2 rotations, the fresh pair test requires at least one evaluated creator and zero unresolved logical reductions among the specified sampled endpoints using paths lifted to the actual rotated endpoint before periodic projection. The previous periodic-BFS test failed on four clean creators: their comparison operators commute with all stabilizers but are outside the stabilizer span, with nonzero winding modulo two. These remain explicit logical-loop controls; they are not silently skipped or added to the stabilizer basis. The scalar signs and conditional class inference apply to the tested contractible comparison-loop family, not every clean torus string. All repetition terms are checked for each tested creator. This is finite creator coverage; universal representative independence still requires the stated localization and admissible-dressing hypotheses. Cluster eigenvalues, gaps and character reconstructions are numerical.

## How this bears on the lane (interpretation, not a claim)

- **The sharpened target, as far as it was posed.** This is a qubit code with qubits on sites, an exact linear action of the cube rotations, and an emergent fermion.
  - Under the twisted action, the fermion's half-turn signs about a site are those of a spin-1/2 particle.
  - The twist is a chosen U(1) charge rotation, by i on the w1-odd elements. It is natural only for number-conserving dynamics.
  - No spin and no 2O action is put into the qubits.
- **It is not yet an ordinary spin-1/2 particle on the lattice** (independent check).
  - On the fermion, C4 conjugation of a translation gives −1.
  - Half-turns about bond-centred axes give λ = −1.
  - So the π fluxes fractionalize the full space group differently from a spin-1/2 particle in a uniform background. Only the point group about a site matches.
- **Where the spin comes from.** The fermion lives between the rotation axes, and sees a π flux around every lattice line. Going round an axis costs a sign, and that sign is the spin-1/2 double cover. This is related to how a charge around a flux line acquires half-integer angular momentum, as in Aharonov–Bohm and the Jackiw–Rebbi / Hasenfratz–'t Hooft "spin from isospin".
- **"Larger than a site."** The localized doublet of item 4 is spread over the twelve corners of a site, within this supplied model; this is not a universal requirement on every code.
- **Open.**
  - A mobile doublet as the certified global lowest band state remains open. The companion long-wavelength note gives numerical evidence for a candidate doublet at k* for tube flux π; it does not prove global uniqueness.
  - Which realization natural dynamics selects.
  - Whether the corner structure and the fluxes can be derived from the framework's axioms.

## Historical author check

These are submitted historical checks, with their original source identities. Current primary coverage is stated separately; numerical cluster spectra and character reconstruction are not exact arithmetic certificates.

A fresh-context agent (same model family) wrote its own code from the note's text, with its own orderings, hop signs and face lists, before reading the runners.
- **Items 1, 2 and 4: confirmed.**
  - Group law: U_a U_b = U_ab as a full operator identity, 576/576 pairs. Every operator is a diagonal quadratic phase times a permutation, so the comparison is exact on the whole space.
  - Hops and stabilizers were checked in full, not sampled. The result holds for two random orderings.
  - Pair test: 252 random clean creators and 216 dressed ones all give the same λ. The twisted λ = +1 for all nine C2.
  - k = 3, θ = −1, and ∏B ∏R = I.
- **Corrections, applied above.**
  - The octant orbit also avoids the C4 axes.
  - E1/2 versus E5/2 is a convention, and H is now written out.
  - The link-orbit argument is stated precisely.
  - The title is narrowed.
  - The twisted action is not on-site.
  - Prior art is added.
- **New caveat.** The space-group fractionalization (translation–C4 relation, bond-centred C2) differs from that of a spin-1/2 particle.

Files: `.claude/science/physics-loops/toe-campaign-20261017/c17_corner_fermion/independent_check/`.

## Premises

- **Axioms used.** Lattice (Z^3, unit translations, proper cubic rotations about sites).
- **Supplied.**
  - The corner graph, the BKSF encoding with repetition halves and the uniform fluxes.
  - The localization relation λ = θη, as in the companion notes.
  - For w2: the twisted realization.
- **Declared enlargement.** 48 qubits per site. For comparison, the half-edge model has 6.

## Relation to prior work

- **Encodings.**
  - BKSF: Bravyi and Kitaev, Ann. Phys. 298, 210 (2002).
  - Generalized superfast encodings: Setia, Bravyi, Mezzacapo and Whitfield, PRR 1, 033033 (2019).
- **Projective symmetry groups.** Wen, PRB 65, 165113 (2002).
- **π flux and projective lattice symmetries** are standard, for example magnetic translations.
- **Spatial symmetry fractionalization.**
  - Essin and Hermele, PRB 87, 104406 (2013).
  - Qi and Fu.
  - Thorngren and Else, PRX 8, 011040 (2018).
- **Spinorial rotations from π-flux hopping on the cube.** Staggered fermions: Kogut and Susskind, PRD 11, 395 (1975); Golterman and Smit, NPB 245, 61 (1984); Kilcup and Sharpe, NPB 283, 493 (1987).
- **T-junction statistics.** Levin and Wen, PRB 67, 245316 (2003).
- **Spin from flux.**
  - Jackiw and Rebbi, PRL 36, 1116 (1976).
  - Hasenfratz and 't Hooft, PRL 36, 1119 (1976).
- **New here.**
  - The corner-graph construction.
  - The exact genuine O action on a site-local qubit code: the CZ network, the Z fixes, and the free-orbit coboundary.
  - The verification that its emergent fermion's pair signs are those of w2 + w1^2, and w2 with the twist.
  - The 12-corner shell, and the chiral splitting to an isolated E1/2 cluster doublet.

## No-Go Discipline Gate

- **N1 — routes.** Other positions (the octant positions, cube centres, generic points) and other fluxes are not treated.
- **N2/N3 — scope.** One supplied model, with exact checks on the L = 4 torus. An historical pre-coverage-repair L = 6 run (10,368 qubits) reported 18/18; it is not a current certificate (loop pack, `runner_qubits_L6.log`).
- **N4 — inputs.**
  - The Pauli algebra is exact.
  - The PSG and the shell use exact GF(2) solves and finite group characters.
  - The class inference uses the stated localization relation.
- **N5 — wording.** "Spin-1/2 class" means the involution signs of w2 under the stated realization. Nothing about physical spin or charge is claimed.
- **N6/N7 — strongest objections.**
  - The twist is a choice of realization, natural only for number-conserving dynamics. Without it the class is w2 + w1^2.
  - The twisted action V is a Clifford but not on-site, because W contains exp(−iπR/4) across neighbouring sites. The independent check gives an on-site alternative, derived analytically but not run.
  - The space-group fractionalization differs from a spin-1/2 particle's: the translation–C4 relation and the bond-centred C2.
  - The lowest mobile state is treated in the companion long-wavelength note (tube flux π), not here.
  - 48 qubits per site is a large enlargement.
- **N8 — earlier claims.** Realizes the open route of the site-localizable note. It does not change the earlier results.

## Verification

```bash
python3 scripts/corner_fermion_qubit_code_genuine_cube_rotation_action_spin_half_class_2026_10_17.py
python3 scripts/corner_fermion_projective_symmetry_group_class_and_site_shell_2026_10_17.py
```

Expected: `TOTAL: PASS=19 FAIL=0` (about two minutes) and `TOTAL: PASS=7 FAIL=0` (about 20 seconds).

## Load-bearing sources

Contextual downstream study, not a premise of this construction: `docs/CORNER_FERMION_LONG_WAVELENGTH_THEORY_IS_ONE_ISOTROPIC_SPIN_HALF_DOUBLET_AND_ONE_QUBIT_BLOCK_EMBEDDING_BOUNDED_THEOREM_NOTE_2026-10-17.md`.

- [Site-localizable obstruction note](SITE_LOCALIZABLE_STABILIZER_CODE_FERMION_CANNOT_CARRY_THE_SPIN_HALF_CLASS_DIRECTION_SHELL_BOUNDED_THEOREM_NOTE_2026-10-17.md)
- [Half-edge note](BKSF_CUBIC_FERMION_CODES_SITE_LOCAL_REALIZATION_WITH_SIX_DIRECTION_QUBITS_PER_SITE_BOUNDED_THEOREM_NOTE_2026-10-17.md)
- [Bare-permutation note](BKSF_CUBIC_FERMION_CODES_BARE_PERMUTATION_ROTATIONS_ACT_SPINORIALLY_ON_THE_FERMION_BOUNDED_THEOREM_NOTE_2026-10-17.md)
- [Axioms](MINIMAL_AXIOMS_2026-06-29.md)
