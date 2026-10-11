---
claim_id: chiral_pair_even_both_spans_partner_kernel_bounded_theorem_note_2026-10-10
claim_type: bounded_theorem
claim_scope: "On the 48 signed permutations of (1, 2, 3), the even space and both ratio spans form a 9-dimensional sum, and the chirality cap lies outside it. The nine-generator partner map has rank 42 and nullity 48, and the kernel projects onto every even coefficient. The sign product plus both cap generators has scaled coefficient 4 and partner rank 10. The sign product plus one cap generator minus one third of the other has scaled coefficient 4/3, swapped-dot coefficient 0, and partner rank 7. That partner kernel is 3-dimensional and depends on the ordered height pair. The sign product plus one swapped-orthogonal generator and the opposite oblique-matched generator has swapped-dot coefficient 1 and partner rank 10. On -e_x and -e_y, the lefts are (-1, -2, -3) and (-1, -2, 3). The swapped-dot vector, against the first oblique-matched generator, has rights (1, -3, -2) and (-1, 2, -3), centre pairs (-1, 0) and (1, 2), and kernel cross sum 2. The scaled coefficient 4 vector, against its cap generator, has rights (1, -3, -2) and (-3, 2, 1), centre pairs (-3, 0) and (1, -4), and kernel cross sum -4. Each listed partner of the coefficient 4/3 vector has cross sum 0 on those directions. A nonzero chirality coefficient is not in this count. The ten-kernel coefficient span is not classified. The full soldered bond space is not classified. No scale is selected."
upstream_dependencies:
  - minimal_axioms
  - chiral_pair_even_span_partner_kernel_bounded_theorem_note_2026-10-10
  - chiral_pair_two_parity_excluded_partner_kernel_bounded_theorem_note_2026-10-10
runner: scripts/chiral_pair_even_both_spans_partner_kernel_2026_10_10.py
---

# The cap ratio 4/3 meets both spans and keeps a partner

**Date:** 2026-10-11

**Type:** bounded_theorem

**Audit:** unset; independent audit remains a separate lane

**Status:** proposed_retained

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/chiral_pair_even_both_spans_partner_kernel_2026_10_10.py`](../scripts/chiral_pair_even_both_spans_partner_kernel_2026_10_10.py)

**Parents:** the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md),
[the even span](CHIRAL_PAIR_EVEN_SPAN_PARTNER_KERNEL_BOUNDED_THEOREM_NOTE_2026-10-10.md),
and [the two ratio spans](CHIRAL_PAIR_TWO_PARITY_EXCLUDED_PARTNER_KERNEL_BOUNDED_THEOREM_NOTE_2026-10-10.md).

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "In the sum of the even space and both ratio spans, the scaled coefficient 4/3 has a 3-dimensional ten-kernel partner and the scaled coefficient 4 has partner rank 10."
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "Other generic orbits and higher-rank bond spaces are not classified."
source_of_blocker_text: frontier_question
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "Decide whether a vector with a nonzero chirality coefficient, a nonzero even part, and a nonzero part in each ratio span, with a nonzero coefficient on the swapped transverse dot or the scaled cross-dot kernel, has a ten-kernel partner other than 0. Inside the even space and the two ratio spans, the scaled coefficient 4/3 has a 3-dimensional partner and the scaled coefficient 4 has partner rank 10. Do not claim the ten-kernel coefficient span is settled."
conditional_surface_status: "48 signed permutations of (1, 2, 3); even space and both ratio spans; witness directions (-1, 0, 0) and (0, -1, 0)"
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
a vector that meets both ratio spans and has a nonzero even part, with a
nonzero coefficient on the swapped transverse dot or the scaled
cross-dot kernel, has a ten-kernel partner other than 0.

**Ansatz.** The even space of the source height and both ratio spans.
Their sum is 9-dimensional. The chirality cap lies outside it. The
swapped transverse dot appears only on the two swapped-orthogonal
generators, and the scaled cross-dot kernel appears only on the two cap
generators. The even generators carry neither coordinate. The
ten-kernel coefficient span is not this ansatz. The full soldered bond
space is not classified.

The kernel cross sum on two perpendicular directions is the sum of the
products of the two centre values. This note does not convert that sum
into an alphabet mean.

**Conclusion.** For every ordered height pair, the nine-generator
partner map has rank 42 and nullity 48. The projection of that kernel
onto the three even blocks has rank 30.

The sign product plus both cap generators has scaled coefficient 4 and
swapped-dot coefficient 0. Its even coefficient and both cap
coefficients are nonzero, and its partner rank is 10.

The sign product plus one cap generator minus one third of the other cap
generator has scaled coefficient `4/3` and swapped-dot coefficient 0.
Its even coefficient and both cap coefficients are nonzero, and its
partner rank is 7. The partner kernel is 3-dimensional. In the
coordinate order chi, ts, prod, matched, swapped, parallel, oblique,
swapped_dot, orthogonal, scaled, it is spanned by the following vectors.

On `(1, 2)` and `(2, 1)`:

`(0, 0, 0, 4/5, 0, -3/5, 1, 0, 0, 0)`,
`(0, 0, 0, 0, -5/8, 0, 0, 1/2, 1, 0)`,
`(0, -1/4, -1, 1, 0, 0, 0, 0, 0, 1)`.

On `(1, 3)`:

`(0, 0, 0, -4/5, 0, -3/5, 1, 0, 0, 0)`,
`(0, 0, 0, 0, -5/8, 0, 0, -1/2, 1, 0)`,
`(0, 1/4, 1, 1, 0, 0, 0, 0, 0, 1)`.

On `(3, 1)`:

`(0, 0, 0, -4/5, 0, 3/5, 1, 0, 0, 0)`,
`(0, 0, 0, 0, -5/2, 0, 0, -2, 1, 0)`,
`(0, 1/4, 1, 1, 0, 0, 0, 0, 0, 1)`.

On `(2, 3)` and `(3, 2)`:

`(0, 0, 0, 4/5, 0, 3/5, 1, 0, 0, 0)`,
`(0, 0, 0, 0, -5/2, 0, 0, 2, 1, 0)`,
`(0, -1/4, -1, 1, 0, 0, 0, 0, 0, 1)`.

The sign product plus one swapped-orthogonal generator and the opposite
oblique-matched generator has swapped-dot coefficient 1 and scaled
coefficient 0. Its partner rank is 10. The sign product alone has
partner rank 6, and one swapped-orthogonal generator has partner rank 7.

At heights 1 and 2, the bond on `-e_x` and `-e_y` has lefts
`(-1, -2, -3)` and `(-1, -2, 3)`. The swapped-dot vector, against the
first oblique-matched generator, has rights `(1, -3, -2)` and
`(-1, 2, -3)`, centre pairs `(-1, 0)` and `(1, 2)`, and kernel cross
sum `2`. The scaled coefficient 4 vector, against that cap generator,
has rights `(1, -3, -2)` and `(-3, 2, 1)`, centre pairs `(-3, 0)` and
`(1, -4)`, and kernel cross sum `-4`. Each of the three listed partners
of the coefficient `4/3` vector has kernel cross sum 0 on these two
directions.

**Proof.** The runner enumerates the proper rotations and the alphabet
and builds the ten kernels. On each ordered height pair the even space
has rank 3. With both ratio spans the rank is 9, and with the chirality
cap the rank is 10. The stated supports of the two excluded kernels are
read off the generators. The difference of the swapped-orthogonal
generators has swapped-dot coordinate 2, and the sum of the cap
generators has scaled coordinate 4.

Let `S` send the nine blocks to the sum of their partner maps. The
runner row-reduces `S` and finds rank 42, so the kernel has dimension
48. The three even blocks of that kernel have rank 30.

The coefficient `4/3` vector and the coefficient 4 vector are the stated
combinations of the sign product and the two cap generators. The runner
projects `S` onto each combination. The first projection has rank 7, and
the three listed vectors are independent and span its kernel. The second
projection has rank 10. The swapped-dot combination has rank 10. The
sign product alone has rank 6, and one swapped-orthogonal generator has
rank 7. The two witness bonds, and the three zero bonds of the listed
partners, are direct centre sums on `-e_x` and `-e_y`.

**Obligations.** Proved here: the sum is 9-dimensional, the chirality
cap lies outside it, the nine-generator map has rank 42 and nullity 48,
the scaled coefficient `4/3` has a 3-dimensional partner, and the scaled
coefficient 4 has partner rank 10. The cross sums are `2`, `-4`, and 0.
Cited from the even-span note, and not re-proved: the name of the even
space. Cited from the ratio-span note, and not re-proved: the names of
the two spans. The strongest missing lemma is whether a vector with a
nonzero chirality coefficient, a nonzero even part, and a nonzero part
in each ratio span, with a nonzero swapped-dot or scaled coefficient,
has a ten-kernel partner other than 0.

## What this does not do

- It does not select a scale. The coefficients are witnesses.
- It does not classify every cap ratio.
- It does not take a nonzero chirality coefficient.
- It does not classify every swapped-dot vector in the sum.
- It does not restate the partner kernel of one ratio span, or of the even space with one span, as a new construction.
- It does not claim that the ten-kernel coefficient span is settled.
- It does not claim that the full soldered bond space is classified.
- It does not apply the order-blind converse.
- It does not convert a kernel cross sum into an alphabet mean.
- It does not repeat the bond-space dimension count.
- It does not return to the modulus-3 triple.
- It does not supply a formation site, probability, or rate.

## Runner

`scripts/chiral_pair_even_both_spans_partner_kernel_2026_10_10.py` checks
the nine-generator kernel, the two cap ratios, and the witness bonds.
`TOTAL: PASS=9 FAIL=0`.

## Imports

No formation site, probability, rate, or selected scale is imported.
The proper rotations, the stacked partner kernel, and the witness sums
are enumerated here. The even-span note names the even space. The
ratio-span note names the two spans. The order-blind converse is not
applied.
