---
claim_id: relational_letters_static_rigidity_needs_a_global_octant_site_and_line_orientations_leave_the_letters_flexible_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "On the side-two core, each of eight global octants has 12 aligned spirals; their union has 48. Exhausting all 4096 orientation fields of the twelve lattice lines gives 11136 distinct core records, only 48 spirals. Exactly 1300 fields admit records; a nonglobal field admits 108. The per-site class has 15024 records, and the inclusions global-octant \u2286 line-field \u2286 per-site are verified record by record.  Thus arbitrary line or site orientations do not guarantee rigidity for this core and these letters. The counts do not prove that every nonglobal field is flexible or that a global octant is necessary among all possible supplied structures. Only the declared seven-value planar support model and side-two core are exhausted. Values outside the core are free. No larger-window classification, unique necessary orientation supply, or physical interpretation is established."
upstream_dependencies:
  - minimal_axioms
  - relational_letters_under_the_static_reading_are_globally_rigid_exactly_for_sidon_angle_sets_bounded_theorem_note_2026-09-23
runner: scripts/relational_letters_static_rigidity_needs_a_global_octant_line_orientations_are_flexible_2026_09_23.py
---

# Finite orientation-field contrasts for seven-value core rigidity

**Date:** 2026-09-23
**Type:** bounded_theorem

## Result and scope

On the side-two core, each of eight global octants has 12 aligned spirals; their union has 48. Exhausting all 4096 orientation fields of the twelve lattice lines gives 11136 distinct core records, only 48 spirals. Exactly 1300 fields admit records; a nonglobal field admits 108. The per-site class has 15024 records, and the inclusions global-octant ⊆ line-field ⊆ per-site are verified record by record.

Thus arbitrary line or site orientations do not guarantee rigidity for this core and these letters. The counts do not prove that every nonglobal field is flexible or that a global octant is necessary among all possible supplied structures.

## Boundaries and non-claims

Only the declared seven-value planar support model and side-two core are exhausted. Values outside the core are free. No larger-window classification, unique necessary orientation supply, or physical interpretation is established.

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

- **Letters and completions.** The seven letters in the planar form, as in
  open PR 8743. At a core site with octant σ, the back neighbours are
  x − σ_i e_i and the forward neighbours x + σ_i e_i. The back
  differences and the forward differences must each be a common-sign
  permutation of the angles.
- **Readings.** Three ways of supplying σ:
  - a global octant;
  - a line-orientation field, with one sign for each of the 12 lines
    through the core;
  - an octant chosen freely at each site.
- **Search.** Core of side 2 on the side-4 box, one core value fixed,
  values outside the core free.



## Theorem — Orientation supply

Two facts come from the search:
- for each global octant, the records are exactly the aligned spirals;
- over all line fields, 11136 records occur, only 48 of them spirals.

Nesting follows from the definitions, and the runner also checks it:
- a line field assigns each site the octant of its lines, so its records
  satisfy the per-site reading;
- a global octant is a line field.


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
- [Companion result from PR #8743](RELATIONAL_LETTERS_UNDER_THE_STATIC_READING_ARE_GLOBALLY_RIGID_EXACTLY_FOR_SIDON_ANGLE_SETS_BOUNDED_THEOREM_NOTE_2026-09-23.md)

The original author narrative and review history are recoverable from
the originating PR. Historical author mutation reports are not a substitute
for the current landing review. No new axiom or retained audit grade is adopted.

## Verification

```bash
python3 scripts/relational_letters_static_rigidity_needs_a_global_octant_line_orientations_are_flexible_2026_09_23.py
```

The runner exits nonzero on a failed check. The fresh captured evidence is
`logs/runner-cache/relational_letters_static_rigidity_needs_a_global_octant_line_orientations_are_flexible_2026_09_23.txt`. Its finite check results and resolution certificate
state the execution scope; analytic claims additionally require the proof above.
