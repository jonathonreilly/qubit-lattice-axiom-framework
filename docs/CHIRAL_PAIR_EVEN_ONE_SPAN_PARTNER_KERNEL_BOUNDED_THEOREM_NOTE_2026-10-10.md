---
claim_id: chiral_pair_even_one_span_partner_kernel_bounded_theorem_note_2026-10-10
claim_type: bounded_theorem
claim_scope: "On the 48 signed permutations of (1, 2, 3), the even space, the chirality cap, and one ratio span form a 7-dimensional sum. The swapped transverse dot sits only on the swapped-orthogonal generator of that span, and the scaled cross-dot kernel sits only on its cap generator. The seven-generator partner map has rank 46 and nullity 24. Its kernel is the product of the odd space of the partner height on the even blocks, the even space of the partner height on the chirality block, and the partner ratio span on the span blocks. Those three spaces meet pairwise only at 0. A nonzero vector in the sum has a nonzero ten-kernel partner if and only if it lies in exactly one summand. A nonzero swapped-dot or scaled coefficient has such a partner exactly when the vector lies in the ratio span. On -e_x and -e_y, the lefts are (-1, -2, -3) and (-1, -2, 3). The sign product plus the swapped-orthogonal generator, against that generator, has rights (1, -2, -3) and (3, 2, -1), centre pairs (-1, 0) and (-1, 2), and kernel cross sum -2. The sign product plus the cap generator, against that generator, has rights (1, -3, -2) and (-3, 2, 1), centre pairs (-3, 0) and (1, -4), and kernel cross sum -4. A vector that meets the other ratio span is not in this count. The ten-kernel coefficient span is not classified. The full soldered bond space is not classified. No scale is selected."
upstream_dependencies:
  - minimal_axioms
  - chiral_pair_even_span_partner_kernel_bounded_theorem_note_2026-10-10
  - chiral_pair_two_parity_excluded_partner_kernel_bounded_theorem_note_2026-10-10
runner: scripts/chiral_pair_even_one_span_partner_kernel_2026_10_10.py
---

# The even space plus one ratio span pairs only on one summand

**Date:** 2026-10-11

**Type:** bounded_theorem

**Audit:** unset; independent audit remains a separate lane

**Status:** proposed_retained

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/chiral_pair_even_one_span_partner_kernel_2026_10_10.py`](../scripts/chiral_pair_even_one_span_partner_kernel_2026_10_10.py)

**Parents:** the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md),
[the even span](CHIRAL_PAIR_EVEN_SPAN_PARTNER_KERNEL_BOUNDED_THEOREM_NOTE_2026-10-10.md),
and [the two ratio spans](CHIRAL_PAIR_TWO_PARITY_EXCLUDED_PARTNER_KERNEL_BOUNDED_THEOREM_NOTE_2026-10-10.md).

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "In the sum of the even space, the chirality cap, and one ratio span, a nonzero swapped-dot or scaled coefficient has a nonzero ten-kernel partner exactly on that ratio span."
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "Other generic orbits and higher-rank bond spaces are not classified."
source_of_blocker_text: frontier_question
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "Decide whether a vector that meets both ratio spans and has a nonzero even part, with a nonzero coefficient on the swapped transverse dot or the scaled cross-dot kernel, has a ten-kernel partner other than 0. Inside the even space, the chirality cap, and one ratio span, such a partner exists exactly on that ratio span. Do not claim the ten-kernel coefficient span is settled."
conditional_surface_status: "48 signed permutations of (1, 2, 3); even space, chirality cap, and one ratio span; witness directions (-1, 0, 0) and (0, -1, 0)"
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
a vector outside the span of the chirality cap and the two ratio spans,
with a nonzero coefficient on the swapped transverse dot or the scaled
cross-dot kernel, has a ten-kernel partner other than 0.

**Ansatz.** One ratio span, the even space of the source height, and the
chirality cap. Their sum is 7-dimensional. The swapped transverse dot
appears only on the swapped-orthogonal generator of the span, and the
scaled cross-dot kernel appears only on its cap generator. The even
generators and the chirality cap carry neither coordinate. A vector that
meets the other ratio span is not in this ansatz. The ten-kernel
coefficient span is not this ansatz. The full soldered bond space is not
classified.

The kernel cross sum on two perpendicular directions is the sum of the
products of the two centre values. This note does not convert that sum
into an alphabet mean.

**Conclusion.** For every ordered height pair and either ratio span, a
nonzero vector in the sum has a nonzero ten-kernel partner if and only
if it lies in exactly one of the three summands. The partner is then the
odd space of the partner height, the even space of the partner height,
or the partner ratio span, according to the summand. The partner ratio
span is the same span on height pairs `(1, 2)`, `(2, 1)`, `(2, 3)`, and
`(3, 2)`, and the other ratio span on `(1, 3)` and `(3, 1)`. If two
summands are nonzero, the partner rank is 10.

A nonzero swapped-dot or scaled coefficient forces a nonzero span part.
Inside this sum, that vector has a ten-kernel partner other than 0
exactly when the even part and the chirality coefficient both vanish, so
the vector lies in the ratio span. The same block kernel covers both
excluded coordinates.

At heights 1 and 2, the bond on `-e_x` and `-e_y` has lefts
`(-1, -2, -3)` and `(-1, -2, 3)`. The sign product plus the
swapped-orthogonal generator has values `-1` and `-1`. Against that
generator, the rights are `(1, -2, -3)` and `(3, 2, -1)`, the centre
pairs are `(-1, 0)` and `(-1, 2)`, and the kernel cross sum is `-2`.
The first left contributes 0. The second left contributes `-2`.

The sign product plus the cap generator, against that generator, has
rights `(1, -3, -2)` and `(-3, 2, 1)`, centre pairs `(-3, 0)` and
`(1, -4)`, and kernel cross sum `-4`.

**Proof.** The runner enumerates the proper rotations and the alphabet
and builds the ten kernels. Each ratio span has rank 3. With the even
space and the chirality cap, the rank is 7. The stated supports of the
two excluded kernels are read off the generators.

On each ordered height pair, the odd space of the partner height, the
even space of that height, and the partner ratio span meet pairwise only
at 0. Let `S` send the seven blocks to the sum of their partner maps.
The runner row-reduces `S` and finds rank 46, so the kernel has
dimension 24. Every kernel vector has its even blocks in the odd space,
its chirality block in the even space, and its span blocks in the
partner span. Those spaces have dimensions 4, 3, and 3, so the tuples
of that form are 24-dimensional and equal the kernel.

A pure tensor lies in the kernel if and only if every nonzero block
group forces the partner into the corresponding space. Two nonzero
groups force the partner into an intersection, so the partner is 0 and
the rank is 10. One nonzero group leaves the whole corresponding space,
so the rank is 6 for a nonzero even vector and 7 for the chirality cap
or a nonzero span vector. The runner checks the sign product plus each
excluded generator, the chirality cap plus the swapped-orthogonal
generator, and the swapped-orthogonal generator alone, on every ordered
height pair. The two witness bonds are direct centre sums.

**Obligations.** Proved here: the seven-generator kernel is the product
of the three spaces, two nonzero summands have partner rank 10, and a
nonzero excluded coefficient inside the sum has a nonzero partner
exactly on the ratio span. The cross sums are `-2` and `-4`. Cited from
the even-span note, and not re-proved: the names of the even space and
its odd partner. Cited from the ratio-span note, and not re-proved: the
names of the two spans and the exchange of their partners. The strongest
missing lemma is whether a vector that meets both ratio spans and has a
nonzero even part, with a nonzero swapped-dot or scaled coefficient,
has a ten-kernel partner other than 0.

## What this does not do

- It does not select a scale. The coefficients are witnesses.
- It does not give two nonzero summands a nonzero partner.
- It does not take a vector that meets the other ratio span.
- It does not restate the partner kernel of the even space, or of one ratio span, as a new construction.
- It does not claim that the ten-kernel coefficient span is settled.
- It does not claim that the full soldered bond space is classified.
- It does not apply the order-blind converse.
- It does not convert a kernel cross sum into an alphabet mean.
- It does not repeat the bond-space dimension count.
- It does not return to the modulus-3 triple.
- It does not supply a formation site, probability, or rate.

## Runner

`scripts/chiral_pair_even_one_span_partner_kernel_2026_10_10.py` checks
the seven-generator kernel and the witness bonds.
`TOTAL: PASS=7 FAIL=0`.

## Imports

No formation site, probability, rate, or selected scale is imported.
The proper rotations, the stacked partner kernel, and the witness sums
are enumerated here. The even-span note names the even space and its
odd partner. The ratio-span note names the two spans. The order-blind
converse is not applied.
