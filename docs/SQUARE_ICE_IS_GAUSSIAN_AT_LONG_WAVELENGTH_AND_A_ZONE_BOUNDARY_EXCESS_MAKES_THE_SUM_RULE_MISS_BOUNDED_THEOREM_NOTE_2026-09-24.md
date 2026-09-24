---
claim_id: square_ice_is_gaussian_at_long_wavelength_and_a_zone_boundary_excess_makes_the_sum_rule_miss_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "For square ice (two of four links occupied at every vertex of the plane) on strips of width a, with the row law psi^2 of the zero-flux top vector, the equal-row correlation of the staggered field S(q) = (1/a) <|E_q|^2> is compared with the Gaussian g(q)/K, g = sqrt(Q/(Q+4)), Q = 2 - 2 cos q, at K = 2 c(2) from the measured flux cost: R(q) = K S(q)/g(q). The site-by-site transfer reproduces the 4 x 4 torus count 2970 and the flux costs of open PR 8930. At the smallest wavenumber 2 pi/a, R = 0.9901, 0.9949, 0.9970 and 0.9981 for a = 8, 12, 16 and 20, rising toward 1: at long wavelength the flux cost and the correlations share one stiffness. R rises monotonically to the zone boundary, where R(pi) = 1.1067, 1.0999, 1.0971 and 1.0957. Because E^2 = 1 exactly, sum_q S(q) = a, so K / K_a is the g-weighted mean of R; it equals 1.04290, 1.04497, 1.04588 and 1.04633 on the four widths (identity within 1e-9). The sum rule's miss in the plane is therefore the zone-boundary excess of square ice's correlations. No limit beyond the computed widths is claimed. No constant is compared with an outside value. No reading, rule, alphabet, unit or order law is adopted."

upstream_dependencies:
  - minimal_axioms
runner: scripts/square_ice_is_gaussian_at_long_wavelength_and_a_zone_boundary_excess_makes_the_sum_rule_miss_2026_09_24.py
---

# Square ice is Gaussian at long wavelength; a zone-boundary excess makes the unit-field sum rule miss

**Date:** 2026-09-24
**Type:** bounded_theorem
**Campaign:** second next-steps campaign. Open PR 8930 found that square
ice's flux cost exceeds the unit-field sum rule by 4.1% to 4.7%, while
three-dimensional uniform ice sits ten times closer. This block asks which
part of the Gaussian picture fails in the plane.

## Result up front

1. **The measure.** On a strip of width a, the row law is ψ² for the
   zero-flux top vector ψ. The equal-row correlation of the staggered field
   is S(q) = (1/a) ⟨|E_q|²⟩. A Gaussian field with stiffness K has
   S(q) = g(q)/K, with g = √(Q/(Q + 4)) and Q = 2 − 2 cos q. Take K = 2c(2)
   from the measured flux cost and define R(q) = K S(q)/g(q).

2. **Long wavelength is Gaussian, with one stiffness.** At the smallest
   wavenumber 2π/a, R = 0.9901, 0.9949, 0.9970 and 0.9981 for a = 8, 12, 16
   and 20, rising toward 1. The flux cost and the long-wavelength
   correlations share one stiffness, as in three dimensions (open PR 8871).

3. **The zone boundary is not.** R rises monotonically from the smallest
   wavenumber to the zone boundary, where R(π) = 1.1067, 1.0999, 1.0971 and
   1.0957. Square ice carries about 10% more correlation there than the
   Gaussian shape.

4. **That excess is the sum rule's miss.** Because E² = 1 exactly,
   Σ_q S(q) = a, and so K/K_a = Σ_q R(q) g(q)/Σ_q g(q): the flux cost
   exceeds the sum rule by the g-weighted mean of R − 1. On the four widths
   this mean is 1.04290, 1.04497, 1.04588 and 1.04633, equal to K/K_a
   within 1e-9.

5. **What this means.** In both dimensions the long-wavelength field is
   Gaussian with one stiffness shared by the flux cost and the
   correlations. What differs is the lattice-scale shape. Square ice
   carries about a 10% excess of correlation at the zone boundary, against
   about 0.7% at the zone corner for cubic ice (open PR 8881). The unit
   field fixes the total correlation, so the zone-boundary excess must be
   taken from long wavelengths, and the stiffness rises above the sum rule:
   by 4.6% in the plane and by 0.5% in three dimensions. This is the
   mechanism behind open PR 8930's tenfold contrast. No constant is
   compared with an outside value.

## Machine status and trace

- **Runner:**
  `scripts/square_ice_is_gaussian_at_long_wavelength_and_a_zone_boundary_excess_makes_the_sum_rule_miss_2026_09_24.py`
- **Result:** `TOTAL: PASS=4 FAIL=0`, about 30 s, stdout 829 characters,
  peak about 460 MB.
- **Cache:**
  `logs/runner-cache/square_ice_is_gaussian_at_long_wavelength_and_a_zone_boundary_excess_makes_the_sum_rule_miss_2026_09_24.txt`
- **Arithmetic:** exact integer transfers; the top vector by Lanczos
  iteration (tolerance 1e-12); the correlations as exact weighted sums
  over the zero-flux states.

## Premises and declared objects

- **Square ice** and its site-by-site transfer: open PR 8930.
- **Row law:** ψ² for the symmetric transfer, as for layers in open PR
  8871.
- **Gaussian comparison:** the planar sum rule and kernel of open PR 8930.

## Prior art and what is new

- Open PR 8930: the planar sum rule misses by 4.6%.
- Open PRs 8871 and 8881: in three dimensions the flux cost and the
  correlations share one stiffness, with a 0.7% zone-corner excess.
- New here: square ice's correlations against its own stiffness; the
  long-wavelength agreement; the 10% zone-boundary excess; the exact
  identity that turns the excess into the sum rule's miss.

## Theorem — Square ice's correlations on the computed strips

On strips of width 8 to 20, R(q) is as stated, and K/K_a equals the
g-weighted mean of R exactly. No limit is claimed beyond the computed
widths.

## No-Go Discipline Gate

- **N1 alternative routes.** Wider strips; the same identity for cubic
  ice's prisms.
- **N2 wall independence.** The flux costs reproduce open PR 8930; the
  identity is exact.
- **N3 hidden walls.** Floating-point eigenvectors with stated tolerance.
- **N4 residual matching.** Nothing is fitted.
- **N5 rhetoric audit.** "Gaussian at long wavelength" means R at the
  smallest wavenumber approaching 1 as stated.
- **N6 partial-closure paths.** The planar limit of R(π).
- **N7 steelman.** For: R at the smallest wavenumber approaches 1 steadily.
  Against: strips of width up to 20 only. Both are recorded.
- **N8 cross-cycle echo.** Open PRs 8871, 8881 and 8930 are cited.

## Falsifiers

- A width on which R at the smallest wavenumber moves away from 1.
- A width on which the g-weighted mean of R differs from K/K_a.

## Boundaries and non-claims

- Square-ice strips of width 8 to 20.
- No planar limit is claimed.
- No reading, rule, alphabet, unit or order law is adopted.
- Nothing here grades, unlocks or audits any other claim.

## Imports

The minimal axioms and open PRs 8871, 8881 and 8930 are cited. No audit
grade, no new axiom, no new primitive, no new comparator and no new framing
is imported.

## Review record

- **Seat:** one Opus 5.5 seat; no subagents; runner and note by the same
  seat.
- **Independence sources:** the flux costs of open PR 8930; the exact
  normalisation of the unit field.
- **Correction before landing.** A first version stored the transform of
  every row state and peaked at 1.4 GB; it now accumulates one wavenumber
  at a time (about 460 MB).
- **Mutation census** (caught means at least one FAIL line or a nonzero
  exit; the runner exits nonzero on any FAIL):

| Mutant | Change | Result |
|---|---|---|
| square ice with one of four links occupied | rule changed | caught (4 FAILs) |
| field without the staggered sign | field changed | caught (4 FAILs) |
| row law ψ in place of ψ² | law changed | caught (2 FAILs) |
| Gaussian weight without the square root | kernel changed | caught (3 FAILs) |
| stiffness read as c in place of 2c | factor 2 dropped | caught (3 FAILs) |

  5 of 5 are caught.

- **Vacuity guard:** every R value, cost and mean is printed.
- **Budget:** 4 checks, stdout 829 characters (ceiling 6000), about 30 s
  (ceiling 900 s), peak about 460 MB.

## Verification

```bash
python3 scripts/square_ice_is_gaussian_at_long_wavelength_and_a_zone_boundary_excess_makes_the_sum_rule_miss_2026_09_24.py
```

Expected summary line: `TOTAL: PASS=4 FAIL=0`; the runner exits nonzero
if any check fails. Cached output:
`logs/runner-cache/square_ice_is_gaussian_at_long_wavelength_and_a_zone_boundary_excess_makes_the_sum_rule_miss_2026_09_24.txt`.
