# c35 criteria (written BEFORE checks/c35_n5bg.py; session 19, 2026-10-27, after RTARGET §42 and before any PROOF.md [S19] text)

Purpose: (A) the background dependence of the gauge-fixed level-0 covariance on a small SU(2) torus; (B) the
Dirichlet-compression random-walk expansion (truncation error versus walk length, s-weakening, square root); (C) the
level-0 constants behind target C (exact slice vector, exact weighted row sums of the trivial operator, measured gap
and decay). Parts are separate jobs (`python3 c35_n5bg.py A|B|C`), one job at a time, nice 10, OPENBLAS/OMP/MKL/vecLib
threads 1, no `timeout`, peak RSS < 1.2 GB. No tolerance beyond those written here. If a criterion fails it is reported
as failed; no criterion is edited after the script is written.

Common objects (d = 4, L = 3 unless stated): the slice h_U(A)(X) = avg_{σ, y∈B(X)} ℓ_{P^σ(c_X→y)}(A); the block transport
mean M_Uλ(X) = avg_{σ,y} Ad(T^σ(c_X ← y))λ(y); (D_Uλ)_b = Ad(U_b)λ(x + e_μ) - λ(x); P_res^U the orthogonal projector onto
{λ : λ(c_X) = 0, M_Uλ = 0}; Q_UA(c) = avg_{σ,y} ℓ_{T^σ_y}(A) over the S4' contours T^σ_y of the coarse link c (the covariant
linearised S4' average); Π_U = 1 - h_U^T(h_Uh_U^T)^{-1}h_U. ℓ_P(A) = Σ_jAd(T_{j-1})ã_j as in NA-FP.

## Part A: SU(2) on (Z/6)⁴ (T = 2), a MODEL level-0 operator
Õ(U) := Π_U(H_W(U) + κQ_U^TQ_U + D_UP_res^UD_U^T)Π_U + (1 - Π_U), κ = 1, H_W(U) the exact Hessian of
A ↦ Σ_p Re tr(1 - (e^AU)_p) at A = 0 (left trivialisation, basis τ_a = iσ_a/√2). This is a MODEL: κ|Q_UA|² replaces the
full soft Hessian (no W_0 polar part, no NA-alg corrections, no defect). Background U_t = exp(t·a), a_b iid Gaussian in
su(2) (seed 0), normalised to max_b|a_b| = 1; t ∈ {0, 0.001, 0.003, 0.01, 0.03, 0.1, 0.3}. b_0 = ((0,0,0,0), μ = 1).
C(U) := Õ(U)^{-1} - (1 - Π_U), columns at b_0 by MINRES (relative residual ≤ 1e-11); p_t(r) := max over links b' at torus
ℓ¹ distance r from b_0 of the 3×3 operator norm of C(U_t)(b', b_0).
- **A0 (validation):** (i) H_W against central finite differences of the plaquette action (step 1e-4) on 3 random
  plaquettes at t = 0.3: max abs error ≤ 1e-5·max|H|; (ii) NA-FP (i) h_U(D_Uλ) = M_Uλ - λ(c) at t = 0.3, random λ: relative
  error ≤ 1e-12; (iii) ⟨v, Õw⟩ = ⟨w, Õv⟩ for random v, w at t = 0.3: relative ≤ 1e-12.
- **A1 (gauge covariance, N5bg-F3):** g Haar-random (seed 1), t = 0.1: ||C(gU)R_ge - R_gC(U)e|| ≤ 1e-7·||C(U)e|| for e the three
  colour unit vectors at b_0 ((R_gA)_b = Ad(g(x))A_b); and |λ_min(Õ(gU)) - λ_min(Õ(U))| ≤ 1e-7·λ_min(Õ(U)).
- **A2 (trivial background):** λ_min(Õ(1)) > 0 and equals the one-colour abelian λ_min to relative 1e-7.
- **A3 (analytic, linear response):** Δ_t(r) := max_{d(b',b_0)=r}||C(U_t)(b', b_0) - C(1)(b', b_0)||. For every r with
  Δ_{0.001}(r) ≥ 1e-6·p_0(0): 2 ≤ Δ_{0.003}(r)/Δ_{0.001}(r) ≤ 4.5.
- **A4 (rate close to trivial):** for t ∈ {0.001, 0.003, 0.01}, the least-squares slope s_t of log p_t(r) on r = 1..8 obeys
  s_t ≤ 0.8·s_0 (both negative; i.e. the decay rate is at least 80% of the trivial one).
- **A5 (informational):** λ_min(Õ(U_t)) and max_p|log U_p| for every t; ||Õ(U_t) - Õ(1)||_op (power iteration) / t; p_t(r).
- PASS iff A0-A4.

## Part B: random-walk expansion, abelian, d = 2, L = 3, coarse torus T = 12 (36² sites, 2592 links)
Õ := Π(d_1^Td_1 + κQ^TQ + d_0P_resd_0^T)Π + (1 - Π), κ = 1, the d = 2 S4' objects (2 coordinate orders). Partitions into
R×R boxes of blocks, R ∈ {1, 2, 3}; Ω_□ = blocks at coarse ℓ^∞ torus distance ≤ R from □; G_□ := (1_ΩÕ1_Ω)^{-1};
P := Σ_□G_□1_□; R := -Σ_□1_{Ω^c}ÕG_□1_□ (dense). q := max row sum of |R|; e_n := max_{x,y}|Õ^{-1} - Σ_{j≤n}PR^j|.
- **B0 (precondition):** λ_min(Õ) > 0.
- **B1:** max|ÕP - (1 - R)| ≤ 1e-10 for each R.
- **B2:** for each R with q < 1 and every n ≤ n_max (n_max: the first n with N_0(|P|)M_0(|R|)q^n/(1 - q) < 1e-13, capped at
  200): e_n ≤ (1 + 1e-9)·N_0(|P|)M_0(|R|)q^n/(1 - q) + 1e-12, M_0 the max entry, N_0 the max row sum.
- **B3:** for each R with q < 1: e_{n_max} ≤ 1e-10.
- **B4 (power):** q(3) < q(2) < q(1) and q(3) < 1.
- **B5 (s-weakening):** 𝒴 := a random half of the boxes (seed 0); s_□ = 0 off 𝒴 and s_□ = 0.5 + 0.5i on 𝒴;
  C(s) := P(1 - Σ_□s_□R_□)^{-1}; for every □' ∉ 𝒴: max|C(s)1_{□'} - G_{□'}1_{□'}| ≤ 1e-12 (for every R with q < 1).
- **B6 (square root, R = 2):** with u = √λ_0·tan θ (λ_0 = √(λ_minλ_max)) and 200-point Gauss-Legendre in θ ∈ (0, π/2):
  (i) the quadrature of (2/π)∫_0^∞(Õ + u²)^{-1}du agrees with Õ^{-1/2} (eigendecomposition) to 1e-6 relative (max entry);
  (ii) the same quadrature applied to the walk series of (Õ + u²)^{-1} (summed until the bound of B2 is < 1e-14) agrees
  with the quadrature of the exact resolvents to 1e-10 relative.
- **B7 (informational):** the proven ε_R of Theorem RW with the measured S_m, γ', m (as printed) versus q.
- PASS iff B0-B6.

## Part C: level-0 constants (d = 4, L = 3, κ = 1, trivial background, one colour)
- **C1 (exact slice vector):** w computed in exact rational arithmetic; print ||w||², Σ|w|, max|w|, and
  ν_w := max|w|·Σ|w|/||w||² (= N_0(|1 - Π|)). Criterion: ν_w ≤ 128L²/(L - 1) and max|w|Σ|w|/||w||² reproduces the float
  value of the rows of 1 - Π to 1e-12.
- **C2 (exact weighted row sums):** the rows of Õ_0 = Π(d_1^Td_1 + κQ^TQ + d_0P_resd_0^T)Π + (1 - Π) for the 324 links
  based in one block, computed by matvecs on the coarse torus T = 3, with Z⁴ base-point distances (lifting the coarse
  shift s ∈ {-1, 0, 1}⁴); D^num(m) := max_bΣ_{b'}|Õ_0(b, b')|(e^{md} - 1) and N^num(m) likewise, each multiplied by
  (1 + 1e-9). Criterion: D^num(m) ≤ 𝔇_0(m) (N5-triv's product-rule bound at i = 0 with n_Π := 1 + 128L²/(L - 1),
  S_O = 24 + 16κp_L + 32, E_O(m) = 24(e^{2m} - 1) + (e^{mp_L} - 1)(16κp_L + 32)) for m ∈ {1e-12, 1e-9, 1e-6, 1e-3}; also
  (validation) the computed rows are symmetric (Õ_0(b, b') = Õ_0(b', b) on the torus) to 1e-12, and range ≤ 1 block.
  Print m_cov^num := the largest m (bisection) with D^num(m) ≤ γ_0/2, γ_0 := c_1·min(1/2, κ/2)/L² (N5-coer at i = 0),
  and the N5-triv value m_cov (from 𝔇_0).
- **C3 (measured gap, Bloch):** Õ_0(K) := Σ_sÕ_{0,s}e^{iK·s} (324×324); validation: for 3 random K on the (2π/3)Z⁴ grid
  the periodic extension of an eigenvector v of Õ_0(K) satisfies ||Õ_0ṽ - λṽ|| ≤ 1e-10||ṽ|| on the T = 3 torus. γ_meas :=
  min over K ∈ (2π/8)Z⁴ of λ_min(Õ_0(K)); the same for Õ^LB (d_1^Td_1 replaced by 2c_E·d_1^Td_1, c_E = 0.004069, the
  Lemma E-low constant at κ ≡ 1, which bounds every level i from below). Criterion (consistency): γ_meas ≥ γ_0 and
  γ_meas^LB ≥ 1.29·10⁻¹⁰ (N5-triv's γ_i). Print both, their argmin, and the ratio to the proven values.
- **C4 (measured decay):** T = 5 torus (15⁴ sites), trivial background, column C_0(·, b_0) = Õ_0^{-1}e_{b_0} - (1 - Π)e_{b_0} by CG
  (relative residual ≤ 1e-12); p(r) := max_{d=r}|C_0(b', b_0)|; m_meas := minus the least-squares slope of log p(r) on
  r = 4..20. Criterion: m_meas ≥ m_cov^num (consistency). Print p(r).
- PASS iff C1-C4.
