---
claim_id: coulomb_measure_selection_hard_static_ice_rules_admit_every_ice_measure_positive_rules_select_the_uniform_one_bounded_theorem_note_2026-09-22
claim_type: bounded_theorem
claim_scope: "On the fine Z_4^3 torus, all 9600 hard ice states have each site's record determined by its neighbours. Every probability measure on this finite support is compatible with the same deterministic local specification, on its own positive-probability conditioning events. Uniform and zero-flux-uniform laws differ: their flux second moments are 76/25 and 0; a point mass is a third compatible law.  The supplied positive weight eps^m, eps>0, counts vertex-link disagreements. It has nearest-neighbour single-site conditionals and is the unique full-support finite joint law with those conditionals. After summing vertex records, conditioning the link pattern to satisfy ice gives exactly the uniform law for every eps>0. As eps tends to zero the finite marginal concentrates on ice. Exact partition calculations at eps=1/10,1/100,1/1000 check this construction; the rounded ratio near 513 at the last value is a finite observation, not a proved asymptotic coefficient. The positive weight is an additional supplied model. Unconditioned link patterns are not uniform ice at positive eps. Hard specifications impose no conditional law at zero-probability conditioning events. No Coulomb phase, infinite-volume selection, or minimal-axiom adoption follows."
upstream_dependencies:
  - static_ice_measure_nearest_neighbour_admissibility_needs_a_frame_source_soldered_vertex_records_or_coordinate_letters_bounded_theorem_note_2026-09-22
  - minimal_axioms
runner: scripts/coulomb_measure_selection_hard_static_rules_admit_every_ice_measure_positive_rules_select_the_uniform_one_2026_09_22.py
---

# Finite hard ice specifications and a positive joint-weight selection

**Date:** 2026-09-23
**Type:** bounded_theorem

## Result and scope

On the fine Z_4^3 torus, all 9600 hard ice states have each site's record determined by its neighbours. Every probability measure on this finite support is compatible with the same deterministic local specification, on its own positive-probability conditioning events. Uniform and zero-flux-uniform laws differ: their flux second moments are 76/25 and 0; a point mass is a third compatible law.

The supplied positive weight eps^m, eps>0, counts vertex-link disagreements. It has nearest-neighbour single-site conditionals and is the unique full-support finite joint law with those conditionals. After summing vertex records, conditioning the link pattern to satisfy ice gives exactly the uniform law for every eps>0. As eps tends to zero the finite marginal concentrates on ice. Exact partition calculations at eps=1/10, 1/100, 1/1000 check this construction; the rounded ratio near 513 at the last value is a finite observation, not a proved asymptotic coefficient.

## Boundaries and non-claims

The positive weight is an additional supplied model. Unconditioned link patterns are not uniform ice at positive eps. Hard specifications impose no conditional law at zero-probability conditioning events. No Coulomb phase, infinite-volume selection, or minimal-axiom adoption follows.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "Conditional finite ice measures, formation and supplied transfer models"
source_of_blocker_text: frontier_question
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Preserve finite hypotheses and test extensions separately"
conditional_surface_status: "The declared model, order, records and numerical tolerances only"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "Conditional mathematics and bounded computation; no retained grade asserted"
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


## Theorem 1 — Hard rules select nothing

In every ice state, each site's value is determined by its neighbours'
values (checked at all 64 sites in all 9600 states). So the conditional
of every site, given all others, is a point mass at its value, on every positive-probability conditioning event of any
measure supported on these states. The deterministic local specification
can be chosen identically, including arbitrary compatible values at null events. The uniform, zero-flux uniform and one-state
laws share these conditionals, and the uniform and zero-flux laws have flux second moments 76/25 and 0.
A point mass has zero variance regardless of its flux value.


## Theorem 2 — The positive rule

The weight factorizes over (vertex, link) pairs. So a link's odds of
being occupied are eps raised to (m_occupied - m_empty), summing disagreements
with the two vertex records, and a vertex's law is proportional to
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


For eps>0 all states of the finite product alphabet have positive weight.
Single-coordinate changes connect that state space; their conditional odds
fix every ratio of joint probabilities. Normalization therefore fixes the
full-support joint law uniquely. The finite partition polynomial has
constant term 9600 and all non-ice link patterns have zero constant term;
this proves concentration as eps tends to zero.

## No-go discipline and falsifiers

Negative claims concern only the stated fixed models and completed searches.
Alternative records, hidden state, adaptive orders, larger units, different
rules and different boundary conditions require separate tests. Caps must
not bind for an exhaustive verdict. Finite spectral patterns do not prove
infinite-cross-section physics. A counterexample under the exact hypotheses,
a failed independent count, or a failed stated control falsifies its result.
No other claim is graded, unlocked or audited here.

## Dependencies and provenance

- [Landed companion from PR #8679](STATIC_ICE_MEASURE_NEAREST_NEIGHBOUR_ADMISSIBILITY_NEEDS_A_FRAME_SOURCE_SOLDERED_VERTEX_RECORDS_OR_COORDINATE_LETTERS_BOUNDED_THEOREM_NOTE_2026-09-22.md)

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md)

Original context and author review history remain recoverable from the
originating PR. Historical mutation claims are not current review evidence.
The landing review preserves conditional proofs and narrows unsupported
extensions; no new axiom, primitive or audit grade is adopted.

## Verification

```bash
python3 scripts/coulomb_measure_selection_hard_static_rules_admit_every_ice_measure_positive_rules_select_the_uniform_one_2026_09_22.py
```

The runner exits nonzero on failure. Its fresh captured cache is
`logs/runner-cache/coulomb_measure_selection_hard_static_rules_admit_every_ice_measure_positive_rules_select_the_uniform_one_2026_09_22.txt`.
Analytic statements require the proofs above in addition to finite checks.
