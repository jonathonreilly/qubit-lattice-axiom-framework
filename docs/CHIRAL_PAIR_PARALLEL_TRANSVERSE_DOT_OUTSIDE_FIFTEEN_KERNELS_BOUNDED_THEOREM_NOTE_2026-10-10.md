---
claim_id: chiral_pair_parallel_transverse_dot_outside_fifteen_kernels_bounded_theorem_note_2026-10-10
claim_type: bounded_theorem
claim_scope: "On the 48 signed permutations of (1, 2, 3), the parallel transverse-dot sign at each absolute height 1, 2, and 3 is bond-symmetric and soldered. It is nonzero only when both endpoints lie on opposite caps of that height and the transverse cross product vanishes, and then it is the sign of the negative transverse dot product. The values lie in {-1, 0, 1}. Each record meets at most one live direction and every left slice sums to 0, so at coefficient 1/2 the factor is strictly positive and every neighbour product has mean 1. Every far-end sum equals 48. At each height the bonds from a fixed left record to the two parallel right records agree on all fifteen comparison kernels and differ by 2 on this kernel, so none of the three kernels is a linear combination of the fifteen. On each opposite-height pair the quarter-turn orbits are 16, and bond symmetry together with the left-slice sums has rank 6, so the soldered bond-symmetric slice-zero kernels on that pair are 10-dimensional. The five same-height kernels span 5 of those dimensions. The parallel-dot kernel raises the rank to 6. The complement is not based. The 300-dimensional affine space is not classified. No scale is selected."
upstream_dependencies:
  - minimal_axioms
  - order_blind_nearest_neighbour_formation_independence_beyond_neighbours_unsoldered_constancy_and_soldered_escape_bounded_theorem_note_2026-09-22
  - chiral_pair_bond_factor_dimension_bounded_theorem_note_2026-10-10
runner: scripts/chiral_pair_parallel_transverse_dot_outside_fifteen_kernels_2026_10_10.py
---

# Parallel transverse dots on the chiral pair lie off fifteen kernels

**Date:** 2026-10-10

**Type:** bounded_theorem

**Audit:** unset; independent audit remains a separate lane

**Status:** proposed_retained

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/chiral_pair_parallel_transverse_dot_outside_fifteen_kernels_2026_10_10.py`](../scripts/chiral_pair_parallel_transverse_dot_outside_fifteen_kernels_2026_10_10.py)

**Parents:** the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md),
[the order-blind formation note](ORDER_BLIND_NEAREST_NEIGHBOUR_FORMATION_INDEPENDENCE_BEYOND_NEIGHBOURS_UNSOLDERED_CONSTANCY_AND_SOLDERED_ESCAPE_BOUNDED_THEOREM_NOTE_2026-09-22.md),
and the [chiral-pair bond note](CHIRAL_PAIR_BOND_FACTOR_DIMENSION_BOUNDED_THEOREM_NOTE_2026-10-10.md).

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Each parallel transverse-dot kernel at coefficient 1/2 is strictly positive and has neighbour-product mean 1, and two bonds at each height separate it from the fifteen kernels."
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "Other generic orbits and higher-rank bond spaces are not classified."
source_of_blocker_text: frontier_question
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "Exhibit a second kernel in the 5-dimensional complement of one opposite-height pair, with an exact formula, outside the five same-height kernels and the parallel-dot kernel. Do not claim that complement is based. Do not claim the 300-dimensional affine space is classified."
conditional_surface_status: "48 signed permutations of (1, 2, 3); parallel transverse-dot sign at absolute heights 1, 2, and 3; coefficient 1/2"
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
fifteen kernels already exhibited: the chirality cap, the transverse-sign
cap, the sign-product cap, and the matched and swapped transverse
crosses, at each absolute height 1, 2, and 3.

**Ansatz.** Fix an absolute height `h` and a direction `d`. The support
is the set of bonds with `a·d = h` and `b·d = -h`. A kernel in this
ansatz is soldered under proper rotations, unchanged by reversing the
bond, and has every left slice equal to 0. Transport uses any proper
`g` with `g e_z = d`. On `e_z` the seed is 0 unless `z = h`, `z' = -h`,
and the transverse cross product `x y' - y x'` is 0. When the transverse
dot product `x x' + y y'` is nonzero, the seed is the sign of its
negative. The family is `phi_d(a, b) = 1 + (1/2) M_d(a, b)`. The same
formula at the other two heights is a separate kernel. A mixed-height
bond is not in this ansatz. A sum across heights is not in this ansatz.
The complement of the exhibited line inside the 10-dimensional space is
not given a basis. The 300-dimensional affine space is not classified.

**Conclusion.** Each of the three kernels is bond-symmetric and soldered,
with values in `{-1, 0, 1}`. A quarter-turn about `z` preserves the
seed, and every proper frame gives the same value. Each record meets at
most one live direction. Every left slice sums to 0. At coefficient
`1/2` the values are `1/2`, `1`, and `3/2`. Every neighbour product has
mean 1, and every far-end sum equals 48, so the quotient by 48 lies in
the normalised space. The parent converse makes each family order-blind
on every window. On `e_z` the two bonds

```text
height 1: (-2, -3, 1) -> (-2, -3, -1) and (-2, -3, 1) -> (2, 3, -1)
height 2: (-1, -3, 2) -> (-1, -3, -2) and (-1, -3, 2) -> (1, 3, -2)
height 3: (-2, -1, 3) -> (-2, -1, -3) and (-2, -1, 3) -> (2, 1, -3)
```

agree on all fifteen comparison kernels. At the active height those
kernels read `(-1, 1, -1, 0, 0)`, and every kernel from another height
is 0. The parallel-dot kernel reads `-1` on the first bond and `+1` on
the second. The bond from `(1, 2, 3)` to itself has all of these kernels
equal to 0. None of the three parallel-dot kernels is a rational linear
combination of the fifteen, and none of the three factors is a linear
combination of those fifteen factors.

On each opposite-height pair the 64 bonds form 16 orbits of size 4
under the quarter-turn about `z`. Bond symmetry, carried to `-e_z` by
the half-turn about `x`, together with the eight left-slice sums, has
rank 6. That ansatz is 10-dimensional. The five same-height kernels
span a 5-dimensional subspace and lie in the ansatz. The parallel-dot
kernel lies in the ansatz and raises the rank to 6. Four further
dimensions at that height are not named.

**Proof.** The runner enumerates the proper rotations and the alphabet.
All four frames of each direction agree, and direct comparison gives
soldered covariance. Reversing a bond leaves the value unchanged. Each
record has one coordinate of each modulus, so only one direction meets
`a·d = h`. The runner finds at most one live direction, values in
`{-1, 0, 1}`, and a zero left slice. For a fixed neighbour condition,
at most one factor differs from 1. The product equals
`1 + (1/2) M_d(a, b)` when the condition uses that live direction, and
equals 1 otherwise. Summing over the centre, the live terms are a left
slice, which is 0. The mean is 1. The far-end sum is the same
cancellation on the right.

The two bonds at one height have the same fifteen comparison values, so
every linear combination of those fifteen agrees on the two bonds. The
parallel-dot values differ by 2. A linear combination of the fifteen
factors that matched one parallel-dot factor would be 1 on the idle
bond, hence would have coefficients summing to 1, and would then
reproduce that kernel. The two bonds forbid it.

The dimension count is row reduction over the rationals on the 16 orbit
coordinates. The five same-height kernels are constant on each orbit and
meet the bond-symmetry and slice equations, and their rank is 5. The
parallel-dot vector meets the same equations and is outside that span.

**Obligations.** Proved here: soldered covariance, frame invariance,
bond symmetry, the live-direction bound, the left slices, the product
means, the three factor values, the far-end sums, the three separations,
the orbit count, and the ranks 6, 5, and 6. Cited from Theorem 2, and
not re-proved: bond symmetry together with every product mean equal to
1 makes the family order-blind on every window. Cited from the
chiral-pair bond note, and not re-proved: far-end sum 1 is the
normalisation of that bond space. The fifteen kernels are comparison
tensors. The strongest missing lemma is an exact formula for a second
vector in the 5-dimensional complement.

## What this does not do

- It does not select a scale. The coefficient `1/2` is a witness.
- It does not classify the order-blind subset.
- It does not claim that the 300-dimensional affine space is classified.
- It does not base the 5-dimensional complement.
- It does not re-derive the order-blindness of the fifteen comparison kernels.
- It does not repeat the bond-space dimension count.
- It does not return to the modulus-3 triple.
- It does not put a mixed-height bond, or a sum across heights, inside
  the ansatz.
- It does not supply a formation site, probability, or rate.

## Runner

`scripts/chiral_pair_parallel_transverse_dot_outside_fifteen_kernels_2026_10_10.py`
repeats the covariance comparison, the slice sums, the three
separations, and the orbit rank. `TOTAL: PASS=10 FAIL=0`.

## Imports

No formation site, probability, rate, or selected scale is imported.
The proper rotations, the parallel-dot seeds, and the slice sums are
enumerated here. Theorem 2's converse is applied to each family. The
chiral-pair bond note supplies the meaning of far-end sum 1.
