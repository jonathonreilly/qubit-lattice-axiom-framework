---
claim_id: one_orbit_bond_factor_dimension_bounded_theorem_note_2026-10-10
claim_type: bounded_theorem
claim_scope: "On one proper-cubic orbit of the record (1, 2, 3), there are 24 points and the stabilizer is trivial. A bond factor assigns a rational to a direction and two records, transforms by the soldered action, and is unchanged by reversing the bond. That space has dimension 84. Sixty orbits have 24 images and 24 orbits have 12. No bond equals its reverse. Forgetting reversal gives 144 ordered orbits. Summing over the far end of a bond gives six independent rows, each totaling 24, so the factors with far-end sum 1 form an affine space of dimension 78. No factor is selected. The 48-point chiral pair and the other generic orbits stay unclassified."
upstream_dependencies:
  - minimal_axioms
  - order_blind_nearest_neighbour_formation_independence_beyond_neighbours_unsoldered_constancy_and_soldered_escape_bounded_theorem_note_2026-09-22
runner: scripts/one_orbit_bond_factor_dimension_2026_10_10.py
---

# One (1, 2, 3) orbit has a 78-dimensional normalised bond space

**Date:** 2026-10-10

**Type:** bounded_theorem

**Audit:** unset; independent audit remains a separate lane

**Status:** proposed_retained

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/one_orbit_bond_factor_dimension_2026_10_10.py`](../scripts/one_orbit_bond_factor_dimension_2026_10_10.py)

**Parents:** the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) supply the
proper cubic rotations. The orbit and the open sentence are in
[the order-blind formation note](ORDER_BLIND_NEAREST_NEIGHBOUR_FORMATION_INDEPENDENCE_BEYOND_NEIGHBOURS_UNSOLDERED_CONSTANCY_AND_SOLDERED_ESCAPE_BOUNDED_THEOREM_NOTE_2026-09-22.md):
other generic orbits and higher-rank bond spaces are not classified. This
note classifies the linear bond space on the single 24-point orbit only.

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact orbit count of soldered bond-symmetric factors and the rank of their far-end sums."
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "Other generic orbits and higher-rank bond spaces are not classified."
source_of_blocker_text: frontier_question
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "Ask whether order-blindness on the 7-site cross cuts the 78-dimensional family to one line."
conditional_surface_status: "one proper orbit of (1, 2, 3); soldered action; bond reversal"
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Theorem

**Target.** On the proper-cubic orbit of `(1, 2, 3)`, the soldered
bond-symmetric rational factors have dimension 84, and those whose
far-end sum equals 1 form an affine space of dimension 78.

**Conclusion.** Let `O` be the proper-cubic orbit of `(1, 2, 3)`. It has
24 points and trivial stabilizer. The axis swap `(2, 1, 3)` lies in the
other proper orbit. A bond is a triple `(direction, left, right)`, with
the direction one of the six axis steps. Reversal replaces it by
`(-direction, right, left)`. No bond equals its reverse. Soldered
covariance and reversal identify an 84-dimensional space of rational bond
factors. Sixty of those orbits have 24 images and 24 have 12. Dropping
reversal leaves 144 ordered orbits. The six far-end sums, one for each
orbit of `(direction, left)`, are independent and each totals 24 on the
constant factor. The factors whose far-end sum is 1 therefore form an
affine space of dimension 78.

**Proof.** The runner enumerates the 24 proper rotations, the orbit, and
the orbits of bonds. It also counts six orbits of a direction together
with one record. The normalisation rank is exact row reduction over the
rationals. Each of those six rows sums to 24, so the constant factor
`1/24` meets every far-end equation. The solution space therefore has
dimension `84 - 6 = 78`. A one-dimensional stand-in fails the dimension
check.

**Obligations.** Proved in this note: the proper group, the orbit and
its stabilizer, the exclusion of the axis swap, the bond-orbit count,
the image-size split, the ordered count, the six direction-record
orbits, and the rank of their far-end rows. The 2026-09-22 note is used
only for the open sentence that higher-rank bond spaces were not
classified. It is not used as a proof that any exhibited family is the
whole space. The strongest missing lemma is whether order-blindness on
the 7-site cross, or strict positivity, cuts this affine space to one
line. The 48-point chiral pair and every other alphabet stay outside
the count.

**Imports.** No formation site, probability, rate, or selected factor
is imported. The proper rotations are enumerated here as the
determinant-+1 signed permutation matrices. The open sentence is quoted
from the parent note named above.

## What this does not do

- It does not select a factor, a value of `kappa`, or a formation law.
- It does not show that order-blindness or strict positivity cuts the
  dimension to 1.
- It does not classify the 48-point chiral pair or any other alphabet.
- It does not supply a formation site, probability, or rate.
- It does not identify a bond factor with a mass density or an action.

## Runner

`scripts/one_orbit_bond_factor_dimension_2026_10_10.py` repeats the group,
the orbit, the six direction-record orbits, the bond count, the
image-size split, the ordered count, and the normalisation rank.
