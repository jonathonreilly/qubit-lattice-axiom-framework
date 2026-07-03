# The First Controlled-Truncation Datum for the d=2 Checkerboard Convention: the Resolvent Error of the Band-Truncated Step Is Measured, Grows With L (Consistent With the Range-Unbounded Tail), and Orders With Truncation Harshness (Bounded)

**Date:** 2026-06-12
**Type:** bounded_theorem (the named follow-on of the range-unbounded d=2 note; cross-referenced, not graded)
**Claim type:** bounded_theorem
**Script:** `scripts/frontier_d2_truncation_error_budget_2026_06_12.py`
**Cache:** `logs/runner-cache/frontier_d2_truncation_error_budget_2026_06_12.txt`
**Status:** source proposal; the audit lane grades. Runner `PASS=10 FAIL=0`.

## Findings

Truncating the exact step-2 Hamiltonian to the step-1 family (`d² ∈ {4,8}` + on-site)
and then stepping exactly: the retained-site resolvent error at `E = 0` is **measured**
(`1.35×10⁻²` at `L = 16` — a regression-style measured ceiling, not an independent bound), **grows with `L`**
(`4.6×10⁻³ → 1.35×10⁻²`, ratio ≤ 4 — attributed to the growing dropped-tail **support**
(more long-range couplings exist to drop at larger `L`; the max dropped-tail amplitude
stays within a factor-two gate), and **orders with harshness** (keep-`d²=4`-only error >
keep-`{4,8}` error > 0). Truncating nothing reproduces the exact step (`10⁻¹²`).

## Scope

Finite-`L`, `E = 0`, free; the measured budget is the datum — no flow or fixed-point
claims. No new axiom/primitive/measure/weight; `r` untouched. The audit lane grades.
