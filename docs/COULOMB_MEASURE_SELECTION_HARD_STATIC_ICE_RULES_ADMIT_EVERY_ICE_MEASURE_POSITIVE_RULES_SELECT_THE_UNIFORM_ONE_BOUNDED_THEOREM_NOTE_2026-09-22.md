---
claim_id: coulomb_measure_selection_hard_static_ice_rules_admit_every_ice_measure_positive_rules_select_the_uniform_one_bounded_theorem_note_2026-09-22
claim_type: bounded_theorem
claim_scope: "Static reading on the landed L = 2 torus (fine Z_4^3 with superlattice roles; 9600 ice states, 880 at zero flux). A hard ice rule (the soldered vertex records of open PR 8679, deterministic conditionals) is satisfied by every measure on the ice states: the uniform law, the zero-flux uniform law and a single state all have the same conditionals and differ (flux variance 76/25, 0, 0). A positive nearest-neighbour rule (vertex records over the 20 ice patterns, weight eps per vertex-link disagreement) is nearest-neighbour (a link's odds depend on its two vertex records; checked on 1440 perturbed configurations) and has link law proportional to prod_v A(p_v), with A = 1 + 9 eps^2 + 9 eps^4 + eps^6 on ice patterns and no eps^0 term otherwise. Given no charged vertex its law is exactly uniform on the 9600 ice states for every eps > 0, and P(no charged vertex) = 0.0957, 0.9508, 0.99949 at eps = 1/10, 1/100, 1/1000, with 1 - P about 513 eps^2. No rule, reading, limit or physical identification is adopted."

upstream_dependencies:
  - minimal_axioms
  - realized_state_primitive
  - spin_half_cubic_ice_exact_rk_coulomb_correlations_and_finite_qubit_photon_phase_bridge_bounded_theorem_note_2026-09-03
  - the_superlattice_role_pattern_is_a_next_nearest_neighbour_support_rule_over_roles_and_roles_are_not_record_values_bounded_theorem_note_2026-09-04
runner: scripts/coulomb_measure_selection_hard_static_rules_admit_every_ice_measure_positive_rules_select_the_uniform_one_2026_09_22.py
---

# What selects the Coulomb measure: hard static ice rules admit every ice measure; positive nearest-neighbour rules select the uniform one

**Date:** 2026-09-22
**Type:** bounded_theorem
**Campaign:** next-steps campaign after the TOE derivation campaign by
underdetermination witnesses. The landed equal-time Coulomb correlations
are uniform averages over ice states. The assembly's static route (open
PR 8648) rests on the landed ice note's supplied quantum Hamiltonian, an
open edge. Its nearest-neighbour admissibility needs a frame source (open
PR 8679). Formation gives directed ice instead (open PR 8687). This block
asks what, under the static reading, selects the uniform measure at all.

## Result up front

1. **A hard ice rule selects nothing.** Take the soldered vertex records
   of open PR 8679. In every one of the 9600 ice states, each site's
   value is a function of its six neighbours' values, so every
   conditional is a point mass. Any measure on the ice states therefore
   has the same conditionals and satisfies the same hard static rule.
   Three such measures differ visibly:
   - the uniform law: flux variance 76/25;
   - the zero-flux uniform law (880 states): flux variance 0;
   - a single state: flux variance 0, and no fluctuation at all.

   Laws produced by formation on ice supports, such as the directed ice
   of open PR 8687 on boxes, are admissible in the same way. The hard rule
   leaves the measure open.

2. **A positive rule is nearest-neighbour and has one law.** Let vertex
   records range over the 20 ice patterns, and give each state weight
   eps^m, where m is the number of (vertex, link) pairs on which a record
   and an occupation disagree.
   - A link's odds depend only on its two vertex records, and a vertex's
     law only on its six links (checked against the full weight on 1440
     perturbed configurations).
   - For eps > 0 every state has positive weight. A positive
     nearest-neighbour specification on a finite torus determines its
     joint law, by Brook's lemma.

3. **That law is uniform on the ice states and concentrates on them.**
   Summing each vertex's record gives a link law proportional to
   prod_v A(p_v).
   - A(p) = 1 + 9 eps^2 + 9 eps^4 + eps^6 when a vertex's links p form an
     ice pattern. Any other pattern has no eps^0 term.
   - Given no charged vertex, the law is exactly uniform on the 9600 ice
     states for every eps > 0. The zero-flux sector keeps its counting
     share, 880/9600.
   - P(no charged vertex) is 0.0957, 0.9508 and 0.99949 at eps = 1/10,
     1/100 and 1/1000, so it tends to 1. The shortfall is about 513
     eps^2, because by parity charges come in pairs.
   - The ice-state part of the transfer sum is computed separately and
     equals 9600 A^8 exactly.

4. **What this means for the photon lane.** Under the static reading,
   the equal-time law behind the landed Coulomb correlations is the
   eps -> 0 limit of a positive nearest-neighbour rule. The rule needs a
   frame source, soldered records here or coordinate letters as in open
   PR 8679, but no supplied Hamiltonian. The landed Hamiltonian is still
   needed for dynamics, the photon's time evolution. What selects the
   uniform measure is the positivity of the rule together with the ice
   limit, which is a property of the rule and not text. Hard rules and
   formation do not select it.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "the static route's Coulomb correlations rest on the landed ice note's supplied quantum Hamiltonian (open edge of open PR 8648); determine what selects the uniform ice measure as a static record law"
source_of_blocker_text: open_pr_8648_open_edges
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "narrow the supplied-Hamiltonian open edge to dynamics; record positivity and the ice limit as the selection of the equal-time law; test coordinate-letter versions and larger tori"
conditional_surface_status: "static reading; supplied superlattice roles; soldered vertex records over ice patterns; declared eps values; the landed uniform measure as the comparison"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "exact enumeration of the 9600 ice states and an exact rational transfer programme over the 2^24 link states; uniqueness by Brook's lemma for positive specifications"
```

## Premises and declared objects

- **The static reading** of the distribution sentence, as in open
  PRs 8646 and 8679.
- **The window.** The fine torus Z_4^3 with superlattice roles, which is
  the landed note's L = 2 torus.
- **The hard rule.** The soldered vertex records of open PR 8679.
- **The positive rule.**
  - Vertex records range over the 20 ice patterns.
  - Links carry occupations; plaquettes and cubes carry nothing.
  - A state has weight eps^m, where m counts vertex-link disagreements.
- **Flux** is counted as in open PR 8679.

## Prior art and what is new

- The landed spin-half cubic-ice note gives 9600 states, 880 at zero
  flux, and uniform RK averages.
- Open PR 8679 gives static admissibility with a frame source; open
  PR 8687 gives directed ice under formation.
- Standard: Gibbs specifications and Brook's lemma. A positive
  specification on a finite set of sites determines its joint law.
- New here: hard static ice rules leave the measure open, while a
  positive nearest-neighbour rule selects the uniform measure exactly
  conditional on no charge, and in the limit.

## Theorem 1 — Hard rules select nothing

In every ice state, each site's value is determined by its neighbours'
values (checked at all 64 sites in all 9600 states). So the conditional
of every site, given all others, is a point mass at its value, whatever
measure the states carry. The uniform, zero-flux uniform and one-state
laws share these conditionals, and their flux variances are 76/25, 0
and 0.

## Theorem 2 — The positive rule

The weight factorizes over (vertex, link) pairs. So a link's odds of
being occupied are eps raised to the net number of its two vertex
records that disagree with it, and a vertex's law is proportional to
eps^(distance to its links). Both are nearest-neighbour (checked against
the full weight).

Given the links, the records are independent. Summing them gives
prod_v A(p_v), with A(p) = sum over ice patterns S of
eps^(Hamming(S, p)). For ice patterns this is 1 + 9 eps^2 + 9 eps^4 +
eps^6, since 9 patterns sit at distance 2, 9 at distance 4 and 1 at
distance 6. Non-ice patterns have no eps^0 term.

A transfer programme over vertices gives Z(eps) exactly. It returns 9600
at eps = 0. Run over ice states only, it returns 9600 A^8, so the
conditional law on ice states is uniform.

## No-Go Discipline Gate

The negative content is scoped: hard static ice rules do not select a
measure on the ice states.

- **N1 alternative routes.** Other positive rules, coordinate-letter
  versions, and larger tori are not computed.
- **N2 wall independence.** Exact enumeration and a transfer programme;
  no dynamics.
- **N3 hidden walls.** The limit eps -> 0 is a declared property of the
  rule. Brook's lemma is standard.
- **N4 residual matching.** The static route's residual narrows: a frame
  source, a positive rule in the ice limit, and the Hamiltonian only for
  dynamics.
- **N5 rhetoric audit.** "Selects" means that the positive rule's law,
  conditioned on no charge, is the uniform measure, and in the limit
  without conditioning.
- **N6 partial-closure paths.** Letters instead of soldered records;
  larger tori; dynamics.
- **N7 steelman.** For the supplied Hamiltonian: it gives dynamics and
  the RK point. Against needing it for equal-time statistics: a positive
  static rule gives the same law. Both are recorded.
- **N8 cross-cycle echo.** Open PRs 8646, 8648, 8679 and 8687 and the
  landed note are cited; the counts are reproduced.

## Falsifiers

- An ice state where some site's value is not determined by its
  neighbours falsifies Theorem 1.
- A configuration where a link's odds depend on more than its vertex
  records, an ice pattern with a different A, or a transfer total at
  eps = 0 different from 9600 falsifies Theorem 2.

## Boundaries and non-claims

No rule, reading, limit or physical identification is adopted. The eps
values are declared. The window is the L = 2 torus. Nothing here
constructs dynamics. Nothing here grades, unlocks or audits any other
claim.

## Imports

The landed notes and open PRs are cited, and Brook's lemma is standard.
No audit grade, no new axiom, no new primitive, no new comparator and no
new framing is imported.

## Review record

- **Seat:** one Opus 5.5 seat; no subagents; runner and note by the same
  seat.
- **Independence sources:**
  - the ice-state count and the zero-flux count are compared with the
    landed note;
  - nearest-neighbour locality is checked against the full weight;
  - the ice part of the transfer sum is computed separately and compared
    with 9600 A^8.
- **Mutation census** (caught means at least one FAIL line or a nonzero
  exit; the runner exits nonzero on any FAIL):

| mutation | substitution | result |
|---|---|---|
| disagreement weight shifted | eps^d to eps^(d+1) | caught (2 FAILs) |
| ice patterns with 2 of 6 | 3 to 2 | caught (3 FAILs) |
| transfer starts from weight 2 | 1 to 2 | caught (2 FAILs) |
| odds read from one endpoint | ends cut | caught (1 FAIL) |
| flux sublattice from fine parity | coarse to fine parity | caught (1 FAIL) |
| weight counts agreements | != to == | caught (1 FAIL) |
| ice sum compared with seven vertices | A^8 to A^7 | caught (1 FAIL) |
| ice-only transfer keeps charged patterns | filter disabled | caught (2 FAILs) |
| vertex weight depends on its first link | extra term | caught (2 FAILs) |
| hard key drops a neighbour | six to five neighbours | missed; diagnosed non-defect (the ice count makes one neighbour redundant) |
| one-state law uses two states | one to two states | missed; diagnosed non-defect (any sub-support has the same conditionals) |

  Nine of nine defect mutants are caught; the two misses are diagnosed
  non-defects.

- **Vacuity guard:** 9600 states and 64 sites; 1440 perturbed
  configurations; a transfer over 2^24 link states at three values of
  eps.
- **Budget:** 6 checks, stdout 1245 characters (ceiling 6000), about
  1.5 s (ceiling 900 s), exact Fractions.

## Verification

```bash
python3 scripts/coulomb_measure_selection_hard_static_rules_admit_every_ice_measure_positive_rules_select_the_uniform_one_2026_09_22.py
```

Expected summary line: `TOTAL: PASS=6 FAIL=0`; the runner exits nonzero
if any check fails. Cached output:
`logs/runner-cache/coulomb_measure_selection_hard_static_rules_admit_every_ice_measure_positive_rules_select_the_uniform_one_2026_09_22.txt`.
