# c26 criteria (written 2026-10-27, BEFORE checks/c26_led.py; RTARGET §20)

Setting: c23's abelian linearised soft chain (Setting SC; S4' root-based one-step Q, L = 3), with chain weights κ_i
(rows of the i-th residual scaled by √κ_i). The claims under test (PROOF L5 [S12]):
- **IT-str**: the composite of m one-step straight averages is the direct straight average of block side L^m.
- **LED-dual**: at the minimiser, r := r_{k-1} is co-closed with zero mean, and it is the minimiser over co-closed
  zero-mean coarse 1-forms of ½⟨r, Pr⟩ + ⟨r, B_k⟩, with P = Σ_{m=0}^{k-1}(κ_{k-1}/κ_{k-1-m})Q_str^m Q_str^{mT} + κ_{k-1}G_k,
  G_k = Q_str^kΔ^{-1}Q_str^{kT}; and E_k = (κ_{k-1}/2)⟨r, Pr⟩; and dB_0 = dΔ^{-1}J_0 with J_0 = -κ_{k-1}Q_str^{kT}r.
- **LED-symb**: P is diagonal in the components with the Poisson (alias) symbol
  P̂_μ(p) = Σ_m(κ_{k-1}/κ_{k-1-m})n_m^{2-d}Σ_{K∈(Z/n_m)^d}|W_{n_m,μ}(p+2πK)|² + κ_{k-1}n^{2-d}Σ_K|W_{n,μ}(p+2πK)|²/φ_f((p+2πK)/n),
  n_m = L^m, n = L^k, W_{n,μ}(θ) = Π_αD_n(θ_α)·D_n(θ_μ), D_n(θ) = n^{-1}Σ_{j<n}e^{-iθj/n}, φ_f(q) = Σ_α4sin²(q_α/2);
  r̂ = -P̂^{-1}(b̂ - νt) with t fixing the coarse divergence to zero; and the Bloch formula for f_0 = L^{2k}dB_0 at each
  fine offset.

**Part A (exact identities; d = 2, T = 5, k = 1, 2, 3 with κ = (1,1,1) and κ = (0.5, 2, 1); d = 3, T = 3, k = 1; d = 4,
T = 3, k = 1; d = 4, T = 2, k = 2 if it runs within the memory budget).** Random Gaussian B_k.
- **V1** LSMR normal-equation residual ≤ 1e-8 at every size.
- **Q1** max|r_LSMR - r_symb|/max|r_LSMR| ≤ 1e-6 at every size (r_symb from the alias/Laplace symbol formula).
- **Q2** |E_LSMR - (κ_{k-1}/2)⟨r_symb, P r_symb⟩|/E_LSMR ≤ 1e-6 (P applied through its symbol).
- **Q3** max|d*r_LSMR|/max|r_LSMR| ≤ 1e-6 and |mean r_LSMR| ≤ 1e-6·max|r_LSMR|.
- **Q4** the fine curvature: max|f_LSMR - f_Bloch|/max|f_LSMR| ≤ 1e-6, f_Bloch from the Bloch/Laplace formula
  (d = 4, T = 3, k = 1 and d = 2, T = 5, k = 2).
- **V2** the Laplace-integral form of the alias sums agrees with the direct alias sums to 1e-9 relative (wherever
  both are computed).
**Part B (informational support; d = 4, L = 3, κ_i ≡ κ ∈ {1} for k = 1..6, plus κ ∈ {0.25, 4} for k = 1..5; coarse
grid T = 16, plus T = 12 and 20 at κ = 1, k ≤ 5).** N_r(k) := the ∞→∞ norm of the periodised kernel of dB_k ↦ r_{k-1}
(max over output components of Σ_X Σ_planes |K|); N_f(k) := the max over sampled fine offsets (corner, centre, 3 fixed
pseudo-random) and planes of the same norm for dB_k ↦ f_0.
- **Q5 (pre-registered)** at κ = 1, T = 16: N_r(6) ≤ 1.25·max_{k≤3}N_r(k).
- **Q6 (pre-registered)** at κ = 1, T = 16: N_f(6) ≤ 1.25·max_{k≤3}N_f(k).
- **I1** N_r, N_f vs k at the other κ and T; the log-slope of max_component|K_r(x e_1)| between x = 3 and 7.
Part B cannot prove uniformity; it can only fail to see growth. Budget: nice 10, BLAS threads 1, peak < 1.2 GB.

## Addendum (written 2026-10-27 after the Part A and Part B runs, BEFORE Part C was coded or run)
Part B's N_f grows with T (4.5, 5.5, 6.3 at T = 12, 16, 20; k-stable at each T). The measured kernel is that of the
formula's extension to ALL 2-forms F. On non-closed F this extension contains the degree-0 projector
ν∧(ν̄⌟·)/ψ (a Calderón-Zygmund kernel ~ |x|^{-4}, not summable). The bound needed is on closed F only. There the
representative 𝒦̂_u + Π_coex, with Π_coex := C^†C/ψ (C the coarse lattice d on 2-forms, ψ = Σ|ν|²), agrees with
𝒦̂_u, because Π_coex F = 0 when dF = 0.
**Part C.** N_f^rep(k, T) := the same norm for the representative 𝒦̂_u + Π_coex, at κ = 1, k = 1..5 (6 at T = 16),
T ∈ {12, 16, 20, 24}.
- **V3** on closed F (dB_k of random B_k, d = 4, T = 3, k = 1, and T = 2, k = 2), the representative reproduces the
  LSMR f_0 to 1e-10 relative. This uses Part A's LSMR runs again.
- **Q7 (pre-registered)** N_f^rep(T = 24) ≤ 1.1·N_f^rep(T = 12) at k = 1..5, and N_f^rep(k = 6, T = 16) ≤
  1.25·max_{k≤3}N_f^rep(k, T = 16).
Part B's Q6 PASSED as written, but it does not test what the proof needs. That limitation is recorded; Q6 is not edited.
