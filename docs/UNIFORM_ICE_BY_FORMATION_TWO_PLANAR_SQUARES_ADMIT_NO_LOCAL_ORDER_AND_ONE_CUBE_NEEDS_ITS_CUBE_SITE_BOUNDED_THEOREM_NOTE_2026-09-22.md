---
claim_id: uniform_ice_by_formation_two_planar_squares_admit_no_local_order_and_one_cube_needs_its_cube_site_bounded_theorem_note_2026-09-22
claim_type: bounded_theorem
claim_scope: "For the declared finite record law, a fixed order can reproduce it with local conditional kernels iff every new site's conditional given the whole formed set depends only on its formed neighbours. Complete exact searches find no order on one square without a plaquette coordinator and an order with it. On two adjacent squares neither the coordinator-free model nor any of five declared coordinator/record variants admits an order.  Full records with plaquettes reach at most 7 of 15 sites on two squares; empty vertex records reach at most 11. A cube with its six plaquettes but no cube record reaches at most 5 of 26 sites. Adding the twelve-edge cube record permits cube, plaquettes, links, vertices in that order. Private-link weighted totals are 10016,501632,6316544 for the square, two squares and cube. Orders are fixed deterministic orders. Each conditional draw uses fresh randomness and depends only on the records of the actual formed neighbours (with the declared hole semantics). The sufficiency criterion permits site/stage-specific kernels; it does not establish a single position-independent covariant law. Negative results in this broader class still exclude any more restrictive fixed-order law. Adaptive orders, hidden shared state, and mixtures whose component finished laws differ from the target are not excluded. Private links are marginalized into the stated grid-record weights; arbitrary hidden private-link formation schemes are not searched. These variants do not prove that every top cell in every model needs its own coordinator."
upstream_dependencies:
  - uniform_ice_by_formation_the_square_loop_obstruction_the_plaquette_coordinator_and_plans_bounded_theorem_note_2026-09-22
  - minimal_axioms
runner: scripts/uniform_ice_two_squares_no_local_formation_order_complete_order_search_2026_09_22.py
---

# Fixed-order local formation searches on one square, two squares and one cube

**Date:** 2026-09-23
**Type:** bounded_theorem

## Result and scope

For the declared finite record law, a fixed order can reproduce it with local conditional kernels iff every new site's conditional given the whole formed set depends only on its formed neighbours. Complete exact searches find no order on one square without a plaquette coordinator and an order with it. On two adjacent squares neither the coordinator-free model nor any of five declared coordinator/record variants admits an order.

Full records with plaquettes reach at most 7 of 15 sites on two squares; empty vertex records reach at most 11. A cube with its six plaquettes but no cube record reaches at most 5 of 26 sites. Adding the twelve-edge cube record permits cube, plaquettes, links, vertices in that order. Private-link weighted totals are 10016, 501632, 6316544 for the square, two squares and cube.

## Boundaries and non-claims

Orders are fixed deterministic orders. Each conditional draw uses fresh randomness and depends only on the records of the actual formed neighbours (with the declared hole semantics). The sufficiency criterion permits site/stage-specific kernels; it does not establish a single position-independent covariant law. Negative results in this broader class still exclude any more restrictive fixed-order law. Adaptive orders, hidden shared state, and mixtures whose component finished laws differ from the target are not excluded. Private links are marginalized into the stated grid-record weights; arbitrary hidden private-link formation schemes are not searched. These variants do not prove that every top cell in every model needs its own coordinator.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "Conditional finite ice measures, formation and supplied transfer models"
source_of_blocker_text: frontier_question
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Preserve finite hypotheses and test extensions separately"
conditional_surface_status: "The declared model, order, records and numerical tolerances only"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "Conditional mathematics and bounded computation; no retained grade asserted"
```

## Premises and declared objects

- **The formation reading.** A site forms with a law that depends on its
  formed nearest neighbours; hole semantics apply. A formation is exact
  when its finished record law is the declared law, with no unrecorded
  site.
- **Windows.** One coarse square, the 2 x 1 rectangle, and one cube. Each
  vertex's other links are private to it: 4 at square corners, 3 at the
  rectangle's middle vertices and at every cube vertex.
- **Plaquette sites.** Each is the nearest neighbour of its square's four
  links.
- **The cube site.** It is the nearest neighbour of the cube's six
  plaquette sites and records the cube's twelve edges. On the cube,
  vertices and plaquettes record their own edge patterns.
- **The uniform ice measure.** It weighs a grid pattern by
  prod_v C(private links, 3 - grid sum).
- **The declared record schemes.** Grid links record their occupation.
  Vertices and plaquettes carry full incident-grid patterns unless varied:
  (vertex,plaquette) = (pattern,pattern), (nothing,pattern),
  (pattern,nothing), (count,pattern), (pattern,count).


## Theorem 1 — The fixed-order conditional-kernel criterion

Suppose a formation is exact. Then each site's law, given the sites
formed before it, is the rule's output on its formed neighbours. So it is
the declared law's conditional given the formed set, and it depends only
on the formed neighbours.

Conversely, take an order in which every site's declared conditional,
given the formed set, depends only on its formed neighbours. Let the rule
be that conditional. The chain rule then reproduces the declared law,
with no unrecorded site.

Private links are summed out to define the target grid-record law.
They are not additional hidden formation sites in these searches.


## Theorem 2 — The search

Start from the empty set and add a site x to a formed set F when the
declared law's conditional of x given F equals its conditional given
x's formed neighbours. The reachable sets are exactly the prefixes of
admissible orders. The full set is:
- unreachable on one square without the plaquette site;
- reachable with it;
- unreachable on two squares, with and without plaquette sites, for
  every scheme tested.

The largest reachable sets are reported. A budget guard stops a search
at 5000 reachable sets (planar) or 1000 (cube) and fails its check; the
real searches reach at most 2560 and 173 sets, so the guard never binds
and every search above is complete.


## Theorem 3 — One cube

On one cube, the search with the six plaquette sites but no cube site
finds no complete order, and the largest admissible formed set has 5 of
the 26 sites. With the cube site, whose local record is its twelve
edges, the cube-first order is admissible site by site: the cube, then
the plaquettes, links and vertices. So one cube is coordinated exactly
by its cube site, as one square is by its plaquette site.


## No-go discipline and falsifiers

Negative claims concern only the stated fixed models and completed searches.
Alternative records, hidden state, adaptive orders, larger units, different
rules and different boundary conditions require separate tests. Caps must
not bind for an exhaustive verdict. Finite spectral patterns do not prove
infinite-cross-section physics. A counterexample under the exact hypotheses,
a failed independent count, or a failed stated control falsifies its result.
No other claim is graded, unlocked or audited here.

## Dependencies and provenance

- [Landed companion from PR #8686](UNIFORM_ICE_BY_FORMATION_THE_SQUARE_LOOP_OBSTRUCTION_THE_PLAQUETTE_COORDINATOR_AND_PLANS_BOUNDED_THEOREM_NOTE_2026-09-22.md)

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md)

Original context and author review history remain recoverable from the
originating PR. Historical mutation claims are not current review evidence.
The landing review preserves conditional proofs and narrows unsupported
extensions; no new axiom, primitive or audit grade is adopted.

## Verification

```bash
python3 scripts/uniform_ice_two_squares_no_local_formation_order_complete_order_search_2026_09_22.py
```

The runner exits nonzero on failure. Its fresh captured cache is
`logs/runner-cache/uniform_ice_two_squares_no_local_formation_order_complete_order_search_2026_09_22.txt`.
Analytic statements require the proofs above in addition to finite checks.
