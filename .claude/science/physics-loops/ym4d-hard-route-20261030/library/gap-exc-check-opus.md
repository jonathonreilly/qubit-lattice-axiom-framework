# Check of gap-exc-astra.md (FINISH row 881)

- Checker: Claude Opus 5.5 (high effort), by hand, no subagents.
- Clone: /Users/jonreilly/ym4d-lead/clone at ff7f7880547a6684c5c117c5a54fc88fe7a8b79a
- Checked: D/library/gap-exc-astra.md (row 875, OpenAI Codex gpt-6-astra, max)
- Against: D/library/gap-filter-ls-opus.md (row 872), D/library/gap-filter-ls-check-astra.md (row 873)
- D = .claude/science/physics-loops/ym4d-hard-route-20261030

Read in full: gap-exc-astra.md 1-419, gap-filter-ls-opus.md 1-445, gap-filter-ls-check-astra.md 1-563.
Also read: gap-crux-skeleton-max.md 137-175 (Lemmas A1, A2, the cited electric seed) and gap-ext-astra.md 77-92
(admissible tori a >= 3, c, d in {a, 2a}). Every inequality below was redone by hand. No code, no numerics as premises.
Unqualified line numbers refer to gap-exc-astra.md. "872" = gap-filter-ls-opus.md, "873" = gap-filter-ls-check-astra.md.

## S1. The statement of isotropic EXC (lines 57-87) against row 872's EXC (872:128-190) — HOLDS

- Objects match. 872's L(s) = z^|E| K(s)^(1/2) B_m K(s)^(1/2). By 872 Step 5.1 (checked HOLDS, 873:232-239),
  K(s) = s^N K(1) with s^N commuting with K(1)^(1/2), so L(s) = s^(N/2) L(1) s^(N/2), the note's line 63.
  B_m is the isotropic spatial multiplier (coupling beta, same as temporal): "isotropic" means the actual model.
- High set. Line 62 sums over j in {5/2, 7/2, ...}. This is 873's correction of Lemma 3.1 (873:123-127).
- Delta. 872 defines Delta = <N>_- - <N>_all. With <N>_all = p n_- + (1-p) n_+ this is (1-p)(n_- - n_+), line 76.
  EXP(c) at t = a gives a Int_1^S Delta ds/s = log p_S - log p_1, so J = (1/a) log(p_S/p_1), line 78. Checked.
- Quantifiers. 872:170-173: order-one interval I in 2.3-2.6, one number s_* > 1, c_0 > 0, all beta in I, all
  admissible tori, twists with m_2 = 0, i in {3, 4}, t = a. The note's line 81 has the same quantifiers. 872 calls
  s_* "a number" but names the beta-dependent s_G as the natural choice; the note says the endpoint must be either
  a single number or a declared function of beta. This removes an ambiguity in 872; it does not change EXC.
  The "eventual version" (from a fixed a_0) is marked as a weaker variant, and the literal version is kept. Correct.
- n = 3acd is the number of spatial edges of the a x c x d torus. Correct.
- Consumer (line 85): p_1 = p_S exp(-aJ) <= exp(-c_0 a); the rate condition c_0 >= -log(eta_0)/2 is 873:159-173,
  credited as prior work. Correct.
- Line 83: average of Delta for the measure ds/s on [1, S] is J/log S, so the condition is c_0/log S edges per slice.
  A term kappa L_i in J gives p_1 <= exp(-kappa a L_i), an area exponent. Correct.
Verdict S1: HOLDS. The note's EXC is row 872's EXC with the corrected high indicator and the row-873 rate condition.

## S2. Positive boost response of the full electric-only reference (Step 8a (14)-(15), Step 8b (16)-(20)) — HOLDS

(14), r_V^(2T)(beta) > r_(1/2)(beta) for every beta > 0. Checked line by line.
- 2T class data: identity (x = 1), -1 (x = -1), 6 elements x = 0, 8 elements x = 1/2, 8 elements x = -1/2.
  So z_T = E e^(beta x) = (2 cosh beta + 6 + 16 cosh(beta/2))/24 (line 274). E_T x^(2n) = (2 + 16/4^n)/24 =
  (4^n + 8)/(12 4^n) for n >= 1; E_T x^2 = 1/4.
- z_U = 2 I_1(beta)/beta = Sum beta^(2n)/(4^n n!(n+1)!), and E_Haar (2x)^(2n) = Cat_n, so b_n = Cat_n/(4^n (2n)!) =
  1/(4^n n!(n+1)!). Then a_n = E_T x^(2n)/E_U x^(2n) = (4^n + 8)/(12 Cat_n) for n >= 1, a_0 = 1. a_1 = a_2 = 1,
  a_3 = 72/60 = 6/5. Correct.
- Cat_(n+1)/Cat_n = (4n+2)/(n+2). (4^(n+1)+8)(n+2) - (4^n+8)(4n+2) = 4^n(4n+8-4n-2) + 8(n+2-4n-2) = 6(4^n - 4n).
  Zero at n = 1, positive for n >= 2. So a_n is nondecreasing and not constant. Correct.
- (15): with w_n = b_n beta^(2n)/z_U, beta d/dbeta w_n = w_n(2n - <2n>_w), so beta d/dbeta (z_T/z_U) =
  Cov_w(a_n, 2n) >= 0 (Chebyshev, both nondecreasing), strict since all w_n > 0 and a_2 < a_3.
- r_V^(2T) = d/dbeta log z_T (eigenvalue on V: (1/2) E[2x e^(beta x)]/z_T); r_(1/2) = I_2/I_1 = d/dbeta log z_U
  (using I_1' = I_2 + I_1/beta). Strict increase of log(z_T/z_U) gives (14). r_V^(2T) < 1 since x <= 1 with
  positive weight on x < 1. HOLDS.

(16)-(20), electric reference B = 1, full gauge-invariant SU(2) space, beta in a compact I inside (0, inf).
- Endpoint spectrum. At s = 1 the largest nontrivial and the largest odd one-link eigenvalue is r_(1/2) = q_1.
  At S = r_V^(2T)/r_(5/2): spin 5/2 becomes q_S = r_V^(2T); spins 7/2, ... stay below it (r_j strictly decreasing);
  spin 1/2 and spin 1 are below it by (14). So q_S is both the largest nontrivial and the largest odd eigenvalue,
  and q_S < 1. Correct.
- (17): w_j <= q_s for j > 0 gives eps_s(a) <= q_s^(a-1) Sum_(j>0) d_j^2 w_j; the sum is bounded on compact I at
  both endpoints (S(beta) is continuous), q_s has a positive minimum and a maximum q < 1. u_s <= eps_s. Correct.
- (18): Tr K_s^a on the unprojected space is (1 + eps_s(a))^n; the gauge projection commutes with K_s, so the
  physical trace is at most that; the constant state gives at least 1. Correct.
- (19) upper: an odd assignment has a half-integer cycle with odd i-pairing; projected to the i-coordinate circle
  it covers every one of the L_i circle edges, so it has >= L_i half-integer edges (this is A1's crossing argument,
  gap-crux-skeleton-max.md:143-145, credited correctly). Union bound over L_i-subsets, then drop the gauge
  projection: Tr(P_- K^a) <= binom(n, L_i) u^(L_i) (1+eps)^(n-L_i). Divide by Z >= 1. Correct.
  (19) lower: chi_j of one straight i-line holonomy (j = 1/2 at s = 1, j = 5/2 at s = S) is gauge invariant, odd,
  and a K_s eigenvector with eigenvalue q_s^(L_i). Then Tr(P_- K^a) >= q_s^(a L_i); divide by Z <= (1+eps)^n. Correct.
- (20): log binom <= L_i log n; n = 3acd <= 12 a^3; a <= L_i <= 2a; n/(a L_i) <= 12a. The error is at most
  log(12 C a^3)/a + 24 C a q^a. Both terms go to 0 uniformly. Redone; correct.
- Conclusion J^el >= (min_I gamma) L_i/2 for large a, gamma = log(r_V^(2T)/r_(1/2)) > 0. Correct.
- Single-endpoint version (line 352): at beta_0, r_(1/2) < S r_(5/2) = r_V^(2T)(beta_0) < 1, strict, so it persists
  on a small compact interval; the proof is unchanged. Correct.
- (21): the 3-torus has |P| = n spatial plaquettes, so e^(-bn) <= B_b <= e^(bn); congruence and min-max give
  |log p_(s,b) - log p_s^el| <= 2abn and |J_b - J^el| <= 4bn. Correct. Gain order L_i ~ a against cost order b a^3.
- The twist m sits in B_m only, so the reference is twist-independent; "uniform in aspect ratios" covers all twists.

Remark (GUIDE size, from 872's decimals, not a premise): gamma(2.3) = log(0.4841/0.4793) ~ 0.010. The reference gain
is real but small, about 0.01 L_i per slice, against a crude magnetic budget 4 beta n ~ 110 a^3 at beta = 2.3.
Verdict S2: HOLDS, in the stated scope (zero spatial coupling). It is not an isotropic EXC result, and the note
says so (lines 354-363).

## S3. Sign reversal of large boosts on even tori (Step 4, (2)-(5)) — HOLDS (scope remark)

- (2) upper bounds. Every vertex of the cubic 3-torus has degree 6, so the full edge set E is a mod-2 cycle with
  cut pairing A_i mod 2, A_i = acd/L_i. Gauge invariance makes the half-integer set C a cycle, so D = E \ C is a
  cycle. If C's parity is opposite to E's, D has odd i-pairing; its projection to the i-circle is then the whole
  circle, so D has >= L_i edges. Integer edges are never high, so N <= |C| <= n - L_i. Correct.
- (2) attainment. The product of spin-5/2 characters over a partition of E into straight coordinate circles is
  gauge invariant, equals 6^(#circles) at U = 1, lies in the spin-5/2 block of every edge: N = n, parity
  (-1)^(A_i). Replacing one i-circle's character by 1 removes L_i edges and flips the cut parity (an i-circle meets
  the cut once). Correct. No eigenvector property is used, as the note says.
- (4). K_s = Sum_q s^q K_q with K_q = Q_q K_1 >= 0 (Q_q commutes with K_1). Z_sigma is a polynomial of degree
  <= t M_sigma; the top coefficient is z^(nt) Tr_sigma(K_M B_m)^t = z^(nt) Tr_sigma(K_M^(1/2) B_m K_M^(1/2))^t.
  B_m >= e^(-beta|P|) gives K_M^(1/2) B_m K_M^(1/2) >= e^(-beta|P|) K_M, which is nonzero on the sector (the
  attaining vector is in Q_M H_sigma and K_1 is injective). So A_sigma > 0. Correct.
- (3). For A_i even, M_+ = n, M_- = n - L_i; p_s = (A_-/A_+) s^(-a L_i)(1 + O(1/s)); n_sigma = M_sigma + O(1/s);
  Delta = (1 - p)(n_- - n_+) -> -L_i. (5) for A_i odd: Delta ~ L_i (A_+/A_-) s^(-a L_i) > 0. Both redone; correct.
- J(beta, S) -> -inf as S -> inf at fixed volume on A_i-even tori. Correct.
- Scope remark (no correction to the mathematics). The proved hypothesis is "A_i even". For i = 3, A_3 = a d; for
  i = 4, A_4 = a c. "Even a" is a sufficient subfamily; the reversal also holds for odd a when the other transverse
  period is 2a. Only odd a with that period equal to a gives A_i odd, where the large-boost response is positive
  but exponentially small.
- The note's limits are stated correctly: fixed-volume constants, no location of the sign change in [1, S(beta)].
  ARGUED remark of this checker (not proved): the reversal comes from the nearly all-high background overtaking
  the vacuum. In the electric reference that needs s r_(5/2) of order 1 or more, while S(beta) r_(5/2) =
  r_V^(2T) < 1 (by about a factor 2 at beta = 2.3). So the reversal mechanism plausibly sits beyond the natural
  endpoint; with the spatial multiplier this is not established.
Verdict S3: HOLDS. It refutes "Delta >= 0 for every boost" and "raise S until EXC holds"; it is not a counterexample
to EXC at the natural endpoint, as the note says (line 138).

## S4. Negative single-link kernel at the natural endpoint (Step 5, (6)-(7)) — HOLDS

- k_1 = e^(beta x)/z = Sum_j d_j r_j chi_j; C_lo + s C_hi = C + (s-1) C_hi has kernel k_1 + (s-1) h,
  h = Sum_high d_j r_j chi_j, uniformly convergent. chi_j(-I) = -d_j for half-integer j. Every high term is negative
  at -I and S >= 1, so k_S(-I) <= e^(-beta)/z - 36 (S-1) r_(5/2) = e^(-beta)/z - 36 (r_V^(2T) - r_(5/2)). Correct.
- r_(5/2) = I_6/I_1. Independent derivation: termwise in the series, I_(nu+1)(x)/I_nu(x) <= x/(2(nu+1)), so
  I_6/I_1 <= (x/2)^5/(2 3 4 5 6) = (beta/2)^5/720. At beta <= 2.6: 1.3^5 = 3.71293 < 4, so r_(5/2) < 1/180. Correct.
  (I did not reread GL4; this derivation stands without it.)
- r_V^(2T) = E[x sinh(beta x)]/E[e^(beta x)] >= beta E[x^2]/e^beta = beta/(4 e^beta). With beta >= 23/10 in the
  numerator and e^beta < e^3 < 27: > 23/1080. And 23 * 48 = 1104 > 1080, so > 1/48. Correct.
- z = 2 I_1/beta >= 1 and e^beta > 1 + beta >= 33/10, so e^(-beta)/z < 10/33. Correct.
- (7): 36/48 = 3/4, 36/180 = 1/5, 3/4 - 1/5 = 11/20; 10/33 - 11/20 = (200 - 363)/660 = -163/660. Correct.
- Scope (line 186) is right: the convolution stays a positive operator (eigenvalues r_j, S r_j > 0); only the
  pointwise-positive density reading fails. This makes 873:260-262's warning concrete. The Z_2 formula
  k_s(-1) = 1 - s tanh(beta) is correct (cosh normalization).
Verdict S4: HOLDS for every beta in [23/10, 13/5].

## S5. What remains: the relative magnetic response (Step 9, (22) and lines 385-392) — HOLDS

- A_(s,b) = z^n e^(bM/2) K_s e^(bM/2) and L_(s,b) = z^n K_s^(1/2) e^(bM) K_s^(1/2) are XX* and X*X for
  X = z^(n/2) e^(bM/2) K_s^(1/2). M is invariant under the cut flip (each spatial plaquette meets the cut in 0 or 2
  edges), so P_- commutes with M and A, and the sector spectra agree. Correct.
- d_b A = (MA + AM)/2; cycling the trace gives d_b log Tr(P_sigma A^a) = a Tr(P_sigma M A^a)/Tr(P_sigma A^a), so
  d_b log p_(s,b) = a d^mag_(s,b). Integrating from b = 0 (the electric reference) to b = beta and subtracting
  s = 1 from s = S gives (22): J_beta = J^el + Int_0^beta (d^mag_(S,b) - d^mag_(1,b)) db. Redone; correct.
- The note correctly says d^mag is a magnetic-cut expectation, not a spin-law expectation of N.
- The residual at lines 388-392 is, as the note says, equivalent to EXC on this path (it is J_beta >= c_0
  rewritten). It is not presented as a weaker lemma. The absolute bound 4 beta n agrees with (21) and with
  |M| <= n. Correct.
- The note claims no obstruction from the magnetic side (line 417 records the wording fix). Correct: no lemma here
  bounds the double difference in either direction.

Read and spot-checked, outside the five assigned statements: Step 6 (8)-(10), redone by hand (the derivative of
Tr(N L^t) gives Sum_(k=0)^(t-1) Tr(N L^k N L^(t-k)); diagonal part is t^2 times a variance, off-diagonal part
nonnegative): HOLDS. Step 7 (12)-(13), translation plus centre change of variables plus vertex gauge invariance of
the cut change: the argument reads as sound; not redone in detail.

## Assessment

Is EXC still live? Yes. Nothing in the note refutes EXC at the natural endpoint or at any bounded fixed endpoint.
Every negative result is against a proof route: unbounded boosting (S3, fixed volume), a positive edge density along
the boost (S4), sector convexity (Step 6), and the crude spatial comparison (21). The one positive result (S2) shows
that the response has the right scale, order L_i, in the complete electric-only SU(2) model. The margin is thin:
gamma = log(r_V^(2T)/r_(1/2)) is about 0.010 at beta = 2.3 (GUIDE decimals from row 872). The same reference
argument passes for U(1), Q_8, 2T and Z_2 references, so it is not SU(2)-selective; all selectivity must come from
the spatial multiplier.

Sharpest open statement (from (22), with S2's gain). Fix beta in I and S = S(beta) (or one S near beta_0). Prove,
uniformly in admissible tori, twists and b in [0, beta], a bound of order L_i, not order n, on the magnetic double
difference
  Int_0^beta [ (<M>_(-,S,b) - <M>_(all,S,b)) - (<M>_(-,1,b) - <M>_(all,1,b)) ] db >= -theta gamma_min L_i
for some theta < 1 (expectations at the magnetic cut A_(s,b), time period a). With S2 this gives
J_beta >= (1 - theta) gamma_min L_i - o(L_i), an area-type EXC that also meets the row-873 rate condition for large
a. The available bound is 4 beta n, order a^3; the target is order L_i with constant below about 0.01 at beta = 2.3.
The weakest form that still carries EXC is the note's own line 389 (>= -J^el + c_0), which is equivalent to EXC.

No repository file was edited. No subagent, simulation or computation was used. This is a check by one model of
another model's text; it is not an independent derivation of EXC and grants no status.

RESULT: S1 HOLDS (the note's EXC is row 872's EXC with row 873's high-indicator and rate corrections, and an explicit endpoint quantifier); S2 HOLDS (strict r_V^(2T) > r_(1/2) for all beta > 0, and an order-L_i positive boost response, gamma = log(r_V^(2T)/r_(1/2)), in the full electric-only reference, zero spatial coupling only); S3 HOLDS (fixed-volume large-boost Delta -> -L_i whenever A_i is even, which includes every even-a torus and also odd a with the other transverse period 2a); S4 HOLDS (k_S(-I) < -163/660 for beta in [2.3, 2.6]); S5 HOLDS (exact identity (22); the residual is equivalent to EXC, and no magnetic-side bound or obstruction is claimed) — EXC remains live and unproved; the sharpest open statement is an order-L_i (not order-n) lower bound, theta < 1 times gamma_min L_i, on the boost-minus-unboosted, odd-minus-all magnetic-cut plaquette response integrated over b in [0, beta]. Checked by Claude Opus 5.5 (high), by hand.
