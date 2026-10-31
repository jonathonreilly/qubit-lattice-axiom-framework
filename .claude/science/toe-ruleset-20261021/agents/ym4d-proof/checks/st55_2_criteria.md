# st55_2 — pre-registered criteria (written before any st55_2 script exists)

Object: STEP55 §3 — the one-step (V fixed) tree-level conditional Hessian H_cond := Hess[S_W + κ_0Σ_cφ̂_c] at LCONV55's stripe,
compared with the bare Hessian Hess S_W (the joint chain's Hessian along following directions, by Lemma FOL). SU(2), d = 4,
L = 3, fine torus side 6 (coarse side 2), V ≡ 1 (the stripe's own following field), stripe S(3, β): direction-1 links
U_1(x) = exp(i a(x_0 mod 3) σ_3) with a = (β, 0, −β), every other link 1, β = 2 arctan τ, τ ∈ {1/50, 1/20, 1/10} and the
control τ = 0. Exact rational quaternions throughout (cos β = (1−τ²)/(1+τ²), sin β = 2τ/(1+τ²)); no floats in any verdict.
Normalisation: S_W = Σ_p Re tr(1 − U_p), φ̂_c = Re tr(W_0⁻¹M̄_c) − Re tr(V_c⁻¹M̄_c) (= Nψ), left-trivialised variations
U_b → e^{tA_b}U_b, A_b = i v_b·σ, Euclidean norm Σ_b|v_b|² (v_b ∈ R³).

Subspaces tested: S_dep = fields depending only on (x_i mod 3)_{i∈dep}, all four directions, dep = {0} (36 dims) and dep = {0,1}
(108 dims); H_red(dep) := the part of S_dep orthogonal to every gauge direction D_Uλ with λ in the same class (by the averaging
argument of STEP55 §3.5 this is exactly S_dep ∩ (G_fl-horizontal)). The S4′ kernel Hessian is computed exactly from the contour
derivative: at zero mismatch Hess φ̂_c[v] = 2|a′_c(v)|²/r_c (r_c the scalar M̄_c, a′_c the vector part of dM̄_c/dt), and by coarse
translation covariance the 16 coarse links of one direction contribute equally.

Gates (PASS required):
- G0  zero mismatch at the stripe: M̄_(0,μ) is a positive scalar for every μ; for the stripe direction r = (1 + 2cos3β)/3 exactly
      (= 2733299/3090903 at τ = 1/10, LCONV55 C1 / Codex R4); for the others r = 1.
- G1  reproduction of Codex R2 (transplanted to the torus): along v_C (v_0 ≡ (1,1,1) on all direction-0 links, v_1 = (4τ, −4τ, 0)
      on direction-1 links with x_0 ≡ 1 mod 3, others 0) the bare Hessian equals −27648τ²(2 + s⁻²), s = 1 + τ² (= 2 × 432 cells ×
      Codex's per-cell −32τ²(2 + s⁻²)), and v_C ∈ H_red({0}) exactly.
- G2  bare negativity: the bare Hessian on H_red({0}) is NOT positive semidefinite at τ ∈ {1/50, 1/20, 1/10} (v_C certifies it).
- G3  one-step positivity: H_cond with κ_0 = 1 is positive definite on H_red({0}) and on H_red({0,1}) at τ = 1/50 and τ = 1/20.
      Prediction: PASS. A FAIL would mean the kernel does not pin the stripe's negative directions at these sizes (a first-class
      negative result, reported as such).
Report (no prediction made): H_cond at τ = 1/10 (PD or not on each subspace); certified lower bounds on the minimum Rayleigh
quotient of H_cond on H_red (largest grid value λ with H_cond − λ·I PD on H_red, grid step 1/1000) for each τ; the
per-direction kernel weights |a′|² on v_C.

Controls (each must fire):
- C1 (designed FAIL) κ_0 = 1/10 at τ = 1/20: H_cond NOT positive semidefinite on H_red({0}) (prediction: along v_C the kernel
      Rayleigh quotient ≈ 2κ_0/9 = 0.022 is below the bare deficit ≈ 0.053).
- C2 (trivial background) τ = 0: the bare Hessian is PSD on H_red({0}) with a non-trivial kernel (the constant holonomies), and
      H_cond (κ_0 = 1) is PD there (the one-step gap at the trivial background).
Overall PASS: G0-G3 PASS and C1, C2 fire as designed. Nothing here bears on the full space (only on S_dep); the full-space
statement is STEP55 Theorem 1S-0 (N5-sf0 (b)).
