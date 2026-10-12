---
claim_id: chiral_pair_both_swapped_dots_twice_each_cap_partner_kernel_bounded_theorem_note_2026-10-10
claim_type: bounded_theorem
claim_scope: "On every ordered height pair, both swapped-dot generators plus twice the cap of each ratio span have swapped-dot coordinate 0, transverse-sign coordinate 0, sign-product coordinate 0, swapped coordinate -2, orthogonal coordinate 2, matched coordinate 8, and scaled coordinate 8. The sum lies in neither ratio span and outside the even space. The base image has rank 10. The 17-row pencil has a nonzero constant maximal-minor gcd, so every chirality coefficient has partner rank 10. The pivot gcd has degree 4 on every ordered height pair. One swapped-dot generator plus twice the cap of each ratio span is not in this count. The ten-kernel coefficient span is not classified. The full soldered bond space is not classified. No scale is selected."
upstream_dependencies:
  - minimal_axioms
  - chiral_pair_even_span_partner_kernel_bounded_theorem_note_2026-10-10
  - chiral_pair_two_parity_excluded_partner_kernel_bounded_theorem_note_2026-10-10
runner: scripts/chiral_pair_both_swapped_dots_twice_each_cap_partner_kernel_2026_10_10.py
---

# Both swapped-dot generators plus twice each cap

**Date:** 2026-10-11

**Type:** bounded_theorem

**Audit:** unset; independent audit remains a separate lane

**Status:** proposed_retained

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/chiral_pair_both_swapped_dots_twice_each_cap_partner_kernel_2026_10_10.py`](../scripts/chiral_pair_both_swapped_dots_twice_each_cap_partner_kernel_2026_10_10.py)

**Parents:** the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md),
[the even span](CHIRAL_PAIR_EVEN_SPAN_PARTNER_KERNEL_BOUNDED_THEOREM_NOTE_2026-10-10.md),
and [the two ratio spans](CHIRAL_PAIR_TWO_PARITY_EXCLUDED_PARTNER_KERNEL_BOUNDED_THEOREM_NOTE_2026-10-10.md).

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "On every ordered height pair, both swapped-dot generators plus twice the cap of each ratio span have partner rank 10 at every chirality coefficient."
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "Other generic orbits and higher-rank bond spaces are not classified."
source_of_blocker_text: frontier_question
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "Decide whether every chirality coefficient on the sum of one swapped-dot generator and twice the cap of each ratio span has partner rank 10. Do not claim the ten-kernel coefficient span is settled."
conditional_surface_status: "every ordered height pair; both swapped-dot generators plus twice the cap of each ratio span"
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

**Target.** On every ordered height pair, decide whether every chirality
coefficient on the sum of both swapped-dot generators and twice the cap
of each ratio span has partner rank 10.

**Ansatz.** There is one sum. The swapped-dot coordinates cancel, and
the transverse-sign and sign-product coordinates cancel, so the sum has
swapped-dot coordinate `0`, transverse-sign coordinate `0`,
sign-product coordinate `0`, swapped coordinate `-2`, orthogonal
coordinate `2`, matched coordinate `8`, and scaled coordinate `8`. It
lies in neither ratio span and outside the even space. One swapped-dot
generator plus twice the cap of each ratio span is not this ansatz. The
ten-kernel coefficient span is not this ansatz. The full soldered bond
space is not classified.

The kernel cross sum on two perpendicular directions is the sum of the
products of the two centre values. This note does not convert that sum
into an alphabet mean.

**Conclusion.** On every ordered height pair, every chirality coefficient
has partner rank 10.

**Proof.** The runner enumerates the proper rotations and the alphabet
and builds the ten kernels. The swapped-dot coordinates cancel, and the
transverse-sign and sign-product coordinates cancel. The sum lies in
neither ratio span and outside the even space. The base image has rank
10. The coefficient pairs compress to 17 rows, and the gcd of the
10-by-10 minors is a nonzero constant, so every chirality coefficient
has partner rank 10. The pivot gcd has degree `4` on every ordered
height pair. At heights 1 and 2 the bond on `-e_x` and `-e_y` has lefts
`(-1, -2, -3)` and `(-1, -2, 3)`. Against the chirality cap, the sum has
rights `(1, -3, -2)` and `(-3, 2, -1)`, centre pairs `(-10, 1)` and
`(0, -1)`, and kernel cross sum `-10`.

**Obligations.** Proved here: both swapped-dot generators plus twice the
cap of each ratio span, on every ordered height pair, for every
chirality coefficient. Cited from the even-span note, and not re-proved:
the name of the even space. Cited from the ratio-span note, and not
re-proved: the names of the two spans. The strongest missing lemma is
whether every chirality coefficient on the sum of one swapped-dot
generator and twice the cap of each ratio span has partner rank 10.

## What this does not do

- It does not select a scale. The vectors are witnesses.
- It does not give one swapped-dot generator plus twice each cap this count.
- It does not claim that the ten-kernel coefficient span is settled.
- It does not claim that the full soldered bond space is classified.
- It does not apply the order-blind converse.
- It does not convert a kernel cross sum into an alphabet mean.
- It does not repeat the bond-space dimension count.
- It does not return to the modulus-3 triple.
- It does not supply a formation site, probability, or rate.

## Runner

`scripts/chiral_pair_both_swapped_dots_twice_each_cap_partner_kernel_2026_10_10.py`
checks the constant maximal-minor gcd and the pivot degree. `TOTAL: PASS=6 FAIL=0`.

## Imports

No formation site, probability, rate, or selected scale is imported.
The proper rotations, the stacked partner kernel, and the maximal-minor
gcds are enumerated here. The even-span note names the even space. The
ratio-span note names the two spans. The order-blind converse is not
applied.
