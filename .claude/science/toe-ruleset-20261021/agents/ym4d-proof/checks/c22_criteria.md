# c22 criteria (written BEFORE c22_soft_su2_4d.py; session 10, 2026-10-27)

Purpose: a non-abelian SU(2), d = 4 instance for Target B (RTARGET §13): the one-step soft S4' minimiser on a small
torus. It measures the quantities the B proofs use: (1) the Noether identity "coarse covariant divergence of the soft
residual = 0 at critical points" (the input of Lemma J-str), (2) the absence of S4' axial-leg (funnel) concentration in
the soft current at the minimiser (the conclusion of J-str), (3) how far the non-abelian minimiser's curvature sup and
sub-block oscillation are from the linear regime (the B-NA perturbation claim). Instances only; not a proof.

Model. L = 3, fine torus 9⁴ (coarse 3⁴), SU(2) links as unit quaternions. Blocks B(X) = 3X + {0, 1, 2}⁴, roots
c_X = 3X + (1, 1, 1, 1). For a coarse link c = (X, μ): the 24 · 81 S4' contours T^σ_y = P^σ(c_X → y)·S_y·
P^σ(c_Y → y + 3e_μ)^{-1} (P^σ complete-axial in the coordinate order σ; S_y three straight steps), M̄_c := their mean
(a quaternion of norm ≤ 1). Energy (normalised kernel, tree level, κ = 1):
  E(U) = Σ_p (1 - Re U_p) + κ Σ_c (|M̄_c| - ⟨V_c, M̄_c⟩)   (⟨,⟩ the R⁴ inner product; this is N^{-1}[Σσ(M̄) - Re tr V^{-1}M̄]
  for SU(2) up to the factor 1, i.e. the normalised soft kernel's tree-level exponent).
Coarse data V_t = exp(t·X) with X a fixed random smooth su(2) coarse field (lowest Fourier modes on 3⁴, fixed seed).
Minimisation: Riemannian gradient descent with Barzilai-Borwein steps from the start configuration U^0 (links on the
straight segments from c_X to c_Y set to V_c^{1/3}, all others 1), stopped when the gradient norm ≤ 1e-7·(initial
gradient norm) or at 6000 iterations (then the run is flagged NOT CONVERGED).
Runs: t ∈ {0.02, 0.1, 0.2, 0.4}; t_ref := 0.02 serves as the linear reference.

Measured quantities (at the minimiser unless stated).
- G^V_c ∈ R³: the left Lie derivative of E in V_c. D(X) := Σ_{c starts at X} G^V_c - Σ_{c ends at X} Ad(V_c^{-1})G^V_c
  (the coarse gauge derivative; by gauge invariance it equals minus the fine root-gauge derivative of the soft term).
  N1 := max_X|D(X)| / max_c|G^V_c|.
- J(b) ∈ R³: the fine Lie gradient of the soft term at link b. Axial set A := the 8·81 links joining a root c_X to
  c_X ± e_ρ. R_ax(J) := mean_{b∈A}|J(b)| / mean_{b∉A}|J(b)|.
  Linear (abelian, componentwise) comparison operators on a coarse R³-valued field r: Q_root^T r (all contour links,
  signed weights 1/1944 per contour occurrence) and Q_str^T r (the straight legs S_y only, weight 1/81 per occurrence).
  r_min := (G^V_c) at the minimiser; r_ctrl := iid N(0, 1) per component and coarse link (fixed seed).
- Curvature in coarse units: a_p := the half-angle log vector of U_p (|a_p| ∈ [0, π]); S := 9·max_p|a_p|.
  ε_3(Q) per block Q: plaquettes with all corners within sup-distance 2 of c_X, logs transported to c_X along the
  complete-axial path (order 1, 2, 3, 4); ε_3 := max_p |ã_p - ã_{(c_X; μν(p))}|. O := 9·mean_Q ε_3(Q).
- Informational: mean ε_V (|log(V_cS_c^{-1})|, S_c the straight transporter), mean soft residual |log(V_c^{-1}M̄_c/|M̄_c|)|,
  energy, iterations, gradient norms.

Criteria.
- V1 (validity, convergence): every run CONVERGED.
- V2 (validity, control power for Q2): R_ax(Q_root^T r_ctrl) ≥ 1.5·R_ax(Q_str^T r_ctrl).
- V3 (validity, control for Q1): at the start configuration U^0 of the t = 0.2 run, N1 ≥ 1e-2.
- Q1 (Noether identity at the minimiser): N1 ≤ 1e-4 in every run.
- Q2 (no funnel concentration, J-str): at t ∈ {0.02, 0.1, 0.2}: R_ax(J) ≤ 1.25·R_ax(Q_str^T r_min) + 0.25.
- Q3 (non-abelian perturbation): with dev_q(t) := |(q(t)/t)/(q(t_ref)/t_ref) - 1| for q ∈ {S, O}:
  dev_S(0.1) ≤ 0.3 and dev_O(0.1) ≤ 0.3; and dev_S(0.2) ≥ dev_S(0.1), dev_O(0.2) ≥ dev_O(0.1) (the deviation grows away
  from the linear regime). t = 0.4 is informational.
Result: VALID iff V1-V3 hold; then Q1-Q3 are the findings (each PASS/FAIL reported; a FAIL is an outcome).
Resource rules: one job, nice 10, OPENBLAS/OMP/MKL threads = 1, load < 8 and ≥ 25% free memory before start; peak
memory < 2 GB and time reported. A pre-run smoke test (one energy/gradient evaluation, finite-difference gradient check,
timing) is allowed and is disclosed; it does not change any criterion. No criterion is edited after the run.
