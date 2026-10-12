---
claim_id: chiral_pair_swapped_transverse_dot_outside_twenty_one_kernels_bounded_theorem_note_2026-10-10
claim_type: bounded_theorem
claim_scope: "On the 48 signed permutations of (1, 2, 3), the swapped transverse-dot sign at each absolute height 1, 2, and 3 is bond-symmetric and soldered. It is nonzero only when both endpoints lie on opposite caps of that height, the absolute transverse coordinates are swapped, and the transverse dot product is nonzero, and then it is the sign of the negative transverse dot product. Its support is disjoint from the parallel transverse-dot kernel and from the matched oblique dot. The values lie in {-1, 0, 1}. Each record meets at most one live direction and every left slice sums to 0, so at coefficient 1/2 the factor is strictly positive and every neighbour product has mean 1. Every far-end sum equals 48. At each height two bonds agree on all fifteen comparison kernels, the parallel and matched-oblique dots vanish, and the swapped-dot values differ by 2, so none of the three kernels is a linear combination of those twenty-one. Inside the 10-dimensional opposite-height ansatz the seven earlier kernels have rank 7, and this kernel raises the rank to 8. Two dimensions remain unnamed. The 300-dimensional affine space is not classified. No scale is selected."
upstream_dependencies:
  - minimal_axioms
  - order_blind_nearest_neighbour_formation_independence_beyond_neighbours_unsoldered_constancy_and_soldered_escape_bounded_theorem_note_2026-09-22
  - chiral_pair_bond_factor_dimension_bounded_theorem_note_2026-10-10
runner: scripts/chiral_pair_swapped_transverse_dot_outside_twenty_one_kernels_2026_10_10.py
---

# Swapped transverse dots on the chiral pair lie off twenty-one kernels

**Date:** 2026-10-10

**Type:** bounded_theorem

**Audit:** unset; independent audit remains a separate lane

**Status:** proposed_retained

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/chiral_pair_swapped_transverse_dot_outside_twenty_one_kernels_2026_10_10.py`](../scripts/chiral_pair_swapped_transverse_dot_outside_twenty_one_kernels_2026_10_10.py)

**Parents:** the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md),
[the order-blind formation note](ORDER_BLIND_NEAREST_NEIGHBOUR_FORMATION_INDEPENDENCE_BEYOND_NEIGHBOURS_UNSOLDERED_CONSTANCY_AND_SOLDERED_ESCAPE_BOUNDED_THEOREM_NOTE_2026-09-22.md),
and the [chiral-pair bond note](CHIRAL_PAIR_BOND_FACTOR_DIMENSION_BOUNDED_THEOREM_NOTE_2026-10-10.md).

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Each swapped transverse-dot kernel at coefficient 1/2 is strictly positive and has neighbour-product mean 1, and two bonds at each height separate it from the twenty-one kernels."
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "Other generic orbits and higher-rank bond spaces are not classified."
source_of_blocker_text: frontier_question
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "Exhibit a fourth kernel in the remaining 2-dimensional complement of one opposite-height pair, with an exact formula, outside the eight kernels now exhibited there. Do not claim that complement is based. Do not claim the 300-dimensional affine space is classified."
conditional_surface_status: "48 signed permutations of (1, 2, 3); swapped transverse-dot sign at absolute heights 1, 2, and 3; coefficient 1/2"
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

Theorem 2 of the parent: "with phi_d(a, b) = phi_-d(b, a) and
E_r0[prod_{(d, b) in N} phi_d(., b)] = 1 for every N. Conversely every
family with these properties is order-blind on every window." The parent
leaves the sentence "Other generic orbits and higher-rank bond spaces
are not classified."

## Theorem

**Target.** On the 48 signed permutations of `(1, 2, 3)`, decide whether
a strictly positive order-blind factor lies outside the span of the
fifteen kernels, the three parallel transverse-dot kernels, and the
three matched oblique dots.

**Ansatz.** Fix an absolute height `h` and a direction `d`. The support
is the set of bonds with `a·d = h` and `b·d = -h`. A kernel in this
ansatz is soldered under proper rotations, unchanged by reversing the
bond, and has every left slice equal to 0. That space is 10-dimensional.
Transport uses any proper `g` with `g e_z = d`. On `e_z` the swapped
seed is 0 unless `z = h`, `z' = -h`, the absolute transverse coordinates
are swapped, and the transverse dot product `x x' + y y'` is nonzero.
The seed is then the sign of the negative of that dot product. The
family is `phi_d(a, b) = 1 + (1/2) M_d(a, b)`. The same formula at the
other two heights is a separate kernel. A mixed-height bond is not in
this ansatz. A sum across heights is not in this ansatz. Two dimensions
of the complement remain unnamed. The 300-dimensional affine space is
not classified.

**Conclusion.** Each of the three kernels is bond-symmetric and soldered,
with values in `{-1, 0, 1}`. A quarter-turn about `z` preserves the
seed, and every proper frame gives the same value. The product of this
kernel with the parallel transverse-dot kernel is 0, and so is its
product with the matched oblique dot. Each record meets at most one live
direction. Every left slice sums to 0. At coefficient `1/2` the values
are `1/2`, `1`, and `3/2`. Every neighbour product has mean 1, and every
far-end sum equals 48, so the quotient by 48 lies in the normalised
space. The parent converse makes each family order-blind on every
window. On `e_z` the two bonds

```text
height 1: (-3, -2, 1) -> (-2, -3, -1) and (-3, 2, 1) -> (2, -3, -1)
height 2: (-3, -1, 2) -> (-1, -3, -2) and (-3, 1, 2) -> (1, -3, -2)
height 3: (-2, -1, 3) -> (-1, -2, -3) and (-2, 1, 3) -> (1, -2, -3)
```

agree on all fifteen comparison kernels. At the active height those
kernels read `(1, 1, 1, 0, 1)`, and every kernel from another height is
0. All three parallel-dot kernels and all three matched oblique dots
vanish on both bonds. The swapped-dot kernel reads `-1` on the first
bond and `+1` on the second. The bond from `(1, 2, 3)` to itself has
all of these kernels equal to 0. None of the three swapped-dot kernels
is a rational linear combination of the twenty-one, and none of the
three factors is a linear combination of those twenty-one factors.

On each opposite-height pair the 64 bonds form 16 orbits under the
quarter-turn about `z`. Bond symmetry together with the left-slice sums
has rank 6, so the ansatz is 10-dimensional. The five same-height
kernels, the parallel-dot kernel, and the matched oblique dot span rank
7. The swapped-dot kernel lies in the ansatz and raises the rank to 8.

**Proof.** The runner enumerates the proper rotations and the alphabet.
All four frames of each direction agree, and direct comparison gives
soldered covariance. Reversing a bond leaves the value unchanged. The
parallel-dot seed requires the transverse cross product to vanish, while
a swapped pair of unequal transverse moduli has nonzero cross product.
The matched oblique seed requires the absolute transverse coordinates to
match, and this seed requires them to be swapped. The two products are
therefore 0. Each record has one coordinate of each modulus, so only one
direction meets `a·d = h`. The runner finds at most one live direction,
values in `{-1, 0, 1}`, and a zero left slice. For a fixed neighbour
condition, at most one factor differs from 1. The product equals
`1 + (1/2) M_d(a, b)` when the condition uses that live direction, and
equals 1 otherwise. Summing over the centre, the live terms are a left
slice, which is 0. The mean is 1. The far-end sum is the same
cancellation on the right.

The two bonds at one height have the same fifteen comparison values, and
every parallel-dot kernel and every matched oblique dot vanishes on
both, so every linear combination of those twenty-one agrees on the two
bonds. The swapped-dot values differ by 2. A linear combination of the
twenty-one factors that matched one swapped-dot factor would be 1 on
the idle bond, hence would have coefficients summing to 1, and would
then reproduce that kernel. The two bonds forbid it.

The dimension count is row reduction over the rationals on the 16 orbit
coordinates. The seven earlier kernels meet the bond-symmetry and slice
equations and have rank 7. The swapped-dot vector meets the same
equations and raises the rank to 8.

**Obligations.** Proved here: soldered covariance, frame invariance,
bond symmetry, disjoint support from the parallel-dot kernel and from
the matched oblique dot, the live-direction bound, the left slices, the
product means, the three factor values, the far-end sums, the three
separations, and the ranks 7 and 8 inside the 10-dimensional ansatz.
Cited from Theorem 2, and not re-proved: bond symmetry together with
every product mean equal to 1 makes the family order-blind on every
window. Cited from the chiral-pair bond note, and not re-proved:
far-end sum 1 is the normalisation of that bond space. The twenty-one
kernels are comparison tensors. The strongest missing lemma is an exact
formula for a fourth vector in the remaining 2-dimensional complement.

## What this does not do

- It does not select a scale. The coefficient `1/2` is a witness.
- It does not classify the order-blind subset.
- It does not claim that the 300-dimensional affine space is classified.
- It does not base the remaining 2-dimensional complement.
- It does not re-derive the order-blindness of the twenty-one comparison kernels.
- It does not repeat the bond-space dimension count.
- It does not return to the modulus-3 triple.
- It does not put a mixed-height bond, or a sum across heights, inside
  the ansatz.
- It does not supply a formation site, probability, or rate.

## Runner

`scripts/chiral_pair_swapped_transverse_dot_outside_twenty_one_kernels_2026_10_10.py`
repeats the covariance comparison, the slice sums, the three
separations, and the orbit rank. `TOTAL: PASS=10 FAIL=0`.

## Imports

No formation site, probability, rate, or selected scale is imported.
The proper rotations, the swapped-dot seeds, and the slice sums are
enumerated here. Theorem 2's converse is applied to each family. The
chiral-pair bond note supplies the meaning of far-end sum 1.
