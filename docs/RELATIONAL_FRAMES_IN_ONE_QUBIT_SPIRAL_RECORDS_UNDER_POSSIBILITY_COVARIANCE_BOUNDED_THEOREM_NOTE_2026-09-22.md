---
claim_id: relational_frames_in_one_qubit_spiral_records_under_possibility_covariance_bounded_theorem_note_2026-09-22
claim_type: bounded_theorem
claim_scope: "For the three declared Pythagorean angles, exact rational spiral witnesses are stationary under the unique-completion rule. Angle differences encode bond labels relative to a choice of great-circle normal; permuting the three inputs preserves the output. A nontrivially rotated witness checks covariance, while the general covariance proof uses the equivariance of dot products, cross products and Rodrigues rotations.  A lone-child conditional law invariant under the full stabilizer of its parent has no atoms away from the two poles. After two nonantipodal formed values fix a candidate spiral plane and finitely many angle assignments, a further lone child has probability zero of hitting those finitely many required nonpolar targets. This does not exclude the initial two-site formation: a uniform draw on a permitted latitude can create that pair with probability one. The conceptual domain is the full real unit sphere; rational points are exact witnesses, not a rotation-closed state space. Conditional draws depend only on the actual formed neighbours, with no hidden shared orientation or memory. The zero-probability conclusion requires an additional lone-child event after the candidate plane has been fixed. The runner's bond decoder is supplied the normal (or its rotated image); it does not independently reconstruct that normal or an absolute frame/role phase. No operational encoding into distinguishable qubit states is established."
upstream_dependencies:
  - minimal_axioms
runner: scripts/relational_frames_in_one_qubit_spiral_records_under_possibility_covariance_2026_09_22.py
---

# Spiral records, relational frames, and a conditional lone-child obstruction

**Date:** 2026-09-23
**Type:** bounded_theorem

## Result and scope

For the three declared Pythagorean angles, exact rational spiral witnesses are stationary under the unique-completion rule. Angle differences encode bond labels relative to a choice of great-circle normal; permuting the three inputs preserves the output. A nontrivially rotated witness checks covariance, while the general covariance proof uses the equivariance of dot products, cross products and Rodrigues rotations.

A lone-child conditional law invariant under the full stabilizer of its parent has no atoms away from the two poles. After two nonantipodal formed values fix a candidate spiral plane and finitely many angle assignments, a further lone child has probability zero of hitting those finitely many required nonpolar targets. This does not exclude the initial two-site formation: a uniform draw on a permitted latitude can create that pair with probability one.

## Boundaries and non-claims

The conceptual domain is the full real unit sphere; rational points are exact witnesses, not a rotation-closed state space. Conditional draws depend only on the actual formed neighbours, with no hidden shared orientation or memory. The zero-probability conclusion requires an additional lone-child event after the candidate plane has been fixed. The runner's bond decoder is supplied the normal (or its rotated image); it does not independently reconstruct that normal or an absolute frame/role phase. No operational encoding into distinguishable qubit states is established.

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

The angles have (cos,sin) = (3/5,4/5), (5/13,12/13), (8/17,15/17).
The conceptual rule takes three unit-sphere inputs. If the first two are
collinear or the third is outside their plane it rejects. Otherwise it
normalizes their cross product, tries both normal signs and all six angle
assignments, and returns the unique candidate obtained by rotating each
input through its assigned angle; zero or multiple candidates reject.
The rational implementation evaluates only the stated exact witnesses.
A spiral is b(x)=R_n(sum_i theta_i x_i)b0, with b0 perpendicular to n.

The internal action rotates the real Bloch sphere and all values at once.
Covariance R(h.config)=h_*R(config) is a declared mathematical premise;
it is not inferred from the finite rational witness domain.

Declared objects:
- real Bloch-sphere points, with rational exact witnesses;
- the three Pythagorean angles and the spiral records built from them;
- the spiral rule;
- the sweep and the static reading;
- first formations with lone children.



## Theorem 1 — Spiral records are stationary and carry the frame

The rule's great circle is the unit normal of w_0 x w_1. It is rational
here because the angle differences have rational sines. The rule checks
all six assignments and both orientations, and exactly one candidate
survives. That uniqueness uses the distinctness of the six signed angles
and the plaquette lemma, checked over 81 cases.

On the box, every site with three back-neighbours equals the rule's
output. This holds for the spiral and for the rotated spiral, which
checks one nontrivial rotation of the sphere. The output
does not change when the inputs are permuted.

Given a common choice of great-circle normal, signed angle differences
decode the six bond labels. The runner supplies this normal.



## Theorem 2 — First formations

Let a lone child's only formed neighbour have value p. Possibility
covariance makes the child's law invariant under rotations about p, so
its atoms lie in {p, -p}. The rotation of the whole spiral by a
Pythagorean angle about p is again a stationary spiral: it agrees at the
parent and differs at the child (checked). The required child values are
never at the poles (checked). Once two nonantipodal formed values fix finitely many candidate spiral
planes/assignments, each further lone child has finitely many required
nonpolar targets. Conditional locality and stabilizer invariance give
probability zero to each; a finite union still has probability zero.
This does not forbid the first nonpolar pair.


General covariance follows because cross products, normalization and
Rodrigues rotations commute with every proper internal rotation. Trying
all assignments and both normal signs makes the output set independent
of the input ordering. A nonpolar atom of an SO(2)-invariant measure would
have infinitely many disjoint equal-mass rotated atoms, so cannot occur.

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
python3 scripts/relational_frames_in_one_qubit_spiral_records_under_possibility_covariance_2026_09_22.py
```

The runner exits nonzero on a failed check. The fresh captured evidence is
`logs/runner-cache/relational_frames_in_one_qubit_spiral_records_under_possibility_covariance_2026_09_22.txt`. Its finite check results and resolution certificate
state the execution scope; analytic claims additionally require the proof above.
