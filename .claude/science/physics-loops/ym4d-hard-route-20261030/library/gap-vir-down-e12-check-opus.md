# Check of rows 1631 (E1) and 1632 (E2), VIR-DOWN line (row 1634)

Checker: Claude Opus 5.5 (laptop subagent, row 1634). Files checked: `library/gap-vir-down-e1-astra62.md` (row 1631, 178 lines) and `library/gap-vir-down-e2-astra62.md` (row 1632, 210 lines), both by gpt-6.2-astra max. Checked by hand, line by line. I did not read `library/gap-vir-down-e2-neon.md`.

## 0. Reading log

- FINISH.md rows 1630-1634 (briefs and RESULT texts), read in full.
- Check 1630 (`library/gap-vir-down-twoside-check-opus.md`), read in full; sections 1 and 3.3 used for the exact (E1), (E2).
- Registry row VIR-DOWN (`library/open-registry.md` L1028).
- Row 1617 (`library/gap-vir-down-astra62.md`): (5)-(6) with proof (L95-116), (12) and the clamped variant (L207-213), U(1) and 5D paragraphs (L219, L233), spectator test (L235).
- ON FILE inputs used as cited, located but not re-proved: row 1215 vacuum lower bound (`gap-solve23-astra62.md` L277, checked in 1221); row 1143 selected-plaquette count M = 3V - 3 (`gap-solve-astra62.md` L31-37, checked in 1144); row 1161 (19) and m_1 <= C_1 (`gap-solve9-astra62.md` L308, checked in 1162).
- Guide run (floating point, not a proof step): one Python process, a few MB, `g1634/guide.py` in this session's scratchpad (outside the repository). It uses its own Bessel power series. It tests the elementary inequalities used: d log c_k/d beta + 3/(2 beta) >= 0 (minimum 3.8e-5 on the grid), g(j) - g(j-1) > 0, I_(j+1)/I_j <= beta/(2(j+1)), 1 + 128^3 <= 2^32, e^(-1/8) >= 7/8, e^(3/16) - 1 <= 3/13, e^(1/6) - 1 < 1/2, sinh(2m) <= m sinh 2 on (0, 1], and c_I <= I(beta) beta^(3/2). All agree with the hand bounds.

## 1. Row 1631 (E1), line by line

Setup. D_psi = E_w sum_e g_beta(k_e) - <V>_psi with g_beta(k) = k/beta + I_(k+2)/I_(k+1) - 1. I re-derived it: T = MCM, M' = -(V/2)M gives -lambda <V>_psi; the per-link multiplier of C is c_k = 2 e^(-beta) I_(k+1)/beta, whose log derivative is g_beta(k). ||w|| = 1. b_psi = D_psi - D_Omega is the quadratic form of r^(-1) F_r A' F_r, the same b_r as in row 1628 (19). ON FILE (row 710); consistent.

**(1)-(3), large spins in magnetic placement. HOLDS.**
- The full temporal-gauge kernel e^(-beta S) is continuous and strictly positive, so its top eigenvector is positive and simple; it is invariant under gauge and centre maps, so ||T|| = lambda_0 (neutral). HOLDS.
- For a plaquette-separated set S, the x_e-dependence (e in S) factorizes: one temporal factor (coefficient beta) and four spatial plaquettes (beta/2 each) per link, each linear in the quaternion x_e, so the exponent is (1/2) tr(x_e A_e) with |A_e| = s_e <= 3 beta. No spatial plaquette carries two S-links, so the factors separate. HOLDS.
- (3): the spin-k/2 component of e^((s/2) tr(xv)) is (k+1)(2 I_(k+1)(s)/s) chi_(k/2)(xv); |chi| <= k+1; 2I_1(s)/s <= e^s; the factor is >= e^(-s); I_(k+1)/I_1 <= (s/2)^k/(k+1)! term by term ((m+1)!/(m+k+1)! <= 1/(k+1)!). So the ratio is <= (k+1)^2 e^(2s)(s/2)^k/(k+1)! <= A_k. HOLDS.
- |<psi, R T psi>| <= (prod A) <|psi|, T|psi|> <= lambda_0 prod A, and <psi, R T psi> = lambda Pr_psi(labels). So Pr <= e^m prod A. HOLDS (R is a product of commuting projections on distinct links, hence a projection commuting with nothing it needs to).
- Six-colour classes: links of one direction in one (i, j) plaquette differ by one in the transverse parity; even n keeps it periodic. HOLDS.
- Exponential moment: expansion over subsets of H, all terms nonnegative, gives E e^(U_H) <= e^m (1 + B_q)^|H|. For k >= q >= 6 e^2 beta, e^k A_k <= (k+1) e^(6 beta) 4^(-k) <= e^(6 beta) 2^(-k). With the third entry of (1), d B_q <= 2d e^(6 beta) 2^(-q) <= e^(-2 beta) delta a/t. Jensen, sum over six classes, Markov in k: (2). HOLDS.

**(4), cutting the plaquette insertion. HOLDS.**
- Multiplication by a fundamental matrix element moves spin label k to k +- 1, so W_p Q^(q-1) = Q^q W_p Q^(q-1). Then X = W_p - Q^q W_p Q^q vanishes on both sides of Q^(q-1), so <psi, X psi> = <(1-Q^(q-1)) psi, X (1-Q^(q-1)) psi> and |<X>| <= 2 <1 - Q^(q-1)> <= 2 sum_(e in dp) Pr(k_e >= q). Four plaquettes per link; ψ and Omega; m >= a/t at a cold point. The constant 8(6 + 2 delta)/q follows. HOLDS. The bound is linear in the tail probability, as the file says (no Cauchy-Schwarz square root).

**Electric part, row 1617 (6). ON FILE, conditions verified.** Row 1617 (5) needs J >= e^2 beta and J >= (8 beta + log(dt/(a delta)))/log 2; (1) gives both. The clamped variant (row 1617 L213) gives the same two-sided bound with omitted score in [0, k/beta]. Checked in check 1621; I re-read the proof (L109-116): it HOLDS as used.

**(5). HOLDS.** Both per-vector bounds hold for every unit vector of an eigenspace (every such vector is an eigenvector). The cut scores are quadratic forms on the eigenspace (psi -> w is linear), so the basis sum is a trace. Weighted sum gives (5) with W_obs.

**(6). HOLDS.** With delta = 1, the error coefficient is 2/beta + 64/q. On a fixed-depth window beta is of order log n and q >= 6 e^2 beta, so both go to zero; q = O(log n) because t is between two multiples of n. The remarks after (6) are correct: E1 for N is equivalent, up to a vanishing rate error, to E1 for N_q. This is a reduction, not a sign.

**(7), second derivation by Taylor degree. HOLDS.** Degree count: a monomial survives R_S only if q|S| <= 4 sum h_f. ||R_e||_(inf->inf) <= 1 + sum_(k<q) (k+1)^2 <= 1 + q^3. Weighting by 2^(4 sum h - q|S|) gives e^(16 sum alpha); division by the factor costs e^(sum alpha); 17 * 3 = 51. Jensen at theta = (q log 2)/2 gives (7). For q >= 128, 1 + q^3 <= 2^(q/4); with the stated lower bound on q the braced remainder is <= a delta/(4t), and 2/log 2 <= 4 gives (2). HOLDS. Standing: it shares the eigenstate norm comparison (the factor e^m) and the Jensen step with (2); only the kernel bound differs. It is a second derivation of the kernel estimate, not an independent check of (2).

**(8), necessary signed local discrepancy. HOLDS.** Telescoping of the clamped score; increments g(j) - g(j-1) = d/d beta log(I_(j+1)/I_j) > 0 (row 1617 (12), Bessel moment identity of row 843; guide agrees); A_M + sum c_j A_j <= (1 + sum c_j) max holds for any signs. W_t >= W_obs >= S_o a/t. g(q) - g(0) <= q/beta + 1 holds directly (the ratio terms are in (0, 1)). With d = 3n^3, t of order n and q/beta bounded, the bound is of order n^(-4). Standing: (8) is a consequence of E1. It proves nothing about Wilson eigenstates; it names the size a positive signal must have.

**Coherence example. HOLDS.** int chi_p = 0, int chi_p^2 = 1, int chi_p^3 = 0 (one-link sign flip); <W_p>_(phi_+-) = +-1/2; all joint spin probabilities agree. Trial vectors only, as stated.

**Comparison laws. ON FILE** (rows 1618, 1626, 1628 (22), check 1630 3.1). Not re-checked beyond agreement with check 1630.

**Scope (cosine U(1), 5D SU(2)). HOLDS.** U(1): the Fourier projection onto |j| = k has kernel bounded by 2; the cosine plaquette moves each charge by one; I_k/I_0 <= (s/2)^k/k!. 5D: s_e <= beta + 6 beta/2 = 4 beta, eight colours, factor 12 in (4). I re-derived each count.

**Spectator. HOLDS.** Observed data and W_obs are those of the Wilson factor; product coldness implies Wilson coldness; oscillator purity (1 - x)/(1 + x) < 1/3 at x = e^(-1/512). Same test as row 1617 L235 (rows 998, 1553, 1573).

Row 1631 verdict: every PROVED item HOLDS. No line fails. No correction needed.

## 2. Row 1632 (E2), line by line

Setup. b_r = r^(-1) F_r A' F_r with A = T/lambda_0 gives b_psi = D_psi - D_0, the same form as row 1631. D_r = ran F_r cap ker E is the orthogonal complement of F_r(ran E) in ran F_r. HOLDS. Raw slab kernel e^(-beta S) with S = temporal actions + half of each boundary spatial action; this is the same T = MCM. Consistent.

**(1). ON FILE** (row 1215, checked 1221). 0 <= L because lambda_0 <= ||M||^2 ||C|| = I^d.

**(2). HOLDS.** With y = beta(1 - x) in the integral for I_(k+1), (1 - x^2) = (y/beta)(2 - y/beta) and dx = dy/beta, so c_k is beta^(-3/2) K_k times int e^(-y) y^p (2 - y/beta)_+^p dy, p = k + 1/2. The integrand increases in beta. I re-derived the powers of beta. Guide agrees (the bound is sharp as beta -> infinity at k = 0).

**(3)-(4). HOLDS.** C^(1/2) w = sqrt(lambda) M^(-1) psi from C M psi = lambda M^(-1) psi; so <e^(beta V)>_psi = lambda^(-1) ||C^(1/2) w||^2 <= I^d/lambda = e^(m + L); Jensen gives beta <V>_psi <= m + L. The electric part is >= -3d/(2 beta) by (2). D_0 <= 0 (positive vacuum, kernel derivative -S e^(-beta S)). With L <= C_0 N and 3d/2 = 9N/2, B = C_0 + 9/2. Valid for every unit vector of the eigenspace, so for the hidden compression. HOLDS.

**(5). HOLDS.** (kappa m - b^h)_+ <= kappa m + (m + BN)/beta per dimension. rho = -(1 + BNt/a)/beta. It is still of order n^4/log n in modulus, so it is still useless as an E2 input, as the file says.

**(6). HOLDS.** The normalized multipliers I_(k+1)/I_1 are products of increasing ratios, so the normalized convolution increases in form order; the singular-value swap; x = C_*^(1/2) w with ||x|| <= 1; Jensen for z^s with s >= 1 and ||x||^(2(1-s)) >= 1; min-max. Then log of lambda-hat_0 = -L gives the second inequality. The right derivative recovers (3) with L' = d d(log I) - D_0. HOLDS. It is a second derivation of (3) through a different route (finite comparison, no excited-eigenvector derivative); both use (1) and (2).

**(7). HOLDS** given ON FILE inputs. Z_+(3) <= Z^0(3) (commuting projection, positive T). Z^0 <= I^(3v-3) is row 1143 (M = 4V - (V-1) - 4 = 3V - 3 at L37 of that file). With lambda_0^3 >= I^(9N) e^(-3 C_0 N) the ratio is I^(-3) e^(3 C_0 N). c_I: Haar class density (2/pi) sin^2 theta; on [0, beta^(-1/2)], beta(1 - cos theta) <= 1/2 and sin theta >= 2 theta/pi; integral gives 8 e^(-1/2)/(3 pi^3). HOLDS.

**(8). HOLDS** given row 1161 (m_1 <= C_1 in the neutral sector). For m >= Lambda, (t - 3) Lambda = (C_Z + 3) N >= 1 makes e^(-(t-3)m) and m e^(-(t-3)m) decreasing; the time-three sum is <= e^(C_Z N); W_t >= (a/t) e^(-C_1 t). The exponent is C_1 t - 3N with C_1 t = O(n). HOLDS.

**(9). HOLDS.** S 1_(S > R) e^(-beta S) <= 4d e^(-beta R/2) e^(-beta S/2) pointwise (S <= 4d). The kernel e^(-(beta/2) S) is the raw Wilson transfer at beta/2, norm lambda_0(beta/2) <= I(beta/2)^d. (2) at k = 0 integrated from beta/2 to beta gives I(beta/2)/I(beta) <= 2^(3/2); with (1), lambda_0(beta/2)/lambda_0(beta) <= e^(FN), F = C_0 + (9/2) log 2 (3d/2 = 9N/2). beta R/2 = (F + 4) N. So the omitted operator over lambda_0 has norm <= 4d e^(-4N); dividing by lambda = e^(-m) lambda_0 and subtracting the vacuum gives e^m + 1. HOLDS.

**(10). HOLDS.** Tr(A)_+ = sup_(0 <= Y <= 1) Tr(YA) is j-Lipschitz in operator norm on a j-dimensional block. Below Lambda the cost is <= 4d e^(-4N)(1 + e^Lambda) G(t) with G(t) <= t W_t/a and Lambda = O(n^2) = o(N). Add (8). HOLDS.

**(10a). HOLDS.** r^t e^m = r^(t-1); Hoelder with exponent 1/(t-3) gives G(t-1)/G(t) <= [G(3)/G(t)]^(1/(t-3)); with G(3) <= e^(C_Z N) and G(t) >= e^(-C_1 t) the log of the ratio is o(N). The positive-measure remark (S = 2d at x = 1, y = -1; S = 0 at x = y = 1; R/N -> 0) HOLDS. The alternative bound ||b^(h,cut)|| <= R(e^m + 1) and the exponent -3N + Lambda + C_1 t HOLD. This check shares (7) and m_1 <= C_1 with (8); it avoids (3) only.

**What (10) removes from the E1 budget. HOLDS.** Under E1 in check 1630's form, the observed term of row 1628 (19) is >= (kappa + eps) W_t - kappa W_obs = kappa W_D + eps W_t; (kappa m - x)_+ <= kappa m + (-x)_+ gives H_kappa <= kappa W_D + H_0. So, given E1, (E2) reduces to H_0 < eps W_t, and by (10) to H_(0,<Lambda)^cut <= (eps/2) W_t eventually. HOLDS (elementary).

**(11), strict hidden sign for 0 < beta <= 1/(16d) = 1/(48 n^3). HOLDS.**
- lambda-hat_0 >= <1, B-hat 1> = int e^(-beta V) >= e^(-2 beta d) >= e^(-1/8) >= 7/8 (C-hat^(1/2) 1 = 1).
- Off-constant multipliers of C-hat are <= I_2/I_1 <= beta/4 (series bound I_(j+1)/I_j <= beta/(2(j+1))). B-hat <= C-hat <= Pi + q(1 - Pi), so p_0 >= (7/8 - q)/(1 - q) >= 5/6 for q <= 1/4.
- If T-hat psi = lambda-hat psi then C-hat^(1/2) M psi is a B-hat eigenvector at the same eigenvalue, so excited w are orthogonal to w_0 (top simple). |<1, w>|^2 <= 1 - p_0, so Pr_w(some k_e >= 1) >= p_0 and E_w sum k_e >= 5/6.
- beta d(log c_k)/d beta = k + beta I_(k+2)/I_(k+1) - beta >= k - beta; beta <V> <= 2 beta d; D_0 <= 0. So beta b_psi >= 5/6 - 3 beta d >= 5/6 - 3/16 > 1/2.
- Coldness: lambda_0 >= e^(-3 beta d) (Jensen gives even e^(-2 beta d)); Tr(MCM) <= Tr C = 1 (diagonal of the convolution kernel is K(1)^d = 1); G(1) <= e^(3/16) - 1 <= 3/13.
HOLDS for every unit vector of every excited eigenspace, so for the hidden compressions.

**Loss check after (11). HOLDS** given row 1145 (19) (ON FILE): with q = I_2/I_1 -> 1 and lambda-hat_0 <= e^(-c_2 N) the refined bound on p_0 is negative on late boxes.

**(12)-(13), pressure chord bound. HOLDS.**
- p = log lambda_0 is convex (supremum over nonnegative unit vectors of log of positive Laplace integrals) and real analytic (simple top eigenvalue). M(x) is finite.
- delta = (1/2) int (s - |y|) p''(x+y) dy <= s^2 M; |l' - p'(x)| <= p'(x+s) - p'(x-s) <= 2sM.
- On |z - x| <= s, |<psi, T_z psi>| <= lambda_0(Re z) and |e^(-l(z))| = e^(-l(Re z)), so |f| <= 1 by convexity. f(x) = e^(-m - delta). Schwarz-Pick: s|f'(x)| <= 1 - q^2. f'/f = D_psi - l'. (1 - q^2)/q = 2 sinh(m + delta). This is (13).
- s = min(1, sqrt(m/M)): delta <= m, sM <= sqrt(mM), sinh(2m) <= m sinh 2 for m <= 1. Then ||b|| <= 2 sqrt(mM) + 2 sinh 2 max(m, sqrt(mM)) <= (2 + 2 sinh 2) m (1 + sqrt(M/m)). HOLDS (the constant is generous). Here p'(x) = D_0 by first-order perturbation of the simple top level.

**(14). HOLDS.** sqrt(M/m) <= sqrt(t M/a) <= sqrt(C_t n M/a). -BN/x <= p'(x) <= 0 from (2) and (4) at m = 0, so mu(I_K^+) <= BN/(beta_K - 1). Vitali (factor 3) for the centred maximal function at scales <= 1; the layer-cake integral int sqrt(M) <= 2 sqrt(3 |I| mu) (split at z_0 = sqrt(3 mu/|I|)). HOLDS. Size: O(1 + n^2/sqrt(beta_K)). (12)-(14) cover only levels with m <= 1; levels 1 < m < Lambda are covered only by (3).

**Gaussian hidden zero slopes. HOLDS.** j + 1 > q_E vectors at energy j omega in two polarizations of one momentum; E restricted to their span has a kernel; that kernel lies in D_r; b_r vanishes on the Q = 0 product subspace (rescaled spectrum independent of beta at Q = 0; the commutator compresses to zero on an eigenspace). In compact Gaussian U(1) the diagonal slopes e_Q/beta >= 0, so H_0 = 0. HOLDS. This shows the non-strict (E2) sign holds in both seedless comparisons.

**Small-coupling sign in 4D Wilson U(1) and 5D Wilson SU(2). HOLDS.** U(1): c_k = e^(-beta) I_|k|; I_1/I_0 <= beta/2; beta d(log c_k)/d beta >= |k| - beta; 1 - cos in [0, 2] with Haar mean 1. 5D: beta <= 1/(16 p_5), p_5 = 6n^4: e^(-2 beta p_5) >= 7/8; beta b >= 5/6 - beta(d_5 + 2 p_5) = 5/6 - 16 n^4 beta >= 2/3; G(1) <= e^(1/6) - 1 < 1/2. HOLDS.

**Scope paragraph (Lemma ALG).** ARGUED, as labelled; I agree with it. Correct that no step fails for weak 5D SU(2).

Row 1632 verdict: every PROVED item HOLDS. No line fails. No correction needed. The RESULT's "levels above (C_Z+3) n^3/(t-3)" means lattice energies of order n^2, far above every thermally relevant energy.

## 3. Item 2: does either file reach the retained Wilson response?

No. Every proved estimate is one of three kinds.

1. Tail and truncation bounds, ultraviolet or large-deviation in kind.
   - Row 1631 (2)-(7): spins k >= q with q = O(log n) and q >= 6 e^2 beta. GUIDE: typical link spins at weak coupling are of order sqrt(beta), far below q.
   - Row 1632 (8): levels m >= Lambda = (C_Z + 3) n^3/(t - 3), of order n^2 in lattice units. Thermally relevant levels have m of order 1/t, about 1/n.
   - Row 1632 (9)-(10a): slab actions S > R = 2(F + 4) N/beta. GUIDE: N/beta is the order of a typical slab action at weak coupling, so this is a large-deviation cut with a fixed constant.
   These bounds move nothing in the retained sum. They show only that the retained sum carries the whole question.
2. Bounds with no sign and of volume size. These are row 1632 (3)-(6) (rho of order n^4/log n) and (12)-(14). (12)-(14) are the only estimates that reach low levels (m <= 1) on the band, but they bound |b| from both sides with relative size O(1 + n^2/sqrt(beta)). The needed size is eps.
3. One sign, at the wrong coupling: (11), with beta <= 1/(48 n^3).

**Does (11) say anything on the band? No.**
- Its range shrinks to zero as n grows. The band has beta_K of order log n, which goes to infinity.
- Its proof needs the dual vacuum to sit on the constant electric representation (p_0 >= 5/6). The file's own loss check shows that this bound becomes negative on late boxes.
- No proved statement carries the sign of b_r in beta from beta ~ n^(-3) to beta ~ log n. Neither monotonicity nor continuation is on file.
- The same conclusion holds in 4D Wilson U(1) and 5D Wilson SU(2). In 4D U(1) at strong coupling the theory has a gap, so (11) is the strong-coupling statement "all levels fall" (row 1610 L141 argued it). It is not a band mechanism.

## 4. Item 3: what is left of (E1) and (E2)

Notation. q from row 1631 (1); b^[q] is the clamped-electric, compressed-plaquette score; Lambda and R are from row 1632; "cold point" means a point with G <= c_col on the kappa_0-characteristic of the window [beta_K, beta_(K+r)], at every box side from L_h to L_h b^r, for the infinitely many K with K + r in E', uniformly in K.

- **(E1) left.** At every cold point, sum_r r^t Tr(J_r b_r^[q]) >= (kappa_0 + eps') W_t. Row 1631 (6) is two-sided, so this is equivalent to (E1) up to an o(1) change of eps. Row 1631 (8) is a consequence of it, not progress towards it. (E1) is still the selective estimate: it fails for the free photon and for compact Gaussian U(1) at every period (ON FILE, row 1628 (22)).
- **(E2) left.** Assume (E1) in check 1630's form, with W_t on the right. Then (E2) reduces to H_0 < eps W_t, and by row 1632 (10) to H_(0,<Lambda)^cut = sum_(0<m<Lambda) r^t Tr_(D_r)(-b_r^(h,cut))_+ <= (eps/2) W_t eventually. This is an upper bound on the negative part of the hidden low-level slopes. The non-strict sign (H_0 = 0) holds in both Gaussian laws (row 1632). So (E2) is not where selectivity sits.
- **PROVED here (one line, a new combination).** The spin cut of row 1631 also applies to the hidden blocks. Row 1631 (4) and row 1617 (6) hold for every unit vector of every eigenspace. So on D_r, ||b_r^h - b_r^(h,[q])|| <= eta m, and |H_kappa - H_kappa^[q]| <= eta W_D. I do not claim that the spin cut and the slab-action cut can be applied together. Each cut separately is controlled relative to the uncut b.
- **Same object?** Yes in substance, but not as one inequality. Row 1628 (20) writes the requirement as one inequality on the same slope forms b_r: sum r^t [Tr F_r(b_r - kappa_0 m) - Tr_(D_r)(b_r^h - kappa_0 m)_+] > 0. (E1) and (E2) split it by visibility. Both are about the retained low-level Wilson response on the window: cold eigenspaces with m < Lambda, spins below q, and slab action below R. (E1) is a positive lower bound on its visible trace. It is selective and fails for the Gaussian laws. (E2) is an upper bound on its hidden negative part. It is not selective and holds for the Gaussian laws. Any selective input must enter through the visible retained response. The running budget (RB) of check 1630 1.3(d) and (HOT) are still needed on top.

## 5. Item 4: selectivity (Lemma ALG, row 1553)

- Row 1631: (2), (4)-(7) hold for cosine 4D U(1) (Fourier label |j|) and for 5D SU(2) (eight colours, s_e <= 4 beta, factor 12). The file proves this and I re-derived the counts. The electric input row 1617 (6) also holds for both (row 1617 L219, L233). The spectator (g4) passes (6) while the seed fails. So nothing in row 1631 reads a 4D SU(2) property.
- Row 1632:
  - (2) is the same one-link integral in 5D. For U(1), beta^(1/2) c_k increases, which is a better bound.
  - (3)-(6), (8)-(10a) and (12)-(14) use only positivity of the kernel, the norm comparison, convexity and analyticity of the pressure, and lattice counts. ARGUED by me: they hold in both comparison models with changed constants. (7) uses the 4D selected-plaquette count. A 5D analogue of the same form is plausible but not checked here.
  - (11) is proved for 4D Wilson U(1) and for 5D SU(2) in the file. I checked it.
  - The Gaussian zero slopes show that the non-strict (E2) sign holds in both seedless Gaussian laws.
- Failure modes for the photon and compact Gaussian U(1). The proved pieces do not fail there: the bounds hold. Only the target (E1) fails, because the observed trace is zero. That failure reads the law (beta-independent Q = 0 spectrum after rescaling) together with the flat-shift symmetry (ON FILE, row 1628 (22), check 1630 3.1).
- Conclusion: no proved step in either file reads a property of typical 4D SU(2) Wilson fields that 4D U(1) or 5D SU(2) lack. This agrees with row 1386 Proposition NEG, since every piece is lattice-local or analytic.

## 6. Item 5: new and on file

| Statement | Standing |
|---|---|
| 1631 (2)-(3): spin tail in magnetic placement, with the factor e^m per eigenstate | New in magnetic placement. Same method (deletion or norm comparison plus Jensen) as row 1617 (4)-(6) in electric placement. Staple and separation as in row 860 Lemma DS. |
| 1631 (4): plaquette compression by one-unit bandwidth | New, elementary. |
| 1631 (5)-(6) | New combination of (4) and row 1617 (6) (checked 1621). |
| 1631 (7) | New second kernel bound. It shares the e^m and Jensen steps with (2). Row 1617 L157 had a second route for the electric side. |
| 1631 (8), coherence example | New. (8) is a consequence of (E1). |
| 1631 comparison laws, spectator | ON FILE (rows 1618, 1626, 1628 (22); row 1617 L235; rows 998, 1553, 1573). |
| 1632 (1), (7) inputs, (8) input m_1 <= C_1 | ON FILE (rows 1215/1221, 1143/1144, 1161/1162). |
| 1632 (2) | New as a bound (row 1618 Lemma 1 integral). |
| 1632 (3)-(5) | New. They improve row 1628's rho by a factor of order beta. They are still volume-sized. |
| 1632 (6) | New finite comparison. It uses the monotonicity of row 843 (row 1617 (12)). |
| 1632 (7)-(10a) | New. The same idea as row 1619 TRUNC and row 1626 (5)-(6) (counting high levels), with an unconditional time-three entropy bound and a cut slab mark. |
| 1632 (11) and its loss check | New as a full-transfer, all-level proof at beta <= 1/(48 n^3). Argued earlier in row 1610 L141. Related: row 710 Proposition EL (electric model), row 1626 (11) (beta -> 0 at fixed size). |
| 1632 (12)-(14) | New (Schwarz-Pick with the vacuum pressure). |
| 1632 Gaussian hidden zero slopes | New explicit form. The mechanism, one hidden zero-slope level, is ON FILE (check 1625 section 3; row 1628 families A and B; row 1629 Corollary 2.2(3)). |
| 1632 (11) for 4D U(1) and 5D SU(2) | New, immediate. |
| This check: the spin cut on hidden blocks | New, one line (section 4). |

Independence: both files are by one model, gpt-6.2-astra max. My check is a third reading of the same routes, by hand. The only different data path is the floating-point guide for the elementary inequalities (section 0), which is not a proof. Nothing on the critical path moved: (VIR-down) on the band, (HOT), (PUR-io) and the gap stay open.

Suggested registry note for VIR-DOWN (not edited by me): "Rows 1631-1632 (check 1634): spin tails (q = O(log n)), levels above order n^2, and slab actions above order N/beta change the (E1) numerator and the (E2) hidden adverse trace by o(1) W_t at every cold point of the window. The non-strict (E2) sign holds in both Gaussian laws. A strict hidden sign is proved only for beta <= 1/(48 n^3). Left: the retained low-level response, (E1) for its visible trace (selective) and H_0^cut <= (eps/2) W_t for its hidden part."

## RESULT

Row 1631 (E1): (1)-(8), (7) and the scope, example and spectator items all HOLD; no line fails. (7) shares its e^m and Jensen steps with (2).
Row 1632 (E2): (2)-(14), (10a), (11), the Gaussian zero slopes and the U(1)/5D small-coupling sign all HOLD; no line fails.
Neither file reaches the retained Wilson response. Both control only tails: spins >= q = O(log n), levels with m >= Lambda (order n^2),
and slab actions above order N/beta. Their other bounds are sign-blind and volume-sized ((3)-(6); (12)-(14) of size n^2/sqrt(beta)).
(11) at beta <= 1/(48 n^3) says nothing on the band: its range goes to 0 while beta_K goes to infinity, its p_0 >= 5/6 step fails late,
nothing carries the sign in beta, and it also holds for strong-coupling 4D U(1) and 5D SU(2).
Left of (E1): sum r^t Tr(J_r b_r^[q]) >= (kappa_0 + eps') W_t at every cold window point, equivalent to (E1) up to o(1).
Left of (E2): given (E1), H_(0,<Lambda)^cut <= (eps/2) W_t. Both are one object, the retained low-level slope form of row 1628 (20),
split by visibility. The (E2) sign holds in both Gaussian laws, so any selective input must come through the visible part, (E1).
Selectivity: every proved piece also holds for 4D Wilson U(1) and 5D SU(2) with changed constants. (7) in 5D is ARGUED only.
No piece reads a 4D SU(2) property (in line with Lemma ALG and Proposition NEG). New: the tail bounds, (3)-(6), (11)-(14) and (8).
ON FILE: row 1617 (6), rows 1215, 1143, 1161, the Gaussian mechanism (row 1628 (22)) and the spectator. Nothing on the critical path moved.
