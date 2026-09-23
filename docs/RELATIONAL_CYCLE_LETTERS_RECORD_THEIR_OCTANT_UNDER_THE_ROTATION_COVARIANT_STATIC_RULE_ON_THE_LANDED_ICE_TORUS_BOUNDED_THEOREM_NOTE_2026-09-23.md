---
claim_id: relational_cycle_letters_record_their_octant_under_the_rotation_covariant_static_rule_on_the_landed_ice_torus_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "A supplied extension permits an independent raw sense per line and adjacent cycle phases in either direction. Its 24576 stars are closed under all 48 signed axis permutations, including the 24 proper rotations; the original 768 fixed-octant stars fail a quarter-turn control. Covariance does not uniquely select this extension.  Complete search on the side-four torus gives exactly 24576 records, equal to an independently generated set of oriented spirals (6 frames \u00d7 8 raw-sense choices \u00d7 8 orientations \u00d7 64 phases). Every record has a common frame, orientation and parity phase, and all eight octants occur. Exhaustive star testing gives (U); 48 sampled records also have singleton centre conditionals at all sites, against a mod-37 control with 864 shared stars. Exactly 768 records recover the fixed-octant/common-sense subclass. The open side-two-core search reaches 100000 full records and stops at that record limit: a lower bound only. The exact classification is only for the declared mod-211 cycles on the side-four torus. The open-box result means at least 100000, not an exhaustive count or a proof from execution of strictly more. Independent outer-face choices are allowed there. No unique axiomatic completion, universal rigidity or physical realization is asserted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/relational_cycle_letters_record_their_octant_under_the_rotation_covariant_static_rule_2026_09_23.py
---

# A covariant cycle extension records orientations on the side-four torus

**Date:** 2026-09-23
**Type:** bounded_theorem

## Result and scope

A supplied extension permits an independent raw sense per line and adjacent cycle phases in either direction. Its 24576 stars are closed under all 48 signed axis permutations, including the 24 proper rotations; the original 768 fixed-octant stars fail a quarter-turn control. Covariance does not uniquely select this extension.

Complete search on the side-four torus gives exactly 24576 records, equal to an independently generated set of oriented spirals (6 frames × 8 raw-sense choices × 8 orientations × 64 phases). Every record has a common frame, orientation and parity phase, and all eight octants occur. Exhaustive star testing gives (U); 48 sampled records also have singleton centre conditionals at all sites, against a mod-37 control with 864 shared stars. Exactly 768 records recover the fixed-octant/common-sense subclass. The open side-two-core search reaches 100000 full records and stops at that record limit: a lower bound only.

## Boundaries and non-claims

The exact classification is only for the declared mod-211 cycles on the side-four torus. The open-box result means at least 100000, not an exhaustive count or a proof from execution of strictly more. Independent outer-face choices are allowed there. No unique axiomatic completion, universal rigidity or physical realization is asserted.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "Conditional mathematics of the declared relational record model"
source_of_blocker_text: frontier_question
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Keep the declared scope; test extensions separately"
conditional_surface_status: "The stated domain, rule, boundaries and finite checks only"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "Conditional proof and exact finite witnesses; no retained grade asserted"
```

## Premises and declared objects

The chosen rule decodes each difference to (raw sense,cycle,phase).
For each axis its B/F differences must have the same raw sense and cycle,
and phases differing by ±1 mod 4. The three axes have distinct cycles;
their raw senses need not agree. The cycles are (19,31,132,29),
(108,43,194,77), (88,39,126,169), modulo 211. This explicitly supplied
rule is one covariant extension of the fixed-octant rule.

- **Admissibility** (minimal axioms): one fixed nearest-neighbour rule,
  covariant under lattice translations and proper cubic rotations.
- **Static reading** (open PR 8691), with the covariant rule in place of a
  supplied octant.
- **Planar form** (open PR 8729); the letters of open PR 8752.
- **Role pattern:** the parity vector x mod 2 up to its 8 global phases
  (landed role-pattern note).



## Theorem — Oriented spirals on the landed torus

For the declared letters, the static records of the covariant rule on the
torus of side 4 are exactly the oriented cycle spirals. The theorem is
established by complete search, cross-checked by generating the 24576
oriented spirals independently. On each line the phase walk may step up or
down at every site; a spiral walks one way at a constant rate. The search
shows that on this torus no walk turns and no line's sense or cycle
changes across parallel lines. Every record has the common frame, orientation and parity phase stated above.


## No-Go Discipline Gate and falsifiers

**N1 alternative routes / N3 hidden walls.** The negative claims use only the premises and domain above. Alternative
rules, boundary conditions, larger units, hidden shared data, physical
encodings and unstated parameter measures remain outside the result.
**N2 wall independence / N5 resolution.** The declared controls test which supplied conditions matter; a finite
search is exhaustive only where it completes below both record and work
caps. Witness prefixes and subsamples are labelled as such.

**N4 residuals / N6 partial closure.** Extending the explicit boundaries is
separate work; the result does not classify all possible repairs or routes.

**N7 strongest alternatives / N8 cross-result scope.** The positive controls
and companion results above remain available within their own hypotheses.
They do not inherit an exclusion from this note.

A counterexample meeting a theorem's stated hypotheses, a changed exact
count in an exhaustive search, or a failed declared control falsifies the
corresponding result. No other claim is graded, unlocked or audited here.

## Dependencies and provenance

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md)

The original author narrative and review history are recoverable from
the originating PR. Historical author mutation reports are not a substitute
for the current landing review. No new axiom or retained audit grade is adopted.

## Verification

```bash
python3 scripts/relational_cycle_letters_record_their_octant_under_the_rotation_covariant_static_rule_2026_09_23.py
```

The runner exits nonzero on a failed check. The fresh captured evidence is
`logs/runner-cache/relational_cycle_letters_record_their_octant_under_the_rotation_covariant_static_rule_2026_09_23.txt`. Its finite check results and resolution certificate
state the execution scope; analytic claims additionally require the proof above.
