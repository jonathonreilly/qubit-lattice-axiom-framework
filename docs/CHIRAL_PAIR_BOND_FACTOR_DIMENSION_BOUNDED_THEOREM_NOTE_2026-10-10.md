---
claim_id: chiral_pair_bond_factor_dimension_bounded_theorem_note_2026-10-10
claim_type: bounded_theorem
claim_scope: "The 48 signed permutations of (1, 2, 3) split into two proper-cubic orbits of 24. A bond factor assigns a rational to a direction and two records, transforms by the soldered proper action, and is unchanged by reversing the bond. That space has dimension 312. 264 orbits have 24 images and 48 orbits have 12. No bond equals its reverse. Forgetting reversal gives 576 ordered orbits. Twelve orbits of a direction and one record give twelve independent far-end rows, each totaling 48, so the factors with far-end sum 1 form an affine space of dimension 300. No factor is selected. Order-blindness on this alphabet is not classified."
upstream_dependencies:
  - minimal_axioms
  - order_blind_nearest_neighbour_formation_independence_beyond_neighbours_unsoldered_constancy_and_soldered_escape_bounded_theorem_note_2026-09-22
runner: scripts/chiral_pair_bond_factor_dimension_2026_10_10.py
---

# The 48-point chiral pair has a 300-dimensional normalised bond space

**Date:** 2026-10-10

**Type:** bounded_theorem

**Audit:** unset; independent audit remains a separate lane

**Status:** proposed_retained

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/chiral_pair_bond_factor_dimension_2026_10_10.py`](../scripts/chiral_pair_bond_factor_dimension_2026_10_10.py)

**Parents:** the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) supply the
proper cubic rotations. The open sentence is in
[the order-blind formation note](ORDER_BLIND_NEAREST_NEIGHBOUR_FORMATION_INDEPENDENCE_BEYOND_NEIGHBOURS_UNSOLDERED_CONSTANCY_AND_SOLDERED_ESCAPE_BOUNDED_THEOREM_NOTE_2026-09-22.md):
other generic orbits and higher-rank bond spaces are not classified. This
note counts the linear bond space on the 48 signed permutations of
`(1, 2, 3)` only.

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact orbit count of soldered bond-symmetric factors on the 48-point alphabet and the rank of their far-end sums."
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "Other generic orbits and higher-rank bond spaces are not classified."
source_of_blocker_text: frontier_question
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "Ask whether any soldered order-blind kernel on the 24-point orbit remains outside the cap lines and the transverse-cross kernel."
conditional_surface_status: "48 signed permutations of (1, 2, 3); soldered proper action; bond reversal"
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Quoted premises

Lattice: "Physical sites are the points of the cubic lattice `Z^3`, with
nearest-neighbor adjacency, standard translations, and proper cubic
rotations about each site."

Admissibility: "There is one fixed nearest-neighbor admissibility rule,
covariant under lattice translations and proper cubic rotations."

Reading note (2), interpretive: "Read with Record, the distribution
concerns which possibility a forming record locks, conditional on
formation at that site; it does not supply the formation site,
probability, or rate."

The parent note leaves the sentence "Other generic orbits and
higher-rank bond spaces are not classified."

## Theorem

**Target.** On the 48 signed permutations of `(1, 2, 3)`, the soldered
bond-symmetric rational factors have dimension 312, and those whose
far-end sum equals 1 form an affine space of dimension 300.

**Conclusion.** Let `A` be the set of signed permutations of `(1, 2, 3)`.
It has 48 points. The proper-cubic orbit of `(1, 2, 3)` has 24 points,
and the complement in `A` is the other proper orbit, also of 24 points.
The axis swap `(2, 1, 3)` lies in that complement. A bond is a triple
`(direction, left, right)`, with the direction one of the six axis
steps and both records in `A`. Reversal replaces it by
`(-direction, right, left)`. No bond equals its reverse. Soldered
covariance and reversal identify a 312-dimensional space of rational
bond factors. 264 of those orbits have 24 images and 48 have 12.
Dropping reversal leaves 576 ordered orbits. The twelve far-end sums,
one for each orbit of `(direction, left)`, are independent and each
totals 48 on the constant factor. The factors whose far-end sum is 1
therefore form an affine space of dimension 300.

**Proof.** The runner enumerates the 24 proper rotations, the 48
records, and the orbits of bonds. It also counts twelve orbits of a
direction together with one record. The normalisation rank is exact
row reduction over the rationals. Each of those twelve rows sums to
48, so the constant factor `1/48` meets every far-end equation. The
solution space therefore has dimension `312 - 12 = 300`. A
one-dimensional stand-in fails the dimension check.

**Obligations.** Proved in this note: the proper group, the 48-point
alphabet, its split into two proper orbits, the bond-orbit count, the
image-size split, the ordered count, the twelve direction-record
orbits, and the rank of their far-end rows. The 2026-09-22 note is
used only for the open sentence. It is not used as a proof of any
exhibited family. The strongest missing lemma is whether
order-blindness cuts this affine space. No factor is selected.

## What this does not do

- It does not select a factor or a value of `kappa`.
- It does not show that order-blindness or strict positivity cuts the
  dimension.
- It does not classify any other alphabet.
- It does not supply a formation site, probability, or rate.
- It does not identify a bond factor with a mass density or an action.

## Runner

`scripts/chiral_pair_bond_factor_dimension_2026_10_10.py` repeats the
group, the alphabet, the twelve direction-record orbits, the bond
count, the image-size split, the ordered count, and the normalisation
rank.

## Imports

No formation site, probability, rate, or selected factor is imported.
The proper rotations and the signed permutations are enumerated here.
The open sentence is quoted from the parent note named above.
