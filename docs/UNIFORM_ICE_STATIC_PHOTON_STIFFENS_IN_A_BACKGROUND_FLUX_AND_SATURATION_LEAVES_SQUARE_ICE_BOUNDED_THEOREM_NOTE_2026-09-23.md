---
claim_id: uniform_ice_static_photon_stiffens_in_a_background_flux_and_saturation_leaves_square_ice_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "For uniform ice on infinite prisms, with the layer transfer T of the landed layer-unit note (PR 8740) applied by the row transfer of the landed note of PR 8859: at full polarization |S| = A every vertex has exactly one of its two vertical links occupied, so each layer carries two of four horizontal links at every vertex, and the top level of the |S| = A sector equals the number of square-ice configurations of the torus, exactly on 2 x 2, 2 x 4, 2 x 6, 2 x 8 and 4 x 4 (18, 114, 858, 7074, 2970). On 4 x 4 the flux cost c(S) = (A/S^2) ln(lam_0/lam_S) rises monotonically from 0.3270 at |S| = 2 to 0.4373 at |S| = 16. The branch rate D_s at physical wavenumber (pi/2, 0) in the |S| = s sector rises from 1.2963 at s = 0 to 1.3081, 1.3452, 1.4120, 1.5184 and 1.6846 at s = 2 to 10; the small-flux shift is quadratic (D_4 - D_0 = 4.118 (D_2 - D_0)). A local quartic cost fitted at |S| = 2 and 4 (c_2 = 0.3261, d = 0.0631) stiffens the field along the background (c_2 + 6 d rho^2) more than across it (c_2 + 2 d rho^2) and so predicts D_s/D_0 - 1 = 2 d rho^2/c_2, which accounts for 66% and 64% of the measured shift at s = 2 and 4. No limit beyond the computed cross-sections is claimed. No constant is compared with an outside value. No reading, rule, alphabet, unit or order law is adopted."

upstream_dependencies:
  - minimal_axioms
runner: scripts/uniform_ice_static_photon_stiffens_in_a_background_flux_and_saturation_leaves_square_ice_2026_09_23.py
---

# Uniform ice: the static photon stiffens in a background flux, and saturation leaves square ice

**Date:** 2026-09-23
**Type:** bounded_theorem
**Campaign:** second next-steps campaign. Open PRs 8871, 8881 and 8890
found that one Gaussian stiffness sets the flux cost and the correlations
of uniform ice at small flux. A Gaussian field is linear: its cost is
quadratic in the flux, and its excitations do not feel a background flux.
This block measures how uniform ice departs from linearity, all the way to
full polarization.

## Result up front

1. **Saturation leaves square ice, exactly.** At full polarization,
   |S| = A, every vertex has exactly one of its two vertical links
   occupied. The three-of-six rule then asks each layer for two of the four
   horizontal links at every vertex: square ice. Each of the sectors S = ±A
   holds one state, and T maps one to the other with weight equal to the
   number of square-ice configurations of the torus. The computed top
   levels agree exactly:

   | cross-section | top level at \|S\| = A | square-ice count |
   |---|---|---|
   | 2 × 2 | 18 | 18 |
   | 2 × 4 | 114 | 114 |
   | 2 × 6 | 858 | 858 |
   | 2 × 8 | 7074 | 7074 |
   | 4 × 4 | 2970 | 2970 |

   At saturation the layers decouple, and each carries two-dimensional ice.

2. **The equation of state on 4 × 4.** The flux cost
   c(S) = (A/S²) ln(λ_0/λ_S) rises monotonically: 0.3270, 0.3300, 0.3352,
   0.3430, 0.3543, 0.3705, 0.3950 and 0.4373 for |S| = 2 to 16. The field
   is Gaussian at small flux and stiffens by 34% at saturation.

3. **The photon feels a background flux.** The branch rate D_s at physical
   wavenumber (π/2, 0), in the sector |S| = s, rises with the background:
   1.2963, 1.3081, 1.3452, 1.4120, 1.5184 and 1.6846 for s = 0 to 10. At
   small flux the shift is quadratic in the background: D_4 − D_0 is 4.118
   times D_2 − D_0. A linear field would show no shift at all.

4. **A local quartic cost explains two thirds of it.** Fit c(ρ) = c_2 + d ρ²
   at |S| = 2 and 4, with ρ = S/A: c_2 = 0.3261, d = 0.0631. A cost
   A(c_2 ρ² + d ρ⁴) stiffens the field along the background, c_2 + 6dρ²,
   more than across it, c_2 + 2dρ². For a divergence-free field with
   stiffness K_z along and K_⊥ across, the rate is √(K_z/K_⊥) |q|, so
   D_s/D_0 − 1 = 2dρ²/c_2. This accounts for 66% and 64% of the measured
   shift at s = 2 and 4. The rest lies beyond a local quartic cost at this
   wavenumber, and it is recorded, not fitted.

5. **What this means.** The static photon of uniform ice is linear only at
   small flux. A background flux raises both its cost and its rate along
   the background, quadratically in the background. The medium responds
   nonlinearly, with its coefficients fixed by the rule and not fitted. At
   full polarization the three-dimensional field freezes into independent
   two-dimensional ice layers. The Gaussian photon of open PRs 8871, 8881
   and 8890 is the small-flux limit of this. No constant is compared with an
   outside value.

## Machine status and trace

- **Runner:**
  `scripts/uniform_ice_static_photon_stiffens_in_a_background_flux_and_saturation_leaves_square_ice_2026_09_23.py`
- **Result:** `TOTAL: PASS=4 FAIL=0`, about 136 s, stdout 975 characters,
  peak about 500 MB.
- **Cache:**
  `logs/runner-cache/uniform_ice_static_photon_stiffens_in_a_background_flux_and_saturation_leaves_square_ice_2026_09_23.txt`
- **Arithmetic:** exact integer row tensors and exact square-ice counts by
  a two-dimensional row transfer; sector tops by dense diagonalisation up
  to 400 states and by Lanczos iteration above; wavenumber sectors by the
  projector of open PR 8869.

## Premises and declared objects

- **Layer units and the transfer matrix:** the landed note of PR 8740.
- **Row transfer:** the landed note of PR 8859. T maps the flux S of a
  layer to −S, so a sector is |S| = s.
- **Branch rate:** as in open PR 8869, with physical wavenumber q at
  occupation wavenumber q + (π, π).
- **Square ice:** two of four links occupied at every vertex of the
  two-dimensional torus.

## Prior art and what is new

- Landed PR 8859: the flux cost on 4 × 4 up to |S| = 8.
- Open PRs 8871, 8881 and 8890: the Gaussian photon at small flux.
- New here: the exact saturation identity with square ice; the equation
  of state to full polarization; the photon's rate in a background flux;
  and the anisotropic quartic account of two thirds of its shift.

## Theorem — Saturation and the nonlinear response

At |S| = A the top level equals the square-ice count of the torus, which is
proved as stated and checked on five cross-sections. On 4 × 4 the flux
costs and branch rates are as stated. No limit is claimed beyond the
computed cross-sections.

## No-Go Discipline Gate

- **N1 alternative routes.** Larger cross-sections, where the quartic fit
  and the rate shift can be separated from lattice-scale wavenumbers.
- **N2 wall independence.** The saturation identity uses an independent
  two-dimensional count, and the rate shift is measured apart from the
  cost.
- **N3 hidden walls.** Floating-point eigenvalues with stated tolerance;
  the checked relations hold with margin.
- **N4 residual matching.** The third of the shift beyond the quartic
  account is reported, not fitted.
- **N5 rhetoric audit.** "Stiffens" means the stated rise in cost and rate
  on the computed cross-section.
- **N6 partial-closure paths.** The rate shift at smaller wavenumbers; the
  full dispersion in a background flux.
- **N7 steelman.** Against: one cross-section and one wavenumber for the
  rate. For: the quadratic law holds to 3% and the saturation identity is
  exact. Both are recorded.
- **N8 cross-cycle echo.** The landed notes of PRs 8740 and 8859 and open
  PRs 8869, 8871, 8881 and 8890 are cited.

## Falsifiers

- A cross-section whose saturated top level differs from its square-ice
  count.
- A background flux that lowers the branch rate at small flux.

## Boundaries and non-claims

- The computed cross-sections; the rate at one wavenumber.
- No limit of large cross-sections is claimed.
- No reading, rule, alphabet, unit or order law is adopted.
- Nothing here grades, unlocks or audits any other claim.

## Imports

The minimal axioms, the landed notes of PRs 8740 and 8859, and open PRs
8869, 8871, 8881 and 8890 are cited. No audit grade, no new axiom, no new
primitive, no new comparator and no new framing is imported.

## Review record

- **Seat:** one Opus 5.5 seat; no subagents; runner and note by the same
  seat.
- **Independence sources:** the two-dimensional square-ice count; the cost
  and the rate as separate spectra.
- **Correction before landing.** A first version built the dense sector
  matrices from rows of an N × N identity, which reached 1.6 GB on this
  machine. It now builds each unit vector directly (peak about 500 MB).
- **Mutation census** (caught means at least one FAIL line or a nonzero
  exit; the runner exits nonzero on any FAIL):

| Mutant | Change | Result |
|---|---|---|
| square ice counted with one occupied link per vertex | count changed | caught (1 FAIL) |
| flux sector S = s in place of \|S\| = s | sector changed | caught (nonzero exit) |
| cost without the 1/S² | cost changed | caught (2 FAILs) |
| photon read at occupation wavenumber (π/2, 0) | wavenumber offset dropped | caught (2 FAILs) |
| quartic stiffening isotropic | anisotropy dropped | caught (1 FAIL) |
| two occupied links per vertex | rule changed | caught (4 FAILs) |
| wrap links not identified | wrap dropped | caught (4 FAILs) |
| row translation by two sites | projector broken | caught (2 FAILs) |

  8 of 8 are caught.
- **Vacuity guard:** every count, cost, rate and fraction is printed.
- **Budget:** 4 checks, stdout 975 characters (ceiling 6000), about 136 s
  (ceiling 900 s), peak about 500 MB.

## Verification

```bash
python3 scripts/uniform_ice_static_photon_stiffens_in_a_background_flux_and_saturation_leaves_square_ice_2026_09_23.py
```

Expected summary line: `TOTAL: PASS=4 FAIL=0`; the runner exits nonzero
if any check fails. Cached output:
`logs/runner-cache/uniform_ice_static_photon_stiffens_in_a_background_flux_and_saturation_leaves_square_ice_2026_09_23.txt`.
