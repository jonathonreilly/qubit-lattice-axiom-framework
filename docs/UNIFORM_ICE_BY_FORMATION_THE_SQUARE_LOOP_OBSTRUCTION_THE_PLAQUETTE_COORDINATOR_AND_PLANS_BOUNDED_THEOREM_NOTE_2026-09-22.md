---
claim_id: uniform_ice_by_formation_the_square_loop_obstruction_the_plaquette_coordinator_and_plans_bounded_theorem_note_2026-09-22
claim_type: bounded_theorem
claim_scope: "Formation model with supplied skip-and-continue semantics, on the square window (four vertices of one coarse plaquette, their twenty links, optionally the plaquette site, which neighbours the square's four links). Uniform ice measure on the window: 10016 configurations (tr T^4, T = [[4,6],[6,4]]). With local records (a vertex's record is equivalent to its six links' occupations, being a function of them that determines them, and a link's record is its occupation), no nearest-neighbour formation law, in any fixed external order with fresh conditional draws and any local rule, reproduces the uniform ice measure without an unrecorded site: the sites formed before the last-formed square site span a forest, and the path's ends are dependent both marginally and given the middle site, for all 8 choices, which no orientation of the path allows. The sweep of open PR 8667 is an instance (1/8000 or 1/12000). A plaquette site that forms first and records its links' pattern (a law invariant under the square's 8 symmetries) reproduces the uniform law exactly with no unrecorded site; on two squares sharing a link the coupling returns (each square's other links depend on the other's given the shared link), so a second coordinator seeing only the shared link cannot supply the law. Non-local plan records also reproduce it. No rule, record scheme, order law or identification is adopted."

upstream_dependencies:
  - minimal_axioms
runner: scripts/uniform_ice_by_formation_square_loop_obstruction_plaquette_coordinator_and_plans_2026_09_22.py
---

# Uniform ice by formation: the square loop obstruction, the plaquette coordinator, and plans

**Date:** 2026-09-22
**Type:** bounded_theorem
The [framework axioms](MINIMAL_AXIOMS_2026-06-29.md) do not select the
abstract record alphabet or stochastic model used below. In the formation
models an external fixed order is supplied, and each draw uses fresh
randomness conditional on its already formed nearest neighbours. These are
stronger conditions than equality of one-site marginals. Skipping failed
attempts and continuing is also supplied; it is not implied by unreadability.
Random/adaptive orders and correlated draws are outside the exclusions.
The static models instead test the explicitly defined conditional-locality
property on a supplied finite joint law. No qubit encoding, physical
realizability, retained grade, photon identification or gravity conclusion
is established by these abstract finite models.


## Result up front

1. **The square's loop blocks it for local records.** On the square
   window, give each vertex a record equivalent to its six links'
   occupations (like the soldered vertex records of open PR 8667), and
   each link its occupation. Then no nearest-neighbour formation law reproduces the
   uniform ice measure without an unrecorded site. This holds for every fixed external order and local rule under the
   fresh-draw factorization; it does not exclude arbitrary order mixtures.

   The proof takes the last-formed of the square's 8 sites. Everything
   formed before it spans a forest of the neighbour graph, so the law
   formed so far is a directed Markov law on a forest. Between that
   site's two neighbours the forest has a single path.
   - If the path's orientation has a collider, the two ends are
     independent.
   - If it has none, the ends are independent given any inner site.

   The uniform measure makes the ends dependent both marginally and
   given the middle site, for every choice of the last site. The sweep of
   open PR 8667 is one instance: it completes, but with masses 1/8000 or
   1/12000.

2. **The plaquette site coordinates the square exactly.** The plaquette
   site is the nearest neighbour of the square's four links. Suppose it
   forms first and records the pattern of its four links, drawn from the
   ice measure's marginal (a law invariant under the square's 8
   symmetries). Its links copy the pattern, the vertices fill their other
   links uniformly, and the finished law is exactly uniform, 1/10016 per
   configuration, with no unrecorded site. The coordinator's record names
   its links, so it needs a frame source (soldering or coordinate
   letters), as in open PRs 8676 and 8679.

3. **The coordination does not simply extend.** On two squares sharing a
   link (501632 ice configurations), each square's other links depend on
   the other square's given the shared link. So a second coordinator that
   sees only the shared link cannot supply the law, and the loop problem
   returns one level up. Larger windows and other orders are not
   classified here.

4. **Plans also work, at a price.** If a vertex records a whole window
   configuration, a "plan", and every site copies it along, the law is
   exactly uniform. The price is 10016 plan records carrying non-local
   content.

5. **Scope.** These are conditional mathematical results. No exhaustive
   decision set, physical necessity or infinite-volume phase is inferred.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "test the explicitly supplied finite record models within their stated domains"
source_of_blocker_text: frontier_question
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "test extensions beyond the finite hypotheses; no physical downstream conclusion is established"
conditional_surface_status: "formation reading; supplied failure convention; declared window; local record scheme (vertex records determining their stars, link occupations); supplied plaquette-coordinator and plan schemes"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "item 1 is a short proof whose finite hypotheses (one loop, forest after removal, dependences) are checked exactly; items 2-4 are exact computations on the declared windows"
```

## Premises and declared objects

Formation model with supplied skip-and-continue semantics: a site forms with a
law that depends on its formed nearest neighbours only, and a site with no
admissible possibility carries no record. The superlattice roles of the
landed roles note place a vertex's six links, and a plaquette site's four
links, among its nearest neighbours.

- **The square window.** The four vertices of one coarse plaquette, their
  twenty links, and, when stated, the plaquette site.
- **The uniform ice measure.** Uniform on the link occupations with 3 of
  every vertex's 6 links occupied.
- **Local records.** A vertex record is equivalent to its six links'
  occupations: it is a function of them and determines them, as the
  six-tuple itself or the soldered set of occupied directions does. A
  link record is its occupation. Plans are not local.
- **Plans.** Records carrying a whole window configuration.

## Relation to earlier work

The mathematical models and proofs used here are stated locally. Earlier
campaign labels and open-PR comparisons supply no load-bearing premise.

## Theorem 1 — The square loop obstruction

Let a formation law, in a fixed external order with fresh conditional draws,
finish without unrecorded sites almost surely and
have the uniform ice measure as its record law, with local records. Let c
be the last-formed of the 8 square sites, and Q the set of sites formed
before it.

1. **The law on Q is a directed Markov law on a forest.** Every site's
   parents are formed neighbours inside Q, and the neighbour graph
   restricted to Q is a forest. The incidence graph has exactly one loop,
   the square, and removing any of its sites leaves a forest (checked).
2. **Between c's two square neighbours a and b the forest has a single
   path**, the other 7 square sites. Along it, either some site formed
   after both its path neighbours (a collider) or none did.
   - With a collider, the path is blocked given nothing, so a and b are
     independent.
   - With no collider, the path is blocked by any inner site, so a and b
     are independent given it.
3. **The uniform measure's marginal on Q must satisfy the same
   independences.** For each of the 8 choices of c, a and b are dependent
   marginally, and dependent given the middle site (checked; given 3 to 5
   of the 5 inner sites). Neither case is possible.

Records with different or partial content are not excluded by this proof.
The single-vertex 5/16 bound requires its own independent Bernoulli sampling
hypotheses and cannot rule out all such record schemes.

## Theorem 2 — The plaquette coordinator

The formation order and its rules:
1. The plaquette site forms first. With no formed neighbour, it draws the
   pattern of its four links from the ice measure's marginal on them. The
   weights are prod over the square's vertices of C(4, 3 - s_v), where
   s_v is the number of the vertex's two square links that are occupied.
   This law is invariant under the square's 8 symmetries (checked).
2. Each square link copies its bit from the pattern.
3. Each vertex takes a uniform consistent star.
4. Each remaining link copies its vertex.

The formation programme returns exactly 1/10016 on each of the 10016
configurations, with no unrecorded site. With the plaquette site present,
removing any square site still leaves a loop through the plaquette, so
Theorem 1's forest step does not apply (checked).

## Theorem 3 — Two squares

On the 2 x 1 window, the six vertices carry 7 grid links and 3 or 4
private links each. The measure's weight on the grid links is the product
of C(private, 3 - grid sum) over vertices, which gives 501632 ice
configurations.

Given the shared link, the other square links of the two squares are
dependent (checked for both values). A coordinator for the second square
that sees only the shared link produces them independently given that
link, so it cannot supply the law in that order.

## Theorem 4 — Plans

Choose a fixed connected order (every later site has an earlier neighbour).
The first site draws one complete link configuration uniformly; each later
site copies its formed neighbours' common plan. Induction gives one identical
plan everywhere. Reading each named link bit from that plan gives exactly the
uniform law. This uses a supplied direction/position interpretation of the plan. The records then carry the whole window's content.

## No-Go Discipline Gate

**N1 — Alternative challenges.**

- **Collider orientation (ATTEMPTED):** a collider on the forest path forces marginal endpoint independence, contrary to the exact target marginal.
- **No collider (ATTEMPTED):** conditioning on the middle path record separates endpoints, again contrary to the exact target marginal.
- **Plaquette coordinator (ATTEMPTED):** the explicitly supplied coordinator distribution yields uniform mass 1/10016.
- **Copied plan (ATTEMPTED):** a connected fixed order propagates a uniform whole-window record, outside the local-record hypothesis.
- **Random/adaptive orders (ATTEMPTED):** the fixed-DAG obstruction does not survive arbitrary mixtures automatically; these are not ruled out.

**N2–N4 — Conditions and residuals.** Alphabet, fixed order, fresh draws,
record content and window are joint hypotheses, not independent physical
walls. The local proofs below support only their stated implications;
no historical campaign residual is closed by analogy. Standard finite
probability, counting and the named elementary inequalities are imports.

**N5 — Resolution.** The runner states its executed windows and enumeration
sizes. Source arguments support universal statements; finite tests do not
execute infinite formation, continuum spectra or a thermodynamic limit.

**N6–N8 — Remaining routes and cross-check.** Informative auxiliary records,
shared randomness, alternative orders and other alphabets remain possible.
The positive alternative constructions identify concrete ways outside each
negative hypothesis. No new axiom/primitive or general physical exclusion
is claimed. Related formation results retain their own declared domains.


## Falsifiers

- An order and rule with local records that reproduce the uniform law on
  the square window with no unrecorded site falsify Theorem 1.
- A plaquette-first law that is not exactly uniform falsifies Theorem 2.
- Conditional independence of the two squares' other links given the
  shared link falsifies Theorem 3.

## Boundaries and non-claims

No rule, record scheme, order law or physical identification is adopted.
The window is one square; larger windows are not classified. Nothing here
changes open PR 8667's finding that the ice support is formed with
soldering and an order law. Nothing here grades, unlocks or audits any
other claim.

## Imports

The landed notes and open PRs are cited. d-separation in directed Markov
laws is standard probability. No audit grade, no new axiom, no new
primitive, no new comparator and no new framing is imported.

## Review record

- **Seat:** one Opus 5.5 seat; no subagents; runner and note by the same
  seat.
- **Independence sources:**
  - the window count is compared with a transfer-matrix trace, and with
    open PR 8667;
  - the forest and loop checks run on the incidence graph directly;
  - dependences are computed from the measure, not from any formation;
  - the coordinator's law comes from a generic formation programme, not
    from the product formula.
- **Mutation census** (caught means at least one FAIL line or a nonzero
  exit; the runner exits nonzero on any FAIL):

| mutation | substitution | result |
|---|---|---|
| ice rule counts 2 of 6 | 3 to 2 | caught (2 FAILs) |
| transfer weights shifted | C(4, 3 - s) to C(4, 2 - s) | caught (1 FAIL) |
| loop count ignores merges | component merge removed | caught (1 FAIL) |
| dependence test always false | test disabled | caught (2 FAILs) |
| middle site replaced by an end's neighbour | inner site index | caught (1 FAIL) |
| sweep vertex ignores formed links | consistency dropped | caught (2 FAILs) |
| coordinator draws patterns uniformly | marginal to uniform | caught (1 FAIL) |
| square links copy one fixed bit | own bit to bit 0 | caught (1 FAIL) |
| symmetry test includes a non-symmetry | a swap of two links | caught (1 FAIL) |
| two-square private counts off by one | 6 to 5 | caught (1 FAIL) |
| plan draw not uniform | 1/10016 to 1/10015 | caught (1 FAIL) |
| forest test includes the plaquette | graph with the plaquette | caught (1 FAIL) |
| coordinator bits read one place round the square | cyclic shift | missed; diagnosed non-defect (the coordinator's law is invariant under the square's rotations) |
| coordinator bits complemented | 1 - bit | missed; diagnosed non-defect (the ice measure is invariant under complementing every link) |

  Twelve of twelve defect mutants are caught; the two relabellings are
  symmetries of the law.

- **Vacuity guard:** window counts (10016 and 501632) and state counts are
  printed; each negative statement is checked for all 8 choices.
- **Budget:** 9 checks, stdout 1530 characters (ceiling 6000), about 8 s
  (ceiling 900 s), exact Fractions.

## Verification

```bash
python3 scripts/uniform_ice_by_formation_square_loop_obstruction_plaquette_coordinator_and_plans_2026_09_22.py
```

Expected summary line: `TOTAL: PASS=9 FAIL=0`; the runner exits nonzero
if any check fails. Cached output:
`logs/runner-cache/uniform_ice_by_formation_square_loop_obstruction_plaquette_coordinator_and_plans_2026_09_22.txt`.

## Pre-landing correction record

Review in the current primary Codex session narrowed unsupported physical and
off-domain conclusions, made model premises explicit, and checked the source
arguments against the paired runner. Original author mutation counts above
are historical reports, not a separate review or a rerun by this session.
No subagents or audit verdicts were used.
