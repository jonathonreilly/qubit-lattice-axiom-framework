---
claim_id: chiral_pair_unequal_swapped_dot_scales_two_cap_multiples_partner_kernel_bounded_theorem_note_2026-10-10
claim_type: bounded_theorem
claim_scope: "On every ordered height pair, and for every quadruple of positive integers (t, u, r, s), t times the plus swapped-dot generator plus u times the minus swapped-dot generator plus r times the plus cap and s times the minus cap has swapped-dot coordinate t-u, swapped coordinate -(t+u), orthogonal coordinate t+u, transverse-sign coordinate s-r, sign-product coordinate s-r, matched coordinate 2r+2s, and scaled coordinate 2r+2s. The sum lies in neither ratio span and outside every even space. Four maximal minors have no common chirality root on that quadruple, so every chirality coefficient has partner rank 10. The pivot gcd is not this certificate. The ten-kernel coefficient span is not classified. The full soldered bond space is not classified. No scale is selected."
upstream_dependencies:
  - minimal_axioms
  - chiral_pair_even_span_partner_kernel_bounded_theorem_note_2026-10-10
  - chiral_pair_two_parity_excluded_partner_kernel_bounded_theorem_note_2026-10-10
runner: scripts/chiral_pair_unequal_swapped_dot_scales_two_cap_multiples_partner_kernel_2026_10_10.py
---

# Unequal swapped-dot scales plus two cap multiples

**Date:** 2026-10-12

**Type:** bounded_theorem

**Audit:** unset; independent audit remains a separate lane

**Status:** proposed_retained

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/chiral_pair_unequal_swapped_dot_scales_two_cap_multiples_partner_kernel_2026_10_10.py`](../scripts/chiral_pair_unequal_swapped_dot_scales_two_cap_multiples_partner_kernel_2026_10_10.py)

**Parents:** the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md),
[the even span](CHIRAL_PAIR_EVEN_SPAN_PARTNER_KERNEL_BOUNDED_THEOREM_NOTE_2026-10-10.md),
and [the two ratio spans](CHIRAL_PAIR_TWO_PARITY_EXCLUDED_PARTNER_KERNEL_BOUNDED_THEOREM_NOTE_2026-10-10.md).

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "On every ordered height pair, unequal positive scales of the two swapped-dot generators plus every pair of positive cap multiples have partner rank 10 at every chirality coefficient."
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "Other generic orbits and higher-rank bond spaces are not classified."
source_of_blocker_text: frontier_question
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "Decide the partner rank, at every chirality coefficient, of a general integer point of the ten-kernel coefficient span. Do not claim the 300-dimensional affine space is classified."
conditional_surface_status: "every ordered height pair; unequal positive swapped-dot scales plus every pair of positive cap multiples"
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

**Target.** On every ordered height pair, decide whether every quadruple
of positive integers `(t, u, r, s)` gives partner rank 10 at every
chirality coefficient on `t` times the plus swapped-dot generator plus
`u` times the minus swapped-dot generator plus `r` times the plus cap
and `s` times the minus cap.

**Ansatz.** The sum has swapped-dot coordinate `t-u`, swapped coordinate
`-(t+u)`, orthogonal coordinate `t+u`, transverse-sign coordinate `s-r`,
sign-product coordinate `s-r`, matched coordinate `2r+2s`, and scaled
coordinate `2r+2s`. It lies in neither ratio span and outside every even
space. The case `t = u` is the equal-scale count already settled. The
ten-kernel coefficient span is not this ansatz. The full soldered bond
space is not classified.

The kernel cross sum on two perpendicular directions is the sum of the
products of the two centre values. This note does not convert that sum
into an alphabet mean.

**Conclusion.** On every ordered height pair, every quadruple of
positive integers `(t, u, r, s)` gives partner rank 10 at every
chirality coefficient.

**Proof.** The runner enumerates the proper rotations and the alphabet
and builds the ten kernels. The coordinate identity is linear, so the
four parameter axes determine it, and the points `(2, 3, 5, 7)` and
`(1, 1, 4, 4)` agree. Membership in the plus ratio span is the kernel
spanned by the plus-dot scale and the plus cap. Membership in the minus
ratio span is the kernel spanned by the minus-dot scale and the minus
cap. Membership in the even space of each ordered height pair is only
the origin. Every positive integer quadruple therefore lies in neither
ratio span and outside every even space. Each compressed partner row is
the linear form `t` times the plus swapped-dot row plus `u` times the
minus swapped-dot row plus `r` times the plus-cap row plus `s` times
the minus-cap row plus `c` times the chirality row. For `t` nonzero,
the row at `(t, u, r, s, c)` equals `t` times the row at
`(1, u/t, r/t, s/t, c/t)`. Every maximal minor therefore scales by
`t^10`. The runner checks the row identity on every compressed row and
checks that one nonzero maximal minor scales by `2^10`.

Write `L = c(2r-2s+t-u)+2(2r+t)(2s+u)`. On each ordered height pair the
runner matches four maximal minors, up to sign and the constant
`8192`, with

- `c^4(4r+t)^3(2r+t-c)(4r+2t-c)^2`,
- `(2r+t-c)(4r+2t-c)^3 L^3`,
- `(4r+2t-c)^2 L^4` on `(1, 2)` and `(2, 1)`, and `c(4r+2t-c)L^4` on
  `(1, 3)`, `(3, 1)`, `(2, 3)`, and `(3, 2)`,
- `c^3(2r+t-c)L^3`.

A polynomial of total degree at most 10 that agrees with one of these
forms on every nonnegative integer point whose coordinates sum to at
most 10 is that form. For positive integers `t, u, r, s`, the factors
`2r+t`, `4r+t`, `2s+u`, and `2r+2s+t+u` are positive. The runner checks
the three specializations `L(0) = 2(2r+t)(2s+u)`,
`L(2r+t) = (2r+t)(2r+2s+t+u)`, and `L(4r+2t) = 2(2r+t)^2`. Thus the
first minor is nonzero when `c` is not `0`, `2r+t`, or `4r+2t`; the
second is nonzero at `c = 0`; the third is nonzero at `c = 2r+t`; and
the fourth is nonzero at `c = 4r+2t`. One of the four minors is
therefore nonzero at every chirality coefficient, and the partner rank
is 10. The pivot gcd is not this certificate. These four minors are
not claimed to be a monic generator of least degree.

At heights 1 and 2 the bond on `-e_x` and `-e_y` has lefts
`(-1, -2, -3)` and `(-1, -2, 3)`. Against the chirality cap, the sum
has rights `(1, -3, -2)` and `(-3, 2, -1)`. The partner centre pair is
`(1, -1)`. The source centres are `-2t-4r` and `0`, so the centre
pairs are `(-2t-4r, 1)` and `(0, -1)` and the kernel cross sum is
`-2t-4r`. The cross sum does not depend on `u` or `s`, and it does not
vanish for positive integers `t` and `r`.

**Obligations.** Proved here: `t` times the plus swapped-dot generator
plus `u` times the minus swapped-dot generator plus `r` times the plus
cap and `s` times the minus cap, for every quadruple of positive
integers `(t, u, r, s)`, on every ordered height pair, for every
chirality coefficient. Cited from the even-span note, and not re-proved:
the name of the even space. Cited from the ratio-span note, and not
re-proved: the names of the two spans. The strongest missing lemma is
the partner rank, at every chirality coefficient, of a general integer
point of the ten-kernel coefficient span.

## What this does not do

- It does not select a scale. The vectors are witnesses.
- It does not claim that the pivot gcd degree is independent of `t`, `u`, `r`, and `s`.
- It does not claim that these four minors are a monic generator of least degree.
- It does not claim that the ten-kernel coefficient span is settled.
- It does not claim that the full soldered bond space is classified.
- It does not apply the order-blind converse.
- It does not convert a kernel cross sum into an alphabet mean.
- It does not repeat the bond-space dimension count.
- It does not return to the modulus-3 triple.
- It does not supply a formation site, probability, or rate.

## Runner

`scripts/chiral_pair_unequal_swapped_dot_scales_two_cap_multiples_partner_kernel_2026_10_10.py`
checks the coordinate identity, the span kernels, the bond, the scale
identity, and the four minor forms. `TOTAL: PASS=9 FAIL=0`.

## Imports

No formation site, probability, rate, or selected scale is imported.
The proper rotations, the stacked partner kernel, and the four minor
forms are enumerated here. The even-span note names the even space.
The ratio-span note names the two spans. The order-blind converse is
not applied.
