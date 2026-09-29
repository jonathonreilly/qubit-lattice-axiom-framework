---
claim_id: ring_model_the_guide_scheme_split_of_the_curvature_estimate_grows_with_the_torus_and_on_8_cubed_is_about_0_05_with_or_without_a_walker_population_bounded_theorem_note_2026-09-26
claim_type: bounded_theorem
claim_scope: "Recorded finite projector/reptation or Ritz diagnostics at the complete parameter grid in the body, for the supplied ring Hamiltonian and explicit guides. Conditional parent spectral identities remain conditional; printed seed/bin errors and sigma ratios are descriptive. No certified eigenvalue, susceptibility, population/projection convergence, bias attribution, limiting law, spectral reconstruction, physical identification or audit verdict."
upstream_dependencies:
  - minimal_axioms
  - ring_model_energy_only_bounds_on_the_pure_ring_photon_from_the_mode_averaged_transverse_susceptibility_bounded_theorem_note_2026-09-25
  - ring_model_energy_only_photon_bound_holds_on_the_20_cubed_torus_with_the_transverse_susceptibility_near_one_down_to_k_pi_over_10_bounded_theorem_note_2026-09-25
runner: scripts/ring_model_8_cubed_curvature_guide_scheme_split_with_and_without_a_walker_population_2026_09_26.py
---

# The guide-scheme split of the curvature estimate grows with the torus; on 8³ it is about 0.05 with or without a walker population

**Date:** 2026-09-26
**Type:** bounded_theorem
**Status:** finite diagnostics; unaudited.

## Supplied setting

Use the supplied Hamiltonian, cyclic transverse modes, probe fields and
conditional moment identities of the landed ring-component note
[RING_MODEL_ENERGY_ONLY_BOUNDS_ON_THE_PURE_RING_PHOTON_FROM_THE_MODE_AVERAGED_TRANSVERSE_SUSCEPTIBILITY_BOUNDED_THEOREM_NOTE_2026-09-25](RING_MODEL_ENERGY_ONLY_BOUNDS_ON_THE_PURE_RING_PHOTON_FROM_THE_MODE_AVERAGED_TRANSVERSE_SUSCEPTIBILITY_BOUNDED_THEOREM_NOTE_2026-09-25.md).
The curvature estimate `χ` comes from `E(0)`, `E(H₁)` and `E(2H₁)`, with
`H₁ = 0.15`, as in
[RING_MODEL_ENERGY_ONLY_PHOTON_BOUND_HOLDS_ON_THE_20_CUBED_TORUS_WITH_THE_TRANSVERSE_SUSCEPTIBILITY_NEAR_ONE_DOWN_TO_K_PI_OVER_10_BOUNDED_THEOREM_NOTE_2026-09-25](RING_MODEL_ENERGY_ONLY_PHOTON_BOUND_HOLDS_ON_THE_20_CUBED_TORUS_WITH_THE_TRANSVERSE_SUSCEPTIBILITY_NEAR_ONE_DOWN_TO_K_PI_OVER_10_BOUNDED_THEOREM_NOTE_2026-09-25.md).

Open PR 9328 found that the fixed-population projector's estimate depends on
how the guide field is chosen. The two schemes are one guide field for the
three probe fields (`0.5 H₁` times the pattern) and a guide per field
(`0.5 h`). On 16³ they give `1.307 ± 0.029` and `1.039 ± 0.022`. That note
asked for an estimator without population bias. This block supplies one on
8³ and measures how the scheme difference changes with the torus.

## Estimator

Each reptation energy is the mixed estimate at the two ends of one path, so
no walker population is used:
- the path is 1600 segments of imaginary time 0.025 (total 40), generated
  by the importance-sampled jump process of the guide;
- a move grows one segment at the leading end, removes one at the trailing
  end, and is accepted with probability `min(1, exp(W_new − W_old))`, where
  `W` is minus the integrated local energy of a segment;
- on rejection the growth direction reverses.

For a path long enough to reach its stationary distribution, the mixed
energy at the ends does not depend on the guide. The guide is
`exp(0.2 N_flip + b Σ_l hv_l σ_l)`, where `b` is the guide field.

## Result

- **Controls.**
  - The rate tables and local energy agree with brute-force wave-function
    ratios on 4³ with charges present (largest difference `1.4e-14`).
  - On the exact 2³ canonical flip component the reptation energies lie
    within `+0.5`, `0.0` and `−0.7` standard errors of exact
    diagonalization.
  - The 2³ curvature estimate is `1.469 ± 0.027`, against the exact
    three-point value `1.4604`.
- **Reptation on 8³ at `k = π/4`.**
  - One guide for the three fields: `E(0) = −443.303 ± 0.089`,
    `E(H₁) = −452.821 ± 0.060`, `E(2H₁) = −482.750 ± 0.124`; so
    `χ = 1.0884 ± 0.0159` and `u = 0.28861`.
  - A guide per field: the energies at `0` and `2H₁` are rerun with their own
    guides, and `E(H₁)` is shared. This gives `χ = 1.0413 ± 0.0156`, a
    difference of `−0.047` (2.1 standard errors).
- **Curvature estimates in both schemes:**

  | torus | method | one guide | a guide per field | difference |
  |---|---|---|---|---|
  | 8³ (`k = π/4`) | reptation, no population | `1.0884 ± 0.0159` | `1.0413 ± 0.0156` | `−0.047` (2.1σ) |
  | 8³ (`k = π/4`) | projector, 960 walkers | `1.1400 ± 0.0167` | `1.0821 ± 0.0382` | `−0.058` (1.4σ) |
  | 12³ (`k = π/6`) | projector, 960 walkers | `1.2520 ± 0.0221` | `1.0690 ± 0.0257` | `−0.183` (5.4σ) |
  | 16³ (`k = π/8`) | projector, 960 walkers (open PR 9328) | `1.307 ± 0.029` | `1.039 ± 0.022` | `−0.268` (7.4σ) |

  The projector runs use the settings of open PRs 9298 and 9328: 960
  walkers, projection 30, resampling interval 0.015, seeds 401 and 402. On
  8³ each projector estimate lies within three combined errors of the
  one-guide reptation value (`+2.2` and `−0.2`), and `u = 0.28837` and
  `0.28851`.
- **What follows.**
  - At this population the scheme difference grows with the torus.
  - On 8³ it is about `0.05` both with and without a walker population, and
    all four 8³ estimates lie between `1.04` and `1.14`.
  - Across 8³, 12³ and 16³ the per-field values stay between `1.04` and
    `1.08`, while the one-guide values rise from `1.14` to `1.31`. This
    suggests that the one-guide scheme carries the growing error, but no
    population-free value beyond 8³ tests it here.
  - With the landed moment identity, the 8³ values give estimated upper
    bounds on the lowest transverse excitation at `k = π/4` of `0.81` to
    `0.77`, with `s = 2 sin(π/8)`.

## Estimator and reproduction boundary

- **Reptation uncertainty is not controlled.** Its errors come from twenty blocks
  of one path per field. The energy differences between the two guide
  schemes (2.4 and 2.9 block errors) do not establish a calibrated error budget or isolate sampling noise
  from finite-path and equilibration effects. A converged population-free estimate should not
  depend on the scheme, but the observed difference `0.047` is not a bound on either
  estimator's remaining convergence error.
- **No larger tori.** Reptation with this guide equilibrates much more
  slowly on larger tori, and no such run is part of the runner.

## Evidence limits and No-Go Discipline Gate

- **N1:** supplied finite ring component on 2³, 4³, 8³ and 12³ with the stated settings.
- **N2:** no phase or no-go wall is imported.
- **N3:** Hamiltonian, sector, guides and estimators remain supplied.
- **N4:** the landed parents' scopes govern; this block measures the size dependence of the scheme difference found in open PR 9328.
- **N5:** finite estimates; the scheme differences and their growth are the result.
- **N6:** a population-free value on 12³ and larger tori remains open.
- **N7:** other guides, path lengths, populations and estimators remain available.
- **N8:** no physical identification, new premise or audit verdict.

## Reproduction

```bash
python3 scripts/ring_model_8_cubed_curvature_guide_scheme_split_with_and_without_a_walker_population_2026_09_26.py
```

Six checks; prints `TOTAL: PASS=6 FAIL=0` in about an hour and a half of computation.

## Review boundary and evidence provenance

These are recorded finite-run diagnostics of supplied models. The full original
runner and its content-pinned successful output are retained; the long simulations
were not repeated during this landing review. Independent controls check the
rate algebra, normalization, reduction formulas and printed comparisons. Original
console labels and introductory runner prose are historical descriptions; this
note's corrected scope governs their interpretation.

Seed/bin errors and printed sigma ratios are descriptive, not calibrated coverage
or hypothesis tests. Shared fields, seeds, initialized populations and time
windows can induce covariance; unpaired quadrature errors do not estimate that
covariance. Matching two guides, populations, intervals or windows does not prove
convergence or absence of common bias. Cross-size energy differences cannot by
themselves isolate population error. Removing walker populations from reptation
does not remove finite-path, equilibration or component uncertainty.

The parent's energy-response symmetries, selected-component condition and centered
positive spectral measure remain necessary. The three-field curvature removes
the quartic term under an even response assumption but has residual field error.
Numerical plug-ins in exact moment inequalities are not certified excitation
frequencies, gaps, structure factors, phase or physical-particle statements.

## Compared source measurements

- [PR 9298 finite source](RING_MODEL_ENERGY_ONLY_PHOTON_BOUND_ON_THE_24_CUBED_TORUS_THE_TRANSVERSE_SUSCEPTIBILITY_AT_K_PI_OVER_12_STAYS_FINITE_WITH_A_SOFTENING_NOT_RESOLVED_BOUNDED_THEOREM_NOTE_2026-09-26.md).
- [PR 9328 finite source](RING_MODEL_ENERGY_CURVATURE_ESTIMATES_DEPEND_ON_THE_GUIDE_SCHEME_BY_ABOUT_A_QUARTER_ON_16_AND_24_CUBED_BOUNDED_THEOREM_NOTE_2026-09-26.md).

[Current axiom memo](MINIMAL_AXIOMS_2026-06-29.md).

Historical filenames and claim identifiers remain stable; the scoped body governs.
