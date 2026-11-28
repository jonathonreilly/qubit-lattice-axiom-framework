# Check of library/gap-band-flux-tail-astra62.md (FINISH row 1589)

Checker: Claude (Opus 5.5). Started 2026-11-26.

## Plan
1. Read GOAL.md, FINISH.md Rules + Working efficiently.
2. Read the target note in full; read check 1585 section (v); row 1568 Thm E, check 1572, rows 1565/1571 as needed.
3. Check positive claims: reduction to D-bar_d; (2); (5)-(6) with constants; (7); model tests.
4. Check the stopping point and attack failure points.
5. What the bounds give toward (N-flux) and Pi.
6. RESULT line.

## Progress
- Step 1 done: read GOAL.md, FINISH.md 'Working efficiently' and 'Rules', the target note in full (155 lines), check 1585 section (v) in full, FINISH rows 1585-1589.
- Step 2 (in progress): hand check of the reduction, (1), rho <= D-bar, (2), the period example, (3), the surface argument, (4)-(6), (7)-(8) and the detour example. Sources still to read: row 823 (R4)-(R5), row 1145 (1)-(2), row 1568 Thm E / check 1572, rows 1565/1571, (N-flux), row 1566 sandwich.

## Step 2 result: reduction and implications (hand check)

- Pin law, end-pair law Q_{d,t}: HOLDS. A_t, B_t are the kernels of P_ev T^t, P_od T^t; P_ev commutes with T, so the arcs other than j compose to A_{d-l_j}(y,x), and the total mass is Tr(P_ev T^d) = Z_e(d). Labels are conditionally independent given all pins because the label density factorizes, prod_j (1/2) K_{l_j}(C^{h_j} x_j, x_{j+1}); so E(H_j | all pins) = b_j depends on its two pins only. The marginal of arc j depends only on (d, l_j). D-bar_d is well defined.
- (1): HOLDS. On {N < c log n} with m >= 2c log n, the number of arcs with |b_j| > 1/2 exceeds m/2; that number is at most 4 sum b_j^2; Markov gives Pr <= 8 E sum b_j^2 / m = 8 D-bar_d.
- Z_o(d)/Z_e(d) = E prod b_j <= E prod |b_j| <= D-bar_d (AM-GM on |b_j|^m, then |b|^m <= b^2 for m >= 2): HOLDS.
- Positive-transfer separation (r_n = exp(-64/sqrt n)): HOLDS. |b_j| = r_n^{l_j} -> exp(-64 sqrt(d/n)) = e^{-2.83} or e^{-4} (both < 1/2); D-bar -> exp(-128 sqrt(d/n)) > 0. "Neutral purity one" is right in the sense Z_+(2u)/Z_+(u)^2 (the even sector is one-dimensional, Z_+ = 1); the untwisted Pi of this model is not one, which the note does not claim.
- Spectator remark: HOLDS (b_j unchanged, purity multiplied).

## Step 3 result: first attack, (2) and its example

- Symmetric-period identity E_{Q_{2t,t}} b_t^2 = Z_o(2t)/Z_e(2t): HOLDS (A_t, B_t symmetric: K_t symmetric and K_t(Cx,Cy)=K_t(x,y)).
- W and E W^2 = Z_e(2t) Z_e(2d-2t)/Z_e(d)^2: HOLDS (strict positivity of the Wilson kernel gives absolute continuity).
- (2): HOLDS. D = E_{Q_2t}[W b^2] <= (E W^2)^{1/2} (E b^4)^{1/2} <= (E W^2)^{1/2} (Z_o(2t)/Z_e(2t))^{1/2}.
- Precision added by the checker (not in the note): Cauchy-Schwarz gives Z_e(d) = Tr(P_ev T^t P_ev T^{d-t}) <= sqrt(Z_e(2t) Z_e(2d-2t)), so the right side of (2) is at least sqrt(Z_o(2t)/Z_e(2t)). The route therefore needs, at least, the short-period odd fraction at period 2 l_j ~ 2 sqrt(d) to be polynomially small; the example shows this is not sufficient. Both directions together make the failure point of attack 1 exact.
- Period example (M = ceil(n^p) auxiliary pairs, s P_const blocks, eta P_all): HOLDS. Odd sector untouched by the even perturbation; Z_e(2t) >= M s^{2t} by monotonicity (perturbation PSD); Z_e(d) <= 1 + M s^d + (M+1) d eta (1+eta)^{d-1} by (lambda+e)^d - lambda^d <= d e (lambda+e)^{d-1} on the M+1 even eigenvalues; M s^d = n^p e^{-d/sqrt n} -> 0; Z_o(d) = r^d -> 1. Pr(N >= 1) <= 2(1 - Z_o/Z_e) from prod|b_j| <= 1 - (1/2) 1{N>=1}: HOLDS.

GUIDE (not a proof step; pure-python floats, scratch script outside the lane): on 150 random C-symmetric positive kernels (2 to 8 states, d in 6..16), D_{d,t}/rhs(2) <= 0.11 and sqrt(Z_o(2t)/Z_e(2t))/rhs(2) <= 1 + 2e-16, as the hand argument requires. I_h(s)/I_1(s) <= exp(-(h-1)/(1+s)) on s in (0,30], h <= 19 (max ratio 0.98).

## Step 4 result: second attack, (3)-(6)

- Marking identity e^{beta w} = e^{-beta|w|}[1 + (e^{2 beta|w|}-1) 1{w>0}] and mark probability 1 - e^{-2 beta (w)_+}: HOLDS. Given adjoints and marks, the link signs and seam bits are uniform on an affine F_2 solution set: HOLDS (two Haar lifts per adjoint link, unmarked factors sign-blind). Spatial pin plaquettes are C-invariant (both direction-1 links of a 12- or 13-plaquette at x_1 = 0 are flipped): HOLDS.
- Precision (implicit in the note, holds): because every pin is disclosed in full, the F_2 constraints decouple across arcs, so the difference of two solutions with opposite H_j is supported on arc j's cylinder. The note uses this without saying it.
- (3) b_j = p_+ - p_-, 1 - |b_j| = q_j + 2 min(p_+, p_-): HOLDS. D <= E(1-q)^2 <= Pr(F^c): HOLDS.
- Necessary surface: HOLDS. delta(sigma) is closed on the torus (zero on the end tangential faces), sums to 1 mod 2 on every 01-torus by Stokes on the strip, its edge-connected components are closed, one has odd pairing with every parallel 01-torus, hence >= A = n^2 faces dual to 01 plaquettes, all unmarked.
- (4) Pr_ev(all k unmarked) <= 2 Phi^{-k} for k faces sharing a direction: HOLDS. Re-derived: pointwise e^{beta w}e^{-2 beta w_+} = e^{-beta|w|} <= 1; label sum becomes (Z^0_del + Z^C_del)/2 by centre changes of variables; in transfer direction mu, Haar projection <= normalized convolution (eigenvalues I_h/I_1 >= 0 vs {1,0,...}), so each modified layer is 0 <= T'_tau <= Phi^{-k_tau} T (tensor products of commuting PSD factors, conjugation by positive magnetic half weights and by the gauge projector preserve order); Schatten-Hoelder plus Weyl monotonicity give |Tr(U prod T'_tau)| <= Phi^{-k} Tr T^D; the static-twist case gives Z^C <= Z^0. Denominator Z_e(d) = (Z^0 + Z^C)/2 >= Z^0/2 since Z^C > 0. Double counting (2k direction incidences over 4 directions) gives 2 Phi^{-k/2} for an arbitrary set: HOLDS.
- (5) constants: HOLDS. Row 823 (R4), checked in 826, counts surfaces with k(S) = |S| - A <= K by N_perp 16^{4K} sum_{b<=2K} C(2(A+K), b); (R5) with t = 1/256 gives 256^{2K}(1+1/256)^{2(A+K)}; here N_perp = nd (root over a fixed 23 base face, (x_0,x_1) placements), periods d, n, n, n >= 3. Log after nd: 32 K log 2 + (A+K)/128 <= (3/16 + 129/16384) A < A/4. Phi >= 1 + beta^2/8 >= 3/2 (E w^2 = 1/4, odd moments zero), log(3/2) = 0.405 > 1/3. Union bound nd e^{A/4} 2 e^{-A/3} = 2nd e^{-A/12}.
- (6) constants: HOLDS with c = 1/8, C = 24. 20 edge neighbours per face, 20^{2(k-1)} rooted connected k-sets, 6 n^3 d roots, 2 Phi^{-k/2} per set; Haar(w >= 1/2) = 1/3 - sqrt3/(4 pi) = 0.196 > 0, so Phi >= 0.196 e^{beta/2} and 400/sqrt(Phi) <= e^{-beta/8} <= 1/2 once beta >= ~55. On the band Phi <= e^3 and 400/sqrt(Phi) > 1: no bound, as the note says.
- Consequence Pr(max_j q_j > h) <= C n^3 d e^{-c beta_K n^2}/h and min(p_+, p_-) >= 1/4 - h/2 on ambiguous arcs: HOLDS.
- Failure point of attack 2: exact on the calibrated sequence (freedom is rare, so any ambiguity is 2 min(p_+, p_-), the balance of opposite disclosed fixed signs). On the band it needs a precision: (5) excludes only sheets with excess <= A/128, so on [2,3] the freedom term q_j is not shown small either; both terms of (3) are uncontrolled there. The note says this ("Larger winding components are unrestricted by (5)"); its closing sentence "(5) and (6) exclude the specified erasure mechanisms" is right only with "near-minimal" understood for (5).

## Step 5 result: third attack, (7)-(8) and the detour comparison

- Predictor test: HOLDS. Pr(U_j != H_j) >= E(1-|b_j|)/2 >= (1/4) Pr(|b_j| <= 1/2), so E N <= 4 sum_j Pr(U_j != H_j), and E N = o(log n) gives Pr(N < c log n) -> 1 by Markov.
- (7): HOLDS on [2,3] and at beta_K = O(log n). Checked: (a) equal priors on the preliminary data: the measure-preserving involution (x -> Cx, toggle h_{j-1} and h_j) preserves K(C^{h_{j-1}} x_{j-1}, x) and K(C^{h_j} x, x_{j+1}) by K(Ca,Cb) = K(a,b) and C^2 = 1, fixes every preliminary datum (C changes only the withheld cut links), and flips H_j; the arcs j-1, j are distinct for m >= 2. (b) No plaquette holds two selected links: parallel direction-1 links in one spatial 1-nu plaquette have opposite parity of x_2 + x_3 (n even), collinear links share none, temporal plaquettes meet only one pin link. (c) Each selected link has conditional density exp(beta rho w(UV)), rho <= 6 (4 spatial + 2 temporal plaquettes; seam signs do not change the bound), so row 1145 (1), I_h(s)/I_1(s) <= exp(-(h-1)/(1+s)) (re-read in gap-solve2-astra62.md, lines 19-27), and its (2) give |p - 1| <= eta(k/(1+6 beta)) per line. (d) The n^2 lines are conditionally independent; the joint density lies in [(1-eta)^{n^2}, (1+eta)^{n^2}], within delta of one; averaging over the conditioned exterior given (preliminary data, H_j) keeps it there. (e) Bayes with equal priors gives |E(H_j | G_j)| <= delta; the note's delta/(1-delta) is weaker and also valid. (f) k/(1+6 beta) >= (A_0+6) log n gives eta <= C n^{-A_0-6}, delta = O(n^{-A_0-4}); 2k < n holds since k = O(log n) on the band and O((log n)^2) at beta_K = O(log n). Extension to omission at every pin: tower property: HOLDS.
- (8): HOLDS (G_j is pin-measurable, E(b_j | G_j) = E(H_j | G_j), law of total variance).
- Detour comparison: HOLDS. f is gauge invariant, C-odd (the circuit crosses the cut once), +-1 a.e.; flipping the cut link and the bypassed selected link preserves Haar, every revealed link (the parallel detour link has the other parity, so it is revealed and unchanged), every straight transport, and flips f. Kernel 1 + r f(x) f(y): eigenvalues 1, r, 0 (since <1,f> = 0, <f,f> = 1), strictly positive, A_l = 1 so the even pin law is product Haar, b_j = r^{l_j} f(x_j) f(x_{j+1}), |b_j| -> 1, and every projected bias in (7) is exactly zero.
- Failure point of attack 3: exact. The missing term is E Var(b_j | G_j), the bias carried by the omitted (k+1) n^2 links; the comparison shows it can be order one with all observed data fair.

## Step 6 result: model tests

- Pinned Dobrushin range (row 1568 Theorem E, check 1572): HOLDS. Theorem E bounds sup_{X,Y} sup_x sum_y |D_x D_y log K_v| <= 3 beta^2 (1-q)^{-2} v q^{v-2}, q = 9 beta/2, uniformly in the pins (read at gap-band-cut-covariance-neon.md lines 247-277; check 1572 Step 7 HOLDS). The four-corner identity (Theorem A(1), same file) integrates this over [0,pi]^2 and the n^2 cut sites: |log(K_l/K_{l,C})| <= (pi^2/2) n^2 3 beta^2 (1-q_*)^{-2} l q_*^{l-2}, pointwise in the pins. b = tanh((1/2) log(K/K_C)), so sup |b_j| -> 0 faster than any power when l ~ sqrt(n); D-bar_d -> 0 and N = m eventually. The fixed subinterval q <= q_* < 1 is needed for the constant; the note says so.
- Weak compact U(1) (rows 1565, 1571): HOLDS. Row 1565 (checked in 1571, "holds as written") proves Pr(Q odd) >= eta_beta > 0 for Villain beta >= 2000 and for Wilson beta_W >= beta_* (existential), on n^3 x w tori with R = n/w in {256, 512}, which are exactly d = n/256, n/512 here; with C the half-turn cut translation the pin-law formalism is unchanged. So rho_d >= d_beta > 0, D-bar_d >= rho_d fails the power bound, and the lower bound Pr(N < c log n) >= (rho_d - n^{-c log 2})/(1 - n^{-c log 2}) follows from rho <= P + (1-P) 2^{-c log n}: HOLDS. So both the count and the D-bar estimate are selective against weak 4D U(1); the 5D SU(2) status is not established (the note says so).
- Positive-transfer example of check 1585 (r_n = exp(-(log n)^2/n)): HOLDS. r_n^d is below every inverse power at d ~ n while |b_j| = r_n^{l_j} -> 1, so the count fails surely with the one-axis flux tiny. Together with the note's own example (Step 2), the order is strict: D-bar estimate => count => one-axis flux, with neither converse.

## Step 7: stopping point, (N-flux), Pi

- Is the uncontrolled quantity exactly the balance of opposite seam signs at fixed full pins? HOLDS. D-bar_d = average of E_Q b_j^2 with b_j = Pr(H_j = +1 | all pins) - Pr(H_j = -1 | all pins); nothing in the note bounds it at Wilson coupling on [2,3] or at beta_K. Attack 1 stops at the trace ratio in (2), which needs at least sqrt(Z_o(2t)/Z_e(2t)) small (checker's precision above); attack 2 at min(p_+, p_-) (and, on the band, also at q_j, see Step 4); attack 3 at E Var(b_j | G_j). Each failure point is exact, with the band precision for attack 2.
- Framing precision: the three attempts are on D-bar_d, a strictly stronger majorant of the requested count (Step 6). So the "three attempts on one stated estimate" stopping test is met for D-bar_d, not for the count of check 1585 (v). The count itself was attacked only through D-bar_d and through the refutation test of attack 3; the conditional-indicator route of check 1585 (v) was not tried. The note's RESULT ("OPEN for the full-pin lower tail") is correct as a statement; it should not be read as three failed attacks on the count.
- Equivalent is not progress: the D-bar estimate is not equivalent to the seed (spectator: D-bar unchanged, purity arbitrary) and is selective against weak 4D U(1) (rho_d <= D-bar_d). It is a stronger restatement of the open lemma, not progress toward it.
- Toward (N-flux) (row 1566 form: 1 - Z_+(2v)/Z^0(2v) <= C' v^{-eps}, v in {u/2, u}, beta in [2,3]): the implication HOLDS. If the count held uniformly on [2,3], f(v) <= 3 R_n/(1+R_n) with R_n = C_0 n^{-eps} + n^{-c log 2}, and n = 512u, so (N-flux, min(eps, c log 2)) follows. The proved bounds (2), (5), (6), (7) give nothing toward it: (2) is conditional on an unproved trace decay, (5)-(7) are about other observations than the full pins.
- Toward Pi: nothing. The identity P_K = Pi (1 - f(u))/(1 - f(u/2))^2 HOLDS (direct algebra), and the row 1566 sandwich HOLDS as quoted (row 1566 (f)-(g), gap-band-cut-covariance-fable.md lines 70-76; with a direct flux bound one may use f in place of 21 delta/8). Every arc-sign quantity is blind to a neutral spectator, which multiplies Pi by its own purity; so no estimate of this kind bounds Pi, and the carry from the band to the release roots is untouched.

## Verdicts

| Part | Verdict |
|---|---|
| Reduction to D-bar_d, (1), rho_d <= D-bar_d, pin law and Q_{d,t} | HOLDS |
| Positive-transfer separation (D-bar stronger than the count) | HOLDS |
| (2) and the symmetric-period identity | HOLDS (checker adds: rhs(2) >= sqrt(Z_o(2t)/Z_e(2t))) |
| Period example (short-period odd fraction insufficient) | HOLDS |
| (3), surface argument | HOLDS (arc decoupling given full pins is implicit) |
| (4) | HOLDS |
| (5) with constants 2nd e^{-A/12}, K = floor(A/128) | HOLDS |
| (6) with constants | HOLDS (c = 1/8, C = 24) |
| (7) and its extension | HOLDS (Bayes constant delta suffices) |
| (8) and the detour comparison | HOLDS |
| Model test: pinned Dobrushin range | HOLDS |
| Model test: weak compact U(1) and the lower-tail bound | HOLDS |
| Model test: positive-transfer example of check 1585 | HOLDS |
| Stopping point = balance of opposite seam signs at full pins | HOLDS |
| Failure point of attacks 1 and 3 | HOLDS (exact) |
| Failure point of attack 2 | HOLDS AFTER CORRECTION: exact on the calibrated sequence; on [2,3] the freedom term q_j is also uncontrolled, since (5) covers only excess <= A/128 |
| Stopping test framing | HOLDS AFTER CORRECTION: the three attempts are on D-bar_d, strictly stronger than the requested count; the count is open without three direct attempts |
| Toward (N-flux) | implication HOLDS; no proved bound gives it |
| Toward Pi | nothing; HOLDS as stated in the note |

Not checked: the repo-search table and the literature attributions in it; row 823 (R4) beyond reading its proof and check 826; row 1145 (2) beyond its statement; check 1585's four-corner integration beyond Theorem A(1) of row 1568; row 1565's Villain proof (relied on check 1571).

RESULT — Row 1587 checks: every proved step (the reduction to D-bar_d and (1), rho_d <= D-bar_d, (2), the period example, (3), the surface argument, (4), (5), (6), (7), (8), the detour comparison) HOLDS with its constants, nothing FAILS, and the three model tests hold. Two precisions: on [2,3] attack 2 leaves the freedom term uncontrolled as well as the sign balance, and the three attempts are on D-bar_d, a strictly stronger majorant of the requested count. The full-pin lower tail, (N-flux) and Pi remain open; the proved bounds give neither.
Checked line by line by Claude (Opus 5.5).
