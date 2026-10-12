---
claim_id: swapped_transverse_crosses_outside_the_matched_crosses_bounded_theorem_note_2026-10-10
claim_type: bounded_theorem
claim_scope: "On the proper orbit of (1, 2, 3), the transverse cross on pairs whose absolute transverse coordinates are swapped, at each absolute height 1, 2, and 3, extends by proper rotations to a soldered bond-symmetric kernel with values in {-1, 0, 1}. For a parameter of absolute value less than 1 the factors are strictly positive. Each record activates one direction and every slice sums to 0, so every neighbour product has mean 1. The 2026-09-22 converse makes each family order-blind. These three kernels and the six cap lines and the three matched transverse crosses are twelve linearly independent kernels. The sum of the matched and swapped kernels at height 3 keeps one live direction and slice sum 0. The sum of the swapped kernels at heights 1 and 2 has two-neighbour moment 23/24. No parameter is selected. Kernels outside these twelve are not classified."
upstream_dependencies:
  - minimal_axioms
  - order_blind_nearest_neighbour_formation_independence_beyond_neighbours_unsoldered_constancy_and_soldered_escape_bounded_theorem_note_2026-09-22
runner: scripts/swapped_transverse_crosses_outside_matched_crosses_2026_10_10.py
---

# Swapped transverse crosses lie outside the matched crosses

**Date:** 2026-10-10

**Type:** bounded_theorem

**Audit:** unset; independent audit remains a separate lane

**Status:** proposed_retained

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/swapped_transverse_crosses_outside_matched_crosses_2026_10_10.py`](../scripts/swapped_transverse_crosses_outside_matched_crosses_2026_10_10.py)

**Parents:** the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) and
[the order-blind formation note](ORDER_BLIND_NEAREST_NEIGHBOUR_FORMATION_INDEPENDENCE_BEYOND_NEIGHBOURS_UNSOLDERED_CONSTANCY_AND_SOLDERED_ESCAPE_BOUNDED_THEOREM_NOTE_2026-09-22.md).

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Three explicit soldered kernels meet the product-mean conditions and lie outside the six cap lines and the three matched transverse crosses."
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "Other generic orbits and higher-rank bond spaces are not classified."
source_of_blocker_text: frontier_question
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "Ask whether a soldered order-blind kernel on this orbit remains outside the six cap lines, the three matched transverse crosses, and the three swapped transverse crosses. Search first. A negative answer must name the ansatz."
conditional_surface_status: "one proper orbit of (1, 2, 3); uniform average; swapped transverse cross at absolute heights 1, 2, and 3; absolute parameter below 1"
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
mean equal to 1, and lies outside the span of the six cap lines and the
three matched transverse crosses.

**Conclusion.** Let `O` be the proper-cubic orbit of `(1, 2, 3)`. For
absolute height `m` and records `a = (x, y, z)`, `b = (x', y', z')`
define

`S_m(a, b) = sign(y x' - x y')`

when `z = -m`, `z' = m`, `|x| = |y'|` and `|y| = |x'|`, and
`S_m(a, b) = 0` otherwise. The cross product `x y' - y x'` is nonzero
on every such pair. For a proper rotation `g` with `g e_z` equal to a
direction `d`, set

`L^{(m)}_d(a, b) = S_m(g^{-1} a, g^{-1} b)`.

The value does not depend on the choice of `g`. It satisfies
`L^{(m)}_d(a, b) = L^{(m)}_{-d}(b, a)`, and it takes values in
`{-1, 0, 1}`. Thus

`phi^{(m)}_d(a, b) = 1 + t L^{(m)}_d(a, b)`

lies in `{1-t, 1, 1+t}`. For `|t| < 1` every factor is positive. Each
record activates exactly one direction. Every slice sums to 0, so every
neighbour product has mean 1. The parent converse makes each strictly
positive family order-blind on every window.

The matched transverse cross at the same height uses the sign of
`x y' - y x'` when `|x| = |x'|` and `|y| = |y'|`, and 0 otherwise. The
cap sign at level `k` is the sign of the product of the two coordinates
transverse to `d` when `a·d = k`, and 0 otherwise. The cap line is the
product of that sign on the left record with the sign on the right
record at `-d`. The six cap lines, the three matched crosses, and the
three swapped crosses are linearly independent. Each swapped kernel
therefore lies outside the span of the six cap lines and the three
matched crosses.

The witnesses are

`L^{(1)}(e_z, (-3, -2, -1), (-2, -3, 1)) = -1`,

`L^{(2)}(e_z, (-3, 1, -2), (1, -3, 2)) = -1`,

`L^{(3)}(e_z, (-2, -1, -3), (-1, -2, 3)) = -1`.

Each of those slices is orthogonal to the six cap signs and to the
matched cross at the same height and the same neighbour.

On height 3 the matched kernel and the swapped kernel are supported on
disjoint bonds. Their sum takes values in `{-1, 0, 1}`, activates one
direction on each record, and has slice sum 0, so it meets the same
product-mean hypotheses. The sum of the swapped kernels at heights 1
and 2 has

`E[(1 + L^{(1)}_{-e_x}(., (-2, -3, 1))) (1 + L^{(2)}_{-e_y}(., (-3, -1, 2)))] = 23/24`.

**Proof.** The runner enumerates the 24 proper rotations and the orbit.
Four rotations carry `e_z` to each direction, and they give one common
value of each `L^{(m)}`. Bond symmetry is the equality of the two
ordered kernels. A record that activated two directions, or none, would
fail the live count. For a fixed neighbour assignment, the product over
directions equals `1 + t L^{(m)}_d(a, b_d)` at the single live direction
of `a`. Summing over the records live on `d` is the full slice sum at
`b_d`, and that sum is 0. At half the parameter the factor values are
exactly `1/2`, `1`, and `3/2`.

Row reduction of the nine comparison vectors has rank 9. Adjoining any
one swapped kernel raises the rank to 10. The twelve vectors together
have rank 12. The matched formula reproduces the witness value `-1` on
the three bonds from `(-3, -2, -1)` to `(-3, 2, 1)`, from
`(-3, 1, -2)` to `(3, 1, 2)`, and from `(-2, -1, -3)` to `(-2, 1, 3)`.
The two-neighbour moment is the uniform average of the displayed
product, equal to `23/24`.

**Obligations.** Proved here: the swapped formulas, independence of the
transporting rotation, bond symmetry, the product means, positivity at
half the parameter, linear independence from the six cap lines and the
three matched crosses, the height-3 sum, and the cross-height moment.
Cited from the parent, and not re-proved: the converse that a
bond-symmetric family with these product means is order-blind on every
window. The strongest missing lemma is whether any soldered order-blind
kernel on this orbit remains outside these twelve kernels. This note
does not give that classification.

## What this does not do

- It does not select `t`.
- It does not claim that these twelve kernels are the whole order-blind
  set.
- It does not claim that a sum of swapped kernels at two heights is
  order-blind. The moment `23/24` says that two-neighbour normalisation
  fails.
- It does not treat a kernel supported on a positive cap `a·d = m`
  except through the cap lines already in the comparison.
- It does not cut the normalised bond space on the 48-point alphabet.
- It does not supply a formation site, probability, or rate.

## Runner

`scripts/swapped_transverse_crosses_outside_matched_crosses_2026_10_10.py`
repeats the group, the orbit, the three extensions, the product-mean
hypotheses, the rank, and the mixture moment.

## Imports

No formation site, probability, rate, or selected parameter is imported.
The proper rotations, the cap signs, and both transverse-cross formulas
are enumerated here. Order-blindness of a family that already meets the
product-mean conditions is the parent converse, quoted above.
