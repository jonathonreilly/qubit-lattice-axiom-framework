# Direct weighted comparison at the flat background, and what DS really reads of FALL

Written 2026-11-02 by anthropic/claude-opus-5-5/high, Mac mini worker, at c16e2a968, as the repair section of `gates/shell-end-c16e2a968.md`. Mapped side. Same-model, not gated. Nothing here is consumed yet. Inputs keep their own labels: Lemma TP-sharp at U = 1 and the bumps of Theorem 6 are in `fibre-propagator.md` and `block-poincare-energy-package.md`, written by the same provider and not gated. The notation is that of `excess-shell-end.md`.

State of attack: Sections 1 to 4 are written hand proofs, each conditional only on the inputs named. Section 5 is a programme, labelled gap, and proves nothing.

## 1. Lemma Q: the first order in the rate is absent for every linear model

**Lemma Q (proved).** *Let R be an orthogonal projection on a real or complex Hilbert space, W bounded, positive, with bounded inverse, P := W^(1/2) R W^(-1/2), J := P - R, j := ||J||. Then ||P||^2 <= 1 + 4 j^2 + 2 j^4.*

*Proof.* P^2 = P gives R J + J R + J^2 = J. Put R' := 1 - R. Multiplying by R on both sides gives R J R = -R J^2 R. Multiplying by R' on both sides gives R' J R' = R' J^2 R'. So the two diagonal blocks of J have norm at most j^2, and the off-diagonal blocks at most j. For a unit vector u = a + b, a in Ran R, b in Ran R', with alpha := |a|, beta := |b|: |R P u| <= (1 + j^2) alpha + j beta and |R' P u| <= j alpha + j^2 beta. So |P u|^2 is at most the quadratic form of [[1 + 3 j^2 + j^4, j + 2 j^3], [j + 2 j^3, j^2 + j^4]] at (alpha, beta). That matrix has trace 1 + 4 j^2 + 2 j^4 and determinant j^8 >= 0, so its top eigenvalue is at most the trace. QED

**Consequence.** sup over trials of the ratio in a quadratic model is ||W^(1/2) R W^(-1/2)||^2. When j <= D nu it is 1 + O(nu^2). So (WAM-slab) improves from 1 + D_lin nu to 1 + O(nu^2), and a test that finds 1 + O(nu^2) learns nothing but that j is finite.

## 2. Weighted fibre Poincare

Setting of `fibre-propagator.md`, U = 1, level-n units, fine spacing eta. Q^o has rows rho_c, probability weights of support diameter at most 5 and overlap at most 2 in each component (Lemma 1 of the package). F Y := sum_c Y(c) psi_c is the right inverse by the bumps of Theorem 6, Q^o F = 1, and psi_c decays at an absolute exponential rate kappa > 0 away from c, so, for g Lipschitz with constant at most kappa/2,

    ||e^g F Y||_Eps <= C ( sum_c e^(2 g(c)) |Y(c)|^2 )^(1/2).                  (F-W)

(F-W) is Schur's test on the bumps. It reads only that the Gram matrix of the rows is finite band with uniform Riesz bound, as Theorem 6 says.

**Lemma WP (implication of TP-sharp at U = 1).** *There are absolute C_1, delta_1 > 0 such that if f is Lipschitz with constant delta <= delta_1 in level-n units, Q^o H = 0 and P_r D^* H = 0, then ||e^f H||_Eps <= C_1 ||e^f d H||.*

*Proof.* Let H_f := e^f H, with f at bond midpoints, and v := Q^o H_f. As Q^o H = 0, v(c) = <rho_c, (e^f - e^(f(c))) H>. So |v(c)|^2 <= C delta^2 <rho_c, |H_f|^2>, and ||v|| <= C delta ||H_f||. Put H^ := H_f - F v, so Q^o H^ = 0, and TP-sharp gives ||H^||_Eps^2 <= C_# ( ||d H^||^2 + ||P_r D^* H^||^2 ). Three pieces.

- ||d H^|| <= ||e^f d H|| + C delta ||H_f|| + C ||v||, since d has a factor 1/eta and f moves by at most delta eta along a bond.
- D^* H_f = e^f phi + E_1, with phi := D^* H and |E_1| <= C delta |H_f|.
- P_r (e^f phi) = e^f P_r phi + [P_r, e^f] phi = [P_r, e^f] phi, and P_r = 1 - r^* r is diagonal over blocks of diameter at most 4, so ||[P_r, e^f] phi|| <= C delta ||e^f phi||. Also ||e^f phi|| <= C ||H_f||_Eps.

So ||P_r D^* H^|| <= C delta ||H_f||_Eps. Then ||H_f||_Eps <= ||H^||_Eps + ||F v||_Eps <= C_#^(1/2) ||e^f d H|| + C delta ||H_f||_Eps. Absorb for delta small. QED

## 3. Theorem WAM-lin, and the flat (LC)

**Theorem WAM-lin (implication of Lemma WP and (F-W)).** *There are absolute C_2, delta_2 > 0 such that for every depth, every volume and every block side L^n: if A_* minimizes ||d A||^2 in a fibre of Q^o, A_t is in the same fibre, and w = e^(2 f) with f Lipschitz with constant delta <= delta_2 in top units, then*

    ||d A_*||_w^2 <= (1 - C_2^2 delta^2)^-1 ||d A_t||_w^2.                     (WAM-lin)

*So (WAM) holds in this model with coefficient O(nu^2), at an absolute rate, free of L, depth and volume. No cut-off, no seam and no absorption of a shell appear.*

*Proof.* H_0 := A_t - A_* is in ker Q^o. There is omega in ker r with H := H_0 - D omega satisfying P_r D^* H = 0, as P_r (-Delta) P_r is positive on ker r (Corollary (H1) of `fibre-propagator.md`), and D omega is in ker Q^o by (Cov). d H = d H_0. Minimality gives <d A_*, d G> = 0 for all G in ker Q^o. Write

    ||d A_t||_w^2 = ||d A_*||_w^2 + 2 <d A_*, w d H> + ||d H||_w^2.

Put E := d(w H) - w d H, so |E(p)| <= C delta w(p) sum_(b in boundary p) |H_b|. Take G := w H - F Q^o(w H), in ker Q^o. Then

    <d A_*, w d H> = <d A_*, d F Q^o(w H)> - <d A_*, E>.

As Q^o H = 0, Q^o(w H)(c) = <rho_c, (w - w(c)) H>, so sum_c w(c)^-1 |Q^o(w H)(c)|^2 <= C delta^2 ||H||_w^2. By (F-W) with g = -f, ||w^(-1/2) d F Q^o(w H)|| <= C delta ||H||_w. Also ||w^(-1/2) E|| <= C delta ||H||_w. So by Lemma WP, |<d A_*, w d H>| <= C_2 delta ||d A_*||_w ||d H||_w. Then ||d A_t||_w^2 >= a^2 - 2 C_2 delta a b + b^2 >= (1 - C_2^2 delta^2) a^2, with a := ||d A_*||_w, b := ||d H||_w. QED

*Where closure enters.* The trial is d A_t, and that is used: H is a connection. The sup over non-closed 2-forms is a different quantity and it grows with the volume, as `checks/gate_se` shows (K3). That is the Hodge tail of the projector, which no closed trial sees.

**Corollary LC-flat (implication of the same).** *Let chi be a cut-off with Lipschitz constant 2/r, r >= 2, with nabla chi supported in S := S_r(D). Then, for the corrector F, the remainder of (SEAM) obeys*

    ||R_chi||^2 <= C r^-2 sum_p exp(-2 delta_1 d(p, S)) ( |d A_*(p)|^2 + |d A_t(p)|^2 ),

*with C absolute. So (LC) holds at the trivial field with C_seam absolute, r = 2, K an exponential kernel of absolute rate, and (E-SHELL) follows in this model with A_s, r, M_* absolute and free of L.*

*Proof.* Use the representative H of the theorem. Then R_chi = [d, chi] H - d F [Q^o, chi] H, and both terms are at most C/r times |H| on S, the second with the tails of (F-W). Apply Lemma WP with f := -delta_1 d(., S), which is 0 on S. For the kernel: if x is in S_r(D), then B_r(x) holds an adjacent pair a in D, b outside D, and B_(r-1)(a) lies in S_r(D). So S has fixed volume near each of its points, and exp(-2 delta_1 d(p, S)) <= C K * 1_S(p) for K proportional to exp(-delta_1 d). QED

So in the flat linear model the rate condition b_s nu_* <= 1/2 is a condition on absolute constants, and nu is chosen before L with room for it. This is a statement about the linear flat model only.

## 4. Lemma DOM: DS needs no FALL at its own rate

Sampling in physical coordinates makes the following a line, and it is the answer to the rate question.

**Lemma DOM (proved, given (FALL) at rate nu_s).** *Let 0 < nu_s <= nu_req, and suppose (FALL) holds for every top profile of rate at most nu_s, with constants q, C_F. Let V be in D_k^+ with flux at most T at every top cell, and W_y(x) := e^(-nu_req d(x, y))/C_nu_req. Then, for all y, with W_y^+ the fixed enlargement read by DS,*

    sum_(m' >= m) I^grad_(k-m')(Lambda_(m') V; W_y^+) <= C(L, nu_s) q^m ( T^2 + Phi(e^-8 N_k/4) ).

*Proof.* W_y^+ <= C W_(s,y) pointwise at every level, with W_(s,y)(x) := e^(-nu_s d(x, y)), as nu_s <= nu_req and both are sampled at the same physical point. Weighted sums are monotone in the weight. Apply (FALL) at W_(s,y). Its bracket is at most C nu_s^-4 (T^2 + the toron term), since E_k(V; W_(s,y)) <= T^2 sum_c W_(s,y)(c), and I_k is at most C_g E_k plus a cubic. QED

**What reads this form.** The readers of (FALL) outside FALL itself, all at this commit:

| Reader | What it uses | Enough? |
|---|---|---|
| Prop DS, values | I_k, E_k at V_t on W_y at most C T_2^2; line 218 of `sector-values.md` | yes |
| Prop DS, order 1 | I_(k-m)(Lambda_m V_t; W_y^+) <= C q^m T_2^2. The decay in y comes from || d_t F^rad ||, by Lemma CRUDE at nu_req | yes |
| Prop DS, order 2 | order 1 and CRUDE | yes |
| (Loc^c) direct | Prop DS only | yes |
| Lemma COMP-B | a_m(V_t; W) <= C q^m T_2^2 | yes |
| Prop GS in Theorem VAL | W = 1, rate 0 | no rate needed; (WAM) is the unweighted comparison there |
| Prop GS in the region clause, Section 6 | W_0, a cut-off to the free cells, rate about 1/r_S | **no**: W_0 is a real cut-off and a slower profile leaves the free cells |

Thus, with nu_s = nu_s(L) inserted in the order of constants just before q(L), every C(L) in DS and COMP-B stays a C(L), paid at x_*. Rates and absolute constants before L do not move: delta'' = min(delta', nu_req) and mu are read off CRUDE and SRC, not off (FALL)'s rate. The region clause keeps a condition, and it can be met by raising r_S: r_S comes after L, so r_S >= C b_s(L) can be added to its maximum, at the cost of a larger t_0. That has not been checked against the budgets t_0 feeds.

A finite A_s(L), r(L), M_*(L) at any one rate then suffices for DS, since b_s(s) s <= 1/2 holds for s small. This does not say that (FALL) holds at nu_req, and it does not prove (E-SHELL).

**Sharpness of the absorption.** (E-SHELL) alone cannot give (WAM) above about 1/(2 r A_s). Abstract scalar profiles on Z, with M_* = 1: a_T := delta_0, a_U(x) := c e^(-lambda |x|) with total at most 1, w := e^(nu x). The superlevel sets are half-lines, and (E-SHELL) holds for them with A_s := max(1, 1/(2 sinh(lambda r))): for R >= r the shell [R - r, R + r) carries at least 2 sinh(lambda r) times the mass of [R, oo) under a_U, for 0 < R < r the shell holds the unit atom, and for R <= 0 the left side is at most 0. But A_U(w) diverges with the volume at nu >= lambda, while A_T(w) = 1. The note's condition is sinh(nu r) <= 1/(4 A_s), so it is sharp within a factor 2. This is about the implication, not about Yang-Mills.

## 5. Nonlinear (WAM) by the same identity: gap, a programme only

(UP) needs less than (WAM): A_U(w) <= [1 + D (nu_l + f_l)] A_T(w) + D tau_l is enough, by the same lines as (UP-constants), since (UP) already pays (f_l + nu_l) E_l.

Candidate, unproved. Let T be the iterated trial, for which TR-SLOW holds. Suppose U = e^(i eta H) T in the gauge P_r D_T^* H = 0, with sup over boxes of ||H||_Eps(box) <= r_0. Put g(s) := A(e^(i s eta H) T; w), so g(0) = A_T(w) and g(1) = A_U(w). The path need not lie in the fibre, and no chart of the fibre is used. Then g(0) = g(1) - g'(1) + integral_0^1 s g''(s) ds. U's stationarity, tested on G := w H - F_U Q_U^o(w H), gives

    |g'(1)| <= C (delta + eps) ||theta_U||_w ||H||_(Eps,w),

and the second-order term is at least (1 - eps) ||d_U H||_w^2, provided that:

- (N1) H exists around T with r_0 small at every partial top. This is (R2) with base T in place of the one-shot U^tr, which needs T to satisfy R(a).
- (N2) Lemma WP at the background: Lemma TP-sharp at a background, read with a weight, as above.
- (N3) N(T) = N(U) gives Q_U^o H = O(H, H) with ||Q_U^o H||_(l^2, w) <= eps ||H||_(Eps, w), eps = C(L) r_0, uniformly in depth. **This is the first place to attack**: it reads D^2 N of the composite on nested contours, with `fibre-propagator.md`, hostile (6'), in view.
- (N4) a weighted form of (Size) along the segment.

If these hold, A_U(w) <= [1 + C (nu^2 + eps^2)] A_T(w), which is more than (UP) needs when r_0 <= C(L) f_l. Compared with (NF-W) of `excess-weighted-fibre-stop.md`, this asks for no inverse A_U^-1, no chart with endpoint coverage and no secant bound in operator norm, only the single secant vector H. Compared with (GLUE-E), it asks for no gluing, so no patch and no class check of a glued field. Nothing here shows that (N1) to (N4) hold.
