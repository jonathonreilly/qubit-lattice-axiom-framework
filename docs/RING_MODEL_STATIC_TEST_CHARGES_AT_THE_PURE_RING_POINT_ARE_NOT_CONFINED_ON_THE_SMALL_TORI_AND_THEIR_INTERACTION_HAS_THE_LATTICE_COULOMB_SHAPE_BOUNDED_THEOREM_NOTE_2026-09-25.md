---
claim_id: ring_model_static_test_charges_at_the_pure_ring_point_are_not_confined_on_the_small_tori_and_their_interaction_has_the_lattice_coulomb_shape_bounded_theorem_note_2026-09-25
claim_type: bounded_theorem
claim_scope: Fixed charged flip-component conservation and zero ground energy at V=g>=0 in a supplied finite link-qubit
  ring model. The Gaussian comparator gives an exact torus source-energy formula. Larger-grid projector energies
  and fits are finite, uncontrolled-bias diagnostics; neither a string-tension exclusion nor confinement, Coulomb
  phase or coupling identification follows.
upstream_dependencies:
- minimal_axioms
- gaussian_lattice_maxwell_comparator_gives_a_linear_size_independent_transverse_structure_factor_and_misses_the_pure_ring_level_step_bounded_theorem_note_2026-09-24
- ring_model_winding_sector_splittings_resolved_on_the_small_tori_and_a_multi_exponential_relaxation_at_the_pure_ring_point_bounded_theorem_note_2026-09-24
- ring_model_energy_only_bounds_on_the_pure_ring_photon_from_the_mode_averaged_transverse_susceptibility_bounded_theorem_note_2026-09-25
- ring_model_energy_only_photon_bounds_soften_from_the_pure_ring_point_to_the_rk_point_and_meet_uniform_ice_there_bounded_theorem_note_2026-09-25
runner: scripts/ring_model_static_test_charges_separation_energy_against_the_lattice_coulomb_law_2026_09_25.py
---

# Static-charge component identities and finite separation-energy diagnostics

**Date:** 2026-09-25
**Type:** bounded_theorem
**Status:** exact identities of the supplied model with finite projector estimates; unaudited.

## Result and interpretation

Plaquette flips preserve the specified charge pattern. At V=g>=0 every nonempty finite flip component has a uniform zero-energy ground vector. At V=0 the runner estimates selected-component energies for fixed string preparations on sides 4,6,8,12 and compares two descriptive fit shapes. These finite estimates do not determine confinement, a Coulomb phase, a physical coupling or a nonzero string-tension bound.

The energy mixed estimator is exact only with the exact projected distribution. Finite walker population, finite projection, guide dependence, component selection and time correlations can bias these runs. Seed/bin errors do not bound those effects. A shared reference energy correlates every separation difference; the printed diagonal-error chi-squared fits omit that covariance and are descriptive only. Neither error-bar agreement nor the reported sigma differences supply a confidence-level exclusion.

## Setting and decision points

- **D-gauss with two test charges, D-roles, D-ring (landed).** The exact
  vertex Gauss law holds at every vertex except two: one with four arrows
  out and two in (divergence `+2`, charge `+1`) and one with two out and four
  in (charge `−1`); for charge 2, five and one. The clause is
  `−g (U + U†) + V N_flip`, `g = 1`, on `L³` tori.
- **The configurations (method).** In the canonical zero-winding ice state
  of the landed winding-sector note, one directed string of arrows from
  `A = (0,0,0)` to `B = (d,0,0)` is reversed (two strings for charge 2,
  each found by a breadth-first search of the arrow graph). Each
  separation has its own flip component; walkers start from that
  configuration and relax under the projector.
- **The projector (method).** The compiled projector of open PR 9236,
  guide `exp(0.2 (1 − V/g) N_flip)`, fixed populations of 1920 walkers,
  projection 50; the limiting mixed estimator is guide-independent; these finite runs are not proven unbiased.

None is adopted.

## Theorem 1 — static charges, and the RK point

1. **The charges are static.** A plaquette flip reverses four links around
   one plaquette; at each of its corners one link turns in and one turns
   out, so every vertex keeps its divergence. The flip component of a
   configuration therefore has fixed charges, and the ground energy `E(d)`
   of a pair at separation `d` is well defined.
2. **No energetic interaction at the RK point.** At `V = g` the clause is a
   sum of projectors and the uniform superposition over any flip component
   is annihilated by every term. So `E(d) = 0` for every separation and
   every charge: whatever interaction the pair has at the RK point is
   entropic, not energetic.
3. **The Gaussian comparator's law.** In the lattice Maxwell comparator of
   the landed note
   `GAUSSIAN_LATTICE_MAXWELL_COMPARATOR_GIVES_A_LINEAR_SIZE_INDEPENDENT_TRANSVERSE_STRUCTURE_FACTOR_AND_MISSES_THE_PURE_RING_LEVEL_STEP_BOUNDED_THEOREM_NOTE_2026-09-24.md`,
   a static pair of divergence `±2Q` costs `4Q² U [G(0) − G(d)]` relative to the zero-source comparator minimum, where `G` is the lattice Green function of the torus
   without its zero mode and `U` is the coupling whose inverse is the
   transverse susceptibility, `χ̄ = 1/U`. So the comparator predicts
   `E(d) − E(1) = 4Q² U [G(1) − G(d)]`, bounded as `d` grows, with the same
   `U` open PR 9236 measured through the transverse response.

The runner checks the first two statements exactly on the 2³ torus. ∎

## Diagnostic 1 — exact control

On the 2³ torus with charges `−1` at `(0,0,0)` and `+1` at `(1,0,0)`: 6000
configurations carry these charges; the flip component of the constructed
one has 508 states, all with the same charges. The RK clause's lowest
eigenvalue on that component is `1.6·10⁻¹⁵` and the projector's local
energy vanishes on every block; at the pure-ring point the exact ground
energy `−7.85688` against the projector's `−7.8576 ± 0.0037`.

## Diagnostic 2 — the pair on 8³

Four seeds per separation; errors are the larger of the seed scatter and
the mean bin error over the square root of the seed count.

| separation `d` | `E(d) − E(1)` | Coulomb shape `4[G(1) − G(d)]` | `U = 0.9` prediction |
|---|---|---|---|
| 2 | +0.269 ± 0.076 | 0.1684 | 0.152 |
| 3 | +0.367 ± 0.062 | 0.2210 | 0.199 |
| 4 | +0.262 ± 0.082 | 0.2340 | 0.211 |

The torus Green function without its zero mode has `G(0) = 0.2246` and
`G(d,0,0) = 0.0583, 0.0162, 0.0030, −0.0002` for `d = 1 … 4`. The Coulomb fit
through separation 1 gives `U = 1.48 ± 0.20` (`χ² = 1.6`); a linear string
`σ (d − 1)` gives `σ = 0.139` with `χ² = 8.6`. Differences from separation 2,
`E(3) − E(2) = 0.10 ± 0.08` and `E(4) − E(2) = −0.01 ± 0.09` (arithmetic on the
printed values, bin errors combined without their correlation), give
`U = 0.9 ± 1.0` against the Coulomb shape.

## Diagnostic 3 — the separation energy against the torus

| torus | `E(L/2) − E(1)` | seeds | Coulomb with `U = 1.48` |
|---|---|---|---|
| 4³ | +0.312 ± 0.011 | 4 | 0.175 |
| 6³ | +0.279 ± 0.028 | 4 | 0.289 |
| 8³ | +0.262 ± 0.082 | 4 | 0.346 |
| 12³ | +0.475 ± 0.572 | 2 | 0.401 |

The apparent lack of growth on three small sizes is a diagnostic, not a tension exclusion. Uncontrolled population/projection effects and component dependence can alter energy differences. Two seeds on side12 do not resolve the trend.

## Diagnostic 4 — charge 2, and the RK potential halfway

- **Charge 2 on 8³.** `E(4) − E(1) = 0.742 ± 0.070` for a pair of divergence
  `±4`, three seeds; `2.8 ± 0.9` times the charge-1 value, where the
  Gaussian comparator gives 4; its effective `U = 0.742/(16 · 0.0585) = 0.79`.
  A vertex of charge 2 has five of its six arrows pointing the same way, so
  the field at the core is saturated and the comparator's unbounded field
  overstates its cost.
- **`V/g = 0.5` on 8³.** The charge-1 separation energy `0.181 ± 0.023`, three
  seeds, is `0.69 ± 0.23` of the `V = 0` value; the susceptibilities of open
  PR 9239 give `1.077/2.220 = 0.49` if `U = 1/χ̄` at both points. ∎

## Interpretation

The table is an author-run historical diagnostic at the listed settings. Fresh runner output is the reproduction record. The comparator is supplied and does not establish the ring model's long-distance interaction. A charge-2 core explanation is a hypothesis; no validated nonlinear response calculation is supplied.

## What stays open

- The charge interaction beyond the core at a precision that tests
  `U = 1/χ̄` (separations 2–6 on 12³ with many more seeds or walkers).
- The 12³ and larger separation energies, where the population effect on
  single energies is large.
- The adjacent-pair core, and charge 2, against a non-Gaussian account.

## Evidence limits

- **Domain:** the listed tori, separations along one axis, the flip
  components of the constructed configurations, the estimator settings.
- **Exact versus estimated:** Theorem 1 is exact algebra; the 2³ eigensystem is a numerical finite control; all
  larger-torus numbers are projector estimates whose errors have no proved
  coverage, and the 12³ ones are dominated by seed scatter.
- **Fits:** the Coulomb and linear fits are one-parameter forms, the
  comparator's shape and a string; neither is a law of the model.

## Prior art

Rokhsar and Kivelson 1988; Hermele, Fisher and Balents 2004; Castelnovo,
Moessner and Sondhi 2008 (emergent charges in ice); Shannon, Sikora,
Pollmann, Penc and Fulde 2012; Kogut 1979 (confinement and string tension
on lattices). All cited as prior art, not as premises.

## Checks

The runner has 4 checks and all pass in about 50 minutes, single-threaded.

| Check | Result |
|---|---|
| Exact 2³ control | Charges conserved on a 508-state component; RK energy zero; pure-ring energy within errors. |
| Pair on 8³ | Reported: the table, the Coulomb and linear fits. |
| Size | Reported: the separation energy on 4³–12³. |
| Charge 2 and `V/g = 0.5` | Reported. |

## Independent check

Landing review checks the exact identities independently. Fresh execution records and unchanged-source comparisons bind reproduction; finite-seed agreement is not error coverage.

## What this does not do

- It adopts no clause, Gauss law, source or method.
- It claims no confinement, deconfinement, Coulomb law, coupling or limit
  beyond these finite tori.

## Actual inputs

- [MINIMAL_AXIOMS_2026-06-29](MINIMAL_AXIOMS_2026-06-29.md)
- [GAUSSIAN_LATTICE_MAXWELL_COMPARATOR_GIVES_A_LINEAR_SIZE_INDEPENDENT_TRANSVERSE_STRUCTURE_FACTOR_AND_MISSES_THE_PURE_RING_LEVEL_STEP_BOUNDED_THEOREM_NOTE_2026-09-24](GAUSSIAN_LATTICE_MAXWELL_COMPARATOR_GIVES_A_LINEAR_SIZE_INDEPENDENT_TRANSVERSE_STRUCTURE_FACTOR_AND_MISSES_THE_PURE_RING_LEVEL_STEP_BOUNDED_THEOREM_NOTE_2026-09-24.md)
- [RING_MODEL_WINDING_SECTOR_SPLITTINGS_RESOLVED_ON_THE_SMALL_TORI_AND_A_MULTI_EXPONENTIAL_RELAXATION_AT_THE_PURE_RING_POINT_BOUNDED_THEOREM_NOTE_2026-09-24](RING_MODEL_WINDING_SECTOR_SPLITTINGS_RESOLVED_ON_THE_SMALL_TORI_AND_A_MULTI_EXPONENTIAL_RELAXATION_AT_THE_PURE_RING_POINT_BOUNDED_THEOREM_NOTE_2026-09-24.md)
- [RING_MODEL_ENERGY_ONLY_BOUNDS_ON_THE_PURE_RING_PHOTON_FROM_THE_MODE_AVERAGED_TRANSVERSE_SUSCEPTIBILITY_BOUNDED_THEOREM_NOTE_2026-09-25](RING_MODEL_ENERGY_ONLY_BOUNDS_ON_THE_PURE_RING_PHOTON_FROM_THE_MODE_AVERAGED_TRANSVERSE_SUSCEPTIBILITY_BOUNDED_THEOREM_NOTE_2026-09-25.md)
- [RING_MODEL_ENERGY_ONLY_PHOTON_BOUNDS_SOFTEN_FROM_THE_PURE_RING_POINT_TO_THE_RK_POINT_AND_MEET_UNIFORM_ICE_THERE_BOUNDED_THEOREM_NOTE_2026-09-25](RING_MODEL_ENERGY_ONLY_PHOTON_BOUNDS_SOFTEN_FROM_THE_PURE_RING_POINT_TO_THE_RK_POINT_AND_MEET_UNIFORM_ICE_THERE_BOUNDED_THEOREM_NOTE_2026-09-25.md)
