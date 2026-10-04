# DM Full Closure Same-Surface Thermal Selector Sensitivity Boundary

**Type:** bounded_theorem
**Claim type:** bounded_theorem


**Status:** bounded - bounded or caveated result note
**Date:** 2026-04-16  
**Branch:** `codex/dm-thermal-review-2026-04-17`  
**Script:** `scripts/frontier_dm_full_closure_same_surface_thermal_selector_sensitivity_boundary.py`

## Corrigendum (2026-09-30)

The roots quoted below (`sigma_2000 = 0.145161`, `sigma_4000 = 0.145600`, `sigma_8000 = 0.145585`,
`sigma_16000 = 0.145581`) belong to a kernel with a half-sized Sommerfeld argument. They are superseded;
the sections below are kept as the record.

**1. Sommerfeld argument.** The thermal kernel behind these numbers used the Sommerfeld factor `S = pi z / (1 - e^{-pi z})`, `z = alpha / v`, where `v` is the relative speed carried by the weight `v^2 e^{-x_f v^2 / 4}`. For a pair of reduced mass `m/2` the s-wave Coulomb factor from the radial Schroedinger equation (wave number `k = m v / 2`, Coulomb parameter `eta = alpha / v`) is `S = 2 pi z / (1 - e^{-2 pi z})`. The old form is the textbook formula written for the per-particle centre-of-mass speed `v/2`; at fixed relative speed it is the correct function at half the coupling, `S_pi(alpha) = S_2pi(alpha/2)`.

With the corrected kernel there is **no root** on `sigma in [0, 1]` at any quadrature resolution: on the
uniform grids of 2000, 4000, 8000 and 16000 points `R(alpha_lo)` runs `7.971519` to `7.971526` and
`R(alpha_hi)` runs `8.067127` to `8.067134`, against the comparator `5.447934`. The refinement spread
(`7e-6`) is negligible next to the gap (`2.52`), so quadrature is not the issue. The apparent `9/62`
near-coincidence was a coincidence of the half-argument kernel; `9/62` must still not be promoted (the answer
"No, not yet" stands, now because there is no selector root to compare with).

**Evidence.** `scripts/dm_sommerfeld_kernel_radial_schrodinger_verification.py` (radial Schroedinger equation integrated numerically with no closed form, mpmath Coulomb function, independent quadrature; it reproduces the archived numbers as the corrected ones at half the coupling) and `scripts/dm_ratio_comparator_planck_central_values_check.py`. Both are same-family checks by their author, not independent referees. No audit verdict, effective status or status field is changed by this corrigendum. The runner
`scripts/frontier_dm_full_closure_same_surface_thermal_selector_sensitivity_boundary.py` is repaired to certify
the absence of a root at every resolution. The comparator (see the bounding-theorem note's corrigendum) was also
a rounded value; against `5.364 +/- 0.065` the family is far above it either way.

**What still stands.** The exact rational/group skeleton (`R_base = 31/9`, the `8/9` and `1/9` channel
fractions, the low-`z` coefficients), and "the branch must not promote `9/62` as a DM selector law".

## Question

Is the apparent structural collapse clue

- `sigma ~= 1/(2 R_base) = 9/62`

actually robust on the retained same-surface DM kernel?

## Answer

No, not yet.

On the coarse retained thermal runner, the admitted-family selector appears to
land extremely close to

- `sigma = 9/62`.

But refining the thermal quadrature shifts the selector root by much more than
the apparent `9/62` residual itself. In particular:

- coarse retained root:
  - `sigma_2000 = 0.145161097420491`
- refined uniform-grid roots:
  - `sigma_4000 = 0.145600347860581`
  - `sigma_8000 = 0.145584750712540`
  - `sigma_16000 = 0.145580852564623`
- structural candidate:
  - `sigma_9/62 = 0.145161290322581`

So the near-coincidence with `9/62` is not stable under thermal refinement.

## Consequence

The branch must not promote `9/62` as a DM selector law.

The exact rational/group skeleton remains interesting:

- `R_base = 31/9`
- exact channel fractions `8/9`, `1/9`
- exact low-`z` weighted coefficients `7/12`, `19/144`

But the retained thermal layer is still too unstable to support selector
collapse from those exact ingredients.

## Honest Endpoint

The remaining DM-side problem is now clear:

1. current-bank selector closure: still no
2. minimal admitted one-scalar DM family: yes
3. structural `9/62` collapse claim: not yet justified
4. next real task:
   replace the retained thermal average with a converged or exact thermal
   theorem before trying to collapse the DM-side scalar further

## Command

```bash
python3 scripts/frontier_dm_full_closure_same_surface_thermal_selector_sensitivity_boundary.py
```
