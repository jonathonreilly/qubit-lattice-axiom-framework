lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-16T12:36Z

# Check of row 1025 (`library/gap-cr-tomboulis-max.md`): row 1029, `gap-cr-tomboulis-check-opus`

Checker: Claude Opus 5.5, max reasoning, Mac mini worker 1. Same provider as the writer (Claude Fable 5.2), so this is
not an independent check in the sense of the working rules; where a claim is tested by a different derivation (hand
computation on a small torus, a direct expansion) that is said at the place. Source pinned: branch
`claude/ym4d-hard-route` at 92ab0f7ca. Started 2026-11-16 00:36Z (`date -u`).

## 0. Plan (at most eight steps; one step per response, result appended before the next)

1. Read the row-1025 file in full; record its numbered claims, its own work item W1 if any, and the line anchors
   (taken with `grep -n -F` at the moment of citing). Read the queue row 1025 for what was asked.
2. Test first (a): Proposition SIGN on the smallest torus by hand (Z_2, strong and weak coupling, Lemmas LT and HT).
3. Test first (b): the sign of the squared-mean term in Identity MOV (direct second-order expansion of one decimation
   step); and (c) Lemma FAC's product reading against Lemma PT of row 998 (`gap-crux-exercise3-max.md`).
4. Proposition BR (the one inequality (TB)_n) and Lemma FAC with Estimate RATE, line by line, against Tomboulis
   0707.2179 where the file cites it.
5. Identity MIS, Proposition RS with Corollary EVEN, line by line.
6. Lemma PAR-T with Proposition KR, line by line.
7. Proposition SIGN in full and Identity MOV in full, line by line; the FAILS verdicts on Questions 2 and 3.
8. Verdict table (HOLDS / HOLDS AFTER CORRECTION / FAILS with first failing line), W1 if the file names one, RESULT.

## Status log

- 00:36Z: file created with the plan. Next: step 1.

## 1. Step 1 result: what is checked, and where

Read in full: `library/gap-cr-tomboulis-max.md` (1006 lines, at 92ab0f7ca; written by Claude Fable 5.2 max, row 1025,
"nothing checked by another model"), queue rows 1025 and 1029, FINISH.md L52-84 and L299-351, GOAL.md L1-40.
All anchors below are `gap-cr-tomboulis-max.md` line numbers taken with `grep -n -F` at 00:37Z ("L" = line there).

The file names its own work item W1 (L903-916). This check follows it, with two differences: the output name is the
queue row's (`gap-cr-tomboulis-check-opus.md`, not W1's `gap-cr-tomboulis-check.md`), and the checker is the same
provider (W1 asks for "a model that did not write this file", met; "cross-provider if one is free", not met).

Claims under check, with anchors:

| Claim | Anchor | Row 1025's mark |
|---|---|---|
| Proposition BR (a)-(e), with (TB)_n | L222-273 (statement L233-260, (TB)_n L241, proof L262-273) | PROVED, unchecked; found again (check 799 B2) |
| Lemma FAC | L340-347 | PROVED |
| Estimate RATE | L353-369 | ARGUED |
| Test table (Lemma PT row etc.) and 4.4 point 3 ("renames the flux half") | L371-396 | - |
| Identity MIS | L424-448 | PROVED |
| Proposition RS (i)-(iii), the rate paragraph, SI reading | L456-507 (statement L471-480, proof L482-489) | PROVED as a conditional |
| Corollary EVEN | L515-523 | PROVED GIVEN H_DEC |
| Lemma PAR-T: Fact 1, Fact 2, statement (i)-(iii) | L547-614 (Fact 1 L556, Fact 2 L572, statement L588) | PROVED by hand |
| Proposition KR | L616-629 | PROVED given row 800 (K2), (K21) |
| Arithmetic of 6.3 (Sizes; against (SER), (SPR)) | L631-658 (L643, L648) | PROVED as arithmetic |
| Proposition SIGN, Lemma LT, Lemma HT | L349-351 (short form), L680-744 (LT L697, HT L716, proof L730) | PROVED by hand |
| Identity MOV (i)-(iv) | L758-786 | PROVED by hand |
| Ways 1-3 and "the one lemma that is left" | L788-817 | - |
| FAILS on Question 2 | L400-533 (5.5 at L525) | FAILS |
| FAILS on Question 3 | L536-665 (6.4 at L660) | FAILS |

Test-first items, in the order run below. From row 1029: (T1) Proposition SIGN on the smallest torus by hand;
(T2) the sign of the squared-mean term in Identity MOV (iv); (T3) Lemma FAC's product reading against Lemma PT.
From W1 (L909-913): (W1.1) BR (a): G^+ strictly increasing, and the quotient of the two fine numbers is Q of the
Wilson model; (W1.2) Fact 2 (b) of 6.1 for rectangles that share a boundary edge; (W1.3) Lemma LT step (2), the cube
argument, and the count g_0 per cell; (W1.4) Lemma HT, the parity of N_y; (W1.5) the coarse coefficient of Z_2,
delta' = q r delta^q (1 + o(1)); (W1.6) Identity MOV (ii): that the decimated twisted model has exactly the coarse
stack flipped; (W1.7) Proposition RS (iii), second part: that the extra condition on j_i keeps (H1) and (H2).
Judgements asked by W1: is "the trapping domain and the endpoint bracket are the same statement" (L259) right as
worded; is 4.4 point 3 (L390-394) right.

- 00:37Z Step 1 done. Next: Step 2, Proposition SIGN on the smallest torus by hand (T1), with W1.3-W1.5.

## 2. Step 2 result: Proposition SIGN on the smallest torus by hand (T1), with W1.3, W1.4, W1.5

Re-derived by hand from the definitions at L682-736; the same method as the writer's (expansion in delta and in c),
so this is a re-derivation, not an independent check.

**The map for Z_2 (L685).** With c = tanh beta, ((1 + c)/(1 - c))^q = e^(2 q beta), so chat = tanh(q beta) and
c' = tanh(q beta)^(q r). Agrees with the general map of L165 (characters 1 and s, d_j = 1).

**W1.5, the coarse coefficient (L730-731).** chat = (1 - delta^q)/(1 + delta^q) (divide numerator and denominator
by (1 + c)^q). So 1 - chat = 2 delta^q (1 + O(delta^q)), and 1 - c' = 1 - chat^(q r) = 2 q r delta^q (1 + O(delta^q))
for fixed q r. Then delta' = (1 - c')/(1 + c') = q r delta^q (1 + O(delta^q)). HOLDS (with the sharper error O(delta^q)).

**W1.3, Lemma LT (L697-714).** (1 + c s) = (1 + c) delta^((1 - s)/2) for s = +1, -1, so rho = sum delta^(E_eta) / sum
delta^(E_1), with the factor (1 + c)^(#plaquettes) cancelled. Step (1): a (1,2)-slice at fixed (x_3, x_4) is a
two-torus in which every link of directions 1, 2 lies in two slice plaquettes, so prod s_p = 1 over the slice; the
slice holds exactly one plaquette of V; so every slice has an odd number of plaquettes with eta_p s_p = -1, and
E_eta >= M_3 M_4. Step (2), the cube argument: at E_eta = M_3 M_4 each slice holds exactly one plaquette of F and F has
no plaquette of another orientation. A 3-cube with directions 1, 2, 3 over a cell y has prod s_p = 1 over its six faces
(each of its 12 edges lies in two faces; sides >= 2 make them distinct), and prod eta_p = 1 (its two (1,2)-faces lie
over the same cell y, so both or neither are in V). So it has an even number of F-faces; its four other faces are not
in F; so bottom in F iff top in F. Hence the F-plaquette of slice (x_3 + 1, x_4) lies over the same cell as that of
slice (x_3, x_4); the same with direction 4; the (x_3, x_4)-torus is connected, so F = V_y. Step (3), the count: F = V_y
means s(sigma) = eta eta^y, and Fact 1's proof gives tau (the product of the tau_e along a path of cells from c_0 to
y) with s(tau) = eta eta^y. sigma -> sigma tau is a bijection from {sigma : F(sigma) = V_y} onto the flat
configurations, so **each cell y carries exactly g_0 minimisers**, and distinct y give distinct F. Numerator =
M_1 M_2 g_0 delta^(M_3 M_4) (1 + O(delta)), denominator = g_0 + O(delta) (g_0 >= 1: sigma = 1). HOLDS.

**W1.4, Lemma HT (L716-728).** Z = sum over closed S of c^|S|, Z^(12) = sum over closed S of (-1)^|S meet V| c^|S|,
u = (sum over closed S with |S meet V| odd of c^|S|)/Z. Parity of N_y: for cells y, y' with common edge e, sum over
the M_3 M_4 links over e of n_l(S) is even (S closed). Counted by plaquettes: a plaquette of V_y or V_y' holds one link
over e; a plaquette of orientation (dir e, 3) or (dir e, 4) based on e holds two; no other plaquette holds one. So
N_y + N_y' is even; all N_y have the parity of N_(c_0) = |S meet V|. Odd parity gives N_y >= 1 for all y and
|S| >= M_1 M_2; equality forces one (1,2)-plaquette over each cell and nothing else; closedness at the link over e at
height h(y) forces h(y') = h(y); so S is one of the M_3 M_4 slices, each closed and meeting V once. HOLDS.

**Proposition SIGN (L690-736).** (a) Lemma LT on both tori, with L'_1 L'_2 = L_1 L_2/q and q L'_3 L'_4 = L_3 L_4:
rho(Lambda(1); c')/rho(Lambda; c) -> q^(-1) (q r)^(L'_3 L'_4); this is > 1 iff r > q^(-1 + 1/(L'_3 L'_4)), implied by
r > q^(-8/9) = b^(-16/9) since L'_3 L'_4 >= 9. (b) For small c, beta = c + O(c^3), so chat = tanh(q beta) = q c (1 + O(c^2))
and c' = (q c)^(q r) (1 + O(c^2)); Lemma HT on both tori with q r L'_1 L'_2 = r L_1 L_2 gives
u(Lambda(1); c')/u(Lambda; c) -> q^(r L_1 L_2 - 1) c^(-(1 - r) L_1 L_2) (r = 1: q^(L_1 L_2 - 1); r < 1: infinity). HOLDS.

**T1, the smallest torus by hand.** b = 2 (q = 4), Lambda = 6^4, Lambda(1) = 3^4, r = 1.
- Weak coupling: rho(Lambda; c) = 36 delta^36 (1 + O(delta)) (36 cells, 36 slices); delta' = 4 delta^4 (1 + O(delta^4));
  rho(Lambda(1); c') = 9 (4 delta^4)^9 (1 + O(delta)) = 9 * 4^9 delta^36 (1 + O(delta)). Quotient -> 4^8 = 65536 > 1:
  the decimated model has the larger rho, the smaller odd-flux weight; (TB)_1 fails. Same energy delta^36 on both
  sides; the factor 4^9 is the entropy q r of the coarse frustrated plaquette in each of the 9 coarse slices, against
  the rigid fine sheet (Step (2) above). For general r the limit is 4^8 r^9, above 1 iff r > 4^(-8/9) = 0.29.
- Strong coupling: u(Lambda; c) = 36 c^36 (1 + O(c)); c' = (4 c)^4 (1 + O(c^2)); u(Lambda(1); c') = 9 (4 c)^36 (1 + o(1)).
  Quotient -> 4^35 > 1: (TB)_1 holds.
- The thresholds in c depend on the torus (the O-constants do). So "on every torus" in the RESULT line (L1006) reads:
  for every torus there are c_-(Lambda) > 0 and c_+(Lambda) < 1 with (TB)_1 true below c_- and false above c_+. The weak
  side needs r > q^(-1 + 1/(L'_3 L'_4)) (true at r = 1, the case Proposition BR (d) uses); the RESULT line omits this
  r-range. Wording only; no defect.

**"What it shows" (L738-744).** (1)-(3) follow. (2) "no correlation inequality for ferromagnetic Z_2 weights gives
(TB)" is right in the sense: any inequality valid for every weight 1 + c s, c in (0, 1), on these tori, that implied
(TB)_1 would contradict (a). (3) is right: for Z_2 the map has delta' = q r delta^q, so it flows to weak coupling at
large beta and (O-flow) fails there as well.

Verdict, Step 2: **Proposition SIGN HOLDS; Lemma LT HOLDS; Lemma HT HOLDS.** W1.3, W1.4, W1.5 pass. No numeric run
(the smallest torus, 3^4, has 324 links; an exact count is out of reach and the row asks for a hand test).

- 00:40Z Step 2 done. Next: Step 3, Identity MOV (T2 and W1.6) and Lemma FAC against Lemma PT (T3).

## 3. Step 3 result: Identity MOV (T2, W1.6) and Lemma FAC against Lemma PT (T3)

### 3.1 Identity MOV (L758-786)

Re-derived from the definitions; same method as the writer's.

- **(i)** Z(lam) = integral of exp(sum_p (1 + lam delta_p) log f(U_p)); log f is bounded (f continuous, positive, G
  compact). So (d/dlam) log Z = E_lam[Y] and (d^2/dlam^2) log Z = Var_lam(Y). Same for Z^(12) with Y^tw. For
  Z^+ = (Z + Z^(12))/2 the first derivative is p E[Y] + (1 - p) E^tw[Y^tw] with p = Z/(Z + Z^(12)), and the second is
  the variance of the two-component mixture. HOLDS.
- **(ii)** At lam = 0 the untwisted law is translation invariant. For the twisted law: with tau = tau_e of Fact 1,
  if U has the law with the stack at c' then W = tau U has the law with the stack at c, and eta^c_p W_p = eta^(c')_p U_p
  for every p. With translations this gives: the law of the family (eta_p U_p) under the twisted measure is
  translation invariant, the plaquettes of V included. So E[log f(eta_p U_p)] is one number per orientation, and
  sum_p delta_p over one orientation is (N/b^2)(b^2 - 1) - N(1 - 1/b^2) = 0 (sides multiples of b). The three first
  derivatives vanish at lam = 0. HOLDS. (At lam > 0 the weights are not translation invariant; (ii) is claimed at
  lam = 0 only, and only that is used.)
- **(iii)** log Z is convex in lam with derivative 0 at 0, so log Z(1) >= log Z(0). Z(1) = F_0'^(|Lambda(1)|)
  Z(Lambda(1); c') (r = 1; see W1.6 below for the exact integration), so this is T's (U) at r = 1. HOLDS.
- **(iv)** Taylor's formula with integral remainder for phi = log Z^+ - log Z, phi'(0) = 0 by (ii):
  phi(1) - phi(0) = integral of (1 - lam) phi''(lam). phi'' = Var^+ - Var = p Var + (1 - p) Var^tw + p (1 - p) (Dm)^2 - Var
  = (1 - p) {Var^tw - Var + p (Dm)^2}, Dm = E^tw[Y^tw] - E[Y]. This is the printed integrand. Q(1) = (1 + rho_dec)/2
  with rho_dec = Z^(12)(Lambda(1); c')/Z(Lambda(1); c') (the bulk factor cancels), so phi(1) - phi(0) <= 0 iff
  rho(Lambda(1); c') <= rho(Lambda), which is (TB)_1. HOLDS.

**T2, the sign of the squared-mean term.** Its coefficient (1 - lam)(1 - p_lam) p_lam is >= 0 (1 - p = rho/(1 + rho)
> 0), and (Dm)^2 >= 0. So it adds a non-negative amount to log Q(1) - log Q(0), that is it pushes towards
rho_dec > rho_fine, against (TB)_1. "A squared shift of its mean, which always works against (TB)" (L784-785) is
right; so is "(TB)_1 needs the twisted model to have the smaller variance, with a margin".

**W1.6, the decimated twisted model has exactly the coarse stack flipped.** At lam = 1 only skeleton plaquettes
carry weight. Checked which links meet them: a link of direction mu with transverse coordinates (x_nu, x_rho, x_sigma)
lies in a skeleton plaquette of orientation (mu, nu) iff x_rho, x_sigma are multiples of b; so a link with exactly
one transverse coordinate off the sublattice lies in one skeleton plane only (interior to one coarse face there), a
link with none off lies on a coarse edge line, and a link with two or three off lies in no weighted plaquette.
So the integral is a product over coarse faces glued along coarse edges, and in 2D the interior integral of a b x b
disc of weights sum_j d_j Fhat_j chi_j gives sum_j d_j Fhat_j^(b^2) chi_j of the boundary holonomy (convolution,
chi_j * chi_k = delta_jk chi_j/d_j). The twisted model at lam = 1: the skeleton plaquettes of V are those over c_0 at
heights in (bZ)^2, one in each coarse slice, inside the coarse face over the coarse cell C_0 that contains c_0.
-1 is central, so it passes through the convolution: the coarse face gets sum_j d_j Fhat_j^(b^2) chi_j(-U_bdry), that
is f'(-U). Non-skeleton plaquettes of V have exponent 0 and no effect. So the coarse model has exactly the coarse
stack over C_0 flipped, one coarse plaquette per coarse height. HOLDS.

Verdict: **Identity MOV (i)-(iv) HOLDS.**

### 3.2 Lemma FAC (L340-347) and its reading against Lemma PT (T3)

**Lemma FAC.** The characters of G_1 x G_2 are chi_j chi_k, of dimension d_j d_k; Fubini gives
Fhat_(j,k) = Fhat^1_j Fhat^2_k, so chat_(j,k) = chat^1_j chat^2_k and c'_(j,k) = (chat^1_j)^(b^2 r) (chat^2_k)^(b^2 r)
(non-negative coefficients make the real powers well defined); F_0' = (Fhat^1_0 Fhat^2_0)^(b^2). The Haar measure of
the product is the product measure and the twist (-1, 1) changes only f_1, so Z^(12) = Z_1^(12) Z_2 and rho = rho_1.
HOLDS. Consequence used by the table: along the bounding sequence, M^n(f_1 f_2) = M^n(f_1) M^n(f_2), so (TB)_n of
the product with the twist (-1, 1) is (TB)_n of the first factor.

**Against Lemma PT** (`gap-crux-exercise3-max.md` L690-713) **and Corollary PT1** (L715-719). PT's product is the same
object (group G_1 x G_2, weight w_1 w_2), with the factor indices swapped (PT1 puts U(1) first; FAC puts the factor
with the central -1 first). PT (a) Z = Z_1 Z_2 is FAC's factorisation. PT1: compact U(1) in its massless phase times
any model of the class has no seed, so a hypothesis that reads only the other factor cannot belong to a valid tool.
The table cell (L375) applies this with SU(2) as FAC's G_1 and U(1) as G_2. The reading matches, with one input the
cell does not name:

- "H_DEC of SU(2) gives H_DEC of the product" needs (O-flow) for the product weight, so the U(1) factor's bounding
  sequence must also reach small norm. Since ||c|| of the product is (1 + ||c^1||)(1 + ||c^2||) - 1, this holds if both
  factors flow. For U(1) at r = 1 this is Ito's theorem (U(N), N = 1; row 1025 L200-201 and its U(1) row L379), cited,
  not rebuilt. With it the cell's conclusion stands: GIVEN H_DEC for SU(2), Ito's flow for U(1), and the U(1)
  theorem I28 behind PT1, the product has H_DEC true and no seed, so DEC is refuted as a tool for T_fix and T_W; its
  conclusion T_flux for the twist (-1, 1) is the SU(2) factor's and is untouched.

Verdict: **Lemma FAC HOLDS; T3 passes, HOLDS AFTER CORRECTION for the table cell L375** (add: "given also Ito's flow
for the U(1) factor"; no conclusion changes).

- 00:43Z Step 3 done. Next: Step 4, Proposition BR against Tomboulis 0707.2179 and PoS(Confinement8)020 (W1.1).

## 4. Step 4 result: Proposition BR against the sources (W1.1), and Estimate RATE

Sources fetched by this check into its own scratch folder (`/tmp/row1029-lit`, PyMuPDF text layer, nothing executed):
Tomboulis arXiv:0707.2179v1 (T) pp. 7-8, 11-14, 22-30, 43-45; Tomboulis PoS(Confinement8)020 pp. 6-8. Quotes are short.

**Reading of the definitions (L162-186).** T (2.19)-(2.22) p. 8: c_j(n) = chat_j(n)^(b^2 r), F_0(n) = Fhat_0(n)^(b^2),
Fhat_j = integral of f(U, n - 1)^zeta chi_j/d_j, zeta = b^(d-2) by (2.17). Matches L165. T (3.9) p. 11 allows c^L_j(n) = 0,
"a restatement of (2.14)"; with it T (3.12) is ctilde = w(alpha) c^U, as row 1025 uses. T (3.16), (3.19): the bulk
factor is (F_0^U)^(h(alpha, t) |Lambda(m)|), |Lambda(m)| = number of plaquettes (T p. 35, "Let |Lambda(n)| denote the
number of plaquettes"). (3.22)-(3.24) existence and uniqueness of the level alpha(t); (3.25)-(3.27) alpha_t = v > 0.
The lane's (I) (L181-188) is a faithful reading.

**W1.1, first part: G^+ is strictly increasing.** T IV.5 (4.16), p. 22: "ln Z^+_(Lambda(m))({ctilde_j(m, alpha, r)}) and
ln Ztilde^+_(Lambda(m))(beta, h, alpha, t, r) are increasing functions of alpha: d ln Z^+/d alpha > 0". G^+(alpha) of
L262 is ln Ztilde^+ at fixed t. So G^+ is strictly increasing on (0, 1) (strict by (4.16)). HOLDS.

**W1.1, second part: the quotient of the two fine numbers is Q of the Wilson model.** The fine numbers at step n are
Z_(Lambda(n-1)) and Z^+_(Lambda(n-1)) of T (5.19)-(5.20). T (5.9) chooses t_m, t_m^+ at every step m < n so that the
bulk factors agree, and then (5.10) p. 26 reads (1 + Z^(-)_Lambda/Z_Lambda) = 2 Ztilde^+_(Lambda(n))(alpha^+(t^+), t^+)/
Ztilde_(Lambda(n))(alpha(t), t) = 2 Z^+_(Lambda(n-1))/Z_(Lambda(n-1)). With Z^+ = (Z + Z^(-))/2 (T (5.1)) this is
Z^+_(Lambda(n-1))/Z_(Lambda(n-1)) = Q(Lambda). HOLDS, given T's claim that (5.9) can be met at each step ("clearly
always possible by (3.32) and (4.25), and by (5.6)", p. 25; PoS (4.3)-(4.5) adds the condition alpha <= 1 - delta,
the reason for r_m < 1). This claim is used only by BR (a)-(b); BR (c)-(d) do not use it.

**BR (a)-(d) (L233-248, proof L262-273).** (a): G^+(alpha^+(t)) = log Z^+_fine and G^+(alpha(t)) = log Z_fine +
log Q_c(alpha(t)) by the two level equations; subtract; strict monotonicity gives the sign. HOLDS. (b): both
directions follow from (a); I_h is an interval since alpha(.) is continuous (T (3.25)). HOLDS. (c): rho_c is
continuous on [0, 1], rho_c(0) = 1 (c^L = 0), rho_c <= 1 (T IV.1, (5.3)), so its range is [min rho_c, 1] and
rho_f <= 1; the IVT gives the claim; (TB)_n gives min rho_c <= rho_c(1) <= rho_f. With (5.24), (5.23) with c^L = 0 is
"1 >= rho_f >= rho_c(1)", which is (TB)_n. HOLDS. Note: (TB)_n is literally T's (5.22) (p. 27), which T derives from
(5.17) at the matching point and (5.16); T's own Appendix C §2 (pp. 44-45, (C.14)-(C.15)) reaches (5.23) from the
assumption "there is t_I with alpha(t_I) < alpha^+(t_I)" and says "One way to complete it would be to show that, for
some interpolation h, there is at least one value t_I such that alpha(t_I) < alpha^+(t_I)". By BR (a) that
assumption is rho_f > rho_c(alpha(t_I)), a bracket at an interior point. This confirms BR's reading from the source.
(d): T's Section 6 consumes V.1 in the form (6.5) p. 29, "exp(-F^(-)_Lambda) = Z^(-)_(Lambda(n))({ctilde(n, alpha*)})/
Z_(Lambda(n))({ctilde(n, alpha*)})", evaluated "within a convergent strong coupling polymer expansion". The
existence form of (5.17) supplies such an alpha* in [0, 1] with ctilde(alpha*) <= c^U(n). So (O-flow) and (TB)_n give
what Section 6 uses. HOLDS. The paraphrase at L272 ("T's use ... is rho_f >= rho(Lambda(n); c^U(n)) and the
expansion at c^U(n)") is (5.22), not (6.5); both are supplied by (TB)_n, so nothing changes.

Caveat on (d) (not a defect of BR's logic). "With r = 1 the flow is Ito's theorem" (L246-247, and the RESULT line)
drops row 1025's own caution at L200-203: the quoted theorem is coefficient by coefficient, and the norm form
||c^U(n)|| <= eps_SC that (O-flow) needs was not checked. So "(TB)_n is the line's only open obligation beyond its
cited inputs" holds with (O-flow) in norm form counted as a cited input whose form is unverified.

**BR (e) and the W1 judgement on L259.** PoS p. 7 (4.8)-(4.9): the system (4.9) is the two level equations at one
(alpha, t), that is (O-match)_n. PoS p. 8: Meyer's monotone iteration under (i) F(x_0) < 0, (ii) [1 + lam F_x]^(-1) >= 0
on D, bounded D with "at least one component of F ... positive on dD"; "the above conditions are satisfied ... for n
large enough and appropriate choice of ... h" is asserted, not shown. PoS p. 7: the chain "[Z^(-)/Z]_(alpha=0) >
Z^(-)_Lambda/Z_Lambda > [Z^(-)/Z]_(alpha=1)" is "seen numerically to hold". So (e)'s reading of the source is right,
and its right-hand inequality is (TB)_n. But the sentence "So a trapping domain exists for some admissible h exactly
when the bracket holds on its alpha-range: **the trapping domain and the endpoint bracket are the same statement**"
(L257-259) claims an equivalence of which only one direction is proved:
- proved: a solution of (4.9) in D (which Meyer's theorem gives from a trapping domain) puts Q_f in Q_c of the
  alpha-range of D (BR (b)); with (5.24) this gives (TB)_n;
- proved: (TB)_n gives the consumed (4.12) = (5.17) in existence form, with no domain and no iteration (BR (c));
- not proved: that the bracket gives a domain with Meyer's hypotheses (i)-(iii), or even a solution of (4.9). A root
  alpha* of Q_c = Q_f solves (4.9) only if alpha* lies on the level curve, alpha* = alpha(t*) for some admissible h
  and t*; with h in [0, 1] that needs Z_c(alpha*) <= Z_fine <= (F_0^U)^(|Lambda'|) Z_c(alpha*), which nothing above
  shows. (Tomboulis's own sentence "by (4.7), is equivalent to a solution of (4.9)", PoS p. 7, skips the same point.)
**Verdict on L259: HOLDS AFTER CORRECTION.** Replace "a trapping domain exists for some admissible h exactly when the
bracket holds on its alpha-range: the trapping domain and the endpoint bracket are the same statement" by "a trapping
domain implies the bracket on its alpha-range, and the bracket alone gives the consumed representation (4.12); so
for the line's conclusion the trapping domain carries no content beyond (TB)_n". Every use of (e) in row 1025
(5.1 L416, 8.5 L885-886, RESULT) needs only this one-way form; no conclusion changes.

**Proposition BR, verdict: HOLDS (a)-(d); (e) HOLDS AFTER CORRECTION (wording, above).**

**Estimate RATE (L353-369), marked ARGUED.** Arithmetic re-done: log(psi/sin psi) = psi^2/6 + O(psi^4); with
beta = 1/(2 tau), 1/(2 tauhat) = zeta beta - (zeta - 1)/3, beta' = (zeta beta - (zeta - 1)/3)/(b^2 r). d = 4 (zeta = b^2):
beta' = beta/r - (b^2 - 1)/(3 b^2 r); b = 2, r = 1: drop 1/4. d = 5 (zeta = b^3): beta' = (b/r) beta - (b^3 - 1)/(3 b^2 r).
One loop: Delta beta per doubling = 8 beta_0 log 2 with beta_0 = 11/(24 pi^2), = (11/(3 pi^2)) log 2 = 0.2575;
log b/Delta_b = 3 b^2 log b/(b^2 - 1) = 2.773 (b = 2), 3.708 (b = 3) against 3 pi^2/11 = 2.692; beta_c(r) =
(b^2 - 1)/(3 b^2 (1 - r)) = 2.5 at b = 2, r = 0.9; d = 5 threshold (b^2 + b + 1)/(3 b^2). All numbers agree. The mark
ARGUED is right: the small-angle step is not controlled at couplings of order one, as row 1025 says.

- 00:47Z Step 4 done. Next: Step 5, Identity MIS, Proposition RS (W1.7) and Corollary EVEN against row 1017.

## 5. Step 5 result: Identity MIS, Proposition RS (W1.7), Corollary EVEN, and the FAILS on Question 2

Inputs read for this step: `gap-compact-rigidity-max.md` (row 1017) L140-200 (rescaling, admissible sequence (H1),
(H2), Lemma UF, Theorem CE with proof). Lane conventions used: F = log Z, f = inf F/|n|, Delta = F - f |n| (row 998
Lemma PT (a) L703-708; row 1017 L140).

**Identity MIS (L424-432).** At one step (fine torus b n, coarse torus n, 6 |n| coarse plaquettes, T p. 35 for the
count) the level equation reads F_A(b n) = 6 |n| h(alpha_n, t) log F_0^U + F_B(n; alpha_n). Subtracting
b^4 f_A |n| and f_B(alpha_n) |n| gives the identity. HOLDS (it is a rewriting). Consequences (a)-(c) (L434-440):
(a) a common alpha_inf on tori of unbounded volume with bounded Delta forces G(alpha_inf) = b^4 f_A, then
Delta_A(b n) = Delta_B(n; alpha_inf); (b) is BR (b); (c) O(1/|n|) in alpha is O(1) in Delta. All follow. HOLDS.

**Proposition RS (L471-489).** (i): for fixed m and large i, side/2^(n_(j_i)) = u_0 2^(q_i + m) is an integer >= 3
(u_0 >= 3, q_i + m >= 0), so (TB) and the coarse bound give u <= g(u_0 2^(q_i + m)) -> 0; by Theorem CE (e) u_E(2^m) is the
limit of these numbers. HOLDS. (ii): the quotient u_0 2^(q_i + m) drops below 3, and (DEC-traj) speaks only of cubes
with an integer quotient >= 3. HOLDS. (iii) first part: q_i >= k_i - sup(n_j - e_j) -> infinity. HOLDS.

**W1.7, (iii) second part.** In the proof of Theorem CE (i)(b) (row 1017 L180), k_i = 2 i + i_0 and j_i is any
member of the Lemma-UF subsequence J with j_i > j_(i-1), l*_(j_i) > 2^(k_i + i), and D_(j_i)(2^(k_i+m) u_(j_i)) <= D_0 + 1/i
for |m| <= i. Each condition holds for all large j in J (l*_j -> infinity along J; (BDD-Delta) from L_0 on). If
n_j - e_j -> infinity, the extra condition n_j - e_j > k_i + i also holds for all large j, so j_i can meet all of them,
and (H1), (H2) hold with i(m) = |m| exactly as before. Omega non-empty is the failure of (PHYS-SEED) (Proposition OM
(b)), which is the hypothesis of CE (i)(b). Then q_i < -i. **Passes.** HOLDS.

**The rate paragraph (L491-499), marked ARGUED.** log 2^(n_j) = (log 2/Delta_2) beta_j = 2.773 beta_j (Delta_2 = 1/4) or
2.756 beta_j (0.2515); minus c_AF = 2.692 gives exp(0.064 beta_j) to exp(0.081 beta_j). Direction of the belief
argument checked: (TB)_n gives sigma_true(beta) >= sigma_c 4^(-n_0(beta)) ~ exp(-2 beta log 2/Delta), and against
sigma_true ~ exp(-2 c_AF beta) this needs Delta <= log 2/c_AF = 0.2575, a map no faster than the true flow. Right as
ARGUED (it rests on Estimate RATE at large beta and on the scaling belief, as the text says).

**Reading against Proposition SI (L501-507).** "It is kept exactly under (RATE)" (L504-505) is stronger than (iii):
(iii) shows "kept" under (RATE) and "not kept" when n_j - e_j -> infinity. If sup(n_j - e_j) is infinite without
divergence, or diverges only off the Lemma-UF subsequence J, neither part applies. Wording: replace "exactly under
(RATE)" by "under (RATE), and not when n_j - e_j tends to infinity". The case the paragraph argues for is the second,
so its conclusion stands. HOLDS AFTER CORRECTION (wording).

**Corollary EVEN (L515-523).** At one coupling write u = u_0 2^0; e_j is constant, which is outside RS's stated setting
(e_j -> infinity), but the proof of RS (i) applies word for word: q_i = k_i - n_0(beta) -> infinity. So every element of
Omega^gr of that coupling has u_E = 0 on cubes for the planes (1, nu) of Theorem CE (e), and by the cubic symmetry for
every plane. The equivalence: a seed at one size gives seeds at all larger sizes (Theorem S), so (H2) fails and Omega
is empty; no seed at any size gives admissible sequences (CE (i)(a)); a non-empty compact invariant Omega has a
uniformly recurrent element (OM (d)); every element of Omega lifts to Omega^gr (CE (e)), centre-even under H_DEC.
HOLDS (GIVEN H_DEC, whose written implication includes the cited coarse expansion T (6.6)-(6.14)). The text's own
remark "it does not need the limit: u tends to 0 directly" is right; EVEN is a restatement.

**FAILS on Question 2 (5.1-5.5, L400-533).** The verdict "compactness supplies neither the parameter nor the trapping
domain" HOLDS, and it has a valid-form support that the file does not state in 5.5: Theorem CE and Proposition OM
are group-blind (they hold for every family of data with (TM); row 1017 3.3, and its Proposition NR uses the
constants log m), while the parameter exists iff (TB)_n (BR (c)), and (TB)_1 fails for Z_2 at weak coupling
(Proposition SIGN, proved by hand, no cited input) and for U(1) at large beta (given the cited theorems). So no
implication "compactness of Omega gives the parameter" can be valid on a class that contains Z_2. 5.1's sentence
"No compactness of a domain can turn that sign" is the same point said informally. 5.2's last paragraph (the
SU(2) x SU(2) family, L450-454) is marked ARGUED and is only that: it needs (TB) for the first factor to fail by a
margin smaller than the second factor's, which is not known.

Verdicts, Step 5: **Identity MIS HOLDS. Proposition RS HOLDS (W1.7 passes). Corollary EVEN HOLDS (given H_DEC). The
SI reading HOLDS AFTER CORRECTION (wording "exactly"). FAILS on Question 2 HOLDS.**

- 00:50Z Step 5 done. Next: Step 6, Lemma PAR-T (W1.2), Proposition KR, the arithmetic of 6.3.

## 6. Step 6 result: Lemma PAR-T (W1.2), Proposition KR, the arithmetic of 6.3, and the FAILS on Question 3

Inputs read for this step: `gap-short-step-max.md` (row 1018) L150-175 (Lemma PAR with (H1), (H2), Fact 0);
`gap-kanazawa-astra.md` (row 800) L80-172 ((K1)-(K6)), L460-476 ((K21)), L655-690 ((K-RESP) and its consumer).

**Fact 1 (L556-564).** Checked in Step 2 (it is also Lemma LT's step (3)). The plaquettes that contain a link over
the common edge e are: the (1,2)-plaquettes over c and c' (one such link each; sides >= 3 give four distinct edges per
cell) and the plaquettes of orientation (dir e, 3) or (dir e, 4) based on e (two such links each). HOLDS.

**Fact 2 (L572-577) and W1.2.** (a): s_i >= 2 gives every cell of D_i a neighbour in D_i across an interior edge, and
V_c contains the links over that edge. (b): a plaquette of P_i fixes cells that must lie in D_i: the cell under a
(1,2)-plaquette; the two cells on the edge under a mixed plaquette (its link of direction 1 or 2 is over an interior
edge, or its link of direction 3 or 4 is over an interior vertex, whose four cells are all in D_i); the four cells
around the vertex under a (3,4)-plaquette. So P_i meet P_j forces a common cell. **W1.2:** for D_1 = [0,2) x [0,2)
and D_2 = [2,4) x [0,2) sharing the edges at x_1 = 2: those edges are interior to neither (their two cells are in
different rectangles), their end points are interior to neither, so the links over them and over the vertices
(2, y) lie in eta; the (1,2)-plaquettes over (1, y) are in P_1 only (their edge at x_1 = 1 is interior to D_1, no
edge is interior to D_2), those over (2, y) in P_2 only, and the mixed plaquettes over the shared edges lie in no
P_i. Disjointness holds. Also checked: a plaquette of P_i has no link in Lam_j (j != i), else it would lie in P_j; so
Z_i depends on eta only. **Passes.** HOLDS.

**Statement (i)-(iii) (L588-605).** (i): the integral with Z_i^tw for i in S and Z_i otherwise is Z^C, C = {c_i : i in S},
|C| = |S|; Fact 1 gives rho or 1. HOLDS. (ii): E[prod (1 + r_i)] = sum over S of E[prod_S r_i] = 2^(k-1) (1 + rho); for
M non-empty the generating polynomial P_M(x) = (1 - x)^|M| (1 + x)^(k - |M|) has P_M(1) = 0 and P_M(-1) = 2^k or 0;
so the sum is 2^(k-1) (1 - rho) for M = all and 0 otherwise; with 1 - r_i = a_i (1 + r_i) this is the claim. HOLDS.
(iii): 1 + (1 - rho)/(1 + rho) = 1/Q, (1 - rho)/2 = Q (1 - rho)/(1 + rho), Hoelder with k factors, and the sup bound. The
identities hold for every positive weight field. **The two sign claims, "0 <= E^+[a_1 ... a_k]" and "u <= E^+[...]",
need rho <= 1.** The proof says so ("rho <= 1 when the lane's transfer argument applies (row 800 (K9))"), but the
Statement (L594-595) and Remark (4) ("for every positive strength field", L613-614) do not. Counter-example to the
unconditional form, inside the setting (w_p may depend on p): Z_2 with w_p = 1 + c s_p off the stack V and 1 - c s_p
on V. Its "twisted" model is the ferromagnetic one and its "untwisted" model the frustrated one, so rho = 1/rho_ferro
> 1 and E^+[a_1 ... a_k] = (1 - rho)/(1 + rho) < 0. The same happens for Wilson SU(2) backgrounds m that already carry
odd flux in the plane of v (m = v gives rho = Z_0/Z_v > 1). For the required pairs of row 800 (m_2 = 0, v = v_13 or
v_14) rho = R_m(v) is in (0, 1] by (K9), so every use in row 1025 (Proposition KR) is covered. **HOLDS AFTER
CORRECTION:** add "if rho <= 1 (true for the required pairs of row 800, by (K9))" to the two sign claims of (iii) and
to Remark (4).

Remarks (1)-(3) (L607-612): (1) moving c_i inside D_i is the substitution tau_e over an interior edge, whose
plaquettes all lie in P_i. (2)-(3): given eta, the 2^k flip patterns are independent with P(flip i) = r_i/(1 + r_i),
so a_i is the conditional mean of the sign of container i and E^+[prod a_i] = P(even) - P(odd) = (1 - rho)/(1 + rho).
Consistent with (ii). HOLD.

Comparison with row 1018's Lemma PAR (L150-172 there): the same parity algebra with pins replaced by the cohomology
argument of Fact 1; the statements (i)-(iii) have the same form. The torus version is a fair transcription.

**Proposition KR (L616-629).** With (K2) D = log Q_c(alpha) - log Q_f and (K5) D = int_0^beta G_f - int_0^alpha G_c,
G = -d log Q, both quotients 1 at zero coupling: D = H_f - H_c(alpha). [D]_+ <= e_a/8 iff H_f <= e_a/8 + H_c(alpha) iff (by
PAR-T (iii)) E^+_m[a_1 ... a_k] <= exp(e_a/8 + H_c(alpha)) - 1. The background signs of m enter PAR-T as plaquette-
dependent weights, which the setting allows; the twist v is put in the plane of TT by symmetry. The left side does
not depend on the family (it equals (1 - rho)/(1 + rho)). Sufficient forms: exp(e_a/8 + H_c) - 1 >= e_a/8 since H_c >= 0,
then Hoelder or sup. G_f = d/ds log(1 + E^+_s[prod a]) since H = log(1 + E^+[prod a]) at each s. HOLDS.

**The arithmetic of 6.3 (L631-658).** Sizes: 1 - tanh(xi/2) = 2/(e^xi + 1) >= e^(-xi), and 1 - x <= e^(-x), so
tanh(xi/2) <= exp(-e^(-xi)); the condition k e^(-xi) >= log(8/e_a) and xi <= 2 log(a/delta) - log(C a) follow. Against
(SER), (SPR): K(2l) <= phi xi(Sigma_2l, D_l) <= kappa phi K(l); the sheet (Sigma_a, D_delta) needs log_2(a/delta) = i uses
of (SER), so xi <= kappa^i (kappa phi)^(J-i) K(l_0); the text's kappa^(i+1) is a weaker valid bound when kappa >= 1 (the
case meant: kappa = 4). Bounded cost with k = 4^(theta J) beating a = 2^J l_0 needs theta > 1/2 and kappa phi^(1-theta) <= 1;
since phi < 1, phi^(1-theta) increases with theta, so some theta works iff kappa phi^(1/2) < 1, that is kappa^2 phi < 1.
Checked also that letting the cost grow does not help: with i = theta J the log of k e^(-xi) is 2 theta J log 2 minus
K(l_0) [kappa phi^(1-theta)]^J, which fails for large J when kappa phi^(1-theta) > 1. So within the sup-cost bound of
PAR-T (iii), kappa^2 phi < 1 is necessary and sufficient, as stated; kappa phi < 1 with i = 1 gives u_f -> 0 at a power
rate. HOLDS (as arithmetic for a cost obeying the three bounds, which is how 9.2 marks it). The remark on row 793's
two consumer clauses (L655-656) was not re-checked against row 793.

**FAILS on Question 3 (L536-541, L660-665).** Valid form: Lemma PAR-T and Corollary MP are identities that hold in
frozen Z_2 (Remark (4); row 1018 3.3 (c)), where the flux sectors stay degenerate above beta = 2.191 (the lane's
Peierls theorem, `parts/gap.md` L211 in the test table, cited by row 1025 as L206) and the analogue of (K-RESP)
fails. So "PAR and MP give (K-RESP)" FAILS. HOLDS. "Reduces to (SER) and (SPR)": implied only under kappa^2 phi < 1
within the sup-cost arithmetic above; the phrase "only under" (L664) is relative to that arithmetic, not a proof that
kappa^2 phi >= 1 excludes (K-RESP). Wording only.

Verdicts, Step 6: **Lemma PAR-T HOLDS AFTER CORRECTION (hypothesis rho <= 1 for the sign claims); Fact 1, Fact 2
(W1.2) HOLD; Proposition KR HOLDS; arithmetic of 6.3 HOLDS; FAILS on Question 3 HOLDS.**

- 00:52Z Step 6 done (counter-example of the rho <= 1 remark replaced at 00:53Z by a cleaner one). Next: Step 7, Proposition SIGN and Identity MOV in context (Ways 1-3, 4.4 point 3), then the verdict table.

## 7. Step 7 result: the test table, 4.4 (W1 judgement), Ways 1-3, 7.3, 8.3 and the RESULT line

**4.4 point 1 (L385-387).** Follows from Lemma FAC and Lemma PT as checked in 3.2 (given also Ito's flow for the U(1)
factor and the U(1) theorem behind Corollary PT1). HOLDS.

**4.4 point 2 (L388-389), with a check of its range in n.** Proposition SIGN is proved for n = 1 only, while the point
says "(TB)_n ... fails for Z_2 at large beta (PROVED)". The extension to every n is one line, done here as a check
(not an attack): by W1.5 iterated, delta^(n) = A_n delta^(q^n) (1 + o(1)) with A_n = q r A_(n-1)^q, A_0 = 1, so
A_n = (q r)^((q^n - 1)/(q - 1)); Lemma LT on Lambda and on Lambda(n) (sides L^(n) = L/b^n >= 3) gives
rho(Lambda(n); c^(n))/rho(Lambda; c) -> q^(-n) A_n^(L^(n)_3 L^(n)_4), which at r = 1 is at least q^(9 (q^n - 1)/(q - 1) - n) > 1.
At strong coupling c^(n) = q^(q + q^2 + ... + q^n) c^(q^n) (1 + o(1)) at r = 1 and Lemma HT gives the quotient of odd-flux
weights -> q^(-n) q^((q + ... + q^n) L_1 L_2/q^n) > 1. So for Z_2 at r = 1 both signs occur for every n. The point HOLDS
with this one-line extension (row 1025 should cite it, or say "n = 1").

**4.4 point 3 (L390-394), the W1 judgement "renames the flux half".** (TB)_n at n >= n_0(beta) implies the flux half
at that coupling (with the cited coarse expansion: u(Lambda) <= C (L_3 L_4/b^(2n)) exp(-kappa L_1 L_2/b^(2n))), but the
converse is not shown and is not expected: (TB)_n also asserts one numerical inequality at every admissible size,
down to quotients 3, and an area law at the rate of the Migdal-Kadanoff model. Row 1025 itself says so in 8.6
(L898-899: "It is not known to follow from that bound") and in 9.1 ("stronger or equivalent"). So "(TB)_n in the range
where DEC needs it is the flux half itself" and "renames" overstate an equivalence. The FAIL as a step stands on the
correct reading: the step replaces the flux half by a statement at least as strong, with no mechanism, so it moves
nothing. **HOLDS AFTER CORRECTION:** read "is the flux half itself" as "implies the flux half and is not known to
follow from it (T_flux with a rate, at every admissible size)"; the same for "renames" in the RESULT line.

**Test table (L371-381), the cells not checked above.** D2, SHEET, NP: readings, consistent with the definitions.
Compact U(1): FAILS GIVEN Ito's flow and Ito and Seiler's Theorem 2.2 (2), correctly marked as cited; the Villain
remark (beta' = beta up to exp(-c beta) at r = 1) agrees with Estimate RATE's formula without the curvature term.
Frozen groups: (O-flow) fails (for Z_2, delta' = q r delta^q flows to weak coupling); the inference "a proof of H_DEC
must use connectedness twice" is the valid-form reading. Five dimensions: T restricts to d <= 4 (T p. 29, "provided
d <= 4"). HOLD.

**Ways 1-3 and the lemma left (L788-817).** Way 1: T's footnote 10 (p. 27) reads "For Abelian systems, comparison
inequalities of the type (5.15) either follow from Griffith's inequalities ... All such known methods fail in the
non-Abelian case"; it is about (5.15), and row 1025's paraphrase is fair. The stop is valid: Griffiths-Ginibre
inequalities hold for the ferromagnetic Z_2 weights where (TB)_1 fails. Way 2: Y = sum delta_p log f(U_p) with
delta_p = b^2 1_skeleton - 1 has mean-zero period-b coefficients, so only momenta (2 pi/b) k, k != 0, in the transverse
directions enter, as said. Way 3: ARGUED and named-matched to row 1018 O2, as said. The 3 percent figure is
(0.2575 - 0.25)/0.2575 = 2.9 percent. The lemma left (L806-807) is (TB)_n as in 2.4. HOLD (descriptions; no claim
beyond the marks).

**7.3 Frozen Q_8 and 2T (ARGUED).** The Q_8 count re-done: costs beta (1 - tr g/2) are 0 at 1, beta at the six
elements of trace 0, 2 beta at -1. Ordered s-tuples with product -1 and least cost 2 beta: one factor -1 (s ways) or two
factors g_a = g_b of trace 0 (g^2 = -1; 6 C(s, 2) = 3 s (s - 1) ways); three or more non-identity factors cost more.
So s + 3 s (s - 1). The mark ARGUED is right (the fine minimisers are not classified).

**8.3 Filters corrected (L863-874).** The valid-form reading is right: U(1) has H_DEC false (its (TB)_n fails, given the
cited theorems), so it cannot refute "flow and (TB) give the flux bound"; the line is set aside for the reasons given
(Lemma FAC with Lemma PT; Proposition RS with Estimate RATE). HOLDS.

**RESULT line of row 1025 (L1006).** Three wordings need the corrections found above: (1) "the 2008 trapping domain
and the endpoint bracket are one inequality (TB)_n": the trapping domain implies the bracket and is superfluous
given it (Section 4); (2) "with r = 1 the flow is Ito's cited theorem": in coefficient form; the norm form is
unverified (Section 4, caveat); (3) "it renames the flux half": it replaces it by a statement at least as strong
(above). "On every torus" for SIGN is right with torus-dependent thresholds and, on the weak side, r above
q^(-1 + 1/(L'_3 L'_4)) (Section 2). No mark changes.

- 00:54Z Step 7 done. Next: Step 8, verdict table and RESULT.
