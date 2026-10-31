# hg55_2 criteria (written before hg55_2.py exists)

Purpose: decide, on the ACTUAL nonlinear soft density of the lane (TOWER-VAR / NA-alg (b): phi_hat(M;V) =
Re tr(W_0^{-1}M) - Re tr(V^{-1}M), W_0 the SU(N) polar maximiser of the S4' mean M), the structural claim of HIGHER55
Lemma HS / §T3: in the exact all-orders slot split of one soft term,
   residual slot  Omega := -d phi_hat / d x_{l+1}(c)          (covector; linear part 2*rho in tau-coordinates),
   plain current  P_{b,i} := d phi_hat / d xi_{b,i} - Q_{cb} * Omega_i   (= derivative at fixed linear residual),
on M-ball-type families x_l(b) = eps*xbar_{dir(b)} + eps^2*g(b), x_{l+1}(c) = (Q x_l)(c) - eps^2*rho_2:
  (i)  Omega - 2*eps^2*rho_2 = O(eps^3)                       [residual slot is third order: own L^{-3(k-l)}];
  (ii) P = O(eps^3) and its eps^3 coefficient equals the BCH2 row 2*sum_j rho_{2,j} * D_{b,i} a^{(2)}_j(xbar),
       computed INDEPENDENTLY from the bilinear BCH2 form (no series machinery) [the only marginal plain term is
       linear in the residual];
  (iii) if rho_2 = 0 (and rho = 0 exactly), P = O(eps^4)     [no non-r-linear marginal plain term at third order:
       the level-count factor cannot re-enter at cubic order].
Model: N = 2 (exact: for SU(2) the polar maximiser is W_0 = M/sqrt(det M), and phi_hat = sqrt(det M)*(2 - Re tr(e^{-v}W_0))),
d = 2, L = 3 (contours of LINEAR_PACKAGE §1.2 in two dimensions: 2 orders x 9 starting points = 18 contours).
su(2) basis tau_1 = [[i,0],[0,-i]], tau_2 = [[0,1],[-1,0]], tau_3 = [[0,i],[i,0]] (Gaussian-integer entries).
Arithmetic: exact truncated power series in eps (through eps^4) with dual numbers (t^2 = 0) for derivatives; matrix
entries are Gaussian rationals (pairs of Fractions). No floats anywhere.
Tested links: 6 level-l links (go-region, straight leg, return region, both directions) x 3 components; Omega: 3 components.

Pre-registered gates:
- B1 (3 samples, rho_2 != 0): for every i, coefficients eps^0, eps^1 of Omega_i are 0 and eps^2 coefficient == 2*rho_{2,i}.
                                                                              PASS iff all.
- B2 (same samples): for every tested (b,i), coefficients eps^0..eps^2 of P_{b,i} are 0 and the eps^3 coefficient equals
      the independent BCH2-row prediction exactly; AND at least one prediction is nonzero (non-vacuity).  PASS iff all.
- B3 (2 samples, rho_2 = 0, x_{l+1}(c) = (Q x_l)(c) exactly): coefficients eps^0..eps^2 of Omega_i are 0 and
      coefficients eps^0..eps^3 of every P_{b,i} are 0; AND some P_{b,i} has a nonzero eps^4 coefficient and some
      Omega_i a nonzero eps^3 coefficient (non-vacuity).                      PASS iff all.
- B4 (negative control; must FIRE): B3's computation with the S4' average replaced by ONE contour (sigma = (0,1),
      y = c_X + e_1), Q replaced by that contour's linearisation: some P_{b,i} has a nonzero eps^3 coefficient OR some
      Omega_i a nonzero eps^2 coefficient.                                    FIRES iff so; otherwise the check is
      NON-DISCRIMINATING (overall FAIL of the check).
- B5 (sanity): det M is real (imaginary part of every coefficient 0) and det W_0 == 1 through eps^4.  PASS iff all.
Overall: PASS iff B1, B2, B3, B5 PASS and B4 FIRES.
What this check cannot decide: d = 4 (the contour combinatorics differ; CEN2 itself is checked in 4D by hg55_1),
N >= 3 (non-scalar H), orders beyond eps^4, uniformity in k or T, and the analytic (Cauchy) tail bounds. It is a model
check of the order-by-order mechanism on the lane's actual soft density, not a proof.
