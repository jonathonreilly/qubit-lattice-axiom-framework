# Check of gap-solve8-astra62.md (FINISH row 1160)

Status: complete. This file was written as the check went.

File under check: `library/gap-solve8-astra62.md` (row 1157 output).
Builds on: `library/gap-solve6-astra62.md`, `library/gap-solve7-astra62.md`
and their checks `library/gap-solve6-check-opus.md`,
`library/gap-solve7-check-opus.md`. Setting: `library/gap-council-brief.md`.

Checker: Claude Opus 5.5, max reasoning, laptop subagent. Cross-provider
check of row 1157's output (the astra file). Started 2026-11-19.

## Plan (at most eight steps)

1. Read the setting and the file under check in full, in ranges.
2. Read the cited parts of solve6, solve7 and their two checks.
3. Check the one-period unconditioned adjoint test (25) with (18).
4. Check the twist-ratio control (23) and the seed consequence (24).
5. Check the charged comparison (1) and its seven exceptional levels.
6. Check the obstructions (14), (27)-(30) and (33).
7. Check the two-photon comparison; run numeric guides (guide only).
8. Verdict table and the RESULT line.

## Step 1. Reading (done)

I read `gap-council-brief.md` (122 lines) and all 551 lines of the file
under check, in four ranges. Line numbers below refer to the file under
check unless a file is named. The file's own status lines say it has no
independent review and used no numerical run (L549).

## Step 2. Cited sources (done)

Read, in the parts the file uses:

- Row 1155 (`gap-solve7-astra62.md`): (9) (L130-134), (10)-(12)
  (L150-168), (14)-(15) (L199-214), (27)-(35) (L386-528). Its check,
  row 1156 (`gap-solve7-check-opus.md`), finds that every statement HOLDS,
  including (9), (10), (15), (27), (29), (30), (34) and (35). So the file's
  remark at L13 that row 1155 is unchecked is out of date.
- `gap-seed-shape.md` 1.1-1.5: (T), Lemma E2, Proposition B3, Theorem SH,
  and the threshold lines r = 2 (two stages, 1/1650) and r = 4 (1/25,
  K = 22.2). Checked once (row 707 lead note).
- `gap-phys-seed.md` (row 720): Theorem ZD-c, (PHYS-SEED) with the
  threshold 1/1650 by the two-stage line.
- `gap-flux-exercise.md` C2 and `gap-flux-exercise-check.md` Section 5:
  (S2), Z^k <= Z^0 for all 64 twists. HOLDS there.
- Row 1145 (`gap-solve2-astra62.md`) (1) and (4): the Bessel-ratio
  barrier and the straight-winding overlap bound.
- `gap-channel-astra.md` (33): the free two-photon state of energy
  4 pi/a. `gap-glue-check-astra.md` Section 5: SEP HOLDS AFTER CORRECTION
  (scope: two finite-box non-implications in the abstract class).
- Row 1153 (`gap-solve6-astra62.md`) and its check (row 1154) are not
  cited by the file under check (no occurrence of "1153" or "solve6"), so
  I read only their section headings. Row 1155's uses of row 1153 were
  checked in row 1156.

Notation used below is the file's: U = F/||F||, T = n/2, Z_chi(v) =
Tr(P_chi U^v), Z_+ the neutral one, p_chi(T) = Z_chi(T)/Tr U^T,
theta_b = Z_b / sum_c Z_c, purity A_t = Tr U^{2T}/(Tr U^T)^2. The basic
fact used again and again: A_t <= 1/Tr U^T = 1/(1 + S(T)), since the
purity of a density matrix is at most its top eigenvalue.

## Step 3. The one-period unconditioned test (25) with (18) (done)

The proof of (25) uses (5), (6), (7), (10), (11), (17)-(20), (23), (24) and
(26). I checked each link by hand. (23) and (24) are in Step 4.

S3.1 Input tilted bound (L100-102). HOLDS. It is row 1155's unnormalized
tilted estimate (row 1155 L420, checked HOLDS in row 1156). The extra
details are right: the normalized one-link multipliers are
I_d(b)/I_1(b) = product of I_{k+1}/I_k, each factor increasing in b by
row 1145 (1), so halving the coupling lowers the layer in operator order;
z_{beta/2}/z_beta is bounded since z_b ~ c b^{-3/2}; Schatten Hoelder over
the layers removes the unitary seam; ordinary Hoelder over the six
orientations; Markov on 1 - w^b >= 1; and sum_b Z_b/Z_0 >= 1.

S3.2 (5) (L104-110). HOLDS. The true twisted negative set is feasible
and has the true periods relative to D. A wrong bit gives a closed
component C of D' + D_0 with a nonzero period; it meets all n disjoint
parallel (i,time)-tori, so |C| >= n. Minimality gives |C cap D'| <= |C|/2,
so at least |C|/2 faces of C are truly negative. 2^k half-sets, the tilted
bound and C n^3 C_1^k rooted connected sets give the sum over k >= n.

S3.3 (6) (L112-116). HOLDS. On the slab T_i x T_time x I, a closed
cochain has the same period on each of the w parallel tori (the slab
between two of them is a 3-chain whose boundary is their sum). So a wrong
bit costs at least w faces. With w = ceil(A(1 + log n/beta)),
beta w >= A log n, which gives any inverse power.

S3.4 (7) and its proof (L121-133). HOLDS. Decoders are separate channels,
so the affinity can only grow. A diagonal pair (c,c) with law q has
rectangle affinity sum q^2 (all four labels must agree). Plancherel on the
two bits gives sum q^2 = (1/4) sum_{chi_j = 0} (p_chi/p_+)^2, using
sum_b chi(b) theta_b = p_chi/p_+ (row 1155 (30)). Then p_chi >= 0,
sum_chi p_chi = 1 and A_t <= 1/Tr U^T <= p_+ give the second bound.
At A_t > 1650/1651, (1-A_t)/A_t < 1/1650, so the bound
(1 + 1650^{-2})/4 is right. L135 (Fourier coefficients bounded by
(1-A_t)/A_t) HOLDS for the same reason.

S3.5 (10), lower bound (L184-191). HOLDS, and it is exact. I rederived the
tilt. With the stationary-segment density psi(x_0) psi(x_h) prod K_1 and
the mixed density (1/(8 Z_+(T))) sum_b [...] K_d(x',y) K_d(y', b x), the
ratio is p_d(x',y) q_d(y',x)/Z_+(T), since psi is flip invariant. A flip of
the whole second segment keeps the reference and the adjoint data, and
q_d(b y', x) = q_d(y', x); averaging gives q_d(x',y) q_d(y',x)/Z_+(T).
q_d is symmetric (p_d symmetric, b an involution), so after pairing with
reversibility the affinity is Z_+(T)^{-1/2} <v,(P^h x P^h) v>, and P >= 0
(positive sandwich) gives >= Z_+(T)^{-1/2} (int v)^2. q_d is the pi-kernel
of P_+ P^d, so int q_d^2 = Tr(P_+ U^{2d}) = Z_+(2d). Hoelder with exponents
3/2 and 3 gives int sqrt(q_d) >= Z_+(2d)^{-1/2}. Data processing (product
reference stays a product), the two-unit-vector test and
A >= sigma_max^4 give A_obs >= Z_+(T)^{-2} Z_+(2d)^{-4}.

S3.6 (10), upper bound (L180-182). HOLDS, given row 1155 (27) in the mixed
cylinder (row 1155 L517, checked HOLDS). The switching sketch at L180 is
row 1155's argument; in the mixture each seam can be moved out of the
collar by a flat flip, which does not change adjoint data, and the
involution keeps the product of the two path weights. The quotient pair
density k_{T/2}^2/Z_+(T), its square-root operator P_+ U^{T/2}/Z_+(T)^{1/2}
on H_+, and affinity Z_+(2T)/Z_+(T)^2 <= 1/Z_+(T) are right. Channels
increase the affinity, so A_obs <= 1/Z_+(T) + 4 (TV)^{1/2}; this is why
the recovery error is taken O(n^{-2k}). Then 1/Z_+(T) = 8 theta_0/Tr U^T,
|u - theta_0| = O(n^{-k}) by (6) and theta_0 >= 1/8 give the right side.

S3.7 (11) (L193-197). HOLDS. Sufficiency: by (10), liminf A_obs/(8u) >
1650/1651 gives limsup S(T; n^3) < 1/1650 at T = n/2, which is
(PHYS-SEED) at ratio 2 (row 720 Theorem ZD-c, two-stage line). Necessity:
the two-stage line of `gap-seed-shape.md` 1.5 gives S(a; (4a)^3) <= 0.0396
< 1/25, and the r = 4 line (j,p,q) = (2,2,3), K = 22.2 drives
limsup_j S(n/4; n^3) to zero on further dyadic sides, uniformly in j.
With h = floor(n/8), 2d >= n/4, so Z_+(T), Z_+(2d) <= 1 + S(n/4) -> 1, the
lower bound of (10) tends to one, and 8u <= Tr U^T + o(1) -> 1.
Note (not a correction): "fixed admissible L" must mean a size in the
dyadic set P of Theorem ZD-c; the file's L9 definition (4 | n) and L397
(8 | n on enlarged sides) are consistent with that.

S3.8 Localization (L261-266). HOLDS. Each marked face has a witness with
1 - w^b >= 1 - a within distance one (a face with alpha < a is its own
witness; a cube with d xi = 1 has a negative face). Witness multiplicity
is bounded, the tilted bound at threshold 1 - a applies, and the rooted
connected-set sums give R, then D_1, then B, all independent of n.

S3.9 Split into zeta and eta, and the six-face bound (L268-274). HOLDS.
Components of xi cannot share a cube, so a component missing every mark is
closed and a bounded one is exact. The six-face argument is right: the
projection to the ij-plane of a bounded dual 2-cycle is a finite 2-cycle
in Z^2, hence zero, so a second disjoint parallel face exists; each of the
four edges of the first face needs another face, and no other unit square
contains two edges of one square. Erasing a clean component is an
injection with weight ratio z_gamma <= e^{-2 a beta |gamma|} <= e^{-12 a
beta}. The slope numbers are right: one-loop SU(2) gives
c_0/log L_block = 11/(3 pi^2) = 0.3715 (I rederived it from
beta_0 = 11 N/(48 pi^2) and beta_W = 4/g^2), which is > 1/3 since
pi^2 < 11.

S3.10 (17) (L277-290). HOLDS. Mark components are more than D_1 - 2R > 2
face steps apart, so the lists D_C are independent; distinct choices in
one list differ by a closed cochain in a box shorter than the periods,
hence exact, so b(v) is well defined. The count of sign preimages is
|ker d| for every allowed xi. Conditioning away an event of mass eps moves
the law by at most eps in TV. Bounded-range form: a mark determines its
region inside a fixed ball, and a mark-bound violation has a local
certificate.

S3.11 (18) and the bounded-range correction (L292-311). HOLDS.
Z(L)/Z(L - i) = 1 + r_i with 0 <= r_i <= z by monotonicity of the
hard-core sum; telescoping over the neighbours gives
r_i = z_i prod (1 + r_j(L_j))^{-1}; each partial derivative is at most z on
the nonnegative cube, so depth-l truncation errs by at most z (D_R z)^l;
log(1+x) is 1-Lipschitz on x >= 0; at most C_R n^4 terms. With
z = e^{-2 a beta} <= n^{-2 a kappa}, l with 2 a kappa (l+1) > k + 4 gives
O(n^{-k}). Averaging over random priorities keeps (18) since it holds for
every order. The split L(z(zeta)) = L_0 + sum_C L_C is exact once no
radius-d_* ball meets two regions, which D_1 > 4(d_* + R + 3) ensures.
The factors e^{+-2 eps_n} after normalization are right.

S3.12 The all-twist mixture, Q and (19) (L316-327). HOLDS. (19): in frame
i, summing e_i inserts 2 P_+ for the flip C_4; the involutions for m_ij,
m_ik commute with it and with the positive static transfer, so dropping
them can only raise the trace; repeating in frame j removes m_jk. So
H_m <= H_0, hence H_0 >= (sum H)/8, and (S2) gives Z_00 >= (sum Z)/64.
The 64-twist tilted bound (L325): reduce the marked couplings in a frame
containing the face orientation, Hoelder removes the electric seam, the
result is C^k Z_{m',0} <= C^k Z_00 by (S2), and the mixture's mass is at
least Z_00. Q: summing over all 64 twists removes the class constraint
(each xi with d xi = M comes from exactly one class, |ker d| sign
cochains). Conditioning: ||P(.|E) - Q(.|E)||_TV <= 2 delta/P(E).

S3.13 (20) (L329-336). HOLDS. Given m = 0 the all-twist law is the
temporal-twist mixture, so A_Q(.|m=0) = A_obs + O(n^{-k}) by the
4 eps^{1/2} continuity, and Q(m=0,e=0)/Q(m=0) = theta_0 + O(n^{-k}) =
u + O(n^{-k}), with both bounded below by 1/8 - o(1) by (19). So (20)'s
quantity equals (11)'s up to o(1).

S3.14 (26) (L409-413). HOLDS. With the label adjoined, the square-root
operator is the direct sum of sqrt(p_m) K_m, so its fourth trace is
sum p_m^2 A_m. Appending a deterministic estimate m(x) is injective, so
the affinity is unchanged; replacing the estimates by the true label costs
TV <= 2 C n^3 e^{-c beta n}, hence o(1) by continuity.

S3.15 (25) sufficiency (L415-419). HOLDS. With r = 256 delta and
min f >= 1 - r from (23): p_m = H_m / sum H <= 8 Z_00/(64 (1-r) Z_00) =
1/(8(1-r)) <= 1/8 + r/4 for r <= 1/2. Since A_m <= 1,
p_0^2 (1 - A_0) <= sum p_m^2 - A + o(1) <= |A - 1/8| + r/4 + o(1), and
p_0 >= 1/8 gives 1 - A_0 <= 64|A - 1/8| + 16 r + o(1). The (20) factor
is (1/8) sum_e f(0,e) in [1-r, 1], so the product falls below one by at
most 64|A - 1/8| + 17 r + o(1). delta >= 0 since p_i(0) >= p_i(c) by
(19) in each frame, so delta = (8 s_perp - 1)_+ + o(1); 17 x 256 = 4352.

S3.16 (25) necessity (L421). HOLDS, given (24) and L397 (Step 4). In the
law given m, the lower comparison of (10) with F_m/lambda_m and its
flip-invariant positive vacuum ((S3)) gives
A_m >= Z_{+,m}(T)^{-2} Z_{+,m}(2d)^{-4}, and each projected trace lies
between 1 and the full trace, which tends to one by (24). So A_m -> 1,
p_m -> 1/8, A -> 1/8 and s_perp -> 1/8.

S3.17 Statement (25) itself (L402-407). HOLDS on the stated trajectories
(beta >= kappa log n, so that (18) gives Q to O(n^{-k})). The test uses
only adjoint links of the one local model Q: the joint law of two
collars and one slice probability.

## Step 4. The twist-ratio control (23) and the seed consequence (24) (done)

S4.1 (23), the order p_i(c) <= p_i(0) and the triangle character bound
(L359-365). HOLDS. (19) holds in every frame i (the same proof with the
other three axes as intermediate times, on any rectangular torus). With
g(c) = (1+delta)/8 - p_i(c) >= 0 and sum g = delta, a nontrivial character
on C_i has mean -sum g(c)(-1)^{eta.c}, of modulus at most delta.

S4.2 (23), star coefficients (L365-369). HOLDS. In frame j,
(1/8) sum_t Z_{c,t} (-1)^{eta.t} = Tr(T_c^{n_j} P_eta) >= 0 with P_eta a
spectral projection of the commuting flips. Summed over c it is
(sum f/8) times a six-bit character mean, and sum f <= 64 by (S2). If
supp eta lies in a tested triangle C_i (i <= 3), each h_{j,c}(eta) is in
[0, 8 delta].

S4.3 (23), the toggles (L371). HOLDS. Toggling edges 14, 24 flips the four
characters {14}, {24}, {14,34}, {24,34} of the star at 4; their supports
lie in C_2, C_1 or C_3. Toggling two spatial edges ij, ik at the star of i
flips {ij}, {ik}, {ij,i4}, {ik,i4}, with supports in C_k or C_j. Each
toggle costs at most 2 x 4 x 8 delta = 64 delta. Any two spatial edges
share a vertex, and any two temporal edges lie in the star at 4, so equal
parities are joined by one toggle of each kind: 128 delta.

S4.4 (23), the end of the proof and the converse (L373). HOLDS. C_1 =
{23, 24, 34} realizes any parity pair; the star at 1 = {12, 13, 14}
adjusts both parities to even; f(c) >= f(c+t) by the trace order in
frame 1 (c is static there); so f(B) >= 1 - 256 delta. Converse:
p_i(0) <= 8/(64(1-r)), so 8 p_i(0) - 1 <= r/(1-r). Cubic symmetry makes
p_1(0) = p_2(0) = p_3(0). The slice reading differs from p_i(0) by
O(n^3 e^{-c beta n}) (shortest side n/2).

S4.5 (24) (L380-395). HOLDS. I rederived each bound.
- A twist on the star of a frame: f >= (1-S)/(1+S) >= 1 - 2 eta (the flip
  invariant vacuum gives +1, the rest at most S <= eta).
- Proper subsets of the magnetic triangle lie on a star. For the full
  triangle, with h >= 0 on the star at 1,
  f(c) - f(c+t_1) - f(c+t_2) + f(c+t_1+t_2) = sum h (1-x)(1-y) >= 0,
  so f >= 2(1 - 2 eta) - 1 = 1 - 4 eta.
- 1 - 4 eta <= Tr(F_m/lambda_0)^{2q} <= a_m X_m and X_m <= 1 + eta give
  a_m >= (1-4 eta)/(1+eta); X_m - a_m <= ((1+eta)^2 - 1 + 4 eta)/(1+eta)
  = (6 eta + eta^2)/(1+eta) <= 6 eta.
- Z_{m,e}/lambda_0^q >= 2 a_m - X_m (flip-invariant top vector of F_m,
  (S3)); dividing by 1 + S(q) <= 1 + eta gives
  2(1-4 eta)/(1+eta)^2 - 1, and this is >= 1 - 12 eta because
  (1-6 eta)(1+eta)^2 = 1 - 4 eta - 11 eta^2 - 6 eta^3.
- Tr(F_m/lambda_m)^q = X_m/a_m <= (1+eta)^2/(1-4 eta).

S4.6 The shapes under (W) (L397). HOLDS. Shape two at side b = n/4 follows
from the shape-four limits by (T). Proposition B3 with a = tau = b/2,
p = q = 1: Pi = (b/(b - tau))^3 = 8 and |H|/|B| <= 64, so
g(tau; H) <= 512 log(1 + s). I listed the tori used: n^3 x q for
q = n/4, n/2, n. In frame 4 the box is n^3 = (4b)^3; in frame i <= 3 the
box is (n, n, q) with q in {b, 2b, 4b}. All sides are in [b, 4b] and all
times are at least tau = n/8, and S is non-increasing in time. So
eta = (1+s)^512 - 1 -> 0, and (24) at q = n/4 and q = n/2 gives all 64
ratios -> 1, a_m -> 1, X_m - a_m -> 0, and p_i(0) -> 1/8.

## Step 5. The charged comparison (1) and the seven exceptional levels (done)

S5.1 (1) (L25-52). HOLDS. I rederived every step.
- P = psi^{-1} U psi is Markov, reversible and positive for pi = psi^2;
  neutral f obey (1 - rho^s) Var f <= E_s(f).
- z = f + i g, r = |z|, w = z^2/r are neutral. int r^2 = int |w|^2 = 2,
  int r w = int z^2 = 0 (orthonormal real f, g). With c = (int r)/2,
  |int w| = |<1 - c r, w>| <= (1 - (int r)^2/2)^{1/2} 2^{1/2}, so
  |int w|^2 <= Var r and Var r + Var w >= 2.
- |r-v|^2 + |w-w'|^2 = 2(r-v)^2 + 4 r v sin^2 d, and
  4|z-z'|^2 = 4(r-v)^2 + 16 r v sin^2(d/2) >= it, since
  sin^2 d <= 4 sin^2(d/2). Zero radius: 2 v^2 <= 4 v^2.
- 2(1-rho^s) <= E_s(r) + E_s(w) <= 4[E_s(f) + E_s(g)]
  = 4[(1 - lambda_1^s) + (1 - lambda_2^s)] <= 8(1 - lambda_2^s).
- At s = 1 each nontrivial sector has at most one level with
  1 - lambda < (1-rho)/4, and the neutral sector only the simple vacuum:
  at most eight in all.
S5.2 Sharpness on the circle (L54). HOLDS: odd levels e^{-h} (twice),
first even excited level e^{-4h}, ratio (1-e^{-h})/(1-e^{-4h}) -> 1/4.
S5.3 (2) (L59-68). HOLDS. Z_chi(v) <= Z_+(v) because every twisted
integral is nonnegative; the levels below the top in a charged sector obey
lambda_{chi,i}^T <= lambda_{chi,2}^{T-v} lambda_{chi,i}^v with
lambda_{chi,2} <= (3+rho)/4 by (1) at s = 1. Purity comparison:
|N/D^2 - N_0/D_0^2| <= eps_1 + 2 eps_2 since N_0 <= D_0^2, D_0 >= 1 and
1 - (1+x)^{-2} <= 2x.
S5.4 (3) (L70-74). HOLDS. rho^v <= S_+(v), S_+(2v) <= S_+(v)^2, and
v log((3 + d^{1/v})/4) -> (log d)/4. The OPEN remark is a fair scope
statement.
S5.5 Finite-group comparison (L76). HOLDS. Eigenvalue 1 on constants and
c on each nontrivial character; strictly positive kernel; purity
(1 + 7 c^{2T})/(1 + 7 c^T)^2 runs over (1/8, 1) as c = e^{-u/T}.
S5.6 (4) (L81-89). HOLDS. A test sign has E_s = 2 P(disagree) and
E_s >= delta_chi, so delta_chi <= 2 h_chi. Var|f| <= delta_chi/gamma,
||sigma - f||^2 = 2(1-a) <= 2(1-a^2) <= 2 delta_chi/gamma, E_s(phi) <=
||phi||^2, and the triangle inequality for E_s^{1/2} give the upper bound.
Products of test signs give h_{chi eta} <= h_chi + h_eta. The winding-loop
sign is equivariant and its zero set is null under Haar, hence under the
absolutely continuous vacuum.
S5.7 Classification (L91). HOLDS. Both sides of (4) give closure of H;
G-invariance of pi and surjectivity of b -> (chi_i(b)) make the sign tuple
exactly uniform; Walsh products are orthonormal.
S5.8 Obstruction (L93). HOLDS. In the group example rho = 0, gamma = 1, the
equivariant sign is unique up to sign, and h_chi = (1 - c^s)/2.

## Step 6. The obstructions (done)

S6.1 (8) (L140-156). HOLDS. No plaquette holds two selected bonds (base
points differ by even vectors). Given the exterior the selected links are
independent with density prop. to exp(k.u), |k| <= 6 beta; the adjoint
leaves {u, -u}; the MAP error is q(s) with the S^3 marginal weight
(1-t^2)^{1/2}; q is nonincreasing (covariance of a decreasing indicator);
q(s) ~ (2/pi)^{1/2} s^{1/2} e^{-s} from N in [c/s, 1/s] and
D = e^s int_0^2 e^{-su} (u(2-u))^{1/2} du ~ e^s s^{-3/2}. The posterior of
V is a product of two-point laws, so a K-list has mass at most K prod
max_e, with mean prod (1 - q(|k_e|)) <= e^{-M q(6 beta)}.
S6.2 Trajectory consequence (L158). HOLDS as arithmetic: with
6 beta <= (3 - 6 eps) log n, M q(6 beta) >= c n^{6 eps}; 11/(3 pi^2) =
0.3715 < 1/2. The external RF lines are not checked here.
S6.3 (9) (L160-165). HOLDS. sigma = sigma_0 prod_{e in S} s_e, the
posterior mean has modulus prod |2 p_e - 1|, and E|2p_e - 1| = 1 - 2q.
The cylinder limit is the trace-norm convergence of normalized powers.
S6.4 (12) (L202-222). HOLDS. C_Pi is lift independent (each link lies in
two faces of Pi) and equals (-1)^{b_i} prod sgn w^b_p. A block's 21
affected faces are right: four links times five other faces, all distinct,
since a second unit square through two edges of a square is the square
itself. Arithmetic: 4 theta = pi/2 + pi/14, sin(pi/14) < pi/14 < 1/4, and
theta < 1/2 gives 20(1 - cos theta) < 5/2, so the action is < 15/4 < 4
(numerically 3.203). Good blocks have both parities with conditional mass
>= c e^{-4 beta} (normalizer <= 1); bad blocks cost the tilted bound.
S6.5 (13) (L229-234). HOLDS. The two patterns differ only at the centre
among all 21 affected faces, so any S gets c|S| usable centres.
S6.6 (14) (L236-241). HOLDS. Distinct coordinate 2-tori have disjoint face
sets, each of size >= n^2/2 (there are 4.5 n^2 <= 6 n^2 planes). Walsh
inversion gives TV <= (1/2) sum_{K nonempty} sum_b |E[prod_K C 1_b]|, and
(13) with H = sign of each coefficient gives sum_b |.| <= C x^{|K|},
x = e^{-c n^2 e^{-4 beta}}; the binomial sum is (1+x)^m - 1. On slopes
below 1/2, m x -> 0.
S6.7 (15)-(16) (L243-254). HOLDS. A k-fold product of spatial plane bits
on two slices uses k n^2 distinct faces; Walsh inversion bounds the
pointwise likelihood ratio; <v, P v> <= eps ||f||_{L^1}^2,
||v||^2 >= (1 - eps) ||f||^2, and 1_{[0,E]}(H) <= e^E P since P >= 0.
S6.8 (21) (L341-346). HOLDS. The designated cube contains the centre, four
side faces (affected) and one exterior face, so the two patterns give
different cube parities. Independence given the exterior, the bad-block
bound, and P(sum I <= M q/2) <= exp[-(1 - e^{-1} - 1/2) M q]
(0.132 > 0) are right.
S6.9 (22) (L348-352). HOLDS. The exponents 6 beta |u.1| and
beta(5|u.1| + |u.v|) have unique maxima [1] and [(5+v)/|5+v|] on
S^3/{+-1} (|5+v| > |5-v| since v.1 = cos h > 0); the other factors of
(17) are bounded and equal one near both maxima; Laplace concentration
gives TV -> 1.
S6.10 (27) (L428-433). HOLDS. On the good event (all O(n) slices read
correctly, union bound Cn^4 e^{-c beta n/2}) a slice outside the box reads
each bit identically for V and V'. Adaptive boxes are covered because the
good events do not depend on the box. The Dirichlet-quotient bound on the
gap follows.
S6.11 (28) (L437-448). HOLDS. Haar gauge rotation conjugates each corner
mismatch L^{-1}L' independently; its mean is (L.L') 1, so the orbit mean
of the new trace is w_p prod h. E w_p >= 1/2 at large beta. The plane
lemma is right: if every face had eps prod h > 2^{-1/2}, all |h| > 2^{-1/2},
each vertex cycle of four in-plane endpoints has sign product +1 (else a
path to the antipode of length < 4 x pi/4 = pi), and the product over all
corners contradicts prod_Pi eps = -1. The corner value L.L' is symmetric,
so link orientation does not matter. The constant 2^{-1/2} is sharp: at
one vertex take L_a = exp(I a pi/4), a = 1..4; then min eps prod h =
2^{-1/2} exactly. Jensen remark right.
S6.12 (29) (L451-458). HOLDS. Faces in distinct parallel planes have
disjoint vertex sets; for a face with w_p >= 0 the gauge-averaged signed
trace is at most 2^{-1/2}; X in [0,2] with E X >= b_* gives
P(X >= b_*/2) >= b_*/4; the binomial bound gives b_* M/16 good faces
except on C e^{-cM}; a union over K candidates covers adaptive selection;
the twisted side uses the unnormalized tilted bound; Cauchy-Schwarz on
E, E^c. The net remark (eight endpoint rotations per plaquette) is right.
S6.13 (30) (L465-481). HOLDS. I rederived Re(a b a^{-1} b^{-1}) =
1 - 2 sin^2 theta_1 sin^2 theta_2 for a = e^{I theta_1}, b = e^{J theta_2},
so the 12-action is 2 beta (sin^2 theta - sin^2(tu))^2 by
sin(theta+x) sin(theta-x) = sin^2 theta - sin^2 x. Second derivatives:
-8 beta sin^2 theta u^2 per 12-face and beta (grad_i u)^2 per mixed face
(four per site), tangent norm 2 sum u^2; this gives (30). For
|k_3|, |k_4| <= (sin theta)/2 the quotient is <= sin^2 theta/2, so the
Hessian is <= -3.5 beta sin^2 theta <= -c''. Scalar pin: the limit vector
would be a common eigenvector of I x and J x, hence parallel to K by the
commutator, and I x K = -J excludes it.
S6.14 (31) (L486-495). HOLDS. cos 4 theta = 8(3/4)^4 - 8(3/4)^2 + 1 =
-31/32; total action 63/32 + 5 = 223/32 < 7; curvature
16(-31/32) + 20(3/4) = -1/2. Transported axes make the four central
rotations add; each other face sees one unit-speed rotation; second
derivative beta(16 w_c + sum w_p), squared norm 4; disjoint supports.
S6.15 (32) (L497-508). HOLDS. D_* = xi + xi' is closed (same syndrome);
assignment plus Cauchy-Schwarz bound differing sets; Markov gives the
O(n^{-4}) exceptional first paths; a small component touching a block has
>= 6 faces and erasure costs exp[-2 beta (5 a_0 - 1)] with 5 a_0 - 1 = 7/3;
Hess(-log sum e^{-S}) = E Hess S - Cov grad S <= E Hess S; cross terms
vanish in every lift.
S6.16 (33) (L511-522). HOLDS. Conditioning only on Y keeps both full-path
marginals true Wilson laws; a component of the observed relative set that
touches a block and leaves the collar has >= R faces; small components are
closed and lie inside the collar; erasure changes only link signs, so it
keeps the conditioning and product Haar on unobserved links; the 21
affected faces are observed. Count c_R n^3 e^{-7 beta} -> infinity on
slopes below 3/7; 11/(3 pi^2) < 3/7 since 9 pi^2 > 81 > 77.
S6.17 Conditional independence at range r_* (L527). HOLDS. The two
boundary layers of each collar shield its interior in the finite-range
model; adding or dropping the interior is a channel each way, so the
affinities are equal; the TV statement follows by contraction.
S6.18 (34) (L529-534). HOLDS. sigma_1^2 >= sum sigma^4 = A; nonnegative
top singular vectors; TV(P, Q) <= (1 - H^2)^{1/2} <= (1-A)^{1/2}; the
triangle inequality with the two marginals gives 3 (1-A)^{1/2}; and
A >= sigma_1^4 >= H(P, P_X x P_Y)^4 >= (1 - TV)^4.
S6.19 Shared label under a seed and the value 7/8 (L536-539). HOLDS.
Sectorwise A_m -> 1 and (34) give TV -> 0 to the shared-uniform-label
comparison law. TV between (m,m) and p x p is
(1/2)[sum p(1-p) + (1 - sum p^2)] = 1 - sum p^2 -> 7/8; the channel
argument gives the upper bound and the coincidence event the lower bound.
The converse to (25) via (23), (26) and A_m >= (1 - TV_m)^4 holds.
S6.20 Support of the measurements (L426). HOLDS. With fixed h,
2d = n/2 - 2h >= n/4 for n >= 8h; recovery error O(n^{-4}) costs O(n^{-2})
in the affinity; strips of fixed width read the transverse bits.
S6.21 Slice and plane remarks (L135, L224). HOLD as stated.

## Step 7. The two-photon comparison and the guide runs (done)

S7.1 Two-photon comparison (L545). HOLDS. `gap-channel-astra.md` (33)
gives, in the free transverse Maxwell field on a periodic cube of side a,
a neutral two-photon state (momenta p, -p, |p| = 2 pi/a, contracted and
summed over the cubic orbit: zero momentum, A_1^+, C = +, trivial
winding) of energy 4 pi/a. With a = L and time L/2 its weight is
e^{-2 pi}. The arithmetic is right: 2 pi < 13/2, e < 3, and
3^{13/2} = 729 x 3^{1/2} < 729 x 2 = 1458 < 1650. So
S(L/2; L^3) >= e^{-2 pi} = 0.00187 > 1/1650 at every L, and the strict
test fails for this quadratic comparison at every size.
S7.2 SEP and the exact-cell construction (L545). HOLD as cited.
SEP is HOLDS AFTER CORRECTION in `gap-glue-check-astra.md` Section 5, and
the file uses it within the corrected scope (a neutral factor keeps every
flux ratio and crossing identity and changes the excited count; abstract
class only). Row 1155 L290 (checked, row 1156 item 45) divides the
rectangle affinity by k while keeping the one-slice marginals and the
cell table. Wording note: the file says "one-collar marginals" and
"square-root affinity"; the cited construction is stated for slices and
for the rectangle affinity of the square-root kernel. It applies to any
nonatomic observation, so no correction is needed.

S7.3 Guide runs (pure Python, `python3 -I`, peak memory about 17 MB; no
numpy). Scripts and outputs are in the session scratchpad, not committed.
They are guides only and prove nothing.
- (1): 400 random Z_2^3-invariant kernels K = W^2 (W >= 0, symmetric,
  invariant), 2 to 5 orbits: min of (1 - lambda_{chi,2}^s)/(1 - rho^s) is
  0.547 (s=1), 0.776 (s=2), 0.799 (s=3), 0.919 (s=10), all >= 1/4.
  Lattice circle with the half-turn: ratios 0.913, 0.355, 0.269 (N=8)
  and 0.259 (N=128, h=0.005), decreasing to 1/4 from above.
- (23): a hit-and-run walk in the polytope {f(0) = 1, all 256 star
  Fourier coefficients >= 0} found max (1 - min f)/delta = 1.23 and no
  violation of (19) or of the converse. In the tangent cone at f = 1 (the
  regime that matters), the walk found max
  64(-min d)/max_i(8 H_i(d) - sum d) = 6.66, at the all-ones twist. So the
  constant 256 in (23), and hence 4352 in (25), has a large margin.
- (34): 3000 random joint laws: max of TV - 3(1-A)^{1/2} is -3.8e-5 and
  max of (1-TV)^4 - A is -4.9e-10, both <= 0.
- (10): exact toy mixed cylinders on X = Z_2^3 x {0,1} with collars of two
  slices: in all seven runs Z_+(T)^{-2} Z_+(2d)^{-4} <= A_obs <= 1/Z_+(T)
  (for example 0.7429 <= 0.9235 <= 0.9945; two runs had a nearly rank-one
  kernel and gave 1.000000 throughout), and in the three runs where it was
  computed the slice-pair affinity equals Z_+(2T)/Z_+(T)^2 to 10 digits.
- (28): hill climbing on a 3 x 3 periodic plane with one twisted face found
  min_p eps_p prod h at most 0.688 < 2^{-1/2}; the hand example in S6.11
  attains 2^{-1/2} exactly.
- Constants: 3.2031 < 4; cos(4 arccos(3/4)) = -0.96875 = -31/32;
  223/32 < 7; 16(-31/32) + 15 = -0.5; 11/(3 pi^2) = 0.37151; 17 x 256 =
  4352; the two scalar inequalities of (24) hold on (0, 1/20).

## Step 8. Verdict table and result (done)

Line numbers are those of `library/gap-solve8-astra62.md`.

| # | Statement (lines) | Verdict |
|---|---|---|
| 1 | Tilted twisted input, Bessel-ratio order, Hoelder (L100-102) | HOLDS (row 1155 L420, checked) |
| 2 | (1), the quarter of the neutral gap, at most eight slow levels (L25-52) | HOLDS (guide agrees) |
| 3 | Sharpness on the circle (L54) | HOLDS (guide agrees) |
| 4 | (2) and the purity comparison, factor three (L59-68) | HOLDS |
| 5 | (3) and the order of limits (L70-74) | HOLDS |
| 6 | Finite-group ambiguity, purity range (1/8, 1) (L76) | HOLDS |
| 7 | (4) (L81-89) | HOLDS |
| 8 | Classification at a separated scale (L91) | HOLDS |
| 9 | Obstruction to the sign route (L93) | HOLDS |
| 10 | (5) (L104-110) | HOLDS |
| 11 | (6) (L112-116) | HOLDS |
| 12 | (7) (L121-133) | HOLDS |
| 13 | What the lost affinity measures (L135) | HOLDS |
| 14 | (8) and q(s) (L140-156) | HOLDS |
| 15 | Consequence on the trajectory (L158) | HOLDS (arithmetic; external RF lines not checked) |
| 16 | (9) (L160-165) | HOLDS |
| 17 | (10), lower bound (L184-191) | HOLDS (exact; guide agrees) |
| 18 | (10), upper bound (L172-182) | HOLDS (given row 1155 (27), checked) |
| 19 | (11) (L193-197) | HOLDS |
| 20 | (12) and the block construction (L202-222) | HOLDS |
| 21 | Comparison with the corrected reading (L224) | HOLDS |
| 22 | (13) (L229-234) | HOLDS |
| 23 | (14) (L236-241) | HOLDS |
| 24 | (15) and (16) (L243-254) | HOLDS |
| 25 | Localization of sign defects, R, D_1, B (L261-266) | HOLDS |
| 26 | Clean and marked split; six-face bound; slope 1/3 form (L268-274) | HOLDS |
| 27 | Finite lists and the class b(v) (L277-281) | HOLDS |
| 28 | (17) (L283-290) | HOLDS |
| 29 | Hard-core gas for clean components (L292) | HOLDS |
| 30 | (18) (L294-304) | HOLDS |
| 31 | Bounded-range formula L_0 + sum L_C, TV O(n^{-k}) (L306-311) | HOLDS |
| 32 | (19) (L318-323) | HOLDS |
| 33 | 64-twist tilted bound; (5), (6) for all twists (L325) | HOLDS |
| 34 | Local model Q, density check, conditioning (L327) | HOLDS |
| 35 | (20) (L329-336) | HOLDS |
| 36 | (21) (L341-346) | HOLDS |
| 37 | (22) (L348-352) | HOLDS |
| 38 | (23) and its converse (L359-373) | HOLDS (guide: constant far from sharp) |
| 39 | (24) (L380-395) | HOLDS |
| 40 | Shapes under (W), B3 factor 512 (L397) | HOLDS |
| 41 | (25), the one-period unconditioned test (L402-407) | HOLDS (on beta >= kappa log n) |
| 42 | (26) (L409-413) | HOLDS |
| 43 | Sufficiency, 64 and 17 x 256 = 4352 (L415-419) | HOLDS |
| 44 | Necessity (L421) | HOLDS |
| 45 | Support of the measurements (L426) | HOLDS |
| 46 | (27) and the relaxation-gap bound (L428-433) | HOLDS |
| 47 | (28), the plane lemma, Jensen remark (L437-448) | HOLDS (constant 2^{-1/2} sharp) |
| 48 | (29) and the net remark (L451-458) | HOLDS |
| 49 | (30) with the scalar pin (L465-481) | HOLDS |
| 50 | Typical instability and (31) (L486-495) | HOLDS |
| 51 | (32) (L497-508) | HOLDS |
| 52 | (33) (L511-522) | HOLDS |
| 53 | Conditional independence at range r_* (L527) | HOLDS |
| 54 | (34) (L529-534) | HOLDS (guide agrees) |
| 55 | Shared label under a seed; converse to (25) (L536) | HOLDS |
| 56 | Unconditioned TV tends to 7/8 (L539) | HOLDS |
| 57 | Limits of the available inferences (L543) | HOLDS as a summary |
| 58 | Limits on the neutral route, SEP, cell table, two photons (L545) | HOLDS (wording note) |
| 59 | OPEN paragraph and RESULT line (L547, L551) | HOLDS as statements of scope |
| - | GUIDE and status lines (L3-23, L98, L167, L259, L316, L357, L378, L435, L463, L549) | Not checked as proof; sources not fetched |

Counts: 59 statements checked by hand. 59 HOLD. None needs a
correction. None FAILS.

Notes (not corrections).
- L13 and L549: row 1155 is now checked (row 1156: every statement
  HOLDS), so the row 1155 inputs used here ((9), (10), (15), (27), (29),
  (30), (34), (35) and the mixed-cylinder recovery) are checked once.
- "Admissible" side in (11) and (25) should be read as a size in the
  dyadic set P of row 720 Theorem ZD-c; L9 (4 | n) and L397 (8 | n) fit.
- L545: "one-collar marginals" and "square-root affinity" refer to row
  1155 L290, which is stated for one-slice marginals and the rectangle
  affinity; the construction carries over to any nonatomic observation.
- L475: "|k_3|, |k_4| <= sin theta/2" reads as (sin theta)/2; the other
  reading also gives a negative Hessian.
- L327: the condition delta < p/2 is not needed for the bound 2 delta/p.
- Not checked: the external lines cited at L5, L7 and L158 (Sussman and
  Alpoge RF10, RF20, RF23-RF28, outline and CA-I lines).
- Independence: the author row is by another provider; this check is one
  reading by hand. The guide runs are a separate data path (toy models,
  random kernels, a polytope walk) and prove nothing.

What the file establishes, as checked here: on trajectories with
beta >= kappa log n, (W) is equivalent to the one-period test (25) on
two unconditioned adjoint collars and one transverse slice probability
in a bounded-range adjoint model; one transverse zero-class probability
controls all 64 twist ratios (23); (W) forces all eight magnetic sectors
to near-vacuum dominance (24). It also proves the obstructions listed
above. It does not prove (25) itself, (W), or a mass gap. The transverse
class frequency and the within-sector dependence of distant collars
remain OPEN.

RESULT: HOLDS - check of row 1157 (`library/gap-solve8-astra62.md`), checked line by line by hand by Claude Opus 5.5 (max effort) as FINISH row 1160, positive claims first: 59 statements, all HOLD, none needs correction, none FAILS; in particular the one-period unconditioned adjoint test (25) with the bounded-range model (17)-(18), the twist-ratio control (23), the seed consequence (24), the charged comparison (1) with at most seven exceptional levels, and the obstructions (14), (27)-(30), (33) and the two-photon comparison (e^{-2 pi} > 1/1650); guide runs (pure Python, about 17 MB) agree and prove nothing; (W), the strict test at a fixed size and the four-dimensional SU(2) mass gap remain OPEN.
