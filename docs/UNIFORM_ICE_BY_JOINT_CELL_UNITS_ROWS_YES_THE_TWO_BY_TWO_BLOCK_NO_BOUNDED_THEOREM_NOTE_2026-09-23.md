---
claim_id: uniform_ice_by_joint_cell_units_rows_yes_the_two_by_two_block_no_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "For fixed joint-unit orders the chain-rule criterion uses the entire new unit's conditional given all formed records and its actual adjacent formed records. Square-cell units admit 1/1 orders on one square,2/2 on two,4/6 on a three-square row, and0/24 on the2x2 block, each failing at the second unit. Whole-row units on2x3 admit4/6 orders, excluding both-end-rows-first.  Two cube units sharing a face admit both orders. On the2x2x1 four-cube slab, each of12 ordered first pairs has an exact witness: two positive-weight formed patterns agree on every adjacent formed record but yield different joint laws for the next unit. All24 orders therefore fail at their second unit. Independent scalar and vectorized enumerations agree on these witnesses. On the declared three-row cylinder (21888 grid patterns), all6 row orders fail. Orders are fixed deterministic orders. Each conditional draw uses fresh randomness and depends only on the records of the actual formed neighbours (with the declared hole semantics). The sufficiency criterion permits site/stage-specific kernels; it does not establish a single position-independent covariant law. Negative results in this broader class still exclude any more restrictive fixed-order law. Adaptive orders, hidden shared state, and mixtures whose component finished laws differ from the target are not excluded. Private links are marginalized into the stated grid-record weights; arbitrary hidden private-link formation schemes are not searched. The one cylinder counterexample does not prove that every exact layer chain needs an open axis."
upstream_dependencies:
  - minimal_axioms
  - uniform_ice_by_formation_two_planar_squares_admit_no_local_order_and_one_cube_needs_its_cube_site_bounded_theorem_note_2026-09-22
runner: scripts/uniform_ice_joint_cell_units_rows_but_not_the_two_by_two_block_2026_09_23.py
---

# Joint-cell formation on the declared rows, blocks and cylinder

**Date:** 2026-09-23
**Type:** bounded_theorem

## Result and scope

For fixed joint-unit orders the chain-rule criterion uses the entire new unit's conditional given all formed records and its actual adjacent formed records. Square-cell units admit 1/1 orders on one square,2/2 on two,4/6 on a three-square row, and0/24 on the2x2 block, each failing at the second unit. Whole-row units on2x3 admit4/6 orders, excluding both-end-rows-first.

Two cube units sharing a face admit both orders. On the2x2x1 four-cube slab, each of12 ordered first pairs has an exact witness: two positive-weight formed patterns agree on every adjacent formed record but yield different joint laws for the next unit. All24 orders therefore fail at their second unit. Independent scalar and vectorized enumerations agree on these witnesses. On the declared three-row cylinder (21888 grid patterns), all6 row orders fail.

## Boundaries and non-claims

Orders are fixed deterministic orders. Each conditional draw uses fresh randomness and depends only on the records of the actual formed neighbours (with the declared hole semantics). The sufficiency criterion permits site/stage-specific kernels; it does not establish a single position-independent covariant law. Negative results in this broader class still exclude any more restrictive fixed-order law. Adaptive orders, hidden shared state, and mixtures whose component finished laws differ from the target are not excluded. Private links are marginalized into the stated grid-record weights; arbitrary hidden private-link formation schemes are not searched. The one cylinder counterexample does not prove that every exact layer chain needs an open axis.

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

- **The formation reading with joint units.** A unit forms its new sites
  at once, with a joint law that depends on the formed sites adjacent to
  them. Hole semantics apply.
- **Windows.** nx x ny coarse squares in a plane, two cubes sharing a
  face, and the 2 x 2 x 1 slab of four cubes, in doubled coordinates, with
  their vertices, grid links, plaquette and cube sites. Each vertex's
  other links are private to it.
- **The uniform ice measure.** It weighs a grid pattern by
  prod_v C(private links, 3 - grid sum).
- **Records.** Links record their occupation. Vertices and plaquettes
  record the pattern of their own grid links.
- **Cell units.** A cell unit forms every not-yet-formed site of one
  closed square or cube. Row units form every not-yet-formed site of a
  whole row of the 2 x 3 window.


## Theorem 1 — The unit criterion

Suppose a unit formation is exact. Then each unit's joint law, given the
sites formed before it, is the declared law's conditional given that
formed set. The rule makes it a function of the adjacent formed sites.
Conversely, suppose an order has every unit's declared conditional depend
only on its adjacent formed sites. Let each unit's law be that
conditional. The chain rule over units then reproduces the declared law.


## Theorem 2 — The windows

All unit orders are checked with exact conditional laws:

| window | weight | exact orders |
|---|---|---|
| one square | 10016 | 1 of 1 |
| 2 x 1 | 501632 | 2 of 2 |
| 3 x 1 | 25123328 | 4 of 6 (not both ends first) |
| 2 x 2 | 125836800 | 0 of 24 (each fails at the second unit) |

Row units on the 2 x 3 window (100352 grid patterns) are exact in 4 of 6
orders: those that do not form both end rows first.


## Theorem 3 — Three dimensions

On two cubes sharing a face, cube units are exact in both orders. The
check enumerates all 614912 grid patterns, with integer cross-
multiplication.

The 2 x 2 x 1 slab has 33 grid links, too many to enumerate. For each of
the 12 ordered pairs of first units, the runner finds two formed patterns
that differ in one formed edge outside every site adjacent to the second
unit. They give different exact laws of the second unit's new records,
summing the remaining edges. So the second unit's law is not a function
of the sites it touches, and every one of the 24 orders fails at the
second unit.


## Theorem 4 — The declared three-row cylinder fails

On a planar cylinder, the runner checks all 6 orders of the three row
units with exact conditional laws: 9 vertices, 15 grid links, 6
plaquettes, and three rows wrapped in y. None is exact. Whichever row
forms second, the unformed third row joins it to the first row's far
side around the loop.


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
python3 scripts/uniform_ice_joint_cell_units_rows_but_not_the_two_by_two_block_2026_09_23.py
```

The runner exits nonzero on failure. Its fresh captured cache is
`logs/runner-cache/uniform_ice_joint_cell_units_rows_but_not_the_two_by_two_block_2026_09_23.txt`.
Analytic statements require the proofs above in addition to finite checks.
