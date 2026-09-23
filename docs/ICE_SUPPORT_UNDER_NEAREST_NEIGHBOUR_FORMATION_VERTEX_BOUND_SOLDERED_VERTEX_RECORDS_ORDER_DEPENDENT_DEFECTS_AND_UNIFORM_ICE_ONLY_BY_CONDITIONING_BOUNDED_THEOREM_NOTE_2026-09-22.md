---
claim_id: ice_support_under_nearest_neighbour_formation_vertex_bound_soldered_vertex_records_order_dependent_defects_and_uniform_ice_only_by_conditioning_bounded_theorem_note_2026-09-22
claim_type: bounded_theorem
claim_scope: "Formation reading with the text's hole semantics, applied to the ice support of the landed spin-half cubic-ice notes (link occupations n in {0,1}, exactly 3 of the 6 links of each vertex occupied), with the superlattice vertex and link roles. For every nearest-neighbour rule and every reading, the link-first order makes a vertex's links independent, so P(ice at a vertex) <= 5/16; under the unsoldered reading the vertex-first order gives the same bound, since a direction-blind rule cannot coordinate a vertex's links. Under the soldered reading, vertex records of one of the 20 ice configurations hold the rule at a single vertex, with defect probability 0,0,0,0,1/8,3/8,11/16 as k = 0..6 links form first; on two vertices sharing a link the vertex-first order leaves the shared link unrecorded with probability 1/2 and the link-first order records both vertices with probability 25/256, both uniform on the 200 ice configurations conditional on no unrecorded site; on a 24-link plaquette a sweep order has no unrecorded site but weights the 10016 ice configurations 1/8000 or 1/12000. The uniform ice measure is a completed-record law only by conditioning. No rule, reading, order law or physical identification is adopted."

upstream_dependencies:
  - minimal_axioms
  - realized_state_primitive
  - covariant_nn_support_rules_gauss_law_as_glued_support_and_hole_statistics_bounded_theorem_note_2026-09-14
  - possibility_covariance_soldered_vs_unsoldered_cl30_invariant_rules_and_haar_fair_coin_bounded_theorem_note_2026-09-14
runner: scripts/ice_support_formation_nn_rules_vertex_bound_soldered_vertex_records_and_conditioning_2026_09_22.py
---

# Ice support under nearest-neighbour formation: the 5/16 vertex bound, soldered vertex records, order-dependent defects, and the uniform ice measure only by conditioning

**Date:** 2026-09-22
**Type:** bounded_theorem
**Campaign:** next-steps campaign after the TOE derivation campaign by
underdetermination witnesses. The landed spin-half cubic-ice notes
obtain Coulomb correlations as uniform averages over ice configurations
at the Rokhsar-Kivelson point of a supplied quantum Hamiltonian. The
previous blocks of this continuation showed that long-range record
statistics need order-sensitive formation or supports. This block asks
whether nearest-neighbour formation, read with the text's hole
semantics (open PR 8666), produces the ice support and its uniform
measure at all.

## Result up front

1. **No nearest-neighbour rule keeps the ice rule in every order.** Links
   are not neighbours of each other. So in the order that forms a vertex's
   six links first, they form with no formed neighbour and are
   independent, under every rule and every reading. The chance that
   exactly three are occupied is 20 p^3 (1-p)^3 <= 5/16.

2. **Under the unsoldered reading a vertex cannot coordinate its links.**
   Vertex first: the rule sees the vertex's record but not the bond
   direction, so the six links are exchangeable and independent given
   that record. The bound 5/16 holds again; by complete enumeration, the maximum over
   729 two-record rules is exactly 5/16. The ice rule fails with
   probability at least 11/16 at a single vertex in both extreme orders.

3. **Under the soldered reading a vertex can record which links to
   occupy.** A vertex that records one of the 20 ice configurations (a
   set of three bond directions) can tell each link its occupation.
   Vertex first, the links copy and the rule holds. With k of the six
   links formed first, the vertex has no consistent record, and is
   unrecorded, with probability 0, 0, 0, 0, 1/8, 3/8, 11/16 for
   k = 0..6. The formation order sets the defect probability.

4. **Shared links move the defects around.** On two vertices sharing a
   link, the vertex-first order leaves the shared link unrecorded with
   probability 1/2 (the two records disagree on it). The link-first
   order records both vertices only with probability 25/256 = (5/16)^2.
   Conditional on no unrecorded site, both orders give exactly the
   uniform law 1/200 on the window's 200 ice configurations.

5. **Defect-free orders exist, but they bias the ice measure.** On the
   24-link plaquette of four vertices, a sweep order (each vertex after
   the links shared with earlier vertices) never leaves a site
   unrecorded and reaches all 10016 ice configurations. Their masses are
   1/8000 or 1/12000 rather than the uniform 1/10016, because the
   closing vertex has 4 or 6 consistent records. A record statistic
   separates the two laws: the two plaquette links at the closing vertex
   agree with probability 62/125 under the sweep and 124/313 under the
   uniform ice measure.

6. **What this means for the photon lane.** The uniform ice measure
   behind the landed Coulomb correlations is the completed-record law of
   nearest-neighbour formation only when histories with unrecorded sites
   are discarded. That convention is not in the text (open PR 8666).
   Under the text, finished states carry unrecorded defects whose
   probability depends on the order law, or, in defect-free orders, a
   different ice measure. The established formation routes to the
   Coulomb phase use the soldered reading (item 2 blocks the link-first
   and vertex-first orders without soldering; other unsoldered orders are
   not classified), together with the order law (items 3-5) or joint
   formation units spanning the glued structure (formation-unit block,
   open PR 8643).
   These are the recorded decision groups, now with exact prices
   attached.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "the landed ice-support Coulomb correlations are uniform averages from a supplied quantum ground state; determine whether nearest-neighbour formation with the text's hole semantics produces the ice support and its uniform measure"
source_of_blocker_text: open_pr_8646_transverse_boundary_and_landed_cubic_ice_notes
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "carry into the re-assembly: the formation route to the Coulomb phase needs the soldered reading plus an order law or joint units, and otherwise leaves order-dependent defects; compute defect densities of covariant order laws on larger windows"
conditional_surface_status: "formation reading; text hole semantics; supplied superlattice roles and ice support; supplied vertex-record alphabet (20 ice configurations) under the soldered reading; declared orders"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "items 1-2 are short exact bounds valid for every rule; items 3-5 are exact enumerations on declared windows and orders"
```

## Premises and declared objects

The ice support in occupation form of the landed spin-half cubic-ice
notes, on the superlattice vertex and link roles of the landed
support-rule note: a vertex is the fine-lattice neighbour of its six
links, and links are not neighbours of each other. Formation reading of
Admissibility with the text's hole semantics: a site with no admissible
possibility carries no record, and formation continues. The soldered
vertex-record rule is supplied: vertex values are the 20 ice
configurations of its six bond directions, which rotate with positions.
A vertex takes a uniform consistent record, or none. A link copies the
occupation its formed vertices assign, takes a fair coin when none is
formed, and has no record when two formed vertices disagree. Windows
and orders are as declared in the runner.

## Prior art and what is new

- Landed spin-half cubic-ice notes (2026-09-03/04), for example
  `docs/SPIN_HALF_CUBIC_ICE_EXACT_RK_COULOMB_CORRELATIONS_AND_FINITE_QUBIT_PHOTON_PHASE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-09-03.md`:
  occupation qubits with exactly three of six links occupied, and
  Coulomb correlations as uniform averages at the Rokhsar-Kivelson point
  of a supplied Hamiltonian. New here: the same support under
  nearest-neighbour formation.
- Landed support-rule note (2026-09-14): superlattice roles and the
  parity support. New here: the integer (ice) support's formation.
- Open PRs 8663, 8664, 8666 (this continuation): order-blind formation
  has nearest-neighbour reach, and holes are unrecorded sites. Open PR
  8643: joint units dissolve holes. New here: exact prices for the ice
  support under each route.

## Theorem 1 — The link-first bound, every reading

For every nearest-neighbour rule, in any order that forms the six links
of a vertex before any of their other neighbours, each link forms with an
empty condition, so the six occupations are independent with the
one-site law. The probability that exactly three are occupied is
20 p^3 (1-p)^3, whose maximum over p in [0, 1] is 5/16 at p = 1/2
(checked on a grid of 65 values).

## Theorem 2 — The unsoldered vertex-first bound

Under the unsoldered reading, if a vertex forms first with record c and
its links follow with no other formed neighbour, each link's conditional
is the same for every direction. So the links are independent and
identically distributed given c, and P(ice) = E_c[20 p_c^3 (1-p_c)^3]
<= 5/16. Complete enumeration: the maximum over the 729 rules with a
two-valued vertex record and link probabilities in {0, 1/8, ..., 1} is
exactly 5/16.

## Theorem 3 — Soldered vertex records: defects, conflicts, sweeps

Exact enumerations on the declared windows. (a) One vertex: the vertex
is unrecorded with probability 0, 0, 0, 0, 1/8, 3/8, 11/16 when k = 0..6
of its links form first. (b) Two vertices sharing a link: vertex-first,
the shared link is unrecorded with probability 1/2; link-first, both
vertices are recorded with probability 25/256. Conditional on no
unrecorded site, the vertex-first records map one-to-one onto the 200
ice configurations of the window with uniform mass, and the link-first
survivors are exactly those 200 configurations. (c) Plaquette of four
vertices: the sweep order leaves no site unrecorded. Every outcome is a
consistent ice configuration and all 10016 are reached, with masses
1/8000 or 1/12000. The closing-vertex agreement statistic is 62/125
under the sweep and 124/313 under the uniform ice measure.

## No-Go Discipline Gate

The negative content is scoped. No nearest-neighbour rule keeps the ice
rule at a vertex with probability above 5/16 in the link-first order,
nor under the unsoldered reading in the vertex-first order.

- **N1 alternative routes.** Order laws beyond the declared ones, larger
  windows, joint formation units, other vertex alphabets and the parity
  support's orders are not classified here.
- **N2 wall independence.** Exact counting on declared windows; no
  Hamiltonian, clock or limit.
- **N3 hidden walls.** The ice support, the roles, the vertex-record
  alphabet and the orders are supplied; the text's hole semantics is the
  previous block's reading.
- **N4 residual matching.** The residual to a formation-based Coulomb
  phase is exactly: the soldered reading plus an order law or joint
  units, or acceptance of order-dependent defects.
- **N5 rhetoric audit.** Bounds and probabilities are exact; no claim
  about screening or long-distance behaviour is made.
- **N6 partial-closure paths.** Defect densities of covariant order laws
  on large windows, and joint units spanning the glued structure, are
  open continuations.
- **N7 steelman.** For formation: the sweep shows that defect-free
  formation of the ice support exists on open windows. Against it: the
  sweep's measure is not the uniform one, so the landed Coulomb averages
  are not its output, and a covariant order law must mix orders.
- **N8 cross-cycle echo.** The landed Coulomb results are cited and not
  re-derived; this block adds the formation layer they do not address.

## Falsifiers

- A nearest-neighbour rule and a link-first order with P(ice at a
  vertex) > 5/16, or an unsoldered rule exceeding 5/16 vertex-first,
  falsifies Theorems 1-2.
- Any listed defect probability, count (200, 10016) or mass failing its
  recomputation falsifies Theorem 3.

## Boundaries and non-claims

No rule, reading, order law, unit or physical identification is
adopted. The results cover the declared windows and orders; the defect
density of a covariant order law on large windows is not computed. The
landed Coulomb correlations remain valid as statements about the
uniform ice measure; this block concerns only whether formation
produces that measure. Nothing here grades, unlocks or audits any other
claim.

## Imports

Supplied support, roles, alphabet, windows and orders; the landed
cubic-ice notes cited for context. No audit grade, no new axiom, no new
primitive, no new comparator and no new framing is imported.

## Review record

- **Seat:** one Opus 5.5 seat; no subagents; runner and note by the same
  seat.
- **Independence sources:** (i) the two-vertex conditional laws compared
  with a direct enumeration of the window's ice configurations; (ii) the
  plaquette sweep outcomes checked one by one for consistency on all
  four shared links; (iii) the plaquette ice count computed by the
  internal-link factorisation and matched by the sweep's reach; (iv) the
  unsoldered bound checked by complete enumeration of a 729-rule family.
- **Mutation census** (caught means at least one FAIL line or a nonzero
  exit; the runner exits nonzero on any FAIL):

| mutation | substitution | result |
|---|---|---|
| ice count 3 of 6 to 2 of 6 | support changed | caught (6 FAILs) |
| bound grid exponent | 20 p^2 (1-p)^4 | caught (1 FAIL) |
| vertex ignores formed links | every record allowed | caught (1 FAIL) |
| agreement reads the same side | shared-link side swapped | caught after strengthening (1 FAIL) |
| link-first stars share nothing | shared link dropped | caught after strengthening (1 FAIL) |
| sweep closing vertex ignores one link | d unconstrained | caught (2 FAILs) |
| sweep second vertex reads the wrong side | +x for -x | caught after strengthening (1 FAIL) |
| unsoldered links misweighted | p^2 for p^3 | caught (1 FAIL) |

  Three mutants were first missed because their counts coincide by
  symmetry (C(5,3) = C(5,2), each direction occupied in half the
  configurations). The checks now compare sets and test every sweep
  outcome for consistency, and all eight are caught.
- **Vacuity guard:** every count is compared with an independently
  enumerated set; the sweep's non-uniformity is shown by the full set of
  masses and by a record statistic.
- **Budget:** 9 checks, stdout 1945 characters (ceiling 6000), about
  0.1 s (ceiling 900 s), exact Fractions; largest enumeration 2^11 link
  configurations.

## Verification

```bash
python3 scripts/ice_support_formation_nn_rules_vertex_bound_soldered_vertex_records_and_conditioning_2026_09_22.py
```

Expected summary line: `TOTAL: PASS=9 FAIL=0`; the runner exits nonzero
if any check fails. Cached output:
`logs/runner-cache/ice_support_formation_nn_rules_vertex_bound_soldered_vertex_records_and_conditioning_2026_09_22.txt`.
