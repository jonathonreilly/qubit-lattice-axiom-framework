# The Order-3 Determinant-Degree Spectral Candidate Is Refuted for Det-Phase Increments Under the Stated Finite-DFT Convention; Higher Orders Remain Open; Domain K ∈ [3,6] by Rank Arithmetic (Bounded)

**Date:** 2026-06-12
**Claim type:** bounded_theorem
**Primary runner:** [`scripts/frontier_det_phase_spectral_law_refuted_2026_06_12.py`](../scripts/frontier_det_phase_spectral_law_refuted_2026_06_12.py)
**Runner cache:** [`logs/runner-cache/frontier_det_phase_spectral_law_refuted_2026_06_12.txt`](../logs/runner-cache/frontier_det_phase_spectral_law_refuted_2026_06_12.txt)
**Status:** source proposal; independent audit required. Runner `PASS=9 FAIL=0`.

## Dependency Boundary

This note is a standalone finite free-sector spectral diagnostic. The runner
defines the `L = 3`, `tau = 0.35`, `T = 256` finite-DFT alias convention and
does not consume a prior determinant-phase spectral law.

## Findings

- **The domain is forced by rank arithmetic**: the 3×3 cross-block of a `K`-particle
  Slater projector has rank `≤ min(K, 9−K)`, so the det-phase is identically
  undefined at `K = 2` and `K = 7` (both gated as exclusion data); the sweep domain
  is `K ∈ [3,6]` (+ a second seed), with the rank floor clean (`min sv = 1.1×10⁻²`).
- **The order-3 candidate is refuted narrowly — and only it**: the sparse order-3 gap-sum
  alias set (3 distinct gaps → **7 of 256 bins**, the determinant-degree carrier)
  captures `0.33–0.85` of the increment spectral power, state-dependently — the
  order-3 law fails at the worst state (gated). **Higher orders are not refuted**:
  they are outside this runner, and the capture-vs-order curve remains the named
  follow-on. The full-support statement is a **finite-window DFT leakage
  statement** (the gaps sit off-grid — e.g. bin
  `42.78 → 43`; aliasing/binning convention stated), not exact spectral support. A
  gcd-style "predicted set" would have covered all bins and made the law vacuous —
  rejected in-runner.
- Amplitudes differ strongly between states (gated) — but at order 3 the
  frequencies-vs-amplitudes split has no adequate carrier. This note does not
  supply an analytic route to the deterministic phase; the integrated
  phase/winding object remains a named follow-on candidate.

## Scope

Free sector, `L = 3`, this period and alias map (`τ = 0.35`, `T = 256` — stated);
trajectories are realized-state data; the refutation and the capture spread are the
data. No new axiom/primitive/measure/weight; `r` untouched. The audit lane grades.
