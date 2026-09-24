---
claim_id: cubic_ice_long_wavelength_stiffness_stays_above_the_sum_rule_from_l12_to_l24_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "Finite binned diagnostics of uniform ice on the L = 12 and L = 24 cubic tori: the smallest wavevectors imply a Gaussian stiffness 0.44% +- 0.05% and 0.31% +- 0.06% above half the continuous zero-mode calibration K_cont = (2N+1)/(3N), the discrete winding fits lie within 1% of it, and the inner and outer halves of the zone keep the same covariance ratios as on L = 16. No thermodynamic limit, mixing bound or physical law is asserted."
upstream_dependencies:
  - minimal_axioms
  - uniform_ice_on_cubic_tori_winding_stiffness_and_correlations_carry_the_sum_rule_stiffness_bounded_theorem_note_2026-09-23
  - cubic_ice_long_wavelength_stiffness_lies_measurably_above_the_unit_field_sum_rule_bounded_theorem_note_2026-09-24
runner: scripts/cubic_ice_long_wavelength_stiffness_stays_above_the_sum_rule_from_l12_to_l24_2026_09_24.py
---

# Cubic ice on L = 12 and L = 24: the smallest wavevectors stay above the continuous calibration

**Date:** 2026-09-24
**Type:** bounded_theorem

Uniform ice and every Gaussian comparison below are supplied mathematical
models, as in landed PR 8881. They are not derived from the repository
axioms or adopted as a physical law. Every number is a finite diagnostic
of the stated sampling.

## Objects

The torus, the loop sampler, the covariance S_zz, the projector P_zz, the
continuous calibration K_cont = (2N+1)/(3N), the batch ratio r = K_cont
Σ S_zz / Σ P_zz over a set of wavevectors, the implied stiffness c =
K_cont/(2r) and the discrete winding fit c_W are those of PR 8968
and landed PR 8881. PR 8968 found the smallest wavevectors on L = 16
0.29% above K_cont/2, at 6.0 binned standard errors. Its first open
question is whether that offset survives on other torus sizes.

## Finite diagnostics on L = 12 and L = 24

The runner uses 10⁶ loops on L = 12 and 5 × 10⁵ on L = 24, each in 40
batches, with fixed seeds. Standard errors are binned and descriptive:
no mixing bound, simultaneous coverage or thermodynamic extrapolation is
asserted.

1. **Identity check.** In every batch on both tori the covariance sums to
   N, within 1.1e-11.

2. **Smallest wavevectors.** The 24 smallest wavevectors (folded |k|² at
   most 3 units of 2π/L, P_zz > 0.05) imply:

   | Torus | c | above K_cont/2 | Source |
   |---|---|---|---|
   | L = 8 | 0.3347 ± 0.0002 | +0.31% ± 0.06% | landed PR 8881 |
   | L = 12 | 0.33490 ± 0.00016 | +0.44% ± 0.05% | this runner |
   | L = 16 | 0.33434 ± 0.00016 | +0.29% ± 0.05% | PR 8968 |
   | L = 16, second seed | 0.33447 ± 0.00018 | +0.33% ± 0.05% | PR 8968 |
   | L = 24 | 0.33437 ± 0.00021 | +0.31% ± 0.06% | this runner |

   On L = 12 and L = 24 the offset is 9.1 and 4.8 binned standard errors.
   The two differ by −0.13% ± 0.08%. L = 12 sits on the high side. The central values are nonmonotone across the sampled sizes;
   these finite diagnostics do not establish a size trend.

3. **Zone halves.** The inner half of the zone (0 < Q < 6) gives r =
   0.99833 ± 0.00007 on L = 12 and 0.99836 ± 0.00005 on L = 24; PR
   8968 gives 0.99825 and 0.99833 ± 0.00005 on its two L = 16 seeds. The
   outer half gives 1.00148 ± 0.00006, 1.00156 ± 0.00004, and 1.00163 and
   1.00156 ± 0.00005. The halves agree across the three sizes within a
   few standard errors. The exact identity of PR 8968 fixes only
   their weighted mean over the whole zone; the smallest-wavevector
   offset is measured separately in item 2.

4. **Discrete winding fits.** c_W = 0.33470 ± 0.00053 on L = 12 and
   0.33554 ± 0.00079 on L = 24, within 1% of K_cont/2. With these seeds
   both lie above it, by 2.4 and 2.8 binned standard errors; with a second pair
   of seeds one of them falls within 2 standard errors, so the side is not
   claimed. With landed PR 8881 (L = 8: 0.3329 ± 0.0013) and open
   PR 8968 (L = 16: 0.33513 ± 0.00056 and 0.33553 ± 0.00039), the fit
   rises with the torus size. Its batch differences to the smallest
   wavevectors are −0.00017 ± 0.00053 on L = 12 and +0.00124 ± 0.00079 on
   L = 24. The two diagnostics need not coincide (landed PR 8881). The
   difference is retained as a finite discrepancy, not fitted away.

## Machine status and trace

- **Runner:**
  `scripts/cubic_ice_long_wavelength_stiffness_stays_above_the_sum_rule_from_l12_to_l24_2026_09_24.py`
- **Result:** `TOTAL: PASS=7 FAIL=0`, about 330 s unloaded and up to 660 s under load, stdout 1667
  characters, peak about 385 MB.
- **Cache:**
  `logs/runner-cache/cubic_ice_long_wavelength_stiffness_stays_above_the_sum_rule_from_l12_to_l24_2026_09_24.txt`
- **Arithmetic:** exact integer enumeration of the L = 2 torus; the
  covariance by fast Fourier transform after every loop; the winding fit
  by bisection on the discrete Gaussian.

## Theorem — L = 12 and L = 24 diagnostics

On the L = 12 and L = 24 tori with the stated sampling, the binned
diagnostics are as stated. On each torus the smallest wavevectors imply
a stiffness 0.1% to 0.5% above K_cont/2, by more than 3 binned standard
errors, and the two offsets agree within 2 combined standard errors. No
limit beyond L = 24 is claimed.

## No-Go Discipline Gate

- **N1 — Domain:** L = 12 and L = 24 with the stated seeds; the L = 2
  torus exactly.
- **N2 — Independence:** four torus sizes from three runners; the
  identity checked batch by batch. Second seeds are run in the census.
- **N3 — Imports:** uniform ice, the Gaussian comparison and the sampler
  are supplied models and tools; no new axiom or primitive.
- **N4 — Dependencies:** landed PR 8881 and PR 8968 supply
  definitions within their scope. The L = 8 and L = 16 rows are cited,
  not recomputed.
- **N5 — Resolution:** binned errors are descriptive estimates. A
  comparison across sizes is descriptive, not an estimate of a proven
  common limit.
- **N6 — Remaining work:** larger tori; whether the smallest-wavevector
  and winding diagnostics meet.
- **N7 — Strongest objection:** L = 24 has 5 × 10⁵ loops and a 0.06%
  error; five rows on four sizes do not establish a limiting stiffness.
- **N8 — Review boundary:** no audit verdict, retained grade or assembly
  decision is applied.

## Falsifiers

- A fresh run of the runner that fails a check. It would challenge the
  stated reproduction, not alone a different infinite-volume theory.

## Imports

- [minimal_axioms](MINIMAL_AXIOMS_2026-06-29.md): repository boundary;
  does not derive the supplied ice model.
- Landed PR 8881 and PR 8968 are cited for definitions and values.
  Finite counting, the discrete Fourier transform and Gaussian integrals
  are mathematical tools, not physical premises.

## Review record

- **Seat:** one Opus 5.5 seat; no subagents; runner and note by the same
  seat. No separate reviewer or audit is claimed.
- **Correction before landing.** The first draft asked each winding fit to
  agree with its torus's smallest wavevectors within 2 standard errors of
  their batch difference. A second seed on L = 16 had already failed that
  form (PR 8968), so the agreement is not claimed. The check then
  asked each winding fit to lie above K_cont/2 by more than 2 standard
  errors and within 1% of it. The census's second pair of seeds failed
  that form on one torus, so the side is not claimed either; the check now
  asks only that each winding fit lie within 1% of K_cont/2.
- **Mutation census** (caught means at least one FAIL line or a nonzero
  exit; the runner exits nonzero on any FAIL):

| Mutant | Change | Result |
|---|---|---|
| projector of E_x in place of E_z | projector changed | caught (1 FAIL) |
| whole zone in place of the smallest wavevectors | set changed | caught (2 FAILs) |
| winding Gaussian of twice the width | Gaussian changed | caught (1 FAIL) |
| sampler biased toward its first candidate | sampler made non-uniform | caught (3 FAILs) |
| spectrum normalized by N − 1 | normalisation changed | caught (1 FAIL) |
| calibration without the zero mode | K_cont shifted by 1/N | caught (2 FAILs) |
| inner and outer halves swapped | halves swapped | caught (1 FAIL) |

  7 of 7 are caught. A second pair of seeds (control) passes all seven
  checks of this form.
- **Budget:** 7 checks, stdout 1667 characters (ceiling 6000), about
  330 s unloaded and up to 660 s under load (declared audit timeout 1800 s), peak about
  385 MB.

## Verification

```bash
python3 scripts/cubic_ice_long_wavelength_stiffness_stays_above_the_sum_rule_from_l12_to_l24_2026_09_24.py
```

Expected summary line: `TOTAL: PASS=7 FAIL=0`; the runner exits nonzero
if any check fails. Cached output:
`logs/runner-cache/cubic_ice_long_wavelength_stiffness_stays_above_the_sum_rule_from_l12_to_l24_2026_09_24.txt`.

## Canonical dependencies and review boundary

- [uniform_ice_on_cubic_tori_winding_stiffness_and_correlations_carry_the_sum_rule_stiffness_bounded_theorem_note_2026-09-23](UNIFORM_ICE_ON_CUBIC_TORI_WINDING_STIFFNESS_AND_CORRELATIONS_CARRY_THE_SUM_RULE_STIFFNESS_BOUNDED_THEOREM_NOTE_2026-09-23.md): supplied model definitions and finite comparisons only.
- [cubic_ice_long_wavelength_stiffness_lies_measurably_above_the_unit_field_sum_rule_bounded_theorem_note_2026-09-24](CUBIC_ICE_LONG_WAVELENGTH_STIFFNESS_LIES_MEASURABLY_ABOVE_THE_UNIT_FIELD_SUM_RULE_BOUNDED_THEOREM_NOTE_2026-09-24.md): supplied model definitions and finite comparisons only.

The historical author review and mutation census above are provenance. Current evidence is freshly captured; binned standard errors have no proven mixing or coverage guarantee. All quoted stiffness offsets compare c with K_cont/2.
