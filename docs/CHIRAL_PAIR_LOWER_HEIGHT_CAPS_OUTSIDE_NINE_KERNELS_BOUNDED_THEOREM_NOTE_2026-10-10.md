---
claim_id: chiral_pair_lower_height_caps_outside_nine_kernels_bounded_theorem_note_2026-10-10
claim_type: bounded_theorem
claim_scope: "On the 48 signed permutations of (1, 2, 3), the chirality cap, the transverse-sign cap, and their sign product at each absolute height 1 and 2 are bond-symmetric and soldered. Each has values in {-1, 0, 1}, mean 0, and at most one live direction, so at coefficient 1/2 each factor is strictly positive and every neighbour product has mean 1. Every far-end sum equals 48. At each height, five bonds have rows (-1, 1, -1, 0, 0), (1, -1, -1, -1, 0), (1, -1, -1, 1, 0), (1, 1, 1, 0, -1), and (-1, -1, 1, 0, -1), with determinant -16. The first of those bonds has all nine comparison kernels equal to 0, so none of the six caps is a linear combination of the nine. The order-blind subset is not classified. No scale is selected."
upstream_dependencies:
  - minimal_axioms
  - order_blind_nearest_neighbour_formation_independence_beyond_neighbours_unsoldered_constancy_and_soldered_escape_bounded_theorem_note_2026-09-22
  - chiral_pair_bond_factor_dimension_bounded_theorem_note_2026-10-10
runner: scripts/chiral_pair_lower_height_caps_outside_nine_kernels_2026_10_10.py
---

# Six lower-height caps on the chiral pair lie off the nine kernels

**Date:** 2026-10-10

**Type:** bounded_theorem

**Audit:** unset; independent audit remains a separate lane

**Status:** proposed_retained

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/chiral_pair_lower_height_caps_outside_nine_kernels_2026_10_10.py`](../scripts/chiral_pair_lower_height_caps_outside_nine_kernels_2026_10_10.py)

**Parents:** the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md),
[the order-blind formation note](ORDER_BLIND_NEAREST_NEIGHBOUR_FORMATION_INDEPENDENCE_BEYOND_NEIGHBOURS_UNSOLDERED_CONSTANCY_AND_SOLDERED_ESCAPE_BOUNDED_THEOREM_NOTE_2026-09-22.md),
and the [chiral-pair bond note](CHIRAL_PAIR_BOND_FACTOR_DIMENSION_BOUNDED_THEOREM_NOTE_2026-10-10.md).

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Each lower-height cap dressing at coefficient 1/2 is strictly positive and has neighbour-product mean 1, and five bonds at each height give determinant -16."
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "Other generic orbits and higher-rank bond spaces are not classified."
source_of_blocker_text: frontier_question
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "Ask whether a strictly positive order-blind factor on the 48-point chiral pair lies outside the span of the nine kernels and these six caps. Do not repeat the dimension count."
conditional_surface_status: "48 signed permutations of (1, 2, 3); chirality, transverse-sign, and sign-product caps at absolute heights 1 and 2; coefficient 1/2"
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
a strictly positive order-blind factor lies outside the span of the nine
kernels already exhibited: the chiral cap, the transverse-sign cap, and
the sign-product cap on `a·d = 3`, together with the matched and swapped
transverse crosses at absolute heights 1, 2, and 3.

**Ansatz.** For absolute height `h` in `{1, 2}` and a record `a`, write
`C_{h,d}(a)` for the orbit chirality of `a` when `a·d = h` and 0
otherwise, and `S_{h,d}(a)` for the sign of the product of the two
coordinates transverse to `d` when `a·d = h` and 0 otherwise. The three
kernels at that height are

```text
C_{h,d}(a) C_{h,-d}(b),
S_{h,d}(a) S_{h,-d}(b),
(C_{h,d} S_{h,d})(a) (C_{h,-d} S_{h,-d})(b).
```

The families are `phi_d(a, b) = 1 + (1/2) M_d(a, b)` with `M` any one of
these six kernels. A factor outside the span of these six and the nine
comparison kernels is not classified here. The 300-dimensional affine
space is not classified. A bond whose two heights differ, and a sum
across heights, are not in this ansatz.

**Conclusion.** Each of the six kernels is bond-symmetric and soldered,
with values in `{-1, 0, 1}`. Each cap sign has mean 0, and each record
meets at most one live direction of that kernel. Every left slice sums
to 0. At coefficient `1/2` the values are `1/2`, `1`, and `3/2`. Every
neighbour product has mean 1, and every far-end sum equals 48, so the
quotient by 48 lies in the normalised space. The parent converse makes
each family order-blind on every window. On `e_z`, the five bonds from
`(-2, -3, 1)` to `(-2, -3, -1)`, `(-2, 3, -1)`, `(2, -3, -1)`,
`(-3, -2, -1)`, and `(-3, 2, -1)`, and the five bonds from
`(-1, -3, 2)` to `(-1, -3, -2)`, `(-1, 3, -2)`, `(1, -3, -2)`,
`(-3, -1, -2)`, and `(-3, 1, -2)`, have the same rows

```text
(-1, 1, -1, 0, 0)
(1, -1, -1, -1, 0)
(1, -1, -1, 1, 0)
(1, 1, 1, 0, -1)
(-1, -1, 1, 0, -1)
```

in the chirality, transverse-sign, sign-product, matched-cross, and
swapped-cross columns at that height. Each determinant is `-16`. Every
kernel supported at a different height vanishes on these bonds. The
bond from `(1, 2, 3)` to itself has all of these kernels equal to 0.
None of the six caps is a rational linear combination of the nine
comparison kernels, and none of the six factors is a linear combination
of those nine factors.

**Proof.** The runner enumerates the proper rotations and the alphabet.
Direct comparison gives soldered covariance. A product
`F_d(a) F_{-d}(b)` is unchanged by reversing the bond. Each record has
one coordinate of each modulus, so only one direction meets `a·d = h`.
The runner finds mean 0, at most one live direction, and a zero left
slice. For a fixed neighbour condition, at most one factor differs from
1. The product equals `1 + (1/2) M_d(a, b)` when the condition uses that
live direction, and equals 1 otherwise. Summing over the centre, the
live terms are a left slice, which is 0. The mean is 1. The far-end sum
is the same cancellation on the right.

The first height-1 row is `(-1, 1, -1, 0, 0)`, so each of the three
height-1 caps is nonzero while both height-1 crosses vanish. The same
holds at height 2. Kernels supported at any other height also vanish on
that bond, and those kernels include the five height-3 kernels and the
two crosses at the other lower height. All nine comparison kernels are
therefore 0 on a bond where the chosen cap kernel is `±1`. The
determinants `-16` add that, at each height, the three caps are
independent of each other and of the two crosses. A linear combination
of the nine factors that matched one cap factor would be 1 on the idle
bond, hence would have coefficients summing to 1, and would then
reproduce that cap column. The witness bond forbids it.

**Obligations.** Proved here: soldered covariance, bond symmetry, the
means, the live-direction bound, the left slices, the product means,
the three factor values, the far-end sums, and the two determinants.
Cited from Theorem 2, and not re-proved: bond symmetry together with
every product mean equal to 1 makes the family order-blind on every
window. Cited from the chiral-pair bond note, and not re-proved:
far-end sum 1 is the normalisation of that bond space. The dimension
count is not repeated. The nine kernels are comparison tensors. The
strongest missing lemma is a strictly positive order-blind factor
outside the span of these fifteen kernels.

## What this does not do

- It does not select a scale. The coefficient `1/2` is a witness.
- It does not classify the order-blind subset.
- It does not claim that the 300-dimensional affine space is classified.
- It does not re-derive the order-blindness of the nine comparison kernels.
- It does not repeat the bond-space dimension count.
- It does not return to the modulus-3 triple.
- It does not put a mixed-height bond, or a sum across heights, inside
  the ansatz.
- It does not supply a formation site, probability, or rate.

## Runner

`scripts/chiral_pair_lower_height_caps_outside_nine_kernels_2026_10_10.py`
repeats the covariance comparison, the slice sums, and the two
determinants. `TOTAL: PASS=10 FAIL=0`.

## Imports

No formation site, probability, rate, or selected scale is imported.
The proper rotations, the six cap products, and the slice sums are
enumerated here. Theorem 2's converse is applied to each family. The
chiral-pair bond note supplies the meaning of far-end sum 1.
