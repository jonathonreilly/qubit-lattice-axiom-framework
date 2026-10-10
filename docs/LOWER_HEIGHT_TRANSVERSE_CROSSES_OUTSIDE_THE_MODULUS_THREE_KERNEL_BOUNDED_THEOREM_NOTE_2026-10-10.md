---
claim_id: lower_height_transverse_crosses_outside_the_modulus_three_kernel_bounded_theorem_note_2026-10-10
claim_type: bounded_theorem
claim_scope: "On the proper orbit of (1, 2, 3), the transverse-cross formula at absolute heights 1 and 2 each extends by proper rotations to a soldered bond-symmetric kernel with values in {-1, 0, 1}. For a parameter of absolute value less than 1 the factors are strictly positive. Each record activates one direction and every slice sums to 0, so every neighbour product has mean 1. The 2026-09-22 converse makes each family order-blind. The six cap lines and the three transverse-cross kernels are nine linearly independent kernels, so each lower-height kernel lies outside the span of the six cap lines and the modulus-3 transverse cross. The sum of the height-1 and height-2 kernels has two-neighbour moment 23/24. No parameter is selected. Kernels outside these nine are not classified."
upstream_dependencies:
  - minimal_axioms
  - order_blind_nearest_neighbour_formation_independence_beyond_neighbours_unsoldered_constancy_and_soldered_escape_bounded_theorem_note_2026-09-22
runner: scripts/lower_height_transverse_crosses_outside_modulus_three_2026_10_10.py
---

# Lower-height transverse crosses lie outside the modulus-3 kernel

**Date:** 2026-10-10

**Type:** bounded_theorem

**Audit:** unset; independent audit remains a separate lane

**Status:** proposed_retained

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/lower_height_transverse_crosses_outside_modulus_three_2026_10_10.py`](../scripts/lower_height_transverse_crosses_outside_modulus_three_2026_10_10.py)

**Parents:** the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) and
[the order-blind formation note](ORDER_BLIND_NEAREST_NEIGHBOUR_FORMATION_INDEPENDENCE_BEYOND_NEIGHBOURS_UNSOLDERED_CONSTANCY_AND_SOLDERED_ESCAPE_BOUNDED_THEOREM_NOTE_2026-09-22.md).

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Two explicit soldered kernels meet the product-mean conditions and lie outside the six cap lines and the modulus-3 transverse cross."
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "Other generic orbits and higher-rank bond spaces are not classified."
source_of_blocker_text: frontier_question
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "Ask whether a soldered order-blind kernel on this orbit remains outside the six cap lines and the three transverse-cross kernels. Search first. A negative answer must name the ansatz."
conditional_surface_status: "one proper orbit of (1, 2, 3); uniform average; transverse-cross formula at absolute heights 1 and 2; absolute parameter below 1"
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
mean equal to 1, and lies outside the span of the six cap lines together
with the modulus-3 transverse cross.

**Conclusion.** Let `O` be the proper-cubic orbit of `(1, 2, 3)`. For
absolute height `m` and records `a = (x, y, z)`, `b = (x', y', z')`
define

`R_m(a, b) = sign(x y' - y x')`

when `z = -m`, `z' = m`, `|x| = |x'|` and `|y| = |y'|`, and
`R_m(a, b) = 0` otherwise. For `m` in `{1, 2}` the cross product is
nonzero whenever the absolute values match. For a proper rotation `g`
with `g e_z` equal to a direction `d`, set

`K^{(m)}_d(a, b) = R_m(g^{-1} a, g^{-1} b)`.

The value does not depend on the choice of `g`. It satisfies
`K^{(m)}_d(a, b) = K^{(m)}_{-d}(b, a)`, and it takes values in
`{-1, 0, 1}`. Thus

`phi^{(m)}_d(a, b) = 1 + t K^{(m)}_d(a, b)`

lies in `{1-t, 1, 1+t}`. For `|t| < 1` every factor is positive. Each
record activates exactly one direction. Every slice sums to 0, so every
neighbour product has mean 1. The parent converse makes each strictly
positive family order-blind on every window.

The cap sign at level `k` is the sign of the product of the two
coordinates transverse to `d` when `a·d = k`, and 0 otherwise. The cap
line at that level is the product of the sign on the left record with
the sign on the right record at `-d`. The same transverse-cross formula
at height 3 supplies the comparison kernel. These six cap lines and the
three kernels `K^{(1)}`, `K^{(2)}`, and `K^{(3)}` are linearly
independent. Each of `K^{(1)}` and `K^{(2)}` therefore lies outside the
span of the six cap lines and `K^{(3)}`.

The witnesses are

`K^{(1)}(e_z, (-3, -2, -1), (-3, 2, 1)) = -1`,

`K^{(2)}(e_z, (-3, 1, -2), (3, 1, 2)) = -1`.

Each of those slices is orthogonal to the six cap signs and to the
height-3 slice at the same neighbour. The sum
`S = K^{(1)} + K^{(2)}` has

`E[(1 + S_{-e_x}(., (-2, -1, -3))) (1 + S_{-e_y}(., (-2, -1, -3)))] = 23/24`.

**Proof.** The runner enumerates the 24 proper rotations and the orbit.
Four rotations carry `e_z` to each direction, and they give one common
value of each `K^{(m)}`. Bond symmetry is the equality of the two
ordered kernels. A record that activated two directions, or none, would
fail the live count. For a fixed neighbour assignment, the product over
directions equals `1 + t K^{(m)}_d(a, b_d)` at the single live direction
of `a`. Summing over the records live on `d` is the full slice sum at
`b_d`, and that sum is 0. At half the parameter the factor values are
exactly `1/2`, `1`, and `3/2`.

Row reduction of the nine bond vectors has rank 9. The seven vectors of
the cap lines and `K^{(3)}` have rank 7, and adjoining either lower-height
kernel raises the rank to 8. A kernel in the span of those seven would
not raise the rank. The comparison kernel reproduces the height-3 witness
value `-1` on the bond from `(-2, -1, -3)` to `(-2, 1, 3)`, so the
comparison is that transverse cross. The two-neighbour moment is the
uniform average of the displayed product, equal to `23/24`.

**Obligations.** Proved here: the coordinate formulas at heights 1 and 2,
independence of the transporting rotation, bond symmetry, the product
means, positivity at half the parameter, linear independence from the six
cap lines and the height-3 transverse cross, and the mixture moment.
Cited from the parent, and not re-proved: the converse that a
bond-symmetric family with these product means is order-blind on every
window. The strongest missing lemma is whether any soldered order-blind
kernel on this orbit remains outside the six cap lines and these three
transverse crosses. This note does not give that classification.

## What this does not do

- It does not select `t`.
- It does not claim that the six cap lines and the three transverse
  crosses are the whole order-blind set.
- It does not claim that `S` is order-blind. The moment `23/24` says the
  two-neighbour normalisation fails for this sum.
- It does not treat a kernel whose live directions overlap, or a coupling
  of unequal absolute heights, except for that one sum.
- It does not cut the normalised bond space on the 48-point alphabet.
- It does not supply a formation site, probability, or rate.

## Runner

`scripts/lower_height_transverse_crosses_outside_modulus_three_2026_10_10.py`
repeats the group, the orbit, the two extensions, the product-mean
hypotheses, the rank, and the mixture moment.

## Imports

No formation site, probability, rate, or selected parameter is imported.
The proper rotations, the cap signs, and the transverse-cross values are
enumerated here. Order-blindness of a family that already meets the
product-mean conditions is the parent converse, quoted above.
