# UI gate: one check of library/ui.md (Lemma 4.5 lem-uniform-increment, step (*))

First failing step: none

Verdict: completed as stated, on the account's standing analytic inputs (CA-I 19585-19596).
Checked line by line by Claude (fresh session).

## Q1. The marked step and the continuation (CA-I)

- Heading CA-I 16019: "Stated; proof incomplete at the step marked $(\ast)$".
- The step (*) is CA-I 16233-16240. It names the route (top-layer placement, exact
  recentring in level-n units, kernel read at the top point, exponential decay under
  delta_0 M >= 32) and says "this argument is not carried out in the present proof".
  It also holds the collar bound R_1 M_1 for the maximal tower (16239-16240).
  What it leaves open: the increment bound (4.5:eq-uniform-increment-a) itself; the
  rest of the proof at 16242-16265 derives the alpha_0 bounds from it.
- The proof environment closes at 16266. The continuation then opens at 16268-16269:
  "We begin the proof of Lemma~\ref{4.5:lem-uniform-increment}." It has four parts:
  geometry 16268-16460, kernel 16462-16730, recentring 16732-16937 (ends with
  (4.5:eq-increment-recentring-5) |dPhi_i/dt| <= (1/2) C_IV alpha_2 lambda^2,
  C_IV := max{2(C'+C'''), 4C_14}), conclusion 16939-16990 (integration in t and the
  alpha_0 bounds).
- Verdict on Q1: the continuation does carry out (*) on the stated route; it does not
  stop short. The status line at 16019 and the sentence at 16238-16239 are stale.
  ui.md 20-30 states this correctly.
- Defects seen in the continuation (not stops): (a) the kernel display 16723 has rate
  delta_0/4 (see Q4 for whether the cited input gives that); (b) the collar step
  16874-16883 lets chi live on all of Q, so a bond crossing the edge of Q can carry
  nu != 0 at one end outside the local gauge, where Ad_U is not controlled; (c) the
  conclusion 16942 cites the kernel display (eq-increment-kernel-a) where the bound
  (eq-increment-recentring-5) is meant (label slip); (d) the near-cube estimate
  16863-16867 leaves the commutator part of the telescoping implicit.

## Q2. Does ui.md prove exactly the marked step, on their route?

Route: yes. ui.md uses their route: top-layer placement (§3), real base and complex datum
(7), kernel at the top point (9), exact infinitesimal recentring (§4), near/far split (§6).
It does not claim a new mechanism (ui 32-34, 553-558).

Line checks (all pass):
- ui 150-160, top layer. x has depth >= 2M/lambda = 2r. If |z-x_0|_inf <= r/2+2 then
  |z-x|_inf <= r/2+3, so depth(z) >= 3r/2-3 >= r when r >= 6. Also r >= M >= 2R_1M_1 >= 8d.
  Then r > r/2 >= depth(X \ Omega_n), so z is in Omega_n. This matches CA-I 16397-16418.
- ui 162-176, (5). Sum_{p<n} ell_p < 1/(L-1) <= 2/L. And 2(R_1+dL)/L <= R_1 is the same as
  2dL <= (L-2)R_1, which holds by L >= 4d and R_1 >= L. Level-n to level-j is a factor
  lambda <= 1. Then the floor 2R_1M_1 <= M. This matches CA-I 16337-16371. The induction is
  shortened but present in the source.
- ui 178-194, (6). The cube Q has side 2M <= c_12 L M (by c_12 L >= 2). (rho1) at CA-I
  13096-13099 reads (1.12) on every cube of side at most c_12LM, so the gauge is licensed.
  |hat A_0| <= (1/2)c_12LMB alpha_0 lambda. s = a_0^Q + alpha_1/2 + alpha_2 <= c_sharp is
  exactly the third ceiling.
- ui 200-208, (7). Same as CA-I 16556-16561, with the second ceiling.
- ui 214-224, the log differential. |B_t| <= (1/2)C_1 eps_1 <= 1/8, because C_1 eps_1 <= 1/4
  (CA-I 16067). e^{1/8}-1 = 0.133 <= 1/7 and e^{1/8} = 1.133 <= 8/7. The series derivative
  is <= (1-1/7)^{-1} = 7/6, and 7/6 * 8/7 = 4/3 < 2. Correct.
- ui 299-312, cutoff. A piecewise-linear chi in |z-x_0|_inf with radii r/2 and 3r/4 has
  slope 4/r, so every coordinate difference quotient is <= 4/r. Support radius 3r/4 plus one
  bond (eta <= 1 < r/4) stays inside Q, so every bond with nu != 0 at an end lies where the
  local gauge holds. This repairs CA-I 16741-16744, where chi may reach the edge of Q.
  |nu| <= alpha_2 lambda * d * 3r/4 <= dM alpha_2. Correct.
- ui 314-355, (12)-(13), the Ward identity. The gauge-orbit velocity under
  U^w(b) = w(b_-)U(b)w(b_+)^{-1} (CA-I 12656) is
  (1/(i eta)) dW^{w}/dz W^{-1} = (nu(b_-) - Ad_W nu(b_+))/eta = -D_W nu. The t-velocity of
  e^{it eta hat A}U is hat A. The block-constant map is e^{iz nu(x_0)} = 1 on Delta(y_x),
  and both readouts transform only at x. So D Phi_i(W_t)[D_W nu] = 0 and
  dPhi_i/dt = D Phi_i(W_t)[hat A + D_W nu]. The extension route is sound: identity for real
  gauge and real data; holomorphy in the data at fixed small real gauge; derivative in a
  real direction; then complex-linearity in nu (nu -> D_W nu and D Phi_i are both
  complex-linear). This is simpler than CA-I 16764-16808 and gives the same result.
- ui 359-369, (14). ||Ad_{e^{iX_1}e^{iX_2}e^{iX_3}} - 1|| <= e^{2 sum|X_k|} - 1, and
  sum|X_k| <= eta lambda s. u = 2 eta lambda s <= 1/2, so e^u - 1 <= u/(1-u) <= 2u.
  This gives 4 eta lambda s <= eta lambda. Correct.
- ui 371-382, (15), covariant difference. The one-bond conjugation difference is
  <= eta^{-1} * eta lambda * alpha_2 lambda = alpha_2 lambda^2. So
  |nabla_0 hat A| < 2 alpha_2 lambda^2. This states the commutator term that CA-I 16869-16870
  leaves in words.
- ui 384-396, (16). eta D_W nu(b) = nu_0(z+eta e_mu) - nu_0(z) + (Ad-1)nu_0(z+eta e_mu)
  = -eta hat A_mu(x_0) + (Ad-1)nu_0(z+eta e_mu). Telescoping (15) along a coordinate path
  inside the inner cube gives 2 alpha_2 lambda^2 |z-x_0|_1. The second term is
  <= lambda * alpha_2 lambda (|z-x_0|_1 + eta). The total is <= 3 alpha_2 lambda^2(|z-x_0|_1+1).
  Correct.
- ui 398-413, (17). Product rule: |nabla_0 nu_0| < alpha_2 lambda, and
  |nu_0||nabla_0 chi| <= alpha_2 lambda * d r * 4/r = 4d alpha_2 lambda. The conjugation term is
  <= lambda * dM alpha_2. Adding |hat A| gives (2+4d+dM) alpha_2 lambda <= (2+5d)(1+M) alpha_2 lambda.
  Outside the support D_W nu = 0. Correct.
- ui 417-431, (18), near part. ell^d ell^{-d} = 1, ell_c <= 1, and (10). The bound
  (u+1)e^{-sigma u} <= (1+2/(e sigma)) e^{-sigma u/2} holds because
  max_u u e^{-sigma u/2} = 2/(e sigma). Then (4) at rate sigma/2. Correct.
- ui 433-442, (19), far part. D_c >= M/(2 lambda) - c_g. Split the exponential in halves:
  one half is summed by (4), the other gives e^{-(sigma/2)(M/(2lambda) - c_g)}
  = e^{sigma c_g/2} e^{-sigma M/(4 lambda)}. Correct.
- ui 444-462, (20)-(22), weaker-rate tail. a = sigma M/4 = delta_0 M/32 >= 1 by the floor.
  v e^{-v} <= 1/e at v = a/(2 lambda) gives e^{-a/(2lambda)} <= 2 lambda/(e a) <= (2/e) lambda.
  The other half is <= e^{-a/2} = e^{-sigma M/8}. Also (1+M)e^{-sigma M/8} <= 1 + 8/(e sigma).
  Then F = (2/e)F_0(1+8/(e sigma)). Correct, and M-free.
- ui 464-477, (23). C_IV = max{4C_14, 2(N+F)} gives |dPhi/dt| <= (N+F) alpha_2 lambda^2
  <= (1/2)C_IV alpha_2 lambda^2. The analytic path on [0,1] and the fundamental theorem of
  calculus give (2). N and F are built from c_g, C_A, K, S, sigma, C_f; none uses M, n, j or X.
  This matches the order slot at CA-I 19411 (C_IV and C_14 in stage 2, before M_1 at 19417
  and M at 19430). C_IV >= 4C_14 is kept.
- ui 479-496, (24)-(25), both halves. Strict: |Phi_i(W_0)| < (1/2)alpha_0 lambda^2, the
  increment is <= (1/2)alpha_0 lambda^2, so the sum is < alpha_0 lambda^2. eta^2 lambda^2 = xi^2.
  The U half is unchanged (same G-valued U). Matches CA-I 16242-16265 and 16951-16968.

Floors and ceilings used: delta_0 M >= 32 (via a >= 1); 2R_1M_1 <= M (geometry); c_12 L >= 2
(gauge cube); L >= 4d (collar sum); the second and third ceilings ((7), (6)); and
alpha_2 <= alpha_0/C_IV. No new floor or ceiling appears. No comparison of alpha_0 with
alpha_1, and no M alpha_1 or M alpha_2 smallness.

Items taken as in the source (inherited, not new; same standing as the continuation):
- ui 239-265, the derivative of g. This is a scale-count sketch on the consumer-assumed
  frame-map and averaging inputs (CA-I 19585-19596). The source has only "O(sup|dot H|)"
  at 16674-16676. ui is no weaker than the source here. I did not check it further.
- ui 282-295, (10). That the hierarchy distance dominates physical displacement up to a fixed
  offset is asserted, as at CA-I 16887-16888. This holds if d(y,y') of CMP96 (2.46) is
  measured in local block units ell_q, as the gap floors in R_1 M_frak (CA-I 13411-13416)
  suggest. I did not read the primary here.
- ui 228-237 (plaquette first variation) and (8) (current variation): finite expansions on
  the supplied value, gradient and D*D members, as at CA-I 16669-16707.

## Q3. Consumers

- CA-I 19781-19790 ((F1)). It applies the lemma to A(t_square) with amplitude (2/3)alpha_2,
  and takes (i), (ii), the first member of (1.14), and (iv) in the uniform form at
  (alpha_0, alpha_1). ui (24)-(25) give (iv) for e^{i xi A}U on every sub-tower. The U half
  and (i)-(ii)-(iii)_1 are CA-I 16158-16231. The current member is the consumer's own
  (19787-19790). Supplied exactly.
- CA-I 19825-19833 ((F6)). This reads only admissibility and the collar <= M/2, applied to the
  maximal tower of X; the window tower is covered only where (iv) is established for it.
  ui 162-176 gives the maximal-tower collar, and ui 175-176 and 529 keep the general tower as
  a hypothesis. Supplied exactly. No window admission is inferred.
- The label-use list in ui 519-533 matches a grep: CA-I 16020, 16269, 16373, 16462, 16939,
  17928, 19525, 19783, 19828, 19915, 19943, 19985, 20001, 20053, 20118; none in CA-II or CA-III.

## Q4. Cited inputs

- Balaban (190). The first-derivative rate is delta_0/8: CA-III 35612-35618 quotes it as
  printed, and CA-II 85863-85870 states the value and gradient members at e^{-delta_0 d/8}.
  CA-I 10200-10203 also says "the rate delta_0/8 of (190)" for all five members, including
  D*D. So ui's sigma = delta_0/8 (ui 139-145) is the rate as stated. The continuation's
  delta_0/4 at CA-I 16723 is not given by that input. ui's correction is right, and §6
  shows the original floor still suffices.
- The sum (4) at sigma/2 = delta_0/16 is covered by the kernel-algebra floor at the fraction
  1/16 (CA-I 13411-13416, 19447-19450).
- Balaban (189) is not used (ui 134-136), consistent with "printed without proof" at
  CA-III 35577-35624.
- C_H is used only through sup|H| <= r_g <= 1 (CA-I 16614-16627) and the value, gradient and
  D*D members. These are the statements the consumer assumes at CA-I 19588-19590. ui keeps
  them as cited inputs and claims no closure (ui 130-137, 556-559).

## Minor (no repair needed)
- ui 153: Q subset X is stated without its one line (depth of x_0 >= 2r-1 > r).
- ui 216: |B_t| <= 1/8 uses C_1 eps_1 <= 1/4 (CA-I 16067), not cited.
- The continuation's label slip at CA-I 16942 is not carried into ui.
