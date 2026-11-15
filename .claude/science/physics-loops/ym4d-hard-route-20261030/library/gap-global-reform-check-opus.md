lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-16T08:46Z

# Check of row 1016 (`library/gap-global-reform-max.md`), work item W1

Row 1020 of `FINISH.md` (queued 2026-11-15 20:45Z). Checker: Claude Opus 5.5, max effort, Mac mini worker,
session started 2026-11-15T20:46Z (by `date -u`). Same provider as the checked row (Claude Fable 5.2), so this is not an
independent cross-provider check. Pinned at commit 0d3b45d91. No commit, no push, no claim.

## Status log

- 2026-11-15T20:46Z: file created; plan below is provisional until W1 of the checked file (L1004 and following) is read.
- 20:48Z: steps 1-2 done (inputs read; tests (a), (b); Identity AV; Theorem BH Steps 1-5): all HOLD.

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
