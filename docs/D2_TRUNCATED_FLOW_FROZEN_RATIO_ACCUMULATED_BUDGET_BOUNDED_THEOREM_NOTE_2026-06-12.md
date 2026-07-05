# Iterating the Band-Truncated d=2 Step: Exact Post-Step-2 Closure (H_kd = 0 Forces the Kept Couplings Invariant — Theorem by Algebra, Verified), Per-Step Errors Decay Then Plateau, and the Accumulated Budget Is Measured (Bounded)

**Date:** 2026-06-12
**Type:** bounded_theorem (follow-on of the d=2 truncation-budget note; cross-referenced source proposal, not graded here)
**Claim type:** bounded_theorem
**Primary runner:** [`scripts/frontier_d2_truncated_flow_frozen_ratio_2026_06_12.py`](../scripts/frontier_d2_truncated_flow_frozen_ratio_2026_06_12.py)
**Runner cache:** [`logs/runner-cache/frontier_d2_truncated_flow_frozen_ratio_2026_06_12.txt`](../logs/runner-cache/frontier_d2_truncated_flow_frozen_ratio_2026_06_12.txt)
**Status:** source proposal; the audit lane grades. Runner `PASS=9 FAIL=0`.

## Findings

Iterating the keep-`{4,8}`-band truncation through four exact checkerboard steps
(`L = 16`; `L = 12` stability probe): **the truncated flow closes exactly after
step 2 — by algebra, not coincidence**: from step 2 onward the kept-band coupling
between retained and decimated sublattices vanishes (`H_kd = 0`; `c8`-count `0`), so
the truncated step leaves `diag` and `c4` invariant identically (verified at
`10⁻¹²`). The freeze is a theorem of this truncation convention, stated as such. Per-step truncation errors **decay then plateau** (`k1 > k2 > k3 = k4`,
gated); the accumulated retained-block resolvent budget is `3.20×10⁻²` at `L = 16`
(frozen regression ceiling `3.21×10⁻²`, labeled — not value-derived at runtime), with
`L = 12` vs `L = 16` stability within the frozen 1% tolerance (labeled). Identity truncation
reproduces the exact pipeline (`10⁻¹²`).

## Scope

Finite-`L`, `E = 0`, free; a measured-budget truncated **trajectory with a frozen
ratio** — not a validated RG flow (the post-step-4 lattice is 16 sites; larger-`L`
iteration depth is the named follow-on). No new axiom/primitive/measure/weight; `r`
untouched. The audit lane grades.
