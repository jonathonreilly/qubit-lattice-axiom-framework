# Check of library/gap-mech-selective-fact-astra62.md (FINISH row 1543)

Checker: Claude (Opus 5.5). Target: row 1532, author gpt-6.2-astra max.

## Plan
1. Read GOAL.md, FINISH.md Rules / Working efficiently, the target note in full.
2. Check: walk construction and erasure rules; event B cap E; lowest-eigenvalue estimates (both directions, exponent 2/d); inequality (3) and uniformity over post-hoc axes; Wilson loops of growing diameter; flat-field nonlocality example; d = 5 and U(1) statements.
3. Selectivity: 4D-specific or generic d-dependence. Compare check 1535 and Proposition NEG of row 1386.
4. Physical-units content, prior results on file (rows 1141, 1283, grep), consumers.
5. Verdict per statement; RESULT line.

## Progress
(steps written below as they complete)

- Step 1 done. Read GOAL.md, FINISH.md Rules and Working efficiently, row 1532 note in full (190 lines),
  row 1532 and 1535 FINISH entries, Proposition NEG / Remark STAB / requirements (a)-(i) of row 1386,
  row 1141 (2) statement, row 1283 (1)-(4), check 1387 decision, check 1535 verdict table.
  A numeric guide check of (8) was attempted and not run (numpy is not importable under `python3 -I`);
  everything below is by hand.

## Step 2. Line-by-line check of the mathematics

### Decisive outcome

The Theorem (1) HOLDS as stated: with Wilson probability at least 1 - N^-p, uniformly for beta in [2, 3],
exp(-C N^2 h_4) <= W_N <= exp(-c N^2 h_4) in 4D SU(2); the same construction gives h_5 in 5D SU(2); W_N = 1
identically in 4D compact U(1). I found no failing line. Two remarks that change its reading, not its truth:

- **R1 (the lower end beta >= 2 is never used).** Every probabilistic input is the j-link conditional density
  bound e^(-K_d j) <= density <= e^(K_d j) relative to product Haar, valid for all beta in [0, 3]. So (1)
  holds verbatim for beta in [0, 3], including beta = 0 (product Haar), and for any gauge-field law with those
  j-link density bounds.
- **R2 (every step is written for general d >= 2).** d enters only through K_d = 12(d-1), the 3^d cells, the
  number t^(-d/2) of cells or links in a cube of side ~ t^(-1/2), and the walk on 2d letters. The one
  d-restriction is rho_N^(-2)/h_d -> infinity, which holds with rho_N = (log N)^(1/6) iff 2/d > 1/3, that is
  2 <= d <= 5. For d >= 6 replace rho_N by floor((log N)^(1/(2d))): then rho_N^2 h_d = (log N)^(-1/d)
  (log log N)^(2/d) -> 0 and every line goes through. So (1) with h_d holds in every dimension d >= 2.

### Lattice, walk, observable (lines 15-25) — HOLDS

- Lazy walk: hold 1/2, each of 2d neighbours 1/(4d). Correct total.
- Erasures. Erasing a hold changes nothing in H_U. Erasing an adjacent inverse pair (a backtrack x->y->x)
  removes U_xy U_yx = 1. Erasing an inverse first/last pair (x0->x1 ... x1->x0) changes the loop rooted at x0
  with holonomy U_{x0x1} H' U_{x1x0} into H' rooted at x1; tr Ad is conjugation invariant. Free reduction in
  the free group F_d on the d direction letters is unique, and cyclic reduction is unique up to the root, so
  the reduced loop and its vertex set (hence its diameter) are well defined. The character is preserved.
  HOLDS.
- B intersect E. E is defined on closed paths only (B), as stated; P_X(B intersect E) >= N^-d/2 > 0 for large
  N (shown at line 166, checked below), so the conditional average W_N is well defined. HOLDS.
- Gauge invariance of lambda and W_N (line 48): a gauge transformation conjugates L_U by the block-diagonal
  orthogonal matrix diag(Ad g_x) and conjugates every closed holonomy at its root. HOLDS.

### j-link density bound (line 58) — HOLDS

Each link lies in 2(d-1) plaquettes; (1/2) Re tr U_p lies in [-1, 1] (range 2); beta <= 3, so each term of the
log-weight has range <= 6, and the at most 2(d-1)j affected terms give range <= 12(d-1)j = K_d j. Max/min of the
unnormalized conditional weight <= e^(K_d j), so the normalized density lies in [e^(-K_d j), e^(K_d j)].

### Inequality (3) and its uniformity over axes (lines 60-68) — HOLDS

- NE and SW plaquettes at the centre of a 3^d cell share only the vertex x; their 8 links are internal to the
  cell. Choose one link of each as private.
- For q = cos(theta) + a, Ad(q) is the rotation by 2 theta about a-hat, so |v - Ad(q)v|^2 = 4 sin^2(theta)
  |v_perp|^2 = 4|a x v|^2. Checked.
- D_x/4 = min_{|v|=1} v^T[(|a1|^2+|a2|^2)I - S]v with S = a1 a1^T + a2 a2^T of eigenvalues mu1 >= mu2 >= 0 = mu3;
  the minimum is mu2, the smaller Gram eigenvalue. Checked.
- mu2 >= det/trace = |a1 x a2|^2/(|a1|^2+|a2|^2) >= |a2 x a1-hat|^2/2 when |a1| >= |a2|. So D_x >= 2|a2 x a1-hat|^2.
  Checked.
- Under product Haar on the two private links (others fixed), q1 and q2 are independent Haar (left/right
  invariance and inversion). Given q1, |a2 x a1-hat|^2 is the squared length of the two coordinates of q2
  orthogonal to (1, a1-hat), uniform on [0, 1] (Hopf coordinates; surface element (1/2) ds dtheta dphi).
  So each ordering contributes <= u/2, total <= u under Haar, and <= e^(2K_d) u under the Wilson conditional
  law (two links). Averaging over the other exposed links of the cell gives (3) conditional on the outside.
- Uniformity over axes chosen after seeing the field: D_x is already the minimum over v, so (3) bounds the
  event "some axis is nearly fixed by both rotations", whatever rule picks the axis. HOLDS.
- Remark: (3) is row 1283 (2) and row 1141 (3)-(4) with the explicit constant e^(2K_d) in place of C b;
  it is lattice-local (one 3^d cell) and holds verbatim in every d >= 2.

### Neumann block inequality (4) (lines 70-77) — HOLDS

- Partition of each coordinate circle into lengths in [r, 2r] (N >= r); floor(L/3) >= L/6 for L >= 4, so
  M >= |A|/6^d disjoint 3^d cells.
- Good root: telescoping 4 transported differences around each loop and Cauchy-Schwarz gives
  |s_x - Ad(q_i)s_x|^2 <= 4 sum_{loop i}|grad s|^2; summing i = 1, 2 and using D_x >= u gives u|s_x|^2 <= 4 sum.
- Poincare: I recomputed the variance sum. With coordinate-by-coordinate paths, sum_x (f_x - fbar)^2 =
  (1/2|A|) sum_{x,y}(f_x-f_y)^2 <= (d/2) sum_i L_i^2 E_i <= 2d r^2 Q_{U,A}; matches line 77. |f_x - f_y| <= |grad_U s|
  by orthogonality of Ad.
- Combining: |G| fbar^2 <= 2 Var + (8/u)Q with |G| >= |A|/(2 6^d) gives (4) with A_d = 2d + 8d 6^d,
  B_d = 16 6^d (my constants). HOLDS.

### First line of (2) (lines 79-85) — HOLDS

r = floor(a t^(-1/2)), u = kt with A_d a^2 + B_d/k < 1/2 gives Q_A >= 2t ||s||_A^2 on a good rectangle. Successive
conditioning over disjoint cells (earlier indicators are measurable outside the next cell) gives (H_d k t)^j for
j specified cells; a rectangle fails only if at least ceil(M/2) cells are bad: <= 2^M (H_d k t)^(M/2) =
(4 H_d k t)^(M/2) <= exp(-c t^(-d/2) log(1/t)) using M >= c t^(-d/2). Crossing bonds are nonnegative, so all
rectangles good implies lambda >= 2t > t. Union bound over <= N^d rectangles. HOLDS.

### Second line of (2) (lines 87-102) — HOLDS

- s = ceil(2 pi sqrt(d/t)), delta = sqrt(t)/(4 sqrt d). Cap mass >= c delta^3; j <= d s^d internal links;
  joint conditional probability >= (e^(-K_d) c delta^3)^(d s^d) >= exp(-C F_d(t)). Checked.
- Trial phi v: |phi_x v - phi_y Ad(U)v|^2 = (phi_x - phi_y)^2 + phi_x phi_y |v - Ad(U)v|^2 (exact, using
  |v - Ad U v|^2 = 2 - 2<v, Ad U v>). |v - Ad(U)v| = |vU - Uv| <= 2|1 - U|. Sum of extra terms <= 4 d delta^2 ||phi||^2.
  Scalar Dirichlet quotient 2d(1 - cos(pi/(s+1))) <= d pi^2/(s+1)^2 <= t/4; 4 d delta^2 = t/4. Total <= t/2.
  Crossing bonds see phi = 0 outside, so only the scalar energy. Checked.
- J >= c (N/s)^d cubes with vertex-disjoint interiors; each success event has conditional probability >= q
  given all links outside its own internal links, and earlier failures are measurable there. So
  P(all fail) <= (1-q)^J <= exp(-c N^d t^(d/2) e^(-C F_d(t))). HOLDS.

### (6) and (7) (lines 104-120) — HOLDS

(xi h)^(-d/2) = xi^(-d/2) log N / log log N and log(1/(xi h)) = (2/d)(LL - LLL) - log xi give (6). xi_- small makes
the first line <= N^(-p-1); xi_+ large makes C F_d <= (d/2) log N, so the second line is <= exp(-c N^(d/2) t^(d/2))
<= N^(-p-1). The size conditions t < t_0, N >= C t^(-1/2) hold eventually (t^(-1/2) ~ (log N)^(1/d)). Constants
depend on d and on beta only through beta <= 3. HOLDS.

### Where 2/d comes from (line 122) — HOLDS, and it is the Lifshitz-tail exponent

A low mode at level t needs a region of side ~ t^(-1/2), so ~ t^(-d/2) cells (upper bound) or links (lower bound),
each costing ~ log(1/t) (a small-ball event of probability ~ t, or a cap of mass ~ t^(3/2)). So
-log P(lambda_box <= t) ~ t^(-d/2) log(1/t), and the extreme over N^d positions gives lambda ~ (log log N/log N)^(2/d).
This is the Lifshitz tail of a random operator with a polynomially small single-site probability near the
spectral bottom (recalled from the random Schrodinger literature, Lifshitz; Kirsch-Martinelli; Simon 1985 for the
Anderson model; Nakamura for random magnetic Laplacians; not re-read here, not load-bearing). Row 1283 (4) already
records the d = 3 form -log E n_Y(u) ~ u^(-3/2) log(1/u).

### (8) and the two-sided trace bounds (lines 126-145) — HOLDS

From Q_U, L_U = 2d I - A_U with off-diagonal blocks Ad(U_{x,i}) and its transpose, so K_U = I/2 + A_U/(4d): diagonal
block I/2, neighbour block Ad(U_xy)/(4d), the walk kernel. 0 <= L_U <= 4d I by |a - b|^2 <= 2|a|^2 + 2|b|^2.
(K^m)_{x0 x0} = sum over closed paths of prob times Ad(U_{x0x1} U_{x1x2} ...), so Tr K^m = 3 N^d J_U. With all
eigenvalues in [0, 1] and top eigenvalue 1 - lambda/(4d): mu^m <= Tr K^m <= 3 N^d mu^m. (9): on (7),
lambda/(4d) <= 1/2 eventually; m h_d/log N = N^2 h_d/log N -> infinity absorbs 3 N^d. HOLDS.

### Walk estimate (10) (lines 147-164) — HOLDS

- Lift to the 2d-regular tree (Cayley graph of F_d): increments (2d-1)/(4d), 1/2, 1/(4d) away from the root; the
  root reflection gives k_m >= sum Y_j by monotone coupling; Cramer bound P(k < eta m) <= e^(-cm). Checked.
- Conditional on k, the reduced word is uniform on the sphere (the lazy simple walk is invariant under
  root-fixing tree automorphisms, which act transitively on spheres). Checked.
- j = floor(k/4) cyclic cancellations prescribe the last j letters from the first j; each has conditional
  probability <= 1/(2d-1): <= (2d-1)^(-floor(k/4)). Otherwise the cyclically reduced word w_{j+1}..w_{k-j} has length
  > k/2 and is a contiguous segment. Checked.
- Martingale: E[v_{i+1}|past] = v_i/(2d-1) in both cases; M_i = z_i + v_i/(2d-2) has zero drift (I recomputed:
  ((2d-1)/(2d-2))(v_i/(2d-1)) - v_i/(2d-2) = 0); conditional variance of v_{i+1} is (2d-2)/(2d-1)^2 if v_i = +-1 and
  2/(2d-1) if v_i = 0, so nu_d = 1/(2d-2) > 0 works. |M - z_*| <= rho + 3/2 up to sigma. Optional stopping gives
  E sigma <= C_d rho^2 uniformly in the state (position, incoming letter); iterated Markov gives survival
  <= C e^(-ch/rho^2). No wrapping for 2 rho + 2 < N. Union over <= m + 1 starts. HOLDS.
- The bound is taken on the unconditioned walk and intersected with B, as stated; correct since
  P(B intersect E^c) <= P(union of the three bad events).

### Final assembly (lines 166-174) — HOLDS

P_X(B) = N^-d Tr K_sc^m >= N^-d (K_sc >= 0, constant eigenvector). rho_N^(-2)/h_d -> infinity for d = 4, 5
((log N)^(2/d - 1/3) / (log log N)^(2/d)). So R_N <= J_U/2 and R_N <= N^-d/2 for large N; numerator in
[J_U/2, 3J_U/2], denominator in [N^-d/2, 1]; W_N in [J_U/2, 3 N^d J_U]; (9) absorbs N^d. (1) follows. HOLDS.

### U(1), the single test, the flat-field example, centre blindness (lines 178-188) — HOLDS

- U(1): the adjoint representation of an abelian group is trivial, tau = 1, W_N = 1 for every field. HOLDS
  (for every abelian group, every law, every d).
- h_5/h_4 = (log N/log log N)^(1/10) -> infinity; h_4 = o((log N)^(-4/9)) (ratio (log N)^(-1/18)(log log N)^(1/2));
  (log N)^(-4/9) = o(h_5) (ratio (log N)^(-2/90)(log log N)^(-2/5)). The single test exp[-N^2 (log N)^(-4/9)] < W_N < 1
  has probability -> 1 in 4D SU(2), 0 in U(1), -> 0 in 5D SU(2). HOLDS.
- Flat-field example: g on the seam links is a flat connection with holonomy g around one cycle, gauge
  equivalent to identity on contractible boxes. The straight winding loop (N steps plus N^2 - N holds) is in B,
  is cyclically reduced, has periodic diameter floor(N/2) >= rho_N, positive probability, and tau(g) < 1 for g
  noncentral; all other characters are <= 1. So W_N < 1 = W_N(identity). HOLDS. It shows W_N is a global
  (toron-sensitive) observable.
- Centre blindness: Ad(-U) = Ad(U), while a sign flip changes the Wilson action. The note's statement that (1)
  gives no bound on the seed ratio HOLDS (as a statement of no consumer).

## Step 3. Selectivity, physical content, prior work, consumers

### Is the 4D/5D contrast specific to four dimensions? — No: generic d-dependence (the Lifshitz exponent 2/d)

- By R2 the theorem holds in every d >= 2 with h_d = (log log N/log N)^(2/d), by the same proof. The exponent 2/d
  is strictly monotone in d with no special value at d = 4. The note's own line 122 says so: dimension enters
  only through the t^(-d/2) cells or links of a cube of side ~ t^(-1/2), a volume count.
- Consequence for the single test of line 181: since h_d is decreasing in 2/d, the test
  exp[-N^2 (log N)^(-4/9)] < W_N < 1 passes with probability -> 1 for SU(2) in d = 2, 3, 4 and fails for d >= 5.
  The cut at 4/9 is a choice: any alpha in (2/(k+1), 2/k) separates d <= k from d >= k+1 for each k. Nothing
  singles out four.
- **Counterexample to reading the contrast as gap versus no gap (PROVED by R1 plus the literature).** By R1 the 5D
  form with h_5 holds for 5D SU(2) at every beta in [0, 3]. 5D SU(2) at small beta (for example beta = 0, product
  Haar) has a mass gap by the strong-coupling expansion (Osterwalder-Seiler; recalled, not re-read). So the
  4D/5D test fails with probability -> 1 also on a gapped 5D model, and the 5D exponent is the same on both sides
  of the believed 5D bulk transition (near beta ~ 1.6, Creutz 1979; recalled, belief grade). W_N reads d, not
  the gap.
- **Phase blindness inside 4D.** By R1, (1) with h_4 holds for 4D SU(2) at every beta in [0, 3] and for any law
  with the j-link density bounds, for example SU(2) with a frozen-length adjoint Higgs at bounded hopping
  (the hopping adds bounded link terms; ARGUED, not written out). So (1) cannot separate 4D SU(2) from 4D
  SU(2) with an adjoint Higgs in a phase believed gapless where that phase meets the bounded regime;
  I state this as ARGUED only, since I did not check where that phase lies relative to beta <= 3.
- **Compared with check 1535.** There the 4D/5D split of row 1530 was the free mode count R^(4-d), which is at least
  marginal exactly at d = 4. Here the split is the Lifshitz exponent 2/d, which has no threshold at d = 4 at all.
  Both are dimension counting; this one is weaker.
- **Compared with Proposition NEG of row 1386.** NEG (b): members of F_loc hold in 5D at the same coupling with
  changed local counts. Row 1532's theorem is a statement of that kind: it holds in 5D (and every d) with the
  count t^(-d/2) changed. Its probabilistic inputs are exactly F4-type cell facts (row 1141 (3)-(4), row 1283 (2)),
  combined by a union bound / extreme-value step that is valid in every d. So it does not escape NEG (b). It
  also does not escape NEG (a): it is a fixed-bare-coupling statement, and on the calibrated trajectory
  beta_K -> infinity, so at late cutoffs (n_K, beta_K) is outside its domain. It fails filter (t2)
  (5D, applied to the step) and (t4) of row 1386 Section 4.5 is moot (it is not a seed hypothesis).
  The U(1) contrast is the triviality of the adjoint of an abelian group (true for every law and every d), so
  it meets filter (t1) only in this trivial sense.

### Content beyond one lattice site in physical units along the calibrated trajectory — No

- In lattice units at fixed beta in [2, 3]: yes formally. lambda(U) is a torus-global quantity and the loops have
  diameter >= rho_N -> infinity; the flat-field example shows W_N is not local.
- But the value of W_N is fixed by lambda, and lambda is fixed by the extreme-value statistics of cells of
  side 3 and of rare near-flat cubes of side ~ (log N/log log N)^(1/d) lattice units. The inputs are one-link
  and j-link density bounds that hold equally at beta = 0.
- Along the calibrated trajectory at late cutoffs beta_K grows like the log of the cutoff, outside [2, 3]; the
  proof's constants (H_d = e^(2K_d), with K_d proportional to beta) degrade as beta grows, and nothing is stated
  at beta_K. A bare beta in [2, 3] is one fixed lattice spacing. So at a fixed physical side L and late cutoffs
  the result has no content. This is the same judgement as check 1535 gave for row 1530, for a different reason
  (there: scales R <= beta^(1/16); here: a fixed bare coupling).

### Already on file? — Mostly; the sharp typical-sample torus form is new

- Upper half of (1), up to a (log log N)^(1/2) factor in the exponent: row 1141 (2) gives, with probability
  >= 1 - (2+R)^(-k), the Neumann adjoint form on a growing d-cube (2 <= d <= 4) in 4D Wilson SU(2) bounded below by
  c/(1 + b + (log(2+R))^(2/d)). Taking the cube to be the whole box (R ~ N; dropping the wrap bonds only lowers the
  form) gives lambda(U) >= c(log N)^(-1/2) w.h.p., hence by the identity (8) and the walk estimate (10)
  W_N <= exp(-c N^2 (log N)^(-1/2)). Row 1532 sharpens the exponent by (log log N)^(1/2).
- The Lifshitz form with the log(1/u) factor: row 1283 (1) and (4), two-sided, in expectation, on a 3D time slice,
  same cell test (2), same Neumann inequality (3), same Dirichlet sine cubes.
- New in row 1532: the 4D (and 5D) full-torus statement; the low-mode lower bound as an existence statement in a
  typical sample (row 1283 has it in expectation); the matching two-sided lambda ~ h_d with the log log factor;
  the walk representation (8) with the reduced-diameter cutoff (10). My grep of library/ and FINISH.md for
  Lifshitz, log log N, adjoint loop or adjoint character and adjoint Laplacian found no earlier statement of these.

### Consumer on file? — None found

- The seed (PUR-io) of `gap-k2-tool-design-fable.md` Section 3.1 is a ratio of centre-averaged twisted transfer
  traces at beta_K. W_N is centre-blind (Ad(-U) = Ad(U)) and is stated at fixed beta; the note says it supplies no
  bound for that ratio, and I agree.
- Row 1283 (5)-(7) use slice coercivity, which row 1283 proves itself on 3D slices; they need nothing from (1).
- grep for open items that need a torus-wide adjoint eigenvalue or an adjoint walk average found none (hits
  are on Hessian identifications, check 1387 and rows 1530-1543 themselves).
- Equivalent is not progress: (1) is not proposed as sufficient for anything, so the rule does not bite; it is
  not equivalent to the seed (it is true and centre-blind; the seed is open).

## Step 4. Verdicts

Provenance: Claude Opus 5.5, by hand, against the lane file at the checkout read on 2026-11-25; no numeric run
(the one guide script did not run), no Lean check; not an audit.

| Statement | Verdict |
|---|---|
| Theorem (1), 4D SU(2), probability >= 1 - N^-p, uniform in beta in [2, 3] | HOLDS (also for beta in [0, 3]: R1) |
| Same construction in 5D gives h_5 | HOLDS (and in every d >= 2 with h_d, rho_N adjusted for d >= 6: R2) |
| W_N = 1 for 4D compact U(1) | HOLDS (trivially: the abelian adjoint is trivial) |
| Erasure rules preserve the adjoint character; B intersect E well defined | HOLDS |
| j-link density bound, K_d = 12(d-1) | HOLDS |
| Inequality (3), H_d = e^(2K_d), uniform over axes chosen after the field | HOLDS (min over v is built in) |
| Neumann block inequality (4) | HOLDS |
| (2) first line, P(lambda <= t) <= N^d exp(-c F_d(t)) | HOLDS |
| (2) second line, typical-sample low mode | HOLDS |
| (6), (7), source of 2/d | HOLDS; 2/d is the Lifshitz-tail exponent, a volume count |
| (8), (9) trace identity and two-sided bounds | HOLDS |
| (10) walk estimate and the final assembly | HOLDS |
| Single test separating 4D SU(2) from U(1) and 5D SU(2) | HOLDS as stated; it equally passes in d = 2, 3 and fails in gapped 5D SU(2) at small beta |
| Flat-field nonlocality example | HOLDS |
| Centre blindness / no bound on the seed ratio | HOLDS |
| Selectivity in dimension (property specific to 4D) | FAILS: first failing line 122 ("The power is 1/2 in four spacetime dimensions and 2/5 in five"): the power is 2/d in every d >= 2 by the same proof; counterexample: 5D SU(2) at beta = 0 (gapped) obeys the same 5D bound |
| Content beyond one lattice site in physical units on the calibrated trajectory | No (fixed bare coupling; extreme-value statistics of lattice cells; nothing at beta_K) |
| On file | Upper half up to (log log N)^(1/2): row 1141 (2) with (8), (10); Lifshitz form: row 1283 (1), (4) in 3D, in expectation. New: sharp two-sided typical-sample torus form in d = 4, 5 and the walk packaging |
| Consumer on file | None |

RESULT Check 1543 of row 1532: every mathematical statement checked HOLDS, including Theorem (1) in 4D and 5D SU(2) uniformly for beta in [2, 3] (in fact [0, 3]), W_N = 1 for U(1), the erasure rules, (2)-(10) and the flat-field example; but the selectivity in dimension FAILS at line 122: the theorem holds in every d >= 2 with h_d = (log log N/log N)^(2/d), a Lifshitz-tail volume count with no special value at d = 4 (weaker than check 1535's marginal R^(4-d)), it holds equally for gapped 5D SU(2) at beta = 0, the U(1) contrast is the triviality of the abelian adjoint, it is a fixed-bare-coupling statement with no content in physical units on the calibrated trajectory, it does not escape Proposition NEG (a) or (b), its upper half is on file up to a (log log N)^(1/2) factor (row 1141 (2)) and its Lifshitz form in 3D (row 1283 (1), (4)), and no consumer on file can use it; no progress toward (PUR-io).
Checked line by line by Claude (Opus 5.5).
