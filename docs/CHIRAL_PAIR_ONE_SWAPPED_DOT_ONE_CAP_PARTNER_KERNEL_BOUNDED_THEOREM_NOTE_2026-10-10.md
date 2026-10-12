---
claim_id: chiral_pair_one_swapped_dot_one_cap_partner_kernel_bounded_theorem_note_2026-10-10
claim_type: bounded_theorem
claim_scope: "On every ordered height pair, one swapped-dot generator plus the cap generator of the same ratio span lies in that span. It has swapped-dot coordinate 1 or -1 and scaled coordinate 2. Chirality coefficient 0 has partner rank 7, and the partner kernel is that span on pairs (1, 2), (2, 1), (2, 3), and (3, 2), and the other span on (1, 3) and (3, 1). The 14-row pencil has maximal-minor gcd equal to a nonzero multiple of the cube of the chirality coefficient, so every nonzero chirality coefficient has partner rank 10. One swapped-dot generator plus the cap generator of the other ratio span lies in neither span. It has the same swapped-dot and scaled coordinates. Its 17-row pencil has a nonzero constant maximal-minor gcd, so every chirality coefficient has partner rank 10. The sum of both swapped-dot generators and one cap is not in this count. The ten-kernel coefficient span is not classified. The full soldered bond space is not classified. No scale is selected."
upstream_dependencies:
  - minimal_axioms
  - chiral_pair_even_span_partner_kernel_bounded_theorem_note_2026-10-10
  - chiral_pair_two_parity_excluded_partner_kernel_bounded_theorem_note_2026-10-10
runner: scripts/chiral_pair_one_swapped_dot_one_cap_partner_kernel_2026_10_10.py
---

# One swapped-dot generator plus one cap splits by span

**Date:** 2026-10-11

**Type:** bounded_theorem

**Audit:** unset; independent audit remains a separate lane

**Status:** proposed_retained

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/chiral_pair_one_swapped_dot_one_cap_partner_kernel_2026_10_10.py`](../scripts/chiral_pair_one_swapped_dot_one_cap_partner_kernel_2026_10_10.py)

**Parents:** the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md),
[the even span](CHIRAL_PAIR_EVEN_SPAN_PARTNER_KERNEL_BOUNDED_THEOREM_NOTE_2026-10-10.md),
and [the two ratio spans](CHIRAL_PAIR_TWO_PARITY_EXCLUDED_PARTNER_KERNEL_BOUNDED_THEOREM_NOTE_2026-10-10.md).

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "On every ordered height pair, one swapped-dot generator plus the cap of the same span has partner rank 7 only at chirality coefficient 0, and one swapped-dot generator plus the cap of the other span has partner rank 10 at every chirality coefficient."
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "Other generic orbits and higher-rank bond spaces are not classified."
source_of_blocker_text: frontier_question
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "Decide whether every chirality coefficient on the sum of one swapped-dot generator and both cap generators has partner rank 10. That sum has both a nonzero swapped-dot coordinate and a nonzero scaled coordinate. Do not claim the ten-kernel coefficient span is settled."
conditional_surface_status: "every ordered height pair; one swapped-dot generator plus one cap generator; same span or opposite span"
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
coefficient on the sum of one swapped-dot generator and the cap
generator of one ratio span has partner rank 10.

**Ansatz.** There are four sums. The same-span plus sum is the
swapped-dot generator and the cap generator of the first ratio span. It
has transverse-sign coordinate `-1`, sign-product coordinate `-1`,
matched coordinate `2`, swapped coordinate `-1`, swapped-dot coordinate
`1`, orthogonal coordinate `1`, and scaled coordinate `2`. The
same-span minus sum uses the second ratio span and has transverse-sign
coordinate `1`, sign-product coordinate `1`, matched coordinate `2`,
swapped coordinate `-1`, swapped-dot coordinate `-1`, orthogonal
coordinate `1`, and scaled coordinate `2`. Each lies in its own span and
not in the other. The opposite sums exchange the cap. The plus-dot
opposite sum has transverse-sign coordinate `1`, sign-product coordinate
`1`, and swapped-dot coordinate `1`. The minus-dot opposite sum has
transverse-sign coordinate `-1`, sign-product coordinate `-1`, and
swapped-dot coordinate `-1`. Both opposite sums have matched coordinate
`2`, swapped coordinate `-1`, orthogonal coordinate `1`, and scaled
coordinate `2`, and neither lies in one ratio span. The sum of both
swapped-dot generators and one cap is not this ansatz. The ten-kernel
coefficient span is not this ansatz. The full soldered bond space is
not classified.

The kernel cross sum on two perpendicular directions is the sum of the
products of the two centre values. This note does not convert that sum
into an alphabet mean.

**Conclusion.** On every ordered height pair, a same-span sum has
partner rank 7 at chirality coefficient 0 and partner rank 10 at every
nonzero chirality coefficient. An opposite-span sum has partner rank 10
at every chirality coefficient, including 0.

**Proof.** The runner enumerates the proper rotations and the alphabet
and builds the ten kernels. Each same-span sum lies in its span. The
base image has rank 7. On pairs `(1, 2)`, `(2, 1)`, `(2, 3)`, and
`(3, 2)` the partner kernel is that span. On `(1, 3)` and `(3, 1)` it
is the other span. The coefficient pairs compress to 14 rows. The gcd
of the 10-by-10 minors is a nonzero multiple of the cube of the
chirality coefficient, so the only root is 0 and every nonzero
chirality coefficient has partner rank 10. Each opposite-span sum lies
in neither span and outside the even space. Its base image has rank 10.
The coefficient pairs compress to 17 rows, and the gcd of the 10-by-10
minors is a nonzero constant, so every chirality coefficient has partner
rank 10. At heights 1 and 2 the bond on `-e_x` and `-e_y` has lefts
`(-1, -2, -3)` and `(-1, -2, 3)`. The same-span plus sum at chirality
coefficient 1, against the matched-oblique generator of its span, has
rights `(1, -3, -2)` and `(-1, 2, -3)`, centre pairs `(-5, 0)` and
`(-1, 2)`, and kernel cross sum `-2`. The same-span minus sum at
chirality coefficient 1 has rights `(1, -3, -2)` and `(-1, 2, 3)`,
centre pairs `(1, 2)` and `(-1, 0)`, and kernel cross sum `2`. The
opposite plus-dot sum, against the chirality cap, has rights
`(1, -3, -2)` and `(-3, 2, -1)`, centre pairs `(-2, 1)` and `(0, -1)`,
and kernel cross sum `-2`. The opposite minus-dot sum has the same
rights, centre pairs `(-4, 1)` and `(0, -1)`, and kernel cross sum `-4`.

**Obligations.** Proved here: the same-span and opposite-span sums, on
every ordered height pair, for every chirality coefficient. Cited from
the even-span note, and not re-proved: the name of the even space.
Cited from the ratio-span note, and not re-proved: the names of the two
spans. The strongest missing lemma is whether every chirality
coefficient on the sum of one swapped-dot generator and both cap
generators has partner rank 10.

## What this does not do

- It does not select a scale. The vectors are witnesses.
- It does not give the sum of both swapped-dot generators and one cap this count.
- It does not give one swapped-dot generator plus both cap generators this count.
- It does not claim that the ten-kernel coefficient span is settled.
- It does not claim that the full soldered bond space is classified.
- It does not apply the order-blind converse.
- It does not convert a kernel cross sum into an alphabet mean.
- It does not repeat the bond-space dimension count.
- It does not return to the modulus-3 triple.
- It does not supply a formation site, probability, or rate.

## Runner

`scripts/chiral_pair_one_swapped_dot_one_cap_partner_kernel_2026_10_10.py`
checks the two maximal-minor gcds. `TOTAL: PASS=9 FAIL=0`.

## Imports

No formation site, probability, rate, or selected scale is imported.
The proper rotations, the stacked partner kernel, and the maximal-minor
gcds are enumerated here. The even-span note names the even space. The
ratio-span note names the two spans. The order-blind converse is not
applied.
