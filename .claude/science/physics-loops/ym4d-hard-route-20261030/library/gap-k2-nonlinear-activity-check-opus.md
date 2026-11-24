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

Status: plan written; steps appended below as done.

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

## Step 4 (in progress 2026-11-24T18:41Z). Unsplit Taylor-remainder tests, (6)-(8), the residual, the joint denominator

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
