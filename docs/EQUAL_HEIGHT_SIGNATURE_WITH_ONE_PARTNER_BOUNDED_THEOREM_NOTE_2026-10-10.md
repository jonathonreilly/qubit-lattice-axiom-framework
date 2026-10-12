---
claim_id: equal_height_signature_with_one_partner_bounded_theorem_note_2026-10-10
claim_type: open_gate
claim_scope: "On the proper orbit of (1, 2, 3), every two height signatures have joint slice-kernel dimension 6, so a slice-zero soldered kernel on one equal-height signature and one partner is the direct sum of the two signature kernels. Beside an opposite partner the pair moments force the equal-height block to zero, and the kernel is that opposite signature, inside the eighteen cap-pair kernels. Beside a second equal-height signature both blocks are zero. The triple (-3, -3), (-3, 3), (3, -3) has joint slice kernel 10 and is outside this ansatz. No scale is selected."
upstream_dependencies:
  - minimal_axioms
  - order_blind_nearest_neighbour_formation_independence_beyond_neighbours_unsoldered_constancy_and_soldered_escape_bounded_theorem_note_2026-09-22
  - single_height_signature_order_blind_kernel_bounded_theorem_note_2026-10-10
runner: scripts/equal_height_signature_with_one_partner_2026_10_10.py
---

# An equal-height signature does not leave the eighteen beside one partner

**Date:** 2026-10-10

**Type:** open_gate

**Audit:** unset; independent audit remains a separate lane

**Status:** open_gate

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
target_claim_type: open_gate
claim_type_reason: "Pair moments force an equal-height signature to zero beside one opposite or equal-height partner."
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "Other generic orbits and higher-rank bond spaces are not classified."
source_of_blocker_text: frontier_question
reachability_to_target: prunes
artifact_role: partial_narrowing_proposal
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

**Landing status:** partial narrowing with an incomplete formal no-go packet.
The scoped arguments and exact checks below are preserved for development;
this note does not carry a no-go packet PASS or retained-grade authority.
The missing N1 route packet is distinct from the mathematical validity of
the finite ansatz results.

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

On each equal-height block the corrected pair moments reduce to

`M1 = u^2 - 2 v w - w^2 = 0`,

`M2 = u v + (1/2) v^2 + v w + (1/2) w^2 = 0`,

`M3 = u w - (1/2) v^2 + (1/2) w^2 = 0`.

Their only common rational (indeed real) zero is the origin. The identity
`v M3 - w M2 = -(v+w)(v^2+w^2)/2` implies `v = -w` or
`v = w = 0`. In the first case `M1 = u^2+w^2`; in the second
`M1 = u^2`. Both force all three coordinates to vanish.
This argument is over the rationals or reals, not the complex numbers.

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
them with the normal forms above. The zero of the corrected three quadrics follows from the
sum-of-squares identity above. The drop from an opposite signature to
the eighteen is the single-signature note.

**Obligations.** Proved here: the direct sum on every pair, the three
corrected normal forms, the axis patterns, and the real-zero identity. Cited from the
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
repeats the group, the joint-kernel counts, the corrected normal forms,
and the exact real-zero polynomial identity.

## Imports

No formation site, probability, rate, or selected scale is imported.
The proper rotations and the height pairs are enumerated here. Which
single signature is order-blind is the single-signature note. The
converse used there is the 2026-09-22 parent, quoted above.


## No-Go Discipline Gate

**Packet status: incomplete; no PASS claimed.** This is a partial narrowing
proposal under the displayed finite ansatz, not a framework-wide exclusion.

- **N1:** The actual routes here are the finite orbit/slice reduction and
  the explicit algebraic argument in the Proof. Related coefficient choices
  are not five independent approach families. The five-family packet is
  absent; no route count or retained prior authority is invented.
- **N2:** The alphabet, covariance, support and coefficient restrictions
  define one ansatz. No count of independent physical walls is asserted.
- **N3:** The uniform finite-record model and any order-blind converse are
  explicit mathematical inputs. They supply no physical selection, formation
  rate, empirical scale or additional framework primitive.
- **N4:** The Imports and Obligations identify which parent result is used.
  A finite kernel rank, a two-centre cross sum and a normalized neighbour
  product are different statements; none is substituted for another.
- **N5:** The primary runner reports the finite resolution it executes.
  Mode spectra, evolving site ensembles and lattice-wide dynamics are not
  computed. Any all-window consequence uses the cited analytical converse
  with strict positivity, not a lattice simulation.
- **N6:** No new axiom is requested or declared necessary. Expanding the
  ansatz is legitimate further work and is not ruled out by these results.
- **N7:** The strongest broader escape is to allow additional support
  signatures or coupled height sectors: cancellation can change when the
  partner domain changes. A full-space classification must derive the joint
  slice and product equations and prove their solution set; the present
  restricted result supplies no such closure. Inside the stated ansatz the
  displayed exact proof, rather than failure to find an escape, is the claim.
- **N8:** The cited parent and companion notes exhibit successive escapes
  from smaller cap and cross spans. Those examples explicitly prohibit
  treating any restricted span classification as closure of the full bond
  space. Historical next-step statements are local frontiers, not evidence
  that later companion results remain unproved.


## Review correction

The original quadratic assembler skipped a cross term when the first
left coefficient was zero, although the symmetric term could be nonzero.
The corrected assembler retains both terms. The earlier fractional
normal form and its nonzero quartic resultant described the wrong
polynomials and are withdrawn. The corrected real-zero proof above
preserves the scoped equal-height conclusion.
