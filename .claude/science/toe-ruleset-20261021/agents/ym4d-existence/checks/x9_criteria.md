# x9 criteria (pre-registered; written 2026-10-28 ~03:46 UTC, after EXISTENCE §19.0 and before any x9 script)

Model (both parts): the Gaussian part of the simplest class member (depth 0, Wilson action at weak coupling, one colour
of the abelianised quadratic form): free lattice Maxwell field on the periodic torus T⁴, gauge-invariant observables only.
Curvature F_12(x) = forward-difference curl of A in the (1,2) plane at x. Correlator along the time axis:
  G_T(d) := Cov(F_12(x), F_12(x + d e_0)) = T^{-4} Σ_{k ≠ 0} cos(k_0 d)(k̂_1² + k̂_2²)/k̂²,  k̂_μ² = 4 sin²(k_μ/2)
(gauge-independent; the k = 0 term has zero numerator). Plaquette energy Φ := ½F_12²; Wick: Cov(Φ_x, Φ_y) = ½G².
Second difference (the RP form of D := Φ - τ_hΦ across a link-reflection plane at separation d = 2t + 1):
  A_T(d, h) := ½[G_T(d)² - 2G_T(d + h)² + G_T(d + 2h)²]   (SU(N): multiply by (N² - 1) and the colour normalisation).

## A (exact; load-bearing only for the explicit value in §19 T29; positivity there is proven analytically)
- A0: G_T(d) > 0 for d = 1..8, T ∈ {16, 24, 32, 48}.  FAIL if any G_T(d) ≤ 0.
- A1: A_T(d, h) > 0 for d ∈ {1, 3, 5}, h ∈ {1, 2}, T ∈ {16, 24, 32, 48}.  FAIL if any ≤ 0.
- A2 (box convergence): |A_32(d, 1) - A_48(d, 1)| / A_48(d, 1) < 1e-2 for d ∈ {1, 3}.  FAIL otherwise.
- A3 (independent formula check): on 4⁴, G from a dense pseudo-inverse of the lattice Maxwell operator (curl^T curl on the
  1024 link variables, applied to the curvature functionals) agrees with the momentum formula to < 1e-10 for d = 0..3.
  FAIL otherwise.
- A4 (informational): log-convexity G(d)G(d + 2) ≥ G(d + 1)² at T = 48, d = 1..6 (an RP consequence); report decay
  exponent of G(d) for d = 2..8 at T = 48.
- Report: A_48(1, 1), A_48(3, 1) as the explicit leading coefficients.

## B (exact Gaussian decomposition; INFORMATIONAL, non-load-bearing)
σ-algebra 𝔅_ℓ := the Fourier modes with |k_μ| < π/ℓ for all μ (a sharp low-momentum σ-algebra, NOT the soft chain's
coarse field). The field splits into independent low and high parts, G = G_l + G_h, and exactly
  Cov(Φ_x, Φ_y) = [½G_h² + G_lG_h] (= E Cov(· | 𝔅_ℓ)) + [½G_l²] (= Cov(E[Φ_x|𝔅_ℓ], E[Φ_y|𝔅_ℓ])).
- B1: report, at T = 64 and ℓ ∈ {4, 8, 16}, V_l := Var(F_12^{low}) = G_l(0), the coarse-mediated term ½G_l(1)², and its ratio
  to ½G(1)²; the expected (dimension-count) scaling is V_l ∝ ℓ^{-4}, coarse term ∝ ℓ^{-8}. Informational: fitted exponent of
  V_l between ℓ = 8 and 16 within [-4.5, -3.5] is "consistent"; otherwise "not consistent" (reported, no FAIL).
- B2: the same for the second-difference combination (d = 1, h = 1): coarse part ½[G_l(1)² - 2G_l(2)² + G_l(3)²] vs A(1, 1).
- The exact identity in B is checked numerically (sum of the two parts = ½G(1)² to < 1e-12).

Run rules: under the numeric lock (mkdir; rmdir exactly once; no trap), nice 10, BLAS/OMP threads 1, python3 without -I,
no `timeout`, load < 8 at start. Expected wall time < 10 min, memory < 1 GB.
