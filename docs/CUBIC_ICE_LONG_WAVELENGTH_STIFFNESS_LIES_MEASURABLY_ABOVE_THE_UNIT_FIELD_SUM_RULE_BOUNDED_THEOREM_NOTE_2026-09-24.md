---
claim_id: cubic_ice_long_wavelength_stiffness_lies_measurably_above_the_unit_field_sum_rule_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "An exact weighted identity for the unit-arrow covariance of uniform ice on cubic tori, and finite binned diagnostics on the L = 16 torus: the smallest wavevectors imply a Gaussian stiffness 0.29% above the continuous zero-mode calibration (K_cont = (2N+1)/(3N)) at 6.0 binned standard errors, the discrete winding fit also lies above it, and the covariance ratio rises across nine momentum shells. No thermodynamic limit, mixing bound or physical law is asserted."
upstream_dependencies:
  - minimal_axioms
  - uniform_ice_on_cubic_tori_winding_stiffness_and_correlations_carry_the_sum_rule_stiffness_bounded_theorem_note_2026-09-23
  - ice_unit_field_sum_rule_is_ten_times_closer_in_three_dimensions_than_in_square_ice_bounded_theorem_note_2026-09-23
  - square_ice_is_gaussian_at_long_wavelength_and_a_zone_boundary_excess_makes_the_sum_rule_miss_bounded_theorem_note_2026-09-24
runner: scripts/cubic_ice_long_wavelength_stiffness_lies_measurably_above_the_unit_field_sum_rule_2026_09_24.py
---

# Cubic ice on the L = 16 torus: the smallest wavevectors sit above the continuous sum-rule calibration

**Date:** 2026-09-24
**Type:** bounded_theorem

Uniform ice and every Gaussian comparison below are supplied mathematical
models, as in landed PR 8881. They are not derived from the repository
axioms or adopted as a physical law. Every number is a finite diagnostic
of the stated sampling.

## Objects

- **Uniform ice** on the even L × L × L torus, N = L³: each positive-axis
  link carries E_i = ±1 and every vertex has zero divergence. The loop
  sampler and the exact L = 2 counts are those of landed PR 8881.
- **Covariance.** S_zz(q) = (1/N)|E_z(q)|², averaged within each batch.
  With s_i² = 2 − 2 cos q_i and Q = s_x² + s_y² + s_z², the transverse
  projector is P_zz = 1 − s_z²/Q.
- **Continuous calibration.** K_cont = (2N + 1)/(3N) is the stiffness at
  which a Gaussian with a continuous zero mode has unit variance (landed
  PR 8881). At L = 16, K_cont/2 = 0.333374.
- **Batch ratio.** Over a set of nonzero wavevectors, r = K_cont Σ S_zz /
  Σ P_zz, formed within each of 40 batches. It carries the exact pairing
  S(q) = S(−q) and every correlation between wavevectors. A Gaussian of
  stiffness K gives r = K_cont/K, so c = K_cont/(2r) is the stiffness
  that set implies.
- **Discrete winding fit.** c_W = K_W/2, where K_W reproduces the sampled
  ⟨W²⟩ under weights exp(−K W²/(2L)) on the even winding grid. Landed PR
  8881 shows why this fit need not equal the continuous calibration.

## Exact identity

Because E_z² = 1 on every link, Σ_q S_zz(q) = N in every configuration.
Write r(q) = K_cont S_zz(q)/P_zz(q) for q ≠ 0 and r_0 = K_cont S_zz(0) =
K_cont ⟨W_z²⟩/L. Where P_zz = 0 the wavevector lies along z, zero
divergence forces E_z(q) = 0, and the term P_zz r = K_cont S_zz vanishes.
The identity becomes

  Σ_{q≠0} P_zz(q) r(q) + r_0 = N K_cont = Σ_{q≠0} P_zz(q) + 1.

So the P_zz-weighted mean of r, with the zero mode at weight 1, equals 1.
Measured against any reference value r_ref, the weighted mean of r/r_ref
is exactly 1/r_ref. With r_ref the smallest-wavevector value, the offset
of the implied stiffness above K_cont/2 equals the zone's weighted mean
excess over that value. This is the cubic counterpart of the weighted
identity of landed PR 8954.

## Finite diagnostics on L = 16

The runner uses 10⁶ loops in 40 batches of 25000, with a fixed seed.
Standard errors are binned and descriptive: no mixing bound,
simultaneous coverage or thermodynamic extrapolation is asserted.

1. **Identity check.** In all 40 batches the covariance sums to N within
   9.1e-13.

2. **Smallest wavevectors.** Take the 24 wavevectors with folded |k|² at
   most 3 units of 2π/16 and P_zz > 0.05. They give r = 0.99711 ±
   0.00048, so c = 0.33434 ± 0.00016. That is 0.29% above K_cont/2, or
   6.0 binned standard errors, and 0.30% above 1/3. A second seed, run in
   the census, gives 0.33447 ± 0.00018: 0.33% above, 6.2 standard errors.

3. **Discrete winding fit.** c_W = 0.33513 ± 0.00056, 0.53% above
   K_cont/2. Batch by batch, c_W − c = +0.00082 ± 0.00054; the second seed
   gives c_W = 0.33553 ± 0.00039 and +0.00107 ± 0.00043. The two
   diagnostics need not coincide (landed PR 8881). The difference is
   retained as a finite discrepancy, not fitted away.

4. **Momentum shells.** In nine shells of Q, the ratio rises:

   | Q shell | r |
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
   outward the rise is well beyond the errors. The inner half of the zone
   (0 < Q < 6) gives 0.99825 ± 0.00005 and the outer half 1.00163 ±
   0.00005. By the identity, the 0.29% offset is the weighted mean of
   this rise measured from the smallest wavevectors.

For comparison, landed PR 8930 records planar strips 4.1% to 4.7% above
their calibration. Here the offset is 0.29%.

## Machine status and trace

- **Runner:**
  `scripts/cubic_ice_long_wavelength_stiffness_lies_measurably_above_the_unit_field_sum_rule_2026_09_24.py`
- **Result:** `TOTAL: PASS=6 FAIL=0`, about 180 to 230 s, stdout 1617
  characters, peak about 385 MB.
- **Cache:**
  `logs/runner-cache/cubic_ice_long_wavelength_stiffness_lies_measurably_above_the_unit_field_sum_rule_2026_09_24.txt`
- **Arithmetic:** exact integer enumeration of the L = 2 torus (all 2^24
  arrow patterns); the L = 16 covariance by fast Fourier transform after
  every loop; the winding fit by bisection on the discrete Gaussian.

## Theorem — Weighted identity and L = 16 diagnostics

The weighted identity holds exactly for every divergence-free unit-arrow configuration
on every even torus. On the L = 16 torus with the stated sampling, the
binned diagnostics are as stated. No limit beyond L = 16 is claimed.

## No-Go Discipline Gate

- **N1 — Domain:** the identity on even tori; the diagnostics on L = 16
  with the stated seeds.
- **N2 — Independence:** the identity is checked batch by batch. The
  smallest wavevectors and the winding fit are separate diagnostics of
  the same samples. A second seed is run in the census.
- **N3 — Imports:** uniform ice, the Gaussian comparison and the sampler
  are supplied models and tools; no new axiom or primitive.
- **N4 — Dependencies:** landed PRs 8881, 8930 and 8954 supply
  definitions and comparisons within their landed scope.
- **N5 — Resolution:** binned errors are descriptive estimates; no mixing
  bound or thermodynamic extrapolation.
- **N6 — Remaining work:** larger tori; whether the smallest-wavevector
  and winding diagnostics meet.
- **N7 — Strongest objection:** a finite offset on one torus size does
  not establish a limiting stiffness.
- **N8 — Review boundary:** no audit verdict, retained grade or assembly
  decision is applied.

## Falsifiers

- A counterexample to the weighted identity for a unit-arrow
  configuration.
- A fresh run of the runner that fails a check. It would challenge the
  stated reproduction, not alone a different infinite-volume theory.

## Imports

- [minimal_axioms](MINIMAL_AXIOMS_2026-06-29.md): repository boundary;
  does not derive the supplied ice model.
- Landed PRs 8881, 8930 and 8954 are cited for definitions and
  comparisons. Finite counting, the discrete Fourier transform and
  Gaussian integrals are mathematical tools, not physical premises.

## Review record

- **Seat:** one Opus 5.5 seat; no subagents; runner and note by the same
  seat. No separate reviewer or audit is claimed.
- **Corrections before landing:**
  - A first version weighted each wavevector by its own inverse variance.
    That counts each pair q, −q twice, so its errors were about 1.4 times
    too small. Every estimate is now a batch ratio, as in the landed
    version of PR 8881.
  - Check B first asked for c above 1/3 by 5 standard errors. The
    whole-zone mutant showed that this passes for the calibration itself,
    since K_cont/2 lies 1/(6N) above 1/3 and a large set has a tiny error.
    B now compares with K_cont/2 and asks for 0.1% to 0.5% above it.
  - Check C first asked the winding fit to agree with the smallest
    wavevectors within 2 standard errors of their batch difference. The
    second seed failed it, so that agreement is not claimed. C now asks the
    winding fit to lie above K_cont/2 by more than 2 standard errors and
    within 1%. The census showed that a one-sided form misses a winding
    Gaussian of twice the width; the bracket catches it.
- **Mutation census** (caught means at least one FAIL line or a nonzero
  exit; the runner exits nonzero on any FAIL):

| Mutant | Change | Result |
|---|---|---|
| projector of E_x in place of E_z | projector changed | caught (1 FAIL) |
| spectrum of E_x against the E_z projector | component changed | caught (1 FAIL) |
| whole zone in place of the smallest wavevectors | set changed | caught (1 FAIL) |
| winding Gaussian of twice the width | Gaussian changed | caught (1 FAIL) |
| zone profile read in reverse | direction reversed | caught (1 FAIL) |
| worm biased toward its first candidate | sampler made non-uniform | caught (2 FAILs) |
| spectrum normalized by N − 1 | normalisation changed | caught (1 FAIL) |
| zone mean in place of zone sum | ratio changed | caught (2 FAILs) |

  8 of 8 are caught. The biased sampler passes the L = 2 control at its
  tolerance and is caught on L = 16. A second seed (control) passes all
  six checks.

- **Budget:** 6 checks, stdout 1617 characters (ceiling 6000), about
  180 to 230 s (ceiling 900 s), peak about 385 MB.

## Verification

```bash
python3 scripts/cubic_ice_long_wavelength_stiffness_lies_measurably_above_the_unit_field_sum_rule_2026_09_24.py
```

Expected summary line: `TOTAL: PASS=6 FAIL=0`; the runner exits nonzero
if any check fails. Cached output:
`logs/runner-cache/cubic_ice_long_wavelength_stiffness_lies_measurably_above_the_unit_field_sum_rule_2026_09_24.txt`.

## Canonical source dependencies

- [uniform_ice_on_cubic_tori_winding_stiffness_and_correlations_carry_the_sum_rule_stiffness_bounded_theorem_note_2026-09-23](UNIFORM_ICE_ON_CUBIC_TORI_WINDING_STIFFNESS_AND_CORRELATIONS_CARRY_THE_SUM_RULE_STIFFNESS_BOUNDED_THEOREM_NOTE_2026-09-23.md): conditional supplied source with its landed qualifications.
- [ice_unit_field_sum_rule_is_ten_times_closer_in_three_dimensions_than_in_square_ice_bounded_theorem_note_2026-09-23](ICE_UNIT_FIELD_SUM_RULE_IS_TEN_TIMES_CLOSER_IN_THREE_DIMENSIONS_THAN_IN_SQUARE_ICE_BOUNDED_THEOREM_NOTE_2026-09-23.md): conditional supplied source with its landed qualifications.
- [square_ice_is_gaussian_at_long_wavelength_and_a_zone_boundary_excess_makes_the_sum_rule_miss_bounded_theorem_note_2026-09-24](SQUARE_ICE_IS_GAUSSIAN_AT_LONG_WAVELENGTH_AND_A_ZONE_BOUNDARY_EXCESS_MAKES_THE_SUM_RULE_MISS_BOUNDED_THEOREM_NOTE_2026-09-24.md): conditional supplied source with its landed qualifications.
