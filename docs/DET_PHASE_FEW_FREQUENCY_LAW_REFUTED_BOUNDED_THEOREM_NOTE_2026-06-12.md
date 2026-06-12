# The Order-3 Determinant-Degree Spectral Candidate Is Refuted for the Det-Phase Under the Stated Finite-DFT Convention (State-Dependent Capture 0.33–0.85 in 7 of 256 Bins); Higher Orders Capture More and Are Not Refuted; Domain K ∈ [3,6] by Rank Arithmetic (Bounded)

**Date:** 2026-06-12
**Type:** bounded theorem (the spectral-anatomy probe of the gauge lane's deterministic baseline phase)
**Claim type:** bounded_theorem
**Script:** `scripts/frontier_det_phase_spectral_law_refuted_2026_06_12.py`
**Cache:** `logs/runner-cache/frontier_det_phase_spectral_law_refuted_2026_06_12.txt`
**Status:** source proposal; the audit lane grades. Runner `PASS=7 FAIL=0`.

## Findings

- **The domain is forced by rank arithmetic**: the 3×3 cross-block of a `K`-particle
  Slater projector has rank `≤ min(K, 9−K)`, so the det-phase is identically
  undefined at `K = 2` and `K = 7` (both gated as exclusion data); the sweep domain
  is `K ∈ [3,6]` (+ a second seed), with the rank floor clean (`min sv = 1.1×10⁻²`).
- **The order-3 candidate dies honestly — and only it**: the sparse order-3 gap-sum
  alias set (3 distinct gaps → **7 of 256 bins**, the determinant-degree carrier)
  captures `0.33–0.85` of the increment spectral power, state-dependently — the
  order-3 law fails at the worst state (gated). **Higher orders are not refuted**:
  the panel's probe shows order-5 already captures substantially more; the
  capture-vs-order curve is the named follow-on. The full-support statement is a
  **finite-window DFT leakage statement** (the gaps sit off-grid — e.g. bin
  `42.78 → 43`; aliasing/binning convention stated), not exact spectral support. A
  gcd-style "predicted set" would have covered all bins and made the law vacuous —
  rejected in-runner.
- Amplitudes differ strongly between states (gated) — but at order 3 the
  frequencies-vs-amplitudes split has no adequate carrier: the analytic route
  to the deterministic phase must go through a different object (the named
  follow-on: the integrated phase / winding rather than increments).

## Scope

Free sector, `L = 3`, this period and alias map (`τ = 0.35`, `T = 256` — stated);
trajectories are realized-state data; the refutation and the capture spread are the
data. No new axiom/primitive/measure/weight; `r` untouched. The audit lane grades.
