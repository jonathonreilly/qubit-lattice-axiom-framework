---
claim_id: chiral_pair_swapped_cross_partner_kernel_bounded_theorem_note_2026-10-10
claim_type: bounded_theorem
claim_scope: "On the 48 signed permutations of (1, 2, 3), the swapped cross is odd on ordered height pairs (1, 2), (2, 1), and (3, 1), and even on (1, 3), (2, 3), and (3, 2). On each odd pair a nonzero scale has partner rank 7, and the partner kernel is the even space of the partner height, so no ten-kernel partner lies outside that space. On (1, 2) and (2, 1) that even space is spanned by the sign product, the oblique dot minus the parallel dot, and the orthogonal cross minus half the swapped cross. On (3, 1) it is spanned by the sign product, the swapped cross, and the parallel dot plus the oblique dot. Its excluded coefficients are 0. On each even pair the even-span note gives partner rank 6 and partner kernel equal to the odd space, which meets the even space only at 0, so every nonzero partner lies outside the even space. At heights 1 and 2 the bond on -e_x and -e_y has lefts (-1, -2, -3) and (-1, -2, 3) and rights (1, -3, -2) and (-1, 2, -3). Against the sign product the centre pairs are (1, -1) and (-1, -1) and the kernel cross sum is 0. Against the chirality cap the centre pairs are (1, -1) and (-1, 1) and the kernel cross sum is -2. Against the matched cross the centre pairs are (1, 0) and (-1, 1) and the kernel cross sum is -1. At heights 1 and 3 the bond on the same directions has lefts (-1, -3, -2) and (-1, -3, 2) and rights (1, -2, -3) and (-2, 3, -1). Against the chirality cap the centre pairs are (-1, 1) and (-1, -1) and the kernel cross sum is 0. Against the sign product the centre pairs are (-1, 1) and (-1, 1) and the kernel cross sum is -2. A vector other than the swapped cross is not in this count. The odd space is not settled. The ten-kernel coefficient span is not classified. The full soldered bond space is not classified. No scale is selected."
upstream_dependencies:
  - minimal_axioms
  - chiral_pair_cross_height_parity_span_cross_moments_bounded_theorem_note_2026-10-10
  - chiral_pair_even_span_partner_kernel_bounded_theorem_note_2026-10-10
runner: scripts/chiral_pair_swapped_cross_partner_kernel_2026_10_10.py
---

# The swapped cross and the even space

**Date:** 2026-10-11

**Type:** bounded_theorem

**Audit:** unset; independent audit remains a separate lane

**Status:** proposed_retained

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/chiral_pair_swapped_cross_partner_kernel_2026_10_10.py`](../scripts/chiral_pair_swapped_cross_partner_kernel_2026_10_10.py)

**Parents:** the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md),
[the parity span](CHIRAL_PAIR_CROSS_HEIGHT_PARITY_SPAN_CROSS_MOMENTS_BOUNDED_THEOREM_NOTE_2026-10-10.md),
and [the even span](CHIRAL_PAIR_EVEN_SPAN_PARTNER_KERNEL_BOUNDED_THEOREM_NOTE_2026-10-10.md).

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "On the pairs where the swapped cross is odd, partner rank is 7 and the partner kernel is the even space, so no ten-kernel partner lies outside that space. On the pairs where it is even, every nonzero partner lies outside the even space."
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "Other generic orbits and higher-rank bond spaces are not classified."
source_of_blocker_text: frontier_question
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "Decide whether a nonzero vector in the odd space, outside the chirality and transverse-sign plane and outside the swapped axis, has a ten-kernel partner outside the even space of the partner height. Do not claim the odd space is settled. Do not claim the ten-kernel coefficient span is settled."
conditional_surface_status: "48 signed permutations of (1, 2, 3); swapped cross; witness directions (-1, 0, 0) and (0, -1, 0)"
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
the swapped cross has a ten-kernel partner outside the even space of the
partner height.

**Ansatz.** The swapped cross is one coefficient vector in the ten-kernel
span. For an ordered height pair it is odd or even at the source height.
On `(1, 2)`, `(2, 1)`, and `(3, 1)` it lies in the odd basis and not in
the even basis. On `(1, 3)`, `(2, 3)`, and `(3, 2)` it lies in the even
basis and not in the odd basis. A vector with both an odd part and an
even part is not this vector. The odd space is not this ansatz. The
ten-kernel coefficient span is not this ansatz. The full soldered bond
space is not classified.

The kernel cross sum on two perpendicular directions is the sum of the
products of the two centre values. This note does not convert that sum
into an alphabet mean.

**Conclusion.** On `(1, 2)`, `(2, 1)`, and `(3, 1)`, a nonzero scale of
the swapped cross has partner rank 7. The partner kernel is the even
space of the partner height. No ten-kernel partner lies outside that
space.

On `(1, 2)` and `(2, 1)` that even space is spanned by the sign product,
the oblique dot minus the parallel dot, and the orthogonal cross minus
half the swapped cross. On `(3, 1)` it is spanned by the sign product,
the swapped cross, and the parallel dot plus the oblique dot. Each
generator has excluded coefficients 0.

On `(1, 3)`, `(2, 3)`, and `(3, 2)` the swapped cross is an even
generator. The even-span note gives it partner rank 6 and partner kernel
equal to the odd space of the partner height. That odd space meets the
even space only at 0, so every nonzero partner lies outside the even
space. On `(1, 3)` the odd space is spanned by the chirality cap, the
transverse-sign cap, the swapped cross, and the parallel dot plus the
oblique dot. On `(2, 3)` and `(3, 2)` it is spanned by the chirality cap,
the transverse-sign cap, the oblique dot minus the parallel dot, and the
orthogonal cross minus half the swapped cross. This note does not
re-prove that partner kernel.

At heights 1 and 2, the bond on `-e_x` and `-e_y` has lefts
`(-1, -2, -3)` and `(-1, -2, 3)`. The rights are `(1, -3, -2)` and
`(-1, 2, -3)`. The swapped values are `1` and `-1`. Against the sign
product the centre pairs are `(1, -1)` and `(-1, -1)`. The first left
contributes `-1`. The second left contributes `1`. The kernel cross sum
is 0. Against the chirality cap the centre pairs are `(1, -1)` and
`(-1, 1)`. The first left contributes `-1`. The second left contributes
`-1`. The kernel cross sum is `-2`. Against the matched cross the centre
pairs are `(1, 0)` and `(-1, 1)`. The first left contributes 0. The
second left contributes `-1`. The kernel cross sum is `-1`.

At heights 1 and 3, the same directions have lefts `(-1, -3, -2)` and
`(-1, -3, 2)`. The rights are `(1, -2, -3)` and `(-2, 3, -1)`. The
swapped values are `-1` and `-1`. Against the chirality cap the centre
pairs are `(-1, 1)` and `(-1, -1)`. The first left contributes `-1`. The
second left contributes `1`. The kernel cross sum is 0. Against the sign
product the centre pairs are `(-1, 1)` and `(-1, 1)`. The first left
contributes `-1`. The second left contributes `-1`. The kernel cross sum
is `-2`.

**Proof.** The runner enumerates the proper rotations and the alphabet
and builds the ten kernels. On each ordered height pair the odd basis of
the source has dimension 4, the even basis has dimension 3, and the two
together have rank 7. The swapped cross lies in the odd basis on the
three odd pairs and in the even basis on the three even pairs.

Fix an odd pair. The partner map of the swapped cross has 10 columns.
The runner row-reduces it, and the same map at scale 2, and both have
rank 7, so the kernel has dimension 3. The three even generators of the
partner height are independent, their excluded coefficients are 0, and
each annihilates every partner row. They therefore span the kernel. A
nonzero scale has the same kernel, because each row is linear in the
source coefficient. No vector outside that even space is a partner. The
chirality cap lies outside it, and so do the matched cross, the swapped
transverse dot, and the scaled cross-dot kernel.

The witness bonds are direct centre sums. The heights 1 and 3 bond is a
centre-sum check of one odd vector and one even vector. It does not
replace the even-span note's partner kernel.

**Obligations.** Proved here: the odd and even membership of the swapped
cross, the rank-7 partner kernel on each odd pair, its equality with the
named even space, and the cross sums `0`, `-2`, and `-1`. Cited from the
even-span note, and not re-proved: on each even pair the partner kernel
is the odd space. Cited from the parity-span note, and not re-proved:
the names of the odd and even bases. The heights 1 and 3 cross sums are
computed here and do not re-prove that kernel. The strongest missing
lemma is whether a nonzero vector in the odd space, outside the
chirality and transverse-sign plane and outside the swapped axis, has a
ten-kernel partner outside the even space of the partner height.

## What this does not do

- It does not select a scale. The coefficients are witnesses.
- It does not give the odd swapped cross a partner outside the even space.
- It does not re-prove the even-span partner kernel.
- It does not take a vector other than the swapped cross.
- It does not claim that the odd space is settled.
- It does not claim that the ten-kernel coefficient span is settled.
- It does not claim that the full soldered bond space is classified.
- It does not apply the order-blind converse.
- It does not convert a kernel cross sum into an alphabet mean.
- It does not repeat the bond-space dimension count.
- It does not return to the modulus-3 triple.
- It does not supply a formation site, probability, or rate.

## Runner

`scripts/chiral_pair_swapped_cross_partner_kernel_2026_10_10.py` checks
the membership, the odd-pair partner kernels, and the witness bonds.
`TOTAL: PASS=9 FAIL=0`.

## Imports

No formation site, probability, rate, or selected scale is imported.
The proper rotations, the odd-pair partner kernels, and the witness sums
are enumerated here. The parity-span note names the odd and even bases.
The even-span note names the partner kernel on the even pairs. The
order-blind converse is not applied.
