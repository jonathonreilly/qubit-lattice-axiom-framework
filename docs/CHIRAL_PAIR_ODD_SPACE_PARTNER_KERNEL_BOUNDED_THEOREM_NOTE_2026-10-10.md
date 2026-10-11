---
claim_id: chiral_pair_odd_space_partner_kernel_bounded_theorem_note_2026-10-10
claim_type: bounded_theorem
claim_scope: "On the 48 signed permutations of (1, 2, 3), the odd space of an ordered height pair is the rational span of the odd basis of the source height. It is 4-dimensional, its excluded coefficients are 0, and it meets the even basis only at 0. For every ordered pair of absolute heights among 1, 2, and 3, every nonzero vector in that space has partner rank 7, and the partner kernel is the even space of the partner height. On partner pairs (1, 2), (2, 1), and (1, 3) that even space is spanned by the sign product, the oblique dot minus the parallel dot, and the orthogonal cross minus half the swapped cross. On pairs (3, 1), (2, 3), and (3, 2) it is spanned by the sign product, the swapped cross, and the parallel dot plus the oblique dot. The parallel-oblique sum lies in the odd space at heights 1 and 2, outside the chirality and transverse-sign plane, with swapped coefficient 0. At those heights the bond on -e_x and -e_y has lefts (-1, -2, -3) and (-1, -2, 3) and rights (1, -2, -3) and (-1, 2, -3). Against the sign product the centre pairs are (-1, -1) and (1, -1) and the kernel cross sum is 0. Against the chirality cap the centre pairs are (-1, -1) and (1, 1) and the kernel cross sum is 2. Against the matched cross the centre pairs are (-1, 0) and (1, 1) and the kernel cross sum is 1. A vector with both an odd part and an even part is not in this count. The ten-kernel coefficient span is not classified. The full soldered bond space is not classified. No scale is selected."
upstream_dependencies:
  - minimal_axioms
  - chiral_pair_cross_height_parity_span_cross_moments_bounded_theorem_note_2026-10-10
  - chiral_pair_swapped_cross_partner_kernel_bounded_theorem_note_2026-10-10
runner: scripts/chiral_pair_odd_space_partner_kernel_2026_10_10.py
---

# The odd space and its even partner

**Date:** 2026-10-11

**Type:** bounded_theorem

**Audit:** unset; independent audit remains a separate lane

**Status:** proposed_retained

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/chiral_pair_odd_space_partner_kernel_2026_10_10.py`](../scripts/chiral_pair_odd_space_partner_kernel_2026_10_10.py)

**Parents:** the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md),
[the parity span](CHIRAL_PAIR_CROSS_HEIGHT_PARITY_SPAN_CROSS_MOMENTS_BOUNDED_THEOREM_NOTE_2026-10-10.md),
and [the swapped cross](CHIRAL_PAIR_SWAPPED_CROSS_PARTNER_KERNEL_BOUNDED_THEOREM_NOTE_2026-10-10.md).

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Every nonzero vector in the odd space has partner rank 7, and the partner kernel is the even space of the partner height."
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "Other generic orbits and higher-rank bond spaces are not classified."
source_of_blocker_text: frontier_question
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "Decide whether a vector with both an odd part and an even part has a ten-kernel partner other than 0. The odd space pairs only with the even space. Do not claim the ten-kernel coefficient span is settled."
conditional_surface_status: "48 signed permutations of (1, 2, 3); odd basis of the source height; witness directions (-1, 0, 0) and (0, -1, 0)"
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
a nonzero vector in the odd space, outside the chirality and
transverse-sign plane and outside the swapped axis, has a ten-kernel
partner outside the even space of the partner height.

**Ansatz.** For an ordered height pair, the odd space is the rational
span of the odd basis of the source height. On source pairs `(1, 2)`,
`(2, 1)`, and `(3, 1)` that basis is the chirality cap, the
transverse-sign cap, the swapped cross, and the parallel dot plus the
oblique dot. On `(1, 3)`, `(2, 3)`, and `(3, 2)` it is the chirality
cap, the transverse-sign cap, the oblique dot minus the parallel dot,
and the orthogonal cross minus half the swapped cross. Each generator
has excluded coefficients 0. The parallel-oblique sum is the last
generator on the first three pairs. It lies outside the chirality and
transverse-sign plane, and its swapped coefficient is 0. A vector with
both an odd part and an even part is not in this ansatz. The ten-kernel
coefficient span is not this ansatz. The full soldered bond space is
not classified.

The kernel cross sum on two perpendicular directions is the sum of the
products of the two centre values. This note does not convert that sum
into an alphabet mean.

**Conclusion.** For every ordered pair of heights among `{1, 2, 3}`,
every nonzero vector in the odd space has partner rank 7. The partner
kernel is the even space of the partner height. No ten-kernel partner
lies outside that space.

On partner pairs `(1, 2)`, `(2, 1)`, and `(1, 3)` the even space is
spanned by the sign product, the oblique dot minus the parallel dot,
and the orthogonal cross minus half the swapped cross. On pairs
`(3, 1)`, `(2, 3)`, and `(3, 2)` it is spanned by the sign product, the
swapped cross, and the parallel dot plus the oblique dot. These
generators have excluded coefficients 0. The chirality cap, the matched
cross, the swapped transverse dot, and the scaled cross-dot kernel lie
outside that space.

The coefficient tuples `(1, 0, 0, 0)`, `(0, 0, 0, 1)`, and
`(1, 1, 1, 1)` each have partner rank 7. The first is the chirality
cap. The second is the last odd generator. The third is a mixture of
all four generators.

At heights 1 and 2, the bond on `-e_x` and `-e_y` has lefts
`(-1, -2, -3)` and `(-1, -2, 3)`. The rights are `(1, -2, -3)` and
`(-1, 2, -3)`. The parallel-oblique values are `-1` and `1`. Against
the sign product the centre pairs are `(-1, -1)` and `(1, -1)`. The
first left contributes `1`. The second left contributes `-1`. The
kernel cross sum is 0. Against the chirality cap the centre pairs are
`(-1, -1)` and `(1, 1)`. The first left contributes `1`. The second
left contributes `1`. The kernel cross sum is `2`. Against the matched
cross the centre pairs are `(-1, 0)` and `(1, 1)`. The first left
contributes 0. The second left contributes `1`. The kernel cross sum
is `1`.

**Proof.** The runner enumerates the proper rotations and the alphabet
and builds the ten kernels. On each ordered height pair the odd basis
has dimension 4, the even basis has dimension 3, and the two together
have rank 7. The odd generators have excluded coefficients 0. The
parallel-oblique sum lies in the odd basis of heights 1 and 2, and
adjoining it to the chirality and transverse-sign plane raises the rank
from 2 to 3.

Each odd generator has partner rank 7. The even space of the partner
height has dimension 3, its excluded coefficients are 0, and each of
its generators annihilates every partner row. That space is therefore
the kernel of each odd generator.

Fix an ordered height pair. Let `M_1`, `M_2`, `M_3`, and `M_4` be the
partner maps of the four odd generators, and let `S` send
`(u, v, w, x)` to `M_1 u + M_2 v + M_3 w + M_4 x`. The partner equation
for odd coefficients `(a, b, c, d)` is `S(a w, b w, c w, d w) = 0`.
The runner row-reduces `S` and finds rank 28, so the kernel has
dimension 12. Every kernel vector has its four blocks in the even
space `E`. That space is 3-dimensional, so the tuples with all four
blocks in `E` form a 12-dimensional space and equal the kernel.

Thus `S(a w, b w, c w, d w) = 0` if and only if `a w`, `b w`, `c w`,
and `d w` all lie in `E`. If `(a, b, c, d)` is not `(0, 0, 0, 0)`, then
`w` lies in `E`, every vector of `E` occurs, and the partner rank is 7.
The runner checks the three named coefficient tuples on every ordered
height pair. The witness bond is a direct centre sum.

**Obligations.** Proved here: the odd space is 4-dimensional and meets
the even basis only at 0, every nonzero vector has partner rank 7, the
partner kernel is the named even space, and the cross sums are 0, `2`,
and `1`. Cited from the parity-span note, and not re-proved: the names
of the odd and even bases. The swapped-cross note first separated the
swapped axis by parity. This count includes that axis and does not
treat it as a separate case. The strongest missing lemma is whether a
vector with both an odd part and an even part has a ten-kernel partner
other than 0.

## What this does not do

- It does not select a scale. The coefficients are witnesses.
- It does not give an odd vector a partner outside the even space.
- It does not take a vector with both an odd part and an even part.
- It does not re-prove the even-span partner kernel.
- It does not claim that the ten-kernel coefficient span is settled.
- It does not claim that the full soldered bond space is classified.
- It does not apply the order-blind converse.
- It does not convert a kernel cross sum into an alphabet mean.
- It does not repeat the bond-space dimension count.
- It does not return to the modulus-3 triple.
- It does not supply a formation site, probability, or rate.

## Runner

`scripts/chiral_pair_odd_space_partner_kernel_2026_10_10.py` checks the
odd space, the generator kernels, the stacked rank, and the witness
bond. `TOTAL: PASS=9 FAIL=0`.

## Imports

No formation site, probability, rate, or selected scale is imported.
The proper rotations, the odd-space partner kernels, the stacked rank,
and the witness sums are enumerated here. The parity-span note names
the odd and even bases. The swapped-cross note names the swapped axis.
The order-blind converse is not applied.
