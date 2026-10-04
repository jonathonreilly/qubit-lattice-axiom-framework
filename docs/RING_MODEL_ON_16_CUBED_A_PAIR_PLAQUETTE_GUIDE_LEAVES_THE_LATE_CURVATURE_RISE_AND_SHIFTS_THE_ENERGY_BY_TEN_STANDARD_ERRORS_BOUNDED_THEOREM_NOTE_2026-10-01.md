---
claim_id: ring_model_on_16_cubed_a_pair_plaquette_guide_leaves_the_late_curvature_rise_and_shifts_the_energy_by_ten_standard_errors_bounded_theorem_note_2026-10-01
claim_type: bounded_theorem
claim_scope: "Recorded finite seeded sampler results for the supplied ring model and the full settings in the body. Numerical matrix controls and nominal bin/seed errors only; no certified spectrum, bias, convergence, component connectivity, physical identification or audit verdict."
upstream_dependencies:
  - minimal_axioms
  - ring_model_energy_only_bounds_on_the_pure_ring_photon_from_the_mode_averaged_transverse_susceptibility_bounded_theorem_note_2026-09-25
  - ring_model_on_16_cubed_the_curvature_estimate_also_rises_to_1_11_and_matches_24_cubed_window_by_window_bounded_theorem_note_2026-09-29
runner: scripts/ring_model_16_cubed_curvature_with_a_pair_plaquette_guide_beside_the_old_guide_2026_10_01.py
---

# Recorded 16³ diagnostics: a pair-plaquette guide leaves the late curvature rise and shifts the energy by ten standard errors

**Date:** 2026-10-01
**Type:** bounded_theorem
**Status:** recorded finite Monte Carlo diagnostics for a supplied model; unaudited.

## Supplied setting

The model is the pure ring Hamiltonian at `V = 0` with the cyclic transverse probe
fields of the landed ring-component notes. Its intended reference is the canonical zero-winding flip component of the 16³ torus, at `k = 2π/16`; the actual loop-prepared initial banks have the component qualification below.

The fixed-population projector uses:
- 960 walkers, seed 411, projection to 90 (6000 generations);
- three windows, `[7.5, 30)`, `[30, 60)` and `[60, 90)`;
- a guide field `0.5 h·hv` per probe field.

The curvature estimate is `χ = 4a/(3N)`, from E(0), E(H₁) and E(2H₁) with `H₁ = 0.15`.

Two positive guides run through the identical code and seed streams:
- **pair:** `ψ = exp(0.35 N_flip − 0.049 N_pair)`;
- **old:** `ψ = exp(0.2 N_flip)`, which is the pair kernel at `γ = 0`.

The landed note
[RING_MODEL_ON_16_CUBED_THE_CURVATURE_ESTIMATE_ALSO_RISES_TO_1_11_AND_MATCHES_24_CUBED_WINDOW_BY_WINDOW_BOUNDED_THEOREM_NOTE_2026-09-29](RING_MODEL_ON_16_CUBED_THE_CURVATURE_ESTIMATE_ALSO_RISES_TO_1_11_AND_MATCHES_24_CUBED_WINDOW_BY_WINDOW_BOUNDED_THEOREM_NOTE_2026-09-29.md)
recorded a slow late rise of `χ` with the old guide. This note asks whether that
rise changes with a guide that keeps more distinct ancestors.

## Checks

1. **Implementation.** On random 4³ and 3³ states, the field-extended pair kernel's
   local energy, rates and maintained tables agree with brute force to machine
   precision. Integer tables agree exactly.
2. **Exact 2³ control.** Both guides reproduce the exact field energies at
   `h = 0, 0.15, 0.3` within 1.4 combined errors of eight runs.

## Recorded diagnostics

| Window | χ (pair) | χ (old) | pair − old χ | u (pair) | u (old) | pair − old u |
|---|---|---|---|---|---|---|
| `[7.5, 30)` | 1.041 ± 0.017 | 1.091 ± 0.022 | −0.050 ± 0.028 | 0.28748 | 0.28666 | +0.00082 (10.5 σ) |
| `[30, 60)` | 1.051 ± 0.021 | 1.099 ± 0.024 | −0.047 ± 0.032 | 0.28756 | 0.28676 | +0.00079 (9.6 σ) |
| `[60, 90)` | 1.091 ± 0.019 | 1.119 ± 0.019 | −0.029 ± 0.026 | 0.28744 | 0.28667 | +0.00077 (11.0 σ) |

- **Rise from the first to the last window.** Pair: `+0.050 ± 0.025`. Old:
  `+0.029 ± 0.029`. Difference: `+0.021 ± 0.038`.
- **Distinct ancestors at lag 2:** pair 0.0019–0.0020, old 0.0013–0.0017.
- **ESS fraction:** pair 0.964, old 0.937.
- **Landed old-guide values** in the same windows (a different kernel and stream,
  for comparison): χ = 1.026, 1.058, 1.113 at 960 walkers and 1.021, 1.086,
  1.105 at 1920 walkers.

## Reading

These are recorded finite diagnostics.
- **Energy.** The converged mixed estimator is the same for every positive guide.
  The differences of about ten nominal combined bin errors are guide-sensitivity diagnostics. They do not by themselves certify nonconvergence, bias magnitude or a calibrated significance; all uncertainties use correlated bins and one seed.
- **Curvature.** The pair-minus-old difference, and the difference between the
  two guides' rises, are within 2 combined errors. They are not resolved here.
- **The late rise.** Both guides show it. At these errors, the more varied
  ancestry of the pair guide does not remove it.

## What this does not establish

- No certified susceptibility.
- No converged energy.
- No convergence law.
- No physical identification.
- No audit verdict.

Each guide uses one seed. Errors are 10-bin errors, and the three windows share walkers.

## Evidence limits and No-Go Discipline Gate

- **N1:** supplied model, 16³, one seed per guide, the stated windows.
- **N2:** no phase or no-go wall is imported.
- **N3:** the Hamiltonian, component, probe fields and guides remain supplied.
- **N4:** the landed component, probe fields and estimator are used as stated there.
- **N5:** recorded Monte Carlo diagnostics, with brute-force and exact-2³ implementation checks.
- **N6:** converged values remain open.
- **N7:** other guides, seeds and populations remain available.
- **N8:** no physical identification, new premise or audit verdict.

## Reproduction

```bash
python3 scripts/ring_model_16_cubed_curvature_with_a_pair_plaquette_guide_beside_the_old_guide_2026_10_01.py
```

Four checks; prints `TOTAL: PASS=4 FAIL=0` in about 4.4 hours (single thread).

## Reviewed interpretation and preparation boundary

The larger-torus initial banks are prepared by zero-winding loop moves from a canonical start. Such loop moves preserve Gauss law and winding but have not been proved to remain in the canonical plaquette-flip component; every subsequent plaquette trajectory stays in its own component. The frozen-family theorem in this batch demonstrates why zero winding alone is insufficient. No all-start or 16³ component certificate is imported. Ideal selected-component ground-state identities remain conditional, with response symmetry and centered positive measure required by the current moment parent.

All numerical matrix eigenvalues are floating-point references, not rigorous enclosures. Bin/seed errors and their quadrature sums are nominal diagnostics; field, window and guide covariance and mixing are not certified. A variance-ratio labelled N_eff is not a number of independent samples. Finite-path motion in reptation does not bound equilibrium or path-length error. Population-free sampling removes walker resampling only. The tables report captured seeded means; they supply no convergence certificate or causal attribution. Historical runner introductory prose and console labels must be read within this corrected scope.

Original source and captured evidence remain recoverable through [PR #9442](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/9442) at frozen head `30ba4d52916d39f01e464029030ac4033dcb1f35`. Review grants no audit status.

## Actual source dependencies

- [MINIMAL_AXIOMS_2026-06-29](MINIMAL_AXIOMS_2026-06-29.md): conditional definitions or the recorded finite comparison only.
- [RING_MODEL_ENERGY_ONLY_BOUNDS_ON_THE_PURE_RING_PHOTON_FROM_THE_MODE_AVERAGED_TRANSVERSE_SUSCEPTIBILITY_BOUNDED_THEOREM_NOTE_2026-09-25](RING_MODEL_ENERGY_ONLY_BOUNDS_ON_THE_PURE_RING_PHOTON_FROM_THE_MODE_AVERAGED_TRANSVERSE_SUSCEPTIBILITY_BOUNDED_THEOREM_NOTE_2026-09-25.md): conditional definitions or the recorded finite comparison only.
- [RING_MODEL_ON_16_CUBED_THE_PROJECTOR_ENERGY_DEPENDS_ON_THE_GUIDE_BY_SIX_STANDARD_ERRORS_AND_THE_EFFECTIVE_POPULATION_STAYS_BELOW_TWENTY_FIVE_BOUNDED_THEOREM_NOTE_2026-10-01](RING_MODEL_ON_16_CUBED_THE_PROJECTOR_ENERGY_DEPENDS_ON_THE_GUIDE_BY_SIX_STANDARD_ERRORS_AND_THE_EFFECTIVE_POPULATION_STAYS_BELOW_TWENTY_FIVE_BOUNDED_THEOREM_NOTE_2026-10-01.md): conditional definitions or the recorded finite comparison only.
- [RING_MODEL_THE_ZERO_WINDING_GAUSS_SECTOR_HAS_FROZEN_FLIP_COMPONENTS_ON_EVERY_EVEN_TORUS_BOUNDED_THEOREM_NOTE_2026-10-01](RING_MODEL_THE_ZERO_WINDING_GAUSS_SECTOR_HAS_FROZEN_FLIP_COMPONENTS_ON_EVERY_EVEN_TORUS_BOUNDED_THEOREM_NOTE_2026-10-01.md): conditional definitions or the recorded finite comparison only.
