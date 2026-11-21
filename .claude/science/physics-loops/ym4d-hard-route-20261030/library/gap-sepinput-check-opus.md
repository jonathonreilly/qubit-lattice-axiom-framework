lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-15T19:04Z

# Check of row 996 (`library/gap-sepinput-max.md`), queue row 997

Row 997, `gap-sepinput-check-opus`. Checker: Claude Opus 5.5 max, Mac mini worker 3. Pinned at commit 011ea3c56 on `claude/ym4d-hard-route`. The note under check was written by Claude Fable 5.2 (row 996). This is a same-provider check (Anthropic model, different model), not an independent check in the sense of the working rules; a gpt-6-astra check is held.

Scope (row 997): check line by line 5.1 (Identity MIX, v = 8 beta_A/3), 5.2 and 5.3 (Proposition TILT and its corollaries; Brascamp-Lieb with hypotheses; non-compact domain with F smooth), 5.5 (Lemma SHEET: Haar-preserving change of variables on the open tube, m at most n - 2), Proposition MF, 6.3 (Proposition ELL), 6.4 (Proposition 4F: interval J and second derivative). Verdicts: HOLDS, HOLDS AFTER CORRECTION, FAILS, with the line. No new attack.

## Plan (one step per response, appended here as it finishes)

1. Read the note in full and the K7 definition it reads (`library/gap-constraints-max.md` L73, `library/gap-mid-max.md`). Record the exact statements under check with line numbers.
2. Check 5.1, Identity MIX, including the variance v = 8 beta_A/3 and the sign and normalisation conventions.
3. Check 5.2 and 5.3, Proposition TILT and Corollary LIP and any other corollary; state Brascamp-Lieb with its hypotheses; decide whether a non-compact domain with F smooth meets them.
4. Check 5.5, Lemma SHEET: the frozen tube, the Haar-preserving change of variables on the open tube, the count m at most n - 2, the bound R_Lambda(0) at most 4/(n-1).
5. Check Proposition MF.
6. Check 6.3, Proposition ELL.
7. Check 6.4, Proposition 4F: the interval J and the second derivative.
8. Verdict table and RESULT line.

## Step results

(Appended below as each step finishes.)

### Step 1: what is under check

Read in full: `library/gap-sepinput-max.md` (571 lines, file as at 011ea3c56). Read for the K7 definition: `gap-mid-max.md` L48 (one-plaquette weight exp(beta_F x + beta_A (4 x^2 - 1)/3), x = (1/2) tr U_p) and `gap-constraints-max.md` L73. The Sussman-Alpoge account is not read: no item under check cites it.

Items and lines (all line numbers are in `gap-sepinput-max.md`):

| Item | Lines | Claim |
|---|---|---|
| 5.0 setting | L256-267 | mu_(b,v) proportional to exp(sum_p (b_p x_p + (v/2) x_p^2)) dU; C = Hess_b F; Sigma^2(v) = sup_b lambda_max C(b,v); R = 1/Sigma^2; 0 < Sigma^2 <= abs(P) |
| 5.1 Identity MIX | L269-290 | (a) Z(b,v+w) = int gamma_w(ds) Z(b+s,v); (b) mixture law, s = w x(U) + sqrt(w) xi; (c) hidden-field density exp(-H), Hess H = 1/w - C(b+s,v); K7 = mu_(beta_F 1, 8 beta_A/3); heat equation; Remark MIX |
| 5.2 Proposition TILT | L292-305 | w Sigma^2(v) < 1 gives C(b,v+w) <= Sigma^2(v)/(1 - w Sigma^2(v)) and R(v+w) >= R(v) - w; uses Brascamp-Lieb |
| 5.3 Corollaries | L307-336 | LIP; K7-A; K7-B; Reading; Remark POL (marked ARGUED) |
| 5.5 Lemma SHEET | L358-390 | frozen side plaquettes of an open tube; Cov(x_(p_i), x_(p_j)) -> 1/4; Sigma^2_Lambda(0) >= (n-1)/4; consequence for TILT |
| Proposition MF | L392-402 | one global Gaussian shift; Var(E)/abs(P) <= X/(1 - w X); converse; "the same statement as" |
| 6.3 Proposition ELL | L419-428 | (Re g_1, Re g_2, Re g_1 g_2) uniform on the elliptope E_3, density 2/pi^2 |
| 6.4 Proposition 4F | L430-445 | rho_4 = (2/pi^3) abs(J); J; rho_4 not log-concave at theta = (0.5, 0.4, 0.4, 0.4) |

Method: each step is redone by hand from the definitions. No numeric run is used for any verdict. The GUIDE controls of the note (5.4, 5.5 remark 3, 6.4 control, 6.5) are not checked and carry no weight here.

### Step 2: 5.0 and 5.1, Identity MIX. Verdict HOLDS

**5.0 (L256-267).** Hess_b F = C: d/db_p F = <x_p>, d^2/(db_p db_q) F = <x_p x_q> - <x_p><x_q>. Differentiation under the integral is allowed: the integral is over a compact group and the integrand is smooth in (b, v). The bound Sigma^2 <= abs(P): lambda_max(C) = sup over unit a of Var<a, x> <= E <a, x>^2 <= abs(x)^2 <= abs(P). Sigma^2 > 0: at b = 0 each U_p is a product of four independent Haar links, so Var x_p = 1/4. HOLDS. (Sigma^2(v) is finite for every real v by the same bound.)

**The variance v = 8 beta_A/3.** The K7 weight is exp(beta_F x + beta_A (4x^2 - 1)/3) = exp(-beta_A/3) exp(beta_F x + (4 beta_A/3) x^2). In 5.0 the quadratic term is (v/2) x^2. So v/2 = 4 beta_A/3 and v = 8 beta_A/3. For s of law N(0, v): E exp(s x) = exp(v x^2/2). So the Gaussian coupling has variance 8 beta_A/3, as L56 and L262 say. Numbers: sqrt(8 x 0.9/3) = sqrt(2.4) = 1.549 (L57: 1.55); v at beta_A = 0.9, 1.25, 1.5 is 2.4, 3.33, 4.0 (L221). The identity needs beta_A >= 0; K7's line lies there. HOLDS.

**(a), L273.** Z(b+s, v) = int dU exp(sum_p ((b_p + s_p) x_p + (v/2) x_p^2)). For each p, int gamma_w(ds_p) exp(s_p x_p) = exp(w x_p^2/2). The integrand is positive, so Tonelli exchanges the s- and U-integrals. Result: int dU exp(sum_p (b_p x_p + ((v+w)/2) x_p^2)) = Z(b, v+w). HOLDS.

**(b), L274-275.** The joint law of (s, U) is gamma_w(ds) Z(b+s,v)/Z(b,v+w) times Z(b+s,v)^(-1) exp(sum_p((b_p+s_p) x_p + (v/2) x_p^2)) dU. The factors Z(b+s, v) cancel. The joint density is proportional to exp(-abs(s)^2/(2w) + <b+s, x> + (v/2) abs(x)^2). The U-marginal is mu_(b,v+w) by (a). Given U, the s-density is proportional to exp(-abs(s)^2/(2w) + <s, x>), which is proportional to exp(-abs(s - w x)^2/(2w)). So s given U is N(w x(U), w 1). Then xi := (s - w x(U))/sqrt(w) has the conditional law N(0, 1) for every U. So xi is standard Gaussian and independent of U. HOLDS.

**(c), L276.** The s-marginal is proportional to exp(-abs(s)^2/(2w)) Z(b+s, v) = exp(-H(s)) with H(s) = abs(s)^2/(2w) - F(b+s, v). Hess H = (1/w) 1 - C(b+s, v) by 5.0. pi is a probability measure because int gamma_w(ds) Z(b+s, v) = Z(b, v+w) is finite. HOLDS.

**Heat equation, L284-285.** dZ/dv = int (1/2) sum_p x_p^2 exp(...) dU, and d^2 Z/d b_p^2 = int x_p^2 exp(...) dU. So dZ/dv = (1/2) Laplace_b Z. HOLDS.

**"Annealed Gaussian couplings", L283.** This means: the K7 partition function is the Gaussian average of the Wilson partition function in the couplings, and the K7 measure is the mixture (b). The couplings are independent under the prior gamma_w only. Under the mixture their law is pi, which is not Gaussian and not a product. The precise statement is (a)-(b), and the note writes it. HOLDS.

**Remark MIX, L287-290.** (1) is immediate from (a)-(b): the unnormalised K7 measure is exp(-beta_A abs(P)/3) int gamma_w(ds) exp(<beta_F 1 + s, x>) dU. (2) Hess H(s) >= kappa 1 for all s, with kappa > 0, holds exactly when sup over s of lambda_max C(b+s, 0) < 1/w. As s runs over R^P, b+s runs over R^P. So the condition is w Sigma^2(0) < 1, as stated. HOLDS.

**Verdict 5.1: HOLDS.** No correction.

### Step 3: 5.2 Proposition TILT and 5.3 corollaries. Verdict HOLDS (K7-A: HOLDS, one wording remark)

**Brascamp-Lieb, with its hypotheses (source read).** E. A. Carlen, D. Cordero-Erausquin, E. H. Lieb, "Asymmetric covariance estimates of Brascamp-Lieb type and related inequalities for log-concave measures", arXiv:1106.0709v2, Section 1, quoted from the PDF fetched to `/tmp/chk997/src/` (extract `/tmp/chk997/out/ccl.txt`): "Let f be a C2 strictly convex function on Rn such that e−f is integrable. By strictly convex, we mean that the Hessian matrix, Hessf, of f is everywhere positive." With dmu = e^(-f) dx normalised and h real in L^2(mu): "The Brascamp-Lieb (BL) inequality [4] for the variance of h is var(h) ≤ ∫Rn (∇h, Hess−1 f ∇h) dµ". Their [4] is H. J. Brascamp and E. H. Lieb, J. Funct. Anal. 22, 366-389 (1976), the paper the note cites. Their Theorem 1.1 takes locally Lipschitz functions that are square integrable. The theorem number 4.1 in the note is not confirmed by this source; the statement is.

So the hypotheses are: (H1) the measure lives on all of R^n; (H2) the potential is C^2; (H3) its Hessian is positive definite at every point; (H4) e^(-potential) is integrable; (H5) the test function is C^1 (or locally Lipschitz) and in L^2(mu).

**Does TILT's setting meet them? Yes, all five.** The potential is H(s) = abs(s)^2/(2w) - F(b+s, v) on R^P.
- (H1) The domain R^P is non-compact. That is the theorem's own setting, not an exception to it. Non-compactness enters only through (H4) and (H5).
- (H2) Z(b', v) = int exp(<b', x> + (v/2) abs(x)^2) dU is an entire function of b' in C^P (an integral over a compact group of an entire integrand, bounded on compact sets of C^P). It is positive on R^P. So F = log Z and H are real-analytic on R^P.
- (H3) C(b+s, v) <= lambda_max(C(b+s, v)) 1 <= Sigma^2(v) 1, so Hess H(s) >= kappa 1 with kappa = 1/w - Sigma^2(v) > 0 at every s. This is uniform, which is more than (H3) asks.
- (H4) By Taylor's formula with Hess H >= kappa 1: H(s) >= H(0) + <grad H(0), s> + kappa abs(s)^2/2. So e^(-H) is integrable and has Gaussian tails.
- (H5) g(s) = <a, s> is smooth, and it is in L^2(pi) by the Gaussian tails. grad g = a.

Then (Hess H)^(-1) <= (1/kappa) 1 gives Var_pi <a, s> <= abs(a)^2/kappa. This is L299-300. HOLDS.

**The rest of the proof, L301-305.** By 5.1 (b), s = w x(U) + sqrt(w) xi, with U of law mu_(b,v+w) and xi standard Gaussian independent of U. So Cov_pi(s) = w^2 C(b, v+w) + w 1 (L301). Hence w^2 <a, C a> + w abs(a)^2 <= abs(a)^2/kappa. Now 1/kappa = w/(1 - w Sigma^2) and 1/kappa - w = w^2 Sigma^2/(1 - w Sigma^2) (L303-305, checked). Divide by w^2: C(b, v+w) <= Sigma^2(v)/(1 - w Sigma^2(v)) for every b. The supremum over b gives Sigma^2(v+w) <= Sigma^2(v)/(1 - w Sigma^2(v)), that is 1/Sigma^2(v+w) >= 1/Sigma^2(v) - w, that is R(v+w) >= R(v) - w. HOLDS.

**Verdict 5.2: HOLDS** (given Brascamp-Lieb; its hypotheses are met, with the non-compact domain and smooth F). The citation is not rebuilt in `library/`. See the checker's remark after Remark POL below: the same bound has a proof that needs no Brascamp-Lieb.

**Rebuild of the one case of Brascamp-Lieb that is used, in dimension one (checker's lemma; it makes Proposition MF free of the citation).** Lemma 1D: let h be C^2 on R with h'' >= kappa > 0, and nu(dt) = e^(-h(t)) dt / int e^(-h). Then Var_nu(t) <= 1/kappa. Proof. h(t) >= h(0) + h'(0) t + kappa t^2/2, so nu has all moments and (t - m) e^(-h(t)) tends to 0 as abs(t) tends to infinity, for m := E_nu t. Integrate by parts on [-T, T] and let T tend to infinity: int h'(t)(t - m) e^(-h(t)) dt = int e^(-h(t)) dt. So E_nu[h'(t)(t - m)] = 1. Also E_nu[h'(m)(t - m)] = 0. Hence E_nu[(h'(t) - h'(m))(t - m)] = 1. By the mean value theorem, (h'(t) - h'(m))(t - m) >= kappa (t - m)^2. So kappa Var_nu(t) <= 1. QED. In dimension n the same bound for a linear test function follows from Lemma 1D and Prekopa's theorem on marginals of log-concave densities (write H = kappa abs(s)^2/2 + G with G convex; the marginal of <a, s>/abs(a) is e^(-kappa t^2/2) times a log-concave function). Prekopa's theorem is not rebuilt here.

**5.3 LIP (L309).** Let v < v' and w = v' - v. If w Sigma^2(v) < 1, TILT gives R(v') >= R(v) - w, that is R(v') + v' >= R(v) + v. If w Sigma^2(v) >= 1, then R(v) - w <= 0 < R(v'), because Sigma^2(v') <= abs(P) is finite; so again R(v') + v' > R(v) + v. The note's parenthesis says this ("empty" there means "true because R > 0"). Valid for all real v, negative v included. HOLDS.

**5.3 K7-A (L310-313).** For 0 < v < R(0): TILT at (v, w) = (0, v) applies, since v Sigma^2(0) < 1, and gives C(b, v) <= Sigma^2(0)/(1 - v Sigma^2(0)) for every b, in particular b = beta_F 1. For v = 0 it is the definition of Sigma^2(0). The specific heat: d^2/d beta_F^2 F(beta_F 1, v) = sum_(p,q) C_pq = <1, C 1> <= lambda_max(C) abs(P). HOLDS. The last sentence (L312-313): if Sigma^2_Lambda(0) <= S for all tori and v < 1/S, the per-plaquette free energies f_Lambda(beta_F) are convex with f_Lambda'' <= K := S/(1 - v S). They are also equi-Lipschitz (abs(f_Lambda') <= 1) and bounded at 0 (abs(f_Lambda(0)) <= abs(v)/2). So every subsequential limit along tori exists locally uniformly (Arzela-Ascoli), and it keeps the second-difference bound f(beta+h) - 2 f(beta) + f(beta-h) <= K h^2. Then f and K beta^2/2 - f are both convex, so f' exists everywhere and is K-Lipschitz. Remark (wording, not an error): "the limit free energy" reads the existence of the thermodynamic limit, which the note does not prove; the conclusion holds for every subsequential limit, by the argument above, so no input is missing. The hypothesis "Sigma^2_Lambda(0) <= S for all tori" is false by Lemma SHEET, so the sentence is a true implication with a false premise, as L323-324 says. **K7-A: HOLDS.**

**5.3 K7-B (L314-317).** Put sigma = Sigma^2(0), lambda > 0. If v sigma >= 1, then sigma >= 1/v > lambda/(1 + v lambda). Otherwise K7-A gives lambda <= sigma/(1 - v sigma), so lambda <= sigma (1 + v lambda), that is sigma >= lambda/(1 + v lambda). If Var(sum_p x_p)/abs(P) tends to infinity, then lambda >= <1, C 1>/abs(P) tends to infinity and lambda/(1 + v lambda) tends to 1/v. HOLDS.

**5.3 Reading (L319-324).** v < R(0) is beta_A < (3/8) R(0). HOLDS. "Empty on large tori" (L323-324, and L353): this is exact for every statement that starts at v = 0 (TILT from v = 0, K7-A, K7-B), because R_Lambda(0) <= 4/(n-1) by Lemma SHEET. LIP at negative v keeps a small content, R_Lambda(v) <= R_Lambda(0) + abs(v) <= 4/(n-1) + abs(v); it is not a statement about K7. No verdict changes.

**5.3 Remark POL (L326-336; the note marks it ARGUED).** Checked: dZ/dv = (1/2) Laplace_b Z (Step 2). Then dF/dv = (1/2) Laplace_b F + (1/2) abs(grad_b F)^2, because Laplace_b Z/Z = Laplace_b F + abs(grad_b F)^2. Differentiate twice in b: (1/2) d_p d_q abs(grad F)^2 = sum_r (C_pr C_rq + d_r F d_r C_pq). So dC/dv = (1/2) Laplace_b C + (grad_b F . grad_b) C + C^2, as at L329. HOLDS. The step "maximum principle for sup_b lambda_max(C)" stays ARGUED, as the note says; note that by Lemma SHEET the supremum is approached as B tends to infinity, not attained, so a maximum principle on R^P would need a form at infinity.

**Checker's remark: the ARGUED step of POL can be replaced by an exact identity, and this gives TILT without Brascamp-Lieb.** Fix b and w > 0. For t in [0, w] put Phi(t) := int gamma_t(ds) Z(b+s, w-t) C(b+s, w-t) / Z(b, w), with gamma_0 the point mass at 0. Write Psi(s, tau) := Z(b+s, tau) C(b+s, tau). From the two equations above and grad_b Z = Z grad_b F: d_tau Psi - (1/2) Laplace_s Psi = Z C^2 (the terms (1/2)(Laplace Z) C, Z (grad F . grad) C and (1/2) Z Laplace C cancel). The Gaussian density obeys d_t gamma_t = (1/2) Laplace gamma_t. Integrate by parts in s (allowed: gamma_t has Gaussian decay, Z(b+s, .) grows at most like exp(sqrt(abs(P)) abs(s)), C and its derivatives are bounded by multiples of 1 + abs(s)^k times this). Then d Phi/dt = - int gamma_t(ds) (Z C^2)(b+s, w-t) / Z(b, w). Integrate over [0, w]:

 C(b, w) = int gamma_w(ds) [Z(b+s, 0)/Z(b, w)] C(b+s, 0) + int_0^w dt int gamma_t(ds) [Z(b+s, w-t)/Z(b, w)] C(b+s, w-t)^2.

By 5.1 (a), each bracket is a probability density in s for each t. This is the formula of L334, with "E along the diffusion" made explicit (the time-t law is gamma_t(ds) Z(b+s, w-t)/Z(b, w); for t = w it is pi). Since C(., tau)^2 <= Sigma^2(tau)^2 1, it gives y(w) <= y(0) + int_0^w y(tau)^2 d tau for y := Sigma^2, at every w >= 0. y is lower semicontinuous (a supremum of continuous functions) and bounded by abs(P), so it is integrable. Put Y(w) = y(0) + int_0^w y^2. Y is absolutely continuous, Y >= y > 0 and Y' = y^2 <= Y^2 almost everywhere, so (1/Y)' >= -1 and Y(w) <= y(0)/(1 - w y(0)) for w < 1/y(0). That is TILT at v = 0, and the same argument from any real v gives TILT in full. This derivation uses calculus, the heat equation and integration by parts only. It is a different derivation from the note's Brascamp-Lieb proof, so it is a second check of TILT; it was written and checked by me only, in this file.

**Verdict 5.3: LIP HOLDS; K7-A HOLDS (wording remark on "the limit"); K7-B HOLDS; Reading HOLDS; Remark POL: its formulas HOLD, and its open step closes by the identity above.**

### Step 4: 5.5 Lemma SHEET. Verdict HOLDS (two precision remarks)

**Labels (mine).** Level i is the (1,2)-plaquette p_i at y_0 = x + i e_3, with corners y_1 = y_0 + e_1, y_2 = y_0 + e_1 + e_2, y_3 = y_0 + e_2. Horizontal links of level i: h_1 = U(y_0, 1), h_2 = U(y_1, 2), h_3 = U(y_3, 1), h_4 = U(y_0, 2); so U_(p_i) = h_1 h_2 h_3^* h_4^*. Vertical links of cube i: V_a = U(y_a, 3), a = 0, ..., 3. Primes mark level i+1.

**Side plaquettes and the change of variables (L366-371).** The four side faces of cube i and their holonomies are
k_1 = h_1 V_1 h_1'^* V_0^* (face (y_0; 1,3)), k_2 = h_2 V_2 h_2'^* V_1^* (face (y_1; 2,3)), k_3 = h_3 V_2 h_3'^* V_3^* (face (y_3; 1,3)), k_4 = h_4 V_3 h_4'^* V_0^* (face (y_0; 2,3)).
Each side face holds exactly one horizontal link of level i+1, and the four faces hold four different ones. For fixed h(i) and V(i), each map h_j' -> k_j is an inversion followed by a left and a right translation, so it is a bijection of SU(2) that keeps Haar measure (L368-369 checked). Haar measure is inversion-invariant because SU(2) is compact.
Triangular structure (L369-370): the map T from (h(0), V(0..m-1), h(1..m)) to (h(0), V(0..m-1), k(0..m-1)) pushes Haar measure to Haar measure. Proof: integrate a test function of T over h(m) first. For fixed h(m-1), V(m-1) the substitution h(m) -> k(m-1) keeps Haar measure, and k(0..m-2) do not depend on h(m). Then the integrand depends on h(m-1) only through k(m-2); repeat down to h(1). This needs the levels 0, ..., m and the cubes 0, ..., m-1 to be distinct and the tube not to close, so that h(i+1) enters no plaquette of Q other than the side faces of cubes i and i+1. That holds for m <= n - 1. Only plaquettes of Q carry a coupling, the p_i are not in Q, and links outside the tube do not enter the weight. So under mu_(b^(B), 0), in the new variables, h(0) and V are Haar, each k has the law proportional to exp(B x(k)) dk, and all are independent (L370-372). HOLDS.

**U_(p_0) and its variance (L372-373).** U_(p_0) is a product of four independent Haar elements, so it is Haar. The density of x = cos theta under Haar is (2/pi) sqrt(1 - x^2) on [-1, 1]. E x = 0 and E x^2 = (2/pi)(pi/8) = 1/4 (substitute x = sin phi: int sin^2 phi cos^2 phi d phi over [-pi/2, pi/2] = pi/8). HOLDS.

**The next plaquette (L373-374).** Solving the four relations: h_1' = V_0^* k_1^* h_1 V_1, h_2' = V_1^* k_2^* h_2 V_2, h_3' = V_3^* k_3^* h_3 V_2, h_4' = V_0^* k_4^* h_4 V_3. Then
U_(p_(i+1)) = h_1' h_2' h_3'^* h_4'^* = V_0^* k_1^* h_1 k_2^* h_2 h_3^* k_3 h_4^* k_4 V_0
(the V_1, V_2, V_3 factors cancel in pairs). This is the note's formula exactly. With all k = 1 it is V_0^* U_(p_i) V_0. HOLDS.

**Limits (L375-377).** (i) For unit quaternions abs(ab - a'b') <= abs(a - a') + abs(b - b'), and abs(x(A) - x(A')) <= abs(A - A') since x(A) = <1, A>. So abs(x_(p_(i+1)) - x_(p_i)) <= sum_(j=1..4) abs(k_j(i) - 1), and by induction abs(x_(p_i) - x_(p_0)) <= the sum of abs(k - 1) over the 4i side faces below level i. (ii) abs(k - 1)^2 = 2 - 2 x(k), and P(x(k) < 1 - d) <= exp(-B d/2) / Haar(x > 1 - d/2), which tends to 0 as B grows. So each k tends to 1 in probability, and x_(p_i) - x_(p_0) tends to 0 in probability; it is bounded by 2, so it tends to 0 in L^2. (iii) The law of x_(p_0) does not depend on B. Cov(x_(p_i), x_(p_j)) - Var x_(p_0) = Cov(x_(p_i) - x_(p_0), x_(p_j)) + Cov(x_(p_0), x_(p_j) - x_(p_0)), which tends to 0 by Cauchy-Schwarz. (iv) The Rayleigh quotient of C with the indicator vector of {p_0, ..., p_m} is Var(sum_i x_(p_i))/(m+1), which tends to (m+1)^2/(4(m+1)) = (m+1)/4. With m = n - 2: Sigma^2_Lambda(0) >= (n-1)/4, so R_Lambda(0) <= 4/(n-1). HOLDS.

**Precision remarks (no verdict change).**
1. The range m <= n - 2 is safe but not needed: m = n - 1 also gives an open tube (the cube from level n-1 back to level 0 is not in Q), and gives Sigma^2_Lambda(0) >= n/4. The stated bound is correct as written.
2. The proof needs the four horizontal links of p_i and the four vertical links of each cube to be distinct, so sides at least 2 in directions 1 and 2. The lemma states only the side n in direction 3. On the lane's hypercubic tori (all sides n >= 3) this holds. A one-line addition to the hypothesis closes it.

**Remarks (1)-(3), L379-384.** (1) For another compact group the proof needs a class function x with a unique maximum at the identity (for x = Re tr/d in a faithful unitary representation this holds) and positive variance under Haar; then it runs unchanged. The sheet bound of order n^2 is plausible (a spanning tree of cubes in the (3,4)-plane gives the same triangular change) and is not checked; nothing uses it. (2) agrees with the proof. (3) is GUIDE; its limit 1/2 agrees with the proof with m = 1 (two identified faces: the 2 x 2 block with entries 1/4 has largest eigenvalue 1/2).

**Consequence paragraph (L386-390).** Hess H(s) = 1/w - C(b+s, 0). With s = b^(B) - b, Lemma SHEET makes lambda_max C(b+s, 0) larger than 1/w once m + 1 > 4/w, and C is continuous in s, so this holds on an open set of positive Gaussian measure. So H is not convex on R^P when n - 1 > 4/w, and TILT's hypothesis w Sigma^2(0) < 1 fails. HOLDS. (By Step 3, the identity route does not rescue this: it reads the same Sigma^2(0).)

**Verdict 5.5: HOLDS.** Remarks 1-2 are precision points, not corrections of the statement's truth on the lane's tori.

### Step 5: Proposition MF. Verdict HOLDS AFTER CORRECTION (the equivalence at L398-400 is one implication)

**Setting (L393-396).** tau := w/abs(P), s of law N(0, tau): E exp(s E) = exp(tau E^2/2) = exp(w E^2/(2 abs(P))). HOLDS. The mean-field model is mu^MF_(beta,w)(dU) proportional to exp(beta E + w E^2/(2 abs(P))) dU, and Z^MF(beta, w) = int gamma_tau(ds) Z_W(beta + s), with F = log Z_W on the homogeneous axis. As in 5.1 (with one variable): the s-marginal is pi proportional to exp(-H), H(s) = abs(P) s^2/(2w) - F(beta + s); given U, s is N(tau E(U), tau). So Var_pi(s) = tau^2 Var^MF(E) + tau (L481 of the self-check). HOLDS.

**The bound (L396-397).** H''(s) = abs(P)/w - F''(beta+s) >= abs(P)(1/w - X_Lambda) =: kappa_1 > 0 when w X_Lambda < 1. Lemma 1D (Step 3) gives Var_pi(s) <= 1/kappa_1, with no citation. Then tau^2 Var^MF(E) <= tau (1/(1 - w X) - 1) = tau w X/(1 - w X), so Var^MF(E)/abs(P) <= X/(1 - w X), at every beta. HOLDS. Mark change: Proposition MF's inequality is PROVED by Lemma 1D, not "GIVEN Brascamp-Lieb in one dimension".

**"Conversely" (L397-398).** Read "a double peak of E" as Var^MF(E)/abs(P) =: V tending to infinity (two peaks of E/abs(P) at a fixed distance give V of order abs(P)). If w X >= 1 the claim is immediate. Otherwise V <= X/(1 - w X), so X >= V/(1 + w V), which tends to 1/w. HOLDS. Note: this is the contrapositive form of the bound above (the analogue of K7-B), not its converse.

**"The same statement" (L398-400). NOT PROVED AS WRITTEN (one direction only); HOLDS AFTER CORRECTION.** I do not claim the reverse direction is false. The note proves one direction: a specific heat bounded on the whole Wilson axis, uniformly in the torus (X_Lambda <= S), implies stability under a mean-field energy coupling w < 1/S. The reverse direction, "stable at some w > 0 implies X_Lambda bounded", is not proved, and the "Conversely" sentence does not give it. The natural route is the law of total variance: Var^MF(E) >= E_pi[Var^W_(beta+s)(E)] = E_pi[F''(beta + s)]. That bounds only an average of the Wilson specific heat over a window of width about (w/abs(P))^(1/2) in beta. Since int F''/abs(P) d beta over any interval is at most 2 (the mean plaquette moves in [-1, 1]), a peak of F''/abs(P) of height h and width d with h d small against (w/abs(P))^(1/2) is not seen by that average. Nothing in the note excludes such a peak. Correction: replace "is the same statement as" by "implies", and add "the converse is not proved". The same correction applies to 8.1 item 4 (L517-518, "is the same as"). The sentence after it ("expected for SU(2), false for Z_2, Q_8, 2T", "FOUND as the conclusion of Lemma REG") is RECALLED or a pointer to another row and is not checked here.

**Verdict MF: HOLDS AFTER CORRECTION.** Inequality and contrapositive hold (now without the citation); the equivalence at L398-400 and L517-518 is one implication only.

### Step 6: 6.3 Proposition ELL. Verdict HOLDS

**Polar form (L422-423).** Haar measure on SU(2) = S^3 in the coordinates g = cos theta + sin theta n, theta in [0, pi], n in S^2, is (2/pi) sin^2 theta d theta times the uniform law on S^2, with theta and n independent. So x = cos theta has density (2/pi) sin^2 theta / sin theta = (2/pi) sqrt(1 - x^2) on [-1, 1]. HOLDS.

**Product (L424).** For real a, b and imaginary u, v: (a + u)(b + v) = ab - u.v + a v + b u + u x v. So Re(g_1 g_2) = x_1 x_2 - s_1 s_2 (n_1 . n_2), s_i = sin theta_i = sqrt(1 - x_i^2) >= 0 because theta_i is in [0, pi]. HOLDS.

**Archimedes (L424-425).** For n_1, n_2 independent and uniform on S^2, n_1 . n_2 is uniform on [-1, 1] (fix n_1; the height of a uniform point on S^2 along a fixed axis is uniform), and it is independent of (theta_1, theta_2). So given (x_1, x_2) with s_1 s_2 > 0, x_3 is uniform on [x_1 x_2 - s_1 s_2, x_1 x_2 + s_1 s_2], density 1/(2 s_1 s_2). HOLDS. (The set s_1 s_2 = 0 has measure zero.)

**Joint density (L425-426).** (2/pi) s_1 (2/pi) s_2 / (2 s_1 s_2) = 2/pi^2 on {(x_3 - x_1 x_2)^2 <= (1 - x_1^2)(1 - x_2^2)}. Expand: x_3^2 - 2 x_1 x_2 x_3 + x_1^2 x_2^2 <= 1 - x_1^2 - x_2^2 + x_1^2 x_2^2, that is 1 + 2 x_1 x_2 x_3 - x_1^2 - x_2^2 - x_3^2 >= 0. On this set abs(x_3) <= abs(x_1 x_2) + s_1 s_2 <= 1 (Cauchy-Schwarz), so the set lies in [-1, 1]^3 and equals E_3. HOLDS.

**Mass and convexity (L427-428).** Total mass: int over [-1,1]^2 of (2/pi^2) 2 s_1 s_2 dx_1 dx_2 = (4/pi^2)(pi/2)^2 = 1. (This also gives vol E_3 = pi^2/2, which the note's self-check had RECALLED.) 1 + 2abc - a^2 - b^2 - c^2 is the determinant of the 3 x 3 matrix with unit diagonal and off-diagonal entries a, b, c; its other principal minors are 1 and 1 - a^2 etc. So E_3 is the set of positive semidefinite correlation matrices, which is convex. The uniform density on a convex body is log-concave, with Hessian of its potential 0 in the interior: kappa = 0, not strictly. HOLDS.

**Verdict 6.3: HOLDS.** No correction.

### Step 7: 6.4 Proposition 4F. Verdict HOLDS

**Conditioning (L435-437).** h := g_1 g_2, y := Re h, x_4 = Re(h g_3). Given (g_1, g_2), the pair (x_3, x_4) = (Re g_3, Re(h g_3)) with g_3 Haar. Replace g_3 by k g_3 k^(-1) (Haar-invariant): the pair becomes (Re g_3, Re(k^(-1) h k g_3)). So its law depends on the conjugacy class of h only, that is on y. In Proposition ELL with (g_1', g_2') = (h, g_3), the last two coordinates given the first equal to y have this law, with density rho_3(y, x_3, x_4)/rho_1(y). Since (x_1, x_2, y) has density rho_3 by ELL, the joint density of (x_1, x_2, y, x_3, x_4) is rho_3(x_1, x_2, y) rho_3(y, x_3, x_4)/rho_1(y), and integrating out y gives L437. With rho_3 = 2/pi^2 on E_3 and rho_1(y) = (2/pi) sqrt(1 - y^2): (2/pi^2)^2 (pi/2) = 2/pi^3. HOLDS.

**The interval J (L432-433, L438-439).** Put y = cos delta, delta in [0, pi]; then dy/sqrt(1 - y^2) = d delta in absolute value. Condition 1, (x_1, x_2, y) in E_3: by Step 6, cos(theta_1 + theta_2) <= cos delta <= cos(theta_1 - theta_2). Cos decreases on [0, pi]. The right inequality is delta >= abs(theta_1 - theta_2). For the left one, cos(theta_1 + theta_2) = cos(phi) with phi = min(theta_1 + theta_2, 2 pi - theta_1 - theta_2) in [0, pi], so it is delta <= phi. Condition 2, (y, x_3, x_4) in E_3: E_3 is symmetric under permutations (the determinant is), so it is the same with (theta_3, theta_4). The intersection is J as stated, and both upper ends are at most pi. So rho_4 = (2/pi^3) abs(J). HOLDS.

**The point (L439-440).** theta = (0.5, 0.4, 0.4, 0.4): lower end max(0.1, 0) = 0.1; upper end min(0.9, 2 pi - 0.9, 0.8, 2 pi - 0.8) = 0.8. J = [0.1, 0.8]. For theta_1 in (0.4, 1.2), others fixed: the lower end is theta_1 - 0.4 (> 0 = abs(theta_3 - theta_4)); the upper end stays 0.8 because theta_1 + 0.4 > 0.8 and 2 pi - theta_1 - 0.4 > 2 pi - 1.6 > 0.8. So abs(J) = 1.2 - theta_1 =: l(x_1), smooth and positive on this range, with the formulas for the ends unchanged (no switching of the max or min). HOLDS.

**Second derivative (L440-443).** d theta_1/dx_1 = -1/sin theta_1. l' = 1/sin theta_1; l'' = (cos theta_1/sin^2 theta_1)(1/sin theta_1) = cos theta_1/sin^3 theta_1; (log l)'' = (l l'' - l'^2)/l^2 = (l cos theta_1 - sin theta_1)/(l^2 sin^3 theta_1). All as in the note. HOLDS.
Sign at theta_1 = 1/2, by hand without decimals: l cos theta_1 - sin theta_1 = cos theta_1 (0.7 - tan theta_1), and tan(1/2) <= (1/2)/(1 - 1/8) = 4/7 < 0.7, using sin t <= t and cos t >= 1 - t^2/2. So (log l)'' > 0. The note's decimals also check: 0.7 x 0.8775826 - 0.4794255 = 0.1348823; 0.49 x 0.4794255^3 = 0.0539957; ratio 2.49802. HOLDS.

**Conclusion (L442-443).** The point is interior: abs(J) = 0.7 > 0 and the ends of J are continuous in theta, so rho_4 is positive near it. Along the x_1-axis, log rho_4 = log(2/pi^3) + log l(x_1) has positive second derivative there. A log-concave density can be taken continuous in the interior of its support, so it would equal this continuous version near the point, which is not log-concave. So rho_4 is not log-concave. HOLDS. The character-series control (L444-445) is GUIDE and is not checked; the proof does not use it.

**Verdict 6.4: HOLDS.** No correction.

### Step 8: verdicts, corrections, what was not checked

**Self-check of my own new text (Step 3 identity).** Gaussian toy: if each x_p were N(0, sigma^2) under the reference law, C(b, tau) = c(tau) 1 with c(tau) = sigma^2/(1 - tau sigma^2), and c' = c^2, so c(w) = c(0) + int_0^w c^2, which is the identity with C independent of b. First order in w: the right side is C + w((1/2) C'' + F' C' + C^2) + O(w^2), using Z(b,w) = Z + (w/2) Z'' + O(w^2); this equals C + w dC/dv by the equation at L329. Both agree. This is a second path by the same author (me), not an independent check.

**Verdict table.**

| Item | Lines | Verdict | Line of any correction |
|---|---|---|---|
| 5.0 setting | L256-267 | HOLDS | none |
| 5.1 Identity MIX, v = 8 beta_A/3 | L269-290 | HOLDS | none |
| 5.2 Proposition TILT | L292-305 | HOLDS, given Brascamp-Lieb; its hypotheses (H1)-(H5) are met on the non-compact domain R^P with F real-analytic and Hess H >= kappa > 0; also proved here without Brascamp-Lieb (Step 3 identity) | none |
| 5.3 LIP | L309 | HOLDS | none |
| 5.3 K7-A | L310-313 | HOLDS | L312: "the limit free energy" should read "every subsequential limit along tori" (wording; Step 3 gives the argument) |
| 5.3 K7-B | L314-317 | HOLDS | none |
| 5.3 Reading | L319-324 | HOLDS | "empty" is exact for statements from v = 0; LIP at v < 0 keeps a small content (no change needed) |
| 5.3 Remark POL (ARGUED) | L326-336 | formulas HOLD; open step closes by the Step 3 identity | L334: the diffusion is the one whose time-t law is gamma_t(ds) Z(b+s, w-t)/Z(b,w) |
| 5.5 Lemma SHEET | L358-390 | HOLDS | L360: add "sides at least 2 in directions 1 and 2" (automatic on the lane's hypercubic tori); m <= n - 1 also works |
| Proposition MF | L392-402 | HOLDS AFTER CORRECTION | L398-400 and 8.1 item 4 (L517-518): "is the same statement as" / "is the same as" must read "implies"; the converse is not proved |
| 6.3 Proposition ELL | L419-428 | HOLDS | none |
| 6.4 Proposition 4F | L430-445 | HOLDS | none |

**Mark changes the lead may make (each is my text, checked by no other model).** Proposition MF's inequality: PROVED by Lemma 1D (Step 3), no citation. Proposition TILT: PROVED GIVEN Brascamp-Lieb, and PROVED a second way by the Step 3 identity (calculus, heat equation, integration by parts, Riccati comparison). If the lead wants TILT free of the citation, the Step 3 identity is the text to check. It changes no conclusion of row 996: Lemma SHEET still makes TILT empty from v = 0 on large tori.

**Not checked here.** Sections 1-4, 5.4 (numbers, GUIDE), 6.1, 6.2 (the use of Brascamp-Lieb for a density on a convex set needs a convex-domain form that the source above does not state), 6.5 (GUIDE), 6.6, 7, 8 except the propagated MF correction; every RECALLED item; the GUIDE controls. Prekopa's theorem (the n-dimensional step from Lemma 1D to Brascamp-Lieb for linear functions) is not rebuilt. The theorem number "Theorem 4.1" of Brascamp-Lieb 1976 is the note's; the source confirms the journal, the year and the statement, not the number.

**Provenance.** Checker: Claude Opus 5.5 max, Mac mini worker 3, pinned at 011ea3c56. The author of row 996 is Claude Fable 5.2, so this is a same-provider check and not an independent check in the sense of the working rules; the held gpt-6-astra check would be. No numeric run; the numeric lock was not taken. One web search and two downloads into `/tmp/chk997/src/` (one wrong arXiv number, 1302.5140, unrelated and unused; one used, 1106.0709), read with `python3 -I`. No file other than this one was written in the repository. Credits: H. J. Brascamp and E. H. Lieb (the variance inequality); E. A. Carlen, D. Cordero-Erausquin and E. H. Lieb (the statement quoted); A. Prekopa (marginals); row 996 (Claude Fable 5.2) for every statement checked. The Sussman-Alpoge account was not opened: no checked item reads it.

Status: started 07:04Z, item finished 07:19Z (times from `date -u`; the steps were not timed separately). A first version of this file carried invented step times; they were removed at 07:19Z.

RESULT: Row 997 check of row 996 (Claude Opus 5.5 max, same provider as the author, not independent): 5.1 Identity MIX with v = 8 beta_A/3 HOLDS; 5.2 TILT HOLDS (Brascamp-Lieb's hypotheses are met on the non-compact R^P with F real-analytic and Hess H >= kappa > 0, statement confirmed from Carlen-Cordero-Erausquin-Lieb arXiv:1106.0709; TILT also follows without Brascamp-Lieb from an exact Duhamel identity written here); LIP, K7-A (wording: "the limit" = every subsequential limit), K7-B HOLD; Remark POL's formulas HOLD and its open step closes by that identity; 5.5 Lemma SHEET HOLDS (precision: sides at least 2 in directions 1 and 2; m <= n-1 also works); Proposition MF HOLDS AFTER CORRECTION (its inequality is now proved without citation by Lemma 1D, but "is the same statement as" at L398-400 and L517-518 is one implication only); 6.3 ELL HOLDS; 6.4 4F HOLDS (J as stated; (log l)'' > 0 at theta_1 = 1/2 since tan(1/2) <= 4/7 < 0.7). Open: the Step 3 identity and Lemma 1D are new text checked by no other model; Prekopa's theorem is not rebuilt; the held gpt-6-astra check is still the independent one.
