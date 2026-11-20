lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-21T03:02Z

# gap-mini-solve-as-opus: the four-dimensional SU(2) mass gap (FINISH row 1293)

Started 2026-11-20T15:02Z (date -u) on the Mac mini Claude worker 2, branch claude/ym4d-hard-route pinned at 05378c8d5.
Research-stage working state. Labels: PROVED, ARGUED, GUIDE, OPEN, as the row asks.

## Status

Steps 0-1 done; Step 2 (reading the step) done, written 2026-11-20T15:18Z (date -u); Step 1 written 2026-11-20T15:10Z (date -u). Step 3 (Theorem PE) written 2026-11-20T15:21Z (date -u). Step 4 (inputs checked factor by factor) written 2026-11-20T15:24Z (date -u). Next: Step 5, consequences for the carry and Route Z, labels, RESULT.

## Repo search (rule "Repo first")

This checkout has no `origin/main` ref and holds `docs/` only in the index, so main and the open PR branches
(#10114, #10133, #10134, #10141, #10144) were not searched from here; only this folder was. Rule 0a grep of
`FINISH.md`, `library/open-core.md`, `library/l17c.md` for "parity envelope", "(PE)", "half-loop": the only match is
row 1280 (`library/gap-mini-solve-ap-opus.md`, this worker's thread, Proposition PE ARGUED). No queued row owns it.

## Step 0. Record read (statements about the record, not evidence)

Read at the pin: `GOAL.md` in full; `FINISH.md` L1-85 and L299-356, row 1293; the RESULT segments of rows 1240-1296;
`parts/gap.md` L1-104; `library/prior/gap-onebound-read-sol.md` in full (row 1218); row 1280
(`library/gap-mini-solve-ap-opus.md`) L42-469; row 1291's file (its Step 1 digest only, no choice yet). Summary:

1. The infrared seed ((N-phys) of row 1161, equivalently (SL)/(RR) of row 1258 at one weak coupling, or the stronger
   full-thermal window (A-B*) of Bhattacharjee et al.) is OPEN. About sixty idea families are screened on file (rows
   1189, 1194, 1199 tables; rows 1228-1287). Row 1218's reading: none of the three published sources supplies it.
2. The one-cutoff carry on the pin route (rows 1233, 1255, 1256, 1260, 1264, 1267, 1268, 1275, 1278, 1280) is a
   chain of implications. Its open inputs after row 1280 and checks 1263, 1266, 1276, 1288: the supplier readings
   (E0)-(E6), (E+), (TH) against Balaban's CMP 116 (not on this machine); either (U-dom) or the inputs (P1)-(P4) of
   row 1280's parity envelope (PE); row 1267's (H2)-(H3) (row 1278: H3' given readings, H2' ARGUED); the account's
   outstanding `9.1:prop-blind-site-expansions`; (V9) (check 1288: row 1275's reading N2 FAILS); (DET)'s inputs.

## Step 1. How best to attack it (judgement, ARGUED; written 2026-11-20T15:10Z by date -u)

**The seed.** I do not attack it. Every route I can name (vortex free energies, Migdal-Kadanoff bounds, abelian
projection, Gribov region, Bakry-Emery, chessboard and infrared bounds, Lee-Yang in beta, twisted boxes, layer
reductions, large N) has a match in the tables cited in Step 0, item 1, and `parts/gap.md` (row 998 9.5) names a
further blind screen as waste. The seed is a statement at order-one coupling with a number in it, and no hand method on
file or in the literature read here reaches it.

**The item: the parity envelope (PE) of row 1280, from ARGUED to PROVED given precisely stated inputs.** Claim of
(PE): the unmarked coefficient of one Balaban step obeys |f_(k+1)| <= C theta_k^(-1) (log theta_k)^q + tails, not only
EM's C theta_k^(-1/2) (log theta_k)^(p_0): one step has no half-loop term. Row 1280 4.5 shows what it buys: the drift
of the account's runs from the scaffold becomes polylog, (U) closes without (U-dom), and Route Z's flow law (B3+) of
row 680 gets its mechanism.

Moves: the one-cutoff carry on the pin route (row 1280 5.2: (U) needs (U-dom) and (E+), or (PE)); Route Z's (B3+)
(row 680 Section 5). Success: (PE) becomes PROVED GIVEN inputs that are read in the account's text, so (U) leaves the
carry without (U-dom). Failure: an odd-in-g term in the step that survives the parity, which would be a named obstruction
for (PE), (B3+) and Route Z.

**New idea for the proof (to be written in Step 3).** Row 1280 used a parity rule degree by degree ((P2)), which needs
Taylor remainders. A cleaner device: every factor of the step that is a function of the configuration depends on the
coupling g and the normalized fluctuation b only through exp(i g b) (and on g^2 through the action's prefactor), so it
is invariant under the joint flip (g, b) -> (-g, -b). Replace g by a complex parameter h in the fluctuation, keep the
cut frozen at the actual g, and use the symmetry of the Gaussian reference: the localized coefficient is then an
analytic function of h that is even up to the cut's asymmetry, and a Cauchy estimate for even functions gives
f(g) - f(0) = O((g/r)^2) on a disc of radius r of order 1/(log theta)^(p_0). The cut's asymmetry is a thin shell at the
threshold (path products and their inverses differ only at third order), so it costs tails by row 1280's Lemma SW.

**Plan.** Step 2: read YM4_EM's one-step kernel and coefficient theorem (definitions of f, of the unmarked output, of
the cut, and what EM assumes of the localization and of complex data). Step 3: state and prove Theorem PE in the form
those definitions allow (Lemmas: flip invariance, even Cauchy estimate, near-evenness from Lemma SW, assembly). Step 4:
check the flip invariance against each factor of the step (action, Haar and chart densities, soft axial weight, cut,
inherited list) in Balaban's CMP 119 as read in rows 1268 and 1280. Step 5: consequences, labels, RESULT.

## Step 2. What the step is, in the account and in Balaban (READ; written 2026-11-20T15:18Z by date -u)

Sources: Sussman and Alpoge, `YM4/EM/YM4_EM.tex` at c7fef8b21b58 (2001 lines; credit Ethan Sussman and Levent Alpoge,
with Claude and Codex as authors of their text), fetched by URL into a scratch folder outside the repository, cited
EM:n; Balaban, CMP 119 (1988) 243-285, the owner's copy, pp. 247, 267, 268 read as page images.

**2.1 The step (EM:544-578).** At real admitted data the step is the actual finite integral
    E_(k+1)[x_k, f](W) = log int K_(k,theta_k)(W, dV) exp(-x_k A(U_k(V)) + S_f(U_k(V))) + x_k A(U_(k+1)(W)) - S_f(U_(k+1)(W)),
where K is "the fixed all-small-field kernel on M(V) = W. It uses the given fibre density, gauge weight and
fluctuation cut. In the resolved fibre chart its real free array is B and its field is V'(W, B)". The frame theta_k fixes
"the lattice partitions, Gaussian references, real fluctuation coordinates and tests"; the Wilson weight x_k does not
(EM:502-506), tau_k = x_k/theta_k. The background identities V'(W, 0) = M^k U_(k+1)(W), U_k(V'(W, 0)) = U_(k+1)(W) are
required of the supplied backgrounds (EM:550-555). The inherited list S_f is a sum of fixed functions of the
configuration (EM:538-543).

**2.2 The cut and the Gaussian (EM:580-606, EM:619-624).** "In the analytic integral presentation the sharp test is a
fixed Borel restriction in the real free variables." The Gaussian reference is exp(-<B, Delta B>/2), Delta = Delta_A +
Delta_G (action and gauge precisions), with the weight shift (tau_k - 1)<B, Delta_A B>/2 as in (em:eq-frozen-gaussian-rewrite).

**2.3 The localization (EM:629-647).** "One prescribed convergent localization gives the pointed output E_(k+1) after
the specified scalar has been separated". It is required to be covariant under the orthogonal maps O_(r,W) of the real
free coordinates that admitted isometries r induce: "This change transports the cut, completed response, measure factors
and point z to rz". Nothing is said about the map B -> -B.

**2.4 The output and the coefficient (EM:678-706, EM:840-843, EM:1173-1205, EM:1338-1384).** E_(k+1) = N_(k+1) +
G_(k+1,tau_k) + F_(k+1); the unmarked residual obeys ||E^u_(k+1) - N_(k+1) - G_(k+1,tau_k)|| <= C delta(theta_k) on the
absolute core (Proposition em:prop-prefix-formation), delta(y) = A_1 y^(-1/2) (log y)^(p_0) (EM:345), 2 p_0 > 1
(EM:874-875). Sum_X N_(k+1) = log Z_k(W) - log Z_k(1), Z_k the "constrained reference Gaussian normalizer without a
fluctuation cut"; the total of G is background-free. The coefficient map b_j (Proposition em:prop-companion-coefficient)
is the second moment of the companion kernel, the limit of the torus Hessians at the trivial datum P_o; it is linear,
real on real data, |b_j(E)| <= C a^(-2) cal(A) for a family of norm cal(A) on a core of physical radius a, and it does not
depend on the coherent localization of a physical total. Theorem em:thm-coefficient-envelope: b_(k+1) = b^0 + f_(k+1) +
q_(k+1) with f_(k+1) = b_(k+1)(F^u_(k+1)); its bound |f| <= C theta_k^(-1/2) (log theta_k)^(p_0) is exactly the norm bound
on F^u times the fixed extraction cost of the absolute core (EM:1379-1384). So EM's envelope is a size bound; nothing in
EM uses the structure of F^u.

**2.5 Balaban's all-small-field step (CMP 119 pp. 267-268, (3.15)-(3.16)).** After the scaling A'_k = g_k A_k the step
is an integral over the free variables A_k of
    exp[-(1/2) <A_k, C* Delta^(k) C A_k> + P^(k)(g_k, U_(k+1), A_k)]
times characteristic functions; the configuration inside P^(k) is U_k(exp i[g_k C A_k - h D~(g_k C A_k)] V^(k)), so it
depends on g_k and A_k only through g_k A_k, and the inherited terms enter as (E_k + R_k + B_k)(that configuration) minus
their value at U_(k+1). The scalars in front (log g_k d(g)|B(Gamma)*|, log sigma_0 |B(Gamma)*|, -log z (L^4 - 1)|Gamma|)
depend on counts only, not on the field. The small-field cut is introduced on the normalized fluctuation itself, (3.16):
chi(sup over b in (box'~2)^(k)* of |A_k(b)| < delta_k) on each cube, and the earlier small-field characteristic function
"is equal to 1, because of the bound on A_k introduced by the second" (p. 268). So the all-small-field cut is a product
of tests |A_k(b)| < delta_k on the free variables: it is even under A_k -> -A_k. The soft axial gauge (1.5) (p. 247) is
an inserted average over gauge transformations with weight exp(-g_0^(-2) [1 - Re tr U^u(y, x)]) and a truncation of the
contour variables U(y, x); it is a function of the configuration, and its truncation sits among the earlier
characteristic functions. Balaban also states that a delta-function axial gauge averaged over lattice symmetries is an
equivalent alternative (p. 247).

**2.6 What this gives (READ).** In the step every factor except the Gaussian reference and the cut is a function of the
configuration, and the configuration is a function of the background and of (scale) x (free variable); the
Gaussian reference is a fixed quadratic form, and the cut is a fixed set that is even in the free variable (Balaban
(3.16); EM's "fixed Borel restriction"). Neither EM nor CMP 119 uses this for the coefficient; EM bounds f by the norm of
F^u. Step 3 uses it.

## Step 3. Theorem PE: the flip symmetry and an even Cauchy estimate (written 2026-11-20T15:21Z by date -u)

Notation. One step k -> k+1 of the unmarked (absolute) chain, frame theta = theta_k, weight x = x_k, tau = x/theta.
Free variables B in R^N (the frame's real free array). g := theta^(-1/2) is the frame's fluctuation scale: the
frame's chart is V'(W, B) = Phi(W, g B), where Phi(W, phi) is the chart in physical units (phi = physical fluctuation);
this is Balaban's scaling A'_k = g_k A_k (2.5). rho := theta^(1/2) delta(theta) = A_1 (log theta)^(p_0) is the cut radius
in the free variables. N := N_(k+1), G := G_(k+1,tau) are EM's Gaussian families (2.4). b := b_(k+1) is the coefficient
map, |b(E)| <= C_x ||E|| on the absolute core (C_x = C a_*^(-2), EM:1201, EM:1383-1384).

**3.1 The interpolation.** For complex h, write the step with the fluctuation scale g replaced by h and the action
weight x = tau/g^2 replaced by tau/h^2, everything else fixed (the frame's Gaussian reference, the cut, the inherited
list, the background). Its integrand is dmu_W(B) 1_Omega(B) exp P(h, B; W), with
    P(h, B; W) := -(tau/h^2) [A(U_k(Phi(W, hB))) - A(U_(k+1)(W))] + (tau/2)<B, Delta_A B>
                  - (1/h^2) Gs(W, hB) + (1/2)<B, Delta_G B>
                  + [S_f(U_k(Phi(W, hB))) - S_f(U_(k+1)(W))] + [log J(W, hB) - log J(W, 0)],
where mu_W is the normalized centred Gaussian with precision Delta(W) (the frame's reference, with EM's weight shift
written as in em:eq-frozen-gaussian-rewrite), Omega is the cut, Gs(W, phi) is the exponent of the gauge weight as a
function of the physical configuration (precision theta, so theta Gs(W, g B) = g^(-2) Gs(W, g B)), and J is the fibre
density in physical coordinates. At h = g the integrand is the actual one, up to field-independent scalars (the
Jacobian g^N of the scaling, the normalizer constants), which have no coefficient. Write E(h) for the prescribed
localization of the step at scale h (with the scalar separated as in EM:563-576) and F(h) := E(h) - N - G. Then
F(g) = F^u_(k+1) and f_(k+1) = b(F(g)).

**3.2 Hypotheses.**
- (S) Structure. (a) mu_W is a centred Gaussian, so mu_W(-S) = mu_W(S) for Borel S; it does not depend on h.
  (b) Omega = -Omega. (c) The four brackets of P are functions of h B alone, or of h B and h^2, except the two
  quadratic forms, which do not depend on h; so P(-h, -B; W) = P(h, B; W) for all h, B, W (Lemma 3.3). (d) The
  background is critical along the fibre and satisfies the gauge condition: the first-order terms of
  A(U_k(Phi(W, phi))) and of Gs(W, phi) in phi vanish at phi = 0, Gs(W, 0) = 0, and Delta_A, Delta_G are the
  second-order Taylor terms; so P extends analytically to h = 0 with P(0, B; W) = 0.
- (H-flip) The prescribed localization is covariant under the orthogonal map O = -I of the free variables in the sense
  that EM input 2 requires for the maps O_(r,W) (EM:643-647): the localization of the step with integrand data
  (mu, Omega, P o O) is the localization of the step with data (O_* mu, O Omega, P), with the same carriers,
  points and branches (the change of variables B' = O B carries the first integral into the second).
- (H-an) There is r > g such that for every complex h with |h| < r the prescribed localization of the step at scale h
  exists, each component of F(h) is holomorphic in h and real for real h, ||F(h)|| <= K_a on the absolute core, and
  the families F(h) meet the hypotheses of em:prop-companion-coefficient uniformly in h.
- (H-tail) ||F(0)|| <= K_t exp(-c theta delta(theta)^2) = K_t exp(-c rho^2): at h = 0 the step is the frame's Gaussian
  with the cut, whose localized logarithm minus N and G is the localized logarithm of the Gaussian mass of the cut.

**3.3 Lemma (joint flip; PROVED, elementary).** Let Phi(W, .) be any map, Q any function of the configuration, and
q a quadratic form. Then T(h, B) := h^(-2) Q(Phi(W, hB)) + Q'(Phi(W, hB)) + q(B) satisfies T(-h, -B) = T(h, B)
for every h != 0 and every B.
*Proof.* (-h)(-B) = hB and (-h)^(-2) = h^(-2), so the first two terms are unchanged; q(-B) = q(B). QED
So every factor of the step that is a function of the configuration, with an inverse-square coupling in front or
none, is invariant under the joint flip, whatever the gauge, the chart or the group. No parity rule degree by degree
(row 1280 (P2)) and no Taylor remainder is needed.

**3.4 Lemma (even holomorphic functions; PROVED, elementary).** Let u be holomorphic on {|h| < r}, even, with
|u| <= M there. Then for |h| < r,
    |u(h) - u(0)| <= M (|h|/r)^2 / (1 - (|h|/r)^2).
*Proof.* u(h) = sum_(n >= 0) a_(2n) h^(2n) on the disc (odd coefficients vanish by evenness), and Cauchy's estimate on
circles of radius s < r gives |a_(2n)| <= M s^(-2n); let s -> r and sum the geometric series over n >= 1. QED

**3.5 Lemma (evenness of the step; PROVED GIVEN (S), (H-flip)).** For |h| < r, F(-h) = F(h), componentwise.
*Proof.* By (S)(c), P(-h, B) = P(h, -B) = (P(h, .) o O)(B) with O = -I. So the data of the step at scale -h are
(mu, Omega, P(h, .) o O). By (H-flip) its localization is that of (O_* mu, O Omega, P(h, .)), and O_* mu = mu,
O Omega = -Omega = Omega by (S)(a)-(b). So E(-h) = E(h); N and G do not depend on h. QED

**3.6 Theorem PE (PROVED GIVEN (S), (H-flip), (H-an), (H-tail)).**
    |f_(k+1)| <= C_x K_a (g/r)^2 / (1 - (g/r)^2) + C_x K_t exp(-c rho^2),
and, for the whole unmarked residual family,
    ||F^u_(k+1)|| <= K_a (g/r)^2 / (1 - (g/r)^2) + K_t exp(-c rho^2).
*Proof.* Fix a component of F (a carrier X, a point z, a field argument in its domain). As a function of h it is
holomorphic on the disc and bounded there by K_a times the inverse of its weight in EM's pointed norm (H-an), and even
(3.5). Lemma 3.4 bounds its change from h = 0 to h = g by that bound times (g/r)^2/(1 - (g/r)^2). Taking the weighted
supremum gives ||F(g) - F(0)|| <= K_a (g/r)^2/(1 - (g/r)^2) (EM's pointed norm is a weighted supremum, monotone,
EM:223-229), and (H-tail) adds ||F(0)||. For the coefficient, u(h) := b(F(h)) is holomorphic on the disc as the locally
uniform limit of holomorphic functions (the companion Hessians at P_o, summed with the moment weights, under the uniform
hypotheses of (H-an)), even by 3.5 and linearity of b, and |u| <= C_x K_a. Lemma 3.4 and |u(0)| <= C_x ||F(0)|| give the
first display. (Shorter: b is linear with |b(E)| <= C_x ||E||, so |f_(k+1) - b(F(0))| <= C_x ||F(g) - F(0)||, and the
family bound gives the first display without the holomorphy of u.) QED
The family bound also needs J(W, 0) to carry no background dependence beyond N (Balaban: the zero-fluctuation factors
are counts, 2.5); otherwise F(0) holds a coupling-free term of one-loop order and the theorem bounds F(g) - F(0).

**3.7 The radius (ARGUED).** On Omega every free variable has |B(b)| < rho (Balaban (3.16); 2.5). Each local piece of P
is then of size at most C (|h| rho^3 + |h| rho) for |h| <= 1/rho: the action beyond second order and the gauge weight
beyond second order are cubic and higher in h B with an h^(-2) in front, the fibre density and the inherited list
enter at first order in h B (the list with its norm E_0 on the absolute radii a_*, EM:667-677), and the constant and
linear terms vanish by (S)(d). So on |h| <= r := c_* rho^(-3) every local piece of P is at most a fixed small multiple
of c_*, which is the same smallness the supplier uses at the actual scale g (there of size g rho^3). A supplier
expansion whose estimates use only that smallness, the frame's Gaussian decay and the Gaussian tail of the cut gives
(H-an) with r = c_* rho^(-3) and K_a of order c_*. Then (g/r)^2 = c_*^(-2) theta^(-1) rho^6 and
    |f_(k+1)| <= C theta_k^(-1) (log theta_k)^(6 p_0) + C exp(-c A_1^2 (log theta_k)^(2 p_0)),
in place of EM's C theta_k^(-1/2) (log theta_k)^(p_0). This is (PE) of row 1280 with q = 6 p_0.

**3.8 What this replaces in row 1280.** (P1) is (S)(a) with (S)(d); (P2), the degree-by-degree parity rule with
Taylor remainders, is replaced by Lemma 3.3, which is exact and needs no expansion, and by (H-an); (P3) is (S)(b); (P4) is
(H-flip), stated in EM's own covariance form. Lemma P of row 1280 (the cosh identity) is not needed.

## Step 4. The inputs of Theorem PE, factor by factor (written 2026-11-20T15:24Z by date -u)

**4.1 (S) for Balaban's all-small-field step (READ, CMP 119 pp. 247, 267-268; with EM:544-606).**
- Gaussian reference: exp(-(1/2)<A_k, C* Delta^(k) C A_k>), centred, no g in the free variables A_k; EM's weight shift
  (tau - 1)<B, Delta_A B>/2 is even and does not depend on h. (S)(a) holds.
- Cut: (3.16), a product over cubes of chi(sup_b |A_k(b)| < delta_k) on the free variables, with the earlier
  characteristic functions equal to 1 on it (p. 268). Each test reads |A_k(b)|, so the cut is even. (S)(b) holds, as
  far as Balaban's text goes (4.3 treats an account cut that is not exactly even).
- Action: the configuration is U_k(exp i[g_k C A_k - h D~(g_k C A_k)] V^(k)), a function of g_k A_k (here h is
  Balaban's operator, not the scale); the action carries 1/g_k^2. Lemma 3.3 applies. The first variation vanishes
  along the free directions because V^(k) is Balaban's constrained minimizer and C maps into the tangent space of the
  linearized constraint; so the 1/h term of the interpolation is zero. If position-dependent couplings 1/g_k^2(.) are
  present, they are scaled with the same 1/h^2 and the background is critical for their sum; outside large-field
  regions they equal 1/g_k^2. (S)(c)-(d) hold.
- Gauge weight: the soft axial weight (1.5) is exp(-g^(-2) sum [1 - Re tr U^u(y, x)]), a function of the configuration
  with 1/g^2 in front; at an axial-gauge background U^u = 1, and 1 - Re tr e^(iX) = O(|X|^2), so its value and first
  variation vanish. In later steps the axial gauge is a delta function removed by C (p. 267), so no weight remains.
  Either way (S)(c)-(d) hold.
- Fibre density and Jacobians: functions of g_k A_k inside P^(k); the zero-fluctuation factors are counts (p. 267,
  log g_k d(g)|B(Gamma)*|, log sigma_0 |B(Gamma)*|, -log z (L^4 - 1)|Gamma|), so they have no coefficient.
- Inherited list: (E_k + R_k + B_k) of the configuration minus its value at U_(k+1) (3.15); in EM, S_f of U_k(V')
  minus S_f at U_(k+1)(W) (EM:556-560). Lemma 3.3 applies with no prefactor; value 0 at h = 0.
- Pivot links: part of the completed chart V'(W, B) (EM:548-549), solved from the constraint, so functions of g B
  (Balaban's D~(g_k C A_k)).
So every factor of the step is of the form of Lemma 3.3. The one structural reading is the scaling form of the chart,
V'(W, B) = Phi(W, theta^(-1/2) B) with Phi free of theta, which is Balaban's A'_k = g_k A_k; EM says only that the frame
fixes the real fluctuation coordinates (EM:504-505), so for the account this is a reading, (S-chart).

**4.2 (H-flip) (ARGUED from the structure of the localization).** The account's transcription of the supplier's
expansion (CA-I I:108483-108507 and I:58700-58730, read in row 1280 4.4') consists of: the centred Gaussian, the Mayer
expansion of local factors e^(v) - 1, the decomposition of the cut into kept and complementary bond indicators,
conditioning, whitening by C(s)^(1/2) and decoupling in s, then polymer and cluster sums. Every localized activity is
an integral over B against a centred Gaussian with a decoupled (real or complex) covariance C(s) of a product of local
factors built from P and of bond indicators. Replacing P by P o O and substituting B -> -B in each such integral gives
the activity built from P with the indicators -Omega, and a centred Gaussian integral is unchanged by B -> -B (also
for complex covariance, by the change of variables in the Lebesgue integral). The conditional means are linear in the
conditioning variables and flip with them; whitening and decoupling are linear. So the localization of (mu, Omega,
P o O) equals that of (mu, -Omega, P), activity by activity, with the same carriers and branches: (H-flip). EM itself
requires the same transport for the orthogonal maps O_(r,W) (EM:643-647); O = -I is the site-wise case, with r the
identity. Not proved here: CMP 116 is not on this machine, and the reading is of the account's transcription.

**4.3 Variant for a cut that is not exactly even (PROVED GIVEN row 1280's Lemma SW and (E+)).** Suppose the cut is a
product of tests 1[t_u(B) < T_u] with |t_u(B) - t_u(-B)| <= Delta_u <= T_u/4 on the integration domain (a thin shell),
and Lemma SW's hypothesis (E+) holds for the pair (Omega, -Omega) uniformly for |h| < r, with outcome
||E_Omega(h) - E_(-Omega)(h)|| <= eta. (H-flip) gives E_(-Omega)(h) = E_Omega(-h), so the odd part
F_o(h) := (F(h) - F(-h))/2 is holomorphic with ||F_o|| <= eta/2 and F_o(0) = 0, and the even part F - F_o is even,
holomorphic and bounded by K_a + eta/2. Lemma 3.4 for the even part gives
    ||F(g) - F(0)|| <= (K_a + eta/2) (g/r)^2/(1 - (g/r)^2) + eta/2,
and eta is a Gaussian tail of the order of row 1280's tau (exp(-(1/2) gamma_2 T_-^2/m'_sig) times constants).

**4.4 Lemma AS (SU(2) path tests are even up to a thin shell; PROVED, elementary).** Let X_1, ..., X_n in su(2) with
s := sum_i |X_i| <= s_0 (s_0 a fixed small number). Put Z_+ := log(e^(X_1) ... e^(X_n)) and
Z_- := log(e^(-X_1) ... e^(-X_n)). Then | |Z_+|^2 - |Z_-|^2 | <= C s^3, hence | |Z_+| - |Z_-| | <= C s^3/(|Z_+| + |Z_-|).
*Proof.* By the Baker-Campbell-Hausdorff series (convergent for s <= s_0), Z_(+/-) = +/- S + C_2 +/- R_3 + O(s^4)
with S = sum X_i, C_2 = (1/2) sum_(i<j) [X_i, X_j] (the same for both signs, since it is quadratic) and R_3 homogeneous
of degree 3. Write Z_(+/-) = +/-(S + R_3) + (C_2 + R_4) + O(s^5) (degree-4 terms are even in X). In the difference of the
squares only cross terms between the odd and the even parts survive: |Z_+|^2 - |Z_-|^2 = 4<S, C_2> + O(s^5) = O(s^3), since
<S, C_2> is a sum of triple products <X_l, [X_i, X_j]> (the terms with l in {i, j} vanish by ad-invariance), each at
most |X_l||X_i||X_j|. QED
So a test |e^(Z) - 1| < eps on a path product of l links of physical size at most g rho (a function of |Z| for SU(2))
and its flipped form differ only on a shell of relative width C l^3 g^3 rho^3/eps^2 at the threshold; for eps of order
g times a power of log theta this is O(theta^(-1/2) polylog), so 4.3 applies with Delta_u of that size. This covers the
soft axial truncation of CMP 119 (1.5) and any test on contour variables, if the account keeps such tests in the cut.

**4.5 (H-an) and (H-tail).** (H-an) is ARGUED in 3.7: on the cut every local piece of P is at most C |h| rho^3, so for
|h| < c_* rho^(-3) the step at scale h is a small-field step of the same kind as the actual one: its local pieces
exceed those at h = g by at most the factor c_*/(g rho^3) and stay below C c_*; its Gaussian reference and cut are the
frame's. A supplier expansion whose estimates use only the per-piece smallness, the Gaussian
decay of C(s) and the tail of the cut gives (H-an). This is a statement about the supplier (Balaban CMP 116 and the
account's one-step theorem), not proved here. (H-tail) is the case P = 0 of the same expansion; its size is EM's term
K exp(-c theta delta(theta)^2) in (em:eq-rs-formation) (READ: EM:682-683).

