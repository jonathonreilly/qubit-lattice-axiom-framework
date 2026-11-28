lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-25T06:31Z

# Check of row 1492: normalized activities at the nonlinear Cartan stripe centre

Row 1494, Mac mini worker 2. Started 2026-11-24T18:31Z (date -u). Pinned commit 52ccf5168.
Provenance: Claude Opus 5.5, effort high, cross-provider check of
`library/gap-k2-nonlinear-activity-astra62.md` (gpt-6.2-astra max). Not an audit.
Credit: Balaban (CMP 89-122), Kotecky-Preiss (cluster expansion criterion),
Sussman-Alpoge complete account (with Claude and Codex as authors of their text).

## Plan

1. Read the checked file in full; read rows 1480/1490 sources only where it cites them
   (coordinates (6), activity (7), joint denominator (10), stripe interval, Hessian 1/108900).
2. Check line by line, in order:
   (a) exact marked integral (1) and joint normalization (2) about the stripe;
   (b) obstruction for the row 1490 (7) activity: rate (4), two-site trial field,
       witness x = 10^(40 37,632);
   (c) cold complement at x = 100, above 1 - 12e-21;
   (d) unsplit Taylor-remainder tests and the all-domain lower bound (8), its source interval;
   (e) adjacent-block test and threshold 1/(81 e).
3. Verdict per statement (HOLDS / HOLDS AFTER CORRECTION / FAILS at first wrong line),
   at most ten defects ranked by what they break.

Status: complete; verdict at the end.

## Sources read

- Checked file `library/gap-k2-nonlinear-activity-astra62.md` (row 1492), in full.
- Row 1490 `library/gap-k2-nonlinear-pin-astra62.md`, in full: stationarity, (1)-(6), (7). Taken as input,
  not rechecked here (row 1491 recorded rows 1489 and 1490 HOLD).
- Row 1480 `library/gap-k2-integrated-activity-astra62.md` lines 23-262: setup (1)-(4), the
  stripe mean, (5)-(11), lines 162-167 (radial ratio), 182-193 (square interchange).
- Row 1472 `library/gap-k2-t1-small-field-astra62.md` lines 16-143: the star-connected
  incompatibility, closed star of 81 blocks.
Repo search for this check: the statements checked here are row 1492's own; I make no new claim
beyond repairs and scope notes, so there was nothing to grep in open-core for novelty.

## Step 1 (done 2026-11-24T18:40Z). Exact marked integral (1) and joint normalization (2): HOLDS

Re-derived independently.
- Haar in right-translated exponential chart: W = e^Z W*, normalized Haar = (2 pi^2)^{-1} (sin|Z|/|Z|)^2 d^3Z
  on |Z| < pi; total 4 pi int_0^pi sin^2 = 2 pi^2. Correct.
- With kappa = x (a = 1): k_c = e^{x Re(M V^-1)}/F(x|M|) = k_0 e^{-x(|M| - Re M V^-1)} h(x)/h(x|M|),
  k_0 = 1/h(x), h(s) = e^{-s}F(s). Hence Z(V) = k_0^{4N} (2pi^2)^{-49N} int prod_e j(Z_e) 1_{|Z_e|<pi}
  exp(-x sum_B S_B) prod_c h(x)/h(x|M_c|) d^nZ, matching row 1480's normalization of Z(V).
- S_B(0) = N_1(t) for every block: at the stripe the eight odd-layer (1,2) plaquettes of B have angle v,
  the direction-2 pin costs 1 - cos(t - v), the direction-1 pin costs 0; and
  |8 + e^{it}| = 8 cos v + cos(t - v) because Im(e^{-iv}(8 + e^{it})) = 0. So 8(1 - cos v) + 1 - cos(t - v) = N_1(t). Correct.
- sum_B l_B Z = 0 is a linear identity on the whole slice (row 1490 stationarity), so it may be used off
  the convexity box; Gaussian integral (2pi/x)^{n/2} det(H_t)^{-1/2} needs H_t > 0, which is row 1490 (5).
  Every free link is assigned to (hence read by) its origin block, so prod_B 1_{D_B} is the full chart.
- (2) is the ratio of physical integrals; all patterns share the denominator. Normalized marked polynomial,
  e^{-P} restoration, and the self budget |z| <= u e^{-u} <= 1/e: correct.

## Step 2 (done 2026-11-24T18:40Z). Obstruction (3)-(4) for the row 1490 (7) activity, and the witness x = 10^(40*37,632): HOLDS

Re-derived independently.
- Rate of j^old at a trial field A: G_* - sum_{D != B} G_D(A) - S_B(A) = -[sum_D G_D(A) - G_*] + [G_B(A) - S_B(A)].
  With 1 + z~ = e^{-P^old - x(G_1 - N_1)} j^old and G_B(m) = 4 w^2 + 32 w^2 = 4t^2/9 = G_1, the rate of
  1 + z~ is N_1 - S(m) + (gain - cost) - lim P^old/x. Correct.
- Trial field I d(phi), phi = s/2 on B, -s/2 on B + e_2: block-constant Cartan gradient on a Cartan
  background, so every fine group plaquette and every internal (tree) link is unchanged; each contour
  crosses exactly one face, so each coarse mean is rotated by e^{I Delta phi_c}. Gaussian cost
  (1/2)(s^2 + 14 s^2/4) = 9s^2/4: 1 + 7 + 7 edges, distinct on the 4^4 torus. Correct.
- Discrepancy change: direction 2, angle -beta -> -beta - s, g(q) = q^2/2 - 1 + cos q convex,
  g'(-beta) = -(beta - sin beta) = -b, gain >= b s. Direction 1: mean cos(w/2) e^{-Is/2}, change
  q^2/2 - r(1 - cos q) >= 0. Directions 3, 4 with r = 1: >= 0. Optimum s = 2b/9 gives b^2/9. Correct.
- (3): |8 + e^{it}| = sqrt(A^2 + L^2) with A = 8 cos w + cos beta, L = 8 sin w - sin beta, since t - w = beta.
  0 < L (sin w > sin(8w)/8 by concavity) and b - L = 8(w - sin w) > 0; A >= 9 cos beta > 8. So
  S(m) - N_1 < L^2/(2A) < b^2/16, and the margin is 7b^2/144. Correct.
- Finite witness: b > beta^3/7 = 1/5103 > 1/6000; margin > 1.35e-9; gradient of the rate on the
  eta-ball below 1536 + 440 + 464 + 1000 < 5000; Haar and radial factors >= 4^{-49} 2^{-4*27} = 2^{-206};
  inscribed cube side 2 eta/sqrt(n) > 1e-18 (sqrt 37,632 < 194); D x^{n/2} >= (x lambda/2pi)^{n/2} > 1.
- (9): checked each constant. Third-order Taylor: 100 local terms x 32000/6 < 5.4e5 < 4e6. Radial:
  -k (log h)'(k) in [0, 27] for k >= 1 (denominator >= e^{-1} 2/3 > 2/9, numerator <= 2 int e^{-w}(1+w^2) = 6),
  so h(x)/h(xr) >= r^27 and -log <= 54(1 - r) for r >= 1/2. Score difference: |Im M - QA| <= 50 |A|^2
  (global path second derivative), second-derivative pin response 1 - Re M <= 10u/sqrt x; Gaussian
  |w| = |8N/9 - N| <= N. sup (1+u)^5 e^{-cu^2/2} ~ 3e20 < 1e30; D (2pi/c)^{n/2} = sqrt(det H_0) c^{-n/2}
  <= (1000/c)^{n/2} < 10^{6n}; 45 + 6n <= 10n. |log J(0)| <= 1 and |t^2 x (log J)''(0)/2| <= K sqrt x/64.
  At x = 10^{40n}: x 1e-10 - K sqrt x > 10^{40n-11}, far above log(2 + 12Nx) < 12 + 120n. Correct.
- Change of reference L_t(Z): Z -> A(Z) is a measure-class bijection (ball to ball, identity outside),
  Jacobian j(Z)/j(A) from Haar, Gaussian ratio with H_0 = flat precision = stripe Hessian at t = 0. Correct.

## Step 3 (done 2026-11-24T18:41Z). Cold complement (5) at x = 100: HOLDS

- rho = lambda/(28 * 32000) = 1/(108900 * 896000) = 1/97,574,400,000. Correct.
- The direction-2 crossing link e with tail (1,1,1,1): its six plaquettes are based at the tail and at
  tail - e_nu (nu = 1, 3, 4), all in B; only the contours of the bond B -> B + e_2 read it (each contour
  has exactly one crossing, on its own face). At t = 0, l_B = 0 and N_1 = 0, so after cancellation the
  density is prod_{D != B} exp(-x H_D/2) times B's exact weights; no H_D with D != B, no other block's
  indicator, and no other R_D reads Z_e. Conditional law of Z_e: Haar times B's local weights. Correct.
- Lipschitz constants: six plaquettes, |e^z - 1| <= |z| each, 6x|z|; |Delta M_c| <= |z|; (log F)' = E q_0
  in [-1, 1], so the normalized pin log x Re(M V^-1) - log F(x|M|) moves by <= 2x|z|. Total 8x|z|. Correct.
- Cap ratio <= e^{8x(R+rho)} (int_0^rho sin^2)/(int_0^R sin^2) <= 4 e^{0.8} (rho/R)^3; with rho/R < 1.03e-8 this
  is below 1e-23, far inside 12e-21. On the R-cap every assigned plaquette is cold (chord <= R + 3 rho) and
  the chart holds, so the denominator restriction is a valid lower bound. Correct.
- The remark that the split (inside box)/(outside box) coefficients cannot both be priced absolutely, while
  the unsplit mark has expectation zero at t = 0: correct and correctly scoped (t = 0, x = 100).

## Step 4 (done 2026-11-24T18:41Z). Unsplit Taylor-remainder tests, (6)-(8), the residual, the joint denominator

Checked so far, all HOLD:
- Local linear term: a direction-2 crossing with first bit 0 is read by 2 of 16 offsets (1/8); B's own
  plaquettes on it are flat, so l_B there is the pin term eps sin(v - t)/8 = -eps sin v (8 sin v + sin(v-t) = 0).
- (7): on a block-constant Cartan gradient a marked bond contributes r[cos th (1 - cos s) + sin th (sin s - s)];
  (s - sin s)/(1 - cos s) increases to pi/2 on [0, pi] (numerator 2 sin(s/2)[2 sin(s/2) - s cos(s/2)] >= 0);
  1 - cos s >= 2s^2/pi^2; r > 1/2, cos th >= 15/16, |sin th| <= 8/35 give (15/16 - 16/35)/16 = 269/8960 > 1/40;
  unmarked 15/64 > 1/40. Wilson terms are constant on this family. Correct.
- (8) flat part: chord/log relations |Z| <= (pi/2)|1 - e^Z| on the closed ball; internal link = holonomy of
  at most three elementary squares (move the appended step past at most three ordered steps); crossing
  differences 13L, contour-to-crossing 93L, exact tail |M - r| <= sqrt(2 E_D), 1 - r <= |U - M|, so
  |1 - U| <= 187 L, log <= 294 L <= 400 L; quadratic tail |Z_U| <= 94 L. Sum 32*72 + 2*400^2*8*8 = 20,482,304
  < 21,000,000. Correct.
- (8) source part: mixed bounds 410 m = (3*100 + 100 + 10) m and 33,000 m^2 >= (31*1000 + 1000 + 100) m^2;
  marked m <= 1/40: 16,500 |t| m^2 by the integral Taylor remainder; m > 1/40: (42 + 410 m) <= 83,600 m^2;
  incidence 14 gives 1,400,000 |t| ||Z||^2; 1/(1.4e6 * 42e6) = 1/58,800,000,000,000. Correct.
- Residual: tan v = t/9 - t^3/81 + O(t^5), so v = t/9 - 28 t^3/2187; log A = -3v^2/16 - v^4/128 gives
  -t^2/432 + 1341/(128*3^9) t^4 = 447/(128*9^4) t^4. Combination (2t, t, 0) kills every even quadratic P_x and
  leaves 12 * 447/(128*9^4) t^4 > 0 at small t. Correct. (The text rightly notes this rules out only a vanishing
  unweighted budget, not the 1/e KP budget.)
- Joint denominator: Schur complement = min over exterior; K_t <= 6000 (400 m^2 per pin, 16 m^2 per plaquette,
  incidence 14 gives 5600); hot witness sum |Z_e| >= 1/2 - 1/35, ||z||^2 >= h_T (33/70)^2/24 > h_T/128;
  d <= 5 * 49 * 3 = 735 per block; box denominator 2^{-206N} e^{-n} (2 sqrt(lambda)/(100 sqrt(2 pi)))^n. Correct.
- Fixed-volume limits: h(x)/h(xr) -> r^{3/2} (h(k) ~ c k^{-3/2}); one mean of length cos(v/2) per marked block;
  x R_B(Y/sqrt x) -> 0 with the Gaussian majorant lambda/4 on the rho-box and (8) outside. The signed
  alternating-sum conclusion at t = 0 follows. Correct.

Step 4 verdict: HOLDS, with one scope repair (R1 below) to the statement of (8).

## Step 5 (done 2026-11-24T18:43Z). Adjacent-block test and the threshold 1/(81 e): HOLDS, scope note

- Pair coefficient: with phi_E = F_{E,C}/J - 1 and E phi_E = 0 at t = 0, the lambda_B lambda_D coefficient of
  log Z is E[phi_B phi_D] = J_{BD}/J^2 - 1. Correct.
- Counts, by hand from the contour definition (row 1480 line 23) and the plaquette assignment: a block reads
  its 49 free links; from each positive neighbour B + e_mu all 32 internal edges (every internal edge ends an
  ordered offset path), of which 17 are free, plus the 12 crossing nu-links with bit mu = 0, bit nu = 1
  (plaquettes based at bit-mu = 1, bit-nu = 1 corners). No diagonal block contributes a link origin.
  165 links per block; B and B + e_1 share exactly D's 29; union 2*165 - 29 = 301, real dimension 903. Correct.
  (A script enumeration was written to /tmp/opus1494/reads.py but not run: memory_pressure showed 41-42% free,
  below the 50% start rule. These counts are hand-checked only.)
- Cubic insertion U_B: Re(v_i v_j v_k) = -det(v_i, v_j, v_k), so x(1 - Re W_p) has cubic g D_p and the log-weight
  insertion is -D_p; Im M = g QY + g^2 avg sum_{i<j} v_i x v_j + O(g^3) and |M| - Re M = |Im M|^2/(|M| + Re M)
  give the pin cubic -(QY)_c . avg sum v_i x v_j. Then x(J_{BD}/J^2 - 1) -> E[U_B U_D] (the g^2 terms
  E V_B + E V_D cancel against J^2 by translation; odd moments vanish). Correct.
- Threshold: for the polymer-indexed KP form of row 1480 line 135 (sum over Y incompatible with X of
  |z_Y| e^{u_Y} <= u_X), take X the translate of the pair with least u (finite torus); the 81 translates
  {C, C + e_1} with C in the closed star of X's first site are incompatible with X, have the same |z| at t = 0
  (coarse translation invariance) and u_Y >= u_X, so 81 |z| e^{u_X} <= u_X and |z| <= 1/(81 e). Correct.

## Verdict

**HOLDS AFTER CORRECTION.** I found no wrong line. Every proved claim of row 1492 that I re-derived holds:
(1), (2), (3), (4), the finite witness x = 10^(40*37,632) with (9), (5), (6), (7), (8), the residual quartic
447/(128*9^4), the joint-denominator bound with d_0, the 301/903 count, the U_B limit and the 1/(81 e)
threshold. The repairs are to the scope of what is stated. None changes a proved inequality.

Repairs and notes, ranked by what they affect:

- **R1 (statement of (8)).** (8) is stated "on the closure of their full principal charts". The
  joint-denominator section uses it with the exterior (unmarked, unread) links ranging over all of R^3, through
  the Schur-complement minimum. The proof covers that domain: unmarked blocks are bounded by additive curl and
  pin estimates that never use the ball, and every link read by a marked block is in that block's chart D_B.
  Repair: state (8) on {links read by T in closed principal balls; all other links arbitrary}.
- **R2 (decisive outcome of row 1495).** J_{BD}/J^2 - 1 is the pair activity only for a polymer gas whose
  polymers are sets of marked blocks with star incompatibility. In any such gas the adjacent singletons
  are incompatible, so rho({B, D}) = E[phi_B phi_D]. A representation that first decouples the Gaussian
  covariance (a Balaban or Sussman-Alpoge style random-walk or interpolation expansion) has different activities
  and is not tested. So a value above 1/(81 e) at x = 100 refutes KP for that unsplit-mark star gas only, not
  the Q2 step in every representation. Row 1495's "refutes a common KP bound for this translated pair activity"
  is accurate. Any summary should keep that qualifier.
- **R3 (threshold, optional sharpening).** 81 is a valid lower count. Counting every translate {C, C + e_1}
  that meets the closed star of X (4 x 27 sites on the 4^4 torus) gives the stronger necessary bound
  |z| <= 1/(108 e) on that torus, under the reading "Y meets the closed star of X". This is unproved here
  beyond that count. Either threshold is a valid test, and 1/(108 e) is easier to violate.
- **N1.** (5) and the split-mark remark hold at t = 0 only, as written. The conditional-probability corollary
  also needs t = 0, because it uses l_B = 0.
- **N2.** (4) and the witness refute the fixed-angle extrapolation of row 1490 (7) only. They do not touch
  row 1490's fluctuation-scale limit. The file says this.

What stays open (unchanged from row 1492): a common rooted bound for the unsplit marks of the stripe-Hessian
Gaussian on |t| <= arcsin(1/4), x >= 100; extending (8) beyond |t| <= 1/58,800,000,000,000; the exact two-block
value at x = 100 (row 1495); and the volume cost d_0^{-N} in the hot bound.

Credit: Balaban (gauge-fixed variational RG, CMP 89-122), Kotecky and Preiss (polymer criterion),
Sussman and Alpoge with Claude and Codex (outline, complete account at 31a47c543775, the 384-contour kernel),
and Codex gpt-6.2-astra for rows 1480, 1490 and 1492. Hand check only. No Lean was run and no numeric job
was run.
