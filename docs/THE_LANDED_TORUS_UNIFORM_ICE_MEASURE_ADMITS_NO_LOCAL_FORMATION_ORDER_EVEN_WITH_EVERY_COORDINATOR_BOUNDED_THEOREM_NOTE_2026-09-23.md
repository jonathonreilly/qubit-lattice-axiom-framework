---
claim_id: the_landed_torus_uniform_ice_measure_admits_no_local_formation_order_even_with_every_coordinator_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "On the fine Z_4^3 torus, direct enumeration gives9600 ice link patterns, with8 vertex,24 link,24 plaquette and8 cube sites. The full-record closed search visits65 sets and finds no complete order. Its maximum size is19, with a recorded attaining set of one cube site,6 plaquettes and12 links. Three specified coarser record schemes also have no order.  A product-measure control on12 fair and12 fixed links does admit an order. Searches compare integer conditional cross-products and fail if their declared work cap binds. Orders are fixed deterministic orders. Each conditional draw uses fresh randomness and depends only on the records of the actual formed neighbours (with the declared hole semantics). The sufficiency criterion permits site/stage-specific kernels; it does not establish a single position-independent covariant law. Negative results in this broader class still exclude any more restrictive fixed-order law. Adaptive orders, hidden shared state, and mixtures whose component finished laws differ from the target are not excluded. Private links are marginalized into the stated grid-record weights; arbitrary hidden private-link formation schemes are not searched. Constant-record coordinator sites remain in the declared neighbour graph; the tests do not classify all altered graphs or all maximal sets."
upstream_dependencies:
  - minimal_axioms
  - uniform_ice_by_formation_two_planar_squares_admit_no_local_order_and_one_cube_needs_its_cube_site_bounded_theorem_note_2026-09-22
  - uniform_ice_by_formation_two_adjacent_cubes_admit_no_local_order_even_with_both_cube_sites_bounded_theorem_note_2026-09-23
runner: scripts/landed_torus_uniform_ice_admits_no_local_formation_order_closed_set_search_2026_09_23.py
---

# No fixed local formation order for the declared finite torus ice law

**Date:** 2026-09-23
**Type:** bounded_theorem

## Result and scope

On the fine Z_4^3 torus, direct enumeration gives 9600 ice link patterns, with 8 vertex, 24 link, 24 plaquette and 8 cube sites. The full-record closed search visits 65 sets and finds no complete order. Its maximum size is 19, with a recorded attaining set of one cube site, 6 plaquettes and 12 links. Three specified coarser record schemes also have no order.

A product-measure control on 12 fair and 12 fixed links does admit an order. Searches compare integer conditional cross-products and fail if their declared work cap binds.

## Boundaries and non-claims

Orders are fixed deterministic orders. Each conditional draw uses fresh randomness and depends only on the records of the actual formed neighbours (with the declared hole semantics). The sufficiency criterion permits site/stage-specific kernels; it does not establish a single position-independent covariant law. Negative results in this broader class still exclude any more restrictive fixed-order law. Adaptive orders, hidden shared state, and mixtures whose component finished laws differ from the target are not excluded. Private links are marginalized into the stated grid-record weights; arbitrary hidden private-link formation schemes are not searched. Constant-record coordinator sites remain in the declared neighbour graph; the tests do not classify all altered graphs or all maximal sets.

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
- **The torus.** Doubled coordinates mod 4: vertices even, links one odd
  coordinate, plaquette sites two, cube sites three. Nearest neighbours
  are at distance 1 mod 4.
- **The uniform ice measure.** It is uniform on the link patterns with 3
  of every vertex's 6 links occupied. There are 9600, enumerated directly,
  the count of the landed note.
- **Records.** Links record their occupation. Vertices, plaquettes and
  cube sites record their own links' pattern, or nothing.


## Theorem — No order on the torus

By the criterion of open PR 8715 and the closure lemma of open PR 8719, a
depth-first search over closed formed sets decides whether an exact
order exists. On the torus it visits 65 closed sets and finds no
complete one. One recorded maximum-size set is one cube's cube site, plaquettes and
edges; the bound on every reachable set is 19. Every conditional is compared by integer cross-multiplication
over the 9600 states.


## No-go discipline and falsifiers

Negative claims concern only the stated fixed models and completed searches.
Alternative records, hidden state, adaptive orders, larger units, different
rules and different boundary conditions require separate tests. Caps must
not bind for an exhaustive verdict. Finite spectral patterns do not prove
infinite-cross-section physics. A counterexample under the exact hypotheses,
a failed independent count, or a failed stated control falsifies its result.
No other claim is graded, unlocked or audited here.

## Dependencies and provenance

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md)
- [Companion result from PR #8715](UNIFORM_ICE_BY_FORMATION_TWO_PLANAR_SQUARES_ADMIT_NO_LOCAL_ORDER_AND_ONE_CUBE_NEEDS_ITS_CUBE_SITE_BOUNDED_THEOREM_NOTE_2026-09-22.md)
- [Companion result from PR #8719](UNIFORM_ICE_BY_FORMATION_TWO_ADJACENT_CUBES_ADMIT_NO_LOCAL_ORDER_EVEN_WITH_BOTH_CUBE_SITES_BOUNDED_THEOREM_NOTE_2026-09-23.md)

Original context and author review history remain recoverable from the
originating PR. Historical mutation claims are not current review evidence.
The landing review preserves conditional proofs and narrows unsupported
extensions; no new axiom, primitive or audit grade is adopted.

## Verification

```bash
python3 scripts/landed_torus_uniform_ice_admits_no_local_formation_order_closed_set_search_2026_09_23.py
```

The runner exits nonzero on failure. Its fresh captured cache is
`logs/runner-cache/landed_torus_uniform_ice_admits_no_local_formation_order_closed_set_search_2026_09_23.txt`.
Analytic statements require the proofs above in addition to finite checks.
