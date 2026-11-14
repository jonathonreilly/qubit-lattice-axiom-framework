# FINISH row 834: area law for 4D SU(2) Wilson loops beyond beta_W = 2/3

Author: Claude Opus 5.5 (max effort), row 834 author lane.
Clone: /Users/jonreilly/ym4d-lead/clone at commit d7a3a22a9e9a6d6485df28693d11e86d041535c6 (2026-11-12).
Lane directory D = .claude/science/physics-loops/ym4d-hard-route-20261030.
During the run the clone advanced to cc2a1c159dd468629ac4e0e9ee58ab8fe9588e9a; `git diff --stat` shows every
library file read here unchanged. The one new file used is D/library/gap-compress-check-astra.md (the
check of row 839), read for its Proposition TB2 verdict only (lines 67-104).
Status: WORKING NOTE. Unchecked. Every statement is marked PROVED (this note), READ (path:line), ARGUED, GUIDE or OPEN.

## Target

Push the area law of row 825 (Theorem A: area law for 4D SU(2) Wilson loops for beta_W < 2/3,
weight exp(beta_W tr U_p / 2), via the background-uniform slab covariance Lemma SC and the slab
reduction Lemma R) to a larger range of beta_W, toward the roughly 0.94 ceiling of
background-uniform slab routes. Improve Lemma SC (the slab is a 3D layer model of S^3 spins with
frustrated orthogonal couplings fixed by the background; single-site influence row sum 6 beta/4).
State the best proved range with explicit constants, the full area-law theorem, the exact blocker,
the bearing of row 839 Proposition TB2, and novelty against D/library/gap-novelty-opus.md.

## Plan (at most eight steps; one step per response; append after each)

1. Read row 825 (gap-arealaw-opus.md) and its check (gap-arealaw-check-astra.md); record the exact
   statements of Theorem A, Lemma SC, Lemma R and the corrections.
2. Read row 839 Proposition TB2 and the needed parts of gap-vmf-lip.md, gap-mixed-opus.md,
   gap-shape-exercise-astra.md (D1, Route C); record what each gives.
3. Determine the exact slab law: spins, couplings, symmetry group of the slab conditional law,
   what a gauge-like fixing inside the slab can remove.
4. Attack 1: field-dependent chord sensitivity a(|F|) and weighted/edge-wise Dobrushin in the slab.
5. Attack 2: block conditioning inside the slab (block influence estimate), explicit constants.
6. Attack 3: comparison with 3D O(4) ferromagnet (Aizenman-Simon); why frustration blocks it; TB2.
7. Assemble the best proved range: full area-law theorem statement with constants.
8. Blockers, novelty against gap-novelty-opus.md, RESULT line.

## Log

### Step 1 (done). Row 825 and its check, as read

Source: D/library/gap-arealaw-opus.md (row 825, Claude Opus 5.5), check
D/library/gap-arealaw-check-astra.md (row 828, Codex gpt-6-astra, HOLDS AFTER CORRECTION).

- Weight exp(beta_W x_p), x_p = (1/2) tr U_p = Re U_p (READ gap-arealaw-opus.md:59-61).
- Layer model: sites h_x in S^3, bonds b=(x,y) with y_b = h_x . O_b h_y, O_b in O(4) fixed,
  J_b in [-1,1]; law prop. to prod_b exp(beta J_b y_b) prod_x sigma(dh_x) (READ :71-75).
- Lemma S: given H (all non-nu edges), the vertical edges of slab k form a layer law on the
  horizontal 3-torus at coupling beta_W, J = 1, O_b = L_a R_conj(a') (READ :186-211; check :82-92 HOLDS,
  with the face-label correction :344, :352-359, which changes no constant).
- Lemma SC: for a layer law on a 3-torus with sides >= 3, beta < 2/3, q = 3 beta/2:
  |mu^xi(h_x) - mu(h_x)| <= 2 G_xy <= 2 q^d/(1-q); covariance |mu(h_x.M h_y) - ...| <= 2 G_xy;
  sign symmetry h -> -h gives mu(h_x) = 0 (READ :213-248; check :105-135 HOLDS).
  Inputs: Lemma INF (12) C_zw <= beta/4 per neighbour, row sum 6 beta/4; Lemma DC.
- Lemma R: |E[W_l | H]| <= prod_k sup_{O in O(4)} |E_{mu_k}[q_{x,k} . O q_{y,k}]| (READ :332-356;
  check :173-192 HOLDS).
- Theorem A: tori with sides >= 3, 0 <= beta_W < 2/3, q = 3 beta_W/2, R <= L_mu/2, T <= L_nu/2:
  |<W_l>| <= (2/(1-q))^min(R,T) q^(RT) (READ :311-330; check :194-209 HOLDS AFTER CORRECTION of the
  beta = 0 log rewriting only). Corollary A3: free boxes, every boundary condition, every Gibbs state
  (READ :403-433; check :244-282 HOLDS).
- Remark A4: weighted rate log(2(1-beta_W)/beta_W) on tori (READ :437-448; check :284-305).
- Ceiling remark: flat background slab = 3D O(4) model; ordering would obstruct the uniform slab
  hypothesis; about 0.94 is a recalled numerical guide (check :376-386, corrected wording).
  The check notes: "The row-sum sufficient test ceases to contract at 2/3; this does not rule out
  stronger comparison arguments" (READ check :385-386).

Key structural point for this row. The whole route needs, per slab k, a bound on
  N_k := sup_{O in O(4)} |E_{mu_k}[h_x . O h_y]|
that decays exponentially in d(x,y), uniformly over all backgrounds O_b. Lemma R needs nothing else.
Lemma R does NOT need a covariance of matrix entries; it needs exactly the "mean matrix"
M_xy := E[h_x h_y^T] (a 4x4 matrix) to have operator norm decaying, since
sup_O |E[h_x . O h_y]| = sup_O |tr(O^T M_xy)| = nuclear norm ||M_xy||_1 (sum of singular values).
(PROVED: sup over O(4) of tr(O^T M) is the sum of singular values, von Neumann trace inequality.)
So the slab target is: ||E_{mu_k}[h_x h_y^T]||_nuclear <= C r^{d(x,y)}, r < 1, uniformly in backgrounds.

### Step 2a (done). Row 839 Proposition TB2, as read

Source: D/library/gap-compress-opus.md (row 839, Claude Opus 5.5; its check gap-compress-check-astra.md
appeared during this run), lines 199-207, 220.
- TB2 (READ :199-205): at the flat background the layer is the 3D O(4) model at beta_W. By the
  Frohlich-Simon-Spencer infrared bound (recalled there), on cubes b^3 the twist deficit
  1 - Z_anti/Z_per >= m^4/32 (1 - o(1)), m^2 = 1 - 4 G_3/beta_W, G_3 = 0.252731 (Watson's integral,
  quadrature; a GUIDE number there). So (AS-bg) is false for beta_1 > 4 G_3 = 1.0109 (READ :207).
- Covariance form (READ :220, marked ARGUED there): long-range order at the flat background excludes a
  background-uniform exponential covariance bound above 1.0109.
- Bearing on this row (ARGUED here; made precise in Step 6): every route that bounds
  N_k = sup_O |E_{mu_k}[h_x . O h_y]| uniformly over backgrounds must include the flat background
  on large periodic slabs, where the infrared bound gives long-range order of the 3D O(4) model for
  beta_W > 4 G_3. So 4 G_3 (about 1.0109) is a proved ceiling (given FSS) for the uniform route; the
  check of row 839 (D/library/gap-compress-check-astra.md:67-104, Codex) rules TB2 HOLDS AFTER CORRECTION
  (positive part; exact threshold 4 G_3, decimals approximate). The believed ceiling is
  the 3D O(4) critical coupling, about 0.936 (GUIDE). The mean-field value of the flat slab is
  N/(2d) = 4/6 = 2/3, exactly the Dobrushin threshold of row 825.

### Step 2b (done). Single-site inputs, as read (D/library/gap-vmf-lip.md, Codex gpt-6-astra, row 785;
checked by Claude Opus 5.5, row 790)

- Theorem V (READ gap-vmf-lip.md:59-77): for mu_F prop. to exp(F.h) sigma(dh) on S^3, every unit e and
  every chord-1-Lipschitz phi: |Cov_{mu_F}(phi, h.e)| <= a(|F|) <= 1/4, a(k) = z'(k)/(k z(k)),
  z(k) = int exp(k h_1) dsigma = 2 I_1(k)/k. The sup over e, phi equals a(|F|). Also E_F h = a(|F|) F
  (READ :96-99, identity (1)). Note: the second argument is LINEAR (h.e).
- Corollary V1 (READ :209-220): d_Lip(mu_F, mu_F') <= |F - F'|/4; more precisely
  <= int_0^1 a(|F + t(F'-F)|) dt |F - F'| (same proof).
- Lemma DC (READ :222-313): for ANY measurable kernels gamma_i (depending on w off i) with
  d_Lip(gamma_i(.|w), gamma_i(.|w')) <= C_ij |w_j - w'_j|, row sums <= alpha < 1, which are versions of
  mu's conditional laws at every site, and mu~ with the same kernels off D:
  |mu~(f) - mu(f)| <= 2 sum_i delta_i(f) sum_{j in D} (sum_n C^n)_ij. The kernels need not be
  single-bond vMF laws: any conditional-law family of mu on a product of copies of S^3 qualifies.
- Lemma INF (12) (READ :315-338): layer model, C_xy <= beta/4 for neighbours, alpha <= 3 beta/2.

### Step 2c (done). Row 818 and the D1 / Route C inputs, as read

- Row 818 (D/library/gap-mixed-opus.md, Claude Opus 5.5; check gap-mixed-check-astra.md): forest
  gauge fixing removes redundant LINK variables of the 4D measure, so a non-forest link has fewer
  moving plaquette neighbours (18 -> 16 or 12) (READ gap-mixed-opus.md:15-40). Lemma W, weighted chord
  Dobrushin: sum_j C_ij w_j <= alpha w_i suffices; the best alpha over w is the Perron root of C
  (READ :42-58). Ceiling of the single-link method: the worst-exterior chord coefficient beta/4 is
  attained (zero conditional field), so no weights beat the Perron root of the count matrix
  (READ :146-152). Block conditioning: "A block route therefore needs a block influence estimate
  (Dobrushin-Shlosman type) proved by hand ... Neither is supplied here." (READ :213).
- Lemma D1 (D/library/gap-shape-exercise-astra.md:249-339, Codex gpt-6-astra; check
  gap-shape-check-opus.md:9-25, HOLDS): for every field h, the vMF law on S^3 has Poincare constant
  1/3: 3 Var_h(f) <= int |grad f|^2 d nu_h, sharp at h = 0.
- Route C (gap-shape-exercise-astra.md:475-605; check :33-110 HOLDS): a 4D gauge-constraint reserve
  for the invariant Langevin gap (endpoint 11/48). It concerns the 4D link measure, not the slab law.
  It does not enter the slab estimate below.

### Step 3 (done). What symmetry the slab law has; why single-site methods stop at 2/3; the decimated chart

Notation. mu_O is the layer law on the horizontal 3-torus Lambda' (sides >= 3) with background
O = (O_b), |J_b| = 1, coupling beta. A = adjacency matrix of Lambda' (6-regular).

**3.1 Covariance, not symmetry (PROVED).** For g = (g_z) in O(4)^Lambda', the map h_z -> g_z h_z sends
mu_O to mu_{O^g}, O^g_b = g_x O_b g_y^T for b = (x, y). Proof: sigma is O(4)-invariant and
h_x . O_b h_y = (g_x h_x) . (g_x O_b g_y^T)(g_y h_y). So the local rotations relabel the background;
they are not symmetries of one slab law. The symmetry group of mu_O is the stabilizer
{g : g_x O_b g_y^T = O_b for all b}; it always contains the global sign g = -I, and for the flat
background it is the global O(4). For the Lemma S backgrounds O_b = L_a R_conj(a'), every element of
SO(4) occurs on every bond (x -> a x b covers SO(4)), and the gauge-invariant content of a background is
its cycle holonomies, i.e. the spatial plaquettes of the two faces (left and right factors).
Consequence (PROVED): the conditional law of g_x h_x under mu_{O^g} is the g_x-rotation of that of h_x
under mu_O, and chord distances are rotation invariant, so every chord coefficient C_xy, every row sum
and every number in Lemma SC is the same for mu_O and mu_{O^g}. "Gauge fixing inside the slab"
(O_b = I on a spanning tree) changes nothing: the slab variables have no local redundancy, so no
neighbour stops moving. This differs from row 818, where forest fixing removes redundant LINK variables
of the 4D measure (READ gap-mixed-opus.md:15-40).
**3.2 4D gauge fixing of vertical edges (ARGUED).** Fixing q_{z,k} = 1 for z in a set S (temporal gauge
on S) makes those sites deterministic. They act as external fields on their neighbours, the sign
symmetry of slab k is lost, and Lemma R's factor picks up the disconnected term E[q_x] E[q_y]^T, which
need not decay in R. So this use of the 4D gauge freedom loses the area law in Lemma R's product.
**3.3 Exactness of the single-site price (PROVED, given Theorem V).** For every background and every
neighbour pair, the optimal worst-exterior chord coefficient
C*_xy = sup { d_Lip(gamma_x(.|w), gamma_x(.|w')) / |w_y - w'_y| : w = w' off y } equals beta/4.
Proof. Upper bound: Corollary V1. Lower bound: the five other neighbours of x can be set so that their
rotated spins sum to -O_xy w_y (five unit vectors reach every vector of norm <= 5); then F_x(w) = 0.
Rotate w_y by a small angle to w'_y; then F' := F_x(w') = beta O_xy (w'_y - w_y). With the test function
h . F'/|F'| (chord-1-Lipschitz) and E_F h = a(|F|) F (READ gap-vmf-lip.md:96-99),
d_Lip >= a(|F'|) |F'| = beta a(beta |w'_y - w_y|) |w'_y - w_y|, and the ratio tends to beta a(0) = beta/4.
So C* = (beta/4) A exactly. Its Perron root is 6 beta/4 = 3 beta/2. By the Collatz-Wielandt bound,
max_i sum_j C*_ij w_j / w_i >= 3 beta/2 for every positive weight vector w. Hence:
(i) no weighted single-site chord-Dobrushin condition (Lemma W of row 818) holds at beta >= 2/3, for any
background; (ii) the field-dependent constant a(|F|) cannot help a worst-exterior argument, because
|F_x| = 0 is attainable at every site. This is the slab analogue of row 818's link ceiling
(READ gap-mixed-opus.md:146-148). Beating 2/3 needs a multi-site (block) influence estimate.
**3.4 The exact target (PROVED).** In Lemma R, ||E_{mu_k}[T_k]||_op = sup over SO(4) of
|E[q_x . O q_y]| <= sup over O(4) = nuclear norm of the 4x4 matrix E[q_x q_y^T] (von Neumann). So the
slab route needs exactly: the matrix two-point function E[h_x h_y^T] of the slab law decays
exponentially in d(x, y), uniformly in the background.
**3.5 The decimated chart (PROVED).** Let the slab be bipartite: a 3-torus with all sides even (>= 4), or
a free cube (Corollary A3). Colour sites even (E) and odd (D). Given h_D, the even spins are
independent with laws mu_{F_x}, F_x = beta sum_{z ~ x} J O_xz h_z. Integrating them out, the odd marginal
mu_D has density prop. to prod_{x in E} z(|F_x(h_D)|) (times fixed boundary factors) w.r.t. sigma^D,
continuous and positive. Its one-site conditional law at z in D is
    nu_z(dh) prop. to exp(F0_z . h) prod_{x ~ z} z(|beta O_xz h + G_x|) sigma(dh),
    G_x = beta sum_{z' ~ x, z' != z} J O_xz' h_z' (+ fixed external terms at boundary sites),
with F0_z a fixed external field (zero on the torus). nu_z depends on h_z' (z' in D) only through the
G_x with x in N(z) cap N(z'), so only for z' at graph distance 2. Write n_zz' = |N(z) cap N(z')|; then
sum_{z'} n_zz' <= 6 * 5 = 30: the six "backtracking" two-step paths z -> x -> z are absent because nu_z
is a conditional law given h_{D minus z}. Lemma DC (READ gap-vmf-lip.md:222-313) applies to mu_D with
the kernels nu_z. Reduction: since |beta O_xz h + G_x| = |beta h + O_xz^T G_x|, we may take O_xz = I.
Define the decimated price
    c(beta) := sup over F0 in R^4, n <= 6, G_1..G_n in R^4, unit Delta, chord-1-Lip psi of
               |d/dt nu^{G_1 + t Delta}(psi)| = |Cov_nu(psi, Delta . m(beta h + G_1))|,
    m(F) := a(|F|) F = E_{mu_F} h (vMF mean), nu prop. to exp(F0.h) prod_i z(|beta h + G_i|).
Then C^D_zz' <= beta c(beta) n_zz' and the decimated row sum is alpha_D <= 30 beta c(beta).

### Step 4 (part a, done). The decimated price c(beta): exact value at zero field, factorization, and the
Dobrushin-inside-the-star bound (which gives back exactly 2/3)

Notation. t(beta) := beta a(beta) = I_2(beta)/I_1(beta) (the one-bond correlation; E_F h = a(|F|)F).
tau(rho) := sup { |Cov_rho(psi, e.h)| : psi chord-1-Lip, |e| = 1 } for a law rho on S^3 (Theorem V:
tau(mu_F) = a(|F|) <= 1/4). S_n := laws prop. to exp(F.h) prod_{i=1}^n z(|beta h + G_i|) sigma(dh).

**4.1 Zero-field value and the ceiling of the decimated method (PROVED).** At F0 = 0, G_i = 0 the law nu
is sigma (z(|beta h|) = z(beta) is constant) and m(beta h) = t(beta) h. With psi = Delta.h,
Cov_sigma(psi, t(beta) Delta.h) = t(beta)/4. So c(beta) >= t(beta)/4, and the bound
alpha_D <= 30 beta c(beta) can certify alpha_D < 1 only if 30 beta t(beta) < 4, i.e. beta < beta_D.
Hand series (t = I_2/I_1 with I_nu(x) = sum (x/2)^(2k+nu)/(k!(k+nu)!)): 30 beta t(beta)/4 = 0.9988 at
beta = 0.738 and 1.0041 at beta = 0.740, so beta_D = 0.7385 to 3 digits (arithmetic GUIDE-checked).
With t(beta) replaced by its bound beta/4 the root is 4/sqrt(30) = 0.7303.
(ARGUED) For the flat background the true optimal decimated coefficients reach beta t(beta) n_zz'/4 at
an environment with all G_x = 0 (x ~ z); such environments should exist (18 free odd spins, six
vector constraints). So beta_D is the ceiling of decimation with worst-environment kernels.

**4.2 Lemma F (factorization; PROVED).** Let nu be as in 3.5 with leaves 1..n and let G_1 -> G'_1. Then
  d_Lip(nu, nu') <= beta * sup_{F in F0 + beta B} tau(lambda_F) * sup_{0<=t<=1} tau(pi^(t)) * |G_1 - G'_1|,
with B the closed unit ball of R^4, lambda_F prop. to exp(F.h) prod_{i>=2} z(|beta h + G_i|) sigma (a law
in S_{n-1}), pi^(t)(dy) prop. to exp(G_1^(t).y) Zhat(beta y) sigma(dy), G_1^(t) = G_1 + t(G'_1 - G_1),
Zhat(v) = int exp(v.h) lambda_{F0}(dh).
Proof. The star law P(dh, dy_1..dy_n) prop. to exp(F0.h + sum_i (beta h + G_i).y_i) has h-marginal nu.
Integrate y_2..y_n: Q(dh, dy_1) prop. to exp(beta h.y_1 + G_1.y_1) lambda_{F0}(dh) sigma(dy_1). Given y_1,
h has law lambda_{F0 + beta y_1}, which does not involve G_1; y_1 has law pi. So nu = int lambda_{F0+beta y}
pi(dy) and nu' = int lambda_{F0+beta y} pi'(dy). For chord-1-Lip psi, y -> lambda_{F0+beta y}(psi) has chord
Lipschitz constant <= beta sup_{F in F0+beta B} tau(lambda_F): along y_t = y + t(y'-y) (inside B),
d/dt lambda_{F0+beta y_t}(psi) = beta Cov(psi, (y'-y).h). Hence |nu(psi) - nu'(psi)| <= (that constant)
d_Lip(pi, pi'), and d_Lip(pi, pi') <= sup_t tau(pi^(t)) |G_1 - G'_1| by the same derivative. QED.
At zero field Lemma F gives c <= beta/16 (it loses the factor 4 a(beta), 0.96 at beta = 0.7).

**4.3 Dobrushin inside the star returns exactly 2/3 (PROVED).** Bound the two tau's by the Dobrushin
comparison theorem inside the star (sites z, y_1..y_n; coefficients beta/4 on the n edges; kernel
discrepancy 1/4 per unit field at the perturbed site; Wasserstein form of the comparison theorem):
with c0 = beta/4, G = (I - C)^(-1) gives G_zz = 1/(1 - n c0^2) and G_{y1 y1} = 1 + c0^2/(1 - n c0^2). So
tau(lambda_F) <= (1/4)/(1 - 5 c0^2) (five leaves) and tau(pi) <= (1/4)(1 - 5 c0^2)/(1 - 6 c0^2) (six).
The product is (1/16)/(1 - 6 c0^2), so alpha_D <= (30 beta^2/16)/(1 - 6 beta^2/16) < 1 iff
36 beta^2/16 < 1 iff beta < 2/3. The decimation is a correct chart, but every bound assembled from
single-site Dobrushin steps returns the mean-field value. The six removed backtracking paths come
back as the loops z -> y_i -> z inside the star. A gain needs a single-site estimate sharper than
Dobrushin for the two tilted classes of Lemma F.

**4.4 The exact sufficient single-site statement (SE).** Let tau_* bound tau on
 (C5) lambda in S_5 (vMF tilted by at most five messages z(|beta h + G_i|), any G_i, any F), and
 (C1') pi prop. to exp(G.y) int exp(beta y.h) lambda(dh) sigma(dy), lambda in S_5 (vMF tilted by one
       Laplace-transform message of an S_5 law).
Then alpha_D <= 30 beta^2 tau_*^2 and the decimated slab has background-uniform decay for
beta < 1/(tau_* sqrt 30). tau_* = 1/4 gives 4/sqrt(30) = 0.7303; tau_* < sqrt(16/30)/(2/3)/4 = 0.2739
is what beats 2/3. Both classes contain the vMF laws (tau <= 1/4) and are exactly tau = 1/4 at zero field.

### Step 5 (in progress). Toward (SE): a perturbation lemma around Theorem V

**Lemma P2 (PROVED, from Theorem V and Lemma D1).** Let mu = mu_Ft (a vMF law) and lambda = w mu with
w = e^R / mu(e^R), R bounded. For chord-1-Lip psi and phi = e.h (|e| = 1), with psi^ = psi - mu(psi),
phi^ = phi - mu(phi), u = w - 1:
  Cov_lambda(psi, phi) = Cov_mu(psi, phi) + E_mu[u psi^ phi^] - (lambda psi - mu psi)(lambda phi - mu phi).
Proof: Cov_lambda(psi, phi) = E_mu[w (psi - lambda psi)(phi - lambda phi)]; expand psi - lambda psi =
psi^ - (lambda psi - mu psi) and the same for phi; use E_mu[w psi^] = lambda psi - mu psi,
E_mu[w phi^] = lambda phi - mu phi, E_mu[w] = 1. QED.
Bounds: |Cov_mu(psi, phi)| <= a(|Ft|) (Theorem V). E_mu[u psi^ phi^] = Cov_mu(psi, u phi^), and by D1
(Var_mu psi <= (1/3) mu|grad psi|^2 <= 1/3) it is at most ||u phi^||_{L2(mu)}/sqrt 3. Also
|lambda f - mu f| <= ||u||_{L2(mu)} sqrt(Var_mu f) <= ||u||_{L2(mu)}/sqrt 3 for chord-1-Lip f. Hence
  tau(lambda) <= a(|Ft|) + ||u phi^||_{L2(mu)}/sqrt 3 + ||u||^2_{L2(mu)}/3,              (P2)
for the best e. With ||u||_inf <= e^omega - 1, omega = osc(R), and ||phi^||_{L2(mu)} <= sqrt(a) <= 1/2:
  tau(lambda) <= 1/4 + (e^omega - 1)/(2 sqrt 3) + (e^omega - 1)^2/3.
**What (P2) needs for the star classes (ARGUED, numbers GUIDE-level hand estimates).** Each message
log z(|beta h + G|) is a function phi_G(s) of s = h.G/|G|, increasing and concave:
phi'' = -(beta g/r)^2 D(r), D(r) = A(r)/r - A'(r) >= 0, A = I_2/I_1, r^2 = beta^2 + g^2 + 2 beta g s
(A concave on [0, inf) gives D >= 0; A' = 1 - A^2 - 3A/r). Hand values at beta = 0.68, g <= 5 beta:
sup |phi''| is about 0.053, reached at s = -1, g = 5 beta. Linearizing each message leaves a remainder
of oscillation about kappa/2 per message, so omega up to about 0.13 for five aligned messages. The sup
form of (P2) then gives tau <= 0.25 + 0.04 + ..., too weak (beating 2/3 needs tau_* < 0.2739 jointly
for both classes, and 0.2685 at beta = 0.68). The L2 form of (P2) with the quadratic model of the
remainder gives about 0.25 + 0.015 at beta = 0.68 (uniform-law moments E s^4 = 1/8, E s^6 = 5/64,
E s^8 = 7/128 on S^3). The margin is thin and the hand control of A, A', D and of the non-uniform
reference law is not done. Status: OPEN as a proof; see GUIDE numerics below.

**GUIDE run 1** (script .../scratchpad/lane834/guide/star2.py, log star2_b070.log; quadrature on S^3,
20 x 28 x 28 nodes; Powell local search, 3 restarts; about 90 s, under 100 MB). beta = 0.7:
t(beta)/4 = 0.04288 (= linear-test value at zero field, as 4.1 says), beta/16 = 0.04375.
- Linear-test proxy L(G) = sup_{e,Delta} Cov_nu(e.h, Delta.m(beta h + G_1)) (a lower bound for c(G)):
  decreases when the perturbed leaf's own field grows (0.0303 at |G_1| = 5 beta); increases slightly
  when other leaves sit in opposite pairs (max 0.04318 found in scans); local search max 0.04323,
  i.e. 0.8 % above t/4 and below beta/16. So 30 beta c is about 0.91 at beta = 0.7 (if linear test
  functions are near optimal, as Theorem V says they are for vMF laws).
- tau proxy (top eigenvalue of Cov_lambda(h)) on S_5: exceeds 1/4 slightly when messages come in
  opposite pairs (equatorial push): 0.25174 at |G| = 5 beta; local search max 0.25206.
  So tau = 1/4 is FALSE on S_5, but the excess found is under 1 %.
Reading (GUIDE): if c(beta) <= 1.01 t(beta)/4 held, the decimated route would reach about 0.735; with
tau_* = 0.2521 in 4.4, 1/(tau_* sqrt 30) = 0.724.

**5.2 A cheaper variant: leaves first (PROVED reduction).** In the star, sample the leaves first:
nu = int mu_{F0 + beta S} dP_L, S = y_1 + ... + y_n, where P_L (the leaves' law) has one-site kernels
rho_j prop. to exp(G_j.y) z(|K_j + beta y|) sigma(dy), K_j = F0 + beta sum_{i != j} y_i: one-message laws
(class S_1). Factor rho_j through the dimer (h, y_j): d_Lip(rho_K, rho_K') <= (beta/4) tau(S_1) |K - K'|.
So inside P_L the coefficients are C^L_ji <= beta^2 tau_1/4 (tau_1 a bound for tau on S_1), the column
sums are <= (n-1) beta^2 tau_1/4, the injected discrepancy at y_1 is <= tau_1 |dG_1|, and
f(y) = mu_{F0+beta S}(psi) has delta_j(f) <= beta/4 (V1). The Wasserstein form of Dobrushin's comparison
theorem (|mu(f) - mu~(f)| <= sum_ij delta_i(f) G_ij b_j; same proof as Lemma DC, with (11) replaced by
|mu~(Gamma~_i g - Gamma_i g)| <= delta_i(g) b_i) gives
    c <= (beta/4) tau_1 / (1 - 5 beta^2 tau_1/4),   alpha_D <= (30 beta^2 tau_1/4)/(1 - 5 beta^2 tau_1/4),
so alpha_D < 1 iff 35 beta^2 tau_1/4 < 1. With tau_1 = 1/4 this is beta < 4/sqrt(35) = 0.6761.
Only one backtracking loop per star (y_1 -> z -> y_1) is now computed exactly: 35 paths instead of 36.
It beats 2/3 iff tau_1 < 36/140 = 0.25714. (P2) with the crude curvature bound sup|phi''| <= 0.053 gives
tau_1 <= 0.2580 (fails by 0.0009); a curvature profile bound (phi'' is largest at s = -1 and about 0.03
at s = +1) would give about 0.2561 (passes), but that needs hand bounds on A = I_2/I_1 on [0, 6 beta]
(for instance from the Riccati equation A' = 1 - A^2 - 3A/r by comparison), not done here. OPEN.

**GUIDE run 2** (star3.py, log star3.log; same quadrature; about 2 min). Max tau proxy on S_1 (one
message, free linear field): 0.25040 at beta = 0.676, 0.25049 at beta = 0.735 (so tau_1 is far below the
36/140 = 0.25714 the leaves-first variant needs; the gap to a proof is the hand control of A = I_2/I_1).
Decimated linear proxy, n = 6, F0 = 0: max L = 1.0039 t/4 at beta = 0.676 (30 beta L = 0.844) and
1.0053 t/4 at beta = 0.735 (30 beta L = 0.996). So the decimated route numerically reaches about 0.736,
just under beta_D = 0.7385 (GUIDE; linear test functions only).

**5.3 Verdict on Step 5.** No rigorous single-site bound sharper than Dobrushin was obtained for the
classes S_5, (C1') or S_1. (P2) is PROVED but its sup form is too weak, and its L2 form needs hand
bounds on Bessel ratios over [0, 6 beta] that are not written. The best PROVED range therefore stays
beta_W < 2/3 (row 825). The reductions (3.5, Lemma F, 5.2) are PROVED and turn any proof of (SE) into an
explicit area law (Step 7).

### Step 6 (done). The ferromagnetic comparison, why frustration blocks it, and TB2

**6.1 The flat slab is a ferromagnet at its mean-field point (PROVED arithmetic).** With all horizontal
edges equal to 1, Lemma S gives O_b = I: the 3D O(4) model with weight exp(beta_W sum h_x.h_y). Its
mean-field value is N/(2d) = 4/6 = 2/3, the Dobrushin threshold of Theorem A. Both come from the same
zero-field response 1/N = 1/4 per neighbour times 2d = 6 neighbours. Row 819 records the ferromagnetic
mean-field range 2/3 as Aizenman-Simon's (READ gap-novelty-opus.md:163, and D/library/gap-crux-fp.md:415, which already notes that their inequalities need ferromagnetic couplings; that paper was not read
there or here).
**6.2 What ferromagnetic tools give beyond it (GUIDE; recalled, not read).** For ferromagnets a
Simon-Lieb type inequality <s_0^1 s_x^1> <= sum_{u in B, v not in B, u~v} beta <s_0^1 s_u^1>_B <s_v^1 s_x^1>
(Simon 1980, Lieb 1980; Aizenman-Simon 1980 by local Ward identities for rotators; its validity for O(4)
is not checked here) gives decay when beta sum_{boundary bonds} <s_0^1 s_u^1>_B < 1. B = {0} gives 6 beta/4,
the mean field. B = the star of 0 (a tree with free boundary, so <s_0^1 s_u^1>_B = t(beta)/4 exactly) has
30 boundary bonds and gives 30 beta t(beta)/4 < 1: beta < 0.7385. This is exactly beta_D of 4.1 (ARGUED:
both are "exact star, worst case outside"). Larger B approach the 3D O(4) critical coupling, about 0.936.
So (SE) is a frustration-blind replacement for the star step of Simon-Lieb: if (SE) holds, the slab
reaches background-uniformly what the star inequality gives the ferromagnet.
**6.3 Why frustration blocks the ferromagnetic route (PROVED, plus ARGUED).** A background O is
gauge-equivalent (3.1) to the flat one iff every cycle holonomy is I: fix g on a spanning tree so that
O^g = I there; each non-tree bond then carries its fundamental-cycle holonomy (PROVED). The Lemma S
backgrounds include every assignment of SO(4) holonomies (the spatial plaquettes of the two faces), so
the uniform route must cover frustrated backgrounds. The Griffiths-Ginibre inequalities behind
Simon-Lieb need nonnegative couplings in one common frame; for a background with nontrivial holonomy no
frame makes all couplings ferromagnetic, and <h_x . O h_y> has no sign (ARGUED). What would transfer the
ferromagnetic gain is a nonlinear diamagnetic inequality, sup_O ||E_O[h_x h_y^T]|| <= C E_flat[h_x . h_y]
for O(4) spins in SO(4) backgrounds. For Gaussian fields the analogue is Kato's inequality (GUIDE,
recalled). For O(4) spins it is OPEN.
**6.4 TB2 and the ceiling of every background-uniform slab route (PROVED given the
Frohlich-Simon-Spencer infrared bound, recalled in row 839 and read in its check).** Lemma R needs a bound on
N_k = sup_O |E_{mu_k}[q_x . O q_y]| for EVERY value of the horizontal edges, so for the flat slab on
large periodic 3-tori. There, translation invariance gives
(1/|Lambda'|) sum_x E[h_0 . h_x] = |Lambda'|^(-2) E|sum_x h_x|^2 >= m_Lambda^2 = 1 - (4/beta_W) G_Lambda
(READ gap-compress-opus.md:201-205, the same infrared step). Since E[h_0 . h_x] <= N(0, x), a bound
N(0, x) <= C r^d(0,x) with C, r < 1 independent of the slab would make the left side O(1/|Lambda'|).
So no background-uniform exponential bound holds for beta_W > 4 G_3 (about 1.01092; Watson's integral).
The check of row 839 reads the FSS component bound E|s-hat^a(p)|^2 <= |Lambda|/(beta E(p)) in the primary
source (FSS 1976, Section 2, Theorems 2.2-2.3) and confirms the step E|M_tot|^2 >= V^2 (1 - N G_Lambda/beta)
(READ gap-compress-check-astra.md:79, 83); it rules that the exact threshold is 4 G_3, with decimals only
approximate (READ :100). This is the covariance form that row 839 marks ARGUED
(READ :220); the direct infrared argument above closes it, given FSS. Believed ceiling: the 3D O(4)
critical coupling, about 0.936 (GUIDE). Between the routes: Dobrushin 2/3 (PROVED barrier, 3.3);
decimation with worst-environment kernels beta_D = 0.7385 (PROVED barrier of the bound, 4.1); every
uniform slab route 4 G_3, about 1.0109 (PROVED given FSS); believed 0.936.

### Step 7 (done). Statements

**Best PROVED range: unchanged.** Theorem A of row 825 (READ gap-arealaw-opus.md:311-330, check HOLDS
AFTER CORRECTION): on every periodic 4D torus with sides >= 3, in free boxes and in every Gibbs state,
for 0 <= beta_W < 2/3, q = 3 beta_W/2, every R x T rectangle (sides at most half the torus sides) obeys
|<W_l>| <= (2/(1 - q))^min(R,T) q^(RT). This row proves no larger range.

**Proposition B (barriers; PROVED, (iv) given FSS).** Weight exp(beta_W Re U_p), slab coupling beta = beta_W.
(i) For every background, the optimal worst-exterior chord coefficients of the slab law are exactly
    (beta/4) A; no weighted single-site chord-Dobrushin certificate exists for beta_W >= 2/3 (3.3).
    Local rotations inside the slab only relabel the background and change no coefficient (3.1).
(ii) In the decimated chart (3.5), bounding the star laws by Dobrushin's comparison inside the star
    gives alpha_D <= (30 beta^2/16)/(1 - 6 beta^2/16), which is < 1 iff beta_W < 2/3 (4.3).
(iii) With worst-environment decimated kernels, c(beta) >= t(beta)/4, so the decimated bound cannot
    certify beta_W >= beta_D, 30 beta_D t(beta_D) = 4, beta_D = 0.7385 (4.1).
(iv) No background-uniform exponential bound on E_{mu_k}[q_x q_y^T] holds for beta_W > 4 G_3, about 1.0109 (6.4).

**Theorem A2 (area law beyond 2/3, CONDITIONAL; the implication is PROVED, its hypothesis is OPEN).**
Hypothesis (SE_tau*): with beta = beta_W, every law in class (C5) and every law in class (C1') of 4.4
has tau <= tau_*. Put q_D = 30 beta_W^2 tau_*^2 and assume q_D < 1. Let Lambda = prod Z/L_mu Z with every
L_mu even and >= 4. Let l be an R x T rectangle in the plane (mu, nu), R <= L_mu/2, T <= L_nu/2. Then
    |<W_l>| <= (C_D q_D^((R-1)/2))^T   and   |<W_l>| <= (C_D q_D^((T-1)/2))^R,   C_D = 48/(1 - q_D),
hence |<W_l>| <= (C_D q_D^(-1/2))^min(R,T) q_D^(RT/2): string tension at least (1/2) log(1/q_D).
Proof. Lemmas S and R of row 825 reduce to N_k = sup_O |E_{mu_k}[q_x . O q_y]| with d(x, y) = R in the
horizontal 3-torus, which is bipartite (even sides). Decimate the colour class D of x (3.5). Lemma F and
(SE_tau*) give c(beta) <= beta tau_*^2, so the decimated row sums are alpha_D <= 30 beta c <= q_D < 1.
Decimated influences join only sites at distance 2, so (C^D)^n_xy = 0 for 2n < d and
G^D_xy <= q_D^ceil(d/2)/(1 - q_D). mu_D is invariant under h -> -h (z(|F|) is even). R even: the pinning
argument of Lemma SC (a)-(b) applied to mu_D gives N_k <= 2 q_D^(R/2)/(1 - q_D). R odd: y is integrated,
E[q_x . O q_y] = E[q_x . O m(F_y)], m(F_y) a function of the six D-neighbours j of y, |m| <= 1, mean zero;
write q_x . O m = sum_a (q_x)_a (O m)_a, use Cov(f, g) = Cov(f, g + ||g||) with the comparison measure
(g + ||g||) mu_D (same kernels off N(y)) and Lemma DC; with sup |(O m)_a| <= 1 for each of the four a and d(x, j) >= R - 1 this gives
N_k <= 4 * 2 * 6 q_D^((R-1)/2)/(1 - q_D). Both cases are <= C_D q_D^((R-1)/2). Lemma R multiplies T such
factors; exchange the directions for the second bound. QED.
Free boxes and Gibbs states: the Corollary A3 argument of row 825 carries over if (SE) is stated with
arbitrary fixed external fields, as 4.4 does (ARGUED, not written out).
Numbers: tau_* = 1/4 gives beta_W < 4/sqrt(30) = 0.7303; the GUIDE value tau_* = 0.2521 gives 0.7243.

**Corollary A2' (leaves-first variant, CONDITIONAL; implication PROVED).** If tau <= tau_1 on S_1 (vMF
times one message z(|beta y + K|), any K, any linear field) and q_1 := 35 beta_W^2 tau_1/4 < 1, then
Theorem A2 holds with q_D replaced by (30 beta_W^2 tau_1/4)/(1 - 5 beta_W^2 tau_1/4) < 1 (5.2). tau_1 = 1/4
gives beta_W < 4/sqrt(35) = 0.6761; GUIDE tau_1 = 0.2504 gives 0.6756; beating 2/3 needs tau_1 < 0.25714.

### Step 8 (done). What blocks further progress, what is new, marks

**Blockers, named exactly.**
- (K1) The single-site statement (SE): tau <= tau_* < 0.2739 on (C5) and (C1') (or directly
  30 beta c(beta) < 1). It is what stands between 2/3 and 0.7303. GUIDE: it holds numerically with
  tau_* about 0.2521 and c within 1 % of t(beta)/4 at beta = 0.7. Missing: a sharp "Theorem V for star
  marginals". Theorem V covers vMF laws only; D1 (Poincare 1/3) loses the factor 4/3 against Lipschitz
  test functions; Lemma P2 in sup form loses about a factor 2 in the curvature term; its L2 form needs hand
  bounds on A = I_2/I_1, A' and D = A/r - A' on [0, 6 beta], not written.
- (K2) The cheapest instance: tau < 0.25714 on S_1 (one message) already passes 2/3 (up to 0.6761 at most).
  GUIDE tau_1 = 0.2505; the hand bound from P2 is 0.2580, short by 0.0009.
- (K3) Beyond beta_D = 0.7385 the decimated bound with worst-environment kernels stops (the zero-field
  environment). Larger exactly treated blocks lead to harder single-site classes; the alternative is
  influence bounds averaged over environments, for which no background-uniform tool is in hand.
- (K4) Beyond 4 G_3, about 1.0109 (proved given FSS) and about 0.936 (believed) no background-uniform slab route exists.
  One must average over the face fields under the 4D law (typical frustration). That is not a slab
  statement, and it is the same kind of input as the crux.
- (K5) Frustration: Griffiths-Ginibre inequalities need a ferromagnetic frame, which exists iff all
  holonomies are trivial (6.3). A nonlinear diamagnetic inequality for O(4) spins in SO(4) backgrounds
  would let ferromagnetic tools (Simon-Lieb with larger sets) act uniformly. OPEN.

**What is new against D/library/gap-novelty-opus.md (row 819) and row 825 Section 6.** No new literature
search was made; comparisons are with the sources those notes read. "NEW" means not found there.
- Proved range: 2/3, EQUAL to row 825 (nothing new).
- Proposition B(i), the exact slab single-site barrier (beta/4)A: NEW as a stated lane result for the
  slab. It is the slab analogue of row 818's link ceiling (READ gap-mixed-opus.md:146-148) and of the
  "ceiling of all single-link Dobrushin arguments" that Bhattacharjee-Bhattacharya state for the 4D link
  measure (READ gap-novelty-opus.md:22). It is a short corollary of Theorem V's sharpness.
- 3.1 (local rotations relabel the background; no local redundancy in the slab): elementary, NEW only
  as an explicit lane statement.
- The even/odd decimated chart, Lemma F, and the exact return to 2/3 under Dobrushin inside the stars
  (Proposition B(ii)): NEW in the lane. Sublattice decimation itself is a classical device (GUIDE,
  recalled, no source attributed here).
- Theorem A2 and Corollary A2' (conditional beyond-mean-field slab routes with explicit constants):
  NEW as conditional statements; none of the read sources states a background-uniform slab bound
  beyond the mean-field value (row 819 lists CNS 1/6, Bauerschmidt-Bodineau 1/3 for scalar couplings,
  and the ferromagnetic mean-field range 2/3, READ gap-novelty-opus.md:158-164).
- 6.2: the decimated zero-field threshold equals the star Simon-Lieb threshold of the flat ferromagnet
  (ARGUED; NEW as an observation).
- 6.4: the covariance-form ceiling 4 G_3 (about 1.0109) for every background-uniform slab route, given FSS.
  Row 839 states it as ARGUED (READ gap-compress-opus.md:220); the direct infrared argument here
  completes it. The infrared bound is Frohlich-Simon-Spencer's (not read here; its component form is READ by the row 839
  check, gap-compress-check-astra.md:79).
Credits: Theorem V, Corollary V1, Lemma DC, Lemma INF: Codex gpt-6-astra (row 785), checked by Claude
Opus 5.5 (row 790). Lemma D1: Codex gpt-6-astra, checked by Claude Opus 5.5. Lemmas S, SC, R, Theorem A:
Claude Opus 5.5 (row 825), checked by Codex gpt-6-astra (row 828). Proposition TB2: Claude Opus 5.5
(row 839, unchecked). Slab reduction: Durhuus and Frohlich (1980), as stated by Cao, Nissim and
Sheffield. Comparison method: Dobrushin. Infrared bound: Frohlich, Simon and Spencer (1976). Simon-Lieb
inequality: Simon (1980), Lieb (1980); Aizenman-Simon (1980) for rotators (all recalled, not read).

**Marks.**
| Statement | Mark | Where |
|---|---|---|
| Local rotations map mu_O to mu_{O^g}; all chord coefficients invariant; no in-slab gauge gain | PROVED | 3.1 |
| Fixing vertical edges in 4D gauge loses the area law in Lemma R's product | ARGUED | 3.2 |
| Optimal single-site chord coefficients are exactly (beta/4)A; no weighted certificate at beta >= 2/3 | PROVED (given Theorem V) | 3.3 |
| Lemma R needs exactly the nuclear norm of E[q_x q_y^T] | PROVED | 3.4 |
| Decimated chart (odd marginal, star kernels, 30 two-step paths) | PROVED | 3.5 |
| c(beta) >= t(beta)/4; decimated bound stops at beta_D = 0.7385 | PROVED (digits by hand series) | 4.1 |
| True decimated coefficients reach that value (all-zero-G environments exist) | ARGUED | 4.1 |
| Lemma F (factorization through one leaf) | PROVED | 4.2 |
| Dobrushin inside the stars returns exactly 2/3 | PROVED | 4.3 |
| Lemma P2 (perturbation of Theorem V) | PROVED (given Theorem V, D1) | Step 5 |
| P2 sup form too weak; L2 form needs Bessel-ratio bounds | ARGUED | Step 5, 5.2 |
| Wasserstein form of Dobrushin's comparison theorem | PROVED (Lemma DC's proof) | 5.2 |
| Leaves-first reduction: alpha_D < 1 iff 35 beta^2 tau_1/4 < 1 | PROVED | 5.2 |
| tau on S_5 up to about 0.2521; on S_1 about 0.2504; c within 1 % of t/4; route to about 0.736 | GUIDE | runs 1-2 |
| tau = 1/4 is false on S_5 (equatorial push by opposite messages) | GUIDE (mechanism ARGUED) | run 1 |
| Star Simon-Lieb threshold for the flat ferromagnet = beta_D | GUIDE (inequality recalled) | 6.2 |
| A background is ferromagnetic up to gauge iff its holonomies are trivial | PROVED | 6.3 |
| Nonlinear diamagnetic inequality for O(4) in SO(4) backgrounds | OPEN | 6.3 |
| No background-uniform slab bound above 4 G_3 (about 1.0109) | PROVED given FSS (component bound READ by the row 839 check) | 6.4 |
| Critical coupling of 3D O(4) about 0.936 | GUIDE | 6.4 |
| Theorem A (beta_W < 2/3) | READ (row 825; check HOLDS AFTER CORRECTION) | Step 7 |
| Theorem A2 (implication) / its hypothesis (SE) | PROVED / OPEN | Step 7 |
| Corollary A2' (implication) / tau_1 < 0.25714 | PROVED / OPEN | Step 7 |
| Free boxes and Gibbs states under (SE) | ARGUED | Step 7 |
| Independent reading of this note | OPEN (not done) | - |

Steps that most need an independent reading: the lower bound in 3.3, the kernel identification in 3.5,
Lemma F, the algebra of 4.3, the Wasserstein comparison form in 5.2, the R-odd case of Theorem A2, and 6.4.

## Summary

The best proved range stays beta_W < 2/3 (row 825). This row shows why, and what would move it.
Every single-site method stops exactly at 2/3, because the worst-exterior price beta/4 per neighbour is
attained and the slab has no local redundancy to remove. An exact block chart exists: integrate out one
colour class, so the other class feels star messages. It removes the six backtracking paths per two
steps (30 instead of 36). With Dobrushin inside the stars it returns exactly 2/3. With a sharp
single-site bound (SE) for vMF laws tilted by star messages it gives an explicit area law up to
4/sqrt(30) = 0.7303 (Theorem A2). Numerics (GUIDE) put the true route near 0.72-0.736. The decimated
bound cannot pass 0.7385, the same number the star Simon-Lieb inequality gives the flat ferromagnet, and
no background-uniform slab route passes 4 G_3, about 1.0109 (given FSS). The blocker is (SE), a single-site estimate
on S^3; the deeper blocker beyond 0.7385 is the lack of frustration-blind tools that see more than one
exact star.

RESULT: No range beyond beta_W = 2/3 is proved (row 825's Theorem A stays the best area law); PROVED: the slab law has only global symmetries, so in-slab gauge fixing changes nothing, and its single-site chord coefficients are exactly (beta/4)A, so no weighted single-site Dobrushin argument passes 2/3; the even/odd decimated chart is exact (30 two-step paths instead of 36) but with Dobrushin inside the stars returns exactly 2/3; Theorem A2: if vMF laws tilted by star messages satisfy tau <= tau_* (hypothesis SE, OPEN), then on tori with even sides |<W>| <= (C_D q_D^((R-1)/2))^T with q_D = 30 beta_W^2 tau_*^2, an area law up to 4/sqrt(30) = 0.7303 at tau_* = 1/4 (leaves-first variant up to 4/sqrt(35) = 0.6761, needing only one-message laws with tau < 0.25714); ceilings: 0.7385 for the worst-environment decimated bound (equal to the star Simon-Lieb threshold of the flat ferromagnet) and 4 G_3 (about 1.0109) for every background-uniform slab route (given the Frohlich-Simon-Spencer bound; this completes row 839's ARGUED covariance form); GUIDE numerics support SE (tau <= 0.2521, decimated price within 1 % of its zero-field value, route near 0.72-0.736); the exact blocker is SE, a sharp Theorem-V-type bound for star-marginal laws on S^3, and beyond 0.7385 a frustration-blind replacement for larger Simon-Lieb sets (a nonlinear diamagnetic inequality, OPEN).
