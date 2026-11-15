# c27 criteria (written 2026-10-27, BEFORE checks/c27_physgap.py; RTARGET §21)

Setting: one level, coarse units (ε = 1/n, ⟨A, A⟩ = ε^dΣ|A|², d with 1/ε, ∂_νA_μ = forward difference/ε), Q_str the
straight block average, h the S4' slice functional (as c24), F(A)(X, μ) := ε^{d-1}Σ_{z ∈ B(X), z_μ top layer} A_μ(z) (the
flux of A through the face from B(X) into B(X + e_μ)). Sizes: d = 4, T = 2, n = 3 (and n = 5 where noted); d = 2, T = 4,
n = 3, 5, 7; d = 3, T = 3, n = 3. Random Gaussian data, fixed seed. The proof (PROOF L5 [S12], Proposition PG) is for
d = 4; the identities E1-E3 hold in every d.
- **E1** For A_c := A - dΔ^{-1}d*A: max|d_c^*F(A_c)| ≤ 1e-10·max|F(A_c)|.
- **E2** ||Q_strA - F(A)||² ≤ 4Σ_μ||∂_μA_μ||² for random A, a smooth A (lowest Fourier modes) and an alternating A
  (ratio ≤ 1 in every case; n = 3 and 5 in d = 4).
- **E3** For random A ∈ H_0: inf_{λ∈Λ_res}||A + dλ||² = ||A_c||² + E(r, m), with r_X = ψ(c_X), m = Mψ, ψ = Δ^{-1}d*A and
  E(r, m) := min{||dφ||² : φ(c_X) = r_X, Mφ = m}, relative difference ≤ 1e-8. Also r - m = h(A_c) to 1e-10.
- **E4** C_3(n) := max_{s0} Σ_{k≠0}|φ_k(s0)|²/λ_k (3D Neumann cube, side n, lattice units) ≤ 14 for n = 2..24.
- **E5** The constants (d = 4): b_n := ||β||_∞ ≤ (π/2)^4 and C_β(n) := ||dβ||² ≤ 163 for odd n = 3..41; ||dγ||² ≤ 20ε²;
  ||dφ̃||² ≤ 22||d_cm||² and Σ_X|m_X - Mφ̃(X)|² ≤ 216||d_cm||² for random m (T = 2, 3; n = 3, 5).
- **E6** The line-trace bound, per block: ε²|h(A)(X)|² ≤ 8ε²||A||²_{B(X)} + 8C_3(n)ε||∇A||²_{B(X)} (block-internal
  differences), random and smooth A, d = 4, n = 3, 5 (ratio ≤ 1).
- **I1 (informational)** max over the tested A ∈ H_0 of inf_λ||A + dλ||²/(||dA||² + ||QA||²), against the proven
  constant 3.5·10⁶.
Budget: nice 10, BLAS threads 1, peak < 1.2 GB.
