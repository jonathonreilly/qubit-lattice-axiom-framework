---
claim_id: transverse_cross_kernel_outside_six_caps_bounded_theorem_note_2026-10-10
claim_type: bounded_theorem
claim_scope: "On the proper orbit of (1, 2, 3), the transverse cross product on the pair of caps a·e_z = -3 and b·e_z = 3, kept only when the transverse absolute values match in index order, extends by proper rotations to a soldered bond-symmetric kernel with values in {-1, 0, 1}. For a parameter of absolute value less than 1 the factors are strictly positive. Each record activates one direction and every slice sums to 0, so every neighbour product has mean 1. The 2026-09-22 converse makes the family order-blind. The slice at neighbour (-2, 1, 3) is nonzero and orthogonal to all six cap signs a·d in {±1, ±2, ±3}, so it lies outside their span. No parameter is selected. The rest of the order-blind set is not classified."
upstream_dependencies:
  - minimal_axioms
  - order_blind_nearest_neighbour_formation_independence_beyond_neighbours_unsoldered_constancy_and_soldered_escape_bounded_theorem_note_2026-09-22
runner: scripts/transverse_cross_kernel_outside_six_caps_2026_10_10.py
---

# A transverse-cross slice lies outside the six cap signs

**Date:** 2026-10-10

**Type:** bounded_theorem

**Audit:** unset; independent audit remains a separate lane

**Status:** proposed_retained

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/transverse_cross_kernel_outside_six_caps_2026_10_10.py`](../scripts/transverse_cross_kernel_outside_six_caps_2026_10_10.py)

**Parents:** the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) and
[the order-blind formation note](ORDER_BLIND_NEAREST_NEIGHBOUR_FORMATION_INDEPENDENCE_BEYOND_NEIGHBOURS_UNSOLDERED_CONSTANCY_AND_SOLDERED_ESCAPE_BOUNDED_THEOREM_NOTE_2026-09-22.md).

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "One explicit soldered kernel meets the product-mean conditions and has a slice orthogonal to every cap sign."
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "Other generic orbits and higher-rank bond spaces are not classified."
source_of_blocker_text: frontier_question
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "Count soldered bond-symmetric factors on the 48-point chiral pair. Do not repeat the existence of the pair."
conditional_surface_status: "one proper orbit of (1, 2, 3); uniform average; transverse-cross kernel on modulus 3; absolute parameter below 1"
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

**Target.** On the proper orbit of `(1, 2, 3)`, some soldered
bond-symmetric factor is strictly positive, has every neighbour-product
mean equal to 1, and has a centre slice outside the span of the six cap
signs.

**Conclusion.** Let `O` be the proper-cubic orbit of `(1, 2, 3)`. For
records `a = (x, y, z)` and `b = (x', y', z')` define

`R(a, b) = sign(x y' - y x')`

when `z = -3`, `z' = 3`, `|x| = |x'|` and `|y| = |y'|`, and `R(a, b) = 0`
otherwise. The cross product in that sign is nonzero whenever the
absolute values match. For a proper rotation `g` with `g e_z` equal to a
direction `d`, set

`K_d(a, b) = R(g^{-1} a, g^{-1} b)`.

The value does not depend on the choice of `g`. It satisfies
`K_d(a, b) = K_{-d}(b, a)`, and it takes values in `{-1, 0, 1}`. Thus

`phi_d(a, b) = 1 + t K_d(a, b)`

lies in `{1-t, 1, 1+t}`. For `|t| < 1` every factor is positive. Each
record activates exactly one direction. Every slice sums to 0, so every
neighbour product has mean 1. The slice at direction `e_z` and neighbour
`(-2, 1, 3)` is nonzero and orthogonal to each cap sign `a·e_z = k` for
`k` in `{±1, ±2, ±3}`. It is therefore outside their span. The parent
converse makes the strictly positive family order-blind on every window.

**Proof.** The runner enumerates the 24 proper rotations and the orbit.
Four rotations carry `e_z` to each direction, and they give one common
value of `K`. Bond symmetry is the equality of the two ordered kernels.
A record that activated two directions, or none, would fail the live
count. For a fixed neighbour assignment, the product over directions
equals `1 + t K_d(a, b_d)` at the single live direction of `a`. Summing
over the records live on `d` is the full slice sum at `b_d`, because the
kernel vanishes off that set, and that sum is 0. The witness bond has
value `-1`. If the witness slice were a linear combination of the six
cap signs, its inner product with itself would vanish, so the slice
would be 0. At half the parameter the factor values are exactly `1/2`,
`1`, and `3/2`.

**Obligations.** Proved here: the coordinate formula, independence of
the transporting rotation, bond symmetry, the product means, positivity
at half the parameter, and the witness slice. Cited from the parent,
and not re-proved: the converse that a bond-symmetric family with these
product means is order-blind on every window. The strongest missing
lemma is a description of every other soldered order-blind kernel on
this orbit. This note does not give one.

## What this does not do

- It does not select `t`.
- It does not claim that this kernel and the cap lines are the whole
  order-blind set.
- It does not compute the dimension of the slice space.
- It does not treat the 48-point chiral pair or any other alphabet.
- It does not supply a formation site, probability, or rate.

## Runner

`scripts/transverse_cross_kernel_outside_six_caps_2026_10_10.py`
repeats the group, the orbit, the extension, the product-mean
hypotheses, and the witness slice.

## Imports

No formation site, probability, rate, or selected parameter is imported.
The proper rotations and the transverse-cross values are enumerated
here. Order-blindness of a family that already meets the product-mean
conditions is the parent converse, quoted above.
