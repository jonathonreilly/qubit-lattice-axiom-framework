# hg55_4 criteria (written before hg55_4.py exists; motivated by hg55_3's non-firing control C5)

Why a new check: hg55_3 C5 (W_0 replaced by the non-maximiser e^{Ybar}) could not fire, for a structural reason found after
the run: in hg55_3's M-ball-type family x_l = eps*xbar_{dir} + eps^2*g, every contour log has the same order-eps part
(L*xbar_mu), so the spread Delta_j := Y_j - Ybar is O(eps^2) and the stationarity defect of e^{Ybar},
Pi(e^{-Ybar}M) = -(1/12) avg [Delta,[Delta,Ybar]] + (1/6) avg Delta^3 + ..., is O(eps^5): beyond eps^4. hg55_3's verdict
stays FAIL (non-discriminating) as pre-registered. This check repeats the Lemma SG comparison on a family where the
spread is O(eps) (so the defect is O(eps^3)) and where the control can therefore fire.

Object and arithmetic: identical to hg55_3 (N = 3, d = 2, L = 3, 18 S4' words; phi_hat = Re tr(W_0^{-1}M) - Re tr(V^{-1}M);
W_0 = e^{X_0}, X_0 the NA-alg (a) fixed point as an exact series; eps through eps^4; dual numbers; Gaussian rationals).
Family: homogeneous, x_l(b) = eps*xi_b (independent random su(3) integer combinations per link), V = e^{v},
v = (Q x_l)(c) - eps*omega (random su(3)).

Pre-registered gates:
- D1 (Lemma SG identity): 2 samples; perturbations t*A at 3 links x 2 basis directions and at v x 2 directions (8 per
  sample): dual part of phi_hat == -Re tr(Theta W_0^{-1} dM) + Re tr(Z Theta G) through eps^4.   PASS iff 16/16 exact.
- D2 (non-vacuity): each of the 16 dual parts has at least one nonzero coefficient among eps^1..eps^4.  PASS iff 16/16.
- D3 (maximiser sanity): Pi(e^{-X_0}M) == 0 (both parts) through eps^4; G eps^1 == 0; anti-Hermitian part of each
  coefficient of G a scalar multiple of 1.                                                            PASS iff all.
- D4 (control, must FIRE): the same 16 comparisons with W_0 := e^{Ybar} (in phi_hat, Theta, G alike): at least one fails.
                                                          FIRES iff so; otherwise D1 is NON-DISCRIMINATING (overall FAIL).
Overall: PASS iff D1, D2, D3 PASS and D4 FIRES.
Cannot decide: d = 4, orders beyond eps^4, analytic tails, uniformity in k or T.
