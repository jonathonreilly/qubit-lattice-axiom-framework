lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-17T03:52Z

# Check of row 1053 (gap-wall-vectors-max), row 1062

Row 1062, `gap-wall-vectors-check-opus`. Written by Claude Opus 5.5 at max effort on Mac mini worker 3, started 2026-11-16T15:52Z (date -u), from commit 1b75bdfba of branch claude/ym4d-hard-route. It checks `library/gap-wall-vectors-max.md` (row 1053, written by Claude Fable 5.2 max). Same provider as the author (Anthropic), so this is not an independent check in the sense of the working rules; row 1061 is the cross-provider check and this file does not read it. A research check, not an audit; no mass gap is claimed. No new attack.

Marks: HOLDS, HOLDS AFTER CORRECTION (with the corrected text), FAILS (with the first failing line).

## Plan (at most eight steps; one per response, appended before the next)

1. Read FINISH.md (efficiency rules, build on published work) and row 1053's file in full; record brief B1 (section 8.2) and its file list.
2. Line-by-line check of 6.1 Lemma FACE-LIM, 6.2 Lemma ANCH and Corollary ANCH-W, 6.3 Lemma RIG.
3. Line-by-line check of 6.4 Lemma FACE-MW (capacity bound 24 t^2/log(R/r); constants 12 pi^2 and 48 pi^2).
4. Line-by-line check of 6.5 Proposition ITER and 6.7 Lemma EVEN.
5. Judge the S0 verdicts of 4.1-4.4, the dimension count of 4.1 (flux twist with frames on a two-dimensional set: excluded, or only not found), the one-loop formula of 4.2, and the Gaussian checks of 6.6.
6. Step 7's claim that Orland's papers hold the anchor: read the papers (open copies only, each in a new empty directory under /tmp) and judge.
7. Judge the five vector verdicts (V1 FAILS as a route since (BR-L) contains the target; V2-V4 renamings; V5 a GUIDE-grade test).
8. Verdict table, what this check did not cover, RESULT line.

## Step log

### Step 1 result: what is checked, and from which files

Read in full: `library/gap-wall-vectors-max.md` at 1b75bdfba (387 lines, 63,004 bytes, the size the lead note records). Read: FINISH.md sections "How we work", "Working efficiently", "Rules"; row 1062 and row 1053 of the queue.

**Items, from brief B1 (8.2 of row 1053) and row 1062.**

- Line-by-line checks: C1 = 6.1 Lemma FACE-LIM (comb tree, weak limit); C2 = 6.2 Lemma ANCH; C3 = 6.2 Corollary ANCH-W; C4 = 6.3 Lemma RIG (the two-sign identity, the constant beta_M/2 times D, the Cauchy-Schwarz step); C5 = 6.4 Lemma FACE-MW (the capacity bound 24 t^2/log(R/r), the constants 12 pi^2 and 48 pi^2); C6 = 6.5 Proposition ITER (K_j = (1 - eps_j) Kbar_j + eps_j R_j, the zero average); C7 = 6.7 Lemma EVEN.
- Judgements: J1-J4 = the S0 verdicts of 4.1-4.4; J5 = the dimension count of 4.1 (is a flux twist with frames on a two-dimensional set excluded, or only not found); J6 = the Gaussian checks of 6.6; J7 = the one-loop formula of 4.2; J8 = step 7's claim that Orland's papers hold the anchor; J9 = the five vector verdicts V1-V5.
- Files named by B1: this file; `library/gap-global-reform-max.md` L491-530 and L1040 (Lemma REM, line F3); `library/gap-invent-selective-max.md` L52-63 (kill sheet); `library/prior/gap-2don-proofs-read-opus.md` L113-176.

**Two notes on the brief.** (1) B1 names the output `library/gap-wall-vectors-check.md`; row 1062 names `library/gap-wall-vectors-check-opus.md`. I follow the row. (2) Row 1062 says I do not read row 1061's file; I do not.

### Step 2 result: C1 Lemma FACE-LIM, C2 Lemma ANCH, C3 Corollary ANCH-W, C4 Lemma RIG

Each proof was redone by hand below. Conventions as in row 1053, 6.0: e^(ta) = cos(t/2) + i sin(t/2) a-hat . sigma, x_p = (1/2) tr U_p.

#### C1 Lemma FACE-LIM (6.1): HOLDS

- *Comb tree.* In a rectangle {x} x Lambda_long, the links of direction 0 and the direction-1 links on one row u_0 = const form a spanning tree: it is connected and has (n_1 - 1) + n_1 (n_0 - 1) = n_0 n_1 - 1 links. The trees of different x lie in disjoint site sets, so their union is a forest. Fixing a forest by a field-dependent gauge transformation is valid for a gauge-invariant integrand: for fixed tree links the map on the other links is a left and right translation by fixed elements, so it keeps Haar measure, and the tree links then integrate out. Checked.
- *Plaquette.* With U_0 = 1: U_p = U_0(u) U_1(u + e_0) U_0(u + e_1)^(-1) U_1(u)^(-1) = V(u + e_0) V(u)^(-1). Checked.
- *Weak limit.* For each line {u_1 = const, x = const} the V are a random walk in u_0 from V = 1, with step law proportional to exp(beta_L (1/2) tr xi) d xi. On SU(2), (1/2) tr xi <= 1 with equality only at xi = 1, so for a neighbourhood N of 1 the step mass outside N is at most exp(-beta_L delta/2)/Haar(N') for some delta > 0 and some N' of positive measure; it tends to 0. Finitely many steps, so the joint law of the V tends to the point mass at V = 1. The remaining factor h = exp(beta_M sum + beta_T sum) is continuous and positive, F is continuous, so numerator and denominator converge, the limit denominator is positive. Checked.
- *Mixed plaquette and residual group.* U_p = Phi_l(u + e_mu) Phi_l(u)^(-1), and tr U = tr U^(-1) in SU(2). A gauge transformation keeps U = 1 on all longitudinal links of a connected rectangle exactly when it is constant in u. Checked.
- *Wording note (no effect on the proof).* "a product over rows of chains" means: one chain in u_0 for each fixed (u_1, x); the "row u_0 = 0" is the spine. The free boundary is essential (on a periodic plane the frozen face keeps two commuting holonomies); the lemma states it.

#### C2 Lemma ANCH (6.2): HOLDS

For unit quaternions q = s_0 + i s.sigma, q' likewise: q q'^(-1) = s_0 s'_0 + s.s' + i(...).sigma, so (1/2) tr(q q'^(-1)) = s . s' (four-vector product). Haar measure on SU(2) is the uniform measure on S^3. Each mixed plaquette (mu in {0, 1}, nu in {2, 3}) at (u, x) corresponds to exactly one pair (l = (x, x + e_nu), bond <u, u + e_mu>). At beta_T = 0 no term joins two transverse links. So M(beta_M, 0) is a product over l of free-boundary two-dimensional O(4) models on Lambda_long with coupling beta_M. Checked.

#### C3 Corollary ANCH-W (6.2): HOLDS AFTER CORRECTION

- *Mixed loop.* With longitudinal links 1, the R x T loop in a (mu, nu) plane is (1/2) tr[Phi_1(R) ... Phi_T(R) Phi_T(0)^(-1) ... Phi_1(0)^(-1)] = (1/2) tr[Phi_1(0)^(-1) Phi_1(R) M_1], M_1 the inner word, independent of sheet 1. By right invariance of one O(4) sheet (Phi -> Phi h^(-1)), A = E[Phi(0)^(-1) Phi(R)] commutes with every h in SU(2), so A = c 1 with c = (1/2) tr A = G(R). (The file uses left invariance and the other order; both are valid, since one O(4) sheet is invariant under left and right translations.) Induction on T gives G(R)^T. Checked. Note: with free boundary G depends on the two end points, not only on R; "G(R)" is the two-point function between the two corners. All sheets have the same longitudinal box and coupling, so the same G.
- *Transverse loop.* The proof uses that some link occurs exactly once, and then E[Phi_l(u)] = 0 (the one-site marginal is uniform on S^3) and independence of the other sheets. **This fails for a loop that traverses each of its links twice.** Example: the plaquette traversed twice, U_p^2. At the anchor U_p is a product of four independent Haar elements, so it is Haar distributed, and E[(1/2) tr U_p^2] = (1/2) E[chi_1(U_p) - 1] = -1/2, not 0.
- **Corrected text:** "A loop in a transverse plane that traverses some link exactly once (for example every simple loop, in particular every rectangle) has expectation 0." Nothing downstream in row 1053 uses non-simple transverse loops, so no other line changes.
- *The area-law sentence (GIVEN input).* With OpenAI's Theorem 1.1 (n = 4, free boundary, uniform in subgraphs; as row 1007 B(1) reads it): 0 <= G(R) <= A e^(-mR), so E[W] <= A^T e^(-mRT) = exp(-T(mR - log A)). This is an area law with tension at least m plus a perimeter term T log A. "Tension at least m" holds in this asymptotic sense. Correct as an implication from the GIVEN theorem.
- *Selectivity paragraph.* U(1): at the anchor the sheets are plane-rotator models; Frohlich-Spencer 1981 (as cited) give a power-law lower bound at large coupling, so no exponential upper bound. Finite subgroups H of SU(2): FACE-LIM goes through (the character of the fundamental representation has its unique maximum at 1 on H as well), and each sheet is a two-dimensional H-valued model with H x H symmetry, ordered at large beta_M by a Peierls argument. That last step is a RECALLED standard fact, not rebuilt in row 1053 or here. With that label, "selective against U(1) and finite groups by theorems" stands at the level of the sheet two-point functions (mixed-plane loops), which is what is claimed.
- *Remark (which split is selective).* ARGUED as labelled. k = 1: at zero spatial coupling the model in temporal gauge is a product of one-dimensional chains, gapped for every compact group: correct. k = 3: there are no plaquettes transverse to a 3-flat in four dimensions, and the free links form three-dimensional O(4) layers, ordered at large coupling (Frohlich, Simon and Spencer 1976): correct as recalled. "Migdal's correspondence ... exact at one point" is a description, not a statement with content; harmless.

#### C4 Lemma RIG (6.3): HOLDS (scope sentence needs one qualifier)

- *Gauge form of the twist at fixed u.* g_x = e^(theta(u) a), g_y = 1 for y != x acts as e^(theta a) Phi_l on links that start at x and Phi_l e^(-theta a) on links that end at x. So every on-site term invariant under the transverse gauge group at u is unchanged. Checked.
- *Bond identity.* Start at x: (1/2) tr(e^(theta(u) a) Phi(u) Phi(u')^(-1) e^(-theta(u') a)) = (1/2) tr(W e^(delta a)), W = Phi(u) Phi(u')^(-1), delta = theta(u) - theta(u'), since the two exponentials have the same axis. End at x: (1/2) tr(W' e^(-delta a)), W' = Phi(u')^(-1) Phi(u), and (1/2) tr W' = (1/2) tr W = w_0. Checked.
- *Two signs.* e^(delta a) + e^(-delta a) = 2 cos(delta/2) 1, so the values at delta and -delta add to 2 w_0 cos(delta/2). Hence (1/2)(S o tau_theta + S o tau_(-theta)) - S = -beta_M sum w_0 (1 - cos(delta/2)), the sum over links at x and bonds meeting C. Checked.
- *Constant.* -w_0 (1 - cos(delta/2)) >= -(1 - cos(delta/2)) >= -delta^2/8; at most four transverse links meet x in a planar Lambda_perp; so the sum is at least -(beta_M/8) 4 D = -(beta_M/2) D. Checked.
- *Cauchy-Schwarz.* The interior change of variables Phi -> tau_theta Phi is a left or right translation of each integrated link, so Z_C(tau_theta omega) = integral of exp(S o tau_theta). Then (integral of exp((S o tau_theta + S o tau_(-theta))/2))^2 <= Z_C(tau_theta omega) Z_C(tau_(-theta) omega), and the left side is at least (e^(-(beta_M/2) D) Z_C(omega))^2. Checked.
- *Scope sentence.* "Every compact Lie group" holds with a group-dependent constant, not with the constant beta_M as stated: the identity of the two signs is the SU(2) fundamental trace. For a unitary representation and a twist generator A, Re tr(W (e^(delta A) + e^(-delta A) - 2)) >= -dim * delta^2 * norm(A)^2, so the bound reads exp(-c_G beta_M D). For U(1) with weight beta cos(phi) and rotation of the phase by delta the same steps give (1/2)(S o tau_theta + S o tau_(-theta)) - S >= -2 beta_M D at a site of degree 4, hence exp(-4 beta_M D) (delta in place of delta/2; with the diagonal U(1) of SU(2) and its phase delta/2 the SU(2) constant returns). **Corrected text:** "Every compact Lie group (with exp(-c_G beta_M D) in place of exp(-beta_M D), c_G depending on the group, the representation in the action and the normalisation of the generator)". Row 1053 uses RIG for U(1) and Pin(2) only qualitatively (4.1 K5, K6), so nothing downstream changes.
- *Comparison with Lemma WN.* Read in row 1013 (`gap-invent-selective-max.md` L136-160): in the isotropic model, the same move with the longitudinal links held has corner angles theta_(p,x) = +-theta(u) on the mixed plaquettes at (u, x), so the cost contains beta xbar sum theta(u)^2, a term per site with no gradient. The remark is correct.

### Step 3 result: C5 Lemma FACE-MW (6.4): HOLDS AFTER CORRECTION (one implicit hypothesis made explicit)

Each line redone by hand.

- *Density ratio.* Write p(zeta) = Z^(-1) exp(S_in(zeta)) W(zeta, omega), S_in the bond and on-site terms inside B_r, W the annulus partition function. W reads zeta only on the layer abs(u)_inf = r (the model is nearest-neighbour in u). A constant g in G_x keeps S_in: the bonds of links at x have delta = 0, the on-site terms are gauge invariant, and Haar measure is kept. So p(g zeta)/p(zeta) = W(g zeta, omega)/W(zeta, omega). Checked.
- *Use of Lemma RIG.* C = {r < abs(u)_inf <= R}, dC = (layer r) together with (layer R + 1, the pin). theta = t on layer r, theta(u) = t log(R/abs(u)_inf)/log(R/r) on C (it is 0 on layer R), theta = 0 on the pin. Then tau_theta moves the inner data by e^(ta) at x and leaves omega fixed, so RIG gives W(e^(ta) zeta, omega) W(e^(-ta) zeta, omega) >= e^(-beta_M D(theta)) W(zeta, omega)^2. Checked.
- *Capacity bound.* A nearest-neighbour bond of Z^2 changes abs(u)_inf by at most 1, so only bonds between shells k and k + 1 contribute. Shell k (k >= 1) has 8k sites: 4 corners with two outward bonds and 8k - 4 side sites with one, so 8k + 4 outward bonds. Their difference is t log((k+1)/k)/log(R/r) <= t/(k log(R/r)) for t >= 0; the bonds from shell R to the pin have difference 0. So D <= (t^2/log^2(R/r)) sum_(k=r)^(R-1) (8k + 4)/k^2 <= (12 t^2/log^2(R/r)) sum_(k=r)^(R-1) 1/k, using 4/k^2 <= 4/k. Then sum_(k=r)^(R-1) 1/k <= 1/r + log((R-1)/r) <= 1 + log(R/r), and 1 + log(R/r) <= 2 log(R/r) when R >= e r. So D <= 24 t^2/log(R/r). **Checked: the capacity bound 24 t^2/log(R/r) holds.**
- *AM-GM and total variation.* With eps = 24 beta_M t^2/log(R/r): q = (1/2)(p o e^(ta) + p o e^(-ta)) >= sqrt(p o e^(ta) p o e^(-ta)) >= e^(-eps/2) p. Both p and q are probability densities (the rotation keeps Haar measure). Then the integral of (p - q)_+ is at most 1 - e^(-eps/2) <= eps/2, the integral of abs(p - q) is at most eps, and by the substitution zeta' = e^(ta) zeta, E_q[f] = E_p[(1/2)(f o e^(ta) + f o e^(-ta))]. So the bound with eps sup abs(f) holds, for vector f with the Euclidean norm. Checked.
- *Constant 12 pi^2.* For f with f(g zeta) = R(g) f(zeta) and t = pi, R(e^(pi a)) = R(e^(-pi a)) = 2 a-hat a-hat^T - 1, so the left side is abs(2 P_perp E[f]), P_perp the projection orthogonal to a-hat. Hence abs(P_perp E[f]) <= (eps/2) sup abs(f) with eps/2 = 12 pi^2 beta_M/log(R/r). With a-hat orthogonal to a chosen unit vector e, abs(e . E[f]) <= abs(P_perp E[f]). **Checked: 12 pi^2 beta_M sup abs(f)/log(R/r).**
- *Constant 48 pi^2.* e^(2 pi a) = -1, which acts at x as the centre; for a centre-odd f the average at t = 2 pi is -f, so 2 abs(E[f]) <= eps sup abs(f) with eps = 24 beta_M (2 pi)^2/log(R/r) = 96 pi^2 beta_M/log(R/r). **Checked: 48 pi^2 beta_M sup abs(f)/log(R/r).**
- *The implicit hypothesis.* The profile log(R/abs(u)_inf) and the bound 1/r <= 1 need r >= 1; at r = 0 the profile is undefined. **Corrected text:** "Let r >= 1 and R >= e r be integers, and let B_r and B_R be the boxes ..." Nothing else changes.
- *Reading.* Correct: the estimate uses only Lemma RIG, which holds for compact U(1) with another constant (C4), so the lemma is blind, as the file says. Credit to Dobrushin and Shlosman, McBryan and Spencer, and Pfister for the method is appropriate.

### Step 4 result: C6 Proposition ITER (6.5) and C7 Lemma EVEN (6.7)

#### C6 Proposition ITER: HOLDS (as an implication from (FACE-TW) for arbitrary pins)

- *Chain.* Put the intra-layer bonds and on-site terms of layer N_j into Z_in(eta_j), the partition function of {abs(u)_inf <= N_j} with boundary data eta_j. Layer N_(j+1) = 2 N_j separates its inside from its outside, so given eta_(j+1) the law of eta_j has Haar density proportional to Z_in(eta_j) W_(N_j)(eta_j, eta_(j+1)), and D_(N_j) = {N_j <= abs(u)_inf <= 2 N_j} is exactly the annulus of (FACE-TW). The law of eta_J depends on omega; the later kernels do not. Checked.
- *Invariance of Z_in.* Constant g in G_x: bonds of links at x have delta = 0, on-site terms are gauge invariant, the change of variables keeps Haar measure. Checked.
- *Inner versus outer pin.* (FACE-TW) moves the outer pin. The push-forward g_* K_j has density Z_in(eta) W(g^(-1) eta, eta_(j+1)), and the constant rotation of the whole annulus gives W(g^(-1) eta, eta') = W(eta, g eta'). So g_* K_j >= (1 - eps_j) K_j for every g. The file does not write this one line; it is correct.
- *Direction of the inequality.* From (g^(-1))_* K_j >= (1 - eps_j) K_j, apply g_*: K_j >= (1 - eps_j) g_* K_j. Averaging over g gives K_j >= (1 - eps_j) Kbar_j, as the file states. (Averaging the first form gives the other direction, Kbar_j >= (1 - eps_j) K_j, which would not suffice.) Then R_j = (K_j - (1 - eps_j) Kbar_j)/eps_j is a probability kernel. Checked.
- *Zero average.* Given eta, the inside law with data g eta is the image under g of the inside law with data eta, so F_j(g eta) = E[f o g given eta], and its average over g is 0 because f has zero G_x-average pointwise. Hence the integral of F_j against Kbar_j = average of g_* K_j vanishes, F_(j+1) = eps_j R_j F_j, and abs(E[f]) = abs(E[F_J(eta_J)]) <= sup abs(f) prod_(j=j_0)^(J-1) eps_j. Checked.
- *Rate.* With eps_j = C/(j log 2 + log N_0), log of the product is -J log J + O(J), and N_J^(-k) = exp(-k J log 2 + O(1)). So the bound is faster than every power of N_J. Checked.
- *Two-point form.* The file's reading in "What (FACE-TW) would and would not be" (the correlation of the vector part of a transverse plaquette holonomy at two points of one plane) follows: condition on the configuration outside B_(N_J); this is a G-invariant bilocal product of two charged factors, not a connected correlation of singlets. Consistent with the file's K1 sentence.
- *U(1) sentence.* The file says (FACE-TW) fails for compact U(1) because the Gaussian charged correlation is a power (6.6). This can be made theorem-grade at beta_T = 0: the face is then a product of plane-rotator models, Frohlich and Spencer 1981 give a power-law lower bound for the two-point function at large coupling, and ITER (whose proof uses no SU(2) structure) would give decay faster than every power. So the U(1) form of (FACE-TW) is false at large beta_M, beta_T = 0, given Frohlich-Spencer (cited, not rebuilt). A strengthening, not a defect.
- *Not checked here.* The sentence that the sign-cluster part of the O(n) text does not port for beta_T > 0 (ARGUED in the file; not in B1's list).

#### C7 Lemma EVEN: HOLDS

j = i sigma_2 = [[0, 1], [-1, 0]], j^(-1) = -j; for t = diag(e^(i phi), e^(-i phi)) a direct product gives j t j^(-1) = diag(e^(-i phi), e^(i phi)) = t^(-1). A gauge-invariant F is invariant under the constant gauge transformation j, which maps a T-valued configuration to the configuration of link inverses (orientations kept). Checked. The same proof holds for functions invariant under Pin(2) gauge transformations, since j is in Pin(2); that is the form 6.7 uses.

*The Consequence paragraph (ARGUED, belief-grade, as labelled).* The leading Gaussian term is right: for Gaussian angles with field-strength covariance D(x) ~ |x|^(-4), the connected correlation of cos theta_p and cos theta_q is e^(-(s_p^2 + s_q^2)/2)(cosh D - 1) ~ D^2/2 ~ |x|^(-8), and odd observables such as sin theta_p are not Pin(2)-invariant. Pin(2) = T together with jT: compact, infinite, non-commutative, with the one-dimensional (abelian) Lie algebra of T. Correct. The Z_2 = pi_0 part is a Z_2 gauge field whose frustrated plaquettes (x_p = 0 on jT) form closed sheets; "flat up to rare closed sheets at large coupling" is the expected deconfined behaviour, not proved here or there. So "no gap on Z^4 at large coupling" stays a belief, as the file says.

## Status

Steps 1-4 done (C1-C7). Next: step 5 (J1-J7: S0 verdicts of 4.1-4.4, the dimension count, the Gaussian checks, the one-loop formula).
