# c31 criteria (written BEFORE checks/c31_linear.py; session 16, 2026-10-27, after RTARGET §38)

Purpose: instances for REVIEW_S15_CONVERGENCE fix 5 (Lemma E-low), for session-16 target B (the analytic
F-representative of the f_0 map, Lemma F-df_0), and the arithmetic of the NA-lev smallness. Not a proof of anything.
Two parts, each its own job (`python3 -I c31_linear.py E|F`), one job at a time, nice 10, BLAS/OMP/MKL threads 1.
No float tolerance is added to any inequality below; if one turns out to be needed, it goes into an addendum to THIS
file, written before the run that uses it.

Notation: c26's symbols (P_symbol with the Laplace G, nu_sym, r_from_b, Phi_f), d = 4, L = 3. For κ = (κ_0, …, κ_{k-1}):
κ := κ_{k-1}, κ̂ := max_i κ_{k-1}/κ_i, R̄ := 1 + κ̂/(L² - 1) + κ/9, **c_E := 2κ/(π²(κ + 4π²R̄))** (Lemma E-low).

## Part E: Lemma E-low (E_k(B_k) ≥ c_E||dB_k||²) and the NA-lev arithmetic
- **E1 (symbol level).** Cases (T, k, κ) = (16, 1, (1)), (16, 2, (1, 1)), (12, 3, (1, 1, 1)), (16, 2, (0.5, 2)). At every grid
  point p ≠ 0, with w_μ := 1/P̂_μ(p), A := W - (Wν)(Wν)^†/(ν^†Wν) (4 × 4, W = diag w), ψ := Σ|ν_μ|²: the per-mode ratio
  e(p) := (κ/2)·λ_2(A)/ψ (λ_2 the second-smallest eigenvalue; λ_1 = 0 with eigenvector ν), which is the exact minimum of
  (κ/2)min_tΣ_μw_μ|b̂_μ - ν_μt|² / |ν∧b̂|² over b̂ ∉ span(ν). **E1 PASS iff min_{p≠0} e(p) ≥ c_E in every case.** Print
  min e / c_E and the minimising p (informational).
- **E2 (chain level).** c26's Chain (LSMR) at (T, k, κ) = (3, 1, (1)), (2, 2, (1, 1)), (2, 2, (0.5, 2)). Data B_k: three
  random normal fields (fixed seed), and the minimising single mode of this torus: at the grid point p_min of the per-mode
  ratio e(p) on the T-grid, B_k(x)_μ := Re(b̂_μe^{ip_min·x}) with b̂ the λ_2-eigenvector of A (real at self-conjugate p).
  E_k is the chain energy at the LSMR minimiser; ||dB_k||² uses the coarse lattice d.
  - **V (validity):** LSMR normal-equation residual ≤ 1e-8 (relative) in every run.
  - **E2a:** every ratio E_k/||dB_k||² ≥ c_E.
  - **E2b (consistency):** for the single-mode datum, |E_k/||dB_k||² - e(p_min)| ≤ 1e-6·e(p_min).
- **E3 (arithmetic).** At κ ≡ 1, L = 3: |c_E - 0.004069| ≤ 5e-7. NA-lev smallness: the largest η̄ with
  (κ/2)L²·81·p_L·(e^{2η̄} - 1)² ≤ ½min(c_E, κ/4)·c_1, p_L := 5L - 4, c_1 := 1/(3.5·10⁶), lies in [1.85e-7, 1.95e-7], and
  η̄/(2L(L - 1)) (the background plaquette angle by the argued Stokes bound) lies in [1.5e-8, 1.65e-8].
- **PASS iff E1, V, E2a, E2b, E3.**

## Part F: the analytic F-representative of the f_0 map (Lemma F-df_0's algebra)
Cases (T, k, u) = (8, 1, (0,0,0,0)), (8, 1, (1,0,0,0)), (8, 2, (0,0,0,0)), (8, 2, (2,1,0,0)), κ ≡ 1, n = 3^k. The B_k-symbol of
f_0 at offset u: for each input direction v, r̂ := r_from_b(P, e_v, ν), and the plane-(a, b) output
B^v_{ab}(p) := n^{5-d}(-κ)(Φ_{ab,u}r̂_b - Φ_{ba,u}r̂_a) (c26 f_bloch's symbol). Representative: for α < β,
h_{αβ} := T_αE_{<α}B^β (a 6-vector of output planes), with E_{<α} the evaluation at p_1 = … = p_{α-1} = 0 (grid points)
and T_αg := (g - g|_{p_α=0})/ν_α. Evaluated at the grid points with every p_α ≠ 0 (the points p_α = 0 need the
derivative limit and are not tested; disclosed).
- **F0 (validity, the hypothesis used):** Σ_vν_vB^v = 0 at every grid point p ≠ 0: max error ≤ 1e-12·max|B|.
- **F1 (the factorisation identity):** at every tested point and every v, Σ_{α<β}h_{αβ}·(ν∧e_v)_{αβ} = B^v, with
  (ν∧e_v)_{αβ} = ν_αδ_{βv} - ν_βδ_{αv}: max error ≤ 1e-10·max|B|.
- F2 (informational): max over tested points of |h|/max|B|.
- **PASS iff F0, F1.**
