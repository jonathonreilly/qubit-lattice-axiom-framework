---
claim_id: the_gaussian_lattice_maxwell_comparator_finite_size_energy_shift_is_far_smaller_than_the_ring_projector_energy_decrease_on_16_and_24_cubed_bounded_theorem_note_2026-10-01
claim_type: bounded_theorem
claim_scope: "Supplied Gaussian lattice-Maxwell comparator of the landed comparator note, H = (U/2) E^2 + (K/2) A^T C^T C A on the L^3 torus with the Gauss law and the holonomy zero modes removed, with the landed reading U = 1/chi, K = 4 u0 (v = sqrt(UK) = 1.025). Its nonzero transverse oscillators are two per k != 0 with omega = v |s(k)| (explicit spectra on L = 4, 6, 8: kernel N + 2, 2(N - 1) oscillators, zero-point energy v N Z(L) to 1e-13). The zero-point energy per plaquette is (v/3) Z(L), Z(L) = N^-1 sum_(k != 0) |s(k)|, so the comparator's energy per plaquette u = -E/(3N) exceeds its infinite-volume value by (v/3)(Z_inf - Z(L)) = 1.43e-4 (8^3), 2.8e-5 (12^3), 8.8e-6 (16^3), 1.7e-6 (24^3), approaching the continuum Casimir form (v/3)(Z_E/pi^2)/L^4 with Z_E = sum_(n != 0)|n|^-4 (Z_inf = 2.38760224286 by a 30-digit heat-kernel integral, cross-checked two ways). From 8^3 the comparator's shift is -1.15e-4, -1.34e-4 and -1.41e-4 on 12^3, 16^3, 24^3, while the landed ring-model projector energies per plaquette (0.2884, 0.28807, 0.28676, 0.28509) fall by 3.7e-4, 1.68e-3 and 3.35e-3: 3, 13 and 24 times as much. So a finite-size effect of this comparator's kind and size does not account for the projector's decrease on 16^3 and 24^3; its source (an estimator bias or physics outside the comparator) remains open. Floating-point and 30-digit numerics, not interval-certified. No ring-model energy, finite-size law, bias attribution or physical reading."
upstream_dependencies:
  - minimal_axioms
  - gaussian_lattice_maxwell_comparator_gives_a_linear_size_independent_transverse_structure_factor_and_misses_the_pure_ring_level_step_bounded_theorem_note_2026-09-24
  - ring_model_energy_only_bounds_on_the_pure_ring_photon_from_the_mode_averaged_transverse_susceptibility_bounded_theorem_note_2026-09-25
runner: scripts/gaussian_lattice_maxwell_comparator_finite_size_energy_beside_the_ring_projector_2026_10_01.py
---

# The Gaussian lattice-Maxwell comparator's finite-size energy shift is far smaller than the ring projector's energy decrease on 16³ and 24³

**Date:** 2026-10-01
**Type:** bounded_theorem
**Status:** comparator numerics; unaudited.

## Supplied setting

**The comparator.** Use the Gaussian lattice-Maxwell comparator of the landed note
`GAUSSIAN_LATTICE_MAXWELL_COMPARATOR_GIVES_A_LINEAR_SIZE_INDEPENDENT_TRANSVERSE_STRUCTURE_FACTOR_AND_MISSES_THE_PURE_RING_LEVEL_STEP_BOUNDED_THEOREM_NOTE_2026-09-24.md`:
- `H = (U/2)E² + (K/2)AᵀCᵀCA` on the links of the `L³` torus;
- the Gauss law `DE = 0`, with the holonomy zero modes removed;
- the reading `U = 1/χ`, `K = 4u₀` of
  `RING_MODEL_ENERGY_ONLY_BOUNDS_ON_THE_PURE_RING_PHOTON_FROM_THE_MODE_AVERAGED_TRANSVERSE_SUSCEPTIBILITY_BOUNDED_THEOREM_NOTE_2026-09-25.md`,
  which gives `v = √(UK) = 1.025`.

The comparator is a supplied comparison model, not the ring model.

**The question.** The ring-model projector's energy per plaquette `u` falls
with the torus. The landed values are:
- `0.2884` on 8³ (two guide schemes, 0.28837 and 0.28851);
- `0.28807` on 12³ (3840 walkers);
- `0.28676` on 16³;
- `0.28509` on 24³.

Population-free reptation gives `0.28861` on 8³. Population, projection time
and resampling interval have been checked without explaining the decrease.
This block asks whether a finite-size zero-point effect of the comparator's
kind could account for it.

## Result

1. **Spectrum.** On `L = 4, 6, 8` the explicit comparator spectrum checks out
   (test couplings `U = 1.7`, `K = 1.2`):
   - the curl preserves the Gauss law;
   - `CᵀC` has kernel `N + 2` and `2(N − 1)` nonzero eigenvalues, two per
     `k ≠ 0` at `|s(k)|²`;
   - the oscillator zero-point energy equals `√(UK) N Z(L)` to `1e-13`, with
     `Z(L) = N⁻¹ Σ_{k≠0} |s(k)|`.
2. **Infinite volume.** `Z_inf = 2.38760224286`, from the heat-kernel
   integral `Z = (2√π)⁻¹ ∫ t^{−3/2}(1 − [e^{−2t}I₀(2t)]³) dt` at 30 digits.
   Two independent checks agree:
   - a shifted midpoint sum on 96³ gives `2.3876022475`;
   - the image heat kernel reproduces `Z(4)` and `Z(8)` to `5e-13`.
3. **Finite-size shift.** The comparator's `u(L) − u_inf = (v/3)(Z_inf − Z(L))`
   is positive and decreasing, and tends to the continuum Casimir form
   `(v/3)(Z_E/π²)/L⁴`, with `Z_E = Σ_{n≠0}|n|⁻⁴` and `Z_E/π² = 1.67507`.

   | L | 4 | 6 | 8 | 12 | 16 | 20 | 24 |
   |---|---|---|---|---|---|---|---|
   | `u(L) − u_inf` | `2.49e-3` | `4.60e-4` | `1.43e-4` | `2.78e-5` | `8.78e-6` | `3.59e-6` | `1.73e-6` |

4. **Beside the projector.** Changes from 8³:

   | L | comparator | ring projector (landed) | ratio |
   |---|---|---|---|
   | 12 | `−1.15e-4` | `−3.7e-4` | 3 |
   | 16 | `−1.34e-4` | `−1.68e-3` | 13 |
   | 24 | `−1.41e-4` | `−3.35e-3` | 24 |

## What follows

- **The projector's decrease is not a comparator-type finite-size effect.**
  The comparator's whole shift beyond 8³ is at most `1.43e-4` per
  plaquette, and below `3e-5` from 12³ on. The projector's decrease is 13
  and 24 times larger on 16³ and 24³. The comparator also has nearly
  finished its change by 12³ (81 percent of its 8³-to-24³ change), whereas
  the projector has made 11 percent of its change by then.
- **The source remains open.** The comparison says neither that the decrease
  is an estimator bias nor which bias it would be. A non-Gaussian effect
  outside the comparator is not excluded.
- **A purely quadratic mode gives no shift.** For `ω ∝ |s|²` the comparator's
  zero-point energy is size-independent, since `Σ_k |s|² = 6N` exactly.

## Boundary

- The comparator rests on the landed matching rules `U = 1/χ` and `K = 4u₀`.
  Its amplitude scales linearly with `v`; for `χ` between 1.06 and 1.11, `v`
  stays within two percent.
- The projector energies are the landed values with their own population,
  guide and window settings.

## Evidence limits and No-Go Discipline Gate

- **N1:** supplied Gaussian comparator on `L³` tori; landed ring-model projector energies as inputs.
- **N2:** no phase or no-go wall is imported.
- **N3:** comparator, matching rules and estimators remain supplied.
- **N4:** the landed comparator and energy-only notes govern their own scopes.
- **N5:** floating-point and 30-digit numerics; ratios of finite estimates.
- **N6:** the source of the projector's decrease remains open.
- **N7:** non-Gaussian finite-size effects, other estimators and other comparators remain available.
- **N8:** no physical identification, new premise or audit verdict.

## Reproduction

```bash
python3 scripts/gaussian_lattice_maxwell_comparator_finite_size_energy_beside_the_ring_projector_2026_10_01.py
```

Four checks; prints `TOTAL: PASS=4 FAIL=0` in a few seconds.
