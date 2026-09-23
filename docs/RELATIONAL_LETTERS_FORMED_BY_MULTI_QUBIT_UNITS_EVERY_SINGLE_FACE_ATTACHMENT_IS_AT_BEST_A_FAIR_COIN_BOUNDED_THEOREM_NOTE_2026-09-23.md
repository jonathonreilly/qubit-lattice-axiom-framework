---
claim_id: relational_letters_formed_by_multi_qubit_units_every_single_face_attachment_is_at_best_a_fair_coin_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "In the declared planar spiral model, a 2x2x2 unit attaching through one face cannot distinguish the two continuation signs under both internal-circle covariance and proper lattice covariance. The reversal/half-turn argument is checked on 144 views (24 proper orientations, two circle orientations, three axes). Each permitted continuation has conditional probability at most 1/2.  Face-connected growth from one seed reaching n units along each axis has at least 3(n-1) single-face attachments; corner growth has exactly that many. With the conditional locality premise, the registration probability is at most 2^(-3(n-1)). For the tested 3x3x3 unit grid, the fresh fair coin attains 1/64 for each of 48 seed patterns. Controls breaking one covariance register 12 and 6 patterns; a two-layer read registers all 48 and lies outside the declared nearest-neighbour input. The product bound assumes sequential face-connected growth from one seed, and at each attachment the conditional law given the whole past depends only on its local input. Fresh draws realize the attaining example; shared hidden randomness is excluded. A first span extension has at most one occupied face, and face connectivity supplies that face; one such event cannot first extend two axes. These assumptions are supplied, not consequences of covariance. No exclusion of all bounded units, seed schemes, or physical multi-qubit formation is claimed."
upstream_dependencies:
  - minimal_axioms
  - relational_frames_in_one_qubit_spiral_records_under_possibility_covariance_bounded_theorem_note_2026-09-22
  - relational_spiral_letters_with_finitely_many_values_seven_suffice_and_are_the_fewest_bounded_theorem_note_2026-09-23
runner: scripts/relational_letters_multi_qubit_units_single_face_attachment_is_a_fair_coin_2026_09_23.py
---

# A single-face symmetry bound for local joint-unit formation

**Date:** 2026-09-23
**Type:** bounded_theorem

## Result and scope

In the declared planar spiral model, a 2x2x2 unit attaching through one face cannot distinguish the two continuation signs under both internal-circle covariance and proper lattice covariance. The reversal/half-turn argument is checked on 144 views (24 proper orientations, two circle orientations, three axes). Each permitted continuation has conditional probability at most 1/2.

Face-connected growth from one seed reaching n units along each axis has at least 3(n-1) single-face attachments; corner growth has exactly that many. With the conditional locality premise, the registration probability is at most 2^(-3(n-1)). For the tested 3x3x3 unit grid, the fresh fair coin attains 1/64 for each of 48 seed patterns. Controls breaking one covariance register 12 and 6 patterns; a two-layer read registers all 48 and lies outside the declared nearest-neighbour input.

## Boundaries and non-claims

The product bound assumes sequential face-connected growth from one seed, and at each attachment the conditional law given the whole past depends only on its local input. Fresh draws realize the attaining example; shared hidden randomness is excluded. A first span extension has at most one occupied face, and face connectivity supplies that face; one such event cannot first extend two axes. These assumptions are supplied, not consequences of covariance. No exclusion of all bounded units, seed schemes, or physical multi-qubit formation is claimed.

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

- **Relational spiral letters.** Values on one great circle with neighbour
  steps from the angles (30, 60, 150) degrees. The planar form uses angles
  modulo 12 in units of 30 degrees; for spiral inputs every fit is a
  congruence (open PR 8729).
- **Covariance.** The rule commutes with rotations of the sphere,
  including the reversal of a great circle. It also commutes with proper
  rotations of the lattice, including the half turn about a growth axis.
- **Units.** Blocks of 2 x 2 x 2 sites, formed jointly. The first unit
  carries the spiral pattern under one of the 24 proper lattice
  orientations and either circle orientation. Later units attach through
  faces.
- **Locality.** A unit's law depends only on its formed neighbours, the
  formed sites adjacent to its sites. This is the unit form of the local
  formation criterion (open PRs 8715, 8720) and matches the lone child of
  open PR 8691.
- **Growth.** Corner growth over an n x n x n grid of units. A unit with
  two or three formed faces reads the step along each growth axis from
  another formed face. A unit with one formed face takes its step from
  the rule under test.



## Theorem 1 — The fair-coin bound

For a face view F and a step s, let U_s(F) be the continuation that adds
s per layer. Let P_F be the rule's law given the view F. Let h be the
half turn about the growth axis. Let ρ be the reversal of the circle
followed by a rotation of the circle by c = 2A0 + α + β.

- The half turn maps F to hF and U_s(F) to U_s(hF). So
  P_hF(U_s(hF)) = P_F(U_s(F)).
- The rotation ρ also maps F to hF, but it maps U_s(F) to U_-s(hF). So
  P_hF(U_-s(hF)) = P_F(U_s(F)).

So at the view hF the continuations with steps s and -s are equally
likely. Every view is hF for some pattern, and the half-turned pattern
keeps the step. The correct step t is ±θ with θ in {1, 2, 5}, which is
never its own negative modulo 12. So the correct continuation has
probability at most 1/2, and a deterministic law would need t = -t.



## Theorem 2 — Attachments

Take a unit that extends the formed region's span along an axis: it
reaches a new maximum or a new minimum there. Every formed unit lies
strictly on one side of it along that axis. So it can touch the formed
region only through the face on that side. Reaching n units along each
axis therefore takes at least n - 1 such attachments per axis. Each is
right with probability at most 1/2 given that everything before it is
right. By the chain rule, registration has probability at most
2^(-3(n - 1)).


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
- [Companion result from PR #8691](RELATIONAL_FRAMES_IN_ONE_QUBIT_SPIRAL_RECORDS_UNDER_POSSIBILITY_COVARIANCE_BOUNDED_THEOREM_NOTE_2026-09-22.md)
- [Companion result from PR #8729](RELATIONAL_SPIRAL_LETTERS_WITH_FINITELY_MANY_VALUES_SEVEN_SUFFICE_AND_ARE_THE_FEWEST_BOUNDED_THEOREM_NOTE_2026-09-23.md)

The original author narrative and review history are recoverable from
the originating PR. Historical author mutation reports are not a substitute
for the current landing review. No new axiom or retained audit grade is adopted.

## Verification

```bash
python3 scripts/relational_letters_multi_qubit_units_single_face_attachment_is_a_fair_coin_2026_09_23.py
```

The runner exits nonzero on a failed check. The fresh captured evidence is
`logs/runner-cache/relational_letters_multi_qubit_units_single_face_attachment_is_a_fair_coin_2026_09_23.txt`. Its finite check results and resolution certificate
state the execution scope; analytic claims additionally require the proof above.
