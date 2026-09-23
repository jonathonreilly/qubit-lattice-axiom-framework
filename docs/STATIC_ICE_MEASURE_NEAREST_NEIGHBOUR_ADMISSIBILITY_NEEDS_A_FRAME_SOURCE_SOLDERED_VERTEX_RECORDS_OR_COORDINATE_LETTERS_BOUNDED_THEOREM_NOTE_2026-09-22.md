---
claim_id: static_ice_measure_nearest_neighbour_admissibility_needs_a_frame_source_soldered_vertex_records_or_coordinate_letters_bounded_theorem_note_2026-09-22
claim_type: bounded_theorem
claim_scope: "Static reading of the distribution sentence (each site's conditional given all others is a function of its six nearest-neighbour values; under the unsoldered reading, of their configuration up to proper rotation), applied to the uniform ice measure of the landed spin-half cubic-ice notes on the fine torus Z_4^3 with superlattice roles (the coarse 2x2x2 torus: 9600 ice configurations, 880 at zero flux). In occupation form (vertex, plaquette and cube records carrying nothing about links) a link's conditional is fixed by next-nearest links and every link takes both values under identical neighbour records, in all states and in the zero-flux sector: the sentence fails. Soldered vertex records naming the occupied directions restore the conditional-locality property at all 64 sites, with the uniform link marginal and a rotation-invariant support. Unsoldered records that cannot tell a vertex's links apart fail on one vertex star and on the 2x2x2 torus with plaquette and cube records constant, for every vertex alphabet. Coordinate letters (open PR 8676) restore it without soldering: the static frame rule is rigid (plaquette lemma checked over every case), neighbour labels fix a site's label, and every site's value is a function of its neighbours' values up to rotation. No reading, record scheme, alphabet or physical identification is adopted."

upstream_dependencies:
  - minimal_axioms
runner: scripts/static_ice_measure_nearest_neighbour_admissibility_needs_a_frame_source_2026_09_22.py
---

# Static conditional locality of four record schemes on the small ice torus

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

1. **Occupation form breaks the nearest-neighbour sentence.** Under the
   static reading, each site's conditional given all other sites must be
   a function of its six nearest neighbours. The ice measure lives on link
   occupations, with exactly 3 of the 6 links of every vertex occupied.
   The test window is the fine torus Z_4^3, which is the landed note's
   L = 2 torus: 9600 ice configurations, 880 of them at zero flux.
   - A link's conditional is fixed by the other five links at either
     endpoint. Those are next-nearest sites.
   - With vertex, plaquette and cube records that carry nothing about the
     links, every link takes both values under identical neighbour
     records. This holds in all 9600 states and in the zero-flux sector
     alone.

   Thus this particular constant-auxiliary occupation scheme fails the
   supplied static conditional-locality property.

2. **Vertex records that name the occupied directions restore it.** Let
   each vertex record the set of bond directions of its occupied links.
   Then a link's value is read from either endpoint, and a vertex's record
   from its six links.
   - Every site's value is a function of its neighbours' values: all 64
     sites, all 9600 states.
   - The link marginal is still the uniform ice measure.
   - A record that names directions must rotate with positions, so it is a
     soldered record. The support is invariant under the 24 rotations
     acting on positions and records together.

3. **Records that cannot tell a vertex's links apart cannot.** Under the
   unsoldered reading a link's rule sees its neighbours' values but not
   which bond it is.
   - *One vertex star.* The link's only neighbour is the vertex, so all six
     links would get the same value, and no ice pattern has that.
   - *The 2x2x2 torus, with plaquette and cube records constant.* The two
     links along an axis join the same pair of vertices. Every ice state
     has an axis whose two links differ, and a rule symmetric in its
     endpoints cannot separate them, whatever the vertex alphabet.

4. **Coordinate letters restore it without soldering.** Put the coordinate
   letters of open PR 8676 on every site, and let each vertex record its
   occupied links in label coordinates.
   - *Rigidity.* A plaquette whose two paths agree, with consistent
     back-steps, forces equal local frames (checked over all 48 x 48
     frame pairs). So the complete
     static records are exactly the 48 signed frames with their offsets,
     and a site's six neighbour labels fix its own.
   - *Admissibility.* Every site's value is a function of its neighbours'
     values up to rotation, across a proper and an improper frame
     (1228800 site-state pairs).
   - *Readouts and covariance.* The ice count, the agreement of links with
     vertex records, and the role letters are read from the labels.
     Rotating positions with values fixed keeps them all.

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
conditional_surface_status: "static reading; supplied superlattice roles for the occupation and soldered schemes; supplied record schemes; the landed uniform ice measure as the law under test"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "each statement is an exact enumeration on the declared torus, or a short proof whose finite core is checked in full"
```

## Premises and declared objects

The supplied mathematical static-locality reading: the
conditional of a site given all other sites is a function of its six
nearest-neighbour values. Under the unsoldered reading it is a function
of their configuration up to proper rotation. This is an explicit test property, not an adopted interpretation of the
framework. The same kernel must apply to rotation-equivalent neighbour keys. The fine
torus Z_4^3 carries the superlattice roles: vertex (all coordinates
even), link (one odd), plaquette (two odd), cube (three odd).

The uniform ice measure is uniform on the link occupations with exactly 3
of every vertex's 6 links occupied. Four record schemes are declared:
- occupation form;
- soldered vertex records;
- unsoldered vertex-only records;
- coordinate letters.

## Relation to earlier work

The mathematical models and proofs used here are stated locally. Earlier
campaign labels and open-PR comparisons supply no load-bearing premise.

## Theorem 1 — Occupation form fails

At each vertex, n(l) = 3 minus the sum of the other five links. So a
link's conditional given all others is a point mass fixed by next-nearest
links (checked in all states).

Suppose the vertex, plaquette and cube records are constant. Then a
link's six neighbour values are constant, while its occupation takes both
values across the support. So the conditional is not a function of the
neighbours: this holds for all 24 links, in all 9600 states and in the
880 zero-flux states. The same argument extends when all auxiliary records jointly are
independent of the link configuration; pairwise independence would not suffice.

## Theorem 2 — Soldered vertex records

The vertex value is S_v, the set of directions d with n(v + d) = 1. The
link value is n; plaquettes and cubes carry nothing. Then:
- a vertex's value is fixed by its six links;
- a link's value is fixed by either endpoint's record;
- plaquettes and cubes are constant.

The support is in bijection with the ice configurations. It is invariant
under the 24 rotations acting on positions and, through S, on records.
All three statements are checked at every site and state.

## Theorem 3 — Records that cannot tell a vertex's links apart

Under the unsoldered reading, a link's conditional depends on its
neighbours' values up to the rotations fixing the link. That group
includes the half-turns exchanging its two endpoints.
- *One vertex star.* A link's only neighbour is the vertex, so all six
  links share one conditional. The full conditional of each bit is already a point mass, since the
other five star bits determine it by the ice constraint. Equal local kernels
therefore force equal bits within a configuration. All links are then equal, and none of the
  20 ice patterns is constant.
- *The 2x2x2 torus.* The links v + e_a and v - e_a join the same two
  vertices. With plaquette and cube records constant, they receive equal
  values. A vertex has 3 occupied links, an odd number, so some axis has
  exactly one occupied link, and every one of the 9600 states has such a
  pair.

So no vertex alphabet works there.

## Theorem 4 — Coordinate letters

The static frame rule asks that each site's six neighbour labels be
c + sigma(d) for a signed permutation sigma. The rigidity lemma: if the
two paths around the plaquette of x, x + d, x + e agree and the
back-steps agree, then
sigma_(x+d)(e) = sigma_x(e) and sigma_(x+e)(d) = sigma_x(d). This is
checked over all 48 x 48 pairs and 24 perpendicular direction pairs, with
the first frame fixed by relabelling.

With the back-steps it gives sigma_(x+d) = sigma_x, so sigma is constant.
The complete static records are then the 48 signed frames, all checked,
together with their offsets. Six neighbour labels fix a site's label
uniquely in every frame.

With vertex records in label coordinates, every site's value is a
function of its neighbours' values up to rotation. The key is a
rotation-invariant summary that ignores directions. It is checked over
all states of a proper and an improper frame, and rotations reach the
other 46 frames.

The ice count, the agreement of every link with both vertex records, and
the role letters hold in every lettered state. They keep holding after
rotating positions with values fixed. The records name directions
through label differences, so their abstract value action is unsoldered.
The rotation readout check samples every seventh ice configuration, while
functionality uses every configuration in two representative frames. Global
rotation covariance also follows directly by reindexing the local formulas.

## No-Go Discipline Gate

**N1 — Alternative challenges.**

- **Occupation records (ATTEMPTED):** the point-mass full conditional varies while the local neighbour key remains constant.
- **Soldered records (ATTEMPTED):** the supplied direction-set alphabet restores neighbour functionality on the declared torus.
- **Unsoldered vertex-only records (ATTEMPTED):** equal endpoint pairs cannot determine unequal axis-pair bits when plaquette/cube records are constant.
- **Coordinate records (ATTEMPTED):** the supplied affine label extension restores functionality; this is a positive abstract model.
- **Other windows/records (ATTEMPTED):** larger tori and informative plaquette records are not excluded by the two-vertex-pair obstruction.

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

- An ice state on the torus in which a link's value is a function of
  constant neighbour records falsifies Theorem 1.
- A site whose soldered value is not fixed by its neighbours falsifies
  Theorem 2.
- An ice state on the 2x2x2 torus with every axis pair equal falsifies
  Theorem 3.
- A plaquette whose two paths agree, with consistent back-steps, but
  with unequal frames,
  or a lettered state whose value is not a function of its neighbours up
  to rotation, falsifies Theorem 4.

## Boundaries and non-claims

No reading, record scheme or alphabet is adopted. The soldered vertex
record is the one supplied in open PR 8667. The coordinate letters are
declared, not derived. The window is the 2x2x2 coarse torus; larger tori
and other windows are not computed. Nothing here addresses the landed
note's supplied Hamiltonian, which remains an open edge of the static
route. Nothing here grades, unlocks or audits any other claim.

## Imports

The Admissibility text and the landed notes are cited. No audit grade, no
new axiom, no new primitive, no new comparator and no new framing is
imported.

## Review record

- **Seat:** one Opus 5.5 seat; no subagents; runner and note by the same
  seat.
- **Independence sources:**
  - the ice count and the zero-flux count are compared with the landed
    note's 9600 and 880;
  - neighbour-functionality is tested by grouping states on neighbour
    keys, not by construction;
  - the rigidity lemma is checked over every case, and the direct frame check is
    separate from it.
- **Mutation census** (caught means at least one FAIL line or a nonzero
  exit; the runner exits nonzero on any FAIL):

| mutation | substitution | result |
|---|---|---|
| ice rule counts 2 of 6 | 3 to 2 | caught (5 FAILs) |
| next-nearest identity off by one | 3 to 2 | caught (1 FAIL) |
| soldered record omits the z directions | directions cut | caught (2 FAILs) |
| soldered rotation leaves records unrotated | record rotation removed | caught (1 FAIL) |
| axis pairs mismatched | opposite pairs to perpendicular | caught (1 FAIL) |
| rigidity lemma drops the back-step condition | condition removed | caught (1 FAIL) |
| frame labels not affine | z to z^2 | caught (4 FAILs) |
| lettered vertex record in lattice directions | label differences dropped | caught (2 FAILs) |
| lettered link records the complement | n to 1 - n | caught (1 FAIL) |
| flux sublattice read from fine parity | coarse to fine parity | caught (1 FAIL) |
| link endpoints taken as plaquettes | V to P | caught (exits on a lookup error) |

  Eleven of eleven defect mutants are caught, ten by a FAIL line and one
  by a nonzero exit.

- **Vacuity guard:** 9600 states and 1228800 site-state pairs are
  reported; each negative statement is checked in every state.
- **Budget:** 13 checks, stdout 2319 characters (ceiling 6000),
  about 57 s (ceiling 900 s), exact integer arithmetic.

## Verification

```bash
python3 scripts/static_ice_measure_nearest_neighbour_admissibility_needs_a_frame_source_2026_09_22.py
```

Expected summary line: `TOTAL: PASS=13 FAIL=0`; the runner exits nonzero
if any check fails. Cached output:
`logs/runner-cache/static_ice_measure_nearest_neighbour_admissibility_needs_a_frame_source_2026_09_22.txt`.

## Pre-landing correction record

Review in the current primary Codex session narrowed unsupported physical and
off-domain conclusions, made model premises explicit, and checked the source
arguments against the paired runner. Original author mutation counts above
are historical reports, not a separate review or a rerun by this session.
No subagents or audit verdicts were used.
