---
claim_id: uniform_ice_by_joint_cell_units_rows_yes_the_two_by_two_block_no_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "Formation reading with joint formation units (open PR 8643) and the text's hole semantics. Cell units: each unit forms, jointly, every not-yet-formed site of one closed square (its plaquette site, four links and four vertices, vertices recording their full grid patterns). A cell-unit formation reproduces the uniform ice measure exactly, with no unrecorded site, if and only if some unit order has each unit's joint conditional, given everything formed before it, depend only on the formed sites adjacent to the unit's new sites. On planar windows, with exact conditional laws over every unit order: one square and two squares, every order is exact; a row of three squares, exactly the four orders that do not form both ends before the middle; the 2 x 2 block (weight 125836800), no order, every one failing at the second unit. Units that are whole rows of the 2 x 3 window form a chain and are exact in exactly the four orders that do not form both end rows first (with two units any split is exact, since the second unit is the whole remainder); on the lattice such units are unbounded and pick a direction, as a sweep's layers do. In three dimensions, cube units on two cubes sharing a face are exact in both orders (enumeration over 614912 grid patterns), and on the 2 x 2 x 1 slab of cubes (75 sites, 33 grid links) every ordered pair of first units fails at the second unit: two formed patterns agreeing on every site adjacent to the second unit give different exact laws for it. So all 24 slab orders fail. Row units wrapped into a loop (a planar cylinder of three rows, 21888 grid patterns) have no exact order, so units spanning an axis must be formed as a chain along an open axis. No rule, unit or order law is adopted."

upstream_dependencies:
  - minimal_axioms
  - realized_state_primitive
  - spin_half_cubic_ice_exact_rk_coulomb_correlations_and_finite_qubit_photon_phase_bridge_bounded_theorem_note_2026-09-03
  - the_superlattice_role_pattern_is_a_next_nearest_neighbour_support_rule_over_roles_and_roles_are_not_record_values_bounded_theorem_note_2026-09-04
runner: scripts/uniform_ice_joint_cell_units_rows_but_not_the_two_by_two_block_2026_09_23.py
---

# Uniform ice by joint cell units: rows yes, the 2 x 2 block no, in the plane and in three dimensions

**Date:** 2026-09-23
**Type:** bounded_theorem
**Campaign:** next-steps campaign after the TOE derivation campaign by
underdetermination witnesses. With single sites, exact local formation of
the uniform ice measure stops at one top cell (open PRs 8715 and 8719). The candidate assembly (open PR 8648) keeps one gravity route
through joint formation units, {soldering, joint units, roles}, and lists
joint-unit formation of the uniform ice measure as an open edge. This
block tests the natural finite units: closed cells formed jointly.

## Result up front

1. **The unit criterion.** A cell-unit formation is exact, with no
   unrecorded site, if and only if some unit order meets this condition:
   each unit's joint conditional, given everything formed before it,
   depends only on the formed sites adjacent to the unit's new sites. The
   proof is the chain rule over units, as for single sites (open
   PR 8715).

2. **Rows work.** One square and two squares are exact in every order. A
   row of three is exact in exactly four of its six orders: those that do
   not form both ends before the middle. When the unformed cells stay on
   one side of each new unit, the formed vertex records screen it.

3. **The 2 x 2 block does not.** No order of the four cell units is exact.
   Every order fails at the second unit: whatever the first two cells,
   the two unformed cells close a loop around the centre. That loop joins
   the new unit to formed vertex records it does not touch.

4. **Units that span the window form a chain, and chains work.** Take
   units that are whole rows of the 2 x 3 window. They are exact in
   exactly the four orders that do not form both end rows before the
   middle, as cells in a row are. With only two units any split is exact,
   because the second unit is the whole remainder. On the lattice such
   units are unbounded along an axis, and they pick a direction, as a
   sweep's layers do.

5. **The same in three dimensions.** Cube units on two cubes sharing a
   face are exact in both orders. On the 2 x 2 x 1 slab of four cubes,
   every ordered pair of first units fails at the second unit. Two formed
   patterns that agree on every site adjacent to the second unit give it
   different exact laws, so all 24 orders fail.

6. **Chains need an open axis.** Wrap three rows into a loop, a planar
   cylinder. Then no order of the row units is exact, although the open
   2 x 3 window has four. Units that span an axis must therefore be
   formed as a chain along an open axis, as a sweep's layers are.

7. **What this means for the photon lane.** In the plane and in three
   dimensions, finite cell units extend the one-cell coordinator along a
   row but not around a block. Exact joint formation of the uniform ice
   measure then needs one of:
   - units unbounded along an axis;
   - plan letters (open PR 8686);
   - conditioning, which is not in the text.

   The assembly's {soldering, joint units, roles} set now rests on units
   unbounded along an axis, which pick a direction as a sweep's layers do.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "exact formation of the uniform ice measure by joint units (open edge of open PR 8648)"
source_of_blocker_text: open_pr_8648
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "record on the joint-unit branch of the formed photon route: finite cell units reach rows, not blocks, in the plane and in three dimensions; units spanning the window pick a direction"
conditional_surface_status: "formation reading with joint units; text hole semantics; declared planar and cubic windows; cell units with full local records"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "a necessary and sufficient unit criterion with a short proof, decided over every unit order with exact conditional laws"
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

## Prior art and what is new

- Open PR 8643: joint covariant-set formation units, and their exact
  comparison with single-site formation.
- Open PR 8715: the single-site criterion and the two-square negative.
- Open PR 8719: two adjacent cubes, and the closure lemma.
- Open PR 8686: the plaquette coordinator and plans.
- New here:
  - the unit criterion;
  - rows exact;
  - the 2 x 2 block without any exact cell-unit order;
  - row units forming a chain, exact exactly as cells in a row are;
  - two cubes exact, and the 2 x 2 x 1 slab failing at the second unit
    for every ordered pair.
- Standard: the chain rule.

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

## Theorem 4 — Chains need an open axis

On a planar cylinder, the runner checks all 6 orders of the three row
units with exact conditional laws: 9 vertices, 15 grid links, 6
plaquettes, and three rows wrapped in y. None is exact. Whichever row
forms second, the unformed third row joins it to the first row's far
side around the loop.

## No-Go Discipline Gate

The negative content is scoped: the declared planar and cubic windows,
cell units, full local records.

- **N1 alternative routes.** The following are outside the search:
  - other finite units;
  - larger cube windows;
  - records beyond local content;
  - conditioning.
- **N2 wall independence.** Exact conditional laws over every unit
  order; no dynamics.
- **N3 hidden walls.** Units are declared: cell units and row units.
- **N4 residual matching.** The joint-unit branch's residual is units
  unbounded along an axis, plan letters or conditioning.
- **N5 rhetoric audit.** "No order" refers to the 2 x 2 block under cell
  units.
- **N6 partial-closure paths.** Other finite unit shapes; larger
  windows.
- **N7 steelman.** For joint units: they extend the coordinator along
  rows, and row units forming a chain work. Against finite units: the 2 x 2
  block and the 2 x 2 x 1 slab fail in every order. Both are recorded.
- **N8 cross-cycle echo.** Open PRs 8643, 8648, 8686, 8715 and 8719 are
  cited.
  The one-square and two-square results agree with open PR 8715's
  coordinator.

## Falsifiers

- An exact cell-unit order on the 2 x 2 block falsifies Theorem 2.
- A slab pair whose two stated patterns give equal laws falsifies
  Theorem 3.
- A failing order on one or two squares does too.
- So does a row of three whose exact orders differ from those stated.

## Boundaries and non-claims

- No rule, unit or order law is adopted.
- The windows are declared; larger cube windows are not searched.
- Nothing here grades, unlocks or audits any other claim.

## Imports

The landed notes and open PRs are cited, and the chain rule is standard.
No audit grade, no new axiom, no new primitive, no new comparator and no
new framing is imported.

## Review record

- **Seat:** one Opus 5.5 seat; no subagents; runner and note by the same
  seat.
- **Independence sources:**
  - the one-square and two-square weights match open PRs 8686 and 8715;
  - the row-unit verdicts on the 2 x 3 window repeat the cell verdicts
    on a row of three, as the chain structure predicts;
  - the two-cube weight matches open PR 8719;
  - each test compares two independently grouped conditional laws.
- **Mutation census** (caught means at least one FAIL line or a nonzero
  exit; the runner exits nonzero on any FAIL):

| mutant | change | outcome |
|---|---|---|
| conditional test always true | early return | caught (4 FAIL) |
| every formed site counted as adjacent | adjacency filter removed | caught (2 FAIL) |
| cells leave out their vertices | vertices dropped from units | caught (2 FAIL) |
| private links counted as 5 | 6 minus grid degree to 5 minus grid degree | caught (1 FAIL) |
| wrong failing set for the row | middle last to middle first | caught (1 FAIL) |
| neighbours out to distance 2 | distance 1 to at most 2 | caught (2 FAIL) |
| vertices record nothing | vertex pattern to empty record | caught (2 FAIL) |
| row check with the wrong failing set | middle last to middle first | caught (1 FAIL) |
| rows assigned by column | row index to column index | caught (1 FAIL) |
| slab flips may touch adjacent records | adjacency guard removed | caught (1 FAIL) |
| slab weights ignore private counts | binomial factor to 1 | caught (1 FAIL) |
| two-cube private links counted as 5 | 6 minus degree to 5 minus degree | caught (1 FAIL) |
| two-cube adjacency is every formed site | adjacency filter removed | caught (1 FAIL) |
| loop unwrapped into a chain | period 6 to 600 | caught (1 FAIL) |
| loop check with every order counted exact | and to or | caught (1 FAIL) |
| slab cells leave out their cube sites | cube sites dropped from units | missed; diagnosed equivalent: a cube site's record is a function of its own unit's link records, and it neighbours only its own plaquettes, so units with or without it carry the same information and the same adjacency |

Fifteen of fifteen defect mutants are caught; the cube-site row is the
diagnosed equivalent. A first version checked row units on the 2 x 2
block, where any split into two units is exact because the second unit
is the whole remainder; that check was vacuous and was replaced by the
2 x 3 window.

- **Vacuity guard:** every window prints its sites, patterns and the
  failing step of each failing order.
- **Budget:** 7 checks, stdout 1899 characters (ceiling 6000), about
  30 s (ceiling 900 s), exact Fractions and integers.

## Verification

```bash
python3 scripts/uniform_ice_joint_cell_units_rows_but_not_the_two_by_two_block_2026_09_23.py
```

Expected summary line: `TOTAL: PASS=7 FAIL=0`; the runner exits nonzero
if any check fails. Cached output:
`logs/runner-cache/uniform_ice_joint_cell_units_rows_but_not_the_two_by_two_block_2026_09_23.txt`.
