---
claim_id: chiral_pair_lower_height_crosses_outside_five_kernels_bounded_theorem_note_2026-10-10
claim_type: bounded_theorem
claim_scope: "On the 48 signed permutations of (1, 2, 3), the matched and swapped transverse crosses at absolute heights 1 and 2 are bond-symmetric and soldered. Each cross has values in {-1, 0, 1}, at most one live direction, and every left slice sums to 0, so at coefficient 1/2 each factor is strictly positive and every neighbour product has mean 1. Every far-end sum equals 48. Nine bonds on e_z have determinant 8 in the five height-3 columns followed by these four crosses. Each lower-height cross is nonzero on a bond where the other eight kernels vanish, so none is a linear combination of the five. The order-blind subset is not classified. No scale is selected."
upstream_dependencies:
  - minimal_axioms
  - order_blind_nearest_neighbour_formation_independence_beyond_neighbours_unsoldered_constancy_and_soldered_escape_bounded_theorem_note_2026-09-22
  - chiral_pair_bond_factor_dimension_bounded_theorem_note_2026-10-10
runner: scripts/chiral_pair_lower_height_crosses_outside_five_kernels_2026_10_10.py
---

# Four lower-height crosses on the chiral pair lie off the five kernels

**Date:** 2026-10-10

**Type:** bounded_theorem

**Audit:** unset; independent audit remains a separate lane

**Status:** proposed_retained

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/chiral_pair_lower_height_crosses_outside_five_kernels_2026_10_10.py`](../scripts/chiral_pair_lower_height_crosses_outside_five_kernels_2026_10_10.py)

**Parents:** the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md),
[the order-blind formation note](ORDER_BLIND_NEAREST_NEIGHBOUR_FORMATION_INDEPENDENCE_BEYOND_NEIGHBOURS_UNSOLDERED_CONSTANCY_AND_SOLDERED_ESCAPE_BOUNDED_THEOREM_NOTE_2026-09-22.md),
and the [chiral-pair bond note](CHIRAL_PAIR_BOND_FACTOR_DIMENSION_BOUNDED_THEOREM_NOTE_2026-10-10.md).

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Each lower-height transverse cross at coefficient 1/2 is strictly positive and has neighbour-product mean 1, and nine bonds give determinant 8 against the five height-3 kernels."
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "Other generic orbits and higher-rank bond spaces are not classified."
source_of_blocker_text: frontier_question
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "Ask whether a strictly positive order-blind factor on the 48-point chiral pair lies outside the span of the five height-3 kernels and these four crosses. Do not repeat the dimension count."
conditional_surface_status: "48 signed permutations of (1, 2, 3); matched and swapped crosses at absolute heights 1 and 2; coefficient 1/2"
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
chiral cap, the transverse-sign cap, the sign-product cap, and the
matched and swapped transverse crosses on `a·d = 3` and `b·d = -3`.

**Ansatz.** On `e_z`, with records `(x, y, z)` and `(x', y', z')` and
with absolute height `h` in `{1, 2}`, the matched cross is
`sign(x y' - y x')` when `z = h`, `z' = -h`, `|x| = |x'|`, and
`|y| = |y'|`, and 0 otherwise. The swapped cross uses the same sign
when `z = h`, `z' = -h`, `|x| = |y'|`, and `|y| = |x'|`, and is 0
otherwise. For a proper rotation `g` with `g e_z = d`, each kernel is
the seed value of `g^{-1}` on the two records. The value does not
depend on the choice of `g`. The families are

```text
phi_d(a, b) = 1 + (1/2) M_d(a, b)
```

with `M` any one of the four crosses. The five comparison kernels are
the chiral cap, the transverse-sign cap, their sign product, and the
matched and swapped crosses on the caps `a·d = 3` and `b·d = -3`. A
factor outside the span of these nine kernels is not classified here.
The 300-dimensional affine space is not classified. A sum across
heights is not in this ansatz.

**Conclusion.** Each of the four crosses is bond-symmetric and
soldered, with values in `{-1, 0, 1}`. Each record meets at most one
live direction of that cross, and every left slice sums to 0. At
coefficient `1/2` the values are `1/2`, `1`, and `3/2`. Every
neighbour product has mean 1, and every far-end sum equals 48, so the
quotient by 48 lies in the normalised space. The parent converse makes
each family order-blind on every window. On `e_z`, nine bonds have
rows

```text
(-1, 1, -1, 0, 0, 0, 0, 0, 0)
(1, -1, -1, -1, 0, 0, 0, 0, 0)
(1, 1, 1, 0, 1, 0, 0, 0, 0)
(-1, -1, 1, 0, -1, 0, 0, 0, 0)
(-1, -1, 1, 0, 1, 0, 0, 0, 0)
(0, 0, 0, 0, 0, 1, 0, 0, 0)
(0, 0, 0, 0, 0, 0, -1, 0, 0)
(0, 0, 0, 0, 0, 0, 0, 1, 0)
(0, 0, 0, 0, 0, 0, 0, 0, -1)
```

in the chiral, transverse-sign, sign-product, height-3 matched,
height-3 swapped, height-1 matched, height-1 swapped, height-2
matched, and height-2 swapped columns. The first five bonds run from
`(-2, -1, 3)` to `(-2, -1, -3)`, `(-2, 1, -3)`, `(-1, -2, -3)`,
`(-1, 2, -3)`, and `(1, -2, -3)`. The last four run from `(2, -3, 1)`
to `(2, 3, -1)`, from `(2, 3, 1)` to `(3, 2, -1)`, from `(1, -3, 2)`
to `(1, 3, -2)`, and from `(1, 3, 2)` to `(3, 1, -2)`. The determinant
is 8. The bond from `(1, 2, 3)` to itself has all nine kernels equal
to 0. None of the four lower-height crosses is a rational linear
combination of the five height-3 kernels, and none of the four factors
is a linear combination of those five factors.

**Proof.** The runner enumerates the proper rotations and the alphabet.
Four rotations send `e_z` to each axis step, and every such frame gives
the same seed value at each height and each matching rule. Direct
comparison gives soldered covariance and bond symmetry.

A record has one coordinate of each modulus, so only one direction can
meet `a·d = h`. The runner finds at most one live direction and a zero
left slice for each cross. For a fixed neighbour condition, at most one
factor differs from 1. The product equals `1 + (1/2) M_d(a, b)` when
the condition uses that live direction, and equals 1 otherwise. Summing
over the centre, the live terms in each direction are the left slice at
the fixed neighbour, which is 0. The mean is 1. The far-end sum is the
same cancellation on the right.

The nine named rows have determinant 8. The last four columns vanish
on the first five rows, and each of those columns is the only nonzero
entry of one later row. Each lower-height column therefore lies outside
the span of the first five, and the four columns are independent of
each other. A linear combination of the five height-3 factors that
matched one lower-height factor would be 1 on the idle bond, hence
would have coefficients summing to 1, and would then reproduce that
lower-height column. The witness row forbids it.

**Obligations.** Proved here: frame independence, soldered covariance,
bond symmetry, the live-direction bound, the left slices, the product
means, the three factor values, the far-end sums, and the determinant.
Cited from Theorem 2, and not re-proved: bond symmetry together with
every product mean equal to 1 makes the family order-blind on every
window. Cited from the chiral-pair bond note, and not re-proved:
far-end sum 1 is the normalisation of that bond space. The dimension
count is not repeated. The five height-3 kernels are comparison
tensors. The strongest missing lemma is a strictly positive
order-blind factor outside the span of these nine kernels.

## What this does not do

- It does not select a scale. The coefficient `1/2` is a witness.
- It does not classify the order-blind subset.
- It does not claim that the 300-dimensional affine space is classified.
- It does not re-derive the order-blindness of the five height-3 kernels.
- It does not repeat the bond-space dimension count.
- It does not return to the modulus-3 triple.
- It does not put a sum across heights inside the ansatz.
- It does not supply a formation site, probability, or rate.

## Runner

`scripts/chiral_pair_lower_height_crosses_outside_five_kernels_2026_10_10.py`
repeats the frame comparison, the slice sums, and the nine-bond
determinant. `TOTAL: PASS=10 FAIL=0`.

## Imports

No formation site, probability, rate, or selected scale is imported.
The proper rotations, the four crosses, and the slice sums are
enumerated here. Theorem 2's converse is applied to each family. The
chiral-pair bond note supplies the meaning of far-end sum 1.
