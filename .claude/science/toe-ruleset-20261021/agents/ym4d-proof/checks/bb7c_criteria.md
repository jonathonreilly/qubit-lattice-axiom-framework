# bb7c criteria (lane B session 7; written after BFT_B §21 and Step 1, before checks/bb7c_resid.py exists)

Model: d = 2, abelian (one real component), L = 3, ternary DD8 refinement pair (S_0 = s ⊗ s, S_1 derived, as in checks/bb5),
roots at fine sites 3I (bb5's convention). Top coarse torus side 6, random top 1-form B_k (iid N(0, 1)), S_1-chain
B_j = S_1B_{j+1} for depths k = 1, …, 5 (the R-chain has the same residuals: R - S_1 = dμ with ev μ = 0, and root maps are
root-covariant). Root maps on level-j 1-forms (own units): Q_ax = the root-row line sum (bb5's q_ax); Q_sym = the average over
y ∈ {-1, 0, 1} of the S4'-type contour c_X → c_X + y e_⊥ → (straight L-leg at transverse offset y) → c_{X+e} + y e_⊥ → c_{X+e}
(transverse-reflection symmetric); Q_asym = the same average over y ∈ {0, 1} (control, not symmetric). Residual r_j := Q B_j -
B_{j+1}; weighted residual W_θ(k, j) := L^{θ(k-j)}·L^{2(k-1-j)}·max|r_j| (= the (C_g-θ) entry with κ = 1).
Thresholds: exactness checks at float precision; the rest are the predicted scalings of Lemma Γ0 / Proposition Cg-lin
(symmetric: W_θ(k, j) ∝ L^θρ_{j+1}^{1-θ}, ratio per level L^{-(1-θ)} = 0.577 at θ = ½) and of 16.13 (e) for the asymmetric map
(W_0 ≈ constant, so W_θ grows by L^θ = 1.73 per level).
- C0 structure: max|Q dλ - d ev λ| ≤ 1e-12·max|λ| for Q ∈ {Q_ax, Q_sym, Q_asym} (random λ); max|Q_ax B_j - B_{j+1}| ≤ 1e-10·max|B_k|.
  PASS required.
- C1 Lemma Γ0 (exact, on a patch with the linear field B = (-Hz_2/2, Hz_1/2), H = 1): |(Q_sym - Q_ax)B| ≤ 1e-12;
  control |(Q_asym - Q_ax)B| ≥ 0.1. PASS required.
- C2 symmetric, θ = ½, depth 5: W(5, 0)/W(5, 4) ≤ 0.5. PASS required.
- C3 symmetric, θ = 1, depth 5: max_j W_1(5, j) ≤ 2·W_1(5, 4). PASS required.
- C4 control, asymmetric, θ = ½, depth 5: W(5, 0)/W(5, 4) ≥ 2. PASS required (= the control grows as predicted).
- C5 informational: the profiles W_θ(5, j), θ ∈ {0, ½, 1}, for both maps; max_j W_½(k, j) for k = 1..5.
Resources: fine side 1458 at depth 5; dense 1D matrices; expected < 1 GB, < 2 min.
