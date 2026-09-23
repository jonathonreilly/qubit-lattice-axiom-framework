---
claim_id: uniform_ice_by_formation_two_planar_squares_admit_no_local_order_and_one_cube_needs_its_cube_site_bounded_theorem_note_2026-09-22
claim_type: bounded_theorem
claim_scope: "Formation reading with the text's hole semantics. With local records, a nearest-neighbour formation law reproduces a record law exactly and without unrecorded sites if and only if some order adds sites one at a time so that each site's conditional, given all sites formed so far, depends only on its formed neighbours; a search over formed-site subsets decides this exactly. For the uniform ice measure (weights prod_v C(private links, 3 - grid sum); 10016 on one square, 501632 on the 2 x 1 rectangle): one square is impossible without the plaquette site and possible with it (as in open PR 8686); two squares are impossible without plaquette sites and impossible with both plaquette coordinators, for five record schemes (vertex records a grid pattern, a count or nothing; plaquette records a four-link pattern, a count or nothing); at most 7 of 15 sites form exactly with full local records, 11 with plaquette records alone. In three dimensions one cube (6316544 weight) admits no order with its six plaquette sites alone (at most 5 of 26 sites), and the cube-first order reproduces it exactly with its cube site: each top cell needs its own coordinator. Two cubes are not searched. No rule, record scheme or order law is adopted."

upstream_dependencies:
  - minimal_axioms
  - realized_state_primitive
  - spin_half_cubic_ice_exact_rk_coulomb_correlations_and_finite_qubit_photon_phase_bridge_bounded_theorem_note_2026-09-03
  - the_superlattice_role_pattern_is_a_next_nearest_neighbour_support_rule_over_roles_and_roles_are_not_record_values_bounded_theorem_note_2026-09-04
runner: scripts/uniform_ice_two_squares_no_local_formation_order_complete_order_search_2026_09_22.py
---

# Uniform ice by formation: two planar squares admit no local order, and one cube needs its cube site

**Date:** 2026-09-22
**Type:** bounded_theorem
**Campaign:** next-steps campaign after the TOE derivation campaign by
underdetermination witnesses. On one square, the plaquette site
coordinates the square's links and reproduces the uniform ice measure
exactly (open PR 8686). On two squares, one second coordinator seeing
only the shared link fails, and the assembly (open PR 8648) records
coordination beyond one square as an open edge. This block answers that
edge on the 2 x 1 window and on one cube by searching every formation
order.

## Result up front

1. **An exact criterion.** Records are local: links record occupations,
   vertices and plaquettes record functions of their own links. A
   nearest-neighbour formation law reproduces a record law exactly, with
   no unrecorded site, if and only if some order meets the following
   condition: each site's conditional, given everything formed before it,
   depends only on its formed neighbours. The rule is then that
   conditional. So a search over the lattice of formed-site subsets
   decides the question completely.

2. **One square: as open PR 8686 found.** Without the plaquette site no
   order works; at most 3 of the 8 sites form exactly. With it, an order
   works: the coordinator.

3. **Two squares: no order works.** On the 2 x 1 rectangle (501632 ice
   configurations), no order works without plaquette sites; at most 4 of
   13 sites form exactly. None works with both plaquette coordinators
   either. That holds for all five record schemes tested:
   - vertex records carry a grid pattern, a count, or nothing;
   - plaquette records carry a four-link pattern, a count, or nothing.

   With full local records at most 7 of 15 sites form exactly, and with
   plaquette records alone at most 11.

4. **The same pattern in three dimensions.** One cube with its six
   plaquette sites but no cube site admits no order; at most 5 of 26
   sites form exactly. With the cube site, the cube-first order
   reproduces the law exactly: cube, then plaquettes, links and vertices.
   So each top cell needs its own coordinator. In the plane, two
   squares have no cell above them, and no order works. Two cubes are not
   searched.

5. **What this means for the photon lane.** In the plane, for these
   record schemes, the uniform ice measure is not a local formation law
   beyond one square: the plaquette coordinator does not extend to two
   squares. In three dimensions every cube has its own cube site, and one
   cube is formed exactly; whether two adjacent cubes are is not
   searched. Formation otherwise gives directed transport (open PRs 8687,
   8701), and the landed Coulomb law comes from the static reading with a
   positive rule (open PR 8698). Where local coordination fails, reaching
   the uniform measure by formation needs:
   - records with non-local content (open PR 8686), or
   - conditioning, which is not in the text.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "coordinated formation of the uniform ice measure beyond one square (open edge of open PR 8648; open PR 8686)"
source_of_blocker_text: open_prs_8648_8686
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "record on the formed photon route that two planar squares admit no local order and one cube needs its cube site; search two adjacent cubes"
conditional_surface_status: "formation reading; text hole semantics; declared windows (one square, the 2 x 1 rectangle, one cube); five declared planar record schemes and full local records on the cube"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "a necessary and sufficient criterion with a short proof, decided by a complete search over formed-site subsets with exact conditional laws"
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
- **The declared record schemes.**

## Prior art and what is new

- Open PR 8686: the loop obstruction and the plaquette coordinator on one
  square, and a failing second-coordinator order on two squares.
- New here: an exact criterion and a complete search over orders.
  Two squares admit no exact local formation order, with or without
  plaquette coordinators, under five record schemes. One cube admits none
  with its plaquette sites alone, and one with its cube site.
- Standard: sequential factorisation of laws (chain rule).

## Theorem 1 — The criterion

Suppose a formation is exact. Then each site's law, given the sites
formed before it, is the rule's output on its formed neighbours. So it is
the declared law's conditional given the formed set, and it depends only
on the formed neighbours.

Conversely, take an order in which every site's declared conditional,
given the formed set, depends only on its formed neighbours. Let the rule
be that conditional. The chain rule then reproduces the declared law,
with no unrecorded site.

Private links are leaves of the neighbour graph and depend only on their
vertex, so leaving them out changes nothing.

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

## No-Go Discipline Gate

The negative content is scoped. On the planar 2 x 1 window, under the
five declared schemes, no exact local formation of the uniform ice
measure exists.

- **N1 alternative routes.** Three things lie outside the search:
  - two cubes, and cube sites joining the two planar plaquettes through
    a vertical plaquette;
  - other functions of local content;
  - larger windows.
- **N2 wall independence.** Exact conditional laws and a finite search;
  no dynamics.
- **N3 hidden walls.** Records are local by declaration. Non-local plans
  work (open PR 8686).
- **N4 residual matching.** The formed photon route's residual is
  non-local records, conditioning, or coordination of two adjacent cubes
  by their cube sites.
- **N5 rhetoric audit.** "No order works" refers to the declared windows
  and schemes.
- **N6 partial-closure paths.** Two cubes; larger windows; other record
  functions.
- **N7 steelman.** For formation: one square is coordinated exactly, and
  the static reading supplies the Coulomb law anyway. Against formation
  of the uniform measure: two squares fail in the plane, and one cube
  needs its own cube site. Both are recorded.
- **N8 cross-cycle echo.** Open PRs 8648, 8686, 8687, 8698 and 8701 are
  cited; the one-square results reproduce open PR 8686.

## Falsifiers

- An order on the 2 x 1 window, under a declared scheme, in which every
  site's conditional given the formed set depends only on its formed
  neighbours, falsifies Theorem 2.
- A one-square result that differs from open PR 8686 does too.
- A complete order on the one cube without its cube site, or a
  cube-first step whose conditional depends on a formed non-neighbour,
  falsifies Theorem 3.

## Boundaries and non-claims

No rule, record scheme or order law is adopted. The windows are one
square, the 2 x 1 rectangle and one cube; two cubes and larger windows
are not searched. Nothing here grades, unlocks or audits any other claim.

## Imports

The landed notes and open PRs are cited, and the chain rule is standard.
No audit grade, no new axiom, no new primitive, no new comparator and no
new framing is imported.

## Review record

- **Seat:** one Opus 5.5 seat; no subagents; runner and note by the same
  seat.
- **Independence sources:**
  - the window weights are compared with the transfer-matrix count and
    with open PR 8686;
  - the one-square searches reproduce open PR 8686 in both directions;
  - the one-cube weight 6316544 is recomputed as a generating-function
    coefficient on independently built unit-cube adjacency;
  - each admissibility test compares two independently grouped
    conditional laws.
- **Mutation census** (caught means at least one FAIL line or a nonzero
  exit; the runner exits nonzero on any FAIL):

| mutant | change | outcome |
|---|---|---|
| planar private links counted as 5 | 6 minus grid degree to 5 minus grid degree | caught (1 FAIL) |
| admissibility always true | early return | caught (4 FAIL) |
| all formed sites treated as neighbours | neighbour filter removed | caught (4 FAIL) |
| search stops after one layer | frontier emptied | caught (1 FAIL) |
| planar ice weights ignore private counts | binomial factor to 1 | caught (4 FAIL) |
| plaquettes see only two of their links | two directions | caught (1 FAIL) |
| cube site records half its edges | 12 edges to 6 | caught (1 FAIL) |
| cube site not a neighbour of its plaquettes | pair removed | caught (1 FAIL) |
| cube ice weights ignore private counts | binomial factor to 1 | caught (1 FAIL) |
| cube plaquettes record only a count | pattern to sum | caught (1 FAIL) |
| planar search cap below the real search | 5000 to 100 | caught (1 FAIL) |
| generating function drops the private factor | C(3, k) to C(2, k) | caught (1 FAIL) |

12 of 12 caught.

- **Vacuity guard:** admissible-set counts and largest reachable sizes
  are printed for every search; a binding search cap fails its check.
- **Budget:** 7 checks, stdout 1205 characters (ceiling 6000), about
  15 s (ceiling 900 s), exact Fractions.

## Verification

```bash
python3 scripts/uniform_ice_two_squares_no_local_formation_order_complete_order_search_2026_09_22.py
```

Expected summary line: `TOTAL: PASS=7 FAIL=0`; the runner exits nonzero
if any check fails. Cached output:
`logs/runner-cache/uniform_ice_two_squares_no_local_formation_order_complete_order_search_2026_09_22.txt`.
