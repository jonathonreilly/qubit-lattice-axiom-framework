# bb6n criteria (lane B session 6; written before checks/bb6n_nf.py exists)

Model: d = 2, SU(2) (unit quaternions; |·| the Euclidean norm of the su(2) ≅ R³ log), L = 3, n = 3 (one coarse unit = 3
links; "level 0" = fine, "level k" = coarse with k = 1), coarse torus side T = 5 (fine side 15). Boxes Ñ_X: fine sites
within torus ℓ^∞ distance 2n = 6 of the root c_X = 3X (side 13). Box functional Φ_{U,X}(g) = Σ_b|log g(x)U(b)g(y)^{-1}|²,
g(c_X) = 1, minimised by right-trivialised gradient descent. Input U = exp(A), A i.i.d. Gaussian scaled so that
n·max|A| = 0.3. Thresholds are generic precision thresholds; none is a session-6 constant.
- N1 (NF-crit, one box): at convergence max_z|(d*w)(z)| ≤ 1e-9 (Neumann divergence of w = log U^g, all box sites). PASS required.
- N2 (NF-uniq, one box): descents from 4 random starts g_0 = exp(η), |η| ≤ 0.5 i.i.d. at non-root sites, converge to the same
  g (max |log(g_a g_b^{-1})| ≤ 1e-7). PASS required.
- N3 (NF-cov, one box): for h Haar-random at every fine site, the descent for U^h from g_0 = exp(η)h(c_X)h^{-1} (|η| ≤ 0.3)
  converges to h(c_X)g_X(U)h^{-1} (max |log(·)| distance ≤ 1e-7). PASS required.
- N4 (KΠ, torus T = 5): (a) G(U)(c_Y) = 1 at every root (≤ 1e-12); (b) idempotence max_z|log G(Π^{NA}(U))(z)| ≤ 1e-7;
  (c) covariance: for h with root values exp(ζ_Y), |ζ_Y| ≤ 0.2, and Haar-random values off the roots, Π^{NA}(U^h) (normal
  forms of U^h solved from scratch) equals Π^{NA}(U)^{ĥ}, ĥ := M[h(c_X)g_X(U)]·M[g_X(U)]^{-1}, to ≤ 1e-7 on every link, and
  ĥ(c_Y) = h(c_Y) (≤ 1e-12). PASS required.
- N5 negative control: with the Karcher mean replaced by gluing in exponential coordinates, G_exp := exp(Σ_Xχ^5_X log g_X),
  the covariance of N4 (c) (with ĥ_exp := G_exp(U^h)hG_exp(U)^{-1}) must FAIL: the extension then is NOT given by the
  formula of N4 (c) (deviation ≥ 1e-4). PASS required (= the control fails as predicted).
- N6 (informational): n·max|w| of the normal forms (the 𝒲_δ size) and ε_f(U).
Verdict: ALL PASS iff N1-N5. Resources < 1 GB, < 20 min; numeric lock.
