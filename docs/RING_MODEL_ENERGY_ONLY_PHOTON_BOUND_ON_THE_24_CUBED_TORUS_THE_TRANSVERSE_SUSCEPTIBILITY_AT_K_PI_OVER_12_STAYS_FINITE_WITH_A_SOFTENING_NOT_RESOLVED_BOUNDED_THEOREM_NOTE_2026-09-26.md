---
claim_id: ring_model_energy_only_photon_bound_on_the_24_cubed_torus_the_transverse_susceptibility_at_k_pi_over_12_stays_finite_with_a_softening_not_resolved_bounded_theorem_note_2026-09-26
claim_type: bounded_theorem
claim_scope: "Restated conditional moment identities of a supplied finite ring component, plus finite-projector energy diagnostics on the 16^3 and 24^3 tori with two seeds (960 walkers, projection 30, resampling interval 0.015). On 24^3 at k = pi/12 the curvature estimate is chi = 0.831 +- 0.077 (seeds 0.908 and 0.754), 1.7 standard errors below the landed 20^3 value 0.990 +- 0.032 at k = pi/10; with it the moment inequalities evaluate to omega_min <= 1.171 s and S_T <= 0.487 s. These are estimated upper bounds, not certified excitation frequencies, soft-mode exclusions, population convergence or a limit; whether chi stays flat or falls at the smallest momenta is not settled, and the three probe fields use different guide fields."
upstream_dependencies:
  - minimal_axioms
  - ring_model_winding_sector_splittings_resolved_on_the_small_tori_and_a_multi_exponential_relaxation_at_the_pure_ring_point_bounded_theorem_note_2026-09-24
  - gaussian_lattice_maxwell_comparator_gives_a_linear_size_independent_transverse_structure_factor_and_misses_the_pure_ring_level_step_bounded_theorem_note_2026-09-24
  - ring_model_energy_only_bounds_on_the_pure_ring_photon_from_the_mode_averaged_transverse_susceptibility_bounded_theorem_note_2026-09-25
  - ring_model_energy_only_photon_bound_holds_on_the_20_cubed_torus_with_the_transverse_susceptibility_near_one_down_to_k_pi_over_10_bounded_theorem_note_2026-09-25
  - ring_model_winding_sector_energies_give_an_electric_coupling_that_agrees_with_the_transverse_susceptibility_on_8_cubed_and_the_comparator_coupling_constant_bounded_theorem_note_2026-09-25
runner: scripts/ring_model_energy_only_photon_bound_on_the_24_cubed_torus_2026_09_26.py
---

# Finite energy-curvature diagnostics on the 24³ torus at k = π/12

**Date:** 2026-09-26
**Type:** bounded_theorem
**Status:** conditional moment identities (restated) and finite estimates; unaudited.

## Supplied setting and exact boundary

Use the supplied Hamiltonian, cyclic transverse modes and exact identities
`m₁ = 2us²`, `m₋₁ = χ/2` and `m₀ = S` of the landed ring-component note
`RING_MODEL_ENERGY_ONLY_BOUNDS_ON_THE_PURE_RING_PHOTON_FROM_THE_MODE_AVERAGED_TRANSVERSE_SUSCEPTIBILITY_BOUNDED_THEOREM_NOTE_2026-09-25.md`.
For the centered positive spectral measure with nonzero weight,
log-convexity gives `ω_min ≤ 2s √(u/χ)` and `S ≤ s √(uχ)`, for the lowest
coupled excitation of the selected component. The real-field curvature
extraction also needs the translation/momentum and field-reversal
hypotheses stated in that parent. Winding-preserving loop sampling alone
does not prove them for the sampled mixture.

A finite-grid `χ` does not establish its small-momentum limit. Even a
controlled asymptotic linear upper bound would need bounded `u` and a
positive lower bound on `χ`, and would not exclude a softer mode with small
spectral weight. No photon, velocity, phase, residual-structure-factor or
quadratic-mode statement follows from these runs.

## What this block adds

The landed note
`RING_MODEL_ENERGY_ONLY_PHOTON_BOUND_HOLDS_ON_THE_20_CUBED_TORUS_WITH_THE_TRANSVERSE_SUSCEPTIBILITY_NEAR_ONE_DOWN_TO_K_PI_OVER_10_BOUNDED_THEOREM_NOTE_2026-09-25.md`
reported `χ = 0.990 ± 0.032` on 20³ at `k = π/10`. This block adds the 24³
torus (41 472 plaquettes) at `k = π/12`, the smallest momentum yet.

- **The 24³ estimate.** `χ = 0.831 ± 0.077` from two seeds (`0.908`,
  `0.754`). With `u = 0.28513`, the moment inequalities evaluate to
  `ω_min ≤ 0.3058 = 1.171 s(k)` and `S ≤ 0.1271 = 0.487 s(k)`. These are
  estimated upper bounds on the selected component.
- **A fall is not settled.** The value lies 1.7 standard errors below the
  20³ value at `π/10`. The ratio `0.84 ± 0.08` is consistent with a flat
  `χ` and with a mild fall at the smallest momenta, and two seeds do not
  decide between them.
- **The guides differ between probe fields.** Each probe field has its own
  guide field (`β = 0.5 h`), so the three energies of each curvature
  estimate do not share a guide. The landed note
  `RING_MODEL_SINGLE_LINK_CHARGE_HOPPING_THE_PROJECTOR_MISSES_THE_EXACT_2_CUBED_ENERGY_WITH_A_MISMATCHED_GUIDE_AND_ITS_6_CUBED_ENERGY_SPANS_TWO_PERCENT_ACROSS_GUIDES_BOUNDED_THEOREM_NOTE_2026-09-26.md`
  found guide-dependent finite-population energies in a related model.
  Whether that affects these curvatures is not tested.
- **The 16³ value.** At `k = π/8` the estimate is `1.039 ± 0.022`, against
  `1.038 ± 0.029` at resampling interval 0.05 in the landed 4³–16³ note.
  That comparison also changes population and seeds, so it is not an
  isolated test of the resampling interval.
- **The comparator number.** `(1/(χu))^{1/2}/(2π) = 0.327` at `π/12`, a number
  of the landed Gaussian comparator that moves with `χ`, compared with no
  measured value.

## Estimator and reproduction boundary

The runner uses 960 walkers, projection 30, resampling interval 0.015, two
seeds per large torus and fields 0.15 and 0.30. The shorter interval keeps
the effective sample size per generation near 0.76 by the heuristic
`exp(−(0.17 N_p^{1/2} dτ)²)`, which is not a proved error bound and does not
establish that population bias is removed. `E(0)` is shared within a seed.
The errors of `u`, field truncation, guide, finite projection and component
are not in the seed and bin errors.

## Diagnostic 1 — the exact 2³ control at `dτ = 0.015`

On the exact 2³ component (864 states), eight independent runs per probe
field (400 walkers, 4000 generations each) give `−9.02751 ± 0.00305`,
`−9.22237 ± 0.00347` and `−9.87066 ± 0.00301` at `h = 0`, `0.15` and `0.30`,
against the exact `−9.026721`, `−9.227240` and `−9.869211` (`−0.3`, `+1.4`
and `−0.5` standard errors), with run-to-run scatter `0.0047`–`0.0098`.

## Diagnostic 2 — the curvature estimates and the bounds

| torus | `k` | `χ` (seeds) | bound on `ω_min` | bound / `s` | bound on `S` | bound / `s` | `(1/(χu))^{1/2}/(2π)` |
|---|---|---|---|---|---|---|---|
| 16³ | π/8 | 1.039 ± 0.022 | — | — | — | — | — |
| 24³ | π/12 | 0.831 ± 0.077 (0.908, 0.754) | 0.3058 | 1.171 | 0.1271 | 0.487 | 0.3270 |

`u` is `0.28680` on 16³ and `0.28513` on 24³. The projector costs 8.4 and
46.4 ms per walker and unit of imaginary time. The fresh run takes about
two hours and forty minutes.

## Evidence limits and No-Go Discipline Gate

- **N1:** supplied finite ring and comparator models on the stated tori and settings.
- **N2:** no phase or no-go wall is imported.
- **N3:** Hamiltonian, sector, guide and comparator remain supplied.
- **N4:** the landed parents' scopes govern.
- **N5:** finite estimates with two seeds and heuristic errors are not certified enclosures.
- **N6:** more seeds on 24³, one guide for all three probe fields, population/projection and limiting control remain open.
- **N7:** soft modes with weak weight and other components remain possible.
- **N8:** no physical identification, new premise or audit verdict.

## Premise authority

The framework boundary is [the current axiom memo](MINIMAL_AXIOMS_2026-06-29.md).
