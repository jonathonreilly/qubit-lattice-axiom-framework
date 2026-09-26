---
claim_id: ring_model_in_a_region_bounded_by_records_the_energy_only_photon_bound_matches_the_torus_and_the_records_reduce_only_the_response_amplitude_bounded_theorem_note_2026-09-25
claim_type: bounded_theorem
claim_scope: Finite selected flip component with supplied frozen boundary and diagonal standing-wave observable.
  Nondegenerate ground-state perturbation and the double commutator give inverse and first spectral moments and
  an upper bound on the lowest coupled excitation. Finite-field derivatives and fixed-population estimates are diagnostics
  only; sampled n=2/4 or3/6 waves are not the fundamental mode, historical torus interpolation/clamping does not
  establish matched spectra, regulator independence or physical photons.
upstream_dependencies:
- minimal_axioms
- ring_model_two_regulators_a_region_bounded_by_records_matches_the_torus_at_size_eight_and_the_walker_population_is_the_larger_regulator_bounded_theorem_note_2026-09-25
- ring_model_energy_only_bounds_on_the_pure_ring_photon_from_the_mode_averaged_transverse_susceptibility_bounded_theorem_note_2026-09-25
runner: scripts/ring_model_energy_only_photon_bounds_in_a_region_bounded_by_records_against_the_torus_2026_09_25.py
---

# Spectral moments in a frozen-boundary region and finite comparisons

**Date:** 2026-09-25
**Type:** bounded_theorem
**Status:** exact identities of the supplied model with finite projector estimates; unaudited.

## Result and interpretation

For a fixed finite flip component, a diagonal observable and an isolated nondegenerate ground state, perturbation theory and a double commutator give an energy-only spectral upper bound. Fixed-boundary geometry does not make that bound an excitation frequency. Agreement between two upper bounds does not show agreement between their spectra or that a boundary changes only response amplitude.

The numerical plan samples n=2,4 at m=8 and n=3,6 at m=12, not the fundamental n=1 mode. Its torus comparison uses historical fitted values; below the table's minimum k it clamps susceptibility and bound/s(k), rather than measuring a matching torus mode. Errors omit interpolation uncertainty, finite population/projection bias, finite-field truncation and covariance. No regulator-independence, spectral-equivalence or photon conclusion follows.

## Setting and decision points

- **D-gauss, D-roles, D-ring (landed).** The exact vertex Gauss law and the
  ring clause at `V = 0`, `g = 1`.
- **The region (method).** The unrecorded interior `{1, …, m}³` of an
  `(m+2)³` cell whose other links carry records, as in the landed
  two-regulator note; records from a uniform-ice sample of the cell's
  zero-winding sector or from its canonical ice state. A record on a link
  removes every ring term containing it (landed).
- **The probe and the projector (methods).** The standing-wave triple
  `W = Σ_a Σ_{a-links} sin(π n x_b/(m+1)) σ`, `b = a + 1 mod 3`, momentum
  `k = πn/(m+1)`; the compiled projector of open PR 9236 extended to
  per-plaquette ring couplings, guide `exp(0.2 N_flip + (h/2) W)`.

None is adopted.

## Theorem 1 — the energy-only bound in a region

On a connected finite flip component with an isolated ground state and nonzero centered W variance, let `a_n = |⟨n|W|0⟩|²` for excited states `n` of the region's flip
component, `ω_n = E_n − E_0`, `m_j = Σ_n a_n ω_n^j`.

1. **The inverse moment from energies.** `E(h) = E_0 − h⟨W⟩ − h² m_{−1} +
   O(h³)`, with odd terms because the records give `⟨W⟩ ≠ 0`. The symmetric
   combinations `S(h) = [E(h) + E(−h)]/2 − E_0 = −h² m_{−1} − b h⁴ + …` at
   `h` and `2h` eliminate `b`: `m_{−1} = −(16 S(h) − S(2h))/(12 h²) + O(h^4)` for analytic E(h); this is an extrapolation, not an exact finite-field identity.
2. **The first moment from energies.** For diagonal `W`,
   `m_1 = ½⟨[W,[H,W]]⟩ = ½ Σ_p c_p ⟨R_p⟩` with `R_p = U_p + U_p†` and
   `c_p = 4 (Σ_{l∈p} w_l sign_l)²`, the squared change of `W` when a
   flippable `p` flips (independent of the configuration, since the links
   of a flippable plaquette follow its circulation). With ring couplings
   `1 + ε c_p`, the Hellmann–Feynman theorem gives `∂E_0/∂ε = −Σ_p c_p ⟨R_p⟩`,
   so `m_1 = −[E(ε) − E(−ε)]/(4ε) + O(ε²)`.
3. **The bound.** Log-convexity of the moments gives
   `ω_min ≤ (m_1/m_{−1})^{1/2}`, where `ω_min` is the lowest excitation with
   `⟨n|W|0⟩ ≠ 0`. The ratio is normalization-free, so it compares directly
   with the torus bound `2 s(k)(u/χ̄)^{1/2}` of open PR 9236.

On the exact 3³ region the Hellmann–Feynman `m_1` equals the double
commutator to `10⁻⁸` for both `n = 1, 2`, and the chain reads
`0.7805 ≤ 0.9925 ≤ 1.2622` and `0.7246 ≤ 0.8143 ≤ 0.9150`. ∎

## Diagnostic — regions against the torus

Two to four seeds per row; `h = 0.15`, `ε = 0.02`; the torus values
interpolate open PR 9236's 8³ and 12³ bounds per unit lattice momentum at
`k = π/4, π/3, π/2`. The normalized susceptibility is `2 m_{−1}/Σ w²`, which
equals the torus `χ̄` for plane waves.

| region | records | seeds | `k` | susceptibility | torus | bound on `ω_min` | torus | ratio | bound / `s(k)` |
|---|---|---|---|---|---|---|---|---|---|
| 8 | uniform ice | 4 | 0.698 | 0.642 ± 0.013 | 1.064 | 0.720 ± 0.010 | 0.713 | 1.010 | 1.05 |
| 8 | uniform ice | 4 | 1.396 | 1.096 ± 0.012 | 1.165 | 1.136 ± 0.007 | 1.279 | 0.888 | 0.884 |
| 8 | canonical | 2 | 0.698 | 0.617 ± 0.049 | 1.064 | 0.710 ± 0.029 | 0.713 | 0.996 | 1.037 |
| 8 | canonical | 2 | 1.396 | 0.930 ± 0.067 | 1.165 | 1.221 ± 0.044 | 1.279 | 0.955 | 0.950 |
| 12 | uniform ice | 3 | 0.725 | 0.801 ± 0.020 | 1.064 | 0.729 ± 0.010 | 0.739 | 0.986 | 1.028 |
| 12 | uniform ice | 3 | 1.450 | 1.119 ± 0.020 | 1.170 | 1.223 ± 0.011 | 1.317 | 0.929 | 0.922 |

The table records historical author-run estimates. Fresh stdout is the reproduction record. These rows compare moment-ratio estimators with a clamped/interpolated historical table. They neither bound the systematic errors nor prove amplitude-only boundary effects.

## What stays open

- Larger regions, to test whether any convergence holds,
  and the larger-momentum offset.
- Other record frames, and regions with a charge inside.
- Independent checks of every number here.

## Evidence limits

- **Domain:** two region sizes, two frames at size 8, the listed momenta,
  the flip components of the frame configurations.
- **Exact versus estimated:** Theorem 1 is conditional algebra; the 3³ eigensystem and linear solve are numerical finite controls; the
  region and torus numbers are projector estimates with errors of no
  proved coverage; the torus column is an interpolation of open PR 9236.
- **Comparison:** agreement within errors is not an equivalence test.

## Prior art

Hellmann 1937 and Feynman 1939; the sum-rule and moment inequalities of
linear-response theory (for example Pitaevskii and Stringari, 2003);
Rokhsar and Kivelson 1988; Hermele, Fisher and Balents 2004. All cited as
prior art, not as premises.

## Checks

The runner has 2 checks and both pass in about 32 minutes, single-threaded.

| Check | Result |
|---|---|
| Exact 3³ control | Hellmann–Feynman first moment equals the double commutator; the chain; the projector's moments within 1.3 standard errors. |
| Regions against the torus | Reported: the table. |

## Independent check

Landing review checks the exact identities independently. Fresh execution records and unchanged-source comparisons bind reproduction; finite-seed agreement is not error coverage.

## What this does not do

- It adopts no clause, Gauss law, record frame or method.
- It claims no limit, boundary independence or photon law; agreement within
  errors on two sizes is not an equivalence.

## Actual inputs

- [MINIMAL_AXIOMS_2026-06-29](MINIMAL_AXIOMS_2026-06-29.md)
- [RING_MODEL_TWO_REGULATORS_A_REGION_BOUNDED_BY_RECORDS_MATCHES_THE_TORUS_AT_SIZE_EIGHT_AND_THE_WALKER_POPULATION_IS_THE_LARGER_REGULATOR_BOUNDED_THEOREM_NOTE_2026-09-25](RING_MODEL_TWO_REGULATORS_A_REGION_BOUNDED_BY_RECORDS_MATCHES_THE_TORUS_AT_SIZE_EIGHT_AND_THE_WALKER_POPULATION_IS_THE_LARGER_REGULATOR_BOUNDED_THEOREM_NOTE_2026-09-25.md)
- [RING_MODEL_ENERGY_ONLY_BOUNDS_ON_THE_PURE_RING_PHOTON_FROM_THE_MODE_AVERAGED_TRANSVERSE_SUSCEPTIBILITY_BOUNDED_THEOREM_NOTE_2026-09-25](RING_MODEL_ENERGY_ONLY_BOUNDS_ON_THE_PURE_RING_PHOTON_FROM_THE_MODE_AVERAGED_TRANSVERSE_SUSCEPTIBILITY_BOUNDED_THEOREM_NOTE_2026-09-25.md)
