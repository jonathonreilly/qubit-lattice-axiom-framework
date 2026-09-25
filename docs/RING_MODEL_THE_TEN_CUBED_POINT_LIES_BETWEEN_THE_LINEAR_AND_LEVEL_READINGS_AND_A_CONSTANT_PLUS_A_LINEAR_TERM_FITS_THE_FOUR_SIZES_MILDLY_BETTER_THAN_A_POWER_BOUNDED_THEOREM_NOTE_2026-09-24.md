---
claim_id: ring_model_the_ten_cubed_point_lies_between_the_linear_and_level_readings_and_a_constant_plus_a_linear_term_fits_the_four_sizes_mildly_better_than_a_power_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "Setting, all supplied and none adopted: spin-1/2 link fields on the cubic lattice with the exact vertex Gauss law (cubic ice) and the covariant plaquette clause -g (U + U^dag) at V = 0, g = 1 (open PRs 9066, 9072); the guided continuous-time projector Monte Carlo of open PR 9148 with the forward-walking estimator of open PR 9161 in the zero-winding sector of open PR 9153. Finite diagnostics on the 10^3 torus (100 walkers, projection 32, forward lags to 6, ten-bin errors): energy per plaquette -0.28741 +- 0.00010; pure transverse structure factor at k_min = pi/5 S_T = 0.510 +- 0.046 (lags 1/2/4/6: 0.543, 0.510, 0.506, 0.512, each +- 0.04; mixed 0.623), at 2pi/5 0.714 +- 0.043; Feynman bound 2 u_0 s^2 / S_T = 0.430 +- 0.039, omega L = 4.30, omega/k = 0.685; the mode's ground-state correlation has effective rates 0.42 +- 0.46, 0.39 +- 0.32, 0.41 +- 0.16 on [0, 0.3], [0.5, 1], [1, 2]. An auxiliary 120-walker projection-40 run (not in the runner) gave S_T(k_min) = 0.495 +- 0.035 with rates 0.43, 0.41, 0.43. The four-size series with open PR 9161's certified 0.692 +- 0.013, 0.557 +- 0.022, 0.575 +- 0.028: pairwise exponents 0.54 +- 0.11 (4^3-6^3), -0.11 +- 0.22 (6^3-8^3), 0.53 +- 0.46 (8^3-10^3), 0.33 +- 0.10 (4^3-10^3); weighted power law nu = 0.34 +- 0.06 (chi^2 5.1 for 2 degrees of freedom); linear-plus-constant S = S_0 + a k with S_0 = 0.392 +- 0.040, a = 0.189 +- 0.030 (chi^2 3.8); their 12^3 predictions 0.473 and 0.491; the 10^3 point against open PR 9166's readings: linear 0.46 (+1.1 standard errors), level 0.575 (-1.4), quadratic 0.375 (+3.0). The Feynman bound at k_min on 4^3-10^3 has omega L = 6.77, 6.22, 4.69, 4.30 and a fitted exponent in k of 1.45 (1 linear, 2 quadratic). No power law, no gap value, no phase and no thermodynamic limit is claimed."
upstream_dependencies:
  - minimal_axioms
  - uniform_ice_rk_photon_single_mode_bound_is_quadratic_with_the_sum_rule_stiffness_bounded_theorem_note_2026-09-23
runner: scripts/ring_model_pure_structure_factor_on_the_ten_cubed_torus_and_the_four_size_series_at_the_smallest_momentum_2026_09_24.py
---

# The 10³ point lies between the linear and level readings, and a constant plus a linear term fits the four sizes mildly better than a power

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** finite numerical diagnostics under supplied decision points; unaudited.

## Result

Open PR 9161 measured the pure transverse structure factor of the
pure-ring ground state at the smallest momentum on 4³, 6³, 8³
(`0.692, 0.557, 0.575`): a fall, then a level step, and no resolved power.
Open PR 9166 supplied a Gaussian comparator and predicted the 10³ value
under three readings: `0.46` for a linear photon, `0.575` for a level,
`0.375` for a quadratic law. This note adds the 10³ point.
- **Between linear and level, not quadratic.** `S_T(k_min = π/5) = 0.510 ± 0.046`
  (forward lag 2; lags 1, 4, 6 give `0.543, 0.506, 0.512`, a plateau
  within errors; the mixed value 0.623 shows the bias the lags remove): 1.1
  standard errors above the linear reading, 1.4 below the level and 3.0
  above the quadratic. An auxiliary run with 120 walkers and projection 40
  gave `0.495 ± 0.035`; the two seeds together put the point near
  `0.50 ± 0.03`, about 2 standard errors below the 8³ value.
- **A constant plus a linear term fits mildly better than a power.** Over
  the four sizes the weighted power law gives `ν = 0.34 ± 0.06` with
  `χ² = 5.1` for two degrees of freedom, while `S_T = S_0 + a·k` gives
  `S_0 = 0.392 ± 0.040`, `a = 0.189 ± 0.030` with `χ² = 3.8`. Pairwise
  exponents: `0.54 ± 0.11` (4³–6³), `−0.11 ± 0.22` (6³–8³),
  `0.53 ± 0.46` (8³–10³). The two forms predict nearly the same 12³ value
  (`0.473` and `0.491`), so 12³ at this precision does not separate them
  from each other; it separates both from the pure linear form through 8³
  (`0.39`, open PR 9166) by about 2.5 standard errors.
- **The mode stays a single excitation.** The ground-state correlation at
  `k_min` has effective rates `0.42 ± 0.46`, `0.39 ± 0.32`, `0.41 ± 0.16`
  on `[0, 0.3]`, `[0.5, 1]`, `[1, 2]`, flat within errors, so the lowest
  coupled excitation at `π/5` sits near `0.4` (its product with `L` near
  4); the Feynman bound is `0.430 ± 0.039` (`ω·L = 4.30`, `ω/k = 0.685`).
- **The bound's exponent in `k` is between one and two.** Over the four
  smallest momenta the bound `2u_0 s²/S_T` scales as `k^{1.45}`; its
  product with `L` runs `6.77, 6.22, 4.69, 4.30`.

- **The 12³ run (auxiliary, not in the runner) shifts the reading.** At
  `k_min = π/6`, `S_T = 0.496 ± 0.057` (forward lags 1–6 on a plateau
  `0.52–0.49`, lag 8 `0.458 ± 0.034`), on top of both fits' predictions
  (0.473, 0.491) and 1.9 standard errors above the pure linear form through
  8³. But at fixed momentum the structure factor grows with the torus:
  `S_T(π/3) = 0.557 ± 0.022` on 6³ against `0.778 ± 0.048` on 12³ (four
  standard errors), and `S_T(π/2) = 0.692 ± 0.013` on 4³, `0.75–0.83` on
  8³, `0.89 ± 0.08` rising to `0.94 ± 0.06` across the lags on 12³. The
  smallest-momentum series therefore mixes the `k`-dependence with a
  finite-size suppression that weakens as `L` grows, and neither fit above
  has an infinite-volume meaning; the observable that does is `S_T(k)` at
  fixed `k` extrapolated in `L`, whose present lower bounds are
  `0.94, 0.78, 0.58, 0.51, 0.50` at `k = π/2, π/3, π/4, π/5, π/6`.

Supplied model, finite diagnostics: no power law, no gap value, no phase
and no thermodynamic limit is claimed. If the constant `S_0` in the
mildly preferred form persists as `L` grows, the transverse fluctuations
keep about a quarter of the uniform-ice pinch-point weight at long
wavelengths and the Feynman quotient turns quadratic there; if it fades,
the linear term is the photon. Open PR 9166 shows why the value of
`S_T(k_min)`, not the quotient's power, is the separator; the separation
needs tori beyond 12³ or a sharper 12³ point.

## Setting and decision points

- **D-gauss, D-roles, D-ring (open PRs 9066, 9072).** Link qubits at link
  sites of the doubled lattice; the exact vertex Gauss law; the covariant
  plaquette clause `−g (U + U†)`; `V = 0`; `g = 1`.
- **Methods.** The projector of open PR 9148, the sector construction of
  open PR 9153, the transverse mode and lineage estimator of open PR 9161
  (six modes per momentum: three axes, two polarisations), forward lags
  `1, 2, 4, 6`, the sum rule of open PR 9163 (the numerator of the Feynman
  bound is `2u_0 s²` exactly).
- **Comparison.** The Gaussian comparator of open PR 9166 supplies the
  three readings; the landed note
  `UNIFORM_ICE_RK_PHOTON_SINGLE_MODE_BOUND_IS_QUADRATIC_WITH_THE_SUM_RULE_STIFFNESS_BOUNDED_THEOREM_NOTE_2026-09-23.md`
  supplies the uniform-ice normalisation.

None is adopted.

## Diagnostic — the 10³ point and the series

| torus | `k_min` | `e_0` | `S_T(k_min)` pure | `ω_SMA` | `ω·L` | `ω/k` | late rate |
|---|---|---|---|---|---|---|---|
| 4³ | π/2 | −0.29263 | 0.692 ± 0.013 (open PR 9161) | 1.690 | 6.76 | 1.076 | 1.40 ± 0.15 |
| 6³ | π/3 | −0.28885 | 0.557 ± 0.022 (open PR 9161) | 1.037 | 6.22 | 0.990 | 0.77 ± 0.21 |
| 8³ | π/4 | −0.28800 | 0.575 ± 0.028 (open PR 9161) | 0.587 | 4.69 | 0.747 | 0.47 ± 0.18 |
| 10³ | π/5 | −0.28741 ± 0.00010 | 0.510 ± 0.046 | 0.430 | 4.30 | 0.685 | 0.39 ± 0.32 |

- **Forward-walking convergence.** Open PR 9166 noted that the lag needed
  for the pure estimator grows with the torus as the relevant gap falls;
  here lags `1, 2, 4, 6` give `0.543, 0.510, 0.506, 0.512 (each ± 0.04)`, a plateau within errors, and the
  mixed value `0.623` shows the size of the bias the lags remove.
- **Population control.** 100 walkers here against 120 in the auxiliary
  run (`0.495 ± 0.035`); on 8³ open PR 9161 found 120 against 240 walkers
  moving `S_T` by less than 1.2 standard errors. The 10³ energy at 100–120
  walkers sits about 0.001 per plaquette above the 8³ value at 240, the
  size of the population-control bias seen there.
- **The fits.** With four points and two parameters each, both forms have
  two degrees of freedom; the power law's `χ² = 5.1` against the
  constant-plus-linear form's `3.8` is a mild preference, one unit and a
  third of `χ²`, not a decision. The
  level step between 6³ and 8³ is what the power law cannot absorb.
- **Second momentum.** `S_T(2π/5) = 0.714 ± 0.043` on 10³ continues the rise with
  `k` at fixed size seen on 8³ (`0.575, 0.833, 1.019` at `π/4, π/2, 3π/4`).

## Auxiliary — the 12³ run and the fixed-momentum series

One run on the 12³ torus (100 walkers, projection 34, blocks of 0.05, the
first 12 discarded, forward lags 1, 2, 4, 6, 8, seed 22; 28 minutes on one
core) is quoted here without a runner of its own; its numbers are not
certified by the cache of this note.

| quantity | value |
|---|---|
| `e_0` per plaquette | `−0.28665 ± 0.00010` (100 walkers; the population-control bias grows with the torus: 8³ gave −0.28800 at 120 and −0.28813 at 240 walkers) |
| `S_T(π/6)`, lags 1 / 2 / 4 / 6 / 8 | `0.518 ± 0.050`, `0.496 ± 0.057`, `0.502 ± 0.057`, `0.486 ± 0.054`, `0.458 ± 0.034` (mixed 0.585) |
| `S_T(π/3)`, lags 1–8 | `0.788, 0.778, 0.792, 0.789, 0.777` (`± 0.03–0.05`; mixed 0.797) |
| `S_T(π/2)`, lags 1–8 | `0.874, 0.891, 0.923, 0.923, 0.943` (`± 0.06–0.08`; mixed 0.956) |
| Feynman bound at `π/6` | `0.310 ± 0.036`, `ω·L = 3.72`, `ω/k = 0.59` |
| correlation rates at `π/6` on `[0, 0.3]`, `[0.5, 1]`, `[1, 2]` | `0.33, 0.28, 0.24` (each `± 0.3–0.5`) |

- **Fixed momentum, growing size.** `S_T(π/3)`: `0.557 ± 0.022` (6³) →
  `0.778 ± 0.048` (12³), a growth of `0.22 ± 0.05`. `S_T(π/2)`:
  `0.692 ± 0.013` (4³) → `0.833 ± 0.040` / `0.751 ± 0.018` (8³ at 120 /
  240 walkers) → `0.89–0.94` (12³). The lags are flat at `π/3` and rise
  with the lag at `π/2`, so the growth is in the ground state, not in the
  estimator. This is the effect open PR 9166 found outside any Gaussian at
  2.7–3.4 standard errors on 8³; on 12³ it is resolved at four.
- **What it does to the series.** Each `S_T(k_min(L), L)` sits on the
  finite-size-suppressed branch of its own torus; the fall from 0.692 to
  0.496 along the series is the sum of the `k`-dependence (a fall) and the
  suppression's weakening (a rise), and the level step between 6³ and 8³ is
  where the two nearly cancel. The constant-plus-linear and power fits
  describe this composite, not `S_∞(k)`. Present lower bounds on
  `S_∞(k)`, taking the largest torus at each momentum, are `0.94, 0.78,
  0.58, 0.51, 0.50` at `k = π/2, π/3, π/4, π/5, π/6`: a factor 1.9 over a
  factor 3 in `k`, still growing at the larger momenta.
- **The bound follows.** With `S_∞(k)` larger than the series values, the
  Feynman bound at each `k` is smaller than the series gave: `1.25` at
  `π/2` and `0.74` at `π/3` on 12³ against `1.69` and `1.04` on 4³ and 6³.
  The mode at `π/6` decays with rate `0.25–0.33`, `ω·L ≈ 3–4`.

## What this means for the lanes

- **Photon lane.** Four sizes now: the smallest-momentum fluctuations fall
  from 0.69 to about 0.5 with one level step, are described mildly better
  by a constant near a quarter of the uniform-ice value plus a linear term
  than by a power, and the mode
  at each `k_min` decays as one exponential with a rate that falls with
  the momentum. The Feynman bound's exponent in `k` is between one and two.
  Whether the constant persists is the question for 12³ and beyond; open
  PRs 9163 and the sweep of the companion block show where the weight
  goes and that the redistribution is continuous from the RK point.
- **What the framework supplied.** The Gauss law, the ring and `V = 0` are
  decision points; the estimators and the comparator are methods.

## What stays open

- The fixed-`k` extrapolations in `L`: `S_T(π/2)` on 16³, `S_T(π/3)` on
  18³, `S_T(π/4)` on 16³, at a precision of 0.03, which need 250–500
  walkers and forward lags growing with the torus; a certified 12³ point.
- The late-time gap on 10³ beyond `τ = 2`.
- Independent checks of every number here.

## Prior art

Feynman 1954; Rokhsar and Kivelson 1988; Trivedi and Ceperley 1990;
Hermele, Fisher and Balents 2004; Benton, Sikora and Shannon 2012. All
cited as prior art, not as premises.

## Checks

The runner has 3 checks and all pass in about 8 minutes, single-threaded.

| Check | Result |
|---|---|
| 10³ point | Energy in range; `S_T(k_min)` resolved (error ≤ 12 %) with a lag plateau; correlation chain (early rate ≤ bound; later rates ≤ earlier within errors). |
| Four-size series | Pairwise exponents, both fits with `χ²`, 12³ predictions, the 10³ point against open PR 9166's readings (reported). |
| Feynman bound series | `ω·L`, `ω/k` and the exponent in `k` over the four points (reported). |

## Independent check

None yet. The runner was rerun from a clean shell to write the cache;
seeded Monte Carlo reproduces the numbers. The auxiliary 120-walker run is
a second seed of the 10³ point.

## What this does not do

- It adopts no clause, Gauss law, method or comparison.
- It claims no power law, no gap value, no phase and no thermodynamic
  limit; both fits are two-parameter descriptions of four finite-torus
  numbers with Monte Carlo errors.
