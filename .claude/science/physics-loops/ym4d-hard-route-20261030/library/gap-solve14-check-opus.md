# Check of gap-solve14-astra62.md (FINISH row 1172)

Checker: Claude Opus 5.5, max effort, laptop subagent. Check of row 1171.
File under check: `library/gap-solve14-astra62.md` (506 lines).
Status: DONE. Written step by step as the check went; RESULT at the end. Checked by hand at the file's
commit `0debbdaa6`; numeric runs (scratch, outside the repo) are GUIDE only and enter no verdict.

## Plan (eight steps)

1. Read the file under check in full, and `library/gap-council-brief.md`.
2. Read the cited parts of rows 1159-1169 (`gap-solve9` to `gap-solve13`) and their checks.
3. Check the twist free-energy bound (33).
4. Check the strip-width majority rates pi^2/8 and pi^2/4, with (32).
5. Check the unanimity cost.
6. Check (2), (13)-(14), (28)-(30).
7. Check every other statement.
8. Verdict table, summary and RESULT line.

## Step 1. Reading (done)

I read all 506 lines of the file under check, in four ranges, and the council brief (122 lines).
I split the file into 99 statements, S1-S99 in file order. Equation tags run from (1) to (33).
The RESULT line (line 506) names as its positive claims: (33); the majority rates pi^2/8 (near cuts) and
pi^2/4 (distant cuts) at growing strip width, in the range widened by (32)-(33); the unanimity cost (27);
and (2), (13)-(14), (28)-(29), (30).
I check these first, in the order of the row. Line numbers below are lines of `library/gap-solve14-astra62.md`.

## Step 2. Cited prior rows (done)

I read in full row 1169 (`library/gap-solve13-astra62.md`, 426 lines) and the RESULT lines of the checks of
rows 1161-1169. Row 1170 (the check of row 1169) found no failure. I read the cited ranges of:
row 1155 (`gap-solve7`, (9): directional halving, c = 1/2 for faces sharing a direction, c = 1/8 in general);
row 1167 (`gap-solve12`, (1)-(2): full directional deletion with cost 1/z_beta per face; (9)-(10));
row 1161 (`gap-solve9`, (1), (13)-(14), the one-cube test s(u) <= 1/2 at some u <= n/512);
row 1141 (`gap-crux2`, (3)-(4): Pr{|u x n| <= t} <= M_b t^2 with M_b = 4(1+6b); D/4 is the smaller Gram eigenvalue);
row 1153 (`gap-solve6` L31-L35: one-plaquette bound E q(U_p)^2 <= C/beta and the width-one strip).
Each cited tag supports the use the file under check makes of it. Row 1169's (2), (5)-(9), (13), (14), (19)-(20),
(25)-(29) match the uses at L75, L121, L123, L130, L149, L270, L317, L321, L382, L391.

## Step 3. The twist free-energy bound (33) and its inputs (done)

The chain is (4) -> (6)-(8) -> (5) -> (9)-(10), and (4) + shared error -> (32) -> (33).
I checked each link by hand.

**S15. (4), L60-L68. HOLDS.** Turn the h direction into time (period p > h). The rectangle mean is the
h-th moment of nu_j/lambda_i under the weights lambda_i^p |V_ji|^2 / sum lambda^p, which do not depend on h
and sum to one (V is an isometry). Jensen for x -> x^h gives E w_{h,k} >= (E w_{1,k})^h. The same step in the
k direction gives E w_{1,k} >= (E w_{1,1})^k. With E w_{1,1} >= 1 - C/beta (row 1153 L31-L33) and Bernoulli,
1 - E w_{h,k} <= C hk/beta, and |1-U|^2 = 2(1-w). Zero lambda_i carry no weight since p - h > 0. The bound
||Ad q - I||_F <= C|q - 1| and the commuting-runs corollary are correct; the rectangle sides are below the periods.

**S17. (6), L77-L82. HOLDS.** C_b C_b^T = b^4 b^{-4} I = I. Each average in (6) is a contraction. With
y_4 = x_4 - 3r + r eps_4 <= x_4 - 2r and time-first paths, every link read by C_r(x) has base time <= x_4 - 1.
The depth is at most 3(b-1) + 4b in time and about 2b in space, inside 10b.

**S18. (7), L84-L90. HOLDS.** For displacement r e_i the parents y_eps with eps_i = 1 of x coincide with the
parents with eps_i = 0 of x + r e_i (also for i = 4). The other eight pairs are (y, y + 2r e_i). Path
mismatches are a bounded number of rectangle interchanges with sides <= Cr, so the error has L^2 norm
<= Cr/sqrt(beta) by (4); ||(T - T')C||_F <= ||T - T'||_F for a row contraction C. Hence
D_r <= (1/2) avg D_{2r} + e_r, and iteration gives 2 sqrt(3)/b + sum_r r^{-1} avg e_r, which is (7).

**S19. Nondegeneracy, L92-L96. HOLDS.** sum w_z = b^2 (top box mass b^{-2} b^4, preserved by averaging),
support <= C b^4, sum w_z^2 <= 1 by Minkowski, and >= 1/C by Cauchy-Schwarz. Reordering the accumulated path
after each scale costs a bounded number of rectangles of side O(r); the sum over scales is Cb/sqrt(beta). The
blockwise Cauchy-Schwarz with weights c_path gives E||C - C_*||_F^2 <= sum_z w_z^2 C b^2/beta. Weyl's bound and
Markov give Pr(s_b < 2 gamma) <= C b^2/beta when 3 gamma < sqrt(c).

**S20. Normalization, L98-L103. HOLDS.** F_l F_l^T = sin^2 I + cos^2 I = I. The polar factor is Lipschitz on
{s_min >= gamma} by the resolvent integral (DD^T)^{-1/2} = (2/pi) int_0^inf (DD^T + t^2)^{-1} dt; across the
cutoff sin alpha <= C |s - s'|. Left orthogonal transport commutes with every step.

**S21. (8), L105-L110. HOLDS.** var F_l <= C var C^[l] + cos alpha(s_l(x)) var F_{l/2}. The deterministic cost
C/l at l < b carries the factor 1{s_{2l}(x) < 2 gamma}, of L^2 norm <= (C/l) min(1, C l/sqrt(beta)). Summing
over dyadic l gives C/b + C log(2b)/sqrt(beta); the E_l terms give C log^2(2b)/sqrt(beta) by Minkowski.

**S22. Gaussian normalization, L112. HOLDS.** A eta is standard Gaussian, (I - A^T A) eta is independent of it,
E|g|^{-2} = 1 in dimension three, and |u/|u| - w/|w|| <= 2|u - w|/|u|. So the normalized mean square is at most
C||A - B||_F^2. Gauge covariance holds by rotating the Gaussian spaces at the source vertices.

**S16. (5) as stated, L70-L75. HOLDS.** It follows from S17-S22. The past restriction holds: F_b(x) uses only
C^[l](x), l <= b, which read base times < x_4.

**S24. The map, L123-L128. HOLDS.** The multiplier on a positive link from x uses v(x), which reads only links of
strictly earlier base time. Process the buffer layers first (their factors are known constants sigma_e), then
the layers from the time origin on. Each step is a left Haar translation by a function of already recovered
original links, so the map is a Haar-preserving bijection (Fubini, layer by layer). This needs a time period
larger than the profile height plus 10b; the hypothesis "every period > C_0 sqrt(1+beta)" with C_0 large gives it.
The central sigma for the collar version has plaquette product -1 exactly on the two normal stacks.

**S25. The cost (10), L130-L135. HOLDS.** Pulling factors to the base along original links gives
U'_p = B_eps U_p up to conjugation, with the four axes within d_p of v(base) (triangle inequality, Ad isometric).
Common axis: tau_p exp(i da_p) has angle pi rho_p mod 2 pi, for both eps (checked at o: pi(1 - rho_o) + pi).
Axis change costs <= d_p sum|a_e| in chord. Action change =
(1 - Re B) Re U_p + Im B . Im U_p <= (1 - Re B) + Im B . Im U_p, linear in B. The eps-average keeps only even
sine products; with a common axis they are real; replacing axes costs C d_p times C sum a_e^2. Then
2uv <= u^2 + v^2 and |Im U_p|^2 <= 2(1 - w_p). Summing with sum rho_p^2 <= R^{-2}, sum a_e^2 <= C log(2R) per
plane, (5) and E(1 - w_p) <= C/beta (from (4)) gives exactly the three terms of (10). Faces of other
orientations have zero common-axis angle because the profile is constant in directions 2, 3.

**S26. Cost to probability, L137. HOLDS.** -log zeta_h <= beta E_mu[S_tau(Phi U) - S(U)] for each map, by change
of variables and Jensen; averaging over maps keeps the bound. 0 <= -log zeta_h because
|Tr(h U^{2t})| <= Tr U^{2t} (h unitary, commuting) and Z_tw > 0. For the collar experiment the map fixes both
collars, so the joint relative entropy equals the one-path entropy and the odd tie rule exchanges the two
majorities; d(1-p||p) = (1-2p) log[(1-p)/p] <= (10). For q = min(p, 1-p) <= 1/4 this is >= (1/2) log(1/(2q))
(GUIDE run: minimum margin 0.20). At beta ~ log n the bound is O(n^2 (log log n)^5).

**S23. (9), L117-L121. HOLDS.** With R ~ sqrt(beta) and dyadic b ~ sqrt(beta), (10) is C m log^5(2+beta).
The rectangular and collar versions and -log p_h <= -2 log zeta_h + log 8 hold.

**S92. Shared error, L470-L474. HOLDS.** Each mismatch at scale r is bounded by rectangle chords of the parent
paths times the unit norm of the parent rows, so it does not depend on the top scale l > r; the averaging chain
below scale r is the same for every l. So one nonnegative E(x,y) with ||E||_{L^2} <= C log(2b)/sqrt(beta)
bounds ||C^[l](x) - T_xy C^[l](y)||_F - 2 sqrt(3)/l for all dyadic l <= b at once.

**S93. Interpolated rows, L476-L477. HOLDS.** Collapse both path families to T(x,z) (the prefixed edge is one
more run). The collapsed coefficients are (1-u) w + u w', with sum l^2, support O(l^4), so sum of squares in
[c, 1]. Blockwise Cauchy-Schwarz with total weight w^u_z gives E||D_l(u) - D_*(u)||_F^2 <= C l^2/beta; all
singular values of D_*(u) equal sqrt(sum (w^u)^2). Markov gives the claim, uniformly in u. The 3D version
(l^{3/2}, O(l^3)) is right. (The phrase "as in (7)" at L477 means the nondegeneracy estimate after (7).)

**S94. Smooth cutoff, L479-L485. HOLDS.** alpha(gamma) = 0 and alpha(2 gamma) = (pi/2) eps (e^A - 1) = pi/2 since
e^A = 1 + 1/eps. alpha' = (A/gamma)(alpha + (pi/2) eps) <= (A/gamma)(pi/2)(sin alpha + eps) by alpha <= (pi/2) sin
alpha on [0, pi/2], and A = log(1 + sqrt(N)) <= C(1 + log N). (GUIDE run: ratio exactly 1 at the right end, for
N = 1 ... 1024.) The bottom path cos(pi u/2) F_1(x) + sin(pi u/2) T_xy F_1(y) has isometric rows because the
two one-vertex source blocks (at x - 4e_4 and y - 4e_4) are distinct; its speed is (pi/2) sqrt(3).

**S95. Proof of (32), L487-L494. HOLDS.** With ||P||_F^2 = ||F_{l/2}||_F^2 = 3 constant, the cross terms vanish
and ||F_l'||^2 = 3 alpha_l'^2 + sin^2 alpha_l ||P_l'||^2 + cos^2 alpha_l ||F_{l/2}'||^2 a.e. (F_l(u) is
Lipschitz in u, so the fundamental theorem of calculus applies). |s'| <= ||D_l'||_F, ||P_l'|| <= C||D_l'|| where
sin alpha_l > 0, and ||D_l'||_F <= 2 sqrt(3)/l + E is constant in u. Unrolling with w_l = prod_{q>l} cos^2
alpha_q: sum w_l sin^2 alpha_l = w_b - (bottom weight) <= 1 and eps^2 sum w_l <= eps^2 N = 1, so E contributes
C(1 + log N)^2 E^2. The C/l^2 terms carry w_l <= 1{s_min(D_{2l}(u)) < 2 gamma} for l < b, with expectation
<= C l^2/beta by S93; summing gives C(1 + log N)^2 [b^{-2} + N/beta]. Cauchy-Schwarz in u and the Gaussian step
of S22 give (32), since N <= C log(2b) and 1 + log N <= C[1 + log(2 + log b)].

**S96 (first part). (33), L496. HOLDS.** At b, R ~ sqrt(beta): beta E d_p^2 <= C J^2 (beta/b^2 + L^2) = O(L^2 J^2),
using log(2b) <= C L_beta and 1 + log(2 + log b) <= C J_beta. Plus the plaquette term O(1). Times
sum a_e^2 = O(L_beta) per plane over m planes, plus beta m/R^2 = O(m): -log zeta_h <= C m L^3 J^2. The collar
version follows the same way.

**S91. Statement of (32)-(33), L454-L468. HOLDS.**

## Step 4. Majority rates pi^2/8 (near cuts) and pi^2/4 (distant cuts), with (32) (done)

Inputs first: (11), (16)-(17), then (22)-(23), the fillings, (30)-(31), and the widened range.

**S28. Geometric lower cost, L151. HOLDS.** By (1) the kept edges differ by a sign whose coboundary vanishes on
clean faces; it is flat at both endpoints, so on the event in (11) every parallel line has negative relative
endpoint product. Stokes on the clean part of each 14 ribbon forces relative sign -1 around the 1 x k
rectangle, whose boundary edges are kept. Antipodal holonomies give theta + theta' = pi; nonabelian Stokes on
the strip and bi-invariance give a total of 2k angles >= pi; with 1 - cos u >= 2u^2/pi^2 and Cauchy-Schwarz
the deficit sum is >= (2/pi^2)(pi^2/(2k)) = 1/k per rectangle.

**S29. L153. HOLDS.** The km faces share directions 1 and 4, so row 1155 (9) applies with c = 1/2 (halving,
cost z_{beta/2}/z_beta per mark). Cauchy-Schwarz on the two marginals and Markov give
-log p >= beta m/(4k) - km log C.

**S30. Matching map, L155. HOLDS.** Angles pi(1 - i/k) on sites 1..k-1, zero at 0 and k: all k residuals are
pi/k (face 0: pi(1 - 1/k) + pi = -pi/k mod 2 pi). Squared residuals 2 pi^2 m/k, squared angles ~ (2/3) pi^2 mk.
The disclosure is preserved: the central cut is flat on slices, kept temporal edges and spatial plaquettes are
unchanged, and the only face with a central discontinuity contains the omitted link at site 1. The (5) axes
read only earlier layers, so the triangular map of S24 applies (the buffer hypothesis is in L142).
Pr(Z = Z') = E sum w_z^2 >= 1/8; the image has Pr(difference h) >= 1/8; D >= Q(E) log(1/P(E)) - log 2.

**S27. (11), L142-L149. HOLDS.** Lower bound from S28-S29, upper bound from S30 and (10)-type costs
(beta E d_p^2 <= C log^4(2+beta) at b_* ~ sqrt(beta)). The two-sided order statement for
2 <= k <= c_0 sqrt(beta)/log^2(2+beta) follows.

**S40. Compression, L210. HOLDS.** All coarse edges (long products, kept temporal and transverse links) have
shared adjoints. Exactly 2m coarse 14 faces contain omitted links. Other coarse faces tile by 1 or k fine faces
with shared adjoints.

**S41. (17), L212-L218. HOLDS.** A clean coarse face in B has a negative fine witness (abelian Stokes); at most
k^{max d_i} witness choices; distinct witnesses share a direction; opposite traces give deficits summing to 2;
row 1167 (1) (full deletion, z_beta^{-1} per face) and Cauchy-Schwarz give (e^{-beta}/z_beta) per witness.
z_beta >= c(1+beta)^{-3/2}, so log H = -beta + O(log(2+beta)) for k <= sqrt(beta).

**S42-S46. (16) and its proof, L202-L208, L220-L234. HOLD.** Hole case: >= m/2 antipodal rectangles give
deficit >= m/(2k) on the fixed 2km fine faces; S29 gives exp[-c beta m/k + Ckm]. Component case: kept
components are closed; compact small ones have equal parity on both arcs (their pairing with the whole time
torus is zero); a negative line gives a kept 14 face on each of its two ribbons, so >= m kept 14 faces, >= m/2
clean when |D cap B| < m/2. The split H^{max d_i} <= H^{(s+gamma) d_1 + eps |S|/2} and the counts
C_K n^3 H^{6 gamma} = n^{3 - 6 kappa gamma + o(1)} = o(n^2), C n^4 sum_j (C_1 H^{eps/2})^j = o(1), and the rooted
forest bound 2^{2m} 2^{j+2m} C_3^{j+2m} (breadth-first cells are connected and contain one root) are right. The
upper bound uses the S30 map, which fixes all raw adjoints.

**S56. Least cost of antipodal boundaries, L295. HOLDS.** If x + y <= pi then cos x + cos y <=
2 cos((x+y)/2). Each average of a largest and a smallest angle lowers the squared-deviation sum by half their
squared difference, so the angles converge to the mean and the minimum of sum(1 - cos) at total u <= pi is
l(1 - cos(u/l)). (GUIDE run: 20000 random cases, no violation.) For two paths, l = 2k and u = pi give 2 a_k. For (22): all 2m rectangles are
negative, total deficit >= 4 m a_k; full deletion on the 2km faces and Cauchy-Schwarz give
-log p >= 2 beta m a_k - 2km log(1/z_beta), and km log(1/z_beta) = o(beta m a_k) iff k^2 log(2+beta) = o(beta).

**S57. Joint count, L297-L301. HOLDS.** Witnesses of clean direction-1 faces and all fine faces of the r dirty
rectangles are disjoint and contain direction one. Deficit on the marks >= 2 d_1^c + 2 a_k r. Full deletion and
Cauchy-Schwarz give H^{d_1^c}(z_beta^{-k} e^{-beta a_k})^r. The dirty loss k log(1/z_beta) is o(beta a_k) under
k^2 log(2+beta) = o(beta). Interpolating with H^{j_c/2} is legitimate (min(A,B) <= A^{1-theta} B^theta).
On N_- >= dm, d_14^c + r >= 2dm.

**S58. Lower rate in (23), L303. HOLDS.** For a small clean component off D: d_1 >= 4 + d_14, d_14 >= 2, so the
unspent exponent is (1-eps) d_1 - z d_14 >= 6(1-eps) - 2z, and kappa[6(1-eps) - 2z] > 1 gives placement cost
n^{3 - (1+xi')} = n^{2-xi}. Large and D-meeting components cost exp(O(m)). Rate >= 2dz for every
z < min(a_k, 3 - 1/(2 kappa)) (a_k <= 1 always; GUIDE: a_1 = 1, k a_k in [1, pi^2/8]). At k -> infinity,
z = (1 - 2 eps) a_k and beta m a_k >> m. N_-/m -> 0 in probability follows.

**S59. Spatial axes and frames, L305. HOLDS.** The 3D version of (6)-(8) has C C^T = I with top weight
b^{-3/2}, sum w = b^{3/2}, support O(b^3), and the same half-overlap; (4) holds on the slice. For (22), the frame
w(P) Im P, w(Q) Im Q and their cross product is invariant under P -> -P and gauge covariant. By the fibre theorem
the observation fixes every gauge-invariant function of the spatial adjoint connection, so the rotations in
local frame coordinates are functions of the observation.

**S60-S61. Fillings and common bijection, L307-L309. HOLD.** Path 1: a(i) = pi i/(2k); path 2: a(0) = 0,
a(i) = pi - pi i/(2k), with the central cut through face 0. Both reach pi/2 at site k and share the ramp, so
all kept temporal edges get the same rotation. Residuals: pi/(2k) inside (path 2, face 0:
pi - pi/(2k) + pi = -pi/(2k) mod 2 pi), pi/(2w) on the ramp. The axes use only spatial adjoints, which central
factors do not change, so both maps are Haar preserving and induce the same bijection j; on clean faces the
transformed trace is fixed by the observation and the common rotations.

**S62. One-path entropy, L311. HOLDS.** exp(-eps a_x v) exp(eps a_y v') has real part
cos(a_y - a_x) - sin a_x sin a_y |v - v'|^2/2 (independent of eps) and eps-averaged imaginary part
-sin a_x sin a_y (v x v'), of size <= |sin a_x sin a_y| |v - v'|. With E|v - v'|^2 <= C log^4(2+beta)/beta and
Cauchy-Schwarz against |Im U_p|, beta times the mean increase is <= beta[1 - tau cos(a_y - a_x)] +
C|sin a_x sin a_y| log^4(2+beta). Ideal cost k beta(1 - cos(pi/(2k))) = beta a_k per rectangle, two per line per
path; ramps O(beta/w); axis error O(M(k+w) log^4) = o(beta M a_k) iff k(k+w) log^4 = o(beta), true for
w ~ sqrt(beta)/log^2 and k log^2/sqrt(beta) -> 0. Band sides: C beta n(k+w) and C beta n s, both
o(beta m a_k) when k(k+w) = o(n) and s = o(n/k).

**S63. Marginal entropy subtracted, L313-L317. HOLDS.** u = arccos|w(H)| is a function of the observation.
V <= sum of plaquette deficits by S56, so log E_{mu_O} e^{beta V} <= 2kM log(1/z_beta). In the image of path 1,
H' = (transported pure unit) H, so |w(H')| <= |Im H| for any axis, and E|Im H| <= E|1 - H| <= C sqrt(k/beta) by (4).
f(u) = k(1 - cos(u/k))/a_k has f(pi/2) = 1 and Lipschitz constant sin(pi/(2k))/a_k <= pi/2 (as k a_k >= 1; GUIDE: the supremum is 4/pi), and
pi/2 - u = arcsin|w(H')| <= (pi/2)|w(H')|. So E V >= (2 - o(1)) M a_k uniformly; Donsker-Varadhan gives the bound.

**S64. Chain rule and upper rates, L319. HOLDS.** For fixed auxiliaries and sign, Q has observation law j_* mu_O
and conditionally independent transformed paths; D(Q||P) = D_1 + D_2 - D_O is exact. Average:
<= 2(2 + o(1)) - (2 - o(1)) = (2 + o(1)) beta M a_k. In (22) directions 2 and 3 cannot disagree (clean ribbon
outside the strips after moving the lines by endpoint flatness) and direction 1 disagrees with probability
<= exp(-c beta m/k + Ckm) by (11); path 2's central cut flips exactly Z_1. In (23) the band reverses exactly M
lines and N_-/m -> 0 before. The binary inequality then gives the upper rates.

**S65. Microscopic branch and physical slope, L321. HOLDS.** This is row 1169 (25) under the raw two-strip
observation (made from the first path's adjoints; the checkerboard selection needs the even grid). Rate
d(6 - 1/kappa) = 2d(3 - 1/(2 kappa)). At kappa = 11/(3 pi^2) = 0.3715 > 1/4 (conditional on the account's flow
premises), 3 - 1/(2 kappa) = 1.654 > 1 >= a_k, and a_k ~ pi^2/(8k).

**S55. (22)-(23), L284-L293. HOLD.** (22): lower S56, upper S59-S64 with M = m. (23): lower S57-S58, upper the
band (S60-S64, d' down to d) and S65. At d = 1/2 and growing k: 2 (1/2) beta n^2 pi^2/(8k) =
(pi^2/8 + o(1)) beta n^2/k. The strict-threshold and tie-rule remark holds.

**S86-S88. (30) lower bound, L441-L445. HOLD.** Subtracting compact primitives of discarded components keeps the
symmetric difference A_0 xor A_t (even pairing means equal endpoint windings mod 2), so |A_0 xor A_t| = N_-.
Each parity change across a transverse edge or a time step needs a kept direction-1 face on that strip; inside
an interval these are clean. With eta = min(d,e)/4, one endpoint set has fraction in [eta, 1 - eta] (else
N_- < 2 eta m <= dm/2 or N_- > (1 - e/2) m). If J < eta m/2 every layer of that interval (>= s_* layers) has
fraction in [eta/2, 1 - eta/2], hence >= c_eta n boundary edges (>= eta n/4 mixed rows, or a full and an empty
row, so two changes in each column). So J >= c n s_*, paid by H^{alpha J}; together with the (23) bound at
threshold d this gives c beta(m/k + n s_*), using beta m/k >> m.

**S89. (30) upper bound, L447. HOLDS.** The S30 map on a band of fraction in (d, 1-e), only on the shorter
interval: interior cost O(beta m/k + mk log^4), band sides C beta nk (no ramp: boundary angles zero) and
C beta n s_*. Raw adjoints are fixed. N_- = o(m) before (count before (27)), so the image event has probability
-> 1.

**S90. (31), L449. HOLDS.** If k s_*/n -> infinity, (30) makes the middle event cost >> beta m a_k; the event
N_- > (1-e) m costs >= (2(1-e) - o(1)) beta m a_k by S58 at any separation; (27) gives the reverse. Hence
(2 + o(1)) beta m a_k for every fixed d, and at growing k this is (pi^2/4 + o(1)) beta n^2/k. The conditional
convergence follows by division.

**S85. Statement of (30)-(31), L428-L439. HOLDS.**

**S96 (second part). Wider range k L_beta J_beta = o(sqrt(beta)), L496. HOLDS.** With (32) the axis error per
face is O(L^2 J^2/beta). With w ~ sqrt(beta)/(L J): k w L^2 J^2 = k sqrt(beta) L J = o(beta); ramps
beta/w = o(beta/k); full deletion k^2 L = o(beta); (11) and the count before (27) need only k = o(sqrt(beta));
the (30) interior error becomes mk L^2 J^2 = O(beta m/k). The band sides need k(k+w) = o(n), as before.

## Step 5. The unanimity cost (27) (done)

**S77. Lower bound and quantitative tail, L384-L389. HOLDS.** The lower-bound proof of (23) uses only the two
complementary ribbons and support costs, not the separation s, so it holds at d = 1 for any separation. With
z = c_kappa a_k, c_kappa < 1 - eps and kappa[6(1-eps) - 2 c_kappa sup_{k>=2} a_k] > 1 (that sup is a_2 < 1), the
extraction exp(-beta z (d_14^c + r)) with d_14^c + r >= 2r gives
Pr(N_- >= r) <= exp[-2 c_kappa beta a_k r + C_kappa m + O(n^{2-xi})], with counts independent of r. At
l = ceil(m/sqrt(beta)) the exponent is -m(2 c_kappa sqrt(beta) a_k - C_kappa) -> -infinity iff
sqrt(beta) a_k -> infinity, i.e. k = o(sqrt(beta)).

**S78. Upper bound, L391. HOLDS.** The two fillings on all m lines have no transverse boundary; the central cut
is flat on every slice of the intervening interval, so S62-S64 hold for any separation and give
-log Pr(N_- >= m - l) <= (2 + o(1)) beta m a_k. Sign repair: for a fixed exception list S, flipping one observed
longitudinal link per line by the center keeps every adjoint (so the second path's conditional law), reverses
exactly those lines, and changes the first-path density by at most e^{12 beta |S|} (six plaquettes, oscillation
two each). The map is injective on the event with that list. Hence
Pr(N_- = m) >= e^{-12 beta l} Pr(N_- >= m - l)/(m+1)^l, an extra cost 12 beta l + l log(m+1) = O(m sqrt(beta)),
which is o(beta m a_k) iff k = o(sqrt(beta)). The checkerboard branch (row 1169 (25), all m lines) gives the rate
2[3 - 1/(2 kappa)].

**S76. (27), L377-L382. HOLDS.** At growing k: 2 beta n^2 pi^2/(8k) = (pi^2/4 + o(1)) beta n^2/k. The remark on
row 1169 (26)-(29) is accurate.

## Step 6. (2), (13)-(14), (28)-(29), (30) (done; (30) is S86-S89 above)

**S13. Proof of (2), L47. HOLDS.** K_t >= 0 pointwise, vertex-gauge invariant at each end and invariant under
diagonal flat flips. By the fibre theorem the array fibre is 8 deck translates of equal Haar weight. With
winding-positive representatives, the fibre pair (g_1 x, g_2 y) has weight K(x, g_1 g_2 y)^2, so
w_z = k_z^2 / sum_v k_v^2. Tr(h U^{2t}) = int int K(x,y) K(x,hy) by diagonal invariance; disintegration gives
zeta_h = E_nu sum_z k_z k_{z+h} / sum_v k_v^2 = E_nu sum_z sqrt(w_z w_{z+h}). Independence gives p_h.
sum u_z^2 >= (sum u_z)^2/8 and u_z <= (w_z + w_{z+h})/2 <= 1/2 for h != 0; then Jensen.
(GUIDE: on a toy space of 6 x 8 states the kernel of L274 reproduces the zeta_h formula and the identity
zeta_h = E sum sqrt(w w) to all six printed digits, and satisfies both inequalities.)

**S12. (2), L39-L45. HOLDS.** The comparison with row 1161 (1) (stationary reference plus s_+ term) is accurate.

**S14. (3), L49-L55. HOLDS.** From (2): -log zeta + log 2 <= -log p <= -2 log zeta + log 8 for each b, so the two
lower limits vanish together. With row 1161's one-cube neutral input, row 1161 (13) is exactly the zeta form.
The remark about flipping finitely many line signs is right (a flipped link changes the sign of each nonzero
incident plaquette trace).

**S33. Regular cells, L179. HOLDS.** Deterministic, finite partition, independent of the law.

**S34. (15), L181-L189. HOLDS.** |H| <= 6 beta (six staples); Phi(s) >= c e^s (1+s)^{-3/2} on the cap of radius
(1+s)^{-1/2}, so the density is <= C(1+beta)^{3/2}, also with seam signs. A simple loop trace has Haar density
(2/pi) sqrt(1 - w^2) <= 2/pi. For the frame pair, the two private links can share a 23 plaquette, but the stated
order (marginal bound of the first = average of its conditional bounds, then the conditional bound of the
second) gives C(1+beta)^3 domination. Under Haar the squared projection of Q on the 2-plane orthogonal to 1 and
a is uniform on [0,1], and E|a|^{-2} < infinity, so Pr(|a x b| <= u) <= C u^2. Summing: e_n = o(1) for
rho = n^{-5}, beta = O(log n).

**S35. Stability within a bin, L191. HOLDS.** Entries of M and G move by C eps. The 2 x 2 Gram block has
lambda_min >= det/trace >= |a x b|^2/2 and the third eigenvalue is |a x b|^2, so lambda_min(G) >= c rho^2 in the
bin (C eps << rho^2). The resolvent integral gives ||Delta G^{-1/2}|| <= C rho^{-3} eps, and (1) gives framed
links within delta = C rho^{-4} eps. Nearer lifts are within C delta (sin(u/4)/sin(u/2) <= 1/sqrt(2)). Face signs
are flat because a sign -1 would need 2|w_p| <= eps + C delta < 2 rho. Winding traces of every member are
>= 2 rho - C n delta >= rho by comparison with the good member (the winding traces are not binned, and the
argument does not need them binned). Equal labels then give trivial cohomology.

**S36. Proof of (13), L193. HOLDS.** For matched configurations only the endpoint spatial half action and the
adjacent temporal plaquettes change, O(n^3) traces by <= C delta each, pointwise in the internal variables, so
K moves by e^{C beta n^3 delta} with delta = C n^{-80}. On a cell pair |K - rms| <= (e^eta - 1) K, so
||K - K~||_HS^2 <= (e^eta - 1)^2 + 2 e_n. The cell entries are sqrt(Pr(Ba, Cd)) = sqrt(Pr(B, C, Z = a+d)/8) by
diagonal flip symmetry; the 8 labelled cells of a bin have equal Haar mass. ||K||_op = X^{-1/2},
||K E_+||_HS^2 = X_+/X, E_G is E_+ on the cell span, and X_+ >= X/8 because each Tr(g U^{2t}) >= 0. The ratio
statement follows since the denominator is >= 1/sqrt(8) - o(1). D is symmetric because the two arcs have equal
length.

**S37. Proof of (14), L195. HOLDS.** On a regular bin pair each w_z is within e^{+-4 eta} of its conditional
average Pr(Z = z | B, C) (tower property). Restricting the numerator of the kernel identity to regular pairs
gives zeta_h times the probability of a regular pair under the positive h-twisted path measure, which is
>= 1 - 2 e_n by (15) (both endpoints are slices of the twisted torus, and regularity is flip invariant). No
division by zeta_h occurs, so the error is relative. The collision-sum corollary follows by Jensen.

**S32. Statement of (12)-(14), L162-L177. HOLDS.**

**S80. Block failure, L403. HOLDS.** Pr(D_z <= u) <= C(1+beta) u from row 1141 (3)-(4) (union of the two cases,
M_b = 4(1+6b)). For u = c_*/b^2 and b^2 >= 1+beta, Pr(bad) <= 2^J [C c_*(1+beta)/b^2]^{J/2}
= exp[-(J/2)(log(1/(4 C c_*)) + log(b^2/(1+beta)))] <= exp(-c b^3 H), with a constant as large as needed by
the choice of c_*. Products over prescribed blocks follow by successive conditioning on pin bonds.

**S81. Block energy, L405-L409. HOLDS.** At a good pin, (c_*/b^2)|v_z|^2 <= 4 (vector energy of its 8 bonds).
With f = |v|, Poincare on the box (variance <= C b^2 times edge energy, and ||v_x| - |Ad v_y|| <= |v_x - Ad v_y|)
and f-bar^2 <= 2 f_x^2 + 2 (f_x - f-bar)^2 averaged over the good pins (a fixed fraction of the block) give
b^{-2} sum_B |v|^2 <= C E(B). The identity |B|(1 - S_B^2) = sum |v|^2 + sum (s - S_B)^2 holds since
s^2 + |v|^2 = 1. The union of two neighbouring blocks, with the seam sign, gives
b |S_B - h S_B'|^2 <= C E(B cup B').

**S82. Block cycles, L411. HOLDS.** Short cap-to-cap dual paths of length L force L/8 bad blocks; with the path
count C(n/b) 16^L the layer failure is exp(-c b^3 H n/b); at least half the n/b layers succeed except with
probability 2^{n/b} exp(-c b^3 H (n/b)^2/2). Each good odd-winding block cycle costs an absolute constant in the
displayed sum (all |S| < 1/2, or a jump >= 1/4, or an intermediate value with |S| <= 1/2). c (n/b)^2 cycles times
b gives E_h >= c m/b.

**S79. (28), L396-L401. HOLDS.** At b = sqrt(1+beta) and at b = c n it recovers and improves (25) and (26).

**S84. Proof of (29), L423. HOLDS.** The one-link affinity is int e^{(beta/2)(U + U').Y} dY / Phi(beta) =
Phi(beta u)/Phi(beta), |U + U'| = 2u. (log Phi)' is a tilted mean of Re q, increasing, in [0,1], and >= c_0 > 0
on [1/2, infinity); the interval argument and d^2/8 <= 1 - u <= d^2/4 give c beta d^2 <= -log <= C beta d^2
(GUIDE: ratio in [0.030, 0.247] over beta in [1, 1000]). The edge sum of d^2 at gauge g is E_h's sum at g^{-1}
by bi-invariance. Jensen and the mean in (25) give the lower bound; (28) at b = max(8, ceil(sqrt(1+beta)))
split on its event gives the upper bound.

**S83. (29), L413-L421. HOLDS.**

## Step 7. Every other statement (done)

**S1. L3. GUIDE.** Plan of the row; no claim.

**S2. L5. GUIDE.** I re-read the local citations on main `8b11ae2bb9`: `research/mass-gap/library/gap-phys-seed.md`
L311-L319 holds Theorem ZD-c with (PHYS-SEED), (Z-SEED) and (BDD-Delta)/(Z-UNB); the finite Peter-Weyl note
L25-L27 bounds a static-source energy from above; the two-region note at L397 starts the fine posterior density
used in its response estimate; registry row W (line 892 of `library/open-registry.md`) points to the T0 tree.
These match. The PR-branch line ranges were not re-read.

**S3. L7. GUIDE.** External outline and account lines not re-read; credits to Sussman and Alpoge, Balaban and
Chatterjee are present.

**S4. L9. OPEN.** The seed 1/1650, (W) with 256 D_0 + 30 and L >= 4 L_0, and the equivalence agree with the
council brief and row 720 (S2).

**S5. L11. GUIDE.** An accurate map of the equations.

**S6. L15. GUIDE.** Accurate orientation (fundamental words, not row 1155's column contraction or row 1167's
adjoint collar).

**S7-S9. Fibre theorem, L17-L30. HOLD.** (P - P^{-1})/2 = Im P, (PQ - QP)/2 = Im P x Im Q, u.v = -Re(uv), so each
entry of M_e is a sum of traces of contractible words P_x U_e P'Q'_y U_e^{-1} of length <= 4+4+1+8+1 = 18.
a.b = w(P)w(Q) - w(PQ); det B_x = |a x b|^2 > 0 a.s. (private links, Haar-null commuting set, positive density).
V_x = B_x G_x^{-1/2} is in SO(3) (orthogonal, positive determinant), so (1) holds. Equal data give
R_x = V'_x V_x^T matching the adjoint links; lifted gauges leave a sign cochain that is closed (equal nonzero
plaquette traces), hence a vertex gauge times a flat flip. The converse is clear.

**S10. Ribbon, L32. HOLDS.** Matching by (1) on the ribbon, closed relative signs on its faces, and Stokes on
the annulus give equal products of the two boundary winding signs.

**S11. L34. HOLDS.** U(1) flat shifts, finite groups (identity patch with positive probability) and spectator
products are correct separation statements; no numbers are claimed.

**S31. L157. HOLDS.** Binary inequality D >= Q(E) log(1/P(E)) - log 2 with P(E) <= exp(-c beta m/k + Ckm).

**S38. L197. OPEN.** The two stated implications are right: a ratio limit above sqrt(2/3) means
limsup X_+(2t) < 3/2, and 2t = 2 floor(n/1024) <= n/512 is in row 1161's test; X(2t) - 1 < 1/2 with
q = floor(n/(4t)) >= 256 gives X(2tq) - 1 <= 2^{-256} and, by monotonicity at 2tq <= n/2, the seed.

**S39. (16), L202-L208. HOLDS** (S40-S46).

**S47. (18), L239-L243. HOLDS.** Flat endpoint signs make the relative winding common to all lines; a clean
ribbon then gives relative sign -1 around each patch; nonabelian Stokes for a simply connected patch (tree-cotree
argument) gives 2A angles summing to >= pi, deficit >= 1/A per patch; directional halving on the <= Am faces and
Cauchy-Schwarz give p_*.

**S48. (19), L245-L250. HOLDS.** Pre-update disagreement <= M p_* (drop the selection probability in each of the
M terms); post-update >= q - M p_*; the comparison completion keeps its reference conditional law since the
selected disclosure is preserved; relative entropy of (index, path) is <= D(mu~||mu) + log M; binary
contraction finishes.

**S49. L252. HOLDS.** M <= C n^2 exp(C_K m + C A m). Under A^2 = o(beta), beta/A -> infinity and log n = o(beta m/A),
so M p_* -> 0 and log M = o(beta m/A); (19) gives c_q beta m/A.

**S50. (20), L257-L261. HOLDS.** The restricted squared HS norm is the pair probability of the listed bins. Given
everything else the >= c n^3 selected private links are independent with tilted densities <= C(1+beta)^{3/2};
each selected trace hits a width-n^{-100} interval with probability <= C(1+beta)^{3/2} n^{-100}. A union over J.

**S51. L263. HOLDS.** A reading-preserving update stays in the fibres (gauge orbits times flat flips), so it fixes
every bounded invariant function a.s.; a plaquette trace has positive variance.

**S52. (21), L265-L270. HOLDS.** If beta sum d^2 < log beta, each centred square of radius j <= beta^{1/4} has
residual sum <= C j sqrt(log beta/beta) = o(1); with the central sign the boundary holonomy is o(1) from -1,
so its O(j) edge angles sum to >= pi/2 and cost >= c/j; summing over j gives c log beta. The abelian floor is
row 1169 L297-L301, with E(1 - w_p) >= c/(1+beta).

**S53. Comparison kernel, L272-L277. HOLDS.** P >= 1 - f(x)f(y) > 0; row sums are 1 since labels are uniform given
the quotient; the bracket is the sum of the seven nontrivial characters; the functions chi(l) f are orthogonal with
norm^2 v; so P^t = 1 + v^{t-1} f f [8 1 - 1] and zeta_h = (1 - v^{2t})/(1 + 7 v^{2t}) (GUIDE: exact on a toy).

**S54. Two examples, L279. HOLDS.** Constant f: entries 1 + 7L and 1 - L, p_h ~ (t delta)^2, zeta_h ~ t delta,
ratio of logs -> 2. Rare set: pairs meeting it have mass (2 delta - delta^2)/(1 + 7 v^{2t}) and collision 1/8,
the rest O((t delta)^2) (needs t^2 delta -> 0, true at delta = e^{-sigma n}), so p_h ~ delta, ratio -> 1.

**S66. L326. GUIDE.** Accurate.

**S67-S72. (24)-(25), L328-L354. HOLD.** The term identity (s_x - h s_y)^2 + |v_x - h Ad v_y|^2 is exact. Pins: row
1141 gives Pr(D_z <= u) <= C(1+beta)u; at a good root delta|v_z|^2 <= 4 (energy of its 8 bonds); the 23 pins avoid
the cut. Dual paths: length >= c_0 n, cost < c_0 n/2 forces L/8 bad roots; count C n 16^L; disjoint pins per layer.
Distance level cuts are edge disjoint, unit cost, and odd on cap-to-cap paths, so they contain odd-winding cycles;
at most two per root. Crossing energy: antiperiodic s; either potential c n delta, or a jump >= 1/4, or
1/(j+1) + 3 delta j/4 >= c sqrt(delta); n > C_0 sqrt(1+beta) makes c n delta >= c sqrt(delta). Mean bound: the ramp
gauge cos theta + v sin theta, with the spatial axes, costs C m [1/w + w log^4(2+beta)/beta], optimal at
w ~ sqrt(beta)/log^2.

**S73-S75. (26), L357-L372. HOLD.** Upper: at most half the N tubes have energy > K/n; antiperiodic scalar with
jumps < 1/2 gives a point with |s| <= 1/4 and L sites with |s| < 1/2, so |v|^2 >= 3/4 and D_z <= CK/n; the count
2^N n^{N/2} [CK(1+beta)/n]^{L N/2} is exp(-c_A n^3 log n). Lower: j i j^{-1} = -i (indeed i j i = j), a chord ball of
radius c_A/n costs 3n^3 (2c_A/n)^2 <= A n, and one-link conditional densities are >= e^{-12 beta}.

**S97. L501. HOLDS.** With pi the actual periodic one-slice marginal and f = sqrt(v) constant, the two end
quotients are independent with the actual quotient marginal, P^{2t}(x,x) = 1 + 7 v^{2t} is constant so the slice
marginal is pi, and the neutral spectrum is {1, 0}. v = 1 - e^{-sigma n} gives -log zeta_h = sigma n + O(log n);
v = 1/2 gives zeta_h -> 1. Reading note: "the exact quotient-pair law" means the common (product) pair law of
the two examples, not the Wilson one; the next sentences say so.

**S98. L503. OPEN.** The margins 1/32 and 8/25 match row 1167 (10); the fixed-coupling condition matches row
1161 (13). The list of obstructions is accurate.

**S99. RESULT, L506. HOLDS as a summary.** Reading note: the two majority rates and the unanimity rate are for the
raw-adjoint two-strip disclosure of (16), (23), (27), (31), with "nearby" meaning s = o(n/k) and "distant" meaning
k s_*/n -> infinity, in the range k L_beta J_beta = o(sqrt(beta)) that (32) permits; they are not collar-only
rates (those are bounded by (9) and (33), far below beta n^2/k in this range).

## Step 8. Verdict table, counts and RESULT

| Statement | Lines | Verdict |
|---|---|---|
| S1 plan | L3 | GUIDE |
| S2 repo search | L5 | GUIDE (local main citations match; PR ranges not re-read) |
| S3 credits | L7 | GUIDE (external lines not re-read) |
| S4 wall | L9 | OPEN (restatement agrees with row 720) |
| S5 map | L11 | GUIDE |
| S6 orientation | L15 | GUIDE |
| S7-S9 fibre theorem, (1) | L17-L30 | HOLD |
| S10 ribbon product | L32 | HOLDS |
| S11 role of SU(2) | L34 | HOLDS |
| S12-S13 (2) and proof | L39-L47 | HOLD |
| S14 (3) | L49-L55 | HOLDS |
| S15 (4) | L60-L68 | HOLDS |
| S16 (5) | L70-L75 | HOLDS |
| S17 (6) | L77-L82 | HOLDS |
| S18 (7) | L84-L90 | HOLDS |
| S19 nondegeneracy | L92-L96 | HOLDS |
| S20 normalization | L98-L103 | HOLDS |
| S21 (8) | L105-L110 | HOLDS |
| S22 Gaussian step | L112 | HOLDS |
| S23 (9) | L117-L121 | HOLDS |
| S24 map and Jacobian | L123-L128 | HOLDS |
| S25 (10) | L130-L135 | HOLDS |
| S26 cost to probability | L137 | HOLDS |
| S27 (11) | L142-L149 | HOLDS |
| S28-S30 (11) proofs | L151-L155 | HOLD |
| S31 limitation | L157 | HOLDS |
| S32 (12)-(14) | L162-L177 | HOLDS |
| S33 regular cells | L179 | HOLDS |
| S34 (15) | L181-L189 | HOLDS |
| S35 stability in a bin | L191 | HOLDS |
| S36 proof of (13) | L193 | HOLDS |
| S37 proof of (14) | L195 | HOLDS |
| S38 short-period test | L197 | OPEN (implications checked) |
| S39 (16) | L202-L208 | HOLDS |
| S40-S46 (16)-(17) proofs | L210-L234 | HOLD |
| S47 (18) | L239-L243 | HOLDS |
| S48 (19) | L245-L250 | HOLDS |
| S49 placement count | L252 | HOLDS |
| S50 (20) | L257-L261 | HOLDS |
| S51 fibre mixing | L263 | HOLDS |
| S52 (21) | L265-L270 | HOLDS |
| S53-S54 comparison kernels | L272-L279 | HOLD |
| S55 (22)-(23) | L284-L293 | HOLDS |
| S56 least cost | L295 | HOLDS |
| S57-S58 joint count, lower rate | L297-L303 | HOLD |
| S59-S61 fillings, common bijection | L305-L309 | HOLD |
| S62-S64 entropies, chain rule | L311-L319 | HOLD |
| S65 microscopic branch, physical slope | L321 | HOLDS |
| S66 matching guide | L326 | GUIDE |
| S67-S72 (24)-(25) | L328-L354 | HOLD |
| S73-S75 (26), obstruction | L357-L372 | HOLD |
| S76-S78 (27) | L377-L391 | HOLD |
| S79-S82 (28) | L396-L411 | HOLD |
| S83-S84 (29) | L413-L423 | HOLD |
| S85-S90 (30)-(31) | L428-L449 | HOLD |
| S91-S95 (32) | L454-L494 | HOLD |
| S96 (33), wider range | L496 | HOLDS |
| S97 undecided data | L501 | HOLDS (reading note) |
| S98 remaining estimates | L503 | OPEN |
| S99 RESULT | L506 | HOLDS as a summary (reading note) |

Counts: 99 statements. 89 PROVED statements HOLD, 6 GUIDE, 3 OPEN, and the RESULT line holds as a summary.
None HOLDS AFTER CORRECTION. None FAILS.

Notes that change no mathematics:
- L477 says the collapsed error is "as in (7)"; it is the estimate of the nondegeneracy paragraph after (7).
- L501: "the exact quotient-pair law" is the common product pair law of the two comparison kernels.
- L506: the pi^2/8, pi^2/4 and unanimity rates are for the raw-adjoint two-strip disclosure, in the range
  k L_beta J_beta = o(sqrt(beta)) given by (32), with "nearby" s = o(n/k) and "distant" k s_*/n -> infinity.
  They are not rates for the collar-only experiment, which (9) and (33) bound far below beta n^2/k.
- The physical slope kappa = 11/(3 pi^2) is used only conditionally on the account's flow premises, as stated.

What was not verified: the PR-branch line ranges in L5 and the external outline and account lines in L7.
GUIDE numeric runs (scratch only): least-cost lemma, a_k range, (2) inequalities, the binary bound, the one-link
affinity ratio, the smooth cutoff, and the toy comparison kernel (exact zeta_h formula and (2) identities).

RESULT: HOLDS - check of row 1171 (`library/gap-solve14-astra62.md`), checked line by line by hand by Claude Opus 5.5 (max effort) as FINISH row 1172, positive claims first: 99 statements, 89 HOLD, 6 GUIDE, 3 OPEN, RESULT holds as a summary, none HOLDS AFTER CORRECTION, none FAILS; the twist bound (33) -log zeta_h <= C m L_beta^3 J_beta^2 holds via the width-h rectangle bound (4), the past-only axis field (5)-(8), the layer-triangular Haar-preserving map and the signed face cost (10), and the shared-error smooth-cutoff estimate (32); the raw-adjoint two-strip rates hold: (23) gives (pi^2/8 + o(1)) beta n^2/k at d = 1/2 for s = o(n/k), (31) gives (pi^2/4 + o(1)) beta n^2/k for k s_*/n -> infinity, and unanimity (27) costs (pi^2/4 + o(1)) beta n^2/k at any separation, from the least-cost bound 2 a_k per dirty rectangle, the common-boundary fillings and the exact chain rule D_1 + D_2 - D_O with D_O >= (2 - o(1)) beta M a_k; (2), (13)-(14), (28)-(29) and (30) hold; reading notes only on L477, L501 and the scope of the RESULT rates (raw-adjoint two-strip disclosure, not collar-only); OPEN items (the order-one charged probability with only collars shared, the neutral upper bound, (W), the Jaffe-Witten gap) remain open.
