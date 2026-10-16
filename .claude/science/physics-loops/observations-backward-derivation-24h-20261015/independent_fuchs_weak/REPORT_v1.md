# Focused independent check: relative motion and weak observation equations

The conditional mechanical and weak-window mathematics check out on the
stated domain. Two v1 scope omissions were found before implementation access
and are corrected in v2: equation (4) requires the calibration force to be off,
and full column rank establishes uniqueness conditional on consistency, not
consistency itself. No remaining mathematical error was found in this focused
scope. This is neither an apparatus identification nor an empirical test or
formal audit verdict.

## Source identity and independence

The checked final note is `FUCHS_RELATIVE_MOTION_AND_WEAK_INVERSE_v2.md`,
SHA256 `87c88650707c10c204a106a86749a9fa42d037ee670e4d1093caa75895538d51`.
The complex supplement is `FUCHS_COMPLEX_PROBE_EXTENSION_v1.md`, SHA256
`5fbb6ac65f01c4dc16b7cddd8dba6347581f1444b856de239dfe68698a4b73dd`.
The initial note, both plans, both helpers, synthetic runners and control
receipts are pinned by `FINAL_SOURCE_BINDING_v1.json`: all 15 sources were
unchanged when packaging this report. Full source snapshots are preserved.

`DERIVATION_BEFORE_CODE_v1.md` precedes the original independent checker;
`INDEPENDENT_OUTPUT_FREEZE_v1.json` freezes that proof, code and output before
author implementation or output-artifact access. The separate complex proof,
fixtures and outputs were also frozen before that access. Parent progress
messages disclosed control counts and the coarse-quadrature failure; this was
not blindness to progress summaries. No author code or output artifact was
read before the respective independent output freezes. No raw Fuchs trace,
raw acquisition receipt or development-results artifact was opened. The
actual development-analysis runners were not read or executed.

## Findings

1. Adding the two body equations eliminates the internal force and gives the
   stated determinant, relative response and internal-calibration quotient.
   Equal uniform acceleration cancels the free-support particular response,
   not arbitrary homogeneous motion. Internal calibration can vanish even
   when the mechanical determinant is nonzero: the frozen example has
   `Delta=-1` and `P-m omega^2=0`. The reaction path therefore matters. A small
   mass ratio can strongly change an uncalibrated near-pole response; the
   free-support internal-calibration quotient instead cancels that common
   pole and equals `m(g_t-g_p)/(1+m/M)`. The source must not be read as a claim
   of pole enhancement for every calibrated ratio.
2. Exact constant-carrier demodulation and the bilinear boundary form yield
   the stated second-order weak equation. Polynomial forcing and separately
   added homogeneous histories satisfy it without estimating or subtracting
   initial amplitudes. A varying carrier needs the additional derivative
   terms. The first-order comparison has a generally nonzero, explicitly
   checked defect. The missing-support reconstruction does not establish that
   the reconstructed motion obeys an independently fixed support model.
3. Exact manufactured rows have real rank four and recover
   `(-1,12/5,3/7,2/7)`. Perturbing one right-hand-side row retains rank four
   while making the equations inconsistent. Monochromatic proportional
   input/output has exact rank two; this limit survives arbitrary complex
   compact probes. The complex-probe numerical example has final two singular
   values about `1.10e-15` and `4.56e-16`, alongside the analytic factorization.
4. Common full-history filtering commutes under the stated initialization
   conditions. Different frequency-dependent filter ratios generally cannot
   be absorbed into one constant gain at fixed physical oscillator
   coefficients; proportional filters are an exception. An added filter-state
   transient has nonzero weak residual despite compact endpoint weights.
5. The complex-probe first and second derivatives have the correct signs.
   The integrals are bilinear. Consistently conjugating all weights is another
   valid convention; mixing conventions or dropping modulation derivatives
   fails the independent negative controls. Matching a stipulated tone can
   prevent input-moment cancellation, without guaranteeing parameter rank or
   conditioning. A sampled phase slope selects a probe; it is not a physical
   force-phase calibration. Multiple probes remain correlated data summaries.

Complete inspection of the synthetic runners and helpers found the declared
moments, real design, column normalization and time-window grouping consistent
with these formulas. In complex applications, the shared `fit()` output keys
`train_windows` and `validation_windows` count probe rows, so two probes per
physical interval double those reported counts. The synthetic chronological
split itself keeps both probes from each physical interval together. Downstream
reporting should distinguish probe rows from physical time windows.

## Actual computation and preserved failure

| Execution | Passed / failed | Wall seconds | Evidence |
|---|---:|---:|---|
| Independent first pass | 60 / 0 | 1.110 | `independent_attempt01.*` |
| Independent complex supplement | 85 / 0 | 0.533 | `supplement_attempt01.*` |
| Unchanged author original synthetic runner | 25 / 0 | 0.468 | `author_weak_v1_attempt01.*` |
| Unchanged author complex v2 synthetic runner | 23 / 0 | 0.275 | `author_complex_v2_attempt01.*` |

Each owned execution used Python `-B`, `PYTHONDONTWRITEBYTECODE=1`, and a
120-second subprocess timeout. Full stdout, stderr, argv, environment flag,
CPU time, peak RSS and before/after source hashes are preserved. No owned
execution failed or timed out. Both author replay stdout files are byte
identical to their pinned synthetic receipts. Independent scripts do not
import author code. Author replay occurs only after the independent freezes.

The author's historical complex v1 result was 19 passed, 1 failed: a maximum
weak residual `1.0229861322125439e-10` exceeded the fixed `1e-10` threshold.
Its source, receipt and execution metadata are preserved in
`AUTHOR_SYNTHETIC_EXPOSURE_v1.json`; it was inspected, not rerun here. The
losslessly serialized v1-to-v2 diff confirms only a time-step change from
0.05 to 0.025 seconds and three convergence controls. No equation or tolerance
changed. In the replayed v2, fine residuals are about one quarter of the
coarse residuals and no larger than `2.5571e-11`. This numerical refinement
does not validate an experimental measurement model.

## Concrete remaining obligation

Before using these equations as a physical force or scalar-theory calibration,
independently establish the receiver/source channel correspondence, support
motion or transfer, calibration reaction path, force/geometry/phase map and
channel-filter relation. Bound quadrature and measurement errors, including
noisy-regressor and data-selected-probe dependence, before claiming precision.
The synthetic checks do not establish any of those premises. Actual
development-trace results are outside this report's checked scope.
