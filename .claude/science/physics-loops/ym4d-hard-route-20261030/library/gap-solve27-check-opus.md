lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-20T21:06Z

# Row 1245: check of row 1236 (`library/gap-solve27-astra62.md`)

Queue row 1245 (FINISH.md line 1326): a line-by-line check by hand, cross-provider, of
`library/gap-solve27-astra62.md` (row 1236), positive claims first: the static-pair threshold (25),
the multiplicity comparison (27), the physical-energy estimate (33); then everything else. Also: is
the main comparison a restatement of an earlier row? Verdict per statement: HOLDS, HOLDS AFTER
CORRECTION, FAILS, with the line. A numeric run may guide only.

Provenance: Claude Opus 5.5 (max reasoning), Mac mini worker 1, started 2026-11-20T09:06Z (date -u),
checkout pinned at commit 3a45c201f on `claude/ym4d-hard-route`. The checked file was written by a
different provider (astra62), so this check is cross-provider; it is still one check by one model.

## Plan (at most eight steps; one step per response, result appended after each)

1. Read FINISH.md rules (head, efficiency rules, Build on published work), GOAL.md, and the checked
   file in full; list every numbered display and statement of the checked file with its line.
2. Check the static-pair threshold (25) with the rows it cites.
3. Check the multiplicity comparison (27) with the rows it cites.
4. Check the physical-energy estimate (33) with the rows it cites.
5. Check everything else, line by line, in file order.
6. Restatement question: grep `library/open-core.md` and the FINISH rows for the main comparison.
7. Optional numeric guide (under the numeric lock, only at 50 percent memory free or more).
8. Verdict table (statement, line, verdict) and the RESULT line.

## Status log

- 09:06Z step 0: file created with the plan.
- about 09:10Z step 1 done: rules, GOAL.md and the checked file read in full (475 lines); inventory below.
- 09:16Z (date -u) step 2 done: (25) HOLDS, with (20), (23), (24), (26), L312, L328, L344.
- 09:18Z step 3 done: (27) HOLDS, with (28), (21), (22).
- 09:20Z step 4 done: (33) HOLDS, with (29)-(32); (34), (35) HOLD.
- 09:25Z step 5 done: every other statement HOLDS; three precision notes, no FAILS.
- 09:27Z step 6 done: the main comparison is not a restatement (searches below).
- 09:28Z step 7 done: numeric guide (about 10 s under the numeric lock, 09:27-09:28Z, memory 54 percent free) agrees.

## Step 1. Inventory and dependency map

The checked file (pinned `b71c9f52a` in its own header; read here at `3a45c201f`) has 35 tagged
displays and 55 PROVED paragraphs (lines 26-471), one ARGUED paragraph (L241), GUIDE paragraphs and
two OPEN paragraphs (L15, L473). Its RESULT (L475) claims three positive results: (25), (27), (33).

Cited earlier rows and their checks (all read from `RESULT` lines at `3a45c201f`):

| Row | File | Used for | Check row, verdict |
|---|---|---|---|
| 1143 | `gap-solve-astra62.md` | (8) open-line isometry and formula | 1144, all HOLD |
| 1145 | `gap-solve2-astra62.md` | (1) one-link adjoint mean, (16)-(18) static charges | 1146, HOLDS |
| 1149 | `gap-solve4-astra62.md` | (16) Bessel-ratio monotonicity | 1150, HOLDS |
| 1151 | `gap-solve5-astra62.md` | (21)-(24) dissemination, pressure, open boxes | 1152, HOLDS |
| 1155 | `gap-solve7-astra62.md` | (9) moments of sqrt(beta)abs(1-U_p) | 1156, HOLDS |
| 1163 | `gap-solve10-astra62.md` | (13)-(14) rectangular source (hypothesis only) | 1164, HOLDS |
| 1231 | `gap-solve26-astra62.md` | (1)-(2) radius comparison, (4)-(5), (8)-(9) | 1235, HOLDS (some items given PL3, PL5) |
| 860 | `gap-hs-max.md` | Lemma OS (electric spin insertion) | to read |

Dependency map of the three positive claims (my reading; to be verified in Steps 2-4):

- (25) = lower bound (24) + upper bound from ribbons. (24) uses the score inequality (23) (self-contained),
  the slow-band plaquette bound (20) (which uses row 1151 (21)-(22a)), the ribbon trial r_xy >= 1 - O(1/beta)
  (row 1143 (8) and a half-tilt bound), and the resistance limit (L328). The upper bound uses the open-line
  formula W(gamma,s) <= r_xy^s (row 1143 (8)), the fixed-loop weak-coupling limit (26) (row 1231 (8)-(9),
  row 1151 (24), row 1155 (9), nested-projection coupling of row 1231 (1)), and the Fejer limit (L344).
- (27) = (24) + the ribbon estimate (28) in every slow state + min-max through the open-line isometry.
  (28) uses Schatten-Holder slab dissemination (L366), the box upper bound of (22) (L276-280) applied to a
  ribbon array (L368-373), and kernel domination for the clipping (L375).
- (33) = the Schur complement (30), the separation (29) (a refinement of (23)), (25), (28), the return-time
  coefficients (31), the self-energy exhaustion (32), then the resolvent identity.

A first quick reading (to be confirmed): the free-field constants are consistent. With SU(2), w = tr/2 and
Gaussian curvature of covariance P_ex/beta per colour, beta(1 - W) -> (3/2)<j, P_ex j> for a fixed loop;
(3/2)R(z) = 3[G_3(0) - G_3(z)] is beta times the Coulomb static energy g^2 C_F [G_3(0) - G_3(z)] with
g^2 = 4/beta, C_F = 3/4; R(e_1) = 1/3 because the three directional integrands sum to one; one plaquette
has <p, P_ex p> = 1/2 (rank 3 of 6 orientations), so c_1 = 3/4 and c_1 - c = 1/4 at a nearest neighbour.

## Step 2. The static-pair threshold (25) (L330-L344), with its inputs

Inputs read: row 1143 L117-L142 (the local input u >= 1 - K/beta at L121-L126; the open-line formula (8)
at L128-L133 and its two uses); row 1151 L240-L312 ((19)-(24) with proofs); row 1231 L14-L105 ((1)-(9)
with proofs); the check rows 1144, 1152, 1235 (RESULT lines: all HOLD).

**(20) L245-L256: HOLDS.** Temporal case: T_{exp(tX)} has the electric factor on one link at coupling
(1-t)beta times z_{(1-t)beta}/z_beta, so it is a positive operator for |t| <= 1/4, and the trace of its
M-th power over Tr U^M is the Wilson log moment of t sum beta(1-w) over the marked temporal plaquette at
all M times. Row 1151 (21) (the trace-Holder dissemination, also valid for t < 0 because all couplings
stay positive) and (22a) give log||T_{exp(tX)}|| <= 3t/4 + C(t^2 + |t| beta^(-eta)) after M -> infinity on
even M >= n (the (22b) error C[(log beta)/b + (b/n) log beta] does not depend on M). The Taylor bound
|e^{tX} - 1 - tX| <= C t^2 e^{X/2} for |t| <= 1/4, X >= 0, holds, and ||T_{e^{X/2}}|| <= z_{beta/2}/z_beta <= C
because c_d(beta/2) <= c_d(beta) (row 1149 (16)) gives the operator order on the full slice, and kernel
domination passes to the projected space. For unit f in Q_h: 1 - delta + t<f,T_X f> - Ct^2 <= <f,T_{exp(tX)}f>
<= exp(3t/4 + C(t^2+|t|beta^(-eta))), and both signs of t with |t| ~ sqrt(delta) give
|<f,T_X f> - 3/4| <= C(sqrt(delta) + beta^(-eta)). The identity T_X = beta(U - W_e^* F_xy W_e) is the
compression formula of (6). Spatial case: U >= h|f><f| for unit f in Q_h holds because U >= 0 (expand f in
eigenvectors with eigenvalues >= h and use Cauchy-Schwarz); then ||U_t|| >= h<f, e^{tX} f> >= h exp(t<f,Xf>)
by Jensen. The compression is self-adjoint, so the uniform Rayleigh bound is the norm bound.

**(23) L290-L303: HOLDS.** I redid each line. The varied bond trace is w(e^{-tv_i} e^{tb_j} H_e) with
b_j = Ad_{X_e} v_j; its second t-derivative at 0 is w((v^2 + b^2 - 2vb)H) = -|v-b|^2 w(H) - 2w((v x b)H), so
the negative second derivative is as written. |Re((v x b)H)| = |Re((v x b)(H-1))| <= |v||b||1-H| because
v x b is imaginary. With Ad_{X_e} = I + O(eps) on internal edges and E|1-H_e| <= eps, the score covariance is
at most beta(1+C eps)L_B + C_B eps beta I <= beta(L_B + C'_B eps I), since L_B <= 12 I. The covariances of
Z = g_x A g_y^(-1) with the scores are c_(x,a) = -a m, c_(y,a) = m a. Bessel in operator form (Gram of
J^(-1/2)s at most I) summed over an orthonormal fibre basis gives
c^T J^(-1) c = beta^(-1) sum_a [G_xx||am||^2 + G_yy||ma||^2 - 2G_xy Re<am, ma>] <= 1 - ||m||^2, and
sum_a Re<am, ma> <= 3||m||^2 with G_xy >= 0 gives 3R||m||^2/beta <= 1 - ||m||^2. (The exact value is
sum_a <am, ma> = 3||m_0||^2 - ||m_1||^2, used later for (29).)

**L305-L312 (ribbon trial r_xy >= 1 - O(1/beta)): HOLDS.** <X(gamma)psi, F_xy X(gamma)psi> = W(gamma,1) is
row 1143 (8) at k = 1 after N -> infinity; shelling gives 1 - w(U_dD) = |1-U_dD|^2/2 <= |gamma| sum (1-w_p),
and E(1-w_p) <= K/beta is row 1143 L121-L126 (uniform in both periods).

**L314-L326 (lower bound (24)): HOLDS.** <A, F_xy A> <= <f, Uf> with f = ||A|| (the charged kernel is k_0
times the conditional expectation of a unitary colour action); the band split gives ||f - Q f|| = O(beta^(-1/4))
for Q = Q_{1-beta^(-1/2)}; (20) with Markov at beta a_p > beta^(3/4)/2 makes every plaquette of a fixed cube B
close to 1 off vanishing f^2 mass, hence internal links O_B(beta^(-1/8)) in tree gauge (B simply connected);
int E_{g|X,Y}|1-H_e| d omega <= C/sqrt(beta) since sqrt(2X) <= C e^{X/2} and ||T_{e^{X/2}}|| <= C; Markov at
beta^(-1/8) leaves omega-mass O(beta^(-3/8)). Then 1 - r_xy >= [1 - (1+3R_B^eps/beta)^(-1/2)] omega(good),
-log r >= 1 - r, eps -> 0. The resistance limit L328 (sup over finitely supported v of 2(v_x - v_y) - Q(v),
increasing in B, equal to the Fourier integral because finitely supported v are dense in the 3D energy space)
HOLDS.

**(26) L335-L342: HOLDS as an implication from row 1231 (1), (2), (8), (9) and row 1151 (24), all checked.**
The scaled boundary deficit is the transported sum of scaled imaginary parts up to O_{L^2}(beta^(-1/2)) (real
defects and second-order products, with all moments of sqrt(beta)|1-U_p| from row 1155 (9)). The law of its
norm is the fixed-window transported-curvature comparison of row 1231 (9) applied to a signed list of temporal
faces; the open-box tree gauge and the translation average treat the time axis like the spatial ones, and
row 1231 (2) is stated for all even M >= n. Uniform integrability from |D_s| sum 2 beta a_p and the three
independent colours give E|.|^2/2 -> 3<j_s,P_ex j_s>/2. The constant is the free value: Var <j,PZ^a> = <j,Pj>.

**L344 (upper bound and Fejer limit): HOLDS.** X(gamma)psi is a unit vector in the centre-invariant matrix
space (seams off gamma), so W(gamma,s) = <X(gamma)psi, F_xy^s X(gamma)psi> <= r_xy^s. In the Fourier integral the
squared time factor over s is the Fejer kernel; for spatial k != 0 the temporal-temporal block of P_ex is
continuous at k_0 = 0 with value t t^*/|t|^2 (only a_0 couples to faces 0i when t_0 = 0); the integrand is
bounded by |gamma|^2; t^* j_gamma(k) is the transform of the path divergence delta_y - delta_x, so the limit
is R(z). R(e_1) = 1/3 by the symmetric sum of the three directional integrands.

**Verdict (25): HOLDS.** It is the free-field (Coulomb) value: (3/2)R(z) = 3[G(0) - G(z)] with
G = (-Delta_Z3)^(-1), which is beta g^2 C_F [G(0) - G(z)] at g^2 = 4/beta, C_F = 3/4.

## Step 3. The multiplicity comparison (27) (L354-L377), with (28), (21), (22)

Inputs read: row 1145 L14-L30 ((1): 0 <= I_d(s)/I_1(s) <= exp[-(d-1)/b_beta], s <= 6 beta) and L196-L222;
row 1149 L216-L222 ((16) and, in its proof, I_{j+1}(v)/I_j(v) increasing, hence normalized C_{beta/2} <= C_beta);
row 1151 (21)-(24) as in Step 2.

**(22) L272-L280: HOLDS.** The Wilson density relative to the product of independent normalized open-box
measures and Haar on the other links is at most e^{CV Delta_b}: drop the nonnegative crossing action, and
Z_W >= Z_product e^{-CV Delta_b} is the gluing lower comparison in the proof of row 1151 (22b). On a good box,
the density relative to the Gaussian of precision (1 - C_1/b) beta D_1^* D_1 is at most e^{Cb^3}: the action
is at least that quadratic form on the chart, and the normalizer ratio between precisions (1 -+ C/b) costs
(1 + O(1/b))^{O(b^4)}. The radius-replacement errors (row 1231 (8)), the Cauchy-Schwarz/AM-GM step
D sqrt(N_b) C b^(-1)||l|| <= C D b^(-1)(N_b + ||l||^2), the Gaussian concentration log moment pi^2 t^2 D^2/8 with
Lipschitz constant C D sqrt(N_b), the quadratic exponential of rank O(b^4) (log moment O(|t| b^3)), and the bad
chart (action >= c b^(-8) outside the chart by the shelling L <= Cb x action; normalizer >= e^{-Cb^4 log beta};
negligible because beta >> b^12 log beta for gamma < 1/12) all check. Per site every error is O(1/b + Delta_b)
plus C_g t^2. The mean converges to mu_g through the nested-projection coupling of row 1231 (1).

**(21) L260-L270, L282-L284: HOLDS.** For a bounded Lipschitz g the one-link kernel e^{t g(R)} x (Wilson
factor) need not be positive definite, but it is real and central, so each layer in a direction of the
plaquette is self-adjoint, and on an even side Tr|F|^n = Tr F^n in the Holder step; layers in other directions
are positive multiplications. The Rayleigh argument is as in (20), with (22) for both signs of t, then
j -> infinity, then t -> 0. Third limit: e^{uX} on the marked temporal plaquette gives the normalized
convolution at beta' = (1-u) beta = beta/(1+tau), so the marked transfer is (z_{beta'}/z_beta) Y^* L_{tau,e} Y;
truncation at X = K costs C_{u'} e^{-(u'-u)K} by domination with T_{exp(u'X)}; the limit value is
(1-u)^{3/2} E e^{u|Z|^2/4} = ((1-u)/(1-u/2))^{3/2} = (1+tau/2)^{-3/2}; V = Y U^(-1/2) is the polar partial isometry
between the two bands, with ||(U^{1/2} - 1)f|| <= 1 - h^{1/2}; monotonicity, tightness and the Laplace transform
give the Maxwell limit.

**(28) L361-L375: HOLDS.** Line by line:
- S_s(X_D) = beta(U^s - W_gamma^* F_xy^s W_gamma) is the open-line formula (row 1143 (8)) with the ribbon
  half-trace as the insertion. S_s(e^{t g_K}) is self-adjoint because time reversal maps the ribbon boundary
  holonomy to a conjugate of its inverse, which has the same half-trace.
- Schatten-Holder: with k = n/l slab operators B_i in one spatial direction and 2l | n,
  |Tr B_1...B_k| <= prod_i ||B_i||_k and ||B_i||_k^k = Tr (B_i^* B_i)^{k/2}; B_i^* is the reflected slab, so the
  trace is the Wilson integral with the source in every slab (alternately reflected) for i = 1 and the
  unperturbed one for the other slabs. Hence log(Z_src/Z_0) <= (l/n) log(Z_1/Z_0), and three directions give
  the factor (l/n)^3. This needs gamma (with all its temporal links) strictly inside one cell, as stated.
- Per-site bound for the array of density alpha = 1/(s l^3): the proof of (22) applies with windows in place
  of single faces. The shelling errors (dropped transports C|gamma| b^(-7/2) per face, real parts and
  second-order products each at most C b^(-7/2) times a scaled face chord, since every |1-U_p| <= C b^(-7/2)
  on a good box), the Lipschitz constant sqrt(2K) of the clipped half-square, and the bounded row and column
  sums of the window map give the same O(|t| b^(-1))(b^4 + ||l||^2) per good box.
- Time root: (1/m) log Tr S^m - (1/m) log Tr U^{sm} <= (l/n)^3 (1/m) n^3 s m x (per-site bound) =
  (per-site bound)/alpha, with m even so that the self-adjoint trace root gives the norm.
- Rayleigh step and clip removal: X_D <= |D_s| sum beta a_p (shelling), e^{v X_D} <= e^{sum beta a_p/2} for
  v|D_s| <= 1/2 halves the temporal couplings in D_s, so ||S_s(e^{v X_D})|| <= (z_{beta/2}/z_beta)^{s|gamma|};
  x 1_{x>K} <= (2/(v e)) e^{-vK/2} e^{vx}. Both limits (j, then t -> 0, then K -> infinity) are uniform.
- c_s = E (1/2)|<j_s, P_ex Z>|^2 = (3/2)<j_s, P_ex j_s> (three colours).

**(27) L354-L359, L377: HOLDS.** Take h_j = r_{k_j,+}; the span of the first k_j + 1 neutral eigenvectors lies
in Q_{h_j}; on it <f, U^s f> >= r_{k,+}^s and, by (28), <f, S_s(X_D) f> <= c_s + o(1). W_gamma is an isometry
(so the image has dimension k_j + 1) and F_xy >= 0, so min-max for F_xy^s gives
r_{k,xy}^s >= r_{k,+}^s - (c_s + o(1))/beta. With 1 - r_{k,+} = o(1/beta) this gives
limsup -beta log r_{k,xy} <= c_s/s for each s, then <= c by L344; the reverse bound is r_{k,xy} <= r_xy and (24).
The statement covers every index at bounded physical energy because 1 - r_{k,+} <= aE and a beta -> 0 on
beta <= B log n; no bound on the number of indices is used, since (28) is uniform on the band.

What (27) does not say: it fixes the k-th charged level only at resolution o(1/beta) in lattice energy; it
gives no information at the physical resolution a = o(1/beta).

## Step 4. The physical-energy estimate (33) (L448-L452), with (29)-(32), and (34)-(35)

**(29) L381-L398: HOLDS.** With a basis i, j, k: -a q a = q for a parallel to the vector part, -q_vec for a
perpendicular, and q_0 for the scalar part, so sum_a (-a) m a = 3 m_0 - m_1 on the complexified quaternions.
Then sum_a <am, ma> = 3||m_0||^2 - ||m_1||^2, and the Bessel bound of (23) becomes
beta^(-1)[3R||m||^2 + 8 G_xy ||m_1||^2] <= 1 - ||m||^2 (diagonal 3(G_xx+G_yy)||m||^2, cross term
-6G_xy||m_0||^2 + 2G_xy||m_1||^2). With r_A = int Re<a,m> d omega and 2(1 - Re<a,m>) = ||a-m||^2 + 1 - ||m||^2,
beta(1 - r_A) = beta(1 - omega(all)) + (1/2) int beta||a-m||^2 d omega + (1/2) int beta(1-||m||^2) d omega, all three
terms nonnegative. The middle term and int(1-||m||^2) d omega = O(1/beta) let ||m_1|| be replaced by ||Pi_1 a(X)||;
||(I-U)f||^2 <= <f,(I-U)f> = O(1/beta) replaces the X-marginal f(Uf) by f^2. ||m_1|| = ||Pi_1(X) m|| is frame
invariant. For the passage from G_B to G(z): use -4G||Pi_1 A||^2 >= -4G_B||Pi_1 A||^2 - 4(G - G_B), then B up.
The triplet excess 4G(z)/beta is the free value: the one-gluon coefficient of G(z) is -C_F = -3/4 in the
singlet channel and C_A/2 - C_F = +1/4 in the adjoint (triplet) channel, a difference of 1, so
beta(V_triplet - V_singlet) = beta g^2 G(z) = 4G(z). (29) is a lower bound only, as stated.

**(30) L400-L409: HOLDS.** For r > ||D||, F_xy - r is congruent (block LDL^T with bounded invertible factors) to
diag(H(r) - r, D - r); D - r < 0, so Sylvester's inertia law gives the count identity; letting r' decrease to
r_xy in #{lambda(H(r')) > r'} = 0 gives H(r_xy) <= r_xy, once r_xy > ||D||, which (25) and (29) give since
beta(r_xy - ||D||) >= 4G(z) - o(1). ||B_1|| <= C_gamma/sqrt(beta): the fibre component perpendicular to X(gamma) of
g_x Y(gamma) g_y^(-1) has norm at most |1 - U_dD1| (one-step ribbon chord) <= sum_{p in D_1} sqrt(2 a_p), and
sqrt(2X_p) <= C e^{X_p/2}, ||T_{e^{X_p/2}}|| <= C.

**(31) L411-L425: HOLDS.** I redid the expansion: Q W^*F^s W Q = Q A^s Q + sum over one-excursion words
+ O_s(beta^(-2)) (two excursions carry four factors B_1 or B_1^*); Q A^s Q = Q U^s Q - (s/beta) Q S_1 Q + o(1/beta);
each one-excursion word is Q B_1^* D^l B_1 Q + o(1/beta), with s-1-l positions; (28) at times 1 and s gives
beta sum_{l<=s-2} (s-1-l) Q B_1^* D^l B_1 Q = (s c_1 - c_s) Q + o(1). With T_s the left side, T_{l+2} - 2T_{l+1} + T_l
is the l-th term, so the second difference gives (31) with c_0 = 0. d_l >= 0 makes c_s concave; with c_s/s -> c
the increments decrease to c, and sum_{l<=N} d_l = c_1 - (c_{N+2} - c_{N+1}) -> c_1 - c. Nearest neighbour,
checked independently from the free field: c_s = (3/2)[s/2 - sum_{u != u'} b(|u-u'|)] because the temporal
plaquette column has <p_0, P_ex p_t> = -b(t) for t >= 1 (Hodge complement: (I - P_ex) on (01) has the symbol of
P_ex on (23)), so d_l = 3 b(l+1) > 0; sum_{t in Z} b(t) = 2/3 (symbol at k_0 = 0) and b(0) = 1/2 give
sum_{t>=1} b(t) = 1/12, so sum d_l = 1/4 = c_1 - c = 3/4 - 1/2.

**(32) L427-L444: HOLDS.** Upper: H(r) <= r gives Q B_1^*(r-D)^(-1) B_1 Q <= Q(r - A)Q =
[(c_1 - c)Q + o(1)]/beta (A = U - S_1(X_D)/beta, (25), (28) at s = 1, beta(1 - h_j) -> 0). Lower: the first K
terms of the Neumann series, by (31) and r -> 1. Tail: the positive remainder after K terms is at most
sum_{l>=K} d_l + o(1) in norm. The scalar inequality 1/(r-x) <= K/r + (x/r)^K/(r - ||D||) for 0 <= x <= ||D|| < r
(split the geometric series at K) gives (r-x)^(-2) <= (K/r)(r-x)^(-1) + (r-||D||)^(-1)(x/r)^K (r-x)^(-1), hence
||(r-D)^(-1) B_1 Q||^2 <= O(K/beta) + (beta/c_z)(sum_{l>=K} d_l + o(1))/beta -> 0 after K -> infinity.

**(33) L448-L452: HOLDS.** r - ||D|| >= c_z/beta and a_j E_0 = o(1/beta) keep r - aE in the resolvent set; the
resolvent identity gives Q[H(r - aE) - H(r)]Q = aE [(r-aE-D)^(-1) B_1 Q]^* [(r-D)^(-1) B_1 Q], and functional
calculus gives ||(r-aE-D)^(-1) B_1 Q|| <= (1 - a E_0 beta/c_z)^(-1) ||(r-D)^(-1) B_1 Q||. Divided by a, the norm is
at most E_0 (1 + o(1)) ||(r-D)^(-1) B_1 Q||^2 -> 0 by (32).

**(34) L454-L458: HOLDS.** (r - 1) + Q S_1 Q/beta - Q B_1^*(r-D)^(-1) B_1 Q = (-c + c_1 - (c_1 - c) + o(1))/beta.

**(35) L460-L471: HOLDS.** M_2(C) is the complexified quaternions and the SU(2) colour actions preserve the
real form, so the top eigenspace contains a real A_*; zeta_* is real and symmetric (self-adjoint F_xy, real
values); its marginal is r||A_*||^2 by the eigenvalue equation; expanding the square gives (35). The last
claim follows from the three-term decomposition in (29) at A = A_*: beta(1 - r) -> c and the third term is at
least c - o(1), so beta(1 - <f, Uf>) -> 0.

What (33) does not say: it controls only the dependence of the effective neutral operator on the spectral
parameter across a physical window. It gives no bound on the spectrum of H(r) itself; (34) compares rI - H(r)
with I - U only to o(1/beta), not to o(a). The checked file states this (L458, L473).

## Step 5. Everything else, in file order

**L19-L24 (setup): HOLDS.** The MCM kernel M(X) prod_e rho(X_e Y_e^(-1)) M(Y) is smooth and strictly positive; the
Perron eigenvector is unique and positive, hence invariant under vertex gauges and centre flips, which
commute with the kernel. The centre-neutral vacuum lies in the singlet space.

**L26 (||F_x|| <= q): HOLDS.** For equivariant v, F_x v(X) = int k_0(X,Y) E_{g|X,Y}[Ad(g_x)] v(Y) dY. Given X, Y
and the other temporal links, g_x has the translated density of row 1145 L16 with tilt s <= 6 beta (six edges
at x), and its adjoint mean is the multiplier I_3(s)/I_1(s) times a rotation, so its norm is at most
exp(-2/b_beta) = q by row 1145 (1). Hence |F_x v| <= q F|v| pointwise, and iteration holds by positivity.

**(1) L28-L38: HOLDS.** C commutes with left translation on link e because rho is central:
C_e(u o L_a) = (C_e u) o L_a. D_e M = -(1/2) J_e M and multiplication operators
commute, so D_e(F phi) = F_x D_e phi - (1/2){J_e F phi + F_x(J_e phi)}; with F phi = r phi this is
(r - F_x) D_e phi = -(1/2)(r + F_x) J_e phi. (1/2)(r+F)(r-F)^(-1) = 1/2 + F(r-F)^(-1) = 1/2 + sum_{s>=1} r^(-s) F^s.
D_e phi is an adjoint vector at the base x (derivative at gX in direction a is the derivative at X in
direction Ad(g_x^(-1)) a).

**(2) L40-L46: HOLDS.** Haar integration by parts of D^a[(D^a S) conj(phi_i) phi_j] and (1) give (2).
sum_a (D^a)^2 w(X_p) = w(sum_a a^2 X_p) = -3 w(X_p), four spatial plaquettes per link in 3D, |B_e| <= 12 beta;
F_x >= 0 gives K_r >= I/2 and ||J_e phi||^2 <= <phi, B_e phi> <= 12 beta.

**(3) L50-L62: HOLDS.** (D_e + J_e/2)F = M (D_e C) M / lambda_0; the kernel derivative has length
beta|Im(X_e Y_e^(-1))| = beta sqrt(1-w^2) <= beta sqrt(2A); beta sqrt(2A) e^{-beta A} <= C sqrt(beta) e^{-beta A/2};
the halved-coupling factor is (z_{beta/2}/z_beta) times a normalized convolution below C_beta in operator
order (row 1149 (16) proof, L222). The identity ||J_e u||^2 = <u, B_e u> + 2 Re<(D_e + J_e/2)u, J_e u> follows
from <u, B_e u> = -2 Re<J_e u, D_e u> (integration by parts of (D^a S)|u|^2). The quadratic inequality and
f = F(F^(-1) f) on the band give the rest.

**(4) L64-L69: HOLDS.** (D_e + J_e/2) phi = -F_x (r - F_x)^(-1) J_e phi from (1); on [r-d, r] with d <= r/2,
lambda/(r - lambda) >= (r-d)/d >= r/(2d); (3) applied to phi = F phi / r gives ||(D_e + J_e/2) phi|| <= C sqrt(beta)/r.

**(5) L73-L87: HOLDS.** I redid the induction: D_e U^{m+1} = F_x D_e U^m - (1/2) J_e U^{m+1} - (1/2) F_x J_e U^m
turns the formula for m into the formula for m+1. Integration by parts of v^a conj(U^m h) U^m k gives
U^m G U^m = -(D_e U^m)^* V U^m - (V U^m)^* D_e U^m; the two half terms give U^m (v.J_e) U^m and the endpoint
term is E_{e,R} with m - 1 = R. For v = J_e the bound C' beta q^R is right because ||J_e U^m|| <= ||J_e F|| <= C sqrt(beta)
by (3) (not only |J_e| <= 4 beta).

**L89: HOLDS.** sum_a (D^a)^2 w = -3w gives G = f for v = -D_e f/3, |D_e w(X_p)| = |Im X_p| <= 1. With
a = i sigma_a, sum_a a (x) a = -sum sigma (x) sigma = I - 2 Swap, which is -I on symmetric tensors, so the Casimir
on spin l (d = 2l factors) is -3d - d(d-1) = -4l(l+1). The density argument holds.

**L91: HOLDS** (GUIDE-level for the cited account lines RF24-RF25, which I did not re-read; the claim
beta = O(log(1/a)) is the usual asymptotic-freedom growth). q^R = e^{-2R/b} <= n^(-2(k+c)) for
R = ceil((k+c) b log n), and a(R+1) = O(L (log n)^2 / n) -> 0.

**(6) L99-L104: HOLDS.** W_e^* F_xy W_e inserts w(X_e^(-1) g_x Y_e g_y^(-1)), the temporal plaquette half-trace,
into the electric factor of e. Since d/d beta of z_beta^(-1) e^{-beta(1-w)} is (w - p_beta) times itself,
w rho_beta = p_beta rho_beta + d rho_beta/d beta, whose multiplier is c_d (p_beta + H_beta(d)) with
c'_d >= 0; min-max through the isometry W_e gives the eigenvalue comparison.

**(7) L106-L111: HOLDS.** U = Y^* Y and the modified product is Y^*(p_beta + H_beta(d_e)) Y; F~ Y = Y U.

**(8) L113-L124: HOLDS** as an implication from the method of row 1151 (23) and the half-coupling moment of
row 1155 (both checked). Truncated kernel sum_{d<=D} d c_d chi_d has modulus at most sum d^2 = (z_beta sum d^2) x
z_beta^(-1) e^{-beta a_p} x e^{beta a_p}; positivity of Tr(P_D F~^2 P_D)^j justifies the bound by the absolute
integrand; j-th roots and F~^2 >= h^2 1_{[h,1]}(F~) give (8). Precision note (P1): the marks here are temporal
plaquettes over one link on alternate cuts, with exponent beta, not the spatial classes with exponent
(1+delta_0) beta of row 1151 (23). The adaptation works: after dissemination the marked faces have coupling 0,
each has the five-face cube detour into the next layer of the perpendicular coordinate, whose five other faces
are unmarked, so the disseminated action is at least 1/21 (hence at least 1/42) of the original. The file
states this adaptation in words at L124; it is not a restatement of (23).

**(9)-(10) L126-L136: HOLDS.** z_beta of order beta^(-3/2) and sum_{d<=D} d^2 ~ k_0^3 beta^{3/2}/3 make (8) at
h = 1/2 at most 1/2 for small k_0. H_beta(d+1) - H_beta(d) = d/d beta log(I_{d+1}/I_d) > 0 (row 1149 L222).
Limits (10), redone: E[sin(k|Z|)/(k|Z|)] = E e^{ik Z_1} = e^{-k^2/2}; beta(w - p_beta) -> (3 - |Z|^2)/2 and
E[(3 - |Z|^2)/2 e^{ikZ_1}] = (k^2/2) e^{-k^2/2}, using E[|Z|^2 e^{ikZ_1}] = (3 - k^2) e^{-k^2/2}. So beta H_beta(D+1)
-> k_0^2/2 and epsilon = k_0^2/8 works.

**L138: HOLDS** (min-max; the last two sentences are conditional on row 1163 (13), as labelled).

**(11) L142-L158 and L160: HOLDS.** The endpoint q^{m-1} h^(-m) -> 0 because h >= (1+q)/2 > q. The instantaneous
force cancels: -(1/2) J_e f + (1/2) rho J_e psi = 0. ||U^(-s) f - f||^2 <= h^(-2s) s^2 delta D(f) by r^(-s) - 1 <= h^(-s) s(1-r)
and (1-r)^2 <= delta(1-r). The colour kernel of F_x^s has norm at most q^s k_s pointwise; the Doob kernel
P_s = k_s psi(Y)/psi(X) is nu-stationary and int int |rho(Y) - rho(X)|^2 nu P_s = 2<f,(I-U^s)f> <= 2s D(f). Both sums
are O((1-q)^(-3/2)). L160: 1 - q ~ 2/(1+6 beta), so beta^2(1-q)^(-3) <= C(1+beta)^5, and D(f) <= aE.

**(12)-(14) L166-L187: HOLDS.** The insertion L_{tau,e} turns C_beta into C_{beta'} on the link, and
z_{beta'}^(-1) e^{-beta'(1-w)} = (z_beta/z_{beta'}) rho_beta e^{u R^2/2} with beta - beta' = beta u. The Gaussian
moment is det(I - Gamma diag(u))^(-3/2); times prod (1+tau_i)^(-3/2) it equals det[I + (I - Gamma) diag(tau)]^(-3/2)
because u_i(1+tau_i) = tau_i. L_{tau,e}(d) -> e^{-tau k^2/2} from (10) at beta and beta'. Tightness, analytic
continuation of the Laplace transform and Stone-Weierstrass hold. The one-link density with covariance I/2
is 4k^2 e^{-k^2}/sqrt(pi).

**(15) L189-L193: HOLDS.** P_ex F = t ^ (iota_{conj t} F)/|t|^2 gives the (0i),(0j) block
(|t_0|^2 I + t t^*)/(|t_0|^2 + s); the k_0 integral of 1/(s + 2 - 2cos k_0) is 1/(2 sinh omega) with
sinh(omega/2) = sqrt(s)/2; t^*(sI - t t^*) = 0.

**(16) L195-L204: HOLDS.** Two cuts: det [[1+tau/2, tau b],[tau b, 1+tau/2]] minus the product of single values.
b(s) is the (23)-(23) free covariance at time distance s (Hodge complement), b(s) ~ 1/(pi^2 s^4) (row 1231 (5),
redone: (1/(2 pi^2))(1/3)(6/s^4)). C_tau(s) ~ (3/2) tau^2 b^2 (1+tau/2)^(-5). The weight statement follows from
r^s >= e^{-s/u_j} on the band and positivity of the spectral measure.

**(17) L210-L224: HOLDS** (redone in Step 2 with (20)): with t = c epsilon and C beta^(-eta) <= epsilon/4, both tails are
at most h^(-1/2) exp(-c' N epsilon^2).

**(18)-(19) L228-L239: HOLDS**, (19) conditional on row 1163 (13)-(14) as labelled. Temporal insertions are exact
(U - W_e^* F_xy W_e); spatial ones carry (5) with error 2C sqrt(beta) q^R ||V U^m||, ||v||_inf <= 1/3. In (19),
||v_R - U^m v|| <= 2||A_R - U^m A U^m||, H commutes with the transfer, U >= e^{-a E_*} on ran Q, and
||QHv||^2 >= int_{E<=E_*} e^{-u_2 a E} d mu >= 15 G/16.

**L241 (ARGUED): consistent** with (18)-(19); it is labelled ARGUED and claims no estimate.

**L258: HOLDS.** Restatement of (20) in Rayleigh-quotient words; the remark on time order n is correct
(n beta^(-1)(sqrt(delta) + beta^(-eta)) does not tend to 0).

**L346-L350 (cost of projecting after every step): HOLDS.** Vacuum trial and (20) at delta = 0 give the lower
bound; for the optimizer, <f,Uf> >= 1 - O(1/beta) because ||T_X|| <= C (T_X need not be positive, but its norm
is bounded), the band split and (20) give <f, T_X f> = 3/4 + o(1). Against (25) at a nearest neighbour (1/2),
the projected chain loses (1/4 + o(1))/beta per step.

**GUIDE and OPEN paragraphs (L3-L15, L93, L97, L164, L208, L288, L473):** context and credits; I did not re-read
the external links (Sussman-Alpoge lines, row 1218 papers). L15 and L473 agree with row 1231 L14 (OPEN).

Precision notes (none breaks a statement):
- (P1) L124: adaptation of row 1151 (23) to temporal alternate-cut marks at exponent beta (above).
- (P2) L99, L104, L117: "row 1149, (16)" points to the statement (16); the Bessel-ratio monotonicity it uses is
  in the proof paragraph of (16) (row 1149 L222), not in the display.
- (P3) L278: the factor e^{Cb^3} checks (normalizer ratio between precisions 1 -+ C/b over rank O(b^4)); any
  further e^{O(b^3 log beta)} from fixed boundary variables would still be o(1) per site. No consequence.

## Step 6. Is the main comparison a restatement of an earlier row?

The main comparison of row 1236 is the neutral sector against the sector of two fundamental static charges:
the operator inequality (6)/(9) through the open-line isometry, the sharp threshold (25), the multiplicity
transfer (27), and the Schur (Feshbach) reduction (30)-(34). **Answer: it is not a restatement.** It extends
earlier rows, which it cites and uses:

- Row 1143 (8) (L128-L139 there): the open-line formula, with Jensen W(k) >= W(1)^k and W(N) <= 4<P_x P_y>. Rows
  1147 (`gap-solve6-astra62.md` L35) and 1171 (`gap-solve14-astra62.md` L64-L68) use the same moment formula to bound
  Wilson-loop deficits 1 - Ew <= Chk/beta. None states an operator inequality or an eigenvalue comparison between
  the two sectors; (6) is new, and the upper half of (25) uses (8) in the other direction (W <= r_xy^s).
- Row 1145 (16)-(18): every local gauge charge costs at least w/(7 b_beta) per step. For a fundamental pair
  (w = 2) this is -beta log r_xy >= about 1/21 at large beta. (24) sharpens the constant to the exact limit
  (3/2)R(z) (1/2 at a nearest neighbour), for this pair only; (25) adds the matching upper bound.
- Row 1151 (21)-(22a): the mean plaquette 3/4 in the vacuum by dissemination and the pressure slope. (20) is its
  extension from the vacuum to every vector of the slow band; (28) is the ribbon version.
- Row 1231 (2), (9): the fixed-window transported-curvature comparison. (26) is its version for a ribbon of
  temporal faces.

Searches (grep counts at `3a45c201f`): `library/open-core.md` has 0 hits for "static potential", "static pair",
"static-pair", "Coulomb", "resistance", "Feshbach", "Schur", "open-line", "triplet", "self-energy",
"Wilson ribbon", "charged threshold". In FINISH.md, "static-pair" hits only rows 1236 and 1245; "Coulomb" (42
hits) is the U(1) Coulomb-phase binding test of rows 708-931, not a static potential; "Feshbach" has 0 hits.
In `library/`, "static potential" appears only as a literature pointer (Bachas, Borgs-Seiler concavity:
`gap-measured-vectors-max.md` L131, `gap-solve-astra62.md` L119); "Wilson ribbon" in row 1211
(`gap-solve22-astra62.md` L13) is a different object (a connected ribbon of spatial links with the exterior
fixed); no `gap-solve*-astra62.md` file has a Schur or Feshbach reduction of a charged transfer (its "Schur"
hits are Schur tests and Gaussian Schur complements). The Sussman-Alpoge index (`library/sa-index/`) has no hit
for "static potential", "static charge", "Polyakov" or "heavy quark"; its "Coulomb" lines (chunk-10 L65, L118)
are Green-kernel bounds. So there is nothing to port from the outline here.

The constants are the textbook leading-order ones (Coulomb static energy g^2 C_F [G(0) - G(z)] with self-energy,
adjoint-channel excess g^2 G(z), mean plaquette 3/(4 beta) for SU(2)); what is new in the lane is the proof on
growing tori at beta <= B log n, uniform over the slow band.

## Step 7. Numeric guide (GUIDE only; no statement of the chain rests on it)

Run 09:27-09:28Z under `lab_ops.py numeric-lock` (holder gap-solve27-check-opus, acquired and released;
memory 54 percent free by `memory_pressure`; BLAS threads 1, `nice`, `python3 -I`, peak RSS 522 MB). Script and
output in the scratch folder /tmp/gs27chk (`guide.py`, `guide.out`), not committed.

| Quantity | Claimed | Computed |
|---|---|---|
| c_d(beta) = I_d/I_1 at d = k sqrt(beta), (10) | e^{-k^2/2} | k = 0.5, 1, 2 at beta = 25600: 0.882512, 0.606538, 0.135336 against 0.882497, 0.606531, 0.135335 |
| beta H_beta(d), (10) | k^2/2 | 0.124985, 0.499995, 1.999980 against 0.125, 0.5, 2 |
| beta(1 - p_beta), L136 | 3/2 | 1.4962, 1.4996, 1.49996 at beta = 100, 1000, 10000 |
| H_beta(d) nondecreasing in d, L131 | yes | yes at beta = 400, d = 1..79 |
| b(0) = diagonal of I - P_ex on a temporal face | 1/2 | 0.500000 |
| sum_{t>=1} b(t); 3 x sum = c_1 - c (L425) | 1/12; 1/4 | 0.083333; 0.250000 |
| R(e_1), (25) | 1/3 | 0.333333 |
| pi^2 s^4 b(s), (16) | -> 1 | 0.68, 1.76, 1.53, 1.09, 1.02, 1.006 at s = 1, 2, 4, 8, 16, 32 |
| c_1, c_s/s, d_l >= 0 (nearest-neighbour column) | 3/4, -> 1/2, yes | 0.750000, c_40/40 = 0.5077, min d_l = 1.5e-7 > 0 |
| 4G(e_1) in (29) | > 0 | 0.341 on a 160^3 midpoint grid (G(0) = 0.2519 there; the exact Watson value is 0.2527, so 4G(e_1) = 4(G(0) - 1/6) = 0.344) |

So at a nearest neighbour: c = 1/2 (true static pair), c_1 = 3/4 (projected one step), triplet threshold at
least c + 4G(e_1) = 0.844 in units 1/beta.
