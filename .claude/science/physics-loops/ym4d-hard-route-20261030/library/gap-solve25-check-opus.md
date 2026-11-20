lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-20T17:55Z

# Check of row 1227 (`library/gap-solve25-astra62.md`), row 1230

Started 2026-11-20T05:55Z (date -u). Claude Opus 5.5, max effort, Mac mini worker 2.
Cross-provider check of a gpt-6.2-astra author file. Check by hand, line by line; no numeric run is a proof step.

## Plan (at most eight steps)

1. Read the target file in full, the FINISH rules it falls under, and list its numbered statements with their author labels.
2. Check the tunnelling-energy bounds (10)-(15) line by line.
3. Check the eight-state thermal limit (the step from (10)-(15) to the limit).
4. Check the winding-weight bound (22).
5. Check the joint-information example (23).
6. Check everything else in the file (the remaining numbered displays, (27) and the stated OPEN items), and for each cited earlier row read the cited statement and its proof where a step depends on it.
7. Say whether the main comparison restates an earlier row (grep `library/open-core.md`, FINISH rows, earlier gap-solve files).
8. Verdict table (HOLDS / HOLDS AFTER CORRECTION / FAILS, with line) and RESULT line.

## Step log

(Each step appends its result below as it finishes.)

### Step 1. Inventory (done 2026-11-20, after reading the target in full)

Target: `library/gap-solve25-astra62.md`, 327 lines, read in full at commit 49128e805. Author pin: `bb8b3eeb2`. Author: gpt-6.2-astra max. Checker: Claude Opus 5.5 max, by hand. No numeric run was used.

Statements, with author labels (line of the label):

| # | Statement | Author label | Line |
|---|---|---|---|
| (1) | one-vertex neutral transfer T = M C1C2C3 M, V = 2 sum abs(v_i x v_j)^2, C_j positive | PROVED | 23-28 |
| (2) | one-coordinate translation bound by D_j^(1/2) | PROVED | 30-34 |
| (3) | confinement along commuting directions | PROVED | 36-45 |
| (4)-(5) | Friedrichs operator and spacing limit (1-lambda_k)/h -> eps_k | PROVED | 49-78 |
| (6) | limiting generator on test functions | PROVED | 71-76 |
| (7)-(8) | heat-trace limit and counting bound N_h(A) <= C(1+A)^(27/2) | PROVED | 82-93 |
| hom. | homogeneous restriction misses the thermal time | PROVED | 95 |
| (9) | fixed-cube localization F <= (Lambda_n + C_n d_beta) I - c_n R | PROVED | 101-128 |
| (10) | tunnelling upper bound E_e <= C_n exp(-c_n sqrt(beta)) | PROVED | 132-138 |
| (11) | lower bounds on E_e and E_{1,+}; upper E_{1,+} <= C_n d_beta | PROVED | 140-170 |
| (12)-(13) | set B; averaged kernel lower bound | PROVED | 148-161 |
| (14) | eight-state thermal limit, trace norm | PROVED | 174-182 |
| (15) | thermal times tau_+, tau_all | PROVED | 184-190 |
| (16) | collective winding estimate, beta >= n^32 | PROVED | 194-203 |
| (17) | bridge bound for P_i at physical coupling | PROVED | 205-210 |
| D-bound | norm of 1_D F at beta = O(log n) | PROVED | 212 |
| (18) | restricting the physical neutral trace | PROVED | 214-221 |
| (19)-(21) | trace of an observation; comparison (20); eigen-expansion (21) | PROVED | 225-247 |
| (22) | physical-scale winding-array weight bound | PROVED | 249-254 |
| (23) | joint determination with small individual traces | PROVED | 260-272 |
| (24) | paired readings | PROVED | 274-279 |
| iter. | iterating the Haar comparison fails (l <= C/beta, v >= c beta^(3/2)) | PROVED | 281 |
| count | counting obstruction for fresh-link sampling | PROVED | 283 |
| (25) | inverse-square trace bound | PROVED GIVEN (PL3) | 289-302 |
| (26) | spectral-weight corollary | PROVED GIVEN reconstruction | 304-309 |
| (27) | exact split of s_+ | PROVED | 315-321 |
| open | upper bound in (27), continuum theory, gap | OPEN | 311, 323 |

Cited earlier rows the steps depend on (file, check on file):

- Row 1215, `gap-solve23-astra62.md`: Gaussian norm L(D), affine Gaussian operations (2)-(3), flat formula S_n(theta), strict inequality, Fourier expansion (7), patch comparisons (16)-(18), flat-cap trial. Check: row 1221, `gap-solve23-check-opus.md`, every statement HOLDS (Claude Opus 5.5, cross-provider for that row).
- Row 1161, `gap-solve9-astra62.md`, (23): one-link character bound, private-link density bound. Check `gap-solve9-check-opus.md`.
- Row 1145, `gap-solve2-astra62.md`, (2): Fourier product bound.
- Row 1155, `gap-solve7-astra62.md`, (9): marked-plaquette exponential moment.
- Row 1171, `gap-solve14-astra62.md`: orbit reconstruction by short trace words.
- Sussman-Alpoge outline lines 3205-3254, (PL1)-(PL3): used as a named input for (25).

Not used as a step: rows 1143, 1179, 1183, 1211, 1218, 1222 (context or pointers only).

### Step 2. The fixed-cube localization (9) and the tunnelling bounds (10)-(13), (15)

All constants below depend on the fixed n >= 3, as the source says (line 99). d_beta = beta^(-1/4)(1+log beta), ell = 1+log beta, r = beta^(-3/8).

**Input from row 1215, read for this step.** Row 1215 lines 28-40 (Gaussian norm L(D) = exp[-(1/2) sum omega(sigma_j^2)]), 50-61 (lower test, localization, patch upper bound), 67-88 (flat formula (4), singular values ell(q), ell(q), 0 per colour character, strict inequality S_n(theta) > S_n(0)). The colour characters at a periodic flat are 0, theta, -theta, and S_n is even, so L(D_A) = exp[-S_n(0) - 2 S_n(theta)] and Lambda_n = exp[-3 S_n(0)] (target line 115-118) follow from row 1215 (2) and the character count. Row 1215 is checked HOLDS in row 1221.

**(9), the drop on a flat (lines 113-120): HOLDS.** Near theta = 0 the k = 0 term is omega(ell(theta/n)) = |theta|/n + O(|theta|^3), since omega(s) = sqrt(s) - s^(3/2)/24 + ... and ell(theta/n) = |theta|^2/n^2 (1 + O(|theta|^2)). The k != 0 sum is smooth and even (k -> -k mod n), so S_n(theta) - S_n(0) >= |theta|/(2n) near 0. Away from 0, compactness of the phase torus and the strict inequality give a positive minimum. R(A) = max_i |sin a_i| = max_i |sin(theta_i/2)| is a function on the phase torus (a_i -> a_i + pi is the centre) and is at most |theta|/2. Hence L(D_A) <= Lambda_n - c_n R(A).

**(9), localization (lines 122-126): HOLDS.** I checked each error against d_beta:
- discard beta V > ell^2: norm error 2 exp(-ell^2/2), since F - PFP = (1-P)MCM + PMCM(1-P) and ||1_{beta V > ell^2} M|| <= exp(-ell^2/2);
- IMS error: kernel F(X,Y) (1/2) sum |chi(X) - chi(Y)|^2 <= C(X,Y) C_n d(X,Y)^2 / r^2; Schur row integral C_n/(beta r^2) = C_n beta^(-1/4);
- Taylor error e(xi): C_n sqrt(beta) r^2 = C_n beta^(-1/4); with both endpoints retained, |b + D xi| = O(ell), so the exponent changes by C_n ell beta^(-1/4) = C_n d_beta;
- cosine against half-square: beta sum x_p^4 <= (max x_p^2) beta sum x_p^2 = O(ell^4/beta);
- electric metric and Jacobians: relative 1 + O(r^2 + 1/beta); at fixed n the dimension 9n^3 is fixed, so the rescaling costs 1 + O_n(r^2).
- distance to an exact flat: u = C_n ell/sqrt(beta); the commutator formula q_1 q_2 - q_2 q_1 = 2 v_1 x v_2 gives |(v_2)_perp| <= C u/|v_1| <= C sqrt(u) when |v_1| >= sqrt(u). So the flat is within C_n (ell/sqrt(beta))^(1/2) = C_n ell^(1/2) beta^(-1/4) <= C_n d_beta. Weyl's inequality and the 1-Lipschitz map sigma -> omega(sigma^2) = 2 arsinh(sigma/2) give |log L(D_*) - log L(D_A)| <= C_n ||D_* - D_A||.
- extension across the discarded set uses c_n <= Lambda_n/2 and R <= 1, so the added integrand is nonnegative.

**(9), lower test (line 128): HOLDS.** Packet radius in the link metric is C beta^(1/8)/sqrt(beta) = C r. The kernel-direction loss is (1/2) E|Z|^2 ||grad phi||^2 = C W^(-2) = C beta^(-1/4). For the electric lower bound, exp at the identity of SU(2) = S^3 is 1-Lipschitz on the ball of radius pi (nonnegative curvature, Rauch), and left translation is an isometry, so d <= |xi - zeta|/sqrt(beta); with 1 - cos u <= u^2/2 the electric factor dominates the Euclidean Gaussian up to the normalization 1 + O(1/beta). So lambda_0 >= Lambda_n - C_n d_beta.

**(10) (lines 132-138): HOLDS.** I redid the weighted vacuum equation. With W = exp(alpha sqrt(beta) rho), rho = d(., D^c), W = 1 on D^c:
lambda_0 P_D W psi = P_D F P_D W psi + P_D F P_{D^c} psi + P_D (W F W^(-1) - F) W psi,
so kappa_n ||P_D W psi|| <= lambda_0 + C_n alpha (||P_D W psi|| + 1), which gives the stated 2(lambda_0 + C_n alpha)/kappa_n when C_n alpha < kappa_n/2. kappa_n = c_n/4 works, from (9), P_D F P_D >= 0 and R > 1/2 on D. The Schur bound uses |W(X)/W(Y) - 1| <= exp(alpha sqrt(beta) d(X,Y)) - 1, F <= C pointwise, and E[e^{alpha Z} - 1] <= alpha E[Z e^Z] for alpha <= 1, with Z = sqrt(beta) d bounded in law by a sum of 3n^3 one-link variables with Gaussian tails. For the trial: flip i (edges in direction i crossing one cut) sends H_i -> -H_i and fixes H_j, j != i, so sigma_e psi lies in sector e; the ground-state identity <f psi, (1 - F/lambda_0) f psi> = (1/2) E|f(X) - f(Y)|^2 is standard for real f. R < 3/4 gives |Re H_i| > sqrt(7)/4, a sign change needs |Re H_i(X) - Re H_i(Y)| >= sqrt(7)/2, hence d(X,Y) >= c_n. The form is <= C e^{-2c sqrt(beta)} + C e^{-c beta}/lambda_0, and -log(1-y) <= 2y.

**(11)-(13) (lines 140-170): HOLDS.** Checked points:
- (12): from (9), lambda = <phi, F phi> <= Lambda_n + C_n d_beta - c_n int R|phi|^2, and lambda >= lambda_0 - d_beta >= Lambda_n - (C_n + 1) d_beta, so int R |phi|^2 <= C_n d_beta; ||1_{beta V > K} phi|| <= e^{-K/2}/lambda from phi = MCM phi/lambda.
- the path stays at beta V <= C_n: the double-wrap commutator chord 2 sin(s a_i) sin(s a_j)|u_i x u_j| is increasing in s on [0,1], and at s = 1 it is the commutator of the root windings, which is within n^2 sqrt(2K_n/beta) of 1 because it is a conjugated product of the n^2 plaquettes of an (i,j) torus at an endpoint with beta V <= K_n. (The bound a_i <= C_n d_beta alone would give only beta V <= C ell^4; the monotone decrease from the endpoint value is what keeps beta V bounded. The source states "which only decreases", which is this argument.)
- (13): with m steps of length <= 1/sqrt(beta) and caps of radius c_n/sqrt(beta), F^m >= c_n^(2m-1) beta^(9n^3/2); I_beta^(-1) ~ c beta^(3/2) per link, 3n^3 links; the gauge caps give measure >= c beta^(-3n^3/2); so the averaged kernel is >= beta^(-C_n) e^{-C_n m}.
- sup bound: ||C(X,.)||_2^2 = prod_l I_{2 beta}/I_beta^2 ~ (c beta^(3/2))^(3n^3), so ||psi||_inf <= C_n beta^(9n^3/4); lambda_0 <= 1 since ||C|| = 1, M <= 1.
- Dirichlet bound: on B x B, (1/2) int int |f(X) - f(Y)|^2 dpi dpi = pi(B)||1_B phi||^2 - (int_B psi phi)^2 >= (7/8)^2 - (1/8)^2 = 3/4, using int_B psi phi = -int_{B^c} psi phi and Cauchy-Schwarz on B^c.
- 1 - x^m <= m log(1/x) gives E >= c beta^(-C) e^{-C m}/m: m = C(1 + sqrt(beta)) gives e^{-C sqrt(beta)}; m = C(1 + d_beta sqrt(beta)) gives e^{-C beta^(1/4)(1 + log beta)}.
- upper bound E_{1,+} <= C_n d_beta: the two saturations are separated by c_n r because the winding angle modulo the centre is Lipschitz and the packets have radius C r while the centres differ by K r; the cross kernel has Schur norm <= P(d >= c r) <= C e^{-c beta r^2} = C e^{-c beta^(1/4)}; min-max on the two invariant top functions and lambda_0 <= Lambda_n + C_n d_beta.

**(15) (lines 184-190): HOLDS.** Lower bounds: one excited term e^{-u E} with E <= C_n d_beta (neutral) or E_e <= C_n e^{-c sqrt(beta)} (all). Upper bounds: sum_{k>=1} e^{-u E_k} <= Tr(U) e^{-(u-1) E_1}, Tr U <= C_n beta^(9n^3/2), with E_1 from (11) (neutral) or from the remark at line 146 that e^{-C_n sqrt(beta)} bounds every nonvacuum physical energy (all sectors). log log beta terms are absorbed. Physical reading checked: at fixed n the neutral time is at most exp(C beta^(1/4) log beta), the full time at least exp(c sqrt(beta)).

Plausibility guide (not a step): the one-loop holonomy potential is linear, 2|theta|/n, with collective mass about beta n, so the lowest neutral energies scale like beta^(-1/3) at fixed n, inside the bound C_n d_beta; the centre tunnelling scale e^{-c sqrt(beta)} matches the e^{-c/g} of Lüscher and van Baal. No contradiction.

### Step 3. The eight-state thermal limit (14) (lines 174-182)

**(14): HOLDS.** Line by line:
- the eight sigma_e psi are orthonormal: distinct characters of the flip group (Z_2)^3, and |sigma_e| = 1 a.e.;
- B is flip-invariant and R <= A_n d_beta < 1 on B, so Re H_i != 0 there and the eight B_z partition B exactly; flips permute them and fix psi, so pi(B_z) = pi(B)/8;
- if the ninth level (index 8) has lambda >= lambda_0 - d_beta, every unit vector of the nine-dimensional span satisfies (12): (9) gives the R-moment, and phi = F (F|span)^(-1) phi gives ||1_{beta V > K} phi|| <= e^{-K/2}/(lambda_0 - d_beta);
- a unit vector orthogonal to the eight psi 1_{B_z} exists (nine dimensions, eight constraints); then sum_z [pi(B_z)||1_{B_z} phi||^2 - 0] = (pi(B)/8)||1_B phi||^2 >= (7/64)(7/8);
- the short path suffices on each B_z x B_z (same centre signs, no flip), so the gauge-averaged kernel bound (13) holds with m' = ceil(C_n(1 + d_beta sqrt(beta)));
- the form of 1 - U^{m'} on the span is <= 1 - e^{-m' E_8}, so E_8 >= e^{-C_n beta^(1/4)(1 + log beta)}; if the hypothesis fails, E_8 >= d_beta, which is larger;
- (10) gives one level per sector below Ce^{-c sqrt(beta)} < E_8, so exactly eight levels lie below the edge, one in each sector;
- at m = floor(exp(beta^gamma)): the tail is <= Tr(U) e^{-(m-1)E_8} -> 0 because gamma > 1/4 beats beta^(1/4) log beta + O(log beta); 1 - e^{-m E_e} <= m E_e -> 0 because gamma < 1/2; ||(1 - P_{phi_e}) sigma_e psi||^2 <= C e^{-c sqrt(beta)}/(1 - e^{-E_8}) -> 0; for unit vectors ||P_u - P_v||_1 = 2 sqrt(1 - |<u,v>|^2).
So Tr_all U^m -> 8 and Tr_+ U^m -> 1 at fixed n. No defect found.

Verdicts so far: (9) HOLDS; (10) HOLDS; (11) HOLDS; (12) HOLDS; (13) HOLDS; (14) HOLDS; (15) HOLDS. All at fixed n with n-dependent constants, as stated.

### Step 4. The winding-weight bound (22) and its inputs (19)-(21); also (16)-(18) and the D-bound

**Input from row 1161, read for this step.** Row 1161 lines 343-358: (23), the selection rule "select the positive mu-link at x if sum_nu x_nu mod p is in A_mu", A_mu a partition of the even residues; and its one-slice form with m' = floor(n/6), N' = 3n^2. Checked HOLDS in row 1162 (S39, S40). I re-derived the slice form: the two lower links of a face start at residue s, the two upper at s + 1; only one of these is even, and at that residue only one direction is selected. A mu-circuit meets every residue once, so it has |A_mu| >= floor(n/6) selected links, and each selected link lies on one circuit. Temporal factors of the bridge meet one spatial link each.

**(19) (lines 225-234): HOLDS.** U^u >= 0 because F is a positive form (line 28 and row 1215 line 26); Tr U <= C_n beta^(9n^3/2) < infinity at finite n. For a finite partition, the normalized indicators are orthonormal in L^2(pi) and <e_B, U^u e_B> = P(Y_0 in B, Y_u in B)/pi_Y(B) in the stationary chain. Refining partitions give Q_k increasing strongly to P_Y (martingale convergence), and Tr(Q_k U^u Q_k) = sum_l mu_l ||Q_k phi_l||^2 increases to Tr(P_Y U^u P_Y) by monotone convergence. Since F commutes with gauge maps and flips, P_Y U^u P_Y = P_Y (P_+ U P_+)^u P_Y for gauge- and centre-invariant Y; working on the full temporal-gauge chain is therefore legitimate.

**(20) (lines 236-241): HOLDS.** Denominator on A x B: >= l H(B) pi_Z(A). Numerator: condition first on everything except Y_0 (this exterior contains Z_0 and all other slices, including Y_u and Z_u, also when u = 1), giving <= v H(B) P(Z_0 in A, Z_u in A, Y_u in B); then condition on everything except Y_u, which contains the event {Z_0 in A, Z_u in A}, giving <= v^2 H(B)^2 P(Z_0 in A, Z_u in A). Summing over B and refining product partitions gives T_{Z,Y} <= (v^2/l) T_Z. Lower bound by subspace inclusion and U^u >= 0. Precision (no change of content): the chain must be two-sided (or periodic), so that "every other time slice" includes the slice before time 0; the conditional law of slice 0 is then the two-step bridge F(X_{-1}, .)F(., X_1), and the vacuum factors cancel, as line 249 says. Conditioning on a finer exterior (all unselected links) than the one named is harmless, since the bounds hold for every value of it.

**(21) (lines 243-247): HOLDS.** Eigen-expansion of Tr(P_Y U^u P_Y) with ||P_Y 1|| = 1; non-neutral eigenvectors have P_Y phi = 0.

**(22) (lines 249-254): HOLDS.** Given the exterior (all unselected links of the slice, both time neighbours), the M = 3n^2 straight windings are conditionally independent, each a product of >= floor(n/6) independent tilted-Haar draws (tilt length <= 6 beta: four spatial faces and two temporal faces per link) with fixed factors. Fourier inversion gives a one-line density in [1 - eta, 1 + eta], eta <= sum_{d>=2} d^2 e^{-(d-1) floor(n/6)/(1+6beta)} <= C e^{-cn/(1+beta)} when the exponent is >= 1. Any function of the matrix array has a law between (1-eta)^M and (1+eta)^M times the pushforward of Haar^M; the reference does not depend on the exterior. Then v^2/l - 1 <= exp(3M eta + O(M eta^2)) - 1 <= C M eta, and at beta <= B log n, M eta = 3C n^2 e^{-cn/(1 + B log n)} -> 0. So T_Y(u) - 1 <= C n^2 e^{-cn/(1+beta)} for every u >= 1. "For large n divisible by four" is more than the construction needs (n even suffices); harmless.

**(16) (lines 194-203): HOLDS, given row 1215 (7), (16)-(18).** Input read: row 1215 lines 269-299 (joint range, retained points, relative localization with product partitions, distance to an exact flat with error C n (N/beta)^(1/4) per edge, the relative Gaussian upper bound (17), the patch lower bound (18), and lambda_0 >= e^{-C_0 N} from the flat-cap trial). Checked:
- Lipschitz constant of P_i: n^{-2} sum over n^2 lines of n link distances, Cauchy-Schwarz over the n^3 links of direction i: n^{-2} sqrt(n^3) = n^{-1/2}.
- compressed norm: a chart centre X_* in D_i is within C n (N/beta)^(1/4) per edge of a flat A, so every winding trace moves by <= C n^2 (N/beta)^(1/4) <= C n^(2.75 - 8) and |P_i(A)| <= 4/5; at a flat P_i = cos a_i and theta_i = 2 a_i give 1 - cos theta_i = 2(1 - P_i^2) >= 18/25; the z = e_i term of the Fourier expansion then gives S_n(theta) - S_n(0) >= c/n; at beta >= n^32 the errors N n (N/beta)^(1/4) <= n^(-3.25), N beta^(-1/4) <= n^(-5), N^2/beta, N beta^(-1/6), e^{-N} are all o(1/n). The nonnegative top function g of the compression gives <g, F_ret g>(1 - C N beta^(-1/4)) <= sum_alpha <chi_alpha g, F_ret chi_alpha g> pointwise, as in row 1215 line 280.
- weighted equation: on short jumps (sqrt(beta) d <= B n^(3/2)) the weight ratio is <= e^{alpha B/n}; on long jumps the factor exp(alpha sqrt(beta) d / n^(5/2)) <= exp(c_0 beta d^2/2 + C), and E exp(c_0 beta d^2) <= C_0^(3N) gives a tail C exp[(3 log C_0 - c_0 B^2/2) N] <= e^{-N} lambda_0 for B large, using lambda_0 >= e^{-C_1 N}. Then ||1_{D_i} W psi|| <= (lambda_0 + delta)/(kappa - delta) <= C n with kappa = c lambda_0/n, delta = c lambda_0/(2n). On {|P_i| <= 1/2}, W >= e^{alpha sqrt(beta)/(4 n^2)}.
- E_e: flip i sends every i-winding to its negative, so P_i -> -P_i and prod_{i in e} sgn(P_i) psi lies in sector e; a sign change with both |P_i| > 1/2 needs d >= sqrt(n), probability <= C_0^(3N) e^{-c_0 beta n}/lambda_0 <= exp(CN - c beta n), negligible at beta >= n^32.

**(17) (lines 205-210): HOLDS.** Marking i-links with z_i = (sum of the transverse coordinates) mod 2: a face of the (i,j) plane has its two i-links at z and z + e_j, of different transverse parity, so at most one is marked; each i-line has n/2 marked links. ||E pi_{1/2}(H)|| <= (e^{-1/(1+6beta)})^{n/2} = b_{n,beta}, so |E Re H| <= b. Lines are conditionally independent with values in [-1, 1]; Hoeffding gives log-mgf <= t^2/2 for the centred variable; the average of n^2 such variables has each tail <= e^{-n^2 s^2/2}; three directions and two signs give 6.

**D-bound (line 212): HOLDS.** (F 1_D F)(X,Y) = F^2(X,Y) P(middle in D | X,Y) <= 6 e^{-n^2 (eta - b)^2/2} F^2(X,Y), and b -> 0 at beta = O(log n). Norm domination for nonnegative kernels gives ||1_D F||^2 = ||F 1_D F|| <= 6 e^{-n^2 eta^2/8} lambda_0^2. The band statement follows from phi = F (F|band)^(-1) phi.

**(18) (lines 214-221): HOLDS.** s = 4 sqrt(log n)/n gives 6 e^{-n^2 s^2/2} = 6 n^(-8) = q_n. Tr_+ (PFP)^u = Tr_+ (PF)^u is the integral over periodic paths averaged over the endpoint gauge and the eight flips; for each fixed group element the conditional law of each slice given the others is a two-step bridge (at the time seam with the neighbour transformed by that element; for u = 2 both neighbours come from the other slice), so successive conditioning gives a probability between (1 - q_n)^u and 1. u-th roots give 1 - q_n <= lambda_P/lambda_0 <= 1 (Tr(K^u)^(1/u) -> ||K|| for positive trace class K; the neutral and full tops of PFP agree by positivity). Combining the two bounds gives (18). u >= 2 is needed (u = 1 has no bridge), as stated.

Verdicts so far: (16) HOLDS; (17) HOLDS; D-bound HOLDS; (18) HOLDS; (19) HOLDS; (20) HOLDS (with the two-sided-chain precision); (21) HOLDS; (22) HOLDS.
