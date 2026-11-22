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
Proof. (i) For every omega the function eps a + phi + kappa eps^2/2 is convex, so the integrand times e^(kappa eps^2/2) is nonnegative and log-convex in eps. A sum or integral of nonnegative log-convex functions is log-convex (Holder, as in Lemma EXP of row 1395 4.5, on the disjoint union of the Omega_h). (ii) g := log F + kappa eps^2/2 is convex, g(0) = log F(0), g'(0) = (log F)'(0), and g <= Lambda + kappa R^2/2. For 0 < r < R convexity gives [g(0) - g(-r)]/r <= g'(0) <= [g(r) - g(0)]/r. Also g(-r) >= g(0) - r g'(0) is not needed: by convexity g(0) <= [g(r) + g(-r)]/2, so g(0) - g(-r) >= -(g(r) - g(0)) >= -(Lambda + kappa R^2/2 - g(0)). Let r -> R. QED

**3.2 Lemma SEMI-C (from a sup bound on a complex disc).** If phi(omega, .) is holomorphic on |eps| < R_z, real on the real axis, and |phi(omega, eps)| <= M there, then on the interval (-R_z/2, R_z/2) it satisfies 3.1 with kappa = 8M/R_z^2.
Proof. Cauchy's inequality on the disc of radius R_z/2 about a real point eps with |eps| <= R_z/2: |phi''(eps)| <= 2M/(R_z/2)^2. QED

**3.3 Theorem S (chain along the diagonal; replaces the fibre condition in check 1397 L48-L56).** Let F(lambda), 0 <= lambda <= 1, be the restricted good sum on the diagonal of the dial domain, and G_z(lambda, eps) its value on the z-fibre. Assume
 (S0) the summed first variation on every subsegment: F is C^1 on [0, 1] with F'(lambda) = sum_z d/d eps G_z(lambda, eps) at eps = 0 (the account's first-variation statement, III 17561-17575, as used by check 1397; ported, not rechecked here), and classes not read by a label of G contribute zero (2.4);
 (S1) (POS-SEMI) for every lambda and every class z read by G, the function eps -> G_z(lambda, eps) has on (-R'_z, R'_z) the form of 3.1 with a constant kappa_z, and G_z <= e^Lambda there;
 (S2) F(0) > 0.
Put d(lambda) := Lambda - log F(lambda), s_1 := sum_z 1/R'_z, s_2 := sum_z kappa_z R'_z/2 (sums over the classes read by G). Then F > 0 on [0, 1] and
  d(0) e^(-s_1) - (s_2/s_1)(1 - e^(-s_1)) <= d(1) <= d(0) e^(s_1) + (s_2/s_1)(e^(s_1) - 1),
so | log F(1) - log F(0) | <= ( d(0) + s_2/s_1 ) ( e^(s_1) - 1 ).
Proof. Positivity: in the form of 3.1, G_z(lambda, eps) = 0 for one eps forces f_h = 0 almost everywhere for all h, hence G_z(lambda, .) = 0 identically; F is continuous, F(0) > 0, and on the set where F > 0 the bound below keeps log F finite, so that set is open and closed in [0, 1]. By 3.1(ii) on each fibre and (S0), |d'(lambda)| <= s_1 d(lambda) + s_2. Then (e^(-s_1 lambda)(d + s_2/s_1))' <= 0 and (e^(s_1 lambda)(d + s_2/s_1))' >= 0; integrate. QED

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

