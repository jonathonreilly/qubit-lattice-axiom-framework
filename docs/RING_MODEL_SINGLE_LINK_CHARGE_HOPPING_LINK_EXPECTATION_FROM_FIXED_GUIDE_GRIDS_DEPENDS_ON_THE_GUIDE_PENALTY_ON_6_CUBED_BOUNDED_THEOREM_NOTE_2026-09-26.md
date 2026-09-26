---
claim_id: ring_model_single_link_charge_hopping_link_expectation_from_fixed_guide_grids_depends_on_the_guide_penalty_on_6_cubed_bounded_theorem_note_2026-09-26
claim_type: bounded_theorem
claim_scope: Finite-dimensional ground-energy concavity and an exact finite-difference decomposition of guide-dependent
  estimator bias. Full fixed-guide grids provide numerical guide-sensitivity diagnostics on4/6tori with heuristic
  errors; derivative forms require smoothness and truncation remainders. No guide-independent expectation, slope,
  transition or size trend is established.
upstream_dependencies:
- minimal_axioms
- ring_model_energy_only_bounds_on_the_pure_ring_photon_from_the_mode_averaged_transverse_susceptibility_bounded_theorem_note_2026-09-25
- ring_model_with_single_link_charge_hopping_changes_rapidly_between_weak_and_strong_hopping_and_its_moment_bound_stays_finite_at_small_momentum_bounded_theorem_note_2026-09-25
runner: scripts/ring_model_single_link_charge_hopping_guide_dependence_of_fixed_guide_energy_grids_2026_09_26.py
---

# Fixed-guide hopping grids: finite differences and guide sensitivity

**Type:** bounded_theorem
**Status:** exact finite-difference algebra and finite diagnostics; unaudited.

## Setting

Use the actual linked supplied single-link model at g=1,M=2, with sign-free projector,1920walkers, projection30, interval0.05 and four/three seeds on4/6tori. Each whole hopping grid0.25,...,0.55 fixes gamma at0.8 or1.1. Initial loop samples are reused within each grid; seed/bin errors are heuristic and cross-energy covariance is omitted in the printed propagation. Calibration, finite projection, population and initialization biases remain uncontrolled. The six-link184320-state control is a restricted reachable component, not the full24-link charge model.

## Exact finite-difference identities

E0(t)=inf_psi <psi|H0-t X|psi> is concave as an infimum of affine functions. Therefore E0(t+delta)-2E0(t)+E0(t-delta)<=0. The *negative* second difference divided by N_l delta² is nonnegative. Hellmann-Feynman gives <sigma_x>=-E0'/N_l on differentiable branches; at crossings the appropriate one-sided slopes replace a derivative.

Write the expectation of the finite estimator as Ehat_gamma(t)=E0(t)+b_gamma(t), with b covering all systematic estimator errors; random noise is additional. Define D_delta f=[f(t+delta)-f(t-delta)]/(2delta). Then the estimated link difference is exactly -D_delta E0/N_l-D_delta b_gamma/N_l. The difference between two guide grids is exactly -D_delta(b_0.8-b_1.1)/N_l at the expectation level; observed grids add random noise. The derivative form -(b_0.8'-b_1.1')/N_l has an O(delta²) remainder only under adequate smoothness. Constant bias cancels; t-dependent bias does not. A vanishing gap need not mean either guide is unbiased.

## Numerical scope

The runner checks agreement of both guides with a small floating-point control and reports finite-difference grids. Its concavity diagnostic allows negative estimates within four heuristic standard errors, so PASS is neither exact monotonicity nor a rigorous statistical confidence statement. The author's tables below display guide dependence; fresh stdout is the reproduction record. No claim about a ground-state rapid-change location, slope, size trend, crossover or transition follows. The motivation from an unreviewed draft is not evidence used by this result.

## Diagnostic 1 — the fixed-guide grids

`⟨σ^x⟩(t)` from central differences of step 0.05; errors in the last
digits.

| torus | `γ` | `t = 0.30` | `0.35` | `0.40` | `0.45` | `0.50` |
|---|---|---|---|---|---|---|
| 4³ | 0.8 | 0.1301(29) | 0.1521(40) | 0.2193(26) | 0.3427(30) | 0.4487(20) |
| 4³ | 1.1 | 0.1355(23) | 0.1580(19) | 0.2052(35) | 0.3108(41) | 0.4179(63) |
| 4³ | gap | −0.0054 (−1.5 σ) | −0.0059 (−1.4 σ) | +0.0141 (+3.2 σ) | +0.0319 (+6.3 σ) | +0.0309 (+4.6 σ) |
| 6³ | 0.8 | 0.1544(67) | 0.2287(49) | 0.3005(34) | 0.3810(47) | 0.4518(17) |
| 6³ | 1.1 | 0.1136(19) | 0.1521(34) | 0.2432(24) | 0.3372(35) | 0.3893(71) |
| 6³ | gap | +0.0408 (+5.9 σ) | +0.0766 (+12.9 σ) | +0.0574 (+13.7 σ) | +0.0439 (+7.5 σ) | +0.0625 (+8.6 σ) |

Slopes from second differences of step 0.1 (errors in hundredths):

| torus | `γ` | `t = 0.35` | `0.40` | `0.45` |
|---|---|---|---|---|
| 4³ | 0.8 | 0.89(5) | 1.91(6) | 2.29(4) |
| 4³ | 1.1 | 0.70(5) | 1.53(5) | 2.13(8) |
| 6³ | 0.8 | 1.46(9) | 1.52(9) | 1.51(4) |
| 6³ | 1.1 | 1.30(4) | 1.85(6) | 1.46(8) |


## Evidence limits and No-Go Discipline Gate

- **N1:** supplied finite Hamiltonian and stated grid.
- **N2:** independent review controls are distinct from primary reproduction.
- **N3:** clauses, guide and comparator remain supplied.
- **N4:** actual linked parent scope controls.
- **N5:** floating-point and finite stochastic evidence; heuristic errors.
- **N6:** guide/population/projection and finite-difference control remain open.
- **N7:** alternative guides, components and soft spectral weights remain possible.
- **N8:** no physical identification, new premise or audit verdict.

## Actual inputs

- [MINIMAL_AXIOMS_2026-06-29](MINIMAL_AXIOMS_2026-06-29.md)
- [RING_MODEL_ENERGY_ONLY_BOUNDS_ON_THE_PURE_RING_PHOTON_FROM_THE_MODE_AVERAGED_TRANSVERSE_SUSCEPTIBILITY_BOUNDED_THEOREM_NOTE_2026-09-25](RING_MODEL_ENERGY_ONLY_BOUNDS_ON_THE_PURE_RING_PHOTON_FROM_THE_MODE_AVERAGED_TRANSVERSE_SUSCEPTIBILITY_BOUNDED_THEOREM_NOTE_2026-09-25.md)
- [RING_MODEL_WITH_SINGLE_LINK_CHARGE_HOPPING_CHANGES_RAPIDLY_BETWEEN_WEAK_AND_STRONG_HOPPING_AND_ITS_MOMENT_BOUND_STAYS_FINITE_AT_SMALL_MOMENTUM_BOUNDED_THEOREM_NOTE_2026-09-25](RING_MODEL_WITH_SINGLE_LINK_CHARGE_HOPPING_CHANGES_RAPIDLY_BETWEEN_WEAK_AND_STRONG_HOPPING_AND_ITS_MOMENT_BOUND_STAYS_FINITE_AT_SMALL_MOMENTUM_BOUNDED_THEOREM_NOTE_2026-09-25.md)
