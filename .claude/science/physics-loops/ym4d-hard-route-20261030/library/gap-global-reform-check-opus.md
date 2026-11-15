lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-16T08:46Z

# Check of row 1016 (`library/gap-global-reform-max.md`), work item W1

Row 1020 of `FINISH.md` (queued 2026-11-15 20:45Z). Checker: Claude Opus 5.5, max effort, Mac mini worker,
session started 2026-11-15T20:46Z (by `date -u`). Same provider as the checked row (Claude Fable 5.2), so this is not an
independent cross-provider check. Pinned at commit 0d3b45d91. No commit, no push, no claim.

## Status log

- 2026-11-15T20:46Z: file created; plan below is provisional until W1 of the checked file (L1004 and following) is read.
- 20:48Z: steps 1-2 done (inputs read; tests (a), (b); Identity AV; Theorem BH Steps 1-5): all HOLD.
- 20:51Z: step 3 done (Theorem BH Steps 6-7; Corollaries AV2, BH2): no WRONG in 7.1-7.2; two corrections (Step 7 qualifier; BH2 sign slip), see 3.1-3.3.
- 20:53Z: step 4 done (Lemma CEN+, test (c)): HOLDS, both cases and the lattice statement.
- 20:56Z: step 5 done (Lemma MC (a)-(c), test (e)): MC HOLDS; test (e) PARTLY: the 'void solution' meets the words of row 1013's (i) only in the measure sense of 'global'; scope note on CEN+'s reading sentence.
- 20:59Z: step 6 done (Lemma HW (i)-(iii) with the mixed coefficient; Proposition LG with test (d)): both HOLD; one cosmetic note on LG's leading-order display.

## Plan (W1 of the checked file, L1004-1018; at most eight steps; one step per response, result appended before the next)

W1 as written (checked file L1004-1018): read Sections 3.0, 3.1, 4.1-4.3, 4.5, 7.1, 7.2, 7.4, with row 1011's
`gap-pinned-cell-gauge-max.md` 3.1-3.2 for notation and `gap-invent-selective-max.md` 4.1 for Lemma WN. Order:
(i) Identity AV; (ii) Theorem BH Steps 4-7; (iii) Corollaries AV2, BH2; (iv) Lemma CEN+ Steps 1-4, both cases;
(v) Lemma MC (a)-(c); (vi) Lemma HW (i)-(iii); (vii) Proposition LG; (viii) Identity HAM1; (ix) Lemma GT (ii), (iv);
(x) Identity CUBE. Tests first: (a)-(e). Verdicts: HOLDS / HOLDS AFTER CORRECTION / WRONG with the failing line.
Stop rule: stop at the first WRONG in 7.1-7.2 and report it; no new attack. Row 1020 adds: most care on Lemma
CEN+, Lemma MC and Theorem BH.

1. Read 7.1-7.2 with the notation of row 1011 3.1-3.2 and Lemma WN; run tests (a) and (b).
2. (i) Identity AV and (ii) Theorem BH Steps 4-5.
3. (ii) Theorem BH Steps 6-7; (iii) Corollaries AV2 and BH2. (Stop here if a WRONG is found in 7.1-7.2.)
4. (iv) Lemma CEN+ with test (c).
5. (v) Lemma MC with test (e) (row 1013's condition (i)).
6. (vi) Lemma HW and (vii) Proposition LG with test (d).
7. (viii) Identity HAM1, (ix) Lemma GT (ii), (iv), (x) Identity CUBE.
8. Verdict table and RESULT line.

## 1. Step 1: inputs and tests (a), (b)

**Read in full.** Checked file (row 1016, Claude Fable 5.2 max) L673-805 (7.0-7.3) and L990-1071 (8.7-8.9 with W1
at L1004-1018); row 1011 `library/gap-pinned-cell-gauge-max.md` L131-183 (3.1 conventions, class C_b, gauge
covariance; 3.2 Proposition A) and L221-262 (4.1 Proposition B; 4.2 Proposition B'); row 1013
`library/gap-invent-selective-max.md` L136-167 (4.1 Lemma WN, Corollaries WN1-WN3). Conventions used below are
row 1011's: SU(2) = unit quaternions, su(2) = Im H = R^3, [u, v] = 2 u x v, t(g) = Re g, s(g) = Im g; a link field
acts by (e^B U)_l = e^(B_l) U_l (left multiplication, B_l in the frame of the tail); U_p = U_1 U_2 U_3^(-1) U_4^(-1)
based at x for p = (x; mu, nu); A_c = sum_p beta_p w_p t_p over ALL plaquettes of c, boundary plaquettes included;
Z_c(omega) = int exp(A_c(omega, U_int)) dU_int; F_c = - log Z_c; H_c(omega; B) = d^2/d eps^2 F_c(e^(eps B) omega) at 0.

**Test (a): in BH, is psi a function of the pin, and is B the field of the statement? YES to both.**
- p_0 = (x; mu, nu) is a boundary plaquette, so by the definition in row 1011 3.1 its four links are boundary
  links. The map U -> e^(eps B) U (B extended by zero) changes boundary links only. So t_(p_0)(e^(eps B) U) is a
  function of (eps, omega) alone, and psi = its eps-derivative at 0 is a function of the pin omega. The same holds
  for D_B psi.
- The statement puts B = a d lambda on the boundary links, (d lambda)_l = lambda(head) - lambda(tail), lambda the
  indicator of z = x + mu. So B_l = + a on boundary links with head z, - a on boundary links with tail z, 0 on all
  other boundary links: supported on the boundary links at z. On p_0: l_1 = (x -> z) has head z, so B_1 = a;
  l_2 = (z -> x + mu + nu) has tail z, so B_2 = - a; l_3 = (x + nu -> x + mu + nu) and l_4 = (x -> x + nu) do not
  meet z, so B_3 = B_4 = 0. This is the B of Step 4. Note (used in Step 4): B is NOT a gauge transformation at z,
  because e^(eps a) acts on l_1 at its tail x, not at its head z; for U(1) it would be one.

**Test (b): in AV, is the law of the boundary links under E_free equal to Z_c(omega)/Z_free d omega, with the
weights w_p? YES.** E_free has density exp(A_c(U))/Z_free with respect to Haar measure on all links of c, with the
same A_c (same beta_p, same w_p, boundary plaquettes included) as in Z_c. Integrating the interior links gives the
marginal density Z_c(omega)/Z_free of the pin, and the conditional law of the interior links given omega has density
exp(A_c(omega, .))/Z_c(omega), which is the pinned law E_omega. So E_free[f(omega) g(U)] = E_free[f(omega) E_omega g]
for every bounded f, g (used in BH Step 2). The weights enter both sides identically; the identity does not depend
on their values.

## 2. Step 2: (i) Identity AV and (ii) Theorem BH Steps 1-5, redone by hand

### 2.1 Identity AV (checked file L693-708): **HOLDS**

Redone. For fixed B on the boundary links, Z(eps, omega) := Z_c(e^(eps B) omega) is real-analytic in (eps, omega) and
positive (compact group, smooth integrand). For each boundary link, omega_l -> e^(eps B_l) omega_l is a left
translation by a FIXED element, so it keeps Haar measure: int Z(eps, omega) d omega = Z_free for all eps.
Differentiating twice under the integral (allowed: smooth integrand on a compact set) gives int Z''(0, omega) d omega = 0.
With F = - log Z: F' = - Z'/Z and F'' = - Z''/Z + (F')^2, so Z F'' = - Z'' + Z (F')^2, and int Z F'' = int Z (F')^2.
Divide by Z_free and use test (b): E_free[H_c(.; B)] = E_free[(F')^2]. Finally Z'(0, omega) = int X_c(B) exp(A_c) dU_int
= Z E_omega[X_c(B)], where X_c(B) = d/d eps A_c(e^(eps B) U) at 0 with B extended by zero (the extension by zero is
what makes e^(eps B)(omega, U_int) = (e^(eps B) omega, U_int)). So F' = - E_omega X_c(B) and the identity follows.
It is the Fisher-information identity E[- (log p)''] = E[((log p)')^2] for the marginal p = Z_c/Z_free along a
measure-preserving flow. Valid for every box, strength field (signed too), compact gauge group and fixed B, as
stated. Nothing to correct.

### 2.2 Theorem BH, Steps 1-3 (L733-741): **HOLD**

- Step 1: E_free restricted to pins is a probability measure and H_c(.; B) is continuous, so sup >= mean. With 2.1.
- Step 2: psi is a function of the pin (test (a)); by test (b), E_free[psi X] = E_free[psi E_omega X]; Cauchy-Schwarz
  gives (E_free[psi X])^2 <= E_free[psi^2] E_free[(E_omega X)^2]. Missing line (harmless, add it): the division needs
  E_free[psi^2] > 0, which holds because E_free[psi^2] = (2/3) E_free(1 - t^2) by Step 5 and t_(p_0) is not a.s.
  equal to +-1 under a law with a positive continuous density with respect to Haar measure.
- Step 3: U -> e^(eps B) U keeps Haar measure on all links, so int exp(A_c(e^(eps B) U)) psi(e^(eps B) U) dU does not
  depend on eps; d/d eps at 0 gives E_free[X psi] + E_free[D_B psi] = 0. That D_B psi is the SECOND derivative of
  eps -> t_(p_0)(e^(eps B) U) uses e^(eps' B) e^(eps B) = e^((eps + eps') B) link by link (one fixed B_l per link: a
  one-parameter subgroup). Steps 1-3 use no property of the strengths: (BH) holds for every strength field, as stated.

### 2.3 Theorem BH, Step 4, the two expansions (L742-749): **HOLDS**

Redone. U_1 -> e^(eps a) U_1, U_2 -> e^(-eps a) U_2, U_3, U_4 fixed, so U_p(eps) = e^(eps a) U_1 e^(-eps a) V with
V = U_2 U_3^(-1) U_4^(-1); and U_1 e^(-eps a) = e^(-eps a') U_1 with a' = Ad(U_1) a (unit, imaginary), so
U_p(eps) = e^(eps a) e^(-eps a') U_p. Expanding, e^(eps a) e^(-eps a') = 1 + eps (a - a') + eps^2 (a^2/2 + a'^2/2 - a a') + O(eps^3).
With Re(v q) = - v . Im q for imaginary v:
- psi = Re((a - a') U_p) = - (a - a') . s.  (matches)
- D_B psi = 2 Re((a^2/2 + a'^2/2 - a a') U_p) = Re(a^2 U_p) + Re(a'^2 U_p) - 2 Re(a a' U_p); with a^2 = a'^2 = - 1 and
  a a' = - a . a' + a x a', Re(a a' U_p) = - (a . a') t - (a x a') . s, so D_B psi = - 2 t + 2 (a . a') t + 2 (a x a') . s. (matches)
- Cross-check against Proposition A (row 1011 3.2): a_1 = c_1 = a, a_2 = c_2 = Ad(U_1)(- a) = - a', a_3 = a_4 = 0, so
  delta = a - a', kappa = [a_1, a_2] = 2 a x (- a') = - 2 a x a', and - (|delta|^2 t + kappa . s) with |a - a'|^2 = 2 - 2 a . a'
  gives the same D_B psi. The parenthetical of L748-749 is right.

### 2.4 Theorem BH, Step 5, the four gauge averages (L750-757): **HOLDS**

The free law is invariant under U -> U^g for every fixed g: sites of c -> G (Haar on every link, A_c gauge
invariant), so one may average over g Haar-distributed and independent of U. Write R = Ad(h) (Haar on SO(3)), with
int R v dR = 0 and int (R v)_i (R w)_j dR = (v . w/3) delta_ij.
- h at x: l_1 and l_4 have tail x, so U_1 -> h U_1, U_4 -> h U_4, U_p -> h U_p h^(-1): t fixed, s -> R s, a' -> R a', a fixed,
  a' . s fixed. Then: E[(a . a') t] = E[(a . (int R dR) a') t] = 0; E[(a x a') . s] -> int (a x R a') . (R s) dR
  = a . (int R dR)(a' x s) = 0 (R(a' x s) = R a' x R s) -- same as the file's "trace of v -> a x v is 0";
  E[(a . s)(a' . s)] -> (a . (int R dR) s)(a' . s) = 0; E[(a . s)^2] -> E|s|^2/3.
- h' at z: l_1 has head z, l_2 has tail z, so U_1 -> U_1 h'^(-1), U_2 -> h' U_2, U_p fixed; a' -> Ad(U_1) Ad(h'^(-1)) a, so
  a' . s -> (Ad(h'^(-1)) a) . (Ad(U_1^(-1)) s) and E[(a' . s)^2] = E|Ad(U_1^(-1)) s|^2/3 = E|s|^2/3.
- Hence E_free[X psi] = - E_free[D_B psi] = 2 E_free[t] and E_free[psi^2] = E(a . s)^2 - 2 E(a . s)(a' . s) + E(a' . s)^2
  = (2/3) E|s|^2 = (2/3) E(1 - t^2) (|s|^2 = 1 - t^2 on unit quaternions). Values 2 E t and (2/3) E(1 - t^2) confirmed.
- Steps 1-5 then give E_free[(E_omega X)^2] >= (2 E t)^2/((2/3) E(1 - t^2)) = 6 (E t)^2/E(1 - t^2): the constant 6 of (BH)
  is right. Only gauge invariance of the FREE model is used (it holds at boundary sites too); the pinned model is
  not gauge invariant at boundary sites, and the proof never needs it.

## 3. Step 3: (ii) Theorem BH Steps 6-7 and (iii) Corollaries AV2, BH2

### 3.1 Theorem BH, Step 6 (the edge link and positivity; L758-766): **HOLDS**

- The plaquettes of c that contain l_e = (0 -> e_1) are the squares {0, e_1, e_nu, e_1 + e_nu}, nu = 2, ..., d; the
  squares {0, e_1, - e_nu, e_1 - e_nu} leave the box. Each has x_rho = 0 for every rho not in {1, nu}, and d >= 3
  gives at least one such rho, so all four links lie in the face x_rho = 0: boundary links, boundary plaquette.
  Weights: all d - 2 such rho have x_rho = 0, so w_nu = 2^(-(d-2)) > 0.
- Conditional law of U = U_(l_e) given all other links under E_free: density prop. to
  exp(sum_nu b w_nu Re(U sigma_nu)) = exp(Re(U Sigma)), sigma_nu = U_2 U_3^(-1) U_4^(-1) of (0; 1, nu). With
  Sigma = r Sigma-hat, U Sigma-hat is Haar distributed, and Re of a Haar point of S^3 has density (2/pi)(1 - y^2)^(1/2)
  on [-1, 1] (normalisation int (1 - y^2)^(1/2) = pi/2). The conditional mean of y is
  int_0^1 y (e^(ry) - e^(-ry)) (1 - y^2)^(1/2) dy / (positive) > 0 for r > 0, and 0 at r = 0.
- Sigma = b sum_nu w_nu > 0 at the trivial configuration; by continuity r > 0 on a neighbourhood of it, which has
  positive E_free-probability (positive continuous density). So E_free[Re(U Sigma)] = sum_nu b w_nu E_free t_((0;1,nu))
  = E_free[r m(r)] > 0, and some (0; 1, nu) has E_free t > 0; with x = 0, mu = 1 it has z = e_1. Uses only beta > 0 on
  the d - 1 plaquettes at l_e.

### 3.2 Theorem BH, Step 7 (the constants; L767-776): **HOLDS AFTER CORRECTION** (last display needs a qualifier)

Redone line by line.
- phi(b) = log int exp(- b G) dU, G = sum_p w_p (1 - t_p) >= 0: a log-Laplace transform, so convex; phi <= 0 = phi(0);
  e(b) = - phi'(b) = E_free[G] at homogeneous strength b (exp(- b G) = e^(- b W) exp(A_c)). Convexity at b against b/2:
  phi(b/2) >= phi(b) + (b/2) e(b), so (b/2) e(b) <= phi(b/2) - phi(b) <= - phi(b). Correct.
- |U_p - 1| <= sum_i |U_i - 1| (telescoping, |AB - 1| <= |A - 1| + |B - 1| for unit A; |U^(-1) - 1| = |U - 1|), so <= 4 r;
  |q - 1|^2 = 2 - 2 Re q for a unit quaternion, so 1 - t_p = |U_p - 1|^2/2 <= 8 r^2. Correct.
- Haar: U = cos phi + sin phi n has density (2/pi) sin^2 phi on [0, pi] and |U - 1| = 2 sin(phi/2); since
  2 arcsin(r/2) >= r the set {|U - 1| <= r} contains {phi <= r}, of measure >= (2/pi) int_0^r sin^2 >= (2/pi)(4/pi^2) r^3/3
  = 8 r^3/(3 pi^3) (Jordan, sin phi >= 2 phi/pi on [0, pi/2], and r <= 1). Correct.
- r = b^(-1/2) (b >= 1): on the product set G <= 8 W/b, so phi(b) >= - 8 W + L log(8/(3 pi^3)) - (3 L/2) log b. Correct.
  Then e(b) <= (2/b)(8 W + L log(3 pi^3/8) + (3 L/2) log b) = (16 W + 2 log(3 pi^3/8) L + 3 L log b)/b, and
  2 log(3 pi^3/8) = 2 log 11.6274 = 4.9067 <= 4.92. Correct (rounded up, as it must be).
- E_free(1 - t_p) <= e(b)/w_p (all terms of G are >= 0) and w_p >= 2^(-(d-2)) (a plaquette lies in at most d - 2 boundary
  hyperplanes, all S_rho >= 1); 1 - t^2 = (1 - t)(1 + t) <= 2 (1 - t). Correct.
- **The failing line (L775-776):** "the right side of (BH) is at least 3 (1 - 2^(d-2) e(b))^2/(2^(d-2) e(b))". The step
  uses E t >= 1 - 2^(d-2) e(b) and then squares it, which is valid only when 1 - 2^(d-2) e(b) >= 0. Without that
  qualifier the display is false: as b -> 0, e(b) -> W, so the display tends to 3 (2^(d-2) W - 1)^2/(2^(d-2) W), a
  positive box-size number, while the right side of (BH) tends to 0 (E_free t_p -> 0). **Correction:** "for every b
  with 2^(d-2) e(b) <= 1, the right side of (BH) is at least 3 (1 - 2^(d-2) e(b))^2/(2^(d-2) e(b))". Since
  e(b) <= (16 W + 4.92 L + 3 L log b)/b -> 0, the qualifier holds for all large b, and the statement of the theorem
  (growth to infinity at least like b/log b at a fixed box, constants depending on the box through W and L) follows
  unchanged: for large b the bound is >= (3 - o(1)) b/(2^(d-2) (16 W + 4.92 L + 3 L log b)).

**Theorem BH as a whole: HOLDS AFTER CORRECTION.** The two inequalities of (BH), the constant 6, the existence of a
boundary plaquette with E_free t > 0 for every b > 0, the consequence "no pin-uniform curl bound for homogeneous
strength", and the growth like b/log b are all correct. Corrections: the qualifier of 3.2, and the positivity line
E_free psi^2 > 0 of 2.2. Neither is a WRONG; the stop rule does not fire.

### 3.3 Corollaries AV2 and BH2

**Corollary AV2 (L710-722): HOLDS.** (a) Linearity: X_c(B) = - sum_l B_l . N_l with N_l the tail-frame gradient of A_c
in the boundary link l (Proposition A (iii) of row 1011 is only this definition). (b) Covariance: from
(e^(eps B) U)^g = e^(eps Ad_g B) U^g link by link and A_c(U^g) = A_c(U), X_c(B)(U) = X_c(Ad_g B)(U^g) for all B, hence
N_l(U^g) = Ad(g_tail(l)) N_l(U). (c) Pinned means: E_(omega^g)[N_l] = E_omega[N_l(U^g)] by the change of variables
U_int -> U_int^g (Haar invariant, and (omega^g, U_int^g) = (omega, U_int)^g), so n_l(omega^g) = Ad(g_tail(l)) n_l(omega).
(d) Z_c(omega^g) = Z_c(omega) and Haar on pins is gauge invariant, so the free pin law is invariant. (e) By AV,
E_free[H_c(.; a theta)] = E_free[(sum_l theta_l a . n_l)^2]; averaging over independent Haar g_x kills pairs with
different tails (int Ad(g) v dg = 0) and gives (1/3) n_l . n_l' for equal tails. Only boundary sites occur (tails of
boundary links). The reading "site-diagonal: no difference of theta across two sites appears" is accurate; within
one site the form couples the links with that tail (corner-type differences, as in Lemma WN).

**Corollary BH2 (L778-797): HOLDS AFTER CORRECTION (cosmetic sign).**
- Corner twists of B = a theta on p = (x; mu, nu), from Proposition A: delta_p . s_p = (theta_1 - theta_4) a . s_(p,x)
  + theta_2 a . s_(p,x+mu) - theta_3 a . s_(p,x+nu) (use Ad(g) a . s_p = a . s(g^(-1) U_p g) with g = U_1, U_1 U_2 U_3^(-1), U_p).
  So the twist at x + nu is **- theta_3**, not theta_3 as written at L780 (Lemma WN's rule theta_(p,y) = F_(l',y) - F_(l,y)
  gives the same: p arrives at x + nu along l_3 at its tail, where F = theta_3, and leaves along l_4 at its head, where
  F = 0). Row 1011's own Proposition B' proof (L254-255) has the - sign. Only squares theta_(p,y)^2 enter m_p, the
  numerator and the bound, so nothing downstream changes. Correction: "- theta_3 at x + nu".
- psi = sum_Q D_B t_p is a function of the pin (Q consists of boundary plaquettes). D_B t_p = - sum_y theta_(p,y) a . s_(p,y)
  (Lemma WN (i), redone here from Proposition A as above). D_B^2 t_p = - t_p m_p + (cross terms in pairs of distinct
  corners); in E_free every site is free, and the gauge average at one corner of a pair kills its cross term
  (the closed word passes that site once): E_free[X psi] = - E_free D_B psi = sum_Q E_free[t_p] m_p. Correct.
- s_(p,y) -> Ad(h) s_(p,y) under h at y, while s_(q,y') for y' != y is unchanged (the word based at y' passes y once,
  as ... V h^(-1) h V' ...). So E_free psi^2 = (1/3) sum_y E_free |sum_Q theta_(p,y) s_(p,y)|^2. At one y at most n_Q terms
  are non-zero, so |sum|^2 <= n_Q sum |theta_(p,y) s_(p,y)|^2 (Cauchy-Schwarz; the file's "Minkowski" followed by the
  same counting is equivalent), and |s_(p,y)|^2 = 1 - t_p^2 for every base point (conjugate holonomies). Summing over y
  gives E_free psi^2 <= (1/3) n_Q max_Q E(1 - t^2) sum_Q m_p, and the displayed bound with the constant 3 follows from
  Steps 1-3. Correct for every strength field.
- Special case: Q = {p_0}, theta = d lambda_z: twists 1 at x, - 1 at z, 0 elsewhere, m = 2, n_Q = 1, bound
  3 (2 E t)^2/(2 E(1 - t^2)) = 6 (E t)^2/E(1 - t^2) = (BH). Correct.
- m_p(theta) = (theta_1 - theta_4)^2 + theta_2^2 + theta_3^2 is the functional of row 1011 Proposition B' (L242-243;
  there weighted by w_p). Correct. The uniform-in-size lower bound on the ratio is labelled ARGUED in the file and is
  not checked here.
- Dependence on Lemma WN: only WN (i) and the cross-term step of WN (iii) are used, and both are redone above, so
  BH2 does not need row 1013's (unchecked) record.

## 4. Step 4: (iv) Lemma CEN+ (checked file L446-490), with test (c)

Notation: <p, q> = Re(p q-bar) is the Euclidean inner product of H = R^4, and q-bar = q^(-1) on unit quaternions.

**Set-up.** M^(-1) = U_2 U_3^(-1) U_4^(-1), so Re U_p = Re(U_1 M^(-1)) = <U_1, M>; likewise the left side of the hypothesis
is <phi_1(U_1), M'>. Correct.

**Step 1: HOLDS.** U_1 is a free variable, so U_1 = M is allowed for every (U_2, U_3, U_4); then <M', phi_1(M)> = 1 and
|M' - phi_1(M)|^2 = 2 - 2 <M', phi_1(M)> = 0. This gives (*).

**Test (c): does M range over all of SU(2)? YES.** M = U_4 U_3 U_2^(-1); U_2 = U_3 = 1, U_4 = M arbitrary.

**Step 2: HOLDS.** By (c), <phi_1(M), phi_1(u)> = <M, u> for all M, u in SU(2). The e_i = 1, i, j, k are unit quaternions,
so f_i = phi_1(e_i) satisfy <f_i, f_j> = delta_ij (an orthonormal basis of R^4) and <phi_1(u), f_i> = <u, e_i>. Expansion in
an orthonormal basis gives phi_1(u) = sum_i <u, e_i> f_i = T u with T: e_i -> f_i in O(4). (The file's remark that the
squares sum to 1 is not needed; expansion in a basis is exact.) No continuity is used, as claimed.

**Step 3: HOLDS.** c = T(1) is a unit quaternion; T' = c^(-1) T is in O(4) and fixes 1, so it preserves Im H = 1-perp
and acts there by an element of O(3) = SO(3) x {+-I}. Proper: T' = Ad(q) on Im H, so T'(u) = q u q^(-1) for all u and
phi_1(u) = (c q) u q^(-1). Improper: T' = - Ad(q) on Im H, and u -> q u-bar q^(-1) fixes 1 and is - Ad(q) on Im H, so
phi_1(u) = (c q) u^(-1) q^(-1). The input "SU(2) -> SO(3) is onto" is classical and named as an input. Correct.

**Step 4, reduction to one type: HOLDS.** From (*): U_2 = U_3 = 1 gives phi_4(u) = phi_1(u) phi_2(1) phi_3(1)^(-1);
U_2 = U_4 = 1 gives phi_3(u) = phi_4(1)^(-1) phi_1(u) phi_2(1); U_3 = U_4 = 1 gives phi_2(u) = phi_1(u^(-1))^(-1) phi_4(1) phi_3(1).
If phi_1(u) = L u R^(-1), then phi_2(u) = R u L^(-1) C, so all four are proper; if phi_1(u) = L u^(-1) R^(-1), then
phi_2(u) = R u^(-1) L^(-1) C, so all four are improper. Correct.

**Step 4, proper case: HOLDS.** The displayed form of (*) is right ((L_2 U_2 R_2^(-1))^(-1) = R_2 U_2^(-1) L_2^(-1)).
- U_2 = U_3 = 1: L_1^(-1) L_4 U_4 = U_4 z with z = R_1^(-1) L_2 R_2^(-1) R_3 L_3^(-1) R_4 constant; U_4 = 1 gives z = L_1^(-1) L_4,
  so z commutes with SU(2), z = +-1, L_4 = +-L_1.
- Cancel L_1 U_4: +- R_4^(-1) L_3 U_3 R_3^(-1) R_2 U_2^(-1) L_2^(-1) = U_3 U_2^(-1) R_1^(-1); at U_2 = 1 this is
  (R_4^(-1) L_3) U_3 = U_3 z' with z' constant, and U_3 = 1 makes z' = R_4^(-1) L_3 central: R_4^(-1) L_3 = +-1.
- Cancel U_3: (R_3^(-1) R_2) U_2^(-1) = +- U_2^(-1) (R_1^(-1) L_2); U_2 = 1 makes the two constants equal up to sign, and
  then central: R_3^(-1) R_2 = +-1, R_1^(-1) L_2 = +-1.
- Corners: g_x = L_1, g_(x+mu) = R_1, g_(x+mu+nu) = R_2, g_(x+nu) = R_4 give phi_1 = g_x u g_(x+mu)^(-1),
  phi_4 = +- g_x u g_(x+nu)^(-1), phi_2 = +- g_(x+mu) u g_(x+mu+nu)^(-1), phi_3 = +- g_(x+nu) u (+- g_(x+mu+nu))^(-1): each is
  sigma_i g_tail u g_head^(-1). The hypothesis then reads (prod sigma_i) Re(g_x U_p g_x^(-1)) = Re U_p; at U = 1, prod sigma_i = +1.

**Step 4, improper case: HOLDS (it does not occur).** The displayed (*) is right: the right side is
phi_1(U_4 U_3 U_2^(-1)) = L_1 U_2 U_3^(-1) U_4^(-1) R_1^(-1). With U_3 = 1 and P = R_4^(-1) L_3 R_3^(-1) R_2:
L_4 U_4^(-1) P U_2 L_2^(-1) = L_1 U_2 U_4^(-1) R_1^(-1). U_4 = 1: (L_1^(-1) L_4 P) U_2 = U_2 (R_1^(-1) L_2) for all U_2, so both
constants equal a central eps. U_2 = 1: (L_1^(-1) L_4) u = u (R_1^(-1) L_2 P^(-1)) for all u = U_4^(-1), so both equal a
central eps'. Then P = eps eps', L_4 = eps' L_1, L_2 = eps R_1, and substitution gives L_1 U_4^(-1) U_2 R_1^(-1) =
L_1 U_2 U_4^(-1) R_1^(-1), i.e. U_4^(-1) U_2 = U_2 U_4^(-1) for all U_2, U_4, false at (U_2, U_4) = (i, j). Correct.

**Lattice statement: HOLDS** (for a box with all S_mu >= 1 or a torus with all sides >= 3, in dimension >= 2).
Details the file compresses, written out: (1) every link lies in a plaquette whose four links are distinct, so the
plaquette statement applies to it; (2) L u R^(-1) = L' u R'^(-1) for all u forces (L', R') = +-(L, R) (at u = 1,
L'^(-1) L = R'^(-1) R is central), so each phi_l fixes its pair of link-end elements up to one common sign; (3) at a
corner of p where p meets y along l and l', both link-end elements at y equal +- g^p_y, hence agree up to sign;
(4) at a site y of a box, any two incident links in different directions span a square of the box (the box is a
product of intervals), and every direction has an incident link (S_nu >= 1), so the corner graph at y is complete
multipartite, connected when d >= 2; (5) so the link-end elements at y are +- g_y for one g_y, phi_l = sigma_l
g_tail u g_head^(-1), and trace preservation at U = 1 gives prod_(l in p) sigma_l = +1 on every plaquette: sigma is a
closed Z_2 link field. The scope is on-site maps (each phi_l a function of U_l alone), as the title says.

**Lemma CEN+: HOLDS** (plaquette statement, both cases, and lattice statement). No continuity, group law or measure
is used, as claimed. The remark on other groups (L486-490) is labelled ARGUED and is not checked; its two facts
(complex conjugation keeps Re tr for SU(N); every automorphism of SU(2) is inner) are true.

**Lemma REM (L492-505; not in W1's list, read in passing).** The displayed step is correct: if no site is an end of
both a link of P_B and a link of P minus P_B, then g = k on the sites of P_B and 1 elsewhere gives u^g = u' on P, and
Z(u^g) = Z(u) by the change of variables on the integrated links. Not checked further.

## 5. Step 5: (v) Lemma MC (checked file L506-531), test (e), and a scope note on Lemma CEN+'s reading

### 5.1 Lemma MC: **HOLDS** ((a), (b), (c); one domain remark)

- Set-up: for p containing l, orient the holonomy to start at x along l; t_p = Re(U_l sigma_p) (Re U = Re U^(-1) on SU(2),
  so the orientation does not matter), and sum_(p contains l) beta_p t_p = Re(U_l Sigma_l). Correct.
- (a) Given the other links, U_l -> k U_l (Sigma-hat k^(-1) Sigma-hat^(-1)) is a left and a right translation by fixed
  elements, so it keeps Haar measure on U_l; Fubini gives the product measure. The set {Sigma_l != 0} is invariant
  (Sigma_l does not involve U_l). Re(U_l' Sigma_l) = |Sigma_l| Re(k U_l Sigma-hat k^(-1)) = |Sigma_l| Re(U_l Sigma-hat) =
  Re(U_l Sigma_l), and S' is untouched. Composition: R_(l,k)(R_(l,k')(U))_l = k k' U_l Sigma-hat k'^(-1) k^(-1) Sigma-hat^(-1)
  = R_(l,kk')(U)_l (Sigma-hat is unchanged by R), and R_(l,-1) = id, so it is an action of SU(2)/{+-1} = SO(3). Correct.
- (b) t_p = Re(U_l Sigma-hat Sigma-hat^(-1) sigma_p) = Re(W q_p) = w_0 q_(p,0) - w . q_p-vec; under R_(l,k), W -> k W k^(-1)
  (w_0 fixed, w -> Ad(k) w) and q_p is a function of the other links. sum_p beta_p q_p = Sigma-hat^(-1) Sigma_l = |Sigma_l| is
  real, so sum_p beta_p q_p-vec = 0. Correct.
- (c) Under R_g: U_l -> g_x U_l g_y^(-1) (l = (x -> y)), sigma_p -> g_y sigma_p g_x^(-1), so Sigma-hat -> g_y Sigma-hat g_x^(-1). Then
  (R_(l,k) R_g U)_l = k g_x U_l Sigma-hat g_x^(-1) k^(-1) g_x Sigma-hat^(-1) g_y^(-1) and (R_g R_(l,k') U)_l = g_x k' U_l Sigma-hat
  k'^(-1) Sigma-hat^(-1) g_y^(-1); they agree for k' = g_x^(-1) k g_x, and on the other links both sides are R_g. With a
  conjugation-invariant law of k, (P F)(R_g U) = int F(R_(l, g_x^(-1) k g_x) U) = (P F)(U) for gauge-invariant F; with Haar
  law, P t_p = w_0 q_(p,0) != t_p in general, so P is not the identity. Correct.
- Domain remark (add one line): the map is defined on {Sigma_l != 0}, which has full measure iff beta_p > 0 for some p
  containing l (Sigma_l is then a non-zero real-analytic function of the other links, equal to sum beta_p at the
  trivial configuration); extend R_(l,k) by the identity on the null complement. For homogeneous beta > 0,
  Sigma-hat and hence R_(l,k) do not depend on beta, which is the sense in which it is "exact for every beta".

### 5.2 Test (e): is Lemma MC a fair reading of row 1013's condition (i)? **PARTLY.**

Row 1013's condition (i) (`library/gap-invent-selective-max.md` L277) is quoted exactly in 6.2. Lemma MC meets its
literal words if "acts as a global symmetry" is read as "acts by maps that keep the whole measure": SO(3) is
continuous and non-abelian, it acts on the integration variables, it keeps the Wilson measure, and it moves
gauge-invariant observables. But row 1013 uses "global" in the physics sense in the sentence that motivates (i)
(same file L183: "a pure gauge theory has none, because its only global symmetry on link variables is the
centre"; under the measure reading that sentence would itself be false by Lemma MC), and in that sense a global
symmetry is a field-independent map applied with one element everywhere, whose localisation is not a symmetry.
R_(l,k) acts on one link with a field-dependent axis, and the checked file itself calls it "a local invariance"
(L524-525). So: the sentence "Lemma MC meets it and gives nothing" (L645-646) is fair about the WORDING (the
wording does not exclude field-dependent maps, so it admits void solutions such as MC or any Gibbs-sampler
step, as 6.3 says), but it is not a counterexample to what row 1013 meant. Correction to the wording of 6.2
(HOLDS AFTER CORRECTION): "Lemma MC meets the literal words of (i) when 'global symmetry' is read as 'symmetry of
the measure'; (R-a) states explicitly the sense row 1013 used." The three-part condition (R-a)-(R-c) is a
reasonable explicit form; whether it is the right filter is a lead's ruling (6.2 labels it ARGUED) and is not
checked here.

### 5.3 Scope note on Lemma CEN+'s reading (L484-485) and on (R-a)'s status line (L657)

Lemma CEN+ assumes that the maps keep EVERY plaquette trace pointwise. The reading "in link variables there is no
hidden rigid symmetry of any kind ... beyond the gauge group and the centre one-form symmetry" and the status line
"(R-a) in link variables: only the gauge group and the centre (Lemma CEN+, PROVED)" speak of symmetries, i.e. maps
that keep the Wilson MEASURE (or only the total action). That is a weaker hypothesis, and the bridge is not written.
As written, both sentences HOLD AFTER CORRECTION: either add "that keep every plaquette trace", or add the bridge.
The bridge looks short; the checker's sketch (not part of W1; unchecked by anyone; for the lead to place):
(1) on a box or torus with all links integrated, the one-link marginal of the Wilson measure is Haar (gauge
average at the tail), so an on-site map phi = prod phi_l with phi_* mu = mu has (phi_l)_* Haar = Haar for every l,
and phi keeps product Haar measure; (2) for phi invertible (bimeasurable), phi_* mu = mu then means S o psi = S a.e.,
psi = phi^(-1); (3) two distinct links lie in at most one common plaquette, so the mixed second difference of
S o psi - S in two links of p is that of beta_p (t_p o psi - t_p); hence g_p = t_p o psi - t_p is a.e. a sum of one-link
functions; (4) averaging over one link with Haar measure (psi_l(U_l) is Haar, so E <psi_1(U_1), M'> = 0 = E <U_1, M>)
makes the other three one-link functions a.e. constant, so g_p is a.e. constant and its Haar mean is 0: t_p o psi = t_p
a.e. whenever beta_p != 0; (5) an a.e. version of CEN+ (choose four triples (U_2, U_3, U_4) whose M span H; the M' then
span H, so psi_1 agrees a.e. with a linear map that is isometric on a dense subset of S^3, hence with some T in O(4);
then CEN+ applies to the continuous representatives). Non-invertible measure-preserving on-site maps are not
covered by this sketch.

## 6. Step 6: (vi) Lemma HW and (vii) Proposition LG (checked file L267-369), with test (d)

Context read and found correct on the way (not in W1's redo list): Lemma AUX (a)-(c) (integrate phi at fixed U);
Identity H2 (with V_l = phi_x^(-1) U_l phi_y = (U^g)_l for g_x = phi_x^(-1), N_kappa(U) = N_kappa(V) by gauge invariance, so
the (V, phi) density does not involve phi: phi is uniform and independent of V); Identity H3 (V -> k_x V k_y^(-1) is a
gauge transformation of V; Re(e^(theta a)(v_0 + v)) = cos(theta) v_0 - sin(theta) a . v with theta = f_x - f_y = - (df)_l).

### 6.1 Lemma HW: **HOLDS** ((i), (ii) with the mixed coefficient, (iii))

- (i) e^(F_x) V e^(-F_y) = V + F_x V - V F_y + (1/2) F_x^2 V + (1/2) V F_y^2 - F_x V F_y + O(F^3). First order: Re(F_x V) - Re(V F_y)
  = - F_x . s + F_y . s = - Delta F . s. Second order: - (1/2)(|F_x|^2 + |F_y|^2) t - Re(F_y F_x V), and Re(F_y F_x V) =
  - (F_x . F_y) t - (F_y x F_x) . s, so the total is - (1/2) |Delta F|^2 t - (F_x x F_y) . s. Correct. J(F) = - sum_l kappa_l
  Delta_l F . s_l is the first-order term, i.e. the derivative along phi_x -> phi_x e^(-eps F_x) (which sends V_l to
  e^(eps F_x) V_l e^(-eps F_y)). Correct.
- (ii) Translation step: in int exp(A(phi e^(-delta F) e^(-eps F'))) d phi_free substitute phi'_x = phi_x e^(-delta F_x) at free
  sites (right translation by a fixed element; F = 0 at pinned sites), which removes delta. So the mixed
  derivative vanishes: E[D_delta D_eps A] + E[J(F) J(F')] = 0. **Mixed coefficient, redone:** the delta eps terms of
  (1 + eps F'_x)(1 + delta F_x) V (1 - delta F_y)(1 - eps F'_y) are F'_x F_x V - F'_x V F_y - F_x V F'_y + V F_y F'_y (exactly the
  file's four). With Re(u v q) = - (u . v) t - (u x v) . s for imaginary u, v and cyclicity of Re:
  t-part: - F'_x . F_x - F_y . F'_y + F_y . F'_x + F'_y . F_x = - Delta F . Delta F';
  s-part: - F'_x x F_x - F_y x F'_y + F_y x F'_x + F'_y x F_x = F_x x (F'_x - F'_y) + F_y x (F'_x - F'_y) = (F_x + F_y) x Delta F'.
  So D_delta D_eps A = sum_l kappa_l [ - t_l Delta F . Delta F' + s_l . ((F_x + F_y) x Delta F') ], and (ii) follows with the
  signs as printed. Special cases: a perpendicular to c kills the contact term and leaves
  - E sum kappa_l (f_x + f_y)(g_x - g_y)(a x c) . s_l; a = c kills the bracket. Correct.
- (iii) With f extended arbitrarily to the free sites (the free-site rotation does not change N_pin, Haar), - log N_pin
  has second derivative - E[A''] - Var(A'); A'' = sum_l kappa_l [ - |Delta F|^2 t_l - 2 (F_x x F_y) . s_l ] with F = a f, so
  F_x x F_y = 0 and - E[A''] = E sum_l kappa_l t_l (df)_l^2; A' = J_a(f). Then H(f) <= sum_l kappa_l (df)_l^2 <= kappa sum_l (df)_l^2
  (|t_l| <= 1, Var >= 0), for every extension. Correct. The Remark identifying HW with OpenAI's (3.5)-(3.8) is a
  reading and is not checked.

### 6.2 Proposition LG: **HOLDS** (one cosmetic note); test (d): **YES** on both counts

- Bond form: Re(e^(-eta a) phi_x^(-1) U phi_y) = Re(phi_x^(-1) U phi_y e^(-eta a)) = <phi_x, U phi_y e^(-eta a)>, so T_l q = U_l q e^(-eta_l a),
  T_l = L_(U_l) R_(e^(-eta_l a)) in SO(4). Correct.
- **Moment rule on S^3:** with G standard Gaussian in R^4, G = |G| phi with |G| independent of phi, and
  E|G|^(2m) = 2^m Gamma(2 + m)/Gamma(2) = 2^m (m + 1)! = 4 . 6 ... (2m + 2). Wick for G divided by this gives
  E prod <phi, w_i> = c(m) sum over matchings prod <w_i, w_j>, c(m) = 1/(2^m (m + 1)!). Checks: c(1) = 1/4 (E phi_i phi_j =
  delta_ij/4); c(2) = 1/24, so E phi_1^4 = 3/24 = 1/8 = 3/(n(n + 2)) at n = 4. Correct.
- Expansion: the integrand is a product over links of exp(kappa <phi_x, T_l phi_y>); expanding and using independent
  uniform phi_x, the Gaussian picture gives, for each choice of n and of pairings pi at every site, products of
  traces of products of T_l (forward) and T_l^T (backward) along the closed walks traced by (n, pi), times prod c(m_x)
  and prod kappa^(n_l)/n_l!. Odd degree gives 0. Correct.
- **Test (d), commutation:** L_A R_B q = A q B = R_B L_A q by associativity. So along gamma the product is
  L_(U_gamma) R_(B_gamma), with B_gamma the product of the e^(-+ eta_l a) in reverse order; all of them have the one axis a,
  so they commute and B_gamma = e^(- eta(gamma) a), eta(gamma) the signed sum (+ forward, - backward; T_l^T = L_(U_l^(-1))
  R_(e^(+eta_l a))).
- **Trace 4 Re(U_gamma) cos(eta(gamma)):** sum over e in {1, i, j, k} of e-bar a e = 0 for imaginary a (the four
  half-turns about 0, i, j, k axes sum to zero), so sum_e e-bar A e = 4 Re A and tr(L_A R_B) = sum_e Re(e-bar A e B)
  = 4 Re A Re B; with Re e^(-theta a) = cos theta this is 4 t_gamma cos(eta(gamma)). It is also the character of
  (1/2, 1/2), (2 Re A)(2 Re B). Correct.
- **Test (d), sign of the twist:** cos is even, so the sign convention of eta(gamma) does not enter the trace;
  what matters is that forward and backward traversals enter with opposite signs, which the T_l^T rule gives.
  Consistency with H3: k_x = e^(f_x a) gives Re(k_x V k_y^(-1)) = Re(e^(- (df)_l a) V), i.e. eta = df in LG's convention, and
  then eta(gamma) = 0 on every closed walk, so N^(df) = N_kappa, as stated (also directly: phi_x -> phi_x e^(- f_x a) is a
  Haar-preserving change of variables). Correct.
- Non-negativity and the diamagnetic bound: the coefficients kappa^(n_l)/n_l!, c(m_x) and the 4's are >= 0, and
  |t_gamma cos(eta(gamma))| <= 1, so each term is bounded by its value at U = 1, eta = 0; those terms are >= 0 and sum to
  N_kappa(1) (Tonelli). N^eta > 0, so N^eta <= N_kappa(1). Correct.
- **Coefficients:** order kappa^2: one link with n_l = 2 (no multiple edges in a box or a torus of side >= 3):
  (kappa^2/2!) c(1)^2 . 4 = kappa^2/8 per link, total kappa^2 L/8. Correct. Order kappa^4: a plaquette with n_l = 1 on its
  four links and the unique pairing at each corner: kappa^4 c(1)^4 . 4 t_p cos((d eta)_p) = (kappa^4/64) t_p cos((d eta)_p),
  orientation-free (cos even, Re U = Re U^(-1)). Correct. The other order-4 terms (one link with n_l = 4; two doubled
  links) live on trees, where every closed walk has U_gamma = 1 and eta(gamma) = 0: free of U and of eta. Correct.
- Leading-order response (L353-355), **cosmetic:** "(kappa^4/64) E_YM[t_p] sum_p (d eta)_p^2" should read
  "(kappa^4/64) sum_p E_YM[t_p] (d eta)_p^2" unless E_YM[t_p] does not depend on p (torus). The derivation
  (N^(eps eta)/N_kappa = 1 + (kappa^4/64) sum_p t_p (cos(eps (d eta)_p) - 1) + O(kappa^6) on a finite lattice) is right.
