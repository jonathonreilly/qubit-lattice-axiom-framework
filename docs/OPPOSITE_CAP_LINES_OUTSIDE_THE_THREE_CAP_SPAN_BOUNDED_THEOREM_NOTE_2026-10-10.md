---
claim_id: opposite_cap_lines_outside_the_three_cap_span_bounded_theorem_note_2026-10-10
claim_type: open_gate
claim_scope: "On the proper orbit of (1, 2, 3), the sign of the transverse coordinate product on the cap a·d = -m, for each m in {1, 2, 3}, defines a soldered bond-symmetric line. For a parameter of absolute value less than 1 the factors are strictly positive, and every one of the 729 neighbour-weight patterns has product mean 1. The 2026-09-22 converse then makes each line order-blind on every window. The centre (1, -2, -3) with neighbour (1, 2, 3) along e_z has level -3 product -1 and every positive-cap product 0, so the line is outside the span of the caps a·d = 1, 2, 3. The same separation holds for levels -1 and -2. No parameter is selected. Higher-rank kernels are not classified."
upstream_dependencies:
  - minimal_axioms
  - order_blind_nearest_neighbour_formation_independence_beyond_neighbours_unsoldered_constancy_and_soldered_escape_bounded_theorem_note_2026-09-22
runner: scripts/opposite_cap_lines_outside_the_three_cap_span_2026_10_10.py
---

# Opposite caps sit outside the three positive cap signs

**Date:** 2026-10-10

**Type:** open_gate

**Audit:** unset; independent audit remains a separate lane

**Status:** open_gate

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/opposite_cap_lines_outside_the_three_cap_span_2026_10_10.py`](../scripts/opposite_cap_lines_outside_the_three_cap_span_2026_10_10.py)

**Parents:** the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) and
[the order-blind formation note](ORDER_BLIND_NEAREST_NEIGHBOUR_FORMATION_INDEPENDENCE_BEYOND_NEIGHBOURS_UNSOLDERED_CONSTANCY_AND_SOLDERED_ESCAPE_BOUNDED_THEOREM_NOTE_2026-09-22.md).

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: open_gate
claim_type_reason: "Three explicit opposite-cap lines meet the product-mean conditions and their centre slices lie outside the positive caps."
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "Other generic orbits and higher-rank bond spaces are not classified."
source_of_blocker_text: frontier_question
reachability_to_target: prunes
artifact_role: partial_narrowing_proposal
next_trace_action: "Ask whether a soldered order-blind factor on this orbit can have a slice outside the six oriented caps."
conditional_surface_status: "one proper orbit of (1, 2, 3); uniform average; opposite cap a·d = -m; absolute parameter below 1"
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
properties is order-blind on every window." Its exhibited line uses "the
sign of the product of the two coordinates of a transverse to d when
a.d = 3, and 0 otherwise" in the factor "1 + kappa X_d(a) X_-d(b)". It
leaves the sentence "Other generic orbits and higher-rank bond spaces
are not classified."

## Theorem

**Landing status:** partial narrowing with an incomplete formal no-go packet.
The scoped arguments and exact checks below are preserved for development;
this note does not carry a no-go packet PASS or retained-grade authority.
The missing N1 route packet is distinct from the mathematical validity of
the finite ansatz results.

**Target.** On the proper orbit of `(1, 2, 3)`, each opposite cap
`a·d = -m` for `m` in `{1, 2, 3}` carries a strictly positive soldered
bond-symmetric line outside the span of the caps `a·d = 1, 2, 3`, and
the parent converse makes that line order-blind.

**Conclusion.** Let `O` be the proper-cubic orbit of `(1, 2, 3)`. For a
direction `d` and a level `k` in `{-1, -2, -3}`, let `C_{d,k}(a)` be the
sign of the product of the two coordinates transverse to `d` when
`a·d = k`, and 0 otherwise. The transverse axes are taken in increasing
coordinate index. Then

`phi_{k,d}(a, b) = 1 + t C_{d,k}(a) C_{-d,k}(b)`

satisfies `phi_{k,d}(a, b) = phi_{k,-d}(b, a)`, because the two cap
values are multiplied and integer multiplication commutes. The same
product is unchanged by every proper rotation. For `|t| < 1` every
factor lies in `{1-t, 1, 1+t}` and is positive. Each opposite cap has
4 points and mean 0. The six caps of one level are disjoint and cover
the orbit, so each record activates one direction. Every one of the 729
patterns of neighbour weights in `{-1, 0, 1}` therefore has product
mean 1. The three levels are distinct. Along `e_z`, the centre
`(1, -2, -3)` and the neighbour `(1, 2, 3)` have level `-3` product
`-1` and positive-level product 0. The same separation holds for levels
`-1` and `-2`. For `v_d` in the span of the caps `a·d = 1, 2, 3`, the kernel
`v_d(a) v_{-d}(b)` vanishes on those bonds, so the factor
`1 + t v_d(a) v_{-d}(b)` equals 1 there. The opposite-cap factor
differs from 1 when its coefficient is nonzero. The parent converse
makes each strictly positive line order-blind on every window.

**Proof.** The runner enumerates the 24 proper rotations and the orbit.
Covariance is the equality of the moved and unmoved cap products.
Quarter-turns about a fixed direction, the trace-1 rotations, flip the
cap sign, and at least one such pair is present. Six disjoint caps of
4 points on a 24-point orbit cover every record exactly once, so a
product of factors equals `1` plus one weighted cap, and the mean is 1.
The named bond is in the orbit, its level `-3` product is `-1`, and
each product of positive caps on that bond is 0. For levels `-1` and
`-2` the runner finds a bond of the same shape: the centre lies in the
opposite cap, so its axis coordinate excludes every positive level on
that direction, while the neighbour makes the opposite product nonzero.
At half the parameter the factor values are exactly `1/2`, `1`, and
`3/2`.

**Obligations.** Proved here: the three opposite-cap formulas, their
covariance, the product means, positivity at half the parameter, the
separation of the three levels, and the witness bonds. Cited from the
parent, and not re-proved: the converse that a bond-symmetric family
with these product means is order-blind on every window. The strongest
missing lemma is a soldered order-blind factor on this orbit whose
slices are not among the six oriented caps. Higher-rank kernels stay
outside this count.

## What this does not do

- It does not select `t`, or any other factor.
- It does not claim that these three lines, or these three together
  with the positive caps, are the whole order-blind set.
- It does not classify a kernel whose slices leave the six oriented caps.
- It does not treat the 48-point chiral pair or any other alphabet.
- It does not supply a formation site, probability, or rate.

## Runner

`scripts/opposite_cap_lines_outside_the_three_cap_span_2026_10_10.py`
repeats the group, the orbit, the three opposite caps, the product
means, and the witness bonds.

## Imports

No formation site, probability, rate, or selected parameter is imported.
The proper rotations and the opposite caps are enumerated here.
Order-blindness of a family that already meets the product-mean
conditions is the parent converse, quoted above.


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
