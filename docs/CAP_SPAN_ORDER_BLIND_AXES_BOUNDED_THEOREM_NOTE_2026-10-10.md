---
claim_id: cap_span_order_blind_axes_bounded_theorem_note_2026-10-10
claim_type: bounded_theorem
claim_scope: "On the proper orbit of (1, 2, 3), let each direction carry a linear combination of the three cap signs, the sign of the transverse coordinate product on a·d = m for m in {1, 2, 3}. The product factor 1 + t v_d(a) v_{-d}(b) has every neighbour-product mean equal to 1 for some t other than 0 exactly when v uses one modulus. Those three axes are the order-blind members of this span. A two-modulus witness has moment 13/12. The integer mixture (-2, -2, 1), whose pairwise moments cancel, has three-neighbour moment -3. Factors outside the span are not classified."
upstream_dependencies:
  - minimal_axioms
  - order_blind_nearest_neighbour_formation_independence_beyond_neighbours_unsoldered_constancy_and_soldered_escape_bounded_theorem_note_2026-09-22
runner: scripts/cap_span_order_blind_axes_2026_10_10.py
---

# Only the three axes are order-blind inside the cap span

**Date:** 2026-10-10

**Type:** bounded_theorem

**Audit:** unset; independent audit remains a separate lane

**Status:** proposed_retained

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/cap_span_order_blind_axes_2026_10_10.py`](../scripts/cap_span_order_blind_axes_2026_10_10.py)

**Parents:** the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) and
[the order-blind formation note](ORDER_BLIND_NEAREST_NEIGHBOUR_FORMATION_INDEPENDENCE_BEYOND_NEIGHBOURS_UNSOLDERED_CONSTANCY_AND_SOLDERED_ESCAPE_BOUNDED_THEOREM_NOTE_2026-09-22.md).

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Inside one three-dimensional span, the product-mean identity holds off t = 0 only on the three axes."
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "Other generic orbits and higher-rank bond spaces are not classified."
source_of_blocker_text: frontier_question
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "Ask whether a soldered order-blind factor on this orbit can sit outside the three-cap span."
conditional_surface_status: "one proper orbit of (1, 2, 3); uniform average; factors in the span of the three cap signs"
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

The parent converse: "Conversely every family with these properties is
order-blind on every window." The same note leaves "Other generic orbits
and higher-rank bond spaces are not classified."

## Theorem

**Target.** Inside the span of the three cap signs on the orbit of
`(1, 2, 3)`, the product-mean identity holds for a nonzero scale exactly
on the three axes.

**Conclusion.** Let `C_{m,d}` be the sign of the transverse coordinate
product when `a·d = m`, and 0 otherwise. For weights `y = (y_1, y_2, y_3)`
set `v_d(a) = y_1 C_{1,d}(a) + y_2 C_{2,d}(a) + y_3 C_{3,d}(a)` and

`phi_d(a, b) = 1 + t v_d(a) v_{-d}(b)`.

On the three positive axes the perpendicular cap correlations are 0 on
equal moduli and `1/24` off that diagonal, and

`E[v_x v_y v_z] = y_1 y_2 y_3 / 8`.

Each opposite cap has a point of sign `+1`, so a neighbour value can equal
any single weight. If two or three weights are nonzero, some
neighbour pattern has product mean different from 1 for every `t` other
than 0. If only one weight is nonzero, every product mean equals 1. The
parent converse makes those three axes order-blind on every window when
the factors are strictly positive.

**Proof.** The caps on one direction are disjoint and each has mean 0, so
a single-modulus `v` makes every product a single factor of mean 1. If
`y_3 = 0` and `y_1 y_2` is nonzero, the same correlations give
`E[v_x v_y] = y_1 y_2 / 12`. Neighbour values `y_1` and `y_2` are attained,
and the two-neighbour excess is `t^2` times a nonzero rational. The
witness `y = (1, 1, 0)` with neighbour values `1, 1` has moment `13/12`.
If all three weights are nonzero, then either some pair has nonzero
correlation, and that two-neighbour pattern has excess proportional to
`t^2`, or every pair correlation vanishes. In the second branch the
three-neighbour excess on the positive axes is `t^3` times
`y_1 y_2 y_3 / 8` times the neighbour values. The witness
`y = (-2, -2, 1)` with neighbour values `-2, -2, -2` has moment `-3`,
so the pairwise cancellation does not restore the mean.

**Obligations.** Proved here: the correlations, the two witness moments,
and the case split above. Cited and not re-proved: the parent converse.
The strongest missing lemma is a soldered order-blind factor on this
orbit whose bond values are not a combination of the three cap signs.

## What this does not do

- It does not select a weight or a scale.
- It does not classify factors outside this span.
- It does not treat the 48-point chiral pair or any other alphabet.
- It does not supply a formation site, probability, or rate.

## Runner

`scripts/cap_span_order_blind_axes_2026_10_10.py` repeats the correlations
and the two witness moments.

## Imports

No formation site, probability, rate, or selected parameter is imported.
The proper rotations and the cap signs are enumerated here. Order-blindness
of a family that already meets the product-mean conditions is the parent
converse, quoted above.
