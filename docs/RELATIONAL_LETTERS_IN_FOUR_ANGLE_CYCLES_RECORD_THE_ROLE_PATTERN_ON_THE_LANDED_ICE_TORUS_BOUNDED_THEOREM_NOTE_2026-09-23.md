---
claim_id: relational_letters_in_four_angle_cycles_record_the_role_pattern_on_the_landed_ice_torus_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "For the fixed-octant planar cycle rule, decoding and straight squares force cycle spirals. The declared mod-211 cycles have 96 straight and zero bent same-sense squares, 768 stars, and no shared-neighbour ambiguity (U). Core sides 2,3,4 have 768 records with unique face completions; direct torus searches at L=2 through 8 give 768 exactly for 4|L. The torus argument extends the wrap criterion to other sizes.  All 768 side-four records carry a frame, sense and phase modulo four, hence parity up to a global phase. Centre uniqueness is checked on all stars and sampled at all 64 sites in 48 records; shift/reflection readout checks use eight records and 31 shifts. A mod-37 (U)-failing control has 24 shared stars. A different mod-37 set with (U) and bent squares has 1344 core records, including 576 nonspirals. The sitewise-orientation variant has 24576 side-four records; the companion covariant-extension note identifies them as oriented spirals, rather than generic flexibility. The fixed-octant rule uses supplied oriented background. The later covariant extension is a chosen rule, not uniquely mandated by the axioms. These are abstract planar support records; composing with ice variables, physical encodings or a gravitational model is not proved here. The 211 residues belong to a supplied angle model."
upstream_dependencies:
  - relational_cycle_letters_record_their_octant_under_the_rotation_covariant_static_rule_on_the_landed_ice_torus_bounded_theorem_note_2026-09-23
  - minimal_axioms
  - relational_spiral_letters_with_finitely_many_values_seven_suffice_and_are_the_fewest_bounded_theorem_note_2026-09-23
  - relational_letters_in_alternating_pairs_record_the_role_pattern_under_the_static_reading_but_not_on_the_side_four_torus_bounded_theorem_note_2026-09-23
runner: scripts/relational_letters_in_four_angle_cycles_record_the_role_pattern_on_the_landed_ice_torus_2026_09_23.py
---

# Four-angle cycle records on the side-four torus

**Date:** 2026-09-23
**Type:** bounded_theorem

## Result and scope

For the fixed-octant planar cycle rule, decoding and straight squares force cycle spirals. The declared mod-211 cycles have 96 straight and zero bent same-sense squares, 768 stars, and no shared-neighbour ambiguity (U). Core sides 2,3,4 have 768 records with unique face completions; direct torus searches at L=2 through 8 give 768 exactly for 4|L. The torus argument extends the wrap criterion to other sizes.

All 768 side-four records carry a frame, sense and phase modulo four, hence parity up to a global phase. Centre uniqueness is checked on all stars and sampled at all 64 sites in 48 records; shift/reflection readout checks use eight records and 31 shifts. A mod-37 (U)-failing control has 24 shared stars. A different mod-37 set with (U) and bent squares has 1344 core records, including 576 nonspirals. The sitewise-orientation variant has 24576 side-four records; the companion covariant-extension note identifies them as oriented spirals, rather than generic flexibility.

## Boundaries and non-claims

The fixed-octant rule uses supplied oriented background. The later covariant extension is a chosen rule, not uniquely mandated by the axioms. These are abstract planar support records; composing with ice variables, physical encodings or a gravitational model is not proved here. The 211 residues belong to a supplied angle model.

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

Write B_i=a(x)-a(x-e_i), F_i=a(x+e_i)-a(x). All six differences
have one common sense; along axis i they decode to consecutive phases
k,k+1 of one cycle, and the axes carry distinct cycles. The cycles are
(19,31,132,29), (108,43,194,77), (88,39,126,169), modulo 211.
The straight-square condition ranges over A!=B, X!=A, Y!=B, X!=Y:
a+b=c+e with a in A, b in X, c in B, e in Y has only b=c,e=a.

- **Static reading** (open PR 8691) with its global octant (open PR 8744).
- **Planar form** (open PR 8729): values on one great circle as residues
  mod m. The one-great-circle step of open PR 8743 uses separations that
  are neither 0 nor 180 degrees. Here m is odd, so no residue is 180
  degrees, and decoding makes every link difference nonzero. This note
  does not restate that step for the cycle rule.
- **Role pattern:** the parity vector x mod 2, up to its 8 global phases
  (landed role-pattern note; open PR 8669).
- **Landed ice torus:** side 4 in fine form (open PRs 8679, 8727).



## Theorem 1 — Cycle spirals

Assume decoding and straight squares, and a core of side at least 2.

- **Links.** On a core link from y to y + e_i, F_i(y) = B_i(y + e_i)
  decodes to one sense, one cycle and one phase k. The rule at y + e_i
  makes its forward phase k + 1. So along every line of core links the
  cycle is constant and the phases advance by one per step. The core is
  connected, so the sense is constant.
- **Squares.** In a core square y, y + e_i, y + e_j, y + e_i + e_j, write
  a = F_i(y), c = F_j(y), b = F_j(y + e_i) and e = F_i(y + e_j). By the
  links step:
  - b carries a cycle X ≠ A, where A is the cycle of line i;
  - e carries a cycle Y ≠ B, where B is the cycle of line j;
  - X ≠ Y at the far corner.

  So a + b = c + e is one of the finitely many square relations. By
  assumption each of them is straight: X = B, Y = A, b = c and e = a.
- **Constancy.** Straight squares carry each line's cycle and phase
  across the transverse directions. Every core link lies in a core square.
  So axis i carries one cycle, and the forward phase at x is
  phi_i + x_i mod 4.

The record is a cycle spiral. Conversely every cycle spiral satisfies the
rule. With one value fixed there are 6 × 2 × 64 = 768.



## Theorem 2 — Tori and roles

On the side-L torus every site is a core site, so for L ≥ 3 a record is
one cycle spiral that wraps. Going once around axis i adds L/4 full
cycles when 4 divides L, which sum to 0 mod m. Otherwise the phase does
not return, since the phase advances by one per step. So records exist
exactly when 4 divides L. The search confirms this for L = 2 to 8 and
finds the 768 spirals for L = 4 and 8.

On the side-4 torus the forward differences at x decode to the frame, the
sense and the phases phi_i + x_i mod 4. Reduced mod 2, the phases give
x mod 2 plus the global phase phi mod 2: the parity vector up to one of
its 8 global phases. The runner reads this at all 64 sites of all 768
records:
- one frame per record;
- one phase per record;
- all 64 cycle phases and all 8 parity phases occur.



## Theorem 3 — The nearest-neighbour form

(U) says that no d ≠ 0 turns an allowed star into another allowed star
with the same six neighbours. For the declared letters the runner tests
all 768 stars and all 210 shifts, and finds none. The positive control is
the cycle set mod 37 ((34, 13, 35, 29), (11, 4, 23, 36), (20, 15, 18, 21)),
which decodes but has 24 such stars. On 48 of the side-4 records, the
rule admits exactly one value at every site given its neighbours.


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

- [Covariant extension and oriented classification](RELATIONAL_CYCLE_LETTERS_RECORD_THEIR_OCTANT_UNDER_THE_ROTATION_COVARIANT_STATIC_RULE_ON_THE_LANDED_ICE_TORUS_BOUNDED_THEOREM_NOTE_2026-09-23.md)

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md)
- [Companion result from PR #8729](RELATIONAL_SPIRAL_LETTERS_WITH_FINITELY_MANY_VALUES_SEVEN_SUFFICE_AND_ARE_THE_FEWEST_BOUNDED_THEOREM_NOTE_2026-09-23.md)
- [Companion result from PR #8750](RELATIONAL_LETTERS_IN_ALTERNATING_PAIRS_RECORD_THE_ROLE_PATTERN_UNDER_THE_STATIC_READING_BUT_NOT_ON_THE_SIDE_FOUR_TORUS_BOUNDED_THEOREM_NOTE_2026-09-23.md)

The original author narrative and review history are recoverable from
the originating PR. Historical author mutation reports are not a substitute
for the current landing review. No new axiom or retained audit grade is adopted.

## Verification

```bash
python3 scripts/relational_letters_in_four_angle_cycles_record_the_role_pattern_on_the_landed_ice_torus_2026_09_23.py
```

The runner exits nonzero on a failed check. The fresh captured evidence is
`logs/runner-cache/relational_letters_in_four_angle_cycles_record_the_role_pattern_on_the_landed_ice_torus_2026_09_23.txt`. Its finite check results and resolution certificate
state the execution scope; analytic claims additionally require the proof above.
