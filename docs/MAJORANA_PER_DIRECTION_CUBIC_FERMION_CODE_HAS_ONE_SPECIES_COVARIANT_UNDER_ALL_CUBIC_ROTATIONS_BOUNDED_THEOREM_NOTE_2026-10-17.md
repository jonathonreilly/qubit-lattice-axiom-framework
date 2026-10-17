---
claim_id: majorana_per_direction_cubic_fermion_code_has_one_species_covariant_under_all_cubic_rotations_bounded_theorem_note_2026-10-17
claim_type: bounded_theorem
claim_scope: "Supplied model: three qubits per site of Z^3 carrying six local Majorana operators gamma_{v,d}, one per direction d (fixed Jordan-Wigner choice inside each site; Majoranas at different sites commute). Generators: site parity B_v = (-i)^3 gamma_{v,0}...gamma_{v,5} and plaquettes S_p = product of the four edge operators A_(v,a) = gamma_{v,+a} gamma_{v+e_a,-a} around a plaquette, with one sign per plaquette orientation. Rotations act by permuting sites together with the on-site Clifford gamma_{v,d} -> eps(d) gamma_{Rv,Rd}, prod eps = sign of the direction permutation. Exact: on even tori all 8 translation-invariant sign sectors are valid commuting stabilizer groups with log2 code dimension 3 (L = 4; also L = 6 for the two uniform sectors; on odd tori only the all-plus sector is valid); the B-violations are moved by the edge operators and have Levin-Wen T-junction sign -1 for all 20 triples of straight legs (L = 6); every one of the 24 rotations, with every admissible sign choice (32 each), maps the signed groups of the two uniform sectors to themselves (L = 4). So the code carries a single fermion species and is covariant under the full proper cubic group, with an on-site Clifford action. Group law: 128 of the 1024 sign choices on a C4 and a C3 generate an order-48 signed-permutation group containing -1, a central extension of O by fermion parity isomorphic to A4 x| Z4 (the extension pulled back from the sign character O = S4 -> Z2; not the spin double cover); in all of them the lifts of axis C2 square to +1 and those of edge C2 to -1. Fractionalization (clean pair creators, consistent group action): every axis C2 and every edge C2 gives pair eigenvalue -1, so eta_f(C2, C2) = +1 for both conjugacy classes and the fermion's class on O is trivial (H^2(O; Z2) = Z2^2 is detected by the two involution classes); twisting by W = prod_v exp(-i pi B_v / 4) (on-site, constant on the code space) is consistent with the group law only along the sign character of O (dress the odd elements), and gives eta_f(axis C2) = +1, eta_f(edge C2) = -1; the spin-1/2 class w2 on O (both -1) is not reachable by such twists, since an axis C2 is the square of a C4. Not claimed: bare-permutation realizations (a bare qubit permutation does not implement the Majorana permutation), the relation to Admissibility, dynamics, or any physical identification."
upstream_dependencies:
  - bksf_cubic_fermion_codes_are_not_rotation_invariant_minimal_orbit_four_bounded_theorem_note_2026-10-17
runner: scripts/majorana_per_direction_cubic_fermion_code_full_rotation_covariance_2026_10_17.py
---

# A Majorana-per-direction cubic fermion code has one fermion species covariant under all cubic rotations

**Date:** 2026-10-17
**Type:** bounded_theorem
**Status:** bounded support, unaudited. Exact for the stated model.
Nothing is adopted.

## Question

In the translation-invariant BKSF family, no code is invariant under the 24
cube rotations. A rotation-covariant stack needs at least four fermion
species (companion orbit note).

The obstruction there is the ordering of edges at each vertex. Is it
intrinsic, or does it come from insisting that rotations act by bare qubit
permutation?

## Result

1. **The code.** Three qubits per site carry six Majoranas γ_{v,d}, one
   for each direction.
   - Edge operators: A_(v,a) = γ_{v,+a} γ_{v+e_a,-a}.
   - Site parity: B_v = (-i)^3 γ_{v,0}...γ_{v,5}.
   - Plaquettes: S_p = the product of the four A around a plaquette, with a
     sign for each plaquette orientation.
   - **Exact results.**
     - On even tori, all 8 translation-invariant sectors are valid
       commuting stabilizer groups with log2 code dimension 3 (L = 4). The
       uniform sectors also have dimension 3 at L = 6. On odd tori only the
       all-plus sector is valid; the independent check found this.
     - The violations of B are moved by the edge operators. Their Levin–Wen
       T-junction sign with straight legs is -1 for all 20 triples of
       directions (L = 6): a fermion. The -1 is built in, since each leg
       contributes a distinct local Majorana at the junction.
2. **Full cubic covariance (exact).** Let a rotation R permute the sites
   and act on each site's Majoranas by γ_{v,d} -> ε(d) γ_{Rv,Rd}, with
   prod ε equal to the sign of the direction permutation, so that B_v goes
   to B_{Rv}. This is an on-site Clifford.
   - For each of the 24 rotations and each of the 32 admissible ε, the
     signed groups of both uniform sectors map to themselves.
   - So this code has one fermion species and the full proper cubic
     symmetry.
   - The check is close to a tautology. Each plaquette contains each of
     its Majorana directions twice, so S_p goes to S_{Rp} for any ε; only
     B constrains ε.
   - The independent check found that the 24 improper elements also
     preserve the code.
3. **Group law (exact).**
   - Choose ε for a C4 and for a C3, and generate the group of signed
     direction permutations. 128 of the 1024 choices give a group of order
     48 containing -1, the global Majorana sign flip, i.e. conjugation by
     fermion parity.
   - So O acts on the code through a central extension by fermion parity.
   - Its element orders are 1, 2 (7 elements), 3 (8), 4 (24) and 6 (8),
     with no element of order 8. So it is A4 x| Z4, the extension pulled back
     from the sign character of O = S4. It is neither the spin double cover
     2O nor GL(2,3).
   - In every such choice, the lifts of the axis C2 square to +1 and the
     lifts of the edge C2 square to -1. This is forced:
     - an axis C2 fixes the two Majoranas along its axis, so its square
       cannot flip all six;
     - an edge C2 is an odd permutation (three transpositions), so the
       determinant condition forces its square to flip every Majorana.

4. **Fractionalization (exact, pair test).** Use the consistent group
   action of item 3.
   - Solve for a clean pair creator S: it flips exactly B_x and B_Rx and
     commutes with every other generator.
   - This is possible here because the plaquettes map to plaquettes
     exactly, so S^R is clean as well.
   - λ = sign(S^dagger S^R) in the signed group.
   - **Result.** At L = 8 in the runner and at L = 10 in exploration, in
     both sectors, λ = -1 for every axis C2 and every edge C2,
     consistently across positions and conjugate elements. So
     eta_f(C2, C2) = +1 for both classes.
   - H^2(O; Z2) = Z2^2 is detected by these two classes, so the fermion's
     class under this action is trivial. It is not spinorial.
   - The independent check found the same for all 128 consistent group
     choices, with both lifts of each element.
5. **Twisted realizations (from 4; corrected by the independent
   check).**
   - Let W = prod_v exp(-i pi B_v / 4). It is on-site, commutes with every
     generator, and is constant on the code space. On a two-fermion state
     it contributes a relative phase -1.
   - The twisted family V_g = U_g W^{n(g)} is an action up to fermion
     parity only if n is a homomorphism O -> Z2, i.e. the sign character.
     - Checked numerically by the independent check: 0 failures for the
       sign twist; 576 of 576 pairs fail when every element is dressed.
   - The sign twist flips the edge C2 (odd) and leaves the axis C2 (even).
     So it gives eta_f(axis C2) = +1 and eta_f(edge C2) = -1: the
     sign-pullback class.
   - The spin-1/2 class w2 (both -1) cannot be reached by any W-twist,
     because an axis C2 is the square of a C4.
   - **More generally (standard group theory): no realization can give
     w2 on O while each fermion has a single local state.**
     - A one-dimensional local action with fermion parity acting as -1
       would be a character of the binary octahedral group 2O sending -1
       to -1.
     - But -1 lies in the commutator subgroup of 2O, already in Q8 over the
       three axis C2. So every character sends it to +1.
     - So a cubic-symmetric spin-1/2 class needs a degenerate,
       doublet-like fermion, like the two spin states of an electron.
6. **Caution, from the exploration.** An earlier solver let S also
   create excitations next to the endpoints. It gave λ = +1 for the axis
   C2.
   - Here a single Majorana flips B_x together with four plaquettes. So
     "fermion plus elementary flux" is a local excitation in the trivial
     sector.
   - Such a dressed creator changes what the endpoints are, rather than
     dressing the fermion.
   - Only clean creators represent the fermion pair. (In BKSF this cannot
     happen: no local operator flips an odd number of charges.)

## How this bears on the lane (interpretation, not a claim)

- **A single cubic-covariant species exists once on-site Cliffords are
  allowed.** The BKSF orbit note's "at least four species" concerns bare
  qubit permutations of BKSF codes.
  - Here, with a different encoding and an on-site Clifford action, one
    species is cubic-covariant.
  - Two things change at once, the encoding and the action. The companion
    site-local note settles the encoding question.
    - In the six-qubit half-edge form, the BKSF codes themselves become
      O-invariant under on-site signed Majorana permutations.
    - So the species minimum is a statement about the bare action.
- **The framework still has to choose.** Whether the rotation acts on a
  site's qubits by bare relabelling or by such an on-site unitary is a
  declared reading of the Lattice axiom. The two readings give different
  species counts.
- **One fully cubic-covariant species, but not (yet) spin-1/2 on all of
  O.**
  - With the consistent on-site action U_R, the single fermion species is
    spinless.
  - With the sign twist, it is spinorial for the edge C2 only.
  - The spin-1/2 class on all of O cannot be carried by a single-state
    fermion at all (item 5). Full cubic spin-1/2 needs a doublet. Here
    "one species" and "spin-1/2 under the full cube" are mutually
    exclusive.
  - "Spin" is again a property of how rotations act on the site's qubits.
    The framework would have to fix that action to make a prediction.
- **Which action does natural dynamics pick?** (Loop pack, c12,
  `hopsym.py`.)
  - U_R maps each Majorana hop A_e to plus or minus A_{Re}. No
    translation-invariant sign pattern of a nearest-neighbour Majorana
    hopping sum t_a A is U_R-symmetric for any of the 128 consistent
    actions. A staggered Z2 gauge dressing by vertex terms repairs this,
    and does not change the class.
  - U_R W instead attaches the endpoint parities B_t B_h to each hop. No
    sign gauge removes that.
  - So Majorana-only hopping selects the spinless realization, as the
    BKSF independent check found for that family. A twisted class needs
    dynamics symmetric under the twisted action, such as number-conserving
    hopping.
  - Under number-conserving hopping both realizations are symmetries.
    They differ by e^{i pi N / 2}, so the distinction merges with the U(1)
    charge, as in a spin-charge relation.

## Independent check

A fresh-context agent (same model family) wrote its own code before
reading the runner.
- **Items 1–4: confirmed.** It added the odd-L caveat, the improper
  elements and the A4 x| Z4 identification.
- **Item 4 (pair test): confirmed** independently, with clean creators:
  λ = -1 for both classes, for all 128 consistent choices, at L = 10 and
  L = 12. It also identified the dressing pitfall of item 6.
- **Second round: one correction.** It refuted the first version of
  item 5, which claimed that U_R W carries w2 on all of O, because
  dressing every element violates the group law. Item 5 is corrected
  accordingly.
- **Prior art.** It found the Li–Po prior art, and noted that the
  Wu–Arovas–Hung 3D example is on the diamond lattice.
- **Interpretation.** It flagged the overreach that is corrected above.

Files: `.claude/science/physics-loops/toe-campaign-20261017/c12_majorana_per_direction/independent_check/`.

## Premises

- **Axioms used.** Lattice (Z^3, unit translations, proper cubic rotations
  about sites).
- **Supplied model.** Three qubits per site, an enlargement of the Qubit
  axiom, with plaquette-range generators.
- **Declared choices.**
  - The Jordan–Wigner choice inside a site; any other is related by an
    on-site Clifford.
  - The rotation action with on-site Cliffords.

## Relation to prior work

- Generalized superfast encoding, with one local Majorana per incident edge
  and d/2 qubits per vertex: Setia, Bravyi, Mezzacapo and Whitfield, PRR 1,
  033033 (2019). The code above is its cubic-lattice instance, with the
  vertex parities imposed as stabilizers.
- A higher-dimensional Jordan–Wigner transformation that keeps spatial
  symmetries manifest, using auxiliary Majoranas on square, triangular and
  cubic lattices: K. Li and H. C. Po, arXiv:2107.14083. This is close prior
  art for the symmetric structure. Auxiliary Majoranas for 2D and 3D
  Jordan–Wigner: Verstraete and Cirac, J. Stat. Mech. P09012 (2005),
  cond-mat/0508353.
- Exactly solvable Γ-matrix generalizations of Kitaev's model use several
  Majoranas per site and emergent Z2 gauge fields; their 3D examples are on
  the diamond lattice: Wu, Arovas and Hung, PRB 79, 134427 (2009).
- BKSF orbit note: the bare-permutation family, with minimal orbit four.
- **New here, modestly.** The construction and its manifest symmetry are
  close to known work (Li and Po). What is added:
  - the exact finite checks;
  - the identification of the on-site group law as A4 x| Z4;
  - the contrast with the BKSF species minimum.

## No-Go Discipline Gate

- **N1 — routes around the claim.** Bare-permutation realizations, other
  on-site actions and other encodings are not treated.
- **N2/N3 — scope.** One code, eight sectors, the full group O.
- **N4 — inputs.** Exact Pauli algebra with phases at L = 4 and L = 6.
  The statistics run uses L = 6, so that opposite legs do not meet across
  the torus.
- **N5 — wording.** "One species" means one type of B-violation, the only
  point charge type.
- **N6/N7 — strongest objection.** On-site Cliffords are not bare
  relabellings. This is stated in item 2 and in the interpretation.
- **N8 — earlier claims.** Consistent with the BKSF orbit note, whose
  species minimum is for bare permutations.

## Verification

```bash
python3 scripts/majorana_per_direction_cubic_fermion_code_full_rotation_covariance_2026_10_17.py
```

Expected: `TOTAL: PASS=8 FAIL=0` (about 2 minutes).

## Load-bearing sources

- [BKSF orbit note](BKSF_CUBIC_FERMION_CODES_ARE_NOT_ROTATION_INVARIANT_MINIMAL_ORBIT_FOUR_BOUNDED_THEOREM_NOTE_2026-10-17.md)
- [Axioms](MINIMAL_AXIOMS_2026-06-29.md)
