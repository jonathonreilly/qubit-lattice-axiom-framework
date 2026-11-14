# hg55_3 criteria (written before hg55_3.py exists)

Purpose: decide exactly, at N = 3 (where G = W_0^{-1}M = H + i theta 1 has a NON-scalar Hermitian part H), the two exact
structural identities on which the all-orders slot estimates rest:
 (SG)  KFACTOR_OFF55 Lemma SG: for every variation, d phi_hat = -Re tr(Theta W_0^{-1} dM) + Re tr(Z Theta G),
       Theta := e^rho - 1, rho := log(V^{-1} W_0), Z := V^{-1} dV, G := W_0^{-1} M  (envelope step + Re tr(ZG) = 0);
 (NC3) HIGHER55 Lemma NC3: in the chart (x_l, w) with x_{l+1}(c) = X_0(x_l) - w, the soft density has quadratic part
       (1/2)|w|^2_HS and NO cubic Taylor term.
Object: phi_hat(M;V) = Re tr(W_0^{-1}M) - Re tr(V^{-1}M) (TOWER-VAR / NA-alg (b)), M = S4' mean of the contour products
(d = 2, L = 3: 18 words), W_0 = e^{X_0} with X_0 the fixed point of X = Ybar + Pi(K(X)) of NA-alg (a) (K(X) = R_X + E +
(R_X - X)(Ybar + E), R_X = e^{-X} - 1 + X, E = M - 1 - Ybar, Ybar = mean of the contour logs), Pi = orthogonal projection
onto su(3) for Re tr(A*B). Exact truncated power series in eps through eps^4, dual numbers (t^2 = 0) for derivatives,
3x3 Gaussian-rational matrices (pairs of Fractions). su(3) basis with Gaussian-integer entries (E12-E21, E13-E31,
E23-E32, i(E12+E21), i(E13+E31), i(E23+E32), i(E11-E22), i(E22-E33)). No floats.

Pre-registered gates:
- C1 (SG identity): 2 samples of the M-ball-type family x_l(b) = eps*xbar_{dir(b)} + eps^2*g(b), V = e^{v},
  v = (Q x_l)(c) - eps^2*rho_2 (random integer data); perturbations t*A at 3 links (2 basis directions each) and at v
  (2 directions): the dual part of phi_hat equals -Re tr(Theta W_0^{-1} dM) + Re tr(Z Theta G) coefficient by coefficient
  through eps^4.                                                                PASS iff all 16 comparisons exact.
- C2 (sanity of the maximiser): Pi(e^{-X_0} M) == 0 through eps^4 (stationarity); G's eps^1 coefficient == 0; the
  anti-Hermitian part of every coefficient of G is a scalar multiple of the identity.   PASS iff all, in every sample.
- C3 (NC3): 3 samples with homogeneous scaling x_l(b) = eps*xi_b (random su(3) per link), x_{l+1}(c) = X_0(eps*xi) - eps*w
  (random w in su(3)): phi_hat's eps^2 coefficient == -(1/2) tr(w^2) and eps^3 coefficient == 0.  PASS iff all 3.
- C4 (control for C3, must FIRE): the same with the LINEAR-residual chart x_{l+1}(c) = (Q eps*xi)(c) - eps*w:
  eps^3 coefficient != 0 in at least one sample.                               FIRES iff so (else C3 NON-DISCRIMINATING).
- C5 (control for C1, must FIRE): the same comparison as C1 but with W_0 replaced by the NON-maximiser e^{Ybar} (in phi_hat,
  Theta, G alike): at least one comparison fails.                             FIRES iff so (else C1 NON-DISCRIMINATING).
Overall: PASS iff C1, C2, C3 PASS and C4, C5 FIRE.
What this cannot decide: d = 4 (CEN2 in 4D is hg55_1), orders beyond eps^4, the analytic (Cauchy) tails, uniformity in
k or T. It checks two exact identities on the lane's actual soft density at one non-abelian rank beyond N = 2.
