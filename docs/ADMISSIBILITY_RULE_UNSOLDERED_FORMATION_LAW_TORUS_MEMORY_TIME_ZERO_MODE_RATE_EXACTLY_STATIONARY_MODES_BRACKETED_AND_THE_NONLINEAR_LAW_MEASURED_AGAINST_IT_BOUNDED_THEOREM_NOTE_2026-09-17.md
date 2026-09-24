---
claim_id: admissibility_rule_unsoldered_formation_law_torus_memory_time_zero_mode_rate_exactly_stationary_modes_bracketed_and_the_nonlinear_law_measured_against_it_bounded_theorem_note_2026-09-17
claim_type: bounded_theorem
claim_scope: "For the supplied gain-one recurrence theta(t+1)=P theta(t)+xi on a finite periodic L by L plane, prove the mode variances, zero-mode memory proxy and stationary nonzero-mode bracket for beta>0. Exact rational controls on L=2,3,4 and memory-time enclosures on the listed beta and size grid. The S_L increment test concerns L=16,32,64 only. This recurrence is a supplied linear comparator, not the exact finite-beta Cartesian mean linearization of the nonlinear sphere kernel. Historical nonlinear simulations are author-reported finite observations, not newly verified results or asymptotic theorems. No physical rule, gravity kernel or axiom selection is derived; no clause is adopted."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06
runner: scripts/admissibility_rule_unsoldered_formation_law_torus_memory_time_zero_mode_rate_exactly_stationary_modes_bracketed_nonlinear_law_measured_2026_09_17.py
---

# Torus mode variances and memory proxy for a supplied gain-one recurrence

**Date:** 2026-09-17
**Type:** bounded_theorem

## Result and scope

For the supplied gain-one recurrence theta(t+1)=P theta(t)+xi on a finite periodic L by L plane, prove the mode variances, zero-mode memory proxy and stationary nonzero-mode bracket for beta>0. Exact rational controls on L=2,3,4 and memory-time enclosures on the listed beta and size grid. The S_L increment test concerns L=16,32,64 only. This recurrence is a supplied linear comparator, not the exact finite-beta Cartesian mean linearization of the nonlinear sphere kernel. Historical nonlinear simulations are author-reported finite observations, not newly verified results or asymptotic theorems. No physical rule, gravity kernel or axiom selection is derived; no clause is adopted.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "Exact properties of an explicitly supplied linear recurrence"
source_of_blocker_text: scoped_review
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Establish a controlled connection to the nonlinear kernel before importing linear conclusions"
conditional_surface_status: "Gain-one surrogate and stated finite checks; nonlinear observations remain historical"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "Algebraic identities under explicit model assumptions"
```

## Premises and declared objects

Fix beta>0, L>=2, and the supplied recurrence theta(t+1)=P theta(t)+xi(t) from zero, where P averages the sites x,x-e1,x-e2 of the preceding level of the periodic L by L plane. The centered noises are independent across sites and levels with component variance sigma^2=A(3beta)/(3beta), A(kappa)=coth(kappa)-1/kappa. Use the positive-exponent modes X_k=L^-1 sum_x exp(+ik.x)theta_x. The proxy exp(-v_t) is defined from the component site variance; it is not identified with nonlinear magnetization.

The separate nonlinear sphere kernel is K_beta(ds|S) proportional to exp(beta s.S) on the real unit sphere, where S is the sum of three predecessor spins. Its normalization under uniform sphere measure is sinh(kappa)/kappa, kappa=beta|S|. Differentiating gives E[s|S]=A(kappa) S/|S|. At S=3e_z, the transverse Cartesian derivative is delta E[s_perp]=(A(3beta)/3)delta S_perp. Integration by parts in the polar coordinate gives E[s_x^2]=A(kappa)/kappa. Thus the chosen noise variance is the aligned conditional variance, but the exact Cartesian mean gain is A(3beta), not one. A direction-normalized or strong-coupling approximation needs an additional argument; none is supplied here.

The fixed rule and record sentences of [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) motivate the comparison. The [finite-window rule note](ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md) supplies background only. All mathematical premises used below are restated here; no unlanded sibling theorem is used as proof.

Define S_L=sum_(n!=0)1/|n|^2 over representatives n_i in (-L/2,L/2], V_L=(sigma^2/L^2)sum_(k!=0)1/(1-u_k), and tau_L=L^2/sigma^2.

## Theorem T1 — the modes

**T1.1.** `P` is a circulant on the torus, diagonalized by the characters: `(Pθ)^_k = φ(k) θ̂_k` with `φ(k) = (1 + e^{ik₁} + e^{ik₂})/3`. *Proof.* `Pθ_x = (θ_x + θ_{x−e₁} + θ_{x−e₂})/3` and with the positive-exponent convention below, each backward spatial shift multiplies the transformed field by `e^{ik·e}`. ∎

**T1.2 (the multiplier identity).** `1 − |φ(k)|² = (4/9)[sin²(k₁/2) + sin²(k₂/2) + sin²((k₁ − k₂)/2)]`; hence `0 ≤ u(k) ≤ 1` with `u = 1` iff `k ∈ 2πZ²`, i.e. only at the zero mode of the torus. *Proof.* `9|φ|² = 3 + 2cos k₁ + 2cos k₂ + 2cos(k₁ − k₂)` and `1 − cos x = 2 sin²(x/2)` (B1, symbolic). ∎

**T1.3 (the mode variances).** With `θ̂_k(t+1) = φ(k) θ̂_k(t) + ξ̂_k(t)` from `θ̂_k(0) = 0`: `Var θ̂_k(t) = σ²(1 − u^t)/(1 − u)` for `u = u(k) < 1` and `σ²t` at the zero mode; so `Var θ̄_t = σ²t/L²` per component and `v_t = (σ²/L²)[t + Σ_{k≠0}(1 − u_k^t)/(1 − u_k)]`. *Proof.* The noises are independent across levels; the spatial covariance is diagonal. Real-field conjugate modes need not be independent; the variance recursion `V(t+1) = uV(t) + σ²` sums geometrically (B2). ∎

## Theorem T2 — the tiny tori

On the tori `L = 2, 3, 4` the cosines `cos(2πn/L)` are rational, so `u_k` and the mode formula are rational; the covariance matrix of the field obeys `Σ_{t+1} = PΣ_tPᵀ + σ²I` from `Σ_0 = 0`, with `P` a rational `L² × L²` matrix. The runner iterates the recursion exactly for `t ≤ 12` (`L = 2, 3`) and `t ≤ 8` (`L = 4`) and finds the site variance `tr Σ_t/L²` equal to the mode formula and the plane-average variance `1ᵀΣ_t1/L⁴` equal to `t/L²` at every level (C1); the exact `V_L` of these tori lies inside T3's bracket (C2).

## Theorem T3 — the memory time and the bracket

**T3.1 (the memory time).** `τ_L = L²/σ² = 3βL²/A(3β)` is the level at which the plane average's variance per component reaches one; the exact proxy is `e^{−v_t} = e^{−V_L(t)} e^{−t/τ_L}` with `V_L(t) ↑ V_L`, so it decays exponentially at the rate `1/τ_L = A(3β)/(3βL²)`. The runner encloses `τ_L` to width below `1/10` at `β = 6, 12, 24, 48` and `L = 16, 32, 64` through the exact enclosure of `A(3β)` (D1): `τ ∈ [4879, 4880]`, `[19516, 19517]`, `[78064, 78065]` at `β = 6`; `[9479, 9480]` at `(12, 16)`; `[18691, 18692]` at `(24, 16)`; `[37121, 37122]` at `(48, 16)`. The approach of V_L(t) to V_L is controlled by the largest nonzero u(k), not by the variance V_L as a time scale. No infinite-plane result is imported here.

**T3.2 (the bracket).** `M` has eigenvalues `1/9` and `1/3`; from `sin²(x/2) ≤ x²/4` (all `x`) one has `1 − u ≤ Q(k) ≤ |k|²/3`, and from `sin(x/2) ≥ x/π` on `[0, π]` one has `1 − u ≥ (4/(9π²))|k|²` for the representative with `|k_i| ≤ π`; with `|k|² = (2π/L)²|n|²`,
```
(3/(4π²)) σ² S_L  ≤  V_L  ≤  (9/16) σ² S_L .
```
(D2: the eigenvalues symbolically; the sine inequalities on an exact grid; the bracket on the tiny tori.) The lattice sums are rational; `S_16, S_32, S_64` increase and consecutive differences lie within one of `2π log 2` (D3), the discrete counterpart of `S_L = 2π log L + O(1)`. Author-reported offsets V_L/sigma^2 - 2c_0 log L were 0.3514, 0.3525, 0.3527, 0.3528 at L=16,32,64,128, with c_0=3sqrt(3)/(4pi). These four values do not prove a limiting offset, an o(1) remainder or equality to the infinite-plane spread at t=L^2.

## Historical nonlinear observations (not fresh evidence)

The following table is preserved from the original author submission. Original simulation scripts, outputs and failed exponential-fit estimator remain recoverable on the original PR branch. They are not included in the current canonical runner certificate. The listed samples neither prove size independence nor a limiting coefficient, an exact phase or a universal memory law.

| `β` | `L` | `σ²/L²` | `τ_L` | `|m|` (stationary) | `D_1/(σ²/L²)` at lags `25, 100, 1000` | linear model, same estimator | `1/|m|²` |
|---|---|---|---|---|---|---|---|
| 6 | 16 | `2.050·10⁻⁴` | `4879` | `0.844` | `1.34, 1.33, 1.27` | `0.99, 0.98, 1.00` | `1.40` |
| 6 | 32 | `5.124·10⁻⁵` | `19516` | `0.809` | `1.42, 1.42, 1.38` | `1.01, 0.99, 0.97` | `1.53` |
| 12 | 16 | `1.055·10⁻⁴` | `9479` | `0.924` | `1.14, 1.14, 1.12` | `1.00, 0.99, 1.01` | `1.17` |
| 12 | 32 | `2.637·10⁻⁵` | `37917` | `0.908` | `1.17, 1.19, 1.21` | `1.01, 1.00, 0.96` | `1.21` |
| 24 | 16 | `5.350·10⁻⁵` | `18692` | `0.963` | `1.06, 1.06, 1.00` | `1.01, 1.00, 1.01` | `1.08` |
| 48 | 16 | `2.694·10⁻⁵` | `37122` | `0.982` | `1.02, 1.02, 1.00` | `1.00, 1.00, 0.98` | `1.04` |

## Boundaries, falsifiers and imports

No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.

No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

A wrong covariance, multiplier, enclosure or Green recurrence falsifies its stated identity. The finite controls do not prove nonlinear asymptotics, physical anisotropy, a gravitational field or the selection of a model. No audit verdict is applied. Standard finite probability, character diagonalization and elementary series are the mathematical tools.

## Review record

The original author's experiments and review claims are historical provenance. This revision corrects the gain assumption, mode independence and transient-time interpretation. The current certificate is the fresh canonical runner output; independent review evidence is recorded by the landing receipt.

## Verification

```bash
python3 scripts/admissibility_rule_unsoldered_formation_law_torus_memory_time_zero_mode_rate_exactly_stationary_modes_bracketed_nonlinear_law_measured_2026_09_17.py
```

Cached output: `logs/runner-cache/admissibility_rule_unsoldered_formation_law_torus_memory_time_zero_mode_rate_exactly_stationary_modes_bracketed_nonlinear_law_measured_2026_09_17.txt`.
