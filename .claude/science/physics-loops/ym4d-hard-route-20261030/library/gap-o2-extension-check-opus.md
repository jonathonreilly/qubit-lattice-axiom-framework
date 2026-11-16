lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-17T00:20Z

# Check of row 1046 (`library/gap-o2-extension.md`), queue row 1047 `gap-o2-extension-check-opus`

Started 2026-11-16T12:20Z (date -u) on Mac mini worker 3. Checker: Claude Opus 5.5, max effort. Author of row 1046: Claude Fable 5.2 medium, so this is a same-provider check, not an independent one. Pinned commit 929e77235, branch claude/ym4d-hard-route. Research-stage working state; no status is granted by this file.

## Plan (at most eight steps; each response does one step and appends its result here)

1. Read the FINISH rules (Working efficiently, Rules, Build on published work), row 1046, `library/gap-o2-extension.md` in full, and the sources it relies on (Lemma FLOW, check 1041 section 4, the (O2)/(W)/(N1) definitions). Record the claim list.
2. Hand tests: Psi = 0 for the gauge extension on the cube; one value of the GR variance; Lemma AVG on a two-point pin law.
3. Line check: Lemma TAN, Theorem CUBE-EXT, the exact GR variance.
4. Line check: Lemma POLY, Theorem EXT (for every pin and boundary field?), Proposition EQ.
5. Line check: Theorem O2-GR with Lemma HIER+, and the flagged point (variance remainder of check 1041 section 4, tree gauge vs. coordinates H = e^eta of a gauge near 1).
6. Line check: Lemma AVG, Lemma MEAN.
7. Line check: Lemma GR+, Theorem O2-GR+, Corollary CURL-Q; the U(1) control.
8. Meaning (closure of 'literal (O2) needs an extension', the upper-face gap on P_3, whether (W) moves, first failing step (N1)); verdicts; RESULT line.

## Step log

(Steps are appended below as they finish.)

### Step 1 (in progress, 2026-11-16T12:3xZ): reading

- Read in full: `library/gap-o2-extension.md` L1-511 (the note under check); FINISH rows 1046-1048; FINISH sections How we work, Joining, Working efficiently, Rules.
- Read: `library/gap-short-step-max.md` 4.1-4.2 (Lemma FLOW, Lemma PROJ). FLOW re-derived here: with g_s = A(tau_s) - A + log J_s, g' = Psi_V(tau_s), F_c(omega_eps) - F_c(omega) = - log E_omega[e^(g_eps)], so F_c' = - E[Psi_V] and H_c = - E[g''] - Var(g') = - E[V Psi_V] - Var(Psi_V). So Q_V := - E[V Psi_V] = H_c + Var(Psi_V) exactly. Holds for any smooth interior field b_l(U) (it may be frozen at the base pin). No defect.
- Early note for Step 4 (kept here in case the session stops): the algebra of EXT re-derived. div(e^(-A) X) = e^(-A) sum R X - e^(-A) X . grad A, so W A + div W = e^(-A) sum R_(l,a) X_l^a; with X = grad v this is e^(-A) Delta v. With Delta v_n = g_n - gbar_n, g_n = - f E_n: Psi_(V_n) = c + e^(-A)[f (e^A - E_n) - gbar_n], and gbar_n = int f (e^A - E_n) dU because int f e^A dU = Z_c E_omega[f] = 0. The bound 4 e^(a_0) r_n sup abs(Psi_0) and Var <= 16 e^(2 a_0) r_n^2 (sup abs(Psi_0))^2 follow. One misstatement to report: POLY (a) says every component of every N_l is in PP_3; for a free link l, N_l = Im(U_l S_l) has degree 4 in the free coordinates. Only pinned-link forces are used in Psi_0, and they have degree at most 3. The degree is only used for finiteness, so nothing breaks.

### Step 1 result (done 2026-11-16, about 12:50Z): sources read, claim list

Read (besides the note in full): `gap-boundary-q.md` (row 1036) Step 2 conventions, 4.1 Theorem GR, 4.2 CUBE-Z, 4.3 Lemma CUBE; `gap-coulomb-frame.md` (row 1042) Step 1, 2.1 CG, 2.2 COUL, Step 3 (3.1-3.5), Step 5 (5.1 LEAD-C, 5.3 HIER, 5.4 EXIST), Step 7 (7.1 SQ, 7.2 CURL-P, 7.3); check 1044 (`gap-coulomb-frame-check-opus.md`) L255-300 (the continuous covariant frame K1 and the graph proof); check 1041 (`gap-collapse-frame-check-astra.md`) section 4 (K7); row 1034 (`gap-sym-reg.md`) 7.1-7.4 (Proposition CURL, Statement O2); row 1011 (`gap-pinned-cell-gauge-max.md`) Section 2 (M1)-(M8), 7.1, 7.4 (N1)-(N3).

Repo search (rule "Repo first", bounded): `grep -rln "Lemma POLY\|Theorem EXT\|Lemma GR+\|Lemma TAN" library/ parts/` and the FINISH rows; hits only in the note itself and its FINISH rows (see Step 2 below for the command output). No earlier check of row 1046 exists; row 1048 (cross-provider) is queued in parallel. This row does not attack any open lemma (no new attack, per the row), so the duplicate rule 0a does not bind.

Sussman-Alpoge account: none of the statements checked here is a port of theirs (row 1046 does not cite a CA label; the route (ii) chain is our own). Nothing of theirs is used below, so nothing is credited for this check.

Claims to check, in the note's order (each with its stated mark):
- 2.1 TAN, 2.2 CUBE-EXT, 2.3 exact GR variance on the cube, 2.4 cube verdict (PROVED).
- Step 3 U(1) control (PROVED).
- 4.1 POLY, 4.2 EXT, 4.3 A-FLOW, 4.4 HIER+, 4.5 O2-GR (PROVED given FLOW, EXIST with K1, LEAD-C, K7).
- 5.1 consumer (S) and (N1)-(N3) (from the record), 5.2 EQ, 5.3 AVG, 5.4 MEAN (PROVED), 5.5 no item of (W) moves.
- 6.1 GR+, 6.2 LEAD-C on all heads and (CONN+), 6.3 O2-GR+, 6.4 CURL-Q (PROVED given the same inputs).
Inputs taken as on record (checked elsewhere, not re-checked here): FLOW (re-derived above anyway), GR (a)-(e), CUBE-Z, CUBE-COUL (HOLDS in checks 1044, 1045), CG, LEAD-C, HIER, EXIST with K1, CURL-P (a), SQ, the graph proof of (CONN) in checks 1044/1045, K7.

### Step 2 result (done 2026-11-16, about 13:05Z): the three hand tests of the row

Notation of the note 2.1-2.3 (cube, lower face pinned, Coulomb gauge H_a = H_1 = q, H_b = H_2 = q^(-1), q = e^((phi/4) u), a = cos(gamma) u + sin(gamma) e, s := sin(gamma), psi := phi/2, c = cos(psi), plane (e, f) as C with e -> 1, f -> i). Ad(e^(x u)) is the right-handed rotation about u by 2x (checked on u = i, v = j: e^(x i) j e^(-x i) = cos(2x) j + sin(2x) k), so Ad(q^(+-1)) multiplies the plane coordinate by e^(+- i psi). All by hand; no run.

**Test 1: Psi = 0 for the gauge extension on the cube. PASSES.**
- The four link equations psi_x - Ad(H_l) psi_y = (lambda_x - lambda_y) a: along u they hold with psi^u_x = cos(gamma) lambda_x. In the plane: (a) w_o - e^(i psi) w_A = s (lambda_o - lambda_A), (1) w_A - e^(i psi) w_C = s theta_1, (b) w_o - e^(- i psi) w_B = s (lambda_o - lambda_B), (2) w_B - e^(- i psi) w_C = s theta_2. The note's w_A, w_B, w_o satisfy (1), (2), (a) by definition. Inserting them in (b): (e^(i phi) - e^(- i phi)) w_C = s [lambda_A - lambda_B - e^(i psi) theta_1 + e^(- i psi) theta_2] = s [theta_1 (1 - e^(i psi)) - theta_2 (1 - e^(- i psi))] (lambda_A - lambda_B = theta_1 - theta_2). This is the note's w_C; it needs sin(phi) != 0, i.e. h != +-1, as stated.
- Psi = 0: the extension (psi_x on the vertical link out of x, 0 on the top links) together with B on the pinned links is, at the base pin, the vector field G of the gauge rotation g_x = exp(eps psi_x) at the four lower sites (g = 1 at the top sites). The Gauss identity at each site x (from A(U^g, omega^g) = A(U, omega) for all g, pinned links included: sum over l out of x of N_l = sum over l into x of Ad(U_l)^(-1) N_l) gives G A = 0 for every U. The divergence is 0 (fixed left rotations). So Psi_V(., omega) = 0 at the base pin, as TAN says. (Psi_V is not 0 at the moved pins omega_s; this is why V Psi_V and Q_V = H_c are not 0. TAN only claims Psi = 0 at the base pin, which is what FLOW reads.)
- Independent value (a different derivation from the note's, which cites CUBE-COUL and row 1038 CUBE-H): TAN's force formula H_c = 2 sum_l (psi_x x Ad(H_l) psi_y) . E[N_l], with E[N_l] = (b_0 + kappa) [p_0 : l] sin(phi) u on all four links (derived here from F_c = - b_0 t - log G(t): for l = 1, dt/d eps = - v . s(k_1), k_1 = H_1 H_2^(-1) H_b^(-1) H_a = q^4; for l = 2, dt/d eps = + v . s(k_2), k_2 = H_b^(-1) H_a H_1 H_2^(-1) = q^4), and (P x P') . u = Im(conj(w) w'). Using the four plane equations, lambda_o drops out and
  sum_l [p_0 : l] (psi_x x Ad(H_l) psi_y) . u = s [theta_1 Im((1 - e^(i psi)) w_A) + theta_2 Im((e^(- i psi) - 1) w_B)]
  = s^2 { - sin(psi)(theta_1^2 + theta_2^2) + ((1 - c)/sin(phi)) [cos(phi)(theta_1^2 + theta_2^2) + 2 c theta_1 theta_2] },
  (with (1 - e^(i psi))^2 = - 4 sin^2(psi/2) e^(i psi), so Re(e^(i psi)(1 - e^(i psi))^2) = - 2 (1 - c) cos(phi)). Multiply by 2 (b_0 + kappa) sin(phi) and use sin(phi) sin(psi) = 2 c (1 - c)(1 + c), cos(phi) = 2 c^2 - 1:
  H_c = - 2 (b_0 + kappa) sin^2(gamma)(1 - c) [(1 + 2 c)(theta_1^2 + theta_2^2) - 2 c theta_1 theta_2].
  This is CUBE-COUL exactly. So 2.2's value is confirmed by a second derivation (TAN's force formula), not only by citation.

**Test 2: one value of the GR variance. PASSES (leading order in beta, and the phi -> 0 limit).**
- Exact representation used: by the substitution of CUBE-Z (T'_l = V_x T_l V_y^(-1)), the side staple of a pinned link l = (x -> y) satisfies H_l R_l = H_l T'_l^(-1) =: Y_l, so N_l(side) = beta Im(Y_l) exactly, and the law of (Y_a, Y_1, Y_2, Y_b) has density proportional to prod_k e^(beta t(Y_k)) times e^(beta t(Y_a^(-1) H_a Y_1^(-1) H_1 H_2^(-1) Y_2 H_b^(-1) Y_b)) against Haar measure. The pinned-plaquette part of N_l is a function of the pin and drops out of every variance.
- Case: phi = pi/2 (c = 1/sqrt 2), gamma = pi/2, lambda = indicator of C (theta_1 = theta_2 = - 1, T = 2 + 2c, Lam = 2), beta -> 0. Formula 2.3: Var = 4 sin^2(gamma)(1 - c){beta xbar + kappa (1 + c)(1 - 2 c)}. At small beta: u_1 = 1 + beta^2/8 + ..., u_1' = beta/4 + ..., u_2 = beta/4 + ..., so xbar(0) = beta/4 + O(beta^2) and kappa = O(beta^5). Formula: Var = (1 - 1/sqrt 2) beta^2 + O(beta^3).
  Direct: Psi = d_1 . N_1 + d_2 . N_2 with d_l = a - Ad(H_l) a, abs(d_l)^2 = 2 (1 - c) sin^2(gamma) = 2 - sqrt 2. At beta -> 0 the Y_k are independent Haar elements, so Cov(N_l(side)) = beta^2 E[Im Y Im Y^T] = (beta^2/4) I (E abs(Im Y)^2 = 3/4 under Haar) and the cross-covariance is O(beta^3) or smaller. Var = (beta^2/4)(2 - sqrt 2) . 2 + O(beta^3) = (1 - 1/sqrt 2) beta^2 + O(beta^3). Agrees.
- phi -> 0: the note's comparison with row 1042 3.4 re-done: 2 sin^2(gamma)(1 - c) -> phi^2 sin^2(gamma)/4, T -> 4 Vv, Lam = Vv + 4 lbar^2, so {kappa T + [beta xbar - 4 kappa] Lam} -> beta xbar Vv + 4 (beta xbar - 4 kappa) lbar^2. Agrees with 3.4.
- What this test does not reach: the kappa terms at order-one beta. Step 3 checks them through the exact derivation instead (they come from first moments only, E[N_l] and xbar, so no covariance needs to be computed).

**Test 3: Lemma AVG on a two-point pin law. PASSES; AVG is sharp for the information it uses.**
Law: pin omega_1 with probability p (in GG: H_c(omega_1; theta n) <= C S(theta), S := sum_p (d theta)_p^2) and omega_2 with probability 1 - p (only abs(H_c) <= A_0 abs(theta)^2). Then E[H_c] = p H_c(omega_1) + (1 - p) H_c(omega_2) <= p C S + (1 - p) A_0 abs(theta)^2, with equality when H_c(omega_1) = C S and H_c(omega_2) = A_0 abs(theta)^2. So no better bound follows from these two facts alone. On (ker d)-perp, abs(theta)^2 <= S/mu_1, so the bound is the curl bound with constant p C + (1 - p) A_0/mu_1; at the eigenvector of mu_1 this is attained, so "below c S only if (1 - p) A_0 <= c mu_1" (the note's 5.3) is right for this bound. On gradients (S = 0) the bound is a pure mass term (1 - p) A_0 abs(theta)^2 > 0. Example with the cube: omega_1 at the H* of COUL with b_0 + kappa > 0 (H_c < 0 on gradients) and omega_2 a point of the same torus orbit with H_c > 0 (exists by MEAN unless H_c vanishes on the orbit); the average has no sign without numbers for p.

### Step 3 result (done 2026-11-16, about 13:15Z): line check of TAN (2.1), CUBE-EXT (2.2), the exact GR variance (2.3), the cube verdict (2.4)

**2.1 Lemma TAN: HOLDS.** Line by line:
- V of class (E-FROZEN) as written is, at the base pin, the generator G of g_x = exp(eps psi_x) on pinned sites (g = 1 on free sites): on a pinned link G_l = psi_x - Ad(omega_l) psi_y = B_l; on a free link out of z, psi_z; into z, - Ad(U_l) psi_z; both ends pinned, psi_x - Ad(U_l) psi_y. So V A = G A = 0 at every U (gauge invariance of A, pinned links included). Correct.
- div V = 0: left rotation by a fixed vector, and U -> e^(eps Ad(U) c) U = U e^(eps c) is a right translation, both Haar-preserving. The direct line sum_a R_(l,a)(Ad(U_l) c)^a = sum_a 2 (e_a x Ad(U_l) c)^a = 0 is right (R_(l,a) Ad(U_l) c = [e_a, Ad(U_l) c] = 2 e_a x Ad(U_l) c, and (e_a x w)^a = 0).
- Q_V = H_c: FLOW with Var(Psi_V) = 0. E[Psi_V] = 0 gives F_c' = 0 along B. Correct.
- Value: the BCH line re-done: order eps^2 of e^(- eps X) e^(eps (X + Y)) e^(- eps Y) is (Y X - X Y)/2 = - [X, Y]/2 = - X x Y; with X = psi_x, Y = - Ad(omega_l) psi_y this is c_l = psi_x x Ad(omega_l) psi_y. Then F_c(e^(eps B) omega) = F_c(pin e^(eps^2 c + O(eps^3)) omega) and the second derivative is 2 sum c_l . E[N_l] (with (d/d eps) F_c(e^(eps v) omega_l) = v . E[N_l], row 1036 Step 2). Correct. Confirmed independently on the cube in Step 2, Test 1.
- U(1) line: psi_x x psi_y = 0. Correct.

**2.2 Theorem CUBE-EXT: HOLDS.** The psi solves the four link equations (Step 2, Test 1; requires h != +-1). The transfer to the original gauge, psi^orig = Ad(g)^(-1) psi, is right: Ad(g_x)^(-1)[psi_x - Ad(H_l) psi_y] = psi^orig_x - Ad(omega_l) psi^orig_y. The value is CUBE-COUL, and Step 2 re-derived it from TAN's force formula. Sign statement: T has eigenvalues 1 + c and 1 + 3 c (matrix [[1 + 2c, - c], [- c, 1 + 2c]]), positive since c = cos(phi/2) > 0 for phi < pi; 1 - c > 0 for phi > 0. So Q < 0 unless theta_1 = theta_2 = 0, given b_0 + kappa > 0 and sin(gamma) != 0. Remarks: w_C -> - s (theta_1 + theta_2)/4 at phi -> 0 (re-derived). "Tangent to the orbit iff t'(0) = 0": for h != +-1 the level set {t(h) = t_0} is one gauge orbit (tree gauge leaves one link with holonomy in a connected conjugacy class), of dimension 11 = 12 - 1 (stabiliser U(1)), and dt != 0 there; correct.

**2.3 Exact GR variance on the cube: HOLDS.** Every line re-derived:
- Q_GR = - E[(d/d eps)^2 A(U, omega_eps)] (GR (a), (d): Psi = V A, div V = 0). Top plaquette: no pinned link, does not move.
- Pinned plaquette: - b_0 t''(0), and t''(0) = 2 sin^2(gamma)(1 - c) T(theta) from CUBE-COUL with t'(0) = 0 (F_c = phi(t), H_c = phi'(t) t'' when t' = 0, phi' = - (b_0 + kappa)).
- Side plaquette over l: beta Re(W_l omega_l R_l); W''(0) has real part - tau^2 abs(D n)^2 and imaginary part - 2 tau^2 n x m (GR (b)); Re(v q) = - v . Im q gives the note's line. E[Re(H_l R_l)] = xbar(t) (d/d beta_k log Z with five strengths in CUBE-Z; same value for the four sides). E[N_l(side)] = E[N_l] - b_0 [p_0 : l] s(h_l) = kappa [p_0 : l] sin(phi) u (Step 2, Test 1 derives E[N_l] with this sign convention: h_l is the plaquette holonomy in its own orientation based at the tail of l).
- abs(D_l n)^2 = 2 sin^2(gamma)(1 - c); [p_0 : l](a x Ad(H_l) a) . u = sin^2(gamma) sin(phi/2) on all four links (u-component of a x Ad(q^(+-1)) a is +- sin^2(gamma) sin(phi/2), times [p_0 : l] = +-1). sin(phi) sin(phi/2) = 2 c (1 - c)(1 + c).
- Sum: side part 2 sin^2(gamma)(1 - c)[beta xbar - 2 kappa c (1 + c)] Lam, Lam = lambda_A^2 + lambda_B^2 + 2 lambda_C^2 (heads A, C, B, C). Q_GR and Var = Q_GR - H_c are as printed.
- Small-beta and phi -> 0 values agree (Step 2, Test 2).

**2.4 Verdict of the cube test: HOLDS AFTER CORRECTION of one equation.** The note writes "With b_0 = 0 it has Q_GR = Var(Psi_GR) >= 0 (exact, 2.3), while H_c < 0". The equation Q_GR = Var(Psi_GR) is false at b_0 = 0: Q_GR = H_c + Var(Psi_GR) and H_c = - 2 kappa sin^2(gamma)(1 - c) T(theta) < 0 there (when kappa > 0, sin(gamma) != 0, theta != 0), so Q_GR < Var. The conclusion Q_GR >= 0 is true, by another line: at b_0 = 0, Q_GR = 2 sin^2(gamma)(1 - c)[beta xbar - 2 kappa c (1 + c)] Lam, and the bracket is >= 0 because it is Var(Psi_GR)/(8 sin^2(gamma)(1 - c) l^2) for lambda_A = lambda_B = lambda_C = l (theta = 0, T = 0, Lam = 4 l^2), a variance.
Corrected text: "With b_0 = 0 it has Q_GR = 2 sin^2(gamma)(1 - c)[beta xbar - 2 kappa c (1 + c)] Lam >= 0 (the bracket is a variance divided by a positive number: take theta = 0 in 2.3), while H_c < 0." Nothing downstream reads the false equation.
The other bullets of 2.4 hold: the extension of 2.2 has Var = 0 and Q = H_c for every b_0 >= 0, pin with h != +-1 and lambda; the cube is special because there "stationary along B" and "tangent to the orbit" coincide (one gauge-invariant coordinate t(h)).
