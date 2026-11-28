lead: anthropic/claude-opus-5-5/max laptop-subagent

# Check of `library/gap-solve19-astra62.md` (row 1186), FINISH row 1191

Status: COMPLETE (all eight steps). Counts: 38 PROVED statements
(62 PROVED paragraphs) checked; 38 HOLD; 0 HOLD AFTER CORRECTION;
0 FAIL. Two wording notes, no verdict change (step 8).

Checker: Claude Opus 5.5, max effort, laptop subagent. Check by hand,
line by line. A numeric run may guide only.

## Plan (at most eight steps)

1. Read the target file in full. Record the line numbers of each
   numbered display, each PROVED / GUIDE / ARGUED / OPEN label and the
   RESULT line.
2. Read every cited earlier row: FINISH.md RESULT lines, the cited
   `library/gap-solve*-astra62.md` files and their `-check-opus.md`
   checks, `library/gap-neutral-chain-check-astra.md`, `parts/gap.md`.
   Record the exact cited statements.
3. Check claim 1: the equivalence of (N-phys) with (26) and with the
   finite binary test (28).
4. Check claim 2: the uniform entropy bound (24).
5. Check claim 3: the obstructions (18) and (29).
6. Check claim 4: the test (6).
7. Check everything else in the file, and the labels and RESULT line
   against the body. Optional small numeric guide (outside the repo,
   BLAS threads 1, under 1 GB).
8. Write the counts, the per-statement verdicts, what was not checked,
   and the RESULT line.

## Step results

### Step 1. Structure of the target

The target has 408 lines. Source read in full: lines 1-408.

- GUIDE paragraphs: lines 3, 5, 7, 9, 69, 406.
- OPEN paragraphs: lines 400, 402, 404.
- RESULT line: line 408.
- No ARGUED label occurs.
- PROVED paragraphs (62): lines 13, 15, 26, 33, 35, 47, 58, 73, 80, 90,
  97, 111, 119, 121, 133, 139, 148, 160, 163, 170, 172, 180, 182, 186,
  205, 207, 209, 213, 220, 223, 231, 233, 235, 239, 246, 248, 255, 257,
  261, 263, 277, 279, 283, 285, 293, 295, 301, 305, 307, 311, 322, 328,
  342, 344, 351, 357, 359, 369, 377, 384, 386, 392.
- Display tags: (1) l.22, (2) l.29, (3) l.41, (4) l.50, (5) l.54,
  (6) l.61, (7) l.76, (8) l.86, (9) l.93, (10) l.102, (11) l.113,
  (12) l.124, (13) l.129, (14) l.135, (15) l.142, (16) l.156, (17) l.166,
  (18) l.176, (19) l.194, (20) l.216, (21) l.242, (22) l.251, (23) l.273,
  (24) l.318, (25) l.324, (26) l.347, (27) l.353, (28) l.363, (29) l.373.

I group the 62 PROVED paragraphs into 38 statements S1-S38 (a claim
with its proof paragraphs). The priority statements are:

- claim 1: S35 (26), lines 344-349, and S37 (28), lines 359-365, with
  S36 (27), lines 351-357;
- claim 2: S34 (24)-(25), lines 311-342;
- claim 3: S20 (18), lines 172-182, and S38 (29), lines 369-396;
- claim 4: S6 (6), lines 58-67, which uses S1-S5, lines 13-56.

Cited rows that a step depends on: 1161 (`gap-solve9`), 1165
(`gap-solve11`), 1178 (`gap-solve18`), 1155 (`gap-solve7`), 1145
(`gap-solve2`), 1173 (`gap-solve15`), 1177 (`gap-solve17`), 1179
(`gap-mini-branch-fable`), 1065 (`gap-measured-vectors-max`), 668
(`gap-os-equiv`).

### Step 2. Cited rows: statements read and their check status

I read each cited statement and its proof where a step of row 1186 uses it.

- Row 1161 (`gap-solve9-astra62.md`). Read L13-168, L213-227, L341-423.
  The one-cube dichotomy (9), the finite-aspect K (L146), the consumer
  (L148), the necessity and Pfaffian converse over physical sizes (L150),
  the explicit test K = 512 with range 4 | n, n >= 2^70 (L215-227), the
  ordinary-shape criteria (26) (L379-400) and the straight-winding bound
  (23) (L343-351). Row 1162 checked all of these: HOLD (its one
  correction is a credit at L235, not used here).
- The meaning of (N-phys). Row 1179 L304-309 states it with the
  existence constant K of row 1161 L146. Row 1161 RESULT and L419 state
  the explicit form: s_j(floor(n/512); n) <= 1/2 on one admissible cube
  for all fine cutoffs. Over the allowed dyadic sides the two forms are
  equivalent, since each gives the Pfaffian seed (L148, L215-227) and the
  seed gives the neutral trace small at any fixed aspect after enlargement
  (L150). Row 1186 uses the explicit form. I use the same.
- Row 1165 (`gap-solve11-astra62.md`). Read L11-76, L281-296, L407-411.
  (3) (Shannon two-slice bounds) and (19) (X_H(u) <= (h_g - d_H)^{-2},
  with d(P,Q) = ||sqrt dP - sqrt dQ||_2, no factor 1/sqrt 2). Row 1166:
  (3) and (19) HOLD. I re-derived (19) by hand: mA <= C <= A with
  m = g^{-1/2}, the second-moment bound (1+m)b - m, the quadratic
  ((1+m)b - 2m)^2 >= 0, and ||C||_op >= b - d_H ||C||_HS. It holds.
- Row 1178 (`gap-solve18-astra62.md`). Read L13-16, L66-89 ((4), (5)),
  L239-289 ((17)-(21)), L431-501 ((36)-(40)), L502-516 ((41)), L554.
  Row 1185 (finished 22:45Z) checked all 88 statements: HOLD. Used here:
  (5) (excited sums S_A(r; s,w,w) <= C e^{-cr/n_0} for s >= w,
  r >= s/16, w >= K n_0, in both seeded branches), (19) (four leading
  levels and long-odd bound in the competing branch), (36)
  (t_chi >= c_q m/(n_0^2 log(2+m))), and the proof of (40) (four rank-one
  terms on an arm, discarded trace norm O(e^{-cd})).
- Row 1155 (`gap-solve7-astra62.md`). Read L44-76. (3) (column kernels
  exp(beta u.R_t v + h.v), |h| <= 4 beta), the contraction
  d(fK,gK) <= tanh(beta) d(f,g) and the 4 beta bound for arbitrary inputs,
  hence delta_r = 4 beta tanh(beta)^{r-1}; the slope
  beta/log n -> 11/(3 pi^2) < 1/2 conditional on RF10, RF20, RF23-25,
  RF28. Row 1156: HOLDS.
- Row 1145 (`gap-solve2-astra62.md`). Read L14-30. (1) multiplier
  0 <= I_d(s)/I_1(s) <= exp[-(d-1)/(1+6 beta)] for tilt s <= 6 beta,
  and (2) the path density bound eta(m/b_beta). Row 1146: HOLDS.
- Row 1173 (`gap-solve15-astra62.md`) L146: the Gaussian comparison,
  action (1/2) sum (phi_x - phi_y)^2 + (1/2) mu^2 sum phi^2, mu = a^2.
  Row 1174: HOLDS. Row 1177 (`gap-solve17-astra62.md`): row 1182 HOLDS;
  row 1186 cites it only in a comparison sentence.
- Rows 1179 and 1065 (Theorem BP, Corollary N-JW) and their check
  `gap-neutral-chain-check-astra.md` (row 1183): HOLDS AFTER CORRECTION.
  Row 1186 cites them only for conditional continuum consequences and
  for the datum assumed in (21)-(22); no step of a PROVED claim depends
  on their proofs.

### Step 3. Claim 1: (N-phys) <=> (26) <=> (28)

**S35. (26), L344-349. HOLDS** (given the checked rows 1161 and 1165,
and (24), which step 4 checks).

- Reverse direction, same side L. If limsup_j I_G(2t) < 1/1024, then
  I_G <= c < 1/1024 for all fine j. The Hellinger bound holds:
  d^2 = 2(1 - A), and Jensen gives A >= exp(-D/2), so
  d^2 <= 2(1 - e^{-D/2}) <= D. Thus d_G <= sqrt(c) < 1/32. Row 1165
  (19) with H = G, g = 8, gives X_G(2t) = Tr(P_+ U^{2t}) = D_0(2t)
  <= (h_8 - d_G)^{-2}, with h_8 = 2 * 8^{-1/4}/(1 + 8^{-1/2}) = 0.8786.
  So D_0(2t) <= (0.8786 - 0.03125)^{-2} = 1.393 < 3/2. Here
  u = 2t = 2 floor(n/1024) is an integer in [3, n/512] for n >= 2048,
  so row 1161's explicit K = 512 test applies (4 | n, n >= 2^70 on the
  grid) and gives the Pfaffian seed. Also s(floor(n/512)) <= s(2t) < 1/2
  by monotonicity in time. Both forms of the neutral input hold at L.
- Forward direction, larger side. The neutral input gives the Pfaffian
  seed (row 1161 L215-227). Row 1161 L150 (converse part, checked as S11
  of row 1162) gives, for each fixed K, D_0(floor(n/K)) <= 3/2 on a
  sufficiently large fixed dyadic side, eventually in the cutoff. Then
  (24) with s = 1/2, d = 3/4, u = floor(n/K), t = floor(n/1024),
  k = t/u -> K/1024 bounds limsup_j I_G(2t) by
  C_8 (3/4)^{k-1} + h_2(Delta) + Delta log 8 with
  Delta <= C_8((k/2)^{-1/2} + (3/4)^{2k-1}). This tends to 0 as
  K -> infinity, so it is below 1/1024 for one fixed K. (26) holds at
  that side.
- The quotient. The I_G of (26) is the information of the two gauge and
  centre orbits. This is the P_G of row 1165 (19). Lifting each orbit by
  its invariant conditional law does not change mutual information
  (data processing in both directions). This holds.

**S36. (27), L351-357. HOLDS.**

- The randomized raw readings have the information of the orbits, since
  the joint law is invariant under independent gauge and centre actions
  at the two slices. Correct.
- One link change at one end moves log K^t by at most 3 beta delta_e
  (four spatial plaquettes at weight beta/2, one temporal plaquette at
  weight beta; the chordal distance bounds the change of Re). The squared
  kernel moves by 6 beta delta_e, and the flip average keeps this bound.
- Relative entropy of e^f to a product with log oscillations c_i is at
  most sum c_i^2/8: chain rule, then psi'(1) - psi(1) =
  int_0^1 s psi''(s) ds <= c_i^2/8, by Popoviciu (tilted variance
  <= c_i^2/4). Correct.
- I_G - I_bin equals the averaged within-bin joint entropy minus two
  nonnegative marginal terms. With 2 ends: 2 (6 beta delta_e)^2/8 =
  9 beta^2 delta_e^2 per link. The constant 9 is exact. The lower bound
  0 is data processing. Correct.

**S37. (28), L359-365. HOLDS.**

- Chain rule: I_bin = sum_i I(X_i; Y | X_{<i}), and each term is
  E D(Bern(p) || Bern(1/2)) because each bit is fair given its own prefix
  (median of the one-slice marginal). Lower bound 2(p - 1/2)^2 (second
  derivative 1/(p(1-p)) >= 4); upper bound chi^2 = 4(p - 1/2)^2 (from
  log x <= x - 1). So 2 B_ord <= I_bin <= 4 B_ord. Correct.
- Diameters 1/((1+beta) v) give beta^2 sum delta_e^2 <= 1/v -> 0.
- Equivalence. If limsup B_ord < 1/4096, then limsup I_bin < 1/1024 and
  limsup I_G <= limsup I_bin by (27); (26) follows, so the neutral input.
  Conversely the neutral input and (24) give limsup I_G < 1/2048 on an
  enlarged side, and B_ord <= I_bin/2 <= I_G/2 < 1/4096. Correct.
- Depth. Only a finite depth is needed for this equivalence. The median
  tree reaches any diameter at finite depth, since the coordinate density
  ratio is bounded at fixed cutoff. The polynomial bound (14) is checked
  in step 7.

Claim 1 verdict: the equivalence of the physical neutral input with (26)
and with (28) HOLDS over the allowed dyadic sides, given rows 1161 and
1165 (both checked) and (24). Scope note: the forward direction changes
the side; the reverse direction keeps it. The RESULT line says "over
allowed fixed sides", which is correct.

### Step 4. Claim 2: the entropy bound (24), with (25)

**S34. (24)-(25), L311-342. HOLDS.**

Line-by-line record.

- L311, L322. The two-slice density relative to pi^2 is p_t^2/Z with
  p_t = sum_q K_q and Z = Tr P^{2t} = sum_q B_q. Independent flip
  averages at the two ends give (1/8) sum_g chi_q(g) chi_q'(g) =
  delta_{qq'}, so the averaged density is sum_q K_q^2/Z, a mixture of
  L_q = K_q^2/B_q with weights w_q = B_q/Z, since
  int int K_q^2 = Tr(P^{2t} Pi_q) = B_q. Correct.
- Lifting the orbit pair by its invariant conditional law keeps the
  mutual information (data processing both ways). Correct.
- l_q(x) = (P^{2t} Pi_q)(x,x)/B_q. Correct.
- (25). P^t Pi_q is a positive operator (P is unitarily equivalent to
  U >= 0, and Pi_q commutes with it), so |K_q(x,y)|^2 <=
  K_q(x,x) K_q(y,y) and K_q(x,x) >= 0. With m_q = K_q(x,x)/A_q,
  L_q <= (A_q^2/B_q) m_q (x) m_q, so I(L_q) <= D(L_q || m_q x m_q)
  <= log(A_q^2/B_q). Then (B_q/Z) log(A_q^2/B_q) <= (A_q^2 - B_q)/Z.
  Correct.
- L328. D_q(u) <= D_0(u): the eight twisted traces are nonnegative.
  r_2^u <= d because r^u + r_2^u <= 1 + s and r_2 <= r. Then
  sum_{i>=2} r_i^v <= r_2^{v-u} sum_{i>=2} r_i^u <= (1+s) d^{v/u-1}
  for real v >= u. All r <= 1 (the periodic vacuum is the top of the
  whole spectrum). So A_q^2 - B_q <= 2 tau + tau^2 with
  tau <= (1+s) d^{k-1}, and the sum of (25) is <= 64 d^{k-1} for s < 1.
  Correct.
- |h| is neutral. E_u(|h|) <= E_u(h) = 1 - r^u (nonnegative kernel of
  P^u, P^u 1 = 1). On neutral functions orthogonal to 1, 1 - P^u >=
  1 - s, since the largest excited neutral ratio is at most s(u) <= s.
  Hence 1 - (pi|h|)^2 <= (1 - r^u)/(1 - s). Correct.
- ||h^2 pi - pi||_TV (sup convention) = (1/2) int ||h| - 1| (|h| + 1)
  <= (1/2) sqrt(2(1 - pi|h|)) sqrt(2(1 + pi|h|)) = sqrt(1 - (pi|h|)^2).
  Correct.
- The marginal display: l_q is the mixture of h_i^2 pi with weights
  r_i^{2t}/B_q. The leading term is r^{2t} sqrt((1 - r^u)/(1 - s))/Z with
  r^{2t} = x^{2k}, x = r^u; the tail is at most sum_{i>=2} r_i^{2t} <=
  (1+s) d^{2k-1}; sum over g sectors and use Z >= 1. Correct. The
  supremum: sup_y e^{-2ky} sqrt(y) = (4ke)^{-1/2} <= C/sqrt(k). Correct.
- L342. Chain rule: I(X;Y) <= I(X;Y,Q) = I(X;Q) + sum_q w_q I(L_q).
  Delta = sum_q w_q ||l_q pi - l pi||_TV is the mean of
  TV(P(Q|X), w), so a maximal coupling gives Q' ~ w independent of X
  with P(Q' != Q) = Delta. Then I(X;Q) = H(Q') - H(Q|X)
  <= H(Q'|Q,X) <= h_2(Delta) + Delta log g. Delta <= 2 x (display) by
  the triangle inequality. This gives (24) with
  Delta <= C_g((k(1-s))^{-1/2} + d^{2k-1}). Correct.
- Uniformity. The bound depends only on s, k and g. It holds for every
  spatial box, coupling and cutoff. Correct.
- L320 comparison sentences. Row 1165 (19) with H = G is a Hellinger
  test for the neutral count; row 1165 (3)-(4) is a Shannon test for the
  full periodic count; row 1165 L409 gives TV convergence after the full
  centre quotient on b^4 in either seeded branch. The sentences agree
  with the sources.

Claim 2 verdict: (24) HOLDS as stated, with absolute constants C_8.
The forward direction of (26) uses it correctly.

### Step 5. Claim 3: the obstructions (18) and (29), with the loop form

**S20. (18), L172-182. HOLDS.**

- L172. With Hopf coordinates, Re g = sqrt(u) cos(2 pi v_1), so
  {Re g >= 0} is a bisection of v_1 after a shift of 1/4. Under (7) the
  kernel K_t is invariant under independent gauge transformations at the
  two ends, so (g_0, g_t) is invariant under (k g_0, k' g_t) for
  independent k, k'. Hence g_0, g_t are independent Haar, the root
  median is 1/2, I_0 and I_t are independent fair bits, and c_root = 0.
  Correct.
- L180, energy bound. On the trivial-twist component (weight 1/64) all
  4V links lie in balls of angle (1+beta)^{-1/2}; Haar mass per link
  >= c(1+beta)^{-3/2}; each plaquette angle <= 4r, so
  1 - W_p <= 8 r^2 = 8/(1+beta). Thus -log Z(beta) <= C V log(2+beta)
  + log 64. Log-convexity with Z(0) = 1 gives E_beta S <= -log Z/beta.
  Equal spatial plaquette expectations: a spatial plaquette function is
  centre-neutral, P_+ commutes with U, with the multiplication operator
  and with spatial translations and rotations (on gauge-invariant
  functions two parallel flip planes differ by a centre gauge
  transformation). So each spatial face has
  E(1 - W_p) <= E S/(3V) <= C log(2+beta)/beta, uniformly in V. Correct.
- L182. |g - h|^2 = 2 - 2<g,h> = 2(1 - W_p). Re g has Haar density
  (2/pi) sqrt(1 - x^2) <= 2/pi. The sign disagreement event lies in
  {|Re g| <= delta} or {|g - h| >= delta}, of probability
  <= C delta + 2 E(1 - W_p)/delta^2 = o(1) with delta the cube root of
  the energy bound. Then E|p_s - I(h)| = o(1); with |I(h) - 1/2| = 1/2
  and |a^2 - b^2| <= |a - b| on [-1/2, 1/2], Var(p_s) -> 1/4 and
  E|(p_0 - 1/2)(p_t - 1/2)| -> 1/4. Uniform in box sizes. On the slope
  of (17), |b_s - p_s| <= e^{2d_r} - 1 -> 0, so the same limits hold for
  b_s. Correct. Both 1/4 values exceed the budget 1/16 of (15).

**S23. Loop form, L207-209. HOLDS.**

- Collinear bonds share no face; the two observation times differ by at
  least three; so each plaquette holds at most one selected bond. Given
  the rest, the selected links are independent with tilt |H| <= 6 beta
  (six incident faces). Row 1145 (1)-(2) gives a sup-density error
  eta(floor(n/2)/(1+6 beta)) for each loop, superpolynomially small when
  beta = O(log n). The two loops are conditionally independent. So each
  sign is fair up to O(eta) and Cov = O(eta). Correct.
- The detour by the three other sides of a transverse face is
  exterior-measurable; |W - W'| = |g - h| by two-sided invariance of the
  chordal distance; anti-concentration of Re W comes from the near-Haar
  law. The (18) limits follow with the energy bound (beta -> infinity).
  The contractible rectangle trace is gauge-invariant and centre-neutral.
  Correct.

**S38. (29), L369-396. HOLDS.**

- L377-382. On the period-2t circle the mode covariance is
  cosh((t - |s|) gamma)/(2 sinh gamma sinh(t gamma)), so
  V_k = coth(t gamma_k)/(2 sinh gamma_k) and rho_k = 1/cosh(t gamma_k);
  W_k = V_k rho_k^2 = 1/(sinh gamma_k sinh(2t gamma_k)). V_k >= c;
  W_k <= C n e^{-c'|k|}/|k| for k != 0 (gamma_k >= c|k|/n, constants
  depend on the aspect 1/1024); W_0 ~ 1/(2 t mu^2) = C_L n log^2 n,
  since 2t gamma_0 -> 0. n gamma_1 -> 2 pi because n mu -> 0. So
  t gamma_1 -> 2 pi/1024, I(X;Y) >= -(1/2) log(1 - rho_1^2) ->
  -log tanh(2 pi/1024) = 5.09, and D_{2t} >= 1 + e^{-2t gamma_1} -> 1.988
  > 3/2. Correct.
- L384. (-Delta_sp)^p has kernel the constants; the site value fixes
  the constant. The information of the ball readings with Y equals that
  of Pi_V X; the Gaussian formula and -log(1 - z) <= 2z on [0, 1/2]
  give the trace bound. Correct.
- L386. Every vector in V annihilates polynomials of degree < 2p (the
  lattice Laplacian lowers degree by two). Subtracting the degree-(2p-1)
  Taylor polynomial of e^{i theta} gives
  ||Pi_V e_k||^2 <= C_p R^3 n^{-3} (R|k|/n)^{4p}, and Pi_V e_0 = 0, so
  the large W_0 does not enter. Sum: Tr(Sigma_V^{-1} W_V) <=
  C_p R^{3+4p} n^{-2-4p}; over n^3 centres, R^{3+4p} n^{1-4p} -> 0
  exactly when p > (1+3 alpha)/(4(1 - alpha)). Each conditional term is
  at most the ball information by the chain rule. Correct.
- L392. The variational formula <v, Sigma_B^{-1} v> = min over
  extensions of <f, Sigma^{-1} f> holds (the stated minimizer is
  admissible and orthogonal to corrections). V_k^{-1} <= 2 sinh gamma_k
  <= C sqrt(mu^2 + lambda_k); Cauchy-Schwarz gives the energy bound
  C R^3 n^{-3}(mu + 1/R + |k|/n). With mu << 1/R the k = 0 term is
  C_L (R/n)^2 log^2 n and the rest is O((R/n)^2). Correct. The extra
  O(log n) local binary questions per reading are absorbed because both
  bounds are o(1) by a power of n. Correct.

Claim 3 verdict: (18), its loop form and (29) HOLD. Both are
obstructions to proof routes, as the file says. Neither gives a Wilson
spectral estimate.

### Step 6. Claim 4: the test (6), with (1)-(5) and the Ising film

**S1. Setup and (1), L13-24. HOLDS.** a = 2m + 2 transitions: two
modified ones and m ordinary ones on each arm. Each marked plane gives
bw spatial links, so N = 2bw per layer. A deleted factor e^{beta W_p}
becomes 1, a ratio in [e^{-beta}, e^{beta}], so
e^{-beta N} U <= L_i <= e^{beta N} U pointwise after gauge integration.
Each L_i = D C_i D/lambda is positive: per spatial link the kernel is
positive definite (Wilson) or the constant kernel (a positive multiple
of a projection); their tensor product commutes with the gauge average;
D-sandwiching keeps positivity. Z_ij/lambda^a = Tr(L_i U^m L_j U^m)
= <A_i, A_j>_HS with A_i = U^{m/2} L_i U^{m/2} (spectral powers; no
pointwise positivity of U^{1/2} is used). R_b >= 1 by Cauchy-Schwarz.
Wording note: at L15 "at each temporal link" means "at each marked or
unmarked spatial link of the transition"; no change to the mathematics.

**S2. (2), L26-31. HOLDS.** In L_0 the marked links enter only through
the flip-invariant magnetic half-weight, so a one-sided flip C_3 or C_4
leaves L_0 unchanged. Every L_i commutes with simultaneous flips. Hence
P L_0 = L_0 = L_0 P, A_0 = P A_0 P, <A_0, A_N> = <A_0, P U^{m+1}>, and
Cauchy-Schwarz gives R_b >= Tr U^a/Tr(P U^a).

**S3-S4. Limits 1 and 4, and (3), L33-43. HOLD given row 1178.**
Row 1178 (5) gives, at fixed cutoff, for w >= K n_0 and arm length
d >= b/16, excited sums <= C e^{-cd/n_0} in the selected transfer. In
the ordinary branch U^d = P_0 + E, ||E||_1 <= C e^{-cd/n_0}. In the
competing branch row 1178 (19) and the proof of (40) keep four levels;
long-odd weight is <= C tanh(beta w^2)^{db}; P removes the three
short-odd levels. So P U^{m/2} = P_0 + E with ||E||_1 <= C e^{-cm}.
k = <psi, L_0 psi> >= e^{-beta N} and ||L_0|| <= e^{beta N} hold.
A_0/k = P_0 + O_HS(e^{2 beta N - cm}) with N = 2bw linear in b and
m ~ e^b/2, so R_b = Tr U^a + o(1). Row 1178 (36):
-log Delta_chi(b) = b t_chi + O(log b) and
t_chi >= c_q w/(n_0^2 log(2+w)) > 1 for large fixed w. With
a = 2 ceil(e^b/2), a Delta_chi -> 0, so R_b -> 1 + 3 = 4. With
a ~ b^2 the same two limits hold. For log a/b -> theta the count
1 + #{chi : t_chi > theta} is correct.

**S5. (4)-(5), L47-56. HOLDS.** E_ii Y = Z_{i+1,i}/Z_ii =
Z_{i,i+1}/Z_ii by the time reflection exchanging the layers;
E_ii(Y Y') = Z_{i+1,i+1}/Z_ii. So v_i = Z_ii Z_{i+1,i+1}/Z_{i,i+1}^2 - 1
>= 0. The cosine of the angle between A_i and A_{i+1} is
(1 + v_i)^{-1/2}, so the angle is arctan sqrt(v_i). The spherical
triangle inequality (proved by splitting off the common vector) gives
(5). arccos(4^{-1/2}) = pi/3. Correct.

**S6. (6), L58-67. HOLDS** (given the neutral premise, row 1161 L148,
L150 and row 1178 (5), (19), (36), (40), all checked).

- Competing branch. Sum over N = 2bw angles >= pi/3 - o(1) and
  arctan x <= x give max_i v_i >= pi^2/(36 b^2 w^2)(1 - o(1)).
  Cov(B_p, B_p') = v_i (E Y)^2/(e^beta - e^{-beta})^2 and E Y >=
  e^{-beta}. So the liminf in (6) is at least
  e^{-2 beta} pi^2/((e^beta - e^{-beta})^2 36 w^2) > 0 for each large
  fixed w. Correct.
- Ordinary branch. For every i, A_i/k_i = P_0 + O_HS(e^{2 beta N - cm}),
  so v_i = O(e^{4 beta N - 2cm}) and b^2 max_i Cov <= C b^2
  e^{8 beta b w - 2cm} -> 0 for each fixed w >= K n_0. Correct.
- Selection. Under the neutral premise, (W) holds over the allowed
  sizes exactly when the ordinary alternative holds at every
  sufficiently fine cutoff (row 1161 L148, L150; the same step as row
  1178 (39)). Correct.
- Note (no verdict change). The display (6) does not restate the time
  period. The file fixes a = 2 ceil(e^b/2) at L33 and allows the even
  integer nearest b^2 at L67. The test needs a/b -> infinity; a reader
  should take a from L33. I suggest restating a in (6).

**S33. Ising film, L305-307. HOLDS.** Each temporal two-spin kernel is
positive semidefinite (eigenvalues 2 cosh J, 2 sinh J, or 2, 0). A fully
deleted layer is rank one in each species, so it is even under each
global flip and (2) applies. Dual even sets with the four boundary
classes, the Peierls bound P(Gamma in D) <= e^{-2J|Gamma|}, the
decomposition into simple cycles, length >= b for a noncontractible
cycle and the count 4 * 3^{l-1} give
P(nontrivial class) = O(ab (3e^{-2J})^b) = O(b (3e^{1-2J})^b) -> 0 for
a ~ e^b. So z -> 0, the ratio in (2) is (2/(1+z))^2 -> 4, and (5) with
N = 2b gives liminf b^2 max v_i >= pi^2/36. Correct.

Claim 4 verdict: (6) HOLDS given the neutral premise and the cited
branch estimates. The Ising film shows the reflection and deletion
identities alone cannot select the branch, as the file says.

### Step 7. The other PROVED statements, the labels, and a guide run

**S7. (7), L73-78. HOLDS.** P_+ commutes with U, so the closed torus
gives Tr(P_+ U^{2t}) = D_{2t}; K_t is symmetric, so the slice law is
K_t(x,y)^2/D_{2t} and the marginal is K_{2t}(x,x)/D_{2t}.

**S8. R(x) >= D_{2t} and (8), L80-88. HOLDS.** P_+(U^t - U^{2t}) >= 0
gives K_t(x,x) >= K_{2t}(x,x); int sqrt(R) d mu = Tr(K_t)/sqrt(D_{2t}).

**S9. (9), L90-95. HOLDS.** Per endpoint link: 4 faces x beta/2 + one
temporal face x beta = 3 beta delta; over v links at two ends,
eta = 6 beta v delta, so C = 6. Numerator and denominator of R(E) each
move by e^{+-2 eta}, giving e^{+-4 eta}.

**S10. (10) and the Markov tail, L97-109. HOLDS.** K_t^2 is a positive
form (Gram matrix of K^{1/2} M_f K^{1/2}); Cauchy-Schwarz against 1
gives nu(E,E) >= mu(E)^2. The 2 x 2 minor gives the upper bound. The
tail bound is Markov's inequality on sqrt(R(E)) - 1 >= 0. The infimum
range is correct.

**S11. (11), L111-115. HOLDS** given row 1161. (5/4) e^{1/25} =
1.3011 < 3/2, and e^{0.04} = 1.0408 <= 25/24. Converse via the Pfaffian
propagation and the Markov tail of (10).

**S12. Balanced bisections, L119. HOLDS.** Hopf coordinates make Haar
uniform (u = cos^2 phi). Exchange symmetry of nu makes one threshold
bisect both marginals. c_A >= 0 by Cauchy-Schwarz for the positive form
on A; c_A <= 1/4 for fair bits; both diagonal cells have 1/4 + c_A.

**S13. (12)-(13), L121-131. HOLDS.** nu(E,E) = prod (1/4 + c_A);
E_fair = sum over leaves with weight 2^{-J}; chord bound
log(1+4c) >= 4 (log 2) c on [0, 1/4]; E_fair |m_E - 1| <= 2 epsilon
because the product is >= max(1, m_E) and E_fair m_E = 1.

**S14. (14), L133-137. HOLDS.** One coordinate change of length s moves
one link by <= C sqrt(s), so the squared kernel has log oscillation
<= 6C beta sqrt(s). With l_0 = c/(1+beta)^2 the density ratio on 3 l_0 is
< 3/2, a short median side would leave two pieces of mass > 2/3 each on
the other side (contradiction), so each split removes min(l_0, l/3);
then O((1+beta)^2) + O(log((1+beta)v/eta)) splits per coordinate and 3v
coordinates. The same oscillation bound holds for the one-slice
marginal used in (28).

**S15. (15), L139-144. HOLDS.** 2^J mu(E) >= 1 on the majority path;
e^{29/100} = 1.336 <= 100/71 = 1.408 < 3/2. The some-path test after
enlargement follows from (11) and (10).

**S16. (16), L148-158. HOLDS.** Quarter-arm projections compose to
P_+ U^t; given M the two observations are independent with law
omega_M; conditional independence gives c_A = Var of the quotient under
the omega_M(A)^2-tilted law.

**S17. Column chain, L160-161. HOLDS** given row 1155 (3) and its
contraction (delta_r = 4 beta tanh(beta)^{r-1}, point inputs allowed).
External fields and endpoint weights do not change cross ratios.

**S18. (17), L163-168. HOLDS.** Left and right messages each have log
oscillation <= d_r, so fixed-end and Haar-end bit laws have pointwise
ratio in [e^{-2 d_r}, e^{2 d_r}]; conditional independence of the two
segments given the four ends gives the constant 4(e^{2 d_r} - 1).

**S19. Discarded contribution, L170. HOLDS.** With
limsup beta/log n < 1/2, r = ceil(e^{2 beta} (log n)^2) = o(n), and
(r - 1)(1 - tanh beta) >= (log n)^2 - e^{-2 beta}, so
d_r <= 4 beta exp(1 - (log n)^2); summed over poly(n) questions -> 0.
log(1 + 4x) is 4-Lipschitz on [0, infinity) and |c_A - x_+| <= |c_A - x|.

**S21. (19), L186-203. HOLDS.** (9) gives m_E sqrt(D_{2t}) <= e^{2 eta}
v_E; good leaves have v_E <= e^{2/32}; so D_{2t} <= (20/19)^2
e^{33/200} = 1.307 < 3/2 (e^{0.165} = 1.179 <= 200/167). Converse:
E_fair B <= epsilon/(2 log 2), and mu{B > 1/32} <= P_fair(B > 1/32)
+ E_fair |m_E - 1| <= (16/log 2 + 2) epsilon. Correct.

**S22. Tree variables, L205. HOLDS.** The map to tree links and
tree-gauge chords has unit Jacobian; the gauge-invariant density does
not depend on tree links, so they are independent Haar at both ends and
c_A = 0 on tree questions; chord count 3n^3 - (n^3 - 1) = 2n^3 + 1.

**S24. (20), L213-229. HOLDS.** Mixed derivative of the log integral is
a covariance of two endpoint exponent changes (each of sup <= 3 beta
delta_e; the magnetic end factors give no mixed term), so the rectangle
is <= 18 beta^2 delta_e^2; exchangeability gives half the rectangle per
link; Hoeffding-type martingale bound for log E e^f - E f (range
6 beta delta_e); Jensen and K_{2t}(x,x) <= K_t(x,x). The constant is
C = 54. Correct.

**S25. Gaussian column screening, L231-235. HOLDS.** Column precision
diagonal 2 + 6 + a^4 and off-diagonal -1; rho = 1/cosh(t alpha) with
alpha >= arccosh 4; Var <= 1/d for V'' >= d on an interval (the
integration by parts is correct); |g'| <= |b|/(2 sqrt B); marginal
log-concavity A - b^2/B; product gives rho/(4 sqrt(1 - rho^2)). Mode
kernel A_0 = 1 + (a^4 + 4 sin^2(pi/n))/2 = cosh gamma, vacuum
exp(-(sinh gamma) x^2/2), ratio e^{-gamma}, gamma < 7/n, so
D_{n/512} >= 1 + e^{-7/512} = 1.986. Correct.

**S26. (21), L239-246. HOLDS** for the datum as assumed. Exponentials
e^{-sE}, s in S, are total in L^2(mu_F) (holomorphy, accumulation point,
moments on [0,1]); the bounded multiplier extends positivity to
1_{[0,M)}. Correct. The outline citation 31606-31626 matches the lane
index (`sa-index/chunk-29.md` L53, lines 31621-31626).

**S27. (22), L248-255. HOLDS** given (H2) as assumed. Squeezing the
monotone diagonal, moment convergence on [0,1], weak convergence; the
plateau test function and the damping lower bound give one direction;
exhaustion of (e^{-hM}, 1] gives the other. Correct.

**S28. Light species, L257. HOLDS.** (Box + mu_j^2) Phi_j =
(mu_j^2 - m^2) phi_m; light covariance O(mu_j^2); the zero-mode factor
(1 - e^{-tau mu_j})^{-1} diverges. The closing sentence "(22) follows"
is a one-line claim; it holds since every vector with a light quantum
carries a factor mu_j.

**S29. (23) and the spectral check, L261-277. HOLDS.** Holomorphy on
Re s > 0, continuity at 0, finite-dimensional span, positivity of
rho_l for small epsilon, Gaussian law fixed by covariance; massless
vacuum uniqueness (omega_0 vanishes on a null set); rho_g supported in
(m^2, 2m^2). Correct.

**S30. Misleading margins, L279. HOLDS.** All entries of the finite
family agree; the gapped margin e^{-Mh} - e^{-mh} > 0 transfers.

**S31. Vanishing summed correlations, L283-293. HOLDS.** Mode
covariances, gamma_k >= c|k|/n, zero mode O_L(1/n), first differences
O(n^{-4}), variance bounded below, Gebelein maximal correlation |rho|;
sum O_L(1/n) + O(1/n) -> 0; D_{2t} >= 1 + e^{-14/1024} > 3/2.

**S32. Hidden first modes, L295-301. HOLDS.** Kernel of
-Delta_sp - kappa_n is the six first modes; six anchors; Y covariances
O(n^{-6}) + O_L(n^{-5}); conditional correlation exactly
1/cosh(t gamma_1); Sheppard: covariance arcsin(rho)/(2 pi); limit
t gamma_1 -> 2 pi/1024.

**Labels and RESULT line.**

- GUIDE L3, L9, L69, L406 agree with the body and FINISH (rows 1179,
  1065 and 1178 had checks in progress at 22:13Z; row 1178's check
  ended 22:45Z). L69 matches row 1178 (41) (signed sheets, 1/b).
- GUIDE L5, L7: lane files exist (`prior/repo-search-2026-11-08.md`;
  no row-specific prior file; open registry line 892 is the W entry
  pointing to the T0 tree; `sa-index` files present). PR and main
  contents and GitHub lines were not checked.
- OPEN L400: the slope 11/(3 pi^2) matches row 1155 L74 (conditional on
  RF10, RF20, RF23-25, RF28). L400, L402, L404 agree with (17), (18),
  (22), (23), (24), (26), (28), (29), (6) and the Ising film.
- No ARGUED label. No PROVED paragraph holds an unproved load-bearing
  claim; its citations are to checked rows.
- RESULT L408 agrees with the body. "(29) obstructs spatially local
  conditioning" refers to a Gaussian comparison model, as the body says.

**Guide run (GUIDE only, proves nothing).** Scratch directory under
/tmp, pure Python with numpy, BLAS threads 1, well under 100 MB.
300 random G-invariant positive kernels on (Z/2)^3 x S, |S| = 2..4, with
s in [0, 0.34], k = 1..5, I_G up to 0.23: (25), the TV display, the
coupling bound, the chain rule, d_G^2 <= I_G, row 1165 (19), (7), (8)
and (10) all held to rounding (largest excess 3e-14). 400 truncated
bivariate Gaussians: the largest found indicator covariance stayed below
rho/(4 sqrt(1 - rho^2)).

### Step 8. Verdict table, counts, what was not checked

| S | Statement (lines) | Verdict |
|---|---|---|
| S1 | Setup, kernel bounds, Gram identity (1) (L13-24) | HOLDS |
| S2 | Deletion projects out short charges, (2) (L26-31) | HOLDS |
| S3 | Limits 1 and 4 given row 1178 (L33) | HOLDS |
| S4 | (3) and the theta count (L35-43) | HOLDS |
| S5 | (4), (5) (L47-56) | HOLDS |
| S6 | (6) equivalent to (W) under the neutral premise (L58-67) | HOLDS (note: restate a in (6)) |
| S7 | (7) (L73-78) | HOLDS |
| S8 | R(x) >= D_{2t}, (8) (L80-88) | HOLDS |
| S9 | (9), C = 6 (L90-95) | HOLDS |
| S10 | (10) and the Markov tail (L97-109) | HOLDS |
| S11 | (11) given row 1161 (L111-115) | HOLDS |
| S12 | Balanced bisections, 0 <= c_A <= 1/4 (L119) | HOLDS |
| S13 | (12), (13) (L121-131) | HOLDS |
| S14 | (14) (L133-137) | HOLDS |
| S15 | (15) (L139-144) | HOLDS |
| S16 | (16) (L148-158) | HOLDS |
| S17 | Column chain given row 1155 (L160-161) | HOLDS |
| S18 | (17) (L163-168) | HOLDS |
| S19 | Discarded contribution under the slope (L170) | HOLDS |
| S20 | (18) with the energy bound (L172-182) | HOLDS |
| S21 | (19) (L186-203) | HOLDS |
| S22 | Tree variables (L205) | HOLDS |
| S23 | Neutral-loop form of (18) (L207-209) | HOLDS |
| S24 | (20), C = 54 (L213-229) | HOLDS |
| S25 | Gaussian column screening (L231-235) | HOLDS |
| S26 | (21) (L239-246) | HOLDS |
| S27 | (22) (L248-255) | HOLDS |
| S28 | Light-species example (L257) | HOLDS |
| S29 | (23) and spectral/locality check (L261-277) | HOLDS |
| S30 | Misleading finite margins (L279) | HOLDS |
| S31 | Vanishing summed correlations (L283-293) | HOLDS |
| S32 | Hidden first modes (L295-301) | HOLDS |
| S33 | Ising film obstruction for (6) (L305-307) | HOLDS |
| S34 | (24), (25) (L311-342) | HOLDS |
| S35 | (26) (L344-349) | HOLDS |
| S36 | (27) (L351-357) | HOLDS |
| S37 | (28) (L359-365) | HOLDS |
| S38 | (29) (L369-396) | HOLDS |

Counts: 38 PROVED statements (62 PROVED paragraphs) checked line by
line by hand, positive claims first. 38 HOLD. 0 HOLD AFTER CORRECTION.
0 FAIL. GUIDE (6 paragraphs), OPEN (3) and the RESULT line agree with
the body; no ARGUED label occurs.

Wording notes (no verdict change):

1. (6), L58-61: the display does not restate the time period. The file
   fixes a = 2 ceil(e^b/2) at L33 and allows the even integer nearest
   b^2 at L67. The test needs a/b -> infinity. Suggest writing
   "with a = 2 ceil(e^b/2)" in (6).
2. L15: "at each temporal link" should read "at each spatial link of
   the transition" (the deleted or Wilson factor sits on the temporal
   plaquette of that link).

Who checked what. Every verdict above is mine, by hand. For inputs I
did not re-derive I relied on the recorded checks: row 1161 by row 1162
(Theorem S-w use, Proposition B3 and Lemma E' enlargement, the constants
of the K = 512 test), row 1165 by row 1166 ((3); I re-derived (19)),
row 1178 by row 1185 ((5), (17)-(19), (36), (40) internals), row 1155
by row 1156 (contraction proof internals; I re-checked the statement),
row 1145 by row 1146 (Bessel-ratio bound internals), row 1173 by row
1174, row 1177 by row 1182, rows 1179 and 1065 by row 1183 (HOLDS AFTER
CORRECTION; row 1186 uses them only as conditional consumers). This
check is cross-provider (row 1186 is by gpt-6.2-astra). It is not an
audit.

Not checked:

- External sources named in GUIDE L5 and L7: PR 10114, 10133, 10134,
  10141, main `8b11ae2bb9` (Theorem ZD-c), and the GitHub outline and
  CA-I lines. I checked only that the lane files they point to exist
  and that `sa-index/chunk-29.md` L53 matches outline 31621-31626.
- The continuum datum, (H2) and (TOT) in (21)-(22): taken as the stated
  hypotheses.
- Row 668 (`gap-os-equiv.md`): cited only in a comparison sentence at
  L244; not read.
- The flow inputs RF10, RF20, RF23-25, RF28 behind the slope
  11/(3 pi^2) (row 1155 L74): taken as cited.
- The guide runs test random finite models and truncated Gaussians only.
  They cover no Wilson estimate and prove nothing.

Open, as the file says: the physical neutral estimate ((26) or (28) for
the Wilson law on one fixed physical side), the periodic wall (W) (a
Wilson upper bound for (6)), the direct continuum route (22), and the
four-dimensional SU(2) Yang-Mills mass gap.

RESULT (2026-11-19 23:29Z (date -u; started 23:00Z), Claude Opus 5.5 max, laptop subagent; cross-provider check of gpt-6.2-astra row 1186, grants no status): row 1186 HOLDS. 38 PROVED statements (62 paragraphs) checked line by line by hand, positive claims first: 38 HOLD, 0 corrections, 0 FAIL. The equivalence of the physical one-cube neutral bound with (26) and with the binary test (28) holds over the allowed dyadic sides (via (24), (27), row 1161's checked K = 512 test and Pfaffian propagation, and row 1165 (19), re-derived here); the uniform entropy bound (24) holds with absolute constants; the obstructions (18) (also for a neutral loop) and (29) hold; (6) is equivalent to (W) under the neutral premise given row 1178's checked estimates, and the Ising film shows the identities alone cannot select the branch. Two wording notes (restate a = 2 ceil(e^b/2) in (6); "temporal link" at L15 means spatial link). Guide runs agree and prove nothing. The physical neutral estimate, (W), the continuum route and the four-dimensional SU(2) mass gap remain OPEN.
