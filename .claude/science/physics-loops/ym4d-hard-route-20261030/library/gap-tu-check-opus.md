# Check of library/gap-tu-retry.md (FINISH row 794), by Claude Opus 5.5, line by line

- Target: `/Users/jonreilly/ym4d-lead/clone/.claude/science/physics-loops/ym4d-hard-route-20261030/library/gap-tu-retry.md`, 533 lines, read in full. Author: Codex gpt-6-astra max (FINISH row 786 in the note).
- Clone commit: `ba1c0f084`. Main commit: `bb4ec020d5` (equals `origin/main` at check time; PV unchanged between them).
- PV: `docs/PERIODIC_FINITE_CLOCK_VILLAIN_COVARIANCE_AND_OBSERVABLE_MASSLESSNESS_BOUNDED_THEOREM_NOTE_2026-09-14.md` at `bb4ec020d5`, sections 1-10 read in full. WV sections 5-7 read for item 6.
- Context read: `gap-ac-lat.md` section 4; `gap-skeleton-max.md` 1.D; `gap-transport-check.md` section 2; `gap-u1-audit-opus.md` section 3 R2.
- Method: by hand. One GUIDE run (under 1 MB, `guide.py` beside this file): it enumerated plaquettes on M = 4, 5, 7 and found no plaquette with two links of one colour (colour counts 32, 108, 108); it printed b_1 = 3.0127. No verdict rests on it.
- This is one check by one model. It is not an independent derivation of PV.

## 1. Section 1.1: the reused estimate and its parity extension

**What PV states.** PV section 1: "Let T_L=(Z/LZ)^4, with L even and L>=4." The constants use a = beta/384 - beta_1, and PV says "We use c only for beta>=2000, so a>0 and every damping bound used below is valid." PV (7.3): Cov_(b+K)(F) >= beta(1-delta(beta)) P_e "for EVERY affine translate, regardless of its conditional mean", uniformly in L. The theorem adds beta_d >= 2000, but (7.3) itself needs only the primal beta. So (5) is PV's statement, for even M and beta >= 2000. The coexact image is PV's last paragraph of section 7 (Hodge star, star_2 delta_3 = -d_1 star_3).

**Where PV uses evenness.** A search of PV for even/parity finds, in sections 2-10, only the 32-colour step of section 5 (line 266, "On an even torus these 32 colors are well defined") and the hypothesis lines. I checked the other steps for hidden parity use: the Smith-invariant duality (2.1); the Haar/Fejer step on H (section 3); the 107-neighbour count (image of the lifted neighbourhood, so at most 107 on any torus); the winding bound "a nonzero-winding simple cycle needs at least L edges"; the box filling and the packing count 4(9r)^4; the scalar gap 4 sin^2(pi/L) >= 16/L^2 (true for every L >= 2, by sin x >= 2x/pi); L <= 8r in (6.5); the Hodge map on the dual torus. None uses evenness. The note's claim at lines 135-136 holds.

**The three-colouring.** For odd M, colour vertex i of Z/MZ by i mod 2 for i <= M-2 and by 3 for i = M-1. Since M-1 is even, vertex M-2 has colour 2 and vertex 0 has colour 1, so both neighbours of M-1 differ from 3. The colouring is proper. A link (x, j) gets colour (j, c(x_k) for k != j): at most 4 * 27 = 108 colours. In a jk-plaquette the two j-links differ by one step in coordinate k, so their k-colours differ; the two k-links likewise; a j-link and a k-link differ in orientation. So no two links of one colour share a plaquette. Correct.

**The exponent 1/1296.** Pigeonhole gives a colour with at least 1/108 of ||rho||^2. PV's identity (5.1) needs only Q_ee = 6 on selected links and no shared plaquette between selected links; both hold for every M >= 4. The damping factor is exp[-(beta/2)(1/6)(1/108)||rho||^2] = exp[-beta||rho||^2/1296]. With (4.3), z_rho <= exp[-(beta/1296 - b_1)||rho||^2]. Correct. The constants 8503056 = 81 * 26244 * 4 and 262144 = 8^6 come from (6.4)-(6.5), which do not involve the colour count. So (6) is PV's constant with 384 replaced by 1296. Correct.

**The hand bound (7).** b_1 < 10/3 (PV section 9). For beta >= 2592 b_1, a >= beta/2592; 2592 * 10/3 = 8640 < 2^14. Then q = exp(-2 pi^2 a) < exp(-pi^2 beta/1296) < exp(-beta/144) (pi^2 > 9), and beta/144 >= 16384/144 > 113 > 64, so q < e^-64 < 2^-64 (log 2 < 1). So q <= 1/1024 and S_5, S_6 <= 2q. Then delta_* = (beta/a)(8503056 S_6 + 262144 S_5)/e <= (beta/a) * 2 * 8765200 q/e < 2592 * 8765200 q < 2^12 * 2^24 * 2^-64 = 2^-28. Each step is correct, and each holds at every beta >= 2^14 directly, with no monotonicity needed.

**Remark (precision, not a correction of a step).** Lines 137-146 say "(5) ... hold for every M >= 4 with" (6), but they do not restate the beta range there. The range matters. With 1296, PV's threshold 2000 does not carry over: a(2000) = 2000/1296 - b_1 < 0 (b_1 > 3). The extended (5) needs a > 0 and PV's positivity step z_rho < 1/2 (section 5). Both hold for beta >= 2^14: a > 6.3, so z_rho <= exp(-4 pi^2 a) < 1/2. The note restricts Theorem V to beta >= 2^14, so no use is wrong. The z_rho < 1/2 step is not re-verified in the note; it follows from (7) in one line.

**Verdict, item 1: HOLDS.** (Precision remark: the extended (5)-(6) holds for beta >= 2^14, which (7) covers, including z_rho < 1/2; PV's own threshold 2000 would fail with the 1296 constant.)

## 2. Section 1.2: (8) and (9)

**(8).** prod_p phi_beta((d_1 theta)_p) = sum_n e^{-||n||^2/(2 beta)} e^{i <d_1^T n, theta>}, absolutely and uniformly convergent. Integrating each link over continuous Haar keeps exactly the n with d_1^* n = 0. So the integer law is the centred discrete Gaussian on Lambda = Z^P intersect ker delta_2. Correct. (Centred: n -> -n.)

**Lower bound in (9).** delta_3 Z^C is a sublattice of Lambda, since delta_2 delta_3 = 0. Each coset is an integer affine translate b + delta_3 Z^C. Its conditional law is the discrete Gaussian on that translate. The coexact (7.3), extended in item 1 to every M >= 4, gives conditional covariance >= beta(1 - delta_*) P_c for every coset. Total covariance = mean of conditional covariances + covariance of conditional means >= beta(1 - delta_*) P_c. This is PV's (8.1) argument with N = infinity. Correct.

**Upper bound in (9).** At fixed M and clock order N, PV's law lives on L_N = {n : delta_2 n in N Z^E}. For fixed n, the indicator of delta_2 n in N Z^E equals the indicator of delta_2 n = 0 once N > max|delta_2 n|. So it converges pointwise. Z^P is finite-dimensional, so (1 + ||n||^2) e^{-||n||^2/(2 beta)} is summable and dominates. Normalizers (each at least the n = 0 term), means and second moments converge: C_N(beta) -> C_M. PV's (8.2) gives C_N <= beta P_c + beta delta(beta_d) P_e + beta P_h. Its dual-side lower bound uses (7.3) on cosets of d Z^E in M_N, at beta_d = N^2/(4 pi^2 beta); this needs the parity extension when M is odd, and it needs beta_d >= 2^14, true for large N. By (7), delta_*(beta_d) < 2^36 q(beta_d) -> 0. The limit gives C_M <= beta(P_c + P_h). Correct. The limit is at one fixed M, as the note says.

A consistency check by a different route: n lies in ker delta_2 = im delta_3 + harmonic, so P_e C_M = 0. The upper bound then says only C_M <= beta I on that subspace, which also follows from PV's (2.1) limit. This agrees.

**Verdict, item 2: HOLDS.**

## 3. Section 1.3: (10), the local limit, (11), (12), the contradiction

**(10) for continuous Haar.** For p != q, mu(s_p s_q) = Z^{-1} sum_n (i n_p)(i n_q) e^{-||n||^2/(2 beta)} 1{delta_2 n = 0} = -E_nu(n_p n_q). For p = q, s^2 = phi''/phi - (log phi)'', and mu(phi''/phi) = -E_nu(n_p^2). So mu(s_p^2) = kappa_M - C_M(p,p). All series converge absolutely. mu(s_p) = 0 by theta -> -theta (s odd), and E_nu(n) = 0. Hence (10). Correct. (It agrees with PV (10.1) and its remark that the diagonal insertion is -phi''/phi.) kappa_M is orientation independent by cubic symmetry, and (log phi)'' is even, so the orientation sign does not matter.

**Local limit.** The space of link configurations of Z^4 is a countable product of circles, compact metrizable; probability measures on it are weakly compact. Embedding fixed boxes in T_M for large M gives local subsequential limits. Translation, cubic and charge-conjugation symmetry pass. s_p s_q and (log phi)'' are bounded continuous local functions, so kappa_M and C_{s,M}(p,q) converge along the subsequence, and by (10) so does C_M(p,q). Correct.

**(11).** For finitely supported f, <f, P_c^{(M)} f> = M^{-4} sum over k in (2 pi/M) Z^4, k != 0, of f-hat^* P_c(k) f-hat; this is a Riemann sum of a bounded function continuous off k = 0, so it converges to the infinite-lattice value. P_h^{(M)}(p,q) = M^{-4} for equal orientation (six constant forms of entry M^{-2}), so it vanishes. The bounds of (9) are uniform in M. So the limit kernel C is positive and translation invariant with beta(1-delta_*)<f,P_c f> <= <f,C f> <= beta<f,P_c f>. A bounded positive translation-invariant kernel is a convolution with an L^infinity positive matrix density; quadratic-form bounds on trigonometric polynomials give the a.e. matrix bounds (11). Correct.

**(12).** P_e = d_1 d_1^*/sum|v_a|^2 at k != 0, and (d_1 d_1^*)_{12,12} = |v_1|^2 + |v_2|^2. With P_e + P_c = I at k != 0 (no harmonic part in infinite volume), (12) follows. It matches PV section 10. Correct.

**Contradiction.** If the score covariance in orientation 12 were in l^1(Z^4), its Fourier series would be continuous. By (10), kappa minus it is a continuous representative of C-hat_{12,12}. The diagonal entries of (11) hold a.e.; both sides are continuous off 0; so they hold everywhere off 0. On the k_1 axis, P_c,12,12 = 0, so C-hat_{12,12} = 0. On the k_3 axis, P_c,12,12 = 1, so C-hat_{12,12} >= beta(1-delta_*) > 0. The two limits at k = 0 differ. No continuous value exists at 0. Correct. Note: this uses the sharpened upper bound beta P_c (no delta(beta_d) P_e term), which item 2 established; on the k_1 axis it forces the value 0 exactly.

The argument applies to every local subsequential limit of every sequence M -> infinity. No boundary selection enters.

**Verdict, item 3: HOLDS.**

## 4. Section 2: (13), Lemma L, and the completion of Theorem V

**(13).** d_e d_{e'} U = sum over plaquettes p containing e and e' of (sign) V''((d_1 theta)_p). It vanishes unless e, e' share a plaquette, i.e. r(e,e') <= 1. For M >= 3 a link lies in 6 distinct plaquettes, each with 4 links (including e). So sum_{e'} B_{ee'} <= 6 * 4 * ||V''|| = 24||V''|| = H. (The diagonal takes 6||V''||, the 18 off-diagonal entries ||V''|| each.) Correct.

**(15).** The SDE d theta = -grad U dt + sqrt2 dW has generator Delta - grad U . grad = -L, so P_t = e^{-tL} is its semigroup. J_t solves J' = -Hess U(theta_t) J, J_0 = I. The Dyson series J_t = sum_k (-1)^k (time-ordered integral of k Hessians) converges, and entrywise |J_t| <= sum_k t^k B^k/k! = e^{tB}. So d_e P_t F = E[sum_i d_i F(theta_t)(J_t)_{ie}] and (15) follows. Smooth periodic drift with bounded derivatives justifies the differentiation. Correct.

**(16).** (B^k)_{ie} != 0 needs a path of at most k adjacency steps, so r(i,e) <= k. Column sums of B^k equal row sums by symmetry, and row sums are at most H^k. So sum_i e^{r(i,e)}(B^k)_{ie} <= e^k H^k, and summing with t^k/k! gives e^{eHt} <= e^{vt}. Correct.

**From (15)-(16).** (e^{tB})_{ie} <= e^{-r(i,e)} e^{vt}. For F supported on X, ||d_e P_t F|| <= sum_{i in X} ||d_i F|| e^{-r(i,e)} e^{vt} <= D(F) e^{-r(e,X)+vt}. Correct.

**(17).** d/dt mu(P_t F . G) = -mu(L P_t F . G) = -mu(grad P_t F . grad G), by reversibility of mu = e^{-U}/Z under L. Integrating from 0 to T and using mu(P_T F) = mu(F) gives (17). Correct.

**T = r/(2v).** First term: for e in Y, r(e,X) >= r, so |mu(grad P_t F . grad G)| <= D(F) D(G) e^{-r+vt}. Integration gives D(F)D(G) e^{-r}(e^{vT}-1)/v <= D(F)D(G) e^{-r/2}/v. Correct.

**Spectral step.** Vertex gauge transformations act as translations theta -> theta + d_0 lambda, isometries that preserve U. So L commutes with them and P_T maps gauge-invariant functions to gauge-invariant functions. The infimum (3) over smooth invariant f equals the bottom of the spectrum of L on invariant mean-zero L^2 (Haar-averaging of a core gives an invariant core). So |Cov(P_T F, G)| = |<P_T(F - mu F), G - mu G>| <= e^{-eps T} sqrt(Var F Var G). Correct. For r = 0, T = 0 gives the trivial bound. (14) holds, with constants depending only on V, F and G.

**Completion of Theorem V.** If (4) fails, limsup gamma_V > 0, so a sequence M_j has gamma_V >= eps. V = -log phi_beta is smooth and periodic (phi_beta > 0). F = s_p, G = s_q are gauge invariant, with ||s||_inf and D = 4||s'||_inf fixed at this beta. A plaquette's links have anchors within l^inf distance 1 of its anchor; an adjacency step moves an anchor by at most 1 in each coordinate. So r(supp s_0, supp s_x) >= |x|_inf - 2 for periodic distance, which equals lattice distance for fixed x and large M. (14) gives a bound C_1 e^{-(|x|-2)/2} + C_2 e^{-eps(|x|-2)/(2v)}, uniform in j. It passes to any local limit of a further subsequence (bounded continuous local observables). The limit covariance is summable over Z^4. Section 1.3 forbids this in every local limit. So every sequence has gamma_V -> 0 along it: the full limit is 0, not only the liminf. The unrestricted gap is an infimum over a larger class, so it is at most the restricted gap. Correct.

**Verdict, item 4: HOLDS.**

## 5. Section 3: (18)-(23) and the logic against (TU)

**(18).** A_M = sum_p V with V = -log phi_{beta_*}, a fixed smooth function; the family is e^{-b A_M}. At b = 1, L_1 = -Delta + grad U_{beta_*,M} . grad, the generator (2). So gamma_M(1) = gamma_V(beta_*; M). Correct.

**(19) and the circle comparison.** Given the other links, theta_e has density proportional to exp(-b_s sum over the 6 plaquettes at e of V). Each term varies by at most O in theta_e, so the oscillation is at most 6 b_s O <= log2 * O/(O+1) < log 2. Haar gap on the circle is 1 (Fourier modes n^2). For m <= rho <= M_rho: Var_rho f <= int (f - Haar mean)^2 rho <= M_rho int |f'|^2 dHaar <= (M_rho/m) int |f'|^2 rho. With M_rho/m <= e^{6 b_s O} < 2, the conditional gap is at least 1/2. Correct.

**Conditional to global.** L_e is the generator of the conditional law in theta_e. It is nonnegative, kills constants, and has gap at least 1/2 on conditional-mean-zero functions. So L_e^2 >= (1/2) L_e as operators (lambda^2 >= lambda/2 on {0} union [1/2, infinity)). Conditionally, int (L_e f)^2 >= (1/2) int (d_e f)^2. Integrating over the other links gives mu((L_e f)^2) >= (1/2) mu((d_e f)^2). Correct.

**(20).** L = sum_e L_e. On the flat torus with mu proportional to e^{-b_s A}, the Gamma_2 identity gives mu((Lf)^2) = mu(|Hess f|^2) + b_s mu(Hess A(grad f, grad f)). The one-link version, under the conditional law, gives the second line. Both are exact. Correct.

**(21).** Subtracting: mu((Lf)^2) = sum_e mu((L_e f)^2) + sum_{e != e'} mu((d_e d_{e'} f)^2) + b_s sum_{e != e'} mu(A_{ee'} d_e f d_{e'} f). Two distinct links share at most one plaquette (M >= 3), so |A_{ee'}| <= K, with 6 * 3 = 18 nonzero off-diagonal entries per row. With 2|xy| <= x^2 + y^2, the last sum is at least -18 b_s K mu(|grad f|^2). Dropping the nonnegative middle sum gives (1/2 - 18 b_s K) mu(|grad f|^2), and 18 b_s K <= 18K/(72(K+1)) < 1/4. For an eigenfunction, gamma^2 mu(f^2) >= (gamma/4) mu(f^2), so gamma_M(b_s) >= 1/4 for every M, restricted or unrestricted. Correct.

**(22).** This is HF4 of `gap-skeleton-max.md` 1.D, checked line by line in `gap-transport-check.md` section 2 (Lemma 2 HOLDS; log gamma is 2 osc(A)-Lipschitz; at a differentiability point every gap mode attains the Rayleigh minimum). The derivation uses only integration by parts on a fixed invariant f, so it holds on the gauge-invariant subspace. The note's description at lines 419-423 matches that check. Correct.

**(23).** If (TU) holds at b with constant c, then by (22) b gamma' >= gamma - (1 + 2cb) gamma = -2cb gamma, so (log gamma_M)' >= -2c (b > 0). This holds at a.e. b in [b_s, 1]. log gamma_M is Lipschitz, hence absolutely continuous, so log gamma_M(1) >= log(1/4) - 2c(1 - b_s). Correct.

**Is "Theorem V contradicts (23)" valid with the start at b_s and the end at b = 1?** Yes. b_s <= 1/2 < 1, so [b_s, 1] is a nondegenerate interval. The start gap 1/4 at b_s is proved by (21), uniformly in M. The end b = 1 is exactly the Villain measure at beta_* >= 2^14, where Theorem V gives gamma_M(1) -> 0. So for each finite c, some M has gamma_M(1) < (1/4) e^{-2c(1-b_s)}. For that M, (log gamma_M)' < -2c on a set of positive measure in [b_s, 1]; there (TU) fails for every gap mode. The negation is correctly stated at lines 434-436.

**Scope.** The contradiction refutes (TU) posed with a starting point b'_s <= 1 at which a volume-uniform gap is known (for b'_s <= b_s of (19) it suffices directly). It does not refute (TU) for SU(2), nor (TU) posed above a b'_s > 1 or above a b'_s with no known uniform start. The note states both limits at lines 443-446. The "method-level" verdict at lines 439-442 is a correct informal reading: any proof of a volume-uniform (TU) on [b_s, 1] that uses only hypotheses satisfied by family (18) on (Z/M)^4 (compactness, smooth local plaquette interaction, gauge invariance, HF1-HF4) would prove a false statement.

**Verdict, item 5: HOLDS.**

## 6. Sections 4-5: do the stated limits match what is proved?

**Section 4, reduction.** For Wilson, V_b = -b cos is smooth and periodic, so Lemma L applies at each fixed b. If (24) holds in every local subsequential limit at b_*, the completion argument of item 4 gives gamma_W(b_*; M) -> 0 (full limit). The reduction is correct. (24) uses sin, a constant multiple of the score; summability is unchanged.

**Transfer 1 (density comparison).** e^{b cos t} = sum_n I_n(b) e^{int}. Proportionality to phi_beta would need I_n(b)/I_0(b) = e^{-n^2/(2 beta)} for all n. I_n(b) >= (b/2)^n/n! >= (b/(2n))^n (first series term; n! <= n^n). The log of the right side is about -n log n, while -n^2/(2 beta) is eventually smaller. So osc h > 0. The Holley-Stroock factor over 6M^4 plaquettes is exp(6M^4 osc h). The note claims only that this comparison fails. Correct.

**Transfers 2-3.** I read WV sections 5-7. Section 5 proves monotonicity of cosine-character means (Ginibre). Section 6 reduces to a diluted Villain comparison and says it "still needs a gauge-phase theorem robust to these deleted plaquettes". Section 7 proves E[t] = infinity for the auxiliary variance. The note's descriptions match. Its logical remark (monotonicity of E(FG) and of E(F)E(G) separately gives no order on their difference) is correct. These are statements that a transfer is not supplied; nothing downstream rests on them.

**Section 5.** "Established": (U-tor) for Villain at beta >= 2^14, full limit over all M >= 4 including odd M (items 1-4); Lemma L (item 4); failure of volume-uniform (TU) on [b_s, 1] for (18) from the start (19) (item 5). Each matches a proved statement. "Not established": Wilson (U-tor), any rate, SU(2) (TU), (AC'-lat). This matches: no rate is proved, and (24) is left open. The warning that the Villain beta is not the HF4 coupling is correct (section 3 opening): -log phi_beta is not beta times a fixed function. The Result paragraph (lines 53-59) states the same scope.

The note's opening search record (lines 1-43) and its literature credits are provenance statements, not proof steps. I did not re-run those searches.

**Verdict, item 6: HOLDS.**

## Verdict table

| Item | Content | Verdict |
|---|---|---|
| 1 | (5) as PV (7.3); odd-M three-colouring, 108 colours; 1/1296; (6); (7) at beta >= 2^14 | HOLDS (precision remark: the extended (5)-(6) needs beta >= 2^14, which (7) covers, including z_rho < 1/2; PV's 2000 fails with 1296) |
| 2 | (8); (9) lower bound by cosets of delta_3 Z^C; upper bound by N -> infinity at fixed M | HOLDS |
| 3 | (10) on Haar; local limit; (11); (12); discontinuity at k = 0 | HOLDS |
| 4 | (13); Lemma L (14)-(17); Theorem V completion, full limit | HOLDS |
| 5 | (18)-(21) uniform start 1/4; (22) HF4; (23); contradiction on [b_s, 1] | HOLDS |
| 6 | Sections 4-5 scope against what is proved | HOLDS |

No FAILS. No correction of a step. One precision remark (item 1).

RESULT: Every step of sections 1-3 of gap-tu-retry.md holds as written: periodic Villain U(1) at beta >= 2^14 has gauge-invariant Langevin gap tending to 0 on all tori M >= 4, and this refutes volume-uniform (TU) on [b_s, 1] for the fixed action (18) from the proved start (19)-(21); the only remark is that the beta range of the extended (5)-(6) should be stated as beta >= 2^14.
