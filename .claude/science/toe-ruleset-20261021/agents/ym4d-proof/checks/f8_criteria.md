# f8 criteria (lane C, session 5). Written before any f8 script exists.

Purpose: test Lemma COV-GI (FLOW §36) and Proposition COV-⊥-C (FLOW §37) numerically in a small-torus U(1) gauge chain
(the abelian / Cartan-sector instance), with a control that must fail.

## Model (stated here, not the S4' contours)
- Torus (Z/N_k)^d at level k in level-k units, N_k = T·L^{n−k}, L = 3, levels k = 0..n. Links (x, μ), μ = 1..d, oriented +μ.
- Model averaging map T_k(φ) (level k → level k+1), gauge covariant by construction: for the coarse link (y', μ), y = Ly',
  the L^{d−1} "staple" paths σ_t, t ∈ {−1, 0, 1}^d with t_μ = 0: axial leg y → y + t (coordinates in increasing index
  order, each in the sign direction of t_ν), then L steps +μ, then the reverse of the axial leg y + Le_μ → y + Le_μ + t.
  Weights w = L^{-(d−1)}. Background: constant flux φ per level-k plaquette in the (1, 2) plane, phase of a path = φ times
  Σ over its steps in ±e_2 of ±(x_1 − y_1) (a local gauge; only closed-loop fluxes enter). With m := Σ_σ w e^{iΦ_σ}:
  T_k(φ) = Σ_σ ω_σ χ_σ^T, ω_σ := w·Re(e^{iΦ_σ}·conj(m))/|m|² (Σω_σ = 1); Π_{k+1}(φ) := |m| (the U(1) instance of the
  kernel Hessian); χ_σ the signed incidence of σ.
- Background fluxes F_k := L^{2k}f at level k (model choice; O(f³) corrections of the true composite do not affect f²
  coefficients and are irrelevant for the exact identities).
- Fine Wilson Hessian at constant f: H = d^T C d, C = cos(f) on (1,2) plaquettes, 1 on the others. M := T_{n−1}⋯T_0.
  Chain covariance 𝒞_n := κ^{-1}Σ_{j=1}^n A_jΠ_j^{-1}A_j^T, A_j := T_{n−1}⋯T_j (A_n = 1), κ = 1.
- Slice S := {X : (d^TX)(x) = 0 at every fine site x that is not a level-n site}; orthonormal basis by SVD null space.
  J μ := d(harmonic extension of μ from the level-n sites), μ in the mean-zero subspace Λ_n^♮; D := d_n (level n).
  P_⊥ := projector onto ker d_n^T; P_G := 1 − P_⊥.

## Part A (exact identities; dense linear algebra)
Cases: (d, T, n) = (2, 3, 1), (2, 3, 2), (3, 3, 1), (4, 2, 1); f ∈ {0, 0.03, 0.07} (fine flux; F_k = L^{2k}f).
LHS(𝒞) := ½log det_S(H + M^T𝒞^{-1}M) + ½log det 𝒞 (Cholesky / slogdet; computed directly, no use of the identity).
- (A0) structural: ||MJ − D||_max ≤ 1e-12 and ||HJ||_max ≤ 1e-12 (S-compressed); min eigenvalue of the S-compressed
  H + M^T𝒞^{-1}M > 0.
- (A1) "B_n depends on 𝒞_n only through P_⊥𝒞_nP_⊥": with 𝒞' := P_⊥𝒞_nP_⊥ + P_G and 𝒞'' := (1 + G)𝒞_n(1 + G)^T,
  G := P_G R P_⊥ (R a fixed random matrix, seed 8, entries N(0,1)), |LHS(𝒞_n) − LHS(𝒞')| ≤ 1e-8 and
  |LHS(𝒞_n) − LHS(𝒞'')| ≤ 1e-8, in every case and every f. PASS iff all hold.
- (A2) full (COV-GI): |LHS(𝒞_n) − RHS| ≤ 1e-8, RHS := ½log det'_S(H + M^TΠM) + ½log det_⊥(P_⊥𝒞_nP_⊥) + ½log det(D^*D)
  − ½log det(J^*J), with det' dropping exactly k = (#level-n sites − 1) eigenvalues, which must be ≤ 1e-9·(largest), while
  the (k+1)-th smallest must be ≥ 1e-6·(largest). PASS iff all hold.
- (A3) the two forms of Π agree: ||Π_1 − Π_2||_max ≤ 1e-10·||Π_1||_max.
- (A4) f² coefficient (cases (2,3,2) and (4,2,1)): the Richardson f²-coefficient of LHS per fine site with 𝒞_n(f) and
  with 𝒞'(f) agree to ≤ 1e-6 relative (fixed step h = 0.01 and 2h). Informational: the same coefficient for
  ½log det 𝒞_n alone and for ½log det_S(H + M^T𝒞_n^{-1}M) alone.
- (A-ctl, must FAIL) H → H + 0.3·1 (so HJ ≠ 0): the (A1) comparison |LHS(𝒞_n) − LHS(𝒞')| must be ≥ 1e-4 in every case
  (at f = 0.03). If it is below 1e-4 anywhere, the control did not discriminate, and A1 is reported as NOT INFORMATIVE.

## Part B (the chain on level-n links; sparse maps)
Cases: d = 4, T = 2, n = 1, 2, 3; and T = 3, n = 1, 2 (if each case runs in < 300 s, else skipped and reported).
- (B1) trivial point, model prediction (Q_tr^m Q_tr^{mT} = L^{-2m}·1 exactly for the transverse box average in d = 4, and
  P_⊥ removes the leg terms, the GS-1 analogue): every eigenvalue of P_⊥𝒞_n(0)P_⊥ on Ran P_⊥ equals
  (1 − L^{-2n})/(1 − L^{-2}) to ≤ 1e-10 relative. PASS iff so for all cases.
- (B2) COV-str (iv) in the model: ⟨v, 𝒞_n(0)v⟩ ≥ n·||v||²(1 − 1e-12) for v = d_nδ_x. PASS iff so.
- (B3) the gauge Schur complement 𝒞^♭_G := (P_G𝒞_n(0)^{-1}P_G|_G)^{-1}: its largest eigenvalue λ_G(n) increases with n and
  the increment ratio r_G := (λ_G(3) − λ_G(2))/(λ_G(2) − λ_G(1)) (T = 2) lies in [0.5, 2] (linear-type growth, no geometric
  damping). This tests REVIEW_FLOW_S4 §2 (4)'s inference in this model only. PASS iff so; FAIL means the inference is not
  supported in the model (not a failure of COV-GI, which does not use it).
- (B4) f² coefficient per fine site of ½log det_⊥(P_⊥𝒞_n(f)P_⊥), c^⊥_n (Richardson, steps h_n = 0.01·L^{-2(n−1)} and 2h_n;
  the two Richardson estimates at (h_n, 2h_n) and (h_n/2, h_n) must agree to ≤ 1e-4 relative, else NOT EVALUATED),
  T = 2, n = 1, 2, 3: bounded and geometric: |c^⊥_3 − c^⊥_2| ≤ 0.5·|c^⊥_2 − c^⊥_1| and |c^⊥_3| ≤ 2·max(|c^⊥_1|, |c^⊥_2|).
  Informational: the same for ½log det 𝒞_n(f) (whole) and the operator bounds of P_⊥𝒞_n(f)P_⊥ at |f| = 0.05·L^{-2n}.
- Reading rule: PASS of A0-A3 and a FAILING control support Lemma COV-GI in this U(1) model to round-off; it says
  nothing about root sectors or the S4' contours. B1-B2, B4 PASS support Proposition COV-⊥-C's mechanism in this model.
  Any FAIL stands as recorded; no criterion is changed after the script exists.

Resources: one NUMERIC LOCK acquisition, nice 10, 1 thread (OMP/OPENBLAS/MKL/VECLIB = 1), expected peak < 1.5 GB (estimate,
not a criterion), wall < 20 min; outputs checks/f8_out.txt, checks/f8_time.txt.

## Amendment A1 (POST-HOC, appended 2026-10-28 04:37 UTC, after the official f8 run; the original criteria above are unchanged and their outcomes stand, including the B1 FAIL)
Reason: B1 failed because the pre-registered staple model averages over transverse offsets t ⊥ μ (a μ-dependent set),
so Q_staple = Q_tr − (μ-dependent component-wise differences), which is not of the form Q_str − d∘h that GS-1 imports for
the S4' map (FLOW_LOG 04:38). This amendment adds a second model that has that structure, and tests Prop. COV-⊥-C's
mechanism there. Script: checks/f8b_fullbox.py (new file, written after this amendment), output f8b_out.txt, f8b_time.txt.
- Model 2 ("full-box staple"): as the staple model, but t runs over the full box {−1, 0, 1}^d (t_μ included, L^d paths),
  legs axial in increasing index order for every μ. Then the leg sums h̄(z) := avg_t(leg sum z → z + t) do not depend on
  μ, and Q_2 = Q_box − d∘h̄ with Q_box the centred straight average (line of length L from y + t, t in the full box).
- (A') Part A of f8, unchanged code and thresholds, run with model 2 (A0-A4 and the control).
- (B1'a) GS-1 analogue, built independently: ||P_⊥(Q_2^m − Q_box^m)||_max ≤ 1e-12 for m = 1, 2 (d = 4, T = 2, f = 0), Q_box
  constructed directly from its definition (not from Q_2).
- (B1'b) GS-2 (e) and Prop. COV-⊥-C (a): ||P_⊥Q_box^mQ_box^{mT}P_⊥|| ≤ L^{-2m}(1 + 1e-12) for m = 1, 2; the spectrum of
  P_⊥𝒞_n(0)P_⊥ on Ran P_⊥ lies in [1 − 1e-12, (1 − L^{-2})^{-1}(1 + 1e-12)] for (T, n) = (2, 1), (2, 2), (2, 3), (3, 1),
  (3, 2); and P_⊥(𝒞_3(0) − 𝒞_2(0))P_⊥ ≥ −1e-12, with norm ≤ L^{-4}(1 + 1e-12) (T = 2).
- (B4') as B4, with model 2.
- Informational: λ_max of the gauge Schur complement 𝒞^♭_G for n = 1, 2, 3 (T = 2), and c_full.
- Reading rule: as for f8; POST-HOC throughout; a PASS here supports the mechanism in model 2 only.
