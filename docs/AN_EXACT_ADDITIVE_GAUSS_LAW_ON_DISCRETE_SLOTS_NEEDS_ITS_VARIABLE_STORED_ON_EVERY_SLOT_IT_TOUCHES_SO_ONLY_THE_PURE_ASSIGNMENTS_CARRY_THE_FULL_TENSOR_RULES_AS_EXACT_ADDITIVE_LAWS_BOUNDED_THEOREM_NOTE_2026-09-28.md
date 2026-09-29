---
claim_id: an_exact_additive_gauss_law_on_discrete_slots_needs_its_variable_stored_on_every_slot_it_touches_so_only_the_pure_assignments_carry_the_full_tensor_rules_as_exact_additive_laws_bounded_theorem_note_2026-09-28
claim_type: bounded_theorem
claim_scope: "Slot assignments on the landed tensor complex, each slot storing (diagonally, with discrete spectrum) either the momentum or the metric component of its slot type. Definition: a rule row G = sum_a c_a X_a (one Hermitian operator per touched slot) is an exact additive Gauss law if exp(i theta G) acts on each touched slot as a translation of the variable conjugate to X_a by the c-number c_a theta (Weyl form). (A) A stored variable with discrete spectrum cannot be translated by a c-number (spectral invariance; on finite slots also the landed per-site trace identity). So each touched slot must store X_a itself. (B) Supports derived from the landed stencils: momentum rows touch {jj, ij, jk}; the scalar row touches all six; every slot is touched by both rules, so any generating set has the same support. Over all 64 slot-type assignments the full momentum rule is additive only in the all-momentum assignment and the scalar rule only in the all-metric one; 15 mixed assignments keep one momentum row additive, 3 keep two, none all three; among cubic-symmetric assignments only the pure ones keep any additive row; the same holds for arbitrary per-slot assignments. Pre-registered outcome FAIL. Not shown: the orders of the 18 partially additive models; non-additive (quantum-link) realisations; slots storing commuting h and E together; unbounded rotor slots' f-sum bounds (a conditional remark only); any state or phase."
upstream_dependencies:
  - minimal_axioms
  - no_per_site_bosonic_ccr_theorem_note_2026-05-02
  - local_finite_clock_tensor_constraints_cubic_dispersion_and_linear_gravity_boundaries_bounded_theorem_note_2026-09-14
  - one_qubit_per_slot_under_the_tensor_momentum_rule_an_exact_sum_rule_bounds_the_graviton_channel_by_q4_a_light_cone_mode_needs_an_incompressible_electric_pattern_bounded_theorem_note_2026-09-28
  - a_quantum_link_deformation_of_the_linear_scalar_constraint_on_tensor_slots_of_spin_at_least_two_keeps_the_dewitt_kinetic_term_weakly_invariant_but_its_classical_algebra_is_not_first_class_on_the_whole_constraint_surface_bounded_theorem_note_2026-09-28
  - the_swapped_quantum_link_assignment_metric_diagonal_makes_einstein_hilbert_exactly_invariant_but_the_tt_metric_f_sum_of_gauss_law_compatible_moves_is_bounded_by_q_squared_bounded_theorem_note_2026-09-28
runner: scripts/which_slot_assignments_carry_the_tensor_constraints_as_exact_additive_gauss_laws_2026_09_28.py
---

# An exact additive Gauss law on discrete slots needs its variable stored on every slot it touches, so only the pure assignments carry the full tensor rules as exact additive laws

**Date:** 2026-09-28
**Type:** bounded_theorem
**Status:** a short lemma with exact checks; pre-registered; unaudited.
Revised after the first referee's FAILS verdict. Independent checks are
recorded below.

## In one paragraph

Probes 10, 14 and 15 store the gravitational momentum on every slot, or the
metric on every slot. This probe asks whether a mixed storage could keep a
full tensor rule as an exact Gauss law of the ordinary (additive) kind.

It cannot. An additive rule works by sliding the partner of each variable
it touches. A stored variable on a discrete slot cannot be slid by a fixed
amount, since its possible values are fixed. So every slot the rule touches
must store the rule's own variable.

The tensor rules touch every slot. So:
- the full momentum rule needs momentum stored everywhere;
- the time rule needs the metric stored everywhere.

Mixed storages can keep one or two of the three momentum rows additive,
never all three, and never the time rule.

## Pre-registration

Written in the probe's scratch file before any check was built.
- **PASS (a new route opens)** if either:
  - some constraint's stencil avoids a slot type, so that a mixed
    assignment keeps a full additive law; or
  - a discrete slot admits a continuous additive shift.
- The registration also listed rotor moves escaping the moment lemmas. That
  part is withdrawn (see C).
- **FAIL** otherwise.

**Outcome: FAIL.**

## Prior art

On main:
- **The per-site CCR note** (NO_PER_SITE_BOSONIC_CCR_THEOREM_NOTE_2026-05-02):
  the trace identity, tr [A, B] = 0 in finite dimension, forbids an exact
  bosonic CCR in the per-site qubit algebra. A uses the same identity.
  Probe 13's trace lemma is the same argument applied to the time gauge,
  and should have cited this note.
- **The 2026-09-14 tensor note:** the stencils.

Of this PR: probes 10, 14 and 15.

External, reference only: the Weyl-versus-CCR distinction. A weak
commutation relation [C, D] = i1 on a dense domain can hold with bounded C
for an unbounded integer D (the rotor phase), without any unitary
translation (Galapon, quant-ph/9908033). The definition below uses the Weyl
form for that reason.

## Definition and premises

- **Slots.** Each slot type stores, diagonally with discrete spectrum,
  either the momentum or the metric component. This is the binary
  slot-type ansatz, extended in B to arbitrary per-slot choices.
- **Exact additive Gauss law.** A rule row G = Σ c_a X_a, one Hermitian
  operator per touched slot, such that exp(iθG) acts on each touched slot as
  a translation, by the c-number c_a θ, of the variable conjugate to X_a
  (Weyl form).

## A — a stored discrete variable cannot be translated (check A)

- A unitary conjugation preserves the spectrum. A translation D → D + cθ
  with c ≠ 0 would move a discrete spectrum off itself. So no one-parameter
  unitary group translates a stored variable.
- On finite slots this is also the landed trace identity: tr [C, D] = 0,
  checked for spins ½ to 3.
- So for G to be an exact additive law, each touched slot must store X_a
  itself. Its conjugate phase is what gets translated.

## B — which assignments carry which rules (check B)

- **Supports.** Derived from the landed stencils on the 4³ torus: the
  momentum rows touch {jj, ij, jk}, and the scalar row touches all six
  types.
- **Every slot is touched.** Every slot at every position is touched by
  some momentum row and by some scalar row; no column is zero. The column
  support of a row space does not depend on the generating set, so an
  equivalent stencil touches the same slots.
- **All 64 slot-type assignments:**
  - the full momentum rule is additive only in the all-momentum assignment;
  - the scalar rule only in the all-metric assignment;
  - 15 mixed assignments keep one momentum row additive, 3 keep two, and
    none keeps all three.
- **Cubic-symmetric assignments:** only the two pure ones keep any additive
  row.
- **Per-slot assignments.** Because every slot is touched, the same holds
  for arbitrary per-slot (translation-breaking) assignments.

## C — rotor slots (withdrawn to a conditional remark)

The first version claimed that unbounded integer (rotor) slots keep probes
10 and 15's f-sum bounds unchanged. That needs three extra hypotheses that
finite slots meet automatically:
- diagonal prefactors bounded in the stored variable;
- summability of the shift components;
- a normalisable ground state in the domain of D².

Under those hypotheses the formal double-commutator identity gives the same
orders (Fable check). Without them nothing is claimed.

## What this means

Among slot assignments with discrete-spectrum storage, the full tensor
rules are carried as exact additive Gauss laws only by the two pure
assignments already tested (probes 10/14 and 15).

Still open:
- the 18 partially additive mixed models, whose orders are not computed;
- non-additive (quantum-link) realisations, as in probes 14 and 15;
- slots storing commuting h and E together, which is outside the
  conjugate-pair premise;
- rotors without the three hypotheses.

## No-Go Discipline Gate

The bounded negative claim: with discrete-spectrum storage, a full tensor
rule is an exact additive (Weyl-form) Gauss law only in the matching pure
assignment.

- **N1 — attack routes.** Five distinct routes, all ATTEMPTED here.
  1. *A c-number translation of a stored discrete variable.* Attempted in A
     (spectral invariance; trace). Fails.
  2. *A weak commutation relation instead.* Attempted in the prior-art
     discussion: it can hold (the rotor phase) but does not exponentiate to
     a translation, so it does not meet the definition. It is outside the
     domain, not a counterexample.
  3. *A stencil that avoids a slot type.* Attempted in B: derived supports.
     Only the individual momentum rows avoid types. Fails for the full
     rules.
  4. *A different generating set.* Attempted in B: the column support of a
     row space is basis-independent, and no column is zero. Fails.
  5. *A mixed or per-slot assignment with a full additive law.* Attempted
     in B: all 64 slot-type assignments, and per-slot by the no-zero-column
     argument. Fails.

  **Open routes:**
  - (i) the 18 partially additive models;
  - (ii) non-additive realisations;
  - (iii) commuting h and E storage;
  - (iv) continuous slots.
- **N2 — pairwise table.**
  - W1: discrete spectrum on every slot.
  - W2: conjugate-pair storage (one variable stored per slot).
  - W3: the Weyl-form additivity definition.

  | Pair | First closes second? | Second closes first? | Relation |
  | --- | --- | --- | --- |
  | W1, W2 | no: a slot can have discrete spectrum and store both h and E | no: continuous slots store one variable | independent |
  | W1, W3 | no | no: Weyl translations exist on continuous slots | independent |
  | W2, W3 | no | no | independent |

- **N3 — hidden conditions.** Named now:
  - the binary slot-type ansatz, extended to per-slot choices;
  - the Weyl form, which excludes weak CCR;
  - conjugate-pair storage;
  - for C, the three rotor hypotheses.
- **N4 — residual matching.**

  | Citation (path:line) | Residual attacked | Residual status here | Match |
  | --- | --- | --- | --- |
  | [per-site CCR note](NO_PER_SITE_BOSONIC_CCR_THEOREM_NOTE_2026-05-02.md), "Admitted-context inputs" | a finite-dimensional CCR | used for A on finite slots | yes |
  | [probe 13](THE_LAMBDA_ONE_QUESTION_THE_DEWITT_FORM_IS_POSITIVE_ON_THE_MOMENTUM_SECTOR_WEAK_INVARIANCE_ADDS_NOTHING_IN_LIFTED_CLOCK_ENCODINGS_FINITE_SLOTS_NEED_A_NON_ADDITIVE_TIME_GAUGE_BOUNDED_THEOREM_NOTE_2026-09-28.md), check E (line 159) | an additive time gauge on finite slots | extended to per-row supports | yes |
  | [probe 10](ONE_QUBIT_PER_SLOT_UNDER_THE_TENSOR_MOMENTUM_RULE_AN_EXACT_SUM_RULE_BOUNDS_THE_GRAVITON_CHANNEL_BY_Q4_A_LIGHT_CONE_MODE_NEEDS_AN_INCOMPRESSIBLE_ELECTRIC_PATTERN_BOUNDED_THEOREM_NOTE_2026-09-28.md) and [probe 15](THE_SWAPPED_QUANTUM_LINK_ASSIGNMENT_METRIC_DIAGONAL_MAKES_EINSTEIN_HILBERT_EXACTLY_INVARIANT_BUT_THE_TT_METRIC_F_SUM_OF_GAUSS_LAW_COMPATIBLE_MOVES_IS_BOUNDED_BY_Q_SQUARED_BOUNDED_THEOREM_NOTE_2026-09-28.md) | the two pure assignments | identified as the only full-rule additive ones | yes |

  All parents are unaudited except the per-site CCR note, whose status is
  set by the audit lane.
- **N5 — rhetoric audit.**

  | Phrase | per_element | per_site | per_mode | per_block | lattice_wide |
  | --- | --- | --- | --- | --- | --- |
  | "needs its variable stored" | the trace on each spin (A) | – (not applicable) | – (not applicable) | – (not applicable) | the spectral argument, for any discrete spectrum |
  | "only the pure assignments" | – (not applicable) | the supports at a torus site, every column checked | – (not applicable) | all 64 slot-type assignments | per-slot assignments, by the no-zero-column argument |

- **N6 — primitive scan.**
  - The registry's minimal_axioms fixes M₂(C) per site.
  - The per-site CCR note is a landed no-go on that algebra.
  - No primitive supplies continuous slots, and none is invoked.
- **N7 — steelman.** A partially additive mixed model, or a non-additive
  realisation, might keep enough exactness for a light cone. So might
  storing h and E together as commuting variables. That is open, and this
  note only removes the full-rule additive versions.
- **N8 — cross-cycle echo.**
  - The per-site CCR no-go: reused.
  - Probe 13's trace lemma: the same identity. Its missing citation is
    recorded here.
- **Outcome.** PASS as scoped. The pre-registered outcome is FAIL.

## Independent checks

- **gpt-5.6-sol (other vendor), first round: FAILS.** Its findings, and how
  this version answers each:
  1. The unbounded-rotor lemma was false as stated (a weak-CCR
     counterexample). A is now in Weyl form, and the weak case is
     discussed.
  2. "Additive" was undefined, and the enumeration hard-coded its premise.
     It is now defined, the supports are derived from the stencils, and the
     no-zero-column argument covers per-slot assignments.
  3. The rotor f-sum extension was unproved. Withdrawn to a conditional
     remark (C).
  4. The runner checks were decorative. A and C are replaced; B asserts
     the exact counts 15, 3 and 1, which the referee confirmed
     independently.
  5. The gate was rewritten.
  6. Provenance: probes 10, 14 and 15 and the per-site CCR note are added.
- **Fable check (same family): STANDS WITH CORRECTIONS.**
  - The Weyl form and a definition of "additive" (applied).
  - The three rotor hypotheses (now C).
  - The title qualifier "as exact additive laws" (applied).
  - Per-slot and generating-set independence (added to B).
  - The commuting h and E storage gap (named).
- Second rounds: pending.

## Reproduction

`python3 scripts/which_slot_assignments_carry_the_tensor_constraints_as_exact_additive_gauss_laws_2026_09_28.py`
prints 2 checks, the N5 lines and TOTAL, in under 1 s. The canonical cache
is at
logs/runner-cache/which_slot_assignments_carry_the_tensor_constraints_as_exact_additive_gauss_laws_2026_09_28.txt.
