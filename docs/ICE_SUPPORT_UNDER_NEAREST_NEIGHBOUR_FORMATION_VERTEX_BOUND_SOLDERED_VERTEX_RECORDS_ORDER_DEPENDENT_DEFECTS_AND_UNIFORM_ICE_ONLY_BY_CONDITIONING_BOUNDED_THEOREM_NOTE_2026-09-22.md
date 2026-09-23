---
claim_id: ice_support_under_nearest_neighbour_formation_vertex_bound_soldered_vertex_records_order_dependent_defects_and_uniform_ice_only_by_conditioning_bounded_theorem_note_2026-09-22
claim_type: bounded_theorem
claim_scope: "Formation reading with the supplied unrecorded-site convention, applied to the ice support of the landed spin-half cubic-ice notes (link occupations n in {0,1}, exactly 3 of the 6 links of each vertex occupied), with the superlattice vertex and link roles. For the supplied independent-draw protocol with a common empty-condition law, the link-first order makes a vertex's links independent, so P(ice at a vertex) <= 5/16; under the unsoldered reading the vertex-first order gives the same bound, under the independent-draw hypothesis. Under the soldered reading, vertex records of one of the 20 ice configurations hold the rule at a single vertex, with defect probability 0,0,0,0,1/8,3/8,11/16 as k = 0..6 links form first; on two vertices sharing a link the vertex-first order leaves the shared link unrecorded with probability 1/2 and the link-first order records both vertices with probability 25/256, both uniform on the 200 ice configurations conditional on no unrecorded site; on a 20-link plaquette a sweep order has no unrecorded site but weights the 10016 ice configurations 1/8000 or 1/12000. The two listed two-vertex orders produce uniform ice conditional on completion; the listed plaquette sweep is biased. Other rules and orders are not classified. No rule, reading, order law or physical identification is adopted."

upstream_dependencies:
  - minimal_axioms
runner: scripts/ice_support_formation_nn_rules_vertex_bound_soldered_vertex_records_and_conditioning_2026_09_22.py
---

# Ice support under nearest-neighbour formation: the 5/16 vertex bound, soldered vertex records, order-dependent defects, and conditional ice measures on the declared windows

**Date:** 2026-09-22
**Type:** bounded_theorem
The results below concern explicitly supplied finite formation models.
Their parameters, alphabets, orders and sampling laws are conditions of the
calculation, not additional framework premises.

## Result up front

1. **Independent link-first sampling has the 5/16 ice bound.** Links
   are not neighbours of each other. So in the order that forms a vertex's
   six links first, they form with no formed neighbour and are
   independent, under the stipulated identical independent link law. The chance that
   exactly three are occupied is 20 p^3 (1-p)^3 <= 5/16.

2. **Under the unsoldered reading a vertex cannot coordinate its links.**
   Vertex first: the rule sees the vertex's record but not the bond
   direction, so the six links are exchangeable and independent given
   that record. The bound 5/16 holds again; by complete enumeration, the maximum over
   729 two-record rules is exactly 5/16. The ice rule fails with
   probability at least 11/16 at a single vertex in both extreme orders.

3. **In the supplied abstract alphabet a vertex records which links to
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
   20-link plaquette of four vertices, a sweep order (each vertex after
   the links shared with earlier vertices) never leaves a site
   unrecorded and reaches all 10016 ice configurations. Their masses are
   1/8000 or 1/12000 rather than the uniform 1/10016, because the
   closing vertex has 4 or 6 consistent records. A record statistic
   separates the two laws: the two plaquette links at the closing vertex
   agree with probability 62/125 under the sweep and 124/313 under the
   uniform ice measure.

6. **The physical formation question stays open.** The two listed
   two-vertex protocols give uniform conditional ice; the particular plaquette
   sweep is biased. This does not prove that conditioning is the only route to
   uniform ice. Other sequential rules, orders and joint draws remain open.
   Vertex labels here are abstract 20-state records; an equivariant encoding
   into the one-qubit possibility domain is a separate unproved condition.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "determine the stated conditional finite-model results without selecting a physical formation law"
source_of_blocker_text: frontier_question
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "test extensions outside the declared finite models; a physical downstream consumer is not yet established"
conditional_surface_status: "formation reading; supplied unrecorded-site convention; supplied superlattice roles and ice support; supplied vertex-record alphabet (20 ice configurations) under the soldered reading; declared orders"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "items 1-2 are exact bounds in the stated product-law model; items 3-5 are exact enumerations on declared windows and orders"
```

## Premises and declared objects

The [framework axioms](MINIMAL_AXIOMS_2026-06-29.md) do not choose the
sampling process studied here. Sequential draws use the declared conditional
law given the previously formed configuration, with fresh randomness at each
step; a chosen order is external to those draws. Correlated joint draws and
adaptive orders are separate models. Skipping a failed attempt and continuing,
or dropping its whole history, are supplied alternatives. Neither convention
follows from unreadability alone.


The ice support in occupation form of the landed spin-half cubic-ice
notes, on the superlattice vertex and link roles of the landed
support-rule note: a vertex is the fine-lattice neighbour of its six
links, and links are not neighbours of each other. Formation reading of
Admissibility with the supplied unrecorded-site convention: a site with no admissible
possibility carries no record, and formation continues. The soldered
vertex-record rule is supplied: vertex values are the 20 ice
configurations of its six bond directions, which rotate with positions.
A vertex takes a uniform consistent record, or none. A link copies the
occupation its formed vertices assign, takes a fair coin when none is
formed, and has no record when two formed vertices disagree. Windows
and orders are as declared in the runner.

## Relation to earlier work

This packet states its supplied models and finite calculations directly.
Earlier campaign comparisons are historical motivation, not imported proof,
physical authority, or an adopted formation law.

## Theorem 1 — The link-first bound, every reading

For every rule in the supplied independent-draw model, in any order that forms the six links
of a vertex before any of their other neighbours, each link forms with an
empty condition, so the six occupations are independent with the
one-site law. The probability that exactly three are occupied is
20 p^3 (1-p)^3, whose maximum over p in [0, 1] is 5/16 at p = 1/2
because p(1-p) <= 1/4. The grid of 65 values is a finite control.

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

The negative scope is only the explicitly stated finite-model implication or
independent-clock bound. No general physical formation exclusion is claimed.

**N1 — Five distinct challenges.** Each is ATTEMPTED by the local argument
or the named finite computation, with its outcome kept explicit:

- **Independent link-first draws (ATTEMPTED):** 20[p(1-p)]^3<=5/16 proves the continuous bound.
- **Independent centre broadcast (ATTEMPTED):** a mixture of identical Bernoulli product laws obeys the same pointwise bound.
- **Abstract directional labels (ATTEMPTED):** the supplied 20-state protocol attains zero defects with the vertex first, outside the unsoldered broadcast restriction.
- **Shared-link compatibility (ATTEMPTED):** the two-vertex enumeration gives the conflict and conditional uniformity values.
- **Plaquette sweep (ATTEMPTED):** the particular sweep avoids defects but has two distinct outcome masses; other rules and orders are not excluded.

**N2 — Conditions.** The stated alphabet, sampling law and domain jointly
specify this model; no theorem counting independent physical walls is asserted.
Changing one condition does not automatically supply the other conditions.
Relations between alternative physical choices remain unclassified.

**N3 — Hidden-condition scan.** Fresh sequential randomness, finite supported
alphabets where used, declared orders, and the particular failure convention
are supplied conditions. No framework grant for them is claimed. Physical
encodings of abstract role labels remain separate from the finite calculations.

**N4 — Residual matching.** All negative implications used here are proved in
this note on the named domain. Historical comparisons are not invoked as
negative witnesses; no external residual is declared closed by analogy.

**N5 — Resolution.** The runner checks the finite elements/sites/windows
listed in its output. Universal implications are the source proofs; infinite
lattice formation, spectral modes and untested block correlations are not
executed or inferred from a finite sample.

**N6 — Partial routes.** Other alphabets, joint or correlated draws, adaptive
orders, retry conventions and other failure handling are not ruled out. No
new axiom is declared necessary. Scale and kinetic-form primitives have no
role in this finite calculation; they are not classified as missing inputs.

**N7 — Steelman.** A different process can evade a product-law bound by shared
randomness, evade an order comparison by conditioning on completion, or evade
a finite-support constancy statement by varying only off the reached support.
These are concrete reasons not to promote this packet to a physical no-go.
The result is restricted to the model whose hypotheses the proof actually uses.

**N8 — Cross-packet check.** The related formation packets distinguish dropped
histories, holes retained as absent sites, directional alphabets and joint
units. Those distinctions are preserved here. Neither a historical campaign
label nor a previous bounded conclusion grants a general exclusion.

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

## Author check record (original proposal)

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

## Landing review correction

Serial source review in one Codex session under the owner's no-subagent
instruction narrowed physical interpretations to supplied model conditions.
Original author check reports above are historical; they do not certify these
corrections. Current source-bound executions and independent controls are
recorded in the combined landing evidence. No independent audit is claimed.

## Verification

```bash
python3 scripts/ice_support_formation_nn_rules_vertex_bound_soldered_vertex_records_and_conditioning_2026_09_22.py
```

Expected summary line: `TOTAL: PASS=9 FAIL=0`; the runner exits nonzero
if any check fails. Cached output:
`logs/runner-cache/ice_support_formation_nn_rules_vertex_bound_soldered_vertex_records_and_conditioning_2026_09_22.txt`.
