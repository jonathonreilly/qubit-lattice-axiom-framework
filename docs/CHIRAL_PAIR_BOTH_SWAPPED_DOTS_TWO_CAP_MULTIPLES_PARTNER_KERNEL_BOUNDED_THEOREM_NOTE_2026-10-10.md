---
claim_id: chiral_pair_both_swapped_dots_two_cap_multiples_partner_kernel_bounded_theorem_note_2026-10-10
claim_type: bounded_theorem
claim_scope: "On every ordered height pair, and for every pair of positive integers (r, s), both swapped-dot generators plus r times the plus cap and s times the minus cap have swapped-dot coordinate 0, swapped coordinate -2, orthogonal coordinate 2, transverse-sign coordinate s-r, sign-product coordinate s-r, matched coordinate 2r+2s, and scaled coordinate 2r+2s. The sum lies in neither ratio span and outside the even space. One 17-row compression has an elimination polynomial with no positive integer root, so every chirality coefficient has partner rank 10. On (1, 2), (2, 1), and (3, 1) that polynomial is (2r+1)^20. On (1, 3), (2, 3), and (3, 2) it is r^10. Neither polynomial depends on s. The pivot gcd is not this certificate. One swapped-dot generator is not in this count. The ten-kernel coefficient span is not classified. The full soldered bond space is not classified. No scale is selected."
upstream_dependencies:
  - minimal_axioms
  - chiral_pair_even_span_partner_kernel_bounded_theorem_note_2026-10-10
  - chiral_pair_two_parity_excluded_partner_kernel_bounded_theorem_note_2026-10-10
runner: scripts/chiral_pair_both_swapped_dots_two_cap_multiples_partner_kernel_2026_10_10.py
---

# Both swapped-dot generators plus two positive cap multiples

**Date:** 2026-10-12

**Type:** bounded_theorem

**Audit:** unset; independent audit remains a separate lane

**Status:** proposed_retained

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/chiral_pair_both_swapped_dots_two_cap_multiples_partner_kernel_2026_10_10.py`](../scripts/chiral_pair_both_swapped_dots_two_cap_multiples_partner_kernel_2026_10_10.py)

**Parents:** the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md),
[the even span](CHIRAL_PAIR_EVEN_SPAN_PARTNER_KERNEL_BOUNDED_THEOREM_NOTE_2026-10-10.md),
and [the two ratio spans](CHIRAL_PAIR_TWO_PARITY_EXCLUDED_PARTNER_KERNEL_BOUNDED_THEOREM_NOTE_2026-10-10.md).

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "On every ordered height pair, both swapped-dot generators plus every pair of positive cap multiples have partner rank 10 at every chirality coefficient."
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "Other generic orbits and higher-rank bond spaces are not classified."
source_of_blocker_text: frontier_question
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "Decide whether every pair of positive integers (r, s) gives partner rank 10, at every chirality coefficient, for one swapped-dot generator plus r times one ratio-span cap and s times the other. The equal-multiple diagonal is settled. Do not claim the ten-kernel coefficient span is settled."
conditional_surface_status: "every ordered height pair; both swapped-dot generators plus every pair of positive cap multiples"
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

**Target.** On every ordered height pair, decide whether every pair of
positive integers `(r, s)` gives partner rank 10 at every chirality
coefficient on the sum of both swapped-dot generators, `r` times the
plus cap, and `s` times the minus cap.

**Ansatz.** There is one sum. The swapped-dot coordinates cancel. The
sum has swapped-dot coordinate `0`, swapped coordinate `-2`, orthogonal
coordinate `2`, transverse-sign coordinate `s-r`, sign-product
coordinate `s-r`, matched coordinate `2r+2s`, and scaled coordinate
`2r+2s`. It lies in neither ratio span and outside the even space. One
swapped-dot generator is not this ansatz. The ten-kernel coefficient
span is not this ansatz. The full soldered bond space is not
classified.

The kernel cross sum on two perpendicular directions is the sum of the
products of the two centre values. This note does not convert that sum
into an alphabet mean.

**Conclusion.** On every ordered height pair, every pair of positive
integers `(r, s)` gives partner rank 10 at every chirality coefficient.

**Proof.** The runner enumerates the proper rotations and the alphabet
and builds the ten kernels. The coordinate identity is the generator
sum. Membership in each ratio span, and in the even space of each
ordered height pair, is cut out by the unit ideal, so the sum lies
outside for every `r` and `s`. The coefficient pairs compress to 17
rows. The primitive elimination polynomial is `(2r+1)^20` on
`(1, 2)`, `(2, 1)`, and `(3, 1)`, and `r^10` on `(1, 3)`, `(2, 3)`, and
`(3, 2)`. Neither polynomial depends on `s`, and neither has a positive
integer root, so every chirality coefficient has partner rank 10. The pivot gcd is not this certificate. At heights 1 and 2 the bond
on `-e_x` and `-e_y` has lefts `(-1, -2, -3)` and `(-1, -2, 3)`.
Against the chirality cap, the sum has rights `(1, -3, -2)` and
`(-3, 2, -1)`. The partner centre pair is `(1, -1)`. The source
centres are `-2-4r` and `0`, so the centre pairs are `(-2-4r, 1)` and
`(0, -1)` and the kernel cross sum is `-2-4r`. The cross sum does not
depend on `s` and does not vanish for a positive integer `r`.

**Obligations.** Proved here: both swapped-dot generators plus `r`
times the plus cap and `s` times the minus cap, for every pair of
positive integers `(r, s)`, on every ordered height pair, for every
chirality coefficient. Cited from the even-span note, and not
re-proved: the name of the even space. Cited from the ratio-span note,
and not re-proved: the names of the two spans. The strongest missing
lemma is whether every pair of positive integers `(r, s)` gives partner
rank 10, at every chirality coefficient, for one swapped-dot generator
plus `r` times one ratio-span cap and `s` times the other.

## What this does not do

- It does not select a scale. The vectors are witnesses.
- It does not put one swapped-dot generator into this count.
- It does not claim that the pivot gcd degree is independent of `r` and `s`.
- It does not claim that this elimination polynomial is the monic generator of least degree.
- It does not claim that the ten-kernel coefficient span is settled.
- It does not claim that the full soldered bond space is classified.
- It does not apply the order-blind converse.
- It does not convert a kernel cross sum into an alphabet mean.
- It does not repeat the bond-space dimension count.
- It does not return to the modulus-3 triple.
- It does not supply a formation site, probability, or rate.

## Runner

`scripts/chiral_pair_both_swapped_dots_two_cap_multiples_partner_kernel_2026_10_10.py`
checks the coordinate identity, the span obstructions, and the
elimination polynomials. `TOTAL: PASS=7 FAIL=0`.

## Imports

No formation site, probability, rate, or selected scale is imported.
The proper rotations, the stacked partner kernel, and the elimination
polynomials are enumerated here. The even-span note names the even
space. The ratio-span note names the two spans. The order-blind
converse is not applied.
