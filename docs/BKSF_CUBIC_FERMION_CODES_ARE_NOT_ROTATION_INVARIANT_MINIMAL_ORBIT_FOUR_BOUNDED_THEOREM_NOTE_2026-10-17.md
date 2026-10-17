---
claim_id: bksf_cubic_fermion_codes_are_not_rotation_invariant_minimal_orbit_four_bounded_theorem_note_2026-10-17
claim_type: bounded_theorem
claim_scope: "Supplied model: translation-invariant Bravyi-Kitaev superfast (BKSF) stabilizer codes on the cubic lattice, one qubit per edge of Z^3, specified by one ordering of the six edge directions used at every vertex; code = <B_v (Z on the six edges at v), S_p (product of the BKSF edge operators A_e around each plaquette)>. Exact (GF(2) algebra, all 720 orderings): every A_e commutes with all S_p and flips exactly its two endpoint B's; with straight legs (products of A_e along axes meeting only at the junction) the Levin-Wen T-junction sign is -1 for all 20 triples of the six axis directions in every code (the untwisted toric code gives +1), so the point charge is a fermion; the torus code dimension is log2 = 3 at L = 4, 6. The 720 orderings give 60 distinct stabilizer groups; the proper cubic group O permutes them in orbits of sizes 4, 6 and 12 (12, 12 and 36 codes). No code is O-invariant; the largest stabilizer is D3 (a C3 about a body diagonal with three edge C2), so a stack of rotated copies that is O-covariant carries at least four fermion species, permuted as the four body diagonals. Not claimed: vertex-dependent orderings, other fermionic encodings, site-covariant qubit placement, coupling between copies, any physical identification (electron, generations)."
upstream_dependencies:
  - minimal_axioms
runner: scripts/bksf_cubic_fermion_codes_rotation_orbits_2026_10_17.py
---

# BKSF fermion codes on the cubic lattice are not rotation-invariant; the smallest rotation orbit has four codes

**Date:** 2026-10-17
**Type:** bounded_theorem
**Status:** bounded support, unaudited. The statements are exact for the
stated family of supplied codes. Nothing is adopted.

## Question

The companion notes searched symmetric star rules and found no coherently
mobile fermionic charge. Known three-dimensional emergent-fermion
constructions use extra structure, such as a framing or a spin structure. A
concrete instance is the BKSF encoding: a qubit on each edge, with edge
operators fixed by an ordering of the edges at each vertex.

How does such a code behave under the cubic rotations? In particular, if
copies are stacked so that the whole is rotation-covariant, how many fermion
species must the stack carry? The repository's BKSF census note lists
rotation covariance of the ordered BKSF operators as untested; this note
tests it for translation-invariant orderings.

## Result

1. **Every code has a fermionic point charge (exact).**
   - For each of the 720 orderings, each A_e commutes with every plaquette
     stabilizer and flips exactly the two charges at its endpoints.
   - Legs are built as products of A_e along straight axis paths, so they
     meet only at the junction. The Levin–Wen T-junction sign is then -1 for
     all 20 triples of the six axis directions.
   - The untwisted toric code gives +1 for all 20.
2. **Bounded code dimension (exact, finite).** log2 = 3 on L = 4 and L = 6
   tori for a code of each orbit type: a Z2 gauge theory with a fermionic
   charge.
3. **Sixty codes (exact).** The 720 orderings give 60 distinct stabilizer
   groups, compared as spans on the L = 4 torus.
4. **Rotation orbits (exact).** The proper cubic group permutes the 60 codes:

   | orbit size | codes | stabilizer in O |
   |---|---|---|
   | 4 | 12 | D3: a C3 about a body diagonal and three edge C2 |
   | 6 | 12 | order 4: one axis C2 and two edge C2 |
   | 12 | 36 | order 2: one edge C2 |

   No code is invariant under the full cubic group.
5. **Consequence.** Stack the rotated images of one code on separate qubits.
   The stack is rotation-covariant and carries one fermion species per
   copy, so at least four species. The minimum, four, is reached by the
   D3-invariant codes, whose copies are labelled by the four body
   diagonals.

## How this bears on the lane (interpretation, not a claim)

- **The species count.** O acts on the four body diagonals as the symmetric
  group S4. As a permutation representation this decomposes as 1 + 3, a
  singlet plus a three-dimensional representation. Restricted to the
  threefold rotation about one diagonal, the 3 carries the characters
  1, omega and omega-bar.
- **The caveats.**
  - In a stack of decoupled copies the four species are separate
    superselection sectors. The "1 + 3" is a labelling of sectors, not a
    flavour space in which states can mix.
  - Turning the labels into mixable flavours would need couplings between
    copies, which are not constructed here.
  - The count depends on the encoding family. Vertex-dependent orderings or
    other fermion encodings might be more symmetric.
- **What it does show.** In this standard family, a fermion that respects the
  framework's cubic covariance cannot come alone: rotation symmetry forces
  copies, and the minimum is four.

## Independent check

A fresh-context agent (same model family) wrote its own code without reading
these scripts. It confirmed all five claims:
- it applied rotations by permuting qubits directly;
- it checked statistics on an L = 10 torus;
- it found code dimensions 3 at L = 4, 5 and 6.

It also attacked the conclusion. Neither per-edge single-qubit Clifford
relabelings nor reflections make any code invariant or merge any orbits. Its
support-count test is exact on the L = 4 torus. Files:
`.claude/science/physics-loops/toe-campaign-20261017/c6_bksf_orbits/independent_check/`.

## Premises

- **Axioms used.** Lattice (Z^3, proper cubic rotations).
- **Supplied model.** BKSF codes with qubits on edges. This is not the
  framework's site-local possibility domain; edges are not sites. Placing
  the qubits covariantly on sites is a separate problem; compare the
  interleaving in the three-axis-qubit note.
- **Declared choices.** One ordering, the same at every vertex;
  translation invariance; the stabilizer group <B, S>.

## Relation to prior work

- The BKSF encoding: Bravyi and Kitaev, Ann. Phys. 298, 210 (2002); Setia,
  Bravyi, Mezzacapo and Whitfield, PRR 1, 033033 (2019).
- Spin-structure dependence of 3D bosonization: Chen and Kapustin,
  PRB 100, 245127 (2019).
- The T-junction criterion: Levin and Wen, PRB 67, 245316 (2003).
- In this repository, `FINITE_BKSF_SIGN_AND_SUPERLATTICE_MARKER_CENSUS_BOUNDED_THEOREM_NOTE_2026-09-02`
  found fermionic T-junction signs for a coordinate-fixed BKSF embedding.
  It recorded that covariance under proper cubic rotations was not tested.
- **New here.**
  - The rotation-orbit classification of translation-invariant BKSF codes.
  - The bound that a rotation-covariant stack needs at least four species.

## No-Go Discipline Gate

- **N1 — routes around the claim.**
  - Not covered: vertex- or sublattice-dependent orderings, generalized
    superfast encodings, other fermionic stabilizer codes, non-Pauli
    constructions, ancilla-assisted symmetrization, and couplings between
    copies.
  - Any of these could be O-invariant. The "at least four" statement holds
    only within this family.
  - It also holds only for rotations acting by bare permutation. The later
    site-local realization note shows the following: with six direction
    qubits per site and on-site Clifford actions (signed permutations of
    in-site Majoranas), these codes are O-invariant.
- **N2/N3 — scope.** One family of 720 codes.
- **N4 — inputs.** Exact GF(2) computations. Group equality is span
  equality on the L = 4 torus. Statistics use straight legs, so leg
  crossings cannot introduce spurious signs.
- **N5 — wording.** "Fermion" is the Levin–Wen T-junction sign. Adiabatic
  exchange and gap stability are not computed.
- **N6/N7 — strongest objection.** The minimal orbit could be an artifact of
  insisting on the same ordering at every vertex. However, the framework's
  Lattice axiom requires covariance under unit translations. A
  vertex-dependent ordering is translation-covariant only if the different
  orderings define the same stabilizer group, which places it in this
  family's classes. Encodings with more qubits per edge, or ancillas, remain
  untested.
- **N8 — earlier claims.** This fills the rotation-covariance gap left by
  the 2026-09-02 BKSF census note. It is consistent with the companion
  notes' finding of no symmetric star fermions.

## Verification

```bash
python3 scripts/bksf_cubic_fermion_codes_rotation_orbits_2026_10_17.py
```

Expected: `TOTAL: PASS=8 FAIL=0` (about 30 seconds).

## Load-bearing sources

- [BKSF census note](FINITE_BKSF_SIGN_AND_SUPERLATTICE_MARKER_CENSUS_BOUNDED_THEOREM_NOTE_2026-09-02.md)
- [Fermion search companion](THREE_AXIS_QUBIT_SYMMETRIC_STABILIZER_RULES_FERMION_SEARCH_FINDS_NO_COHERENTLY_MOBILE_FERMION_BOUNDED_THEOREM_NOTE_2026-10-17.md)
- [Axioms](MINIMAL_AXIOMS_2026-06-29.md)
