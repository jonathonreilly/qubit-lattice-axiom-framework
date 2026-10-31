# f10 criteria (lane C, session 7) — written before any f10 script

Purpose: numerical checks of the session-7 PRE-STATED items of FLOW.md §50: (P2) Lemma FP-exact and (P3) Theorem V-heat.
Rules: NUMERIC LOCK, nice 10, BLAS threads = 1, PYTHONDONTWRITEBYTECODE=1, plain python3, no `timeout`; job < 20 min,
peak < 1 GB. f9_root_sector.py is imported read-only (its builder `build_su2`, `theta_landau`, `adinv`, `j`) for the
operator-identity part only. A verdict line PASSes when its stated inequality holds; controls PASS when they FAIL as
required. Outcomes are recorded as they come; no criterion is changed after the script exists (amendments, if any, are
appended and labelled POST-HOC).

## Part A: Lemma FP-exact (P2), charge-1 complex link field on 2D tori, realified
Setting: torus (9, 9), L = 3 (one level, ℓ = 3, 9 blocks c_X + {−1, 0, 1}²), Landau gauge with seam (quantised flux k
quanta, f = 2πk/81), NA-FP conventions: (D_Uλ)_b = U_bλ(y) − λ(x) for b = (x → y); h_U(A)(X) = avg over the 2 axial orders σ
and y ∈ B(X) of ℓ_{P^σ(c_X→y)}(A); M_Uλ(X) = avg_{σ,y}T^σ(c_X ← y)λ(y); Λ' = {λ(c_X) = 0}; Λ_res = Λ' ∩ ker M_U; P_res its
projector; χΓ := (h_UD_U, P_resD_U^*D_U) on Λ'. Q := P_{S_0}BP_{S_0} with B := c_U^*c_U + 0.3·1 (c_U the covariant plaquette
sum; any positive B is admissible for the lemma, which is linear algebra), S_0 = (D_UΛ')^⊥. Cases k = 1 and k = 3.
- A0 (implementation of NA-FP (i)): max|h_U(D_Uλ) − (M_Uλ − λ(c))| ≤ 1e-12 for 3 random λ.
- A1 (admissibility): σ_min(χΓ) ≥ 1e-6.
- A2 (the identity, no constant): |LHS − RHS| ≤ 1e-8·(1 + |RHS|), LHS := ½log det(ΠOΠ|_{ker h}) + ½log det(hh^*) − log|det χΓ|,
  RHS := ½log det_{S_0}Q − ½log det Δ' (all real determinants of the realified operators; O := Q + D_UP_resD_U^*).
- A3 (factorisation): |log|det χΓ| − log det(M_U|_{Λ'⊖Λ_res}) − log det(P_resΔ'P_res|_{Λ_res})| ≤ 1e-8 (|·| of dets).
- A4 (positivity): λ_min(ΠOΠ|_{ker h}) > 0.
- A-ctl (must FAIL A2): the same LHS with |det χΓ| and det(hh^*) computed at f = 0 (Δ_FP(1)) instead of at U_f:
  |LHS_ctl − RHS| ≥ 1e-4.
- A5 (reported only): log det(hh^*) and log|det χΓ| at f vs f = 0 (shows the U_0-dependence of the exact factor).

## Part V: Theorem V-heat (P3)
- V1 (structure (i), SU(2)): on f9's 2D periodic torus (9, 9) with one flux quantum (seam gauge) and on f9's open box 11²
  at f = 0.07: the root block of f9's Wilson Hessian, transformed to the left chart (X_left = Ad(U_b)X_right) and written in
  the complex coordinate w = x_1 − ix_2, equals Σ_p[C_pc_p^*c_p + S_p𝒮_p] built link-wise from the plaquette transports
  (C_p = cos Φ_p, S_p = 2 sin Φ_p, Φ_p the Cartan plaquette angle): max entry difference ≤ 1e-12. Same for D_0 (left chart:
  λ(x) − e^{2iθ_b}λ(x + μ)). Control (must FAIL): S_p := 0: difference ≥ 1e-3.
- V2 (closed form (ii), SU(2), independent of f9's builder): on an open 2D box B = 101 with the operator of (i) built from
  the formula (Landau gauge, C = cos(φ/2), S = 2 sin(φ/2), q = 2), the f² coefficient of the diagonal heat trace at the centre
  (Richardson in f, as f9) divided by q²t²j_0² equals (1 + ρ)² − ρ²/3 + 1/(2t), ρ = j_1/j_0, at t = 2, 3, 4, 6, 8, 12, 16, 24:
  max relative deviation ≤ 1e-5.
- V3 (closed form (ii), general γ): the same with C = ½(cos a + cos b), S = 2C tan(φ/2) for a = √(3/2)Φ, b = 0 (the SU(3)
  root (1, 2) of H_1 = i√(3/2)diag(1, 0, −1): q = √(3/2), γ = 1/4): R_12 against (1 + ρ)² − ρ²/3 + ρ/(2t) + (1 − ρ)/t:
  max relative deviation ≤ 1e-5. (This checks the Moyal step for γ ≠ 1/8; the SU(N) Wilson structure (i) for N ≥ 3 is
  checked only analytically.)
- V4 (agreement with f9): the closed form against checks/f9_out.txt's printed R_12 and R_S (6 decimals) at all eight t:
  max |difference| ≤ 3e-6.
- V5 (reported): the closed form's R_12, R_12 + R_S, R_V^{4D} at t = 10², 10³, 10⁴ and t(R_12 − 11/3) (→ −1/3).
