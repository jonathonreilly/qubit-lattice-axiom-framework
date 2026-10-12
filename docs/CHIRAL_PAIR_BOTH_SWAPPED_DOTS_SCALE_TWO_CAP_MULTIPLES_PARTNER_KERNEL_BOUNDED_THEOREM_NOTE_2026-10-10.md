---
claim_id: chiral_pair_both_swapped_dots_scale_two_cap_multiples_partner_kernel_bounded_theorem_note_2026-10-10
claim_type: bounded_theorem
claim_scope: "On every ordered height pair, and for every triple of positive integers (t, r, s), t times both swapped-dot generators plus r times the plus cap and s times the minus cap has swapped-dot coordinate 0, swapped coordinate -2t, orthogonal coordinate 2t, transverse-sign coordinate s-r, sign-product coordinate s-r, matched coordinate 2r+2s, and scaled coordinate 2r+2s. The sum lies in neither ratio span and outside the even space. The partner rows are homogeneous of degree 1, so the matrix at (t, r, s, c) is t times the matrix at (1, r/t, s/t, c/t). The unit-scale elimination polynomial is (2r+1)^20 on (1, 2), (2, 1), and (3, 1) and r^10 on (1, 3), (2, 3), and (3, 2). Clearing the positive scale gives (2r+t)^20 or r^10. None depends on s, and none has a positive integer root, so every chirality coefficient has partner rank 10. The pivot gcd is not this certificate. Unequal scales of the two swapped-dot generators are not in this count. The ten-kernel coefficient span is not classified. The full soldered bond space is not classified. No scale is selected."
upstream_dependencies:
  - minimal_axioms
  - chiral_pair_even_span_partner_kernel_bounded_theorem_note_2026-10-10
  - chiral_pair_two_parity_excluded_partner_kernel_bounded_theorem_note_2026-10-10
runner: scripts/chiral_pair_both_swapped_dots_scale_two_cap_multiples_partner_kernel_2026_10_10.py
---

# One positive scale of both swapped-dot generators plus two cap multiples

**Date:** 2026-10-12

**Type:** bounded_theorem

**Audit:** unset; independent audit remains a separate lane

**Status:** proposed_retained

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/chiral_pair_both_swapped_dots_scale_two_cap_multiples_partner_kernel_2026_10_10.py`](../scripts/chiral_pair_both_swapped_dots_scale_two_cap_multiples_partner_kernel_2026_10_10.py)

**Parents:** the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md),
[the even span](CHIRAL_PAIR_EVEN_SPAN_PARTNER_KERNEL_BOUNDED_THEOREM_NOTE_2026-10-10.md),
and [the two ratio spans](CHIRAL_PAIR_TWO_PARITY_EXCLUDED_PARTNER_KERNEL_BOUNDED_THEOREM_NOTE_2026-10-10.md).

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "On every ordered height pair, t times both swapped-dot generators plus every pair of positive cap multiples has partner rank 10 at every chirality coefficient, for every positive integer t."
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "Other generic orbits and higher-rank bond spaces are not classified."
source_of_blocker_text: frontier_question
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "Decide whether every quadruple of positive integers (t, u, r, s) gives partner rank 10, at every chirality coefficient, for t times the plus swapped-dot generator plus u times the minus swapped-dot generator plus r times the plus cap and s times the minus cap. The case t = u is settled. Do not claim the ten-kernel coefficient span is settled."
conditional_surface_status: "every ordered height pair; t times both swapped-dot generators plus every pair of positive cap multiples"
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

**Target.** On every ordered height pair, decide whether every triple of
positive integers `(t, r, s)` gives partner rank 10 at every chirality
coefficient on the sum of `t` times both swapped-dot generators, `r`
times the plus cap, and `s` times the minus cap.

**Ansatz.** The sum has swapped-dot coordinate `0`, swapped coordinate
`-2t`, orthogonal coordinate `2t`, transverse-sign coordinate `s-r`,
sign-product coordinate `s-r`, matched coordinate `2r+2s`, and scaled
coordinate `2r+2s`. It lies in neither ratio span and outside the even
space. The case `t = 1` is the equal-generator count already settled.
Unequal positive scales of the two swapped-dot generators are not this
ansatz. The ten-kernel coefficient span is not this ansatz. The full
soldered bond space is not classified.

The kernel cross sum on two perpendicular directions is the sum of the
products of the two centre values. This note does not convert that sum
into an alphabet mean.

**Conclusion.** On every ordered height pair, every triple of positive
integers `(t, r, s)` gives partner rank 10 at every chirality
coefficient.

**Proof.** The runner enumerates the proper rotations and the alphabet
and builds the ten kernels. The coordinate identity is linear, so the
three parameter axes determine it, and the point `(2, 3, 5)` agrees.
Membership in each ratio span, and in the even space of each ordered
height pair, is the vanishing of linear forms in `(t, r, s)`. Those
forms have no strictly positive rational zero, so the sum lies outside
for every positive integer triple. Each compressed partner row is the
linear form `t` times the sum of the two swapped-dot rows plus `r`
times the plus-cap row plus `s` times the minus-cap row plus `c` times
the chirality row. For `t` nonzero, the row at `(t, r, s, c)` equals
`t` times the row at `(1, r/t, s/t, c/t)`. Every maximal minor therefore
scales by `t^10`. The runner checks the row identity on every compressed
row at `(2, 3, 5, 1)`, and checks that one nonzero maximal minor scales
by `2^10`. The unit-scale elimination polynomial, recomputed here, is
`(2r+1)^20` on `(1, 2)`, `(2, 1)`, and `(3, 1)`, and `r^10` on
`(1, 3)`, `(2, 3)`, and `(3, 2)`. None depends on `s`. Substituting
`(r/t, s/t)` and clearing the positive power of `t` gives `(2r+t)^20`
on `(1, 2)`, `(2, 1)`, and `(3, 1)`, and `r^10` on the other three
pairs. The specialization `t = 1` returns the unit-scale polynomial.
None depends on `s`, and none has a positive integer root. A positive
integer triple therefore makes the unit-scale resultant nonzero at
`(r/t, s/t)`, so the two maximal minors have no common chirality root
and every chirality coefficient has partner rank 10. The pivot gcd is
not this certificate. At heights 1 and 2 the bond on `-e_x` and `-e_y`
has lefts `(-1, -2, -3)` and `(-1, -2, 3)`. Against the chirality cap,
the sum has rights `(1, -3, -2)` and `(-3, 2, -1)`. The partner centre
pair is `(1, -1)`. The source centres are `-2t-4r` and `0`, so the
centre pairs are `(-2t-4r, 1)` and `(0, -1)` and the kernel cross sum
is `-2t-4r`. The cross sum does not depend on `s`, and it does not
vanish for positive integers `t` and `r`.

**Obligations.** Proved here: `t` times both swapped-dot generators plus
`r` times the plus cap and `s` times the minus cap, for every triple of
positive integers `(t, r, s)`, on every ordered height pair, for every
chirality coefficient. Cited from the even-span note, and not re-proved:
the name of the even space. Cited from the ratio-span note, and not
re-proved: the names of the two spans. The strongest missing lemma is
whether every quadruple of positive integers `(t, u, r, s)` gives
partner rank 10, at every chirality coefficient, for `t` times the plus
swapped-dot generator plus `u` times the minus swapped-dot generator
plus `r` times the plus cap and `s` times the minus cap.

## What this does not do

- It does not select a scale. The vectors are witnesses.
- It does not put unequal scales of the two swapped-dot generators into this count.
- It does not claim that the pivot gcd degree is independent of `t`, `r`, and `s`.
- It does not claim that this resultant is the monic generator of least degree.
- It does not claim that the ten-kernel coefficient span is settled.
- It does not claim that the full soldered bond space is classified.
- It does not apply the order-blind converse.
- It does not convert a kernel cross sum into an alphabet mean.
- It does not repeat the bond-space dimension count.
- It does not return to the modulus-3 triple.
- It does not supply a formation site, probability, or rate.

## Runner

`scripts/chiral_pair_both_swapped_dots_scale_two_cap_multiples_partner_kernel_2026_10_10.py`
checks the coordinate identity, the span obstructions, the bond, the
scale identity, and the elimination polynomials. `TOTAL: PASS=9 FAIL=0`.

## Imports

No formation site, probability, rate, or selected scale is imported.
The proper rotations, the stacked partner kernel, and the elimination
polynomials are enumerated here. The even-span note names the even
space. The ratio-span note names the two spans. The order-blind
converse is not applied.
