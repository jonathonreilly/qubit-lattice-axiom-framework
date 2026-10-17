---
claim_id: one_qubit_cubic_covariant_nearest_neighbour_stabilizer_rules_have_no_three_dimensionally_mobile_defect_bounded_theorem_note_2026-10-17
claim_type: bounded_theorem
claim_scope: "Supplied reading: a nearest-neighbour rule is a set of signed Pauli strings on the seven-site star of a site of Z^3 (one qubit per site), closed under the proper cubic group O acting on positions and on Pauli labels by one of the four soldering-menu actions; its translates generate an abelian stabilizer group not containing -1. Exact (finite enumeration of all 4^7 - 1 strings, and Groebner bases over GF(2)): under the axis and full actions the only such rule is Chamon's octahedral stabilizer X(+-x) Y(+-y) Z(+-z) up to an overall sign, with identity at the centre (both signs are valid on Z^3; on L^3 tori with odd relations, e.g. L = 6, only +1 is consistent). Its charge module is R/I with I the intersection of four primes, curves along the four body diagonals, so no excitation is mobile in three dimensions, a single defect cannot be translated (fracton), and the mobile classes move only within planes orthogonal to a body diagonal. Under the trivial and sign actions every rule is single-label (all creating and moving operators of one label commute, so exchange is trivial) or a single cluster-type orbit (every defect created by one single-site Pauli). Hence no rule in this class has a point excitation that both moves in three dimensions and has fermionic exchange. Not claimed: non-Pauli commuting projectors, frustrated or non-commuting rules, several qubits per site, block rules, any dynamics or tick, or any physical identification."
upstream_dependencies:
  - minimal_axioms
runner: scripts/cubic_covariant_nearest_neighbour_stabilizer_rules_one_qubit_defects_2026_10_17.py
---

# One-qubit cubic-covariant nearest-neighbour stabilizer rules have no defect that moves in three dimensions

**Date:** 2026-10-17
**Type:** bounded_theorem
**Status:** bounded support, unaudited. The classification and module
statements are exact; the stabilizer reading of Admissibility is a supplied
model, not axiom content. Nothing is adopted.

## Question

The previous campaign found that one qubit per site cannot carry a moving,
cubic-covariant free tick. One possible way out is that an electron is not a
free walker but an excitation of many local conditions, a defect of the
Admissibility rule. This note asks the simplest version of that question.

Take the hard-support reading of Admissibility. The rule's support at each
site is fixed by commuting Pauli conditions on the site and its six
neighbours. Can such a rule have point defects that move in three dimensions
and are fermions?

## Result

1. **Classification (exact).** Enumerate every signed Pauli string on the
   star, its O-orbit under each soldering action, sign consistency, and
   commutation with all translates. Then form every maximal commuting union
   of orbits.

   | action on Pauli labels | rules |
   |---|---|
   | axis, full (labels turn with space) | exactly one: Chamon's octahedron X(+-x) Y(+-y) Z(+-z), identity at the centre |
   | trivial, sign twist | single-label rules (one Pauli label throughout), or one cluster-type orbit (label P at the centre, Q != P on all six neighbours) |

   The Chamon rule is determined up to an overall sign. On Z^3 both signs
   are valid rules, because translates of one generator per site satisfy no
   finite relation. On a torus the sign can matter: at L = 6 every relation
   has odd size, so only +1 is consistent.

   Under the axis and full actions no Pauli label at the centre is
   O-invariant. So no soldered rule constrains a site through its own
   label: every soldered condition acts on the neighbour shell.
2. **The soldered rule has fracton defects (exact).** For the Chamon rule
   the syndromes of X and Z at a site are y + 1/y + z + 1/z and
   x + 1/x + y + 1/y over GF(2). The charge module is R/I, with R the
   Laurent ring F2[x, y, z] and
   I = ((y+z)(1+yz), (x+y)(1+xy), (x+z)(1+xz)). The runner proves:
   - I is the intersection of the four primes (yz+1, x+y), (yz+1, x+z),
     (xz+1, y+z) and (y+z, x+z). These are curves along the four body
     diagonals; none contains a monomial.
   - No charge is mobile in three dimensions: (I : x+1) = (I : y+1) =
     (I : z+1) = I.
   - A single defect cannot be moved by any nonzero translation (checked
     for every t in {-2,...,2}^3, and true for all t, since x^t + 1 would
     have to vanish on all four curves).
   - Charges supported on one curve are planons. For the curve
     (s, s, 1/s) they move by t exactly when t is orthogonal to (1, 1, -1).
3. **The unsoldered rules have no mobile fermion (exact).**
   - In a single-label rule, every operator that creates or moves a defect
     can be taken of one other label. Those operators commute, so the
     Levin–Wen hopping commutator is +1 and exchange is trivial.
   - In a cluster-type rule, the single-site Pauli Q at a site flips only
     the generator centred there. Every defect is local and carries no
     topological charge; the rule has a unique ground state.
4. **Tori (exact, finite).** On L^3 tori with L = 4 and 6, the Chamon rule
   has log2 code dimension 4L, the type-I fracton growth, and no product of
   generators equals -1 or +-i.

So, in this class, a point excitation that moves in three dimensions and has
fermionic exchange does not exist. With spin turning with space, no point
excitation moves in three dimensions at all.

## Relation to the free-tick results

The October 2026 tick notes found that a cubic-covariant one-qubit free tick
is frozen at the ranges where it is accepted. The soldered spinor then
appears only on reducible coins or on blocks. This note finds the same
pattern for defects of the simplest constraint reading. With one qubit per
site and soldered labels:
- the free walker does not move;
- the constraint defects move at most in planes.

In both cases the obstruction is that the cubic group leaves too little room
on one qubit. This is an analogy between two separate theorems, not a single
theorem.

## Premises

- **Axioms used.** Lattice (Z^3, nearest-neighbour adjacency, proper cubic
  rotations) and Qubit (M_2(C) per site).
- **Supplied model.** The hard-support stabilizer reading of
  Admissibility. The rule's support at a site is the +1 eigenspace of
  commuting Pauli conditions on the star, generated covariantly. The axiom
  states a nearest-neighbour conditional probability law for record
  formation; reading its support as a quantum stabilizer constraint is a
  declared model.
- **Declared choices.** The four soldering-menu actions, Pauli (not general
  projector) conditions, and star support.

## Proof notes

- **Classification.** This is finite: 4^7 - 1 strings, 24 group elements and
  translates within distance two. Sign consistency means no element maps a
  string to its negative. Commutation is checked against every translate
  whose support overlaps. Maximal commuting unions are found by a
  Bron–Kerbosch search over the compatibility graph: 63 orbits and 9
  maximal sets under the trivial action, 43 and 5 under the sign twist.
- **Fracton statement.** If I = P1 ∩ ... ∩ P4 with P_i prime and m the
  maximal ideal at (1, 1, 1), then (I : m) = ∩ (P_i : m) = I, since m is
  contained in no P_i. The runner verifies the intersection and each colon
  ideal directly with GF(2) Groebner bases. Over GF(2) this is the exact
  arithmetic of the Pauli binary symplectic representation; there is no
  characteristic-zero lift to certify.
- **Exchange in single-label rules.** The Levin–Wen T-junction invariant
  does not depend on the choice of hopping operators. Choosing them of one
  label makes every commutator +1.

## Relation to prior work

- **Chamon's model** (C. Chamon, PRL 94, 040402 (2005)) and its analysis by
  Bravyi, Leemhuis and Terhal (Ann. Phys. 326, 839 (2011)) are standard. So
  are its four-foliated fracton order and emergent fermionic gauge theory
  (W. Shirley, X. Liu and A. Dua, PRB 107, 035136 (2023), arXiv:2206.12791). The fracton and planon
  statements in item 2 recover known properties with the framework's
  conventions.
- **Polynomial formalism.** Haah, Commun. Math. Phys. 324, 351 (2013).
- **Cluster states.** Briegel and Raussendorf, PRL 86, 910 (2001).
- **New here, within the stated class.**
  - Under the framework's soldered cubic covariance with nearest-neighbour
    support and one qubit per site, Chamon's stabilizer is the only Pauli
    rule. The unsoldered actions give only classical or cluster-type rules.
  - So the simplest constraint reading of a neighbourhood electron has no
    three-dimensionally mobile fermionic defect.

We found no published classification of this form. The search covered Haah's
classification programme and the sorting of three-dimensional topological
stabilizer models by Dua, Kim, Cheng and Williamson (PRB 100, 155137 (2019)).

## No-Go Discipline Gate

- **N1 — routes around the claim.**
  - The claim covers only Pauli stabilizer conditions on the seven-site star,
    with one qubit per site and the four menu actions.
  - These are not excluded: general commuting projectors, frustrated
    Hamiltonians, energetics with perturbations, several qubits per site,
    rules on staggered blocks, non-star supports, and any dynamics.
  - Planons of the Chamon rule are mobile in planes, and their statistics are
    not computed here.
- **N2/N3 — scope.** One class and one statement: no point excitation that
  is both three-dimensionally mobile and fermionic.
- **N4 — inputs.** Only the declared model and the menu actions.
- **N5 — wording.** "No defect that moves in three dimensions" refers to
  the stabilizer charge module. Energetics or other dynamics are not
  considered.
- **N6/N7 — strongest objection.** Admissibility is a probability law for
  record formation, not a stabilizer Hamiltonian, so the reading may be the
  wrong one. Mitigation: the reading is declared, and the result is stated
  only for it.
- **N8 — earlier claims.** None changed. This is consistent with the
  repository's supplied Gauss-defect model, whose T-junction sign is +1.

## Independent check

A fresh-context agent (same model family) wrote its own implementation
without reading these scripts. It confirmed every claim:
- **Signs.** It built explicit SU(2) lifts and conjugated actual Pauli
  matrices.
- **Classification.** It enumerated all orbits; pairwise commutation of
  orbits is exhaustive for unions.
- **Fracton and planon statements.** It used exact "not in I" certificates
  by restricting to the four curves. Separately, GF(2) linear algebra on open
  boxes up to [-12, 12]^3 found explicit moving operators where mobility
  holds and none where it fails.
- **Radical decomposition.** A Singular computation in the Laurent ring
  confirmed it.
- **Tori.** Explicit phases throughout.

It corrected one statement: the overall sign of the Chamon rule is not fixed
on Z^3. The fix is in item 1. Scripts:
`.claude/science/physics-loops/toe-campaign-20261017/c1_stabilizer_rules/independent_check/`.

## Verification

```bash
python3 scripts/cubic_covariant_nearest_neighbour_stabilizer_rules_one_qubit_defects_2026_10_17.py
```

Expected: `TOTAL: PASS=20 FAIL=0` (about a minute). Working files are in
`.claude/science/physics-loops/toe-campaign-20261017/`.

## Load-bearing sources

- [Axioms](MINIMAL_AXIOMS_2026-06-29.md)
- [Soldering menu](THE_SOLDERING_MENU_FOUR_ACTIONS_OF_THE_PROPER_CUBIC_ROTATIONS_ON_QUBIT_POSSIBILITIES_AND_WHAT_EACH_LETS_FORMATION_BUILD_BOUNDED_THEOREM_NOTE_2026-09-22.md)
- [Companion free-tick note](CUBIC_COVARIANCE_FREEZES_A_ONE_QUBIT_TICK_CELL_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-10-16.md)
