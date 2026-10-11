---
claim_id: chiral_pair_both_swapped_dots_both_caps_partner_kernel_bounded_theorem_note_2026-10-10
claim_type: bounded_theorem
claim_scope: "On every ordered height pair, both swapped-dot generators plus both cap generators lie outside the even space and outside both ratio spans. The swapped-dot coordinates cancel, so the sum has swapped-dot coordinate 0, matched coordinate 4, swapped coordinate -2, orthogonal coordinate 2, and scaled coordinate 4. The base image has rank 10. The coefficient pairs compress to 17 rows, and the gcd of the 10-by-10 minors is a nonzero constant, so every chirality coefficient has partner rank 10. The pivot minors at 0, 1, -1, -1/2, 1/2, 3/2, 5/2, 2, -2, and -2/3 do not have a constant gcd. One swapped-dot generator plus twice the cap of the same span is not in this count. The ten-kernel coefficient span is not classified. The full soldered bond space is not classified. No scale is selected."
upstream_dependencies:
  - minimal_axioms
  - chiral_pair_even_span_partner_kernel_bounded_theorem_note_2026-10-10
  - chiral_pair_two_parity_excluded_partner_kernel_bounded_theorem_note_2026-10-10
runner: scripts/chiral_pair_both_swapped_dots_both_caps_partner_kernel_2026_10_10.py
---

# Both swapped-dot generators plus both caps keep partner rank 10

**Date:** 2026-10-11

**Type:** bounded_theorem

**Audit:** unset; independent audit remains a separate lane

**Status:** proposed_retained

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/chiral_pair_both_swapped_dots_both_caps_partner_kernel_2026_10_10.py`](../scripts/chiral_pair_both_swapped_dots_both_caps_partner_kernel_2026_10_10.py)

**Parents:** the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md),
[the even span](CHIRAL_PAIR_EVEN_SPAN_PARTNER_KERNEL_BOUNDED_THEOREM_NOTE_2026-10-10.md),
and [the two ratio spans](CHIRAL_PAIR_TWO_PARITY_EXCLUDED_PARTNER_KERNEL_BOUNDED_THEOREM_NOTE_2026-10-10.md).

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "On every ordered height pair, both swapped-dot generators plus both cap generators have partner rank 10 at every chirality coefficient."
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "Other generic orbits and higher-rank bond spaces are not classified."
source_of_blocker_text: frontier_question
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "Decide whether every chirality coefficient on the sum of one swapped-dot generator and twice the cap of the same ratio span has partner rank 10. That sum lies in the span and has swapped-dot coordinate 1 or -1 and scaled coordinate 4. Do not claim the ten-kernel coefficient span is settled."
conditional_surface_status: "every ordered height pair; both swapped-dot generators plus both cap generators; every chirality coefficient"
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
coefficient on the sum of both swapped-dot generators and both cap
generators has partner rank 10.

**Ansatz.** The sum is the two swapped-dot generators plus the two cap
generators. The swapped-dot coordinates cancel. The sum has matched
coordinate `4`, swapped coordinate `-2`, orthogonal coordinate `2`, and
scaled coordinate `4`. Transverse-sign, sign-product, and swapped-dot
coordinates are `0`. The sum lies outside the even space and outside
both ratio spans. One swapped-dot generator plus twice the cap of the
same span is not this ansatz. The ten-kernel coefficient span is not
this ansatz. The full soldered bond space is not classified.

The kernel cross sum on two perpendicular directions is the sum of the
products of the two centre values. This note does not convert that sum
into an alphabet mean.

**Conclusion.** On every ordered height pair, the sum has partner rank
10 at every chirality coefficient, including 0.

**Proof.** The runner enumerates the proper rotations and the alphabet
and builds the ten kernels. The sum lies outside the even space and
outside both ratio spans. The base image has rank 10 and nullity 0. The
coefficient pairs compress to 17 rows, and the gcd of the 10-by-10
minors is a nonzero constant, so every chirality coefficient has partner
rank 10. The pivot minors at `0`, `1`, `-1`, `-1/2`, `1/2`, `3/2`,
`5/2`, `2`, `-2`, and `-2/3` do not have a constant gcd. At heights 1
and 2 the bond on `-e_x` and `-e_y` has lefts `(-1, -2, -3)` and
`(-1, -2, 3)`. Against the chirality cap, the sum has rights
`(1, -3, -2)` and `(-3, 2, -1)`, centre pairs `(-6, 1)` and `(0, -1)`,
and kernel cross sum `-6`.

**Obligations.** Proved here: both swapped-dot generators plus both cap
generators, on every ordered height pair, for every chirality
coefficient. Cited from the even-span note, and not re-proved: the name
of the even space. Cited from the ratio-span note, and not re-proved:
the names of the two spans. The strongest missing lemma is whether
every chirality coefficient on the sum of one swapped-dot generator and
twice the cap of the same ratio span has partner rank 10. That sum lies
in the span and has a nonzero swapped-dot coordinate.

## What this does not do

- It does not select a scale. The vector is a witness.
- It does not give one swapped-dot generator plus twice the cap of the same span this count.
- It does not give one swapped-dot generator plus both caps this count.
- It does not claim that the ten-kernel coefficient span is settled.
- It does not claim that the full soldered bond space is classified.
- It does not apply the order-blind converse.
- It does not convert a kernel cross sum into an alphabet mean.
- It does not repeat the bond-space dimension count.
- It does not return to the modulus-3 triple.
- It does not supply a formation site, probability, or rate.

## Runner

`scripts/chiral_pair_both_swapped_dots_both_caps_partner_kernel_2026_10_10.py`
checks the maximal-minor gcd and the pivot-sample gap. `TOTAL: PASS=6 FAIL=0`.

## Imports

No formation site, probability, rate, or selected scale is imported.
The proper rotations, the stacked partner kernel, and the maximal-minor
gcds are enumerated here. The even-span note names the even space. The
ratio-span note names the two spans. The order-blind converse is not
applied.
