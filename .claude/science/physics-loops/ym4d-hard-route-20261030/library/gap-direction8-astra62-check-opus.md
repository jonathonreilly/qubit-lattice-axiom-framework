# Check of row 1642 (library/gap-direction8-astra62.md), FINISH.md row 1644

Checker: Claude Opus 5.5 (laptop subagent). Status: done 2026-11-27.

## 0. Reading log

Read in full: `library/gap-direction8-astra62.md` (row 1642, 542 lines); FINISH.md rows 1613, 1630, 1641, 1642, 1644 (brief and RESULT texts).
Read in the parts used: row 1610 (`gap-direction7-fable.md`) sections 2.2-4; check 1613 (`gap-direction7-fable-check-astra62.md`) selectivity table and last-crossing paragraph; check 1630 (`gap-vir-down-twoside-check-opus.md`) section 1; row 1227 (`gap-solve25-astra62.md`) lines 9-110, equations (1)-(8) and the homogeneous restriction; check 1230 (`gap-solve25-check-opus.md`) step 6; row 1145 (`gap-solve2-astra62.md`) section 1, equations (1)-(4); row 1565 (`gap-band-cut-covariance-astra62.md`) the Villain flux bound and its Wilson transfer; row 1573 (`gap-band-neutral-astra62.md`) lines 125-150; row 1553 (`gap-mech-direction4-fable.md`) sections 1.3-1.5 (Lemma ALG, tests g1-g6); row 1386 (`gap-mech-direction2-fable.md`) section 2.1 (SV-Z); registry rows VIR-DOWN, LEV-FAIL, WMIX-SLICE.
Not read: `library/gap-direction8-fable.md` (rule); rows 1618/1622, 1638/1640 beyond the formulas quoted in row 1642 (I re-derived those formulas); the PV note on main (the Villain current expansion stays a cited input, as in checks 1571, 1579, 1613).
Search: "flowed holonom", "flowed winding" in library/ and FINISH.md hit only row 1642. No numerics, no Lean. Every verdict below is by hand.

## 1. The PROVED items, line by line

### 1.1 Consumer: (2) gives (HOT) (section 3, lines 157-174). HOLDS.

- J_n is an isometry: the integral of h(Y)^2 |f(Y)|^2 under pi equals the integral of |f|^2 under pi_B, with h^2 = d pi_B / d nu_n. Mutual equivalence (lines 141-146): the flow is a diffeomorphism, so the flowed slice law has a smooth density bounded below; the unflowed winding map pushes a density bounded below to one bounded below (one link per line moves the three products freely). Correct. Centre flips and gauge act on Y as in section 2: the spatial Wilson action is seam-flip invariant (a plaquette contains 0 or 2 seam links), so the flow commutes with the flips. Correct.
- S = J_n D_B^q J_n^* has the spectrum of D_B^q plus zeros: top 1 (vector J_n 1), second p in [2/5, 3/5] by (1) with q = ceil(tau_0 / eps). Weyl's inequality for the ordered eigenvalues and ||.||_op <= ||.||_HS give 3/10 <= p_1 <= 7/10. Correct.
- (3): G(2jqn) is the sum of p_i^(2j) over the excited eigenvalues p_i of D_n^(qn); p_i^(2j) <= (7/10)^(2j-2) p_i^2 and the sum of p_i^2 is at most ||D_n^(qn)||_HS^2 - 1 <= M^2. The printed bound with M^2 is correct (M^2 - 1 is slightly sharper).
- Budget: with W(r) from check 1630 section 1.2 (uniform in K), kappa_0 (s r - W(r)) >= log(512 alpha_h) gives t_h >= alpha_h n. Correct. Since b is odd, l = L_h b^r is in 1024 N exactly when L_h is; the text's "choose L_h in the allowed side class" covers this.
- The chain to the seed (lines 176-189) is ON FILE (rows 1610, 1613, 1630): last crossing with c_col = 4/21 > s_0 = 1/10, time monotonicity of G, and P_K >= (1 + G(u))^(-2) >= 100/121. Integer check: 100 * 625 = 62500 > 457 * 121 = 55297. Correct.
Verdict: HOLDS. (HOT) is supplied at the fixed aspect alpha_h = 2jq with s_0 = 1/10, uniform in K on the passing subsequence. Scope: the consumer uses only the UPPER bound p_1 <= 7/10 and the HS bound M. The lower bound p_1 >= 3/10, which (2) also forces, plays no part in (HOT).

### 1.2 Necessary affinity test (5) and the 11/16 annulus (sections 3.1, 5). HOLDS.

- (5): write 1 = A_n v + w with v = J_n 1, w orthogonal to v. Then (D_n^(qn) - S) 1 = (I - S) w, and on the orthogonal complement of v, I - S >= (1 - p) I. So the error is at least (1 - p) sqrt(1 - A_n^2), in operator norm. Correct. With p <= 3/5, (2) needs A_n^2 >= 15/16. Correct.
- Annulus: total variation <= sqrt(1 - A_n^2) <= 1/4 (Cauchy-Schwarz on (sqrt p - sqrt r)(sqrt p + sqrt r)); the reference mass of the annulus is > 15/16 for large B by the strong vacuum limit of row 1227 and |Im exp(eps x)| = sin(eps |x|); the boundary spheres are null. So nu_n(annulus) > 15/16 - 1/4 = 11/16. Correct.
- Decomposition (4): the kernel of J D_B^q J^* relative to pi x pi is h(Y) k_B(Y, Y') h(Y'), which is (Y, Y')-measurable; conditional expectation is an orthogonal projection. Correct.
- Separations (lines 206-221): beta = 0 is rank one, Weyl gives distance >= 2/5; the two-state cold spectator has purity limit (1 + 1)/4 = 1/2 while the hot norm is unchanged. Correct, on abstract positive families only, as the text says.
- Scale-sensitive reference observable (lines 255-263): correct; it is a statement about the one-vertex model, not about the Wilson law.

### 1.3 Unflowed readout fails (section 3.1, lines 239-252). HOLDS.

Row 1145 (3): the based straight windings with end links dropped are conditionally independent, joint density within (1 +- eta)^3 of Haar, eta = eta((n-2)/b_beta) -> 0 since b_beta = 1 + 6 beta_(K+r) = O(K) and n grows like b^K; uniform in the other links, so it passes to the vacuum slice law. Then nu_n(S_z) <= (1 + eta)^3 / 32 < 1/16, pi_B(S_z) > 15/16, A_n <= 1/4 + 1/4 = 1/2, and (5) >= (2/5)(sqrt 3 / 2) = sqrt 3 / 5 > 1/10. Correct. This is a consequence of row 1145, as stated.

### 1.4 Product benchmark (6) (section 4). HOLDS, with a scope remark.

- Photon variance: stationary variance (2B sinh omega)^(-1) with cosh omega = 1 + k^2/2 (discrete Gaussian chain). sinh omega = k sqrt(1 + k^2/4) >= k >= 4|m|/n in the centred zone (sin x >= 2x/pi). Heat factor e^(-2 sigma n^2 k^2) <= e^(-32 sigma |m|^2). The displayed bound follows; the lattice sum is finite and independent of n. Correct.
- Ordered line: d(prod exp a_k, 1) <= sum |a_k| by bi-invariance, then Cauchy-Schwarz. E d(H, 1)^2 = O(1/B) uniformly in n. Correct. (A sharper count, the line integral projects on m_i = 0, gives the same order with a smaller constant; the order is all the proof uses.)
- Photon trace: six real oscillators per momentum (3 colours x 2 polarizations), n omega >= c |m|, log Tr D_ph^(2qn) <= 6 sum -log(1 - e^(-2cq|m|)) = O(e^(-c'q)). The HS residual after removing the photon vacuum is the trace minus one. Correct.
- Compact factor: normalizer >= c B^(-3/2) per link, kernel <= C B^(9/2), D_(B,all) unitarily equivalent to T_B / lambda_0 (ground-state transform), the full Perron vector is the invariant one, so ||D_(B,all)^q||_HS <= C' B^(9/2). Product with e^(-c'q/2), q ~ tau_0 B^(1/3), tends to 0. Compression to joint singlets: the photon-vacuum part is exactly J_0 D_B^q J_0^* (the Gaussian law is colour invariant, so the xi-average of a joint singlet is a U-singlet). Correct.
- Density correction (7): along a subsequence the rescaled eigenfunction converges strongly; approximate by a smooth compactly supported chi; its lift has L^2 invariant gradient O(1/eps); the translation error is at most |X| times that gradient norm (integrate along the geodesic, right invariance), so squared error O(eps^(-2) B^(-1)) = O(B^(-1/3)). Subsequence principle. Correct.
- j = 0 and j > 0 vector estimates: the identity J f_j -> psi_j(y) w(y, xi) and J_0 f_j -> psi_j(y H^(-1)) after multiplication by psi_0 is correct; |b - psi_0| <= ||psi_0(y H^(-1)) - psi_0(y)||_xi by the reverse triangle inequality; the bounded-multiplier approximation of psi_j by g psi_0 is valid since phi_0 > 0 a.e. Summing with the uniform thermal tail of (1) at time 2 tau_0, and ||J D J^* - J_0 D J_0^*||_HS <= 2 ||(J - J_0) D||_HS. Correct.
Scope remark (not a failing line). (6) is a decoupled product: the transverse modes perturb the readout only, not the compact dynamics, and the compact factor IS the reference. So (6) shows that the norm in (2) is not spoiled by free nonzero modes and their thermal weight. It is a consistency check of the definition of (2), not evidence about the Wilson box.

### 1.5 Stability under a bounded joint potential (section 4.1). HOLDS, with a scope remark.

- e^(-delta) <= lambda <= e^(delta): the multiplier norm, and the Rayleigh quotient on 1 with a positivity-preserving D_*. Correct.
- Kernel sandwich: S^q carries W with total weight q (halves at the ends, whole in the q - 1 inner slices); with lambda^(-q) the factor is in [e^(-2q delta), e^(2q delta)]. HS distance <= (e^(2q delta) - 1) ||D_*^q||_HS = o(1) when q delta_B -> 0. Correct.
- ||omega - 1|| = o(1): from (I - D_*^q) omega = o(1) and the spectral gap of D_*^q on the complement of 1 (at least 2/5 - o(1)). Correct.
- ||v - 1||_(2|Y) <= 2 ||omega - 1||_(2|Y): with a = ||omega||_(2|Y), ||omega/a - 1|| <= |1 - a| + ||omega - 1|| <= 2 ||omega - 1||. Correct, and no lower bound on a is needed.
- Clipping of J f_j and the sum over j: correct, uniform in n.
Scope remark (not a failing line). The hypothesis is a sup-norm oscillation o(B^(-1/3)) per box time, which is below the reference gap per box time. The leading Wilson coupling between the zero mode and the nonzero modes is not of this form: it is a zero-mode-dependent mass term for the transverse modes, quadratic in them and unbounded in sup norm on the joint space (and of order one along the toron valleys). So 4.1 does not cover the actual interaction even at leading order. Row 1642 line 442 says that no such bound is established for Wilson; the further point is that the Wilson effective interaction is outside the class of 4.1, so a weighted or localized version would be needed.

### 1.6 Weak compact Wilson U(1) fails at each fixed aspect alpha (section 5, lines 459-486). HOLDS given the cited periodic Villain input.

I re-did the change of geometry against row 1565 (Villain flux bound) and row 1573 lines 131-150.
- The unit sheet S has harmonic part 1/n^2 on all V = alpha n^4 plaquettes of type 23, so ||h||^2 = V/n^4 = alpha. Correct (row 1565 had w/n = 1/R).
- Supports r < n/8: the support box has side < 3n/8 and the joined graph has < n/4 edges, so no winding; the filling bound d_rho^2 <= 81 r^3 ||rho||^2 / n^4 is unchanged. Correct, since the shortest period is now n, not w.
- Supports r >= n/8: V = alpha n^4 <= alpha (8r)^4. So the first coefficient of M gains the factor alpha and 512^3 becomes alpha. Correct. M_(gamma,alpha) -> 0 as gamma -> infinity at fixed alpha.
- d_(gamma,alpha) = exp[-alpha/(2 gamma) - M/2] -> 1; the step-two second difference of row 1573 gives W_2 + W_(-2) >= 2 d^4 W_0; the offset mixture of row 1565 (6) carries it to Wilson cosine at all large bare beta with gamma fixed first; the vacuum has Q = 0, so G(alpha n) >= 2 d^4 > 1, against (3). All periods are even (n even, alpha n even). Correct.
Verdict: HOLDS given the PV current expansion, with the same source qualification as checks 1571 and 1613. NEW against check 1613, which proved G_even(n/512) > 1 only; G decreases in t, so the aspect-alpha statement needed this geometry change.
The compact Gaussian paragraph (lines 447-457) HOLDS: flux rotor |Q|^2/(2 beta n), ratio e^(-2q/beta) -> 1 at fixed q (upper bound fails); with the whole continuous centre only photons remain and the LOWER bound 3/10 fails.

### 1.7 Summary of item 1

No PROVED item fails. No correction is needed to any displayed inequality. Two scope remarks (1.4, 1.5) and one selectivity remark (section 3 below) qualify what the items show.

## 2. Is this the best next attack?

My answer is no, as a gap attack (ARGUED; a judgement over the record).

1. Supplying (HOT) moves no open input. (T-down) gives the seed only with (VIR-down) at the cold points of the characteristic on every side from L_h to L_h b^r (check 1630 section 1.3 (c)). That is registry row VIR-DOWN. It has no method (row 1610 C4), and its one test route, (E1)/(E2), is stopped (row 1641). (PUR-io), (VIR-down), (K-I), (K-II) stand as before.
2. The quality of (HOT) does not matter. Check 1630 section 1.3 (a)-(b): a larger r costs nothing in (HOT), and A alpha_h is independent of r. Any (HOT) with ANY fixed aspect, uniform in K, is absorbed by the choice of r. So a sharp hot-end tool buys nothing beyond a crude one.
3. (2) is stronger than (HOT). The consumer uses only p_1 <= 7/10 and the HS bound. (2) also forces p_1 >= 3/10, an eigenfunction match through J_n, and A_n^2 >= 15/16. The first buildable component (the annulus) tests the anti-concentration half, which (HOT) does not need. If a hot-end row is ever run, the right target is the one-sided (HOT) of row 1610 Corollary B (n m_1(beta_h) >= gamma and G(t_0; beta_h) <= N_0, uniform in K), not (2).
4. (2) forces B large (B^(-1/3) small against fixed constants), so L_h is a very weak box and the window must also cross more of the weak part C3. With a tight weak hot box, (RB) forces kappa_0 down to the weak level rate (check 1630 section 1.3 (e)). The band then needs a smaller uniform positive rate. That is pointwise weaker, but it is the same kind of input, an order-one-coupling running estimate (K-II).
5. What row 1642 adds to row 1610's Row B: a precise C2 target with a proved consumer, a necessary one-slice test, and a toy benchmark. It does not change row 1610's judgement (section 4, Row B: "this row moves no open item while C4 has no method"), which I share. Its one merit stays the one row 1610 named: a proved (HOT) would be a selective fact at a physical size, at late cutoffs, in the consumer's variable. It would change the inventory of Proposition NEG (row 1386), not the seed.

## 3. Does the U(1) failure read the law? (Lemma ALG, row 1553)

- Half-turn projection (section 1.6): the failing line is Z_even(alpha n) >= (1 + 2 d^4) Z_(Q=0)(alpha n), the Coulomb cost alpha/(2 gamma) of flux +-2. It fires only at weak coupling. At the gapped twin (4D U(1) at small beta) the flux sectors cost a string tension times the area, and G(alpha n) is small. So the line passes test (g3) and reads the law. ARGUED for the twin; the twin bound is not written out in either file. What it reads is electric-flux deconfinement in sectors Q = +-2. These sectors survive only because the half-turn projection is the Z_2 analogue; they have no SU(2) counterpart (SU(2) electric flux is Z_2-valued and P_0 removes it). This agrees with check 1571's reading of row 1565 ("electric-flux confinement, not the gap").
- Full continuous centre: the U(1) hot box PASSES (HOT). Only photons remain, n omega >= c |m|, so G(alpha n) is about 12 e^(-2 pi alpha), below 1/10 for alpha >= 1 (ARGUED; one-line Gaussian count, the same as section 4 of row 1642). Only (2) fails, at its LOWER bound 3/10. That failure reads the choice of an SU(2) reference with p in [2/5, 3/5], so it is decided by the algebra (Lemma ALG). It is no selectivity evidence. With this projection, the selectivity of (T-down) against U(1) rests on (VIR-down) (check 1613: beta-independent photon levels force kappa = 0).
- Gapless member with an SU(2) factor (test g4): a neutral massless spectator breaks p_1 <= 7/10 (row 1642 lines 504-506). So (HOT) and (2) read the neutral sector. HOLDS (one line).
- 5D: GUESSED in row 1642 and in check 1613; no failure line is proved.
Summary: the half-turn U(1) failure reads the law but reads flux deconfinement at the hot end; the full-centre U(1) failure of (2) reads only the algebra. Neither is a statement about the band.

## 4. The first open estimate of (2) on actual 4D Wilson boxes

Statement (row 1642 section 5, made explicit). Fix B large, a_0 < a_1 as in section 5, the flow time (n/128)^2. On the spatial torus (Z/n)^3, n = L_h b^(K+r), in the 4D Wilson vacuum slice law at beta_(K+r), let Y_1 be the flowed based winding holonomy. Show
  liminf over K of P( a_0 B^(-1/3) < |Im Y_1| < a_1 B^(-1/3) ) >= 11/16.
It is necessary for (2) and sufficient for nothing.

Is it ultraviolet? Yes. It is a one-slice vacuum statement at one fixed weak box (box coupling about 4/B), uniform in the cutoff.

Is it plausibly within reach? Not soon (ARGUED).
- Before flow, the winding holonomy is close to Haar (row 1145). So the flow must remove order-one ultraviolet noise and bring the holonomy to within a_1 B^(-1/3), that is order g(L_h)^(2/3), of the centre. This is a cutoff-uniform smoothing estimate for the nonlinear 4D Wilson flow on typical weak-coupling fields. No such estimate is on file (search above).
- The upper tail needs confinement of the flowed zero mode along the whole toron valley. This is item (i) of row 1386 section 2.1 for (SV-Z): the effective action at flat block fields with a nontrivial holonomy on the whole valley. Items (ii) (large fields on the last coarse torus) and (iii) (a comparison for a weight that is Wilson only up to a small error) also enter. None is on file.
- The lower tail (anti-concentration at scale a_0 B^(-1/3)) needs an upper bound on the effective electric stiffness at the box scale. No tool on file.
- Precision: an e^(+-C) error on the coarse weight, which is what (SV-Z) would tolerate, does not preserve 11/16. The full (2) needs more: its dynamical error must be o(B^(-1/3)) per box time (the scale of section 4.1), and section 1.5 shows that the leading Wilson interaction is outside that class.
So the first estimate is ultraviolet but it is the hard part of the rigorous small-volume expansion (Luscher; Koller and van Baal), made uniform in the cutoff. It is a multi-row ultraviolet construction of the size that rows 1386 and 1515 declined for (SV-Z). It is not a one-row lemma.

## 5. New against on file

| Item | Standing | Anchor |
|---|---|---|
| One-vertex spectrum, heat trace, vacuum compactness | ON FILE | row 1227 (5)-(8), check 1230 step 6 |
| Unflowed winding holonomies close to Haar | ON FILE | row 1145 (1)-(4) |
| TR-down, last crossing, (RB), r fixed first | ON FILE | rows 1610, 1613, 1630 |
| Hot end C2 as a target; its judgement | ON FILE | row 1610 sections 2.6, 4 (Row B); row 1386 section 2.1 (SV-Z) |
| Half-turn U(1) flux bound at aspect 1/512 | ON FILE | rows 1565/1571, 1573/1579, check 1613 |
| Compact Gaussian flux rotor; photon variance | ON FILE | rows 1618/1622, 1638/1640 |
| Gapless spectator test | ON FILE | rows 1553 (g4), 1573 |
| Comparison (2) with the flowed winding readout and the one-vertex reference | NEW | row 1642 section 3 |
| (2) gives (HOT) at alpha_h = 2jq | NEW (consumer) | section 3 |
| Affinity bound (5), annulus 11/16, decomposition (4) | NEW | sections 3, 3.1, 5 |
| Separations of (2) from the seed on abstract families | NEW | section 3 |
| Product benchmark (6), density correction (7), stability 4.1 | NEW | section 4 |
| U(1) Villain failure at each fixed aspect alpha >= 1 | NEW (geometry change of rows 1565/1573) | section 5 |
| 5D failure; (2) on actual Wilson boxes | GUESSED, open | section 5 |

Provenance: Claude Opus 5.5, laptop subagent; cross-provider check of a gpt-6.2-astra max row; by hand; no numerics, no Lean; one reader. This is not an independent derivation of any input it cites: rows 1145, 1227, 1565 and 1573 were read, not re-proved, apart from the steps re-derived above.

## RESULT

Row 1644 (Claude Opus 5.5, by hand, no numerics or Lean): check of row 1642 (gpt-6.2-astra max).
Item 1: every PROVED item HOLDS with no failing line: (2) gives (HOT) at aspect 2jq and forces A_n^2 >= 15/16 and annulus mass >= 11/16;
(6) and its stability 4.1; the unflowed readout fails (from row 1145); weak Wilson U(1) with half-turns fails at each fixed aspect (given PV).
Scope: (6) is a decoupled product, and 4.1's sup-norm class excludes the leading Wilson zero-mode/nonzero-mode coupling.
Item 2: not the best next attack. (HOT) moves no open input: (T-down) still needs (VIR-down) on every side L_h..L_h b^r (no method; row 1641),
and any fixed hot aspect is absorbed by r (check 1630). (2) is stronger than (HOT): the lower bound and the annulus are not needed for it.
Item 3: half-turn U(1) failure reads the law (flux deconfinement, fires only at weak coupling); with the full centre U(1) passes (HOT) and (2)
fails only at its lower bound, which reads the algebra. Item 4: the first estimate (annulus for one flowed winding holonomy) is ultraviolet but
needs a cutoff-uniform flow smoothing and the toron-valley effective action (row 1386 SV-Z (i)-(iii)); not within one row.
Recommendation: do NOT run a proof row on comparison (2). If the owner wants the hot end as side work, target the one-sided (HOT) of
row 1610 Corollary B instead. The crux remains VIR-DOWN on the band.
