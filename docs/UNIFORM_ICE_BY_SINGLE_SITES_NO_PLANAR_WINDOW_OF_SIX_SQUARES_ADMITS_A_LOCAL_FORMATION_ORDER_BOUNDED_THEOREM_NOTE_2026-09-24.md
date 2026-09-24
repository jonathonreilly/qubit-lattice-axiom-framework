---
claim_id: uniform_ice_by_single_sites_no_planar_window_of_six_squares_admits_a_local_formation_order_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "The 35 free hexominoes span 32 induced vertex/link windows that no smaller polyomino spans, with 13 or 14 vertices and 6 or 7 plaquette coordinators. Every total weight agrees with an independent generating-function coefficient. With full local records and every coordinator, none of the 32 windows admits a fixed single-site formation order under the criterion of landed PR 8715 and the closed-set search of landed PR 8719; every search completes within its budget. In each window one recorded maximum-size formed set is a plaquette with its links and unshared corners, 7 sites, and no outside site is admissible. Coarser record schemes, adaptive orders and larger windows are not tested."
upstream_dependencies:
  - minimal_axioms
  - uniform_ice_by_formation_two_planar_squares_admit_no_local_order_and_one_cube_needs_its_cube_site_bounded_theorem_note_2026-09-22
  - uniform_ice_by_formation_two_adjacent_cubes_admit_no_local_order_even_with_both_cube_sites_bounded_theorem_note_2026-09-23
  - uniform_ice_by_single_sites_no_planar_window_of_two_to_five_squares_admits_a_local_formation_order_bounded_theorem_note_2026-09-23
runner: scripts/uniform_ice_planar_windows_of_six_squares_admit_no_single_site_formation_order_2026_09_24.py
---

# No fixed single-site order on the thirty-two induced windows of six squares

**Date:** 2026-09-24
**Type:** bounded_theorem

## Result and scope

Landed PR 8735 swept the induced windows of free polyominoes of one to
five squares and found a fixed single-site formation order only for the
lone square. This note extends that sweep to six squares. The 35 free
hexominoes span 32 windows that no smaller polyomino spans. With full
local records and every coordinator, none of them admits an order. In each
window the search stops at a 7-site set built from one square.

Uniform ice is a supplied finite model, and the results are exact finite
computations on the stated windows. The boundaries of landed PR 8735 apply
unchanged:
- orders are fixed and deterministic;
- each conditional draw uses fresh randomness and depends only on the
  records of the actual formed neighbours;
- the sufficiency criterion permits site- and stage-specific kernels.

Adaptive orders, hidden shared state, mixtures, private-link formation
schemes, coarser record schemes and windows of seven or more squares are
not tested.

## Premises and declared objects

All objects are those of landed PR 8735, unchanged:
- **Criterion.** With local records, a nearest-neighbour formation law
  reproduces a record law exactly, with no unrecorded sites, precisely
  when some order adds sites one at a time so that each site's
  conditional, given all sites formed so far, depends only on its formed
  neighbours (landed PR 8715).
- **Search.** The closed-set search with its closure lemma (landed PR
  8719). It is checked here, as in landed PR 8735, against the plain
  search on five small windows.
- **Windows.** A window is the vertex set of a polyomino in doubled
  coordinates, with every link between its vertices and a plaquette
  coordinator on every square whose four links are in the window. Each
  vertex's other links are private to it.
- **Measure.** The uniform ice measure: 3 of each vertex's 6 links are
  occupied. On grid links it weighs a pattern by
  prod_v C(private links, 3 − grid sum).
- **Records.** Links record occupation; vertices and plaquettes record the
  pattern of their own grid links.

## Theorem 1 — No order on the six-square windows

Count the free hexominoes by canonical form under the eight symmetries of
the square: there are 35. Their vertex sets give 32 windows not spanned by
any polyomino of one to five squares, with 13 or 14 vertices and 6 or 7
coordinators (29 with 6, 3 with 7). Every window's total weight equals its
generating-function coefficient; the totals run from 315644174336 to 3156272283648.

With full local records and every coordinator, none of the 32 windows
admits a fixed single-site order. Every search completes within its
budget of 5000 closed sets, using 38 to 42 closed sets.

## Theorem 2 — The stopping set

In each of the 32 windows one recorded maximum-size formed set is
{plaquette of s} ∪ {links of s} ∪ {corners of s in no other square}, for
a square s with the fewest shared corners. It has 7 sites. From it, no
outside site's conditional given the formed set equals its conditional
given its formed neighbours. By the closure lemma every reachable formed
set lies in a reachable closed set, so none holds all nine sites of a
square, as for five squares.

## Machine status and trace

- **Runner:**
  `scripts/uniform_ice_planar_windows_of_six_squares_admit_no_single_site_formation_order_2026_09_24.py`
  (declares `AUDIT_TIMEOUT_SEC = 1800`).
- **Result:** `TOTAL: PASS=5 FAIL=0`, about 1030 s alone and 1230 s under load,
  stdout 1407 characters, peak about 1.5 GB. The windows are searched one at a time,
  since a 14-vertex window's search holds about 1.5 GB.
- **Cache:**
  `logs/runner-cache/uniform_ice_planar_windows_of_six_squares_admit_no_single_site_formation_order_2026_09_24.txt`
- **Arithmetic:** exact integer weights and exact integer cross-product
  tests for every conditional, as in landed PR 8735.

## No-Go Discipline Gate

- **N1 — Domain:** the 32 windows with full records and every
  coordinator; fixed deterministic orders.
- **N2 — Independence:** every total weight is recomputed by an
  independent generating function, and the closed-set search is checked
  against the plain search.
- **N3 — Imports:** the supplied ice model and the criterion, search and
  records of landed PRs 8715, 8719 and 8735; no new axiom or primitive.
- **N4 — Dependencies:** the three landed notes supply definitions within
  their scope.
- **N5 — Resolution:** exact integer arithmetic; every search completes,
  so no cap binds.
- **N6 — Remaining work:** coarser record schemes on these windows;
  windows of seven or more squares; adaptive orders.
- **N7 — Strongest objection:** finite windows do not establish
  impossibility on the plane.
- **N8 — Review boundary:** no audit verdict, retained grade or assembly
  decision is applied.

## Falsifiers

- A counterexample under the exact hypotheses: an order on one of the 32
  windows, or a failed independent weight count.
- A fresh run of the runner that fails a check.

## Imports

- [minimal_axioms](MINIMAL_AXIOMS_2026-06-29.md): repository boundary;
  does not derive the supplied ice model.
- [Companion result from PR #8715](UNIFORM_ICE_BY_FORMATION_TWO_PLANAR_SQUARES_ADMIT_NO_LOCAL_ORDER_AND_ONE_CUBE_NEEDS_ITS_CUBE_SITE_BOUNDED_THEOREM_NOTE_2026-09-22.md)
- [Companion result from PR #8719](UNIFORM_ICE_BY_FORMATION_TWO_ADJACENT_CUBES_ADMIT_NO_LOCAL_ORDER_EVEN_WITH_BOTH_CUBE_SITES_BOUNDED_THEOREM_NOTE_2026-09-23.md)
- [The sweep of one to five squares, PR #8735](UNIFORM_ICE_BY_SINGLE_SITES_NO_PLANAR_WINDOW_OF_TWO_TO_FIVE_SQUARES_ADMITS_A_LOCAL_FORMATION_ORDER_BOUNDED_THEOREM_NOTE_2026-09-23.md)

## Review record

- **Seat:** one Opus 5.5 seat; no subagents. The runner reuses the
  functions and the search check of landed PR 8735 verbatim and adds the
  six-square windows. No separate reviewer or audit is claimed.
- **Correction before landing.** A first version built all 32 windows at
  once, as the five-square runner does; with 14-vertex windows that would
  hold several GB. The windows are now built and searched one at a time,
  and the weights are checked in a cheap first pass so that a weight
  failure stops the sweep.
- **Mutation census** (caught means at least one FAIL line or a nonzero
  exit; the runner exits nonzero on any FAIL):

| Mutant | Change | Result |
|---|---|---|
| admissibility always granted | admissibility removed | caught (search check fails; no sweep) |
| every record read as a function of its formed neighbours | closure changed | caught (search check fails; no sweep) |
| polyominoes grown in three directions | enumeration changed | caught (window check fails; no sweep) |
| generating weight with five link slots per vertex | independent count changed | caught (weight check fails; no sweep) |
| windows of smaller polyominoes kept | window set changed | caught (window check fails; no sweep) |
| search budget of five closed sets | cap made to bind | caught (2 FAILs) |
| shared corners ignored in the stopping shape | stopping set changed | caught (1 FAIL) |

  7 of 7 are caught.

## Verification

```bash
python3 scripts/uniform_ice_planar_windows_of_six_squares_admit_no_single_site_formation_order_2026_09_24.py
```

Expected summary line: `TOTAL: PASS=5 FAIL=0`; the runner exits nonzero
if any check fails. Cached output:
`logs/runner-cache/uniform_ice_planar_windows_of_six_squares_admit_no_single_site_formation_order_2026_09_24.txt`.
