# The Det-Phase's Harmonic Depth Is Realized-State Data: One State Saturates at Order 4 (Capture 0.995) While Others Do Not Reach 0.99 Through Order 8 (Ceilings 0.957–0.984) — Exact-Tone, Leakage-Free (Bounded)

**Date:** 2026-06-12
**Type:** bounded_theorem (the capture-vs-order follow-on of the order-3 refutation, in review — cross-referenced, not graded)
**Claim type:** bounded_theorem
**Script:** `scripts/frontier_det_phase_capture_vs_order_2026_06_12.py`
**Cache:** `logs/runner-cache/frontier_det_phase_capture_vs_order_2026_06_12.txt`
**Status:** source proposal; the audit lane grades. Runner `PASS=12 FAIL=0` — exact-tone least-squares projection (no binned DFT; the leakage critique implemented).

## Findings

With the predicted tone sets `W_o` (signed sums of ≤ `o` of the 3 single-particle
gaps; sparse, gated), the captured fraction is monotone-nondecreasing in `o`
(nested spans, gated) and the saturation pattern is **mixed — the panel caught the
draft's "every state" as false**: the `K = 6` state **saturates at `o* = 4`**
(capture `0.995`), while the `K = 3` and `K = 4` states do **not** reach `0.99`
through `o = 8` (ceilings `0.957–0.984`) — each gated as the fixed per-state
statement. **The harmonic depth itself is realized-state data** (the counterfactual
split applied to spectral depth): no state-independent 0.99 capture depth exists
through order `8` on the tested family, and the analytic route must handle
state-dependent harmonic content (the
named follow-on: the winding/integrated-phase route, and what distinguishes the
shallow `K = 6` state). Domain `K ∈ [3,6]` by rank
arithmetic; rank floors gated.

## Scope

Free sector, `L = 3`, this period; trajectories are realized-state data under the
realized-state primitive
([`REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md`](REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md)).
The capture curve is registered data for the supplied state family, not a
state-selection, typicality, genericity, weighting, or averaging rule. No new
axiom/primitive/measure/weight; `r` untouched. The audit lane grades.
