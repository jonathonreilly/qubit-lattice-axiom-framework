# FINISH row 924, gap-univk-opus, Claude Opus 5.5 max

(file seeded by the lead; the author writes below)

Clone: /Users/jonreilly/ym4d-lead/clone at commit 1020c3efcfe45c942f5711c05eae8fa49e0ea698 (git pull --ff-only: already up to date, 2026-11-13).
Sussman-Alpoge sources: /Users/jonreilly/ym4d-lead/sa (commit 31a47c543775) and /Users/jonreilly/ym4d-lead/sa1400/YM4_1400.tex.
Credit: the account is by Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of its text. Balaban for his estimates.
Lane directory D = .claude/science/physics-loops/ym4d-hard-route-20261030 (in the clone).

## Target (provisional; Step 1 replaces it with the exact text after check 917's corrections)

(UNIV-K), as named by row 916 Step 7: along chains of first-passage data that match final couplings, the seed functional Phi changes by at most (L^4+1) eps_K between a first-passage datum and its predecessor, with sum_K eps_K < infinity. Under (UNIV-K), (ONE-K) holds: a seed at one cutoff's window suffices.

## Plan (one step per response; each step appended here before the next)

1. Read row 916 Step 7 and check 917. Write the exact (UNIV-K) and (ONE-K) with 917's quantifier correction.
2. Read (SEED-FP) (gap-finishline-opus.md L110-160) and row 904 (gap-univfp-opus.md). Fix Phi, the first-passage datum, the chain, and the predecessor map.
3. Read the account's finite-horizon universality theorem (YM4_1400.tex L94364-94381) and its definitions. Record hypotheses and conclusion with line numbers.
4. Regular part: prove or refute "summable eps_K" from the account's statements.
5. Missing part A: vacuum factors / unnormalized masses on two fixed tori (L94473-94474). Prove from the account's estimates or state the exact missing statement.
6. Missing part B: large-field histories (L94511-94512). Same treatment.
7. Fact tests: U(1) Coulomb phase (row 786), Q_8 and 2T (rows 838, 843), Dobrushin caps (row 839), (AN1) (row 845).
8. Status table (PROVED / READ / ARGUED / GUIDE / OPEN) and the RESULT line.

## Step 1. Exact (UNIV-K) and (ONE-K) after check 917

Sources read in full for this step: row 916 Steps 6-8 (READ D/library/gap-chain-ce-opus.md L253-386) and check 917
Sections 3-4 (READ D/library/gap-chain-ce-check-astra.md L237-412).

Setting (READ gap-chain-ce-opus.md L290-291). Fix g, odd L >= 25, and ell with T_ell, T_(L ell) in the account's
family. A first-passage datum is d = (K, beta) with beta in W_K(g) = {beta >= g^-2 + B_sharp : K(beta, g) = K}, and
K(beta, g) = min{k : x_k(beta) <= g^-2 + B_sharp} (READ CA L1666-1667). F_d(T) = log Z_(K,T,beta).
Phi(d) = L^4 F_d(T_ell) - F_d(T_(L ell)), and vol(T_(L ell)) = L^4 vol(T_ell).

**(UNIV-K), exact form (row 916 L293-295, with 917's corrections).** There are K_0, a map pi, and eps_K >= 0 with
E(K_0) := sum_(K > K_0) eps_K < infinity, such that:
 (i) pi is defined on EVERY first-passage datum d of cutoff K > K_0, and pi(d) is a first-passage datum of cutoff K - 1
     (917 L254-256: existence of each intermediate datum is part of the hypothesis; nonempty windows do not supply it);
 (ii) for every such d there is a real c_d with |F_d(T) - F_(pi d)(T) - c_d vol(T)| <= eps_K for T = T_ell and T = T_(L ell).

**Lemma 1.1 (two-torus reduction). PROVED (re-derived; 917 L389-394 states it).** (ii) holds for d with some c_d iff
|Phi(d) - Phi(pi d)| <= (L^4 + 1) eps_K.
Proof. Put u = F_d(T_ell) - F_(pi d)(T_ell), w = F_d(T_(L ell)) - F_(pi d)(T_(L ell)), v = vol(T_ell). Then
Phi(d) - Phi(pi d) = L^4 u - w. (=>) u = c v + r_1, w = c L^4 v + r_2 with |r_i| <= eps_K, so L^4 u - w = L^4 r_1 - r_2,
of size <= (L^4 + 1) eps_K. (<=) Take c_d = (u + w)/((L^4 + 1) v). Then u - c_d v = (L^4 u - w)/(L^4 + 1) and
w - c_d L^4 v = -(L^4 u - w)/(L^4 + 1). Both have size |Phi(d) - Phi(pi d)|/(L^4 + 1) <= eps_K. QED

So on the two fixed tori, (UNIV-K) says exactly: the increments of Phi along pi are uniformly summable,
  sum_(K > K_0) sup_(d of cutoff K) |Phi(d) - Phi(pi d)| < infinity.                                     (UNIV-K')
The constant c_d carries no information of its own. Convergence of Phi along chains is weaker (917 L395-397: (-1)^K/K).

**(ONE-K), exact form after 917's base-set correction (917 L262-268). PROVED in row 916 L297-302; algebra re-checked
here.** Under (UNIV-K): if Phi(d_0) <= phi_* - (L^4 + 1) E(K_0) for every first-passage datum d_0 of cutoff K_0, then
Phi(d) <= phi_* for every first-passage datum d with K >= K_0. (Telescope |Phi(d) - Phi(pi^(K-K_0) d)| <=
(L^4+1) sum_(k=K_0+1)^K eps_k <= (L^4+1) E(K_0).) The margin bound keeps the logarithm:
(L^4+1) E(K_0) < (L/2) log(13/10) is necessary for a nonnegative base (917 L319-331; the decimal 0.131 is not used).

**Matched variant (UNIV-K, match).** Same, with the extra clause x_(K-1)(beta') = x_K(beta) for pi(K, beta) =
(K-1, beta'). 917 L285-306: matching is NOT logically necessary for (UNIV-K); it is a hypothesis of the account
theorem (U2) one would use. Using (U2) across consecutive cutoffs also needs a common frozen presentation, horizon,
domain, measure and an admitted initial profile (917 L302-306).

**Corrections from 917 that bind the later steps.**
- C1. The n = 0 statement must be a two-volume comparison after one common extensive subtraction, with uniformly
  summable consecutive errors (917 L353). Separate convergence of the two normalizers does not give it.
- C2. (U2) bounds the ratio of regular integrands and of their normalizers (917 L350, CA L94495-94496). If the
  interaction difference on the common domain D with common positive measure nu (CA L94456-94488) is <= delta, then
  |log Z^reg_H - log Z^reg_(H~)| <= delta, delta = C V q_2^N ||H - H~|| (917 L355-367). Re-derived: PROVED (pointwise
  e^(-delta) <= w_H/w_(H~) <= e^delta and integrate against nu).
- C3. What (U2) leaves out: scalar vacuum factors (CA L94473-94475), complementary histories (CA L94511-94512),
  consistency between horizons and clustering (CA L94509-94510). A normalized-law bound cannot recover an omitted
  scalar (917 L370-372).
- C4. Precision: (ST5) at zero source gives Phi(d) = L^4 V_(a,ell) - V_(a,L ell) + R_d with |R_d| <= (C_+ + C_-) L^4
  ell^4 (917 L376-383); this is not Phi = O(L^4 ell^4) without control of the vacuum defect L^4 V_(a,ell) - V_(a,L ell).
- C5. Clause (d)'s n >= 2 restriction is at CA L1746 (917 L345).

**Step 1 status.** Target fixed: (UNIV-K') on every first-passage datum of cutoff > K_0, with pi into first-passage
data. Next: Step 2 fixes Phi, the datum and the seed constant from (SEED-FP) and row 904.

## Step 2. Phi, the datum and the seed (READ row 837, gap-finishline-opus.md L110-150; row 904, gap-univfp-opus.md)

READ gap-finishline-opus.md L114-118: odd L, reference coupling g <= gamma_H, first-passage data (K, beta) with beta in
W_K(g), bare spacing a_K = L^-K in the first-passage unit; Z_(K,T,beta) is the bare Wilson partition function on a torus
of physical side T; the account's sides are ell = 2 L^m >= ell_*(g), so T_ell carries ell/a_K = 2 L^(m+K) sites per side.
READ L126: (SEED-L) is limsup over first-passage data of Phi_L <= phi_*, phi_* < (L/2) log(13/10). READ L126 and SA
L6863-6869 (via row 837): the dilation by L maps Lambda_(K,L ell) onto Lambda_(K+1,ell) with the same weight, so
Phi_L = L^4 F_(K,ell,beta) - F_(K+1,ell,beta). READ L120 (SA L17285, CA-I L2582 via row 837): the integral of rho_k dV_k
equals Z_(K,ell,beta) at every level k <= K, exactly.

**Remark 2.1. PROVED (definitions only).** Let Z^W(N, beta) be the Wilson partition function on the periodic N^4 lattice.
Then Phi(K, beta) = psi(2 L^(m+K), beta) with psi(N, beta) := L^4 log Z^W(N, beta) - log Z^W(L N, beta). So Phi depends on
the datum only through the lattice side N and the bare coupling. (UNIV-K') reads
  sum_(K > K_0) sup_(beta in W_K(g)) |psi(2L^(m+K), beta) - psi(2L^(m+K-1), beta'(K, beta))| < infinity,
where pi(K, beta) = (K - 1, beta'(K, beta)). It is a rate of approach to the continuum limit for one dimensionless,
non-extensive quantity of two tori of fixed physical size: the free-energy defect at one block step.

**Remark 2.2. PROVED (from the exact identity READ above).** Phi(d) = L^4 log M_K(T_ell) - log M_K(T_(L ell)), where
M_K(T) is the total mass of the last-scale density rho_K on the unit lattice of T (ell^4 or L^4 ell^4 unit cells). So
(UNIV-K) is a statement about the last-scale effective theory at the window coupling x_K in (g^-2, g^-2 + B_sharp], with g
small (g <= gamma_H): a cutoff-universality statement for the n = 0 observable log M_K on two fixed unit-cell tori.

**The three parts to attack (set-up; the account's split is read in Step 3).** If the account writes
M_K(T) = e^(E_K(T)) Z^reg_K(T) (1 + Q_K(T)), with E_K(T) the accumulated scalar vacuum factor, Z^reg_K(T) the regular
normalizer on a common final domain, and Q_K(T) >= -1 the relative weight of the complementary (large-field) histories,
then Phi = Phi^vac + Phi^reg + Phi^LF with Phi^vac = L^4 E_K(T_ell) - E_K(T_(L ell)), Phi^reg likewise with log Z^reg,
Phi^LF likewise with log(1 + Q). PROVED (triangle inequality): if each of the three has increments along pi bounded by
(L^4 + 1) eps_K^(i) with sum_K eps_K^(i) < infinity, then (UNIV-K) holds with eps_K = sum_i eps_K^(i). Each part needs
only an extensive density that is common to the two tori at each datum; the extensive parts cancel in Phi.

**Row 904 (READ gap-univfp-opus.md Step 2-3, revision 2bc0658f91d2 of YM4_1400; its line numbers run about 4 above the
ones row 916 uses).** The universality subsection is rts:section ("Universality for bounded ultraviolet profiles at a
fixed horizon"); the ball B_0 has zero first jet and zero companion curvature coefficient, "An input with a nonzero
marginal coefficient is not part of the irrelevant ball"; the frozen frame a_j = X_0 + sum_(l >= j) b_l with all cutoffs
and maps fixed when h_0 or the endpoint varies; the regular trajectory excludes the large-field complementary
operations (HRT opening). Step 3 re-reads these lines in the sa1400 copy and fixes their numbers.

## Step 3. The account's finite-horizon universality, re-read in the sa1400 copy (YM4_1400.tex, 136637 lines)

All lines below are READ in /Users/jonreilly/ym4d-lead/sa1400/YM4_1400.tex (account of Ethan Sussman and Levent Alpoge,
text by Claude and Codex). The numbers agree with rows 916/917 to within one or two lines.

- R1. Scope, L94034-94040: "one finite horizon, one family of regular maps and one frozen cutoff presentation"; the
  comparison "does not compare different horizons or construct an infinite-horizon flow" (L94039-94040).
- R2. The ultraviolet ball, L94052-94057: B_0 = gauge-invariant, hypercubic-covariant, normalized complete pointings,
  "with zero first jet and zero companion curvature coefficient"; "All finite-period versions and their companions are
  included"; a nonzero marginal coefficient is excluded (L94056-94057).
- R3. Radii and constants, L94059-94069: ||h_0|| < R_uv + 2 allowed, estimates on ||h_0|| <= R_uv; ceiling
  H_* >= 2 C_T (R_uv + 2) + 1 + 2 B_n/(1 - q); constants depend on the ball and the rates, "but not on depth, horizon or
  compatible volume" (L94068-94069).
- R4. The frozen frame, L94071-94080: a_j = X_0 + sum_(l=j)^(N-1) b_l, theta_j = a_j, a_N = X_0; "every cutoff,
  fluctuation scaling, gauge normalization and map stays fixed when h_0 or the endpoint is varied".
- R5. Recursion and bounds, L94110-94126: x_(j+1) = x_j - b_j - r_j(x_j, h_j), h_(j+1) = T_j h_j + n_j + f_j(x_j, h_j);
  |r_j| + ||f_j|| <= C e_j, e_j = (log a_j)^m / a_j. L94127-94129: "The scalar coefficients use the infinite companion,
  so the coupling sequence is independent of the torus. Finite-period differences remain in the profiles."
- R6. Tuning, Prop. rts-bounded-UV-tuning, L94131-94145: for each R_uv a floor X_0 independent of N; a unique trajectory
  with h_0 = H, x_N = X_0 + zeta, ||H|| < R_uv + 2, |zeta| < c X_0; holomorphic; ||h_j||_(j,*) <= H_*.
- R7. Prop. rts-exponential-universality, L94364-94381 (statement), proof L94382-94397: H, H~ in the smaller ball, "the
  same endpoint, horizon and frozen presentation"; |x_j(H) - x_j(H~)| <= C e_j q_2^j ||H - H~||_(B_0),
  ||h_j(H) - h_j(H~)||_(j,*) <= C q_2^j ||H - H~||_(B_0); constants "independent of the horizon and compatible volume".
- R8. Finite-volume interaction, L94455-94475: for the same real endpoint X = x_N and a fixed final coarse volume V,
  sup_V |H_N^H(V) - H_N^(H~)(V)| <= C V q_2^N ||H - H~|| (L94465-94468); "The exact regular-step identity of LCF and the
  tuning construction identify these with the actual finite-volume effective interactions of the stated regular integral
  operations" (L94470-94473); "Scalar vacuum factors may differ and do not affect a normalized final law" (L94474-94475).
- R9. The law, L94477-94512: common real final domain D inside the working ball, fixed positive finite measure nu,
  neither depending on the profile; dP_H = Z_H^-1 e^(-X S_N(V) + H_N^H(V)) 1_D(V) dnu(V); the unnormalized ratio and the
  ratio of normalizers lie in [e^-delta, e^delta], delta = C V q_2^N ||H - H~||; TV bound min{1, e^(C V q_2^N ||H-H~||) - 1};
  "not uniform over growing volumes", "neither clustering nor consistency between horizons" (L94508-94510); "No
  complementary-history measure has been introduced in this comparison" (L94511-94512). L94514: END of the file.
- R10. The Gaussian increments depend on the step index. READ L94530-94545 (next subsection, rds:section): for the
  actual regular trajectory, "Write b_j for its Gaussian scalar increment"; "The index in both symbols is the transfer
  from j to j+1"; |b_j - b_inf| + |m_j - b_inf| <= C lambda_0^j, b_inf = (11/(3 pi^2)) log L, 0 < lambda_0 < 1.

**What (U2) is (ARGUED from R1-R9).** It compares two bare weights on ONE bare lattice: Wilson at the retuned bare
coupling x_0(H) plus an irrelevant analytic profile H, run through the SAME N regular steps with the same maps, to the same
endpoint. It is universality in the bare action at a fixed cutoff, not across cutoffs.

**Observation 3.1 (the frames at horizons K and K - 1 differ). ARGUED from R4 and R10.** The step-j data b_j, m_j are
indexed from the bare end (R10: they converge as j grows, at rate lambda_0^j). The horizon-K frame is
a_j^(K) = X_0 + sum_(l=j)^(K-1) b_l. Shifting d's run by one step (steps 1..K-1) uses b_1, ..., b_(K-1); the run of
pi(d) at horizon K - 1 uses b_0, ..., b_(K-2). These agree only up to C lambda_0^j at step j. So "the same frozen
presentation" (R7) does not hold for the shifted run of d and the run of pi(d), even with matched endpoints. Row 916's
use of R7 needs either (a) a re-run of d's one-step output in the horizon-(K-1) presentation, or (b) a comparison
of two runs whose maps differ by O(lambda_0^j) at step j. The account states neither (R1: "does not compare different
horizons").

## Step 4. The regular part

Further lines READ for this step: the exact linear system with step sources (L94196-94236), its kernels and Green
envelopes (L94238-94280), the general source bound (L94288-94313), the weighted initial-profile response
(L94315-94357), the endpoint jets (L94424-94453).

- R11. L94196-94212: u_(j+1) = A_j u_j - R_j v_j + sigma_j, v_(j+1) = D_j v_j + F_j u_j + tau_j, u_N = xi, v_0 = eta;
  |A_j - 1|, ||F_j|| <= C k_j, ||R_j|| <= C e_j, ||D_j|| <= q_1. L94219-94236: P_(jl) = prod_(t=j)^l A_t^-1 with
  |P_(jl)| <= C, U_(ji) = D_(j-1)...D_(i+1) with ||U_(ji)|| <= q_1^(j-1-i), and the exact mixed factorization
  u = u^0 + B v, v = v^0 + K u, u^0_j = P_(j,N-1) xi - sum_(l>=j) P_(jl) sigma_l, v^0_j = D_(j-1)...D_0 eta +
  sum_(i<j) U_(ji) tau_i, (Bv)_j = sum_(l>=j) P_(jl) R_l v_l, (Ku)_j = sum_(i<j) U_(ji) F_i u_i.
- R12. L94288-94296: the general source bound, ||u||_inf <= C{|xi| + sum|sigma_i| + e_0||eta|| + sum e_(i+1)||tau_i||},
  ||v_j|| <= q_1^j ||eta|| + C k_j ||u||_inf + sum_(i<j) q_1^(j-1-i) ||tau_i||. L94311-94313: "No symmetric exponential
  bound for an arbitrary scale impulse is claimed."
- R13. L94450-94453: the endpoint jets "are derivatives of the single presentation ... They do not differentiate a
  sharp cutoff or replace its reference frame by one recomputed from the moving endpoint."
- R14. L94101: a_l >= c X_0 on the frame; with e_j = (log a_j)^m / a_j decreasing for large argument, e_l <= e_*/c and
  k_l = e_l/a_l <= e_*/(c^2 X_0) (ARGUED from R14 and the definition L94082-94083; uses only a_l >= c X_0 large).

**Lemma 4.1 (two tori, one horizon). PROVED from R5, R7-R9.** Let H, H~ lie in the smaller ball, with the same endpoint
X, horizon N and frozen presentation, and let D_T, nu_T be common final domains and measures on T = T_ell, T_(L ell)
(unit-cell volumes V = ell^4, L^4 ell^4). Put Phi^reg_H = L^4 log Z_H(T_ell) - log Z_H(T_(L ell)), Z_H(T) the R9 normalizer.
Then |Phi^reg_H - Phi^reg_(H~)| <= 2 C L^4 ell^4 q_2^N ||H - H~||.
Proof. R5: the coupling sequence, hence X, is the same on both tori. R8-R9 on each torus: |log Z_H(T) - log Z_(H~)(T)|
<= C V_T q_2^N ||H - H~|| (C2 of Step 1). Add L^4 times the T_ell bound to the T_(L ell) bound. QED

**Finding 4.2 (row 916's derivation of the regular part does not go through as written). ARGUED from R1, R4, R7, R10.**
Row 916 applied R7 to H = h_1 (d's profile after one block step) against H~ = 0 (the bare Wilson weight of pi d), at
horizon K - 1. R7 asks for the SAME frozen presentation. d's steps 1..K-1 use the step data b_1, ..., b_(K-1) and the
frame a_j^(K); pi d's steps 0..K-2 use b_0, ..., b_(K-2) and the frame a_j^(K-1). By Observation 3.1 these differ at
relabelled step j by O(lambda_0^j) (R10), not by zero. R1 and R13 exclude horizon and frame changes. So the account's
statement compares bare actions at ONE cutoff; it does not by itself compare consecutive cutoffs. The geometric rate is
still the right expectation; Proposition 4.3 below supplies the missing linear estimate.

**Proposition 4.3 (exponentially decaying step sources). PROVED from R11 and R14.** Fix q_3 with
max(q_1, lambda_0) < q_3 < 1. In the system of R11 take xi = 0, ||eta|| <= R, |sigma_j| <= s lambda_0^j,
||tau_j|| <= t lambda_0^j. After a floor increase depending only on q_1, q_3, lambda_0 and the constants of R11, every
solution has, for all j <= N and with C independent of N,
  |u_j| <= C (s + R + t) q_3^j,      ||v_j|| <= C (R + t + s) q_3^j.
Proof. Norms ||u||_E3 = max_j q_3^-j |u_j|, ||v||_Q3 = max_j q_3^-j ||v_j||. (i) |u^0_j| <= C s sum_(l>=j) lambda_0^l
<= C s q_3^j/(1 - lambda_0). (ii) ||v^0_j|| <= q_1^j R + t sum_(i<j) q_1^(j-1-i) lambda_0^i <= q_1^j R + t j mu^(j-1),
mu = max(q_1, lambda_0) < q_3, and j mu^(j-1) <= C_mu q_3^j; so ||v^0||_Q3 <= R + C t. (iii) |(Bv)_j| <=
C sum_(l>=j) e_l q_3^l ||v||_Q3 <= C (e_*/c) q_3^j ||v||_Q3/(1 - q_3) (R14). (iv) ||(Ku)_j|| <= C sum_(i<j)
q_1^(j-1-i) k_i q_3^i ||u||_E3 <= C k-bar q_3^j ||u||_E3/(q_3 - q_1), k-bar = e_*/(c^2 X_0). (v) The loop constant
theta_3 = C^2 (e_*/c) k-bar/((1 - q_3)(q_3 - q_1)) tends to 0 as X_0 grows (e_* k-bar = O((log X_0)^(2m)/X_0^2)); take the
floor with theta_3 <= 1/2. Then ||u||_E3 <= 2(||u^0||_E3 + C e_* ||v^0||_Q3/(c(1 - q_3))) and
||v||_Q3 <= ||v^0||_Q3 + C k-bar ||u||_E3/(q_3 - q_1). Insert (i), (ii). QED
(The account's R12 is the unweighted form; R12's remark that no symmetric bound holds for an ARBITRARY impulse is
consistent: the sources here decay in the scale index.)

**Proposition 4.4 (two runs whose maps differ by decaying amounts). PROVED GIVEN (MAPCONV) and (CLASS).** Let run A be
d's own regular trajectory from step 1 (initial profile h_1^d, ||h_1^d|| <= H_* by R6) and run B the regular trajectory of
pi d from step 0 (profile 0), relabelled so that step j of B and step j + 1 of A act on the same lattice (both have cells of
side L^(j+1-K) in the first-passage unit). Assume
 (MAPCONV) on common fixed domains, |b^A_j - b^B_j| + sup|r^A_j - r^B_j| <= s lambda_0^j and
   ||T^A_j - T^B_j|| H_* + ||n^A_j - n^B_j|| + sup||f^A_j - f^B_j|| <= t lambda_0^j, with the adapted norms of the two
   runs equivalent at each step with constants independent of j and K;
 (CLASS) the interpolated maps M^B_j + s'(M^A_j - M^B_j), s' in [0,1], satisfy the bounds R5 and ||T_j|| <= q, so that R6
   holds along the segment;
and the same endpoint X. Then ||h^A_(N) - h^B_(N)|| <= C (H_* + s + t) q_3^N with N = K - 1, and by R8-R9 and Lemma 4.1's
argument, |Phi^reg(d) - Phi^reg(pi d)| <= 2 C L^4 ell^4 (H_* + s + t) q_3^(K-1).
Proof. Under (CLASS), R6 gives a holomorphic family of tuned trajectories in s'. Its s'-derivative solves R11 with
xi = 0, eta = h_1^d (only at s' where the initial data is interpolated as well), sigma_j = -(b^A_j - b^B_j) -
(r^A_j - r^B_j)(x_j, h_j), tau_j = (T^A_j - T^B_j) h_j + (n^A_j - n^B_j) + (f^A_j - f^B_j)(x_j, h_j). (MAPCONV) and
||h_j|| <= H_* give the source bounds of Proposition 4.3. Integrate over s' in [0, 1], as in the proof of R7 (L94382-94397).
QED. (CLASS) is ARGUED: R6's proof (L94146-94184) uses only R5's bounds and the contraction; I did not check every
formation constant it calls.

**Corollary 4.5 (regular part of (UNIV-K)). PROVED GIVEN (MAPCONV), (CLASS) and endpoint matching.** With pi(d) =
(K - 1, beta'), beta' the run-B bare coupling tuned (R6, H = 0) to d's endpoint X = x_K(beta), the regular parts satisfy
(UNIV-K) with eps_K^reg <= 2 C ell^4 (H_* + s + t) q_3^(K-1), and E^reg(K_0) <= 2 C ell^4 (H_* + s + t) q_3^(K_0)/(q_3(1 - q_3)).

**What the account does and does not supply for the regular part (READ).** It supplies R5-R12: one-horizon tuning,
one-horizon universality, the exact linear inverse with sources, and b_j, m_j -> b_inf at rate lambda_0^j (R10). It does
not supply (MAPCONV) for r_j, T_j, n_j, f_j or for the adapted norms, and it excludes frame changes (R13). Open sub-items:
(MAPCONV); (CLASS) in full; whether beta' lies in W_(K-1)(g) (edge matching; by 917 the base set may be taken as the image
of the chains at K_0, so this affects only which data carry the seed).

Erratum to the proof of Proposition 4.4 (wording only): interpolate the initial profile as s' h_1^d together with the
maps, so eta = h_1^d in R11. The radii are fixed in this order: H_*^0 = the HRT ceiling of d's own run (h_0 = 0); then
R_uv := C_eq H_*^0 (C_eq the assumed norm equivalence of (MAPCONV)); then H_*(R_uv) and the floor X_0(R_uv) by R3, R6.
No circularity.

## Step 5a. The account's density representation (Proposition large-field-2-1), READ L61903-61945

The core is due to Balaban (READ L61945: CMP 119 (1988) 243, Theorem 1 and Corollary 3, with CMP 122 (1989) 175 and 355).
- R15. L61905: regular expansion needs plaquettes within eps_k eta_k^2 of 1, eps_k = g_k p_0(g_k); failed tests store the
  fields and supply e^(-c x_k eps_k^2) = e^(-c p_0(g_k)^2); "For a failed plaquette test this weight is the Wilson
  weight"; the density is a sum over histories collected by labels S = (Omega_j, Lambda_j, S_j)_(j<=k) with marks.
- R16. L61911 (hypotheses): primitive step hypotheses H_step; torus admissible up to level k: ell L^(K-j) >= 2 L^11 M
  R-check_j; g_j <= gamma; lambda_sharp (j - i) - c_5 <= x_i - x_j <= B_sharp (j - i); provided for first-passage data.
- R17. L61913-61926: rho_k(V_k) = sum_S T'_k(S)[chi_(k,S) exp A_(k,S)(U_k(V))],
  A_(k,S) = -A(x_k(.), U) + E_k + R_k + B_k - Ecal_(k,S); ||E^(j)||_(j,kappa) <= E_0, ||R^(j)||_(j,kappa) <= g_j^kappa_0,
  |B^(j)(X, .)| <= B e^(-kappa d^nat_j(S; X)), M(i, X) <= e^(-(2-c') p_0(g_i)); -Ecal_(k,S) is "the constant term of
  the action of the label".
- R18. L61932: "every component C of Z_k keeps a factor e^(-c p_0(g_k) - kappa_1 |C|_k)", kappa_1 "outweighs the number
  C^n of connected sets of n cells that contain a given cell"; "Each term is a non-negative measure"; "Neither E^(j) nor
  R^(j) carries a label index. On non-wrapping domains with matching step data they are the values, at the lifts of the
  domains in those units, of a single family on Z^4. (The constant Ecal_(k,S), by contrast, depends on the label and on
  the torus.)"
- R19. L61934-61941: chi_k e^(-x_k A(U_k(V_k)) - E_- |T^(k)|) <= rho-bar_k; integral of rho-bar_k <= e^(C(1 + log x_k)
  |T^(k)|); integral of rho_k dV_k = Z_(K,ell,beta).
- R20. L61943: the theorem is the case theta = x(beta) of an induction along an arbitrary frame theta, which "runs on all
  admissible tori simultaneously".

**Consequences for (UNIV-K) (ARGUED from R17-R19).**
1. The split of Step 2 is the account's: M_K(T) = sum_S (label term). The all-regular label S = empty carries
   e^(-Ecal_(K,empty)(T)) times the regular integral; Q_K(T) collects the labels S != empty.
2. The local regular terms E^(j), R^(j) are torus-independent on non-wrapping domains with matching step data (R18).
   Between T_ell and T_(L ell) at ONE datum the step data match (one run; R5: the coupling sequence is torus-independent).
   So inside one Phi(d), the non-wrapping parts of E, R cancel exactly between L^4 copies of T_ell and T_(L ell), after
   the cell counts are matched. What remains of E, R in Phi(d) is their wrapping part.
3. The scalar Ecal_(K,S) is stated to depend on the torus, with no stated split into a bulk density and a wrapping
   remainder in these lines. R19's bounds are e^(O(|T^(k)|)): extensive, so they bound Phi only by O(L^4 ell^4).
4. R17's polymer norms ||.||_(j,kappa) and the factor e^(-kappa_1 |C|_k) are the account's tools for a wrapping bound;
   whether ||.||_(j,kappa) weights a polymer by e^(kappa d_j(X)) must be read (next step).

## Step 5b. Missing part A: scalar vacuum factors on the two fixed tori

Further lines READ: C2 (L2320-2331), the vacuum-transfer remark (L2636-2649), and the account's "local companion
criterion for vacuum-density compatibility" (L102529-102592), with its index entry (L136062).
- R21. L2328-2330 (C2): "Use the companion identities on non-wrapping domains in matching step units. Other carriers
  enter the torus estimates with their winding retained."
- R22. L2643-2649: "Compatible local counterterms, the floor and vacuum-density comparison give one sufficient route. The
  local companion criterion in (ET8)-(ET10) proves that vacuum comparison from explicit nonwrapping and normalization
  data".
- R23. L102538-102555, (ET8): with a_j = L^(j-K), if the vacuum constant has the form
  E_(ell,K) = sum_(j=0)^K [(ell/a_j)^4 c_(j,K) + sum_z sum_(D in D_(ell,j)(z)) v_(ell,j)(D, z)], where c_(j,K), the
  coupling sequence and every auxiliary choice are the same for all ell; there is a translation-covariant infinite
  companion v_(inf,j); domain entropy <= C_D e^(kappa_D m), |v| <= C_E e^(-kappa_E m), kappa_E > kappa_D, uniformly in
  j, K, ell; and rooted domains with m < ell/(C_0 a_j) correspond bijectively to companion domains with equal values
  ("an explicit locality and nonwrapping assumption").
- R24. L102557-102579, (ET9)-(ET10): then |ell^-4 E_(ell,K) - A_K| <= C sum_j a_j^-4 e^(-c ell/a_j) <= C_(ell_0) e^(-c ell/2)
  for ell >= ell_0, independently of K, with A_K = sum_j a_j^-4 (c_(j,K) + v-bar_j); "The divergent common number A_K
  need not converge as the cutoff is removed; it cancels exactly in the comparison."
- R25. L102586-102589: "If the coupling sequence or local normalizer numbers differ between tori, or if nonwrapping
  compatibility has not been established for the actual formation rule, (ET9) has not been proved for that construction."
- R26. L136062: E_(ell,K) is the "finite-torus vacuum constant" of the finite-reference route.

**Lemma 5.1 (the vacuum part is uniformly small under the account's criterion). PROVED GIVEN (ET8) for the vacuum
scalar that enters M_K (hypothesis VAC-ID below), from R24.** For every first-passage datum d,
|Phi^vac(d)| <= 2 C C_(ell_0) L^4 ell^4 e^(-c ell/2), uniformly in K.
Proof. Write W_T(d) = E_(T,K) - vol(T) A_K. R24 gives |W_(T_ell)| <= C C_(ell_0) ell^4 e^(-c ell/2) and |W_(T_(L ell))|
<= C C_(ell_0) L^4 ell^4 e^(-c L ell/2). Since vol(T_(L ell)) = L^4 vol(T_ell), the A_K terms cancel in
Phi^vac = L^4 E_(ell,K) - E_(L ell,K) (with either sign convention for the scalar). So |Phi^vac| <= L^4 |W_(T_ell)| +
|W_(T_(L ell))|. QED

**Lemma 5.2 (a uniformly small part need not have summable increments). PROVED.** Suppose Phi = P + Q on first-passage
data, with sup |Q| <= eta and P satisfying (UNIV-K') along pi with sum E(K_0). If Phi(d_0) <= phi_* - (L^4+1) E(K_0) -
2 eta for every datum d_0 of cutoff K_0, then Phi(d) <= phi_* for every first-passage datum d with K >= K_0.
Proof. Phi(d) <= P(d) + eta <= P(pi^(K-K_0) d) + (L^4+1) E(K_0) + eta <= Phi(pi^(K-K_0) d) + 2 eta + (L^4+1) E(K_0). QED
So for the use of (ONE-K), Lemma 5.1 makes the literal increments of Phi^vac unnecessary: they cost 2 eta_vac,
eta_vac = 2 C C_(ell_0) L^4 ell^4 e^(-c ell/2), in the base margin. This is a corrected form of (ONE-K), not (UNIV-K).

**Lemma 5.3 (literal increments of the vacuum part). PROVED GIVEN (ET8), (VAC-LIP) and the trajectory comparison of
Proposition 4.4.** (VAC-LIP): each wrapping term w_(T,j) := sum_z sum_D [v_(T,j)(D,z) - v_(inf,j)(D,z)] (the terms not
matched by R23's bijection) is a holomorphic function of the step-j data on the common domains, with
|w_(T,j)| <= C (vol(T)/a_j^4) e^(-c ell_T/a_j) there (ell_T the side of T). Then
|Phi^vac(d) - Phi^vac(pi d)| <= C' (L^4 + 1) L^4 ell^4 q_3^K, summable.
Proof. Bulk terms (vol/a_j^4)(c_(j,K) + v-bar_j) cancel inside each Phi (R23: the same for all ell). Step j + 1 of d and
step j of pi d act on the same lattice (Proposition 4.4). Cauchy on a fixed inner margin turns (VAC-LIP) into a Lipschitz
constant C (vol/a_j^4) e^(-c ell_T/a_j); Proposition 4.4 bounds the step-data differences by C q_3^j. The extra step 0 of
d contributes at most C vol a_0^-4 e^(-c ell_T/a_0) <= C vol L^(4K) e^(-c ell L^K). With b = K - j, the sum is
<= C vol q_3^K sum_b L^(4b) e^(-c ell L^b) q_3^-b, and the b-series converges (superexponential decay). QED

**Disposition of part A.**
- (VAC-ID), OPEN as an account statement: the scalar that enters the total mass M_K(T) (R17's -Ecal_(K,S), summed with
  the label weights) has the (ET8) form with R23's locality and nonwrapping hypotheses, uniformly in K and ell. The account
  states (ET8)-(ET10) as a criterion (R22), says Ecal_(k,S) "depends on the label and on the torus" (R18), and says (ET9)
  is not proved for a construction whose nonwrapping compatibility is not established (R25). It states the nonwrapping
  identity for E^(j), R^(j) (R18), not for Ecal.
- What part A does NOT need: convergence of A_K (R24: it cancels); uniformity in the volume (both tori are fixed).
- Size check (ARGUED): eta_vac is far below the margin when ell is large, since ell >= ell_*(g) and the seed needs ell above
  the correlation length; but c, C, C_(ell_0) are not explicit in R24, so no numerical margin is claimed.

## Step 6. Missing part B: large-field (complementary) histories

Further lines READ: L94019-94025, L95023-95025, L3520-3523, L72866-72892 (the class C_k(theta)), L1110-1118 and
L2334-2340 (the threshold p_0 and the rarity statement C3).
- R27. L94019-94025: the regular construction "is a coupling and profile trajectory, not a bound for the mass or source
  moments of all complementary histories. Those quantities require the positive history estimates used in the full
  construction." R28. L95023-95025: complementary-history insertions "require their own source and mass estimates".
  R29. L3520-3523: the continuum statements "also require the stated estimates for complementary histories".
- R30. L72870-72892 (the class C_k(theta)): every coupling-dependent choice of level j is made with the frame theta_j
  ("the tests, the regions, the histories, the domains of analyticity and the measures of the integral operations depend
  on theta only, and on no entry of the density"); an element is an array "specified simultaneously on every admissible
  torus and cutoff"; clause (i) the tube |theta_j - x_j| <= t_j ~ c theta_j (log theta_j)^-C; clause (v) coherence:
  "This single clause contains locality in the history, covariance under translations and independence of the torus";
  clause (vii) every term with its stored variables is a non-negative measure.
- R31. L1115: p_0(g) = A_0 (log g^-2)^(p_0-exponent), with exponent p_0 > p_1 (L1118). L2335-2340 (C3): a created component
  X at level j has mass <= exp[-c p_0(g_j) - kappa |X|_j], kappa above the entropy rate. R17: M(i, X) <= e^(-(2-c') p_0(g_i)).

**Finding 6.1 (no comparison of two history sums is stated). READ R9 (L94511-94512), R27, R28.** Every history estimate
in the lines read is a bound for ONE presentation (R17-R18, R30, R31). None compares the history sums of two runs, of two
bare weights, or of two cutoffs.

**Finding 6.2 (the all-regular split does not isolate the large-field part). ARGUED.** At the bare level of d,
g_0^-2 = theta_0 ~ beta ~ g^-2 + c_0 K (READ CA L1755 via row 916). A failed bare plaquette test has probability about
e^(-c p_0(g_0)^2) (Gaussian tail at the threshold eps_0 = g_0 p_0(g_0), R15; heuristic lower bound, not proved here),
i.e. exp(-c A_0^2 (log(c_0 K))^(2 p_0-exponent)). A final unit cell holds L^(4K) bare cells. So the expected number of
bare-level components per unit cell grows without bound in K, and the all-regular label S = empty carries a share of
M_K(T) that tends to 0. Then log(1 + Q_K(T)) is dominated by an extensive part, and its non-extensive part is a property
of the unit-scale integral (the crux), which no account statement controls (R19 is e^(O(|T|))). So neither Lemma 5.2
(uniform smallness) nor an increment bound for Phi^LF can come from the split of Step 2 with one-presentation bounds.
The large-field part must be compared together with the regular part, level by level.

**Statement 6.3 (DENS-K), the exact missing statement for parts A and B together.** For every first-passage datum d of
cutoff K > K_0, with pi(d) = (K - 1, beta') of matched endpoint, and with matched frames theta^(pi d)_j = theta^d_(j+1)
(allowed by R20 and R30(i) when the two coupling sequences lie in each other's tubes): on each T in {T_ell, T_(L ell)}
let rho~^d_T(V) be the final density of d on the unit-lattice field V with all stored variables integrated, and
rho~^(pi d)_T(V) that of pi d. There are one real c_d (for both tori) and delta_K >= 0 with sum_K delta_K < infinity, such
that, as measures in V,
   e^(c_d vol(T) - delta_K) rho~^(pi d)_T <= rho~^d_T <= e^(c_d vol(T) + delta_K) rho~^(pi d)_T.
(Equivalently, by the exact identity R19 for both runs: the unit-scale block marginals of the two bare Wilson measures,
taken with the matched block kernels, have log-ratio c_d vol(T) + O(delta_K) uniformly in V.)

**Lemma 6.4. PROVED.** (DENS-K) implies (UNIV-K) with eps_K = delta_K and the same pi.
Proof. Integrate over V (R19: the total mass of rho~ is Z): |F_d(T) - F_(pi d)(T) - c_d vol(T)| <= delta_K on both tori.
That is clause (ii) of (UNIV-K) (Step 1). QED

**What (DENS-K) contains, part by part (ARGUED; each item is a statement the account does not make).**
- B1 (the extra finest level of d). d's level-0 islands and drop-outs have no counterpart in pi d. Needed: after
  integrating them, their effect on rho~^d is e^(constant x vol) times a factor e^(O(delta_K)). Heuristic power count (not a
  proof): a bare-level component of mass <= e^(-c p_0(g_0)) (R31) shifts the unit-scale action by a marginal term of
  relative size O(e^(-c p_0(g_0))) per unit cell plus irrelevant terms smaller by powers of L^-2K. The marginal shift is
  summable in K exactly when sum_K exp(-c A_0 (log(c_0 K))^(p_0-exponent)) < infinity, i.e. if the exponent is > 1, or
  equal to 1 with c A_0 > 1 (PROVED as arithmetic; the exponent's value was not read).
- B2 (matched levels). For j >= 1, d's level-j and pi d's level-(j-1) island and boundary terms (B^(j), Phi_omega, Ecal)
  act on the same unit cells with the same theta but on fine lattices of spacing L^-K and L^-(K-1) (R17: the background
  U_k(V) lives on the fine lattice). Needed: their difference is summable, which is the large-field analogue of
  (MAPCONV) plus a contraction of the history response (the analogue of R7 for the full class).
- B3 (regular and vacuum parts). Proposition 4.4 and Lemma 5.3 give these, under (MAPCONV), (CLASS), (VAC-ID), (VAC-LIP).

## Step 7. Fact tests

(UNIV-K) is a convergence statement along the first-passage chain. Through (ONE-K) it moves the seed to one cutoff; it
does not supply a seed or a gap. So the tests bear on where the group enters each result here.

- **U(1) in its Coulomb phase (row 786).** (a) The first-passage chain needs a running coupling. For U(1) the one-loop
  increment vanishes (the account's b_inf = (11/(3 pi^2)) log L, R10, is the SU(2) value), x_k(beta) does not fall to
  the window, and W_K(g) is empty for K >= 1 (ARGUED). (UNIV-K) and (ONE-K) are then vacuous and claim nothing. (b) The
  only estimate proved here from the account, Proposition 4.3, uses |P_(jl)| <= C (READ L94221-94222), which rests on
  sum_j k_j < infinity (READ L94086-94088, from a_j ~ X_0 + N - j, L94085): the coupling grows linearly toward the bare end.
  That is asymptotic freedom. At a fixed U(1) coupling a_j is constant, sum_(j<N) k_j grows like N, and the bound on P
  fails (ARGUED). (c) A convergent Phi is consistent with no gap: by Lemma Z' (row 720, checked row 727, READ via
  gap-finishline-opus.md L130) Phi_rho >= (rho/2) log(1 + S) >= 0, and S is not small without a gap; so the base seed
  fails for U(1) even if a U(1) analogue of (UNIV-K) held (ARGUED). Nothing here contradicts row 786.
- **Q_8 and 2T (rows 838, 843).** Finite groups have no continuous field, no Gaussian increment b_j and no regular
  trajectory; the account's system R5/R11 does not exist for them, and the first-passage chain is empty (ARGUED). No result
  here passes for them; the group enters through the account's SU(2) trajectory, as the test asks.
- **Dobrushin caps 2/3 and 0.775, layer twist bound 4 G_3 = 1.0109 (row 839), (AN1) (row 845).** No single-site,
  vertex-block, layer-twist or annealed bound is used anywhere in this file. Not applicable.
- **Order-one window (bare beta_W about 2.3 to 2.6).** This file works at the account's first-passage scale with g <=
  gamma_H small (READ gap-finishline-opus.md L114). It says nothing about the order-one window; the crux stays at the base
  seed, as row 916 and row 913 said (READ gap-chain-ce-opus.md L344-347).

## Step 8. Status, errata and result

**Line-number errata (re-checked by grep in the sa1400 copy).** R14 and Proposition 4.3: a_l >= c X_0 is at L94103-94104
(not L94101). Step 7: |P_(jl)| <= C and the U bound are at L94224-94227 (not L94221-94222); the HRT envelope
a_j ~ X_0 + N - j is at L94085-94086 and (rts:weight-sums) at L94087-94091. Step 7: Lemma Z' is used at
gap-finishline-opus.md L132 (table entry L102), not L130; row 916's "not the crux" sentence is at gap-chain-ce-opus.md
L353-354, not L344-347. The statements are unchanged.

| Statement | Mark |
|---|---|
| Lemma 1.1: on the two fixed tori, (UNIV-K) holds iff sum_K sup_d abs(Phi(d) - Phi(pi d)) < infinity (UNIV-K'); c_d is free | PROVED (also stated by check 917) |
| (ONE-K) with 917's base-set quantifier: base bound on every datum of cutoff K_0 gives Phi <= phi_* for all K >= K_0 | PROVED (row 916's algebra, re-checked) |
| Remarks 2.1-2.2: Phi(K, beta) = psi(2L^(m+K), beta); Phi is a function of the last-scale total masses on ell^4 and L^4 ell^4 unit cells | PROVED from READ identities (row 837 L120, L126) |
| Lemma 4.1: at one horizon and one presentation, abs(Phi^reg_H - Phi^reg_H~) <= 2 C L^4 ell^4 q_2^N norm(H - H~) | PROVED from READ L94127-94129, L94364-94381, L94455-94512 |
| Finding 4.2: row 916's use of the finite-horizon universality for consecutive cutoffs needs "the same frozen presentation", which fails: the Gaussian increments b_j depend on the step index (L94540-94545), so d's steps 1..K-1 and pi d's steps 0..K-2 differ by O(lambda_0^j) | ARGUED from READ L94034-94040, L94071-94080, L94364-94368, L94450-94453, L94530-94545 |
| Proposition 4.3: in the account's exact linear system, step sources of size O(lambda_0^j) and an initial profile R give responses O((R + s + t) q_3^j), max(q_1, lambda_0) < q_3 < 1, uniformly in the horizon | PROVED from READ L94196-94236, L94085-94104 (one floor increase) |
| Proposition 4.4, Corollary 4.5: regular part of (UNIV-K) with eps_K^reg <= 2 C ell^4 (H_* + s + t) q_3^(K-1), summable | PROVED GIVEN (MAPCONV), (CLASS) and endpoint matching |
| (MAPCONV): the regular step maps r_j, T_j, n_j, f_j and the adapted norms of d's step j+1 and pi d's step j differ by O(lambda_0^j) | OPEN (the account states it for b_j, m_j only, L94540-94545, and excludes frame changes, L94450-94453) |
| (CLASS): the interpolated maps stay in the class used by the tuning proposition | ARGUED (L94146-94184 use only the stated bounds); not checked in full |
| Edge matching: beta' in W_(K-1)(g) | OPEN; by 917 the base set can be the image of the chains at K_0 |
| Lemma 5.1: under the account's own (ET8) form, abs(Phi^vac) <= 2 C C_(ell_0) L^4 ell^4 e^(-c ell/2), uniformly in K | PROVED GIVEN (VAC-ID), from READ L102538-102579 (the account's local companion criterion) |
| Lemma 5.2: a uniformly bounded part need not have summable increments; it costs 2 eta in the base margin | PROVED |
| Lemma 5.3: literal vacuum increments summable, eps_K^vac <= C q_3^K | PROVED GIVEN (ET8), (VAC-LIP) and Proposition 4.4's hypotheses |
| (VAC-ID): the scalar that enters M_K (Ecal_(K,S)) has the (ET8) form with its locality and nonwrapping hypotheses | OPEN (the account: Ecal "depends on the label and on the torus", L61932; (ET9) not proved without nonwrapping compatibility, L102586-102589) |
| Finding 6.1: no account statement compares the history sums of two runs | READ L94511-94512, L94019-94025, L95023-95025 |
| Finding 6.2: bare-level large-field components are dense per unit cell as K grows, so the all-regular split cannot isolate the large-field part | ARGUED (Gaussian-tail lower bound heuristic) |
| Statement 6.3 (DENS-K): matched-level comparison of the full final densities, e^(c_d vol +- delta_K), sum delta_K < infinity | the exact missing statement for parts A and B together; OPEN |
| Lemma 6.4: (DENS-K) implies (UNIV-K) with eps_K = delta_K | PROVED |
| B1: summability of the bare-level marginal shift iff sum_K exp(-c A_0 (log(c_0 K))^p0) < infinity (exponent > 1, or = 1 with c A_0 > 1) | the arithmetic PROVED; the power count ARGUED (heuristic); the exponent's value not read |
| B2: matched-level island and boundary terms differ by a summable amount | OPEN |
| (UNIV-K) | OPEN |
| Fact tests | pass as stated in Step 7 (ARGUED): the only account estimate used rests on asymptotic freedom (L94085-94091, L94224-94227) |

**Not done, not verified.** No proof inside the account was checked line by line; only statements at the lines named.
Lemma FL (row 837) is not re-checked. The value of the threshold exponent of p_0 was not read. No numeric run was made
(no GUIDE item). No other model has checked this file.

**What changed against rows 916 and 917.** Row 916 ARGUED the regular part from the finite-horizon universality; here
that theorem is shown not to apply as stated to consecutive cutoffs (Finding 4.2), and the missing estimate is supplied
in linear form (Proposition 4.3, PROVED) up to one named hypothesis (MAPCONV). For the vacuum factors the account's own
local companion criterion (L102529-102592) gives uniform smallness under its (ET8) hypothesis, and Lemma 5.2 shows that
uniform smallness is enough for (ONE-K) at a cost 2 eta_vac in the margin. For the large-field histories the exact missing
statement is (DENS-K), with its two large-field parts B1, B2 named.

RESULT: (UNIV-K) remains OPEN. PROVED: on the two fixed tori (UNIV-K) is exactly uniformly summable increments of Phi (Lemma 1.1); (ONE-K) with 917's base quantifier; a uniformly bounded part of Phi costs only 2 eta in the base margin (Lemma 5.2); in the account's exact regular linear system (YM4_1400 L94196-94236, Ethan Sussman and Levent Alpoge, text by Claude and Codex), step sources decaying like lambda_0^j give responses O(q_3^j) uniformly in the horizon (Proposition 4.3); (DENS-K) implies (UNIV-K) (Lemma 6.4). ARGUED: the finite-horizon universality L94364-94381 does not by itself compare consecutive cutoffs, since b_j depends on the step index (L94540-94545), so row 916's regular-part derivation needs (MAPCONV). PROVED GIVEN hypotheses: regular part summable, eps_K <= C ell^4 q_3^K, given (MAPCONV), (CLASS) and endpoint matching; vacuum part uniformly below 2 C C_(ell_0) L^4 ell^4 e^(-c ell/2) given the account's own (ET8) form (L102538-102579), and summable given also (VAC-LIP). OPEN: (MAPCONV); (VAC-ID) (the account says Ecal depends on the label and torus, L61932, and (ET9) is unproved without nonwrapping compatibility, L102586-102589); the large-field histories, stated exactly as (DENS-K) parts B1 (the extra bare level of d) and B2 (matched-level island terms), with no account comparison of two history sums (L94511-94512, L94019-94025).
