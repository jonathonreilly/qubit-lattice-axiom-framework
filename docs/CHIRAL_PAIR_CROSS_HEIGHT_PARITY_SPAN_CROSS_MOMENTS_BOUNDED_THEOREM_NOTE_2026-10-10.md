---
claim_id: chiral_pair_cross_height_parity_span_cross_moments_bounded_theorem_note_2026-10-10
claim_type: bounded_theorem
claim_scope: "On the 48 signed permutations of (1, 2, 3), the parity span of an opposite-height basis is the rational span of the chirality cap, the transverse-sign cap, their sign product, the swapped transverse cross, the parallel transverse dot, the matched oblique dot, and the orthogonal swapped cross. The matched cross, the swapped transverse dot, and the scaled cross-dot kernel lie outside it. For a height and a partner height, that span splits into an odd space of dimension 4 and an even space of dimension 3, intersecting only at 0. On the two centres that meet those heights, an odd vector takes opposite values and an even vector takes equal values. For coefficient vectors in the two parity spans, every cross moment vanishes if and only if the odd coefficient vectors are not both nonzero and the even coefficient vectors are not both nonzero. The height-1 and height-2 chirality caps, and the two sign-product caps, each have witness moment 97/96. The swapped crosses at heights 1 and 2 have witness moment 95/96. The swapped crosses at heights 2 and 3 have witness moment 95/96. The parallel-oblique sum with the other-height sign product, at coefficient 1/2, has every cross moment equal to 0, takes values 1/2, 1, and 3/2, and has every one-neighbour and two-direction mean equal to 1. The swapped crosses at heights 1 and 3 have every cross moment equal to 0. The matched cross, the swapped transverse dot, and the scaled kernel are not in this ansatz. The full soldered bond space is not classified. No scale is selected."
upstream_dependencies:
  - minimal_axioms
  - order_blind_nearest_neighbour_formation_independence_beyond_neighbours_unsoldered_constancy_and_soldered_escape_bounded_theorem_note_2026-09-22
  - chiral_pair_opposite_height_basis_mixtures_product_means_bounded_theorem_note_2026-10-10
  - chiral_pair_scaled_cross_dot_bases_opposite_height_ansatz_bounded_theorem_note_2026-10-10
runner: scripts/chiral_pair_cross_height_parity_span_cross_moments_2026_10_10.py
---

# Parity span cross moments on two opposite-height bases

**Date:** 2026-10-10

**Type:** bounded_theorem

**Audit:** unset; independent audit remains a separate lane

**Status:** proposed_retained

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/chiral_pair_cross_height_parity_span_cross_moments_2026_10_10.py`](../scripts/chiral_pair_cross_height_parity_span_cross_moments_2026_10_10.py)

**Parents:** the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md),
[the order-blind formation note](ORDER_BLIND_NEAREST_NEIGHBOUR_FORMATION_INDEPENDENCE_BEYOND_NEIGHBOURS_UNSOLDERED_CONSTANCY_AND_SOLDERED_ESCAPE_BOUNDED_THEOREM_NOTE_2026-09-22.md),
[the opposite-height mixture note](CHIRAL_PAIR_OPPOSITE_HEIGHT_BASIS_MIXTURES_PRODUCT_MEANS_BOUNDED_THEOREM_NOTE_2026-10-10.md),
and the [scaled cross-dot basis note](CHIRAL_PAIR_SCALED_CROSS_DOT_BASES_OPPOSITE_HEIGHT_ANSATZ_BOUNDED_THEOREM_NOTE_2026-10-10.md).

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Inside the parity span, cross moments vanish exactly when the odd parts are not both nonzero and the even parts are not both nonzero."
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "Other generic orbits and higher-rank bond spaces are not classified."
source_of_blocker_text: frontier_question
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "Decide whether a nonzero coefficient on the matched cross, the swapped transverse dot, or the scaled cross-dot kernel can pair with a nonzero vector at the other height and still have every cross moment equal to 0. Do not claim the ten-kernel coefficient span is settled."
conditional_surface_status: "48 signed permutations of (1, 2, 3); parity span of two opposite-height bases; witness far ends (1, -3, -2), (-3, 2, -1), (2, -1, -3), and (-1, 3, -2)"
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

**Target.** On the 48 signed permutations of `(1, 2, 3)`, decide which
rational coefficient vectors in the parity spans of two opposite-height
bases have every cross moment equal to 0.

**Ansatz.** The parity span is the rational span of seven kernels: the
chirality cap, the transverse-sign cap, their sign product, the swapped
transverse cross, the parallel transverse dot, the matched oblique dot,
and the orthogonal swapped cross. The matched transverse cross, the
swapped transverse dot, and the scaled cross-dot kernel are outside
this span. Each raises the rank of the seven vectors from 7 to 8. The
ten-kernel coefficient span is not this ansatz. The full soldered bond
space is not classified.

For absolute heights `h` and `k`, the two centres that meet height `h`
in one direction and height `k` in a perpendicular direction differ by
the sign of the unused coordinate. A vector in the parity span is odd,
relative to that partner, when its two centre values are always
negatives, and even when those values are always equal. The odd and
even spaces intersect only at 0.

At heights `(1, 2)`, `(2, 1)`, and `(3, 1)` the odd basis is the
chirality cap, the transverse-sign cap, the swapped cross, and the sum
of the parallel and oblique dots. The even basis is the sign product,
the difference of the oblique and parallel dots, and the orthogonal
cross minus half the swapped cross. At heights `(1, 3)`, `(2, 3)`, and
`(3, 2)` those two bases are exchanged, except that the chirality cap
and the transverse-sign cap stay odd and the sign product stays even.

**Conclusion.** Let `p` and `q` be the odd and even coefficient vectors
of the first height, and let `r` and `s` be those of the second height,
in the bases just named. Every cross moment vanishes if and only if
every product `p_a r_b` is 0 and every product `q_c s_d` is 0. Over the
rationals this says that `p` or `r` is 0, and `q` or `s` is 0.

In particular, an odd vector at one height and an even vector at the
other have every cross moment equal to 0, and so does every pair in
which either coefficient vector is 0. Two nonzero odd vectors do not,
and two nonzero even vectors do not. A vector with both parts nonzero
pairs only with 0. The orthogonal cross at heights 1 and 2 is such a
vector: it is half the swapped cross plus an even basis vector.

The height-1 and height-2 chirality caps, at coefficient `1/2`, have
moment `97/96` on `-e_x` and `-e_y` at `(1, -3, -2)` and `(-3, 2, -1)`.
The two sign-product caps have the same moment on those bonds. The
swapped crosses at those heights have moment `95/96` there. The swapped
crosses at heights 2 and 3 have moment `95/96` on the same directions
at `(2, -1, -3)` and `(-1, 3, -2)`. The swapped crosses at heights 1
and 3 have every cross moment equal to 0, because one is even and the
other is odd.

The sum of the parallel and oblique dots at height 1, plus the height-2
sign product, at coefficient `1/2`, takes values `1/2`, `1`, and `3/2`.
Every one-neighbour mean and every two-direction mean equals 1. Every
far-end sum equals 48. Each record meets at most two live directions,
and those directions are not opposites, so every neighbour product has
mean 1. Theorem 2's converse applies to this one family. It is not
applied to a pair whose cross moment is not 0, and it is not applied to
a coefficient large enough to leave the positive cone.

**Proof.** The runner enumerates the proper rotations and the alphabet,
builds the ten kernels, and row-reduces the two-centre sign conditions.
Each of the six ordered height-partner pairs has odd dimension 4, even
dimension 3, and intersection 0, with the bases named above. The seven
vectors are independent. Each excluded kernel raises that rank to 8.

On two centres, an odd value is `(t, -t)` and an even value is
`(u, u)`. The cross sum is `2 t_1 t_2 + 2 u_1 u_2`. Odd does not meet
even. The runner assembles one row for every far-end pair, with one
column for each odd-odd coefficient product and each even-even
coefficient product. That is 25 columns. On each of the three unordered
height pairs the row rank is 25, so every such product is 0. Over the
rationals, the odd products all vanish only when one odd vector is 0,
and the even products all vanish only when one even vector is 0. The
same identity gives the converse: if one odd vector is 0 and one even
vector is 0, every cross sum is 0.

The witness moments are the normalised two-centre sums. Both orbit
signs on the first witness are `-1` for the chirality caps, and the
sign products are `+1`, so each failing cap pair has kernel cross sum
`2`. At coefficient `1/2` the excess sum is `1/2` and the mean is
`1 + (1/2)/48 = 97/96`. The swapped pair at heights 1 and 2 has kernel
cross sum `-2`, so the mean is `95/96`. The heights 2 and 3 witness has
the same excess.

The passing odd-even mixture is supported on one height in each
direction. Its values are the stated set. Summing over either endpoint
gives 48. The direct scan finds no nonzero cross sum. A third direction
cannot carry a third factor, because each height meets a record in only
one direction.

**Obligations.** Proved here: the odd and even bases, their dimensions
and trivial intersection, the exclusion of the three named kernels, the
rank-25 product equations, the witness moments `97/96` and `95/96`, the
passing cross moments, the value set, the endpoint sums, and the
live-direction bound. Cited from Theorem 2, and not re-proved: bond
symmetry together with every product mean equal to 1 makes a strictly
positive family order-blind on every window. The converse is applied
only to the odd-even mixture at coefficient `1/2`. Cited from the
basis note, and not re-proved: the ten named kernels are a basis of one
opposite-height ansatz. Cited from the one-height mixture note, and not
re-proved: a mixture supported on one height is bond-symmetric and
soldered, and a bond meets only one height. The strongest missing lemma
is whether a nonzero coefficient on the matched cross, the swapped
transverse dot, or the scaled cross-dot kernel can pair with a nonzero
vector at the other height and still have every cross moment equal to 0.

## What this does not do

- It does not select a scale. The coefficient `1/2` is a witness.
- It does not put the matched cross, the swapped transverse dot, or the
  scaled cross-dot kernel into the parity span.
- It does not claim that the ten-kernel coefficient span is settled.
- It does not claim that the full soldered bond space is classified.
- It does not apply Theorem 2's converse to a failing pair.
- It does not repeat the one-height classification.
- It does not repeat the bond-space dimension count.
- It does not return to the modulus-3 triple.
- It does not supply a formation site, probability, or rate.

## Runner

`scripts/chiral_pair_cross_height_parity_span_cross_moments_2026_10_10.py`
checks the parity bases, the product rank, and the witness moments.
`TOTAL: PASS=9 FAIL=0`.

## Imports

No formation site, probability, rate, or selected scale is imported.
The proper rotations, the parity bases, and the moment sums are
enumerated here. Theorem 2's converse is applied to the one positive
odd-even mixture. The basis note supplies the ten-kernel basis. The
one-height mixture note supplies bond symmetry on a single height.
