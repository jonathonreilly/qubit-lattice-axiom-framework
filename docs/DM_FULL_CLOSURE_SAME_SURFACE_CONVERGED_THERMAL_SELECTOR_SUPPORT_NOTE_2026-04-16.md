# DM Full Closure Same-Surface Converged Thermal Selector Support

**Status:** bounded - bounded or caveated result note
**Date:** 2026-04-16  
**Branch:** `codex/dm-thermal-review-2026-04-17`  
**Script:** `scripts/frontier_dm_full_closure_same_surface_converged_thermal_selector_support.py`

## Corrigendum (2026-09-30)

The positive result below (a unique interior selector on the one-scalar family) rests on a half-sized
Sommerfeld argument and is withdrawn. The sections below are kept as the record of what was claimed.

**1. Sommerfeld argument.** The thermal kernel behind these numbers used the Sommerfeld factor `S = pi z / (1 - e^{-pi z})`, `z = alpha / v`, where `v` is the relative speed carried by the weight `v^2 e^{-x_f v^2 / 4}`. For a pair of reduced mass `m/2` the s-wave Coulomb factor from the radial Schroedinger equation (wave number `k = m v / 2`, Coulomb parameter `eta = alpha / v`) is `S = 2 pi z / (1 - e^{-2 pi z})`. The old form is the textbook formula written for the per-particle centre-of-mass speed `v/2`; at fixed relative speed it is the correct function at half the coupling, `S_pi(alpha) = S_2pi(alpha/2)`.

With the corrected kernel and the same converged evaluator:

- `R(alpha_lo) = 7.971567067`, `R(alpha_hi) = 8.067175363`, both above the runner comparator `5.447934281`,
  so the one-scalar family has **no crossing** on `sigma in [0, 1]`. The archived `sigma_conv = 0.145077095756643`,
  `alpha_conv = 0.090899546858439`, `R_conv = 5.447934280746` and `Omega_DM = 0.268` belonged to the
  half-argument kernel; the corrected kernel gives `R = 5.447934` at `alpha = 0.0454498`, outside the family.
- The coarse retained grid and the converged evaluator agree at both endpoints to `7e-6`, so quadrature is not
  what separates the family from the comparator.
- The "fake `9/62`" conclusion stands, more strongly: at `sigma = 9/62` the corrected ratio is `7.985423`.
- Withdrawn: "the admitted one-scalar family still has a unique interior closure crossing" and "one-scalar
  admitted DM family: still yes" (the family is defined, but it does not reach the comparator).

**2. Comparator.** The comparison values used in this lane (`5.469` from the rounded `0.268 / 0.049`, `5.47`, `5.375` / `5.38`, and `5.448` from `0.268` over the BBN `Omega_b`) are not the physical density ratio. The Planck-2018 physical densities, which cancel `h`, give `R_obs = (Omega_c h^2)/(Omega_b h^2) = 0.1200 / 0.02237 = 5.364 +/- 0.065` (`Omega_c h^2 = 0.1200 +/- 0.0012`, `Omega_b h^2 = 0.02237 +/- 0.00015`, TT,TE,EE+lowE+lensing; external comparator recalled from Planck 2018 results VI, not re-fetched; errors propagated as independent, the posterior correlation is not applied). Against that, the archived endpoint ratios `5.442` and `5.483` were `+1.5%` and `+2.2%` (`+1.2` and `+1.8` sigma) misses, not the `0.25%` agreement obtained against `5.469`. The runner comparator `5.4479` (`0.268` over the BBN `Omega_b` for `eta = 6.12e-10`) is itself `+1.6%` (`+1.3` sigma) above `5.364`.

**Evidence.** `scripts/dm_sommerfeld_kernel_radial_schrodinger_verification.py` (radial Schroedinger equation integrated numerically with no closed form, mpmath Coulomb function, independent quadrature; it reproduces the archived numbers as the corrected ones at half the coupling) and `scripts/dm_ratio_comparator_planck_central_values_check.py`. Both are same-family checks by their author, not independent referees. No audit verdict, effective status or status field is changed by this corrigendum. The runner `scripts/frontier_dm_full_closure_same_surface_converged_thermal_selector_support.py`
is repaired to certify the absence of a crossing. Current-bank selector closure remains open.

## Question

After rejecting the unstable coarse thermal runner, does the admitted
one-scalar same-surface DM family still close on a numerically stable thermal
evaluation?

## Answer

Yes, at support level.

Using a corrected high-precision continuum thermal evaluator on the same-surface DM
family, the one-scalar admitted family still has a unique interior closure
crossing:

- `sigma_conv = 0.145077095756643`
- `alpha_conv = 0.090899546858439`
- `R_conv = 5.447934280746`
- `Omega_DM = 0.268000000000`

## Consequence

This does two useful things:

1. it preserves the positive one-scalar DM-side admitted family;  
2. it kills the fake `9/62` selector collapse.

The converged selector differs materially from both:

- the coarse retained runner:
  - `sigma_base = 0.145161097420491`
- the coarse structural clue:
  - `sigma_9/62 = 0.145161290322581`

## Honest Status

- current-bank DM selector closure: still no
- one-scalar admitted DM family: still yes
- this file remains a convergence/sanity check on the corrected continuum evaluator
- the theorem-grade promotion now lives in
  [DM_FULL_CLOSURE_SAME_SURFACE_THERMAL_BOUNDING_THEOREM_NOTE_2026-04-17.md](/Users/jonBridger/Toy%20Physics/.codex/dm-thermal-review/docs/DM_FULL_CLOSURE_SAME_SURFACE_THERMAL_BOUNDING_THEOREM_NOTE_2026-04-17.md:1)

## Command

```bash
python3 scripts/frontier_dm_full_closure_same_surface_converged_thermal_selector_support.py
```
