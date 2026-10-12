---
claim_id: chiral_pair_bounded_parallel_scale_unequal_dot_caps_partner_kernel_bounded_theorem_note_2026-10-10
claim_type: bounded_theorem
claim_scope: "On every ordered height pair, and for every quintuple of positive integers (t, u, r, s, q) with q at most 2(4r+t), q times the parallel kernel vector plus t times the plus swapped-dot generator plus u times the minus swapped-dot generator plus r times the plus cap and s times the minus cap has parallel coordinate q, swapped-dot coordinate t-u, swapped coordinate -(t+u), orthogonal coordinate t+u, transverse-sign coordinate s-r, sign-product coordinate s-r, matched coordinate 2r+2s, and scaled coordinate 2r+2s. The sum lies in neither ratio span and outside every even space. Four maximal minors have no common nonnegative chirality root on that quintuple, so every nonnegative chirality coefficient has partner rank 10. The case q = 0 is outside this count. Chirality below zero and q above 2(4r+t) are outside this count. The pivot gcd is not this certificate. The ten-kernel coefficient span is not classified. The full soldered bond space is not classified. No scale is selected."
upstream_dependencies:
  - minimal_axioms
  - chiral_pair_even_span_partner_kernel_bounded_theorem_note_2026-10-10
  - chiral_pair_two_parity_excluded_partner_kernel_bounded_theorem_note_2026-10-10
runner: scripts/chiral_pair_bounded_parallel_scale_unequal_dot_caps_partner_kernel_2026_10_10.py
---

# Bounded parallel scale plus unequal swapped-dot scales and two caps

**Date:** 2026-10-12

**Type:** bounded_theorem

**Audit:** unset; independent audit remains a separate lane

**Status:** proposed_retained

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/chiral_pair_bounded_parallel_scale_unequal_dot_caps_partner_kernel_2026_10_10.py`](../scripts/chiral_pair_bounded_parallel_scale_unequal_dot_caps_partner_kernel_2026_10_10.py)

**Parents:** the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md),
[the even span](CHIRAL_PAIR_EVEN_SPAN_PARTNER_KERNEL_BOUNDED_THEOREM_NOTE_2026-10-10.md),
and [the two ratio spans](CHIRAL_PAIR_TWO_PARITY_EXCLUDED_PARTNER_KERNEL_BOUNDED_THEOREM_NOTE_2026-10-10.md).

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "On every ordered height pair, a positive parallel scale at most 2(4r+t), added to unequal positive swapped-dot scales and both positive cap multiples, has partner rank 10 at every nonnegative chirality coefficient."
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "Other generic orbits and higher-rank bond spaces are not classified."
source_of_blocker_text: frontier_question
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "Decide the partner rank, at every chirality coefficient, of a general integer point of the ten-kernel coefficient span. Do not claim the 300-dimensional affine space is classified. Do not return to the bounded parallel quintuple."
conditional_surface_status: "every ordered height pair; positive parallel scale at most 2(4r+t) plus unequal positive swapped-dot scales and both caps; nonnegative chirality"
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

**Target.** On every ordered height pair, decide whether every quintuple
of positive integers `(t, u, r, s, q)` with `q` at most `2(4r+t)` gives
partner rank 10 at every nonnegative chirality coefficient on `q` times
the parallel kernel vector plus `t` times the plus swapped-dot generator
plus `u` times the minus swapped-dot generator plus `r` times the plus
cap and `s` times the minus cap.

**Ansatz.** The sum has parallel coordinate `q`, swapped-dot coordinate
`t-u`, swapped coordinate `-(t+u)`, orthogonal coordinate `t+u`,
transverse-sign coordinate `s-r`, sign-product coordinate `s-r`, matched
coordinate `2r+2s`, and scaled coordinate `2r+2s`. It lies in neither
ratio span and outside every even space. The case `q = 0` is the unequal
swapped-dot quadruple already settled, and it is not this count. A
chirality coefficient below zero is not this count. A parallel scale
above `2(4r+t)` is not this count. The ten-kernel coefficient span is
not this ansatz. The full soldered bond space is not classified.

The kernel cross sum on two perpendicular directions is the sum of the
products of the two centre values. This note does not convert that sum
into an alphabet mean.

**Conclusion.** On every ordered height pair, every quintuple of
positive integers `(t, u, r, s, q)` with `q` at most `2(4r+t)` gives
partner rank 10 at every nonnegative chirality coefficient.

**Proof.** The runner enumerates the proper rotations and the alphabet
and builds the ten kernels. The coordinate identity is linear, so the
five parameter axes determine it, and the points `(2, 3, 5, 7, 11)` and
`(1, 1, 4, 4, 9)` agree. Membership in the plus ratio span is the kernel
spanned by the plus-dot scale and the plus cap. Membership in the minus
ratio span is the kernel spanned by the minus-dot scale and the minus
cap. Membership in the even space of each ordered height pair is only
the origin. Every positive integer quintuple therefore lies in neither
ratio span and outside every even space. Each compressed partner row is
the linear form `t` times the plus swapped-dot row plus `u` times the
minus swapped-dot row plus `r` times the plus-cap row plus `s` times
the minus-cap row plus `q` times the parallel row plus `c` times the
chirality row. The parallel block is attached after the row selection,
so it does not enter the pivot. For `t` nonzero, the row at
`(t, u, r, s, q, c)` equals `t` times the row at
`(1, u/t, r/t, s/t, q/t, c/t)`. Every maximal minor therefore scales by
`t^10`. The runner checks the row identity on every compressed row and
checks that one nonzero maximal minor scales by `2^10`.

Write `M = (2(4r+t)-q)c+(4r+2t)q` and
`L = c(2r-2s+t-u)+2(2r+t)(2s+u)`. On each ordered height pair the
runner matches four maximal minors. The generic minor equals
`1024 c (c-4r-2t)^2 (c-2r-t) M^3` on `(1, 2)`, `(2, 1)`, `(2, 3)`, and
`(3, 2)`, and equals the negative of that product on `(1, 3)` and
`(3, 1)`. The other three minors do not depend on `q`. Up to sign and
the constant `8192` they equal

- `(2r+t-c)(4r+2t-c)^3 L^3`,
- `(4r+2t-c)^2 L^4` on `(1, 2)` and `(2, 1)`, and `c(4r+2t-c)L^4` on
  `(1, 3)`, `(3, 1)`, `(2, 3)`, and `(3, 2)`,
- `c^3(2r+t-c)L^3`.

A polynomial of total degree at most 10 that agrees with one of these
forms on every nonnegative integer point whose six coordinates sum to
at most 10 is that form. There are 8008 such points.

For positive integers `t`, `r`, and `q` with `q` at most `2(4r+t)`, the
coefficient `2(4r+t)-q` is a nonnegative integer and the term
`(4r+2t)q` is a positive integer, so `M` is a positive integer at every
nonnegative integer chirality. The runner checks that comparison on
every simplex point inside the bound. The same predicate is false for
the witness `(t, r, q, c) = (1, 1, 11, 0)` and for a negative chirality.
For positive integers `t, u, r, s`, the factors `2r+t`, `4r+t`, `2s+u`,
`2r+2s+t+u`, `4r+2t`, and `2(4r+t)` are positive. The runner checks the
three specializations `L(0) = 2(2r+t)(2s+u)`,
`L(2r+t) = (2r+t)(2r+2s+t+u)`, and `L(4r+2t) = 2(2r+t)^2`. Thus, inside
the bound, the generic minor is nonzero at a nonnegative chirality
other than `0`, `2r+t`, and `4r+2t`, including every nonnegative
chirality at which `L` vanishes. The second minor is nonzero at
`c = 0`; the third is nonzero at `c = 2r+t`; and the fourth is nonzero
at `c = 4r+2t`. One of the four minors is therefore nonzero at every
nonnegative chirality coefficient, and the partner rank is 10. The
pivot gcd is not this certificate. These four minors are not claimed to
be a monic generator of least degree.

At heights 1 and 2 the bond on `-e_x` and `-e_y` has lefts
`(-1, -2, -3)` and `(-1, -2, 3)`. Against the chirality cap, the sum
has rights `(1, -3, -2)` and `(-3, 2, -1)`. The partner centre pair is
`(1, -1)`. The source centres are `-2t-4r` and `0`, so the centre
pairs are `(-2t-4r, 1)` and `(0, -1)` and the kernel cross sum is
`-2t-4r`. The cross sum does not depend on `u`, `s`, or `q`, and it
does not vanish for positive integers `t` and `r`.

**Obligations.** Proved here: `q` times the parallel kernel vector plus
`t` times the plus swapped-dot generator plus `u` times the minus
swapped-dot generator plus `r` times the plus cap and `s` times the
minus cap, for every quintuple of positive integers `(t, u, r, s, q)`
with `q` at most `2(4r+t)`, on every ordered height pair, for every
nonnegative chirality coefficient. Cited from the even-span note, and
not re-proved: the name of the even space. Cited from the ratio-span
note, and not re-proved: the names of the two spans. The strongest
missing lemma is the partner rank, at every chirality coefficient, of
a general integer point of the ten-kernel coefficient span.

## What this does not do

- It does not select a scale. The vectors are witnesses.
- It does not claim that the pivot gcd degree is independent of `t`, `u`, `r`, `s`, and `q`.
- It does not claim that these four minors are a monic generator of least degree.
- It does not claim that the ten-kernel coefficient span is settled.
- It does not claim that the full soldered bond space is classified.
- It does not claim partner rank 10 for a parallel scale above `2(4r+t)`.
- It does not claim partner rank 10 at a negative chirality coefficient.
- It does not return to the unequal swapped-dot quadruple.
- It does not apply the order-blind converse.
- It does not convert a kernel cross sum into an alphabet mean.
- It does not repeat the bond-space dimension count.
- It does not return to the modulus-3 triple.
- It does not supply a formation site, probability, or rate.

## Runner

`scripts/chiral_pair_bounded_parallel_scale_unequal_dot_caps_partner_kernel_2026_10_10.py`
checks the coordinate identity, the span kernels, the bond, the scale
identity, and the four minor forms. `TOTAL: PASS=9 FAIL=0`.

## Imports

No formation site, probability, rate, or selected scale is imported.
The proper rotations, the stacked partner kernel, and the four minor
forms are enumerated here. The even-span note names the even space.
The ratio-span note names the two spans. The order-blind converse is
not applied.
