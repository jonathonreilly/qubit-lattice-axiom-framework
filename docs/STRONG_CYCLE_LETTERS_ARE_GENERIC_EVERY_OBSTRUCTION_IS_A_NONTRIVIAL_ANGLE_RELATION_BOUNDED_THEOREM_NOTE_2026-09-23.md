---
claim_id: strong_cycle_letters_are_generic_every_obstruction_is_a_nontrivial_angle_relation_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "Three zero-sum four-angle cycles have nine free circle parameters. The symbolic check finds 135 sign-normalized nonzero decoding relation vectors and 3645 nonzero nonstraight-square relation vectors from 73344 nonstraight configurations. It also verifies that all 24576 symbolic neighbour-class five-tuples differ. Thus failure of decoding, mixed-sign straightness or (U) lies in a finite union of nontrivial character kernels. Its complement has full measure in this supplied nine-torus; strong letters with (U) are generic there.  The symbolic normalization only identifies v with -v and does not divide out integer factors. For uniform parameters over F_p, a fixed relation vanishes with probability 1/p only if its coefficient vector remains nonzero modulo p. The runner separately samples sixty sets at each of three moduli with seeded draws of distinct nonzero entries within each triple. Those draws are conditioned samples, not uniform on F_p^9. The reproducible successful counts 1,34,56 and the factor-four comparison are empirical; 135+3645 omits (U) and is not a theorem about total failure probability. Genericity is relative to the supplied continuous angle parameterization, not a physical distribution, selection mechanism or tuning measure. For (U), collision requires simultaneous equality of five forms; the bad set is contained in the finite union used in the proof, not necessarily equal to it. Small primes can annihilate nonzero integer coefficient vectors. Strong retains its prior definition; (U) is additional."
upstream_dependencies:
  - minimal_axioms
  - strong_cycle_letters_record_frame_and_roles_under_the_rotation_covariant_rule_on_every_window_bounded_theorem_note_2026-09-23
runner: scripts/strong_cycle_letters_are_generic_every_obstruction_is_a_nontrivial_angle_relation_2026_09_23.py
---

# Generic strong cycle angles with neighbour uniqueness in the supplied parameter space

**Date:** 2026-09-23
**Type:** bounded_theorem

## Result and scope

Three zero-sum four-angle cycles have nine free circle parameters. The symbolic check finds 135 sign-normalized nonzero decoding relation vectors and 3645 nonzero nonstraight-square relation vectors from 73344 nonstraight configurations. It also verifies that all 24576 symbolic neighbour-class five-tuples differ. Thus failure of decoding, mixed-sign straightness or (U) lies in a finite union of nontrivial character kernels. Its complement has full measure in this supplied nine-torus; strong letters with (U) are generic there.

The symbolic normalization only identifies v with -v and does not divide out integer factors. For uniform parameters over F_p, a fixed relation vanishes with probability 1/p only if its coefficient vector remains nonzero modulo p. The runner separately samples sixty sets at each of three moduli with seeded draws of distinct nonzero entries within each triple. Those draws are conditioned samples, not uniform on F_p^9. The reproducible successful counts 1,34,56 and the factor-four comparison are empirical; 135+3645 omits (U) and is not a theorem about total failure probability.

## Boundaries and non-claims

Genericity is relative to the supplied continuous angle parameterization, not a physical distribution, selection mechanism or tuning measure. For (U), collision requires simultaneous equality of five forms; the bad set is contained in the finite union used in the proof, not necessarily equal to it. Small primes can annihilate nonzero integer coefficient vectors. Strong retains its prior definition; (U) is additional.

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

Each angle is represented by a nine-component integer coefficient
vector; the fourth angle in each cycle is minus the sum of its first
three. A signed-angle coincidence or nonstraight square is a character
relation v·theta=0 mod 2pi. A star at centre zero is (B,F); its neighbour
class is (B_1-B_0,B_2-B_0,F_0+B_0,F_1+B_0,F_2+B_0). Two stars can
share neighbours after a centre shift only when all five components agree.
There are finitely many pairs of stars, and symbolic distinctness supplies
at least one nonzero integer difference per pair. A nonzero integer
character of a real torus has a zero-measure kernel even when its
coefficients have a common factor. This proves the required containment
and measure statement without treating simultaneous equalities as one.

- **Strong cycle letters** and the rotation-covariant rule (open PRs 8854
  and 8856).
- **Parameters:** c_{j,0}, c_{j,1}, c_{j,2} free for each cycle j, and
  c_{j,3} = −(c_{j,0} + c_{j,1} + c_{j,2}).



## Theorem — Genericity

If one of the declared conditions fails, at least one of a finite
collection of nontrivial integer relations holds modulo a full turn. Every such relation reduces, in the 9 free
parameters, to a nonzero integer vector; the runner checks this for all
decoding and square relations. For (U), two stars collide only if their
five neighbour-class forms agree, and the runner checks that the symbolic
forms of distinct stars differ, so some difference is a nonzero relation.
A nonzero integer relation cuts a closed set of measure zero from the torus
of angles. There are finitely many such relations, so their union has
measure zero, and the good set of strong letters with (U), which contains the
complement of that union, has full measure.


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
- [Companion result from PR #8856](STRONG_CYCLE_LETTERS_RECORD_FRAME_AND_ROLES_UNDER_THE_ROTATION_COVARIANT_RULE_ON_EVERY_WINDOW_BOUNDED_THEOREM_NOTE_2026-09-23.md)

The original author narrative and review history are recoverable from
the originating PR. Historical author mutation reports are not a substitute
for the current landing review. No new axiom or retained audit grade is adopted.

## Verification

```bash
python3 scripts/strong_cycle_letters_are_generic_every_obstruction_is_a_nontrivial_angle_relation_2026_09_23.py
```

The runner exits nonzero on a failed check. The fresh captured evidence is
`logs/runner-cache/strong_cycle_letters_are_generic_every_obstruction_is_a_nontrivial_angle_relation_2026_09_23.txt`. Its finite check results and resolution certificate
state the execution scope; analytic claims additionally require the proof above.
