---
claim_id: ring_model_on_16_cubed_the_projector_energy_depends_on_the_guide_by_six_standard_errors_and_the_effective_population_stays_below_twenty_five_bounded_theorem_note_2026-10-01
claim_type: bounded_theorem
claim_scope: "Recorded finite seeded sampler results for the supplied ring model and the full settings in the body. Numerical matrix controls and nominal bin/seed errors only; no certified spectrum, bias, convergence, component connectivity, physical identification or audit verdict."
upstream_dependencies:
  - minimal_axioms
  - ring_model_energy_only_bounds_on_the_pure_ring_photon_from_the_mode_averaged_transverse_susceptibility_bounded_theorem_note_2026-09-25
  - ring_model_on_16_cubed_a_longer_projection_leaves_the_energy_unchanged_and_moves_the_curvature_estimate_within_its_errors_bounded_theorem_note_2026-09-28
runner: scripts/ring_model_projector_energy_offset_depends_on_the_guide_and_the_population_2026_10_01.py
---

# Recorded 16³ projector diagnostics: the energy depends on the guide, and the effective population stays below 25

**Date:** 2026-10-01
**Type:** bounded_theorem
**Status:** recorded finite Monte Carlo diagnostics for a supplied model; unaudited.

## Supplied setting

The model is the pure ring Hamiltonian `H = −Σ_p (U_p + U_p†)` at `V = 0`, on the
intended canonical zero-winding flip component of the cubic `L³` torus. The actual loop-prepared initial banks have the component qualification below. The reference setting appears in
[RING_MODEL_ON_16_CUBED_A_LONGER_PROJECTION_LEAVES_THE_ENERGY_UNCHANGED_AND_MOVES_THE_CURVATURE_ESTIMATE_WITHIN_ITS_ERRORS_BOUNDED_THEOREM_NOTE_2026-09-28](RING_MODEL_ON_16_CUBED_A_LONGER_PROJECTION_LEAVES_THE_ENERGY_UNCHANGED_AND_MOVES_THE_CURVATURE_ESTIMATE_WITHIN_ITS_ERRORS_BOUNDED_THEOREM_NOTE_2026-09-28.md).

- **Projector.** A fixed-population, continuous-time, importance-sampled walk,
  resampled every `Δτ = 0.015`.
- **Energy.** `u = −E/(3N)`, the mixed estimator.
- **Old guide.** `ψ = exp(0.2 N_flip)`.
- **Pair guide.** `ψ = exp(α N_flip + γ N_pair)`, where `N_pair` counts adjacent
  pairs of flippable plaquettes. The 8³ and 16³ runs use `α = 0.35`, `γ = −0.049`.

For exact-distribution evolution in one finite connected component, a positive guide and nonzero positive preparation have ground overlap; the mixed energy tends to that component ground energy as projection time increases. Consistency of the implemented finite-population resampling limit is an additional obligation.

## Checks

1. **Implementation.** On random 4³ states, the pair guide's local energy and
   flip rates match brute-force evaluation to `7·10⁻¹⁵`. The incremental typed
   pair counts match exactly. The brute force evaluates `ψ` of each flipped state
   directly, with adjacency built independently.
2. **Exact 2³ component.** Two pair guides reproduce the exact ground energy
   `E₀ = −9.026721` within 3 standard errors of eight independent runs. The
   offsets are `−0.66` and `+0.06` errors.

## Recorded diagnostics

**8³, 960 walkers, two seeds:**

| Guide | `u(Lc = 0)` | `u(Lc = 40)` | distinct ancestors, lag 2 | `sd(E_L)` |
|---|---|---|---|---|
| old | `0.28863 ± 0.00009` | `0.28869` | `0.0251` | `6.55` |
| pair | `0.28873 ± 0.00002` | `0.28883` | `0.0431` | `4.81` |

**16³, 960 walkers, seed 1:**

| Guide | `u(Lc = 0)` | `u(Lc = 40)` | distinct ancestors, lag 2 | `sd(E_L)` |
|---|---|---|---|---|
| old | `0.28687 ± 0.00009` | `0.28749` | `0.0014` | `17.6` |
| pair | `0.28755 ± 0.00007` | `0.28814` | `0.0020` | `12.9` |

The two recorded 16³ means differ by `0.00068`, or 5.9 nominal combined bin errors. This is a convergence diagnostic, not a calibrated rejection of a common mean or proof that either estimator has a specified bias. Correlated bins and a single seed do not give certified uncertainty or the converged value.

**16³, old guide, seed 1, population series:**

| `N_w` | `u(Lc = 0)` | `N_eff` |
|---|---|---|
| 240 | `0.28606 ± 0.00010` | 9.3 |
| 480 | `0.28662 ± 0.00011` | 10.3 |
| 960 | `0.28664 ± 0.00004` | 24.6 |
| 1920 | `0.28699 ± 0.00008` | 15.6 |

- `N_eff` is the mean walker variance of the local energy divided by the
  generation variance of its population mean.
- It stays between 9 and 25 while the population grows eightfold.
- A fit `u = u_∞ − cN_w^{−k}` is not constrained: its best exponent sits at the
  grid bound.
- This series uses a second code path. Its 960-walker value (`0.28664`) and the
  value in the guide comparison (`0.28687`) differ by about 2.3 combined bin errors.

## Reading

These are recorded finite diagnostics.
- The two recorded 16³ estimates span approximately `0.0007` per plaquette; this is not an enclosure of the energy.
- That is comparable to the earlier 8³-to-16³ decrease of about `0.0017`.
- The recorded variance-ratio diagnostic is nonmonotone over this range. It is not a certified number of independent walkers.

## What this does not establish

- No converged energy or bias magnitude.
- No population or projection convergence law.
- No certified eigenvalue.
- No physical identification.
- No audit verdict.

Bin errors are 10-bin errors and are lower bounds under autocorrelation. Runs
use one seed unless stated.

## Evidence limits and No-Go Discipline Gate

- **N1:** supplied model; the stated tori, guides and populations.
- **N2:** no phase or no-go wall is imported.
- **N3:** the Hamiltonian, component and guides remain supplied.
- **N4:** the landed component and estimator are used as stated there.
- **N5:** recorded Monte Carlo diagnostics, plus brute-force and exact-2³ implementation checks.
- **N6:** converged values remain open.
- **N7:** other guides, populations and estimators remain available.
- **N8:** no physical identification, new premise or audit verdict.

## Reproduction

```bash
python3 scripts/ring_model_projector_energy_offset_depends_on_the_guide_and_the_population_2026_10_01.py
```

Seven checks; prints `TOTAL: PASS=7 FAIL=0` in about one hour (single thread).

## Reviewed interpretation and preparation boundary

The larger-torus initial banks are prepared by zero-winding loop moves from a canonical start. Such loop moves preserve Gauss law and winding but have not been proved to remain in the canonical plaquette-flip component; every subsequent plaquette trajectory stays in its own component. The frozen-family theorem in this batch demonstrates why zero winding alone is insufficient. No all-start or 16³ component certificate is imported. Ideal selected-component ground-state identities remain conditional, with response symmetry and centered positive measure required by the current moment parent.

All numerical matrix eigenvalues are floating-point references, not rigorous enclosures. Bin/seed errors and their quadrature sums are nominal diagnostics; field, window and guide covariance and mixing are not certified. A variance-ratio labelled N_eff is not a number of independent samples. Finite-path motion in reptation does not bound equilibrium or path-length error. Population-free sampling removes walker resampling only. The tables report captured seeded means; they supply no convergence certificate or causal attribution. Historical runner introductory prose and console labels must be read within this corrected scope.

Original source and captured evidence remain recoverable through [PR #9434](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/9434) at frozen head `10c82780df967ba1f723eac54a7c2aaa9f4278f3`. Review grants no audit status.

## Actual source dependencies

- [MINIMAL_AXIOMS_2026-06-29](MINIMAL_AXIOMS_2026-06-29.md): conditional definitions or the recorded finite comparison only.
- [RING_MODEL_ENERGY_ONLY_BOUNDS_ON_THE_PURE_RING_PHOTON_FROM_THE_MODE_AVERAGED_TRANSVERSE_SUSCEPTIBILITY_BOUNDED_THEOREM_NOTE_2026-09-25](RING_MODEL_ENERGY_ONLY_BOUNDS_ON_THE_PURE_RING_PHOTON_FROM_THE_MODE_AVERAGED_TRANSVERSE_SUSCEPTIBILITY_BOUNDED_THEOREM_NOTE_2026-09-25.md): conditional definitions or the recorded finite comparison only.
- [RING_MODEL_THE_ZERO_WINDING_GAUSS_SECTOR_HAS_FROZEN_FLIP_COMPONENTS_ON_EVERY_EVEN_TORUS_BOUNDED_THEOREM_NOTE_2026-10-01](RING_MODEL_THE_ZERO_WINDING_GAUSS_SECTOR_HAS_FROZEN_FLIP_COMPONENTS_ON_EVERY_EVEN_TORUS_BOUNDED_THEOREM_NOTE_2026-10-01.md): conditional definitions or the recorded finite comparison only.
