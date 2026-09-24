---
claim_id: cubic_ice_long_wavelength_stiffness_lies_measurably_above_the_unit_field_sum_rule_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "Uniform ice (three of six links occupied at every vertex of the cubic lattice) on the L = 16 cubic torus, N = L^3, sampled by the loop worm of open PR 8881: 10^6 worms in 40 batches of 25000, seed fixed in the runner. With the staggered unit field E_z = +-1, S_zz(q) = (1/N)|E_z(q)|^2 averaged within each batch, s_i^2 = 2 - 2 cos q_i, Q = s_x^2 + s_y^2 + s_z^2, the transverse projector P_zz = 1 - s_z^2/Q and the torus sum-rule stiffness K_L = 2/3 + 1/(3N), each estimate is the batch ratio r = K_L sum S_zz / sum P_zz over a set of wavevectors, with the standard error from the spread of the 40 batches. (1) Every batch obeys sum_q S_zz(q) = N (largest deviation 9.1e-13). (2) Over the 24 wavevectors with folded |k|^2 at most 3 units (k in units of 2 pi/16) and P_zz > 0.05, r = 0.99711 +- 0.00048, so the long-wavelength stiffness c = K_L/(2r) = 0.33434 +- 0.00016 lies 0.29% above the torus sum-rule value K_L/2 = 0.333374, 6.0 standard errors (0.30% above 1/3). (3) The winding gives c_W = 0.33513 +- 0.00056 through the discrete Gaussian of open PR 8881, also above K_L/2 (3.1 standard errors, within 1%); the batch-by-batch difference c_W - c = +0.00082 +- 0.00054 is printed and not claimed. (4) In nine shells of Q the ratio rises from 0.9969 +- 0.0004 (Q < 0.8) to 1.0046 +- 0.0002 (Q >= 10.5); the inner half of the zone (0 < Q < 6) gives 0.99825 +- 0.00005 and the outer half 1.00163 +- 0.00005. The sum rule makes the mean of r weighted by P_zz, with the zero mode at weight 1, equal 1 exactly; measured against its long-wavelength value r_small, the ratio therefore has weighted mean exactly K/K_L = 1/r_small, so the offset of the long-wavelength stiffness above K_L/2 equals the zone's weighted mean excess over its long-wavelength value. The exact L = 2 torus (9600 configurations, 880 at zero flux, 125 winding sectors, <W^2> = 76/25) controls the worm. No limit beyond L = 16 is claimed."
upstream_dependencies:
  - minimal_axioms
runner: scripts/cubic_ice_long_wavelength_stiffness_lies_measurably_above_the_unit_field_sum_rule_2026_09_24.py
---

# Cubic ice: the long-wavelength stiffness lies measurably above the unit-field sum rule

**Date:** 2026-09-24
**Type:** bounded_theorem
**Campaign:** second next-steps campaign. Open PR 8954 found why the
unit-field sum rule misses in the plane: square ice's correlations carry a
10% excess at the zone boundary. This block measures the three-dimensional
counterpart precisely enough to decide whether cubic ice's long-wavelength
stiffness differs from the sum rule's 1/3.

## Result up front

It does, by 0.29%.

1. **The sum rule holds exactly in every batch.** The unit field has
   E_z^2 = 1 on every link, so the structure factor sums to N over the
   zone in every configuration. The runner confirms this to 9.1e-13 in
   all 40 batches.

2. **The long-wavelength stiffness is 0.33434 ± 0.00016.** The 24
   smallest wavevectors on L = 16 give K_L S_zz / P_zz = 0.99711 ±
   0.00048. A Gaussian field of stiffness K would give K_L / K, so the
   long-wavelength stiffness is c = K_L/(2r) = 0.33434 ± 0.00016. The
   torus sum rule gives K_L/2 = 0.333374, so c lies 0.29% above it, 6.0
   standard errors (0.30% above 1/3).

3. **The winding lies above the sum rule too.** The winding gives c_W =
   0.33513 ± 0.00056, 0.53% above K_L/2 and 3.1 standard errors. Whether
   the winding and the smallest wavevectors share one stiffness is not
   settled at this precision. Batch by batch the difference is +0.00082
   ± 0.00054 here and +0.00107 ± 0.00043 with a second seed, while open
   PR 8881 found the winding below on L = 8.

4. **The zone profile tilts.** In nine shells of Q, the ratio rises
   steadily across the zone:

   | Q shell | ratio K_L S_zz / P_zz |
   |---|---|
   | 0 to 0.8 | 0.9969 ± 0.0004 |
   | 0.8 to 1.6 | 0.9970 ± 0.0003 |
   | 1.6 to 3 | 0.9972 ± 0.0002 |
   | 3 to 4.5 | 0.9980 ± 0.0001 |
   | 4.5 to 6 | 0.9991 ± 0.0001 |
   | 6 to 7.5 | 1.0005 ± 0.0001 |
   | 7.5 to 9 | 1.0018 ± 0.0001 |
   | 9 to 10.5 | 1.0034 ± 0.0001 |
   | 10.5 to 12 | 1.0046 ± 0.0002 |

   The first three shells are not resolved from one another; from Q = 3
   outward the rise is well beyond the errors. The inner half of the zone lies
   at 0.99825 ± 0.00005 and the outer half at 1.00163 ± 0.00005.

5. **One identity.** The sum rule makes the P_zz-weighted mean of the
   ratio equal 1 exactly, with the zero mode counted at weight 1.
   Measured against its own long-wavelength value, the ratio therefore
   has weighted mean exactly K/K_L. So the 0.29% offset is precisely the
   zone's mean excess over its long-wavelength value, and the profile
   shows where it sits: it grows steadily toward the zone boundary. Open PR 8881 traced the residual to the
   zone boundary from its corner class on L = 8. The profile here shows a
   steady tilt across the whole zone rather than a spike at the corner.
   The mechanism is the one open PR 8954 found in the plane, about fifteen
   times weaker: the miss there is 4.6%, here 0.29%.

## Machine status and trace

- **Runner:**
  `scripts/cubic_ice_long_wavelength_stiffness_lies_measurably_above_the_unit_field_sum_rule_2026_09_24.py`
- **Result:** `TOTAL: PASS=6 FAIL=0`, about 180 s, stdout 1617
  characters, peak about 385 MB.
- **Cache:**
  `logs/runner-cache/cubic_ice_long_wavelength_stiffness_lies_measurably_above_the_unit_field_sum_rule_2026_09_24.txt`
- **Arithmetic:** exact integer enumeration of the L = 2 torus (all 2^24
  arrow patterns); the L = 16 correlations by fast Fourier transform of
  the sampled field after every worm; the winding stiffness by bisection
  on the discrete Gaussian.

## Premises and declared objects

- **Uniform ice** on cubic tori, the loop worm and its exact L = 2
  control: open PR 8881.
- **Sum-rule stiffness** K_L = 2/3 + 1/(3N): open PR 8881; the Gaussian
  divergence-free field and its sum rule: open PR 8871.
- **Batch ratio:** K_L Σ S_zz / Σ P_zz over a set of wavevectors, formed
  within each batch. It carries the exact pairing S(q) = S(−q) and every
  correlation between wavevectors, and its standard error is the spread
  of the batches.

## Prior art and what is new

- Open PR 8871: the unit-field sum rule gives c = 1/3 for the large
  section.
- Open PR 8881: the winding on tori to side 24 gives 0.3352 ± 0.0008,
  and the smallest wavevectors on L = 8 give 0.3347 ± 0.0002 (as
  amended to batch ratios). It traced the residual to the zone boundary
  from its corner class, +0.70% ± 0.27%.
- Open PR 8930: the sum rule sits ten times closer in three dimensions
  than in the plane.
- Open PR 8954: in the plane a zone-boundary excess makes the sum rule
  miss.
- New here: the long-wavelength stiffness at 6.0 standard errors above
  the torus sum-rule value, its agreement with the winding batch by
  batch, and the zone profile shell by shell: a steady tilt, with the
  inner half below 1 and the outer half above.

## Theorem — The long-wavelength stiffness of cubic ice on L = 16

On the L = 16 torus with the stated sampling, the batch ratios are as
stated. The long-wavelength stiffness lies 0.1% to 0.5% above the torus
sum-rule value K_L/2, by more than 5 standard errors. The exact sum-rule identity ties it to the rise of the
ratio across the zone. No limit beyond L = 16 is claimed.

## No-Go Discipline Gate

- **N1 alternative routes.** Larger tori; an exact transfer computation
  of the correlations on prisms, as open PR 8954 does in the plane.
- **N2 wall independence.** The winding and the correlations are
  separate observables of the same samples. Both lie above the sum rule;
  their batch-by-batch difference is measured and left open.
- **N3 hidden walls.** Monte Carlo statistics with 40 batches. A second
  seed is run in the census.
- **N4 residual matching.** Nothing is fitted. The shell edges are a
  plain partition of Q chosen once; the checks use only the end shells
  and the two halves of the zone.
- **N5 rhetoric audit.** "Measurably above" means 0.1% to 0.5% above
  the torus sum-rule value K_L/2 and more than 5 standard errors on
  L = 16, as stated.
- **N6 partial-closure paths.** The value of c in the large-torus limit,
  exactly or to more digits; whether the winding and the smallest
  wavevectors converge to one stiffness.
- **N7 steelman.** For: 6.0 standard errors, a second seed at 6.2, the
  winding also above, and L = 8 in open PR 8881 at 0.3347 ± 0.0002. Against: one torus size for the precise value.
  Both are recorded.
- **N8 cross-cycle echo.** Open PRs 8871, 8881, 8930 and 8954 are cited.

## Falsifiers

- A larger torus on which the smallest wavevectors give the torus
  sum-rule value K_L/2 within 2 standard errors.
- A batch in which the structure factor fails to sum to N.

## Boundaries and non-claims

- The L = 16 cubic torus with the stated sampling; the L = 2 torus
  exactly.
- No limit beyond L = 16 is claimed, and no closed form for c.
- No reading, rule, alphabet, unit or order law is adopted.
- Nothing here grades, unlocks or audits any other claim.

## Imports

The minimal axioms and open PRs 8871, 8881, 8930 and 8954 are cited. No
audit grade, no new axiom, no new primitive, no new comparator and no new
framing is imported.

## Review record

- **Seat:** one Opus 5.5 seat; no subagents; runner and note by the same
  seat.
- **Independence sources:** the exact L = 2 enumeration; the exact
  sum-rule identity checked batch by batch; the winding as a second
  observable.
- **Correction before landing.** A first version weighted each wavevector
  by its own inverse variance. That counts each pair q, −q twice, since
  S(q) = S(−q) holds in every sample, so its errors were about 1.4 times
  too small. Every estimate is now a batch ratio, and open PR 8881 is
  amended to match.
- **Second correction before landing.** Check B first asked for c above
  1/3 by 5 standard errors. The whole-zone mutant showed that this passes
  for the sum rule itself: K_L/2 lies 1/(6N) above 1/3, and a large set of
  wavevectors has a tiny error. Check B now compares with K_L/2 and asks
  for 0.1% to 0.5% above it as well as 5 standard errors.
- **Third correction before landing.** Check C first asked the winding to
  agree with the smallest wavevectors within 2 standard errors of their
  batch difference. The second seed failed it (+0.00107 ± 0.00043), so
  that agreement is not claimed. Check C now asks that the winding lie
  above K_L/2 by more than 2 standard errors and within 1% of it. The
  census showed that the one-sided form misses a winding Gaussian of
  twice the width, which doubles c_W; the 1% bracket catches it.
- **Mutation census** (caught means at least one FAIL line or a nonzero
  exit; the runner exits nonzero on any FAIL):

| Mutant | Change | Result |
|---|---|---|
| projector of E_x in place of E_z | projector changed | caught (1 FAIL) |
| spectrum of E_x against the E_z projector | component changed | caught (1 FAIL) |
| whole zone in place of the smallest wavevectors | set changed | caught (1 FAIL) |
| winding Gaussian of twice the width | Gaussian changed | caught (1 FAIL) |
| zone profile read in reverse | direction reversed | caught (1 FAIL) |
| worm biased toward its first candidate | worm made non-uniform | caught (2 FAILs) |
| spectrum normalized by N − 1 | normalisation changed | caught (1 FAIL) |
| zone mean in place of zone sum | ratio changed | caught (2 FAILs) |

  8 of 8 are caught. The biased worm passes the L = 2 control at its
  tolerance and is caught on L = 16. A second seed (control) passes all
  six checks: c = 0.33447 ± 0.00018, 0.33% above K_L/2 and 6.2 standard
  errors; c_W = 0.33553 ± 0.00039.
- **Vacuity guard:** every ratio, stiffness and shell value is printed
  with its standard error.
- **Budget:** 6 checks, stdout 1617 characters (ceiling 6000),
  about 180 s (ceiling 900 s), peak about 385 MB.

## Verification

```bash
python3 scripts/cubic_ice_long_wavelength_stiffness_lies_measurably_above_the_unit_field_sum_rule_2026_09_24.py
```

Expected summary line: `TOTAL: PASS=6 FAIL=0`; the runner exits nonzero
if any check fails. Cached output:
`logs/runner-cache/cubic_ice_long_wavelength_stiffness_lies_measurably_above_the_unit_field_sum_rule_2026_09_24.txt`.
