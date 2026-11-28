# Check of library/gap-wmix-solve-neon.md (row 1602) -- FINISH.md row 1605

Checker: Claude Opus 5.5 (subagent). Status: complete.

Inputs read: `library/gap-wmix-solve-neon.md` (481 lines, read in full); FINISH.md row 1602
(brief and RESULT); row 1526 `gap-agy-seed-approaches-neon.md` Theorems 1-2 (lines 189-258);
check 1527 `gap-agy-seed-approaches-neon-check-astra62.md` parts (i)-(ii) and Handoff
(lines 32-60); check 1120 `gap-resp-in-law-sheet-check-opus.md` Steps 1, 3.15, 5.2-5.3;
row 1584 `gap-band-direction5-fable.md` (13.4); row 1597 `gap-direction6-fable.md` (PZ-why),
(WB1)-(WB3). Further sources are listed at each step. Not read (per brief):
`gap-wmix-solve-astra62.md`, `gap-wmix-obstruct-astra62.md`, `prior/gap-wmix-lit-luna.md`;
I also did not read `gap-wmix-solve-fable.md` (row 1600), to keep this check independent.

## Step 0. What the on-file (W-mix) forms are (needed to judge "equivalent")

- (H-two) on file (row 1115 3.4, quoted in check 1120 Step 1): "Draw two pins independently
  from the ring law. Ask that the interior laws of one cell under the two pins are close, in
  mean." The core is ONE CELL of side l, the ring its collar, in a large-volume state. Check 1120
  5.2-5.3 (Lemma TS3) shows the two-sample mean is within factor 2 of the one-scale beta-mixing
  coefficient of core vs outside. This is a LOCAL, one-cell statement.
- Row 1584 (13.4): the "two ends, mean at typical ends" kind is bound (2) and E_mu J of row 1573,
  ending at "Lemma JI of check 1121 and Lemma TS3 of check 1120: one-scale in-law mixing".
- Row 1597 (WB2): an admissible object's open estimate must not be "the seed as an identity, ...
  not two-sample mixing across a cylinder at the same or a shorter period". So the lane already
  treats full-slice two-sample mixing across the period as the wall.
- Row 1526 Theorem 1 (2.1)-(2.2), checked HOLDS in check 1527 (i): P_K = E[Aff(p_A1,p_A2)^2] for
  the midpoint law p_A of the period-u neutral torus given slice 0 = A, and
  P_K >= (1 - E d_TV(p_A1,p_A2))^2. Check 1527 (i) adds: "A threshold on the left of (2.1)
  restated on its right has precisely the force of the seed." Row 1526 line 260 already states
  that a two-sample Hellinger bound at the long aspect K(delta) proves the gap.

Consequence for the check: the neon "(H-two)" of its 2.1 item 2 is NOT the on-file (H-two). It is
the full-slice, period-u, midpoint-given-opposite-slice two-sample law of row 1526 Theorem 1. Its
core is the whole spatial slice (3n^3 links), not one cell. Calling it "the cylinder form of
(H-two) of rows 1118-1120" is a relabelling; Theorems 1A/1B say nothing about the local one-cell
(H-two) of rows 1115-1123 or about Lemma TS3's class.

## Step 1. Theorem 1A (single-box bounds on F_+): HOLDS

Checked line by line.
- (1) Aff(p_x,p_x') = k_2(x,x')/sqrt(k_2(x,x)k_2(x',x')); the null set {rho = 0} is handled by
  Cauchy-Schwarz (k_2(x,x)=0 forces k_2(x,.)=0). Integration gives Tr(A^4)/Z^2. Correct. This is
  row 1526 Theorem 1 (2.1), checked HOLDS in check 1527 (i); the extension to kernels that are
  not strictly positive is new but trivial.
- (T1.1): R in [0,1], E R^2 = P, so P <= E R <= sqrt P. Correct.
- (T1.2): H^2 <= d_TV (standard); d_TV^2 <= 1 - Aff^2 by Cauchy-Schwarz with
  int(sqrt f + sqrt g)^2 = 2 + 2 Aff (Le Cam's inequality); Jensen for sqrt(1 - t). Correct.
- (T1.3): Aff(p,m) = int sqrt(rho(y)) [int rho(x) sqrt(p_x(y)) dx] dy; Cauchy-Schwarz in y gives
  Aff(p,m)^2 <= E R <= sqrt P; concavity of sqrt gives Aff(p,m) >= E R. Both directions checked.
- (T1.4): H^2(p,m) <= d_TV(p,m) = beta_mix; convexity of q -> d_TV(p_x,q) gives
  beta_mix <= d_TV^two. Correct. (1-x)^4 > (1-2x)_+^2 on (0,1): correct.
- Witness A (k_N = alpha sqrt N I + 1 1^T): recomputed Z_N = N^2(1+alpha^2) + 2 alpha N^{3/2},
  Tr k^4 = N^4 + O(N^{7/2}), p_x(x) -> t, Aff(p_x,p_x') -> 1-t for x != x' (probability
  1 - 1/N), d_TV -> t, Aff(p,m) -> sqrt(1-t). All limits correct; P -> (1-t)^2.
- Witness B: as delta -> 0, p_x -> point masses, rho -> (q,1-q), E R -> q^2+(1-q)^2 = P, so
  H_two^2 -> 1-P. Correct, for P in [1/2,1).
- Witness C: eigenvalues 2-eps, eps; d_TV^two = beta_mix = eps/2 + O(eps^2);
  1 - P = 2a^2eps^2/(a^2+eps^2)^2 = eps^2/2 + O(eps^3) (a = 2 - eps). Ratio -> 1/sqrt 2.
  So the exponent 1/2 cannot be raised (the constant 1 is not shown sharp; the file does not
  claim it is). Correct.

Verdict: HOLDS. No counterexample exists (all steps are proved inequalities).
Novelty: the lower bounds (direction mixing => P) are ON FILE (row 1526 Theorem 1 (2.2), check
1527 (i)). New: the upper bounds H_two^2 <= 1-P, d_TV^two <= sqrt(1-P) (Le Cam), the
joint-to-product pair (T1.3)-(T1.4), and the sharpness witnesses. All are standard
information-theory facts applied to the on-file identity (2.1).

## Step 2. Theorem 1B (equivalence to (PUR-io) on beta_K): HOLDS given the checked inputs

Checked the five implications and every cited input in its file.
- (2)=>(1): Theorem 1A gives P >= (1 - d_TV^two)^2 >= 457/625, resp. (1-beta_mix)^4. Correct.
- (4)=>(1): Theorem 1A gives P(n/A) >= 1/2 + eps. Check 1527 Theorem 2(2) ("For a general
  margin, one explicit even aspect is A = 2 ceil(log 10^6 / log(1 + sqrt(2 eps)))", lines
  49-51) gives S_kappa(n/2;(2n)^3) < 1/25. The file uses any even A >= that value; I checked row
  1368 Theorem 4 (line 211): its hypotheses are 4 | n, u >= 3, real K >= 4 with n >= K u, and
  t := d^{n/(2u)} <= d^{K/2}. So a larger aspect only lowers t; the extension is valid.
  4 | n holds since l in 4A N.
- Step 3 (Theorem SH at r = 4, row 705 table line 123: step (2,2,3), threshold 1/25,
  K = 22.2; statement (i) "K s_k <= (K s)^(j^k)", line 97): gives
  s_j <= (22.2/25)^{2^j}/22.2 at side 2^{j+1} n, time 2^{j-1} n. Matches check 1527 Handoff.
- Step 4 (B3-q, row 705 line 76, with p = q = 1, a = B/4 < B): beta_i = 4/3, multiplier
  128^3 (4/3)^3 = (512/3)^3 on log(1+s_j). Matches check 1527 Handoff "(128.4/3)^3".
  Arithmetic: (512/3)^3 = 4,971,026.96 < 22.2 * 2^18 = 5,819,596.8; (9/10)^7 < 1/2;
  floor(2^j/7) >= (2^j - 6)/7. So X_j <= 2^{(132 - 2^j)/7}. Correct.
- Step 5: 2^{j(eta)} >= 146 + 14 L with L = ceil(log2(1/eta)) gives (132 - 2^j)/7 <= -2 - 2L
  <= log2(eta^2/4). e^x - 1 <= 2x on [0,1/4]. Neutral excess <= Pfaffian excess: check 1370
  line 102 ("the even sector, since it is contained in the Pfaffian transfer") and check 1527
  Handoff. P >= (1+s)^{-2} >= 1 - 2s. V_K = N_K/1024 = 2^{j-2} n. All correct.
- (1)=>(4): eps = 289/1250, sqrt(2 eps) = 17/25, 2 ceil(26.63) = 54 <= 512. Correct.
- beta_K does not move when l is enlarged: check 1453 line 26 ("Choose ... the reference torus
  index M ... g_K > 0 is the least root") and check 1527 Handoff ("The calibrated coupling is
  still the least root on the original reference torus"). Correct.

Verdict: HOLDS (conditional exactly on the checked rows 705/707, 1368/1370, 1453, 1527, which
the file names). Counterexample: none; it is a chain of proved implications.

Two scope corrections (wording, not logic):
(a) The thresholds covered are those that force P >= 1/2 + eps at an aspect A >= A_0(eps), or
    the "every eta" form. A bounded criterion with a threshold above 1 - 1/sqrt 2 (for d_TV^two),
    or at a short aspect A < A_0(eps), is implied by (PUR-io) but is not shown sufficient; the
    file's "at any admissible aspect and threshold" means exactly these admissible ones.
(b) The object is the FULL-SLICE law of the midpoint slice given the opposite slice on the
    period-u neutral torus (row 1526's p_A). It is not the one-cell (H-two) of rows 1115-1123
    (Step 0). The sentence "the cylinder form of (H-two) of rows 1118-1120" should read "the
    full-slice half-period two-sample law of row 1526 Theorem 1".

Novelty: the direction criterion => (PUR-io) is ON FILE (row 1526 Theorem 1 (2.2) and Theorem
2(2), line 260; check 1527 (i) "has precisely the force of the seed" and the Handoff). The
lane's withdrawal bar (WB2) of row 1597 already excludes "two-sample mixing across a cylinder at
the same or a shorter period". The converse (PUR-io) => every such quantity below any eta at a
fixed enlarged side is new as a written statement; it is Le Cam's bound plus the on-file
enlargement chain of check 1527 Handoff / check 1370 line 106 ("recover the original shorter
time caps on a sufficiently large fixed dyadic enlargement"). Under the lane rule this is a
valid but small obstruction result: it makes formal an equivalence the lane already used.

## Step 3. Theorem 2 (f-divergence trichotomy and -log P <= 2 min(I,L)): HOLDS

- (1) phi_f convex, phi_f(0)=0, phi_f > 0 on (0,1] by non-degeneracy (a convex nonnegative
  function vanishing at 1-delta, 1, 1+delta vanishes on the interval, so f is affine there).
  D_f(P||Q) >= phi_f(d_TV): data processing to the two cells {p>q}, {p<=q}, then
  f~(1+delta) <= b f~(1+delta/b) and f~(1-delta) <= (1-b) f~(1-delta/(1-b)) by convexity with
  f~(1)=0; the edge cases b = 0 and 1-b = delta are handled with M_inf and f~(0). Checked.
- (2) f~(t) <= M_0 (1-t) on [0,1] and f~(t) <= M_inf (t-1) on [1,inf) (slope monotone), so
  D_f <= M(f) d_TV. Checked. The equivalence on beta_K then follows from Theorem 1B with the
  threshold transformed by phi_f^{-1}; same scope as Step 2 (a)-(b).
- (3) Case A (M_0 = inf), kernel [[1,delta],[delta,c]]: I recomputed Z = 1+2 delta^2+c^2,
  rho_1 >= 1/2, rho_2 >= c^2/2, Tr k^4 >= k_2(1,1)^2, P >= (1+3c^2)^{-2} (needs
  2c^2 + 3c^2 delta^2 >= delta^2, true), p_12/m_12 <= 2 delta^2/c^2, p_1(2)/p_2(2) <= 2 delta^2,
  weights c^2/4 and c^2/8. Case B (M_inf = inf), kernel diag(sqrt(1-delta), sqrt(delta/M),...)
  + eps 1 1^T: Z <= 1 + delta/(2M), p_ii >= 8 delta/(9M), rho_i <= 3 delta/(2M),
  p_ii/m_ii >= 32M/(81 delta) >= M/(3 delta), p_i(i) >= 16/27, p_0(i) <= 1.5 eps^2, and the
  monotonicity of f~(t)/t on [1,inf). All bounds checked; D_f -> inf while P -> 1.
- (4) Aff(p,m) = E_p exp(-(1/2) log(p/m)) >= e^{-I/2} (Jensen), likewise >= e^{-L/2}; with
  (T1.3) P >= Aff(p,m)^4 this gives -log P <= 2 min(I,L). Separation example
  delta = c e^{-1/c^3}: I <= c^2(1 + log(2/c^2)) -> 0 and L >= 1/c - (c^2/2)(1 + log 2) -> inf.
  Recomputed; correct.

Verdict: HOLDS. Counterexample: none.
Novelty: -log P <= I + L, and "strictly stronger than the seed on abstract positive kernels"
for I + L, are ON FILE (row 1573 line 105 "Jensen gives -log P_K <= E_mu J <= B_K"; check 1579
item 7, which cites Lemma JI of check 1121 and the same two-eigenvalue pattern as check 1527
(vi)). New: the dichotomy by M(f) for every non-degenerate f, and the factor-2 sharpening
-log P <= 2 min(I,L). The latter is true and small; it does not move a lane input, since I is
still strictly stronger than the seed (Case B).
The "Contrast with row 839" paragraph after the proof is a reading (unlabelled ARGUED), not
part of the theorem; I did not check it against row 839.

## Step 4. Theorem 3 ((H-two-N1) and rho_max): HOLDS; its bearing is narrower than stated

- (1) alpha_N1 <= alpha^two <= 2 alpha_N1 (Jensen, triangle); alpha^two <= 2 d_TV^two;
  alpha_N1 <= ||Q f~||_{L1} <= ||Q f~||_{L2} <= rho_max (Q self-adjoint on L^2(rho) because p is
  symmetric). Checked.
- (2) k_1 = (1/2)[[1+r,1-r],[1-r,1+r]]: P(k_1) = (1+r^4)/(1+r^2)^2 <= e^{-r^2/2} for r <= 1;
  Q_1 eigenvalue 2r/(1+r^2); tensor power: rho_max = 2r/(1+r^2) <= delta/2 and
  P = P(k_1)^M <= e^{-c^2/2} = eps. Checked.
- (3) Massive free scalar: mode purity (1-q)/(1+q) (ON FILE, check 1527 (i) Prop 1.2(1));
  Mehler/Hermite diagonalization; rho_max = rho_0 <= 2 e^{-uE_0/2}; mode count: for A >= 66,
  2R+1 >= A/6, R <= A/10 < n/2, u E_k <= u E_0 + 1 on the cube. P <= exp(-C/(108 e)) = eps.
  All steps and constants checked (2 sqrt3 pi = 10.88 < 11; 2A/11 - 1 >= A/6 iff A >= 66).
- (4) k_c = [[1,c^2],[c^2,c]]: Case A gives P -> 1; Q's nontrivial eigenvalue
  1/(1+c^2) + 1/(1+c^4) - 1 -> 1. Checked.

Verdict: HOLDS. Counterexample: none.
Correction of reading (not of mathematics): on file, (H-two-N1) of check 1120 5.3 is a
hypothesis for (CONV) (exponential clustering of a local cell in a DLR state), with a LOCAL core
of one cell. It was never proposed as a supplier of a lower bound on P_K. Theorem 3 shows that
the full-slice analogue alpha^two gives no lower bound on P; it does not refute (H-two-N1) in
its on-file role, and the file's "a natural escape attempt ... recorded on file as (H-two-N1)"
overstates what is on file. The phenomenon (one observable or one mode cannot see an extensive
product of mode purities) is standard; the explicit theorem is new in the lane as far as I
found (I grepped for "maximal correlation" and "rho_max": see Step 7).

Guide run (not a proof step): a pure numpy script in the scratchpad (outside the repo) drew 3000
random nonnegative PSD kernels of size 2-6 and confirmed (2.1), (T1.1)-(T1.4) and (T2.4) up to
roundoff (one P = 1 rank-one case needed a 1e-7 tolerance on sqrt(1-P)); it also reproduced the
Theorem 3(4) numbers (c = 0.1: P = 0.980, rho_max = 0.990).

## Step 5. Theorem 4 (Propositions 4.1-4.3): HOLDS AFTER CORRECTION

Sources opened: row 1574 `gap-band-neutral-fable.md` Steps 3-4 (lines 118-245, Proposition ROT,
Lemma CO, the pair rotation formulas, Theorem SW, Lemma CORNER, Attack 2 at 345-372); check 1580
`gap-band-neutral-fable-check-astra62.md` (lines 20-66, 94-140); row 1573 line 105; check 1121
section 8 (Proposition J); row 1118 4.2 ((4.4), eps_0(d) = 1/(2 5^d)); row 1072 CA-FAIL (337-368)
and its check `gap-bridge-exercise-check-astra.md` section 2; row 1468 4.1 (C4).

### 4.1 (P_{GxG} D_p P_{GxG} = 0; Lemma CORNER vanishes): HOLDS. New.
I rederived it. For GxG-invariant F, average over (g_A, g_B), pull out the diagonal part
(Proposition ROT (iv)), and write u = g_A^{-1} g_B. Then (P D_p F)(A,B) = <grad F(A,B), int V(u) du>,
where V(u) is the velocity of the pulled-back orbit at the FIXED point (A,B). With
c~_1 = a_1^{-1} u_x b_1 u_y^{-1} and c~_2 = u_y b_2 u_z^{-1} a_2^{-1} (matches row 1574's head- and
tail-based coordinates), the e_1 velocities are linear in k~ and otherwise depend on (u_x,u_y) only;
the Haar-preserving map u_z -> a_2^{-1} u_y b_2 u_z^{-1} a_2^{-1} u_y b_2 inverts c~_2, negates n~_2
and k~. So the u_z-average of the e_1 velocities is 0; symmetrically the u_x-average of the e_2
velocities. x, y, z are distinct because n >= 4 is even. I also redid the U(1) square-contour
case: on an open side phi_1-dot = -sgn(phi_2) 4 rho/pi, odd under phi_2 -> -phi_2 via u_z.
The kernels of T^v and P_0 T^v are GxG-invariant at each end (row 1574 lines 281-282), so
MM = P MM P, every eigenvector of MM with nonzero eigenvalue is invariant, <a,Gb> = 0, and
Tr(G MM G MM) = 0. Part (3): the s = 0 case works for any second argument; (sigma,sigma)-
invariance of mu moves s = pi to s = 0 with t -> t + pi; t in {0,pi} by the same argument in the
second argument. Checked. E_mu J = I + L also rechecked (it is row 1573's identity).
Corrections: (i) check 1580 line 60 says the eigenfunctions are smooth; their GxG invariance
comes from row 1574 lines 281-282, not from check 1580. (ii) Attack 2 (a) of row 1574 becomes
"0 <= right side", not "0 = 0".
Bearing: row 1574's Lemma CORNER (and check 1580's HOLDS of it) stand as identities, but their
value is identically 0, so the "necessary test E[jk] <= N_p L_sigma/2" and Attack 2 (a) control
nothing. This is a genuine correction to an on-file reading (neither row 1574 nor check 1580
noticed it). It refutes no estimate: (SW) takes a supremum over interior angles.

### 4.2 ((SW) inner-absolute-value form diverges as n^2 on massive free scalar trajectories):
HOLDS for (1), (2) and the literal (3); the summary sentence needs a correction. New.
- (1): E Q^4 = s1^4 + 12 s1^2 s2 + 12 s2^2 + 32 s1 s3 + 48 s4 agrees with the cumulant formula
  (kappa_r = 2^{r-1}(r-1)! s_r). AM-GM step and Hoelder step checked; constant 17 valid.
- (2): cross-end term <phi', M_v phi> with M_v(x,y) = G_int((x,1),(y,v-1)) > 0;
  M^_v(k) = sinh E_k / sinh(v E_k) (Dirichlet chain, cosh E = 1 + mu^2/2); replica split
  2<phibar',M phibar> + 2<dphi',M dphi>; generator at s = pi/2 gives -dphi; Wick formula with
  covariances C_0/2, C_v/2; C_t > 0; diagonal-term and 4-term Cauchy-Schwarz; sum over the
  partition of dimers gives 2 M^_v(0); C_0(0) >= 1/(16 + m0^2); sinh E_0 >= m0; v E_0 <= ml/(2K).
  All checked. So (pi^2/2) N_p L_sigma >= c(ml, K) n^2 with N_p = n^3/2.
- (3): E H^2 formula, C^_0 = cosh(vE)/(2 sinh E sinh vE), C^_v = 1/(2 sinh E sinh vE),
  M^C^_v = 2q/(1-q)^2, M^C^_0 = sqrt q (1+q)/(1-q)^2, Gaussian I and L, I + L = sum 4q/(1-q)^2:
  all checked.
Correction: (3) bounds the outer-absolute-value integrand at ONE point s = t = pi/2. It does not
bound B_K, which integrates E|sum h(s,t)| over the whole square, where R_s does not commute with
the translation-invariant M_v and C_t. The phrases "outer-absolute-value B_K -> 0" (6.1 table)
and "even when P_cont -> 1 and B_K -> 0" (RESULT (4)) are therefore not proved. Replace by "the
outer-absolute-value integrand at s = t = pi/2 is O(1)". (A Hilbert-Schmidt bound suggests the
other angles are also O(1); I did not prove it: ARGUED at most.)
Bearing: the object is the free-scalar analogue of (SW), not the Wilson (SW). It shows the
trajectory form of (SW) fails in a gapped continuum theory where P_cont can be made > 457/625; so
(SW)'s trajectory form is not a selective weakening of the seed. The Wilson (SW) on beta_K stays
open, as the file says. Not found on file (grep of rows 1573, 1574 and check 1580 for free or
massive tests: only the free-field GUIDE at row 1574 line 324 and check 1580 line 136).

### 4.3 ((H-swap) and uniform mixing fail on the tail of beta_K): HOLDS. Mostly ON FILE.
- (T4.6): convexity of log Z with log Z(0) = 0; geodesic balls B_delta, plaquette distance
  <= 4 delta, cos(4 delta) >= 1 - 8 delta^2, Haar(B_delta) >= 8 delta^3/(3 pi^3) >= delta^3/12
  (3 pi^3 = 93.0 < 96), delta = (8 beta)^{-1/2} < pi/8, (2/3) log 12 < 2. Checked.
- (T4.7): check 1121 Proposition J(a) gives E p_c >= (1 - e^{-3 beta l}) Pbar / 2; (c) gives 0.010
  at beta >= 2.3, L >= 20 (its bounds increase with beta, check 1121 line 158, so the window
  value holds for all beta >= 2.3). With (T4.6), liminf >= 1/2. Checked. Since check 1121 already
  refutes (H-swap) at beta >= 2.3 for every l by the monotone bound, part (2) is ON FILE in
  substance; only the constant 1/2 is new.
- (3): CA-FAIL (row 1072) plus beta_K -> infinity (check 1453 BND-1/BND-2). Correction: the
  threshold "approx 1.0109" is a recalled value; check 1072-astra section 2 corrects CA-FAIL to
  "for every beta > 2 I3" (I3 < 1) and to uniform STRONG mixing over all finite link sets and
  exterior configurations. The consequence for (CM_k) is ON FILE as row 1468 4.1 (C4).

Verdict for Theorem 4: HOLDS AFTER CORRECTION (the B_K sentence of 4.2; the CA-FAIL threshold and
scope; two citation details of 4.1). No counterexample to any stated part.

## Step 6. Does "every bounded half-cylinder criterion ((H-two), beta_mix, Hellinger, affinity)
## is equivalent to (PUR-io) on beta_K" hold as stated? Over what class?

HOLDS AFTER CORRECTION, over this exact class. Let p be the two-slice law of A = P_0 T^v, v = u/2,
at beta_K on (Z/n)^3, n = l b^K: the law of the WHOLE midpoint slice given the WHOLE opposite slice
on the period-u neutral torus, with the thermal marginal rho (row 1526's p_A, pi_u). A criterion is
"Phi(p) <= tau at infinitely many K, for one l", with
- Phi one of d_TV^two, H_two^2, beta_mix, H^2(p,m), or D_f^two, D_f(p||m) for a convex f that is
  non-degenerate at 1 with M(f) < inf (Theorem 2(2));
- an even aspect A = n/u >= A_0(eps) = 2 ceil(log 10^6 / log(1 + sqrt(2 eps))) and l in 4A N;
- a threshold tau that forces P >= 1/2 + eps through Theorem 1A or (T2.1)
  (for d_TV^two: tau <= 1 - sqrt(1/2 + eps)); or the "every eta, enlarged side" form.
Then the criterion holds iff (PUR-io) holds, with l replaced by a K-independent dyadic multiple and
the same infinite set E. Outside this class nothing is proved:
- the one-cell (H-two), (CONV-two), (H-two-N1), (H-two-col) of rows 1115-1123 / check 1120
  (local core in a DLR state; no implication to or from P_K is proved);
- thresholds that do not force P > 1/2, and aspects below A_0(eps) (implied by (PUR-io), not
  shown sufficient);
- the unprojected T^v (reads Pi; Pi-criteria are sufficient since P_K >= Pi on the passing range,
  check 1580 line 55, but equivalence is not shown);
- other time separations, open cylinders, or ground-state (Doob) marginals;
- supremum-over-boundary and unbounded (I, L, I+L, chi^2) forms, which are strictly stronger on
  F_+ (Theorem 2(3); ON FILE for I + L, check 1579 item 7).
Under the lane rule this is a valid obstruction result, but small: the sufficiency direction and
the "force of the seed" reading were on file (row 1526, check 1527, row 1597 (WB2)); the file adds
the converse direction (Le Cam plus the on-file enlargement chain), the sharp exponents, and the
extension to all bounded f-divergences.

## Step 7. What row 1602 leaves open, and whether its list is right

Its list (RESULT): pure-Wilson strictness on beta_K of I, B_K, N_p L_sigma, TC/TS; single-step RG
mixing (FL), regular-set (CM_k); the carries R11/R12; (PUR-io).
Corrections:
1. Add: the local one-cell (H-two)/(CONV-two) and (H-two-N1)/(H-two-col) of rows 1115-1123 and
   check 1120 are untouched (the file's "(H-two)" is a different, full-slice object, and Theorem 3
   addresses only the full-slice analogue of (H-two-N1)). Proposition 4.3 covers (H-swap) only.
2. Reword "strictness of I, B_K, N_p L_sigma, TC/TS": what is open is whether these sufficient
   estimates HOLD on beta_K (they are already known to be stronger than the seed: I, I + L and B_K
   on F_+ by Theorem 2(3) and check 1579; (SW) and TC/TS by checks 1580 and 1582). For the free
   scalar, the boundedness of B_K itself is also open (Step 5, 4.2).
3. The (SW) BAND form (beta in [2,3], fixed lattice mass, v -> infinity) is not touched by
   Proposition 4.2, which works along a continuum trajectory; it stays open as in row 1574.
4. The non-(W-mix) inputs of row 1386 ((K-I), (K-II)) are listed in the body (6.2 item 3) but
   dropped from RESULT; they remain open.
5. (T-mix) of row 1553 3.3: its "two-sample mixing at typical ends across a half-cylinder"
   branch is now formally equivalent to the seed (Theorem 1B, scope of Step 6); its (FL) and
   defect-measure branches stay open. The list is right to keep (FL) and (CM_k).
Not checked here: the selectivity paragraph 6.3 (U(1) P_even bound, 5D belief, gapped twin), which
is not one of the five theorems; the "Contrast with row 839" paragraph of section 3.

## Step 8. Novelty summary
- ON FILE in substance: Theorem 1A lower bounds and identity (row 1526 Thm 1, check 1527 (i));
  sufficiency direction of 1B (row 1526 Thm 2(2), check 1527 Handoff); -log P <= I + L and its
  strictness on F_+ (row 1573, check 1579); Proposition 4.3 (2)-(3) (check 1121 Prop J; row 1072
  CA-FAIL with check 1072-astra; row 1468 (C4)).
- New: upper bounds and sharpness in 1A; the converse direction of 1B; the M(f) dichotomy of
  Theorem 2 and -log P <= 2 min(I,L); Theorem 3; Proposition 4.1 (corrects the reading of row 1574
  Lemma CORNER / Attack 2 (a)); Proposition 4.2; (T4.6) (standard).
- None moves a lane input: no estimate on beta_K is proved, and every new statement is an
  equivalence, a strict-strength statement, or a vanishing.

Who checked what: every step of the five theorems above was checked line by line by Claude Opus 5.5
(this file), against the cited files opened at the stated lines. The author is gemini-4-neon-xhigh,
so this is a cross-provider check; no second reader. Nothing formalized; one numpy
guide run outside the repo; no other file written; nothing committed.

## RESULT
Theorem 1A HOLDS (lower bounds ON FILE, row 1526/check 1527; upper bounds, joint forms, sharpness new).
Theorem 1B HOLDS given checked rows 705/707, 1368/1370, 1453, 1527; corrections: its object is the
full-slice half-period law of row 1526, not the one-cell (H-two) of rows 1115-1123, and it covers only
thresholds forcing P >= 1/2 + eps at aspect A >= A_0(eps); sufficiency ON FILE, converse new.
Theorem 2 HOLDS (I + L case ON FILE, row 1573/check 1579; M(f) dichotomy and 2 min(I,L) new).
Theorem 3 HOLDS, new; it bears on the full-slice analogue only, not on (H-two-N1)'s on-file role for (CONV).
Theorem 4 HOLDS AFTER CORRECTION: 4.1 holds and is new (row 1574's Lemma CORNER corner is identically
0, so Attack 2 (a) controls nothing); 4.2 holds, but "B_K -> 0" is not proved (only the integrand at
s = t = pi/2 is O(1)); 4.3 holds, ON FILE in substance (check 1121 Prop J; CA-FAIL is for beta > 2 I3).
No theorem FAILS; no counterexample to any stated part.
Overall: outcome (c) HOLDS AFTER CORRECTION as an equivalence-type obstruction over the class of Step 6.
It is small, largely a two-sided restatement of on-file facts, and moves no lane input.
