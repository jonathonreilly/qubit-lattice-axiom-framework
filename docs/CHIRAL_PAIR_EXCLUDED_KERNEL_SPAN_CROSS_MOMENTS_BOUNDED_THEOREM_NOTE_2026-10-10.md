---
claim_id: chiral_pair_excluded_kernel_span_cross_moments_bounded_theorem_note_2026-10-10
claim_type: bounded_theorem
claim_scope: "On the 48 signed permutations of (1, 2, 3), the excluded span is the rational span of the matched transverse cross, the swapped transverse dot, and the scaled cross-dot kernel. For every ordered pair of absolute heights among 1, 2, and 3, a vector in that span and a vector in the ten-kernel space have every two-centre kernel cross sum equal to 0 if and only if one of the two vectors is 0. The matched kernel at height 1 with the zero vector at height 2 is such a pair. The matched kernels at heights 1 and 2 fail on the bond with directions (-1, 0, 0) and (0, -1, 0), lefts (-1, -2, -3) and (-1, -2, 3), and rights (1, 2, 3) and (1, 2, 3): the centre values are (0, 1) and (0, -1), the kernel cross sum is -1, and the direct alphabet mean is 47/48. Matched and swapped-dot self-cross sums take the values -1, 0, and 1 on each unordered height pair. Scaled self-cross sums take -4, -1, 0, and 2 on heights (1, 2) and (2, 3), and -2, 0, 1, and 4 on heights (1, 3). A vector with both a parity-span component and a nonzero excluded coefficient is outside this ansatz. The ten-kernel coefficient span is not classified. The full soldered bond space is not classified. No scale is selected."
upstream_dependencies:
  - minimal_axioms
  - chiral_pair_cross_height_parity_span_cross_moments_bounded_theorem_note_2026-10-10
  - chiral_pair_scaled_cross_dot_bases_opposite_height_ansatz_bounded_theorem_note_2026-10-10
  - chiral_pair_opposite_height_basis_mixtures_product_means_bounded_theorem_note_2026-10-10
runner: scripts/chiral_pair_excluded_kernel_span_cross_moments_2026_10_10.py
---

# Excluded-kernel cross moments on two opposite-height bases

**Date:** 2026-10-10

**Type:** bounded_theorem

**Audit:** unset; independent audit remains a separate lane

**Status:** proposed_retained

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/chiral_pair_excluded_kernel_span_cross_moments_2026_10_10.py`](../scripts/chiral_pair_excluded_kernel_span_cross_moments_2026_10_10.py)

**Parents:** the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md),
[the parity-span cross-moment note](CHIRAL_PAIR_CROSS_HEIGHT_PARITY_SPAN_CROSS_MOMENTS_BOUNDED_THEOREM_NOTE_2026-10-10.md),
[the scaled cross-dot basis note](CHIRAL_PAIR_SCALED_CROSS_DOT_BASES_OPPOSITE_HEIGHT_ANSATZ_BOUNDED_THEOREM_NOTE_2026-10-10.md),
and the [opposite-height mixture note](CHIRAL_PAIR_OPPOSITE_HEIGHT_BASIS_MIXTURES_PRODUCT_MEANS_BOUNDED_THEOREM_NOTE_2026-10-10.md).

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Inside the excluded three-kernel span, every kernel cross sum with a ten-kernel partner vanishes exactly when one of the two vectors is zero."
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "Other generic orbits and higher-rank bond spaces are not classified."
source_of_blocker_text: frontier_question
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "Decide whether a vector with both a parity-span component and a nonzero coefficient on the matched cross, the swapped transverse dot, or the scaled cross-dot kernel can pair with a nonzero ten-kernel vector and still have every cross moment equal to 0. Do not claim the ten-kernel coefficient span is settled."
conditional_surface_status: "48 signed permutations of (1, 2, 3); excluded span of the matched cross, the swapped transverse dot, and the scaled cross-dot kernel; witness directions (-1, 0, 0) and (0, -1, 0)"
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

## Theorem

**Target.** On the 48 signed permutations of `(1, 2, 3)`, decide which
rational coefficient vectors in the span of the matched transverse
cross, the swapped transverse dot, and the scaled cross-dot kernel have
every cross moment equal to 0 against a vector in the ten-kernel space
at the other height.

**Ansatz.** The excluded span is the rational span of those three
kernels. The parity span is the rational span of the other seven, and
its cross moments are already settled. A coefficient vector that uses
both a parity-span kernel and one of these three is outside this
ansatz. The ten-kernel coefficient span is not this ansatz. The full
soldered bond space is not classified.

For absolute heights `h` and `k`, the two centres that meet height `h`
in one direction and height `k` in a perpendicular direction differ by
the sign of the unused coordinate. The kernel cross sum on that bond is
the sum of the two products of centre values. The alphabet mean on a
bond is the average, over the 48 records, of the product of the two
factors `1 + kernel`. That mean is computed directly on one witness
bond. A kernel cross sum is not by itself that mean.

**Conclusion.** Let `x` lie in the excluded span at one absolute height,
and let `y` lie in the ten-kernel space at the other. Every two-centre
kernel cross sum vanishes if and only if `x` is 0 or `y` is 0. This
holds for every ordered pair of heights among `{1, 2, 3}`.

The matched kernel at height 1 with the zero vector at height 2 has
every kernel cross sum equal to 0. The height-2 factor is identically
1. The one-height mixture note gives every neighbour product of a
single-height rational mixture mean 1, so every product that multiplies
by this partner also has mean 1. The matched kernel at coefficient 1
takes values in `{-1, 0, 1}`, so the factor `1 + kernel` takes 0. This
note does not apply the order-blind converse.

The same matched kernel against the height-2 chirality cap does not
have every kernel cross sum equal to 0. Against itself, the matched
kernels at heights 1 and 2 fail on one named bond. The directions are
`-e_x` and `-e_y`. The lefts are `(-1, -2, -3)` and `(-1, -2, 3)`. Both
rights are `(1, 2, 3)`. The centre values are `(0, 1)` and `(0, -1)`.
The kernel cross sum is `-1`. The direct alphabet mean is `47/48`.

On each unordered height pair, the matched kernel with itself, and the
swapped transverse dot with itself, take kernel cross sums in
`{-1, 0, 1}`. The scaled kernel with itself takes kernel cross sums in
`{-4, -1, 0, 2}` on heights `(1, 2)` and `(2, 3)`, and in
`{-2, 0, 1, 4}` on heights `(1, 3)`. Each nonzero value is a failing
bond. These sets are kernel cross sums, not alphabet means.

**Proof.** The runner enumerates the proper rotations and the alphabet
and builds the ten kernels. For each ordered height pair it forms, at
every perpendicular direction pair and every admissible pair of far
ends, the three rows of excluded-kernel centre products against the ten
kernels at the other height. Six coefficient weights each select ten
independent rows. The determinant of the general excluded combination
on those rows is a polynomial in the three coefficients. The only
common zero of the six polynomials, on every ordered height pair, is
the origin. A nonzero excluded vector whose partner rank was below 10
would make every such determinant vanish. Therefore that rank is 10, and
the only ten-kernel partner with every kernel cross sum equal to 0 is
the zero vector. The zero vector on either side has every cross sum
equal to 0. The runner checks the matched kernel against the zero
vector, and checks that the matched kernel against the chirality cap
fails.

The self-cross sets are the two-centre sums of each excluded kernel
with itself. The witness mean is the direct sum of the 48 products,
divided by 48.

**Obligations.** Proved here: the six partner determinants have only the
origin as a common zero on each ordered height pair, the resulting
rank, the zero-partner identity, the chirality-cap failure, the
self-cross sets, and the witness centre values, kernel cross sum `-1`,
and alphabet mean `47/48`. Cited from the parity-span note, and not
re-proved: cross moments inside the seven-kernel parity span vanish
exactly when the odd parts are not both nonzero and the even parts are
not both nonzero, and these three kernels lie outside that span. Cited
from the basis note, and not re-proved: the ten named kernels are a
basis of one opposite-height ansatz. Cited from the one-height mixture
note, and not re-proved: a rational mixture supported on one height has
every neighbour product of mean 1. The strongest missing lemma is
whether a vector with both a parity-span component and a nonzero
excluded coefficient can pair with a nonzero ten-kernel vector and
still have every cross moment equal to 0.

## What this does not do

- It does not select a scale. Coefficient 1 is a witness.
- It does not put a parity-span component into the excluded span.
- It does not claim that the ten-kernel coefficient span is settled.
- It does not claim that the full soldered bond space is classified.
- It does not apply the order-blind converse.
- It does not treat a kernel cross sum as an alphabet mean, except on
  the one bond whose mean was summed directly.
- It does not repeat the parity-span classification.
- It does not repeat the bond-space dimension count.
- It does not return to the modulus-3 triple.
- It does not supply a formation site, probability, or rate.

## Runner

`scripts/chiral_pair_excluded_kernel_span_cross_moments_2026_10_10.py`
checks the partner determinants, the self-cross sets, and the witness.
`TOTAL: PASS=9 FAIL=0`.

## Imports

No formation site, probability, rate, or selected scale is imported.
The proper rotations, the partner determinants, and the witness sum are
enumerated here. The parity-span note supplies the seven-kernel split
and the exclusion of these three kernels. The basis note supplies the
ten-kernel basis. The one-height mixture note supplies mean 1 for a
mixture supported on one height. The order-blind converse is not
applied.
