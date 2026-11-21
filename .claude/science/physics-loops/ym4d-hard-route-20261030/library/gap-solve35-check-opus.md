# Check of row 1315 (gap-solve35-astra62.md) — FINISH row 1316

Checker: Claude Opus 5.5, by hand, line by line.
Target: `library/gap-solve35-astra62.md` (row 1315, gpt-6.2-astra).
Builds on: `library/gap-solve34-astra62.md` (row 1298) and its check
`library/gap-solve34-check-opus.md` (row 1307).
Method: each step derived again by hand. Numeric runs, where used, only guide.

## Verdicts

Checkout: branch `claude/ym4d-hard-route` at `dde2238e6`. Target: 285 lines,
37 PROVED blocks, 1 ARGUED, 4 OPEN, 12 GUIDE, equations (1)-(22).
Definitions of K, the cap and base flags, G_d, (29), (36) and (37) were read
in row 1298, lines 353-481. Row 1307 found (29)-(37) of row 1298 to hold.

### Section 1. Cap/base chain: (1)-(7) (positive claim 1)

- L25-30 (cap updates preserve 1_A). HOLDS. Row 1298 puts both the old and
  the new spin of a cap flag in the round cap of radius beta^{-1/2} about
  t_e = h/H, with H >= 3. Then h.x_e = H t_e.x_e >= 3 t_e.x_e, each other
  v_j.x_e <= 1, so every incident trace v_i.x_e >= 3 t_e.x_e - 3 -> 0 > -eta.
  So p is outside A at both ends. A colour fixes a direction and the parity
  of the other two coordinates. The two parallel edges of p differ by one in
  one of those coordinates, so a colour holds at most one edge of p.
  Wording: if the cap radius is a Euclidean chord, t_e.x_e >= 1 - 1/(2 beta)
  replaces cos(beta^{-1/2}); the conclusion is the same. The example: one
  link equal to -1 gives two deficits of 2 per orientation in any cube, so
  beta*4 < B d^3 suffices; Bd^3 > 8 beta is enough. The flat field and this
  field have open neighbourhoods of positive density. So 1_{A cap G_d} is a
  nonconstant fixed function of the cap-only chain restricted to G_d. This is
  new against row 1298 (L397 there): the H_e = 0 field of row 1298 has
  deficit 1 on every face, hence lies outside G_d once beta > B.
- L36-42, (1) (labelled GUIDE, used as a proof step). HOLDS. Row 1149 (23)
  (`gap-solve4-astra62.md` L307-311) states E exp(beta sum_S a(U_p)) <=
  z_beta^{-|S|} on homogeneous rectangular tori for faces with one common
  direction. The four spatial faces at e contain the direction of e. The
  bound z_beta >= c(1+beta)^{-3/2}: Haar density (2/pi) sin^2(phi) dphi;
  on phi <= (1+beta)^{-1/2} the weight is >= e^{-1/2} and the mass is
  about (2/(3 pi)) (1+beta)^{-3/2}.
- L44-50, (2). HOLDS. rho_h(A_theta) = int_{A_theta} e^{-beta D_e(s)} ds /
  int e^{-beta D_e(s)} ds with D_e(s) = 4 - h.s. Denominator: near s = h/H,
  D_e <= 4 - H + 2 phi^2, so >= c(1+beta)^{-3/2} e^{-beta(4-H)}. Numerator:
  on A_theta, D_e(s) >= D_p(s) > D_theta. Then 4 - H <= 4 - h.x_e = D_e(X),
  and (1) gives z_beta^{-4} <= C(1+beta)^6. Total power 3/2 + 6 = 15/2.
- L52-57, (3). HOLDS. Only an edge e of p changes w_p. Cap moves do not
  change 1_{A_theta} (L25 with eta = -cos theta in (0,1)). Row 1298 fixes
  the base flag probability p_0 given (U,Y,Z), and given that flag the old
  spin has law rho^0_e, which depends on Z only. So the contribution of e is
  at most (1/6) p_0 E_nu[rho_h(A_theta)]. Four edges, each in one colour:
  Q <= (4/6)(1/2) e^{-4 beta} C(1+beta)^{15/2} e^{-beta D_theta}.
- L61-66, (4). HOLDS. Symbol of d is v -> t wedge v, kernel span(t), rank 3
  for t != 0. J is the projection onto the closed range, J real. Translation
  and coordinate permutation give six equal diagonal entries with trace 3,
  so J_pp = 1/2. Then w = 2 alpha J delta_p has w_p = alpha and
  ||w||^2 = 4 alpha^2 J_pp = 2 alpha^2, so sum_{q != p} w_q^2 = alpha^2.
  Approximation by finite real curls and rescaling by alpha/(du_n)_p gives
  (4). Credit: J_pp = 1/2 was already used in row files
  `gap-solve26-astra62.md` L455 and `gap-solve27-astra62.md` L187; the
  rank-three symbol is from Sussman-Alpoge, as the file says.
- L68-73, (5). HOLDS. V_e = exp(i u_e) is abelian, so V_q = exp(i (du)_q)
  and w_q = cos (du)_q. Action of V in units of beta is
  (1 - cos alpha) + sum_{q != p}(1 - cos (du)_q) <= (1 - cos alpha) +
  (1+eps') alpha^2/2 -> D_theta + theta^2/2 as alpha -> theta, eps' -> 0.
  cos alpha < cos theta for theta < alpha < pi. Wording: the statement says
  "isotropic"; the proof and the use at L77 (time period to infinity) need
  rectangular tori with all periods large. The proof covers them unchanged.
- L75 (starting event). HOLDS. nu(D_q > delta) <= z_beta^{-1} e^{-beta delta}
  by (1) with one mark, so all faces of a fixed box are near flat with
  probability -> 1. On the tree slice the flat set is the single point all
  links = 1 (simply connected box); compactness gives the neighbourhood.
  Gauge averaging: Pr(box links in N) >= Pr(near flat) * prod Haar ball mass.
- L77 (change of variables). HOLDS. Left multiplication preserves Haar. On
  E the density ratio is >= exp[-beta(D_theta + theta^2/2 + eps)]. So
  mu(VE) >= r mu(E) and VE is inside A_theta. Passage to nu at fixed n by
  the simple top eigenvalue is valid.
- L81-86, (6). HOLDS. For S = A_theta cap G_d in pi = nu(.|G_d): the
  Dirichlet form of 1_S is the restricted outgoing flux, at most Q/nu(G_d);
  Var_pi 1_S = (s/nu(G_d))(1 - s/nu(G_d)). The ratio is
  Q/(s(1 - s/nu(G_d))). Row 1298 (36) at r = 1 gives nu(G_d^c) <=
  3 n^{3 - c K_0}, with c independent of beta (row 1307 L58). The lower
  bound (5) is n^{-b(I_theta+eps)(1+o(1))}. So K_0 large gives s >= half of
  (5). One deletion gives nu(A_theta) <= z_beta^{-1} e^{-beta D_theta} -> 0.
  Exponent: (4 + D_theta) - (D_theta + theta^2/2 + eps) = 4 - theta^2/2 - eps.
- L88-92, (7) and the endpoint arithmetic. HOLDS. At theta = pi/2 the
  condition 4 - pi^2/8 > 3 pi^2/11 is 352 > 35 pi^2, true since
  35 pi^2 < 350. The inequality is strict, so theta slightly above pi/2 and
  a small eps keep it. Then limsup log(gamma_d)/log n <=
  -b_*(4 - theta^2/2 - eps) < -1 and log a/log n -> -1, so gamma_d/a -> 0.
  The margin is small: b_*(4 - pi^2/8) is about 1.028. The closing remarks
  are right: (37) of row 1298 stays a valid implication; its premise fails
  for this concrete K only; (29) bounds I - K by 2(I - P), so a small K-gap
  says nothing about the P-gap.

Section 1 verdict: (6) and (7) HOLD. The cap/base chain of row 1298, with
or without the G_d rejection, has gap o(a) on the bare schedule at b_*. The
premise gamma_d >= ca of row 1298 (37) is false for that kernel.

### Section 2. Spectral weight bound (8) for the true transfer (positive claim 2)

- L94-106, (8). HOLDS. On a torus of time period 2l, mark A_theta at times
  0, 2, ..., 2l-2. The l marked faces share both spatial directions of p.
  Markov's inequality with (1) for l marks gives probability <= q^l,
  q = z_beta^{-1} e^{-beta D_theta}. In temporal gauge with the gauge
  projection, that probability is Tr[(1_A T^2 1_A)^l]/Tr T^{2l}. The ground
  state transform is unitary and commutes with 1_A, so the ratio equals
  Tr[(1_A P^2 1_A)^l]/Tr P^{2l}. At fixed grid P is compact and
  self-adjoint with simple top eigenvalue 1, so Tr P^{2l} -> 1 and
  Tr[X^l]^{1/l} -> ||X|| for X = 1_A P^2 1_A >= 0. Hence
  ||P 1_A||^2 = ||1_A P^2 1_A|| <= q. For S inside A_theta,
  ||P 1_S||^2 <= q nu(S), and <P 1_S, 1> = nu(S) gives
  ||P(1_S - nu(S))||^2 = ||P 1_S||^2 - nu(S)^2. This is (8). Band step:
  on Ran 1_{[0,E]}(H) one has P >= e^{-aE}, so ||Pi_E v||^2 <=
  e^{2aE} ||P v||^2. The bound -> 0 because q -> 0.
  Not a restatement of a result: it applies the marked-trace method of
  row 1290 (11) and row 1298 (30) to a new event, as the file says.

Section 2 verdict: (8) HOLDS. Each single centred plaquette indicator has
physical low-energy weight O(q) -> 0. This is consistent with (7): the
small K-gap comes from the base flag, not from the true transfer.

### Section 3. Excursion kernel (16)-(17) and the residual (positive claim 3)

- L196-205, (16) and T_G. HOLDS. 1_B <= sum_p 1_{A_p}, so
  ||1_B P f||^2 <= sum_p ||1_{A_p} P f||^2 <= k q ||f||^2. Then
  ||P_BB|| <= eta < 1 and the Neumann series converges with nonnegative
  kernels. (1 - P_BB) 1_B = 1_B P 1 - 1_B P 1_B = P_BG 1_G, so
  (1 - P_BB)^{-1} P_BG 1_G = 1_B and T_G 1_G = 1_G. T_G is symmetric in the
  unnormalized restriction of nu, so reversible in nu(.|G).
- L207-216, (17). HOLDS. In block form, with A = 1 - P_BB >= (1-eta)I,
  H = A^{-1} P_BG and f = (g, Hg + h), the Schur complement identity gives
  <f,(1-P)f> = <g,(1-T_G)g>_G + <h,Ah>_B, using P_GB^* = P_BG. Also
  ||H|| <= eta/(1-eta), H 1_G = 1_B, so f - c = (g - c, H(g - c) + h). The
  map (g,h) -> (g, Hg + h) is I + N with ||N|| = ||H||, norm <=
  1/(1-eta). With <h,Ah> >= (1-eta)||h||^2 this gives the lower bound. For
  the upper bound take h = 0; H keeps gauge invariance since B is gauge
  invariant.
- L218 (finite excursion truncation). HOLDS. eta^2 = kq <=
  z_beta^{-1} e^{-zeta beta}. The tail is P_GB P_BB^l (1 - P_BB)^{-1} P_BG,
  norm <= eta^{l+2}/(1-eta), which is o(a) when (l+2) b zeta/2 > 1.
- L283 (OPEN residual and the implication). The implication HOLDS: with
  d_G >= ca, (17) gives d_P >= (1-eta)^2 c a for small a; P is a positive
  operator (reflection positivity of the Wilson action), so the centred norm
  of P^{floor(t/a)} is at most (1 - d_P)^{floor(t/a)}, which passes to a
  matched continuum limit on a dense family as in row 1298 L479.
  Finding: the residual is equivalent to the target lattice bound, not a
  reduction of it. By (17), d_P <= d_G always, and d_P >=
  (1-eta)^2 min(d_G, 1-eta). With eta -> 0, "d_G >= ca uniformly" holds if
  and only if "d_P >= c'a uniformly" holds, up to the constant. So this
  residual only restates the uniform lattice gap of the true transfer for an
  equivalent operator. The file calls it "one precise residual"; it does not
  claim it is weaker, but a reader should know it moves nothing.

Section 3 verdict: (16), (17) and the implication HOLD. The residual
d_G >= ca is equivalent to the uniform lattice mass gap itself.

### Section 4. All other statements

- L15 (summary PROVED). HOLDS as a summary of (21), (20), (10) and (8).
- L110 (single crossing). HOLDS. J_qp = <J delta_q, J delta_p>, so
  |J_qp| <= 1/2 by Cauchy-Schwarz. Collinearity is excluded: with e an edge
  of p not in q, g = d delta_e is in the range, <J delta_p, g> = +-1 and
  <J delta_q, g> = 0. Since sum_q J_qp^2 = J_pp is finite, the sup over
  q != p is attained on a finite set, so s_* < 1. l^2 approximation controls
  every coefficient, so |(du)_q| < theta for q != p, and the image marks p
  alone.
- L112-125, (9). HOLDS. The family condition makes the conditional density
  factor over copies and makes each summand see at most one copy. On E_p no
  affected face is marked and on V E_p only p is, so F^{(p)} rises by c_p.
  With density ratio rho >= r, |x|^2 + rho |x + c|^2 >= (r/(1+r))|c|^2.
  E_p and V E_p are disjoint. Integrating over the exterior gives
  (r/(1+r)) |c_p|^2 mu(E_p). Law of total variance and the 1/J_0 family
  give (9) on the torus; the slice passage at fixed grid is valid.
- L127-133, (10). HOLDS. For one colour, <F,(1-K_I)F> = E Var(F | flags,
  unflagged spins). Given these, F = const + sum over flagged e of
  g_e(x_e), independent. Cap flags: g_e is zero on the cap (L25). Base
  flags: Var g_e <= 4 sum_{p ni e} |c_p|^2 rho_h(Y_p). Then (2)-(3) give
  p_0 C(1+beta)^{15/2} e^{-beta D_theta} per incidence, with no factor M.
- L135 (restricted chain, all F_c). HOLDS. With F~ = F - nu F and
  |F~| <= sqrt(M) ||c||_2: nu(G) Var_pi F = int_G |F~|^2 - (int_{G^c} F~)^2
  / nu(G) >= Var_nu F - M nu(G^c) ||c||^2 (1 + nu(G^c)/nu(G)). With
  nu(G^c) <= 3 n^{3 - cK_0}, M = 3n^3, a large K_0 makes this
  o(e^{-(I_theta+eps) beta}). Rejection removes jumps only.
- L139-143, (11). HOLDS. |1 - ab| <= |1-a| + |1-b| and invariance under
  conjugation and inversion give |1 - U_p| <= sum of the five others; with
  |1-U|^2 = 2D and Cauchy-Schwarz, D_p <= 5 sum D_q. The four cubes have
  disjoint five-face sets (21 faces in all). S_i has p, four opposite faces
  and two (i,k)-type sides per cube: 1 + 4*3 = 13. Half-weighted sum =
  D_p + sum_opp D + (1/2) sum_sides D >= D_p + (1/2)(4/5) D_p = 7 D_p/5.
  Cauchy-Schwarz and (1) for 13 faces in direction i, resp. j, give (11).
  Credit: the five-face bound is row 1151 (`gap-solve5-astra62.md` L300).
- L145-152, (12). HOLDS. Tr(Pi_W P^2 Pi_W) = Tr(G^{-1/2} V^* P^2 V G^{-1/2})
  <= ||G^{-1}|| sum_p ||P(Y_p - nu Y_p)||^2 <= ||G^{-1}|| sum_p q nu(Y_p).
  With (9) and (11): exponent 7D_theta/5 - theta^2/2 - eps, prefactor
  z_beta^{-14} <= C(1+beta)^{21}. At pi/2: 7/5 - pi^2/8 > 0 (about 0.166).
- L154. HOLDS. Trace <= M delta, so at most M sqrt(delta) eigenvalues exceed
  sqrt(delta); on the rest <v,P^2 v> <= sqrt(delta) and the band step of
  (8) applies. The caveat on the scalar sum is correct.
- L158-164, (13). HOLDS. Pair U and VU on E_p and V E_p; X_{t_*} is the
  same; the two-square inequality gives the factor r/(1+r). Then
  E|f(X_0) - f(X_{t_*})|^2 = 2<f,(1-P^{t_*})f> <= 2 t_* <f,(1-P)f>, valid
  for spectrum in [-1,1]. The torus-to-slab passage and the Fatou
  truncation (bounded Radon-Nikodym ratio at fixed beta) are valid.
- L166. HOLDS. I_{pi/2} = 1 + pi^2/8 < 3pi^2/11 iff 88 < 13 pi^2 (true).
  On the band <f,(1-P)f> <= 1 - e^{-aE} <= aE, and a e^{(I+eps)beta} -> 0.
- L168 (ARGUED, not counted). Sound as stated: every edge within pi/9 of 1
  gives plaquette angle <= 4pi/9 < pi/2; separated four-edge blocks are
  conditionally independent; row 1215 (26) gives each the negative sign with
  probability >= p_beta; b_* E_* is about 0.937 < 1.
- L174-178, (14). HOLDS. Overlap = E_q min(1, R_1 R_2); concavity in each
  variable; two-point reduction with x = q(R=u), y = p(R=l) gives
  u = (1-y)/x, l = y/(1-x), x + y <= 1. Outcome sum x^2 + y^2 +
  2 min(x(1-x), y(1-y)). If max < 1/2: xy >= (1-x)(1-y)/D >= 1/(4D) and the
  mixed term >= min(x,y). If max^2 < (xy)^{2/3} then max^2 < min, which
  gives min >= (xy)^{2/3}. So overlap >= (4D)^{-2/3} >= D^{-2/3}/4.
- L180 (sharpness). HOLDS. x = t^2, y = t: D ~ t^{-3}, overlap ~ 3t^2.
- L182-188, (15). HOLDS. In temporal gauge the one-step kernel from
  (s,z) is proportional to b_z(u) exp(beta sum_{e in J} s_e.u_e); the
  log-ratio oscillation is <= 2 beta sum |s_e - s'_e| <= 4k beta. U and Y
  are conditionally independent with this law. (14) gives row overlap
  delta = e^{-8k beta/3}/4; a further Markov kernel keeps it. Dobrushin
  contraction 1 - delta on oscillation, compactness and continuity of
  eigenfunctions give <f,(1-R_J)f>_z >= delta Var_z f. Upper bound with the
  predictor f(U).
- L190. HOLDS. 8 b_*/3 < 1 iff 88 < 9 pi^2 (about 88.83; pi > 223/71
  gives 9(223/71)^2 about 88.78 > 88). Row 1215 (26) gives each sign of p
  probability >= p_beta given the exterior and both ends (read at
  `gap-solve23-astra62.md` L433-438), so Var(Y_p | .) >= p_beta E(Y_p | .).
  Wording: the step to the true transfer uses the factor 2 of
  E Var(f | rest, U, Y) <= 2<f,(1-P)f>; the file leaves it implicit.
- L218: see Section 3.
- L220-226, (18). HOLDS. From the traceless wall of row 1215 (26), right
  multiply one edge along the axis of U_p by angle theta - pi/2 + xi; the
  six incident traces are 1-Lipschitz, cost <= 6 times the angle. Small
  Haar balls and compactness keep the bound uniform in the exterior.
  Coefficient times b_*: b_* E_* is about 0.937, so theta near pi/2 works.
  With c n^3 separated sets the no-mark probability is <=
  (1 - p)^{cn^3} -> 0, and ||1_B P 1|| = sqrt(nu(B)) -> 1.
- L230-237, (19). HOLDS. One link moves F by <= 4, so the conditional
  variance is <= 4 (the file's 16 is also true). With (9),
  ratio <= C n^{-3} e^{(I+eps)beta}, which is o(n^{-2}) since
  b_*(1 + pi^2/8) is about 0.83 < 1.
- L241-252, (20). HOLDS. With initial deficit < D_theta/2 the density ratio
  is in [r, 1]. Two-point records give independent binary choices with
  new-choice probability in [r/(1+r), 1/2], each raising F by 1. Reverse
  Markov gives N >= c''M with positive probability. v >= c' M r -> infinity.
  E D^4 <= 2v + 3(2v)^2, Paley-Zygmund: Pr(D^2 >= v) >= v^2/(2v + 12 v^2)
  >= 1/14 for v >= 1. One of F, F' is >= sqrt(v)/2 from m; same law gives
  1/28.
- L254-262, (21). HOLDS. nu(G_n) Var_{nu|G_n} F >= c_1^2 M r (c_2 -
  nu(G_n^c)), the jump form is <= (10) with c_p = 1, and the ratio has
  exponent 4 - theta^2/2 - eps, which is o(a) as in (7). It needs only
  nu(G_n) -> 1; gauge invariance keeps the chain on physical functions.
- L266-275, (22). HOLDS. The error of the predictor F_c(X_{t_*}) is at
  least the expected conditional variance from (9), and equals
  2<F_c,(1-P^{t_*})F_c> <= 2 t_* E_P(F_c). Dividing (10) by this gives the
  second line.
- L277. HOLDS, by (22) and the exponent check of (7).
- GUIDE and OPEN blocks (L3-13, L17, L21-23, L32, L172, L192, L279, L283).
  Labels are accurate. External links and PR heads were not refetched.
  The last line of the file (L285) is an accurate summary.

### Restatement search

Fixed-string greps over `library/` for first-return, T_G, D^{-2/3}, J_{pp},
rank three, cap/base, gamma_d, base flag, 35\pi^2, 13\pi^2, 9\pi^2,
two-point record, Paley; hits read at the matching lines.
- (1) is row 1149 (23), as cited. (11) uses the five-face bound of row 1151.
  (8) and (12) apply the marked-trace method of rows 1290 and 1298 (30).
  J_pp = 1/2 in (4) was used before in `gap-solve26-astra62.md` L455 and
  `gap-solve27-astra62.md` L187.
- Not restatements: (6)-(7), (9)-(10), (13)-(22). Row 1300
  (`gap-mini-solve-ax-opus.md` RESULT, L180) tested (37) only on free modes
  and did not kill it; (7) is the first counterexample to its premise for
  the concrete K.
- The OPEN residual of L283 restates the target: by (17) it is equivalent
  to a uniform lattice gap of P.

### Numeric guide (not a proof step)

Python arithmetic only: 35 pi^2 = 345.44 < 352; 13 pi^2 = 128.3 > 88;
9 pi^2 = 88.83 > 88; b_*(4 - pi^2/8) = 1.028; b_*(1 + pi^2/8) = 0.830;
8 b_*/3 = 0.991; b_* E_* = 0.937; 7/5 - pi^2/8 = 0.166. All agree with
the hand steps.

### Not checked

External links (Sussman-Alpoge outline lines, PR heads) were not opened.
Rows 1149, 1151, 1215 were read at the cited statements; their full proofs
rest on their own checks.

### Counts

37 PROVED blocks: 37 HOLD, 0 HOLD AFTER CORRECTION, 0 FAIL. Four wording
precisions (L28 cap constant, L68 "isotropic", L190 implicit factor 2,
L230 constant 16 can be 4). One ARGUED block (L168), sound as stated.

RESULT: 37 of 37 PROVED statements of row 1315 HOLD, 0 need correction, 0 FAIL; main finding: on the bare schedule at the one-loop slope 11/(3 pi^2) the cap/base chain of row 1298 has gap o(a) on every gauge-invariant restriction of probability tending to one ((6), (7), (21); endpoint 35 pi^2 < 352), so the premise gamma_d >= ca of row 1298 (37) is false for that kernel, while the true Wilson transfer gives each plaquette test low-energy weight O(q) -> 0 by (8); the residual d_G >= ca around (17) does imply a lattice gap, but by (17) it is equivalent to the uniform lattice gap of P itself, so it restates the target; the mass gap stays OPEN.
