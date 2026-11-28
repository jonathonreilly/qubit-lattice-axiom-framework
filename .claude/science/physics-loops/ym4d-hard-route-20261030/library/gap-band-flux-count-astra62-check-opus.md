# Check of library/gap-band-flux-count-astra62.md (FINISH row 1595)

Status: complete. Checker: Claude (Opus 5.5), hand check, no numerics; not an audit.

## Plan
1. Read GOAL.md, FINISH.md Rules and Working efficiently.
2. Read library/gap-band-flux-count-astra62.md in full.
3. Read check 1585 section (v), rows 1587/1588 and checks 1589/1590.
4. Check each section line by line; write verdicts as I go.
5. Stopping point and proof/refutation status; RESULT line.

## Progress
- Step 1 done: read GOAL.md, FINISH.md 'Working efficiently' and 'Rules', the target row in full (201 lines), check 1585 section (v) in full, row 1587 in full, checks 1589 and 1590 in full.
- Step 2 done (hand check, results below): setup, section 1, section 2, section 3 with its model test, section 4 except the input from row 1141, the flux consequence, model tests, purity. Still to read: row 1141 (3)-(4) for (12).

## Step 2 results (hand check)

### Setup and (1)
- A_t, B_t are the kernels of P_e T^t, P_o T^t; both symmetric (K_t symmetric, K_t(Cx,Cy)=K_t(x,y)); A composes since P_e commutes with T. B_t(x,y) uses C on the second pin, which equals check 1585's b_j with C on the first pin since K(x,Cy)=K(Cx,y). Lemma (1) is the lemma of check 1585 (v). HOLDS.

### Section 1: (2)-(5)
- Outer pins x_0, x_2, ..., (and x_{m-1} for odd m); middle pin x_{2i+1} appears only in A_{t_2i}(x_2i, .) A_{t_2i+1}(., x_2i+2); normalizer is A_{s+t} by the semigroup. Conditional independence and (2): HOLDS.
- (3): (D_s D_t)(x,z)/A_{s+t}(x,z) is the conditional probability that both arcs of the pair have |b|>1/2. HOLDS. J <= N <= 2J+1 (the +1 only from the unpaired arc for odd m): HOLDS.
- (4): on {M >= a log n}, P(J < c log n | A) <= n^c prod(1 - alpha q_i) <= n^{c - alpha a}, alpha = 1 - e^{-1}; N < c log n implies J < c log n. HOLDS.
- (5): on {M <= (c/8) log n}, E(N|A) <= 2M+1 <= (c/4) log n + 1, so P(N >= c log n | A) <= 1/4 + 1/(c log n) <= 1/2 once c log n >= 4. HOLDS.
- Equivalence: (1) at (c, eps) gives mu(M <= (c/8) log n) <= 2 C_0 n^{-eps}; a power bound for mu(M < a log n) gives (1) for every c < alpha a. HOLDS. It is an equivalent restatement (rule "equivalent is not progress"); the row labels it so.

### Section 2: (6)-(8)
- R_theta (left multiplication of the a = n^2 cut links by cos theta + J sin theta) preserves product Haar, commutes with C, and R_{theta+pi} = C R_theta. Only Haar invariance of the raw-slice density is used, not gauge covariance. HOLDS.
- |b| <= 1/2 iff |L| <= 2 artanh(1/2) = log 3. L(theta+pi) = -L(theta); w(theta+pi) = w(theta) by A_t(x,Cy) = A_t(x,y). HOLDS.
- (7): one cut link occurs in 1 end temporal plaquette and in 4 spatial plaquettes at half weight (each 12/13 plaquette at the cut holds two cut links; counting incidences handles this), each occurrence moves the normalized trace by at most 1 per radian; so |d log K_s| <= 3 beta a and |(log w)'| <= 6 beta a. In L the end spatial factor is C-even and cancels identically, leaving one temporal incidence per cut link in each of the two integrals: |L'| <= 2 beta a. HOLDS.
- Angle count: a zero theta_0 and theta_0 + pi, window radius r = log3/(2 beta a), measure min(2pi, 4r), proportion min{1, log3/(pi beta a)}; log w is pi-periodic with Lipschitz 6 beta a and circular distance <= pi/2, so min w/max w >= e^{-3 pi beta a}. Averaging over theta then y gives (6). HOLDS.
- Sequential use: given x_0..x_j the law of x_{j+1} is (2) with z = x_0, t = sum_{i>j} t_i > 0 for j <= m-2; G_0..G_{j-1} are functions of x_0..x_j; closing arc omitted. (8): HOLDS. q_i >= p_{n,beta}: HOLDS.
- Failure point: (m-1) p_{n,beta} -> 0: HOLDS. The stated cause needs a correction (see verdicts): even with w constant, the window alone gives (m-1) log3/(pi beta n^2) ~ n^{-3/2} -> 0, while (8) needs (m-1) p >= ((c+eps)/alpha) log n. So the Lipschitz window and the orbit weight ratio each fail on their own.

### Section 3: (9)-(11)
- E e^{-N} = Tr prod[h A + (1-h) D]/Z_e(d): factor h^{G_j} = h + (1-h)(1 - G_j). HOLDS.
- ||A_t||_{d/t} = Z_e(d)^{t/d} (A_t = P_e T^t >= 0); sum 1/p_j = 1; triangle inequality; Markov. (9): HOLDS.
- Unequal-exponent trace Hoelder: Horn's inequality on exterior powers, then sum_i [log(a_i/r)]_+ = max_k sum_{i<=k} log(a_i/r) (b_i also decreasing), integral_0^a log(a/r) dr = a, scalar Hoelder. Approximation in HS norm controls p_j-norms because p_j >= 2. HOLDS.
- Equal tiling, even m: z_t^m = Tr(D_t^m)/Z_e(d) = mu(N=0). HOLDS. mu(N=0) <= C n^{-a} implies m(1 - z_t) >= (a - o(1)) log n: HOLDS AFTER the routine case split (if 1 - z_t >= delta_n -> 0 slowly, m(1-z) >= m delta_n >> log n; else -log z <= (1-z)/z). The row's "by m ~ sqrt n" covers the first case only; the second is one line. Not a defect in the conclusion.
- (10): |D_t f| <= A_t|f| gives ||D_t||_op <= lambda^t; |b| > 1/2 gives A_t < 2|B_t| so ||D_t||_2^2 <= 4 ||B_t||_2^2 = 4 Z_o(2t); then sum s_i^p <= s_1^{p-2} sum s_i^2. HOLDS. The step to sum_j(1 - z_{t_j}) >= (a - o(1)) log n: -log z_t >= (t/d)(a log n - log C) -> 0, so 1 - z_t >= (1 - o(1))(-log z_t). HOLDS.
- Precision (checker): Z_e(d) <= lambda^{d-2t} Z_e(2t) for T >= 0, so RHS(10)/4 >= Z_o(2t)/Z_e(2t). Route (10) therefore needs at least a power decay of the one-axis odd fraction at the short period 2t ~ 2 sqrt d, the same cost check 1590 found in row 1588 Theorem 2. Also row 1587's bound (2) satisfies RHS(2)^2 <= RHS(10)/4, since Z_e(2d-2t) <= lambda^{d-2t} Z_e(d). The three trace routes (row 1587 (2), row 1588 (2.10), row 1591 (10)) carry the same short-period cost.
- Four-site test: raw entries (E_ii +- O_ii)/2 and delta/2, all positive for large n in both models; E, O positive definite; even kernel (E^v)_{ij}/2 and sector traces Tr E^v, 4^{-v} + gamma^{2v} identical in both. All-A probability prod (E^{t_j})_{AA}/Tr E^d; (E^t)_AA >= (1+delta)^t >= 1; ||E^d - E_0^d|| <= 2 d delta (1+2 delta)^{d-1}; Tr E^d <= 1 + gamma^d + 4 d delta(1+2delta)^{d-1}; (11): HOLDS (gamma^d = exp(-d n^{-3/4}) is below every power since d ~ n). Bias on all-A: O_AA^t/(E^t)_AA; model I <= 4^{-t} (N = m), model II >= (gamma^2/(1+2delta))^t -> 1 since t n^{-3/4} -> 0 (N = 0). RHS(10) -> 4 in both: lambda in [1, 1+2delta], Z_o(2t) -> 1, Z_e(d) -> 1. HOLDS. The parameters do not depend on the period, so check 1590's correction to row 1588 Prop 1.2(3) (alpha_n depended on the period) does not arise here.

### Section 4: (12)-(14), except the row 1141 input
- |log K_s(x,y)/K_s(x,Cy)| <= beta H(y): spatial actions of g.y, y, Cy agree; each end link sits in one end temporal plaquette; |Re(X(a-b))| <= |a-b| and |a^{-1}-b^{-1}| = |a-b| for unit quaternions; K_s(x, g.y) = K_s(x,y). HOLDS. beta H(x_j) <= log 3 implies |b_j| <= 1/2 and |b_{j-1}| <= 1/2. HOLDS.
- (12) given the conditional bound P(Delta >= 1/152 | exterior of the pair) >= 1/2: e^{L/4} (1 - (1-e^{-1})/2)^L <= e^{-kappa L}, kappa = (1-e^{-1})/2 - 1/4 = 0.066; union over m pins. HOLDS. 8(1+6 beta) <= 152 on beta <= 3: HOLDS. |h| <= 6 beta: each 2- or 3-link at the cut lies in 4 spatial plaquettes (full weight after the two half weights) and 2 temporal plaquettes; the twist flips only 1-links, so no seam sign enters these. HOLDS.
- Telescoping: |prod a_i - prod b_i| <= sum |a_i - b_i| for unit quaternions, and |g_a W g_a^{-1} - chi W| = |g_a - chi W g_a W^{-1}|. Winding line (chi = -1): >= |2 Re g_a + (q + Ad_W q)| >= 2|Re g_a|. Plaquettes (chi = +1, no cut link): >= |q - Ad_U q| + |q - Ad_V q| >= |q| sqrt(Delta). Line and plaquette edges disjoint across bases. min(2, 1/sqrt152)(|r| + |q|) >= 1/sqrt152. (13): HOLDS. Identity gauge gives H <= 2n^2. HOLDS.
- (14): on each direction-1 line the edge errors sum to >= |Re(g W g^{-1}) + Re W| = 2|Re W| for every gauge; so H >= #{lines: |Re W| >= 1/2}. The joint density of the n^2 line transports at one pin is <= (1+eta)^{n^2} = 1 + O(n^{-A_0-4}) <= 2 for large n (row 1587 (7) proof; check 1589 step 5 (c)-(d)). Under product Haar the count is Bin(n^2, p_H), p_H = 2(1/3 - sqrt3/(4 pi)) = 0.391; exponential Markov gives exp(p_H n^2/2 - (1-e^{-1}) p_H n^2) = exp(-(1/2 - e^{-1}) p_H n^2), times 2 for the density, times m for the union. HOLDS. beta H <= log 3 with beta >= 2 gives H <= 0.55 < p_H n^2/2 for n >= 2. So the RESULT bound 2m e^{-(1/2 - e^{-1}) p_H n^2} for passing beta H <= log 3: HOLDS.
- (13) and (14) are two derivations from different inputs (row 1141's local axis estimate; row 1587's winding-density estimate). They agree on the area scale of H.

### Flux consequence, model tests, purity
- (15): prod |b_j| <= 2^{-N} <= n^{-c log 2} on {N >= c log n}. HOLDS. Odd probability rho/(1+rho); joint law of the three commuting parities (d even, T >= 0); union bound; f(d) <= 3R_n/(1+R_n) = O(v^{-min(eps, c log 2)}) with n = 512u. HOLDS as an implication.
- Weak compact U(1): p >= (rho - n^{-c log 2})/(1 - n^{-c log 2}) with rho >= eta/(1-eta). HOLDS (relies on rows 1565/1571 as checked in 1571/1589). U(1): g_a W g_a^{-1} = W so each line error is 2 and H = 2n^2. HOLDS. 5D SU(2): remark only, no claim. HOLDS as stated.
- Purity: spectator K (x) S^t leaves every b_j and the pin law unchanged and multiplies both purities by Tr S^{2u}/(Tr S^u)^2; S = rI + (1-r)P_const on q sites has Tr S^v = 1 + (q-1) r^v -> q at v ~ n, factor -> 1/q. P = Pi (1 - f(2u))/(1 - f(u))^2 with f indexed by period. HOLDS.

## Step 3 result: the row 1141 input to (12)
- Read library/gap-crux2-astra62.md lines 50-82. Re-derived (3): fibre average of e^{h.q} over q exp(tn) is I_0(v) <= I_0(kappa); Z_kappa >= e^{-1/2} I_0(kappa)/(2(1+kappa)) (integrate r >= 1 - 1/(2(1+kappa)), (log I_0)' <= 1); pushforward density <= 2 e^{1/2}(1+kappa) <= 4(1+6b); chord-cap fraction t^2; |n - Ad q n| = 2|u x n|. HOLDS.
- (4): D/4 is the smaller eigenvalue of the rank-<=2 outer-product sum, >= |u_1 x u_2|^2/(|u_1|^2+|u_2|^2) >= |u_2 x u_1hat|^2/2 when |u_1| >= |u_2|; {D < delta} lies in the union of two cross-product events, each bounded by M_b delta/2 by exposing one link that lies only in the other plaquette. P(D >= delta_b | outside) >= 1/2. HOLDS. The proof uses only distinct bonds, a common root and one-link densities with |h| <= 6b, for every b >= 0.
- So the transfer to the pin (NE and SW 23-plaquettes at (0,4i,4j), eight distinct bonds, |h| <= 6 beta in the labelled torus law) HOLDS, and (12)-(13) HOLD on [2,3].
- Because (4) holds for every b >= 0, (12)-(13) also hold at fixed 0 < beta < 2/9 (threshold >= 1/152 still), where check 1585's Dobrushin test makes every arc ambiguous. And under Haar pins (b = 0) they hold for row 1587's detour comparison kernel, where N = 0 eventually. The row's two remarks HOLD. So H ~ n^2 at every pin is compatible with N = m and with N = 0: the gauge-matching test says nothing about (1).

## Step 4: stopping point and comparison with rows 1587, 1588 and checks 1589, 1590
- Check 1589 noted that row 1587 attacked only the majorant D-bar_d, and that the conditional-indicator route of check 1585 (v) was not tried. Row 1591 attacks the count (1) itself three distinct ways: the conditional-indicator route (section 2), the weighted trace (section 3), and a sufficient pin mechanism (section 4); section 1 is an equivalent restatement. So the stopping test "three distinct arguments on one stated estimate" is met for (1) itself.
- Failure points. Section 2: exact after the correction in the verdicts (two separately fatal losses). Section 3: exact. (9) is lossless on equal even tilings (z_t^m = mu(N=0)); the loss is in (10). The four-site test shows (10) can tend to 4 while (1) holds, and RHS(10)/4 >= Z_o(2t)/Z_e(2t). Section 4: exact. The test fires with probability at most 2m e^{-(1/2 - e^{-1}) p_H n^2}, and it is not necessary (small beta).
- Trace routes compared. Row 1587 (2), row 1588 (2.10) and row 1591 (10) all need at least a power decay of the one-axis odd fraction at period 2t ~ 2 sqrt d (RHS(2)^2 <= RHS(10)/4; check 1590's Step 4 for (2.10)). On positive transfer data that short-period fraction is neither sufficient for (1) (row 1587's period example: O(n^{-p}) while P(N >= 1) -> 0) nor necessary (row 1591 model I: Z_o(2t)/Z_e(2t) -> 1/2 while (1) holds). Model-class statements only.
- Section 2 and row 1588 Prop 1.2(3) (check 1590) are consistent. 1588 shows the conditional route can fail on transfer data. 1591 shows that on Wilson pins the conditional probability is positive at every history, but only of size about e^{-3 pi beta n^2}/n^2.
- (14) uses row 1587's winding-density bound as checked in check 1589 step 5. (13) uses row 1141. They are different inputs, so the area scale of H has two derivations.
- The remaining unknown is exactly (1) on the full Wilson pins at d in {n/512, n/256}, beta in [2,3], or equivalently by (4)-(5) the lower tail of M under the alternate-pin law. Nothing in the row proves or refutes (1). The proved Wilson statements are (6)-(8) (true, but they give nothing at this scale), (9)-(10) (conditional bounds), and (12)-(14) (refutation of one sufficient mechanism). The model tests are about positive transfer data, weak compact U(1), or the Dobrushin range. (N-flux) stays conditional. Pi and (PUR-io) are untouched.

## Verdicts

| Part | Verdict |
|---|---|
| Setup and lemma (1) (same as check 1585 (v)) | HOLDS |
| Section 1: conditional independence, (2), (3), J <= N <= 2J+1 | HOLDS |
| (4), (5) and the equivalence of the two lower tails | HOLDS (equivalent restatement; not progress, and the row does not claim it as progress) |
| (6), with (7) and the angle/weight count | HOLDS |
| (8), the sequential Wilson bound after any indicator history | HOLDS |
| Failure-point sentence of section 2 ("the cost comes from replacing the bridge's weight ... by the smallest weight on the whole orbit"), repeated in the closing paragraph ("Angle integration loses the weight at sign crossings") | HOLDS AFTER CORRECTION. Replace with: "Two losses, each fatal alone. The worst-case slope bound abs(L') <= 2 beta n^2 limits the certified window to a fraction log3/(pi beta n^2). The orbit weight ratio costs e^{-3 pi beta n^2}. Even with w constant, (m-1) log3/(pi beta n^2) ~ n^{-3/2} -> 0, while (8) needs (m-1)p >= ((c+eps)/(1-e^{-1})) log n. A usable bound needs both the typical slope of L near its zeros and the typical weight there." |
| E e^{-N} identity, (9), unequal-exponent trace Hoelder | HOLDS |
| Equal even tiling: z_t^m = mu(N=0), and a power bound on mu(N=0) implies (1) | HOLDS (the step m(1 - z_t) >= (a - o(1)) log n needs the one-line case split written in Step 2; the conclusion stands) |
| (10) and its consequence for (9) | HOLDS. Checker's precision: RHS(10)/4 >= Z_o(2t)/Z_e(2t), so this route needs a short-period one-axis flux bound, the same cost as row 1587 (2) and row 1588 (2.10) |
| Four-site test of the loss in (10): positivity, identical even kernel and sector traces, (11), N = m versus N = 0, RHS(10) -> 4 | HOLDS at both periods (parameters do not depend on the period) |
| Section 4: abs(log K_s(x,y)/K_s(x,Cy)) <= beta H(y) | HOLDS |
| (12) with the row 1141 input (rechecked (3)-(4)) | HOLDS |
| (13) | HOLDS |
| (14), and the RESULT bound 2m e^{-(1/2 - e^{-1}) p_H n^2} for passing beta H <= log 3 | HOLDS (p_H = 0.391; relies on row 1587's density bound as checked in check 1589 step 5) |
| What section 4 shows about making arcs ambiguous | HOLDS. It refutes the cheap gauge-matching mechanism on [2,3]. By the small-beta case and the Haar comparison kernel it says nothing about (1) either way |
| (15) and the conditional (N-flux) bound f(d) <= 3R_n/(1+R_n) | HOLDS as an implication. No proved Wilson estimate gives a rate |
| Model tests: weak compact U(1) lower bound on p, H = 2n^2 in U(1), 5D remark | HOLDS (U(1) input from rows 1565/1571 not rechecked) |
| Purity paragraph: spectator, 1/q factor, P = Pi(1 - f(2u))/(1 - f(u))^2 | HOLDS |
| Stopping point | HOLDS. Exact once the section 2 correction is made. Three distinct direct attempts on (1), which check 1589 had found missing from row 1587 |
| Is anything a proof or refutation of the count? | No. The row's RESULT ("neither proved nor refuted") HOLDS |

Not checked: the repo-search table and its attributions; row 1568 section 1.1 (the cut rotation was re-derived directly instead); rows 1565/1571 and check 1585's Dobrushin integration (used as checked in 1571, 1572 and 1589); row 1588 beyond check 1590.

RESULT — Row 1591 checks: every proved step ((2)-(5), (6)-(8), (9)-(10) with the trace Hoelder, the four-site test (11), (12)-(14) with row 1141's (3)-(4) rechecked, (15) and the purity algebra) HOLDS, and nothing FAILS. One correction: the section 2 failure point has two separately fatal losses, the slope window ~ 1/(beta n^2) and the weight ratio e^{-3 pi beta n^2}, not only the weight. The count (1) is neither proved nor refuted. The gauge-matching test fires with probability at most 2m e^{-(1/2 - e^{-1}) p_H n^2}, and it is uninformative about (1). (N-flux) stays conditional, and Pi is untouched.
Checked line by line by Claude (Opus 5.5): sections 1-4, the flux consequence, the model tests and the purity paragraph of library/gap-band-flux-count-astra62.md, and row 1141's (3)-(4); not the repo-search table or the inputs listed as not checked.
