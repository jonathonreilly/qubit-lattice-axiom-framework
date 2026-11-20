# Check of row 1330 (gap-solve42-astra62.md), FINISH row 1333

Checker: Claude Opus 5.5, by hand, line by line. Line numbers refer to
gap-solve42-astra62.md at the commit checked. Each step was derived again
here. No numeric run was used as a proof step.

File checked: gap-solve42-astra62.md at commit e1f487843 (row 1330, by
gpt-6.2-astra). Inputs opened: Theorem ZD-c (gap-phys-seed.md, lines
311-320); row 1151 (gap-solve5-astra62.md, (21), (22a), (22b)); row 1227
(gap-solve25-astra62.md, (10)) and its check, row 1230; row 1325, line 305-310,
and its check, row 1327; row 1328, line 192, and its check, row 1329.

The file has 39 PROVED blocks. They are grouped below by section.

## 1. One-link estimate, (1)-(2), lines 21-40

- L21-29, statement (1). Verified through the three proof blocks below.
  HOLDS.
- L31, the pointwise bound. With t = 1/beta the R^4 heat kernel with
  generator (1/2)Laplacian restricted to S^3 is proportional to
  exp(-beta|x-y|^2/2). For unit quaternions |x-y|^2 = 2(1 - tr(x y*)/2), so
  this is the Wilson link weight. J is constant by rotation invariance.
  The killed-to-free ratio is the bridge survival probability. The bridge is
  the chord segment (norm at most 1) plus a centred bridge. Exit needs
  |centred part| >= R-1, hence one coordinate >= (R-1)/2, since
  |v| <= 2 max|v_i| in R^4. The one-sided crossing probability of a 0-to-0
  bridge at level b is exp(-2b^2/t). Eight one-sided events give
  8 exp(-beta(R-1)^2/2). Nothing uses the angle between x and y, so
  antipodal pairs are included. HOLDS.
- L33-38, multiplier (2). This is the skew-product decomposition: the
  angular part is spherical Brownian motion run at clock A = int r^{-2}.
  Killing depends on the radius only. The degree-l eigenvalue of
  (1/2)Laplacian on S^3 is -l(l+2)/2. I checked the annulus step: in four
  dimensions P(hit eta before R') = (1 - R'^{-2})/(eta^{-2} - R'^{-2}),
  which tends to eta^2. Dividing by J removes the radial density at
  radius 1. HOLDS.
- L40, factorization. On survival r_u < R, so A >= t/R^2 = s. The measure
  D = E[1_surv H_{A-s}] has multipliers E[1_surv e^{-l(l+2)(A-s)/2}] >= 0
  and total mass P(surv) <= 1. Also H_s D has multiplier (2). Central heat
  convolutions are diagonal in characters, so C_{beta,R} = H_s D. Both are
  positive semidefinite. HOLDS.

Not a restatement. B8 (Hartman-Watson) writes the Wilson multipliers as a
heat mixture with no lower bound on the time. BR (row 947) uses the ambient
bridge for an interpolation. The radial killing that gives a deterministic
angular time s with a pointwise relative error is new.

## 2. The full periodic cube, (3)-(6) and the row 1227 test, lines 44-80

- L44-56, (3). Z(u) is the integral of the product of mu one-link kernels,
  m per layer, against the positive magnetic weight. The gauge average is a
  positive integral done once. By (1), k_{beta,R} >= (1-eps_R) k_beta
  pointwise, so e^{-u b_R} Z(u) <= Z_R(u) <= Z(u). Each log trace moves by
  an amount in [-u b_R, 0]. In Psi = 2 log Z(T) - log Z(2T) the two moves
  lie in [-2T b_R, 0], so |Psi_R - Psi| <= 2T b_R. HOLDS.
- L58-64, (4). The kernels satisfy 0 <= K - K_R <= d K pointwise, with
  d = 1 - e^{-b_R}. Then |(K-K_R)f| <= d K|f|. Since |f| is gauge
  invariant, ||K - K_R|| <= d lambda_0, and Weyl gives the first bound.
  Perron: lambda_0^R <= lambda_0 by kernel order, and testing K_R on the
  nonnegative top vector gives (1-d) lambda_0 <= lambda_0^R. For the
  ratios, |r_i^R - r_i| <= d/(1-d) + r_i d/(1-d) <= 2d/(1-d). For
  r_i >= 1/2 and d <= 1/16 one gets r_i^R >= 1/2 - 2/15 = 11/30. The mean
  value bound gives at most (32/15)(30/11) d = (64/11) d < 6d. A bounded
  physical energy has r_i -> 1, so the physical error is at most
  6 d n/L. HOLDS.
- L66-71, (5). With R_n - 1 = sqrt(2(4+p) log n/beta) one gets
  eps = 8 n^{-4-p} exactly. Then b_R ~ m eps = 24 n^{-1-p} and
  2T b_R = n b_R = O(n^{-p}). The energy error is 6 d n/L = O_L(n^{-p}).
  Also s_n = 1/(beta R_n^2) = (sqrt(beta) + sqrt(2(4+p) log n))^{-2}, and
  the bound for beta <= B log n follows. In the multiplicative comparison
  both log Z_R - log Z and u(log lambda_0^R - log lambda_0) lie in
  [-u b_R, 0], since 1 - d = e^{-b_R}. So their difference is at most
  u b_R. Need eps < 1: 8/4^4 < 1. HOLDS.
- L73-78, (6). The model is M = 1. The normalized multipliers are at most
  e^{-l(l+2)s/2}. The degree-l multiplicity on S^3 is
  C(l+3,3) - C(l+1,3) = (l+1)^2. The tail bound comes from factoring out
  e^{-3v/2}, since l(l+2) - 3 >= 0. T s_n >= c n/log n, so
  3n^3 e^{-3T s_n/2} -> 0. The trace before projection bounds the trace
  after it. HOLDS.
- L80, test with row 1227. I read row 1227, (10): at fixed n >= 3 each of
  the seven nontrivial centre sectors has lowest lattice energy at most
  C_n e^{-c_n sqrt(beta)}. Its check, row 1230, found no failure. With
  u = ceil(beta^2), the term u C_n e^{-c_n sqrt(beta)} tends to 0. So the
  normalized Wilson trace has lower limit at least 8. At fixed R,
  u b_R ~ 8 m beta^2 e^{-beta(R-1)^2/2} -> 0. The right side of (6) has
  u s = beta/R^2 -> infinity at fixed m, so it tends to 1. The file
  correctly limits this to fixed spatial side, not the physical aspect
  ratio. HOLDS.

## 3. Split transfer and the first endpoint test, (7)-(14), lines 84-187

- L84-97, (7)-(8) (GUIDE, read as setup). Since C_{beta,R} = H_s D and the
  factors commute, one has C_{beta,R} = H_h (H_{s-2h} D) H_h when 2h <= s.
  For fixed alpha and h = alpha/beta: 2h <= s_n iff
  sqrt(2 alpha)(1 + sqrt(2(4+p) log n/beta)) <= 1. This needs the lower
  bound beta >= b log n. The middle factor H_h M^2 H_h, the symmetry of F
  and the cancellation of a(x)b(y) in (8) are correct.
- L99-114, (9)-(10). The 12-plaquette holonomy is e^{-2 I eps_v theta},
  since eps flips under e_1. The 13- and 23-plaquettes are trivial, so
  S(y) = beta V (1 - cos 2 theta). For a direction-2 edge,
  <g_u e^{I eps theta}, g_v> = cos theta <g_u,g_v> + eps sin theta J(g_u,g_v).
  This gives the displayed expansion. J(a,b) = <aI,b> is antisymmetric. The
  circulation of a square is j_1(v) + j_2(v+e_1) - j_1(v+e_2) - j_2(v).
  Against eps_v, the j_1 terms cancel by periodicity in direction 2. The j_2
  terms give -2 sum eps_v j_2(v). The identity
  J(a,b)+J(b,c)+J(c,d)+J(d,a) = J(b-a,c-a) + J(c-a,d-a) checks by
  bilinearity. Each edge lies in at most two 12-squares. For |theta| <= 1,
  cos theta >= 1 - |theta|/2. This proves (10) for all frames. HOLDS.
- L116-130, (11). With k = l+1 the character series is
  e^{t/2} sum k e^{-k^2 t/2} sin(kd)/sin d. Poisson summation gives the
  periodized form. For d <= pi/2, the pairs j, -j sit at arguments
  >= 3 pi/2. Their ratio to the j = 0 term is O((1+1/t) e^{-pi^2/t}).
  For d >= pi/2 the pairing at (2k+1)pi -+ u is right, and sin d >= 2u/pi.
  The factor (1 + 1/t) is absorbed by e^{-delta pi^2/(8t)}. HOLDS.
- L132, midpoint ball. On B(b, sqrt h) both distances are at most
  d/2 + sqrt h <= pi/2. Taylor gives f <= d^2/2 + Ch. The ratio of the
  lower local bound to H_{2h}(d) is c h^{-3/2}, and the ball volume is
  c h^{3/2}. HOLDS.
- L134-148, (12). The plaquette differences satisfy
  ||Delta_p|| <= 4 ||delta|| (4 edges per plaquette, 4 plaquettes per edge,
  Cauchy-Schwarz). With (a-b)^2 >= (1-eta) a^2 - b^2/eta this gives
  S(z) >= (1-eta) S(y) - (8 beta/eta) sum d^2. At eta = 1/8 the insertion
  is e^{64 beta d^2}. Here 64 beta = 64 alpha/h <= 1/(8h) iff
  alpha <= 1/512. The first kernel keeps e^{-d^2/(4h)}, the second
  e^{-3d^2/(8h)}. The edge integral is C h^{-3/2} e^{-c d(y,(gy))^2/h}. The
  spanning tree gives (C h^{3/2})^{V-1}. The denominator on the sqrt(h)
  frame ball uses d(y, g_u y g_v^{-1}) <= d(1,g_u) + d(1,g_v) <= 2 sqrt h.
  The h-powers leave h^{-3/2} (m = 3V). HOLDS.
- L150-161, (13), denominator. Global (11) at time 2h, geodesic >= chord,
  (10) with 1 - C|theta| >= 1/2, and a tree integral in the chord metric.
  HOLDS.
- L163-175, (13), numerator and limit. Distances: on direction-2 edges at
  most theta + 2 sqrt h, else 2 sqrt h, total V(theta^2 + 4 theta sqrt h +
  12 h). The midpoint of 1 and (gy)_e is its principal root, within
  C sqrt h of y_e^{1/2}. At y^{1/2}, S = beta V(1 - cos theta) <= V A^2/2.
  The chord step gives S(z) <= V(A/sqrt 2 + C sqrt alpha)^2. The leading
  terms: [(1-delta) 2(1 - cos theta) - theta^2]/(4h) =
  -delta A^2/(4 alpha) + O(A^4/(alpha beta)). The cross term theta/sqrt h is
  A/sqrt(alpha). The h-powers leave h^{3/2}, and |log h|/V -> 0. HOLDS.
- L177-187, (14). F(o,o) <= 1 by Chapman-Kolmogorov and e^{-S} <= 1.
  S(y)/V -> 2A^2. With (12), (13) and F(y,o) = F(o,y), the per-site lower
  limit is (3/4 - delta/(2 alpha)) A^2 - 2 C_alpha A - C'. At
  delta = alpha/4 the coefficient is 5/8 (and delta < 1/4 holds). The
  alternating-sum argument for a(x) b(y) is correct. HOLDS.

## 4. Thermal restriction, (15)-(16), lines 191-224

- L191-199, statement (15). Verified through the three blocks below.
  HOLDS.
- L201-206, original slices. Row 1151, (21), bounds
  log E exp[t sum_{S_p}(1-w)] <= |S_p|[p_V(u) - p_V(0)] for any subset of
  one orientation on the n^3 x T and n^3 x 2T tori. (22a) gives
  p_V' = 3/4 + O(|u| + beta^{-eta}) for |u| <= 1/4. Row 1151 assumes
  beta -> infinity and beta = O(log n) (its line 13), so it applies on the
  schedule b log n <= beta <= B log n. Markov at the threshold
  3/4 + eps/6 per orientation, plus a union over three orientations, gives
  3 e^{-c_eps |B|}. Transfer to the K_R integral: the integrand is
  dominated pointwise and Z_R(u) >= e^{-u b_R} Z(u). HOLDS.
- L208-214, (16). (11) at delta = 1/4 gives
  e^{d^2/(16h)} H_h <= C h^{-3/2} e^{-5 d^2/(16h)}. I checked the global
  lower bound H_{2h}(d) >= c h^{-3/2} e^{-d^2/(4h)} for d >= pi/2. The
  first pair is f(d) - f(d+2w) >= f(d)(1 - e^{-dw/t}), since
  1 + 2w/d <= e^{dw/t} for small t. The cases dw/t <= 1 and > 1 both give
  c e^{-d^2/(2t)} after dividing by sin d <= w. The later pairs are
  nonnegative because f decreases on [sqrt t, infinity). Then the
  replacement by H_{2h} on the edges in I acts through E_I, a product of
  central heat convolutions. It is gauge covariant, commutes with every
  layer convolution, and has multipliers in [0,1]. So M E_I C_R M <= K_R in
  form order. Also Tr(A B) <= Tr(A' B) for 0 <= A <= A' and B >= 0, using
  Tr(B^{1/2} A B^{1/2}). HOLDS.
- L216-224, inserted slices and K_res. 12|B| edges per cube. Markov:
  C_0^{12|B|} e^{-C_1 |B|/16} = e^{-|B|} for C_1 = 16(12 log C_0 + 1).
  The chord step on a cube gives sqrt(S_B(x)) <= sqrt(S_B(z)) +
  sqrt(beta/2) * 4 * sqrt(C_1 h |B|) = sqrt(S_B(z)) + sqrt(8 C_1 alpha |B|).
  Union: at most 3u n^4 terms, with u <= n. The total is
  C n^{5 - K min(1,c_eps)}, so K min(1,c_eps) > 6 + p gives O(n^{-1-p}).
  This is better than needed. K_res = X D X* with X = Q M H_h Q, so it is
  positive. Q^2 = Q. Q depends only on plaquette actions, so it is gauge
  and centre invariant. HOLDS.

## 5. The test inside (15), (17)-(25), lines 230-303

- L230-236, (17). The 12-holonomy is e^{4 I sigma_v vartheta}, since sigma
  flips under e_1 and e_2. The 13- and 23-plaquettes are trivial because
  sigma does not depend on v_3. beta(1 - cos 4 vartheta) <= 8 beta
  vartheta^2 = 2. For w the bound is 1/2. Reflection in v_1 sends the
  direction-1 link at v to the reversed link at (2c - v_1 - 1, v_2, v_3),
  where sigma has the opposite sign. So the field is invariant. HOLDS.
- L238-248, (18)-(19). The direction-1 and direction-2 current terms are
  -2 sin(vartheta) sigma_v j_1 and +2 sin(vartheta) sigma_v j_2. Against
  sigma, the circulation sum is 2 sum sigma (j_1 - j_2). Both sides of (19)
  follow, with B_theta = 4V(1 - cos vartheta) from 2V twisted edges.
  HOLDS.
- L250-259, proof of (18). On an edge with d(1,(g y')_e) > pi/2 one has
  d(g_u,g_v) >= pi/2 - vartheta, so the global loss delta pi^2 is paid by
  C delta |g_u - g_v|^2. Normalizer: on the sqrt(h) ball E <= 12 h V. The
  geodesic-chord error per edge is O((vartheta + sqrt h)^4)/h =
  O(1/(alpha beta)) -> 0. The upper side of (19) applies. The quotient is
  C^V h^{-3/2}. Jensen gives E E(g) <= C h V/k. HOLDS.
- L261-265, (20), bridge moment. For d(a,a') <= pi/4 and z within pi/4 of
  the midpoint, both distances are at most 3 pi/8. The Hessian of
  (1/2) d^2 has eigenvalues 1 and r cot r >= 0.48. Strong convexity gives
  f - d^2/2 >= c d(z,b)^2 there. Outside that ball, uniqueness of the
  midpoint and compactness give the bound. HOLDS.
- L267, (20), frames. On short edges the midpoint is (g_u y'_e g_v^{-1})^{1/2},
  within C d(g_u,g_v) of g_u w_e g_u^{-1}, and that point is within
  d(g_u,g_v) of (gw)_e. On long edges d(g_u,g_v) >= pi/4 - vartheta. With
  (18) the sum is C h V. Period-two invariance gives 24 classes of V/8
  edges. HOLDS.
- L269-274, (21), one tile. 54 edges on a closed side-two cube. Markov
  gives 1 - C h beta/zeta^2 = 1 - C sqrt(alpha). The reflection property:
  for a crossing link, H_h(1,z^{-1}) H_h(z^{-1}, g_v y'^{-1} g_u^{-1}) =
  H_h(1,z) H_h(z, g_u y' g_v^{-1}), so the factors are preserved. Given the
  two plane slices, the weight factors into reflected halves. Cauchy-Schwarz
  gives the reflection inequality. The method is the chessboard argument
  credited to Sussman and Alpoge (AM6). HOLDS.
- L276, dissemination. 4 | n makes n/2 even, so each site reflection maps
  the n/2 slabs onto themselves. The longest-run argument then works. The
  single-slot chessboard bound gives
  P(all tiles) >= P(one tile)^{(n/2)^3}, which is the lower-bound direction
  needed. P(21) >= exp(-C sqrt(alpha) V). HOLDS.
- L278-285, (22). sqrt(beta/2) * 4 * sqrt(12|B|) zeta/sqrt(beta) =
  sqrt(96) zeta sqrt(|B|). The square of 1/sqrt 2 + sqrt(96) zeta is
  below 9/4. On B equal to the torus, S(z)/V <= 1/2 + C alpha^{1/4}. The
  probability cost e^{-C sqrt(alpha) V} is absorbed. HOLDS.
- L287-296, (23)-(24). The insertion e^{d^2/(16h)} leaves coefficient
  5/(16h) >= 1/(4h) in the first kernel, and the (12) integration applies.
  With eta = sqrt(alpha): S(z) >= (1 - sqrt alpha) S(y) -
  (8 sqrt(alpha)/h) sum d^2. Convexity of the log moment phi with
  phi(0) = 0 gives phi(8 sqrt(alpha)/h) <= 128 sqrt(alpha) C V, valid
  when 8 sqrt(alpha) <= 1/16. HOLDS.
- L298-303, (25). The numerator is at least e^{-V(1 + C alpha^{1/4})}. In
  the denominator F_Q(o,o) <= 1, and log F_Q(y',y') <= -(1 - sqrt alpha)
  2V(1 + o(1)) + C sqrt(alpha) V. The per-site lower limit is
  1 - C alpha^{1/4} >= 1/2. One of the four pairs then carries log error
  at least n^3/8. The file does not claim any thermal probability for
  these pairs. HOLDS.

## 6. Three two-sided windows and (29), (26)-(29), lines 307-359

- L307-312, (26). Row 1151, (21), is stated for t >= 0. I checked the
  negative tilt. The Hoelder step bounds log Z(tilted on S_p) by
  (|S_p|/V) log Z_V(u) + (1 - |S_p|/V) log Z_V(0), with no sign condition.
  At u < 0 the marked coupling beta(1 + |u|) still gives positive layer
  operators: Bessel-ratio multipliers for M C_i M, and C^{1/2} M_i^2 C^{1/2}.
  (22b), hence (22a), is proved there for both signs and |u| <= 1/4.
  Markov on -S_{B,ij} then gives the lower tail with exponent
  |B| |u| (-eps/2 + O(|u| + beta^{-eta})). On inserted slices the chord
  bound controls |sqrt(S_{B,ij}(x)) - sqrt(S_{B,ij}(z))|, so a two-sided
  window survives. Wording only: (26) should repeat |B| <= V, as in (15).
  HOLDS.
- L314-320, (27). For the ij-plaquette, a_{v+e_j,i} - a_{v,i} =
  -2 c_ij (-1)^{v_i+v_j} kappa/sqrt(beta) and a_{v+e_i,j} - a_{v,j} =
  +2 c_ij (-1)^{v_i+v_j} kappa/sqrt(beta). The angle is
  4 c_ij (-1)^{v_i+v_j} t kappa/sqrt(beta), and it is never zero. Its
  action tends to 8 t^2 kappa^2 = 3t^2/4. About half the links have a_e = 0;
  the rest have |a_e| = 2 kappa/sqrt(beta), as stated. I checked
  invariance under reflection with link reversal. HOLDS.
- L322-333, (28), chord cost. With g = p + qJ and z J = J zbar on C_I, one
  gets g_u y_e - x_e g_v = [p_u e^{I(1+d)a} - e^{I(1-d)a} p_v] +
  [q_u e^{-I(1+d)a} - e^{I(1-d)a} q_v] J. This gives the two displayed
  moduli. The expansion with Im(b_u bbar_v), an antisymmetric real form,
  is correct. Since |a_e| takes one nonzero value, sin(k a_e) = lambda_k a_e
  with |lambda_k| <= |k| <= 2. The pairwise weighted current is one half of
  the signed circulation sum, as in (19). HOLDS.
- L335-340, G bound. After using |p|^2 = 1 - |q|^2, the coefficient is
  cos(2da) - cos(2a) = 2 sin((1+d)a) sin((1-d)a), between c a^2 and
  C a^2. On the sqrt(h) ball |q_v| <= C sqrt(h), so G <= C h V. Sanity
  check: a global J rotation costs order V/alpha in G/h, so it is
  suppressed, as required. HOLDS.
- L342, (28) finished. |g y g^{-1} - y| = |q| |y - ybar| = 2 |q| |sin phi|.
  The midpoint of x_e, y_e is w_e exactly. Lipschitz midpoints plus E G
  give (28). HOLDS.
- L344-350, statement (29). Verified through the next two blocks. HOLDS.
- L352-357, first normalization. Period two in all directions gives V/8
  edges per class. Markov plus dissemination (x, y, w are all reflection
  invariant) give P >= e^{-C sqrt(alpha) V}. Per plaquette,
  |sqrt(action(z)) - sqrt(action(w))| <= sqrt(beta/2) * 4 zeta/sqrt(beta)
  = 2 sqrt(2) zeta. So every plaquette passes, and S(z)/V <= 9/4 + C zeta.
  With (24) at x and y the per-site limit is
  -9/2 + (9/4)(2 + 2d^2) - C alpha^{1/4} = 9d^2/2 - C alpha^{1/4}. HOLDS.
- L359, second normalization. The mixed end only gains. At an equal end,
  (23) and Jensen give sum E d(z_e, x_e)^2 <= C h V. The ends have margin
  eps/2 - o(1), so the tile event implies (26) with probability at least
  e^{-C sqrt(alpha) V}. The order of choices (window, then d, then alpha)
  is consistent. HOLDS.

Positive claim 2 (the magnetic kernel fails (29) in the three windows):
HOLDS.

## 7. The conditional implication, (30), lines 363-368

The inequality chain holds. Let U = K/lambda_0 on the vertex-gauge-invariant
space with all centre sectors, and S(T) = Tr U^T - 1. Tr K^u is the Wilson
torus partition function, so this is the S_j of Theorem ZD-c. Each ratio
r_i^{2T} <= r_i^T, so Tr U^{2T} <= Tr U^T. Hence
exp(Psi) = (Tr U^T)^2 / Tr U^{2T} >= 1 + S(T). Then
log(30) = Psi_res = Psi_R + O(n^{-p}) by Section 4 at u = T and u = 2T.
Also Psi_R = Psi + O(n^{-p}) by (3) and (5). So
limsup_j (30) < 1651/1650 gives limsup_j S_j(L/(2 a_j); (L/a_j)^3) < 1/1650.
T = n/2 = L/(2 a_j) matches (PHYS-SEED). For L in P, L/(4 a_j) is an
integer, so 4 | n. The constants 1651/1650 and 1/1650 are right, and the
strict inequality is kept.

Coupling hypotheses. Each O(n^{-p}) step after (5) needs the schedule
b log n_j <= beta_j <= B log n_j, with n_j = L/a_j and fixed 0 < b <= B.
- The lower bound is used for 2h <= s_n at fixed alpha (Section 3, line
  84). Through beta_j -> infinity it is also used for theta, vartheta -> 0,
  for the beta^{-eta} error in (22a), and for h < t_0.
- The upper bound is the beta = O(log n) hypothesis of row 1151 (its line
  13). Row 1151 supplies (15) and (26).
Theorem ZD-c holds for any trajectory (a_j, beta_j) and does not supply
this range. Lines 363-368 say only "the choices above" and "the admissible
dyadic physical sizes and cutoff sequences of Theorem ZD-c". They state
that the implication "reuses ZD-c with its stated hypotheses". So the
range is missing from the statement. This is the same kind of gap that
check 1327 found in row 1325.

Verdict L363-368: HOLDS AFTER CORRECTION. Correction: add the hypothesis
that, at the chosen L in P, the trajectory satisfies
b log(L/a_j) <= beta_j <= B log(L/a_j) for all large j, with fixed
0 < b <= B < infinity. alpha and K_eps(p) are chosen after b, B, eps, p.
(For a fixed L this is equivalent to the same bounds with log(1/a_j), with
other constants.) With this added, the implication is correct.

Restatement: the threshold step (Tr U^{2T} <= Tr U^T, then 1651/1650 to
1/1650) restates row 1325, lines 305-310, and row 1328, line 192. What is
new in this block is that the reduction transfers to the restricted
transfer K_{eps,n} with O(n^{-p}) error.

Positive claim 1 (a common angular time and the three windows keep Psi up
to O(n^{-p})): HOLDS on b log n <= beta <= B log n with 4 | n and T = n/2,
by (3), (5), (15), (16) and (26). The same range is what must be added to
claim 3.

## 8. GUIDE, OPEN, RESULT line, restatement and credits

- L3-15 (GUIDE). The ZD-c description matches lines 311-320 of
  gap-phys-seed.md. The descriptions of row 1328, (12), and of B8, BR and
  row 1151 match the sources I opened. I did not reopen the PR 10114,
  10133, 10134 and 10141 passages; this check does not rely on them.
- L19 (GUIDE). The link kernel exp(-beta|x-y|^2/2) is the Wilson temporal
  weight. Psi does not change when K is multiplied by a scalar, so the
  normalization by J does not matter.
- L226 (GUIDE). Correct: A large in (14) leaves (15), which is why (17)
  is used.
- L370 (OPEN). Accurate. (29) is a pointwise kernel statement. It gives no
  thermal weight to the four pairs and does not decide (30).
- L372 (RESULT line of the file). It matches the proofs. It says "on the
  stated logarithmic coupling schedules", which is the range that the
  implication in L363-368 must also state.
- Wording. The letter d is used for three things: 1 - e^{-b_R} in (4),
  round distance in (11)-(25), and the amplitude in (27)-(29). The file
  notes the last clash. The constant 6 in (4) can be 64/11.
- Restatement. No main step only restates an earlier row, apart from the
  threshold step in Section 7. The original-slice bound in (15) applies
  row 1151, (21)-(22a), directly. (26) extends it to negative tilts, which
  I checked. I found no earlier row with the radial-killing factorization
  (1), the frame-cost bound (10), or the endpoint tests (14), (25), (29). I
  searched the library for the key phrases.
- Credits as given in the file: Ethan Sussman and Levent Alpoge (GL3, GL8,
  CA-I, the chessboard inequality AM6); Philip Hartman and Geoffrey Watson
  (heat-kernel mixture, via B8); Sourav Chatterjee (open-box pressure
  comparison behind row 1151, (22a)); Martin Luescher and Pierre van Baal
  (small-volume tunnelling, via row 1227); Deep Bhattacharjee, Ushashi
  Bhattacharya, James Montgomery Lockwood, Tristan Romanov, Ikailo John
  Sessford and Sanjeevan Singha Roy; Zeng Chunping.
- I made no numeric run. Every verdict above is a hand derivation.

RESULT: 39 PROVED statements of row 1330 checked by hand by Claude Opus 5.5: 38 HOLD, 1 HOLDS AFTER CORRECTION, 0 FAIL; main finding: the radial-killing factorization C_{beta,R} = H_s D_{beta,R} with relative error 8 e^{-beta(R-1)^2/2}, and the thermal restriction to the three plaquette windows (26), keep the full Wilson two-period defect Psi(T) to O(n^{-p}); the magnetic kernel fails the separate-endpoint test (29) by at least d^2 n^3 inside those windows; the reduction of (30) < 1651/1650 to the two-stage seed of Theorem ZD-c holds after adding the coupling range b log(L/a_j) <= beta_j <= B log(L/a_j) along the trajectory, which the restricted transfer needs and ZD-c does not supply; its threshold step restates rows 1325 and 1328; no seed is proved and (30) stays open.
