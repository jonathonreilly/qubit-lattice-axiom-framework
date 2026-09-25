---
claim_id: ring_model_the_ten_cubed_point_lies_between_the_linear_and_level_readings_and_a_constant_plus_a_linear_term_fits_the_four_sizes_mildly_better_than_a_power_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "Setting, all supplied and none adopted: spin-1/2 link fields on the cubic lattice with the exact vertex Gauss law (cubic ice) and the covariant plaquette clause -g (U + U^dag) at V = 0, g = 1 (open PRs 9066, 9072); the guided continuous-time projector Monte Carlo of open PR 9148 with the forward-walking estimator of open PR 9161 in the zero-winding sector of open PR 9153. Finite diagnostics on the 10^3 torus (100 walkers, projection 32, forward lags to 6, ten-bin errors): energy per plaquette -0.28741 +- 0.00010; pure transverse structure factor at k_min = pi/5 S_T = 0.510 +- 0.046 (lags 1/2/4/6: 0.543, 0.510, 0.506, 0.512, each +- 0.04; mixed 0.623), at 2pi/5 0.714 +- 0.043; Feynman bound 2 u_0 s^2 / S_T = 0.430 +- 0.039, omega L = 4.30, omega/k = 0.685; the mode's ground-state correlation has effective rates 0.42 +- 0.46, 0.39 +- 0.32, 0.41 +- 0.16 on [0, 0.3], [0.5, 1], [1, 2]. An auxiliary 120-walker projection-40 run (not in the runner) gave S_T(k_min) = 0.495 +- 0.035 with rates 0.43, 0.41, 0.43. The four-size series with open PR 9161's certified 0.692 +- 0.013, 0.557 +- 0.022, 0.575 +- 0.028: pairwise exponents 0.54 +- 0.11 (4^3-6^3), -0.11 +- 0.22 (6^3-8^3), 0.53 +- 0.46 (8^3-10^3), 0.33 +- 0.10 (4^3-10^3); weighted power law nu = 0.34 +- 0.06 (chi^2 5.1 for 2 degrees of freedom); linear-plus-constant S = S_0 + a k with S_0 = 0.392 +- 0.040, a = 0.189 +- 0.030 (chi^2 3.8); their 12^3 predictions 0.473 and 0.491; the 10^3 point against open PR 9166's readings: linear 0.46 (+1.1 standard errors), level 0.575 (-1.4), quadratic 0.375 (+3.0). The Feynman bound at k_min on 4^3-10^3 has omega L = 6.77, 6.22, 4.69, 4.30 and a fitted exponent in k of 1.45 (1 linear, 2 quadratic). No power law, no gap value, no phase and no thermodynamic limit is claimed. Correction (open PR 9220): the ten-bin errors of the forward-walking structure factor understate the run-to-run scatter by about a factor of two, so both fits are within that scatter; run averages give 0.710 +- 0.010, 0.572 +- 0.018, 0.491 +- 0.022 on 4^3, 6^3, 8^3; the auxiliary 12^3 and 16^3 runs at 100-120 walkers carry a population bias that grows with the torus, and the fixed-momentum growth they show is not established."
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

- **The 12³ and 16³ runs (auxiliary, not in the runner) do not decide.**
  At `k_min = π/6` the 12³ torus gave `S_T = 0.496 ± 0.057` (100 walkers)
  and at `π/8` the 16³ torus gave `0.591 ± 0.037` (120 walkers). At fixed
  momentum the measured values grow with the torus (`S_T(π/3)`: 0.557 on
  6³, 0.778 on 12³; `S_T(π/2)`: 0.692 on 4³, 0.75–0.83 on 8³, 0.89–0.94 on
  12³, 1.04 on 16³). Open PR 9220 found that these runs are not a clean
  test: the walker weights spread as the square root of the system size, so
  the population bias grows with the torus (on 8³ it already moves the
  energy per plaquette by 0.0012 between 60 and 480 walkers), and the
  forward-walking errors are about half the run-to-run scatter. The
  fixed-momentum growth is therefore not established as a property of the
  ground state; an earlier version of this bullet read it as one, and that
  reading is withdrawn.

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

- **Fixed momentum, growing size (not established).** `S_T(π/3)`:
  `0.557 ± 0.022` (6³) → `0.778 ± 0.048` (12³). `S_T(π/2)`: `0.692 ± 0.013`
  (4³) → `0.75–0.83` (8³) → `0.89–0.94` (12³) → `1.039 ± 0.073` (16³; that
  run, 120 walkers and projection 30, also gave `S_T(π/4) = 0.770 ± 0.047`,
  `S_T(π/8) = 0.591 ± 0.037` and `e_0 = −0.28576` per plaquette). An earlier
  version read the flat forward-walking lags as showing that the growth is
  in the ground state. That does not follow: flat lags exclude a lag bias,
  not a population bias. Open PR 9220 measured the population bias on 8³
  (the energy and the short-range correlations move with the walker number,
  and extrapolating in it returns the 6³ value of the nearest-neighbour
  correlation), found the weight spread per block twice as large on 12³
  and 16³ as on 8³, and found the forward-walking errors understated by
  about a factor of two. The growth may be a finite-size property of the
  ground state or a bias that grows with the torus; these runs do not
  decide.
- **The series and the bound.** Earlier bullets here built lower bounds on
  the infinite-lattice structure factor, and a smaller Feynman bound, from
  the largest-torus values; they are withdrawn with the reading they rested
  on. Averaged over independent runs (open PR 9220) the smallest-momentum
  structure factor is `0.710 ± 0.010`, `0.572 ± 0.018`, `0.491 ± 0.022` on
  4³, 6³, 8³, a monotonic fall; the two fits of this note use single-run
  ten-bin errors and are within the run-to-run scatter.
- **The mode at the smallest momentum.** Its correlation decays with rate
  `0.25–0.33` at `π/6` on 12³ and `0.07–0.13` at `π/8` on 16³, with the same
  caveats.

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

- A controlled walker population first (open PR 9220), then the fixed-`k`
  extrapolations in `L`: `S_T(π/2)` on 16³, `S_T(π/3)` on
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
