---
claim_id: relational_spiral_frames_are_locally_rigid_under_the_static_reading_nonlinear_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "For the declared Pythagorean angles on L=4 and L=5 boxes, the full static equations have linearized nullity five. Three global rotations and the two independent corner-axis turns supply five exact kernel vectors and a smooth five-parameter family of exact solutions. The implicit-function argument below identifies every sufficiently nearby solution with that family. Core values are a rotated spiral; each corner turn changes three outer neighbours while leaving the core unchanged. This is a local theorem near the specified spiral, for L=4,5 only. No neighbourhood radius, global rigidity, all-size result or extension to other angle sets is asserted. The runner checks rational points of the nonlinear families and their exact derivatives; the smooth family and local exhaustion follow from the source argument, not finite sampling."
upstream_dependencies:
  - minimal_axioms
  - relational_frames_in_one_qubit_spiral_records_under_possibility_covariance_bounded_theorem_note_2026-09-22
  - relational_spiral_frames_are_rigid_on_the_lattice_and_under_the_static_reading_but_flexible_and_amplified_under_the_sweep_bounded_theorem_note_2026-09-23
runner: scripts/relational_spiral_frames_locally_rigid_under_the_static_reading_nonlinear_2026_09_23.py
---

# Local nonlinear rigidity of static spirals on two finite boxes

**Date:** 2026-09-23
**Type:** bounded_theorem

## Result and scope

For the declared Pythagorean angles on L=4 and L=5 boxes, the full static equations have linearized nullity five. Three global rotations and the two independent corner-axis turns supply five exact kernel vectors and a smooth five-parameter family of exact solutions. The implicit-function argument below identifies every sufficiently nearby solution with that family. Core values are a rotated spiral; each corner turn changes three outer neighbours while leaving the core unchanged.

## Boundaries and non-claims

This is a local theorem near the specified spiral, for L=4,5 only. No neighbourhood radius, global rigidity, all-size result or extension to other angle sets is asserted. The runner checks rational points of the nonlinear families and their exact derivatives; the smooth family and local exhaustion follow from the source argument, not finite sampling.

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

- **Open PR 8691's spiral and angles.** b(x) = R_z(θ . x) b0 with
  (cos θ_j, sin θ_j) = (3/5, 4/5), (5/13, 12/13) and (8/17, 15/17).
- **Its static reading.** Each core site x completes from its
  back-neighbours with an axis n_b(x) and from its forward neighbours with
  an axis n_f(x). Here:
  - n_b . b = n_f . b = 0;
  - b(x - e_i) = R_nb(-θ_i) b(x);
  - b(x + e_i) = R_nf(θ_i) b(x);
  - values and axes are unit vectors.

  Near the spiral the assignment of angles to directions is the spiral's
  own.
- **Boxes.** Core sites have coordinates 1..L-2. Used sites are the core
  sites and their six neighbours.
- **The Rodrigues formula.**
  R_n(a) v = cos a v + sin a (n × v) + (1 - cos a)(n . v) n.



## Theorem — Local rigidity

For L=4 or L=5 with the declared angles, write the static system as F = 0 on the space of values and axes, with
n unknowns. At the spiral p:
- rank DF(p) = n - 5;
- the five kernel vectors are exact.

The map from SO(3) × (back corner turn) × (forward corner turn) to
records is smooth and sends the identity to p. Its image lies in F = 0.
Its derivative at the identity has rank 5, and its columns are the kernel
vectors. So near p the image is a 5-dimensional submanifold M inside
F = 0.

Choose n - 5 components of F with independent gradients at p. Their zero
set N is a 5-dimensional manifold near p, and it contains F = 0, which
contains M. A 5-dimensional submanifold of a 5-dimensional manifold is
open in it. So near p, M = N = {F = 0}.

The corner turns are free because each corner's three outer neighbours
lie in that corner's relation and in no other.


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
- [Companion result from PR #8717](RELATIONAL_SPIRAL_FRAMES_ARE_RIGID_ON_THE_LATTICE_AND_UNDER_THE_STATIC_READING_BUT_FLEXIBLE_AND_AMPLIFIED_UNDER_THE_SWEEP_BOUNDED_THEOREM_NOTE_2026-09-23.md)

The original author narrative and review history are recoverable from
the originating PR. Historical author mutation reports are not a substitute
for the current landing review. No new axiom or retained audit grade is adopted.

## Verification

```bash
python3 scripts/relational_spiral_frames_locally_rigid_under_the_static_reading_nonlinear_2026_09_23.py
```

The runner exits nonzero on a failed check. The fresh captured evidence is
`logs/runner-cache/relational_spiral_frames_locally_rigid_under_the_static_reading_nonlinear_2026_09_23.txt`. Its finite check results and resolution certificate
state the execution scope; analytic claims additionally require the proof above.
