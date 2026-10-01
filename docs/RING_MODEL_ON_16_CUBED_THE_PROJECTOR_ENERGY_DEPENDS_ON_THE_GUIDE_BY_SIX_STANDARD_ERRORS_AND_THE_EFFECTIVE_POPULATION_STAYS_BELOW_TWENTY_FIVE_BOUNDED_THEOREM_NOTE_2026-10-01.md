---
claim_id: ring_model_on_16_cubed_the_projector_energy_depends_on_the_guide_by_six_standard_errors_and_the_effective_population_stays_below_twenty_five_bounded_theorem_note_2026-10-01
claim_type: bounded_theorem
claim_scope: "Recorded finite fixed-population projector diagnostics for the supplied pure ring Hamiltonian H = -sum_p (U_p + U_p^dag) (V = 0) on the canonical zero-winding flip component of the cubic L^3 torus, with two explicit positive guides: old psi = exp(0.2 N_flip) and pair psi = exp(alpha N_flip + gamma N_pair) (N_pair = adjacent pairs of flippable plaquettes). Checked: the pair guide's local energy, rates and incremental pair counts against brute force on random 4^3 states (machine precision, integer counts exact); on the exact 2^3 component, two pair guides reproduce the exact ground energy within 3 standard errors of eight independent runs. Recorded: on 8^3 at 960 walkers, two seeds, u(Lc=0) = 0.28863 +- 0.00009 (old) and 0.28873 +- 0.00002 (pair, alpha 0.35, gamma -0.049) and the pair guide keeps 1.72 times the old guide's distinct-ancestor fraction at projection lag 2; on 16^3 at 960 walkers, one seed, u(Lc=0) = 0.28687 +- 0.00009 (old) and 0.28755 +- 0.00007 (pair), a difference of 5.9 combined bin errors, with u(Lc=40) = 0.28749 and 0.28814; on 16^3 with the old guide at N_w = 240, 480, 960, 1920 (one seed, a second code path), u(Lc=0) = 0.28606, 0.28662, 0.28664, 0.28699 and the effective population N_eff = mean walker variance / generation variance of the population-mean local energy = 9.3, 10.3, 24.6, 15.6. The converged mixed estimator is the same for every positive guide, so the 16^3 difference shows that at least one of the two finite-population estimates is not converged; it does not say which, nor the converged value. The power-law population fit is not constrained (its exponent sits at the grid bound). Bin errors are 10-bin errors (lower bounds under autocorrelation); one seed unless stated. No certified eigenvalue, converged energy, population or projection convergence law, bias magnitude, limiting law, physical identification or audit verdict."
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
canonical zero-winding flip component of the cubic `L³` torus. This is the same
component as in
`RING_MODEL_ON_16_CUBED_A_LONGER_PROJECTION_LEAVES_THE_ENERGY_UNCHANGED_AND_MOVES_THE_CURVATURE_ESTIMATE_WITHIN_ITS_ERRORS_BOUNDED_THEOREM_NOTE_2026-09-28.md`.

- **Projector.** A fixed-population, continuous-time, importance-sampled walk,
  resampled every `Δτ = 0.015`.
- **Energy.** `u = −E/(3N)`, the mixed estimator.
- **Old guide.** `ψ = exp(0.2 N_flip)`.
- **Pair guide.** `ψ = exp(α N_flip + γ N_pair)`, where `N_pair` counts adjacent
  pairs of flippable plaquettes. The 8³ and 16³ runs use `α = 0.35`, `γ = −0.049`.

For any positive guide, the mixed estimator converges to the same ground energy
in the limit of infinite population and projection time.

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

The two 16³ values differ by `0.00068`, which is 5.9 combined bin errors. The
converged estimator does not depend on the guide. So at least one of the two
finite-population estimates is not converged. The data do not say which one,
and they do not give the converged value.

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
- They place the 16³ fixed-population energy within a guide-dependent window of
  at least `0.0007` per plaquette.
- That is comparable to the earlier 8³-to-16³ decrease of about `0.0017`.
- The effective population does not grow with the walker count over this range.

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
