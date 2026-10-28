# bb6 criteria (lane B session 6; written after BFT_B §18 and Step 1, before checks/bb6_transport.py exists)

Model: d = 4 abelian chain (one real component), L = 3, k = 2, coarse torus side T = 2 (level sides 18, 6, 2). Root map
Q_l := Q_str,l - d∘h_l with h_l(v)(X) := average over y in the block B(X) of the line sum of v along the axial path
c_X → y (coordinate order 0,1,2,3); this Q is root-covariant (Q d = d ev) and of lane A's form (BL-2 (b)). κ_0 = 1.0,
κ_1 = 0.7. Sources: G_0, G_1 random 2-forms; j_0 = d*(random 2-form), j_1 = d*(random 2-form) (co-closed); s_0, s_1 random;
data B_2 random. Critical point by conjugate gradients on the normal equations. All thresholds below are generic
(machine/solver precision) or lane A's constants (BL-2 (c), (e)); none is a constant derived in session 6.

## Part A (identities at the critical point)
- A0 structure: max|Q_l dλ - d ev λ| ≤ 1e-12·max|λ| for random λ (l = 0, 1). PASS required.
- A1 solver: relative gradient residual of the normal equations ≤ 1e-9. PASS required.
- A2 co-closedness: max|d*ρ_l| ≤ 1e-7·max|ρ_l| for l = 0, 1 (ρ_l := κ_lr_l - s_l). PASS required.
- A3 funnel term: max|Q_1^Tρ_1 - Q_str,1^Tρ_1| ≤ 1e-7·max|ρ_1|. PASS required.
- A4 transport formula for r_0 (with every source class present): max|κ_0r_0 - [s_0 + Q_str,1^Tρ_1 - d*G_1 - j_1]| ≤
  1e-7·max|κ_0r_0|. PASS required.
- A5 negative control [edited 09:25:02 UTC (exact time: RBB6-fix RS6-9, session 7), before the script existed: the original control (a non-co-closed j_1) has no critical
  point, since such a j_1 pairs with gauge directions, so it cannot test A2]: for a random NON-co-closed level-2 1-form v,
  A3's identity must FAIL: max|Q_1^Tv - Q_str,1^Tv| ≥ 1e-3·max|v| (the funnel term vanishes only on co-closed forms).
  PASS required (= the control fails as predicted).
- A6 sizes (lane A BL-2 (c)): coarse sup of (Q_str,1^Tρ_1) at level 1 ≤ L^{-2}·max|ρ_1| (coarse at level 2 = own) ·(1 + 1e-12).
  PASS required.

## Part B (depth scaling of the transported top term; no solve)
Random level-k 1-form ρ on the coarse torus of side 2; H_m := coarse-unit (level k - m, 1-form units) value of
(Q_str^{(L^m)})^Tρ for m = 1, 2, 3 (level sides 6, 18, 54). Measured: S_m := sup|H_m|, D_m := sup|∇^cH_m|, P_m := axis-shift
pointwise Hölder proxy of ∇^cH_m (α = ¼; offsets 1, 2, 4, …, L^m own steps along each axis, |offset| ≤ 1 coarse).
- B1 (BL-2 (c)): S_m ≤ L^{-2m}·max|ρ|·(1 + 1e-12). PASS required.
- B2 (BL-2 (e)): D_m ≤ 2L^m·S_m·(1 + 1e-12). PASS required.
- B3 (BL-2 (e)-type, pointwise): P_m ≤ 2·L^{αm}·D_m·(1 + 1e-12). PASS required.
- B4 [guess, informational, RH-F3]: the normalised proxy L^{(1-α)m}P_m/max|ρ| varies by at most a factor 3 over m = 1..3
  (the transported term saturates the inverse estimate up to a constant).

Verdict: ALL PASS iff A0-A6 and B1-B3 pass. B4 is recorded either way and not repaired.
Resources: < 1 GB, < 20 min; numeric lock; nice 10; thread variables 1.
