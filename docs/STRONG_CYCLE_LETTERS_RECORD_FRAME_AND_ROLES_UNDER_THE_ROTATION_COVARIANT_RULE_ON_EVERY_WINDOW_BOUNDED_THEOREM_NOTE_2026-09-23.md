---
claim_id: strong_cycle_letters_record_frame_and_roles_under_the_rotation_covariant_rule_on_every_window_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "Strong means decoding, zero cycle sums and the mixed-sign straight-square condition; (U) is an additional property of the chosen mod-100003 example. For cubic cores of side at least two the internal-link proof gives one cycle and raw sense per axis and shared phase walks with \u00b11 increments. Thus core values are folded spirals, and parity is fixed up to one global phase.  On the side-three core the exhaustive set of 24576 restrictions equals the separately generated folded spirals and has global frame/parity readouts. The chosen letters have 24576 distinct neighbour classes and (U); controls include 240 bent mixed-sign squares for mod 211 and collisions for mod 37. Closed zero-sum phase walks on side four are all monotone (eight per cycle); side eight admits folds (64 per cycle). An explicit side-eight folded record satisfies all 512 site constraints and has varying orientation but constant frame/parity phase. The mod-211 side-three contrast has 33792 restrictions, 9216 failing the canonical parity readout. Shared walks describe internal core links. Outer-face steps at distinct boundary sites can choose \u00b11 independently; their phase parity is nevertheless the opposite of the adjacent internal phase, so the same parity offset extends to each boundary readout. A canonical folded extension chooses shared outer steps, but not all extensions do. The theorem is for cubic cores and the stated compatible tori, not arbitrary window shapes. Orientation is not generally constant, and no physical role encoding is derived."
upstream_dependencies:
  - minimal_axioms
  - relational_cycle_letters_record_their_octant_under_the_rotation_covariant_static_rule_on_the_landed_ice_torus_bounded_theorem_note_2026-09-23
runner: scripts/strong_cycle_letters_record_frame_and_roles_under_the_rotation_covariant_rule_on_every_window_2026_09_23.py
---

# Strong cycle letters fix core frames and parity with possible folds

**Date:** 2026-09-23
**Type:** bounded_theorem

## Result and scope

Strong means decoding, zero cycle sums and the mixed-sign straight-square condition; (U) is an additional property of the chosen mod-100003 example. For cubic cores of side at least two the internal-link proof gives one cycle and raw sense per axis and shared phase walks with ±1 increments. Thus core values are folded spirals, and parity is fixed up to one global phase.

On the side-three core the exhaustive set of 24576 restrictions equals the separately generated folded spirals and has global frame/parity readouts. The chosen letters have 24576 distinct neighbour classes and (U); controls include 240 bent mixed-sign squares for mod 211 and collisions for mod 37. Closed zero-sum phase walks on side four are all monotone (eight per cycle); side eight admits folds (64 per cycle). An explicit side-eight folded record satisfies all 512 site constraints and has varying orientation but constant frame/parity phase. The mod-211 side-three contrast has 33792 restrictions, 9216 failing the canonical parity readout.

## Boundaries and non-claims

Shared walks describe internal core links. Outer-face steps at distinct boundary sites can choose ±1 independently; their phase parity is nevertheless the opposite of the adjacent internal phase, so the same parity offset extends to each boundary readout. A canonical folded extension chooses shared outer steps, but not all extensions do. The theorem is for cubic cores and the stated compatible tori, not arbitrary window shapes. Orientation is not generally constant, and no physical role encoding is derived.

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

The strong example uses modulus 100003 and cycles
(17612,74607,8272,99515), (33433,15456,64938,86179),
(99741,58916,61899,79453). The companion rule permits equal raw sense
and cycle within each axis, phases differing by ±1, and distinct cycles
across axes. Mixed-sign straightness quantifies every allowed cycle and
phase assignment and all four independent edge signs in a+b=c+e.
The mod-211 and mod-37 controls are the explicit sets in the runner.

- **Admissibility** (minimal axioms): one fixed nearest-neighbour rule,
  covariant under lattice translations and proper cubic rotations.
- **The covariant rule** (octant block, open PR 8854).
- **Planar form** (open PR 8729); cycle letters (open PR 8752).
- **Role pattern:** the parity vector x mod 2 up to its 8 global phases.



## Theorem — Folded spirals

Let the letters be strong, and take a cubic core of side at least 2.

- **Links.** On a core link from y to y + e_i the difference is F_i(y) and
  also B_i(y + e_i), and it decodes to one raw sense, one cycle and one
  phase. So along a line of core links the raw sense and the cycle are
  constant, and at each site the phase steps by ±1.
- **Squares.** In a core square, write a = F_i(y) and c = F_j(y), and
  b = F_j(y + e_i) and e = F_i(y + e_j). The line through y + e_i along i
  carries the cycle of a, so b carries another cycle; likewise e. At the
  far corner b and e carry different cycles. The relation a + b = c + e,
  with any raw senses, then has only straight solutions: b = c and e = a,
  with the same cycle, phase and raw sense.
- **Folded spirals.** Parallel internal core links therefore agree step by step. Each
  axis carries one cycle, one raw sense and one phase walk, and every such
  choice has a canonical extension satisfying the rule. Outer-face
  choices need not agree across parallel lines.

**Readouts.** The forward step along axis i at x has phase w_i(x_i), and
w_i(x_i) ≡ w_i(1) + x_i − 1 (mod 2). The parity vector is x mod 2 plus one
global phase. The frame is the cycle carried by each axis.

**Windows.** On the side-L torus each walk must close, and its steps must
sum to 0 mod m. For the declared letters and L = 4, only monotone walks
do; for L = 8, folded walks do as well.


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
- [Companion result from PR #8854](RELATIONAL_CYCLE_LETTERS_RECORD_THEIR_OCTANT_UNDER_THE_ROTATION_COVARIANT_STATIC_RULE_ON_THE_LANDED_ICE_TORUS_BOUNDED_THEOREM_NOTE_2026-09-23.md)

The original author narrative and review history are recoverable from
the originating PR. Historical author mutation reports are not a substitute
for the current landing review. No new axiom or retained audit grade is adopted.

## Verification

```bash
python3 scripts/strong_cycle_letters_record_frame_and_roles_under_the_rotation_covariant_rule_on_every_window_2026_09_23.py
```

The runner exits nonzero on a failed check. The fresh captured evidence is
`logs/runner-cache/strong_cycle_letters_record_frame_and_roles_under_the_rotation_covariant_rule_on_every_window_2026_09_23.txt`. Its finite check results and resolution certificate
state the execution scope; analytic claims additionally require the proof above.
