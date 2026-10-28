# r55n_a1 criteria — exact arithmetic behind NORMS Theorem N1-15, §N4, §N7 and NQ-1's constant

Written 2026-10-28T22:27:47Z UTC by the REVIEW55_NORMS reviewer (claude-opus-5-5), BEFORE r55n_a1.py exists.
Exact Fraction arithmetic; decimals in the files are parsed as exact rationals.

- a1-1 SERIES: sum_{n=1}^{K} 3^{3-n} -> 27/2: PASS iff partial sums at K = 1..40 are < 27/2, increasing, and
  27/2 - S_K == (27/2) 3^{-K} exactly (closed form), and L^{d-1}/(L-1) == 27/2 at (L,d) = (3,4).
- a1-2 EXPONENTS: for d in 2..7, n in 1..6 and symbolic theta-triples: the soft exponent
  d*n - theta_r*(n-1) - 2*theta_A*n equals (d - theta_r - 2 theta_A) n + theta_r; at (theta_r, theta_A) = (d-1, 1) it equals
  (d-1) - n (n-coefficient exactly -1 for every d); Wilson exponent (d - theta_c - 2 theta_A) k at (2,1) equals (d-4)k.
  PASS iff all identities hold.
- a1-3 SINGLE-WEIGHT NO-SOLUTION: for theta_w on a grid of rationals in (0, 2] (step 1/1000) and the boundary,
  theta_w + 2 min(1, theta_w - 1) > 4 never holds; and with the cap theta_A <= 1 alone, theta_w + 2 theta_A <= 4 for every
  theta_w <= 2 (algebraic, checked on the grid). PASS iff never satisfied.
- a1-4 NQ-1 CONSTANT: q0(L,d) = 1 + d(L+1)/(2L) equals 11/3 at (3,4); is strictly decreasing in odd L >= 3 at d = 4
  (checked L = 3..101); and the closed-form identity L^j + (d(L^2-1)/(2L))(L^j-1)/(L-1) = L^j + (d(L+1)/(2L))(L^j-1)
  holds for L in {3,5,7}, d in {2,3,4}, j in 1..8. PASS iff all hold.
- a1-5 QUOTED NUMBERS (NORMS §N4/§N5/n1-E, from the quoted decimals): Z_col*Z_row^2 at (156.08, 2.849) rounds to 1266.87;
  (1+Z_col)(1+Z_row)^2 rounds to 2327.11; 81*0.1202 rounds to 9.74; (2/3)*2.219 rounds to 1.48; 156.08/9.7362 rounds to
  16.03; 1266.87-gain endpoints 1266.8726.../(9*0.1202) and .../(9*0.1236)^3 round to 1171.1 and 920.3. PASS iff all
  round as stated (2 decimals unless stated).
- a1-6 PIGEONHOLE (max column vs average): for nonnegative column masses over the d(d-1)/2 coarse-plaquette types of a
  cell, max <= (d(d-1)/2) * average; evaluated bound (d(d-1)/2)(L^d K + (2/(d-1)) K_rho) at K = 0.1202, K_rho = 2.219.
  Informational number only (the inequality is proved by hand in the review).
