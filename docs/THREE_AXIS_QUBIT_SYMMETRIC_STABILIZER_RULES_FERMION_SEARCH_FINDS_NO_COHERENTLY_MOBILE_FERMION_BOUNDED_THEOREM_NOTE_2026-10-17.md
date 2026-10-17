---
claim_id: three_axis_qubit_symmetric_stabilizer_rules_fermion_search_finds_no_coherently_mobile_fermion_bounded_theorem_note_2026-10-17
claim_type: bounded_theorem
claim_scope: "Supplied stabilizer model with three axis-indexed qubits per site of Z^3 (O permutes them as axes; Pauli labels unsoldered or fully soldered); star-supported signed Pauli rules closed under O. Exact lemma: if every generator label lies in a single-site abelian alphabet A that is its own single-site commutant, then either A lies in the group (product state) or every operator commuting with all free single-site variables commutes with every generator. Exact (soldered): among all star strings fixed by some nontrivial rotation (34927 strings fixed by one of four representative rotations, 70999 after closing under O, forming 4319 sign-consistent orbits; the axis-C2 part of the enumeration is reproduced in the runner's --full mode), every rule either lies in the alphabet <X_x, Y_y, Z_z> (lemma applies), or lies in one of eight valid 3-orbit fracton rules (no three-dimensionally mobile charge), or lies in one of two sets whose unions contain -1 and whose valid sub-rules have code dimension at least 32, 48 at L = 4, 6. So no such soldered rule has bounded code dimension together with a charge moved by free-variable-preserving operators. Exact within the search (unsoldered): among C4/C3-fixed strings, the valid maximal commuting sets with equal nonzero code dimension at L = 4, 6 are 36 rules, all with log2 dimension 24, and every same-site charge pattern that moves by 2e_x, 2e_y, 2e_z is a boson (Levin-Wen T-junction). Not claimed: strings with trivial stabilizer, non-maximal bounded rules, charge patterns spread over several sites, non-Pauli rules, dynamics, or any physical identification."
upstream_dependencies:
  - three_axis_qubit_site_stabilizer_rules_unsoldered_toric_codes_move_soldered_maximal_rules_do_not_bounded_theorem_note_2026-10-17
runner: scripts/three_axis_qubit_symmetric_stabilizer_rules_fermion_search_2026_10_17.py
---

# Symmetric three-axis-qubit stabilizer rules: no coherently mobile fermion

**Date:** 2026-10-17
**Type:** bounded_theorem
**Status:** bounded support, unaudited. The statements are exact within the
supplied model and the stated search restrictions. Nothing is adopted.

## Question

The three-axis-qubit companion note found coherent three-dimensional motion
of bosonic charges with unsoldered labels, and none in the restricted
soldered class. Does any symmetric star rule in these classes carry a
three-dimensionally mobile **fermionic** point charge? A hypothesis worth
testing: fermion strings need a framing, the cubic group fixes no direction
at a site, and soldering supplies the extra signs that might allow
fermions.

## Result

1. **Alphabet lemma (exact).**
   - Suppose every generator's single-site labels lie in an abelian
     single-site subgroup A whose single-site commutant is A.
   - Let A_G be the part of A inside the stabilizer group. If A_G = A, the
     rule is a product state.
   - Otherwise the free single-site variables are A minus A_G. The
     complement of a proper subgroup generates the group, so they generate
     A. An operator commuting with them therefore lies in A on every site,
     and commutes with every generator.
   - This unifies the Bell family of the two-qubit note and the 187-orbit
     family of the three-axis-qubit note.
2. **Soldered, all rotation-fixed strings (exact).**
   - **Count.** 34927 star strings are fixed by one of four representative
     rotations (C2 about z, C2 about (1, 1, 0), C4 about z, C3 about
     (1, 1, 1)) and commute with all translates of all rotated images. After
     closing under O there are 70999 strings, forming 4319 sign-consistent
     orbits.
   - **Alphabet orbits.** 4259 orbits use only the alphabet <X_x, Y_y, Z_z>,
     so the lemma applies to them.
   - **Outsider orbits.** The 60 others lie in exactly ten maximal commuting
     sets that contain a non-alphabet orbit:
     - eight valid 3-orbit rules, with log2 code dimension 48 at L = 4 and 72
       at L = 6, and no three-dimensionally mobile charge (companion note);
     - two sets of 43 and 47 orbits whose unions contain -1. For these,
       3L^3 - rank is 32 at L = 4 and 48 at L = 6, a lower bound for every
       valid sub-rule.
   - **Consequence.** In this class no rule has bounded code dimension
     together with a charge moved by free-variable-preserving operators.
     Fermionic or bosonic, no charge moves coherently.
3. **Unsoldered, C4/C3-fixed strings (exact within the search).** The
   valid maximal commuting sets with equal nonzero code dimension at L = 4
   and 6 are 36 rules.
   - All have log2 dimension 24: they are relabellings of the interleaved
     toric codes.
   - In each, exactly one same-site charge pattern moves by 2e_x, 2e_y and
     2e_z, and its T-junction sign is +1, a boson.
   - The nine largest maximal sets (383 orbits) are abelian self-commutant
     alphabets, so the lemma covers them.
4. **Statistics tool (validated).** The leg operators are found by GF(2)
   solving on an open box, and the sign is the product of their pairwise
   commutation signs.
   - It returns +1 for the 2D toric code's e and m, and -1 for e x m.
   - It returns +1 for the interleaved toric codes' vertex charge.

**Conclusion within these classes.** No coherently three-dimensionally
mobile fermion exists:
- soldered labels give no coherent mobility at all;
- unsoldered labels give only bosons.

The hypothesis that soldering enables fermions is not supported here.

## How this bears on the lane (interpretation, not a claim)

Across the four campaign notes, the simplest framework-covariant
constraint readings never produce a coherently mobile emergent fermion:
- one, two or three qubits per site;
- Pauli conditions on the nearest-neighbour star;
- symmetric generators.

Known constructions of emergent fermions in three dimensions use string
operators that need extra structure, such as a framing, an orientation or
larger supports. Whether some such structure can be made compatible with
the framework's site-centred cubic covariance is the natural next question.

## Independent check

A fresh-context agent (same model family) wrote its own code without reading
these scripts. It confirmed all three claims:
- **Lemma.** Confirmed by proof.
- **Soldered class.** It confirmed this with a pruned backtracking
  enumeration, cross-checked against brute force on random slices. It found
  exactly ten outsider sets: the eight 3-orbit sets are valid with no
  three-dimensionally mobile charge, and the 43- and 47-orbit sets contain
  -1 under any re-signing.
- **Unsoldered class.** It recomputed all 1233 maximal sets, finding exactly
  36 bounded ones. In each, its own statistics code found a one-dimensional
  space of three-dimensionally mobile same-site charges, a boson, stable
  under other legs and box sizes.
- **Wording.** It corrected one count, now fixed: 34927 counts the
  representative-fixed strings, and 70999 is the count after closing under O.

Files: `.claude/science/physics-loops/toe-campaign-20261017/c4_fermion_search/independent_check/`.

## Premises

- **Axioms used.** Lattice; Qubit read as three qubits per site, a declared
  enlargement.
- **Supplied model.** The stabilizer reading of nearest-neighbour
  conditions.
- **Declared choices.**
  - The search covers only strings fixed by some nontrivial rotation.
  - The unsoldered search keeps only C4/C3-fixed strings.
  - Exchange is tested only for same-site charge patterns and axis legs of
    length two.

## Relation to prior work

- The Levin–Wen hopping-operator statistics criterion is from PRB 67, 245316
  (2003).
- Fermionic point charges in 3D lattice models are known: Levin–Wen (2003),
  and the 3D bosonization of Chen and Kapustin, PRB 100, 245127 (2019),
  arXiv:1807.07081, whose map depends on a choice of spin structure. Those
  constructions use non-symmetric choices, for example framings or a
  branching structure.
- **New here.**
  - The exhaustive searches in the framework's covariance classes.
  - The alphabet lemma, in this form.

## No-Go Discipline Gate

- **N1 — routes around the claim.**
  - Strings with trivial stabilizer, a generic 64^7/24 family, are not
    searched.
  - Bounded rules that are not maximal commuting sets are not searched.
  - Composite charges spread over several sites, legs other than 2e_a, and
    larger supports are not tested.
  - Also outside: non-Pauli rules, other site structures and dynamics.
- **N2/N3 — scope.** Two finite classes and one statement each.
- **N4 — inputs.**
  - The soldered survivor set is stored in the loop pack. The runner
    re-verifies every element and recomputes the C4, C3 and edge-C2 parts.
    The axis-C2 part (64^5 strings, about 40 minutes) runs only in --full
    mode.
  - The unsoldered maximal-set survey is in the loop pack (1224 of 1233 sets
    evaluated directly; the remaining 9 are abelian alphabets). The runner
    re-checks the 36 bounded rules.
- **N5 — wording.** "No coherently mobile fermion" means no charge in these
  classes is both moved by free-variable-preserving operators in a rule of
  bounded code dimension and fermionic.
- **N6/N7 — strongest objection.** Known fermionic models need low-symmetry
  generators, which are excluded here. The negative result may say more
  about the symmetric restriction than about cubic covariance. That is the
  next target.
- **N8 — earlier claims.** Consistent with the companion notes.

## Verification

```bash
python3 scripts/three_axis_qubit_symmetric_stabilizer_rules_fermion_search_2026_10_17.py          # about 3 minutes
python3 scripts/three_axis_qubit_symmetric_stabilizer_rules_fermion_search_2026_10_17.py --full   # adds the axis-C2 enumeration
```

Expected: `TOTAL: PASS=8 FAIL=0` (and `PASS=9` with `--full`). Data and logs
are in `.claude/science/physics-loops/toe-campaign-20261017/c4_fermion_search/`.

## Load-bearing sources

- [Three-axis-qubit companion](THREE_AXIS_QUBIT_SITE_STABILIZER_RULES_UNSOLDERED_TORIC_CODES_MOVE_SOLDERED_MAXIMAL_RULES_DO_NOT_BOUNDED_THEOREM_NOTE_2026-10-17.md)
- [Two-qubit companion](TWO_QUBIT_SITE_SOLDERED_SPIN_STABILIZER_RULES_THREE_DIMENSIONAL_CHARGE_MOTION_FLIPS_A_FREE_LOCAL_VARIABLE_BOUNDED_THEOREM_NOTE_2026-10-17.md)
