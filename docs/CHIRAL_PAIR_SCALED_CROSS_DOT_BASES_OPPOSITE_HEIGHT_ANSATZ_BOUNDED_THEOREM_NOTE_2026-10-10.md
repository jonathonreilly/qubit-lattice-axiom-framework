---
claim_id: chiral_pair_scaled_cross_dot_bases_opposite_height_ansatz_bounded_theorem_note_2026-10-10
claim_type: bounded_theorem
claim_scope: "On the 48 signed permutations of (1, 2, 3), the scaled cross-dot kernel at each absolute height 1, 2, and 3 is bond-symmetric and soldered. On opposite caps of that height it is twice the sign of the negative product of the transverse cross and the transverse dot when the absolute transverse coordinates match and that dot product is positive, and it is that sign when the absolute transverse coordinates are swapped and the dot product is nonzero. It is 0 when either transverse product vanishes, and when the coordinates match and the dot product is negative. The values lie in {-2, -1, 0, 1, 2}. The product with the parallel-dot kernel is 0, and so is the product with the orthogonal swapped cross. Each record meets at most one live direction and every left slice sums to 0, so at coefficient 1/4 the factor is strictly positive and every neighbour product has mean 1. The values are 1/2, 3/4, 1, 5/4, and 3/2. Every far-end sum equals 48. At each height four bonds with weights +1, +1, -1, and -1 have alternating sum 0 on all twenty-seven comparison kernels and alternating sum 4 on this kernel. Inside the 10-dimensional opposite-height ansatz the nine earlier kernels have rank 9, and this kernel raises the rank to 10. Those ten kernels are a basis of that ansatz. The order-blind subset of the span is not classified. The 300-dimensional affine space is not classified. No scale is selected."
upstream_dependencies:
  - minimal_axioms
  - order_blind_nearest_neighbour_formation_independence_beyond_neighbours_unsoldered_constancy_and_soldered_escape_bounded_theorem_note_2026-09-22
  - chiral_pair_bond_factor_dimension_bounded_theorem_note_2026-10-10
runner: scripts/chiral_pair_scaled_cross_dot_bases_opposite_height_ansatz_2026_10_10.py
---

# A scaled cross-dot kernel bases the opposite-height ansatz

**Date:** 2026-10-10

**Type:** bounded_theorem

**Audit:** unset; independent audit remains a separate lane

**Status:** proposed_retained

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/chiral_pair_scaled_cross_dot_bases_opposite_height_ansatz_2026_10_10.py`](../scripts/chiral_pair_scaled_cross_dot_bases_opposite_height_ansatz_2026_10_10.py)

**Parents:** the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md),
[the order-blind formation note](ORDER_BLIND_NEAREST_NEIGHBOUR_FORMATION_INDEPENDENCE_BEYOND_NEIGHBOURS_UNSOLDERED_CONSTANCY_AND_SOLDERED_ESCAPE_BOUNDED_THEOREM_NOTE_2026-09-22.md),
and the [chiral-pair bond note](CHIRAL_PAIR_BOND_FACTOR_DIMENSION_BOUNDED_THEOREM_NOTE_2026-10-10.md).

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Each scaled cross-dot kernel at coefficient 1/4 is strictly positive and has neighbour-product mean 1, and with the nine earlier kernels it bases the 10-dimensional opposite-height ansatz."
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "Other generic orbits and higher-rank bond spaces are not classified."
source_of_blocker_text: frontier_question
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "Decide which rational mixtures of these ten basis kernels have every neighbour-product mean equal to 1. Do not claim that order-blind subset is classified. Do not claim the 300-dimensional affine space is classified."
conditional_surface_status: "48 signed permutations of (1, 2, 3); scaled cross-dot kernel at absolute heights 1, 2, and 3; coefficient 1/4"
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

**Target.** On the 48 signed permutations of `(1, 2, 3)`, name a basis
of the 10-dimensional slice-zero bond-symmetric soldered kernels on one
opposite-height pair.

**Ansatz.** Fix an absolute height `h` and a direction `d`. The support
is the set of bonds with `a·d = h` and `b·d = -h`. A kernel in this
ansatz is soldered under proper rotations, unchanged by reversing the
bond, and has every left slice equal to 0. That space is 10-dimensional.
Transport uses any proper `g` with `g e_z = d`. On `e_z` let
`c = x y' - y x'` and `delta = x x' + y y'`. The scaled seed is 0 when
`z` is not `h`, `z'` is not `-h`, `c = 0`, or `delta = 0`. Otherwise
let `epsilon` be the sign of `-c delta`. If the absolute transverse
coordinates match and `delta` is positive, the seed is `2 epsilon`. If
the absolute transverse coordinates are swapped, the seed is `epsilon`.
If the coordinates match and `delta` is negative, the seed is 0. The
family is `phi_d(a, b) = 1 + (1/4) M_d(a, b)`. The same formula at the
other two heights is a separate kernel. A mixed-height bond is not in
this ansatz. A sum across heights is not in this ansatz. The
300-dimensional affine space is not classified.

**Conclusion.** Each of the three kernels is bond-symmetric and soldered,
with values in `{-2, -1, 0, 1, 2}`. A quarter-turn about `z` preserves
the seed, and every proper frame gives the same value. The product with
the parallel-dot kernel is 0, and so is the product with the orthogonal
swapped cross. Each record meets at most one live direction. Every left
slice sums to 0. At coefficient `1/4` the values are `1/2`, `3/4`, `1`,
`5/4`, and `3/2`. Every neighbour product has mean 1, and every far-end
sum equals 48, so the quotient by 48 lies in the normalised space. The
parent converse makes each family order-blind on every window. On `e_z`,
with weights `+1`, `+1`, `-1`, and `-1`, the bonds

```text
height 1: (-3, -2, 1) -> (-3, 2, -1), (-3, -2, 1) -> (3, -2, -1),
          (-3, 2, 1) -> (-3, -2, -1), (-3, 2, 1) -> (3, 2, -1)
height 2: (-3, -1, 2) -> (-3, 1, -2), (-3, -1, 2) -> (3, -1, -2),
          (-3, 1, 2) -> (-3, -1, -2), (-3, 1, 2) -> (3, 1, -2)
height 3: (-2, -1, 3) -> (-2, 1, -3), (-2, -1, 3) -> (2, -1, -3),
          (-2, 1, 3) -> (-2, -1, -3), (-2, 1, 3) -> (2, 1, -3)
```

have active rows

```text
(1, -1, -1, -1, 0, 0, -1, 0, 0, 2)
(1, -1, -1, 1, 0, 0, 1, 0, 0, 0)
(1, -1, -1, 1, 0, 0, -1, 0, 0, -2)
(1, -1, -1, -1, 0, 0, 1, 0, 0, 0)
```

in the order chirality cap, transverse-sign cap, sign product, matched
cross, swapped cross, parallel dot, matched oblique dot, swapped dot,
orthogonal swapped cross, and this kernel. Every kernel from another
height is 0. The alternating sum is 0 on the first nine columns and
equals 4 on this kernel. The bond from `(1, 2, 3)` to itself has all of
these kernels equal to 0. None of the three scaled kernels is a rational
linear combination of the twenty-seven, and none of the three factors is
a linear combination of those twenty-seven factors.

On each opposite-height pair the 64 bonds form 16 orbits under the
quarter-turn about `z`. Bond symmetry together with the left-slice sums
has rank 6, so the ansatz is 10-dimensional. The five same-height
kernels, the three dot kernels, and the orthogonal swapped cross span
rank 9. The scaled cross-dot kernel lies in the ansatz and raises the
rank to 10. Those ten kernels are a basis of the ansatz.

**Proof.** The runner enumerates the proper rotations and the alphabet.
All four frames of each direction agree, and direct comparison gives
soldered covariance. Reversing a bond leaves the value unchanged. The
parallel-dot seed requires the transverse cross product to vanish, and
this seed requires it to be nonzero. The orthogonal swapped cross
requires the transverse dot product to vanish, and this seed requires it
to be nonzero. The two products are therefore 0. Each record has one
coordinate of each modulus, so only one direction meets `a·d = h`. The
runner finds at most one live direction, values in `{-2, -1, 0, 1, 2}`,
and a zero left slice. For a fixed neighbour condition, at most one
factor differs from 1. The product equals `1 + (1/4) M_d(a, b)` when the
condition uses that live direction, and equals 1 otherwise. Summing over
the centre, the live terms are a left slice, which is 0. The mean is 1.
The far-end sum is the same cancellation on the right.

The four stated rows are the values on those bonds. Their alternating
sum vanishes on the nine active kernels and equals 4 on this kernel.
Every kernel from another height vanishes because `a·e_z` is the active
height. Every linear combination of the twenty-seven therefore has
alternating sum 0. A linear combination of the twenty-seven factors that
matched one scaled factor would be 1 on the idle bond, hence would have
coefficients summing to 1, and would then reproduce that kernel. The
alternating sum forbids it.

The dimension count is row reduction over the rationals on the 16 orbit
coordinates. The nine earlier kernels meet the bond-symmetry and slice
equations and have rank 9. The scaled vector meets the same equations
and raises the rank to 10. Ten independent vectors in a 10-dimensional
space are a basis.

**Obligations.** Proved here: soldered covariance, frame invariance,
bond symmetry, the two vanishing products, the live-direction bound, the
left slices, the product means, the five factor values, the far-end
sums, the three separations, and the ranks 9 and 10 inside the
10-dimensional ansatz. Cited from Theorem 2, and not re-proved: bond
symmetry together with every product mean equal to 1 makes the family
order-blind on every window. Cited from the chiral-pair bond note, and
not re-proved: far-end sum 1 is the normalisation of that bond space.
The twenty-seven kernels are comparison tensors. The strongest missing
lemma is which rational mixtures of the ten basis kernels have every
neighbour-product mean equal to 1.

## What this does not do

- It does not select a scale. The coefficient `1/4` is a witness.
- It does not classify the order-blind subset of the span.
- It does not claim that the 300-dimensional affine space is classified.
- It does not re-derive the order-blindness of the twenty-seven comparison kernels.
- It does not repeat the bond-space dimension count.
- It does not return to the modulus-3 triple.
- It does not put a mixed-height bond, or a sum across heights, inside
  the ansatz.
- It does not supply a formation site, probability, or rate.

## Runner

`scripts/chiral_pair_scaled_cross_dot_bases_opposite_height_ansatz_2026_10_10.py`
repeats the covariance comparison, the slice sums, the three
separations, and the orbit rank. `TOTAL: PASS=10 FAIL=0`.

## Imports

No formation site, probability, rate, or selected scale is imported.
The proper rotations, the scaled cross-dot seeds, and the slice sums are
enumerated here. Theorem 2's converse is applied to each family. The
chiral-pair bond note supplies the meaning of far-end sum 1.
