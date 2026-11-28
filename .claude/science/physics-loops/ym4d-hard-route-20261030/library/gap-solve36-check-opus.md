# Check of row 1317 (gap-solve36-astra62.md), FINISH row 1318

Checked line by line by hand by Claude Opus 5.5. Each step was derived again here. Line numbers refer to the file at the checkout commit named below.

Source commit: ffbd23e2c

Target: 271 lines, 32 PROVED blocks, 11 GUIDE, 2 OPEN, equations (1)-(17).
Also read: row 1215 (`gap-solve23-astra62.md`, lines 419-464, the four-link
construction behind its (26)-(29)) and row 1218
(`prior/gap-onebound-read-sol.md`, lines 74-101, the window input A-B* and
A-B** of Deep Bhattacharjee, Ushashi Bhattacharya, James Montgomery Lockwood,
Tristan Romanov, Ikailo John Sessford and Sanjeevan Singha Roy).
No numeric run was used.

## Verdicts

### Section 0. Sign and count moduli: (1)-(4) (supports claim 2)

- L23-30, (1). HOLDS. Row 1215, line 435, perturbs on the traceless wall
  of p after making every other incident trace nonzero. So the two closed
  balls have equal indicators on all other incident plaquettes and opposite
  indicators at p. On these two pieces, of mass p_beta each, the phases
  differ by exactly t_p. Then |E| <= 1 - 2p_beta + 2p_beta|cos(t_p/2)|.
  Since 1-|c| >= (1-c^2)/2, this is <= 1 - p_beta sin^2(t_p/2). The colour
  class makes the four-link blocks conditionally independent, and each
  marked phase sees one block only. The product over the best colour gives
  (1) with c = 1/(number of colours). At t_p = pi it is row 1215's bound
  1 - 2p_beta. The threshold extension holds: the balls have strict margins
  on every trace, and a finite subcover keeps them for all small |d|.
- L32-38, (2). HOLDS. 1_z = q^{-B} sum_l prod_i exp(2 pi i l_i(N_i - z_i)/q).
  So D U M_z U(x,y) - U^2(x,y) = U^2(x,y) sum_{l != 0}(phase) E_{x,y}[...],
  with t_p = 2 pi l_i/q on S_i. By (1) each term is at most
  prod_i exp(-c p_beta |S_i| sin^2(pi l_i/q)). With l_i in (-q/2, q/2] and
  Jordan's inequality sin(pi l/q) >= 2|l|/q, the sum of the product over
  l != 0 is at most the stated product minus one. Schedule: 1-cos x < x^2/2
  gives E_* < 1 + 5 pi^2/32, and 1 + 5 pi^2/32 < 3 pi^2/11 is
  41 pi^2/352 > 1, true for pi > 3. So p_beta >= n^{-gamma}, gamma < 1, and
  with k = n, q <= n^{(1-gamma)/4} each exponent is >= 4c n^{(1-gamma)/2}.
  The error is superpolynomially small for polynomial B. The 12-row example
  has k = n, B = n^2. The value 11/(3 pi^2) is the one-loop slope for
  beta = 4/g^2.
- L42-51, (3). HOLDS. With X = sqrt(D) U M, XX* = D U M U = A and
  X*X = D M U^2 M = B_M. Pointwise |A - U^2| <= delta U^2 gives
  |<f,(A-U^2)g>| <= delta <|f|,U^2|g|> <= delta ||f|| ||g||. Weyl then gives
  |rho_i - u_i^2| <= delta, rho_0 in [1-delta, 1+delta], and
  |rho_i/rho_0 - u_i^2| <= (delta + u_i^2 delta)/(1-delta) <= 2delta/(1-delta).
  Here U >= 0 (reflection positivity, Osterwalder-Seiler), so the order of
  u_i^2 is that of u_i. Gauge averaging keeps the pointwise inequality, as
  L21 says.
- L53-59, (4). HOLDS. Tr A^j is a cycle integral of nonnegative kernels.
  The pointwise sandwich gives (1 -/+ delta)^j Tr U^{2j}. Tr B_M^j = Tr A^j.
  Division by rho_0^j in [(1-delta)^j, (1+delta)^j] gives (4). The kernels
  are continuous on a compact space, so the j = 1 diagonal formula holds
  (Tr XX* = ||X||_HS^2). With delta = o(a) and j = O(1/a), j delta -> 0.

### Section 1. The magnetic-action Fourier bound (5)-(6) (claim 1)

- L65-75, statement of (5). HOLDS, by the four blocks below.
- L77 (Laplacian, good set, Hessian). HOLDS. On S^3 a linear coordinate has
  round Laplacian -3 times itself, so Delta(x.Oy) = -6 x.Oy and
  -Delta H = beta(6 x.Oy + 3a.x + 3b.y) <= 36 beta. Integrating
  div(e^H grad H) = 0 gives E_mu|grad H|^2 = -E_mu Delta H <= 36 beta. Markov
  gives mu(|grad H|^2 > 81(1+beta)) <= 36/81 < 1/2. Along a product geodesic
  with speeds v_x, v_y, (x.Oy)'' = -(|v_x|^2+|v_y|^2) x.Oy + 2 v_x.O v_y,
  at most 2|v|^2; the linear terms give at most 5|v|^2. Total 7 beta |v|^2.
- L79 (cap mixture). HOLDS. On a product of caps of radius r the geodesic
  length is <= sqrt2 r. Taylor gives |H(w)-H(z)| <= 9 sqrt(1+beta) sqrt2 r
  + 7 beta r^2 <= 9 sqrt2/8 + 7/64, an absolute C_0. The cap kernel is
  symmetric, dz K_z(dw) = dw K_w(dz), so
  int_G mu(dz) K_z(dw) <= e^{C_0} mu(dw). Hence
  nu = e^{-C_0} int_G mu(dz) K_z <= mu, a mixture of uniform product caps of
  mass >= e^{-C_0}/2.
- L81-90 (mixed phase on one cap pair). HOLDS. Two Cauchy-Schwarz steps
  remove f and then g(Y) - g(Y'), leaving
  |I|^4 <= E cos(beta t (X-X').O(Y-Y')). Chords are <= 2r, so the argument is
  <= 4 beta |t| r^2 <= 1/16. For a cap about x_0, X = cos(theta) x_0 +
  sin(theta) omega with omega uniform on the unit sphere of x_0-perp, so the
  tangent covariance is (E sin^2 theta/3) I and the mixed block vanishes;
  E sin^2 theta >= c r^2 since theta has density proportional to sin^2 theta.
  E[(u.Ov)^2] = tr(Cov u O Cov v O^T) = 4 tr(Sigma_X O Sigma_Y O^T), and
  tr(Pi_{x0-perp} Pi_{(Oy0)-perp}) = 4 - 2 + (x_0.Oy_0)^2 >= 2. So
  1 - |I|^4 >= c beta^2 t^2 r^4 and 1 - |I| >= (1 - |I|^4)/4. With
  beta >= 1, beta^2 r^4 = beta^2/(4096 (1+beta)^2 max(1,t^2)) >=
  1/(16384 max(1,t^2)). So the loss is >= c min(t^2,1). The cap mixture of
  mass m then gives |E_H| <= 1 - m c min(t^2,1).
- L92-97 (high frequencies). HOLDS. Cauchy-Schwarz in x leaves
  int int |int e^{i s x.O(y-y')} dx| dy dy'. A coordinate of a uniform point
  of S^3 has density (2/pi) sqrt(1-u^2), which vanishes at +-1 and has
  integrable derivative; one integration by parts gives
  |phi(lambda)| <= C/|lambda|. The integral of 1/|y-y'| over S^3 is finite
  (sin^2 theta / sin(theta/2) is bounded). So the square is <= C/|s|.
  For e^H: the expansion uses x.Oy = sum_{i=1}^4 x_i (Oy)_i, four products
  of factors of modulus <= 1, so the coefficients sum to e^{4 beta}. (An
  expansion over the 16 matrix entries would give e^{8 beta}; the file's
  four-coordinate reading is the right one.) The linear factors cost
  e^{10 beta}, and Z >= exp(E_Haar H) = 1. With s = beta t this is (5).
- L99-106, (6). HOLDS. Two perpendicular edges sharing a vertex lie in one
  plaquette only. With the other links fixed, w_p = Re(xyQ) = <x-bar, yQ>,
  which is x.Oy with O orthogonal. In a two-step bridge in temporal gauge a
  middle spatial link lies in 4 spatial and 2 temporal plaquettes; the 5
  besides p are linear in that link with unit coefficient vectors, so
  |a|,|b| <= 5. This is the law of (5) with every coefficient beta. The
  marked phase is -beta t_p x.Oy plus one-variable terms. Within one colour
  the pairs are disjoint and no face sees two roots, so the conditional law
  and the phase factor. The best colour carries >= 1/J of
  sum_p -log h_beta(t_p), which gives prod_p h_beta(t_p)^{1/J}. The second
  inequality follows from h_beta <= e^{-c min(t^2,1)}. The constant
  sum_p beta t_p is a unit phase. Gauge averaging at the ends is a convex
  combination of bridges, so the bound survives. The four-torus extension
  holds by the same count: every link lies in 6 plaquettes.

### Section 2. Residues and the original/rounded comparisons (7)-(11) (claim 2)

- L110-115, (7). HOLDS. The Fourier coefficient of (R_b) at l in Z^B is the
  bridge expectation of exp(i sum t_p A_p) with t_p = 2 pi l_b/h on S_b, so
  (6) bounds it by prod_b h_beta(2 pi l_b/h)^{|S_b|/J}. With d = k/J: for
  |2 pi l/h| <= 1 the Gaussian sum over l != 0 is <= C e^{-c k/h^2} once
  k/h^2 is large. For |t| > 1, h_beta^d <= (e^{-c})^{d-4}
  (C e^{14 beta}(1+|t|)^{-1/2})^4, and sum (1 + 2 pi |l|/h)^{-2} <= C(1+h).
  The product structure gives sum_{l != 0} |hat g(l)| <= (1+eta)^B - 1. The
  absolutely summable series is continuous and equals the density.
- L117 (positive reweighting). HOLDS. UWU(u,v) = U^2(u,v) int W g_{u,v},
  and |int W g - W-bar| <= Delta W-bar for W >= 0. For count residues, (2)
  says the residue law is within delta of uniform counting measure, so the
  same follows.
- L119-123, (8). HOLDS. With X = U W^{1/2}, XX* = UWU and X*X = B'. So the
  positive spectrum of B' lies within delta of that of U^2 and
  ||B'|| <= 1 + delta. V^2 and B' have kernels W^{1/2}(x)(UWU)(x,y)W^{1/2}(y)
  and W^{1/2}(x)U^2(x,y)W^{1/2}(y), so |V^2 - B'| <= delta B' pointwise and
  ||V^2 - B'|| <= delta(1+delta). V >= 0, so lambda_i(V)^2 are the ordered
  eigenvalues of V^2. Total error delta + delta + delta^2 = (2+delta)delta.
  Normalization: |lambda_i^2/lambda_0^2 - lambda_i^2| =
  (lambda_i^2/lambda_0^2)|1 - lambda_0^2| <= (2+delta)delta. A uniform
  o(a) error then moves e^{-2ma} by e^{-2ma} o(a), which a fixed slack in m
  absorbs.
- L125-131, (9). HOLDS. Pointwise V^2 within (1 +- delta) B' gives
  Tr V^{2j} within (1 +- delta)^j Tr (B')^j, and
  Tr (B')^j = Tr (UWU)^j is within (1 +- delta)^j Tr U^{2j}. Hence (9) and,
  by 2j-th roots, 1 - delta <= lambda_0(V) <= 1 + delta. For the neutral
  trace each flip-twisted cycle is a nonnegative integral with the same
  pointwise sandwich, because the bridge bound holds for all end pairs and
  W is flip invariant. The top eigenvalue of a strictly positive kernel is
  simple (Jentzsch), so its eigenfunction is flip invariant.
- L133-139, (10). HOLDS. With k ~ (log n)^2 and h = (log n)^{1/4},
  k/h^2 = (log n)^{3/2}. Then e^{-c k/h^2} = n^{-c (log n)^{1/2}}, and with
  beta <= C log n, e^{56 beta - c k} is also superpolynomially small. With
  B = O(n^3/k), Delta <= e^{B eta} - 1 = o(n^{-A}). The uniform mean of W is
  ((e^h - 1)/h)^B, and e^{-S}e^{hR} = e^{-h floor(S/h)} since
  R = S/h - floor(S/h). V = W^{1/2} U W^{1/2} >= 0 is a genuine transfer.
  At even periods 2j = O(n) the normalized trace ratio is
  1 + O(j Delta) = 1 + o(n^{-A}).
- L141 (all periods T >= 3). HOLDS. Tr V^T / Tr U^T is the original
  periodic expectation of prod_t W(x_t) (W normalized). A proper 3-colouring
  of the time cycle makes one colour class a set of independent two-end
  bridges given the rest, each with conditional mean of W in
  [1 - delta, 1 + delta]. Since all factors are nonnegative, removing one
  colour at a time gives [(1-delta)^T, (1+delta)^T]. At a flip seam the
  bridge ends are (x_{T-1}, g x_0), and W(gx) = W(x) keeps the bound.
- L143-147, (11). HOLDS. log Z_rd(s,T) = T log W-bar + log Z(s,T) + e_T
  with |e_T| <= 2 T Delta for Delta <= 1/2. In Psi the T log W-bar terms
  cancel, and |2 e_T - e_{2T}| <= 4T Delta + 4T Delta = 8 T Delta. The
  threshold gamma V(s) with gamma = y_0/(2(96T)^3) and V(s) >= 8T^3 is at
  least 4 y_0/96^3, a fixed constant. Delta is superpolynomially small in T
  on sides in [2T, 48T) at beta = O(log T), so 8 T Delta -> 0 and a bound
  (1 - epsilon) gamma V for Psi^rd gives A-B** for the original action. This
  matches row 1218, lines 84-97. Precision: the conclusion "propagation
  theorem applies" refers to the authors' Theorem 7.56; their mass-gap
  conclusion, Theorem F, also assumes their hypothesis (W) (row 1218,
  line 81).

### Section 3. Integer actions in the rounded bridge (12)-(15) (claim 5)

- L153-157, (12). HOLDS. |E e^{i tau S_b}| <= h_beta(tau)^{k/J} by (6). The
  integral over |tau| <= 1 of e^{-c k tau^2/J} is C k^{-1/2}; the tail is
  C e^{56 beta - c k} as in (7). Gaussian smoothing and dominated
  convergence identify the bounded density.
- L159 (mixed joint bound). HOLDS. The mixed transform factorizes over
  groups by (6); integrating the real frequencies gives L_k each and
  summing the integer frequencies gives (1+eta) each.
- L161-166, (13). HOLDS. The rounded bridge law is the original one times
  W/E_{u,v}W. On N_b = d_b, R_b = S_b/h - d_b, so the integral of e^{hR_b}
  over the bin is int_0^h e^u du = e^h - 1; each free group gives
  (e^h - 1)/h; the denominator is >= (1 - Delta)((e^h-1)/h)^B. The ratio is
  (13). With L_k ~ (log n)^{-1} and h = (log n)^{1/4}, h L_k -> 0, and
  o(sqrt(k)/h) candidate levels still have vanishing total probability.
  The last sentence of the block is a reading, not a theorem; it is
  consistent with (13).
- L168-173 (variance). HOLDS. For small tau, |E e^{i tau X}| =
  1 - tau^2 Var X/2 + o(tau^2) for bounded X, while (6) gives
  <= exp(-c J^{-1} tau^2 sum b_p^2) once tau max|b_p| <= 1. Comparing
  tau^2 coefficients gives c' = 2c/J.
- L179-183, (14) upper part. HOLDS. d(q) = 1 - Re q = |1-q|^2/2. Temporal
  gauge on the first T-1 steps uses only interior vertices, so m = 3N(T-1)
  middle links and N last-step frames remain. Dropping interior magnetic
  terms and last-step non-tree temporal terms only increases Z_{beta/2}.
  Leaf-by-leaf Haar integration of the frames gives z_{beta/2}^{N-1},
  independent of slice T-1; the layers then give z_{beta/2}^m. With
  1 - cos alpha >= 2 alpha^2/pi^2 on [0, pi] and Haar density
  (2/pi) sin^2 alpha, z_beta <= C beta^{-3/2}.
- L185-190, (14) lower part. HOLDS. Caps of angle beta^{-1/2} have Haar mass
  >= c beta^{-3/2}. Chords are <= angles, so each temporal chord is
  <= 3 beta^{-1/2} and each temporal deficit is <= C/beta, over 3NT faces.
  For a middle plaquette |X_p - A_p| <= 4 beta^{-1/2} by bi-invariance and
  subadditivity, and (u+v)^2/2 <= u^2 + v^2 gives
  d(X_p) <= 2 d(A_p) + 16/beta. So Z_beta >= (c beta^{-3/2})^{m+N}
  exp(-CNT - 2 beta T D(A)). Then
  P(E > b) <= e^{-beta b/2} Z_{beta/2}/Z_beta, and b = C_0 T(N/beta + D(A))
  with C_0 >= 4 and C_0 large against C + 1 + 3/2 (using log beta <= NT)
  gives e^{-NT}.
- L192-200, (15). HOLDS. A_2 has period 2R^2 in x_1, and n is a multiple
  of 2R^2. Only 12-plaquettes are nontrivial, each exp(i pi/R^2), with
  deficit 1 - cos(pi/R^2) <= pi^2/(2R^4) <= 5/R^4. An R x R square has
  holonomy exp(i pi) = -1, chord 2. Non-abelian Stokes over the top filling
  and the four side ribbons, with conjugation invariance and subadditivity
  of the chord, bounds 2 by the sum of face chords sqrt(2d). Summed over N
  base points: each top face counts R^2 times, and each 01 or 02 temporal
  face counts 2R times per layer. Cauchy-Schwarz over N top faces and over
  2Nt side faces gives 2N <= R^2 sqrt(2N D_12) + 2R sqrt(2Nt) sqrt(2E),
  which is (15).
- L202-206 (detection). HOLDS. D(A) <= 5N/R^4 and N/beta = N/(K R^4), so on
  the good event E/N <= 6 C_0 T/R^4. Then 4R sqrt(t E/N) <= 4 c_0 sqrt(6C_0)
  < 1 for t < T, so R^2 sqrt(2 D_12/N) > 1 and beta D_12/N > K/2 at every
  interior time. Flat ends give the average <= C_0 T/(T-1) <= 2 C_0. With
  K > 12 C_0 + 12 the two ranges are disjoint.
- L208 (after rounding). HOLDS. e^{h R_b} lies in [1, e^h], so the rounded
  and original middle weights differ by a factor in [1, e^{hB(T-1)}], and
  P_rd(F) <= e^{hB(T-1)} P(F). hB = O(hN/k) = o(N). Each group has one
  orientation, and 0 <= S_b - h N_b < h, so the 12-type rounded sum is
  within hB of beta D_12. The stated failure of an end-independent uniform
  comparison follows; T ~ c_0 (beta/K)^{1/4}.

### Section 4. The free-scalar test (16) and the zero-mass readings (claim 4)

- L212-228, (16). HOLDS. In the middle slice of a two-step bridge each site
  has 6 spatial and 2 temporal neighbours, so the two-site precision is
  [[8+mu^2, -1], [-1, 8+mu^2]] with eigenvalues 7+mu^2 and 9+mu^2 <= 10.
  So C >= I/10 and ||C^{-1}|| <= 10. The edge's own term gives the
  off-diagonal -t_e/2 of D; other incident edges only add diagonal and
  linear terms. Since D = C^{-1/2} M C^{-1/2} with M = C^{1/2} D C^{1/2},
  |t_e|/2 <= ||D|| <= 10 ||M||. After whitening and diagonalizing,
  |E e^{i(lambda Z^2 + bZ)}| = |1 - 2i lambda|^{-1/2}
  exp(-b^2 Re(1/(2(1-2i lambda)))) is the displayed formula. The larger
  |lambda| >= |t_e|/20 gives (1 + t_e^2/100)^{-1/4}. Pairs at graph distance
  >= 2 are conditionally independent and their phases separate, so a
  bounded colouring and the best colour give (16). The Gaussian time
  kernel has positive Fourier multiplier, so the transfer is positive.
  Note: (16) implies the Gaussian-min form of (6),
  (1 + c t^2)^{-1/(4J')} <= exp(-c'' min(t^2,1)), uniformly in 0 < mu <= 1.
  This is what makes the model a test of (6).
- L230-235 (divergent doubling defect). HOLDS. Per spatial mode the time
  precision is circulant with eigenvalues 2cosh(omega) - 2cos(2 pi j/T) =
  e^omega |1 - e^{-omega} e^{2 pi i j/T}|^2. prod_j (1 - z e^{2 pi i j/T})
  = 1 - z^T gives e^{T omega}(1 - e^{-T omega})^2. Then
  2 log Z(T) - log Z(2T) = log[(1 - e^{-2T omega})/(1 - e^{-T omega})^2]
  = log[(1 + e^{-T omega})/(1 - e^{-T omega})] > 0, with the (2 pi)^{T/2}
  and e^{-T omega/2} factors cancelling. For the zero mode
  sinh(omega/2) = mu/2, so omega = 2 arsinh(mu/2) <= mu = a^2 and
  T omega <= a t -> 0, and its term -> infinity. All terms are positive and
  the A-B** threshold on s = (2T,2T,2T) is the constant 4 y_0/96^3. So
  A-B** fails.
- L237-244 (zero mass in a local magnetic reading). HOLDS. The time Green
  function e^{-|l| omega}/(2 sinh omega) solves the difference equation:
  off l = 0 by 2cosh(omega) = 2 + mu^2 + lambda, and at l = 0 by
  A(e^omega - e^{-omega}) = 1. The difference multiplier is
  4 sin^2(k_i/2). With k = ap: a^{-4} times the covariance tends to
  int p_i^2 e^{-t|p|}/(2|p|) d^3p/(2pi)^3 = (4 pi/3) 6 t^{-4}/(2 (2pi)^3),
  a positive multiple of t^{-4}. Domination: 4 sinh^2(omega/2) >=
  sum 4k_j^2/pi^2, so omega >= c|k| on the bounded cube; with
  la >= t/2 the rescaled integrand is <= C|p| e^{-ct|p|/2}. Wick gives
  Cov(X^2, Y^2) = 2 Cov(X,Y)^2, so the squared differences have connected
  covariance ~ c t^{-8} after rescaling by a^{-8}. A uniform physical gap m
  would give decay e^{-m(t - 2t_0)} for the padded vector of finite norm,
  which contradicts t^{-8}.
- L246-251 (limiting spectral measure). HOLDS. The square of the limiting
  Fourier integral is the double integral over (p,q) with weight
  p_i^2 q_i^2/(|p||q|) e^{-t(|p|+|q|)}, so the measure is the stated image
  under (p,q) -> |p| + |q|. It is finite for t_0 > 0 and gives positive mass
  to {|p| + |q| < epsilon}. The infinite-volume statement has no isolated
  zero mode, so the test does not rest on it.

### Section 5. Local insertions (17) (claim 3)

- L255 (conditional (6)). HOLDS. A listed link is a chosen edge only of
  roots that contain it, at most 6, so at most 6m roots drop. Retained
  pairs have all listed links in their exterior, and their conditional
  Wilson density still has the form of (5). Every group keeps at least
  k - 6m roots. The four-torus version of (6) applies with all periods
  >= 4.
- L257-263, (17). HOLDS. The rounded law is P_rd = P prod W/E[prod W]
  over all BT groups. Its density on the listed links is
  E[prod W | L_0]/E[prod W]. By the conditional and unconditional residue
  densities over Z^{BT}, both quantities lie in W-bar^{BT}[1 - Delta',
  1 + Delta']. Their ratio is within 2Delta'/(1 - Delta') of 1. For
  m <= k/12, k - 6m >= k/2, and with BT polynomial in n, Delta' is
  superpolynomially small. Consequence: |E_rd F - E F| <=
  (2Delta'/(1 - Delta')) E|F| for every F of the listed links; summing over
  products with total weight <= n^C gives o(n^{-A}). The stated limits of
  scope (no convergence, no infinite-volume uniformity) are correct.

### Section 6. Everything else

- L3-11 (GUIDE, sources). Consistent with row 1218 and row 1215 as read.
  Credits are given to Ethan Sussman and Levent Alpoge (with Claude and
  Codex as authors of their text), the six authors of the window criterion,
  and Zeng Chunping. Not rechecked against the external sources here.
- L15 (GUIDE). Correct: a count supported on even integers has
  E(-1)^count = 1 at any variance, so a variance bound gives no angle-pi
  cancellation.
- L19-21 (GUIDE, conventions). Correct; the bridge description is the one
  used in every block above.
- L61, L151, L177 (GUIDE). Readings only; consistent with the blocks that
  follow.
- L267 (OPEN). The quantifiers match row 1218, lines 84-89. The listed roles
  of (5)-(11), (13), (14)-(15) and (16) are accurate.
- L269 (OPEN). Correct: (17) compares two finite-volume laws and gives no
  continuum construction, no Osterwalder-Schrader or Wightman structure, and
  no spectral gap.
- L271 (RESULT of the file). Accurate. It claims no gap.

### Does a main step only restate an earlier row?

- (1) and (2) extend row 1215's (26)-(27) from angle pi and parity to
  arbitrary angles and moduli q. The key input, two balls with equal
  indicators off p, is in row 1215's proof (line 435). At t = pi and q = 2
  they restate row 1215; the file says so (L30, L38).
- (3)-(4), (8)-(9) and (17) use the standard XX*/X*X identity and pointwise
  kernel sandwiches. They are new comparisons, not restatements; row 1315's
  (17) concerns a different transfer, as L59 says.
- (5)-(7), (10)-(16) are new in the lane. Row 1211 used a free scalar for a
  wall-observation bound; (16) concerns the Fourier transform of the
  spatial action itself, as L228 says.

### Does the conclusion follow?

Yes, in this precise sense. The free scalar at mu = a^2 has a positive
time transfer, local nonnegative magnetic readings, and a two-step bridge
bound (16) of the same Gaussian-min form as (6), uniformly in mu. Yet its
doubling defect diverges (L230-235) and its magnetic readings have spectral
weight down to zero (L237-251). So no argument that uses only a bound of the
form of (6), with transfer positivity and locality, can give A-B**. The
test lies outside the compact gauge class. It does not show that A-B** fails
for the Wilson action. The file does not claim that. The one-scale thermal
bound stays open.

## Summary

32 PROVED blocks: 32 HOLD, 0 HOLD AFTER CORRECTION, 0 FAIL. Precisions only:
L30 (c in (1) is 1/(number of colours)); L97 (the e^{4 beta} count uses the
four-coordinate expansion of x.Oy); L147 (Theorem F of the six authors also
needs their (W)); L222 (c = 1/100 in (16)).

RESULT: 32 of 32 PROVED statements of row 1317 HOLD, 0 need correction, 0 FAIL; main finding: the magnetic-action Fourier bound (6) holds pointwise in every Wilson bridge at beta >= 1, and with it the rounded-action comparisons (8)-(11) and (17) hold with superpolynomially small error at beta = O(log n), so A-B** for the rounded action with fixed slack would give A-B** for Wilson; but the free scalar at mu = a^2 satisfies a bound of the same form (16) while its doubling defect diverges and its magnetic readings are massless, so (6) alone cannot force the one-scale thermal bound, and the mass gap stays OPEN.
