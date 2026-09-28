---
claim_id: an_exact_additive_gauss_law_on_discrete_slots_needs_its_variable_diagonal_on_every_slot_it_touches_so_only_the_pure_assignments_carry_the_full_tensor_rules_and_integer_rotors_keep_the_orders_bounded_theorem_note_2026-09-28
claim_type: bounded_theorem
claim_scope: "Slot-wise assignments on the landed tensor complex, each slot with a discrete-spectrum diagonal variable (a spin S, or an integer rotor, possibly unbounded). (A) No self-adjoint C gives [C, D] = i c 1 (c != 0) for a diagonal D with discrete spectrum: finite dimension by the trace; the unbounded rotor because a unitary conjugation cannot shift the spectrum Z by a continuous amount. So an exact additive constraint sum_a c_a X_a can act only on variables that are diagonal on every slot of its support. (B) The momentum rows G_j touch slot types {jj, ij, jk} and the scalar row touches all six. Over all 64 slot-type assignments, the full momentum rule is additive only when every type is momentum-diagonal (probes 10, 14) and the scalar rule only when every type is metric-diagonal (probe 15). 18 mixed assignments make one or two momentum rows additive, never all three and never the scalar rule. Among cubic-symmetric assignments only the two pure ones have any additive row. (C) With integer rotor slots the shift operators obey the same double-commutator identity and are unitary; move patterns are the same integer patterns, so the moment lemmas and both f-sum bounds (probes 10, 15) hold unchanged. Pre-registered outcome FAIL (no new route). Not shown: the orders of the 18 partially additive mixed models, non-slot-wise encodings, continuous (oscillator) slots (the landed comparator), any state or phase."
upstream_dependencies:
  - minimal_axioms
  - local_finite_clock_tensor_constraints_cubic_dispersion_and_linear_gravity_boundaries_bounded_theorem_note_2026-09-14
  - the_lambda_one_question_the_dewitt_form_is_positive_on_the_momentum_sector_weak_invariance_adds_nothing_in_lifted_clock_encodings_finite_slots_need_a_non_additive_time_gauge_bounded_theorem_note_2026-09-28
  - the_swapped_quantum_link_assignment_metric_diagonal_makes_einstein_hilbert_exactly_invariant_but_the_tt_metric_f_sum_of_gauss_law_compatible_moves_is_bounded_by_q_squared_bounded_theorem_note_2026-09-28
runner: scripts/which_slot_assignments_allow_an_exact_gauss_law_for_the_tensor_constraints_and_integer_rotor_slots_2026_09_28.py
---

# An exact additive Gauss law on discrete slots needs its variable diagonal on every slot it touches, so only the pure assignments carry the full tensor rules, and integer rotors keep the orders

**Date:** 2026-09-28
**Type:** bounded_theorem
**Status:** a short lemma with exact checks; pre-registered; unaudited.
Independent checks are recorded below.

## In one paragraph

Probes 10, 14 and 15 put the gravitational momentum on every slot, or the
metric on every slot. Two escapes stayed open:
- a mixed assignment (some slots holding the metric, others the momentum);
- records that are unbounded whole numbers rather than finite.

Both are closed for exact Gauss laws that carry a full tensor rule:
- An exact additive rule can act only on a variable that is stored directly
  on every slot the rule touches. The tensor rules touch all six slot
  types, so the full momentum rule needs momentum everywhere and the time
  rule needs the metric everywhere.
- Mixed assignments can keep one or two of the three momentum rules
  additive, but never all of them, and never the time rule. With cubic
  symmetry, they keep none.
- Unbounded whole-number records obey the same bounds as finite ones.

So among the constructions that carry a full tensor rule as an exact Gauss
law, Einstein's order has appeared only with continuous variables on both
sides. Partially additive mixed models, multi-slot encodings and
non-additive (quantum-link) realisations are not covered.

## Pre-registration

Written in the probe's scratch file before any check was built.
- **PASS (a new route opens)** if either:
  - some constraint's stencil avoids a slot type, so that a mixed
    assignment with one full additive law exists;
  - an integer rotor admits a continuous additive shift;
  - rotor moves escape the moment lemmas.
- **FAIL** otherwise.

**Outcome: FAIL.**

## Prior art

On main:
- the 2026-09-14 tensor note (the stencils; the moment lemma; finite-clock
  and lifted-character encodings).

Of this PR:
- probe 13's trace lemma, for finite dimension; A adds the unbounded
  integer case;
- probes 10, 14 and 15, the two pure assignments.

The spectrum argument is standard: the Stone–von Neumann setting, and the
reason the phase of a rotor is not a self-adjoint operator. It is cited for
context only.

## A — the spectrum lemma (check A)

Take a slot whose diagonal variable D has discrete spectrum.
- **Finite dimension.** tr [C, D] = 0 for every C, so [C, D] = i c 1 is
  impossible for c ≠ 0. This is checked for spins ½ to 3 and truncated
  rotors.
- **Unbounded integer rotor.** If [C, D] = i c 1 with C self-adjoint, then
  exp(itC) D exp(−itC) = D + ct. Conjugation by a unitary preserves the
  spectrum, but ℤ + ct ≠ ℤ for small t.
- **Consequence.** An exact additive constraint Σ c_a X_a generates
  continuous shifts of the variables conjugate to the X_a. It can do so on
  discrete slots only if every X_a in its support is the diagonal variable,
  rotating a compact conjugate.

## B — which assignments carry which rules (check B)

- **Supports.** Each momentum row G_j touches the types {jj, ij, jk}: 3 of 6.
  The scalar row touches all 6.
- **All 64 slot-type assignments** (each type momentum-diagonal or
  metric-diagonal):
  - the full momentum rule is additive only in the all-momentum assignment
    (probes 10, 14);
  - the scalar rule is additive only in the all-metric assignment
    (probe 15);
  - 18 mixed assignments make one or two momentum rows additive, never all
    three and never the scalar rule.
- **Cubic-symmetric assignments** (all, none, diagonals only, faces only):
  only the two pure ones have any additive row.

## C — integer rotors keep the orders (check C)

- A shift operator T with [D, T] = r T obeys
  `[[T + T^dag, A], A^dag] = |a·r|² (T + T^dag)` for diagonal A. This is
  checked on spin-1 and truncated-rotor toys.
- Rotor shifts are unitary (norm 1).
- The move patterns are the same integer patterns.
- So the moment lemmas (probe 10 T2; probe 15 B) and both f-sum bounds hold
  unchanged: the electric bound O(q⁴) with the momentum diagonal, and the
  metric bound O(q²) with the metric diagonal.

## What this means

In the exact-rule class with slot-wise, discrete-spectrum records:
- the full tensor rules are carried as exact Gauss laws only by the two pure
  assignments already tested;
- whole-number records, even unbounded, do not change their orders.

Einstein's order (a local kinetic term with a curvature potential)
appeared, among the constructions tested, only in the landed comparator,
where both the metric and its momentum are continuous.

Still open:
- the 18 partially additive mixed models, whose orders are not computed
  here;
- non-slot-wise encodings;
- approximate (emergent) rules;
- strongly correlated states;
- composite metrics.

## No-Go Discipline Gate

The bounded negative claims:
- (a) in slot-wise discrete-spectrum assignments, the full momentum rule is
  an exact additive law only in the all-momentum assignment, and the scalar
  rule only in the all-metric one;
- (b) integer rotors keep probes 10 and 15's bounds.

- **N1 — attack routes.** Five, all ATTEMPTED here.
  1. *A continuous additive shift on a discrete slot.* Attempted in A (trace;
     spectrum). Fails.
  2. *A stencil that avoids a slot type.* Attempted in B (all rows'
     supports). Only the momentum rows individually avoid types; the full
     rules do not. Fails for the full rules.
  3. *A mixed assignment with a full additive law.* Attempted in B (all 64
     assignments). Fails.
  4. *Rotor moves escaping the identity.* Attempted in C. Fails.
  5. *Rotor moves escaping the moment lemma.* Attempted as an argument: the
     patterns are the same integer patterns. Fails.

  **Open routes:**
  - (i) the 18 partially additive models;
  - (ii) non-slot-wise encodings (records spanning several slots);
  - (iii) continuous slots, which are outside the premise.
- **N2 — pairwise table.**
  - W1: discrete spectrum on every slot.
  - W2: slot-wise assignments.
  - W3: exact additive realisation.

  | Pair | First closes second? | Second closes first? | Relation |
  | --- | --- | --- | --- |
  | W1, W2 | no | no | independent |
  | W1, W3 | no | no | independent |
  | W2, W3 | no | no | independent |

- **N3 — hidden conditions.** All explicit: slot-wise assignment, discrete
  spectrum, additivity.
- **N4 — residual matching.**

  | Citation (path:line) | Residual attacked | Residual claimed closed here | Match |
  | --- | --- | --- | --- |
  | probe 13 note (docs/THE_LAMBDA_ONE_QUESTION_..._2026-09-28.md):159 | an additive shift on a finite slot | none; A extends it to unbounded integer slots | yes |
  | probe 15 note (docs/THE_SWAPPED_QUANTUM_LINK_ASSIGNMENT_..._2026-09-28.md), check B | a Gauss-law-compatible move with a zeroth moment | none; C carries it to rotors | yes |

  Both are unaudited parents.
- **N5 — rhetoric audit.**

  | Phrase | Resolutions tested | Holds at untested ones? |
  | --- | --- | --- |
  | "only the pure assignments" | per_block (all 64 assignments) | exhaustive for slot-wise assignments |
  | "rotors keep the orders" | per_element (identity on toys); the patterns | yes: pattern statements |

- **N6 — primitive scan.** The registry's minimal_axioms fixes M₂(C) per
  site. No primitive supplies continuous local variables, and none is
  invoked.
- **N7 — steelman.** A partially additive mixed model, or a multi-slot
  encoding, might keep enough exactness for a light cone. That is open.
  This note only removes the full-rule versions.
- **N8 — cross-cycle echo.**
  - Probe 13's trace lemma: extended.
  - The landed statement for the specified comparator: consistent with it;
    the comparator is the continuous case.
- **Outcome.** PASS as scoped for (a) and (b). The pre-registered outcome is
  FAIL.

## Independent checks

Pending.

## Reproduction

`python3 scripts/which_slot_assignments_allow_an_exact_gauss_law_for_the_tensor_constraints_and_integer_rotor_slots_2026_09_28.py`
prints 3 checks, the N5 lines and TOTAL, in under 1 s. The canonical cache is
at
logs/runner-cache/which_slot_assignments_allow_an_exact_gauss_law_for_the_tensor_constraints_and_integer_rotor_slots_2026_09_28.txt.
