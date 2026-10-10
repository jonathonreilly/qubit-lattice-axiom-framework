---
claim_id: three_cap_order_blind_lines_on_one_orbit_bounded_theorem_note_2026-10-10
claim_type: bounded_theorem
claim_scope: "On the proper-cubic orbit of (1, 2, 3), the sign of the transverse coordinate product on the cap a·d = m, for each m in {1, 2, 3}, defines a soldered bond-symmetric line. For a parameter of absolute value less than 1 the factors are strictly positive, and every one of the 729 neighbour-cap patterns has product mean 1. The 2026-09-22 converse then makes each line order-blind on every window. The modulus-3 line is the exhibited line. The modulus-1 and modulus-2 lines are distinct from it and from each other. A mixture of the modulus-3 and modulus-2 lines has a two-neighbour moment 25/24. No parameter is selected, and the rest of the order-blind set is not classified."
upstream_dependencies:
  - minimal_axioms
  - order_blind_nearest_neighbour_formation_independence_beyond_neighbours_unsoldered_constancy_and_soldered_escape_bounded_theorem_note_2026-09-22
runner: scripts/three_cap_order_blind_lines_2026_10_10.py
---

# Three cap lines stay order-blind on one (1, 2, 3) orbit

**Date:** 2026-10-10

**Type:** bounded_theorem

**Audit:** unset; independent audit remains a separate lane

**Status:** proposed_retained

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/three_cap_order_blind_lines_2026_10_10.py`](../scripts/three_cap_order_blind_lines_2026_10_10.py)

**Parents:** the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) and
[the order-blind formation note](ORDER_BLIND_NEAREST_NEIGHBOUR_FORMATION_INDEPENDENCE_BEYOND_NEIGHBOURS_UNSOLDERED_CONSTANCY_AND_SOLDERED_ESCAPE_BOUNDED_THEOREM_NOTE_2026-09-22.md).

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Three explicit soldered lines meet the product-mean conditions, and one mixture misses a two-neighbour moment."
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "Other generic orbits and higher-rank bond spaces are not classified."
source_of_blocker_text: frontier_question
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "Ask whether every soldered order-blind factor on this orbit is one of these three lines."
conditional_surface_status: "one proper orbit of (1, 2, 3); uniform one-site law; cap sign formula; absolute parameter below 1"
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

The parent note's converse: "Conversely every family with these
properties is order-blind on every window." Its exhibited line uses "the
sign of the product of the two coordinates of a transverse to d when
a.d = 3, and 0 otherwise." It leaves the sentence "Other generic orbits
and higher-rank bond spaces are not classified."

## Theorem

**Target.** On the proper orbit of `(1, 2, 3)`, each cap `a·d = m` for
`m` in `{1, 2, 3}` carries a strictly positive soldered bond-symmetric
line that the parent converse makes order-blind, and a mixture of the
modulus-3 and modulus-2 lines misses normalisation.

**Conclusion.** Let `O` be the proper-cubic orbit of `(1, 2, 3)`. For a
direction `d` and a modulus `m` in `{1, 2, 3}`, let `C_{m,d}(a)` be the
sign of the product of the two coordinates transverse to `d` when
`a·d = m`, and 0 otherwise. The transverse axes are taken in increasing
coordinate index. Then

`phi_{m,d}(a, b) = 1 + t C_{m,d}(a) C_{m,-d}(b)`

is unchanged by proper rotations and satisfies
`phi_{m,d}(a, b) = phi_{m,-d}(b, a)`, because the two cap values are
multiplied and integer multiplication commutes. For `|t| < 1` every
factor lies in `{1-t, 1, 1+t}` and is positive. Each cap has 4 points,
mean 0, and activates only one direction at each record. Every one of
the 729 patterns of neighbour weights in `{-1, 0, 1}` therefore has
product mean 1. The parent converse makes each of the three lines
order-blind on every window. The three caps are distinct. The modulus-3
line is the exhibited line. Some two-neighbour condition of the
modulus-3 plus modulus-2 mixture has moment `25/24`.

**Proof.** The runner enumerates the 24 proper rotations and the orbit.
Covariance is the equality of the moved and unmoved cap products.
Quarter-turns about a fixed direction, the trace-1 rotations, flip the
cap sign, and at least one such pair is present, so the alternation
check is not empty. Mean 0 and one hot direction make a pure product
equal to a single factor, whose mean is 1. The mixture moment is the
average of two pure factors on distinct directions. An independent
expansion gives the same `25/24`: if the cap correlation sums to 1 and
the neighbour weight is 1, the cross term is `1/24`.

**Obligations.** Proved here: the three cap formulas, their covariance,
the product means, positivity at half the parameter, and the mixture
moment. Cited from the parent, and not re-proved: the converse that a
bond-symmetric family with these product means is order-blind on every
window. The strongest missing lemma is whether any soldered order-blind
factor on this orbit lies off these three lines.

## What this does not do

- It does not select `t`, or any other factor.
- It does not classify the rest of the order-blind set.
- It does not claim that the linear bond space of dimension 84 is
  order-blind. The mixture witness is a point of that shape whose
  two-neighbour moment is not 1.
- It does not treat the 48-point chiral pair or any other alphabet.
- It does not supply a formation site, probability, or rate.

## Runner

`scripts/three_cap_order_blind_lines_2026_10_10.py` repeats the group,
the orbit, the three caps, the product means, and the mixture moment.

## Imports

No formation site, probability, rate, or selected parameter is imported.
The proper rotations are enumerated here. Order-blindness of a family
that already meets the product-mean conditions is the parent converse,
quoted above.
