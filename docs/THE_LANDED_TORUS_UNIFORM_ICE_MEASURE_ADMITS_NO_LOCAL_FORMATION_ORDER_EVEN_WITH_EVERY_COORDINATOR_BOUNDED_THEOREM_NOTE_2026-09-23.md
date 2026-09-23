---
claim_id: the_landed_torus_uniform_ice_measure_admits_no_local_formation_order_even_with_every_coordinator_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "Formation reading with the text's hole semantics and local records, on the 2 x 2 x 2 torus of the landed spin-half cubic-ice note (8 vertices, 24 links, 24 plaquette sites, 8 cube sites in doubled coordinates mod 4; no boundary, no private links). The uniform ice measure on its 9600 ice states admits no nearest-neighbour formation order with no unrecorded site, even with every plaquette and cube coordinator present: the closed-set search (open PRs 8715, 8719) visits 65 closed sets, and the largest formed set is one cube site with its 6 plaquettes and 12 edges, with no vertex. With vertex records carrying nothing, without coordinators, and with links alone, no order exists either. A control law (twelve independent fair links, twelve fixed) is formed in order. No rule, record scheme or order law is adopted."

upstream_dependencies:
  - minimal_axioms
  - realized_state_primitive
  - spin_half_cubic_ice_exact_rk_coulomb_correlations_and_finite_qubit_photon_phase_bridge_bounded_theorem_note_2026-09-03
runner: scripts/landed_torus_uniform_ice_admits_no_local_formation_order_closed_set_search_2026_09_23.py
---

# The landed torus uniform ice measure admits no local formation order, even with every coordinator

**Date:** 2026-09-23
**Type:** bounded_theorem
**Campaign:** next-steps campaign after the TOE derivation campaign by
underdetermination witnesses. Open PRs 8715 and 8719 showed that exact
local formation of the uniform ice measure stops at one top cell on open
windows. Each vertex's links outside those windows were private to it.
This block removes the window and its boundary. It asks the question of
the landed spin-half cubic-ice note's own object: the uniform ice measure
on the 2 x 2 x 2 torus, the equal-time law behind the landed Coulomb
correlations.

## Result up front

1. **No order, with every coordinator.** On the torus there are 8
   vertices, 24 links, 24 plaquette sites and 8 cube sites. Take the
   uniform ice measure on its 9600 states. No nearest-neighbour formation
   order reproduces it with no unrecorded site, even with every plaquette
   and cube site present. The closed-set search visits 65 closed sets.

2. **Where it stops.** The largest formed set is one cube site, its 6
   plaquettes and its 12 edges: 19 sites. No vertex joins it, because
   every vertex's six-link record reaches outside any one cube.

3. **Robust to the records.** There is no order in any of these cases
   either:
   - vertex records carrying nothing;
   - no plaquette or cube coordinators;
   - links alone.

   A control law, twelve independent fair links with the other twelve
   fixed, is formed in order.

4. **What this means for the photon lane.** The landed Coulomb law is not
   a local formation law on its own torus. The negative results of open
   PRs 8715 and 8719 therefore do not depend on open windows or private
   links. The equal-time law comes from the static reading with a
   positive rule (open PR 8698). By formation it needs one of:
   - plan records (open PR 8686);
   - layer units formed in order (open PR 8720);
   - conditioning, which is not in the text.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "exact local formation of the uniform ice measure beyond one top cell was shown on open windows with private links (open PRs 8715, 8719)"
source_of_blocker_text: open_prs_8715_8719
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "record on the formed photon route that the landed torus measure itself admits no local formation order"
conditional_surface_status: "formation reading; text hole semantics; the landed 2 x 2 x 2 torus; local record schemes (patterns or nothing)"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "a complete closed-set search with exact integer conditionals, the criterion and closure lemma of open PRs 8715 and 8719, and a positive control"
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

## Prior art and what is new

- The landed spin-half cubic-ice note: the torus measure and its Coulomb
  correlations.
- Open PR 8715: the criterion and the plain search.
- Open PR 8719: the closure lemma and the closed-set search.
- New here: no local formation order for the landed torus measure, with
  every coordinator, and its largest formed set.

## Theorem — No order on the torus

By the criterion of open PR 8715 and the closure lemma of open PR 8719, a
depth-first search over closed formed sets decides whether an exact
order exists. On the torus it visits 65 closed sets and finds no
complete one. The largest set is one cube's cube site, plaquettes and
edges. Every conditional is compared by integer cross-multiplication
over the 9600 states.

## No-Go Discipline Gate

The negative content is scoped: the landed torus, local records.

- **N1 alternative routes.** The following are outside the search:
  - larger tori;
  - plan records;
  - layer units;
  - conditioning.
- **N2 wall independence.** An exact search with integer conditionals.
- **N3 hidden walls.** Records are local by declaration.
- **N4 residual matching.** The formed photon route's residual is plan
  records, layer units or conditioning.
- **N5 rhetoric audit.** "No order" refers to the torus and the declared
  schemes.
- **N6 partial-closure paths.** Larger tori; layer units on periodic
  slabs.
- **N7 steelman.** For formation: one cube is coordinated on the torus
  too. Against it: no complete order exists, whatever the records. Both
  are recorded.
- **N8 cross-cycle echo.** Open PRs 8686, 8698, 8715, 8719 and 8720 and
  the landed note are cited.

## Falsifiers

Any of the following falsifies the theorem:
- a complete order on the torus under a declared scheme;
- a count other than 9600;
- a control law found without an order.

## Boundaries and non-claims

- The 2 x 2 x 2 torus only.
- No rule, record scheme or order law is adopted.
- Nothing here grades, unlocks or audits any other claim.

## Imports

The landed note and open PRs are cited. No audit grade, no new axiom, no
new primitive, no new comparator and no new framing is imported.

## Review record

- **Seat:** one Opus 5.5 seat; no subagents; runner and note by the same
  seat.
- **Independence sources:**
  - the 9600 states are enumerated directly and match the landed note;
  - the control law confirms that the search finds orders when they
    exist;
  - the search itself is the closure-lemma search of open PR 8719, which
    was checked there against the plain search on six windows.
- **Mutation census** (caught means at least one FAIL line or a nonzero
  exit; the runner exits nonzero on any FAIL):

| mutant | change | outcome |
|---|---|---|
| two of six links per vertex | ice count 3 to 2 | caught (1 FAIL, then a nonzero exit) |
| cube sites record nothing | edge selection emptied | caught (1 FAIL) |
| neighbours out to distance 2 | distance 1 to at most 2 | caught (2 FAIL) |
| admissibility always true | early return | caught (2 FAIL) |
| control is the ice measure | control law replaced | caught (1 FAIL) |
| comparison reversed | all equal to any different | caught (2 FAIL) |
| vertex stars miss a link | six links to five | caught (2 FAIL) |

7 of 7 caught.

- **Vacuity guard:** closed-set counts and largest formed sets are
  printed for every search; a binding budget fails its check.
- **Budget:** 4 checks, stdout 999 characters (ceiling 6000), about
  8 s (ceiling 900 s), exact integers.

## Verification

```bash
python3 scripts/landed_torus_uniform_ice_admits_no_local_formation_order_closed_set_search_2026_09_23.py
```

Expected summary line: `TOTAL: PASS=4 FAIL=0`; the runner exits nonzero
if any check fails. Cached output:
`logs/runner-cache/landed_torus_uniform_ice_admits_no_local_formation_order_closed_set_search_2026_09_23.txt`.
