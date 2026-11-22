lead: anthropic/claude-fable-5-2/medium mac-mini-worker
lease_until: 2026-11-23T02:56Z

# gap-univk-str: the structural input (STR) of the logarithmic two-cutoff comparison (row 1398)

Provenance: Claude Fable 5.2, medium effort, Mac mini worker 2, at commit 778392267. Started 2026-11-22T14:56Z (date -u). Working state, not an audit; nothing here is a public claim.

Credit: the objects under study (the resolved interpolation, the assembly formula P_h, the stored units, the summed first variation, the ramp move) are from the complete account of Ethan Sussman and Levent Alpoge (with Claude and Codex as authors of their text), part III, and YM4_1400.tex. The reduction (LOG) to (STR)+(RAR) is row 1395; the corrected form of (STR) is check 1397 (gpt-6.2-astra).

## 0. Plan (written before reading)

Target: decide (STR) in the corrected form of check 1397, section 'An admissible repair of STR': along the ordinary common interpolation with A ramps, for every lambda and each recent direction z = (b, t), the restricted aligned sum with the fixed good-label projection, on its actual transverse fibre, is either positive with convex logarithm on (-R_z, R_z) or zero-free on the disc of radius R_z, R_z >= E_1/l_b; same for the ramp and stop-production move.

Steps, one per response, each appended here:

1. Read row 1395 sections 2, 4, 6, 8 and check 1397 in full; record the exact statement of (STR) and what the consumer needs.
2. Repo search: grep open-core.md and FINISH rows for (STR), aligned sum, good-label projection, diagonal fibre, zero-free; cite matches.
3. Read the account: CA-III 11962-11974 (P_h, stored units), 12104-12124 (diagonal fibres), 13621-13686 (conditional holomorphy), 13931 and 17436 ((c2)*), 17449-17459, 17561-17575 (summed first variation), 17679-17714 (ramp move); YM4_1400 L130223-130350.
4. Decide: prove one alternative for the summed retained function, or build a recent unit inside the account's stated bounds for which both fail with positive density.
5. Next two rows with decisive outcomes; RESULT line.

## 1. Repo search and the statement to decide (written after reading row 1395 and check 1397 in full)

Repo search (this lane folder; `origin/main` and the PR branches are not refs in this checkout; check 1397 L5-L7 ran the five-ref search for `restricted aligned sum|gap-univk-str` on 2026-11-22 and found no hit).
- `library/open-core.md`: zero hits for (STR), restricted aligned, good-label, diagonal fibre, zero-free, log-convex.
- FINISH rows with (STR): 1395, 1397, 1398 only.
- On file and used, not redone: row 1395 Theorem A/B (convex or zero-free chain), Lemma EXP, examples (E1), (E2); check 1397's diagonal-fibre repair of (STR) with the differential inequality |d'| <= s d, its example F(s) = 1 + 4s(1-s)/R^2 (LOG exact, STR false), and its source verdict that III 13621-13686 "supplies conditional holomorphy, exact ends and reading-level incidence, not positivity or a zero-free restricted sum" and that outline OH1 (23388-23404) "explicitly assumes nonnegative zero-source label measures".

**(STR*), the statement to decide (check 1397 L48, L110).** Let G be the fixed good set of labels (aligned, no live component of age a_0 or more), and for a point of the dial domain D* (III 12104-12124) let F := sum over h in G of tau_h[x](V_w), zero source, real centres, ramps of A. For every lambda in [0, 1] and every recent direction z = (b, t) (b >= k - a_0), the function eps -> F(lambda; eps e_z) on the fibre through the diagonal point lambda is (cvx*) positive with convex logarithm on the real interval (-R_z, R_z), or (zf*) free of zeros on |eps| < R_z, with R_z >= E_1/l_b. The same for the parameter s of the ramp and stop-production move (III 17679-17714).
The consumer (Theorem E as corrected by check 1397) needs it for every lambda, at every matched real centre in the window, on T_ell and T_(L ell).

## 2. What the account says about how the array enters a label term (READ; "III n" = line n of LOCAL:ym4d-papers/sa-ca)

READ in this step: III 11804-12170, 13621-13790, 13915-13945, 17405-17600, 17640-17730.

2.1 **The label term.** tau^c_h is "the h-th term chi T^w e^(A^w - E^c) of that expansion, read as a complex Borel measure", chi "the product of the characteristic functions of the label", T^w "the large-field operation at the stop", A^w "the effective action at the stop" (III 11855-11862). "tau_h[x; t^A]" is "the V_w-marginal of an integrand that P_h assembles from the array", and "That integrand is entire in the entries of the array" (III 17436-17441). Norms are total variations on the chart space (Omega_h, mu_h) "of the label's common inner variables" (III 11884-11886).

2.2 **No positivity statement.** A grep of III 11000-19000 for nonnegative / non-negative / positive measure / signed / real-valued finds no statement that tau_h[x^(lambda, eps)] is a nonnegative measure at real arrays; the only reality statement on the dial domain is "the data s^0 and D^0 are real" (III 17490). The proof of the modulus bound says "Neither a Schwarz-type step nor any cancellation between different labels is used" (III 17517). This agrees with check 1397 L99-L100 (the outline's OH1 assumes nonnegative zero-source label measures as a hypothesis).

2.3 **The array is not of exponent type only.** The proof of the resolved interpolation lemma (III 13709-13775) lists how slots move on the dial domain:
 (x) slots of direct uses and of stored terms: "A slot u of a resolved stored term B carries the value (1-lambda) x_u^A + lambda x_u^B + eps G_u^(n)" (III 13715-13719), read through an "activity per cell" and a "value per cell" (III 13727-13740). These are the units of the effective action and the stored boundary terms.
 (o) "At the T-site, operator slots again carry a convex combination of the two runs' values. It lies in the tolerance ball of the tolerance lemma of the T-site. The class-n pieces, at |eps| <= Lambda_z, move this combination by at most |eps| d^op_n" with |eps| d^op_n <= (1/4) m_G^T (III 13742-13762). The operator direction W^(z),op "consists of the class-n pieces of Lemma zone-split: the operator pieces, the potential pieces and the normaliser pieces" (III 13928).
 (a) "Among the class pieces at the T-site, those that enter as potentials have activity |eps| d^op_n eps-bar^pr [...] The remaining class pieces enter additively and need no such factor" (III 13767-13775).
So a class z = (n, k') carries, besides exponent units, operator, potential and normaliser pieces of the T-sites and pieces that enter additively. Lemma EXP of row 1395 covers (x) only, and only if the remaining factor is a nonnegative density.

2.4 **Incidence (ported, III 17522-17548 and 13664-13686).** eps_z enters tau_h only if zone j is present in h at level k', inside a component live at k' (untouched, second-class with omega_Y kept in the label, or arrested); for j <= k-2 this forces a live component of age >= k-j-1 at the stop. So for the good set G (no live component of age >= a_0) only classes with j >= k - a_0 occur, and a class with j >= k-1 can be read by every label with a large-field region.

2.5 **The ramp and stop-production move (III 17679-17714).** (m3) "replaces the ramps by t^A + s(t^B - t^A), and at the same time it interpolates the small slots of the production block P at the stop level"; the slots "read V_k only [...] and there are at most N_w^4 of them", each with |eta^A + s(eta^B - eta^A)| <= (1 + 20 C_chi theta_chi^k |s|) 1{f^B < (1+varpi_0)c}; the disc is |s| <= (20 C_chi N_w^4 theta_chi^k)^(-1). The slots are multiplicative factors of the integrand (the integrand of a label is "a product prod_iota v_iota over its components", III 17726), affine in s. They are not exponents.

## 3. A weaker sufficient structure than (STR*): positivity plus a bounded non-affine part (PROVED, elementary; unchecked)

Section 2.3 shows that exact log-convexity by Lemma EXP of row 1395 cannot be read off slot by slot: the operator direction of a class contains potential-type pieces that need not be affine in the dial. The next statement tolerates them. It replaces (cvx*) and is implied by neither alternative of (STR*) nor implies one; like (STR*) it carries no rate and no comparison of cutoffs, so it is not equivalent to (LOG) (the separation examples of check 1397 L107-L108 apply unchanged).

**3.1 Lemma SEMI (one fibre).** Let G be countable, (Omega_h, mu_h) measure spaces with mu_h >= 0, R > 0, kappa >= 0, and for eps in (-R, R)
  F(eps) := sum_(h in G) integral f_h(omega) exp( eps a_h(omega) + phi_h(omega, eps) ) d mu_h(omega),
with f_h >= 0 and a_h real measurable (no bound on a_h is asked), phi_h real with eps -> phi_h(omega, eps) + kappa eps^2/2 convex on (-R, R) for every omega (for C^2 functions: d^2 phi_h/d eps^2 >= -kappa). Assume 0 < F < infinity on (-R, R). Then
 (i) eps -> log F(eps) + kappa eps^2/2 is convex on (-R, R);
 (ii) if also log F <= Lambda on (-R, R) and F is differentiable at 0, then | (log F)'(0) | <= (Lambda - log F(0))/R + kappa R/2.
Proof. (i) For every omega the function eps a + phi + kappa eps^2/2 is convex, so the integrand times e^(kappa eps^2/2) is nonnegative and log-convex in eps. A sum or integral of nonnegative log-convex functions is log-convex (Holder, as in Lemma EXP of row 1395 4.5, on the disjoint union of the Omega_h). (ii) g := log F + kappa eps^2/2 is convex, g(0) = log F(0), g'(0) = (log F)'(0), and g <= Lambda + kappa R^2/2. For 0 < r < R convexity gives [g(0) - g(-r)]/r <= g'(0) <= [g(r) - g(0)]/r. Since g(r) and g(-r) are at most Lambda + kappa R^2/2, both outer members are at most (Lambda + kappa R^2/2 - g(0))/r in absolute value on the side that matters: g'(0) <= (Lambda + kappa R^2/2 - g(0))/r and g'(0) >= -(Lambda + kappa R^2/2 - g(0))/r. Let r -> R. QED

**3.2 Lemma SEMI-C (from a sup bound on a complex disc).** If phi(omega, .) is holomorphic on |eps| < R_z, real on the real axis, and |phi(omega, eps)| <= M there, then on the interval (-R_z/2, R_z/2) it satisfies 3.1 with kappa = 8M/R_z^2.
Proof. Cauchy's inequality on the disc of radius R_z/2 about a real point eps with |eps| <= R_z/2: |phi''(eps)| <= 2M/(R_z/2)^2. QED

**3.3 Theorem S (chain along the diagonal; replaces the fibre condition in check 1397 L48-L56).** Let F(lambda), 0 <= lambda <= 1, be the restricted good sum on the diagonal of the dial domain, and G_z(lambda, eps) its value on the z-fibre. Assume
 (S0) the summed first variation on every subsegment: F is C^1 on [0, 1] with F'(lambda) = sum_z d/d eps G_z(lambda, eps) at eps = 0 (the account's first-variation statement, III 17561-17575, as used by check 1397; ported, not rechecked here), and classes not read by a label of G contribute zero (2.4);
 (S1) (POS-SEMI) for every lambda and every class z read by G, the function eps -> G_z(lambda, eps) has on (-R'_z, R'_z) the form of 3.1 with a constant kappa_z, and G_z <= e^Lambda there;
 (S2) F(0) > 0.
Put d(lambda) := Lambda - log F(lambda), s_1 := sum_z 1/R'_z, s_2 := sum_z kappa_z R'_z/2 (sums over the classes read by G). Then F > 0 on [0, 1] and
  d(0) e^(-s_1) - (s_2/s_1)(1 - e^(-s_1)) <= d(1) <= d(0) e^(s_1) + (s_2/s_1)(e^(s_1) - 1),
so | log F(1) - log F(0) | <= ( d(0) + s_2/s_1 ) ( e^(s_1) - 1 ).
Proof. Let U be the connected component of 0 in the open set {lambda : F(lambda) > 0}. For lambda in U and a class z, G_z(lambda, 0) = F(lambda) > 0, so some f_h is not almost everywhere zero and G_z(lambda, eps) > 0 on the whole real fibre; 3.1 applies. By 3.1(ii) on each fibre and (S0), |d'(lambda)| <= s_1 d(lambda) + s_2 on U. The integration below bounds d on U, so log F is bounded below on U; F is continuous, hence F > 0 at the right end of U, and U = [0, 1]. Then (e^(-s_1 lambda)(d + s_2/s_1))' <= 0 and (e^(s_1 lambda)(d + s_2/s_1))' >= 0; integrate. QED

**3.4 Corollary (extensive form).** If Lambda = E_+^sharpsharp N_w^4, F(0) >= e^(-C' N_w^4), R'_z = R_z/2 with R_z >= E_1/l_b, and the non-affine part of each fibre obeys the sup bound of 3.2 with M = M_phi N_w^4, then kappa_z R'_z/2 = 2 M_phi N_w^4/R_z, s_1 = 2 sum_z 1/R_z, s_2/s_1 = M_phi N_w^4, and
  | log F(1) - log F(0) | <= ( E_+^sharpsharp + C' + M_phi ) N_w^4 ( e^(s_1) - 1 ),   s_1 <= (2/E_1) sum over recent classes of l_b <= (2/E_1) q_a^(-(a_0-1)) Sigma_k^(q_a).
This is the retained endpoint bound of check 1397 L50-L56 with the same s (their coefficient 2 for the zero-free alternative, here from halving the interval) and d_0 enlarged by the torus-proportional constant M_phi N_w^4. Theorem E of row 1395, in the corrected form of check 1397 L76, therefore holds with (H2) replaced by (S1) for the recent classes.

**3.5 What (S1) asks of the assembly formula, slot type by slot type (ARGUED from 2.3; the form of P_h itself is NOT printed in the lines read).**
 (S-form) On the label's chart, at real (lambda, eps) of the dial domain, zero source and real centres, the density of tau_h[x^(lambda, eps); t^A] against the dial-free reference measure is f_h exp( sum of real slot terms ), with f_h >= 0 free of eps (characteristic functions at the ramps of A, delta factors, Haar and Gaussian reference weights).
 Given (S-form):
 - (x) list slots, stored boundary and derived terms, vacuum constants, z-pieces: the slot value is affine in eps (III 13715-13719), so these go into a_h. No bound is needed.
 - (o1) the fluctuation covariance D and the first form F as kernels (III 12609-12611): a quadratic form in inner variables, affine in the kernel, so affine in eps; into a_h. This holds also on large-field components where the inner variable is not small.
 - (o2) the walk operator Gamma, the potentials Psi, Phi, the Jacobians and sigma(g_i B) (III 12612-12613), if they enter through compositions: not affine. The account bounds their class-n pieces on the disc in Balaban's activity norm by |eps| d^op_n eps-bar^pr <= (E_1^z/(E_0 C^natural_cl)) eps-bar^pr per unit (III 13767-13772), a sup bound on the complex disc. If that sup bound sums to M_phi N_w^4 over the polymers of the label, 3.2 gives (S-semi).
 - (o3) the normaliser, "localised as a sum" (III 12614-12615), entering "additively" (III 13774): affine if it sits in the exponent; if it enters as a reciprocal factor 1/(N + eps dN) with N + eps dN > 0 on the interval, that factor is log-convex in eps; if it enters as a factor N + eps dN it is log-concave with (log)'' = -(dN/(N + eps dN))^2, and the relative bound of III 12729-12732 (|dL^(n)(X'')| <= (d^op_n/C^T_cl) C_F L-bar(X'')) with |eps| d^op_n <= m^T_G/4 gives kappa of order (number of pieces)/R_z^2, again inside 3.1.
So every listed unit type is compatible with (S1) GIVEN (S-form) and the summability of the (o2) sup bounds; no listed unit type forces a failure. What is missing in the account is (S-form) itself: positivity of the assembled density at real dials.

 - Remark 3.6 (direct form for the mark direction; the proposal of check 1392, "a uniform bound on the actual log derivative along a common real interpolation", made concrete). GIVEN (S-form), the derivative of log G_z at eps = 0 is the mean of a_h + d phi_h/d eps in the probability measure proportional to the density. For the units of type (x) the account's "value per cell <= |eps| K(d) y_n" (III 13736-13740) is a pointwise bound |a_h| <= K(d) l_b (number of cells of the zone met), so that part of the log derivative is at most K(d) l_b N_w^4 with no disc, no majorant and no convexity. For (o1) on large-field components a_h is a quadratic form in an inner variable that is not small, so no pointwise bound is available; there Lemma SEMI is the tool, because it asks no bound on a_h.

## 4. Positivity at the physical end points: what Balaban's text says (READ in LOCAL:ym4d-papers/cmp122b.txt, an OCR text; formulas not legible, sentences are) (written 15:06Z by date -u)

Tadeusz Balaban, Large field renormalization II (CMP 122), section 1, after the definition (1.71) of the operation T'_k(X) and the definition (1.72) of the R-operation: "All the expressions in the definition (1.71), for the configuration U, are real, and the exponential density in the integral is positive" and "The expression T'_k(X, (U, 0)) 1 is obviously positive, although it may be very small" (text lines 1264-1273). The Mayer expansion of the curly bracket of (1.72) is exponentiated again, "{...} = exp R'^(k) = exp sum R'^(k)(X)" (1.98) (text lines 1668-1777), so no signed cluster term stays as a term of the density; the sum that stays in the label is over the large-field sequences and the Euclidean frames r of (1.71).
Consequence (ARGUED, unchecked; it is a reading of Balaban, not of the account): at a real configuration and zero source, each term of one run's density is a product of characteristic functions, positive integral operations and the exponential of a real action, hence nonnegative. This supports (S-form) at the two physical arrays x^A and x^B (lambda = 0, 1, eps = 0). It says nothing at a dialled array, where slots that are logarithms of one run's integrals (R', B', the normaliser) are replaced by real convex combinations: positivity there holds if and only if P_h reads those slots through exponentials and positive kernels, which is the content of (S-form) and is not printed in III 11804-18330 (2.2).

## 5. The ramp and stop-production move (written 15:06Z by date -u)

**5.1 The slots are of multiplicative type, so the exponent tools do not apply (READ III 17679-17700, Y 130281-130297).** The slot factor is eta^A + s(eta^B - eta^A), bounded by (1 + p_0 |s|) times "the enlarged support indicator in run B", p_0 := 20 C_chi theta_chi^k, with at most n := N_w^4 slots; the printed disc is |s| <= 1/(n p_0). A positive affine factor is strictly log-concave in s unless constant. How the ramps t^A + s(t^B - t^A) themselves enter a term is not stated in the lines read; the statements below cover factors affine in s.

**5.2 Proposition RAMP-D (direct; no disc). PROVED (elementary); unchecked.** Let f_h >= 0 on (Omega_h, mu_h), I_h finite with at most n elements, eta^A_i, eta^B_i >= 0 measurable, and for 0 <= s <= 1
  F(s) := sum_h integral f_h prod_(i in I_h) [ (1-s) eta^A_i + s eta^B_i ] d mu_h, finite, F(0) > 0.
 (a) If (RAMP-REL) |eta^B_i - eta^A_i| <= p' min(eta^A_i, eta^B_i) holds pointwise on the support of f_h, then | log F(1) - log F(0) | <= n p'.
 (b) If F is C^1 with the derivative taken under the sum and the integral, and (RAMP-INT) sum_h sum_(i in I_h) integral f_h |eta^B_i - eta^A_i| prod_(j != i) [ (1-s) eta^A_j + s eta^B_j ] d mu_h <= n p'' F(s) for 0 <= s <= 1, then | log F(1) - log F(0) | <= n p''.
Proof. (a) Where min(eta^A_i, eta^B_i) = 0 the hypothesis gives eta^A_i = eta^B_i = 0 and the integrand vanishes for all s. Elsewhere each factor is at least the minimum, and its logarithmic derivative in s is at most p' in absolute value, so the integrand rho(s) obeys e^(-n p' s) rho(0) <= rho(s) <= e^(n p' s) rho(0) pointwise; integrate. (b) |F'| <= n p'' F. QED
With p' or p'' of order theta_chi^k this gives a remainder of order N_w^4 theta_chi^k, linear in the volume. Row 1395 6.3 and check 1397 L72 obtained N_w^8 theta_chi^k from the printed disc under ramp (STR), with the floor 20 C_chi N_w^4 theta_chi^k <= 1/2. So under (RAMP-REL) or (RAMP-INT) the ramp (STR) is not needed, the floor goes away and the ell^8 term of Theorem E becomes an ell^4 term.

**5.3 On the printed disc, ramp (zf*) holds given the same relative bound (half-plane). PROVED (elementary).** Under the hypotheses of 5.2(a) with p' <= p_0, for complex |s| < 1/(n p_0) every factor is eta^A_i (1 + s r_i) with real |r_i| <= p_0, so its argument is at most arcsin(p_0 |s|) in absolute value, and the product of at most n factors has argument less than n arcsin(1/n) <= pi/2 (sin x >= 2x/pi on [0, pi/2]). Hence Re F(s) > 0 and F has no zero on the printed disc. So the printed radius is the half-plane radius of a relative bound with the same constant; with a larger constant K p_0 the half-plane argument covers the radius 1/(K n p_0) only.

**5.4 The printed slot bound does not give the relative bound, and inside it both alternatives can fail (model; PROVED by substitution; it is (E2) of row 1395 4.4 placed on a slot).** The printed bound is absolute and allows eta^A_i = 0 < eta^B_i <= p_0 on a part of the enlarged support (the edge of the cut-off of run A). Model: labels of kind 0 read no edge slot and have mass w_0; labels of kind 1 read two slots at such an edge and have mass w_1 p_0^2 s^2 after the move. F(s) = w_0 + w_1 p_0^2 s^2 with w_0, w_1 > 0. The slot bound, the majorant and the one-run bounds hold whenever e^(-C n) <= w_0 and w_0 + w_1 <= e^(C n). For w_1/w_0 > n^2 the zeros +- i (w_0/w_1)^(1/2)/p_0 lie in the printed disc and log F is concave for s^2 > w_0/(w_1 p_0^2), inside the printed interval; log F(1) - log F(0) = log(1 + w_1 p_0^2/w_0), which is c n - 2 log(1/p_0) up to a bounded term when w_1/w_0 = e^(c n), so of order n once c n exceeds 4 log(1/p_0). The edge slot is present at every site of the last lattice (positive density of the unit); each label of the model reads two of them. This shows that ramp (STR*) does not follow from III 17679-17714; it is not a statement about Wilson runs. In the model (RAMP-INT) fails at s near 0, as it must.

**5.5 What decides the ramp move.** By 5.2(b), the ramp comparison in logarithmic form is (RAMP-INT). With |eta^B_i - eta^A_i| <= p_0 on the enlarged support, (RAMP-INT) follows from
 (CUT-1) for every slot i and 0 <= s <= 1: the retained sum with the factor of slot i replaced by the enlarged support indicator is at most C_cut times the retained sum, C_cut free of the torus, of i and of s,
with p'' = C_cut p_0. (CUT-1) says that one stop-level cut-off holds with conditional weight at least 1/C_cut given the rest. It is a one-run, one-site statement of the kind of (RAR) (a conditional lower bound uniform in the outside, row 1391 7.2b (REL-hist)); the chessboard route of row 1395 section 5 does not give it as stated, since it bounds an event by its all-tiles disseminated weight and not a conditional weight. NOT DECIDED.

## 6. Verdicts (written 15:06Z by date -u)

**6.1 (STR*) for the dial directions of the recent classes: NOT DECIDED for the account's formula. REDUCED (PROVED, elementary, unchecked) to (S-form) plus a sup bound the account states.**
 - Not proved: the account prints no formula for P_h in the lines the row names and no positivity statement (2.2); it prints holomorphy, exact ends, incidence and moduli (as check 1397 L99 found).
 - Not refuted: no listed unit type forces a failure (3.5). The slots that are not affine in the dial ((o2), and (o3) if multiplicative) have bounded effect per unit on the whole disc by the account's own activity and tolerance bounds, which is what Lemma SEMI needs. A signed or concave single slot was found ((o3) as a factor, 5.1) and is inconclusive, as the row says.
 - What changed: exact log-convexity (cvx*) or zero-freeness (zf*) is not needed. Theorem S gives the same retained bound from (S1) = positivity of the assembled density at real dials, exponent form, and a second-derivative floor -kappa_z with kappa_z R_z^2 at most a constant times N_w^4. So (H2) of Theorem E can be replaced by:
   (S-form) of 3.5, for lambda in [0, 1] and real eps on the half fibres, for the labels of G and the recent classes; and
   (S-sum) the sup bounds of the (o2) pieces on the disc sum to M_phi N_w^4 over the polymers of a label, M_phi free of the torus.
 - Is this equivalent to the open target? No, for the reason check 1397 L105-L108 accepts for (STR): (S-form) and (S-sum) are statements about one assembly formula at real arrays and hold for families with no comparison between cutoffs (a family constant in the dial satisfies them), and (LOG) can hold with (S-form) false (the polynomial example of check 1397 L107 has a density that is not of exponent form). I cannot show that (S-form) is strictly weaker than "(cvx*) for every class": for a formula with affine slots only they coincide by Lemma EXP. The gain is for the non-affine slots and in naming one checkable property of P_h.

**6.2 The ramp and stop-production move: ramp (STR*) does NOT follow from the printed bounds (model 5.4, both alternatives fail inside III 17679-17714), and it is not needed.** Proposition RAMP-D replaces it: given (RAMP-INT), or (CUT-1) with the printed slot difference bound, the ramp remainder is C_cut 20 C_chi N_w^4 theta_chi^k, linear in the volume, with no floor on N_w^4 theta_chi^k. Given the pointwise relative bound with the printed constant, (zf*) also holds on the printed disc (5.3). (RAMP-INT) and (CUT-1) are NOT DECIDED; the dependence of a term on the ramps t themselves was not read.

**6.3 Positivity at the physical arrays** is supported by Balaban's own sentences (section 4), unchecked and not a statement of the account. Positivity at dialled arrays is the open content of (S-form).

**6.4 Consequence for Theorem E (row 1395 6.4 as corrected by check 1397 L76). PROVED GIVEN the named inputs; unchecked.** With (H1), (H3) in the quantitative form of check 1397 L60-L66, (H4), and (H2) replaced by (S-form) + (S-sum) for the recent classes and (CUT-1) for the ramp move, the single-torus estimate is
   | log Z~^B - log Z~^A | <= C N_w^4 ( e_w^(1/2) + r_K + theta_chi^k ),
with C free of the torus: the term N_w^8 theta_chi^k and the ramp floor are gone. Proof: 3.4 for the dial part (d_0 enlarged by M_phi N_w^4), 5.2(b) with 5.5 for the ramp part started from the hybrid end point, Theorem D of row 1395 for the discarded labels. The two-torus carry then has only ell^4 terms.

## 7. Next two rows and their decisive outcomes

**Row 1, `gap-univk-sform` (reading row, one formula): find the printed form of the terminal assembly P_h and decide (S-form).** Sources: the correlation theorem of the complete account and its torus bound, where "the h-th term chi T^w e^(A^w - E)" is defined (the statement cited at III 11852-11862; grep "torus bound of the correlation theorem" and the "moduli argument" cited at III 17443), the dial interpolation proposition with its item (c1) (cited at III 13706), the sharp interpolation proposition, and Balaban CMP 122 (1.70)-(1.72), (1.98), (1.102) from page images (the OCR text loses the formulas). Questions, in order: (1) at a real array, is the integrand of P_h on the chart a product of nonnegative dial-free factors and the exponential of a real sum of slot terms? (2) do D and the first form enter only as quadratic forms, and the normaliser only in the exponent or as a reciprocal? (3) do the (o2) sup bounds sum to M_phi N_w^4 per label?
 Decisive outcomes: (1) yes to the three: (H2) holds by Theorem S; the dial part of (LOG-al) is a theorem GIVEN III 9.1. (2) a slot enters as a signed factor or through a difference of two positive terms at a real dialled array (for example a stored R' read outside an exponential), with positive density on the last lattice: then (S-form) is false for the common interpolation; test whether the geometric interpolation of that slot (linear in its logarithm) stays inside the account's majorant; if not, the dial part falls back to outcome (a) of row 1395 7.3.

**Row 2, `gap-univk-rar` (as proposed by row 1395 and check 1397), widened by one item: (CUT-1).** Decide (PART), (TILE), (PROD) for the discarded labels with r_K(a_0) = O(e_w^(1/2)) on both tori, and decide (CUT-1) for the stop-level slots: is the conditional weight of one stop-level cut-off, given the rest of a retained label, bounded below uniformly? Read the stop-level slot bound and the common-slot statement behind III 17644-17650, the definition of the quantity f and its threshold c in III 17688-17692, and how the ramps t enter a term.
 Decisive outcomes: (1) (CUT-1) holds (for example the cut-off is implied, up to a set of conditional weight at most 1/2, by small-field conditions the label already carries): the ramp remainder is linear in the volume and the ell^8 term leaves the carry. (2) (CUT-1) fails or stays open: keep the printed-disc bound N_w^8 theta_chi^k under ramp (STR), which then needs its own proof, or the full-end-point shortcut of check 1397 L74; the carry keeps the ell^8 term, harmless only where ell^8 theta_chi^K -> 0.
Order: Row 1 first; it is a reading row on one formula and decides whether Theorem S applies at all.

## 8. Status

| Statement | Mark |
|---|---|
| Lemma SEMI (3.1), Lemma SEMI-C (3.2), Theorem S (3.3), Corollary 3.4: positivity, exponent form and a second-derivative floor on each real half fibre give the retained end point bound with d_0 enlarged by M_phi N_w^4 | PROVED (Holder, Cauchy, Gronwall); unchecked. Uses the account's summed first variation on subsegments (III 17561-17575), ported, not rechecked |
| 2.1-2.5: how the array enters a term; operator, potential and normaliser pieces in a class; no positivity statement in III 11000-19000 | READ (lines cited) |
| 3.5: every listed unit type is compatible with (S1) given (S-form) and (S-sum) | ARGUED from the lines read; the form of P_h was not found in print |
| Section 4: positivity of one run's terms at real configurations | READ in Balaban CMP 122 (OCR text, sentences only); unchecked |
| Proposition RAMP-D (5.2), half-plane statement (5.3) | PROVED (elementary); unchecked |
| Model 5.4: inside the printed ramp bounds both alternatives of (STR*) can fail | PROVED (substitution); a model, not Wilson runs |
| (STR*) for the account's dial directions | NOT DECIDED; reduced to (S-form) + (S-sum) |
| Ramp (STR*) | does not follow from the printed bounds; replaced by (RAMP-INT) / (CUT-1), NOT DECIDED |
| (S-form), (S-sum), (CUT-1), the entry of the ramps t into a term | OPEN |
| Not read: the correlation theorem's definition of the terms, the dial and sharp interpolation propositions, the ramp-weight statements, Balaban's formulas from page images | NOT READ |

No numeric job was run (none was needed). No file other than this one was written in the repository. Scratch: none.

RESULT: (STR) in the corrected form of check 1397 is NOT DECIDED for the account's assembly formula: the lines named by the row print holomorphy, incidence and moduli but neither the form of P_h nor any positivity, and no listed recent unit forces a failure. PROVED (elementary, unchecked): Theorem S, which replaces exact log-convexity or zero-freeness by positivity of the assembled density at real dials in exponent form plus a second-derivative floor of order N_w^4/R_z^2 (supplied by the account's sup bounds on the disc for the non-affine operator pieces), and gives the same retained bound with d_0 enlarged by a torus-proportional constant; Proposition RAMP-D, which gives a ramp remainder linear in the volume with no disc and no floor from an integrated relative slot bound. Ramp (STR) does not follow from the printed slot bounds (explicit model with both alternatives failing), and is not needed. OPEN: (S-form) and (S-sum) for P_h, (CUT-1) for the stop-level slots, how the ramps enter a term, then (RAR), term D, (GEO) and the hypotheses of III 9.1; next rows gap-univk-sform (read the printed terminal formula), then gap-univk-rar widened by (CUT-1).
