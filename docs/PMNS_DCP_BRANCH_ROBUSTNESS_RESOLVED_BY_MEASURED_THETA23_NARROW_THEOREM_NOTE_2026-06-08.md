# PMNS delta_CP Forecast Robustness: Two-Angle Branch Dependence and the Measured theta23 Filter

**Date:** 2026-06-08
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome.
**Scope:** pressure-test of the headline delta_CP forecast
([`PMNS_THETA12_THETA13_DCP_PREDICTIONS_NARROW_THEOREM_NOTE_2026-05-17`](PMNS_THETA12_THETA13_DCP_PREDICTIONS_NARROW_THEOREM_NOTE_2026-05-17.md)).
It does **not** dispute that note's 200-bit interval certificate (rigorous over box `B` / Basin-1);
it **answers that note's own open §5 question** about competing chamber-boundary branches and proposes
a cleaner framing. It adds no axiom and no derived fitted value; the measured
mixing angles are explicit external inputs/comparators.
**Primary runner:**
[`scripts/pmns_dcp_branch_robustness_pressure_test_2026_06_08.py`](../scripts/pmns_dcp_branch_robustness_pressure_test_2026_06_08.py)
**Cached output:**
[`logs/runner-cache/pmns_dcp_branch_robustness_pressure_test_2026_06_08.txt`](../logs/runner-cache/pmns_dcp_branch_robustness_pressure_test_2026_06_08.txt)
(float diagnostic; PASS=4; **anchor-validated** — reproduces the note's
`(s₁₂²,s₁₃²,s₂₃²,δ_CP)=(0.307,0.0218,0.545,260.88°)` at the PDG-central pin).

## The question

P1 forecasts `δ_CP ∈ [251.86°, 270.00°]` (third quadrant, near-maximal CP), via a rigorous box-Krawczyk
interval certificate over box `B` — the **Basin-1** preimage of the NuFit `(s₁₂²,s₁₃²)` rectangle on
the chamber boundary `q = √(8/3) − δ`. The P1 note explicitly states (§5, §7, residual list) that the
certificate is **silent on whether competing chamber-boundary branches give the same δ_CP**, and that
other branches are "inadmissible under the **imposed branch-choice rule**." A reviewer's first attack is:
*is the third-quadrant result a genuine forecast, or an artifact of selecting Basin-1?* This note settles
it at float precision on the note's own chart.

## Findings

Using the identical chart `H(m,δ,q)` (`GAMMA=0.5`) and observable convention (eigen-projectors,
flavor rows `(e,μ,τ)=(2,1,0)`, `δ_CP = atan2(J, −cos_neg_num)`), anchor-validated against the note's
260.88°:

1. **Two-angle input IS branch-dependent (verified).** Scanning a broad `(m,δ)` domain on the chamber
   boundary, the NuFit-central `(s₁₂²,s₁₃²)=(0.307,0.0218)` has **two** preimage basins:
   - **Basin-1** `(m,δ)≈(0.678,0.929)` — `δ_CP` near-maximal (~Q3), `s₂₃²≈0.545`. *(P1's region.)*
   - **Basin-0** `(m,δ)≈(−0.012,1.061)` — `δ_CP ∈ Q2 (~98–114°)`, `s₂₃²≈0.70`.

   So under the note's **stated** logic (`s₁₂²,s₁₃²` as the only inputs), δ_CP is **not** confined to Q3:
   the competing branch lands in the **second** quadrant. This answers the note's open §5 question —
   *competing branches do not agree* — and confirms the imposed Basin-1 rule is genuinely load-bearing
   under two-angle input.

2. **But the competing branch is empirically excluded by the measured `s₂₃²` (the fair test).** Basin-0
   predicts `s₂₃²≈0.70`, whereas the **measured** value is `≈0.545`. When all **three** measured mixing
   angles `(s₁₂²,s₁₃²,s₂₃²)=(0.307,0.0218,0.545)` are imposed, **exactly one** basin survives (Basin-1) —
   the Q2 competitor is gone — and it gives near-maximal CP (`δ_CP` ~Q3). So the branch selection is
   resolved by **data**, not only by an imposed rule.

3. **Embedding sensitivity.** Perturbing the embedding surface `q = √(8/3) − δ + t` by `t∈[−0.1,0.1]`
   moves `δ_CP` by ~25° — but it also moves `(s₁₂²,s₁₃²)` off the NuFit point, so this is the ordinary
   input-dependence of a forecast pinned to the chamber boundary, not a free dial.

## Constructive reframing (the recommendation)

State the δ_CP forecast **conditional on all three measured mixing angles** `(s₁₂²,s₁₃²,s₂₃²)`, not on
two. This **replaces the "imposed branch-choice rule" with the empirically distinguishable `s₂₃²`**: the
branch the framework selects (Basin-1) is exactly the one consistent with the measured `s₂₃²`, and the
Q2 competitor is then excluded by data. Cost: `s₂₃²` becomes an input rather than a co-prediction
(P2's `s₂₃²>0.5` would then be a consistency statement on the same branch, not an independent forecast).
Benefit: the headline DUNE forecast no longer rests on an unjustified branch rule — its only remaining
conditionalities are the (named external) NuFit inputs and the **(X6) preimage-localization to `B`**,
which remains the genuine unaudited admission to close.

## What is and is not claimed

- **Is:** the two-angle δ_CP forecast is branch-dependent (a competing chamber-boundary preimage gives
  Q2, `s₂₃²≈0.70`); fixing the measured `s₂₃²` leaves a single near-maximal-CP branch (the Q2 competitor
  is data-excluded); so the prediction is best stated conditional on all three measured angles, dropping
  the imposed branch rule.
- **Is not:** does **not** dispute the P1 200-bit interval certificate or its `[251.86°,270°]` bracket
  (that is rigorous over `B`/Basin-1; this float scan checks only branch structure, not the bracket);
  does **not** derive the chart, the chamber boundary, or the NuFit inputs; does **not** close the (X6)
  preimage-localization admission; adds no axiom or fitted value.

## Boundaries (honest)

- **Float diagnostic, bounded scan.** The branch-structure facts are float-precision over the scanned
  domain `m∈[−1.5,3.5], δ∈[0,2.6]`; a broader/finer scan could find further basins. The rigorous bracket
  is the P1 note's interval certificate, not this note.
- **`s₂₃²` is itself measured.** Treating it as a third input is legitimate (it is an observed quantity),
  but it converts P2's octant statement into a same-branch consistency check on this surface.

## Forbidden-imports check

No PDG / NuFit value is consumed as a derived quantity. The measured
`(0.307,0.0218,0.545)` triple is an explicit external localization/comparison
target, exactly as the forecast note uses the NuFit rectangle. The chart,
eigen-projectors, Jarlskog, and cos-companion are reproduced in the runner from
the framework chart; the anchor cross-check ties the convention to the forecast
note's reported 260.88°.
