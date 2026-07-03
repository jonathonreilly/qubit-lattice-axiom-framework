# The Erosion Recurrence Derived Exactly: the Correlator Is a Closed Path-Product c₀·∏(1−ε²)/(1+sⱼεp₍ⱼ₋₁₎)², and the Threshold Indicator Locates the Checked Single-Ratio Obstruction (Bounded)

**Date:** 2026-06-12
**Type:** bounded_theorem (rate-law follow-on of the erosion-rate-table note; cross-referenced source proposal, not graded here)
**Claim type:** bounded_theorem
**Related source:** [`EROSION_RATE_TABLE_NO_TESTED_CLOSED_FORM_BOUNDED_THEOREM_NOTE_2026-06-12.md`](EROSION_RATE_TABLE_NO_TESTED_CLOSED_FORM_BOUNDED_THEOREM_NOTE_2026-06-12.md)
**Primary runner:** [`scripts/frontier_erosion_exact_recurrence_path_product_2026_06_12.py`](../scripts/frontier_erosion_exact_recurrence_path_product_2026_06_12.py)
**Runner cache:** [`logs/runner-cache/frontier_erosion_exact_recurrence_path_product_2026_06_12.txt`](../logs/runner-cache/frontier_erosion_exact_recurrence_path_product_2026_06_12.txt)
**Status:** source proposal; the audit lane grades. Runner `PASS=16 FAIL=0`.

## Findings

- **The single-branch Kraus action derived exactly.** For `M± = √((1 ± εZ)/2)` on a
  branch with pointer Bloch vector `(x, y, p)`: the outcome-`s` daughter has weight
  `w_s = (1 + sεp)/2`, polarization `p_s = (p + sε)/(1 + sεp)`, and transverse
  components scaled by `√(1−ε²)/(1 + sεp)` — so the pointer–fragment connected
  correlator picks up exactly `(1−ε²)/(1 + sεp)²` per step (each of the two
  transverse-coherence factors contributes once; gated against direct 2×2 algebra at
  `10⁻¹⁴`). Hence the **closed path-product** along any phase-2 outcome path:
  `c_path = c₀ · ∏ⱼ (1−ε²)/(1 + sⱼ ε p₍ⱼ₋₁₎)²`.
- **The recurrence matches the direct 16-dim tree** at `10⁻¹²` (`ε = 0.6`; the
  `ε = 0.9` comparison holds at the `10⁻⁸` round-off floor from normalized-weight
  division on near-extinct branches — disclosed), and reproduces the measured
  `R̄(t)` tables exactly.
- **The checked-table obstruction located**: the correlator dynamics is closed-form; the
  threshold-count `R̄` applies a nonlinear indicator to the path-product, and the
  crossing ledger (printed, ~10⁴ edge events at `ε = 0.6`) is why **no single ε-only envelope ratio appears on the checked table** (the
  bounded statement; a proof of nonexistence is not claimed) — the in-review
  predecessor's no-closed-form finding now has its located mechanism.

## Scope

This model, exact; the path-product and the checked-table obstruction are the
data. Branch weights are the explicit Kraus/Born weights of this model; no new
axiom, primitive, or extra measure is introduced. `r` untouched. The audit lane
grades.
