# r55n_q1 criteria — independent exact enumeration of Setting SC's Q (= Q_root, S4' linearised) at L = 3, d = 4

Written 2026-10-28T22:27:47Z UTC by the REVIEW55_NORMS reviewer (claude-opus-5-5), BEFORE r55n_q1.py exists.
No code from nq1_qnorm.py, nd1_qrow.py, nd1b_hnorm.py or any review scratch is imported or read for this check.

Definitions used (from primary sources only):
- PROOF.md S4' (locating string "For each of the d! coordinate orders σ, let P^σ be the complete-axial transporter"):
  T^σ_y = P^σ(c_X -> y) . S_y . P^σ(c_Y -> y + L e_mu)^dag, S_y the straight leg of L steps from y.
- LINEAR_PACKAGE.md §1.1-1.2 (locating strings "B(X) = LX + {0, …, L-1}⁴", "Q_rootA(X, μ) := avg_{σ,y}",
  "(Q_strA)(X, μ) := L^{-4}Σ_{y∈B(X)}Σ_{j<L}", "h(A)(X) := avg_σavg_{y∈B(X)}∫_{P^σ(c_X→y)}A"):
  block B(X) = L X + {0..L-1}^d, root c_X = L X + (L-1)/2 (1,..,1), c_Y = c_X + L e_mu.
- Complete-axial path in order sigma: change coordinate sigma(1) first (unit steps), then sigma(2), ...
- Norm: ||M||_{inf->inf} = max row l1 sum (row = coarse link, columns = fine links).
- NORMS Q_str (NORMS.md §N1 "Q_str B(c) := L^{−(d−1)}Σ_{paths}Σ_{b∈path}σ_bB_b over the L^{d−1} straight paths of L links"):
  realised two ways, (N-a) paths from c_X + t to c_X + t + L e_mu, (N-b) paths from (block low face) + t, t over the
  L^{d-1} transverse block offsets.

Pre-registered gates (exact Fraction arithmetic, plain python, python3 -I -B, no numpy):
- q1-A VALUE: for every mu in 0..3, sum_b |Q_root(c,b)| == 205/27 exactly AND support == 459.
  PASS iff both hold for all four mu. FAIL otherwise (then my value is reported as the finding, provided q1-C and q1-D PASS).
- q1-B STRICT: the q1-A value > L = 3. PASS iff true for all mu.
- q1-C SLICE IDENTITY: Q_root == Q_str^LP - d∘h entrywise (0 differing entries), all mu, where (d∘h)(X,mu) = h(X+e_mu) - h(X)
  with h(X+e_mu) built independently from the contours' far funnels from c_Y. PASS iff 0 differing entries for all mu.
  Control q1-C': same identity with NORMS Q_str (N-a) and (N-b) in place of Q_str^LP. Designed to FAIL (nonzero
  differing entries). If it does NOT fail for some realisation, the control is reported as non-discriminating.
- q1-D ROOT COVARIANCE: Q_root(d_0 lam) == lam(c_Y) - lam(c_X) exactly for lam(s) = sum_i (i+2)*s_i^3 + s_0*s_1*s_2*s_3
  + 3*s_1*s_2^2 (cubic in every coordinate), all mu. PASS iff exact for all mu.
  Control q1-D': Q_str^LP(d_0 lam) == lam(c_Y) - lam(c_X) must FAIL in all four directions. If it fails to fire in some
  direction, that direction is reported as under-powered.
- q1-E COMPOSITE j = 2 (mu = 0 and mu = 3): sum_b |Q^(2)(c,b)| == 2021/81 and support == 47385, where
  Q^(2) = Q_1 ∘ Q_0 with Q_1 the same pattern in level-1 units (level-1 site s1 has level-0 root L*s1 + (L-1)/2(1,..,1)).
  Control: Q_str^(2) (same composition code) has all entries >= 0 and row sum == 9.
  PASS iff both. FAIL otherwise (my value reported).
- q1-F NQ-1 DOMINATION: computed values <= L^j + (d(L^2-1)/(2L))(L^j-1)/(L-1) (= 25/3, 91/3 at j = 1, 2) and
  <= (11/3) L^j; and computed/L^j >= 205/81 at j = 1. PASS iff all hold.
- q1-G h NORM: row l1 of h == 8/3 == avg_{y in B(X)} |y - c_X|_1 == d(L^2-1)/(4L). PASS iff all equal.
- q1-H Q_str SUPPORTS: Q_str^LP support == 135 with longitudinal multiplicity profile (1,2,3,2,1)/81 per transverse
  position; NORMS Q_str support == 81 (both realisations). PASS iff all hold.

Verdict use: q1-A/q1-B decide NQ_DEF's "||Q|| = 205/27 > L"; q1-C/q1-D/q1-E controls decide whether my construction is
the right operator; q1-F decides NQ-1's numerical consistency (not its proof, which is re-derived by hand in the review).
A PASS here is evidence about j = 1, 2 only and is never used as a proof of an all-j statement.
