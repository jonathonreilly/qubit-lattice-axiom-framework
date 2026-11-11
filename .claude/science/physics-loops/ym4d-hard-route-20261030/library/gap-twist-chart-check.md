lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-11T16:51Z

# Check of `library/gap-twist-chart.md`, Theorem (CH) (FINISH row 695)

Provenance: Claude Opus 5.5, high effort, Mac mini worker 2, at commit dade30a82. Line-by-line check of a text written by Claude Fable 5.2 medium (row 679). Not an audit. The checker did not write any of the checked text.

## Repo search

- `grep -l gap-twist-chart library/*.md`: hits in `gap-skeleton-final.md` (13.2 records the result, line 303 says the check is row 695), `gap-skeleton-max.md` (the brief), `gap-twist-port.md`, `gap-ac-lat.md` (both only name row 679 as another statement). `library/open-registry.md` and `library/open-core.md` have no entry for (CH). No existing check of (CH) was found, so this check proceeds.

## Point 1. Lemma L (product structure, anticommutation, gap)

**Verdict: HOLDS.**

- *Transports.* With Gamma_1 = i sigma_1, sigma_1 sigma_c sigma_1 = sigma_c for c = 1 and -sigma_c otherwise, so Ad(Gamma_1) = diag(1, -1, -1); likewise Ad(Gamma_2) = diag(-1, 1, -1). Seam links of direction 1 flip colours 2, 3; of direction 2 flip colours 1, 3. So colour 1 is antiperiodic in direction 2, colour 2 in direction 1, colour 3 in both: **every colour has an antiperiodic fibre direction**, with exactly one sign flip (at j = n-1) along that cycle.
- *(1.1) and D_0, D_1.* Rederived: U_p = V_mu e^{X_mu(y)} V_nu e^{X_nu(y+mu)} e^{-X_mu(y+nu)} V_mu^{-1} e^{-X_nu(y)} V_nu^{-1} (using V_nu(y+mu) = V_nu(y), V_mu(y+nu) = V_mu(y)); moving V_nu left through e^{X_mu(y)} gives Ad(V_nu^{-1}), which is the transport of the link (y+mu, nu), and moving V_mu^{-1} right through e^{-X_nu(y)} gives Ad(V_mu^{-1}), the transport of (y+nu, mu). Then U_p = W E_p W^{-1} z_p with z_p central, as in (1.1). d_p = 1 - (1/2) tr E_p on and off P_0. The linearisation of (1.2) is X - D_0 lambda with D_0 as defined. D_0^* is the adjoint (tau orthogonal and symmetric).
- *Product structure.* The sign of colour c on the link (y+mu, nu) is s_nu(x_nu(y)), so it depends only on direction and on the coordinate in that direction; the twisted complex of each colour is the tensor product of the four one-dimensional twisted complexes. I rechecked that d equals D_0 on sites and D_1 on links, including the sign gamma_mu = -1 in front of the slot-nu difference for X_mu (mu < nu): -(X_mu(y+nu) - s_nu X_mu(y)) + (X_nu(y+mu) - s_mu X_nu(y)) = (D_1 X)(y; mu, nu).
- *Anticommutation.* For nu < rho, d_nu d_rho^* and d_rho^* d_nu agree in all slots but slot nu, where they read delta_nu gamma_nu = delta_nu and gamma_nu delta_nu = -delta_nu. For nu > rho the slot-rho factors are delta_rho^* gamma_rho = -delta_rho^* and gamma_rho delta_rho^* = delta_rho^*. So all cross terms cancel and (2.1) holds on cochains of every degree; the slot term is block-diagonal, delta^* delta on E^0 and delta delta^* on E^1.
- *Chain fact.* The antiperiodic extension F(j+n) = -F(j) turns the sum into the plain difference sum; the antiperiodic Fourier modes are k = (2m+1) pi/n, and min (2 - 2 cos k) = 2 - 2 cos(pi/n) = 4 sin^2(pi/2n) = mu_n. On the cycle delta is square, so delta delta^* has the spectrum of delta^* delta. Hence the slot-i(c) term is >= mu_n on E^0 + E^1, the other slots are >= 0, and Lemma L follows for all cochains, (i) for 0-cochains (d^* = 0 there) and (ii) for 1-cochains with d^* X = D_0^* X = 0.

**Own derivation (n = 2, by hand).** On Z/2 with s(0) = 1, s(1) = -1, the matrix of delta (rows: edges [0,1], [1,0]; columns: f(0), f(1)) is [[-1, 1], [1, 1]]. Then delta^T delta = [[2, 0], [0, 2]] and delta delta^T = [[2, 0], [0, 2]]. So the antiperiodic slot operator is exactly 2 I on E^0 + E^1, and by (2.1) the twisted Hodge Laplacian is 2 + (non-negative) >= 2 = (2 sin(pi/4))^2 = mu_2 on every cochain, with equality attained (the periodic slots have kernel). A second route for (i) only, without the Hodge identity: |D_0 lambda|^2 is at least the sum over the links of direction i(c) of colour c, which splits into chains along the fibre cycles of direction i(c), each >= mu_n times the sum of lambda_c^2 on that cycle by the chain fact; summing over cycles and colours gives |D_0 lambda|^2 >= mu_n |lambda|^2. Both agree with the file.

## Point 2. Lemma G (Combes-Thomas / Schur, rate, K_n)

**Verdict: HOLDS.**

- (i) T = M Delta_0 M^{-1}; for real u, <u, T u> = sum Delta_0(y, y') cosh(alpha(phi(y) - phi(y'))) u(y) u(y'). The weight is 1 on the diagonal and on fibre neighbours (phi depends only on the base point; this also covers n = 2, where two fibre links join the same pair of sites). Base neighbours: one link, |A(y, y')| = 1, |phi(y) - phi(y')| <= 1. The Schur bound sum over ordered base pairs |u(y)||u(y')| <= sum_y deg_base(y) u(y)^2 <= 4 |u|^2, and cosh(a) - 1 <= a^2 for a <= 1 (cosh 1 - 1 = 0.543), give a perturbation of at most 4 alpha_n^2 = mu_n/2. With Lemma L(i), <u, T u> >= (mu_n/2)|u|^2, so ||T^{-1}|| <= 2/mu_n and each kernel entry e^{alpha(phi(y) - phi(y'))} g_c(y, y') is at most 2/mu_n. With phi = -|b - b(y)|_1 this is the claimed decay. alpha_n <= 1/2 <= 1 holds because mu_n <= 2 for n >= 2.
- Rate: alpha_n = sqrt(mu_n/8) >= 1/(sqrt 2 n) since sin(pi/2n) >= 1/n gives mu_n >= 4/n^2. Correct.
- (ii) Minkowski over colours gives |(G_0 f)(y)| <= sum m(y, y') |f(y')|; w(y) <= w(y') e^{(alpha/2)|b - b'|}; sum over Z^2 of e^{-t|b|_1} = coth(t/2)^2 <= (1 + 2/t)^2 with t = alpha_n/2 >= 1/(2 sqrt 2 n), so coth <= 1 + 4 sqrt 2 n <= 7n; total (2/mu_n) n^2 49 n^2 <= (n^2/2)(49 n^4) = 24.5 n^6 <= 25 n^6 = K_n. Correct. The remark on the heat-kernel bound is labelled "not used" and is not used.

## Point 3. Group estimates G1-G4

**Verdict: HOLDS.** C_3 and C_4 come **from compactness only** (supremum of a continuous function on a compact set); neither is given a value. That is an admissible "stated existence argument" under GOAL.md, but every constant downstream (eps_1, eps_2, delta_0, C_c) is explicit only up to C_3, C_4.

- G1: d_p = 1 - cos(t/2) = 2 sin^2(t/4) >= t^2/(2 pi^2), so t <= pi sqrt(2 d_p); rho(U_p, z_p) = |log(z_p U_p)| since z_p is central. Correct.
- G2: inner product of S with Gamma_1 S Gamma_1^{-1} is 1 - 2(s_2^2 + s_3^2) >= cos(omega/2) >= 1 - omega^2/8; adding the two directions gives |s|^2 <= s_1^2 + s_2^2 + 2 s_3^2 <= omega^2/8; rho = 2 arcsin|s| <= pi |s| <= (pi/(2 sqrt 2)) omega = 1.111 omega. Correct.
- G3: Re(A B A^{-1} B^{-1}) = b_0^2 + (R b).b <= -1 + kappa, (R b).b >= 2|b_par|^2 - |b|^2, hence 2 b_0^2 + 2|b_par|^2 <= kappa <= eta^2/8; the same for a_0 by inverting the commutator. After the rotation, cos(rho/2) = |a| (resp. |b_perp|) and sin(rho/2) = |a_0| (resp. sqrt(b_0^2 + |b_par|^2)) <= sqrt(kappa/2) <= eta/4, so rho <= pi eta/4 <= 1.2 eta. a != 0 and b_perp != 0 are justified. Correct.
- G4: the product of three (four) exponentials of norm <= 1/2 is within 3/2 (2) of 1, away from -1, where log is analytic (d exp is invertible for |X| < 2 pi: ad X has eigenvalues 0, +-i|X|). N_3, Q_4 vanish to second order at 0; (3.1) follows from |DN_3(v)| <= C_3 |v| on the convex set containing 0 and the segment; N_3(0, b, 0) = 0; (3.2) is Taylor's bound. Correct.

## Point 4. Lemma R (Steps A, B, C)

**Verdict: HOLDS.**

- Step A: the tree (row x_2 = 0 in direction 1 for x_1 < n-1, all columns in direction 2 for x_2 < n-1) has n^2 - 1 links, reaches every site, and consists of non-seam links (V = 1). I rechecked each plaquette: at (x_1, x_2 - 1) with x_1 <= n-2 both vertical links are tree links and z_p = 1; at (n-1, x_2 - 1) the vertical links are U_2(0, .) and U_2(n-1, .), both in the tree, and z_p = Gamma_1 Gamma_1^{-1} = 1; at (x_1, n-1), x_1 < n-1, the top link U_1(x_1, 0) is a tree link and z_p = 1. The count eta = (1 + (n-1) + n(n-1)) theta = n^2 theta is right, and eta <= 2 follows from 27 n^3 theta < 2 pi. After G3 and the constant gauge k the bound on all fibre links is max((n-1) theta + 1.2 n^2 theta, n(n-1) theta + 1.2 n^2 theta) <= 2.2 n^2 theta = eps_f. Correct.
- Step B: replacing the two fibre links of the (mu, a) plaquette by V_mu(x) (the same on both fibres) gives theta_1 = theta + 2 eps_f <= 5.4 n^2 theta; n steps around the mu-cycle conjugate by the product of the V's, which is Gamma_mu; n theta_1 <= 5.4 (2 pi/27) < 2 permits G2; rho(S(x), e(x)) <= 6.48 n^3 theta <= eps_0; a sign change between fibre neighbours would need 2 pi <= 2 eps_0 + theta_1 <= 18.4 n^3 theta < 2 pi. Correct.
- Step C: the four signs of a base plaquette multiply to within theta + 4 eps_0 = (1 + 26 n^3) theta <= 27 n^3 theta < 2 pi of 1, hence to 1. I re-ran the induction for zeta: zeta(b) zeta(b + e_3) = e_3(b_3, 0) prod_{j < b_4} e_4(b_3, j) e_4(b_3 + 1, j), and the flatness at (b_3, b_4 - 1) gives the step. The paths used (row b_4 = 0, then the column at b_3) lie in the rectangle. **Flat Z_2 signs over a rectangle are a pure gauge: correct** (the rectangle is simply connected; the proof is the explicit zeta). After the central gauge zeta every base link is within eps_0 of e_a(b)^2 = 1 = V_a, and eps_f <= eps_0, eps_0 < 2 pi, so X^0 = log(V^{-1} U^h) has |X^0| = rho <= eps_0. Correct.

## Point 5. Lemma T (contraction, ball, constants)

**Verdict: HOLDS.**

- Transversality of F(lambda, X^0) = X^0 - D_0 lambda + N is equivalent to lambda = G_0 D_0^*(X^0 + N), since Delta_0 is invertible (Lemma L(i)).
- Ball: sup |lambda| <= r = 2 K' eps_0, with r <= eps_1/3 <= 1/2 and eps_0 <= r, so all arguments of L_3 are in the domain of G4. 8 e^{1/2} K_n = 13.19 K_n <= 14 K_n = K'. 2.5 C_3 K' r <= 2.5 C_3 K' eps_1/3 = 2.5/(36 n) <= 1/2.
- (5.1): |u| <= sqrt 3 r, |u - u'| <= sqrt 2 max, sqrt 6 <= 2.5; the second bound uses u_0 = (0, X^0_l, 0) and N_3(u_0) = 0. Correct.
- Self-map: K' eps_0 + K' 2.5 C_3 r^2 <= r/2 + r/2; contraction constant <= 1/2; the ball is closed in a finite-dimensional space, so Banach's theorem applies. |X_l| <= eps_0 + 2r + 2.5 C_3 r^2 <= r/2 + 2r + r/(2K') <= 3r. Correct.

## Point 6. Lemma Q (uniqueness among small charts)

**Verdict: HOLDS.**

- g(y+mu) = e^{-X'_l} V_l^{-1} g(y) V_l e^{X_l} (rechecked by inverting the link relation), so rho(g(y+mu), V_l^{-1} g(y) V_l) <= 2 eps. Around a fibre cycle of direction i the V's multiply to Gamma_i, so rho(g(y), Gamma_i^{-1} g(y) Gamma_i) <= 2 n eps <= 2; G2 gives rho(g(y), z(y)) <= 2.4 n eps = r_eps. A sign change across a link would need 2 pi <= 2 r_eps + 2 eps < 3. Sigma_B is connected. r_1 = 2.4 n eps_1 = 1/(5 C_3 K') is right.
- The constant z cancels from the gauge action; X' = F(lambda, X) because exp is injective on {|X| < 2 pi} and both sides lie there; transversality of both gives lambda = G_0 D_0^* N(lambda, X); with eps <= eps_1 <= r_1 (so (5.1) applies at radius r_1) the map has constant K' 2.5 C_3 r_1 = 1/2, hence lambda = 0. Correct. The uniqueness is only among charts with sup |X'| <= eps_1(n), as the file says (difference (i) from the brief).
- Proof of (a): composition (U^{h_1})^g = U^{g h_1} rechecked; gauge invariance of X via the chart h k^{-1} of U^k and Lemma Q. Correct.

## Point 7. Part (b), A^tw >= (mu_n/16) |X|^2

**Verdict: HOLDS.**

- Y_p = (D_1 X)_p + Q_p with Q_p = Q_4(u_p), all four arguments of norm <= eps <= 1/2. |Q_p| <= (C_4/2)|u_p|^2 <= C_4 eps |u_p|; each link lies in at most 6 plaquettes (also for n = 2: the two (1,2)-plaquettes through a link sit at distinct sites), so ||Q||_2 <= sqrt 6 C_4 eps |X|.
- sqrt 6/13 = 0.188 <= 0.2 <= sqrt(mu_n)/10 times n, so ||Q|| <= sqrt(mu_n)|X|/10; with Lemma L(ii) (X transverse), |Y| >= 0.9 sqrt(mu_n)|X|.
- |Y_p| <= 4 eps + 2 C_4 eps^2 <= 1; 1 - cos(t/2) >= (t^2/8)(1 - t^2/48) >= (47/48) t^2/8 on [0, 1]; (47/48)(1/8)(0.81) = 0.0991 >= 1/16. Correct. The chart of (a) has sup |X| <= C(n) sqrt(delta) <= eps_2, so (b) applies to it.

## Point 8. Parts (c) and (c'), locality, rate 1/(3n)

**Verdict: HOLDS AFTER CORRECTION** (a constant, only when r is not an integer).

Checked and correct:
- R intersected with B is connected (monotone coordinate moves toward b_0 stay in R and in the rectangle).
- Step 1: g = h' h^{-1} satisfies the link relation on every link with both ends over R; the first half of Lemma Q uses only the fibre cycles over one base point (all inside R) and connectedness, so g = z exp(lambda) over R with |lambda| <= r_eps, and X' = F(lambda, X) there.
- Step 2: for y over R^o all links at y have both ends over R, and since B and B' agree on R the set of links at y is the same in both lattices, so the two transversality equations at y give Delta_0 lambda = D_0^* N(lambda, X) at y. f vanishes over R^oo, and |f| <= 16 sup|lam| + 8 (2.5 C_3 r_eps) sup|lam| <= 17 r_eps.
- Step 3: the weighted bounds |Nt|_w <= 2.5 C_3 r_eps e^{alpha/2} |lam|_w and |D_0^* Y|_w <= 8 e^{alpha/2} |Y|_w (weight of a link at its start; neighbouring weights differ by at most e^{alpha/2}), Lemma G(ii) with phi = -|b - b_0|_1, and 8 e^{alpha} K_n 2.5 C_3 r_eps <= K' 2.5 C_3 r_1 = 1/2 give |lam|_w <= 2 K_n |f|_w.
- Step 4: 3m = 102 K_n r_eps e^{alpha_n} e^{-alpha_n r/2} <= 102 x 25 x 2.4 x e^{1/2} n^7 eps e^{-alpha_n r/2} = 1.009 x 10^4 n^7 eps e^{-alpha_n r/2} <= 1.1 x 10^4 n^7 eps e^{-alpha_n r/2}; eps <= C(n) max(sqrt delta, sqrt delta'); alpha_n/2 >= 1/(2 sqrt 2 n) = 0.354/n >= 1/(3n). The case r < 2 is covered by 2 eps <= C_c e^{-1/2}(...).

The broken line: Step 3, "f vanishes over R^oo, so |f|_w <= 17 r_eps exp(-(alpha_n/2)(r-1))". f can be non-zero at base distance d > r - 2, and base distances are integers, so d >= floor(r) - 1, which is below r - 1 when r is not an integer (r = 2.5: d = 1 = r - 1.5). Then Step 4 gives the bound with floor(r) in place of r.

Correction (written in full): in (c) and (c') take r to be a non-negative integer. This loses nothing, because the hypothesis "U = U' on links whose ends have base distance at most r" depends only on floor(r). For a real r >= 0 the conclusion holds with r replaced by floor(r), or equivalently with C_c(n) replaced by e^{1/4} x 1.009 x 10^4 n^7 C(n) <= 1.3 x 10^4 n^7 C(n) (from e^{-alpha_n floor(r)/2} <= e^{alpha_n/2} e^{-alpha_n r/2} and alpha_n <= 1/2). With r an integer, (c) and (c') hold as written, including the version on two different rectangles.

## Point 9. Arithmetic of the constants

**Verdict: HOLDS** (one harmless slip).

- K_n = 25 n^6 >= 24.5 n^6; K' = 350 n^6 >= 8 e^{1/2} K_n = 329.7 n^6; eps_1 = 1/(12 C_3 K' n) = 1/(4200 C_3 n^7); eps_2 = min(eps_1, 1/(13 C_4 n)) (the min is needed: C_4 is not compared with C_3).
- C(n): 6 K' x 6.5 n^3 x pi sqrt 2 = 2100 x 6.5 x 4.44288 n^9 = 60645.3 n^9. The file writes 60647 n^9; the correct value is 60645.3 n^9. Both are below 6.1 x 10^4 n^9, so nothing changes.
- delta_0 = (eps_2/C(n))^2: then 6 K' eps_0 <= C(n) sqrt(delta) <= eps_2 <= eps_1 (Lemma T and part (b)), and 27 n^3 theta = (27/6.5) eps_0 <= eps_2 < 2 pi (Lemma R). Order: delta_0 <= (4200 x 6.1 x 10^4 C_3)^{-2} n^{-32} = (2.56 x 10^8 C_3)^{-2} n^{-32}. Correct.
- r_1 = 2.4 n eps_1 = 1/(5 C_3 K'); 2.5 C_3 K' r_1 = 1/2; 2.5/(36 n) <= 1/2. Correct.
- C_c(n) = 1.1 x 10^4 n^7 C(n) = 6.71 x 10^8 n^16 (status block: 6.7 x 10^8 n^16). Correct for integer r (Point 8).

## Point 10. The free base boundary

**Verdict: HOLDS.** Every place where the boundary of B enters:

- Hodge form: Sigma_B is the product of two cycles and two intervals {0..L_nu}; d is the coboundary of this complex and d^* its adjoint, which at a boundary site has fewer terms; the interval slot operators are >= 0 (and 0 if L_nu = 0); the gap comes from a fibre slot, so no boundary condition is needed. Transversality is imposed at every site, boundary sites included, with that d^*. Correct.
- Green function: Lemma L(i) holds on Sigma_B as it is; in the Combes-Thomas step a boundary site has fewer than four base neighbours, which only helps the Schur bound; the sum over B is bounded by the sum over Z^2. Correct.
- Gauge fixing: Steps A and B work fibre by fibre and link by link, so the boundary plays no role; Step C uses only that B is a rectangle (the zeta paths stay in B, and a flat Z_2 field on it is a pure gauge). Lemmas T and Q use D_0^*, Delta_0 and G_0 of Sigma_B as defined. In (c') the boundary enters through "B and B' agree on R", which is exactly what makes the set of links at a site over R^o the same in both lattices. Correct.

## Summary table

| # | Point | Verdict |
|---|---|---|
| 1 | Lemma L: product structure, anticommutation, gap mu_n on all cochains, antiperiodic direction for every colour | HOLDS (n = 2 rederived by hand: slot operator = 2 I) |
| 2 | Lemma G: Combes-Thomas/Schur, rate alpha_n >= 1/(sqrt 2 n), K_n = 25 n^6 | HOLDS |
| 3 | G1-G4 | HOLDS; C_3, C_4 from compactness only, not explicit |
| 4 | Lemma R, Steps A, B, C; flat Z_2 over a rectangle is pure gauge | HOLDS |
| 5 | Lemma T: contraction, ball r = 2 K' eps_0, constants | HOLDS |
| 6 | Lemma Q: uniqueness among charts with sup abs(X') <= eps_1 | HOLDS |
| 7 | Part (b), mu_n/16 | HOLDS |
| 8 | Parts (c), (c'), rate 1/(3n) | HOLDS AFTER CORRECTION: r an integer (or C_c times e^{1/4}, i.e. 1.3 x 10^4 n^7 C(n)) |
| 9 | Constants C(n), C_c(n), eps_1, eps_2, delta_0, K_n, K' | HOLDS (60647 should read 60645.3; no effect) |
| 10 | Free base boundary | HOLDS |

No defect breaks a statement. The file's numerical check (its section 9) was not used as evidence. No numerics were run for this check.

**What a consumer may use.** Theorem (CH) (a), (b), (c) and (c') of `library/gap-twist-chart.md`, for every n >= 2 and every rectangle B with free base boundary, with the base radius r in (c), (c') a non-negative integer, and the constants of its 8.1: mu_n = (2 sin(pi/2n))^2, alpha_n = sqrt(mu_n/8), K_n = 25 n^6, K' = 350 n^6, eps_1 = 1/(4200 C_3 n^7), eps_2 = min(eps_1, 1/(13 C_4 n)), C(n) = 6.1 x 10^4 n^9, delta_0(n) = (eps_2/C(n))^2, lower bound (mu_n/16) sum abs(X_l)^2 in (b), C_c(n) = 1.1 x 10^4 n^7 C(n) and rate 1/(3n) in (c). C_3 and C_4 are the absolute bounds of G4, defined by compactness and not given values, so delta_0(n) is explicit only up to them. Label after this check: checked line by line by a model that did not write it (Claude Opus 5.5 high). No other provider has checked it.

RESULT: All ten points of (CH) in `gap-twist-chart.md` hold. Nine hold as written. Point 8, locality (c)/(c'), holds once r is read as an integer, or with C_c raised to 1.3e4 n^7 C(n) for real r. There is one harmless arithmetic slip (60647 for 60645.3). C_3 and C_4 come from compactness only. Open: their explicit values, and everything the row excluded (regions with holes, the bad-region bound, derivative bounds of U -> X).
