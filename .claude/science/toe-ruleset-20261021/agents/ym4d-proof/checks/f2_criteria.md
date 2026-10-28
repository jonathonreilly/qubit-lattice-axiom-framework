# f2 criteria (written 2026-10-27 23:07 UTC [file mtime], before checks/f2_e2_soft.py)

Purpose. The E² channel of the one-loop computation (L4b: the spin term of the background-field operator contributes
through tr(G E G E); for constant E its coefficient is (1/V)tr G², whose UV log coefficient is 1/(8π²) per unit log of
the UV/IR ratio). Here the IR regulator is the soft block kernel itself (no mass): the claim tested is that the soft
kernel acts as an IR regulator at the block scale that does not change the universal log coefficient, for any κ
(scheme dependence sits in the constant). A scalar toy: this does not test the gauge structure (f3, f1 do parts of
that).

Object. Real scalar on the fine 4D lattice, D = -Δ (massless), straight block average Q (block side ℓ odd, rows ℓ^{-4}
on each block), kernel κ|Qφ|², κ = κ_cℓ² (κ_c fixed in coarse units). G := (D + κQ^TQ)^{-1}, τ(ℓ, κ_c) := (1/V_f)tr G²
(infinite volume: coarse-BZ integral of the per-P alias trace; Sherman-Morrison per P; κ_c = ∞ is the hard constraint).

Pre-registered criteria:
- (A) validation: fine torus 6⁴ (ℓ = 3, coarse side 2), κ_c = 1: dense τ vs the per-P alias formula on the torus
  momenta: relative difference ≤ 1e-10. Sherman-Morrison vs direct per-P inversion at 5 random P (ℓ = 3): ≤ 1e-10.
- (E) two-step chain = one big step (d = 2 dense test, fine torus 18², L = 3 twice): the φ_0-marginal covariance of
  the joint Gaussian (levels 0, 1; level 2 pinned to 0) equals (D + κ_eff(Q'Q)^T(Q'Q))^{-1}, κ_eff = κ_0κ_1/(κ_0 +
  κ_1L^{-2}): max entry difference ≤ 1e-12.
- (B) quadrature: τ(7, 1) with coarse midpoint grids n_P = 8 and 12: |difference| ≤ 2e-4.
- (C) universality: slopes σ(ℓ_1, ℓ_2) := (τ(ℓ_2) - τ(ℓ_1))/log(ℓ_2/ℓ_1) for consecutive odd ℓ from 3 to 15 (n_P = 8);
  at the largest pair (13, 15), |σ·8π² - 1| ≤ 0.03 for each κ_c ∈ {0.25, 1, 4, ∞}.
- (D) κ-independence: at (13, 15), max_κ σ - min_κ σ ≤ 0.03/(8π²). Informational: the constants
  τ(15, κ_c) - log(15)/(8π²) for the four κ_c.

Outcome in checks/f2_out.txt, checks/f2_time.txt. A FAIL is reported as a FAIL.
