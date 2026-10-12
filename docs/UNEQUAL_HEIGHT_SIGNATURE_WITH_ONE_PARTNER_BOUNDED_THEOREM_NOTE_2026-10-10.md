---
claim_id: unequal_height_signature_with_one_partner_bounded_theorem_note_2026-10-10
claim_type: bounded_theorem
claim_scope: "On the proper orbit of (1, 2, 3), let a soldered bond-symmetric kernel with every slice sum 0 be supported on one unequal height signature and at most one other height signature. The six quadratic monomials in the unequal coordinates are consequences of the pair moments, with no remaining term, so those coordinates vanish. The kernel drops to the partner signature. By the single-signature classification, it is order-blind outside zero only when that partner has opposite heights, and then it lies in the eighteen cap-pair kernels. The square test does not force an equal-height signature to zero beside one opposite partner. No scale is selected."
upstream_dependencies:
  - minimal_axioms
  - order_blind_nearest_neighbour_formation_independence_beyond_neighbours_unsoldered_constancy_and_soldered_escape_bounded_theorem_note_2026-09-22
  - single_height_signature_order_blind_kernel_bounded_theorem_note_2026-10-10
runner: scripts/unequal_height_signature_with_one_partner_2026_10_10.py
---

# An unequal height signature vanishes beside one partner

**Date:** 2026-10-10

**Type:** bounded_theorem

**Audit:** unset; independent audit remains a separate lane

**Status:** proposed_retained

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/unequal_height_signature_with_one_partner_2026_10_10.py`](../scripts/unequal_height_signature_with_one_partner_2026_10_10.py)

**Parents:** the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md),
[the order-blind formation note](ORDER_BLIND_NEAREST_NEIGHBOUR_FORMATION_INDEPENDENCE_BEYOND_NEIGHBOURS_UNSOLDERED_CONSTANCY_AND_SOLDERED_ESCAPE_BOUNDED_THEOREM_NOTE_2026-09-22.md),
and the [single height-signature note](SINGLE_HEIGHT_SIGNATURE_ORDER_BLIND_KERNEL_BOUNDED_THEOREM_NOTE_2026-10-10.md).

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Pair moments force an unequal height signature to zero beside any one partner signature."
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "Other generic orbits and higher-rank bond spaces are not classified."
source_of_blocker_text: frontier_question
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "Ask whether an equal-height signature beside one opposite signature, or two equal-height signatures, can leave the eighteen cap-pair kernels. The square test does not decide it."
conditional_surface_status: "one proper orbit of (1, 2, 3); one unequal height signature plus at most one partner; uniform average"
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
on one unequal height signature and at most one other signature, decide
whether any order-blind kernel lies outside the eighteen cap-pair
kernels.

**Ansatz.** Height signatures are the reversal classes of the pair
`(a·d, b·d)`. An unequal signature has two heights that are neither
equal nor opposite. The kernel is bond-symmetric and soldered, every
slice sums to 0, and its support meets one unequal signature and at
most one other signature.

**Conclusion.** For each of the twelve unequal signatures and each of
the other twenty signatures, row reduction of the pair moments puts the
six monomials in the unequal coordinates in pivot position, with zeros
in every partner monomial. Those monomials vanish, so the unequal
coordinates are zero. The kernel is supported on the partner alone.

The single-signature note then applies. A nonzero order-blind kernel on
one signature exists only for opposite heights, and that kernel lies in
the eighteen cap-pair kernels. An equal-height partner, or a second
unequal partner, has only the zero order-blind kernel. No order-blind
kernel in this ansatz lies outside the eighteen.

The same square test does not force the equal-height signature
`(-3, -3)` to zero beside the opposite signature `(3, -3)`. That pair,
and a sum of two equal-height signatures, stay outside this ansatz.

**Proof.** The runner enumerates the group, the 21 signatures, and the
three-dimensional slice kernel of each. For every unequal-plus-partner
pair it builds the quadratic pair moments and row-reduces them with the
unequal monomials first. The control pair `(-3, -3)` with `(3, -3)`
fails that square test, so the test is not vacuous. The drop from the
partner to a single signature, and the order-blindness of the opposite
signatures, are the single-signature note.

**Obligations.** Proved here: the 240 square eliminations and the
equal-height control. Cited from the single-signature note, and not
re-proved: which single signatures are order-blind. Cited from the
2026-09-22 parent, through that note: the converse. The strongest
missing lemma is an equal-height signature beside one opposite
signature, or two equal-height signatures.

## What this does not do

- It does not select a scale.
- It does not claim that an equal-height signature beside an opposite
  signature is zero. The square test leaves that pair open.
- It does not claim that the 84-dimensional bond space, or a kernel on
  three signatures, has been classified.
- It does not cut the normalised bond space on the 48-point alphabet.
- It does not supply a formation site, probability, or rate.

## Runner

`scripts/unequal_height_signature_with_one_partner_2026_10_10.py`
repeats the group, the 240 eliminations, and the equal-height control.

## Imports

No formation site, probability, rate, or selected scale is imported.
The proper rotations and the height pairs are enumerated here. Which
single signature is order-blind is the single-signature note. The
converse used there is the 2026-09-22 parent, quoted above.
