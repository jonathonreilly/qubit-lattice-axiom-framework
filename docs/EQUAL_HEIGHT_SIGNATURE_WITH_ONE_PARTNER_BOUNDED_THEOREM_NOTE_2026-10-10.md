---
claim_id: equal_height_signature_with_one_partner_bounded_theorem_note_2026-10-10
claim_type: bounded_theorem
claim_scope: "On the proper orbit of (1, 2, 3), every two height signatures have joint slice-kernel dimension 6, so a slice-zero soldered kernel on one equal-height signature and one partner is the direct sum of the two signature kernels. Beside an opposite partner the pair moments force the equal-height block to zero, and the kernel is that opposite signature, inside the eighteen cap-pair kernels. Beside a second equal-height signature both blocks are zero. The triple (-3, -3), (-3, 3), (3, -3) has joint slice kernel 10 and is outside this ansatz. No scale is selected."
upstream_dependencies:
  - minimal_axioms
  - order_blind_nearest_neighbour_formation_independence_beyond_neighbours_unsoldered_constancy_and_soldered_escape_bounded_theorem_note_2026-09-22
  - single_height_signature_order_blind_kernel_bounded_theorem_note_2026-10-10
runner: scripts/equal_height_signature_with_one_partner_2026_10_10.py
---

# An equal-height signature does not leave the eighteen beside one partner

**Date:** 2026-10-10

**Type:** bounded_theorem

**Audit:** unset; independent audit remains a separate lane

**Status:** proposed_retained

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/equal_height_signature_with_one_partner_2026_10_10.py`](../scripts/equal_height_signature_with_one_partner_2026_10_10.py)

**Parents:** the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md),
[the order-blind formation note](ORDER_BLIND_NEAREST_NEIGHBOUR_FORMATION_INDEPENDENCE_BEYOND_NEIGHBOURS_UNSOLDERED_CONSTANCY_AND_SOLDERED_ESCAPE_BOUNDED_THEOREM_NOTE_2026-09-22.md),
and the [single height-signature note](SINGLE_HEIGHT_SIGNATURE_ORDER_BLIND_KERNEL_BOUNDED_THEOREM_NOTE_2026-10-10.md).

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Pair moments force an equal-height signature to zero beside one opposite or equal-height partner."
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "Other generic orbits and higher-rank bond spaces are not classified."
source_of_blocker_text: frontier_question
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "Ask whether the extra slice direction on the signatures (-3, -3), (-3, 3), and (3, -3) is order-blind outside the eighteen. The joint kernel there has dimension 10. Do not restate the one-partner cut."
conditional_surface_status: "one proper orbit of (1, 2, 3); one equal-height signature plus one opposite or equal-height partner; uniform average"
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

The parent note's converse: "Conversely every family with these
properties is order-blind on every window." It leaves the sentence
"Other generic orbits and higher-rank bond spaces are not classified."

## Theorem

**Target.** Inside the ansatz of a slice-zero soldered kernel supported
on one equal-height signature and one partner signature, the partner
being opposite or equal-height, decide whether any order-blind kernel
lies outside the eighteen cap-pair kernels.

**Ansatz.** Height signatures are the reversal classes of `(a·d, b·d)`.
An equal-height signature has the form `(h, h)`. The kernel is
bond-symmetric and soldered, every slice sums to 0, and its support is
one equal-height signature together with one opposite signature or one
other equal-height signature.

**Conclusion.** Any two of the 21 signatures have joint slice-kernel
dimension 6. The supports are disjoint, so that kernel is the direct
sum of the two three-dimensional signature kernels. There is no
two-signature coupling.

On each equal-height block the pair moments reduce to

`u^2 - (3/2) v w - (4/3) w^2 = 0`,

`u v + v^2 + (3/2) v w + (2/3) w^2 = 0`,

`u w - v^2 - (1/2) v w + (2/3) w^2 = 0`.

The only common zero is the origin. If `w = 0`, the first two equations
are `u^2 = 0` and `v^2 = 0`. If `w ≠ 0`, scale `w = 1`. The first
equation gives `v = (6 u^2 - 8) / 9`, and substitution produces the
quartics `36 u^4 + 54 u^3 - 15 u^2 - 72 u + 10` and
`36 u^4 - 69 u^2 - 81 u - 26`. Their resultant is
`113027603142816`, so they have no common root.

Six pairs share a modulus and an axis on every record. Their cross
moments are three bilinear forms with no pure partner term, so they
vanish when the equal-height block is zero. The opposite coordinates
stay free. By the single-signature note that kernel lies in the
eighteen cap-pair kernels and is order-blind.

Twelve pairs have different moduli and disjoint axes. Their nine cross
moments are the products of one coordinate from each block. A nonzero
partner coordinate forces the equal-height block to zero, and the
opposite block that remains is again inside the eighteen.

Three pairs are two equal-height signatures, also on disjoint axes.
Both blocks carry the three quadrics, so both are zero. No nonzero
kernel with vanishing pair moments lies on those pairs.

No order-blind kernel in this ansatz lies outside the eighteen. A
partner basis vector satisfies a same-modulus system. The pure
equal-height vector with coordinate `u = 1` does not.

**Proof.** The runner enumerates the group, the 21 signatures, and the
joint slice kernels of all 210 pairs and all 1330 triples. It
row-reduces the pair moments of each equal-height partner and compares
them with the normal forms above. The zero of the three quadrics is the
substitution and the resultant. The drop from an opposite signature to
the eighteen is the single-signature note.

**Obligations.** Proved here: the direct sum on every pair, the three
normal forms, the axis patterns, and the resultant. Cited from the
single-signature note, and not re-proved: which single signatures are
order-blind, and that each opposite signature is the cap-pair span.
Cited from the 2026-09-22 parent, through that note: the converse. The
strongest missing lemma is the extra slice direction on the signatures
`(-3, -3)`, `(-3, 3)`, and `(3, -3)`. That triple has joint slice
kernel 10, and 10 is the maximum among the 1330 triples.

## What this does not do

- It does not select a scale.
- It does not classify the extra direction in a joint kernel of
  dimension 10.
- It does not claim that the 84-dimensional bond space has been
  classified.
- It does not cut the normalised bond space on the 48-point alphabet.
- It does not supply a formation site, probability, or rate.

## Runner

`scripts/equal_height_signature_with_one_partner_2026_10_10.py`
repeats the group, the joint-kernel counts, the normal forms, and the
resultant.

## Imports

No formation site, probability, rate, or selected scale is imported.
The proper rotations and the height pairs are enumerated here. Which
single signature is order-blind is the single-signature note. The
converse used there is the 2026-09-22 parent, quoted above.
