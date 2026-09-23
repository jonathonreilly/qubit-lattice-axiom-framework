---
claim_id: formed_flux_transport_for_every_linear_ice_sweep_rule_is_a_markov_walk_damped_or_rigid_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "For arrow-reversal-symmetric ice sweep rules, let pi^(j) be the forward minority law given back minority j. The mean is linear on all eight back patterns iff M with these columns is doubly stochastic. Exactly6 of27 deterministic rules qualify;40 seeded mixtures and40 off-polytope laws check the criterion. Linear means obey F_t(q)=M E(q)F_(t-1)(q).  Strictly positive M has spectral radius below one unless all three wavevector phases agree. Exact power-norm certificates check7 positive matrices on60 transverse quarter-period wavevectors. Permutation matrices have unimodular monomial powers. These are not an exhaustive dichotomy: M=diag(1,J_2/2) at phases(1,1,-1) has an undamped eigenvalue1 and a nilpotent two-dimensional block. The straight-continuation occupation rates agree at p=0,1/2,3/4. For any rule in the declared class, one reversed arrow in a saturated state follows the column-stochastic pi kernel;20 seeded strictly positive off-polytope rules pass the finite damping grid checks. No classification of every zero-containing stochastic matrix, isotropic-undamped impossibility theorem, photon dynamics, or nonlinear disordered-state transport is asserted. A single-defect result is not a many-defect dilute-limit theorem. The rule, sweep, frame and fresh local draws are supplied."
upstream_dependencies:
  - minimal_axioms
  - formed_flux_as_a_persistent_walk_straight_continuation_gives_ballistic_then_diffusive_transport_bounded_theorem_note_2026-09-22
runner: scripts/formed_flux_transport_for_every_linear_ice_sweep_rule_birkhoff_markov_walks_2026_09_23.py
---

# Linear sweep means are Markov walks: positive, permutation and mixed cases

**Date:** 2026-09-23
**Type:** bounded_theorem

## Result and scope

For arrow-reversal-symmetric ice sweep rules, let pi^(j) be the forward minority law given back minority j. The mean is linear on all eight back patterns iff M with these columns is doubly stochastic. Exactly 6 of 27 deterministic rules qualify; 40 seeded mixtures and 40 off-polytope laws check the criterion. Linear means obey F_t(q)=M E(q)F_(t-1)(q).

Strictly positive M has spectral radius below one unless all three wavevector phases agree. Exact power-norm certificates check 7 positive matrices on 60 transverse quarter-period wavevectors. Permutation matrices have unimodular monomial powers. These are not an exhaustive dichotomy: M=diag(1,J_2/2) at phases(1, 1,-1) has an undamped eigenvalue 1 and a nilpotent two-dimensional block. The straight-continuation occupation rates agree at p=0, 1/2, 3/4. For any rule in the declared class, one reversed arrow in a saturated state follows the column-stochastic pi kernel; 20 seeded strictly positive off-polytope rules pass the finite damping grid checks.

## Boundaries and non-claims

No classification of every zero-containing stochastic matrix, isotropic-undamped impossibility theorem, photon dynamics, or nonlinear disordered-state transport is asserted. A single-defect result is not a many-defect dilute-limit theorem. The rule, sweep, frame and fresh local draws are supplied.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "Conditional finite ice measures, formation and supplied transfer models"
source_of_blocker_text: frontier_question
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Preserve finite hypotheses and test extensions separately"
conditional_surface_status: "The declared model, order, records and numerical tolerances only"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "Conditional mathematics and bounded computation; no retained grade asserted"
```

## Premises and declared objects

- **Arrows.** σ = ±1 on links, with σ = +1 along +e_i. The ice rule in
  arrow form: at each vertex the forward arrows sum to the back arrows'
  sum (open PRs 8687, 8701).
- **Sweep rules.** A law for the three forward arrows given the three back
  arrows, symmetric under reversing all six. When the back sum is ±3 the
  forward arrows equal the back ones. Otherwise the rule places the
  forward minority by the law π^(j), where j is the back minority.
- **Layers.** t = x_1 + x_2 + x_3. F_t(q) is the transform of the mean
  arrows on layer t.


## Theorem 1 — Linear rules

For the back pattern 1 - 2 e_j, the mean forward arrows are 1 - 2π^(j).
For the all-plus pattern they are 1. A linear map M therefore needs
M e_j = π^(j) and M 1 = 1. This happens exactly when Σ_j π^(j) = 1, and
reversing every arrow then gives the remaining patterns. The runner
checks all 27 deterministic rules, 40 random mixtures of permutations and
40 random laws off the polytope, over all eight back patterns exactly.


## Theorem 2 — Strictly positive matrices and permutations

T(q) = M E(q) has spectral radius at most 1. By Wielandt's condition,
equality needs phases consistent along every allowed transition. When
every transition is allowed, that forces q_1 ≡ q_2 ≡ q_3, so the
transverse part is 0. The runner certifies spectral radius below 1 at all
60 quarter-period wavevectors with nonzero transverse part, for 7 such
rules, by a power with infinity norm below 1.

For a permutation, T(q) is monomial with unimodular entries, and so are
its powers: rigid translation.


## Theorem 3 — One defect in the saturated state

In the saturated state every back sum is 3, and the rule passes the
arrows on. A single reversed arrow entering along j makes the back sum 1
with minority j. The rule places the forward minority at i with
probability π^(j)_i, and every other vertex stays saturated. So the
defect's direction is a Markov chain with transition j → i of
probability π^(j)_i. Its matrix is column-stochastic with spectral
radius 1, and Wielandt's condition applies as in Theorem 2. The runner
checks the forward laws exactly for 20 random rules off the Birkhoff
polytope. It certifies spectral radius below 1 at all 60 transverse grid
wavevectors.


Zero-containing non-permutations need separate analysis: diag(1,J_2/2)
at phases(1, 1,-1) has a rigid one-dimensional block and a nilpotent
two-dimensional block. Thus the two cases above are not exhaustive.

## No-go discipline and falsifiers

Negative claims concern only the stated fixed models and completed searches.
Alternative records, hidden state, adaptive orders, larger units, different
rules and different boundary conditions require separate tests. Caps must
not bind for an exhaustive verdict. Finite spectral patterns do not prove
infinite-cross-section physics. A counterexample under the exact hypotheses,
a failed independent count, or a failed stated control falsifies its result.
No other claim is graded, unlocked or audited here.

## Dependencies and provenance

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md)
- [Companion result from PR #8701](FORMED_FLUX_AS_A_PERSISTENT_WALK_STRAIGHT_CONTINUATION_GIVES_BALLISTIC_THEN_DIFFUSIVE_TRANSPORT_BOUNDED_THEOREM_NOTE_2026-09-22.md)

Original context and author review history remain recoverable from the
originating PR. Historical mutation claims are not current review evidence.
The landing review preserves conditional proofs and narrows unsupported
extensions; no new axiom, primitive or audit grade is adopted.

## Verification

```bash
python3 scripts/formed_flux_transport_for_every_linear_ice_sweep_rule_birkhoff_markov_walks_2026_09_23.py
```

The runner exits nonzero on failure. Its fresh captured cache is
`logs/runner-cache/formed_flux_transport_for_every_linear_ice_sweep_rule_birkhoff_markov_walks_2026_09_23.txt`.
Analytic statements require the proofs above in addition to finite checks.
