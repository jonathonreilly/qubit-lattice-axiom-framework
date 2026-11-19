# Check of row 1153 (gap-solve6-astra62.md): FINISH row 1154

Status: complete. Written step by step as the check went.

File under check: `library/gap-solve6-astra62.md` (413 lines).
Checker: Claude (Opus 5.5), FINISH row 1154, check of row 1153.
All paths are relative to the lane folder L.

## Plan (at most eight steps)

1. Read the file under check in full, in ranges. Read the cited parts of
   rows 1143-1151, row 720 Proposition MB and its check (line 89), and the
   council brief.
2. Check the comparison (3) with (2): the entropy upper bound, the holonomy
   positivity, and both Gaussian sides.
3. Check the endpoint bound (4), the short-time law (5) with (6), and the
   integral pi^2/8.
4. Check the excess bound (16) and the (APR) discharge for Proposition MB.
5. Check the reformulation (24), the conditional count criterion, and the
   larger ranges in (28).
6. Check (1), (7)-(15), (17)-(23) and the obstructions.
7. Numeric guide runs (Python -I, under 2 GB). A guide only.
8. Verdict table and the RESULT line.

## Log

- Step 0: file created with this plan.
- Step 1 (reading), part a: read the file under check in full (lines 1-413),
  the council brief, and row 1151 Sections 13-17 (lines 409-534 of
  `library/gap-solve5-astra62.md`).
- Step 1, part b: read row 720 notation (line 55: F = log Z, f = inf F/|n|,
  Delta = F - f|n|) and Proposition MB (lines 351-363); its check, lines
  84-94 (line 89 is the weakened (APR)); row 1149 Section 5 and (16)
  (lines 166-222); row 1151 Section 3 (lines 39-66); the check of row 1151,
  Section 14 part (lines 65-140).

## Step 2 result: the comparison (3) with (2) (L27-78)

Notation: q(g)^2 = 2a(g), a = 1 - tr g/2. So e^{beta q^2/4} = e^{beta a/2},
and beta a_p = beta q_p^2/2 is matched by the Gaussian action beta|dX_p|^2/2.

**2.1 One-plaquette tail (L29-33). HOLDS.** Row 1149 (16) (L216-222 of
`library/gap-solve4-astra62.md`) gives the Bessel ordering C_{beta/2} <= C_beta
of normalized one-link convolutions. Take either direction of p as transfer
time. Replace the one factor of p by C_{beta/2}. The layer M C' M is below
M C M, and Tr(F^{(L-1)/2} M C' M F^{(L-1)/2}) <= Tr F^L for any period L, so no
parity is needed. The scalar z_{beta/2}/z_beta tends to 2^{3/2}. Jensen gives
E q^2 <= 4 log C / beta.

**2.2 Width-one rectangles (L35). HOLDS.** This is row 1151 (4) (L60-66 of
`library/gap-solve5-astra62.md`), checked in row 1152. With the long side as
transfer time (period n > h), E w(U_{1 x h}) = sum pi_{ik} (nu_k/lambda_i)^h,
pi_{ik} = lambda_i^n |V_ki|^2 / sum lambda^n. The weights have mass one by the
isometry, and nu_k/lambda_i >= 0. Jensen gives E w >= (E w_p)^h >= 1 - Ch/beta,
so E q^2 = 2(1 - E w) <= Ch/beta. Every strip used in (2) has a spatial long
side of length at most b+1 < n, so the hypothesis h < n holds.

**2.3 Tree coordinates and (2) (L37-41). HOLDS.** Corner comb: all axis-1
links, the axis-2 links in the plane x1 = 0, the axis-3 links on the line
x1 = x2 = 0. A non-tree axis-2 link slides along axis 1 onto a tree link (one
strip). A non-tree axis-3 link slides along axis 1, then along axis 2 onto the
spine (two strips). All strip sides are tree links. With q(gh) <= q(g) + q(h)
and conjugation invariance, Q_e is at most the sum of at most two strip
chords. For a temporal link the comb path from the root has at most three
straight segments. The three temporal strips concatenate, and the temporal
links at the two junctions cancel up to conjugation. So Q_e is at most three
strip chords, also on the wrap step. Each Q_e is the chord of a closed-loop
holonomy, so it is gauge invariant. Then E Q_e^2 <= 9 C (b+1)/beta, and the sum
over at most 4vs links gives (2). The pointwise form Q_e <= 3(b+1)d follows by
tiling each strip by its plaquettes.

**2.4 Statement of (3) (L45-51). HOLDS.** The tiling needs
n mod b <= floor(n/b), which n >= 2(b+1)^2 gives.

**2.5 Upper bound, entropy step (L53-61). HOLDS.**
- p_B: P(q_p > d) <= C(2+beta)^{-K/4}. The box has at most
  6vs <= 6(b+1)^4 <= C beta internal plaquettes. K >= 40 gives p_B <= beta^-8.
- log Z_s = -beta E_mu A - D(mu || Haar) at the Gibbs law. Marginalizing out
  the joining links lowers D. Then
  D(mu_{union B} || prod Haar_B) = sum_B D(mu_B || Haar_B) + D(mu_{union B} || prod mu_B),
  and the last term is >= 0. Dropping the crossing actions raises the bound.
- For mu_B = (1-p) nu_g + p nu_b with disjoint supports,
  D(mu_B) = (1-p) D(nu_g) + p D(nu_b) - h(p). The Gibbs bound on each set gives
  E H_B + h(p_B) + (1-p_B) log I_g + p_B log I_b. I_b <= 1 since the integrand
  is at most one. The penalty mean is paid in the true marginal, where (2)
  applies.

**2.6 Upper bound, holonomy (L63). HOLDS.** Gauge invariance of the integrand
(actions, chords of loop holonomies, indicators) lets one fix the spatial
trees and the root links on steps 0..s-2. On the wrap step substitute
k_x = k~_x h. The temporal plaquette holonomy becomes the root-one holonomy
with the next slice conjugated by h. The penalty q(k_x h^{-1}) becomes q(k~_x).
So the wrap kernel is K_B(x, h y h^{-1}) and I_g = int dh Tr(K_B^s R_h).
Symmetry: exchanging the slices and inverting the temporal links maps each
temporal plaquette holonomy to a conjugate of its inverse. Traces, chords and
Haar measure are invariant, and the spatial factors are split evenly (the
indicators are idempotent). K_B is real, bounded by one, hence Hilbert-Schmidt
and self-adjoint. For even s, K_B^s = (K_B^{s/2})^2 >= 0 is trace class, and
|Tr(K_B^s R_h)| <= ||K_B^s||_1 = Tr K_B^s. Even s is needed because K_B need
not be positive. The argument indeed allows the sharp cutoff.

**2.7 Upper bound, chart comparison (L65-69). HOLDS.** At h = 1 on the good set
every free link has Q_e <= 3(b+1)d = O(beta^{-1/4}(log beta)^{1/2}). In
quaternions U_p = 1 + (dX)_p + O(sum |X_e|^2), so |q_p - |(dX)_p|| <=
C sum |X_e|^2 and |q_p^2 - |(dX)_p|^2| <= C(d + b^2 d^2) sum_{e in p} |X_e|^2.
|X| <= (pi/2) Q <= 2Q since 2 sin(r/2) >= 2r/pi. The Haar density is
h_0 (sin|X|/|X|)^2 with h_0 = 1/(2 pi^2). Linearized paths: each link is a
signed sum of at most C b curls on its own slice or step. Cauchy-Schwarz and at
most C b^3 paths through one plaquette give ||X||^2 <= C b^4 ||dX||^2.
Incidence gives d*d <= 24. So |log G_{B,s}| <= C vs log(2+beta). Error per site:
E H_B/(vs) <= C b(d + b^2 d^2) = O(beta^{-1/4} log(2+beta)), plus p_B log beta
and log 2/(vs). So the upper side has error O(beta^{-1/4} log(2+beta)). This also
confirms the remark at L373.

**2.8 Lower bound (L71-78). HOLDS.**
- The s slice combs and the s-1 root links of a box form a spanning tree of
  B x Z_s. The union over boxes is a forest, so the rest is product Haar.
- Every crossing plaquette has only restricted or tree links. Spatial ones:
  two joining and two boundary-tangent links (four joining at a corner).
  Temporal ones: two joining links and two boundary temporal links, where a
  root temporal link is tree-fixed or is the restricted wrap link.
- There are at most C s b^2 restrictions per box. A Haar ball of radius 1/beta
  has mass >= c beta^-3.
- Setting a restricted link to one changes beta a_p by at most
  beta (q + q')|q - q'|/2 <= 2 per incident plaquette.
- The Schur complement lies between the extreme eigenvalues of the form, so
  restoring the C s b^2 coordinates costs O(s b^2 log(2+beta)).
- In the restricted Gaussian, Cov(DX) = beta^{-1} D(D*D)^{-1} D*, a projection
  over beta. The path formula stays valid with extra zero coordinates, so
  Var X_e <= |c_e|^2/beta <= C b/beta. The union bound over <= C beta
  coordinates gives the event with probability >= 1/2.
- On the event: beta |q^2 - |dX|^2| <= C beta (b l/beta)(sqrt(l/beta) + b l/beta)
  = C[b l^{3/2}/sqrt(beta) + b^2 l^2/beta], l = log(2+beta). Jacobian cost
  <= C r^2 <= C b l/beta. Boundary cost per site C l/b. At b = floor(beta^{1/4})
  the total per site is C eps_beta.

**Verdict on (3): HOLDS.** The upper side is better than stated
(beta^{-1/4} log); the lower side carries the (log)^{3/2}.

## Step 3 result: (6), (4), (5) and the integral pi^2/8 (L80-107)

**3.1 (6) (L94-99). HOLDS.** Two uses of (3) at s = m and s = 2m (both even,
2m <= b) give error 4 C N m eps. Per-step scalars cancel, and per mode the
periodic determinant prod_h (2 cosh w - 2 cos(2 pi h/m)) = 2 cosh(m w) - 2 =
e^{m w}(1 - e^{-m w})^2 gives -(3/2)[2 log det_m - log det_2m] = 3 f(m w). This is
row 1151 Section 14, checked in row 1152 (14.5) with a ten-digit guide run.
The multiplicity r(q) - 1 is new here. I re-derived it. On index q the edge
Laplacian equals lambda_q on the r(q) available directions (cross terms cancel,
row 1151 L452). The gradient of the vertex mode q spans one line, with entries
2 sin(pi q_i/(2 b_i)). ker(grad*) is its orthogonal complement, where
d*d = lambda_q. So the multiplicity is r(q) - 1, and the total
sum (r(q) - 1) = |E| - |V| + 1 is the transverse dimension. A guide run
(Step 7) confirms the spectrum on small boxes.

**3.2 (4) (L101). HOLDS.**
- Shell bound: sin x >= 2x/pi gives lambda_q >= 4|q|_inf^2/(b+1)^2. With
  w = 2 arcsinh(sqrt(lambda)/2) and lambda <= 12, w >= c sqrt(lambda), so
  w >= c|q|_inf/b.
- sum_{k>=1} k^2 e^{-yk} = e^{-y}(1 + e^{-y})/(1 - e^{-y})^3 <= C y^{-3} for
  all y > 0. With f = 2 sum_{h odd} e^{-hx}/h this gives C(b/m)^3 per box and
  C N/m^3 in all.
- g_s is convex (log-sum-exp of linear functions), so
  J_s' = 2(g_s' - g_{2s}') <= 0. Also g_{2s} <= g_s and g_{2s} >= 0 give
  g_s <= J_s <= 2 g_s.
- J_T <= J_m <= C N(m^-3 + m eps). With m the even integer nearest eps^{-1/4},
  m << beta^{1/4}/2 and m <= T. So J_T/N <= C eps^{3/4} = C beta^{-3/16} l^{9/8}.

**3.3 (5), first limit (L103-107). HOLDS.**
- Spacing in u_i = pi m q_i/b_i is pi m/b_i. lambda_q = 4 sum sin^2(u_i/(2m)), so
  m w_q -> |u| uniformly on compacts.
- In the bulk r - 1 = 2; with three colours the per-box limit is
  6 pi^-3 int_{octant} f(|u|) du = (6/(2 pi)^3) int_{R^3} f(|u|) du.
- int_{R^3} f(|u|) du = 4 pi int r^2 f(r) dr = 8 pi sum_{h odd} (1/h)(2/h^3)
  = 16 pi sum_{h odd} h^-4 = 16 pi (pi^4/96) = pi^5/6.
  (sum_{h odd} h^-4 = (15/16) zeta(4); Parseval on x^2 gives zeta(4) = pi^4/90.)
- So the limit is 6 pi^5/(6 * 8 pi^3) = pi^2/8.
- Small |u|: (m/b)^3 sum_{k <= delta b/m} k^2 (1 + |log(c m k/b)|) is
  C delta^3 (1 + |log delta|) + o(1). Large |u|: R^2 e^{-cR}. Coordinate planes
  carry relative weight O(m/b). All uniform in the b or b+1 choices. The
  normalized error of (6) is O(m^4 eps). Odd and real periods follow by
  monotonicity.
- Physical check: six bosonic modes of free energy pi^2/90 each give
  g_m ~ (pi^2/15) N/m^3, so J_m = 2 g_m - g_2m ~ (pi^2/15)(2 - 1/8) N/m^3
  = (pi^2/8) N/m^3.

**3.4 (5), second limit (L107). HOLDS.** g_m = sum_{k<h} 2^{-k-1} J_{2^k m}
+ 2^{-h} g_{2^h m}, with 0 <= g_{2^h m} <= J_{2^h m} <= J_m. Each fixed
dilation 2^k m still satisfies (2^k m)^4 eps -> 0 and 2^{k+1} m <= b. The limit
is (pi^2/8) sum_k 2^{-k-1} 2^{-3k} = (pi^2/8)(1/2)(16/15) = pi^2/15.

**3.5 Statement of (4)-(5) (L82-92). HOLDS.** The window m^4 eps -> 0 forces
m << beta^{1/16}, so the physical duration m a_j tends to zero, as stated.

## Step 4 result: (16) and the (APR) discharge (L256-268)

Row 720 notation (L55 of `library/gap-phys-seed.md`): F = log Z,
f = inf F(n)/|n|, Delta(n) = F(n) - f|n| >= 0, D(a) = Delta(a,a,a,a). The file's
D_beta(n) = P(n) - n^4 f_beta is this D.

**4.1 (16) (L258-264). HOLDS.**
- (3), (6), (4) need only that each spatial side is >= 2(b+1)^2: each circle
  is tiled separately, and the one-plaquette and rectangle bounds hold on any
  rectangular torus with sides above b+1.
- Doubling one side t of a torus of volume V = N_sp t:
  log Z_t/V - log Z_2t/(2V) = J_t/(2V) exactly (scalars cancel). For t >= m,
  J_t <= J_m <= C N_sp eps^{3/4}, so the drop is <= C eps^{3/4}/t.
- Doubling the four sides of the n^4 cube one at a time: at each step the
  doubled side has length n and the other three are >= n >= 2(b+1)^2. So
  p(n) - p(2n) <= 4 C eps^{3/4}/n. Summing over the cubes 2^j n gives
  8 C eps^{3/4}/n.
- The cubes 2^j n are cofinal and p is monotone in each side, so their limit is
  the infimum f_beta. Hence 0 <= D_beta(n) <= C n^3 eps^{3/4}.
- The remark at L262 is right: on the physical grid n^3 eps^{3/4} diverges.

**4.2 D_beta(n) <= C beta n^3 (L266). HOLDS.** Tiling (kn)^4 by open n^4 cubes
leaves at most C k^4 n^3 crossing plaquettes, each with action <= 2. With them
bounded by e^{-2 beta}, the joining links appear nowhere else and integrate to
one. So log Z((kn)^4) >= k^4 log Z_open(n) - C beta k^4 n^3. Dropping the
plaquettes that contain a wrapping link frees the wrapping links and leaves
the open cube, so P(n) <= log Z_open(n). Take k = 2^J; the left side over
(kn)^4 tends to f_beta (cofinal cubes). This gives f_beta >= p(n) - C beta/n.

**4.3 The (APR) discharge (L268). HOLDS.**
- The check of row 720 (L89 of `library/gap-phys-seed-check.md`) states that
  (APR) can be weakened to rho^{-4i} M(rho^i nu) -> 0 for each nu. I confirm
  this: the iteration gives
  M(nu) <= P_0 sum_{k=1}^{i} rho^{-4k} + rho^{-4i} M(rho^i nu).
- With M(nu) = D_{beta(nu)}(L_0 nu) and 4.2:
  rho^{-4i} M(rho^i nu) <= C L_0^3 nu^3 rho^{-i} beta(rho^i nu)
  = C L_0^3 nu^4 [beta(rho^i nu)/(rho^i nu)] -> 0 when beta(nu) = o(nu).
  L_0 nu = n_0 rho^i is an integer >= 3 on the geometric set.
- The identity D(n) = rho^-4 (Phi_rho(n) + D(rho n)) holds at one coupling. The
  use of (MONO-Delta) at the torus of rho L_0 nu sites is as in the check
  (L88). The final step to rho^k L_0 nu is (MONO-Delta) again.
- So on the geometric set with beta(nu) = o(nu), (MONO-Delta) and (BASE-Phi)
  give D_{beta(nu)}(rho^k L_0 nu) <= P_0/(rho^4 - 1). The file correctly keeps
  (MONO-Delta), (BASE-Phi) and the spectral part of (W) as open inputs, and
  correctly notes that an arbitrary cutoff sequence need not be closed under
  nu -> rho nu.
- Scope remark (not a correction): this removes only the boundary hypothesis.
  On this class the hypothesis that the check found missing from Corollary
  MB1 (L94 of the check) is supplied by 4.2, so MB1 holds there as stated.

## Step 5 result: (24), the count criterion, and the larger ranges in (28)

**5.1 (24) (L381-391). HOLDS.** With E_i > 0 for i > 0 (positivity improving
on the full invariant space, so the vacuum is simple):
sum_{E_i > E_o} e^{-kT E_i} <= (sum_i e^{-m E_i}) e^{-(kT - m) E_o}
= e^{g_m - (kT - m) E_o} <= e^{g_m - (T - m) E_o} <= n^-7 for k = 1, 2, since
g_m <= R_0. As the traces
are >= 1, J_T = 2 log(1 + S_1) - log(1 + S_2) + O(n^-7). The dimension bound:
(13) with l = floor(c R_0/[T(1+beta)]) needs C(1+beta) l <= E_o; on the grid
R_0/[T(1+beta)] ~ n^2 e_beta^{3/4}/beta -> infinity, so the dimension diverges.
0 <= S_2 <= S_1 gives log(1 + S_1) <= J_T + o(1) <= 2 log(1 + S_1), so the total is
bounded exactly when S_1 = O(1).

**5.2 The exact-gap estimate (L393-397). HOLDS.**
sum_{i>0} e^{-T E_i} <= e^{-(T-m) Delta}(e^{g_m} - 1) is valid. (13) at l = 1
gives at least floor(c_1 sqrt(beta)) >= 2 states with E <= C(1+beta), so
Delta <= C(1+beta). With m << beta^{1/16}, n^3/m^3 >= n^3 beta^{-3/16} and
T(1+beta) = n(1+beta)/2, so the right side diverges in the whole window.

**5.3 Conditional count criterion (L399). HOLDS.** D_j(0) = 0 and D_j is
bounded, so S_1 = int_0^inf e^{-x} D_j(x) dx. The cap extends the count bound
above T E_o. Then S_1 <= K int_X^inf e^{-x} e^{eta(x-X)} dx = K e^{-X}/(1 - eta).
J_T <= 2 log(1 + S_1) + O(n^-7) gives the wall test under the stated
inequality. The window remark is right: E_o/(N/m^4) = O(e_beta^{3/4} m^4/T).

**5.4 (10) (L159-163). HOLDS.**
- Couplings in [beta/2, 3 beta/2], so the one-plaquette tail holds with
  exponent beta a/4 and the rectangle bound holds on every axis.
- In an open four-cube the comb slides a link along at most three axes onto the
  spine; this gives (2) with b^4 in place of vs. There is no wrap, so no
  holonomy step is needed.
- The weighted Taylor error, the bad-cube probability, the penalty mean
  (C b^5/beta per cube) and the precision bounds (weighted precision >= beta
  d*d/2, curl covariance <= 2/beta, path variance <= C b/beta) are as in (3).
- The uncovered fraction O(b/n) times |g_b| = O(log beta) and the boundary
  pins cost O((1/b + b/n) log(2+beta)) per site, which is below eps_beta on the
  grid.

**5.5 Derivative of g_b and p_V (L165). HOLDS.** g_b(u) - g_b(0) =
-(3/(2b^4)) log det(I - uH), 0 <= H <= I. Tr H = Tr(1_o Pi) = d_b/6 by cube
symmetry, with d_b = |E| - |V| + 1 = 4b^4 - 4b^3 - b^4 + 1 = 3b^4 - 4b^3 + 1.
So g_b'(0) = d_b/(4 b^4) = 3/4 + O(1/b), and |g_b''| <= (3/(2b^4)) Tr H * 4 <= C
for |u| <= 1/2. Convexity of p_V with secants at distance sqrt(eps) gives
p_V'(u) = g_b'(u) + O(sqrt(eps)) for |u| <= 1/4; O(1/b) = O(beta^{-1/4}) is
absorbed.

**5.6 (9) (L152-157, L167). HOLDS.** For u < 0 the couplings rise, so marked
electric convolutions stay positive and marked magnetic multipliers stay
positive; trace Holder disseminates for both signs. Hoelder with exponent six
over orientations needs |6u| <= 1/8 <= 1/4, which |u| <= 1/48 gives. Jensen
gives the lower bound with p_V^{(o)'}(0) = 3/4 + O(sqrt(eps)) for every
orientation, since g_b is orientation free. So
log E exp(beta u sum_S a) = (3/4)|S| u + O(|S||u|(|u| + sqrt(eps))) in each period,
and the leading terms cancel in 2(one period) - (two periods). The width
beta^{1+epsilon}/M gives error C beta^epsilon(beta^epsilon/M + beta^{-1/8} l^{3/4}),
which tends to zero for epsilon < 1/8.

**5.7 Combination with full deletions (L169). HOLDS.** log E e^{q Y_i} =
O(beta^epsilon(beta^epsilon/|D'| + sqrt(eps))) -> 0 for each fixed q. Cauchy-Schwarz
under the tilt gives (1 + o(1)) sqrt(P(bad)); Holder from delta to delta' keeps
(34). The deletion of k faces and the change of denominator cost
<= 4 i t k = o(1) since |D'_j| exceeds every power of beta. The cold-end
reduction is inherited unchanged. Row 1151 L417 marks row 1149's box estimate
as unchecked at the pin; its check (row 1150, RESULT at L805 of
`library/gap-solve4-check-opus.md`) has since found all its statements HOLD.

**5.8 Tilted tails and strips (L173-177). HOLDS.** For a plaquette of
orientation o' != o, a direction of o' outside the plane o makes all sources
magnetic (positive multipliers), so the Bessel ordering applies on the copy.
For orientation o, dissemination of e^{beta a_p/2}: in-plane layers M C_i M are
self-adjoint (each joint crossing kernel is a function of the traces of
U_i U_i'^{-1}, which are inversion invariant), and even extents make
||L||_n^n = Tr L^n; perpendicular layers are positive after the half-power
split. Removing the source costs 2|z|B <= 2, and (10) at u = 1/2 bounds the
remaining difference by -(3/(2b^4)) log det(I - H/2) + O(eps) <= C. Strips:
with even extent n_i the weights lambda_i^{n_i}|V_ki|^2 are nonnegative, so
Jensen applies to x^h for even h on the whole line; odd h uses the
triangle inequality with one plaquette.

**5.9 (11) (L179-188). HOLDS.** The Lipschitz constant of min(exp(sum r^2/2), B)
is at most B sqrt(2 log B) <= H_1. The added penalty C|z| H_1 sqrt(beta) sum Q^2
absorbs the radius replacement by the product estimate; its true mean is
C|z| H_1 b/sqrt(beta) per site. The cube source sum is C b^2 H_1-Lipschitz in
standard normals (the stacked curl map has norm one), and the Gaussian moment
bound pi^2 z^2 K_1^2/8 gives the z^2 H_1^2 term per site. Periodic rank
3b^4 - 3 (closed = exact + four periods), constant diagonal (1 - b^-4)/2, common
subspace of codimension O(b^3), Hilbert-Schmidt bound rank x norm^2 = O(b^3),
mean squared diagonal difference O(1/b): all correct. The target mean
E min(exp(sum |Z_i|^2/4), B) uses variance 1/2 per component.

**5.10 Sampling, alpha < 3/80 (L190-197). HOLDS.** sup sigma delta'/(2(1+delta'))
= (3/16)(2/3)/(10/3) = 3/80. The window alpha/delta' < sigma/2 - alpha is
equivalent to alpha < sigma delta'/(2(1+delta')). Errors divided by |z|:
J_T/N and eps give exponents below sigma - 3/16 < 0 and sigma - 1/4 < 0;
H_1/sqrt(b) gives kappa - 1/8 < -h; H_1 b/sqrt(beta) gives kappa - 1/4;
|z| H_1^2 gives kappa - sigma/2 < -h. |mu_*^r - mu_{r,B}| <= E e^{(1+delta')X} B^{-delta'}
with X = sum |Z_i|^2/4 is finite for delta' < 1. The distinct-site argument
needs k beta^-h -> 0, k B^{-delta'} -> 0, k^2 B/P -> 0 and P|z|beta^-h >> k; all hold.

**5.11 Limit of that bound (L199). HOLDS.** min over |z| of A/|z| + C|z|H_1^2 is
2 sqrt(C A) H_1; with H_1 ~ B the two conditions force
alpha < sigma delta'/(2(1+delta')).

**5.12 (17) (L272-285). HOLDS.** q_p >= 1/6: u = d(delta_e) for an edge e of p
lies in the curl range (after a gradient shift into the tree gauge), has
|u_p| = 1 and ||u||^2 <= 6, so Pi_pp >= <e_p,u>^2/||u||^2 >= 1/6.
L_p L_p* = I_{3r}, and sum L_p* L_p <= 6 A*A <= 6 I. The semigroup proof:
for u_p = log P_t F_p, d_t u = (Delta - y.grad) u + |grad u|^2; pullback by L_p
commutes with the generator since L_p L_p* = I; Gaussian integration by parts
gives the displayed derivative; the bracket is >= 0 because
x -> (sqrt(c_0) L_p x)_p has norm <= 1. t = 0 and t = infinity give (17).

**5.13 Variance and mean (L287-289). HOLDS.** e^x <= 1 + x + C x^2 on [-6, 6].
On |Z|^2 <= 4 log B with q <= 1/2 + 1/log B the density times e^{q|Z|^2} is at
most e^4 (2 pi)^{-3r/2}; the ball volume is C(log B)^{3r/2}; the outside part is
B^2 P(chi^2_{3r} > 4 log B) = poly(log B). Chebyshev on the O(1/b) mean squared
diagonal deviation gives the C(1 + log B)^2/b fraction. dE G_q/dq is dominated
by |Z|^2 e^{|Z|^2/3}/2 on [0, 2/3], integrable.

**5.14 (18) and alpha < 3/40 (L291-304). HOLDS.** sup sigma delta'/(1+delta') =
(3/16)(2/3)/(5/3) = 3/40, and at delta' -> 2/3 one has alpha/delta' -> 9/80 < 1/8,
so both conditions can hold. kappa and h exist as stated. With B = beta^kappa,
|z| = 1/B: exchange O(beta^{kappa - sigma}); eps term O(beta^{kappa - 1/4} l^{3/2});
linear terms C[beta^{-1/8} + beta^{kappa - 1/4} sqrt(l)]; quadratic terms
beta^{-kappa} l^6 + beta^{kappa - 1/4} l^2 <= beta^{-kappa} l^6 since 2 kappa < 1/4.
All are o(beta^-h) under h < min(kappa, sigma - kappa, 1/8, 1/4 - kappa).

**5.15 Limit of the improved bound (L306). HOLDS.**

**5.16 Dyadic tail and (19) (L310-327). HOLDS.**
- Restricting L to a dyadic tail keeps the existential test: row 1145 §10
  (L380 of `library/gap-solve2-astra62.md`) states that a seed gives
  arbitrarily small limsup S on sufficiently large fixed dyadic cubes.
- Patch cost: the six faces of the elementary 3-cube give
  |x_z - x_z'| <= sum of the four side chords. Side faces for distinct transverse
  edges are distinct and unmarked. Patches of distinct marks are disjoint
  for R > 2r + 2. 2 U_0 >= sum_patches [sum_{z != 0} x_z^2 + (1/4) sum (x_z - x_z')^2],
  and the minimum with x_0 fixed is (1/G_r - 1) x_0^2.
- (I + Delta_r/4)^{-1} = (1/2) sum 2^{-j} K_r^j; the tail beyond j = r is at most
  2^{-r}; Fourier gives (19). Ray recursion c -> (1 + c)/(5 + 4c): 0, 1/5, 6/29;
  four rays give 24/29. So 1 - G_inf >= 24/53 and (3/16)(24/53) = 9/106.
- Moment: blocks L^{(R-1)/2} L_i L^{(R-1)/2} need a common residue, which the
  class has. In-plane layers need n/R even (2R | n); perpendicular layers are
  positive, so R | T suffices in time. U_0 - delta M_0 >= ((eta - delta)/(1 + eta))
  (U_0 + M_0), and p(c beta) - p(beta) = int 6 E a <= 6 C log(1/c).
- Exponents: alpha < (3/16) eta/(1 + eta) = (3/16)(1 - G_inf); alpha/delta' < 1/8
  needs 1 + eta > 3/2, which eta_inf >= 24/29 gives; delta' < eta < 1 keeps the
  Gaussian moment finite. G_inf > 1/2 from P_2 = 1/4 > 0 gives the bound 3/32.

## Step 6 result: (1), (7)-(8), (12)-(15), (20)-(23) and the obstructions

**6.1 (1) (L15-19). HOLDS.** For a positive trace-class transfer,
(Tr T^r)^{1/r} is non-increasing in r, so F/|n| is non-increasing in each side.
For u <= T <= n every side of (n,n,n,T) is >= u, so 2 log Z(n,n,n,T) <= 2 n^3 T p(u)
= n^4 p(u). P(n) >= n^4 p(v) for v >= n. With 2T = n this is (1). The scalars
cancel in J. The conditional consequence J_T <= L^4 C is immediate.

**6.2 Separate error bars (L25). HOLDS.** With log Z_i = V_i c + r_i and
|r_i| <= B V_i, a^-4 [p(u) - p(v)] = r_1/V_1 - r_2/V_2 can equal 2B. The file
correctly says this is about the inference, not about Wilson values.

**6.3 (7) (L111-123). HOLDS.** log Zbar - log Z = beta E_mu A_d + D(mu || nu) from
the density ratio. In the cut law every joining link lies in no plaquette, so
it is independent Haar. Integrating the free-end joining link along each time
path gives z_beta per temporal plaquette for any fixed temporal links, so
E_nu e^{-beta B_0} = z_beta^{(s-1) E_d}. The entropy variational inequality and
B_0 <= A_d give (7). z_beta <= C beta^{-3/2} from the angle density
(2/pi) sin^2 r and 1 - cos r >= 2 r^2/pi^2. Consequence: 2 log Zbar_m - log Z_2m
>= J_m + 2 E_d (m-1)[(3/2) log beta - C] >= c n^2 for m >= 2.

**6.4 Entropy loss of the upper step (L125). HOLDS.** The conditional law of a
link is von Mises-Fisher on S^3 with concentration v = beta |sum_p V_p| <= 6 beta.
E<U, e> = A(v)<u, e> <= A(v) <= A(6 beta) since A' is a variance. The band
[beta^-1/2, 2 beta^-1/2] has vMF probability >= c, so 1 - A(6 beta) >= c/beta. A
guide run gives beta(1 - A(6 beta)) = 0.2498 at beta = 50 and 500.

**6.5 (8) (L129-136). HOLDS.** Upper exponent min_t (t x + c t^-3)
= 4 (c/27)^{1/4} x^{3/4} (also checked numerically). The lower bound is the
standard tilted-count argument: under weights e^{-t m E_i - g_tm},
(1/v_m) log E e^{h v_m Y} -> c[(t - h)^{-3} - t^{-3}], strictly convex in h with slope
3 c t^-4 at 0, so Y concentrates exponentially. Wording note on L134: the count
uses the two-sided limit (5), hence both sides of (3); "the Gaussian comparison
alone would not imply this" should read "a one-sided bound would not imply
this". Not a proof step.

**6.6 Short-cylinder construction (L140-148). HOLDS.** V_k psi = D_* psi and
||V_k|| <= 1 + (D_* - 1) give the top eigenvalue; equality in the Rayleigh
quotient forces a top eigenvector of U, so it is simple. Min-max gives
lambda_i(V) >= lambda_i(U), the first k eigenvalues >= D_* - 1, and
lambda_{i+k}(V) <= lambda_i(U). For s <= 2m, log k + s log D_* = O(log n + m v_m/T)
= o(v_m) while g_s >= g_2m ~ c v_m/8. The kernel of V_k dominates that of U
pointwise, so the path law is a mixture with weight Tr U^s/Tr V^s on the Wilson
law. At T, 2T: excess <= e^{g_m} << D_*^T = e^{3 g_m}, and T/D_* -> 0 since
g_m/T ~ 2c n^2/m^3. So J_T(V_k) = log k + o(1). Wording note: the log-trace
agreement is in the normalization ||F|| V_k, whose top eigenvalue is
||F|| D_*; after the rescaling at L148 the log traces differ from Wilson by the
common per-step scalar s log D_*, as the phrase "with a common per-step scalar"
allows.

**6.7 (12) (L203-222). HOLDS.** A = C^{1/2} M^2 C^{1/2} has the nonzero spectrum
of M C M. A marked layer is <= e^{2 beta e} U by the pointwise multiplier bound
(each altered weight rises by at most e^{2 beta}). Both normalized traces are
>= 1 since the actions only decreased. mE_* = o(R) because
m beta n^2 h/(n^3 eps^{3/4}) -> 0. ||W - W_*||_1 <= e^{g_m - (r_0 - m) E_*}; the one- and
two-period replacement errors are <= ||W - W_*||_1 ||K||^j <= e^{g_m - R} n^-6.
For (15), K is a power of one positive layer, so W_*^{1/2} K W_*^{1/2} >= 0 has
rank <= rank P_*, and (Tr X)^2 <= d Tr X^2 gives J' <= log d + o(1) <= R(1 + o(1)).
The (28) deletions change the two logs by [0, 2 beta k] and [0, 4 beta k] with
the same sign, so |J| <= C N eps^{3/4} + 4 beta k.

**6.8 (13) (L224-230). HOLDS.** At most 16 l spatial plaquettes touch the 4l
links. F = DGD with e^{-16 beta l} <= D <= I, and G^{1/2} D^2 G^{1/2} between
e^{-32 beta l} G and G gives the ordered eigenvalue bounds; lambda_0(F) <=
lambda_0(G) handles the normalization. The cut transfer factorizes before
projection; its vacuum is simple, so gauge invariant. chi_d(U_p) times the
exterior vacuum is a gauge-invariant eigenfunction with eigenvalue ratio
a_beta(d)^4; the characters of disjoint holonomies are orthonormal.
a_beta(d) = E[sin(dr)/(d sin r)] >= 1 - d^2 E r^2/2 >= 1/2 for d <= c_1 sqrt(beta).
(Guide: a_beta(d) = 0.886 at beta = 100, d = 5 and 0.883 at beta = 400, d = 10.)
The rank consequence uses E_* >= 24 beta n^2 h and l = floor(c_2 n^2 h) <= c_0 N.

**6.9 (14) (L234-245). HOLDS.** f_i' = w_i - 1 in [-2, 0], f_1 - f_2 = J/(2M).
|[d d']| <= 4 ||d||, |int d (f_1'' - f_2'')| <= 4 ||d||, so int (d')^2 <= 8||d|| <= 4R/M.
|D'_j| >= c h (n/floor(beta^theta))^3 by row 1149 §6, so R/M <= C beta^{3 theta}
eps^{3/4}/h -> 0.

**6.10 (15) (L247-252). HOLDS.** With spatial couplings v in [beta/2, beta] the
tail, rectangle and penalty steps of (3) hold with constants changed, and the
mode equation is 2 cosh w = 2 + (v/beta) lambda_q, with the same shell bound. So
J_T(v) <= R on [beta/2, beta]. With M = 3NT, ||d|| <= R/(6NT) = C eps^{3/4}/T.
Chebyshev gives the measure statement.

**6.11 Convex example (L254). HOLDS.** f_1'' = (A/beta^2)(2C + s'') >= 0 for
2C > ||s''||; slopes lie in [-2, 0] for small A; S' vanishes near both ends;
the slope difference has squared integral A^2 int s'^2/beta <= C R/M; and
2M (f_1 - f_2)|_0^beta = 2MA = R. It tests only the pressure information, as stated.

**6.12 (20) (L331-342). HOLDS.** P(x, y) = U(x, y)/(psi(x) psi(y)) is a
symmetric Markov density for pi. The unprojected kernel lies in
[e^{-12 beta N}, 1] times a scalar; gauge averaging keeps the bounds; the
vacuum equation gives lambda in [k_-, k_+] and sup psi/inf psi <= k_+/k_-, with
inf psi <= 1 <= sup psi. So H/l <= (k_+/k_-)^3 <= e^{C_2(1+beta)N}. Markov
composition keeps [l, H]; rows have squared norm <= H. The middle complement has
norm <= e^{-(r_0 - 2)E}; the sandwich gives the relative error
(H/l) e^{-(r_0 - 2)E_dagger} = n^-7. Rank: m E_dagger ~ m(1+beta) n^2 = o(N eps^{3/4});
lower bound from (13) with l = floor(c' n^2).

**6.13 Scalar subgroup example (L346). HOLDS.** |sin kx| <= k|sin x| gives the
rare-branch bound k^2(1 - cos d)/(8b); the alternating branch has angle 0 or d;
the case split gives E a_k <= k(1 - cos d)/2 for k >= 2, and
1 - cos^k d >= k(1 - cos d)/2 when (k - 1)(1 - cos d) <= 1. At k = b the rare branch
gives E q_b^4 >= c b^3/beta^2. (Guide at beta = 10^4, b = 25: all k <= b pass;
E q_b^4 / (b^3/beta^2) = 0.124.)

**6.14 (21) (L348-355). HOLDS.** In temporal gauge the strip chord is
|f(X_k) - f(X_0)|. The one-step insertion gives E_vac e^{beta q^2/4} <= z_{beta/2}/z_beta,
so E q^4 <= C/beta^2. A_t and B_t are forward and reversed martingale
differences with L^4 norm <= 2L; their sums give the increment of (I + P)f;
(I - P)f has L^4 norm <= L. The induction for E S_k^4 <= C_0 k^2 d^4 closes for
C_0 >= 36 (the cubic-linear term vanishes).

**6.15 Finite-period obstruction (L357). HOLDS.** Equality of the bridge
transition with the vacuum transition for all x_0 forces K^{s-t-1}(., x_0)
proportional to psi, hence rank one; the projected Wilson transfer has
infinitely many positive eigenvalues.

**6.16 (22) (L359-364). HOLDS.** For b <= beta^{1/2}, P(max |X_e| > c_*) <=
C b^4 exp(-c beta/b) -> 0. On the fixed chart a_p = |dX_p|^2/2 + P_3 + O(sum |X_e|^4).
The centered Gaussian and the event are symmetric under X -> -X, so the
conditional cubic mean is zero; conditioning at most doubles nonnegative
moments. Per site the cost is C(b^2/beta + b/beta) plus log 2/(box) and the
boundary C l/b. At b = floor((beta l)^{1/3}) both terms are
O(beta^{-1/3} l^{2/3}).

**6.17 Sign obstruction (L366). HOLDS.** i j k = -1 and (-i)(-j)(-k) = +1, so
the trace changes sign; the cubic Taylor term Re(X_1 X_2 X_3) = -X_1.(X_2 x X_3)
is odd. The Cauchy-Schwarz estimate beta E[q Q^2] <= beta sqrt(1/beta)
sqrt(b^2/beta^2) = b/sqrt(beta) and the balance b = beta^{1/4} are right.

**6.18 (23) (L368-377). HOLDS.** Upper side O(beta^{-1/4} l) (see 2.7), lower
side from (22) at b = floor(beta^{1/4}) is O(beta^{-1/4} l + beta^{-1/2}); so the
two-sided error is e_beta. m ~ e_beta^{-1/4} in (6) gives
J_T <= C n^3 beta^{-3/16} l^{3/4}.

**6.19 Endpoint setting and OPEN items (L11, L403-411). HOLDS.**
Tr rho_T^2 = Tr F^{2T}/(Tr F^T)^2 = e^{-J_T}, so the wall is a purity lower
bound above 1650/1651, as stated. The scope list matches the proved
statements. The OPEN items are stated as open.

**6.20 GUIDE paragraphs (L3-7, L21-23). Not checked as proof** (they are not
proof steps). Local spot checks agree: the registry W entry (L892 of
`library/open-registry.md`) points to `t0-tree.md`; the check of row 720,
L19-22 and L92, keeps the identification of the subtraction, uniformity in the
cutoff and the physical unit. External line citations were not fetched. The
local PDF link at L23 was ignored as instructed.

## Step 7 result: guide runs (pure Python, run with -I, peak memory about 16 MB)

These are guides, not proof steps. Scripts: scalars.py, modes.py, mult.py,
cube4.py, misc.py in the session scratchpad (not in the repo).

- int_{R^3} f(|u|) du = 51.0032807976 = pi^5/6; times 6/(2 pi)^3 gives
  1.2337005501 = pi^2/8. sum_{h odd} h^-4 = pi^4/96. sum 2^{-k-1} 2^{-3k} = 8/15.
- (8): min_t (t x + c t^-3) matches 4 (c/27)^{1/4} x^{3/4} at x = 0.3, 1, 5 to 1e-7.
- Transverse multiplicity r(q) - 1: on open boxes 2x3x4, 3x3x4, 3x4x5 the
  nonzero spectrum of d*d equals the predicted multiset (23, 40, 74 values;
  max deviation 4e-13).
- Normalized per-box mode sum of (6), target pi^2/8 = 1.23370: m = 4 gives
  1.708 (b = 60) and 1.720 (b = 120); m = 8, b = 120: 1.3055; m = 12, b = 180:
  1.2554; m = 16, b = 240: 1.2395. It approaches pi^2/8 from above.
- Open 4-cube b = 3: curl rank 136 = 3b^4 - 4b^3 + 1; minimum projection
  diagonal 0.529 >= 1/6. Periodic 3^4: rank 240 = 3b^4 - 3; diagonal constant
  0.493827 = (1 - 3^-4)/2.
- G_inf = 0.5365910036, eta_inf = 0.863617 >= 24/29 = 0.827586;
  (3/16)(1 - G_inf) = 0.086889, above 9/106 = 0.084906 and below 3/32 = 0.09375.
  G_r by conjugate gradients: eta_2 = 0.863141, eta_3 = 0.863605,
  eta_5 = 0.863617; all >= 24/29. Ray recursion gives 6/29 exactly.
- Scalar subgroup example at beta = 10^4, b = 25: E w_k >= (E w_1)^k for all
  k <= b; E q_b^4 = 0.124 b^3/beta^2.
- a_beta(d) = 0.886 (beta = 100, d = 5) and 0.883 (beta = 400, d = 10).
- beta (1 - A(6 beta)) = 0.2498 at beta = 50 and 500 (vMF on S^3).
- (17) in R^2 with six unit rows at angles k pi/6 (sum L*L/6 = I/2): Monte Carlo
  E prod = 1.42 <= prod (E f^6)^{1/6} = 1.92.

## Step 8: verdict table and result

Scope remarks (not corrections).
(a) No statement fails. The two wording notes (L134, L148) change no proof.
(b) (4), (16) and (23) are density bounds: n^3 beta^{-3/16} diverges on the
physical grid, and the file says so (L262, L377, L411). (5) shows that no
short-period bound can be O(1).
(c) The (APR) discharge needs the geometric spacing set of Proposition MB and
beta(nu) = o(nu). (MONO-Delta), (BASE-Phi) and the spectral part of (W) stay
open, as the file says.
(d) The new (28) ranges rest on the equivalence of (28) with row 1149 (15)
(row 1151 Section 13), now backed by the check of row 1149 (row 1150).
(e) As in the check of row 1151, none of these estimates separates SU(2) from
compact U(1) at weak coupling; the file claims no selectivity.

| # | Statement (line in `library/gap-solve6-astra62.md`) | Verdict |
|---|---|---|
| 1 | Endpoint setting, J_T and the wall test (L11) | HOLDS |
| 2 | (1) and its conditional consequence (L15-19) | HOLDS |
| 3 | Separate error bars cost 2 B L^4 (L25) | HOLDS |
| 4 | One-plaquette tail E e^{beta q^2/4} <= C (L29-33) | HOLDS |
| 5 | Width-one rectangle bound C h/beta (L35) | HOLDS |
| 6 | (2) and the pointwise bound Q_e <= C b d (L37-41) | HOLDS |
| 7 | (3), statement (L45-51) | HOLDS |
| 8 | (3) upper: entropy step, good/bad split (L53-61) | HOLDS |
| 9 | (3) upper: holonomy positivity, even s (L63) | HOLDS |
| 10 | (3) upper: chart comparison, upper Gaussian side (L65-69) | HOLDS |
| 11 | (3) lower: forest gauge, restrictions, Schur complement (L71) | HOLDS |
| 12 | (3) lower: restricted Gaussian event, lower Gaussian side (L73-78) | HOLDS |
| 13 | (4) and (5), statements (L82-92) | HOLDS |
| 14 | (6) with multiplicity r(q) - 1 (L94-99) | HOLDS (guide run agrees) |
| 15 | Shell bound, monotonicity of J_s, proof of (4) (L101) | HOLDS |
| 16 | First limit of (5), integral pi^2/8 (L103-107) | HOLDS (guide run agrees) |
| 17 | Second limit of (5), factor 8/15 (L107) | HOLDS |
| 18 | (7) (L111-123) | HOLDS |
| 19 | Entropy loss of the upper step (L125) | HOLDS |
| 20 | (8) (L129-136) | HOLDS (wording note on L134) |
| 21 | Short-cylinder construction V_k (L140-148) | HOLDS (wording note on L148) |
| 22 | (9), statement, epsilon < 1/8 (L152-157) | HOLDS |
| 23 | (10) (L159-163) | HOLDS |
| 24 | g_b'(0) = d_b/(4b^4), p_V' = 3/4 + O(...) (L165) | HOLDS |
| 25 | Proof of (9) for both signs (L167) | HOLDS |
| 26 | Combination with full deletions (L169) | HOLDS |
| 27 | alpha < 3/80, tilted tails (L173-175) | HOLDS |
| 28 | Strips in the tilted law (L177) | HOLDS |
| 29 | (11) (L179-188) | HOLDS |
| 30 | Sampling and exponents for alpha < 3/80 (L190-197) | HOLDS |
| 31 | Limit of that sampling bound (L199) | HOLDS |
| 32 | (12), compression and rank (L203-222) | HOLDS |
| 33 | (13) and the rank lower bound (L224-230) | HOLDS |
| 34 | (14) (L234-245) | HOLDS |
| 35 | (15) (L247-252) | HOLDS |
| 36 | Convex example for the response norms (L254) | HOLDS |
| 37 | (16) (L258-264) | HOLDS |
| 38 | D_beta(n) <= C beta n^3 (L266) | HOLDS |
| 39 | (APR) discharge for Proposition MB (L268) | HOLDS |
| 40 | (17), Gaussian product inequality (L272-285) | HOLDS |
| 41 | Variance and mean of the clip (L287-289) | HOLDS |
| 42 | (18) and alpha < 3/40 (L291-304) | HOLDS |
| 43 | Limit of the improved bound (L306) | HOLDS |
| 44 | Dyadic tail and (19), statement (L310-315) | HOLDS |
| 45 | Patch cost, eta_r >= 24/29 (L317-323) | HOLDS (guide run agrees) |
| 46 | Negative-coupling moment (L325) | HOLDS |
| 47 | Range (3/16)(1 - G_inf), 9/106, 3/32 (L327) | HOLDS (guide run agrees) |
| 48 | (20) (L331-342) | HOLDS |
| 49 | Scalar subgroup example (L346) | HOLDS (guide run agrees) |
| 50 | (21) (L348-355) | HOLDS |
| 51 | Finite-period bridge obstruction (L357) | HOLDS |
| 52 | (22) (L359-364) | HOLDS |
| 53 | Sign obstruction for the Wilson marginal (L366) | HOLDS |
| 54 | (23) (L368-377) | HOLDS |
| 55 | (24) and the dimension bound (L381-391) | HOLDS |
| 56 | Exact first gap gives a diverging bound (L393-397) | HOLDS |
| 57 | Conditional count criterion (L399) | HOLDS |
| 58 | OPEN integral, purity form, scope (L403-411) | HOLDS |
| 59 | RESULT line (L413) | HOLDS |
| 60 | GUIDE paragraphs (L3-7, L21-23) | Not checked as proof; local spot checks agree |

Not checked: the external source lines cited in the GUIDE paragraphs (outline,
CA-I, Balaban's printed theorem). No proof step above depends on them.

RESULT: HOLDS - check of row 1153 (`library/gap-solve6-astra62.md`), checked
line by line by hand by Claude Opus 5.5 (max effort) as row 1154, positive
claims first. No statement FAILS. All PROVED statements HOLD, with two wording
notes (L134, L148). In particular: the two-sided comparison (3) with the tree
bound (2) (entropy upper bound with the penalty paid in the Wilson marginal,
holonomy positivity at even s, both Gaussian sides); the endpoint bound (4)
and its sharper form (23); the short-time law (5) with (6), the multiplicity
r(q) - 1, the integral pi^2/8 and the limit pi^2/15; the excess bound (16);
the (APR) discharge for Proposition MB on geometric spacings with
beta(nu) = o(nu), via D_beta(n) <= C beta n^3; the reformulation (24) and the
conditional count criterion; and the (28) ranges epsilon < 1/8 with
alpha < 3/80, alpha < 3/40, and alpha < (3/16)(1 - G_inf) (which contains
alpha < 9/106) on a dyadic tail. Guide runs agree with every constant
tested. These are density bounds and reformulations: an O(1) bound on J_T,
the strict inequality (28), (W) and the four-dimensional SU(2) mass gap
remain OPEN.
