---
claim_id: modulus_three_triple_complement_bounded_theorem_note_2026-10-10
claim_type: open_gate
claim_scope: "On the proper orbit of (1, 2, 3), the joint slice kernel on the signatures (-3, -3), (-3, 3), and (3, -3) has dimension 10. The complement of the three signature kernels is one line, with values -1, +1, and +1 on one bond orbit of each signature. Every record has two live directions. The pair moment on the opposite x-directions at (-3, -2, -1) is 2, with uniform average 1/12, so the line is not order-blind. Its equal-height component puts it outside the eighteen. Mixtures with the signature kernels are not in this ansatz. No scale is selected."
upstream_dependencies:
  - minimal_axioms
  - order_blind_nearest_neighbour_formation_independence_beyond_neighbours_unsoldered_constancy_and_soldered_escape_bounded_theorem_note_2026-09-22
  - single_height_signature_order_blind_kernel_bounded_theorem_note_2026-10-10
runner: scripts/modulus_three_triple_complement_2026_10_10.py
---

# The modulus-3 triple complement is not order-blind

**Date:** 2026-10-10

**Type:** open_gate

**Audit:** unset; independent audit remains a separate lane

**Status:** open_gate

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/modulus_three_triple_complement_2026_10_10.py`](../scripts/modulus_three_triple_complement_2026_10_10.py)

**Parents:** the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md),
[the order-blind formation note](ORDER_BLIND_NEAREST_NEIGHBOUR_FORMATION_INDEPENDENCE_BEYOND_NEIGHBOURS_UNSOLDERED_CONSTANCY_AND_SOLDERED_ESCAPE_BOUNDED_THEOREM_NOTE_2026-09-22.md),
and the [single height-signature note](SINGLE_HEIGHT_SIGNATURE_ORDER_BLIND_KERNEL_BOUNDED_THEOREM_NOTE_2026-10-10.md).

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: open_gate
claim_type_reason: "The one-dimensional complement on the modulus-3 triple has pair moment 2."
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "Other generic orbits and higher-rank bond spaces are not classified."
source_of_blocker_text: frontier_question
reachability_to_target: prunes
artifact_role: partial_narrowing_proposal
next_trace_action: "Ask whether a mixture of this complement line with the three signature kernels can cancel the moment and leave the eighteen. Do not restate the pure-line cut."
conditional_surface_status: "one proper orbit of (1, 2, 3); the complement line on signatures (-3, -3), (-3, 3), and (3, -3); uniform average"
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

**Target.** Inside the one-dimensional complement of the three signature
kernels in the joint slice kernel on `(-3, -3)`, `(-3, 3)`, and
`(3, -3)`, decide whether that line is an order-blind kernel outside
the eighteen cap-pair kernels.

**Ansatz.** The kernel is bond-symmetric and soldered, and it lies in
the joint slice kernel of those three signatures. It is orthogonal, in
the quotient, to the direct sum of the three signature kernels. A
mixture of the line with those kernels is not in this ansatz.

**Conclusion.** The joint slice kernel has dimension 10 on 12 bond
orbits. The three signature kernels have rank 9 inside it. The
complement is one line. On the record `(-3, -2, -1)` its values are
`-1` from `(-3, -2, -1)` to `(-3, 2, 1)` along `-e_x`, signature
`(-3, -3)`, and `+1` from `(-3, -2, -1)` to `(3, 2, -1)` along `-e_x`,
signature `(3, -3)`. Along `e_x` the second bond has signature
`(-3, 3)` and value `+1`. Those are the only three nonzero bond
orbits.

Every record activates two directions. The sum over the orbit of the
product of the values on `-e_x` and `e_x` at the right record
`(-3, -2, -1)` is `2`. The uniform average is `1/12`. The neighbour
product of those two directions does not have mean 1, so the line is
not order-blind.

The value `-1` lies on signature `(-3, -3)`. The single-signature note
places the eighteen cap-pair kernels on the opposite signatures, so
this line is outside the eighteen. It is a slice-zero kernel outside
that span, and it is not order-blind.

**Proof.** The runner enumerates the group and the bond orbits,
row-reduces the joint slice kernel and the three signature kernels, and
evaluates the complement on the witness bonds. The moment is that
explicit sum.

**Obligations.** Proved here: dimension 10, the one-line complement,
the witness values, the two live directions, and the moment `2`. Cited
from the single-signature note, and not re-proved: the eighteen are
the opposite-signature kernels. The parent converse is not applied.
The moment already fails. The strongest missing lemma is a mixture of
this line with the three signature kernels.

## What this does not do

- It does not select a scale.
- It does not claim that a mixture of this line with the signature
  kernels has a nonzero moment.
- It does not claim that the 84-dimensional bond space has been
  classified.
- It does not cut the normalised bond space on the 48-point alphabet.
- It does not supply a formation site, probability, or rate.

## Runner

`scripts/modulus_three_triple_complement_2026_10_10.py` repeats the
group, the complement line, and the moment `2`.

## Imports

No formation site, probability, rate, or selected scale is imported.
The proper rotations and the witness bonds are enumerated here. The
support of the eighteen is the single-signature note. The parent
converse is not applied to this line.


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
