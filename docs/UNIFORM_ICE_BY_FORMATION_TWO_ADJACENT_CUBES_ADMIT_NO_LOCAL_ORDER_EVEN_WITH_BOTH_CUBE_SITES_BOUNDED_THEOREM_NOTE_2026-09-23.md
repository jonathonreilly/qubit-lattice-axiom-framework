---
claim_id: uniform_ice_by_formation_two_adjacent_cubes_admit_no_local_order_even_with_both_cube_sites_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "Formation reading with the text's hole semantics and local records. Closure lemma: in an order that reproduces a record law, a site whose record is a function of its formed neighbours' records can be moved forward to the first moment it is one without breaking any later step, so a search over formed sets closed under such sites decides whether an order exists; it reproduces the plain search of open PR 8715 on six windows (same verdicts and same largest formed sets). On two cubes sharing a face (45 sites; uniform ice weight 3985518592, recomputed as a generating-function coefficient), with both cube sites, no complete order reproduces the uniform ice measure for full local records (vertex, plaquette and cube-site records are their edge patterns) or for three coarser schemes (vertex records carry nothing; plaquette records carry nothing; both carry nothing). With full local records the largest formed set is one cube's sites: its cube site, 6 plaquettes, 12 links and 4 outer vertices; the other cube site depends on the formed cube beyond the shared plaquette. One top cell is coordinated exactly by its own site (open PR 8715); two adjacent ones are not. Larger windows are not searched. No rule, record scheme or order law is adopted."

upstream_dependencies:
  - minimal_axioms
  - realized_state_primitive
  - spin_half_cubic_ice_exact_rk_coulomb_correlations_and_finite_qubit_photon_phase_bridge_bounded_theorem_note_2026-09-03
  - the_superlattice_role_pattern_is_a_next_nearest_neighbour_support_rule_over_roles_and_roles_are_not_record_values_bounded_theorem_note_2026-09-04
runner: scripts/uniform_ice_two_adjacent_cubes_no_local_formation_order_closed_set_search_2026_09_23.py
---

# Uniform ice by formation: two adjacent cubes admit no local order, even with both cube sites

**Date:** 2026-09-23
**Type:** bounded_theorem
**Campaign:** next-steps campaign after the TOE derivation campaign by
underdetermination witnesses. Open PR 8715 showed three things about
exact local formation of the uniform ice measure:
- one square is formed exactly with its plaquette site;
- two squares in the plane are not formed exactly by any order;
- one cube is formed exactly with its cube site.

It left two adjacent cubes unsearched. That case decides whether cube
coordination extends in three dimensions, where every cube has its own
cube site. This block searches it.

## Result up front

1. **A closure lemma makes the search small.** Take any site whose record
   is a function of its formed neighbours' records. Moving it forward, to
   the first moment it becomes such a function, keeps every later step
   admissible. So an order exists if and only if one exists that adds such
   sites at once. A depth-first search over formed sets closed in this way
   decides the question. On six windows this search agrees with the plain
   search of open PR 8715: the same verdicts and the same largest formed
   sets.

2. **Two cubes: no order.** On two cubes sharing a face (45 sites), no
   order reproduces the uniform ice measure, even with both cube sites
   present. This holds for full local records and for three coarser
   schemes. With full local records the largest formed set is one cube's
   sites: its cube site, its 6 plaquettes, its 12 links and its 4 outer
   vertices. Nothing of the other cube can follow. In particular, the
   other cube site's conditional depends on the formed cube beyond the
   shared plaquette.

3. **Local coordination stops at one top cell, in both dimensions.** A
   top cell's own site coordinates it exactly (open PR 8715). Two
   adjacent top cells are not formed exactly by any order, whether two
   squares in the plane (open PR 8715) or two cubes here, for every record
   scheme tested.

4. **What this means for the photon lane.** On these windows, local
   formation does not reach the uniform ice measure behind the landed
   Coulomb correlations beyond one top cell. The equal-time Coulomb law
   comes instead from the static reading with a positive rule (open
   PR 8698). By formation it needs one of:
   - plan records with non-local content (open PR 8686);
   - conditioning, which is not in the text.

   With local records, formation gives directed, causal ice with
   persistent-walk transport (open PRs 8687, 8701).

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "coordinated formation of the uniform ice measure beyond one top cell (open edge of open PR 8648; open PRs 8686, 8715)"
source_of_blocker_text: open_prs_8648_8686_8715
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "record on the formed photon route that the uniform measure by formation needs plan records or conditioning beyond one top cell"
conditional_surface_status: "formation reading; text hole semantics; declared windows; local record schemes (edge patterns or nothing)"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "a lemma with a short proof that reduces the search, checked against the plain search, and a complete closed-set search with exact conditional laws"
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

## Prior art and what is new

- Open PR 8715: the criterion, the plain search, two squares with no
  order, and one cube formed exactly by its cube site.
- Open PR 8686: the loop obstruction, the plaquette coordinator and plans.
- New here:
  - the closure lemma;
  - the closed-set search, checked against the plain one;
  - two adjacent cubes admit no order even with both cube sites.
- Standard: conditional expectations and the tower property.

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

Under full local records, the largest set is one cube's own sites. There,
the other cube site's conditional given that cube and the shared plaquette
differs from its conditional given the shared plaquette alone. This is
because the four shared vertices' weights couple the two cubes' edges
perpendicular to the shared face.

## No-Go Discipline Gate

The negative content is scoped: two cubes sharing a face, the declared
record schemes, local records.

- **N1 alternative routes.** The following are outside the search:
  - larger windows;
  - other functions of local content;
  - plan records;
  - conditioning.
- **N2 wall independence.** Exact conditional laws and a finite search;
  no dynamics.
- **N3 hidden walls.** Records are local by declaration. Plans work (open
  PR 8686).
- **N4 residual matching.** The formed photon route's residual is plan
  records or conditioning.
- **N5 rhetoric audit.** "No order" refers to the declared window and
  schemes.
- **N6 partial-closure paths.** Larger windows; other record functions.
- **N7 steelman.** For formation: every top cell alone is coordinated
  exactly, and the static reading supplies the Coulomb law. Against
  exact formation of the uniform measure: two adjacent cubes fail as two
  squares do. Both are recorded.
- **N8 cross-cycle echo.** Open PRs 8648, 8686, 8687, 8698, 8701 and 8715
  are cited; the six validation windows reproduce open PR 8715.

## Falsifiers

- An order on the two cubes, under a declared scheme, with every site's
  conditional depending only on its formed neighbours, falsifies
  Theorem 2.
- A site moved forward by the closure lemma whose conditional changes
  falsifies Theorem 1.
- A validation window where the two searches disagree does too.

## Boundaries and non-claims

- No rule, record scheme or order law is adopted.
- The windows are declared: larger windows and the infinite-volume
  measure are not searched.
- Nothing here grades, unlocks or audits any other claim.

## Imports

The landed notes and open PRs are cited. Conditional expectations are
standard. No audit grade, no new axiom, no new primitive, no new
comparator and no new framing is imported.

## Review record

- **Seat:** one Opus 5.5 seat; no subagents; runner and note by the same
  seat.
- **Independence sources:**
  - the closed-set search reproduces the plain search of open PR 8715 on
    six windows;
  - the two-cube weight is recomputed as a generating-function
    coefficient, with vertex-by-vertex elimination on unit coordinates;
  - each admissibility test compares two independently grouped
    conditional laws by integer cross-multiplication.
- **Mutation census** (caught means at least one FAIL line or a nonzero
  exit; the runner exits nonzero on any FAIL):

| mutant | change | outcome |
|---|---|---|
| closure adds every site | function test always true | caught (1 FAIL) |
| closure adds no site | function test always false | caught (1 FAIL) |
| admissibility always true | early return | caught (1 FAIL) |
| neighbours out to distance 2 | distance 1 to at most 2 | caught (1 FAIL) |
| private links counted as 5 | 6 minus grid degree to 5 minus grid degree | caught (1 FAIL) |
| cube sites record half their edges | 12 edges to 6 | caught (1 FAIL) |
| generating function drops a private link | C(6 - deg, k) to C(5 - deg, k) | caught (1 FAIL) |
| two-cube budget below the real search | 1000 to 10 | caught (1 FAIL) |
| shared-face plaquette missing | plaquette (2, 1, 1) removed | caught (2 FAIL, then a nonzero exit) |
| coupling table with three private links | C(2, k) to C(3, k) | caught (1 FAIL) |
| largest set compared with the wrong outer face | x = 2 to x = 0 | caught (1 FAIL) |
| closure tests the whole formed set | formed neighbours to all formed sites | not run to the end; diagnosed equivalent here: at every closed state of the six validation windows, no site is a function of the formed set without being a function of its formed neighbours |

Eleven of eleven defect mutants are caught; the whole-set closure mutant
is the diagnosed equivalent row.

- **Vacuity guard:** closed-set counts and largest formed sets are
  printed for every search; a binding budget fails its check.
- **Budget:** 5 checks, stdout 1435 characters (ceiling 6000),
  about 200 s (ceiling 900 s), exact integer arithmetic.

## Verification

```bash
python3 scripts/uniform_ice_two_adjacent_cubes_no_local_formation_order_closed_set_search_2026_09_23.py
```

Expected summary line: `TOTAL: PASS=5 FAIL=0`; the runner exits
nonzero if any check fails. Cached output:
`logs/runner-cache/uniform_ice_two_adjacent_cubes_no_local_formation_order_closed_set_search_2026_09_23.txt`.
