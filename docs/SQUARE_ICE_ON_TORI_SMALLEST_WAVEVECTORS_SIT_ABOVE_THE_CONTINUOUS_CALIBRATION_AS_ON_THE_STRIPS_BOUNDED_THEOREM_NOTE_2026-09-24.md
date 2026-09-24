---
claim_id: square_ice_on_tori_smallest_wavevectors_sit_above_the_continuous_calibration_as_on_the_strips_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "An exact weighted identity for the unit-arrow covariance of square ice on L x L tori, exact L = 2 counts, and finite binned diagnostics on L = 32, 64 and 128: the smallest wavevectors imply a Gaussian stiffness 4.3% to 4.7% above the continuous zero-mode calibration K_cont = (N+1)/(2N), in the range landed PR 8930 records for strip flux costs; the discrete winding fit agrees with them within binned errors on each torus; the covariance ratio rises by about 15% across the zone. No thermodynamic limit, mixing bound or physical law is asserted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/square_ice_on_tori_smallest_wavevectors_sit_above_the_continuous_calibration_as_on_the_strips_2026_09_24.py
---

# Square ice on L × L tori: the smallest wavevectors sit above the continuous calibration, as on the strips

**Date:** 2026-09-24
**Type:** bounded_theorem

Square ice and every Gaussian comparison below are supplied mathematical
models, as in landed PRs 8930 and 8954. They are not derived from the
repository axioms or adopted as a physical law. Every number is a finite
diagnostic of the stated sampling.

## Objects

- **Square ice** on the even L × L torus, N = L²: two of the four links
  at every vertex are occupied, so the staggered unit field E_i = ±1 has
  zero divergence at every vertex.
- **Loop sampler.** A loop starts at a uniform vertex, reverses an
  outgoing arrow, and at each later vertex reverses one of the two
  outgoing arrows other than the one just reversed, each with probability
  1/2, until it returns to the start. A reversed loop has the same
  probability, so the uniform measure is stationary; this is the planar
  form of the sampler of landed PR 8881.
- **Covariance and calibration.** S_yy(q) = (1/N)|E_y(q)|², averaged
  within each batch. With s_i² = 2 − 2 cos q_i and Q = s_x² + s_y², the
  transverse projector is P_yy = 1 − s_y²/Q. Its sum over q ≠ 0 is
  (N − 1)/2, so a Gaussian with a continuous zero mode has unit variance
  at K_cont = (N + 1)/(2N).
- **Batch ratio.** r = K_cont Σ S_yy / Σ P_yy over a set of wavevectors,
  formed within each of 40 batches; c = K_cont/(2r) is the Gaussian
  stiffness that set implies.
- **Discrete winding fit.** c_W = K_W/2, where K_W reproduces the
  sampled ⟨W²⟩ under weights exp(−K W²/2) on W = −L, −L + 2, …, L.

## Exact statements

- **Identity.** Because E_y² = 1 on every link, Σ_q S_yy(q) = N in every
  configuration. Where P_yy = 0 the wavevector lies along y, zero
  divergence forces E_y(q) = 0, and the term vanishes. Hence the
  P_yy-weighted mean of r = K_cont S_yy/P_yy, with the zero mode at weight
  1, equals 1. This is the planar form of the identity of open PR 8968.
- **L = 2 control.** All 2^8 arrow patterns of the 2 × 2 torus give 18
  ice configurations, 6 at zero flux, in 9 winding sectors, with ⟨W²⟩ =
  16/9.

## Finite diagnostics

The runner uses 10⁶ loops on each of L = 32, 64 and 128, in 40 batches,
with fixed seeds; the spectrum is taken after every loop, or every second
loop on L = 128. Standard errors are binned and descriptive: no mixing
bound, simultaneous coverage or thermodynamic extrapolation is asserted.

1. **Controls.** On L = 2 the sampler gives ⟨W²⟩ = 1.7757 ± 0.0029
   against 16/9 and visits all 9 sectors. On the three tori every batch
   obeys the identity within 3.6e-12, and no vertex carries divergence.

2. **Smallest wavevectors.** Take the wavevectors with folded |k|² at most
   2 units of 2π/L and P_yy > 0.05:

   | Torus | c | above K_cont/2 |
   |---|---|---|
   | L = 32 | 0.26198 ± 0.00043 | +4.69% ± 0.17% |
   | L = 64 | 0.26155 ± 0.00054 | +4.59% ± 0.22% |
   | L = 128 | 0.26076 ± 0.00061 | +4.30% ± 0.25% |

   Landed PR 8930 records strip flux costs 4.1% to 4.7% above the planar
   calibration, rising to 0.26090 at width 20. The torus values fall in
   the same range, by an independent method. L = 128 sits 1.3 combined
   standard errors below L = 32.

3. **Discrete winding fits.** c_W = 0.26193 ± 0.00061, 0.26202 ± 0.00080
   and 0.26044 ± 0.00075 on the three tori, 4.2% to 4.8% above the
   calibration. Batch by batch the differences to the smallest wavevectors
   are −0.00003 ± 0.00077, +0.00051 ± 0.00109 and −0.00030 ± 0.00087. On
   the cubic tori of open PRs 8968 and 8984 the two diagnostics sit
   0.0008 to 0.0012 apart on the larger tori; on these planar tori they
   are not resolved from each other.

4. **Zone profile on L = 128.** In eight shells of Q the ratio reads
   0.9556, 0.9580, 0.9604, 0.9650, 0.9678, 0.9808, 1.0147 and 1.1082, a
   rise of about 15% from the innermost shell to the outermost. The outer
   half of the zone (Q ≥ 4) reads 1.03552 ± 0.00006. By the identity, the
   long-wavelength offset is the weighted mean of this rise measured from
   the smallest wavevectors. Landed PR 8954 records the same pattern in
   row correlations on strips.

## Machine status and trace

- **Runner:**
  `scripts/square_ice_on_tori_smallest_wavevectors_sit_above_the_continuous_calibration_as_on_the_strips_2026_09_24.py`
- **Result:** `TOTAL: PASS=6 FAIL=0`, about 340 s, stdout 1457 characters,
  peak about 105 MB.
- **Cache:**
  `logs/runner-cache/square_ice_on_tori_smallest_wavevectors_sit_above_the_continuous_calibration_as_on_the_strips_2026_09_24.txt`
- **Arithmetic:** exact enumeration of the 2 × 2 torus with rational
  ⟨W²⟩; the covariance by fast Fourier transform; the winding fit by
  bisection on the discrete Gaussian.

## Theorem — Planar identity and torus diagnostics

The weighted identity holds exactly for every unit-arrow configuration of
square ice on every even torus, and the L = 2 counts are exact. On the
L = 32, 64 and 128 tori with the stated sampling, the binned diagnostics
are as stated. No limit beyond L = 128 is claimed.

## No-Go Discipline Gate

- **N1 — Domain:** the identity on even tori; the diagnostics on L = 32,
  64 and 128 with the stated seeds.
- **N2 — Independence:** the torus loop sampler is independent of the
  strip transfer computations of landed PR 8930; the identity is checked
  batch by batch; second seeds are run in the census.
- **N3 — Imports:** square ice, the Gaussian comparison and the sampler
  are supplied models and tools; no new axiom, primitive or comparator.
- **N4 — Dependencies:** landed PRs 8930 and 8954 and open PR 8968 supply
  definitions and comparisons within their scope.
- **N5 — Resolution:** binned errors are descriptive estimates. The
  comparison with the strips is descriptive, not an estimate of a proven
  common limit.
- **N6 — Remaining work:** larger tori; the size dependence of the
  offset; why the winding fit and the smallest wavevectors separate on
  cubic tori and not on these.
- **N7 — Strongest objection:** three torus sizes do not establish a
  limiting stiffness.
- **N8 — Review boundary:** no audit verdict, retained grade or assembly
  decision is applied.

## Falsifiers

- A counterexample to the weighted identity for a unit-arrow
  configuration of square ice.
- A fresh run of the runner that fails a check. It would challenge the
  stated reproduction, not alone a different infinite-volume theory.

## Imports

- [minimal_axioms](MINIMAL_AXIOMS_2026-06-29.md): repository boundary;
  does not derive the supplied ice model.
- Landed PRs 8930 and 8954 and open PR 8968 are cited for definitions and
  comparisons. Finite counting, the discrete Fourier transform and
  Gaussian integrals are mathematical tools, not physical premises.

## Review record

- **Seat:** one Opus 5.5 seat; no subagents; runner and note by the same
  seat. No separate reviewer or audit is claimed.
- **Design before the run.** The check brackets (3% to 6% above the
  calibration, more than 10 standard errors, a rise above 5%) were set
  from the strip values of landed PR 8930 before the full run. A trial
  with 10⁵ loops per torus gave the same offsets with errors three times
  larger and failed only the 10-standard-error condition.
- **Mutation census** (caught means at least one FAIL line or a nonzero
  exit; the runner exits nonzero on any FAIL):

| Mutant | Change | Result |
|---|---|---|
| projector of E_x in place of E_y | projector changed | caught (1 FAIL) |
| spectrum of E_x against the E_y projector | component changed | caught (1 FAIL) |
| whole zone in place of the smallest wavevectors | set changed | caught (1 FAIL) |
| winding Gaussian of twice the width | Gaussian changed | caught (1 FAIL) |
| sampler biased toward its first candidate | sampler made non-uniform | caught (3 FAILs) |
| spectrum normalized by N − 1 | normalisation changed | caught (1 FAIL) |
| zone profile read in reverse | direction reversed | caught (1 FAIL) |
| cubic calibration in the plane | calibration changed | caught (2 FAILs) |

  8 of 8 are caught. A second set of seeds (control) passes all six
  checks.
- **Budget:** 6 checks, stdout 1457 characters (ceiling 6000), about
  340 s (declared audit timeout 1800 s), peak about 105 MB.

## Verification

```bash
python3 scripts/square_ice_on_tori_smallest_wavevectors_sit_above_the_continuous_calibration_as_on_the_strips_2026_09_24.py
```

Expected summary line: `TOTAL: PASS=6 FAIL=0`; the runner exits nonzero
if any check fails. Cached output:
`logs/runner-cache/square_ice_on_tori_smallest_wavevectors_sit_above_the_continuous_calibration_as_on_the_strips_2026_09_24.txt`.
