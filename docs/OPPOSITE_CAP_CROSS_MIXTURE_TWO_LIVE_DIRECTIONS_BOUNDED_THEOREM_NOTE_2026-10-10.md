---
claim_id: opposite_cap_cross_mixture_two_live_directions_bounded_theorem_note_2026-10-10
claim_type: bounded_theorem
claim_scope: "On the proper orbit of (1, 2, 3), the sum of the cap line at level +3 and the matched transverse cross on the caps a·d = -3 is bond-symmetric, takes values in {-1, 0, 1}, and activates two opposite directions on every record. Every slice sums to 0 and every opposite-direction neighbour product has mean 1. For absolute parameter below 1 the factors are positive, so the 2026-09-22 converse makes the family order-blind. The two supports are disjoint. The sum of the cap lines at levels +3 and -3 has two-neighbour moment 7/6. No parameter is selected. This mixture lies in the span of two cap-pair kernels. Kernels outside that span are not classified."
upstream_dependencies:
  - minimal_axioms
  - order_blind_nearest_neighbour_formation_independence_beyond_neighbours_unsoldered_constancy_and_soldered_escape_bounded_theorem_note_2026-09-22
runner: scripts/opposite_cap_cross_mixture_two_live_directions_2026_10_10.py
---

# An opposite cap and cross stay order-blind together

**Date:** 2026-10-10

**Type:** bounded_theorem

**Audit:** unset; independent audit remains a separate lane

**Status:** proposed_retained

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/opposite_cap_cross_mixture_two_live_directions_2026_10_10.py`](../scripts/opposite_cap_cross_mixture_two_live_directions_2026_10_10.py)

**Parents:** the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) and
[the order-blind formation note](ORDER_BLIND_NEAREST_NEIGHBOUR_FORMATION_INDEPENDENCE_BEYOND_NEIGHBOURS_UNSOLDERED_CONSTANCY_AND_SOLDERED_ESCAPE_BOUNDED_THEOREM_NOTE_2026-09-22.md).

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "One explicit sum of a cap line and an opposite matched cross has two live directions and product mean 1."
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "Other generic orbits and higher-rank bond spaces are not classified."
source_of_blocker_text: frontier_question
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "Ask whether a soldered order-blind kernel on this orbit lies outside the eighteen cap-pair kernels. Search first. A negative answer must name the ansatz."
conditional_surface_status: "one proper orbit of (1, 2, 3); sum of the level-+3 cap and the matched cross on a·d = -3; uniform average; absolute parameter below 1"
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
properties is order-blind on every window." It leaves the sentence
"Other generic orbits and higher-rank bond spaces are not classified."

## Theorem

**Target.** On the proper orbit of `(1, 2, 3)`, exhibit a soldered
bond-symmetric kernel that activates two directions on a record and
still has neighbour-product mean 1.

**Conclusion.** Let the cap sign at level `k` be the sign of the product
of the two coordinates transverse to `d` when `a·d = k`, and 0 otherwise.
The cap line is the product of that sign on the left record with the
sign on the right record at `-d`. The matched cross of orientation `-1`
and height 3 is `sign(x y' - y x')` when `z = -3`, `z' = 3`,
`|x| = |x'|` and `|y| = |y'|`, and 0 otherwise, transported by a proper
rotation carrying `e_z` to the direction. Let `S` be the sum of the cap
line at level `+3` and that matched cross.

`S` is bond-symmetric and takes values in `{-1, 0, 1}`. The two
summands are supported on disjoint bonds. Every record activates exactly
two directions, and those directions are opposites. The seed `(1, 2, 3)`
is live in `e_z` and `-e_z`. Every slice sums to 0. For every direction
`d` and every pair of neighbour records, the uniform average of
`(1 + S_d)(1 + S_{-d})` equals 1. Thus

`phi_d(a, b) = 1 + t S_d(a, b)`

has every opposite-direction product of mean 1, and for `|t| < 1` every
factor is positive. The parent converse makes the family order-blind on
every window.

The sum of the cap lines at levels `+3` and `-3`, evaluated on `e_x` and
`-e_x` at the neighbour `(-3, -2, -1)`, has mean `7/6`.

**Proof.** The runner enumerates the 24 proper rotations and the orbit.
Bond symmetry and the value set are checked on every bond. A record with
a live-direction count other than 2, or with a live direction that is
not the opposite of the other, fails the live check. The slice sums are
the full sums over the orbit. The opposite-direction moments are the
uniform averages over all 24 records, all six directions, and all pairs
of neighbour records. At half the parameter the factor values are `1/2`,
`1`, and `3/2`. The cap moment is the same average on the named bonds,
equal to `7/6`.

**Obligations.** Proved here: this one sum, its two live directions, the
product means, positivity at half the parameter, and the cap moment
`7/6`. Cited from the parent, and not re-proved: the converse. The
strongest missing lemma is whether any soldered order-blind kernel lies
outside the span of the cap-pair kernels. This sum does not. It is the
sum of one cap line and one matched cross.

## What this does not do

- It does not select `t`.
- It does not claim that `S` lies outside the cap-pair span.
- It does not claim that every sum of two cap-pair kernels is
  order-blind. The moment `7/6` is a sum that fails.
- It does not classify kernels supported off the cap pairs.
- It does not cut the normalised bond space on the 48-point alphabet.
- It does not supply a formation site, probability, or rate.

## Runner

`scripts/opposite_cap_cross_mixture_two_live_directions_2026_10_10.py`
repeats the group, the orbit, the live directions, the product means,
and the cap moment.

## Imports

No formation site, probability, rate, or selected parameter is imported.
The proper rotations, the cap signs, and the matched cross are enumerated
here. Order-blindness of a family that already meets the product-mean
conditions is the parent converse, quoted above.
