# Check of gap-solve3-astra62.md (FINISH row 1148)

Status: done (Steps 1-8). Verdict table and RESULT line at the end.

Checker: Claude (Opus 5.5), row 1148.
File under check: library/gap-solve3-astra62.md (411 lines).
Builds on: library/gap-solve2-astra62.md (row 1145) and its check library/gap-solve2-check-opus.md.
Setting: library/gap-council-brief.md.

## Plan (at most eight steps)

1. Read the setting (gap-council-brief.md), the cited parts of row 1145 and its check.
2. Read gap-solve3-astra62.md in full; list its numbered statements.
3. Check the open-box gauge estimate (1) and gap (2).
4. Check (4)-(9), the localization to (9).
5. Check the positive restoration (27)-(28), the polymer expansion and resummation of Section 11, and the equivalence (30).
6. Check the periodic-cube gap (13) and its consequence, and the sewing identity (16)-(19).
7. Check the obstructions: (10)-(12), (15), (21), (22)-(24a), (25)-(26), (29), the divergence arguments of Sections 10-11, and Section 13.
8. Verdict table and RESULT line.

## Log

- Step 1 done. Read `library/gap-council-brief.md` (all). Read row 1145,
  `library/gap-solve2-astra62.md`, L1-60 and L198-444: Sections 1, 5, 7-12,
  with (1), (2), (16)-(18), (21), (22), (24), (25), (26). Read its check
  `library/gap-solve2-check-opus.md` L29-333 and L434-690. That check finds
  every statement of row 1145 HOLDS (two citation corrections, 0 FAILS).
  Facts used below from row 1145, each checked there: the one-link bound
  (1) and the inversion bound (2); the charge bounds (16)-(18); the
  variance (21) with 1 - r_beta <= C_1/beta; the thermal seed (22) on the
  strip |z| <= c/(1+beta); the real form (24); the per-block projected
  expansion of Section 11 with ||D_l - 1|| <= eta(l d_beta) (L394); the
  repeated-polymer divergence (26) with z_B.
- Step 2 done. Read `library/gap-solve3-astra62.md` L1-411 in two ranges.

Notation (the file's own). Line numbers "L" are lines of
`library/gap-solve3-astra62.md`. a(u) = 1 - (1/2) tr u = |1-u|^2/2 on unit
quaternions. c_beta = e^(-beta a)/I(beta). r_beta = I_2(beta)/I_1(beta),
d_beta = -log r_beta. "(24)" is row 1145's real form of the seed: its left
side is limsup_j J(beta_j) with J = 2 log Z_T - log Z_2T, T = n/2.

## Step 3. The open-box estimate (1) and the gap (2), L13-53

**(1), L17-21. HOLDS.** Gauge: the 1-lines, the 2-links of the plane
x_1 = r and the 3-links of its line x_2 = 0 form a spanning tree of the open
box (each 1-line meets the plane once; the plane carries a comb). A plaquette
with two tree links fixed to one gives |U_e - U_e'| = |1 - U_p| =
sqrt(2 a(U_p)) for its two parallel links. Chains have length <= 2b. A
1i-plaquette lies in <= b_1 chains; a plane 23-plaquette in <= b_1 b chains
(b_1 values of x_1 times <= b values of x_2 beyond it). Cauchy-Schwarz:
sum_e |1-U_e|^2 <= 2b * 2 * [b_1 A + b_1 b (A/b_1)] <= 8 b^2 A. So C = 8.

**Set-up of (2), L23-36. HOLDS.** c_beta is a probability density, so
convolution has norm one; its multipliers I_d/I_1 are positive. Haar angle
density (2/pi) sin^2 r; 2r^2/pi^2 <= 1 - cos r <= r^2/2 on [0, pi];
c beta^(-3/2) <= I(beta) <= C beta^(-3/2); the ball |1-u| <= c_0/sqrt(beta)
has Haar mass >= c c_0^3 beta^(-3/2). Kernel (3): the kernel of M C P M,
after the change Y' = g^(-1).Y; it is separately gauge invariant in U and Y
because c_beta is a class function. M C P M = (M (CP)^(1/2))(...)^* >= 0
with norm <= 1; it is zero on non-invariant functions; K > 0 pointwise. The
Jentzsch argument for simplicity and strict positivity of psi is standard
and correct; psi = K psi/lambda_0 is continuous and gauge invariant.

**Diagonal and vacuum bounds, L38. HOLDS.** In tree gauge, sup c_beta =
1/I(beta) <= C beta^(3/2) on the d chords and M <= 1; the tree factors
c_beta(g_w g_v^(-1)) integrate to one from the leaves. Lower bound: the trial
set (chords within c_0/sqrt(beta) of one in tree gauge) is invariant under
the residual global conjugation, has mass >= (c_1 beta^(-3/2))^d; on it every
plaquette has a <= 8 c_0^2/beta, so M >= e^(-CE) (there are at most E
plaquettes; the file's 2E is also true); with g_v = g_* h_v each electric
argument is within 4 c_0/sqrt(beta) of one, so each c_beta >= c beta^(3/2).
Rayleigh: lambda_0 >= |S| inf K >= e^(-C_0 E), since E - (V-1) = d.

**Minorization on D x D, L40-46. HOLDS.** For U, Y in D gauge each
by (1): sum_e |1-U_e|^2 <= C b^2 h/s. With the restricted gauges,
|U_e - g_v Y_e g_w^(-1)| <= |U_e - 1| + |Y_e - 1| + 2c_0/sqrt(beta). The sum
of squares is <= C(b^2 h/s + E/beta). L40 calls this "a total electric
action" in the file's convention for A (no coupling factor); the weight
uses beta times it, C(beta b^2 h/s + E), as displayed. The display then
follows with M(U)M(Y) >=
e^(-h). The second inequality uses lambda_0 psi(U) psi(Y) <= (C beta^(3/2))^d
(from lambda_0 psi^2 <= K(U,U), true since K - lambda_0 |psi><psi| >= 0 has a
continuous kernel) and h <= C E. Tail: ||1_(D^c) K|| <= ||1_(D^c) M|| <=
e^(-h/2), so ||1_(D^c) phi|| <= 2 e^(-h/2)/lambda_0 <= 2/8 = 1/4.

**Dirichlet form and (2), L48-53. HOLDS.** The identity
1 - lambda/lambda_0 = (1/(2 lambda_0)) int int K psi psi (f(U)-f(Y))^2
follows from symmetry, K psi = lambda_0 psi and ||phi|| = 1. Keeping D x D
gives epsilon [mu(D) int_D f^2 dmu - (int_D f dmu)^2] >= epsilon
[(15/16)^2 - (1/16)^2] = (7/8) epsilon, using orthogonality for the last
term. Eigenvalues below lambda_0/2 give deficit >= 1/2. So (2) holds, and at
s = beta its right side exp[-CE(1+b^2)] is free of beta.

## Step 4. The localization (4)-(9), L55-106

**(4), L57-64. HOLDS.** The unprojected kernel M C^(tensor E) M is strictly
positive, so its top eigenfunction is simple and positive; a gauge rotation
commutes with the operator and preserves positivity, so the top
eigenfunction is invariant and lambda_0 is the projected one. On the
invariant subspace the unprojected operator equals K, and (2) at s = beta
with E <= 3b^3 gives a deficit >= e^(-C b^5). On a nontrivial isotypic
component the argument of row 1145 (16)-(18) goes through on the box times a
time circle: a temporal link at v lies in deg(v) <= 6 temporal plaquettes of
coupling beta (one per spatial edge at v), so its conditional parameter is
<= 6 beta, and greedy colouring needs <= 7 colours. The character
coefficient gives Tr K_pi^k / Tr(P K^k) <= (prod d_v) e^(-kw/(7 b_beta));
with Tr K_pi^k >= ||K_pi||^k and Tr(P K^k)/lambda_0^k -> 1 at a fixed box,
k-th roots give ||K_pi||/lambda_0 <= e^(-1/(7 b_beta)) <= 1 - c/(1+beta).
Trace: K(U,U) = M(U)^2 I(beta)^(-E) <= (C beta^(3/2))^E, with
lambda_0 >= e^(-C_0 E). Free link: the multipliers are I_d/I_1, so
lambda_0 = 1, second eigenvalue r_beta <= e^(-1/b_beta), trace 1/I(beta).

**(5), L66-71. HOLDS.** With n = qb + r, q = floor(n/b) >= 2b - 1 > r when
b^2 <= n/2, so the remainder can be spread. Per plane type q n^2 <= n^3/b
plaquettes cross in each of its two directions: at most 6n^3/b per slice. A
link joining two boxes lies only in plaquettes of Sigma, so it is free; the
unprojected transfer is the stated tensor product. The product vacuum is
invariant under every vertex rotation, so 1 <= Tr(P G^k)/Lambda^k
<= Tr(G^k)/Lambda^k. Then 0 <= J_cut (sum mu_i^(2T) <= (sum mu_i^T)^2) and
J_cut <= 2 log Tr(G/Lambda)^T <= 2 sum_f (1-delta)^(T-1) Tr(G_f/lambda_f),
over at most n^3/b^3 + 3n^3/b <= C n^3 factors with sides <= b+1. This is (5).

**L73. HOLDS.** With b = floor(gamma (log n)^(1/5)), C(b+1)^5 <= (1/4) log n
for small gamma, and c/(1+beta) >= n^(-1/4) since beta = O(log n). Then
(T-1) delta_(b+1) >= c n^(3/4) beats C(b+1)^3 log(2+beta) + log(C n^3), so
J_cut -> 0. The fraction of Sigma is (6n^3/b)/(3n^3) = 2/b.

**(6), L75-80. HOLDS.** d/du log Z_k = -k|Sigma| (1 - wbar_(k,Sigma)), so
J'(u) = 2T|Sigma| (wbar_T - wbar_2T), and J(beta) - J_cut is the integral.
By (5) and row 1145 (22) both J_cut and J(s_0) are o(1), so (6) and the left
side of (24) are the same limsup.

**(8), L90-95. HOLDS.** Upper kernel bound 1/I(beta)^E <= (C beta^(3/2))^E;
lower bound uses e^(-2 beta) in every c_beta and M(x)M(y) >= e^(-2 beta E)
(A <= 2E). Perron: (l/lambda) int psi <= psi <= (U/lambda) int psi, so sup psi/inf psi <= U/l,
sup psi >= 1, inf psi >= l/U. For r >= 2, G^r(x,y) = lambda^r psi(x)psi(y) +
<G(x,.), R_(r-2) G(.,y)> with ||R_(r-2)|| <= (lambda(1-delta))^(r-2), and each
row has L^2 norm <= U. The relative error is <= U^4 (1-delta)^(r-2)/(lambda^2
l^2) <= exp[C(1+beta)(b+1)^3 - (r-2) delta_(b+1)], using log beta <= beta and
E <= 3(b+1)^3. The free link is the same with lambda = 1, psi = 1.

**Transfer word, L97. HOLDS.** With layer weights M_i^2 split as
M_i C M_(i+1) on each edge, the h-1 edges between the h cut layers carry the
product transfer G; the other edges give a nonnegative rest kernel; one
vertex projection suffices because P commutes with every edge operator.

**(7), L84-88 and L99. HOLDS.** With C(b+1)^5 <= (eta/3) log n,
delta_(b+1) >= n^(-eta/3), so (8) at r = h - 1 ~ n^eta is
exp[-c n^(2eta/3)] = o(n^(-4)). At most 4n^3 factors give
1 - eps_j <= G^r/(Lambda^r Psi Psi) <= 1 + eps_j, eps_j -> 0. Integrating
against the nonnegative rest kernel (projection included) once and twice gives
Z_1 in [1 -/+ eps] c_R and Z_2 in [(1 -/+ eps)^2] c_R^2, so
|J_hole| <= 2 log[(1+eps)/(1-eps)]. The proof uses only R >= 0 and c_R > 0,
so the general-weight version also holds.

**(9), L101-106. HOLDS.** d/du log Z_i = -i|D_j| (1 - w_(i,D)), so
J' = 2|D_j| (w_(1,D) - w_(2,D)), and J(beta) - J_hole is the integral in (9).
With (7) this has the same limsup as (24)'s left side. The strict threshold
is the same. a_j h = L n^(eta-1) -> 0, and the affected fraction of each
layer is <= 2/b.

## Step 5. Positive restoration (27)-(28), Section 11 resummation, (30)

**Parameters of (27), L318-324. HOLDS.** With b = floor(gamma
[log(2+beta)]^(1/5)) one has (b+1)^5 <= 32 gamma^5 log(2+beta) eventually, so
e^(C(b+1)^5) and H are at most a fixed power of 1+beta; h = 1 + mH is
polylogarithmic in n and a_j h -> 0. b -> infinity along the trajectory, so
b >= 2 eventually.

**Reference measure, L326. HOLDS (given (15) on an open box; see Step 6).**
Each spatial link has a unique base vertex; a cell carries its open box and at
most 3(b+1)^2 outgoing crossing links. Box part: the projected kernel keeps
the pointwise bounds l, U of (8) and has deficit >= e^(-C(b+1)^5) by (2) at
s = beta, uniformly in beta. The row argument of (8) then gives relative
error exp[C(1+beta)(b+1)^3 - (l-2) e^(-C(b+1)^5)], which is <= sigma/3 for
l >= H when the constant in H is large. (15) on the box, with at most
(b+1)^3 vertices and l/(7(1+6beta)) >= c(b+1)^3, gives the unprojected kernel
within 1 +/- sigma/3 of the projected one. Note: the unprojected deficit
delta = c/(1+beta) of (4) would need l >= C(1+beta)^2, which H need not
reach for small gamma; the file's route (projected gap (2), then (15)) avoids
this. Links: ||D_l - 1|| <= eta(l d_beta) <= C e^(-cl/(1+beta)), and
(1 + C e^(-cH/(1+beta)))^(3(b+1)^2) - 1 <= sigma since H >= C(1+beta)(b+1)^3.

**Factor expression, L328-333. HOLDS.** A Sigma plaquette based in cell c
crosses in one of its two directions at the top of an interval: at most
2 x 3 x (b+1)^2 = 6(b+1)^2 per cell. Its links have base x, x, x+e_i, x+e_j,
so they lie in c and its positive neighbours; a component is read by at most
four groups. Writing G_c(a,b) = lambda_c psi_c(a) psi_c(b) k_c(a,b), the
mH-step open kernel with the insertions is Lambda^(mH) Psi(x) Psi(y) times
E[prod D_(H,c) prod exp(u sum_(t in block) X_c(U_t))] times
e^(u[X(y)-X(x)]/2), where block endpoints are independent mu_c and bridges
are independent given endpoints. Checked by multiplying the one-step
densities. For |u| <= u_*: |u H X_c| <= 6c, so both factor types are within
sigma of one.

**(28), L335-339. HOLDS.** Dependency: a label in block k reads endpoints at
boundaries k, k+1 and bridges in block k of its components; two labels share
a variable only if they read a common component in equal or adjacent blocks.
So non-adjacent families are independent under the reference. Neighbourhood
4 x 3 x 5 = 60; connected sets of size r through a label <= 60^(2(r-1)); the
Kotecky-Preiss condition sum_(Y not~ X) |z_Y| e^(2|Y|) <= |X| follows from
the choice of sigma, as in row 1145 Section 7 (checked there against the
account's tree theorem). Weighted absolute sum <= (number of labels) <=
C n^3 m. A cluster missing block 1 does not depend on x (block-1 labels are
the only ones reading x), and one missing block m does not depend on y, so
both cancel in the four-term cross ratio; a connected list touching blocks 1
and m has >= m labels. Hence Delta <= 4 C n^3 m e^(-m) -> 0 for
m = ceil(10 log n). The rank-one comparison with v(x) = G(x,z)/sqrt(G(z,z))
gives e^(-Delta) <= G/(v v) <= e^Delta, and the rest-kernel step of (7) gives
|J| <= 4 Delta. So (27) holds uniformly on 0 <= u <= u_*, and (7) at this h is
its case u = 0.

**Section 11, L353-355. HOLDS (with a precision).** A link x -> x+e_i
crosses iff x_i is the top of an interval; intervals have length >= 2, so in
each direction the crossing links form disjoint edges, and the crossing-link
graph is the product of three graphs of isolated vertices and disjoint
edges. Its components are boxes with 1 or 2 vertices per side; their
internal plaquettes are exactly the plaquettes whose four links cross, i.e.
Sigma_2 (both x_i and x_j at interval tops). So turning Sigma_2 on keeps the
tensor product. Precision: for a small box at coupling beta the unprojected
deficit is only c/(1+beta); use, as in L326, the projected deficit from (2)
(an absolute constant for bounded E) with (8), then (15) with at most 8
vertices. This needs block lengths >= C(1+beta), which H, the h of (20) and
the h of Section 3 all exceed. Grouping: each small box has a vertex on the
boundary of its assigned cell and small boxes are vertex-disjoint, so at most
C(b+1)^2 per cell; a Sigma_1 group reads components assigned within coarse
distance two. The neighbourhood constant stays absolute and (28) goes through
with new absolute sigma, c, C.

**(20), L235-243 (used by Section 11). HOLDS.** (b+1)^5 <= 32 gamma^5
log(2+beta) gives a projected box deficit >= (1+beta)^(-1/2) for small gamma.
At r = h - 1, r (1+beta)^(-1/2) >= C_1 (1+beta)^(1/2) log n dominates
C(1+beta)(b+1)^3 + 6 log n because beta = O(log n); the projected error is
o(n^(-5)). (15) on a box: C (b+1)^3 e^(-r/(7(1+6beta))) <= C (b+1)^3
n^(-C_1/42) = o(n^(-5)) for C_1 large; free links likewise. At most 4n^3
factors. The omitted fraction is 2h/(bT) and a_j h -> 0.

**(30), L378-385. HOLDS (the lower limit conditional on the witness).** With
m = floor(n/(H log n)) the bound of (28) is still C n^3 m e^(-m) -> 0, for
every real |u| <= u_* (the factor bound holds for negative u too). J_D(beta)
is the isotropic J. As in (9), J_D(beta) - J_D(u_*) is the integral in (30),
so (30) and (24) state the same strict inequality. The lower limit
log(1 + rho_CA^(L/(3d))) is J(beta) >= log(1+S_ev) from row 865's W-phys-CA
(row 1145 Section 9, checked HOLDS conditional on the witness); with
2t/(3d) = L/(3d) at t = L/2. The statement that deleting Sigma_1 on D_j
changes J by at least that amount follows.

## Step 6. (15), the periodic-cube gap (13), and the sewing identity (16)-(19)

**(15), L181-186. HOLDS.** Checked first, since L243, L326 and (17) use it.
Given all spatial links, the layer gauges g_t are independent; in one layer
g_(t,v) has a translated one-link density with parameter <= deg(v) beta <=
6 beta; a greedy 7-colouring and row 1145 (1) bound the transform of the
ordered product in (x)_v pi_(d_v) by e^(-r w/(7 b_beta)); mixtures keep the
bound; inversion costs prod d_v^2 and the sum factors into N copies of
1 + eta. Change of variables: with G_t = g_0...g_(t-1) and U'_t = G_t.U_t,
the electric argument becomes a conjugate of U'_(t,e) U'_(t+1,e)^(-1) (class
function), magnetic factors are invariant, Jacobian one, last endpoint
G_r.y. So the slab weight at fixed gauges is F^r(x, G_r.y), and the density
of G_r is F^r(x, g.y)/(PF^r)(x,y). On an open box the same proof holds with
N its vertex count.

**(14), L156-161. HOLDS.** Interior link: a chain of <= 2b plaquettes to a
tree link, |U_e - 1|^2 <= 2b * 2A = 4bA. Wrapping link: a transverse step
costs |1-U_p| plus two link distances, <= C sqrt(bA); <= 2b steps give
|U_e - H_i|^2 <= C b^3 A. Sum: 3b^2 C b^3 A + 3b^3 4bA <= C b^5 A. Second
bound: |1 - B_p| <= |1 - U_p| + sum_(e in p) |U_e - B_e|, squared and summed
with <= 4 occurrences per edge.

**Path, L163. HOLDS.** Along geodesics each link stays within |U_e - B_e| of
B_e, so the action stays <= C b^5 A(U). In B(H) the only nontrivial
plaquettes are commutators [H_i, H_j]; Re[q_i, q_j] = 1 - 2 |Im q_i x Im
q_j|^2 gives the stated action, which decreases as the angles shrink; signs
joined in one circle subgroup commute. Speeds are bounded. The remarks on
frozen finite groups and U(1) are correct descriptions.

**(13), L149-154 and L165-171. HOLDS.** Diagonal bound, vacuum bound and the
1/4 tail bounds of Section 1 hold on the torus (spanning tree with d chords;
<= E plaquettes in the trial set; M <= 1). Kernel of the projected k-step
transfer: int (MCM)^k(U, g.Y) dg. Electric: one-step distance <= C/k +
C/sqrt(beta), so the electric exponent is <= kE beta (C/k^2 + C/beta) =
CE(beta/k + k). Magnetic: each slice has beta A <= C b^5 H_0 + CE. Powers of
beta: 3kE/2 - 3(k-1)E/2 - 3(V-1)/2 = 3d/2. With E = 3b^3, H_0 <= C b^3 the
bound K^k >= beta^(3d/2) exp[-C(b^3 beta/k + k b^8)] follows, and
lambda_0^k psi psi <= (C beta^(3/2))^d converts it. The Dirichlet argument
for K^k uses the same eigenfunctions. With k ~ sqrt(beta)/b^(5/2) both terms
are b^(11/2) sqrt(beta); at k = 1, b^3 beta <= b^(11/2) sqrt(beta). The
factor 1/k <= sqrt(beta) is absorbed. All gauge-invariant states, so all
flux sectors, are covered.

**Consequence, L173-175. HOLDS.** With b_j = o(beta_j^(1/11)),
b^8 + b^(11/2) sqrt(beta) = o(beta), so m >= e^(-o(beta)); first passage
(both passage bounds, K = Theta(beta)) gives log T_j >= c beta_j; hence
(T_j - 1) m -> infinity much faster than C b^3 log(2+beta), and J <=
2 log(1+S) -> 0. At b = n the b^8 term already exceeds log T.

**(16), L188-203. HOLDS.** Swapping x_s, y_s exchanges A_(s-1) with B_(s-1)
and A_s with B_s, so nu is invariant. Expanding prod (A_t + B_t): an even set
of crossed edges gives two T-loops ((Tr F^T)^2), an odd set one 2T-loop;
2^(T-1) of each. c_beta(u v^(-1)) = e^(-beta + beta u.v)/I(beta) gives
A_t/B_t = e^(beta D_t) with all magnetic factors cancelling. Then
E_nu prod (A-B)/(A+B) = (Zh_T^2 - Zh_2T)/(Zh_T^2 + Zh_2T) = tanh(Jh/2).

**(17), L205-217. HOLDS.** Relabelling inside a fixed crossing pattern flips
two signs of D_t and keeps |D_t|. Bad matched step: Tr(F_bad F^(k-1)) <=
||F_bad||_(S_k) ||F^(k-1)||_(S_(k/(k-1))), and Tr|F_bad|^k = Tr F_bad^k for
even k (T = n/2 is even on row 720's grid); Tr F_bad^k <= e^(-k beta E/4)
pointwise; Tr F^k >= exp[-CkE(1 + log beta)]. So each matched sum is >= 3E/4
except with probability e^(-c beta E). Unmatched sum: in two T-loops a
constant gauge on the second loop preserves the law; in one 2T-loop (15)
replaces F^(T-1) by its projection at a factor (1 +/- eps)^2, eps -> 0, giving
the same invariance. Under independent Haar vertex gauges the sum has mean 0
(distinct endpoints), and one gauge moves it by <= 6 x 2 x 2 = 24;
McDiarmid gives P(|S| > E/2) <= 2 e^(-N/128). Then D_t >= 3E/2 - E/2 = E.
Summing over T edges and the two laws gives (17).

**(18)-(19), L219-229. HOLDS.** prod_t sgn D_t = 1 - 2 1[sheets exchange],
so its nu-mean is 1 - 2p_j. On the good event 1 - tanh(beta E/2) <=
2e^(-beta E), and off it the difference is at most 2. Row 1145 (17) gives
J - Jh = o(1). tanh(log(1651/1650)/2) = 1/3301, and
limsup (1 - 2p_j) < 1/3301 iff liminf p_j > 1650/3301. So (19) is (24).

## Step 7. Obstructions

### 7a. (10)-(12), L231, (21)

**(10), L110-129. HOLDS.** With U_p = x a y^(-1) b, w_p = Re(b x a ybar) =
(b x a).y, and x -> b x a is orthogonal. At sides >= 3 only p contains two
opposite links. Each link lies in six plaquettes, so |a|, |d| <= 5B. The
Gaussian identity: E_z exp(sqrt|t| z.w) = exp(|t| |w|^2/2) with
|w|^2 = 2 + 2 sgn(t) x^t O y, which gives e^(t x^t O y). Given z the links
are independent; given (x, y), z ~ N(sqrt|t| w, I) with shift <= 2 sqrt(B),
so P(|z| <= 2 sqrt(B) + 4) >= P(|N(0,I_4)| <= 4); there the fields are
<= 7B + 4 sqrt(B). Tangential covariance (1/3) E sin^2 r >= c/(1+|H|):
denominator <= C|H|^(-3/2), numerator >= c|H|^(-5/2) on
[1/(2 sqrt|H|), 1/sqrt|H|]. The bilinear part (x-Ex)^t O (y-Ey) is
orthogonal to L^2(x) + L^2(y) for independent x, y; its variance
tr(C_x O C_y O^t) >= c_x c_y tr(P_1 P_2) >= 2 c_x c_y, since two 3-planes of
R^4 meet in >= 2 dimensions. Conflict degree <= 2 x 6 x 4 x 6 = 288, so 289
colours; within a colour each plaquette term reads at most one pair, so the
pairs are conditionally independent and variances add. Sharpness: with one
coupling B the holonomy is tilted Haar and Var(w_p) <= E(1 - cos r)^2 <=
C(1+B)^(-2).

**(11), L131-136. HOLDS.** A(t,t') = Z((t+t')/2)/sqrt(Z(t) Z(t')). With
f(s) = log Z on the segment, f'' >= kappa = c||t'-t||^2/(1+B)^2 by (10), and
(f(0)+f(1))/2 - f(1/2) >= kappa/8. The cylinder is a torus with sides >= 3.
For cut against full on D_j: ||t'-t||^2 = beta^2 |D_j|, B = beta >= 1. TV >=
1 - A since min(p,q) <= sqrt(pq).

**(12), L138-143. HOLDS.** A(cut, restored) = E sqrt(W)/sqrt(EW) >= sqrt(EW)
since sqrt(W) >= W. With couplings 0 and 2 beta on D_j,
Z(s) = Z_cut e^(s|D|) E_cut e^(-s sum_D a), so A(0, 2beta) = EW/sqrt(EW^2),
and (11) with ||Delta t||^2 = 4 beta^2 |D_j|, B = 2 beta gives (12). Route
count: affinity >= q forces ||Delta t|| <= C(C_*, q) beta per step, and the
endpoints are beta sqrt(|D_j|) apart.

**L231 (absolute or local swap estimate). HOLDS.** prod_t sgn D_t is
invariant under slice swaps, so it is a function of the unordered history; it
equals the expansion parity on the good event of (17) under both covers,
hence TV >= 1 - C T e^(-cN). Each term of D_t has modulus <= 4, so changing
one link moves D_t by <= 8; at most 2E/32 links change at a time edge, so
D_t moves by <= E/2 < E and its sign is kept on the good event.

**(21), L245-250. HOLDS.** Selected 12-plaquettes need x_1 and x_2 at
interval tops; tops are never consecutive (intervals have length >= 2), so
the plaquettes are edge-disjoint and all their links are free crossing
links; M_* = q^2 n. On a free link C_beta multiplies fundamental
coefficients by r_beta, so Psi prod_(p in S) w_p has eigenvalue
Lambda r_beta^(4|S|); different S are orthogonal (an unpaired w_p integrates
to zero over its own free links); all are gauge invariant. With
1 + S <= e^J: J_cut(h) >= log sum_S r_beta^(4h|S|) = M_* log(1 + r_beta^(4h)).
With 1 - r_beta <= C/beta, M_* r_beta^(4h) >= M_* e^(-8Ch/beta) -> infinity
when h = o(beta log M_*); log M_* ~ 3 log n. A pointwise (1 +/- eps) kernel
bound for the stand-alone segment would give |J_cut(h)| <= 2 log((1+eps)/
(1-eps)), so such a bound needs h >= c beta log n.

### 7b. (22)-(24a), L284, L286, Section 12 (L387-396)

**(23), L264-275. HOLDS.** V(q) = E_x e^(qY) with |Y| <= 3Nk, so
|V| <= e^(3Nk|q|). Jensen at a radius in [2w, 3w]: each zero in |q| <= w
adds >= log 2, so at most 9Nkw/log 2 zeros. Blaschke factors
r(q-a)/(r^2 - abar q) have modulus one on |q| = r and |B_a(0)| = |a|/r <= 1,
so |g(0)| >= 1. 3Nkr - log|g| is a nonnegative harmonic function with mean
<= 3Nkr; the Poisson-kernel gradient bound on |q| <= 2r/3 gives
|g'/g| <= CNk. |abar/(r^2 - abar q)| <= r/(r^2/3) = 3/r. The pole terms of
D = 2V_T'/V_T - V_2T'/V_2T combine to sum m_zeta/(q - zeta) with
m_zeta = ord_zeta R and sum |m_zeta| <= CNTw. |P| <= 1 on U and
|P(z)/(z-zeta)| <= 1/(4(beta+w)). This gives |PD| <= CNT on the half tube.

**(24a), L277-282. HOLDS.** Cauchy on row 1145 (22): |J'| <= 2(1+beta)
C N m e^(-m/4)/c on |z| <= s_0/2, with m ~ c n/(1+beta). With beta ~ log n
(both RF25 bounds), w is of order A_eps while s_0 -> 0. PD is analytic on
the half tube (each counted pole of D is a simple pole cancelled by P).
Three circles at radii s_0/2, w/8, w/2 give inner weight
log 4/log(w/s_0); each later step w/8 -> w/4 inside w/2 has weight 1/2 and
covers the next centre; ceil(8 beta/w) steps leave the factor
>= (1/2) exp[-8 (log 2) beta/w].

**Return to real couplings, L284. HOLDS.** With 8 log 2/A_eps < eps/4 the
factor is >= n^(-eps/4)/2, and log(2 + w/s_0) = O(log log n), so the
negative term is >= n^(1 - eps/4 - o(1)). Off the radius-n^(-12) disks,
-log|P| <= M log[4(beta+w) n^12] = O(n^(1-eps) log n). On the removed set
(length <= 2M n^(-12)), |J'| = 6NT |wbar_T - wbar_2T| <= 12NT. So
int |J'| -> 0 and J(beta) = J(0) + o(1) -> 0. Real zeros or poles do not
occur: Z_k(s) > 0 for every real s.

**(22), L254-262. HOLDS.** The direct statement is the last paragraph; the
converse is its contrapositive. w = A_eps beta/log n is bounded and
w/beta -> 0.

**Witness, L286. HOLDS (conditional on row 865's W-phys-CA).** J(beta) >=
log(1+S_ev) >= log(1 + rho_CA^(L/(3d))) at t = L/2; the contrapositive of
(22) gives M > n^(1-eps) for all fine cutoffs. R has real coefficients and no
real zeros or poles, so its points come in conjugate pairs off the axis. The
file correctly says this gives no bound above the seed threshold.

**Section 12, L387-396. HOLDS (the count conditional on the witness).** For
R_D the moments involve <= 2|D_j| insertions, so (23) holds with C|D_j|.
J_D'' = 2 Var_1 - Var_2 gives |J_D''| <= 2|D_j|^2 + 4|D_j|^2. With
|J_D| <= C n^3 m e^(-m) on |u| <= u_* (from (28)) and step
l = e^(-m/3)/(1+|D_j|): |J_D'| <= 2|J_D|/l + 3|D_j|^2 l <= e^(-m/5), since
m >= n/(log n)^C' and |D_j| <= C n^4. Rectangle: v is harmonic
(k = pi/(2r)), zero on the sides and top, cos(pi x/(2r)) on the bottom;
log(|PD|/B_0) + (m/5) v <= 0 on the boundary, hence inside; min v on
|x| <= r/2, y <= r/2 is cos(pi/4) sinh(pi/4)/sinh(pi/2) > 0. The rectangle
lies in the half tube since sqrt(2) r << w. Propagation as in (24a) with
log(2 + w/r) = O(log log n), and the same disk removal (|J_D'| <= 4|D_j|),
give int |J_D'| -> 0 when M <= n^(1-eps). With J_D(beta) = J(beta) >= j_L on
witness sizes, M > n^(1-eps) eventually.

### 7c. (25)-(26), L290-314

**(25), L292-304. HOLDS (conditional on the witness).** C_h: vertex averaging
keeps G^h(x, g.y) within (1 +/- eps) Lambda^h Psi(x) Psi(y) because Psi is
invariant, so Delta(C_h) <= 2 log((1+eps)/(1-eps)) = o(1). An error d gives
Delta(K_h) <= Delta(C_h) + 4d. Doob kernel p_x: its ratio extrema satisfy
M/m <= e^(Delta(K_h)) and the p_y-mean of p_x/p_y is one; the chord bound
for (t-1)_+ gives TV <= (M-1)(1-m)/(M-m), maximal at m = R^(-1/2) with
value (sqrt R - 1)/(sqrt R + 1) = tanh(log R/4). For an excited
eigenfunction phi (continuous, phi/psi bounded and not constant), the Doob
operator multiplies phi/psi by (lambda/lambda_0)^h, so
(lambda/lambda_0)^h <= tanh(Delta/4). The witness gives
(lambda/lambda_0)^h >= rho = e^(-M_K a_j h), hence Delta >= 2 log((1+rho)/
(1-rho)) and d >= (1/2) log((1+rho)/(1-rho)) - o(1). M_K is the even-gap
constant of row 865 (log(1/rho_CA) = log(3C_K/c_K)), as in row 1145 (27).

**(26), L306-312. HOLDS (conditional on the witness).** The 2h cylinder has
endpoint marginal K_h(x,y) K_h(y,x)/Tr(PF^(2h)) = K_h^2/Tr. The integral is
<sqrt p, K_h sqrt q>/sqrt(Tr K_h^2) with unit vectors sqrt p, sqrt q, so the
supremum is ||K_h||/||K_h||_HS = lambda_0^h/sqrt(Tr PF^(2h)), attained at
psi^2, and the one even excitation gives (1 + e^(-2 M_K a_j h))^(-1/2).
Cut side: C_h^2 alpha(x)^2 beta(y)^2 is within (1 +/- eps)^4 of a product
law, so its TV distance to a product is o(1); then
|A(Q, Q') - A(Q, Pi)| <= (int (sqrt Q' - sqrt Pi)^2)^(1/2) <= sqrt(2 TV)
by Cauchy-Schwarz, which gives the 1/sqrt(2) + o(1) bound.

### 7d. Divergence arguments of Sections 10-11, (29)

**L341-347 (Section 10 divergence). HOLDS.** Every other Sigma plaquette
assigned to the cell has a crossing link outside p: Sigma_2 plaquettes are
edge-disjoint from p, and a Sigma_1 plaquette has two parallel crossing
links, which cannot both lie in p since a parallel pair fixes the
plaquette. A free link is its own tensor factor with Haar endpoint law and
the centre-invariant kernel C_beta, so flipping its block path is a symmetry
independent of everything else; hence E[Y_rest | paths of p] = 0 and
conditional Jensen gives z_A >= E e^(uY_p) - 1 = E cosh(uY_p) - 1. Reference
against stationary: density prod 1/D_H >= 2^(-4). Stationary moment
<w_p, C^(4 tensor d) w_p> = r_beta^(4d)/4; with r_beta^(4d) >= 1/2 for
d <= c_2 beta and H >= C_2 beta, E Y_p^2 >= c_3 H beta. z_B: integrating
the intermediate mu-endpoints gives (D_H - 1)^(*m) = D_(mH) - 1. If z_B were
f(x) + g(y), integrating each variable against mu would force z_B = 0, but
the free link keeps the multiplier r_beta^(mH) != 0. A and B share a
component in one block, so they are incompatible; in the two-polymer gas
1 + t_A z_A + t_B z_B the t_B t_A^k coefficient of the log is
(-1)^k z_B z_A^k. These lists reach both end blocks through B, so they
survive the end cancellation; with z_A >= 1 the terms do not tend to zero.

**(29), L357-370. HOLDS.** Deficits: <psi_beta, K_(beta/2) psi_beta> =
lambda(beta) E_stat e^((beta/2) sum a) <= lambda(beta/2), and
I(beta/2)/I(beta) <= C, so E sum_e a(U_e U_e'^(-1)) <= CE/beta by Jensen,
and 1 - r_e = E a. Choice of faces: a crossing 1-link is a single-link
component iff its 2- and 3-coordinates are neither tops nor bottoms; with
b >= 8 there are >= c b^2 such plaquettes per face, each inner 2-link used
once, so one plaquette has internal deficit <= Cb/beta. Invariance of the
stationary pair law under (U, U') -> (g.U, g.U') makes Delta = U_e^(-1) U_e'
independent of U_e with a central law, so E[U_e' | U_e] = r_e U_e. The four
links lie in four distinct tensor factors, and w_p is multilinear in them,
so the one-step quotient is prod r_e >= 1 - Cb/beta; the trial vector has
mean 0 and norm 1/4 (U_p is Haar). Jensen for x^t on the spectral measure
in [0,1]. Disjoint faces give independent factors; the normalized products
form an orthonormal invariant family, and the trace of the positive
operator dominates its diagonal sum: (1 + (1 - Cb/beta)^t)^(M') with
M' >= c n^3/b^3.

**L372. HOLDS.** The singleton activity is E cosh(uY_p) - 1 >=
u^2 E Y_p^2/2; the stationary moment at separation d is >= (1-Cb/beta)^d/4
by the proof of (29); the reference costs a factor (1+sigma)^(-4); summing
d <= c' beta/b gives c u^2 H beta/b. The electric polymer of a component
group containing a free link of p again has a nonzero rectangular
difference, so the same (-1)^k z_B z_A^k family diverges when
u sqrt(H beta/b) >= C'.

### 7e. Section 13 (L398-407) and the closing paragraphs

**L400. HOLDS.** With second eigenvalue exp[-d + (d - kappa/T) z/beta], its
T-th power is v and R = (1+v)^2/(1+v^2). On |z| <= c/(1+beta),
|v| <= exp[-Td(1 - c/(beta(1+beta)))], so log R is exponentially small in
T/(1+6beta). At z = beta, v = e^(-kappa) and R - 1 = 2e^(-kappa)/(1 +
e^(-2kappa)): 0.648 at kappa = 1 and 4.5e-6 at kappa = 13, against
1/1650 = 6.06e-4 (GUIDE values; the file's inequalities e < 3 and e > 2
give the same comparisons by hand).

**L402-407. HOLDS.** v = -1 (double zero of R) and v = +/- i (simple poles)
give z = beta (Td + i phi)/(Td - kappa), i.e. the displayed line, with
phi = (2r+1) pi and (r + 1/2) pi; the phase sets are disjoint, so nothing
cancels. Spacing in Im z is of order beta/(Td) ~ 6 beta^2/T and the real
offset kappa beta/(Td - kappa) = O(beta^2/n) is far inside the tube, so the
count in the tube of width w = A_eps beta/log n is Theta(n/(beta log n)),
which exceeds n^(1-eps). The two offsets differ by O(beta^2/n). So both
models pass the count of (22) and lie on opposite sides of the threshold.

**OPEN paragraphs (L11, L145, L314, L349, L374, L409).** They claim nothing
beyond the proved statements. L409's remark that (11) also applies with u_*
in place of zero holds: ||Delta t||^2 = (beta - u_*)^2 |D_j| >=
beta^2 |D_j|/4.

**GUIDE paragraphs (L3, L7, L9, L15, L179, L254, L290).** Not proof steps.
Spot checks: L7's account of row 1146 (the (APR) and L394 corrections)
matches that check's table rows 28 and 40; L286 and (25) cite row 865
correctly (`gap-sdcyl-ca-astra.md` L218-242: S_ev(n_A; B) >=
rho_CA^(2A/(3d)) with A >= 2d, and m_ev <= (2/(3d)) log(3C_K/c_K)); L335's
outline lines 1225-1347 are the tree estimate read by row 1146.

**RESULT line (L411). HOLDS.** It states the equivalence (24) <=> (30), the
vanishing response up to u_*, and the count on witness sizes (conditional on
the witness, as "admitted witness sizes" says), and it marks (30), (W) and
the gap OPEN. It says "unchecked"; this file is the check.

GUIDE run (pure Python, script `guide.py` in this session's scratchpad
folder `row1148`, not kept in the repository; peak memory a few MB):
tanh(log(1651/1650)/2) = 1/3301; the two-level excess ratios above; the
chord maximum (sqrt R - 1)/(sqrt R + 1) at m = R^(-1/2) for R = 1.5, 4, 50;
the tangential variance of e^(H.x) on S^3 times (1+H) stays in [0.25, 1] for
H in [0, 1000]; the commutator identity (error 9e-16 on 2000 random pairs);
min v = 0.267 on the quarter rectangle; McDiarmid exponent 1/128 per site.
All agree with the hand arguments. They guide only.

## Step 8. Verdict table and result

Scope remarks (not corrections). (a) (30) is an exact real restatement of
(24), hence of (W) through row 720; it carries no estimate of its own. (b)
The positive restoration (27) is a small-coupling expansion on a set of
vanishing physical four-volume; it is not selective in the sense of the
brief, Section 4, and the file does not offer it as a step on the crux. (c)
Statements at u = beta that use row 865's W-phys-CA (L286, (25), (26), the
lower limit in (30), Section 12) are conditional on the account's premises,
as the file labels them.

| # | Statement (line in `gap-solve3-astra62.md`) | Verdict |
|---|---|---|
| 1 | (1), open-box gauge estimate, C = 8 (L17-21) | HOLDS |
| 2 | Set-up of (2): c_beta, I(beta) ~ beta^(-3/2), ball mass, kernel (3), positivity, simple positive invariant top (L23-36) | HOLDS |
| 3 | K(U,U) <= (C beta^(3/2))^d; lambda_0 >= e^(-C_0 E) (L38) | HOLDS |
| 4 | Minorization on D x D; tail bound 1/4 (L40-46) | HOLDS |
| 5 | Dirichlet form; (2) (L48-53) | HOLDS |
| 6 | (4) (L57-64) | HOLDS |
| 7 | (5) (L66-71) | HOLDS |
| 8 | b = floor(gamma (log n)^(1/5)), J_cut -> 0, fraction 2/b (L73) | HOLDS |
| 9 | (6) (L75-80) | HOLDS |
| 10 | (8) (L90-95) | HOLDS |
| 11 | Transfer word with rest kernel (L97) | HOLDS |
| 12 | (7), also for general nonnegative weights (L84-88, L99) | HOLDS |
| 13 | (9) and its equivalence with (24) (L101-106) | HOLDS |
| 14 | (10), with the optimal power (L110-129) | HOLDS |
| 15 | (11) (L131-136) | HOLDS |
| 16 | (12) and the sqrt(|D_j|) route count (L138-143) | HOLDS |
| 17 | (13) (L149-154, L165-171) | HOLDS |
| 18 | (14) (L156-161) | HOLDS |
| 19 | Path construction to central signs (L163) | HOLDS |
| 20 | J -> 0 for b_j = o(beta_j^(1/11)); no decay at b = n (L173-175) | HOLDS |
| 21 | (15) (L181-186) | HOLDS |
| 22 | (16), the sewing identity (L188-203) | HOLDS |
| 23 | (17) (L205-217) | HOLDS |
| 24 | (18) and (19) <=> (24) (L219-229) | HOLDS |
| 25 | Swap obstruction: TV >= 1 - CTe^(-cN), E/32 robustness (L231) | HOLDS |
| 26 | (20) (L235-243) | HOLDS |
| 27 | (21) and the length bound h >= c beta log n (L245-250) | HOLDS |
| 28 | (23) (L264-275) | HOLDS |
| 29 | (24a) (L277-282) | HOLDS |
| 30 | Return to real couplings; (22) and its converse (L254-262, L284) | HOLDS |
| 31 | Witness count M > n^(1-eps), conjugate pairs (L286) | HOLDS, conditional on W-phys-CA |
| 32 | (25) (L292-304) | HOLDS, conditional on W-phys-CA |
| 33 | (26) and the cut-side affinities (L306-312) | HOLDS, conditional on W-phys-CA |
| 34 | (27): parameters, a_j h -> 0, J -> 0 on 0 <= u <= u_* (L318-324) | HOLDS |
| 35 | Reference measure: ||D_(l,c) - 1|| <= sigma for l >= H (L326) | HOLDS |
| 36 | Factor expression and bound sigma for |u| <= u_* (L328-333) | HOLDS |
| 37 | (28) and the rest-kernel step (L335-339) | HOLDS |
| 38 | Section 10 divergence for u sqrt(H beta) >= C' (L341-347) | HOLDS |
| 39 | Section 11: Sigma_2 restored at full strength in (7), (9), (20), (27) (L353-355) | HOLDS (precision: a small box at coupling beta must use the projected gap from (2) with (8), then (15), as L326 does; the unprojected deficit c/(1+beta) alone would need blocks of length C(1+beta)^2) |
| 40 | (29) (L357-370) | HOLDS |
| 41 | Next expansion stops for u sqrt(H beta/b) >= C' (L372) | HOLDS |
| 42 | (30) <=> (24) (L378-385) | HOLDS (the lower limit conditional on W-phys-CA) |
| 43 | Section 12: count for R_D after resummation (L387-396) | HOLDS, conditional on W-phys-CA |
| 44 | Section 13: two-level models, kappa = 1, 13; zero and pole lines (L400-407) | HOLDS |
| 45 | RESULT line (L411) | HOLDS |

No statement FAILS. No correction is needed. One precision note (row 39)
changes no constant or conclusion. No mass gap is claimed by the file or by
this check.

RESULT: HOLDS — check of row 1147 (`library/gap-solve3-astra62.md`),
checked line by line by hand by Claude Opus 5.5 (max effort), positive
claims first: the open-box estimate (1) and gap (2); the localization (4)-(9);
the positive restoration (27)-(28) with its polymer expansion and the exact
resummation of the double-boundary plaquettes in Section 11; the
equivalence (30); the periodic-cube gap (13) and its consequence; the
sewing identity (16)-(19) — all HOLD. All obstructions ((10)-(12), (15),
(21), (22)-(24a), (25)-(26), (29), the divergences of Sections 10-11,
Section 13) HOLD, those at u = beta conditionally on row 865's W-phys-CA as
labelled. 45 statements; 0 FAILS; 0 corrections; one precision note on the
small-box route in Section 11. (30) is an exact real restatement of (24)
and of (W), with no estimate of its own; the strict bound in (30), (W) and
the four-dimensional SU(2) mass gap stay OPEN.
