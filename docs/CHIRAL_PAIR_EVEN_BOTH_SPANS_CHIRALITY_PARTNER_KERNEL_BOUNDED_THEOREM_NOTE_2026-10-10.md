---
claim_id: chiral_pair_even_both_spans_chirality_partner_kernel_bounded_theorem_note_2026-10-10
claim_type: bounded_theorem
claim_scope: "On the 48 signed permutations of (1, 2, 3), the even space, both ratio spans, and the chirality cap form a 10-dimensional sum. The ten-generator partner map has rank 49 and nullity 51. The chirality cap alone has partner rank 7. The sign product plus one cap generator minus one third of the other has scaled coefficient 4/3 and partner rank 7. The chirality block meets that 3-dimensional partner only at 0, so every nonzero chirality coefficient removes those partners. With chirality coefficient 1, that vector, the scaled coefficient 4 vector, and the swapped-dot coefficient 1 vector each have partner rank 10. On -e_x and -e_y, the lefts are (-1, -2, -3) and (-1, -2, 3). Against the three listed partners, the coefficient 4/3 vector plus the chirality cap has cross sums -6/5, -1/4, and 1/2. A chirality coefficient other than 1 is not given a full partner rank here. The ten-kernel coefficient span is not classified. The full soldered bond space is not classified. No scale is selected."
upstream_dependencies:
  - minimal_axioms
  - chiral_pair_even_span_partner_kernel_bounded_theorem_note_2026-10-10
  - chiral_pair_two_parity_excluded_partner_kernel_bounded_theorem_note_2026-10-10
runner: scripts/chiral_pair_even_both_spans_chirality_partner_kernel_2026_10_10.py
---

# Chirality coefficient 1 on both spans pairs only with zero

**Date:** 2026-10-11

**Type:** bounded_theorem

**Audit:** unset; independent audit remains a separate lane

**Status:** proposed_retained

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/chiral_pair_even_both_spans_chirality_partner_kernel_2026_10_10.py`](../scripts/chiral_pair_even_both_spans_chirality_partner_kernel_2026_10_10.py)

**Parents:** the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md),
[the even span](CHIRAL_PAIR_EVEN_SPAN_PARTNER_KERNEL_BOUNDED_THEOREM_NOTE_2026-10-10.md),
and [the two ratio spans](CHIRAL_PAIR_TWO_PARITY_EXCLUDED_PARTNER_KERNEL_BOUNDED_THEOREM_NOTE_2026-10-10.md).

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "With chirality coefficient 1, the scaled coefficient 4/3 vector, the scaled coefficient 4 vector, and the swapped-dot coefficient 1 vector each have partner rank 10."
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "Other generic orbits and higher-rank bond spaces are not classified."
source_of_blocker_text: frontier_question
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "Decide whether a chirality coefficient other than 1, on the scaled coefficient 4/3 vector, has a ten-kernel partner other than 0. Every nonzero chirality coefficient removes the original 3-dimensional partner, and coefficient 1 has partner rank 10. Do not claim the ten-kernel coefficient span is settled."
conditional_surface_status: "48 signed permutations of (1, 2, 3); even space, both ratio spans, and the chirality cap; witness directions (-1, 0, 0) and (0, -1, 0)"
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

**Target.** On the 48 signed permutations of `(1, 2, 3)`, decide whether
a vector with a nonzero chirality coefficient, a nonzero even part, and
a nonzero part in each ratio span, with a nonzero coefficient on the
swapped transverse dot or the scaled cross-dot kernel, has a ten-kernel
partner other than 0.

**Ansatz.** The even space of the source height, both ratio spans, and
the chirality cap. Their sum is 10-dimensional. The swapped transverse
dot appears only on the two swapped-orthogonal generators, and the
scaled cross-dot kernel appears only on the two cap generators. The
even generators and the chirality cap carry neither coordinate. The
ten-kernel coefficient span is not this ansatz. The full soldered bond
space is not classified.

The kernel cross sum on two perpendicular directions is the sum of the
products of the two centre values. This note does not convert that sum
into an alphabet mean.

**Conclusion.** For every ordered height pair, the ten-generator partner
map has rank 49 and nullity 51. The chirality cap alone has partner
rank 7.

The sign product plus one cap generator minus one third of the other has
scaled coefficient `4/3` and partner rank 7. In the coordinate order
chi, ts, prod, matched, swapped, parallel, oblique, swapped_dot,
orthogonal, scaled, that partner is the same 3-dimensional space as in
the sum without the chirality cap. The chirality block has rank 3 on
that space. Every nonzero chirality coefficient therefore removes those
three partners.

With chirality coefficient 1, the same vector has partner rank 10. The
sign product plus both cap generators, still with scaled coefficient 4,
has partner rank 10. The sign product plus one swapped-orthogonal
generator and the opposite oblique-matched generator, with swapped-dot
coefficient 1, has partner rank 10.

At heights 1 and 2, the bond on `-e_x` and `-e_y` has lefts
`(-1, -2, -3)` and `(-1, -2, 3)`. The coefficient `4/3` vector plus the
chirality cap, against the first listed partner, has rights
`(1, -3, -2)` and `(-1, 2, -3)`, centre pairs `(-2, 3/5)` and
`(0, 9/5)`, and kernel cross sum `-6/5`. Against the second listed
partner, the rights are `(1, -3, -2)` and `(-3, 2, -1)`, the centre
pairs are `(-2, 1/8)` and `(0, 3/8)`, and the kernel cross sum is
`-1/4`. Against the third, the rights are the same, the centre pairs
are `(-2, -1/4)` and `(0, -3/4)`, and the kernel cross sum is `1/2`.

**Proof.** The runner enumerates the proper rotations and the alphabet
and builds the ten kernels. On each ordered height pair the even space
and both ratio spans have rank 9, and the chirality cap raises the rank
to 10. The nine-generator map has rank 42 and nullity 48. Adjoining the
chirality cap raises the map rank to 49, so the kernel has dimension
51.

The coefficient `4/3` vector, with chirality coefficient 0, has
projected rank 7. Its kernel is the listed 3-dimensional space. The
three images of that kernel under the chirality block are independent,
so none of those partners survives a nonzero chirality coefficient.
At chirality coefficient 1 the projected rank is 10, so the partner
kernel is 0. The coefficient 4 vector and the swapped-dot vector have
the same projected rank 10 at chirality coefficient 1. The chirality
cap alone has projected rank 7. The three witness bonds are direct
centre sums on `-e_x` and `-e_y`.

**Obligations.** Proved here: the sum is 10-dimensional, the
ten-generator map has rank 49 and nullity 51, every nonzero chirality
coefficient removes the 3-dimensional partner of the coefficient `4/3`
vector, and chirality coefficient 1 gives that vector, the coefficient
4 vector, and the swapped-dot vector partner rank 10. The cross sums
are `-6/5`, `-1/4`, and `1/2`. Cited from the even-span note, and not
re-proved: the name of the even space. Cited from the ratio-span note,
and not re-proved: the names of the two spans. The strongest missing
lemma is whether a chirality coefficient other than 1, on the scaled
coefficient `4/3` vector, has a ten-kernel partner other than 0.

## What this does not do

- It does not select a scale. The coefficients are witnesses.
- It does not classify a chirality coefficient other than 1.
- It does not classify every cap ratio.
- It does not restate the partner kernel inside the even space and both spans, with chirality coefficient 0, as a new construction.
- It does not claim that the ten-kernel coefficient span is settled.
- It does not claim that the full soldered bond space is classified.
- It does not apply the order-blind converse.
- It does not convert a kernel cross sum into an alphabet mean.
- It does not repeat the bond-space dimension count.
- It does not return to the modulus-3 triple.
- It does not supply a formation site, probability, or rate.

## Runner

`scripts/chiral_pair_even_both_spans_chirality_partner_kernel_2026_10_10.py`
checks the ten-generator kernel, chirality coefficient 1, and the
witness bonds. `TOTAL: PASS=11 FAIL=0`.

## Imports

No formation site, probability, rate, or selected scale is imported.
The proper rotations, the stacked partner kernel, and the witness sums
are enumerated here. The even-span note names the even space. The
ratio-span note names the two spans. The order-blind converse is not
applied.
