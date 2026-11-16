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
