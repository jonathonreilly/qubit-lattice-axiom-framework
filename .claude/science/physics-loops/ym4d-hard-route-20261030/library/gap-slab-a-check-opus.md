# Check of library/gap-slab-a-astra.md (FINISH row 1138)

Checker: Claude Opus 5.5 (this file). Status: done, steps 1-6. Written as I go.

Files read for this check (paths relative to the lane folder):
- library/gap-slab-a-astra.md (file under check)
- library/gap-council-op-astra.md (row 1132; defines statement (A))
- library/gap-council-brief.md (setting)

## Log

Note: the first tool call created this file without the plan. The plan is
added here, in the second call.

## Plan (six steps)

1. Read the file under check, row 1132 and the brief in full.
2. Strong-coupling sign: the polymer bound with b = e^(256 beta) - 1, the
   induction 41/42, and the chart remark.
3. The volume bound (1) and the noisy-sign experiment (commutator density
   (pi - theta)/(2 sin theta), s_4); the refresh-model counterexample.
4. The Moser non-locality, the coefficient -1/25344 in (2) and its
   remainder; the constant-candidate failure and the Dobrushin bound (3)
   with its order of limits.
5. The line-spin model with gap m and D to infinity, and its extraction.
6. Verdict table and RESULT line.

### Step 1 result (reading)

- Read in full: library/gap-slab-a-astra.md (183 lines),
  library/gap-council-op-astra.md (106 lines), library/gap-council-brief.md
  (122 lines). Line numbers below refer to library/gap-slab-a-astra.md
  unless another file is named.
- Statement (A) is defined in gap-council-op-astra.md, lines 29-35. The file
  under check restates it at line 30. The restatement matches: fixed t, p
  (the delta of row 1132 is redundant, since q_G = 1/4 by row 1132 line 37),
  all dyadic L >= L_0, all j >= j_0(L), k = floor(t/a), the density
  j_k(x,y) = T^k(Sx,Sy)/[lambda^k psi(Sx) psi(Sy)], and the sign-test form
  of row 1132 line 51.
- Checked by hand: the stationary pair law is
  T^k(U,V)/(lambda^k psi(U) psi(V)) times pi(dU) pi(dV). The map S^{-1}
  sends pi to H. So j_k is the Haar density of the pair in the chart, and
  j_k(x,y) = [b_k(Sx,V)/rho(V)] at V = Sy, with
  b_k(U,V) = T^k(U,V) psi(V)/(lambda^k psi(U)). This is the identity used
  at line 64.
- Parts under check: Section 3 (lines 32-66), Section 4 (lines 68-101),
  Section 5 (lines 103-160), Section 6 (lines 162-179).

### Step 2 result: strong-coupling sign and chart remark (lines 34-66)

**Statement S3a (lines 34-38, proof lines 40-62).** For beta <= 10^-6,
every k >= 1 and every admitted cube, D_{E,V} b_k(U,V) > 0. Verdict: HOLDS.

- Local form (lines 40-44). Put psi(V) = lambda^{-1} int T(V,W) psi(W) dH(W)
  into b_k. Then T^k(U,V) and T(V,W) each give one factor M(V), so the
  V-dependence carries M(V)^2 = exp[beta sum_{q spatial} w_q(V)]. With the
  gauge integrals and the two neighbouring slices frozen, the rest of the
  V-dependence is e^{beta w} of the two temporal plaquettes at each edge.
  Each temporal face reads V_e once. All other factors are positive and do
  not depend on V. Checked.
- Degree 20 (line 46). A spatial face has 4 edges; each edge lies in 4
  spatial and 2 temporal faces, so 5 others per edge. Checked.
- Bound |z_C| <= b^{|C|} (lines 46-54). I used the unit left-invariant
  fields X_a f(U) = d/dt f(U exp(t i sigma_a)). Then Delta_e = sum_a X_a^2
  on the round unit three-sphere; check: sum_a X_a^2 U = -3U, the value
  -4j(j+1) at j = 1/2. Each X_a puts the unitary i sigma_a (up to sign) at
  one occurrence of U_e or U_e^{-1}, and creates no new occurrence. So
  (1 - Delta_e) gives at most 1 + 3 d_e^2 terms. Each term is a product of
  normalized traces of unitaries, of modulus at most 1. Also
  sum_e d_e = sum_q h_q (number of edges read by q) <= 4 sum_q h_q.
  1 + 3d^2 <= 4^d: true at d = 0, 1; the step needs 2d + 1 <= 4^d. The
  exponential series gives prod_q (e^{256 beta} - 1). The first-order term
  is sharp: for a spatial face, D_{E(q)} w_q = 4^4 w_q = 256 w_q. Checked.
- Factorization and recursion (lines 56-61). Components of a face set have
  disjoint edge sets, and (1 - Delta_e) is the identity on a function that
  does not read V_e. This is the usual hard-core polymer sum. Checked.
- Induction (line 62). The ratio Z_{A\N[C]}/Z_{A\{q}} needs at most
  21m - 1 deletions, each costing at most 42/41 by the induction hypothesis
  (which also gives positivity of every smaller Z_B). (41/42)^21 >= 1/2 by
  Bernoulli, so (42/41)^{21m} <= 2^m. Counting: a depth-first walk on a
  rooted spanning tree has 2(m-1) steps, each to one of at most 20 graph
  neighbours; the visited set is recovered. Sum over m:
  sum_m 20^{2(m-1)} 2^m b^m = 2b/(1 - 800b). At beta <= 10^-6,
  b <= 256 beta/(1 - 256 beta) <= 512 beta = 5.12e-4 < 1/1600, so the
  correction is at most 1/400 < 1/42. Checked.
- Entrance law (line 38, line 62). Stationarity gives
  int rho(U) D_{E,z} b_k(U,z) dH(U) = D_E rho(z). So this branch has
  entrance D_E rho dH, not Haar. The text says so. Checked.

**Statement S3b, the chart remark (line 64).** Verdict: HOLDS.

- j_k(x,y) = [b_k(Sx,V)/rho(V)] at V = Sy: checked in step 1.
- At beta = 0: T is the projection on constants, psi = 1, S = id, j_k = 1,
  p_* = 1. Checked.
- Fixed cube, small beta: T_beta is entire in beta with smooth kernels. T_0
  is an orthogonal projection, so its resolvent has norm at most 2 on
  |z - 1| = 1/2, and the Neumann series converges once
  ||T_beta - T_0|| < 1/2. Then psi, rho, u and the flow converge in every
  C^r norm, and D_{E,y} j_1 (order 2|E|, fixed at fixed n) tends to 1
  uniformly. The interval depends on n, as the text says. Checked.
- Higher k: j_k(x,.) = int j_{k-1}(x,z) j_1(z,.) dH(z), and J_{k-1} r is
  again Haar-stationary. Checked.

No numeric run was used in this step.

### Step 3 result: the volume bound (1), the noisy-sign experiment, the refresh model (lines 70-101)

**Statement S4a, the volume bound (1) (lines 70-81).** Verdict: HOLDS.

- N = n^3/4 (line 70). In each plane x_3 = const, the 12-plaquettes with
  lower corner at even (x_1, x_2) are edge-disjoint; different planes use
  different edges. n (n/2)^2 = n^3/4. Checked.
- Logic of (1). Let Q_sigma be the physical law from sigma I and R_sigma the
  branch law. Domination gives Q_sigma >= p R_sigma for every sigma (after
  line 83). So M_N >= p P_branch(B_N <= s_4 + u) >= p (1 - 1/(4Nu^2)),
  using Chebyshev with s_4(1 - s_4) <= 1/4. This is (1). Checked.
- Consequences (line 81). Chebyshev gives M_N <= v_N/u^2 when the mean of B_N
  is at least s_4 + 2u. 1 - 2/pi < 1 - 14/22 = 4/11, and
  (4/11)^4 = 256/14641 < 1/50, so s_4 < 51/100. Checked.

**Statement S4b, singular inputs (line 83).** Verdict: HOLDS.

- Transpose. With H(dy) r(y,dz) = H(dz) r^*(z,dy) and the H-symmetry of
  W_E, the transpose of H(dx)(rW_E)(x,dy) is H(dx)(W_E r^*)(x,dy). j_k is
  symmetric. Checked.
- Extension to every x. The left side int j_k(x,y) phi(y) dH(y) is
  continuous in x. The right side is the convolution of a bounded function
  with the L^1 kernel h^{(x)E}, so it is continuous and does not see the
  null set where r^* is undefined. A countable dense set of tests gives the
  a.e. inequality for all tests at once; continuity extends it to every x.
  Checked.
- S(sigma I) = sigma I. The velocity field is equivariant under global
  conjugation. At a central configuration it is a vector in su(2)^E fixed
  by the adjoint action, hence zero. The text's argument (discrete fixed set,
  continuous flow) gives the same. Checked.

**Statement S4c, the noisy-sign experiment (line 85).** Verdict: HOLDS.

- The commutator density relative to Haar is sum_d chi_d/d, since
  E chi_d([a,b]) = tr(I/d^2) = 1/d. With chi_d = sin(d theta)/sin(theta)
  and sum_d sin(d theta)/d = (pi - theta)/2 on (0, 2 pi), this is
  h = (pi - theta)/(2 sin theta). Normalization: the Haar angle density is
  (2/pi) sin^2(theta), and int_0^pi (pi - theta) sin(theta) d theta = pi.
  Checked.
- Fair sign: the angle of -g is pi - theta, so the output angle density is
  (1/(2 pi)) sin(theta) [(pi - theta) + theta] = (1/2) sin(theta). The
  likelihood depends only on the angle (h is a class function, sigma is
  central). Posterior mean 1 - 2 theta/pi. Mean absolute value
  int_0^{pi/2} (1 - 2 theta/pi) sin(theta) d theta = 1 - 2/pi. Checked.
- Domination by Bin(N, s_4). Given z and the decoder output d (independent
  of the signs given z), the success indicators are independent with
  parameters at most (1 + |m_i|)/2, m_i = prod_{e in q_i} (1 - 2 theta_e/pi).
  The m_i read disjoint edges, and the angles are i.i.d. with density
  (1/2) sin(theta) after averaging over the signs. So the dominating
  Bernoulli variables are independent with mean s_4. Checked.
- Numeric guide (not proof; pure Python, 4 x 10^5 Haar commutators,
  script in the scratchpad): bin masses of the commutator angle match
  (1/pi) sin(theta)(pi - theta) within 6e-4; E|1 - 2 theta/pi| = 0.36323
  against 1 - 2/pi = 0.36338; s_4 = 0.508718.

**Statement S4d, the refresh model (lines 89-101).** Verdict: HOLDS.

- Model (line 93). Pi_e and Delta_e commute and (I - Pi_e) Pi_e = 0, so
  exp[-a H_{e,a}] = e^{-am} e^{a d_a Delta_e} + (1 - e^{-am}) Pi_e. On a
  Peter-Weyl block the energy is sum over nontrivial links of
  m + 4 d_a j_e(j_e + 1), at least m. Both operators are bi-invariant, so
  they commute with gauge projection. Haar is stationary, so rho = 1 and
  S = id. Checked.
- Physical side (line 95). No refresh on 4 links in k steps has probability
  e^{-4 m t_a} >= q. For an unrefreshed link the increment is a heat step of
  time d_a t_a, and E||g - I||_op^2 = 2(1 - E (1/2)tr g) = 2(1 - e^{-3 d_a t_a}).
  The trace difference is at most the sum of the four operator distances.
  So the conditional match probability tends to 1 uniformly in x as
  d_a t_a -> 0. Checked.
- Branch side (line 97). Under Haar the trace w has density
  (2/pi) sqrt(1 - w^2) <= 2/pi, so an interval of width 2 epsilon has mass
  at most 2 epsilon. ||h||_2^2 = pi^2/6 <= 2. Cauchy-Schwarz gives match
  probability at most sqrt(2) sqrt(2 epsilon) = 2 sqrt(epsilon), uniformly in
  x and z. Checked.
- Chebyshev: physical probability of at most Nq/2 matches is at most
  (N/4)/(Nq/4)^2 = 4/(Nq^2); branch probability at least 1 - 4/(Nq^2). So
  p <= 4/(Nq^2 - 4). N = n^3/4 grows as a -> 0 at fixed L. Checked.
- Logic (line 101). (A) gives a uniform gap through the consumer
  (row 1132 line 37); the model has a uniform gap m and fails (A) for every
  t. So (A) is strictly stronger in this class. The text limits the claim
  correctly.

### Step 4 result: Section 5 (lines 105-160)

**Statement S5a, non-locality at intermediate times (lines 105-114).**
Verdict: HOLDS.

- lambda(gamma) >= int e^{gamma F} dH (line 107). C_E P >= Pi_0 in form
  order (nonnegative multipliers, constant multiplier 1). Test with
  f = M/||M||: <M, T M>/||M||^2 >= (int M^2)^2/int M^2 = int e^{gamma F} dH.
  The text's word "sandwiching" means this choice. Checked.
- Convexity of log lambda and (log lambda)'(beta) = int F d pi: Holder
  convexity of each l^{-1} log <1, T^l 1>, limit since <1, psi> > 0;
  lambda' = <psi, T' psi> = lambda <psi, F psi>. Checked.
- lambda(gamma) >= I(gamma)^{n^3/64} (line 109). The (n/4)^3 corner
  12-plaquettes are edge-disjoint. An unselected 13- or 23-plaquette has a
  direction-3 edge, which is untouched. An unselected 12-plaquette cannot
  take all four edges from selected ones, since those lie 4 apart. So every
  unselected plaquette has a Haar link and mean zero; Jensen gives the bound.
  I(beta) >= 1 + beta^2/8 from the even moments and int w^2 = 1/4. Checked.
- c_beta: convexity gives (log lambda)'(beta) >= log lambda(beta)/beta >=
  (n^3/64) log(1 + beta^2/8)/beta; divide by 3n^3. 64 x 3 = 192. Checked.
- Mixture and contradiction (line 114). The density at time s is
  1 - s + s rho, so the image law is (1-s)H + s pi. Between-component
  variance s(1-s)(mean difference)^2 >= s(1-s) c_beta^2. Clipped
  approximants: Var = O((R+1)^3/n^3); triangle inequality gives
  sd <= sqrt(Var) + epsilon. Let n grow at fixed epsilon, R(epsilon), then
  epsilon -> 0. Checked.

**Statement S5b, the coefficient in (2) (lines 116-136).** Verdict: HOLDS.

- Which terms enter (line 123). With psi = M phi, the Perron equation is
  phi = lambda^{-1} C_E P (M^2 phi). On gauge-invariant non-constant blocks
  the support has no degree-one vertex, so it has a cycle of at least 4
  edges, and the multiplier is at most a_2^4 = O(beta^4). The input
  M^2 phi minus its mean is O_n(beta). So phi = const + O_n(beta^5), and rho
  equals e^{beta F}/int e^{beta F} up to O_n(beta^5) (better than the stated
  order three). The phrase "M psi is constant plus O_n(beta)" is true; it
  is the input bound for this step.
- Multivariate reduction. Give each face its own coupling. The beta^3
  coefficient is the sum of mixed coefficients over face multisets of size
  3, each computed in the model with only those faces. Spin 1 on all four
  edges of R needs two fundamental factors on each, so R twice; one face
  must read an edge of Q to move f. A near face Q' != Q gives
  int grad f . grad w_{Q'} dH = 12 int f w_{Q'} dH = 0. Orders 1 and 2
  vanish. So the coefficient is the alpha gamma^2 coefficient of the
  two-face model with density proportional to e^{alpha f + gamma h}.
  Checked.
- Calculation (lines 125-136), redone by hand. B = 1 + gamma h +
  gamma^2 g/2 + O(gamma^3) since int e^{gamma h} = 1 + gamma^2/8 + ....
  u_1 = f (l - Delta_R)^{-1} B with l = 12 solves Delta u_1 = -f B, so the
  Q displacement is alpha I_gamma grad f. Resolvent: 1, h, g go to 1/l,
  h/(2l), g/(l + eta), with eta = 32 (spin 1 per edge, Casimir 8, four
  edges). Base flow u_0 = gamma h/12 + O(gamma^2), so
  h(Y_s) = h + s gamma |grad h|^2/l + O(gamma^2). Expanding
  N_s/D_s to second order and integrating s over [0,1] (int s = 1/2,
  int s^2 = 1/3) gives exactly the text's line 132-133 expression; the
  first-order term h/(2l) - s h/l integrates to zero.
  |grad h|^2 = l h^2 - eta g/2 from Delta(h^2) = -2 l h^2 + 2|grad h|^2
  = -eta g. Then 1/88 - 1/48 + 1/108 = (54 - 99 + 44)/4752 = -1/4752.
  Pairing: int |grad f|^2 = 12/4 = 3, int g^2 = 1/16, so
  3 (-1/4752)/16 = -1/25344. Checked.
- A second route for the same number: pair the s-integrated second-order
  term with g directly, using int h^2 g = int g^2 = 1/16 and
  int |grad h|^2 g = (l - eta/2)/16. This gives
  (1/16)(1/88 - 1/48 + 1/432 + 1/144) = (1/16)(-1/4752). Same value.
- Consequence (line 121): an exact common radius on an interval of small
  couplings would make A_{QR} vanish there for distant pairs (Haar
  independence and int g = 0). Checked.

**Statement S5c, remainder control and scope (lines 138-144).**
Verdict: HOLDS.

- Tube bounds (line 140). In the tube ||U||, ||U^{-1}|| < e, each plaquette
  trace is at most 2e^4, the exponent has O(b) terms, so the normalized
  kernel is 1 + O(|beta| b), also for complex beta. On L^infinity the
  resolvent of Pi_0 on |z - 1| = 1/2 is bounded (at most 6). The Riesz
  projection gives psi = 1 + O(|beta| b), extended to the tube by the
  Perron integral. Checked.
- Inverse Laplacian (line 142). The tube is invariant under right
  multiplication by real elements; the heat average of a mean-zero
  holomorphic function stays mean zero; for v >= 1,
  ||p_v - 1||_{L^1} <= sum_{d>=2} d^2 e^{-(d^2-1)v} <= C e^{-3v}, and
  telescoping gives C b e^{-3v}. So sup|u| <= C b sup|rho - 1| <=
  C |beta| b^2. Cauchy estimates give the component speed bound; at
  |beta| <= c_0/b^2 the flow stays in the smaller tube (Gronwall on the
  matrix norms). Checked.
- Tail (line 144). Cauchy on the disc of radius r = c_0/b^2 with |A| <= C_0
  gives tail <= 2 C_0 (|beta|/r)^4 for |beta| <= r/2. At beta = b^{-9}
  this is 2 C_0 b^{-28}/c_0^4, against the cubic term b^{-27}/25344. Half
  of the cubic term remains: b^{-27}/50688. b = 3n^3 is polynomial in n,
  so this beats C e^{-cn/4}. Checked.
- Exact range outside a countable set (line 144). On a fixed cube the
  Perron root is simple and isolated at every real beta > 0, and the real
  flow has a positive denominator, so A_{QR} is real analytic on a
  neighbourhood of [0, infinity) (at 0 by the disc above). Its cubic
  coefficient is nonzero, so its zeros are discrete. Countable union over
  cubes. Checked.

**Statement S5d, failure of the constant candidate (lines 146-148).**
Verdict: HOLDS.

- Cited input: PR 10114 source, MASS_GAP_LOCAL_BLOCK_ASTRA.md at
  f76f6c649c, bound (11). I read its derivation, (1)-(11), in the primary
  text. It gives C_F(a) = <F psi, (T/lambda_0) F psi> >= eta_C(beta) > 0 for
  every beta > 0, independent of volume. For an elementary plaquette:
  b = 4, p_B = 13, eta = (1/16) e^{-68 beta}/(1 + 1/(4 r_f^4)) with
  r_f = I_2/I_1. Since <f, P_0 f>_pi = <psi f, T psi f>/lambda, this is the
  input the text uses. I checked its steps (2), (3), (4), (7), (9), (10) by
  hand: they hold.
- Jensen step. P_0 is positive and self-adjoint on L^2(pi). With
  m = ||f||^2 <= 1 (|w| <= 1), Jensen on mu_f/m gives
  <f, P_0^k f> >= <f, P_0 f>^k / m^{k-1} >= eta^k. Checked.
- Variance (line 148). Each edge of the 4D torus has 6 plaquettes with 3
  other edges: 18 neighbours. A neighbour change tilts one plaquette weight
  by a log of oscillation at most 4 beta; |Cov(1_A, phi)| <= osc(phi)/4
  gives influence at most beta. Row sum at most 18 beta <= 3/8 for
  beta <= 1/48. Dobrushin's comparison gives covariance at most a constant
  times sum [(I - C)^{-1}]_{ee'}; with disjoint 8-edge supports this is
  O(1/N), uniformly in the period and in k. The period limit gives the
  stationary pair law for gauge-invariant observables. Chebyshev at
  eta^k/2 gives p <= O(1/(N eta^{2k})). Checked.

**Statement S5e, the Dobrushin bound (3) (lines 150-156).** Verdict: HOLDS.

- d/d(top edge) of log T^k(U,V) = (top half-weight term, independent of U)
  + beta E[X w_top], where the top temporal plaquette reads three free
  edges, all with lower time k - 1. |X w| <= 1. Checked.
- Mismatch. The comparison gives m <= sum_l C_ff^l C_fb 1_b; a walk from
  lower time k - 1 to the bottom slice needs at least k - 1 steps, since a
  plaquette changes the lower time by at most one. So each mismatch is at
  most sum_{l >= k-1} d^l = d^{k-1}/(1 - d), and the derivative difference
  is at most beta x 2 x 3 x d^{k-1}/(1 - d). Checked.
- Cross ratio: one geodesic of length at most pi per top edge, |E| edges;
  psi factors cancel. Two rows of j_k have likelihood ratio with mean one
  and log oscillation at most -log p, so its minimum is at least p.
  Averaging over the denominator input gives j_k >= p. Checked.
- k >= 2 is used so that the three edges are free; this is consistent.

**Statement S5f, order of limits (line 158).** Verdict: HOLDS.

- With beta in [0, 1/48], d <= 3/8 and beta/(1 - d) <= 1/30. The exponent is
  at most (6 pi/30) 3 n^3 (3/8)^{k-1} with k = floor(t/a_j) about t n/L,
  which tends to 0. So g = 1/2 passes for all fine cutoffs at each L, with
  any t. This is an assigned-spacing strong-coupling family, not the
  asymptotically free trajectory; the text says so. Consistency with S5d:
  there N eta^{2k} -> 0 at k about t n/L, so no conflict. Checked.

Citations in line 158 (row 863, row 1031 F8): checked in step 5 below.

### Step 5 result: Section 6 (lines 164-179) and the citations

**Statement S6a, the line-spin model (lines 164-175).** Verdict: HOLDS.

- Model (line 164). The weight factors into 4n^3 independent closed chains,
  one per spin type and transverse position. The bond kernel
  p_tau(g^{-1}h), tau = ma/3, is symmetric, pointwise positive, and has
  multipliers e^{-tau(d^2-1)} > 0. Reflection positivity: split each
  crossing bond as C_a = C_a^{1/2} C_a^{1/2} (again a positive symmetric
  heat kernel); the usual square-completion gives the positive form.
  Permuting axes permutes the spin types. Checked.
- Spectrum (lines 166-171). Tr C_a^b = sum_d d^2 e^{-tau b (d^2-1)}
  (Peter-Weyl: the spin block of dimension d has multiplicity d^2 and
  Laplace eigenvalue -(d^2-1)). The transfer in direction 0 is
  C_a^{(x) n^3} on the time-parallel spins times the rank-one kernel
  A(V)A(V') on the perpendicular spins, with eigenfunction A. Top
  eigenvalue simple; next ratio e^{-3 tau} = e^{-ma}, so the gap is exactly
  m in physical units for every a and n. Checked.
- Pressure and excess (lines 171-175). F_a(n) = 4n^3 log Z_line(n),
  Z_line(n) -> 1, so f = 0 and D_a(n) = F_a(n). The d = 2 term gives
  Z_line(n) >= 1 + 4 e^{-3 tau n} = 1 + 4 e^{-mL}. So
  D_a(n) >= 4 (L/a)^3 log(1 + 4e^{-mL}) -> infinity as a -> 0 at fixed L,
  and D^+(L) = infinity for every L. Checked.

**Statement S6b, extraction in the line-spin model (line 177).**
Verdict: HOLDS.

- psi = 1 (x) A/||A||, so rho depends only on perpendicular spins, u too,
  and the flow fixes the time-parallel spins. In the chart the
  perpendicular pair has density 1 (it is pi_perp (x) pi_perp, mapped to
  H (x) H). The time-parallel pair has density prod p_{ms/3}(x^{-1}y),
  s = ka. Checked.
- (1 - Delta) p_tau = sum_d d^3 chi_d e^{-tau(d^2-1)}, so the nonconstant
  part is at most sum_{d>=2} d^4 e^{-tau(d^2-1)} in sup norm; this
  decreases in tau and tends to 0. For a <= t/2, s = a floor(t/a) >= t - a
  >= t/2. Each factor is positive with mass one; r is Haar-stationary
  since D_E 1 = 1. So p = 1 for every a <= t/2 and every n. Checked.

**Statement S6c, the sufficient extra input (line 179, inside an OPEN
paragraph).** Verdict: HOLDS (as a consequence of row 720).

- I read row 720 (library/gap-phys-seed.md): Corollary Z1 (line 259 and
  table line 395: b m(b^3) >= 256 D(b/4) + 29.64 gives the seed),
  Corollary Z2 (line 306, the fixed-cutoff form of this statement) and
  Theorem ZD-c (lines 311-320). With z^-(4L) >= 4L m_0 > 256 D^+(L) + 30,
  limsup and liminf give z_j(4L) >= 256 D_j(L/a_j) + 29.64 for all large j;
  b = 4L/a_j is a multiple of 4 and at least 12. Z1 gives the seed for all
  large j, and ZD-c gives (BDD-Delta). The text's statement is the
  continuum form of Corollary Z2. The line-spin model has D^+ = infinity,
  so it does not meet this condition; no conflict.

**Citations checked in the primary text.**

- Row 863 = library/gap-crux-skeleton-max.md; lines 202-203 are Lemma B2
  (Hopf), with cross ratio kappa <= e^{4 beta_t N_b}: extensive, as line 158
  says.
- Row 1031 = library/gap-afield-a-max.md; line 343 is F8 (Dobrushin,
  disagreement percolation, Doeblin and renewal in time; "capped at small
  beta"). This matches lines 5 and 158.
- PR 10114 source at f76f6c649c: Section 2 starts at line 106 and (11) is
  at line 164, inside the cited range 106-169.
- prior/gap-lit-casimir.md lines 14-32: small thermal weights do not by
  themselves bound D. Row 1032 (library/gap-afield-b-max.md) Lemma CHAIN-4:
  D = G_0 + G_1 + G_2 + G_3, all nonnegative. Both match line 179.

### Step 6 result: verdict table

Who checked what: every step below was checked line by line by hand by
Claude Opus 5.5 (this file). The author of row 1135 is gpt-6.2-astra, a
different provider. One numeric run was used, as a guide only (pure Python,
4 x 10^5 Haar commutators, far under 2 GB; script in the scratchpad, not in
the lane): it agrees with S4c and proves nothing.

| Id | Statement (file under check) | Lines | Verdict |
|---|---|---|---|
| S3a | D_{E,V} b_k > 0 for beta <= 10^-6, every k >= 1, every admitted cube: polymer bound with b = e^{256 beta} - 1, induction Z_A/Z_{A\{q}} >= 41/42, entrance law D_E rho dH | 34-62 | HOLDS |
| S3b | Chart remark: j_k = b_k/rho at V = Sy; p_* = 1 at beta = 0 and on [0, eps_n] at k = 1 on each fixed cube; no common interval; higher k inherit | 64 | HOLDS |
| S4a | Volume bound (1); s_4 < 51/100; 51 percent recovery forces p_* -> 0 | 70-81 | HOLDS |
| S4b | Domination extends to every input, including centre inputs; S(sigma I) = sigma I | 83 | HOLDS |
| S4c | Noisy-sign experiment: h = (pi - theta)/(2 sin theta), output angle density (1/2) sin theta, posterior mean 1 - 2 theta/pi, domination by Bin(N, s_4) | 85 | HOLDS |
| S4d | Refresh model: uniform gap m, p_* <= 4/(Nq^2 - 4) at every fixed t; (A) strictly stronger than a uniform gap among local transfer evolutions | 89-101 | HOLDS |
| S5a | Moser map S_s, 0 < s < 1, not uniformly local in Haar L^2 (c_beta = log(1 + beta^2/8)/(192 beta), mixture variance) | 105-114 | HOLDS |
| S5b | (2): A_QR(beta) = -beta^3/25344 + O_n(beta^4), independent of the separation; no finite coding radius on a small-coupling interval | 116-136 | HOLDS |
| S5c | Remainder control on the disc abs(beta) <= c_0/b^2; no uniform exponential locality bound; unbounded exact range outside a countable set | 138-144 | HOLDS |
| S5d | Constant candidate g = p: largest mass -> 0 as n -> infinity at fixed k, 0 < beta <= 1/48 (input: bound (11) of the PR 10114 source, re-derived here) | 146-148 | HOLDS |
| S5e | Dobrushin bound (3): j_k >= exp[-(6 pi beta/(1 - d)) abs(E) d^{k-1}], d = 18 beta, k >= 2, 0 < beta <= 1/48 | 150-156 | HOLDS |
| S5f | Order of limits: (A) with p = 1/2 on an assigned-spacing family with beta in [0, 1/48]; 18 beta < 1 fails in the window | 158 | HOLDS |
| S6a | Line-spin model: local, hypercubic, reflection positive, simple vacuum, exact gap m, D_a(n) >= 4(L/a)^3 log(1 + 4e^{-mL}) -> infinity | 164-175 | HOLDS |
| S6b | Line-spin model passes the sign test with p = 1 for a <= t/2 | 177 | HOLDS |
| S6c | Sufficient extra input: gap m_0 and liminf D^+(L)/L < m_0/64 give (BDD-Delta) (continuum form of row 720's Corollary Z2, via Z1 and ZD-c) | 179 | HOLDS |

First failing step: none. No correction is needed for any statement.

Remarks that need no correction:
1. Line 62: 21m - 1 deletions suffice; the text's 21m is a valid bound.
2. Line 107: "sandwiching" means the test vector M/||M||; written out in
   step 4.
3. Line 123: "M psi is constant plus O_n(beta)" is the input bound for the
   Perron step; that step gives psi/M = const + O_n(beta^5), so rho agrees
   with e^{beta F}/int e^{beta F} through order four, more than the stated
   order three.
4. Line 140 reuses the letter b for abs(E) = 3n^3; in Section 3, b was
   e^{256 beta} - 1.
5. Line 70: the window 23/10 <= beta <= 13/5 is not used in the proof of
   (1); (1) holds at every beta.

Scope of this check:
- Not re-checked here, used as stated: row 720's Corollary Z1 and Theorem
  ZD-c (S6c only; the brief lists ZD-c as proved and checked once); the
  Frobenius multiplier of rows 778 and 780 (prior work); the Bessel facts
  a_d <= a_2 = I_2/I_1 = O(beta) from GL3-4.
- Re-derived by hand from the primary text: bound (11) of the PR 10114
  source, steps (2), (3), (4), (7), (9), (10), (11).
- Nothing here bears on (A) in the Wilson window, on a Wilson-specific
  route to (BDD-Delta), or on (W). They stay open, as the file says.

RESULT: Row 1138 check of row 1135 (library/gap-slab-a-astra.md, Sections 3-6), Claude Opus 5.5 max, cross-provider (author gpt-6.2-astra), checked line by line by hand with one pure-Python numeric guide that proves nothing: first failing step none; all fifteen statements HOLD with no correction (the strong-coupling sign at beta <= 1e-6 with b = e^{256 beta} - 1 and the 41/42 induction; the chart remark; the volume bound (1) with h = (pi - theta)/(2 sin theta) and s_4 < 51/100; the refresh-model proof that (A) is strictly stronger than a uniform gap; the Moser non-locality; the coefficient -1/25344 in (2), recomputed two ways, with its remainder control; the constant-candidate failure with bound (11) of PR 10114 re-derived; the Dobrushin bound (3) and its order of limits; the line-spin model with exact gap m, D -> infinity and p = 1; the sufficient input liminf D^+/L < m_0/64); open, not moved: (A) in the Wilson window, the Wilson-specific route to (BDD-Delta), and (W); no mass gap is claimed.
