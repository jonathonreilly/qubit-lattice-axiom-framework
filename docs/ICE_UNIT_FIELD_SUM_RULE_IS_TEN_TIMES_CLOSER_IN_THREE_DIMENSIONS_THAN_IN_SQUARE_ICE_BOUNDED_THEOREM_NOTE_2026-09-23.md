---
claim_id: ice_unit_field_sum_rule_is_ten_times_closer_in_three_dimensions_than_in_square_ice_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "For ice with unit link field E = +-1, a Gaussian divergence-free field whose stiffness is fixed by the sum rule <E^2> = 1 predicts the flux cost c = K/2. For square ice (two of four links occupied at every vertex of the plane) on strips of width a, periodic across and infinite along, the sum rule gives K_a = (1/a) sum_q sqrt(Q/(Q+4)), Q = 2 - 2 cos q; the one-dimensional zone average of sqrt(Q/(Q+4)) is 1/2 (within 1e-9 numerically), so K = 1/2 and c = 1/4 on wide strips. A site-by-site square-ice transfer reproduces the torus counts of an independent dense row transfer (2970, 98466, 98466 and 16448400 on 4 x 4, 4 x 6, 6 x 4 and 6 x 6). Its measured flux cost c(2) = (a/4) ln(lam_0/lam_2) rises from 0.24252 at a = 4 to 0.26090 at a = 20 and exceeds K_a/2 by 4.1% to 4.7% at every width, the excess growing from a = 6 on (+4.63% at a = 20). For three-dimensional uniform ice, by the row transfer of the landed note of PR 8859, the flux cost lies within 0.5% of its sum-rule value on the prisms 2 x 8 (-0.40%) and 4 x 4 (-0.02%), at least ten times closer than square ice at every width; on cubic tori to side 24 the long-wavelength value lies 0.5% above (open PR 8881). No limit beyond the computed widths is claimed. No constant is compared with an outside value. No reading, rule, alphabet, unit or order law is adopted."

upstream_dependencies:
  - minimal_axioms
runner: scripts/ice_unit_field_sum_rule_is_ten_times_closer_in_three_dimensions_than_in_square_ice_2026_09_23.py
---

# The unit-field sum rule is ten times closer for three-dimensional ice than for square ice

**Date:** 2026-09-23
**Type:** bounded_theorem
**Campaign:** second next-steps campaign. Open PRs 8871 and 8881 found
that for three-dimensional uniform ice the flux cost is fixed, to half a
percent, by the sum rule of a Gaussian divergence-free field whose unit
link field has ⟨E²⟩ = 1. Open PR 8928 found that each fully polarized
layer of three-dimensional ice is square ice. This block applies the same
sum rule to square ice, to see whether its accuracy is a property of the
rule or of three dimensions.

## Result up front

1. **The sum rule in the plane.** On a strip of width a, periodic across
   and infinite along, a Gaussian divergence-free field with stiffness K
   costs K S²/(2a) per row for a flux S, so c = K/2. Its equal-row
   correlation is √(Q/(Q + 4))/K with Q = 2 − 2 cos q, and the unit link
   field fixes K_a = (1/a) Σ_q √(Q/(Q + 4)). In the plane the transverse
   projector has trace 1, shared by two directions, so the zone average of
   √(Q/(Q + 4)) is 1/2: K = 1/2 and c = 1/4 on wide strips.

2. **The square-ice transfer.** Applied site by site along a row, it
   reproduces the torus counts of an independent dense row transfer: 2970,
   98466, 98466 and 16448400 on 4 × 4, 4 × 6, 6 × 4 and 6 × 6.

3. **Square ice misses the sum rule by 4% to 5%.** The flux cost
   c(2) = (a/4) ln(λ_0/λ_2), against the sum-rule value K_a/2:

   | width | c(2) | excess over K_a/2 |
   |---|---|---|
   | 4 | 0.24252 | +4.21% |
   | 6 | 0.25255 | +4.11% |
   | 8 | 0.25641 | +4.29% |
   | 12 | 0.25933 | +4.50% |
   | 16 | 0.26040 | +4.59% |
   | 20 | 0.26090 | +4.63% |

   The cost rises with width, and the excess grows from a = 6 on.

4. **Three-dimensional ice sits ten times closer.** On the prisms 2 × 8 and
   4 × 4 the flux cost lies within 0.5% of its sum-rule value (−0.40% and
   −0.02%). That is at least ten times closer than square ice at every
   width. On cubic tori to side 24, the long-wavelength value lies 0.5%
   above the sum rule (open PR 8881).

5. **What this means.** The unit-field sum rule is a property of the rule,
   but its accuracy depends on dimension. In three dimensions the static
   photon of uniform ice is Gaussian to half a percent, down to the lattice
   scale. In the plane, square ice is not: its flux cost exceeds the
   Gaussian value by about 4.6%, and the excess is still growing at width
   20. The near-Gaussian photon of open PRs 8869, 8871, 8881 and 8890 is
   therefore a three-dimensional result. The same rule in the plane leaves
   a correction ten times larger. No constant is compared with an outside
   value.

## Machine status and trace

- **Runner:**
  `scripts/ice_unit_field_sum_rule_is_ten_times_closer_in_three_dimensions_than_in_square_ice_2026_09_23.py`
- **Result:** `TOTAL: PASS=4 FAIL=0`, about 38 s, stdout 965 characters,
  peak about 700 MB.
- **Cache:**
  `logs/runner-cache/ice_unit_field_sum_rule_is_ten_times_closer_in_three_dimensions_than_in_square_ice_2026_09_23.txt`
- **Arithmetic:** exact integer transfers; the square-ice counts exact by
  matrix powers; sector tops by dense diagonalisation up to 256 states and
  by Lanczos iteration (tolerance 1e-12) above.

## Premises and declared objects

- **Square ice:** two of four links occupied at every vertex of the plane;
  with the staggered sign, a divergence-free unit field.
- **Three-dimensional uniform ice** and its row transfer: the landed note
  of PR 8859.
- **Sum rule:** as in open PR 8871, now in the plane as well.

## Prior art and what is new

- Open PRs 8871 and 8881: the sum rule in three dimensions.
- Open PR 8928: saturated layers are square ice.
- New here: the sum rule for square ice, its 4.1% to 4.7% miss on strips
  to width 20, and the tenfold contrast with three dimensions.

## Theorem — Square ice against the sum rule

On strips of width 4 to 20 the square-ice flux costs and their excess over
the sum-rule value are as stated; on the prisms 2 × 8 and 4 × 4 the
three-dimensional costs are as stated. No limit is claimed beyond the
computed widths.

## No-Go Discipline Gate

- **N1 alternative routes.** Wider strips; the correlations of square ice
  against the planar projector.
- **N2 wall independence.** The site transfer is checked against an
  independent dense count, and the three-dimensional costs reproduce the
  landed note of PR 8859.
- **N3 hidden walls.** Floating-point eigenvalues with stated tolerance.
- **N4 residual matching.** Nothing is fitted; the excess is reported.
- **N5 rhetoric audit.** "Ten times closer" means the computed ratio of
  deviations, at least 10.3 on these cross-sections.
- **N6 partial-closure paths.** The planar limit of the excess.
- **N7 steelman.** Against: strips of width 2 in three dimensions are not
  squares. For: the square 4 × 4 is closer still, and the tori agree at
  0.5%. Both are recorded.
- **N8 cross-cycle echo.** Open PRs 8871, 8881 and 8928 and the landed note
  of PR 8859 are cited.

## Falsifiers

- A square-ice strip whose flux cost lies within 1% of K_a/2.
- A three-dimensional prism whose cost departs from its sum-rule value by
  more than 0.5%.

## Boundaries and non-claims

- Square-ice strips of width 4 to 20; three-dimensional prisms 2 × 8 and
  4 × 4.
- No planar limit is claimed.
- No reading, rule, alphabet, unit or order law is adopted.
- Nothing here grades, unlocks or audits any other claim.

## Imports

The minimal axioms, the landed note of PR 8859 and open PRs 8871, 8881 and
8928 are cited. No audit grade, no new axiom, no new primitive, no new
comparator and no new framing is imported.

## Review record

- **Seat:** one Opus 5.5 seat; no subagents; runner and note by the same
  seat.
- **Independence sources:** the dense square-ice count; the landed
  three-dimensional costs.
- **Correction before landing.** A first threshold required an excess of
  at least 4.2%; the strip of width 6 sits at 4.11%, and the check now
  states 4.1% to 4.7%.
- **Mutation census** (caught means at least one FAIL line or a nonzero
  exit; the runner exits nonzero on any FAIL):

| Mutant | Change | Result |
|---|---|---|
| square ice with one of four links occupied | rule changed | caught (2 FAILs) |
| planar flux without the staggered sign | sectors changed | caught (2 FAILs) |
| planar kernel with Q + 2 | zone average changed | caught (1 FAIL) |
| planar cost with a/2 | cost changed | caught (1 FAIL) |
| site transfer without the periodic carry | wrap dropped | caught (1 FAIL) |
| three-dimensional sum rule over one axis | kernel changed | caught (1 FAIL) |
| two occupied links per vertex in three dimensions | rule changed | caught (1 FAIL) |

  7 of 7 are caught.

- **Vacuity guard:** every count, cost and excess is printed.
- **Budget:** 4 checks, stdout 965 characters (ceiling 6000), about 38 s
  (ceiling 900 s), peak about 700 MB.

## Verification

```bash
python3 scripts/ice_unit_field_sum_rule_is_ten_times_closer_in_three_dimensions_than_in_square_ice_2026_09_23.py
```

Expected summary line: `TOTAL: PASS=4 FAIL=0`; the runner exits nonzero
if any check fails. Cached output:
`logs/runner-cache/ice_unit_field_sum_rule_is_ten_times_closer_in_three_dimensions_than_in_square_ice_2026_09_23.txt`.
