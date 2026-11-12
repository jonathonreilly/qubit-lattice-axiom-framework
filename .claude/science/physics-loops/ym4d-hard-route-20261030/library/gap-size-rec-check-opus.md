# Check of library/gap-size-rec-astra.md (FINISH row 803), by Claude Opus 5.5, line by line

Clone: `/Users/jonreilly/ym4d-lead/clone` at commit `619472ccd0702b20c2b5a753d3bc56eb47cfec91`.
Lane D = `.claude/science/physics-loops/ym4d-hard-route-20261030`.
Target: `D/library/gap-size-rec-astra.md` (504 lines, Codex gpt-6-astra max, FINISH row 802). Read in full.
Context read: `gap-skeleton-max.md` 110-135 (B3) and 250-305 (Lemma 4, E.2-E.4);
`gap-means-max.md` 140-250 (4.1-4.6, Theorem R); `gap-kanazawa-astra.md` 211-500 (Section 3, (K21)) and 607-655;
`gap-ext-astra.md` 78-129 and 474-522 ((LC)); `gap-cf-astra.md` 248-264, 485-524.
All checks are by hand. No numerical run was made, not even a GUIDE run.
Not checked: the SA outline (AM6, lines 2885-2942), the two downloaded sources, and the provenance record of Section 6.

## Item 1. Section 1: identities (2)-(3) and the convexity example

**(2)-(3) against Lemma 4.** Lemma 4 of `gap-skeleton-max.md` (line 266, inside E.1 at 259-270) states
(D-sheet) f_m(2l_1) = 2f_m(l_1) + R(T_m,l_1) - R(T,l_1) and
(D-plane) r(2l_3) = r(l_3)^2 exp(R(T_even,l_3) - R(T_odd,l_3)), with
R(S,l) = log((Tr S^l)^2/Tr S^{2l}) and r = tanh(f_m/2).
The note's H_2 is R. Its T_+, T_- are T_even, T_odd. Its T_m, T_0 are T_m, T.
So (2) is (D-plane) and (3) is (D-sheet), with the same signs.
I re-derived both. Z_0 = Tr T^l and Z_n = Tr T_m^l give (D-sheet) from Tr S^{2l} = (Tr S^l)^2 e^{-R(S,l)}.
In the twist plane, Z_0 +- Z_n = 2 Tr_{even/odd} T^l, so r = Tr_odd T^l / Tr_even T^l. The same substitution gives (D-plane).
The note's citation 258-277 covers E.1, Lemma 4 and its consequences. It is correct.
The claim 0 < Z^{m+v}/Z^m <= 1 follows from (K9) in `gap-kanazawa-astra.md` 3.1. It holds.

**Convexity example.** T = diag(1,r,r), C = diag(1,1,-1), 0<r<1. C commutes with T.
Z(t) = Tr T^t = 1 + 2r^t. Z^v(t) = Tr(C T^t) = 1 + r^t - r^t = 1. Both are positive.
F(t) = -log(Z^v/Z) = log(1+2r^t). With g = 1+2r^t: g' = 2r^t log r, g'' = 2r^t (log r)^2.
(log g)'' = [g'' g - g'^2]/g^2 = 2r^t (log r)^2 [1 + 2r^t - 2r^t]/g^2 = 2(log r)^2 r^t/(1+2r^t)^2 > 0.
This matches the displayed F''. So log Z is convex, log Z^v = 0 is convex, and their difference F is strictly convex, not concave.
B3 (line 130) says "log Z_0 and log Z_n are convex ... so the flux energies are concave". The example refutes that inference as an implication.
The same example also works in the sheet direction: replace Z^v by Tr S^t with S = [1] on one state.
The note correctly scopes it as a finite operator example, not a Wilson counterexample.

**Verdict: HOLDS.**

## Item 2. Section 2: the operator example (4), the superlinear refutation, Theorem R, crossed backgrounds

**The operator.** On N+2 states, u = (N+2)^{-1/2}(1,...,1), T = rI + (1-r)|u><u|, r = 2^{-1/t}.
Entries: T_xy = r delta_xy + (1-r)/(N+2) > 0. Eigenvalues: 1 on u, r on u-perp (N+1 copies). So T is positive definite and u is the simple top eigenvector.
J swaps two states. Ju = u, so JT = TJ and u is even.
The even subspace has dimension N+1 and contains u. So T_+ has eigenvalues 1 and N copies of r.
The odd subspace is spanned by e_1 - e_2, in u-perp. So T_- has the single eigenvalue r. Both claims hold.
Twisted trace: Tr(J T^s) = Tr_+ T^s - Tr_- T^s = 1 + N r^s - r^s = 1 + (N-1)2^{-s/t} > 0. Holds.

**q(t), q(2t).** q = Tr_- T^t / Tr_+ T^t. This equals tanh(F/2), because Z_n/Z_0 = (1-q)/(1+q) gives F = 2 artanh q.
r^t = 1/2: q(t) = (1/2)/(1 + N/2) = 1/(N+2).
r^{2t} = 1/4: q(2t) = (1/4)/(1 + N/4) = 1/(N+4).
q(2t)/q(t)^2 = (N+2)^2/(N+4), unbounded in N. F(2t)/F(t) = artanh(1/(N+4))/artanh(1/(N+2)) -> 1. All hold.

**Superlinear refutation.** artanh(q)/q is increasing on [0,1). At q = 1/2 it is 1.0986 < 2. So 2q <= 2 artanh q <= 4q on [0,1/2]. Holds.
Then F(2t) >= 2/(N+4) and F(t)^p <= (4/(N+2))^p, since q(t) <= 1/4.
For p>1, C(4/(N+2))^p ~ C 4^p N^{-p} is eventually below 1/(N+4). q(t) and q(2t) do not depend on t, so t can be chosen after N with A e^{-mu t^2} < 1/(N+4).
Then C F(t)^p + A e^{-mu t^2} < 2/(N+4) <= F(2t). The estimate fails on this class. Holds.
The hypothesis t >= 3 is never used. It is harmless.
The ARGUED scope paragraph (lines 143-147) claims no more than this.

**Theorem R.** In `gap-means-max.md` 4.2, S_ev(t;B) = Z_0(t;B)/lambda_0(B)^t - 1.
In (4), Z_0 = Tr_+ T^t = 1 + N/2 and lambda_0 = 1, so S_ev = N/2. The note's "already N/2" holds.
Theorem R's hypothesis (ES) bounds eps = S_ev and delta, the vacuum-energy additivity defect (4.6). Neither is a function of F. Holds.
Tensoring test: replace each sector operator T_m by T_m (x) B, and C^e by C^e (x) 1, with B >= 0 neutral.
Then Z^{e+m} = Tr(T_m^t C^e) Tr(B^t). Every ratio Z^k/Z^0 is unchanged.
lambda_0 becomes lambda_0 lambda_max(B), so 1 + S_ev is multiplied by Tr(B^t)/lambda_max(B)^t.
Example: B = diag(1, s, ..., s) with M-1 copies of s in (0,1). The factor is 1 + (M-1)s^t, unbounded in M, and the top eigenvalue stays simple. Holds.
The note correctly says this is an algebraic test, not a Wilson model.

**Crossed-background remark.** (K20) in `gap-kanazawa-astra.md` 3.4 (lines 434-456) gives the seam operator C_4(T_0^t + T_{v13}^t)/2 for m = v_24, v = v_13, time 2.
(K20) says its form is nonpositive on the C_4 = -1 subspace and strictly negative on a nonzero such state.
The note says "negative on its nonzero odd subspace". With T_0^t + T_v^t positive invertible, this is the same. Holds.
The conclusion (the derivation of (2) in one frame does not transfer to every frame) follows.
The cited range 417-456 includes 3.4's READ paragraph; the proof is 424-456. Cosmetic.

**Verdict: HOLDS.**

## Item 3. Section 3: propagation lemma, seed, budget, exponent, bridge

**Propagation lemma (5)-(7).** b_n = exp(-mu a_n^2/4). a_{n+1}^2 = 4a_n^2, so b_{n+1} = exp(-mu a_n^2) = b_n^4.
So the error term in (5) is A_n b_n^4. With g_n = max(f_n, b_n):
f_{n+1} <= C_n g_n^4 + A_n g_n^4 <= K_n g_n^4, and b_{n+1} = b_n^4 <= g_n^4 <= K_n g_n^4 because K_n >= 1.
Hence g_{n+1} <= K_n g_n^4, and log g_{n+1} <= log K_n + 4 log g_n.
Divide by 4^{n+1} and sum: 4^{-n} log g_n <= log g_0 + sum_{j<n} 4^{-j-1} log K_j <= log g_0 + B = -gamma.
The last step uses log K_j >= 0, so partial sums are at most B.
So f_n <= g_n <= exp(-gamma 4^n) = exp(-(gamma/a_0^2) a_n^2). The floor keeps g_n > 0. Holds.
Consistency: g_n >= b_n forces gamma/a_0^2 <= mu/4. This is automatic from g_0 >= e^{-mu a_0^2/4} and B >= 0.

**Seed (8).** For constant K: B = log K sum_{n>=0} 4^{-n-1} = log K (1/4)/(3/4) = (log K)/3. Holds.
a_0^2 >= 4(1+B)/mu gives e^{-mu a_0^2/4} <= e^{-1-B}. F(a_0) <= e^{-1}K^{-1/3} = e^{-1-B}.
So g_0 <= e^{-1-B} < e^{-B}, and gamma = -log g_0 - B >= 1. Holds.
The condition a_0 >= 3 is not used by the lemma. It only matches the box family. Harmless.

**Coefficient budget.** log K_n <= D a_n^r = D a_0^r 2^{nr}, so B <= (D a_0^r/4) sum_n 2^{(r-2)n} = D a_0^r/[4(1-2^{r-2})] for r < 2. Holds.
Polynomial K_n: log K_n = O(n + log a_0), and sum 4^{-n} n converges. Holds.
log K_n of order a_n^3: the terms grow like 2^n. B diverges. Holds. (r = 2 also diverges; the note's "0<=r<2" is correct.)

**Exponent requirement.** Put h_n = C^{1/(p-1)} f_n. Then h_{n+1} = C^{1/(p-1)+1} f_n^p = C^{p/(p-1)} f_n^p = h_n^p. So h_n = h_0^{p^n} and the displayed formula holds.
With h_0 < 1, f_n = C^{-1/(p-1)} exp(-c p^n), c = -log h_0 > 0. p^n = (a_n/a_0)^{log_2 p}.
For 1<p<4, log_2 p < 2. Then f_n / [C' a_n^q exp(-sigma a_n^2)] -> infinity for every C', q, sigma > 0. So the equality sequence obeys the p-recursion and fails every area bound. Holds.
p = 2 gives exp(-c a): holds. For a -> ka, p^n = (a_n/a_0)^{log_k p}, and area decay needs log_k p >= 2, i.e. p >= k^2. Holds.
The (FQ) sentence is hedged ("might"). With S_ev >= eta_*^a (`gap-ext-astra.md` line 127), an e^{-ca} bound meets (FQ) whenever c exceeds (1/2)log(1/eta_*) plus polynomial slack. I did not check (FQ) beyond this reading.

**Bridge (9).** For b >= a_0 pick the dyadic a_n with a_n <= b < 2a_n. Then a_n >= b/2.
F(a_n)^eta <= exp(-eta gamma a_n^2/a_0^2) <= exp(-eta gamma b^2/(4a_0^2)). e^{-nu a_n^2} <= e^{-nu b^2/4}. D a_n^h <= D b^h.
So F(b) <= 2D b^h exp(-sigma b^2), sigma = min(eta gamma/a_0^2, nu)/4. This is the stated exponent. Holds.
It needs (9) for every box and frame of the b-family, as the note says. Sizes below a_0 are finite in number and absorb into the constant.
The OPEN paragraph on the seed (lines 264-272) makes no claim to check.

**Verdict: HOLDS.**

## Item 4. Section 4: the latent-bit example, AM6, the scalar inverse example

**4.1 AM6 reading.** Skipped, as the brief allows. I did not open the SA outline lines 2885-2942.

**4.1 Latent bit.** All four slots equal H, with P(H=1) = p in (0,1).
Any cut splits the slots into two halves of two slots, with a reflection theta swapping them. A half-function f sees (H,H). theta f sees the same value.
So E(conj(f) theta f) = (1-p)|f(0,0)|^2 + p|f(1,1)|^2 >= 0. The measure is invariant under every slot permutation. So reflection positivity holds in every cut. Holds.
Each event {slot i = 1} equals {H = 1}, with probability p. The intersection is {H = 1}, with probability p, not p^4.
The disseminated event of {slot 1 = 1} is {all slots = 1} = {H = 1}. The chessboard bound gives P(intersection) <= (p^{1/4})^4 = p. Equality holds. Holds.
So four small averages need not give a small fourth-power joint average under reflection positivity alone. The note scopes it as a probability example, not a Wilson one. Correct.
The ARGUED paragraph (lines 300-308) and the Mack-Petkova READ paragraph state no new claim beyond the missing estimate.

**4.2 Representation (10).** Q = (1+e^{-F})/2 = Z_m^+/Z_m by (K9). D_a = log Q_c - log Q_f matches the (K17) proof (`D = log Q_c(alpha) - log Q_f`, |D| <= log 2). Holds.
Q in (1/2, 1], so log Q in (-log 2, 0], and the difference lies in (-log 2, log 2). The (K17) proof solves L_c(alpha_Lambda) = L_c(alpha) + D for any |D| <= log 2. Section 4.1 of `gap-kanazawa-astra.md` (lines 479-484) already says any prescribed q in [1/2,1] works. So the constant data Q_f = (1+e^{-eps})/2 are encoded at every sufficiently large size with the same (K11) constants and the (K17) shift bound. Holds.

**4.2 Contradiction with (5).** With F = eps at every size: C eps^3 < 1/2 gives C eps^4 < eps/2. For a large, A e^{-mu a^2} < eps/2. So C F^4 + A e^{-mu a^2} < eps = F(2a). This contradicts (5). Holds for constant C, A.
**Correction (scope).** (5) is stated with C_n, A_n, and (6) admits growing budgets (polynomial K_n, or log K_n <= D a_n^r). The literal contradiction with (5) needs sup_n C_n < infinity (so that C_n eps^3 < 1/2 for small eps) and A_n e^{-mu a_n^2} -> 0. For C_n >= eps^{-3} eventually, the constant data satisfy (5).
The note's conclusion survives in the general case by a different route: (5), (6) and the seed together give (7), and constant F = eps contradicts (7). So the representation bounds cannot imply the recursion together with its seed. The text should say "for constant C, A" in the contradiction sentence, or cite (7) for the general budget.

**Verdict: 4.1 HOLDS (AM6 reading not checked). 4.2 HOLDS AFTER CORRECTION: the direct contradiction with (5) is for bounded C_n and subgaussian A_n; for general (6) budgets use (7).**

## Item 5. Section 5: logical qualification, algebraic tail, binary icosahedral remarks

**Qualification.** Constant f > 0: f <= C f^4 iff f^3 >= 1/C iff f >= C^{-1/3}. Holds.
f(a) = tau a^2: f(2a) = 4 tau a^2 <= C tau^4 a^8 iff a^6 >= 4/(C tau^3). True for large a. Holds.
So a non-contracting phase can satisfy the upper inequality and fail only the seed. The logical point is correct.

**Algebraic tail.** F(a) ~ kappa/a^2 gives F(2a)/F(a) -> 1/4. C F(a)^3 -> 0. A e^{-mu a^2}/F(a) ~ (A/kappa) a^2 e^{-mu a^2} -> 0. So the right side of (5) divided by F(a) tends to 0, and (5) fails for large a. Holds for constant C, A.
**Correction (scope).** The note's own budget (6) admits polynomial K_n ("A K_n polynomial in a_n also qualifies", line 224). With C_n of order a_n^6 the tail is consistent with (5).
Exact case: F(a) = kappa/a^2, A_n = 0, C_n = a_n^6/(4 kappa^3). Then C_n F(a_n)^4 = kappa/(4a_n^2) = F(a_{n+1}). (5) holds with equality.
For this budget, B = sum 4^{-n-1}[6 log a_0 + 6n log 2 - log(4 kappa^3)] = (1/3)(6 log a_0 - log 4 - 3 log kappa) + (6 log 2)(1/9) = 2 log a_0 - log kappa.
So e^{-B} = kappa/a_0^2 = F(a_0), and the seed condition g_0 < e^{-B} fails exactly at equality. This agrees with the note's main thesis: the phase defeats the seed, not the inequality.
So "Thus (5) is false in that limit" needs "with C_n = o(a_n^6) and A_n = o(a_n^{-2} e^{mu a_n^2})", for example constant coefficients as written.
The warning about F versus F/B (lines 394-398) is correct and needed.

**U(1) paragraph (ARGUED).** Skeleton B3 (iii) gives the classical Villain value 2 pi^2 b n^2 l_1 l_2/(l_3 l_4), a ratio of transverse to twist-plane area. On n = (a,a,c,d), c,d in {a,2a}, the ratio lies in [1/4, 4]. So the total is order one, as the note says. The note claims nothing more.

**Binary icosahedral.** Its elements other than 1 have trace at most 2cos(pi/5). So Delta_G = 1 - cos(pi/5) > 0.
For M > pi/(2 Delta_G), the (LC) bound 1 - tr/2 <= pi/(2M) < Delta_G forces A_M = B_M = 1. Their commutator is 1, and 1^M != -1. Holds; it is the reused `gap-ext-astra.md` 4.2 argument (lines 509-514).
The norm 1/4: (K25) gives E rho([A,B]) = d_rho^{-2} I. Center-odd irreducibles have dimension at least 2 (`gap-kanazawa-astra.md` 632-637), so the norm is at most 1/4, attained by the defining representation. Holds.
The Delta_G a^2 classical bound is READ from `gap-cf-astra.md` 248-264. I read that passage; it states this bound. The note correctly leaves the finite-beta torus phase estimate open.
The disposition paragraph (lines 434-439) is consistent with the qualification above.

**Verdict: HOLDS AFTER CORRECTION: the algebraic-tail contradiction holds for C_n = o(a_n^6), A_n = o(a_n^{-2}e^{mu a_n^2}); for C_n of order a_n^6, which (6) admits, (5) holds and the seed fails at equality.** The rest of Section 5 HOLDS.

## Stopping decision and RESULT line

The stopping decision names three mechanisms and their failing steps: signed entropy (Section 2), normalized boundary control (4.1), cross-size shift relation (4.2). Each matches a checked counterexample with its stated scope. It claims no impossibility theorem.
The RESULT line says a quartic recursion with an explicit seed implies dyadic (V). The lemma proves that, with sigma = gamma/a_0^2 on the dyadic sizes. It says the Wilson recursion, seed and bridge remain unproved. That matches Section 6. It says the three shortcuts "do not supply them". That is fair as scoped in the text: each shortcut fails on a model class, not on Wilson SU(2).
The summary is fair. The two scope corrections above do not change it.

## Verdict table

| Item | Claim | Verdict |
|---|---|---|
| 1 | (2)-(3) equal Lemma 4 (D-plane), (D-sheet) | HOLDS |
| 1 | Convexity example diag(1,r,r), diag(1,1,-1) | HOLDS |
| 2 | Spectra of T_+, T_-; twisted traces; (4) | HOLDS |
| 2 | Refutation of F(2t) <= C F(t)^p + A e^{-mu t^2} | HOLDS |
| 2 | Theorem R inputs; S_ev = N/2; tensoring test | HOLDS |
| 2 | Crossed-background seam operator (K20) | HOLDS |
| 3 | Propagation lemma (5)-(7) with floor b_n | HOLDS |
| 3 | Seed (8), B = (log K)/3, gamma >= 1 | HOLDS |
| 3 | Coefficient budget examples | HOLDS |
| 3 | Exponent requirement; p<4 fails area decay; p >= k^2 | HOLDS |
| 3 | Bridge (9) and exponent min(eta gamma/a_0^2, nu)/4 | HOLDS |
| 4.1 | Latent-bit example | HOLDS |
| 4.1 | AM6 reading | NOT CHECKED (skipped as allowed) |
| 4.2 | Scalar inverse example and contradiction with (5) | HOLDS AFTER CORRECTION (bounded C_n; general budgets via (7)) |
| 5 | Constant and growing sequences | HOLDS |
| 5 | Algebraic-tail contradiction | HOLDS AFTER CORRECTION (C_n = o(a_n^6); degree-6 budget is a counterexample to the literal claim) |
| 5 | Binary icosahedral remarks, (LC) failure, norm 1/4 | HOLDS |
| - | Stopping decision and RESULT | FAIR |

No FAILS.

RESULT: Every PROVED step of gap-size-rec-astra.md holds by hand, with two scope corrections (the contradictions with (5) in 4.2 and in the algebraic-tail paragraph need bounded, respectively o(a_n^6), coefficients, since the note's own budget (6) admits C_n of order a_n^6 under which an exact kappa/a^2 tail satisfies (5) and fails the seed at equality), and the OPEN stopping decision and RESULT line are a fair summary.
