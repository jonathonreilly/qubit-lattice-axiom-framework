---
claim_id: uniform_ice_by_formation_two_adjacent_cubes_admit_no_local_order_even_with_both_cube_sites_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "A locally determined record can be moved earlier without changing any conditional sigma algebra, so deterministic closure preserves existence of a complete fixed order. Five small cases compare the closed-set algorithm with plain search; a sixth cube-with-coordinator case is a known successful-order control.  Two adjacent cubes have 45 sites,20 grid links,614912 positive-weight patterns and total weight3985518592. With full records the complete closed search visits46 sets and reaches at most23 sites; one attaining set is one cube record,6 plaquettes,12 links and4 outer vertices. Empty vertex, empty plaquette, and both-empty variants respectively visit34,35,23 sets and reach31,16,24 sites, with no complete order. The other cube's conditional depends on more than the shared plaquette; a shared-vertex weight matrix [[1,2],[2,1]] has rank two. Orders are fixed deterministic orders. Each conditional draw uses fresh randomness and depends only on the records of the actual formed neighbours (with the declared hole semantics). The sufficiency criterion permits site/stage-specific kernels; it does not establish a single position-independent covariant law. Negative results in this broader class still exclude any more restrictive fixed-order law. Adaptive orders, hidden shared state, and mixtures whose component finished laws differ from the target are not excluded. Private links are marginalized into the stated grid-record weights; arbitrary hidden private-link formation schemes are not searched. The recorded attaining set does not classify all maximal sets."
upstream_dependencies:
  - minimal_axioms
  - uniform_ice_by_formation_two_planar_squares_admit_no_local_order_and_one_cube_needs_its_cube_site_bounded_theorem_note_2026-09-22
runner: scripts/uniform_ice_two_adjacent_cubes_no_local_formation_order_closed_set_search_2026_09_23.py
---

# Closed-set formation search on two adjacent cubes

**Date:** 2026-09-23
**Type:** bounded_theorem

## Result and scope

A locally determined record can be moved earlier without changing any conditional sigma algebra, so deterministic closure preserves existence of a complete fixed order. Five small cases compare the closed-set algorithm with plain search; a sixth cube-with-coordinator case is a known successful-order control.

Two adjacent cubes have 45 sites,20 grid links,614912 positive-weight patterns and total weight3985518592. With full records the complete closed search visits46 sets and reaches at most23 sites; one attaining set is one cube record,6 plaquettes,12 links and4 outer vertices. Empty vertex, empty plaquette, and both-empty variants respectively visit34,35,23 sets and reach31,16,24 sites, with no complete order. The other cube's conditional depends on more than the shared plaquette; a shared-vertex weight matrix [[1,2],[2,1]] has rank two.

## Boundaries and non-claims

Orders are fixed deterministic orders. Each conditional draw uses fresh randomness and depends only on the records of the actual formed neighbours (with the declared hole semantics). The sufficiency criterion permits site/stage-specific kernels; it does not establish a single position-independent covariant law. Negative results in this broader class still exclude any more restrictive fixed-order law. Adaptive orders, hidden shared state, and mixtures whose component finished laws differ from the target are not excluded. Private links are marginalized into the stated grid-record weights; arbitrary hidden private-link formation schemes are not searched. The recorded attaining set does not classify all maximal sets.

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
- **The criterion of open PR 8715.** With local records, an exact
  formation exists if and only if some order has each site's conditional,
  given the formed set, depend only on its formed neighbours.
- **Windows** in doubled coordinates. Vertices have even coordinates,
  links one odd coordinate, plaquettes two and cube sites three. The
  windows are one square, the 2 x 1 rectangle, one cube, and two cubes
  sharing a face. Nearest neighbours are sites at distance 1. Each
  vertex's other links are private to it: 3 at each outer vertex of the
  two cubes and 2 at each vertex of the shared face.
- **The uniform ice measure.** It weighs a grid pattern by
  prod_v C(private links, 3 - grid sum).
- **Record schemes.** Links record occupations. Vertices, plaquettes and
  cube sites record the pattern of their own grid links, or nothing. The
  tested combinations are listed in Theorem 2.


## Theorem 1 — The closure lemma

Let an order reproduce the law, and let F be a formed set in it. Let y be
unformed at F, with y's record a function of the records of its formed
neighbours F ∩ N(y). Move y to right after F. Then:

1. **y itself.** Its conditional given F is a point mass fixed by
   F ∩ N(y), so it depends only on its formed neighbours.
2. **Each site z between F and y's old place.** Call z's old formed set
   F_z. Since y is a function of F, conditioning on F_z ∪ {y} is
   conditioning on F_z. The conditional given F_z depends only on
   F_z ∩ N(z), because the old order was admissible. If y is a neighbour
   of z, conditioning on (F_z ∩ N(z)) ∪ {y} lies between conditioning on
   F_z ∩ N(z) and on F_z. By the tower property it gives the same law.
3. **Later sites** see the same formed sets as before.

Repeating the move, an order exists if and only if one exists that adds
every such site as soon as it is one. After each other step, that order's
formed sets are closed under the move. So a depth-first search over
closed sets decides existence.


## Theorem 2 — Two adjacent cubes

On two cubes sharing a face, with both cube sites, the closed-set search
finds no complete order. The largest formed sets, and the number of
closed sets visited, are:

| records | closed sets | largest formed set |
|---|---|---|
| full local records | 46 | 23 of 45: one cube site, its 6 plaquettes, 12 links and 4 outer vertices |
| vertex records carry nothing | 34 | 31 |
| plaquette records carry nothing | 35 | 16 |
| vertex and plaquette records carry nothing | 23 | 24 |

Sites whose records carry nothing are functions of anything, so the
closure forms them at once; they count toward the largest sets.

Under full local records, one recorded maximum-size set has the stated cube shape. There,
the other cube site's conditional given that cube and the shared plaquette
differs from its conditional given the shared plaquette alone. This is
because the four shared vertices' weights couple the two cubes' edges
perpendicular to the shared face.


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

Original context and author review history remain recoverable from the
originating PR. Historical mutation claims are not current review evidence.
The landing review preserves conditional proofs and narrows unsupported
extensions; no new axiom, primitive or audit grade is adopted.

## Verification

```bash
python3 scripts/uniform_ice_two_adjacent_cubes_no_local_formation_order_closed_set_search_2026_09_23.py
```

The runner exits nonzero on failure. Its fresh captured cache is
`logs/runner-cache/uniform_ice_two_adjacent_cubes_no_local_formation_order_closed_set_search_2026_09_23.txt`.
Analytic statements require the proofs above in addition to finite checks.
