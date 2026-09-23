---
claim_id: formed_flux_as_a_persistent_walk_straight_continuation_gives_ballistic_then_diffusive_transport_bounded_theorem_note_2026-09-22
claim_type: bounded_theorem
claim_scope: "Fix an oriented diagonal sweep, supplied axis pairing and fresh conditional draws. For 0<=p<=1, R_p copies the back arrows with probability p and otherwise samples uniformly among ice-consistent forward arrows. Its mean kernel is K=p I+(1-p)J/3. Exact enumeration checks the rule on all eight back patterns at p=0,1/3,1/2,1 and its six axis-permutation symmetries.  The mean flux is a direction-memory walk. Through 24 layers it has mass one, is deterministic along the initial axis at p=1, and agrees with the multinomial walk at p=0 (2925 sites). The occupation-variance formula agrees through layers 1..15 at p=1/2; for each fixed p<1 its asymptotic variance per layer is (2/9)(1+p)/(1-p). At p=1 the position is ballistic but variance is zero for the fixed initial direction. With independent fair inflow and independent site noise, second-moment closure is checked on the 4x4x4 box at p=1/2,3/4. The supplied sweep, axis pairing and probability rule are premises. The explicit finite error bound below is checked only at p=1/2 over the printed range. No continuum telegraph limit, isotropic wave theorem, photon dynamics or physical diffusion coefficient is established."
upstream_dependencies:
  - directed_ice_sweep_formation_makes_ice_correlations_causal_flux_propagates_as_a_directed_random_walk_bounded_theorem_note_2026-09-22
  - minimal_axioms
runner: scripts/formed_flux_persistent_walk_straight_continuation_ballistic_then_diffusive_2026_09_22.py
---

# Persistent mean-flux transport for a supplied straight-continuation rule

**Date:** 2026-09-23
**Type:** bounded_theorem

## Result and scope

Fix an oriented diagonal sweep, supplied axis pairing and fresh conditional draws. For 0<=p<=1, R_p copies the back arrows with probability p and otherwise samples uniformly among ice-consistent forward arrows. Its mean kernel is K=p I+(1-p)J/3. Exact enumeration checks the rule on all eight back patterns at p=0, 1/3, 1/2, 1 and its six axis-permutation symmetries.

The mean flux is a direction-memory walk. Through 24 layers it has mass one, is deterministic along the initial axis at p=1, and agrees with the multinomial walk at p=0 (2925 sites). The occupation-variance formula agrees through layers 1..15 at p=1/2; for each fixed p<1 its asymptotic variance per layer is (2/9)(1+p)/(1-p). At p=1 the position is ballistic but variance is zero for the fixed initial direction. With independent fair inflow and independent site noise, second-moment closure is checked on the 4x 4x 4 box at p=1/2, 3/4.

## Boundaries and non-claims

The supplied sweep, axis pairing and probability rule are premises. The explicit finite error bound below is checked only at p=1/2 over the printed range. No continuum telegraph limit, isotropic wave theorem, photon dynamics or physical diffusion coefficient is established.

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

- **Arrows and the ice rule.** Arrows are ±1 along positive coarse axes;
  at a vertex the forward triple has the same sum as the back triple.
- **The sweep.** t=x_1+x_2+x_3, with independent conditional site noise
  and independent fair inflow for the covariance statement.
- **The rule family R_p.** Copy back arrows with probability p; otherwise
  sample uniformly among forward triples with the same sum, using a
  supplied frame to pair axes. Take 0<=p<=1.
- **The direction kernel K,** and the flux kernel G(y, j): the expected
  flux arriving at y along axis j from a unit arriving at the origin
  along axis 0.


## Theorem 1 — The rule and its kernel

Enumeration of the 8 back patterns, for p = 0, 1/3, 1/2 and 1, confirms:
- the ice rule;
- the forward mean;
- covariance under the six axis permutations.

K sends the uniform vector to itself, and sum-zero vectors to p times
themselves.


## Theorem 2 — The persistent walk

G(y, j) = sum_i G(y - e_j, i) K_ij, starting from G(0, 0) = 1. The
following are checked exactly up to 24 layers:
- layer flux 1;
- at p = 1, support on the source axis only;
- at p = 0, the multinomial walk at every site.

The spread along the source axis equals sum_t a_t(1 - a_t) plus twice
sum_(s<t) a_s(1/3 + (2/3)p^(t-s) - a_t), where a_t = 1/3 + (2/3)p^t.
This is the occupation variance of the direction chain started on the
source axis, and the agreement is checked for layers 1-15 at p = 1/2.
At p=1/2 the runner checks the consecutive-difference error bound
4(s+2)p^(s+1) for its finite range; it is not claimed as an all-p bound.
For a stationary direction chain, Cov(1_{J_s=0}, 1_{J_t=0})=(2/9)p^{t-s}.
Summing gives variance per step tending to (2/9)(1+p)/(1-p) for p<1.
From a fixed initial direction the covariance correction is bounded by a
constant times p^s p^{t-s}; the sum over s<t is finite for fixed p<1.
The initial-condition correction is therefore O(1), leaving the same slope.


## Theorem 3 — Causal covariance

For R_p, the conditional mean of a forward arrow is linear in the back
arrows, and for distinct i,k, E[f_i f_k | b] = p b_i b_k + (1 - p)(B^2 - 3)/6 is quadratic.
So the second moments close. Suppose the back arrows of a vertex are
uncorrelated with variance 1. Then the forward arrows are uncorrelated
too, since the linear and fluctuating parts cancel exactly. By induction
over layers every back sum has variance 3, and every covariance is carried
by the mean kernel. Checked exactly on a 4x 4x 4 box for p = 1/2 and 3/4.


## No-go discipline and falsifiers

Negative claims concern only the stated fixed models and completed searches.
Alternative records, hidden state, adaptive orders, larger units, different
rules and different boundary conditions require separate tests. Caps must
not bind for an exhaustive verdict. Finite spectral patterns do not prove
infinite-cross-section physics. A counterexample under the exact hypotheses,
a failed independent count, or a failed stated control falsifies its result.
No other claim is graded, unlocked or audited here.

## Dependencies and provenance

- [Landed companion from PR #8687](DIRECTED_ICE_SWEEP_FORMATION_MAKES_ICE_CORRELATIONS_CAUSAL_FLUX_PROPAGATES_AS_A_DIRECTED_RANDOM_WALK_BOUNDED_THEOREM_NOTE_2026-09-22.md)

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md)

Original context and author review history remain recoverable from the
originating PR. Historical mutation claims are not current review evidence.
The landing review preserves conditional proofs and narrows unsupported
extensions; no new axiom, primitive or audit grade is adopted.

## Verification

```bash
python3 scripts/formed_flux_persistent_walk_straight_continuation_ballistic_then_diffusive_2026_09_22.py
```

The runner exits nonzero on failure. Its fresh captured cache is
`logs/runner-cache/formed_flux_persistent_walk_straight_continuation_ballistic_then_diffusive_2026_09_22.txt`.
Analytic statements require the proofs above in addition to finite checks.
