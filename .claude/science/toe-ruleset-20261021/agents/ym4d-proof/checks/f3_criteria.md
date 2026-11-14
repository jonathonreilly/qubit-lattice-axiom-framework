# f3 criteria (written 2026-10-27 23:08 UTC [file mtime], before checks/f3_omega2_lattice.py)

Purpose. The Ω² (diamagnetic) channel of the one-loop coefficient on the lattice: a unit-charge complex lattice scalar,
Γ(A) = log det M_A, φ^*M_Aφ = Σ_{x,μ}|φ(x+e_μ) - e^{iA_{x,μ}}φ(x)|² + m²Σ|φ|². By L4a-Π (Γ is gauge invariant, B_4
symmetric), its marginal part is c_Γ(m)·Σ_p(dA)_p² with c_Γ := β[Γ]/2 (β[Σ_p(dA)²] = 2). Continuum heat kernel
(a_2 = (1/12)Ω², L4b): c_Γ(m) = (1/(48π²))log(1/m) + const + o(1). This sharpens L4b's c2(B) (Ω² slope 0.94-1.10).

Formula. β = Σ_zz_1z_2Π_12(z) = -∂_{k_1}∂_{k_2}F(0), F(k) = ∫_{BZ}d⁴q/(2π)⁴ g(q)g(q+k)(e^{i(q+k)_1} - e^{-iq_1})(e^{iq_2} -
e^{-i(q+k)_2}), g = 1/(ω + m²), ω = Σ_α(2 - 2cos q_α); the k-derivatives are taken analytically under the integral
(derived in FLOW.md §5.6).

Pre-registered criteria:
- (A) validation on the torus 4⁴, m² = 1: Π_12(z) from a central finite-difference Hessian of log det M_A (step 1e-4)
  against the torus momentum sum, for all z: max |difference| ≤ 1e-6. The analytic-derivative β on the torus momenta
  against Σ_zz_1z_2Π_12(z) from the finite-difference Π with z in centred torus coordinates is NOT required to match
  (wrap-around); informational only.
- (B) infinite-volume transversality: |F(0)| ≤ 1e-9 at m = 0.2 (the uncentred Π̂_12(0) vanishes).
- (C) slope: s(m_1, m_2) := (c_Γ(m_2) - c_Γ(m_1))/log(m_1/m_2) for m ∈ {0.4, 0.2, 0.1, 0.05}; at (0.1, 0.05),
  |s·48π² - 1| ≤ 0.02, and |s·48π² - 1| is non-increasing along the three pairs.
- (D) quadrature: c_Γ(0.05) with 40 and 56 mapped Gauss-Legendre points per dimension: |difference| ≤ 1e-5.

Outcome in checks/f3_out.txt, checks/f3_time.txt. A FAIL is reported as a FAIL.
