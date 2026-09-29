---
claim_id: ring_model_on_24_cubed_the_per_field_curvature_estimate_holds_when_the_population_doubles_bounded_theorem_note_2026-09-27
claim_type: bounded_theorem
claim_scope: "Recorded finite projector/reptation or Ritz diagnostics at the complete parameter grid in the body, for the supplied ring Hamiltonian and explicit guides. Conditional parent spectral identities remain conditional; printed seed/bin errors and sigma ratios are descriptive. No certified eigenvalue, susceptibility, population/projection convergence, bias attribution, limiting law, spectral reconstruction, physical identification or audit verdict."
upstream_dependencies:
  - minimal_axioms
  - ring_model_energy_only_bounds_on_the_pure_ring_photon_from_the_mode_averaged_transverse_susceptibility_bounded_theorem_note_2026-09-25
  - ring_model_energy_only_photon_bound_holds_on_the_20_cubed_torus_with_the_transverse_susceptibility_near_one_down_to_k_pi_over_10_bounded_theorem_note_2026-09-25
runner: scripts/ring_model_24_cubed_per_field_curvature_doubled_population_2026_09_27.py
---

# On 24³ the per-field curvature estimate holds when the population doubles

**Date:** 2026-09-27
**Type:** bounded_theorem
**Status:** finite projector diagnostics; unaudited.

## Supplied setting

Use the supplied Hamiltonian, cyclic transverse modes, probe fields and
conditional moment identities of the landed ring-component note
[RING_MODEL_ENERGY_ONLY_BOUNDS_ON_THE_PURE_RING_PHOTON_FROM_THE_MODE_AVERAGED_TRANSVERSE_SUSCEPTIBILITY_BOUNDED_THEOREM_NOTE_2026-09-25](RING_MODEL_ENERGY_ONLY_BOUNDS_ON_THE_PURE_RING_PHOTON_FROM_THE_MODE_AVERAGED_TRANSVERSE_SUSCEPTIBILITY_BOUNDED_THEOREM_NOTE_2026-09-25.md).
The curvature estimate `χ` comes from `E(0)`, `E(H₁)` and `E(2H₁)`, with
`H₁ = 0.15` and a guide field per probe field (`0.5 h`), the scheme of
[RING_MODEL_ENERGY_ONLY_PHOTON_BOUND_HOLDS_ON_THE_20_CUBED_TORUS_WITH_THE_TRANSVERSE_SUSCEPTIBILITY_NEAR_ONE_DOWN_TO_K_PI_OVER_10_BOUNDED_THEOREM_NOTE_2026-09-25](RING_MODEL_ENERGY_ONLY_PHOTON_BOUND_HOLDS_ON_THE_20_CUBED_TORUS_WITH_THE_TRANSVERSE_SUSCEPTIBILITY_NEAR_ONE_DOWN_TO_K_PI_OVER_10_BOUNDED_THEOREM_NOTE_2026-09-25.md).

Open PR 9361 put the 24³ estimate at `k = π/12` at `0.856 ± 0.042` from four
seeds at 960 walkers, below the 20³ and 16³ values. Its 24³ energy per
plaquette lay `0.0036` below the 8³ finite reptation estimate, so a population
error could not be excluded. This block uses new seeds 603 and 604 at 1920
walkers (projection 30, resampling interval 0.015).

## Result

**24³ at `k = π/12`, a guide per field.**

| population | seeds | `χ` | energy per plaquette |
|---|---|---|---|
| 960 (open PR 9298) | 601, 602: `0.908`, `0.754` | mean `0.831` | — |
| 960 (open PR 9361) | four seeds | `0.856 ± 0.042` | `0.28502` (seeds 605, 606) |
| 1920 (this block) | 603, 604: `0.8752`, `0.8113` | `0.843 ± 0.041` | `0.28537` |

What follows:
- **The estimate holds.** Doubling the population moves the two-seed
  estimate by `+0.012`, within its errors, as on 12³ and 16³ (open PRs 9356,
  9358). Agreement at two finite populations does not exclude a common bias,
  slow transient or a change at larger populations.
- **The decrease stands.** Per field, the estimates are `1.061 ± 0.036` on
  16³ (`π/8`), `0.990 ± 0.032` on 20³ (`π/10`) and about `0.85` on 24³
  (`π/12`).
- **Open question.** The energy per plaquette rises by only `0.0004` and
  stays `0.0032` below the 8³ finite reptation estimate `0.2886`. This block does
  not explain that offset, and it leaves open whether the decrease comes from
  the momentum or from the torus. A 24³ value at `k = π/6`, the smallest
  momentum of 12³, would separate the two; that run is queued as backlog
  work.

## Estimator and reproduction boundary

- **Errors.** They are the larger of the seed scatter and the mean bin error,
  over two seeds, so they are rough.
- **Seeds.** The 960-walker values come from other runs with the same
  settings.

## Evidence limits and No-Go Discipline Gate

- **N1:** supplied finite ring component on 2³ and 24³ with the stated settings.
- **N2:** no phase or no-go wall is imported.
- **N3:** Hamiltonian, sector, guide and estimator remain supplied.
- **N4:** the landed parents' scopes govern; this block tests the population dependence of the 24³ estimate.
- **N5:** finite estimates at two populations; the stability and the unexplained energy offset are the result.
- **N6:** a fixed-momentum comparison and a population-free value on 24³ remain open.
- **N7:** other guides, populations and estimators remain available.
- **N8:** no physical identification, soft-mode claim, new premise or audit verdict.

## Reproduction

```bash
python3 scripts/ring_model_24_cubed_per_field_curvature_doubled_population_2026_09_27.py
```

Two checks; prints `TOTAL: PASS=2 FAIL=0` in about six hours of computation on a shared machine.

## Seed provenance correction

PR 9298's actual production call uses labels 601 and 602, yielding the
printed 0.908 and 0.754 values. References in the original runner labels to
603 and 604 for that earlier run are incorrect. Later 603/604 runs are distinct
realizations; they are not a matched-seed rerun of PR 9298.

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
- [PR 9356 finite source](RING_MODEL_ON_12_CUBED_THE_PER_FIELD_GUIDE_CURVATURE_ESTIMATE_HOLDS_UNDER_A_FOURFOLD_POPULATION_WHILE_THE_ONE_GUIDE_ESTIMATE_FALLS_BOUNDED_THEOREM_NOTE_2026-09-26.md).
- [PR 9361 finite source](RING_MODEL_ON_24_CUBED_FOUR_SEEDS_PUT_THE_PER_FIELD_CURVATURE_ESTIMATE_AT_0_86_BELOW_THE_16_AND_20_CUBED_VALUES_BOUNDED_THEOREM_NOTE_2026-09-27.md).

[Current axiom memo](MINIMAL_AXIOMS_2026-06-29.md).

- [PR9358 finite comparison](RING_MODEL_ON_16_CUBED_THE_PER_FIELD_GUIDE_CURVATURE_ESTIMATE_HOLDS_UNDER_A_FOURFOLD_POPULATION_BOUNDED_THEOREM_NOTE_2026-09-27.md).

Historical filenames and claim identifiers remain stable; the scoped body governs.

The unchanged historical capture used a 36000-second limit; the runner declares
28800 seconds. Its measured 21268.70-second completion is below both. This
provenance discrepancy is preserved, not relabelled as a new execution.
