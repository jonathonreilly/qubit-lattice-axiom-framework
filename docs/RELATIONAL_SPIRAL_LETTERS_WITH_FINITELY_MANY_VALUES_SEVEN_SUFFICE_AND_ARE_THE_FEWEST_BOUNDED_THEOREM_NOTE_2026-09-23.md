---
claim_id: relational_spiral_letters_with_finitely_many_values_seven_suffice_and_are_the_fewest_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "The three stated angle conditions suffice for unique completion of nondegenerate spiral inputs. The exact Q(sqrt(3)) runner checks the twelve-value example (30,60,150 degrees), input permutations and a rationally rotated witness; (30,90,150) gives a two-output contrast. The planar congruence rule agrees at all 27 tested twelve-value sites. For (1,2,4) modulo 7 it gives a unique output at all 64 sites of the tested 5-box.  A spiral decoder requiring six distinct nonzero signed step residues needs m-1 >= 6. Seven is achieved, and the admissible moduli through 12 are exactly 7,9,10,11,12. This is a minimum within that decoding class, not for all encodings. The ambiguity contrast does not establish necessity of every sufficient condition on degenerate inputs. Seven or twelve means distinct values within one spiral, with its rotated copies allowed on the real sphere; it is not a fixed finite SO(3)-invariant alphabet. Exact-field normalization is implemented only for the declared witnesses. The finite-box linear and nonlinear rank results for other angles are not imported here. No absolute roles, physical qubit storage capacity, or arbitrary-record uniqueness follows."
upstream_dependencies:
  - minimal_axioms
  - relational_frames_in_one_qubit_spiral_records_under_possibility_covariance_bounded_theorem_note_2026-09-22
runner: scripts/relational_spiral_letters_with_finitely_many_values_seven_suffice_2026_09_23.py
---

# Seven values suffice for the declared spiral decoding class

**Date:** 2026-09-23
**Type:** bounded_theorem

## Result and scope

The three stated angle conditions suffice for unique completion of nondegenerate spiral inputs. The exact Q(sqrt(3)) runner checks the twelve-value example (30,60,150 degrees), input permutations and a rationally rotated witness; (30,90,150) gives a two-output contrast. The planar congruence rule agrees at all 27 tested twelve-value sites. For (1,2,4) modulo 7 it gives a unique output at all 64 sites of the tested 5-box.

A spiral decoder requiring six distinct nonzero signed step residues needs m-1 >= 6. Seven is achieved, and the admissible moduli through 12 are exactly 7,9,10,11,12. This is a minimum within that decoding class, not for all encodings. The ambiguity contrast does not establish necessity of every sufficient condition on degenerate inputs.

## Boundaries and non-claims

Seven or twelve means distinct values within one spiral, with its rotated copies allowed on the real sphere; it is not a fixed finite SO(3)-invariant alphabet. Exact-field normalization is implemented only for the declared witnesses. The finite-box linear and nonlinear rank results for other angles are not imported here. No absolute roles, physical qubit storage capacity, or arbitrary-record uniqueness follows.

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

- **Open PR 8691's rule.** From back-neighbour values w_0, w_1, w_2 it
  reads the great circle with normal w_0 × w_1, normalised. It then tries
  every assignment σ of the angles and both orientations o. A point b is
  kept when w_i = R_{o n}(-θ_σ(i)) b for all i. The rule outputs the
  unique kept point, and records nothing otherwise.
- **Spiral records.** b(x) = R_z(θ . x) b0 with b0 = (1, 0, 0).
- **Exact arithmetic in Q(√3).** Pairs a + b√3 of Fractions. The cosines
  and sines of multiples of 30 degrees lie in this field, and so does
  every normal the rule needs here.



The sufficient conditions, modulo a full turn, are: (a) the three angles
are pairwise distinct modulo a half turn; (b) no nonidentity cyclic
permutation shifts all three by the same amount; (c) twice any angle is
not the sum of the other two. Bond decoding additionally requires all
six signed angles to be distinct and nonzero.

## Theorem 1 — Uniqueness

For a spiral, the three back-neighbours are rotations of b by -θ_i about
one axis. Another fit with assignment σ and the same orientation needs
θ_σ(i) - θ_i to be one constant. For a transposition this forces two
equal angles. For a 3-cycle it forces equal shifts: condition (b).

With the orientation reversed, the fit needs θ_i + θ_σ(i) to be one
constant:
- for the identity, two angles agree modulo 180 degrees (a);
- for a transposition, one angle is the mean of the other two (c);
- for a 3-cycle, two angles are equal.

The runner checks uniqueness directly at every site of the 4-box.



## Theorem 2 — Finite alphabets

A spiral whose angles are multiples of 360/m takes at most m values. The
frame reading needs six distinct signed angles. These are nonzero
residues modulo m closed under negation, so m - 1 ≥ 6. The runner lists
the m up to 12 with a valid triple.



## Theorem 3 — The planar reduction

For spiral inputs, w_0 and w_1 are distinct and not antipodal, by
condition (a). So the normal w_0 × w_1 is ±z, and every rotation the
rule tries is a rotation of the equator by a multiple of 360/m. A
candidate b = R(s θ_σ(0)) w_0 fits exactly when
angle(w_i) ≡ angle(b) - s θ_σ(i) (mod m) for all i, with s = ±1. The
runner checks that this reduction gives the same unique output as the
exact Q(√3) rule at all 27 sites of the twelve-value box. It then
applies the reduction to (1, 2, 4) × 360/7 on a 5-box: one output at
each of the 64 sites, seven values, and six distinct signed angles.


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

The original author narrative and review history are recoverable from
the originating PR. Historical author mutation reports are not a substitute
for the current landing review. No new axiom or retained audit grade is adopted.

## Verification

```bash
python3 scripts/relational_spiral_letters_with_finitely_many_values_seven_suffice_2026_09_23.py
```

The runner exits nonzero on a failed check. The fresh captured evidence is
`logs/runner-cache/relational_spiral_letters_with_finitely_many_values_seven_suffice_2026_09_23.txt`. Its finite check results and resolution certificate
state the execution scope; analytic claims additionally require the proof above.
