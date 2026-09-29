---
claim_id: ring_model_energy_curvature_estimates_depend_on_the_guide_scheme_by_about_a_quarter_on_16_and_24_cubed_bounded_theorem_note_2026-09-26
claim_type: bounded_theorem
claim_scope: "Recorded finite projector/reptation or Ritz diagnostics at the complete parameter grid in the body, for the supplied ring Hamiltonian and explicit guides. Conditional parent spectral identities remain conditional; printed seed/bin errors and sigma ratios are descriptive. No certified eigenvalue, susceptibility, population/projection convergence, bias attribution, limiting law, spectral reconstruction, physical identification or audit verdict."
upstream_dependencies:
  - minimal_axioms
  - ring_model_energy_only_bounds_on_the_pure_ring_photon_from_the_mode_averaged_transverse_susceptibility_bounded_theorem_note_2026-09-25
  - ring_model_energy_only_photon_bound_holds_on_the_20_cubed_torus_with_the_transverse_susceptibility_near_one_down_to_k_pi_over_10_bounded_theorem_note_2026-09-25
runner: scripts/ring_model_24_cubed_curvature_with_one_guide_for_all_probe_fields_2026_09_26.py
---

# The ring component's energy-curvature estimates depend on the guide scheme by about a quarter on 16³ and 24³

**Date:** 2026-09-26
**Type:** bounded_theorem
**Status:** finite projector diagnostics; unaudited.

## Supplied setting

Use the supplied Hamiltonian, cyclic transverse modes, probe fields and
conditional moment identities of the landed ring-component note
[RING_MODEL_ENERGY_ONLY_BOUNDS_ON_THE_PURE_RING_PHOTON_FROM_THE_MODE_AVERAGED_TRANSVERSE_SUSCEPTIBILITY_BOUNDED_THEOREM_NOTE_2026-09-25](RING_MODEL_ENERGY_ONLY_BOUNDS_ON_THE_PURE_RING_PHOTON_FROM_THE_MODE_AVERAGED_TRANSVERSE_SUSCEPTIBILITY_BOUNDED_THEOREM_NOTE_2026-09-25.md).
The curvature estimate `χ` is taken from the projector energies `E(0)`, `E(h)`
and `E(2h)`, which also yield `u`. The landed notes, including
[RING_MODEL_ENERGY_ONLY_PHOTON_BOUND_HOLDS_ON_THE_20_CUBED_TORUS_WITH_THE_TRANSVERSE_SUSCEPTIBILITY_NEAR_ONE_DOWN_TO_K_PI_OVER_10_BOUNDED_THEOREM_NOTE_2026-09-25](RING_MODEL_ENERGY_ONLY_PHOTON_BOUND_HOLDS_ON_THE_20_CUBED_TORUS_WITH_THE_TRANSVERSE_SUSCEPTIBILITY_NEAR_ONE_DOWN_TO_K_PI_OVER_10_BOUNDED_THEOREM_NOTE_2026-09-25.md),
use per-field guide fields (`β = 0.5 h`), so each probe field has its own
guide. Their scopes already exclude population convergence. This block
measures how large the guide-dependent part is.

## Result

- **One guide for all three fields.** Here the three energies of each
  estimate share one guide field, `0.5 H₁` times the probe pattern with
  `H₁ = 0.15`. Otherwise everything is as in open PR 9298: 960 walkers,
  projection 30, resampling interval 0.015, the same 16³ seeds.
- **16³ at `k = π/8`.** `χ = 1.307 ± 0.029` with the shared guide, against
  `1.039 ± 0.022` with per-field guides and the same seeds, population and
  interval (open PR 9298). That is `+0.268`, 7.4 standard errors. The plain
  energy per plaquette `u` moves from `0.28680` to `0.28574`, by 13 units of
  total energy.
- **24³ at `k = π/12`.** `χ = 1.077 ± 0.050` from two new seeds (`1.088`,
  `1.067`), against `0.831 ± 0.077` with per-field guides (open PR 9298, other
  seeds).
- **What follows.** At this population the curvature estimates on these tori
  carry a guide-scheme spread of about a quarter of
  their value. The estimated bounds scale as `χ^{−1/2}` and `χ^{1/2}`, so they
  move by about an eighth. Neither the flat susceptibility read in the landed
  notes nor the softening considered in open PR 9298 is established by these
  estimates. Both need an estimator without population bias.
- **The small control does not see it.** The exact 2³ control passes in
  both schemes: `+1.7`, `+1.4` and `−0.8` standard errors at `h = 0`, `0.15`
  and `0.30` with the shared guide. Agreement on 2³ does not control errors on a larger torus.

## Estimator and reproduction boundary

Seed and bin errors do not control finite-population, projection or field errors. With the shared guide, `E(0)` and `E(2h)` are computed with a guide
field that does not match their probe field, so sharing a guide does not
make the three biases equal either. The finite sample means are scheme-dependent; these data do not isolate
or bound either estimator's bias. The run was paused for twenty minutes for other
work, so the elapsed time and the per-walker costs in the cache overstate
the computation.

## Evidence limits and No-Go Discipline Gate

- **N1:** supplied finite ring component and comparator number on the stated tori and settings.
- **N2:** no phase or no-go wall is imported.
- **N3:** Hamiltonian, sector, guides and comparator remain supplied.
- **N4:** the landed parents' scopes govern; this block qualifies their estimates, not their identities.
- **N5:** finite estimates with two seeds; the scheme difference is the result.
- **N6:** a population-free estimator of the curvature remains open.
- **N7:** other guides, populations and estimators remain available.
- **N8:** no physical identification, new premise or audit verdict.

## Reproduction

```bash
python3 scripts/ring_model_24_cubed_curvature_with_one_guide_for_all_probe_fields_2026_09_26.py
```

Three checks; prints `TOTAL: PASS=3 FAIL=0` in about three hours of computation.

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

[Current axiom memo](MINIMAL_AXIOMS_2026-06-29.md).

Historical filenames and claim identifiers remain stable; the scoped body governs.
