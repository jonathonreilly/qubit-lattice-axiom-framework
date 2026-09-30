# DM Full Closure Same-Surface Endpoint Non-Overlap Arithmetic Certificate

**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Status:** bounded arithmetic certificate over helper-defined endpoint and
interval outputs only.
**Date:** 2026-04-16 (scope narrowed 2026-06-16 to arithmetic-only endpoint
non-overlap).
**Audit status:** assigned only by the independent audit lane.
**Script:** `scripts/frontier_dm_full_closure_same_surface_numerator_selector_boundary.py`

## Corrigendum (2026-09-30)

The interval values in "Computed Endpoint Data" below were computed with a half-sized Sommerfeld argument.
The arithmetic conclusions (ordering, endpoint disjointness) are unchanged; the numbers are superseded.

**1. Sommerfeld argument.** The thermal kernel behind these numbers used the Sommerfeld factor `S = pi z / (1 - e^{-pi z})`, `z = alpha / v`, where `v` is the relative speed carried by the weight `v^2 e^{-x_f v^2 / 4}`. For a pair of reduced mass `m/2` the s-wave Coulomb factor from the radial Schroedinger equation (wave number `k = m v / 2`, Coulomb parameter `eta = alpha / v`) is `S = 2 pi z / (1 - e^{-2 pi z})`. The old form is the textbook formula written for the per-particle centre-of-mass speed `v/2`; at fixed relative speed it is the correct function at half the coupling, `S_pi(alpha) = S_2pi(alpha/2)`.

Corrected helper-defined interval outputs (same endpoints):

```text
R(alpha_lo) in [7.971567066957, 7.971567066957]      (was [5.442019867867, 5.442019867931])
R(alpha_hi) in [8.067175363433, 8.067175363433]      (was [5.482855571890, 5.482855571936])

Omega_DM(alpha_lo) in [0.392144960613, 0.392144960613]  (was [0.267709052538, 0.267709052541])
Omega_DM(alpha_hi) in [0.396848215486, 0.396848215486]  (was [0.269717881594, 0.269717881596])
```

**2. Comparator.** The comparison values used in this lane (`5.469` from the rounded `0.268 / 0.049`, `5.47`, `5.375` / `5.38`, and `5.448` from `0.268` over the BBN `Omega_b`) are not the physical density ratio. The Planck-2018 physical densities, which cancel `h`, give `R_obs = (Omega_c h^2)/(Omega_b h^2) = 0.1200 / 0.02237 = 5.364 +/- 0.065` (`Omega_c h^2 = 0.1200 +/- 0.0012`, `Omega_b h^2 = 0.02237 +/- 0.00015`, TT,TE,EE+lowE+lensing; external comparator recalled from Planck 2018 results VI, not re-fetched; errors propagated as independent, the posterior correlation is not applied). Against that, the archived endpoint ratios `5.442` and `5.483` were `+1.5%` and `+2.2%` (`+1.2` and `+1.8` sigma) misses, not the `0.25%` agreement obtained against `5.469`. The runner comparator `5.4479` (`0.268` over the BBN `Omega_b` for `eta = 6.12e-10`) is itself `+1.6%` (`+1.3` sigma) above `5.364`.

**Evidence.** `scripts/dm_sommerfeld_kernel_radial_schrodinger_verification.py` (radial Schroedinger equation integrated numerically with no closed form, mpmath Coulomb function, independent quadrature; it reproduces the archived numbers as the corrected ones at half the coupling) and `scripts/dm_ratio_comparator_planck_central_values_check.py`. Both are same-family checks by their author, not independent referees. No audit verdict, effective status or status field is changed by this corrigendum. The runner is unchanged; its checks (ordering and disjointness only) still pass with the repaired
helper, and its cached output is re-pinned with the corrected numbers.

## Claim Boundary

This note verifies an arithmetic fact about the current helper-defined DM
same-surface packet:

- the helper layer supplies two endpoint couplings, `alpha_lo` and `alpha_hi`;
- the two endpoint couplings are distinct and both lie above the common
  ingredient `alpha_bare = 1/(4 pi)`;
- the helper-returned certified `R(alpha)` intervals at those endpoints are
  disjoint;
- after multiplying by the helper-returned `Omega_b`, the displayed
  `Omega_DM` intervals are also disjoint.

This is not a selector theorem, not an absence theorem, and not a
completeness theorem for the DM bank. The phrase "selector boundary" remains
only in the historical filename and runner name.

## Computed Endpoint Data

The runner obtains the following helper-defined values:

```text
alpha_lo = 0.090667836017286
alpha_hi = 0.092264992618360
alpha_bare = 0.079577471545948
```

and certified interval outputs:

```text
R(alpha_lo) in [5.442019867867, 5.442019867931]
R(alpha_hi) in [5.482855571890, 5.482855571936]

Omega_DM(alpha_lo) in [0.267709052538, 0.267709052541]
Omega_DM(alpha_hi) in [0.269717881594, 0.269717881596]
```

The arithmetic conclusion is exactly:

```text
alpha_bare < alpha_lo < alpha_hi,
R(alpha_lo)_hi < R(alpha_hi)_lo,
Omega_DM(alpha_lo)_hi < Omega_DM(alpha_hi)_lo.
```

## What This Does Not Prove

This note does not prove:

- that either endpoint is selected by the framework;
- that no other same-surface scale-selection datum exists;
- that the helper packet is complete;
- that the plaquette endpoint, eta/omega conversion, or certified-bound
  helpers have independent retained status in this row.

Any selector or completeness claim requires a separate bridge theorem.

## Verification

Run:

```bash
python3 scripts/frontier_dm_full_closure_same_surface_numerator_selector_boundary.py
```

Expected final line:

```text
SUMMARY: PASS=8 FAIL=0
```

Regenerate the cache with the standard runner-cache tool after editing the
runner.

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links named by a prior conditional audit so the audit citation graph can track them. It does not promote this note or change the audited claim scope.

- [dm_full_closure_same_surface_thermal_selector_sensitivity_boundary_note_2026-04-16](DM_FULL_CLOSURE_SAME_SURFACE_THERMAL_SELECTOR_SENSITIVITY_BOUNDARY_NOTE_2026-04-16.md)
- [dm_full_closure_same_surface_converged_thermal_selector_support_note_2026-04-16](DM_FULL_CLOSURE_SAME_SURFACE_CONVERGED_THERMAL_SELECTOR_SUPPORT_NOTE_2026-04-16.md)
