# hg55_1 criteria (written before hg55_1.py exists)

Purpose: decide, exactly, the second-order cancellation of the S4' average (BFT_A Lemma BA-4, "CEN2") on the actual
d = 4, L = 3 contours. HIGHER55's third-order estimate uses it as load-bearing: the full nonlinear residual-type slot
is O(L^{-3(k-l)}) own and the non-r-linear plain current is O(L^{-4(k-l)}) own ONLY because the second-order part
a^{(2)} of the averaged polar log is O(eps^3) (not O(eps^2)) on M-ball fields.

Model: Lie algebra (Q^3, x) (cross product) = so(3) = su(2); |.|_1 the l1 norm; |a x b|_1 <= |a|_1 |b|_1.
Contours (LINEAR_PACKAGE §1.2, BFT_A §3.4): level-l lattice Z^4, coarse link c = (X = 0, mu), block B(0) = {0,1,2}^4,
root c_X = (1,1,1,1), c_Y = c_X + 3 e_mu. T^sigma_y = axial path c_X -> y in coordinate order sigma, then 3 straight
mu-steps y -> y + 3e_mu, then the REVERSE of the axial path c_Y -> y + 3e_mu in order sigma. sigma over all 24 orders,
y over all 81 points of B(0): 1944 contours per mu. Letter of a step = +x(link) forward, -x(link) backward.
B_2(word) := (1/2) sum_{a<b} [z_a, z_b]. "avg" = uniform average over (sigma, y).
Exact integer / Fraction arithmetic only. Seeds fixed in the script.

Pre-registered gates (all four mu = 0..3, six random fields each = 24 cases per gate):
- A1: direction-constant fields x(b) = xbar_{dir(b)} (xbar_nu random nonzero integer vectors in [-5,5]^3):
      avg B_2 == 0 exactly.                                                     PASS iff all 24 exact zeros.
- A2 (non-vacuity of A1): for the same fields some single contour has B_2 != 0.  PASS iff true in all 24.
- A3 (BA-4 general bound, l1 form): x(b) = 100*xbar_{dir(b)} + delta(b), delta(b) random integer vectors in [-1,1]^3:
      |avg B_2|_1 <= (p(p-1)/4) * D * (2*X + D), p = 11 (= 5L-4), D := max_b |delta(b)|_1 over all links used,
      X := max_nu |100 xbar_nu|_1.                                               PASS iff true in all 24.
- A4 (scaling on M-ball-type fields): x(b) = eps*xbar_{dir(b)} + eps^2*g(b), g(b) random integer vectors in [-3,3]^3;
      avg B_2 as a polynomial in eps: coefficient of eps^2 == 0 in all 24 cases, AND coefficient of eps^3 != 0 in at
      least one case.                                                            PASS iff both.
- A5 (negative control; must FIRE): A4's computation with the y-average removed (y := c_X + e_nu for one nu != mu,
      average over sigma only): coefficient of eps^2 != 0 in at least one case.  FIRES iff so. If it does not fire, the
      check is declared NON-DISCRIMINATING (overall FAIL of the check, no verdict on the claim).
- A6 (linearisation sanity): for direction-constant fields avg (sum of letters) == 3*xbar_mu exactly (Q xbar = L xbar_mu).
                                                                                 PASS iff all 24.
Overall: PASS iff A1, A2, A3, A4, A6 PASS and A5 FIRES. Any other outcome is reported as FAIL with the failing gate.
What this check cannot decide: anything about the analytic (all-orders) tail, uniformity in k or T, or N >= 3; it
re-checks one CONFIRMED algebraic input (REVIEW_BFT_A_S1 Part 4) on the exact contour set used by the theorem.
