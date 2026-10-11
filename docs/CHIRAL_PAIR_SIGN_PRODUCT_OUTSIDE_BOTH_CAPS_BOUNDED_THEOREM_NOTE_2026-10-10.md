---
claim_id: chiral_pair_sign_product_outside_both_caps_bounded_theorem_note_2026-10-10
claim_type: bounded_theorem
claim_scope: "On the 48 signed permutations of (1, 2, 3), the sign-product cap phi_d(a, b) = 1 + (1/2) P_d(a) P_{-d}(b) is bond-symmetric and soldered. P_d is orbit chirality times the transverse sign on the cap a·d = 3. All 729 partner patterns have product mean 1, the values are 1/2, 1, and 3/2, and every far-end sum equals 48. The bonds e_z from (1, 2, 3), (2, -1, 3), and (-2, -1, 3) to (-2, -1, -3) give kernel rows (1, 1, 1), (1, -1, -1), and (-1, 1, -1) in the chiral, transverse-sign, and sign-product columns, with determinant 4. The sign-product kernel is not a linear combination of those two caps. The order-blind subset is not classified. No scale is selected."
upstream_dependencies:
  - minimal_axioms
  - order_blind_nearest_neighbour_formation_independence_beyond_neighbours_unsoldered_constancy_and_soldered_escape_bounded_theorem_note_2026-09-22
  - chiral_pair_bond_factor_dimension_bounded_theorem_note_2026-10-10
runner: scripts/chiral_pair_sign_product_outside_both_caps_2026_10_10.py
---

# A sign-product cap on the chiral pair lies off both exhibited lines

**Date:** 2026-10-10

**Type:** bounded_theorem

**Audit:** unset; independent audit remains a separate lane

**Status:** proposed_retained

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/chiral_pair_sign_product_outside_both_caps_2026_10_10.py`](../scripts/chiral_pair_sign_product_outside_both_caps_2026_10_10.py)

**Parents:** the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md),
[the order-blind formation note](ORDER_BLIND_NEAREST_NEIGHBOUR_FORMATION_INDEPENDENCE_BEYOND_NEIGHBOURS_UNSOLDERED_CONSTANCY_AND_SOLDERED_ESCAPE_BOUNDED_THEOREM_NOTE_2026-09-22.md),
and the [chiral-pair bond note](CHIRAL_PAIR_BOND_FACTOR_DIMENSION_BOUNDED_THEOREM_NOTE_2026-10-10.md).

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The sign product of orbit chirality and the transverse sign at coefficient 1/2 is strictly positive, every partner pattern has mean 1, and three bonds give determinant 4 against the two exhibited caps."
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "Other generic orbits and higher-rank bond spaces are not classified."
source_of_blocker_text: frontier_question
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "Ask whether a strictly positive order-blind factor on the 48-point chiral pair lies outside the span of the chiral cap, the transverse-sign cap, and this sign-product cap. Do not repeat the dimension count."
conditional_surface_status: "48 signed permutations of (1, 2, 3); sign-product cap; coefficient 1/2; uniform partner patterns"
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

Theorem 4(b) names the transverse sign on one orbit: "let X_d(a) be the
sign of the product of the two coordinates of a transverse to d when
a.d = 3, and 0 otherwise." Theorem 4(c) names the other cap: "On the
48-point chiral pair, chirality (+1 on one proper-rotation orbit, -1 on
the other) on the same caps gives a second varying order-blind rule."

## Theorem

**Target.** On the 48 signed permutations of `(1, 2, 3)`, decide whether
a strictly positive order-blind factor lies outside both the chiral-cap
line and the transverse-sign cap.

**Ansatz.** Let `χ(a)` be `+1` on the proper orbit of `(1, 2, 3)` and
`-1` on the other orbit. Let `S_d(a)` be the sign of the product of the
two coordinates transverse to an axis step `d` when `a·d = 3`, and 0
otherwise. The sign product is `P_d(a) = χ(a) S_d(a)`. The family is

```text
phi_d(a, b) = 1 + (1/2) P_d(a) P_{-d}(b)
```

The chiral-cap kernel is `χ_d(a) χ_{-d}(b)`, where `χ_d` is `χ` on the
cap `a·d = 3` and 0 otherwise. The transverse-sign kernel is
`S_d(a) S_{-d}(b)`. A factor outside the span of these three kernels is
not classified here. The 300-dimensional affine space is not classified.

**Conclusion.** The sign-product factor is bond-symmetric and soldered.
Chirality is invariant. The transverse sign changes by one
point-independent sign, and that sign is the same on `d` and on `-d`.
The three cap signs have mean 0, and the six caps are disjoint. All 729
partner patterns have uniform product mean 1. The values are `1/2`,
`1`, and `3/2`. Every far-end sum equals 48, so the quotient by 48 lies
in the normalised space. The parent converse makes the family
order-blind on every window. On `e_z`, the bonds from `(1, 2, 3)`,
`(2, -1, 3)`, and `(-2, -1, 3)` to `(-2, -1, -3)` have kernel rows
`(1, 1, 1)`, `(1, -1, -1)`, and `(-1, 1, -1)` in the chiral,
transverse-sign, and sign-product columns. The determinant is 4. The
bond on `e_z` from `(1, 2, 3)` to itself has all three kernels equal to
0, so a linear combination of the two exhibited factors that reproduced
this factor would have coefficients summing to 1 and would reproduce
the third column. No such coefficients exist.

**Proof.** The runner enumerates the proper rotations and the alphabet.
`(2, 1, 3)` and `(1, 2, -3)` lie in the second proper orbit. The
positive set is that orbit, so chirality is unchanged by every proper
rotation. Each record has one coordinate of modulus 3, so it meets
`a·d = 3` for exactly one axis step. Direct summation gives mean 0 for
each of the three cap signs.

For each rotation and each direction, the ratios of the transported
transverse sign to the original sign, on the support, form one common
value, and the opposite direction has the same value. Some rotation
flips the sign. Chirality contributes no further sign, so `P` is
transported by that common sign on both `d` and `-d`. The product is
therefore unchanged. Direct comparison gives the same equality on every
bond, and it gives bond symmetry.

Every 6-tuple with entries in `{-1, 0, 1}` has product mean 1, because
a record meets only one cap and that cap sign has mean 0. The same
tuples are every value of `P_{-d}(b)`. The three named bonds give the
rows above. Their determinant is 4, so no rational coefficients
reproduce the third column from the first two. The bond from
`(1, 2, 3)` to itself on `e_z` has every kernel equal to 0. Matching
the factors on that bond forces the two coefficients to sum to 1, and
the three rows then forbid the combination.

**Obligations.** Proved here: invariance of chirality, the common
transverse-sign cocycle, soldered covariance of the product, bond
symmetry, disjoint mean-zero supports, the 729 means, the three values,
the far-end sums, and the determinant obstruction. Cited from Theorem
2, and not re-proved: bond symmetry together with every product mean
equal to 1 makes the family order-blind on every window. Cited from the
chiral-pair bond note, and not re-proved: far-end sum 1 is the
normalisation of that bond space. The dimension count is not repeated.
The two exhibited caps are the comparison tensors, not a re-derivation
of their order-blindness. The strongest missing lemma is a strictly
positive order-blind factor outside the span of these three kernels.

## What this does not do

- It does not select a scale. The coefficient `1/2` is a witness.
- It does not classify the order-blind subset.
- It does not claim that the 300-dimensional affine space is classified.
- It does not re-derive the order-blindness of either exhibited cap.
- It does not repeat the bond-space dimension count.
- It does not return to the modulus-3 triple.
- It does not supply a formation site, probability, or rate.

## Runner

`scripts/chiral_pair_sign_product_outside_both_caps_2026_10_10.py`
repeats the cocycle, the 729 means, and the three-bond determinant.
`TOTAL: PASS=11 FAIL=0`.

## Imports

No formation site, probability, rate, or selected scale is imported.
The proper rotations, the cap signs, and the partner means are
enumerated here. Theorem 2's converse is applied to this family. The
chiral-pair bond note supplies the meaning of far-end sum 1.
