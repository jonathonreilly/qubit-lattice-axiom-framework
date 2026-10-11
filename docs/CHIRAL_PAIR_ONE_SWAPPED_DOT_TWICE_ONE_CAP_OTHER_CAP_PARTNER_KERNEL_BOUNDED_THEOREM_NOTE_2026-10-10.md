---
claim_id: chiral_pair_one_swapped_dot_twice_one_cap_other_cap_partner_kernel_bounded_theorem_note_2026-10-10
claim_type: bounded_theorem
claim_scope: "On every ordered height pair, one swapped-dot generator plus twice the cap of one ratio span plus the cap of the other ratio span has swapped coordinate -1, orthogonal coordinate 1, matched coordinate 6, and scaled coordinate 6. The plus-dot sums have swapped-dot coordinate 1. The minus-dot sums have swapped-dot coordinate -1. Doubling the plus cap gives transverse-sign coordinate -1 and sign-product coordinate -1. Doubling the minus cap gives transverse-sign coordinate 1 and sign-product coordinate 1. Each of the four sums lies in neither ratio span and outside the even space. The four sums have rank 3. The base image has rank 10. The 17-row pencil has a nonzero constant maximal-minor gcd, so every chirality coefficient has partner rank 10. The twice-plus pivot gcd has degree 7 on every ordered height pair. The plus-dot twice-minus pivot gcd has degree 7 on (1, 2), (2, 1), and (3, 1), and degree 5 on (1, 3), (2, 3), and (3, 2). The minus-dot twice-minus pivot gcd has degree 5 on every ordered height pair. Both swapped-dot generators plus twice one cap and the other cap are not in this count. The ten-kernel coefficient span is not classified. The full soldered bond space is not classified. No scale is selected."
upstream_dependencies:
  - minimal_axioms
  - chiral_pair_even_span_partner_kernel_bounded_theorem_note_2026-10-10
  - chiral_pair_two_parity_excluded_partner_kernel_bounded_theorem_note_2026-10-10
runner: scripts/chiral_pair_one_swapped_dot_twice_one_cap_other_cap_partner_kernel_2026_10_10.py
---

# One swapped-dot generator plus twice one cap and the other cap

**Date:** 2026-10-11

**Type:** bounded_theorem

**Audit:** unset; independent audit remains a separate lane

**Status:** proposed_retained

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/chiral_pair_one_swapped_dot_twice_one_cap_other_cap_partner_kernel_2026_10_10.py`](../scripts/chiral_pair_one_swapped_dot_twice_one_cap_other_cap_partner_kernel_2026_10_10.py)

**Parents:** the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md),
[the even span](CHIRAL_PAIR_EVEN_SPAN_PARTNER_KERNEL_BOUNDED_THEOREM_NOTE_2026-10-10.md),
and [the two ratio spans](CHIRAL_PAIR_TWO_PARITY_EXCLUDED_PARTNER_KERNEL_BOUNDED_THEOREM_NOTE_2026-10-10.md).

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "On every ordered height pair, one swapped-dot generator plus twice the cap of one ratio span plus the cap of the other ratio span has partner rank 10 at every chirality coefficient."
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "Other generic orbits and higher-rank bond spaces are not classified."
source_of_blocker_text: frontier_question
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "Decide whether every chirality coefficient on the sum of both swapped-dot generators and twice the cap of one ratio span plus the cap of the other ratio span has partner rank 10. Do not claim the ten-kernel coefficient span is settled."
conditional_surface_status: "every ordered height pair; one swapped-dot generator plus twice one cap and the other cap"
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
coefficient on the sum of one swapped-dot generator and twice the cap
of one ratio span plus the cap of the other ratio span has partner
rank 10.

**Ansatz.** There are four sums. Each uses one swapped-dot generator,
twice the cap of one ratio span, and the cap of the other ratio span.
Each has swapped coordinate `-1`, orthogonal coordinate `1`, matched
coordinate `6`, and scaled coordinate `6`. The plus-dot sums have
swapped-dot coordinate `1`. The minus-dot sums have swapped-dot
coordinate `-1`. Doubling the plus cap gives transverse-sign coordinate
`-1` and sign-product coordinate `-1`. Doubling the minus cap gives
transverse-sign coordinate `1` and sign-product coordinate `1`. Each
lies in neither ratio span and outside the even space. The four sums
have rank `3`: the plus-dot twice-plus sum plus the minus-dot
twice-minus sum equals the plus-dot twice-minus sum plus the minus-dot
twice-plus sum. Both swapped-dot generators plus twice one cap and the
other cap are not this ansatz. The ten-kernel coefficient span is not
this ansatz. The full soldered bond space is not classified.

The kernel cross sum on two perpendicular directions is the sum of the
products of the two centre values. This note does not convert that sum
into an alphabet mean.

**Conclusion.** On every ordered height pair, every chirality coefficient
has partner rank 10.

**Proof.** The runner enumerates the proper rotations and the alphabet
and builds the ten kernels. Each sum lies in neither ratio span and
outside the even space. The four sums have rank 3, with the relation
above. The base image has rank 10. The coefficient pairs compress to
17 rows, and the gcd of the 10-by-10 minors is a nonzero constant, so
every chirality coefficient has partner rank 10. The twice-plus pivot
gcd has degree `7` on every ordered height pair. The plus-dot
twice-minus pivot gcd has degree `7` on `(1, 2)`, `(2, 1)`, and
`(3, 1)`, and degree `5` on `(1, 3)`, `(2, 3)`, and `(3, 2)`. The
minus-dot twice-minus pivot gcd has degree `5` on every ordered height
pair. At heights 1 and 2 the bond on `-e_x` and `-e_y` has lefts
`(-1, -2, -3)` and `(-1, -2, 3)`. Against the chirality cap, each sum
has rights `(1, -3, -2)` and `(-3, 2, -1)`. The plus-dot twice-plus sum
has centre pairs `(-10, 1)` and `(0, -1)`, and kernel cross sum `-10`.
The plus-dot twice-minus sum has centre pairs `(-6, 1)` and `(0, -1)`,
and kernel cross sum `-6`. The minus-dot twice-plus sum has centre
pairs `(-8, 1)` and `(0, -1)`, and kernel cross sum `-8`. The minus-dot
twice-minus sum has centre pairs `(-4, 1)` and `(0, -1)`, and kernel
cross sum `-4`.

**Obligations.** Proved here: one swapped-dot generator plus twice the
cap of one ratio span plus the cap of the other ratio span, on every
ordered height pair, for every chirality coefficient, and for both
choices of the doubled cap. Cited from the even-span note, and not
re-proved: the name of the even space. Cited from the ratio-span note,
and not re-proved: the names of the two spans. The strongest missing
lemma is whether every chirality coefficient on the sum of both
swapped-dot generators and twice the cap of one ratio span plus the cap
of the other ratio span has partner rank 10.

## What this does not do

- It does not select a scale. The vectors are witnesses.
- It does not give both swapped-dot generators plus twice one cap and the other cap this count.
- It does not claim that the ten-kernel coefficient span is settled.
- It does not claim that the full soldered bond space is classified.
- It does not apply the order-blind converse.
- It does not convert a kernel cross sum into an alphabet mean.
- It does not repeat the bond-space dimension count.
- It does not return to the modulus-3 triple.
- It does not supply a formation site, probability, or rate.

## Runner

`scripts/chiral_pair_one_swapped_dot_twice_one_cap_other_cap_partner_kernel_2026_10_10.py`
checks the constant maximal-minor gcd and the pivot split. `TOTAL: PASS=9 FAIL=0`.

## Imports

No formation site, probability, rate, or selected scale is imported.
The proper rotations, the stacked partner kernel, and the maximal-minor
gcds are enumerated here. The even-span note names the even space. The
ratio-span note names the two spans. The order-blind converse is not
applied.
