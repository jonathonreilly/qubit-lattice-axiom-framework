# ui55_1 — criteria (pre-registered BEFORE any ui55_1 script exists)

Owner file: UIR55.md (§2.2 Lemma P♮, §2.1 Finding 2.1, §3 Lemma SPLIT). Worker: claude-opus-5-5. Written 2026-10-29 (UTC).
Arithmetic: plain python `fractions.Fraction` only (exact rationals); no floats in any verdict; no numpy/BLAS. nice 10.

## Part A — the abstract fine/level split (finite dimensions, exact)
Data (fixed seed 5501, integers): fine space R^9, fine gauge R^3 with D_0 (9x3, full rank); level space R^5, level gauge
R^2 with D (5x2, full rank); ev (2x3). M := D·ev·D_0^+ + N(1 − D_0D_0^+) (N random 5x9), D_0^+ := (D_0^TD_0)^{-1}D_0^T.
𝒞 := R R^T + 1 (5x5, SPD). Π := 𝒞^{-1} − 𝒞^{-1}D(D^T𝒞^{-1}D)^{-1}D^T𝒞^{-1}. P_0 := 1 − D_0D_0^+. A := P_0 R_A P_0 (R_A SPD 9x9).
B := M^TΠM, H := A + B. U_0, U_n := integer bases of E_0 = ker D_0^T, E_n = ker D^T. For an operator X and basis U,
"det_U X" := det(U^T X U)/det(U^T U) (the determinant of the compression, basis-independent).
- A0: M D_0 = D ev (hypothesis realised).
- A1: Π D = 0 and B D_0 = 0.
- A2: H D_0 = 0 and A D_0 = 0.
- A3 (SPLIT): det_{U_0}H · det_{U_n}𝒞 = det_{U_0}A · det_{U_n}(𝒞 + M A_0^+ M^T), A_0^+ := U_0(U_0^TAU_0)^{-1}U_0^T.
- A4 (envelope = Woodbury): 𝔅 := Π − ΠMH^+M^TΠ, H^+ := U_0(U_0^THU_0)^{-1}U_0^T. (i) 𝔅D = 0; (ii) on E_n,
  [(U_n^TU_n)^{-1}U_n^T𝔅U_n]·[(U_n^TU_n)^{-1}U_n^T(𝒞 + MA_0^+M^T)U_n] = 1; (iii) for 3 random v, with x* := H^+M^TΠv,
  q(x*, v) = ½v^T𝔅v where q(x, v) := ½x^TAx + ½(v − Mx)^TΠ(v − Mx), and q(x* + δ, v) − q(x*, v) ≥ 0 for 3 random δ.
- A5 (fine Feynman form): det(A + D_0D_0^T) = det_{U_0}A · det(D_0^TD_0).
- A6 (level Feynman form): det(𝔅 + DD^T) = det_{U_n}𝔅 · det(D^TD), and det_{U_n}𝔅 · det_{U_n}(𝒞 + MA_0^+M^T) = 1.
Designed-FAIL controls (each must FIRE, i.e. the displayed equality must be FALSE):
- Ac1: B_bad := M^T𝒞^{-1}M: B_bad D_0 = 0 (FLOW's pre-K̄ IR term is not transverse).
- Ac2: A3 with the level-group factor det_{U_n}𝒞 omitted.
- Ac3: A5 with A replaced by A′ := A + E, E := e_1e_2^T + e_2e_1^T (symmetric, E D_0 ≠ 0).
PASS(A) iff A0-A6 all hold exactly AND Ac1-Ac3 all fire.

## Part B — Lemma P♮ on an actual lattice (2D analogue of S4′, exact)
2D periodic torus, fine side 6, L = 3, one step (ℓ = 3), level side 2. Fine 1-forms (72), level 1-forms (8); d, d_c forward
differences; ev(X) := fine root c_X = 3X + (1,1). S2′ root map: for level link (X, μ), average over y ∈ B(X) (9 points) and
the 2 coordinate orders σ of the line integral of A along P^σ(c_X → y) + S_y − P^σ(c_Y → y + 3e_μ) (S_y: 3 steps from y in
direction μ; P^σ: axial path moving first in σ_1, then in σ_2). h(A)(X) := avg_{σ,y}∫_{P^σ(c_X→y)}A; Q_str := avg_y∫_{S_y}A.
𝒞 := ½·1 (κ = 2; the one-step composite covariance is κ^{-1}·1). Π as in Part A with D := d_c (pseudo-inverse on mean-zero
level 0-forms). Δ_0 := d^Td (fine 0-forms), Δ_0^+ := (Δ_0 + J/36)^{-1} − J/36. P_L := dΔ_0^+d^T, P_T := 1 − P_L.
O := d^Td + dd^T + Q^TΠQ.
- B1: Q d = d_c ev.   B2: Q = Q_str − d_c∘h.
- B3: Q^TΠQ d = 0.   B4: P_L O P_T = 0 (no cross block).   B5: P_T(Q^TΠQ − Q_str^TΠQ_str)P_T = 0.
- B6: with G_T := (P_TOP_T + P_L)^{-1}P_T and G_L := dΔ_0^+Δ_0^+d^T: O·(G_T + G_L) = 1.
Designed-FAIL control: Bc: with Π replaced by 𝒞^{-1}, P_L O_bad P_T = 0 must be FALSE.
PASS(B) iff B1-B6 hold exactly AND Bc fires.

## Part C — the composite straight-average kernel (Finding 2.1)
- C1: as Laurent polynomials in z, K_3(z)·K_3(z³) = K_9(z), K_s(z) := s^{-1}(Σ_{y<s}z^y)(Σ_{j<s}z^j) (two-step telescoping of the
  one-step leg-direction kernel).
- C2: in the Part B lattice, the real-space weights of Q_str on a level link (X, μ) along the leg direction μ are the triangle
  filter (1, 2, 3, 2, 1)/3 (unit = one fine link) and along the transverse direction the box (1, 1, 1)/3 (product form).
Designed-FAIL control: Cc: C2's leg-direction weights equal the single box (1, 1, 1) (the form "ℓΠ_αD_ℓ(q_α)" of FLOW §24 (F2)
read with ONE Dirichlet factor in the leg direction) — must be FALSE.
PASS(C) iff C1, C2 hold AND Cc fires.

Overall PASS iff PASS(A), PASS(B), PASS(C). Each sub-verdict is printed; a crash is a FAIL. Outputs go to
checks/ui55_1_out.txt (unaltered stdout) and checks/ui55_1_err.txt (stderr + time/memory).
What this check can NOT decide: anything n-uniform; the analytic estimates of §3-§4; the identification of 𝔅 with the tree
Hessian beyond the quadratic (Gaussian) level (A4 is its zero-residual, quadratic instance only).
