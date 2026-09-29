---
claim_id: ring_model_on_24_cubed_four_seeds_put_the_per_field_curvature_estimate_at_0_86_below_the_16_and_20_cubed_values_bounded_theorem_note_2026-09-27
claim_type: bounded_theorem
claim_scope: "Recorded finite projector/reptation or Ritz diagnostics at the complete parameter grid in the body, for the supplied ring Hamiltonian and explicit guides. Conditional parent spectral identities remain conditional; printed seed/bin errors and sigma ratios are descriptive. No certified eigenvalue, susceptibility, population/projection convergence, bias attribution, limiting law, spectral reconstruction, physical identification or audit verdict."
upstream_dependencies:
  - minimal_axioms
  - ring_model_energy_only_bounds_on_the_pure_ring_photon_from_the_mode_averaged_transverse_susceptibility_bounded_theorem_note_2026-09-25
  - ring_model_energy_only_photon_bound_holds_on_the_20_cubed_torus_with_the_transverse_susceptibility_near_one_down_to_k_pi_over_10_bounded_theorem_note_2026-09-25
runner: scripts/ring_model_24_cubed_per_field_curvature_two_more_seeds_2026_09_27.py
---

# On 24³ four seeds put the per-field curvature estimate at 0.86, below the 16³ and 20³ values

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
Open PRs 9356 and 9358 found this scheme stable within rough errors over the tested populations on 12³ and 16³
between 960 and 3840 walkers.

Open PR 9298 gave `0.831 ± 0.077` on 24³ at `k = π/12` from two seeds
(`0.908`, `0.754`), 1.7 standard errors below the 20³ value. This block adds
two seeds with the same settings (960 walkers, projection 30, resampling
interval 0.015).

## Result

**24³ at `k = π/12`, a guide per field.**
- New seeds `605` and `606` give `0.9407` and `0.8198` (bin errors `0.054`,
  `0.070`); energy per plaquette `u = 0.28502`.
- With seeds `601` and `602` (open PR 9298), the four seeds `0.941`, `0.820`,
  `0.908` and `0.754` give **`χ = 0.856 ± 0.042`**.

**Beside the other tori (per-field scheme):**

| torus | `k` | `χ` | source |
|---|---|---|---|
| 16³ | `π/8` | `1.061 ± 0.036` (fit over three populations) | open PR 9358 |
| 20³ | `π/10` | `0.990 ± 0.032` | landed |
| 24³ | `π/12` | `0.856 ± 0.042` (four seeds) | this block |

The 24³ value lies 2.5 standard errors below 20³.

**Moment inequalities.** With `s = 2 sin(π/24)` they give estimated upper
bounds of `0.301 = 1.154 s(k)` on the lowest transverse excitation and
`0.129 = 0.494 s(k)` on the structure factor.

**What follows.**
- **The decrease holds with more seeds.** The per-field estimate falls from
  16³ to 24³, and on 24³ it now stands 2.5 standard errors below 20³ rather
  than 1.7.
- **Its cause is not settled.** The 24³ energy per plaquette, `0.28502`,
  lies `0.0036` below the 8³ finite reptation estimate `0.2886` (open PR 9352).
  The 16³ value at 3840 walkers is `0.2872`. Comparing different tori, estimators and populations does not isolate
  population bias from true finite-size effects or other sampling errors. The decrease may be a softening at the smallest momenta, or a
  population error on 24³.
- **What would settle it.** A population series on 24³ (memory-limited
  here) or a population-free estimate there.

## Estimator and reproduction boundary

- **Errors.** They are the larger of the four-seed scatter and the mean bin
  error of the new seeds.
- **Seeds.** Seeds `601` and `602` come from open PR 9298's run with the same
  settings.
- **Energy.** Its drift with the torus (`0.2886` on 8³ from reptation,
  `0.2872` on 16³ at 3840 walkers, `0.2850` on 24³ at 960) is the reason for
  the caveat.

## Evidence limits and No-Go Discipline Gate

- **N1:** supplied finite ring component on 2³ and 24³ with the stated settings.
- **N2:** no phase or no-go wall is imported.
- **N3:** Hamiltonian, sector, guide and estimator remain supplied.
- **N4:** the landed parents' scopes govern; this block narrows the 24³ estimate and states its population caveat.
- **N5:** finite estimates from four seeds; the decrease and its unsettled cause are the result.
- **N6:** a population series or population-free value on 24³ remains open.
- **N7:** other guides, populations and estimators remain available.
- **N8:** no physical identification, soft-mode claim, new premise or audit verdict.

## Reproduction

```bash
python3 scripts/ring_model_24_cubed_per_field_curvature_two_more_seeds_2026_09_27.py
```

Two checks; prints `TOTAL: PASS=2 FAIL=0` in about three and a quarter hours of computation.

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
- [PR 9352 finite source](RING_MODEL_THE_GUIDE_SCHEME_SPLIT_OF_THE_CURVATURE_ESTIMATE_GROWS_WITH_THE_TORUS_AND_ON_8_CUBED_IS_ABOUT_0_05_WITH_OR_WITHOUT_A_WALKER_POPULATION_BOUNDED_THEOREM_NOTE_2026-09-26.md).
- [PR 9356 finite source](RING_MODEL_ON_12_CUBED_THE_PER_FIELD_GUIDE_CURVATURE_ESTIMATE_HOLDS_UNDER_A_FOURFOLD_POPULATION_WHILE_THE_ONE_GUIDE_ESTIMATE_FALLS_BOUNDED_THEOREM_NOTE_2026-09-26.md).
- [PR 9358 finite source](RING_MODEL_ON_16_CUBED_THE_PER_FIELD_GUIDE_CURVATURE_ESTIMATE_HOLDS_UNDER_A_FOURFOLD_POPULATION_BOUNDED_THEOREM_NOTE_2026-09-27.md).

[Current axiom memo](MINIMAL_AXIOMS_2026-06-29.md).

Historical filenames and claim identifiers remain stable; the scoped body governs.
