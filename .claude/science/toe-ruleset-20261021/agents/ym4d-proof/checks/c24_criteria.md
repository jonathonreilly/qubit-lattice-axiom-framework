# c24 criteria (written 2026-10-27 BEFORE checks/c24_fp_gap.py; RTARGET §17)

Setting: one level, fine block side n (odd), coarse torus side T, abelian 1-forms in coarse units (L3g(a)-glob
normalisation: ⟨A, A⟩ = ε^dΣ|A|², ε = 1/n). Q = Q_root (S4' root-based, all orders, all y), h = the L3g(a)-slice
functional, H_0 = {h = 0}. Λ_res = {λ : λ(c_X) = 0, Σ_{B(X)}λ = 0}, P_res = the orthogonal projector onto Λ_res.
Operators on H_0, a = 1:
- O_Δ := d*d + dd* + aQ^TQ (L3g(a)-slice's double gauge fixing);
- O_FP := d*d + dP_resd* + aQ^TQ (the legitimate one, if Lemma FP-ab says so).
Sizes: d = 2, T = 4, n = 3, 5, 7, 9; d = 3, T = 3, n = 3, 5; d = 4, T = 2, n = 3. Dense generalised eigenproblems.
- **V1 (validity).** λ_min(O_Δ on H_0) ≥ min(1/5, a/2) = 1/5 at every size (the PROVEN L3g(a)-slice bound).
- **Q1 (admissibility).** λ_min(O_FP on H_0) > 1e-8 at every size (strict positivity).
- **I1 (informational).** λ_min(O_FP)/λ_min(O_Δ) vs n in each d; whether it stabilises or decreases. Not pass/fail:
  small sizes cannot establish uniformity.
