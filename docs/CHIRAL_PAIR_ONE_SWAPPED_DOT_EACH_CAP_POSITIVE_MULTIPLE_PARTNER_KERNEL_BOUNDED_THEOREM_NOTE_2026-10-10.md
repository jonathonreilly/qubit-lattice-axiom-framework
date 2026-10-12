---
claim_id: chiral_pair_one_swapped_dot_each_cap_positive_multiple_partner_kernel_bounded_theorem_note_2026-10-10
claim_type: bounded_theorem
claim_scope: "On every ordered height pair, and for every positive integer m, one swapped-dot generator plus m times the cap of each ratio span has transverse-sign coordinate 0, sign-product coordinate 0, swapped coordinate -1, orthogonal coordinate 1, matched coordinate 4m, and scaled coordinate 4m. The plus-dot sum has swapped-dot coordinate 1. The minus-dot sum has swapped-dot coordinate -1. The two sums are linearly independent. Each lies in neither ratio span and outside the even space. One 17-row compression has an elimination polynomial with no positive integer root, so every chirality coefficient has partner rank 10. On (1, 2), (2, 1), and (3, 1) that polynomial is a rational multiple of m^4(2m+1)^12(4m+1)^4 for the plus-dot sum and of m^12(2m+1)^3(4m+1)^4 for the minus-dot sum. On (1, 3), (2, 3), and (3, 2) it is a rational multiple of m^10 for both sums. The pivot gcd is not this certificate. Both swapped-dot generators are not in this count. The ten-kernel coefficient span is not classified. The full soldered bond space is not classified. No scale is selected."
upstream_dependencies:
  - minimal_axioms
  - chiral_pair_even_span_partner_kernel_bounded_theorem_note_2026-10-10
  - chiral_pair_two_parity_excluded_partner_kernel_bounded_theorem_note_2026-10-10
runner: scripts/chiral_pair_one_swapped_dot_each_cap_positive_multiple_partner_kernel_2026_10_10.py
---

# One swapped-dot generator plus every positive multiple of each cap

**Date:** 2026-10-12

**Type:** bounded_theorem

**Audit:** unset; independent audit remains a separate lane

**Status:** proposed_retained

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/chiral_pair_one_swapped_dot_each_cap_positive_multiple_partner_kernel_2026_10_10.py`](../scripts/chiral_pair_one_swapped_dot_each_cap_positive_multiple_partner_kernel_2026_10_10.py)

**Parents:** the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md),
[the even span](CHIRAL_PAIR_EVEN_SPAN_PARTNER_KERNEL_BOUNDED_THEOREM_NOTE_2026-10-10.md),
and [the two ratio spans](CHIRAL_PAIR_TWO_PARITY_EXCLUDED_PARTNER_KERNEL_BOUNDED_THEOREM_NOTE_2026-10-10.md).

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "On every ordered height pair, one swapped-dot generator plus every positive integer multiple of each ratio-span cap has partner rank 10 at every chirality coefficient."
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "Other generic orbits and higher-rank bond spaces are not classified."
source_of_blocker_text: frontier_question
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "Decide whether every positive integer m gives partner rank 10, at every chirality coefficient, for both swapped-dot generators plus m times the cap of each ratio span. The cases m = 2 and m = 3 are settled. Do not claim the ten-kernel coefficient span is settled."
conditional_surface_status: "every ordered height pair; one swapped-dot generator plus every positive integer multiple of each ratio-span cap"
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

**Target.** On every ordered height pair, decide whether every positive
integer `m` gives partner rank 10 at every chirality coefficient on the
sum of one swapped-dot generator and `m` times the cap of each ratio
span.

**Ansatz.** There are two sums. `m` times each cap cancels the
transverse-sign coordinate and the sign-product coordinate. The plus-dot
sum has swapped-dot coordinate `1`. The minus-dot sum has swapped-dot
coordinate `-1`. Each has swapped coordinate `-1`, orthogonal coordinate
`1`, matched coordinate `4m`, and scaled coordinate `4m`. The two sums
are linearly independent. Each lies in neither ratio span and outside
the even space for every positive integer `m`. Both swapped-dot
generators are not this ansatz. The ten-kernel coefficient span is not
this ansatz. The full soldered bond space is not classified.

The kernel cross sum on two perpendicular directions is the sum of the
products of the two centre values. This note does not convert that sum
into an alphabet mean.

**Conclusion.** On every ordered height pair, every positive integer
`m` gives partner rank 10 at every chirality coefficient.

**Proof.** The runner enumerates the proper rotations and the alphabet
and builds the ten kernels. The coordinate identities are the generator
sum: one swapped-dot generator plus `m` times each cap. The two sums
differ by twice the swapped-dot axis, so they are linearly independent
for every `m`. Membership in each ratio span, and in the even space of
each ordered height pair, is cut out by a polynomial in `m` with no
positive integer root. The coefficient pairs at multiple `1` compress to
17 rows. The maximal minors that reduce the chirality gcd generate an
elimination ideal in the multiple. On `(1, 2)`, `(2, 1)`, and `(3, 1)`
the generator is a rational multiple of `m^4(2m+1)^12(4m+1)^4` for the
plus-dot sum and of `m^12(2m+1)^3(4m+1)^4` for the minus-dot sum. On
`(1, 3)`, `(2, 3)`, and `(3, 2)` it is a rational multiple of `m^10`
for both sums. None of those polynomials has a positive integer root, so
every positive integer `m` has a nonzero constant maximal-minor gcd and
every chirality coefficient has partner rank 10. The pivot gcd is not
this certificate. At heights 1 and 2 the bond on `-e_x` and `-e_y` has
lefts `(-1, -2, -3)` and `(-1, -2, 3)`. Against the chirality cap, both
sums have rights `(1, -3, -2)` and `(-3, 2, -1)`. The partner centre
pair is `(1, -1)`. The plus-dot sum has source centres `-2-4m` and `0`,
so the centre pairs are `(-2-4m, 1)` and `(0, -1)` and the kernel cross
sum is `-2-4m`. The minus-dot sum has source centres `-4m` and `0`, so
the centre pairs are `(-4m, 1)` and `(0, -1)` and the kernel cross sum
is `-4m`. Neither cross sum vanishes for a positive integer `m`, and no
lexicographically earlier right pair has a nonzero cross polynomial.

**Obligations.** Proved here: one swapped-dot generator plus `m` times
the cap of each ratio span, for every positive integer `m`, on every
ordered height pair, for every chirality coefficient, for both choices
of the swapped-dot generator. Cited from the even-span note, and not
re-proved: the name of the even space. Cited from the ratio-span note,
and not re-proved: the names of the two spans. The strongest missing
lemma is whether every positive integer `m` gives partner rank 10, at
every chirality coefficient, for both swapped-dot generators plus `m`
times the cap of each ratio span.

## What this does not do

- It does not select a scale. The vectors are witnesses.
- It does not put both swapped-dot generators into this count.
- It does not claim that the pivot gcd degree is independent of `m`.
- It does not claim that the ten-kernel coefficient span is settled.
- It does not claim that the full soldered bond space is classified.
- It does not apply the order-blind converse.
- It does not convert a kernel cross sum into an alphabet mean.
- It does not repeat the bond-space dimension count.
- It does not return to the modulus-3 triple.
- It does not supply a formation site, probability, or rate.

## Runner

`scripts/chiral_pair_one_swapped_dot_each_cap_positive_multiple_partner_kernel_2026_10_10.py`
checks the coordinate identities, the span obstructions, and the
elimination polynomials. `TOTAL: PASS=8 FAIL=0`.

## Imports

No formation site, probability, rate, or selected scale is imported.
The proper rotations, the stacked partner kernel, and the elimination
polynomials are enumerated here. The even-span note names the even
space. The ratio-span note names the two spans. The order-blind
converse is not applied.
