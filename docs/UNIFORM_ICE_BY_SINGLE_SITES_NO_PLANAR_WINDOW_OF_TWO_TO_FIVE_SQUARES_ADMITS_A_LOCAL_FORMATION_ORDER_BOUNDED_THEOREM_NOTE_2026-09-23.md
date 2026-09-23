---
claim_id: uniform_ice_by_single_sites_no_planar_window_of_two_to_five_squares_admits_a_local_formation_order_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "Formation reading with the text's hole semantics and local records, single sites, the uniform ice measure on planar windows with private links. A window is the vertex set of a polyomino with every link between its vertices and a plaquette coordinator on every square whose four links are in the window. The free polyominoes of one to five squares (1, 1, 2, 5, 12) span 21 windows; the U pentomino spans the 3 x 2 rectangle. Every window's total weight equals its generating-function coefficient. With full local records the closed-set search of open PR 8719, checked against the plain search of open PR 8715 on five windows, finds an order on the lone square and on none of the 20 windows of two to five squares. Every search stops at one square's plaquette, its four links and its unshared vertices, for a square with the fewest shared vertices (7 sites, or 6 on the 2 x 2 and 3 x 2 windows); from there no site's conditional depends only on its formed neighbours, so no formed set holds all nine sites of any square. With vertices recording nothing, plaquettes recording nothing, or both, none of the 20 windows admits an order. Windows beyond five squares and three-dimensional windows beyond two cubes are not searched. No reading, rule, alphabet, unit or order law is adopted."

upstream_dependencies:
  - minimal_axioms
  - realized_state_primitive
  - spin_half_cubic_ice_exact_rk_coulomb_correlations_and_finite_qubit_photon_phase_bridge_bounded_theorem_note_2026-09-03
  - the_superlattice_role_pattern_is_a_next_nearest_neighbour_support_rule_over_roles_and_roles_are_not_record_values_bounded_theorem_note_2026-09-04
runner: scripts/uniform_ice_planar_windows_of_two_to_five_squares_admit_no_single_site_formation_order_2026_09_23.py
---

# Uniform ice by single sites: no planar window of two to five squares admits a local formation order

**Date:** 2026-09-23
**Type:** bounded_theorem
**Campaign:** next-steps campaign after the TOE derivation campaign by
underdetermination witnesses. The assembly (open PR 8648) lists as an
open edge exact formation of the uniform ice measure "by single sites on
windows beyond two top cells", marked as not searched. This block
searches every planar window of up to five squares.

## Result up front

1. **No planar window of two to five squares admits a single-site
   order.** Every free polyomino of two to five squares is searched with a
   plaquette coordinator on every square: 20 windows in all, since the U
   pentomino spans the 3 x 2 rectangle. Full local records give no order
   on any of them. The lone square has one (open PR 8715).

2. **Every search stops at one square, minus its shared vertices.** The
   largest formed set is always one square's plaquette, its four links
   and those of its corners that belong to no other square. The square
   chosen has the fewest shared corners, giving 7 sites, or 6 on the
   2 x 2 and 3 x 2 windows where every square shares three corners. From
   there no further site's conditional depends only on its formed
   neighbours. Every formed set lies in a closed one, so no formed set
   holds all nine sites of any square. This matches the two cubes of open
   PR 8719, where the search stops at one cube and its four unshared
   vertices.

3. **Why the shared corners stay out.** The mechanism is the one found
   for two cubes (open PR 8719). A corner shared with another square
   carries links of that square. Through that square's other corners,
   those links are tied to the formed square's links. So the corner's
   record depends on the formed square beyond its own formed links. The
   runner checks the consequence directly: from the stopping set, no
   outside site is admissible.

4. **Coarser records do not help.** With vertices recording nothing,
   plaquettes recording nothing, or both, none of the 20 windows admits
   an order.

5. **What this means for the single-site route.** Single-site formation
   of the uniform ice measure reproduces it on one square and on no planar
   window of two to five squares. The same holds on two cubes (open PR
   8719) and on the landed torus even with every coordinator (open PR
   8727). The single-site route needs plan letters (open PR 8686). The
   joint-unit route needs chains of units (open PR 8720).

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "exact formation of the uniform ice measure by single sites on windows beyond two top cells (assembly open edge, open PR 8648)"
source_of_blocker_text: open_pr_8648
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "record in the assembly: single sites fail on every planar window of two to five squares; the open edge narrows to larger planar windows and to three-dimensional windows beyond two cubes"
conditional_surface_status: "formation reading with local records; single sites; planar windows with private links"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "exact finite searches, checked against the plain search, over every window in a declared family"
```

## Premises and declared objects

- **Criterion.** With local records, a nearest-neighbour formation law
  reproduces a record law exactly, with no unrecorded sites, precisely
  when some order adds sites one at a time so that each site's
  conditional, given all sites formed so far, depends only on its formed
  neighbours (open PR 8715).
- **Search.** The closed-set search of open PR 8719, using its closure
  lemma. It is checked here against the plain search on five windows,
  including the L tromino.
- **Windows.** Doubled coordinates: vertices even, links with one odd
  coordinate, plaquettes with two. A window is the vertex set of a
  polyomino, with every link between its vertices. It has a plaquette
  coordinator on every square whose four links are in the window. Each
  vertex's other links are private to it.
- **Measure.** The uniform ice measure: 3 of each vertex's 6 links are
  occupied. On grid links it weighs a pattern by
  prod_v C(private links, 3 - grid sum).
- **Records.** Links record occupation. Vertices and plaquettes record
  the pattern of their own grid links, or nothing.

## Prior art and what is new

- Open PR 8715: the criterion; two planar squares admit no order.
- Open PR 8719: the closure lemma and the closed-set search; two cubes
  admit no order.
- Open PR 8727: the landed torus admits no order.
- Open PR 8720: joint cell units.
- New here:
  - every planar window of two to five squares;
  - the stopping set: one square minus its shared corners;
  - the coarser schemes on all of them.

## Theorem 1 — No order on the windows

Count the free polyominoes of one to five squares by canonical form under
the eight symmetries of the square. The counts are 1, 1, 2, 5 and 12.
They span 21 windows, since the U pentomino's vertex set is the 3 x 2
rectangle. Every window's total weight is recomputed as a
generating-function coefficient, with four totals pinned: one square
10016, 2 x 1 501632, 3 x 1 25123328, 2 x 2 125836800.

With full local records and every coordinator:
- the lone square has an order;
- each of the 20 windows of two to five squares has none.

## Theorem 2 — The stopping set

In each of the 20 windows the largest formed set is
{plaquette of s} ∪ {links of s} ∪ {corners of s in no other square}, for
a square s with the fewest shared corners. From it, no outside site's
conditional given the formed set equals its conditional given its formed
neighbours. By the closure lemma, the closure of a reachable formed set is
reachable and contains it. So every reachable formed set has at most 7
sites, and none holds all nine sites of a square.

## No-Go Discipline Gate

The negative content is scoped: single sites, local records, the uniform
ice measure on the declared planar windows.

- **N1 alternative routes.** The following are outside this block:
  - plan letters (open PR 8686);
  - joint units (open PR 8720);
  - planar windows of six or more squares, other than the 3 x 2
    rectangle;
  - three-dimensional windows beyond two cubes;
  - the static reading (open PR 8679).
- **N2 wall independence.** Exact searches with a validated search
  method, and a weight check against an independent generating function.
- **N3 hidden walls.** The window measure's private links are declared.
  Open PR 8727 shows the negative does not come from them on the landed
  torus.
- **N4 residual matching.** The single-site route's residual is plan
  letters.
- **N5 rhetoric audit.** "No order" refers to the declared windows and
  schemes.
- **N6 partial-closure paths.** Larger windows; coordinators on
  non-square cells; plan letters.
- **N7 steelman.** For single sites: one square forms, and the stopping
  set is almost a full square. Against: no window of two to five squares
  forms, and no formed set holds a whole square. Both are recorded.
- **N8 cross-cycle echo.** Open PRs 8648, 8679, 8686, 8715, 8719, 8720 and
  8727 are cited.

## Falsifiers

Any of the following falsifies the theorems:
- an order on any of the 20 windows under any declared scheme;
- a stopping set other than the declared square set;
- a window weight differing from its generating-function coefficient.

## Boundaries and non-claims

- The declared windows, measure, records and criterion.
- No reading, rule, alphabet, unit or order law is adopted.
- Nothing here grades, unlocks or audits any other claim.

## Imports

Open PRs 8648, 8679, 8686, 8715, 8719, 8720 and 8727 and the landed
cubic-ice and role-pattern notes are cited. No audit grade, no new axiom,
no new primitive, no new comparator and no new framing is imported.

## Review record

- **Seat:** one Opus 5.5 seat; no subagents; runner and note by the same
  seat.
- **Independence sources:**
  - the closed-set search is checked against the plain search;
  - window weights are checked against a generating function;
  - polyomino counts are checked against the known sequence;
  - the stopping set is checked against its predicted form, and its dead
    end is checked directly.
- **Mutation census** (caught means at least one FAIL line or a nonzero
  exit; the runner exits nonzero on any FAIL):

| Mutant | Change | Result |
|---|---|---|
| every step admissible | admissibility returns true | caught (1 FAIL) |
| five other links per vertex | 6 - degree to 5 - degree | caught (1 FAIL) |
| coordinators only on polyomino cells | fully bounded squares dropped | caught (3 FAILs) |
| canonical form without the diagonal swap | 8 symmetries to 4 | caught (3 FAILs) |
| stopping set keeps shared corners | shared corners not removed | caught (1 FAIL) |
| plain search budget too small | 20000 to 50 | caught (1 FAIL) |
| generating function with five other links | private factor 6 - degree to 5 - degree | caught (1 FAIL) |
| formed neighbours are all formed sites | neighbour filter removed | caught (1 FAIL) |
| groups drop one site | first site skipped | caught (1 FAIL) |
| coarser schemes ignored | scheme not passed | caught (1 FAIL) |
| closure step disabled | closure removed | caught (1 FAIL) |
| sweep budget too small | 5000 to 5 | caught (2 FAILs) |
| stopping set predicted from the worst square | max to min | caught (1 FAIL) |

  All 13 are caught.

- **Vacuity guard:** window counts, closed-set counts and largest formed
  sets are printed.
- **Budget:** 6 checks, stdout 1941 characters (ceiling 6000), about
  105 s (ceiling 900 s), peak memory about 0.4 GB, exact integer
  comparisons.

## Verification

```bash
python3 scripts/uniform_ice_planar_windows_of_two_to_five_squares_admit_no_single_site_formation_order_2026_09_23.py
```

Expected summary line: `TOTAL: PASS=6 FAIL=0`; the runner exits nonzero
if any check fails. Cached output:
`logs/runner-cache/uniform_ice_planar_windows_of_two_to_five_squares_admit_no_single_site_formation_order_2026_09_23.txt`.
