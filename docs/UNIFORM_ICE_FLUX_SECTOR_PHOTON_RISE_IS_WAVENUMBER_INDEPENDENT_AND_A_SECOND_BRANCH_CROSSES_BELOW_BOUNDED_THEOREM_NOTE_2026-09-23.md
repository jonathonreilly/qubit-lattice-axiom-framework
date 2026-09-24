---
claim_id: uniform_ice_flux_sector_photon_rise_is_wavenumber_independent_and_a_second_branch_crosses_below_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "On the strips 2 x 4 to 2 x 10 of uniform ice, with the layer transfer of the landed layer-unit note (PR 8740) applied by the row transfer of the landed note of PR 8859, the branch rate in the flux sector |S| = s at physical wavenumber (0, q) is D_s(q) = ln(lam_s / |lam_top(k)|), k = (pi, pi + q), and its shift is d_s(q) = D_s(q) - D_0(q). At |S| = 2 the shifts at the smallest wavenumbers agree within 25% while D_0 grows by at least 60% across them: 0.01672 and 0.01418 on 2 x 6 (D_0 0.951 to 1.563), 0.00765, 0.00756 and 0.00798 on 2 x 8 (D_0 0.743 to 1.658), 0.00404 and 0.00438 on 2 x 10 (D_0 0.606 to 1.117). The shift is quadratic in the background: d_4/d_2 lies between 4.10 and 4.39 at each of those wavenumbers. At fixed flux density rho = 1/4 and q = pi/2 the shift shrinks with the cross-section, 0.0436 on 2 x 4 (|S| = 2) against 0.0323 on 2 x 8 (|S| = 4). At the zone boundary q = pi the top of the |S| = 2 sector lies below the zero-flux photon on every strip, by 0.1207, 0.1592, 0.1712 and 0.1765 on 2 x 4 to 2 x 10: another state leads there. On 2 x 8 that state is even under the complement v -> 1 - v and has a positive level, while the zero-flux photon at q = pi is odd with a negative level, and the |S| = 2 top at q = pi/4 is odd and negative like the photon: the second branch is not a single photon but a mode of the flux sector itself. Whether the rise survives on large cross-sections at fixed density is not decided. No constant is compared with an outside value. No reading, rule, alphabet, unit or order law is adopted."

upstream_dependencies:
  - minimal_axioms
runner: scripts/uniform_ice_flux_sector_photon_rise_is_wavenumber_independent_and_a_second_branch_crosses_below_2026_09_23.py
---

# Uniform ice: in a flux sector the photon's rate rises by a wavenumber-independent amount, and a second branch crosses below it

**Date:** 2026-09-23
**Type:** bounded_theorem
**Campaign:** second next-steps campaign. Open PR 8928 found that a
background flux raises the photon's rate on the 4 × 4 prism by the same
amount at two wavenumbers. The rise is near-constant, not the rescaling a
smooth quartic cost would give, and its origin was left open. This block
measures the rise on strips, where more wavenumbers and more sizes are
available.

## Result up front

1. **The measure.** On a strip 2 × b the branch rate in the flux sector
   |S| = s at physical wavenumber (0, q) is D_s(q) = ln(λ_s/|λ_top(k)|),
   with k = (π, π + q) as in open PR 8869. Its shift is
   d_s(q) = D_s(q) − D_0(q).

2. **The rise does not follow the wavenumber.** At |S| = 2:

   | strip | shifts at the smallest wavenumbers | D_0 across them |
   |---|---|---|
   | 2 × 6 | 0.01672, 0.01418 | 0.951 to 1.563 |
   | 2 × 8 | 0.00765, 0.00756, 0.00798 | 0.743 to 1.658 |
   | 2 × 10 | 0.00404, 0.00438 | 0.606 to 1.117 |

   The shifts agree within 25% while D_0 grows by 60% or more.

3. **It is quadratic in the background.** At each of those wavenumbers
   d_4/d_2 lies between 4.10 and 4.39: doubling the flux about quadruples
   the rise.

4. **At fixed density it shrinks with the cross-section.** At density
   ρ = 1/4 and q = π/2 the rise is 0.0436 on 2 × 4 (|S| = 2) and 0.0323 on
   2 × 8 (|S| = 4).

5. **A second branch, and it is not a photon.** At the zone boundary
   q = π, the top of the |S| = 2 sector lies below the zero-flux photon on
   every strip, by 0.1207, 0.1592, 0.1712 and 0.1765 on 2 × 4 to 2 × 10.
   On 2 × 8 that state is even under the complement v → 1 − v and has a
   positive level, while the zero-flux photon at q = π is odd with a
   negative level (open PR 8869). At q = π/4 the |S| = 2 top is odd and
   negative, like the photon. The branch leading at the zone boundary is
   therefore a mode of the flux sector itself, not a single photon.

6. **What this means.** On these cross-sections a background flux raises
   the photon's rate by an amount that is independent of the wavenumber
   and quadratic in the flux, and that at fixed density shrinks as the
   cross-section grows. A smooth nonlinear medium would rescale the rate
   instead. The data are consistent with a finite-size effect of discrete
   flux quanta, each a threading line on these small cross-sections, which
   also carry a complement-even branch of their own that leads near the
   zone boundary. Whether any
   rise survives on large cross-sections at fixed density is not decided
   here. This sharpens the open point of open PR 8928 without closing it.
   No constant is compared with an outside value.

## Machine status and trace

- **Runner:**
  `scripts/uniform_ice_flux_sector_photon_rise_is_wavenumber_independent_and_a_second_branch_crosses_below_2026_09_23.py`
- **Result:** `TOTAL: PASS=5 FAIL=0`, about 290 s, stdout 1279 characters,
  peak about 1.1 GB.
- **Cache:**
  `logs/runner-cache/uniform_ice_flux_sector_photon_rise_is_wavenumber_independent_and_a_second_branch_crosses_below_2026_09_23.txt`
- **Arithmetic:** exact integer row tensors; sector tops by dense
  diagonalisation up to 400 states and Lanczos iteration above; wavenumber
  sectors by the projector of open PR 8869.

## Premises and declared objects

- **Layer units and the transfer matrix:** the landed note of PR 8740.
- **Row transfer:** the landed note of PR 8859. A flux sector is |S| = s.
- **Branch rate:** as in open PR 8869.

## Prior art and what is new

- Open PR 8928: the rise on 4 × 4 at two wavenumbers.
- New here: the rise on strips at up to three wavenumbers each; its
  quadratic law; its shrinking at fixed density; the second branch at the
  zone boundary and its complement parity.

## Theorem — The flux-sector rise on the computed strips

On the strips 2 × 4 to 2 × 10 the shifts are as stated. No limit is
claimed beyond the computed cross-sections.

## No-Go Discipline Gate

- **N1 alternative routes.** Larger cross-sections at fixed density, for
  which this machine's memory is the limit.
- **N2 wall independence.** The zero-flux rates reproduce open PR 8869.
- **N3 hidden walls.** Floating-point eigenvalues with stated tolerance.
- **N4 residual matching.** Nothing is fitted.
- **N5 rhetoric audit.** "Wavenumber-independent" means the stated 25%
  agreement against D_0's growth; "consistent with a finite-size effect"
  is a reading, not a claim.
- **N6 partial-closure paths.** The rise at fixed density on squares; the
  second branch's own dispersion.
- **N7 steelman.** For a genuine medium effect: the rise is quadratic in
  the flux. Against: at fixed density it shrinks with size, and it does not
  rescale. Both are recorded.
- **N8 cross-cycle echo.** Open PRs 8869 and 8928 and the landed notes of
  PRs 8740 and 8859 are cited.

## Falsifiers

- A strip on which the |S| = 2 shifts at the smallest wavenumbers differ by
  more than 25%.
- A strip on which the zone-boundary top of the |S| = 2 sector lies above
  the zero-flux photon.

## Boundaries and non-claims

- The strips 2 × 4 to 2 × 10.
- No large-cross-section limit is claimed.
- No reading, rule, alphabet, unit or order law is adopted.
- Nothing here grades, unlocks or audits any other claim.

## Imports

The minimal axioms, the landed notes of PRs 8740 and 8859, and open PRs
8869 and 8928 are cited. No audit grade, no new axiom, no new primitive, no
new comparator and no new framing is imported.

## Review record

- **Seat:** one Opus 5.5 seat; no subagents; runner and note by the same
  seat.
- **Independence sources:** the zero-flux rates of open PR 8869; the shifts
  measured at several wavenumbers and sizes.
- **Mutation census** (caught means at least one FAIL line or a nonzero
  exit; the runner exits nonzero on any FAIL):

| Mutant | Change | Result |
|---|---|---|
| wavenumber offset dropped | sectors misread | caught (4 FAILs) |
| flux sector S = s in place of \|S\| = s | sector changed | caught (nonzero exit) |
| two occupied links per vertex | rule changed | caught (4 FAILs) |
| zone boundary read one step early | wavenumber changed | caught (1 FAIL) |
| fixed density read at the wrong flux | sector changed | caught (1 FAIL) |
| parity read without the complement | parity changed | caught (1 FAIL) |
| zone boundary replaced by a small wavenumber | check E changed | caught (1 FAIL) |

  7 of 7 are caught.
- **Vacuity guard:** every shift, rate and ratio is printed.
- **Budget:** 5 checks, stdout 1279 characters (ceiling 6000), about 290 s
  (ceiling 900 s), peak about 1.1 GB. The census ran one mutant at a time
  to keep memory within this machine.

## Verification

```bash
python3 scripts/uniform_ice_flux_sector_photon_rise_is_wavenumber_independent_and_a_second_branch_crosses_below_2026_09_23.py
```

Expected summary line: `TOTAL: PASS=5 FAIL=0`; the runner exits nonzero
if any check fails. Cached output:
`logs/runner-cache/uniform_ice_flux_sector_photon_rise_is_wavenumber_independent_and_a_second_branch_crosses_below_2026_09_23.txt`.
