# mc55_3 — criteria (written 2026-10-29T06:05:18Z, before any mc55 script exists)

Purpose: test MINCB55 Lemma LIFT_j's counting on exact SU(2) configurations: (i) the intra-block ladder bound, (ii) the contour
comparison bound with n_L, (iii) the maximiser step ||W_0(Mbar_c) - T_b|| <= 1.7 sqrt(N) n_L eps'. SU(2) = unit quaternions with
rational coordinates (stereographic parametrisation), products exact (Fractions); norms ||U - 1||_op = |q - 1| (Euclidean, quaternion);
square roots only through rigorous rational interval enclosures (bisection to width < 1e-30, rational endpoints).

Geometry: d = 3, L = 3, fine torus 6x6x6 (2x2x2 level-(j+1) blocks of 3x3x3 sites, roots at coordinates = 1 mod 3), axial paths in
coordinate order (1,2,3). S4' contours of a coarse link c = (X, X+e_mu): for every order sigma of the 3 axes and every y' in B(X):
P^sigma(c_X -> y') . straight L-step segment y' -> y'+L e_mu . P^sigma(c_Y -> y'+L e_mu)^(-1). Weights uniform.
n_L(d=3, L=3) := (2d(L-1) + L + 1)((2L-1) + (d-1)(L-1)) = 16 * 9 = 144. Rung bound for an intra-block link b = (x, x+e_mu):
r(b) := sum_{nu > mu} |x_nu - (c_X)_nu|. eps' := max over all plaquettes of |U(p) - 1|.

Instances (fixed seeds, stated before running): 4 random instances U_b = g(x) q_b g(y)^(-1) with q_b small (stereographic from
v in {-1,0,1}^3 / 10^5) and g arbitrary (stereographic from v in {-3..3}^3 / 2); 1 aligned instance (constant field in the (1,2)
plane built from powers of one rational unit quaternion of small angle, gauged by a random g).

Gates (each must hold on every instance):
- L1: the axial gauge h(z) := T(c_X -> z) has h(c_X) = 1 and gives U^h_b = 1 exactly on every tree link.
- L2: every intra-block non-tree link has |U^h_b - 1| <= r(b) * eps' (rigorous: upper enclosure of the left side <= lower
  enclosure of the right side), and r(b) <= (d-1)(L-1)/2 = 2.
- L3: for every inter-block link b and every contour of its coarse link: |T(path_b) - T(contour)| <= n_L * eps'.
- L4: for every coarse link: with Mbar := mean of the contour transports and W_0 := Mbar/|Mbar| (SU(2): a positive multiple of a
  unit quaternion, LCONV55 Lemma PM), |W_0 - T_b| <= 1.7 * sqrt(2) * n_L * eps' for every inter-block link b of that coarse link
  (sqrt(2) replaced by its lower bound 14142/10000 on the right side, so the test is conservative), and the NA-alg regime holds:
  1.04 * sqrt(2) * n_L * eps' <= 1/20 (upper bound 14143/10000 for sqrt(2)).
Designed controls (each must FAIL on the aligned instance, otherwise NON-DISCRIMINATING and the verdict is FAIL):
- C1: L2 with r(b) replaced by max(r(b) - 1, 0).
- C2: L3 with n_L replaced by 1.
Verdict: PASS iff L1-L4 hold on all five instances and both C1 and C2 FAIL on the aligned instance.
Scope (stated in advance): d = 3 instead of d = 4 (the lemma's constants are stated for general d; the check uses the d = 3 values);
finitely many instances; it can expose a wrong rung count or a wrong n_L formula, it cannot prove the lemma.
