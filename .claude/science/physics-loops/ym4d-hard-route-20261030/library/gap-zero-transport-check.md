lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-11T13:38Z

# Check of Route Z (gap-zero-transport) and (TM_B)

Provenance: Claude Opus 5.5, high effort, Mac mini worker 2, commit d76689eed. One line-by-line reading by a model that did not write the proofs. Not an audit. FINISH row 681; brief: `library/gap-skeleton-max-b.md` Part 4 Item 3 (lines 549-554).

Status: complete. Verdicts (table in Section 10): Theorem ZB, Theorem Z, Corollary 5' HOLD AFTER CORRECTION (their shape condition (TUBE) holds for no bounded domain, so as written they are vacuous; repaired by (TUBE') and a Harnack-chain bound, conclusion unchanged); Theorem LP HOLDS AFTER CORRECTION (proof repair at irregular boundary points); Lemma HM, Lemmas 1, 1', 2, 3, Proposition 3 and the Hessian bound HOLD. (TM_B) is written out in Section 9 as a port of row 667.

## 0. Repo search and scope

- Sources read: `library/gap-zero-transport.md` (all 108 lines, the text under check, written by Claude Fable 5.2); `library/gap-skeleton-max-b.md` sections 1.4, 1.5, 1.7, 1.9, 2.5, 3.1 and Part 4 Item 3 (the plan, same author); `library/gap-transfer.md` lines 1-197 (row 667, the torus transfer operator, written by an earlier Claude Opus 5.5 run on this Mini). Credit for (TM_B) below: the construction is row 667's, which ports Sussman and Alpoge's layer transfer operator (GL3, GL8 of `YM4_sketch_500.tex` at 31a47c543775, lines 2196-2335; Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text). Classical credits are as in the files: Luescher, Osterwalder-Seiler (transfer matrix), Jentzsch, Perron-Frobenius, Nevanlinna (two constants), Lebowitz-Penrose, 't Hooft, Borel-Caratheodory, Vitali.
- Duplicate check (rule 0a): `grep` of `library/open-core.md` for TM_B, gap-zero-transport, Theorem ZB, Theorem LP, Lemma HM: no hit. FINISH rows: only this row 681 names TM_B. No other row owns these statements.
- Independence: I did not write `gap-zero-transport.md` or the plan. `gap-transfer.md` was written by a run of the same model (Opus 5.5) on this machine; it is used here as an input, not checked here.
- No numeric job was run. Every step below is by hand.
- Where the two texts state a result differently, I check the version in `gap-zero-transport.md` (it is the later one, and the brief names it) and note the plan version only where it differs in substance.

## 1. Theorem LP (two constants) — `gap-zero-transport.md` line 48; plan 1.7

**Verdict: HOLDS AFTER CORRECTION (proof only; the statement stands as written).**

Defect. The proof says that "limsup of (log|h| - v) at every boundary point is <= 0". With omega the Perron solution this is false at an irregular point zeta of Gamma_2: there omega need not tend to 0, so v = log M - omega log(M/eps) can stay below log M while log|h| tends to log|h(zeta)|, which may equal log M. The statement allows irregular points explicitly, so the proof as written does not cover it. (In the uses below, Gamma_1 is a circular arc, but Gamma_2 is a level set {d = delta}, which can have isolated or irregular points.)

Corrected proof (Perron upper class). If h vanishes identically on Omega the claim is trivial. Otherwise:
1. |h| <= M on Omega, by the maximum modulus principle, since h is continuous on the closure, |h| <= max(eps, M) = M on the boundary, and Omega is bounded.
2. Put s = (log M - log|h|)/log(M/eps) on Omega. It is superharmonic (since -log|h| is superharmonic, with value +infinity at zeros), and s >= 0 by step 1.
3. At zeta in Gamma_1: |h(z)| -> |h(zeta)| <= eps as z -> zeta, so liminf s >= 1. At every boundary point liminf s >= 0. So s is in the upper Perron class of the boundary function 1_{Gamma_1}.
4. 1_{Gamma_1} is a bounded Borel function on the boundary of a bounded plane domain, hence resolutive (Brelot; Wiener), and omega is its Perron solution, the infimum of the upper class. So omega <= s on Omega, which is log|h| <= omega log eps + (1 - omega) log M. QED.

Note for the users (Theorem Z step 3, Theorem ZB step 2). The truncated sets D_j, D_k = {beta in D: Re beta > 0, |beta| > r_0, d(beta) > delta} need not be connected. Apply LP on each component; on a component whose boundary does not meet the arc, omega = 0 and the bound is |h| <= M, which is what the stated bounds give there. No change to any conclusion.

## 2. Lemma HM (half-strip) — `gap-zero-transport.md` lines 51-53; plan 1.7

**Verdict: HOLDS.** Checked:
- Put a = pi/(2w) and z = x + iy. The series equals (4/pi) Re arctan(e^{-a z}) for x > 0 (power series of arctan, |e^{-az}| < 1; the real part of the k-th term is (-1)^{(k-1)/2} e^{-akx} cos(aky)/k). It is harmonic.
- z -> e^{-az} maps the half-strip onto the half-disc {|zeta| < 1, Re zeta > 0}. On y = +-w, e^{-az} = -+ i r with 0 < r < 1, and arctan(-+ i r) = -+ i artanh r is purely imaginary: value 0. As z -> (0, y_0) with |y_0| < w, zeta -> e^{-i a y_0} with cos(a y_0) > 0, and Re arctan(e^{i phi}) = pi/4 when cos phi > 0: value 1. So the boundary values are attained in the full (not only radial) sense, except at the two corners.
- Uniqueness among bounded harmonic functions with these boundary values off the two corners: the difference of two such is bounded, harmonic, and tends to 0 at every boundary point except two; points are polar, so the extended maximum principle (or Phragmen-Lindeloef in the strip) gives 0. The file's citation of Phragmen-Lindeloef is adequate.
- On the axis the sum is arctan q with q = e^{-ax} in (0, 1). arctan is concave on [0, infinity) (second derivative -2q/(1+q^2)^2 <= 0) with arctan 0 = 0 and arctan 1 = pi/4, so arctan q >= (pi/4) q on [0, 1]. Hence omega(x, 0) >= e^{-pi x/(2w)}.
- Monotonicity in the domain (line 53): correct when Gamma_1 lies in the boundary of both domains and its points are regular for the larger one (true for a circular arc or a segment: every point of a non-degenerate continuum in the boundary is regular in the plane). Then on the smaller domain omega' is a nonnegative harmonic function with boundary values >= 1 on Gamma_1, so it lies in the upper class and dominates omega (same argument as Section 1, step 4).

## 3. Theorem ZB (boxes with free walls) — `gap-zero-transport.md` lines 90-98; plan 2.5

**Verdict: HOLDS AFTER CORRECTION. As written the theorem is vacuous: no domain satisfies its hypotheses (defect Z1 below). With the shape condition replaced by (TUBE') and two small additions to the hypotheses, the statement and its conclusion m_B(beta) >= kappa_0 omega_D(beta) hold. The proof of step 1 is replaced, and the limit k -> infinity of step 4 is proved below (the file gives it one clause).**

### 3.1 Defect Z1: (TUBE) is inconsistent with a bounded domain

(TUBE), as stated (line 57): for every beta = x + iy in D with x >= 0, the closed disc with centre x (on the real axis) and radius |y| + theta d(beta) lies in D.

**Claim.** If D is bounded and satisfies (TUBE) with any theta >= 0, then D contains no point beta with Re beta >= 0 and Im beta != 0. Since D must contain the disc |beta| <= r_0, no domain satisfies the hypotheses of Theorem Z or Theorem ZB.

Proof. Let beta_0 = x_0 + i y_0 in D with x_0 >= 0, y_0 != 0, and fix n >= 1. Pick angles alpha_1, ..., alpha_{n-1} in (0, pi/2) and alpha_n = 0 with cos alpha_1 = sin alpha_1 cos alpha_2 = ... = sin alpha_1 ... sin alpha_{n-1} = 1/sqrt(n) (the spherical coordinates of the unit vector (1, ..., 1)/sqrt(n) of R^n). Put z_0 = x_0 + i|y_0| (in D by symmetry) and z_{j} = Re z_{j-1} + |Im z_{j-1}| e^{i alpha_j}. By induction Re z_j >= x_0 >= 0, and z_j lies on the circle with centre Re z_{j-1} and radius |Im z_{j-1}|, which is inside the closed disc that (TUBE) puts in D at z_{j-1}. So every z_j is in D. Then z_n is real and Re z_n = x_0 + |y_0| (cos alpha_1 + sin alpha_1 cos alpha_2 + ...) = x_0 + sqrt(n) |y_0|. This is unbounded in n, against boundedness of D. QED.

Concrete case, n = 4, theta = 0, D the unit disc: the point 0.905 + 0.125 i is in D, but the disc with centre 0.905 and radius 0.125 contains 1.03, outside D. The file's remark in the plan (1.9: "A strip satisfies it") is true for the unbounded strip, but Theorem Z and Theorem ZB need D bounded (for Theorem LP and for the bound M with X), and every cut of a strip fails at its right end.

### 3.2 Repair: (TUBE') and a Harnack chain in place of the one-disc bound

**(TUBE').** There is theta in (0, 1] such that for every beta = x + iy in D with x >= 0, and every real t between 0 and y: x + it is in D and d(x + it) >= theta (|y| - |t| + d(beta)).

Sufficient condition (a "Lipschitz lens"). Let D = {x + iy: -2 r_0 < x < X, |y| < h(x)} with h > 0 Lambda-Lipschitz on (-2 r_0, X), h -> 0 at both ends, sqrt(r_0^2 - x^2) < h(x) on [-r_0, r_0] and h(x) < sqrt(4 r_0^2 - x^2) for x <= 0. Then D is bounded, symmetric, simply connected, contains |beta| <= r_0, its part in Re beta <= 0 lies in |beta| < 2 r_0, D intersected with {|beta| < 2 r_0} is connected (both sets are vertically convex and contain the real segment of their common slices), and (TUBE') holds with theta = (1 + Lambda^2)^{-1/2}. Proof of the last point: for x + it with |t| < h(x), the ball of radius (h(x) - |t|)(1 + Lambda^2)^{-1/2} about it lies under the Lipschitz graph (a cone of slope Lambda fits under it), and it stays in -2 r_0 < Re < X because h(x) <= Lambda min(x + 2 r_0, X - x). So d(x + it) >= (h(x) - |t|)(1 + Lambda^2)^{-1/2}, and h(x) - |t| = (h(x) - |y|) + (|y| - |t|) >= d(beta) + (|y| - |t|), since d(beta) <= h(x) - |y|. The plan's intended domain (strong-coupling disc, a tube over [r_0, beta_1], the asymptotic strip of half-width tending to 11/(6 pi)), cut by a wedge end at X, is of this form as long as its upper boundary is a Lipschitz graph; this is a condition the harmonic-measure item (N5) must respect.

**Lemma S (replaces step 1 of Theorem ZB and of Theorem Z).** Let D satisfy (TUBE'). Let L be analytic on D with Re L <= A on D (A >= 0), and for real x >= 0 in D let L(x) be real with -bx <= L(x) <= 0. Then for beta = x + iy in D with x >= 0 and delta = d(beta):
|L(beta)| <= 3 (A + 2bx) (1 + |y|/delta)^{4.4/theta}.

Proof. By symmetry take y > 0. Put rho(t) = y - t + delta, p(t) = x + it, so d(p(t)) >= theta rho(t). Let t_0 = 0 and t_{j+1} = min(y, t_j + (theta/4) rho(t_j)); while t_j < y, rho(t_{j+1}) = (1 - theta/4) rho(t_j), and rho >= delta, so y is reached after N <= 1 + (4/theta) log((y + delta)/delta) steps (using -log(1 - s) >= s). Write p_j = p(t_j); then |p_{j+1} - p_j| <= d(p_j)/4.
(i) P = A - Re L is harmonic and >= 0 on D. Harnack's inequality on the disc of radius d(p_j) about p_j, at distance r <= d(p_j)/2: P <= ((R + r)/(R - r)) P(p_j) <= 3 P(p_j). So P(p_j) <= 3^j P(p_0) <= 3^j (A + bx).
(ii) Borel-Caratheodory for g = L - L(p_j) on the closed disc of radius R = d(p_j)/2 about p_j (inside D), at r = |p_{j+1} - p_j| <= R/2: |g| <= (2r/(R - r)) max Re g <= 2 max (P(p_j) - P) <= 2 P(p_j). (The form used, |g(z)| <= 2r/(R - r) max_{|w|=R} Re g(w) for g(centre) = 0, holds with no sign condition because the mean of Re g on the circle is 0.)
(iii) Summing, |L(beta) - L(x)| <= 2 (A + bx) (1 + 3 + ... + 3^{N-1}) <= 3^N (A + bx), so |L(beta)| <= bx + 3^N (A + bx) <= 3^N (A + 2bx). Finally 3^N <= 3 ((y + delta)/delta)^{(4 log 3)/theta} and 4 log 3 < 4.4. QED.

Use in Theorem ZB: A = 24 k|B| r_0, b = 12 k|B|, so for beta in D, Re beta >= 0, d(beta) >= 1/k, Re beta <= X, |Im beta| <= H:
|L_1|, |L_q| <= 72 k|B| (r_0 + X)(1 + H k)^{4.4/theta}, and M_k := 144 k|B| (r_0 + X)(1 + H k)^{4.4/theta}.
M_k is polynomial in k, so (1/k) log max(M_k, 1) -> 0 as k -> infinity, which is all that step 4 needs. The constant changes; the conclusion of Theorem ZB does not.

### 3.3 Two hypotheses to add

- **(X)** D lies in {Re beta < X}. Step 2 bounds |g_q| by M_k using Re beta <= X at points with d = 1/k; the statement only says D contains [0, X). Since D is bounded one may instead put X := sup Re over D; the conclusion of Theorem ZB does not involve X.
- **(C)** D intersected with {|beta| < 2 r_0} is connected. Step 2 applies (SC_B) on the segment of the imaginary axis in the boundary of D_k. (SC_B) holds for the branch of the logarithm that is real on the real axis in the disc |beta| <= 2 r_0; the proof uses the branch on D. Both are analytic on D intersected with the disc and equal (to 0) at beta = 0, so they agree on the component of that set that contains 0, but on another component they can differ by 2 pi i m (for L_1) or 2 pi i m/q (for L_q), and then the bound on the segment fails. (C) removes this; the Lipschitz lens satisfies it. (Remark: the branch of log Z on D that vanishes at 0 is real at every real point of D, by conjugation symmetry: L(conj beta) conj is another branch equal at 0.)

### 3.4 Steps 2-3 checked

- Step 2: the boundary of D_k lies in the arc {|beta| = r_0, Re beta >= 0}, the segment of the imaginary axis in D (inside |beta| < 2 r_0 by hypothesis), and {d = 1/k}. The bounds on the three pieces are right (with Lemma S for the third). Theorem LP is applied with Gamma_1 = the arc part and Gamma_2 = the rest (on the segment |g_q| <= eps_k <= max(eps_k, M_k), so taking the smaller harmonic measure of the arc alone is allowed). The bound eps_k^{omega} M_k^{1 - omega} <= max(M_k, 1) max(C_0|B|k, 1) e^{-kappa_0 omega k} is right, and in the case eps_k >= M_k the maximum principle gives |g_q| <= eps_k, which is below the same right side. Uniform in q: yes.
- Step 3: for real beta in D_k, with the real branch, g_q = log(1 + s_k) - (1/q) log(1 + s_{qk}) (the powers of lambda_0 cancel). Since lambda_0 is simple and T_B >= 0, every r_i = lambda_i/lambda_0 lies in [0, r_1] with r_1 < 1, so s_{qk} <= r_1^{(q-1)k} s_k -> 0. The limit q -> infinity gives log(1 + s_k) <= R_k. Correct.
- Step 4: e^{-k m_B} = r_1^k <= s_k <= e^{R_k} - 1 <= 2 R_k once R_k <= 1 (e^x - 1 <= x e^x <= e x). R_k -> 0 because omega_k(beta) increases to omega_D(beta) > 0 (if omega_D(beta) = 0 the claim is empty) and M_k grows polynomially. |B| is fixed while k -> infinity, so the factor |B| drops out: this is why the bound is uniform in B. Correct, given the limit below.

### 3.5 The limit k -> infinity: omega_k(beta) -> omega_D(beta)

The file says "harmonic measure is monotone in the domain and continuous under increasing unions". Monotone: correct (Section 2, last item; arc points are regular for every D_k). "Continuous under increasing unions" is not proved and is not true without conditions on the boundary data (the data 1_arc is discontinuous at the arc's end points). Proof for the present case:

Let D' = {beta in D: Re beta > 0, |beta| > r_0}, omega = omega_D on D', delta_0 = dist(closed disc |beta| <= r_0, boundary of D) > 0.
1. Regularity. Every point zeta of the boundary of D is regular for D': C minus D is connected (D is bounded and simply connected), contains zeta and other points, and lies in C minus D'. A barrier at zeta: with a != zeta in that connected set E, z -> log((z - zeta)/(z - a)) has a single-valued branch on C minus E, and b = -Re(1/log((z - zeta)/(z - a))) is positive harmonic near zeta in D' and tends to 0 at zeta (Lebesgue-Bouligand; classical, Ransford Thm 4.2.2). Points of the imaginary axis and of the arc are regular too (the complement of D' contains a half-plane, respectively the closed disc).
2. Continuity at the boundary. The data 1_arc is 0 near the boundary of D (the arc is at distance >= delta_0), so omega tends to 0 at every point of the boundary of D and of the imaginary-axis segment (regular point, data continuous there: barrier argument). Hence the function equal to omega on D' and 0 on (D minus D') and on the boundary of D is continuous on the compact set K = {zeta in closure(D): d(zeta) <= delta_0/2}, which contains no arc point. So eta_k := sup{omega(zeta): zeta in D', d(zeta) = 1/k} -> 0 (uniform continuity on K, and every such zeta is within 1/k of a point of the boundary of D, where the function is 0).
3. Comparison. For k > 2/delta_0, u = omega - omega_k - eta_k is harmonic and bounded on D_k. At boundary points of D_k on the arc both omega and omega_k tend to 1; on the imaginary segment omega tends to 0 and omega_k >= 0; at points with d = 1/k, omega <= eta_k and omega_k >= 0. So limsup u <= 0 at every boundary point of D_k except possibly the two end points +-i r_0 of the arc. A bounded subharmonic function with limsup <= 0 off a finite set of boundary points of a bounded plane domain is <= 0 (add epsilon sum log(|z - p|/diam) and let epsilon -> 0). So omega - eta_k <= omega_k <= omega on D_k.
Hence omega_k(beta) -> omega_D(beta), and step 4 gives m_B(beta) >= kappa_0 omega_D(beta). Even without this step the proof gives m_B(beta) >= kappa_0 omega_Omega(beta) for every open Omega in D' with inf over Omega of d > 0 and the arc in its boundary (Omega lies in D_k for large k), which is what a comparison-domain proof of (N5) would use anyway.

### 3.6 Corrected statement

**Theorem ZB (corrected).** Let D be a bounded, simply connected domain, symmetric under conjugation, with |beta| <= r_0 in D, [0, X) in D and D in {Re beta < X}, D intersected with {Re beta <= 0} inside {|beta| < 2 r_0}, D intersected with {|beta| < 2 r_0} connected, and (TUBE') with theta. Assume (TM_B) (Section 9 below), (SC_B), and (ZF_B): Z(k, B; beta) != 0 for beta in D and k >= k_0. Then for every real beta in D with beta > r_0: m_B(beta) >= kappa_0 omega_D(beta), with omega_D the harmonic measure of the arc {|beta| = r_0, Re beta >= 0} in {beta in D: Re beta > 0, |beta| > r_0}. Proof: the file's steps 2-4 with Lemma S as step 1 and 3.5 for the limit.

Inputs still open: (SC_B) (queue item `gap-sc-box`) and (ZF_B). Not checked here: whether (SC_B) as stated is true; I only note that its form (only polymers winding the time circle survive in the difference; such a polymer has at least 4k plaquettes) is the right one.

## 4. Corollary 5' — `gap-zero-transport.md` line 100; plan 2.5

**Verdict: HOLDS AFTER CORRECTION** (inherits Section 3; one more defect).

- It applies Theorem ZB box by box. Since the bound of Theorem ZB does not depend on B, on k_0(B) or on X, the conclusion m_B(beta) >= kappa_0 eps a(beta) is uniform in the box. Correct.
- Defect: D is bounded (Theorem ZB needs it), so "for real beta >= beta_1" can only mean real beta in D with beta >= beta_1. Corrected statement: if the hypotheses of corrected Theorem ZB hold on a family of domains D_X (one for each cut X, with the same r_0, C_0, kappa_0; theta may depend on X) and omega_{D_X}(beta) >= eps a(beta) for real beta in [beta_1, X - s], then m_B(beta) >= kappa_0 eps a(beta) for those beta. Taking X -> infinity covers every beta >= beta_1. Since omega is monotone in the domain, the (HM) bound for a lens D_X is implied by the same bound for any smaller comparison domain that contains the arc.
- The plan's physical reading ("a gap of at least kappa_0 eps in physical units") is m_B/a(beta) >= kappa_0 eps. Correct as arithmetic.
- (HM) and (ZF_B) are open; the shape of D must satisfy (TUBE') (or another condition that makes Lemma S hold with M_k subexponential in k). This is a new constraint on node N5: the domain bounded by the curves on which a(beta) is imaginary must be cut by a Lipschitz (for example wedge-shaped) end, and its upper boundary must be a Lipschitz graph.

## 5. Theorem Z (periodic tori, zero-flux sector) — `gap-zero-transport.md` lines 57-71; plan 1.9

**Verdict: HOLDS AFTER CORRECTION.** Same defect Z1 as Theorem ZB (vacuous as written), the same two added hypotheses (X), (C), and three changes to the constants.

Line-by-line:
- Step 1, upper bound: |Z^(0)| <= (1/8) sum |Z_k| <= exp(12 n^4 max(0, -Re beta)) (Lemma 3(b)), so Re f_j <= 24 r_0 on D. Correct.
- Step 1, real axis: Z^(0)(x) >= lambda_0^{n} >= exp(n^4 f_inf(x)) >= exp(-12 x n^4) (Lemma 1(d), Lemma 1'), and Z^(0) <= Z <= 1. At x = 0 every Z_k = 1. Correct.
- Step 1, the bound of item 1: the Borel-Caratheodory arithmetic is right (2|y|/(theta d) 24 r_0 + (1 + 2|y|/(theta d)) 12 x <= 12 (2 r_0 + x)(1 + 4|y|/(theta d))), but the disc it uses does not exist (Z1). Replace by Lemma S with A = 24 r_0, b = 12: |f_j(beta)| <= 72 (r_0 + x)(1 + |y|/d(beta))^{4.4/theta}. This is the corrected item 1.
- Step 1, part Re beta <= 0: (SC) gives |f_j| <= sup_{|beta| <= 2 r_0} |f_inf| + C_0 there, for the disc branch. It equals the D-branch only under (C).
- Step 2: f_j(x) -> f_inf(x) on the real interval because f_inf <= f^(0)(n_j) <= f(n_j) (Lemma 1') and f(n_j) -> f_inf (Lemma 1(c)). Local boundedness from step 1. Vitali (classical; locally bounded analytic functions converging on a set with a limit point in a domain converge locally uniformly). The limit equals the (SC) function f_inf on the disc by the identity theorem along (0, r_0). Correct.
- Step 3: u_j = f_j - f_inf, |u_j| <= M_j := 144 (r_0 + X)(1 + H n_j)^{4.4/theta} on {d = 1/n_j} (corrected), eps = C_0 e^{-kappa_0 n_j} on the arc and on the imaginary segment (needs (C)). Theorem LP: Delta^(0)(n_j^4; beta) = n_j^4 u_j(beta) <= n_j^4 max(M_j, 1) max(C_0, 1) e^{-kappa_0 omega_j(beta) n_j}. The file writes M_j where max(M_j, 1) is needed (M_j can be < 1 if r_0 + X < 1/144 with the old constant 48; harmless, but the stated inequality is then not what LP gives).
- Step 4: e^{-n m^(0)} <= e^{Delta^(0)} - 1 <= 2 Delta^(0) for Delta^(0) <= log 2 (e^x - 1 <= x e^x). With the corrected M_j: m^(0)(n_j^3; beta) >= kappa_0 omega_j(beta) - ((4 + 4.4/theta) log n_j + c)/n_j, c = log(2 max(144 (r_0 + X)(1 + H)^{4.4/theta}, 1) max(C_0, 1)). The file's "5 log n_j" and "c depending on r_0, X, theta, C_0 only" change: the coefficient becomes 4 + 4.4/theta, and c depends on H too. (Even with the file's own M_j, c depends on H through log(1 + 4H/theta).)

Corrected item 3 and 4 as just stated. Items 1-2 corrected as in Step 1. Remark (iii) ("omega_j increases to omega_D") is Section 3.5 with delta_j = 1/n_j; it holds.

The warning of Section 6 of the file (periodic tori admit only the narrow strip, so Theorem Z cannot give a continuum gap) is a physical argument, not a theorem; I did not check it. Corollary A and Corollary B are not in my brief; Corollary A's limit statement uses 3.5 and holds after the same corrections; its explicit strip bound c(r_0, w) exp(-pi beta/(2w)) was not checked.

## 6. Lemmas 1, 1', 2, 3 — `gap-zero-transport.md` lines 22-44; plan 1.5

### Lemma 1 (free energy bounds the spectrum). **Verdict: HOLDS.**
- (a) sum mu^{k+1} <= mu_max sum mu^k <= (sum mu^k)^{1 + 1/k}, which is the monotonicity; lambda_0^k <= Tr A^k <= lambda_0^{k-1} Tr A gives the limit (trace class is used here). Correct.
- (b) Correct (max_{j>=1} r_j^{k'} <= S(k')).
- (c) Correct. Two points the text leaves implicit, both harmless: (TM) is needed for boxes with unequal sides (n_2, n_3, n_4), while row 667 builds the cubic N^3 torus only; the construction is the same word for word (only the lattice changes; see Section 9, which does it for a general finite spatial graph). And monotonicity in n_mu holds for n_mu >= 3 (where Z = Tr T^{n_mu}), which is the domain of f. The bound f >= -12 beta uses 6|n| plaquettes with a_p <= 2. The limit argument for a coordinatewise non-increasing function bounded below is right.
- (d) Correct. Here S counts the eigenvalues of T_P on all of L^2; those off the gauge-invariant subspace are 0 and do not contribute.

### Lemma 1' (zero flux). **Verdict: HOLDS.**
Z^(0) = Tr(T^{n_1} P_0) is the trace of the restriction of T^{n_1} to H_0 (P_0 commutes with T, compute in a basis adapted to H_0 + H_0^perp), so Z^(0) = lambda_0^{n_1}(1 + S^(0)) because Psi_0 is in H_0 (Lemma 3(c)). Z^(0) >= lambda_0^{n_1} >= exp(|n| f_inf) gives Delta^(0) >= 0. Z - Z^(0) = Tr((1 - P_0) T^{n_1} (1 - P_0)) >= 0 gives Delta^(0) <= Delta. The gap bound follows as in Lemma 1(d) (if H_0 has no second eigenvalue, m^(0) = infinity and the bound is empty).

### Lemma 2 (integral formula). **Verdict: HOLDS.**
F(n; .) is real-analytic on R (Z entire and positive on R), F' = -6|n| abar, F'' = variance >= 0. f_inf is a pointwise limit of convex functions on [0, infinity) (at beta = 0 every f(n) = 0; for beta > 0 by Lemma 1(c)), hence convex. It is continuous at 0 because -12 beta <= f_inf <= 0. A convex function continuous on [0, beta] is absolutely continuous there (its right derivative is monotone, and f(beta) - f(eps) = integral of f' over [eps, beta] tends to a finite limit as eps -> 0, so f' is integrable; in fact here the difference quotients at 0 are >= -12, so f_inf is Lipschitz on [0, beta]). Delta(n; 0) = 0 and both sides of the formula have the same derivative almost everywhere. The ">= 0" in the plan's version is Lemma 1(c).

### Lemma 3 (centre flips and twists). **Verdict: HOLDS.**
- (a) A spatial plaquette in a plane (i, j) has its two i-links at the same coordinate x_i, so it has 0 or 2 flipped links; -1 is central, so U_p is unchanged; planes without direction i have none. A time-like plaquette on a link b contains U(t)_b and U(t+1)_b once each; both flipped leaves its holonomy unchanged. The flip commutes with the gauge action (-1 is central: h . (u^C) = (h . u)^C), so the kernel A_T of row 667 satisfies A_T(u^C, v^C) = A_T(u, v) and C_i commutes with P and with T_P. The flip is a measure-preserving involution. Correct.
- (b) The kernel of T_P C is A_T(u, w^C); in the trace (row 667, Lemma A0(e)) the last factor carries U(1)^C. On the flipped links the time-like plaquettes of the last step get holonomy multiplied by -1, so 1 - (1/2) tr becomes 1 + (1/2) tr (tr is real on SU(2)). Entire, positive on R (positive integrand), and the modulus bound (0 <= 1 +- (1/2) tr <= 2) are right.
- (c) Correct (simplicity, C_i^2 = 1, positivity of Psi_0, which is row 667 statement (4c)).
- (d) Correct, and slightly more is true: it suffices that the loop has winding number 0 in direction i (total crossings of the flipped layer are congruent to the net crossing number mod 2).

## 7. Proposition 3 (uniform count of states) — plan 1.5

**Verdict: HOLDS (as an implication from (ST5) at W = 0 and (V-ext); one line of the proof mixes units and is corrected here).**

The proof writes "f_inf >= liminf (V_{a,l'} - C_- l'^4)/l'^4". f_inf is per lattice site, the right side is per physical volume. Written out: with n' = l'/a, f_inf = lim F(n')/n'^4 (Lemma 1(c) along symmetric tori) and F(n') = log Z_{a,l'} >= V_{a,l'} - C_- l'^4, so f_inf >= a^4 liminf (V_{a,l'}/l'^4 - C_-) >= a^4 (V_{a,l}/l^4 - C_V - C_-) by (V-ext). Hence (l/a)^4 f_inf >= V_{a,l} - (C_V + C_-) l^4 and Delta_a(l) = log Z_{a,l} - (l/a)^4 f_inf <= (C_+ + C_- + C_V) l^4. This is the stated bound.

Count: with H = -(1/a) log T on the box (l/a)^3 and time n_1 = l/a, S(n_1) = sum_{i>=1} e^{-l (E_i - E_0)}. If N eigenvalues (with multiplicity, including E_0) lie in [E_0, E_0 + E], then N e^{-lE} <= 1 + (N - 1) e^{-lE} <= 1 + S(n_1) <= e^{Delta} (Lemma 1(d)). So N <= exp(lE + (C_+ + C_- + C_V) l^4), uniformly in a. Correct.

Not checked: whether (ST5) of the account is stated as quoted (lines 98405-98413 of the complete account were not opened in this run); (V-ext) is an added hypothesis the account does not state (the plan says so). The paragraph "Meaning" after the proposition is not part of it and is not a proof: a weak limit of spectral measures with at most N atoms below E gives discrete spectrum below E, but "spec(H_l) in {0} union [m(l), infinity) with m(l) > 0" needs also that the vacuum stays simple in the limit, or must be read on the orthocomplement of ker H_l.

## 8. The Hessian bound of 1.4 — plan 1.4, "Attack on (HESS): the numbers"

**Verdict: HOLDS** (the bound Hess a_p >= -5 sum_{b in p} |v_b|^2 and Ric + beta Hess A >= 2 - 30 beta). The Bakry-Emery criterion that turns it into a Poincare inequality is classical and cited, not rebuilt. The heuristic paragraphs of 1.4 ((DEF), "the other end", the Langevin rate) are labelled heuristics in the plan and are not checked.

Checked:
- SU(2) = unit S^3 in R^4, round metric, Ric = 2 g. Left and right multiplications are isometries, t -> U e^{i t y.sigma} is a geodesic of speed |y|, and on a product manifold the Hessian along v is the second derivative along the product of geodesics.
- U_p(t) = U_1 e^{ity_1.s} U_2 e^{ity_2.s} e^{-ity_3.s} U_3^{-1} e^{-ity_4.s} U_4^{-1} = e^{it w_1.s} e^{it w_2.s} e^{it w_3.s} e^{it w_4.s} U_p, with w_b obtained from +-y_b by rotations (conjugation), so |w_b| = |v_b|. The order is fixed by the plaquette; the bound below does not use it.
- prod_b e^{it w_b.s} = 1 + it W.s - (t^2/2) |W|^2 - i t^2 sum_{b<b'} (w_b x w_b').s + O(t^3), W = sum w_b, using (a.s)(b.s) = a.b + i (a x b).s. With (1/2) tr((w_0 + i w.s)(u_0 + i u.s)) = w_0 u_0 - w.u: a_p(t) = 1 - u_0 + t W.u + (t^2/2) u_0 |W|^2 - t^2 u.sum_{b<b'} (w_b x w_b') + O(t^3). So Hess a_p(v, v) = u_0 |W|^2 - 2 u.sum_{b<b'} w_b x w_b', as stated.
- |W|^2 <= 4 sum |w_b|^2; |sum_{b<b'} w_b x w_b'| <= sum_{b<b'} |w_b||w_b'| = ((sum |w_b|)^2 - sum |w_b|^2)/2 <= (3/2) sum |w_b|^2; so Hess a_p >= -(4|u_0| + 3|u|) sum |v_b|^2 >= -5 sum |v_b|^2 (Cauchy-Schwarz, u_0^2 + |u|^2 = 1).
- Each link is in 2(d-1) = 6 plaquettes for d = 4 (sides >= 3), so Hess A >= -30 |v|^2 and Ric + beta Hess A >= (2 - 30 beta) g for every configuration and every volume. Correct.
- U(1): Ric = 0 and Hess a_p = cos(theta_p) (sum +-v_b)^2 takes negative values, so the criterion never holds for beta > 0. Correct.

## 9. (TM_B) written out: the transfer operator of a box with free walls

Credit: this is the construction of FINISH row 667 (`library/gap-transfer.md`, statements (1)-(5)), which ports Sussman and Alpoge's layer transfer operator (GL3, GL8; `YM4_sketch_500.tex` at 31a47c543775, lines 2196-2335; Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text); classical sources Luescher (1977) and Osterwalder-Seiler (1978), not read. Row 667's general lemmas A0-A4 hold for any compact metric probability space and are reused verbatim. Only the lattice changes. Standing: proved here as a port of row 667, which is itself awaiting its check by another model; I read row 667's steps 1.1-5.7 and A3 in full while porting and found no failing step, but row 667 was written by the same model (Opus 5.5) as this check, so that reading is not an independent check.

**Setting.** B = {0, ..., L_1 - 1} x {0, ..., L_2 - 1} x {0, ..., L_3 - 1} in Z^3 (the argument works for any finite set B of sites). Links E_B = {(x, i): x, x + e_i in B}; spatial plaquettes P_B = {(x; i < j): x, x + e_i, x + e_j, x + e_i + e_j in B}; |E_B| <= 3|B|, |P_B| <= 3|B|. X_B = G^{E_B} with product Haar measure du, H_B = L^2(X_B). Gauge group G^B acting by (h . u)_{(x,i)} = h(x) u_{(x,i)} h(x + e_i)^{-1}. Space-time B x Z_k, k >= 2: spatial links (x, i, t) for (x, i) in E_B; time-like links (x, t) for x in B; spatial plaquettes (p, t) for p in P_B; one time-like plaquette (x, i, t) for each (x, i) in E_B and t in Z_k. These are exactly the plaquettes of the box with free walls of `gap-zero-transport.md` Section 6 (a plaquette is present when its four links are). Z(k, B; beta) = int exp(-beta sum_P (1 - (1/2) tr U_P)) dU.

**Objects.** V_B(u) = beta sum_{p in P_B} (1 - (1/2) tr u_p), in [0, 2 beta |P_B|]. c(g) = exp(-beta (1 - (1/2) tr g)). K_B(u, v) = prod_{l in E_B} c(u_l v_l^{-1}), in [e^{-2 beta |E_B|}, 1]. T_0(u, v) = e^{-V_B(u)/2} K_B(u, v) e^{-V_B(v)/2}. A_B(u, v) = int_{G^B} T_0(u, h . v) dh. T_B = the integral operator on H_B with kernel A_B (equal to P T P = T P with T the operator of kernel T_0 and P the gauge average, as in row 667 (1a)). kappa_B := exp(-2 beta (|P_B| + |E_B|)) >= exp(-12 beta |B|).

**Statement (TM_B).** Let beta > 0 be real.
(a) A_B is real, symmetric, continuous, gauge invariant in each variable, and kappa_B <= A_B <= 1.
(b) T_B is bounded, self-adjoint, T_B >= 0, and trace class with Tr T_B <= int e^{-V_B} du <= 1.
(c) Z(k, B; beta) = Tr T_B^k for every k >= 2.
(d) lambda_0 = ||T_B|| is a simple eigenvalue of T_B on H_B, kappa_B <= lambda_0 <= 1; its eigenvector Omega has a continuous, gauge-invariant representative with kappa_B <= Omega <= 1/kappa_B; T_B maps every nonzero f >= 0 to a function >= kappa_B int f > 0 everywhere.
(e) Every other eigenvalue lambda_i (i >= 1, with multiplicity) satisfies 0 <= lambda_i <= lambda_0 (1 - kappa_B^2). So m_B = log(lambda_0/lambda_1) >= -log(1 - kappa_B^2) > 0, and for every k >= 2, Z(k, B; beta) = lambda_0^k (1 + s_k) with s_k = sum_{i>=1} (lambda_i/lambda_0)^k <= (1 - kappa_B^2)^{k-1} (Tr T_B)/lambda_0 < infinity.
(f) If at least two of the L_i are >= 2 (so P_B is non-empty), lambda_1 > 0 and m_B < infinity. (Not needed by Theorem ZB. If P_B is empty, for example a one-dimensional box, T_B restricted to gauge-invariant functions is lambda_0 times the projection on constants: this is the plan's two-dimensional test of 2.5.)

**Proof (by row 667, step by step, with the replacements Lambda -> B, E -> E_B, spatial plaquettes -> P_B, G^V -> G^B, and the constants e^{-12 beta N^3} -> kappa_B).**
1. Plaquettes and factorization (row 667, 1.1-1.2). A time-like plaquette at (x, t) in the plane (0, i) exists exactly when (x, i) is in E_B; its holonomy is g_t(x) U(t+1)_{(x,i)} g_t(x + e_i)^{-1} U(t)_{(x,i)}^{-1} = (g_t . U(t+1))_{(x,i)} U(t)_{(x,i)}^{-1}; for k >= 2 these plaquettes are distinct. V_B(h . u) = V_B(u) because (h . u)_p = h(x) u_p h(x)^{-1} for p in P_B based at x. No step uses periodicity in space. Hence e^{-S} = prod_{t in Z_k} T_0(U(t), g_t . U(t+1)), as in (1.2).
2. Gauge average and trace identity (row 667, 1.3-1.7). Each g_t occurs in one factor; integrating it gives A_B(U(t), U(t+1)). The properties of A_B in (a) follow as in 1.4: continuity by uniform continuity on the compact X_B x G^B x X_B; bounds from e^{-V_B/2} >= e^{-beta |P_B|} and K_B >= e^{-2 beta |E_B|}; invariance and symmetry from the invariance of Haar measure. P is an orthogonal projection and T P = S_{A_B} = P T P (1.5-1.6). By Lemma A0(e) and Fubini, Z(k, B; beta) = int prod_t A_B(U(t), U(t+1)) prod_t dU(t) = Tr T_B^k (1.7). This is (c).
3. Positivity (row 667, 2.2-2.4). The Gram expansion (2.2) holds with I = E_B x {1,2}^2, sum_i |iota_i(u)|^2 = 2|E_B| and w_n = e^{-beta |E_B|} (beta/2)^n/n!; so the operator with kernel K_B is >= 0, hence T >= 0 and T_B = P T P >= 0. Bounded and self-adjoint since A_B is real, symmetric and <= 1.
4. Trace class (row 667, 3.2-3.3). With R built from the same expansion, the operator of kernel K_B is R R^* with ||R||_HS = 1, T = (R^* M)^* (R^* M) with Tr T = int e^{-V_B} <= 1, and T_B = (R^* M P)^* (R^* M P) with Tr T_B <= Tr T. This is (b).
5. Jentzsch (row 667, 4.1-4.3, Lemma A3 with kappa_1 = kappa_B, kappa_2 = 1). A_B is real, symmetric, continuous, kappa_B <= A_B <= 1, T_B >= 0, on the compact metric probability space X_B. A3 gives (d): positivity improving, lambda_0 simple with kappa_B <= lambda_0 <= 1, the bounds on Omega; gauge invariance of Omega as in 4.2.
6. Gap (row 667, 5.2). A3(d) gives <phi, T_B phi> <= lambda_0 (1 - delta) ||phi||^2 for phi orthogonal to Omega, with delta >= kappa_B lambda_0 >= kappa_B^2. By the min-max formula of A2(iii) every eigenvalue other than the first is <= lambda_0 (1 - kappa_B^2). Then s_k = sum_{i>=1} r_i^k <= (1 - kappa_B^2)^{k-1} sum_{i>=1} r_i <= (1 - kappa_B^2)^{k-1} Tr T_B/lambda_0, and Tr T_B^k = sum_i lambda_i^k (A2(iv) applied to T_B^k). This is (e).
7. (f) is row 667, 5.3-5.7, with the plaquette p_* taken in P_B: the proof uses one spatial plaquette with four distinct links and nothing else about the lattice. QED.

What (TM_B) gives Theorem ZB: Z(k, B) = Tr T_B^k for k >= 2 (ZB asks k >= 3), lambda_0 simple, r_i <= 1 - kappa_B^2 < 1 for i >= 1 (step 3), s_k finite. What it does not give: any bound on m_B uniform in B or in beta; the explicit bound (e) decays like exp(-24 beta |B|).

## 10. Table of verdicts

| Statement | Where | Verdict | Defect (ranked by what it breaks) |
|---|---|---|---|
| Theorem ZB | gap-zero-transport 6; plan 2.5 | HOLDS AFTER CORRECTION | Z1: (TUBE) holds for no bounded domain, so the theorem is vacuous as written (3.1, with proof). Repaired by (TUBE') and Lemma S (3.2); added (X) and (C) (3.3); limit k -> infinity proved (3.5). Conclusion unchanged. |
| Theorem Z | gap-zero-transport 5; plan 1.9 | HOLDS AFTER CORRECTION | Same Z1, (X), (C). Constants: item 1 becomes 72 (r_0 + x)(1 + |y|/d)^{4.4/theta}; item 4's 5 log n becomes (4 + 4.4/theta) log n, c depends on H; max(M_j, 1) in item 3. |
| Corollary 5' | gap-zero-transport 6; plan 2.5 | HOLDS AFTER CORRECTION | Inherits Z1; "for real beta >= beta_1" must be "for real beta in D (or in a family D_X)". New constraint on N5: the domain must satisfy (TUBE'). |
| Theorem LP | gap-zero-transport 4; plan 1.7 | HOLDS AFTER CORRECTION | Proof only: the boundary step fails at irregular points of Gamma_2; replaced by the Perron upper-class argument (Section 1). Statement unchanged. |
| Lemma HM | gap-zero-transport 4; plan 1.7 | HOLDS | none |
| Lemma 1 | gap-zero-transport 2; plan 1.5 | HOLDS | none (needs (TM) for non-cubic boxes, same construction; Section 9 does it for any finite spatial set) |
| Lemma 1' | gap-zero-transport 3; plan 1.5 | HOLDS | none |
| Lemma 2 | gap-zero-transport 2; plan 1.5 | HOLDS | none |
| Lemma 3 | gap-zero-transport 3 | HOLDS | none |
| Proposition 3 | plan 1.5 | HOLDS | one line mixes per-site and per-volume units; written out in Section 7. Input (ST5) not compared with the account's lines; the "Meaning" paragraph is not a proof. |
| Hessian bound | plan 1.4 | HOLDS | none (Bakry-Emery cited, not rebuilt) |
| (TM_B) | new, Section 9 | PROVED here as a port of row 667 | row 667 itself awaits another model's check |

What this moves (brief: nodes N1, N3, N4 and the side results): N3 (LP, HM) checked, LP with a proof repair. N4 (Theorem ZB) checked and repaired; it now holds as an implication from (TM_B), (SC_B), (ZF_B) on domains with (TUBE'). N1 (TM_B) written out, standing on row 667. Side results (Lemmas 1, 1', 2, 3, Proposition 3, Hessian bound, Theorem Z) checked.

What stays open: (SC_B) (queue item `gap-sc-box`), (ZF_B) on any domain beyond the strong-coupling disc (N6, N7), the harmonic-measure bound (N5), which must now be proved for a domain that satisfies (TUBE') or for a comparison domain inside it, and the check of row 667 by a model other than Opus 5.5. The follow-up `gap-comb` named in the brief (harmonic measure of a slit strip) is not touched; note that a strip with slits {Re beta = x_j, |Im beta| >= h} does not satisfy (TUBE') near the slit tips if the tube is taken wider than h, so that item should state its domain with (TUBE') in mind or prove its own replacement of Lemma S.
