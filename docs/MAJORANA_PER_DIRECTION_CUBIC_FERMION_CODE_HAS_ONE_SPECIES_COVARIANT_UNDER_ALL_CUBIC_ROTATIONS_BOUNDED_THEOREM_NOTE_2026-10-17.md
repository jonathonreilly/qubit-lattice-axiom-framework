---
claim_id: majorana_per_direction_cubic_fermion_code_has_one_species_covariant_under_all_cubic_rotations_bounded_theorem_note_2026-10-17
claim_type: bounded_theorem
claim_scope: "Supplied model: three qubits per site of Z^3 carrying six local Majorana operators gamma_{v,d}, one per direction d (fixed Jordan-Wigner choice inside each site; Majoranas at different sites commute). Generators: site parity B_v = (-i)^3 gamma_{v,0}...gamma_{v,5} and plaquettes S_p = product of the four edge operators A_(v,a) = gamma_{v,+a} gamma_{v+e_a,-a} around a plaquette, with one sign per plaquette orientation. Rotations act by permuting sites together with the on-site Clifford gamma_{v,d} -> eps(d) gamma_{Rv,Rd}, prod eps = sign of the direction permutation. Exact: on even tori all 8 translation-invariant sign sectors are valid commuting stabilizer groups with log2 code dimension 3 (L = 4; also L = 6 for the two uniform sectors; on odd tori only the all-plus sector is valid); the B-violations are moved by the edge operators and have Levin-Wen T-junction sign -1 for all 20 triples of straight legs (L = 6); every one of the 24 rotations, with every admissible sign choice (32 each), maps the signed groups of the two uniform sectors to themselves (L = 4). So the code carries a single fermion species and is covariant under the full proper cubic group, with an on-site Clifford action. Group law: 128 of the 1024 sign choices on a C4 and a C3 generate an order-48 signed-permutation group containing -1, a central extension of O by fermion parity isomorphic to A4 x| Z4 (the extension pulled back from the sign character O = S4 -> Z2; not the spin double cover); in all of them the lifts of axis C2 square to +1 and those of edge C2 to -1. Not claimed: the fractionalization class of the emergent fermion (under study), bare-permutation realizations (a bare qubit permutation does not implement the Majorana permutation), the relation to Admissibility, dynamics, or any physical identification."
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

## How this bears on the lane (interpretation, not a claim)

- **A single cubic-covariant species exists once on-site Cliffords are
  allowed.** The BKSF orbit note's "at least four species" concerns bare
  qubit permutations of BKSF codes.
  - Here, with a different encoding and an on-site Clifford action, one
    species is cubic-covariant.
  - Two things change at once, the encoding and the action. Whether the
    BKSF codes themselves become invariant under some local-Clifford action
    is not shown.
- **The framework still has to choose.** Whether the rotation acts on a
  site's qubits by bare relabelling or by such an on-site unitary is a
  declared reading of the Lattice axiom. The two readings give different
  species counts.
- **The spin question is open here.** How the emergent fermion's
  fractionalization class depends on the realization is under study (loop
  pack, c12).

## Independent check

A fresh-context agent (same model family) wrote its own code before
reading the runner.
- **Items 1–4: confirmed.** It added the odd-L caveat, the improper
  elements and the A4 x| Z4 identification.
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

Expected: `TOTAL: PASS=7 FAIL=0` (about 1.5 minutes).

## Load-bearing sources

- [BKSF orbit note](BKSF_CUBIC_FERMION_CODES_ARE_NOT_ROTATION_INVARIANT_MINIMAL_ORBIT_FOUR_BOUNDED_THEOREM_NOTE_2026-10-17.md)
- [Axioms](MINIMAL_AXIOMS_2026-06-29.md)
