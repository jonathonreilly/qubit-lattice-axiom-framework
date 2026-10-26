---
claim_id: cubic_ice_small_wavevector_covariance_keeps_the_transverse_angular_form_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "DRAFT, preserved for review. Finite binned diagnostics of uniform ice's unit-arrow covariance on the L = 16 cubic torus. Wavevector sets whose folded components are the same multiset share Q exactly, so under the transverse form their covariance ratios agree. With the runner's four seeds (4001-4004, 160 batches) the mean difference over five multisets is +0.00008 +- 0.00030 and every check passes; with four control seeds (4005-4008) one multiset reaches 3.0 binned standard errors and the per-multiset check fails; pooled over 400 batches with the two seeds of landed PR 8968 the mean is +0.00050 +- 0.00019. The transverse form holds within about 0.2%; below that it is unsettled, and the seed-set scatter suggests the binned errors understate the spread. The offset of landed PR 8968 is reproduced with independent seeds: c = 0.33450 +- 0.00010, 0.337% above half the continuous calibration. No thermodynamic limit, mixing bound or physical law is asserted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/cubic_ice_small_wavevector_covariance_keeps_the_transverse_angular_form_2026_09_24.py
---

# Cubic ice on L = 16: the transverse angular form holds within 0.2%; below that it is unsettled (draft)

**Date:** 2026-09-24
**Type:** bounded_theorem

Uniform ice and every Gaussian comparison below are supplied mathematical
models, as in landed PR 8881. They are not derived from the repository
axioms or adopted as a physical law. Every number is a finite diagnostic
of the stated sampling.

## Question

Landed PR 8968 found that the smallest wavevectors of the unit-arrow
covariance on the L = 16 torus imply a Gaussian stiffness 0.29% above half
the continuous calibration K_cont = (2N+1)/(3N). Landed PR 8984 found the
same offset on L = 12 and L = 24. Reading that offset as one stiffness
assumes the covariance keeps the transverse form S_zz = P_zz/K at small
wavevectors, with P_zz = 1 − s_z²/Q. If the form failed, the implied
stiffness would depend on the direction of the wavevector.

## Exact statement

Q = Σ_i 2(1 − cos k_i) is symmetric in the three components. Wavevectors
whose folded components form the same multiset {a, b, c} therefore share
Q exactly, while P_zz depends on which component lies along z. Under the
transverse form, the batch ratio r = K_cont Σ S_zz / Σ P_zz (landed PR
8968) is the same for every assignment of the multiset. The runner
confirms the shared Q to 1.3e-15 and finds five multisets with |k|² at
most 9 units that have two usable assignments (P_zz > 0.05).

## Finite diagnostics

The runner uses four fresh seeds of 10⁶ loops each, 160 batches in all.
Standard errors are binned and descriptive: no mixing bound, simultaneous
coverage or thermodynamic extrapolation is asserted.

1. **Identity and offset.** Every batch obeys the unit-arrow identity
   within 1.8e-12. The 24 smallest wavevectors imply c = 0.33450 ±
   0.00010, 0.337% above K_cont/2 at 10.8 binned standard errors. This
   reproduces landed PR 8968 (0.33434 ± 0.00016 and 0.33447 ± 0.00018) with
   independent seeds.

2. **Angular form.** For each multiset, the ratio of the assignment with
   the smallest P_zz minus the one with the largest:

   | Multiset | P_zz (large, small) | Difference |
   |---|---|---|
   | {0, 1, 1} | 1.000, 0.500 | −0.0006 ± 0.0008 |
   | {0, 1, 2} | 1.000, 0.206 | +0.0003 ± 0.0006 |
   | {0, 2, 2} | 1.000, 0.500 | +0.0001 ± 0.0009 |
   | {1, 1, 2} | 0.829, 0.342 | −0.0005 ± 0.0006 |
   | {1, 2, 2} | 0.885, 0.558 | +0.0010 ± 0.0006 |

   With these seeds the mean is +0.00008 ± 0.00030, and every check
   passes.

3. **Other seeds disagree.** The census control, four other seeds
   (4005–4008), gives {0, 1, 1} +0.0024 ± 0.0008, 3.0 standard errors, and
   fails the per-multiset check; its mean is +0.00072 ± 0.00031. The two
   seeds of landed PR 8968 give +0.00089 ± 0.00045. Pooled over all 400
   batches the mean is +0.00050 ± 0.00019. For {0, 1, 1} and {1, 1, 2}
   the three seed sets scatter more than their binned errors allow (χ²
   probabilities about 0.02 and 0.05), so the binned errors likely
   understate the spread of these small differences. These values were
   computed outside the runner from the same sampler and are recorded here.

4. **Reading.** The transverse form holds within about 0.2%; no seed set
   exceeds 0.25% in any multiset. Below that it is unsettled: a
   difference of about 0.05% is neither established nor excluded. The
   offset itself is robust. The three seed sets give c = 0.33434, 0.33447
   and 0.33450, within their errors.

## Machine status and trace

- **Runner:**
  `scripts/cubic_ice_small_wavevector_covariance_keeps_the_transverse_angular_form_2026_09_24.py`
  (declares `AUDIT_TIMEOUT_SEC = 3600`).
- **Result:** `TOTAL: PASS=6 FAIL=0`, about 12 minutes alone and 18 minutes under
  load, stdout 1454 characters, peak about 390 MB.
- **Cache:**
  `logs/runner-cache/cubic_ice_small_wavevector_covariance_keeps_the_transverse_angular_form_2026_09_24.txt`
- **Arithmetic:** exact integer enumeration of the L = 2 torus; the
  covariance by fast Fourier transform after every loop.

## Theorem — Permuted sets and L = 16 diagnostics

Permuted wavevector sets share Q exactly. On the L = 16 torus with the
runner's seeds, the binned diagnostics are as stated, and every check
passes. The runner's angular check is not robust to the choice of seeds,
so it is not claimed as a property of the model. No limit beyond L = 16 is
claimed.

## No-Go Discipline Gate

- **N1 — Domain:** L = 16 with the stated seeds; multisets with |k|² at
  most 9 units.
- **N2 — Independence:** four seeds not used in landed PR 8968; the
  identity checked batch by batch; a further seed set is run in the
  census.
- **N3 — Imports:** uniform ice, the Gaussian comparison and the sampler
  are supplied models and tools; no new axiom or primitive.
- **N4 — Dependencies:** landed PRs 8881, 8968 and 8984 supply
  definitions and values within their scope.
- **N5 — Resolution:** binned errors are descriptive estimates. The
  angular form is tested only through the five multisets named.
- **N6 — Remaining work:** larger tori; larger |k|; the other components.
- **N7 — Strongest objection:** the angular check passes on the runner's
  seeds but fails on the control seeds, and binned errors may understate
  the spread; only the 0.2% bound and the replicated offset are robust.
- **N8 — Review boundary:** no audit verdict, retained grade or assembly
  decision is applied.

## Falsifiers

- A fresh run of the runner that fails a check. It would challenge the
  stated reproduction, not alone a different infinite-volume theory.

## Imports

- [minimal_axioms](MINIMAL_AXIOMS_2026-06-29.md): repository boundary;
  does not derive the supplied ice model.
- Landed PRs 8881, 8968 and 8984 are cited for definitions and values.
  The discrete Fourier transform and Gaussian integrals are mathematical
  tools, not physical premises.

## Review record

- **Seat:** one Opus 5.5 seat; no subagents. The runner reuses the
  functions and the exact L = 2 control of landed PR 8968. No separate
  reviewer or audit is claimed.
- **Design.** The permutation test was first run on the two saved seeds
  of landed PR 8968 and gave a 2.0-standard-error hint. The runner was then
  written with four fresh seeds and its thresholds set at 3 standard errors
  and 0.1%. The census runs a further four seeds as a control, and that
  control FAILS the angular check (see item 3). This PR is therefore a
  draft that preserves the test and its data. A clean version would use
  errors from independent seeds rather than batches, more seeds, and a
  bound of about 0.2%.
- **Mutation census** (caught means at least one FAIL line or a nonzero
  exit; the runner exits nonzero on any FAIL):

| Mutant | Change | Result |
|---|---|---|
| projector of E_x in place of E_z | projector changed | caught (3 FAILs) |
| squared projector | angular form changed | caught (2 FAILs) |
| spectrum of E_x against the E_z projector | component changed | caught (2 FAILs) |
| spectrum normalized by N − 1 | normalisation changed | caught (1 FAIL) |
| sampler biased toward its first candidate | sampler made non-uniform | caught (2 FAILs) |
| whole zone in place of the smallest wavevectors | set changed | caught (1 FAIL) |
| control: four other seeds | seeds changed | FAILS the angular check (1 FAIL) |

  6 of 6 mutants are caught, but the seed control fails, so the angular
  check is seed-fragile.
- **Budget:** 6 checks, stdout 1454 characters (ceiling 6000), about
  12 to 18 minutes (declared audit timeout 3600 s), peak about 390 MB.

## Verification

```bash
python3 scripts/cubic_ice_small_wavevector_covariance_keeps_the_transverse_angular_form_2026_09_24.py
```

Expected summary line: `TOTAL: PASS=6 FAIL=0`; the runner exits nonzero
if any check fails. Cached output:
`logs/runner-cache/cubic_ice_small_wavevector_covariance_keeps_the_transverse_angular_form_2026_09_24.txt`.
