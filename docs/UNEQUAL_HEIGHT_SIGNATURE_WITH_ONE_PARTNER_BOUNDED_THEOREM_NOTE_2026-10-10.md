---
claim_id: unequal_height_signature_with_one_partner_bounded_theorem_note_2026-10-10
claim_type: open_gate
claim_scope: "On the proper 24-point orbit, corrected pair-moment assembly certifies direct elimination of the unequal block in 168 of 240 ordered unequal-plus-partner cases. The other 72 cases are unresolved by this linear monomial test. The former all-240 certificate dropped symmetric cross terms and is withdrawn. Failure of this sufficient test is not a nonzero solution or a disproof of the larger conjecture. No scale or physical dynamics is selected."
upstream_dependencies:
  - minimal_axioms
  - order_blind_nearest_neighbour_formation_independence_beyond_neighbours_unsoldered_constancy_and_soldered_escape_bounded_theorem_note_2026-09-22
  - single_height_signature_order_blind_kernel_bounded_theorem_note_2026-10-10
runner: scripts/unequal_height_signature_with_one_partner_2026_10_10.py
---

# Partial unequal-height elimination with 72 unresolved partner cases

**Date:** 2026-10-10

**Type:** open_gate

**Audit:** unset; independent audit remains a separate lane

**Status:** open_gate

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
target_claim_type: open_gate
claim_type_reason: "The corrected finite monomial certificate resolves 168 cases; 72 need an additional argument."
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "Other generic orbits and higher-rank bond spaces are not classified."
source_of_blocker_text: frontier_question
reachability_to_target: prunes
artifact_role: partial_narrowing_proposal
next_trace_action: "Solve the real or rational zero sets of the 72 DIRECT_TEST_UNRESOLVED pairs; distinguish nonlinear consequences from membership in the linear moment span before claiming all-240 elimination."
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

**Landing status:** partial narrowing with an incomplete formal no-go packet.
The scoped arguments and exact checks below are preserved for development;
this note does not carry a no-go packet PASS or retained-grade authority.
The missing N1 route packet is distinct from the mathematical validity of
the finite ansatz results.

**Target.** Inside the ansatz of a slice-zero soldered kernel supported
on one unequal height signature and at most one other signature, decide
whether any order-blind kernel lies outside the eighteen cap-pair
kernels.

**Ansatz.** Height signatures are the reversal classes of the pair
`(a·d, b·d)`. An unequal signature has two heights that are neither
equal nor opposite. The kernel is bond-symmetric and soldered, every
slice sums to 0, and its support meets one unequal signature and at
most one other signature.

**Conclusion.** The corrected runner certifies 168 of the 240 ordered
unequal-plus-partner cases by the direct linear monomial test. In each
certified case the six unequal-block quadratic monomials belong to the
pair-moment span without partner terms. In particular all three squares
vanish, so the unequal block is zero. The single-signature result then
classifies the remaining partner under its own assumptions.

The other 72 ordered pairs are printed as `DIRECT_TEST_UNRESOLVED` by the
runner and are not eliminated by this test. For example `(-3, -2)` with
`(-3, -1)` is unresolved. This is a failure of the proposed linear
certificate, not evidence that a nonzero solution exists. Nonlinear
consequences of the quadratic equations may still force the block to zero.
No universal one-partner elimination theorem is asserted here.

**Derivation and correction.** For coefficient vectors `l` and `r`, the
coefficient of `x_i x_j`, for `i < j`, in their product is
`l_i r_j + l_j r_i`. The previous assembler skipped the second term when
`l_i = 0`. For `l=(0,1)` and `r=(1,0)` that loses the entire product
`x_0 x_1`. Both symmetric terms are now retained before summing centre
records. Exact row reduction of those corrected moments gives the stated
168/72 split. The original assertion of 240 pure-monomial eliminations is
withdrawn. The equal-height control still fails the direct square test.

**Open obligation.** For each of the 72 listed cases, prove that all real
or rational solutions have zero unequal block, or give a nonzero solution
and then test all neighbour-product and positivity conditions. A pair-moment
solution alone is not a positive, order-blind factor. The single-signature
classification cannot resolve a coupled case before elimination is proved.

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
repeats the group, the corrected 240-case scan, the 168 successful direct
eliminations, the explicit 72-case unresolved list, and the equal-height
control. A passing execution certifies this partial result only.

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
  restricted result supplies no such closure. Within the present two-signature
  ansatz, 72 pairs also remain unresolved by this certificate.
- **N8:** The cited parent and companion notes exhibit successive escapes
  from smaller cap and cross spans. Those examples explicitly prohibit
  treating any restricted span classification as closure of the full bond
  space. Historical next-step statements are local frontiers, not evidence
  that later companion results remain unproved.
