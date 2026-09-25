---
claim_id: ring_model_pure_ring_point_transverse_fluctuations_at_the_smallest_momentum_are_a_third_of_the_uniform_ice_constant_and_the_feynman_photon_bound_shows_no_resolved_power_on_small_tori_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: Conditional ground-state f-sum and finite transverse-mode estimates.
  Supplied finite-model identities and explicitly biased finite numerical diagnostics
  only; no phase, convergence certificate or new framework premise.
upstream_dependencies:
- ring_model_projector_monte_carlo_at_the_pure_ring_point_energies_below_variational_and_no_growth_of_plaquette_order_bounded_theorem_note_2026-09-24
- ring_model_winding_sector_splittings_resolved_on_the_small_tori_and_a_multi_exponential_relaxation_at_the_pure_ring_point_bounded_theorem_note_2026-09-24
- uniform_ice_rk_photon_single_mode_bound_is_quadratic_with_the_sum_rule_stiffness_bounded_theorem_note_2026-09-23
- minimal_axioms
runner: scripts/ring_model_pure_ring_point_feynman_photon_bound_and_pure_structure_factor_at_the_smallest_momentum_2026_09_24.py
---

# Conditional ground-state f-sum and finite transverse-mode estimates

**Type:** bounded_theorem
**Status:** conditional finite mathematics and numerical diagnostics; unaudited.

Supply g>0 (the numerical runs use g=1), H=-g sum_p R_p, R_p=U_p+U_p†, and a real normalized ground vector psi in a chosen connected flip component. For diagonal complex O, the double commutator has matrix elements [O†,[H,O]]_ij=-|O_i-O_j|² H_ij. In a ground eigenstate, half its expectation is the average of the O and O† excitation numerators; these coincide for real H and real psi. The equality need not hold in an arbitrary noneigenstate.

Let O_b(k e_a)=N^(-1/2) sum_x exp(ik x_a) sigma_b(x), a≠b. Average over the six axis/polarization choices. A plaquette affects two of these modes, with squared increment 4s²/N, where s²=2-2cos(k). Hence the averaged numerator is (1/2)*(2/6)*(4s²/N)*g*sum_p <R_p> = 2g u s², with u=sum_p<R_p>/(3N). This averaging identity needs no cubic symmetry of the state; an individual mode instead involves its orientation-specific ring expectations.

The numerator divided by S=mean ||O psi||² is a Rayleigh quotient when S>0. It bounds the least energy in that vector family's spectral support. A positive-excitation bound additionally requires removal of **all** ground-space components. Nonzero momentum alone is insufficient on a disconnected flip graph. In a connected component the Perron ground state is unique, and centering O removes its ground overlap; the denominator then changes if its mean was nonzero. No unproved connectivity of the large zero-winding sector is assumed here.

The L=2 component control uses a complete dense numerical eigensystem, residual checks, and all coupled levels rather than a truncated eigsh multiplet. Its spectral correlation is a positive sum of decaying exponentials; the exact logarithmic effective rate decreases with time. Numerical residuals are not rigorous spectral enclosures.

The larger-torus forward-walking S, mixed energies, quotients and correlation rates are finite estimator outputs. The quotient plugged with these estimates is not itself a certified upper bound. Flat lag or rate estimates do not prove convergence, a single excitation, or the lowest gap. Reported error propagation omits covariance and energy uncertainty and is not necessarily conservative. Uniform-ice reference samples can mix winding sectors unlike the guided zero-winding runs. Earlier constants are historical reproducibility comparisons. Neither a few sizes nor an inferred static exponent establishes a photon or phase.

## Evidence limits and No-Go Discipline Gate

- **N1 — Domain:** the explicit supplied finite models, supports, boundaries and estimator settings above.
- **N2 — Independence:** primary reproduction is not independent verification; the combined review receipt records separate structural controls.
- **N3 — Imports:** link qubits, Gauss law, ring Hamiltonian, initial ensembles, projection and Gaussian comparators are supplied, not adopted framework premises.
- **N4 — Dependencies:** corrected parent scopes govern; filenames are historical identifiers, not stronger claims.
- **N5 — Resolution:** floating-point eigensystems and finite Monte Carlo are observations, not certified enclosures or limit theorems. Bin errors lack proved coverage or mixing bounds.
- **N6 — Deferred:** component connectivity, population/lag/projection convergence and infinite-volume physics require additional science.
- **N7 — Counterroutes:** alternative sectors, non-Gaussian states, finite-size effects and correlated estimator error remain available.
- **N8 — Boundary:** ordinary source review only; no audit verdict, retained grade or assembly decision.

## Falsifiers and verification

A counterexample satisfying the exact hypotheses refutes the corresponding identity. Failed numerical controls must be investigated and not relabelled as a new phase. The runner's numerical thresholds describe only its finite experiment. Successful fresh execution has exit zero and FAIL=0; its cache binds this source and its declared inputs.

## Inputs

- [RING_MODEL_PROJECTOR_MONTE_CARLO_AT_THE_PURE_RING_POINT_ENERGIES_BELOW_VARIATIONAL_AND_NO_GROWTH_OF_PLAQUETTE_ORDER_BOUNDED_THEOREM_NOTE_2026-09-24](RING_MODEL_PROJECTOR_MONTE_CARLO_AT_THE_PURE_RING_POINT_ENERGIES_BELOW_VARIATIONAL_AND_NO_GROWTH_OF_PLAQUETTE_ORDER_BOUNDED_THEOREM_NOTE_2026-09-24.md): corrected conditional definitions and boundaries.
- [RING_MODEL_WINDING_SECTOR_SPLITTINGS_RESOLVED_ON_THE_SMALL_TORI_AND_A_MULTI_EXPONENTIAL_RELAXATION_AT_THE_PURE_RING_POINT_BOUNDED_THEOREM_NOTE_2026-09-24](RING_MODEL_WINDING_SECTOR_SPLITTINGS_RESOLVED_ON_THE_SMALL_TORI_AND_A_MULTI_EXPONENTIAL_RELAXATION_AT_THE_PURE_RING_POINT_BOUNDED_THEOREM_NOTE_2026-09-24.md): corrected conditional definitions and boundaries.
- [MINIMAL_AXIOMS_2026-06-29](MINIMAL_AXIOMS_2026-06-29.md): corrected conditional definitions and boundaries.
- [UNIFORM_ICE_RK_PHOTON_SINGLE_MODE_BOUND_IS_QUADRATIC_WITH_THE_SUM_RULE_STIFFNESS_BOUNDED_THEOREM_NOTE_2026-09-23](UNIFORM_ICE_RK_PHOTON_SINGLE_MODE_BOUND_IS_QUADRATIC_WITH_THE_SUM_RULE_STIFFNESS_BOUNDED_THEOREM_NOTE_2026-09-23.md): corrected conditional definitions and boundaries.

## Review record

Original PR #9161, frozen head `3bc88bce2ee80024795fa3fcd3f50bc324495fb3`. Original note and complete runner reviewed in one primary session without subagents. The original branch and frozen patch remain recovery handles for deferred work. Historical titles and claim identifiers remain stable; this body and scope govern. Fresh controls and same-session affected-fix confirmation are recorded in the combined landing receipt.

```bash
python3 scripts/ring_model_pure_ring_point_feynman_photon_bound_and_pure_structure_factor_at_the_smallest_momentum_2026_09_24.py
```
