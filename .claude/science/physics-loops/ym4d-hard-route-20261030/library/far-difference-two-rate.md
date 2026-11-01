# Far differences across sectors at an absolute rate: the two-rate weight

Own derivation, 2026-11-01, pinned at 23eddd87f, for queue item 8d `rc-far`. Not reviewed. Same model as the mapped attempt's author, so not independent and not an audit. Part: `hard-core--mapped`. The covariance formula is Helffer and Sjostrand's, the commutation Bakry and Emery's, the exponential conjugation Combes and Thomas's, and block averages and minimal fields are Balaban's. Lemma W and Lemma FAR are new here as far as I know; I have not searched for them. This line is not independent of the Sussman-Alpoge repository, which supplied the map; this note does not read it. Nothing here reads the sibling attempt.

Status, by part. Lemma W: proved, elementary. Lemma FAR: proved given the hypotheses it names, on top of Lemmas HS-P, HS-M, HS-C of `library/preconditioned-covariance.md`. Lemma CL: level of each term at order one; higher orders by the same recursion, not displayed. Prop LF: level of each term. Theorem RC: implication from H(k) of `library/one-step-closure.md` with (Loc^c) replaced by (Loc^f). All rest on Theorem F, Prop AN3, (H1)-(H3) and the cut at their own labels, none gated at those labels by me.

## 0. The obstacle this removes

Lemma O2 of `library/sector-values.md` compares two parents V', V'' equal on a ball by S_t := (1 - t) S_{V'} + t S_{V''}, with no path of fields, so sectors do not matter. Its hostile point (13) records the price: Theorem F gives an absolute rate for each of the two Hessians, not for their convex combination, so O2, the tail of O3 and (Loc^c_k) are read at a Combes-Thomas rate mu_c(L) that falls with L. Point (13) lists the readers and finds that none needs the absolute rate.

(RC-far) does. In `library/current-locality-reduced-law.md` a tier of rate below kappa must have amplitude <= C zeta_(j+1). A difference of D R_k at the rate mu_c(L), read through g in the action, has amplitude g C(L), which is a power of g. Unless L mu_c(L) >= 2 kappa, it is exactly the slow tail that note's rate test excludes. So the route Lemma O2 -> (Loc^c) -> a covariance in S_t does not deliver RC-far as written.

The repair rests on one observation. To read a far difference at o across Q_n(o), the combination S_t needs the fast rate only **inside** Q_n(o), where its Hessian is close to that of one field. Outside, a slow rate is enough, since it is used only to kill the volume.

## 1. Lemma W (the inverse of a convex combination, with a two-rate weight)

*Setting.* I a finite set with a metric d, of polynomial growth with a fixed degree (box distance). M_1, M_2 symmetric on R^I with, for a = 1, 2:

- (a) gamma <= M_a <= Gamma, and |M_a(i, j)| <= C_0 e^{-mu_1 d(i, j)};
- (b) |M_1^-1(i, j)| <= C_A e^{-delta d(i, j)};
- (c) r: I -> [0, infinity) is 1-Lipschitz, and |M_1(i, j) - M_2(i, j)| <= C_E e^{-delta_E max(r(i), r(j))}.

Nothing is asked of M_2^-1. Put M_t := (1 - t) M_1 + t M_2, A_t := M_t^-1, m := min(delta, delta_E). Let mu_c > 0, mu_c <= delta, be a Combes-Thomas rate for (a): |A_t(i, j)| <= C_c e^{-mu_c d(i, j)}, for all t. Let S be a subset of I, R := min_S r. Since r is 1-Lipschitz, r(i) + d(i, S) >= R for all i. Let rho <= m/4, rho_c <= min(rho, mu_c/8), and

    f(i) := rho min(d(i, S), R) + rho_c (d(i, S) - R)_+.

*Conclusion.* ||e^f A_t e^-f||_(l^2 -> l^2) <= C_W, and the same with -f, with C_W depending on C_0, C_A, C_E, C_c, gamma, mu_1, mu_c, delta, delta_E and the growth, and **not on R or on the size of I.**

*Proof.* Let E := M_t - M_1, so |E| <= |M_2 - M_1| entrywise. The resolvent identity A_t = A_1 - A_t E A_1 gives

    |A_t(i, j) - A_1(i, j)| <= gamma^-1 || E A_1 e_j ||_2 <= gamma^-1 || E A_1 e_j ||_1.

Interpolate (a) and (c), weight 1/4 on (a): |E(i, k)| <= C e^{-(mu_1/4) d(i, k)} e^{-(3/4) delta_E r(k)}. So sum_i |E(i, k)| <= C e^{-(3/4) m r(k)}. With (b), and r(k) + d(k, j) >= r(j),

    || E A_1 e_j ||_1 <= C sum_k e^{-(3/4) m (r(k) + d(k, j))} e^{-(m/4) d(k, j)} <= C e^{-(3/4) m r(j)}.

By symmetry of A_t, A_1: |A_t(i, j) - A_1(i, j)| <= C e^{-(3/4) m max(r(i), r(j))}. Also |A_t - A_1|(i, j) <= (C_c + C_A) e^{-mu_c d(i, j)}. Take the geometric mean with weights 3/4, 1/4:

    |A_t(i, j)| <= C_A e^{-delta d(i, j)} + C e^{-(9/16) m max(r(i), r(j))} e^{-(mu_c/4) d(i, j)}.

Now the increment of f. It is at most rho d(i, j) always. Claim: f(i) - f(j) <= rho max(r(i), r(j)) + rho_c d(i, j). If d(i, S), d(j, S) >= R it is at most rho_c d(i, j). If d(i, S) >= R > d(j, S): f(i) - f(j) = rho (R - d(j, S)) + rho_c (d(i, S) - R) <= rho r(j) + rho_c d(i, j). If both are below R: f(i) - f(j) <= rho (R - d(j, S)) <= rho r(j). If d(i, S) < R <= d(j, S) the increment is at most 0. So

    e^{f(i) - f(j)} |A_t(i, j)| <= C_A e^{-(3/4) delta d(i, j)} + C e^{-(5/16) m max(r(i), r(j))} e^{-(mu_c/8) d(i, j)}.

Schur's test on each term gives C_W, with no dependence on R or I. The sign -f is the transpose, since A_t is symmetric. QED

*What it does not say.* M_t may have a slow region outside the set r > 0, and the weight rate falls to rho_c there. I do not know whether a single rate rho holds for the actual pairs of chart Hessians: Lemma W only avoids asking. No run here shows that a single rate fails (controls below).

## 2. Lemma FAR (a covariance across a cube, with cut and tiers)

*Setting.* Level k, W_1, W_2 in D_{k+1} agreeing on a cube P of parent cells, I the free coordinates of Text 5.1 (common to both, as the trees and designated bonds are geometric), d the box distance, r(i) the box distance to the complement of P. K := prod_c K_c, Psi the soft barrier of the cut, independent of W. S_a := S(.; W_a) := x_k [A_k(Phi(W_a, g xi)) - A_{k+1}(W_a)] + R_k(Phi(W_a, g xi)) - log J. M_a := D_xi^2 of the first term at 0. V_a(xi) := D^2 S_a(xi) - M_a, split V_a = V_{a,f} + V_{a,s} by kernel support at tree length y_*, as in Lemma HS-C. S_t, M_t, V_t := convex combinations, mu_t proportional to e^{-S_t - Psi} on K. D := S_2 - S_1. Then

    d/dt E_t[T] = -Cov_t(T, D),    so    (E_2 - E_1)[T] = -int_0^1 Cov_t(T, D) dt.        (INT)

This is exact and reads no path of fields. D is bounded on K, so differentiation is justified.

*Hypotheses.* (F1) (a), (b) of Lemma W: (H1), (H2) in the chart, Theorem F at V^*(W_1). (F2) (c) of Lemma W with delta_E := delta_#/2: Lemma CL below. (F3) For every weight h with Lipschitz constant at most delta_#/8 per box, sup_K ||e^h V_{t,f} e^-h|| <= eps_V, eps_V <= C(L) (tau + g^2): `library/preconditioned-covariance.md`, *(V), and (A) of HS-P*, whose bound is convex in the action. (F4) The slow weight: (W), (V) of HS-M for M_t, Theta_s := e^{rho_s d(., S)}. (W) is linear in M: applying it to each of M_1, M_2 and Cauchy-Schwarz in t gives it for M_t, with the same eps_1, and likewise the form bound zeta_V for V_{t,s}. (F5) The moments (M) and the barrier: sup_c E_t ||B_c|| =: zeta_c <= poly(x) z. Both hold uniformly in t, as the proofs read only the gap and D S(0).

**Order of constants, one change.** Put C_W(L) of Lemma W for rho := delta_#/8. Then tau and x_* must also satisfy C_W(L) eps_V <= 1/4. C_W comes after L and before tau, since M_1, M_2 do not involve the cut. So tau carries one more function of L. Nothing else moves.

**Lemma FAR.** Let T be C^1 on K, S a set of boxes, R := dist(S, P^c) >= 1, f the weight of Lemma W with rho = delta_#/8, and write, with t fixed,

    e_f := || e^f D T ||_(L^2(mu_t; l^2)),   e_s := || Theta_s D T ||_(L^2(mu_t; l^2)),
    eps_2(b)^2 := E_t |d_b D|^2,   eps_inf(b) := sup_K |d_b D|,   A(h)^2 := sum_b e^{-2 h(b)} eps(b)^2.

Then

    |Cov_t(T, D)| <= 4 C_W A_2(f) e_f + C(L) ( zeta_c^{1/2} + zeta_V ) [ sum_c e^{-2 rho_s d(c, S)} Y_c^2 ]^{1/2} e_s,

with Y_c := C(L) A_inf(f_c), f_c the weight of Lemma W with S replaced by the box of c, R by r(c).

*Proof.* As HS-M: with u solving L_A u = T - mu(T) for A := A_t, and w := A D u, one has Cov(T, D) = E[(D D)^T w] and L_A w + w + A V_f w + A V_s w + A B w = A D T. Let G := (L_A + 1 + A V_f)^-1. By Lemma W and (F3), ||e^f A V_f e^-f|| <= 1/2 for f and each f_c, and, since L_A is non-negative on L^2(mu) and sub-Markov on the pointwise norm, G is bounded by 2 on L^2(mu; l^2) and on L^infinity(mu; l^2) in those weights, as in HS-C. So

    Cov(T, D) = E[ (D D)^T G A D T ] - E[ Y^T V_s w ] - E[ Y^T B w ],    Y := A G^* D D.

First term: at most ||e^-f D D|| 2 C_W ||e^f D T||. For the other two: |Y_c| <= ||e^{-f_c} Y||_(l^2), since f_c vanishes at c, and ||e^{-f_c} A G^* e^{f_c}|| <= 2 C_W on L^infinity(mu; l^2), so sup_K |Y_c| <= Y_c as defined. For the barrier term use Cauchy-Schwarz over cells with theta_c := e^{rho_s d(c, S)}, constant on cells: its square is at most (sum_c theta_c^-2 sup_K |Y_c|^2 E ||B_c||) (sum_c theta_c^2 E w_c^T B_c w_c), and the second factor is at most 4 ||Theta_s D T||^2_(L^2(M^-1)), by Term 4 of HS-M. The term in V_s is the same with zeta_V. QED

*The volume.* It does not enter. D has gradient of order one at every far bond, and A(f) is finite because f keeps growing beyond R at the slow rate rho_c. Use: if eps(b) <= C_e e^{-delta_e r(b)} with delta_e >= delta_#/8, then, as d(b, S) + r(b) >= R,

    A(f)^2 <= C_e^2 C(L) (1 + R)^4 e^{-(delta_#/4) R} + C_e^2 C(L) rho_c^-4 (1 + R)^3 e^{-(delta_#/4) R},        (VOL)

with the same at slow rates. And sum_c e^{-2 rho_s d(c, S)} Y_c^2 <= poly(x) C(L) (1 + R)^8 e^{-2 rho_s R}, for rho_s <= delta_#/8.

## 3. Lemma CL (classical locality in every sector)

Notation. V_a := V^*(W_a), in the tree gauge of each box, with W_1 = W_2 on P. r(y), for a level-k bond y, is the box distance from its parent to P^c. Recall from `library/sector-values.md`, Section 1, that V_a is the unique class minimiser on the fibre, and its flux is at most C_r L^-1 T_2. Since a tree-gauge angle in a box is a sum of at most C L^2 plaquette angles, and a crossing bond is within the same of its parent, |log V_2 V_1^-1| <= a_0 := C L T_2 on boxes of P.

(P_k) For V, V'' in D_k equal on a set Y of level-k cells, y in Y, r_k(y) := dist(y, Y^c): |D A_k(V)[y] - D A_k(V'')[y]| <= D_k T_2 e^{-(delta_#/2) r_k(y)}. The same for the energy densities a_{k,c}, rooted at c, summed over b with a tail in d(b, c).

**Lemma CL.** *There are C(L), free of k and the volume, with: (a) |log V_2 V_1^-1 (y)| <= C(L) T_2 e^{-(delta_#/2) r(y)}; (b) sup_k D_k <= C(L); (c) for free coordinates i, j, and the same xi in the two charts, with Phi(W_a, g xi) class, the classical Hessians in the chart differ by at most C(L) T_2 e^{-(delta_#/2) max(r(i), r(j))}, and the Taylor coefficients of a_c o Phi at 0 to order two differ by at most C(L) T_2 e^{-(delta_#/2) r(c)}, with x-free normalisation.*

*Proof, by induction on k.* (P_0): A_0 is the Wilson action, strictly local, so D_0 = 0.

*Hybrid.* Let chi be 1 on boxes with r >= C_0 + 1 and 0 on boxes with r <= 1, with Lipschitz constant 1/(C_0 L) per level-k cell, C_0 absolute, so that (grad chi) a_0 <= T_2/4. Let P_h be the field on the fibre of W_1 with relative field chi log(V_2 V_1^-1) to V_1, the constraint restored by a bump of height at most C T_2 on each box, not by the designated bond, whose spike would leave the class. Flux of P_h is at most T_2, by the flux bound on V_a. P_h = V_2 on boxes with r >= C_0 + 2 and P_h = V_1 off P. Let xi_h be its free coordinates in the chart of W_1 at V_1, unscaled. On the segment s xi_h the designated part is linear in xi_h, so the segment stays in the class up to second order, and A_k is uniformly convex along it for a_* <= a_th(L).

*(a).* Let g(xi) := D_xi (A_k o Phi(W_1, .))(xi). By criticality g(0) = 0, so g(xi_h) = Mbar xi_h, Mbar := int_0^1 D^2 (s xi_h) ds = M_1 + dM, with dM of size C(L) T_2 and tree decay, by Prop AN3. So e^f Mbar^-1 e^-f is bounded for f Lipschitz at rate 3 delta_#/4, by Theorem F and a Neumann series, for a_* small. For y with r(y) >= C_0 + 3: Phi(W_1, xi_h) = P_h = V_2 near y, and the chart direction of y at P_h is that of W_2 at V_2, so D A_k(V_2) annihilates it, by criticality on the fibre of W_2. Hence g(xi_h)(y) = (D A_k(P_h) - D A_k(V_2))[d_y Phi], which by (P_k) is at most C(L) D_k T_2 e^{-(delta_#/2) L (r(y) - C_0 - 2)}. For smaller r(y), and off P, |g(xi_h)(y)| <= C(L) a_0 with tail. Take the minimum of the two bounds: g(xi_h)(y) is at most C(L) a_0 for r(y) <= r_2 and decays at rate delta_# L / 2 beyond, r_2 := C_0 + 2 + (log (D_k / C(L)))_+ / (delta_# L / 2). Then xi_h = Mbar^-1 g(xi_h) gives (a) with constant E_k := C(L) a_0 / T_2 times e^{(3 delta_#/4) r_2}, that is at most C'(L) (1 + D_k)^{2/L}.

*(b), (P_{k+1}).* Let W_1, W_2 be equal on Y', y' in Y', r := r_{k+1}(y'). Since D A_k(V_a) annihilates the fibre, D A_{k+1}(W_a)[y'] = D A_k(V_a)[X_a], X_a any local direction over y': the multiplier identity D_Y A_n = lambda. Take X_a on the block of y', with ||X_a||_(l^1) <= C(L). Fix a hybrid at depth r/3: P_y := e^{i chi_y log(V_2 V_1^-1)} V_1, chi_y a cut-off on the ball of radius 2 r/3 about y' and equal to 1 on radius r/3. By (a) its relative field is at most E_k T_2 e^{-(delta_#/6) r} at the transition, so it is class and on a class path from V_1, and D A_k(V_1)[y] - D A_k(P_y)[y] <= C(L) E_k T_2 e^{-(delta_#/2) r}, reading the relative field at y' with the tail of D^2 A_k at rate delta_# per level-k cell, which covers the transition. And (P_k) on the ball: |D A_k(P_y)[y] - D A_k(V_2)[y]| <= D_k T_2 e^{-(delta_#/2) L r/3}. So

    D_{k+1} e^{-(delta_#/2) r} <= C(L) D_k e^{-(delta_#/6) L r} + C(L) E_k e^{-(delta_#/2) r} + C(L) e^{-(delta_#/2) r}.

For r >= r_min, with C(L) e^{-(delta_#/6)(L - 3) r_min} <= 1/2, the first term is at most (1/2) D_k. Below r_min use the trivial bound, 2 sup |D A_{k+1}| <= C T_2. So D_{k+1} <= D_k / 2 + C''(L) (1 + D_k)^{2/L} + C''(L), and sup_k D_k is finite, free of k.

*Higher orders.* D^2 A_{k+1} reads D V^*, and the difference K_1 - K_2 of the two lifts is X_1 - X_2 - T (A_1 - A_2) T^T D^2 A_k [X], with A_1 - A_2 = A_1 (M_2 - M_1) A_2, in which each of A_1, A_2 has the fast rate by Theorem F, at its own field, so no Lemma W is needed here. So (c) follows by the same two moves, hybrid at depth r/3 and the class path on the near part, at each order up to five, with Prop AN3 for the sizes. Not displayed. The energy density: a_{k+1,c'} = sum_{c in B(c')} a_{k,c} o V^*, and D a_{k,c} sums over the block with a constant C(L) only, by AN2(a) and (2) of Prop AN3: |D_b a_c| <= 2 ||F||_(L^2(c)) ||H_b||_(Eps(c)), free of the level. That line is what (CF_j)(d) needs for a_c. Consequence 3 of `library/analytic-lift.md` states it for A_n only. QED at this level.

*Why Theorem F-D is not read.* `library/sector-values.md`, Section 5, says "by Theorem F-D on the ball with parents equal". The argument above reads only the torus form at V_1, through Mbar^-1.

## 4. Prop LF: (Loc^c) at an absolute rate

Replace (Loc^c_k), order one, by

    (Loc^f_k)   for V_1, V_2 in D_k^+ equal on Y, y in Y:  |D R_k(V_1)[y] - D R_k(V_2)[y]| <= D^R Phi^l_k(r_k(y)),
                Phi^l_k(r) := e^{-mu_l r} + zeta_k e^{-mu_s r},   mu_l := delta_#/16,   mu_s := min(rho_s, mu_c)/8,

with zeta_k as in `library/one-step-closure.md`, Section 1, and rates per cell of level k. The first tier is absolute.

**Prop LF (level of each term).** *H(k) with (Loc^f_j) for j <= k implies (Loc^f_{k+1}), with D^R free of k, for x_* large.*

*Proof.* R_0 = 0. Let W_1, W_2 in D_{k+1}^+ be equal on Y', y' in Y', r := r_{k+1}(y'). R_{k+1} = beta_{k+1} A_{k+1} + G_k - W^gas_k - (vac), G_k := -log of the base integral. So D_{y'} R_{k+1}(W) = beta_{k+1} D_{y'} A_{k+1}(W) + E_W[T_W] - D_{y'} W^gas(W), T_W := D_{y'} S(.; W) at fixed xi.

*(i) beta.* Lemma CL, |beta| <= C(L).

*(ii) Gas.* The clause of Lemma O2 for the gas at the rate mu_c(L), amplitude x^M z: activities of near polymers agree up to the tail, and far polymers contribute by tree graphs. **Read at its label, unchecked here.** It goes in the second tier: x^M z <= zeta_k.

*(iii) Base.* E_1 T_1 - E_2 T_2 = E_1 [T_1 - T_2] + (E_1 - E_2) T_2. Write T_W = T^cl_W + T^R_W - D_{y'} log J. T^cl_W := x_k D_{y'}[A_k(Phi(W, g xi)) - A_{k+1}(W)] vanishes at xi = 0 and has no term linear in xi, since D_xi (A_k o Phi)(0; W) = 0 for every W. So T^cl_W = (1/2) <xi, D_{y'} M_W xi> + O(g), no factor x, and Lemma CL at order three gives |T^cl_1 - T^cl_2| <= C(L) e^{-(delta_#/2) r} (1 + Omega^3), Omega the local field of Step 1 of `library/convex-laplace-tree-decay.md`. log J is local. For T^R: T^R_W = D R_k(Phi_W)[K_W], K_W := D_{y'} Phi_W. For each xi let P_y be the hybrid at depth r/3 between Phi_1, Phi_2, in D_k^+ as flux grows by a tiny amount. So

    |T^R_1 - T^R_2| <= sum_y |D R_k(Phi_1)[y] - D R_k(P_y)[y]| |K_1(y)| + sum_y |D R_k(P_y)[y] - D R_k(Phi_2)[y]| |K_1(y)| + B_1 ||K_1 - K_2||_(l^1).

The first sum reads ||R_k||_2 and Lemma CL(a): at most C(L) B_2 (1 + Omega) e^{-(delta_#/2) r}, in the first tier, and with zeta_k e^{-mu_s L r/C} in the second. The third reads Lemma CL. The second reads (Loc^f_k) at distance L r/3, with sum_y |K(y, y')| e^{mu d} <= C_1 L^3: at most C_1 L^3 D^R Phi^l_k(L r/3).

For (E_1 - E_2) T_2: (INT), Lemma FAR with S := the box of y', R = r, e_f, e_s <= C(L), by (H2), (H3) for mixed derivatives. And d_b D = classical part + g [D R_k(Phi_2)[d_b Phi_2] - D R_k(Phi_1)[d_b Phi_1]] + log J part. The classical part vanishes at xi = 0, for both charts, so it is at most C(L) e^{-(delta_#/2) r(b)} (1 + Omega(b)) on P by Lemma CL(c), and at most C(L) (1 + Omega(b)) off P. No factor x. The R part: as for T^R, with a factor g. So (VOL) gives

    |Cov_t(T_2, D)| <= C(L) (1 + r)^4 [ e^{-(delta_#/8) r} (1 + g D^R) + (poly(x) z^{1/2} + zeta_V + g D^R zeta_k) e^{-mu_s r} ].

*Closure.* With mu_l <= delta_#/16 the polynomial is absorbed. For r >= r_min := C log L / (mu_l L): C_1 L^3 Phi^l_k(L r/3) <= (1/4) Phi^l_{k+1}(r) in the first tier. In the second tier the same holds for r >= r_s := C log L / (mu_s L), given zeta_k <= C zeta_{k+1}; for r < r_s the second tier of the old term is below the first tier of the new one with a tiny coefficient, as zeta_k <= e^{-mu_l r_s} for x >= x_*, which is the crossing argument of the upper chain's 21.7(iii). Below r_min use 2 ||R||_1 and enlarge D^R. So D^R <= (1/2 + C(L) g) D^R + C''(L), and D^R := 4 C''(L) closes for x_* large. QED at this level.

(Loc^c_k) at order one then holds at mu_l, with the second tier, so hostile (13) of `library/sector-values.md` stops being a limitation at that order. O2 and O3's tails for values, and higher orders of (Loc^c), go the same way; they are not needed below and I have not written them.

## 5. Theorem RC

Dictionary on this map. S^r_W := x A_k o Phi + Q^reg o Phi - log J with Q^reg = R_k and Q^s = 0 (Text 5.8, Requests): this is S(.; W) of Text 5, up to the constant x A_{k+1}(W) + vac. The law E^r_W is proportional to e^{-S - Psi} on K, the base integral T(W), and E^good_W of (C2_j) on this map is that same law: one cut chi_c, one domain K, both independent of W. So **(LAW) is trivial and RC-transfer vanishes.** G_W := G^cur_(k;c',c'') is the polynomial of Lemma 14.16 in the common coordinates xi, with

    grad_(c,b) = x^{1/2} d_b (a_c o Phi_0)(0),    Q_c(b, b') = d_b d_b' (a_c o Phi_0)(0),

Phi_0 the unscaled chart. Let delta_cl >= delta_#/2 be the rate of the tree decay of a_c to order two, per level-k cell. Then, by Prop AN3 and AN2(a), for c in B(c'), b in B(c''), d := d(c', c''), L large: |grad_(c,b)| <= x^{1/2} C(L) T_2 e^{-delta_cl L (d - 3)_+}, |Q_c(b, b')| <= C(L) e^{-(delta_cl/2) L (d - 3)_+} e^{-(delta_cl/2) d_k(c, b')}: the chart reaches at most 3 L cells.

**Theorem RC (implication).** *Assume H(k) with (Loc^f_j), j <= k, and x_k >= x_*. Set sigma := delta_cl L / 4, rho_f := delta_#/16, rho_s' := mu_s / 2. For every W, Wtilde in D_{k+1}, with U := iota^new_k x_{k+1}^{3/2}, t := x_{k+1}/x_k, C_I(L) large:*

    (RC-size)   |f(W)| <= C U e^{-sigma d};
    (RC-far)    t |E^r_W G_W - E^r_Wtilde G_Wtilde| <= C U [ e^{-sigma d - rho_f (n - d)} + a_s e^{-sigma d - rho_s' (n - d)} ],

*if W, Wtilde agree on a non-full Q_n(o), n >= d, with a_s := poly(x_k) z_k^{1/2}. C depends on Theta only.*

*Proof. Size.* By (M), E_W |xi_b xi_b'| <= C(L), so |E_W G_W| <= C(L) (x^{1/2} T_2 + 1) e^{-(delta_cl/2) L (d - 3)_+}, summing over the C L^8 pairs in the two blocks and the tails. Since x^{1/2} <= C x_{k+1}^{3/2}/x_k, this is at most C U e^{-sigma d}, taking C_I(L) large; the same at W = 1.

*Far.* If d >= n - C, this follows from size, as e^{-rho_f (n - d)} >= e^{-C rho_f}. Otherwise let S be the boxes of c', c'', R := dist(S, Q_n(o)^c) >= n - d/2 - 2, and (SPLIT): E_1 G_1 - E_2 G_2 = E_1 [G_1 - G_2] + (E_1 - E_2) G_2.

*Coefficient response.* By Lemma CL(c), each coefficient of G_1 - G_2 is at most C(L) (x^{1/2} T_2 + 1) e^{-(delta_#/2) R}. By the size bound it is at most twice the bound above. The geometric mean, with (M), gives |E_1 [G_1 - G_2]| <= C(L) x^{1/2} e^{-(delta_#/4) R} e^{-(delta_cl/4) L (d - 3)_+}.

*Law.* (INT) with T := G_2, Lemma FAR. D G_2 is supported near S, with the tails of its coefficients, so e_f, e_s <= C(L) x^{1/2} e^{-(delta_cl/4) L (d - 3)_+}, as rho and rho_s are far below delta_cl L. eps(b) as in Prop LF, with (Loc^f_k) for the R part. So

    |(E_1 - E_2) G_2| <= C(L) x^{1/2} (1 + R)^8 e^{-(delta_cl/4) L (d - 3)_+} [ e^{-(delta_#/8) R} + poly(x) z^{1/2} e^{-mu_s R} ].

Write R >= (n - d) + d/2 - 2, and absorb the polynomial with rho_f <= delta_#/16, rho_s' <= mu_s/2, using n - d >= 0: (1 + R)^8 e^{-epsilon R} <= C(epsilon). QED

*Rates.* c_t = rho/3 in Prop MD*, with rho at most delta_#. So kappa = c_t/32 <= delta_#/96, at c_t <= 1, and 2 kappa <= delta_#/48 < rho_f. kappa_s <= c_s/16 with c_s = rho_s/3: 2 kappa_s <= rho_s/24, so rho_s' >= 2 kappa_s once mu_s is taken as in Prop LF and kappa_s is lowered to mu_s/4 if mu_c < rho_s; kappa_s only weakens the profile (it must still fit (TT), which carries it). sigma = delta_cl L / 4 >= delta_# L / 8. Take c_I := sigma and c_* := sigma - 2 max(kappa, kappa_s), positive for L large, and c_r < c_*. So (RC-rates) hold, with rho_v >= 2 kappa_v, the stronger form Lemma EXT' reads. a_s <= C zeta_{k+1}: z^{1/2} <= zeta_k^4 and poly(x) zeta_k^3 <= 1, by the argument of `library/current-locality-reduced-law.md`, section 2.

## 6. Hostile check

1. *Could M_1 alone be the reference, with E in V?* No. (A) would need ||e^f A_1 E e^-f|| small, and E is of order one far out. So A_t has to be the reference, and that is why Lemma W is needed. HS-P allows it, as M_t is constant for fixed t.
2. *Lemma W reads only the inverse at one field.* True, and it is the asymmetry that makes it work. W_2 enters through gamma, Gamma, the tail and closeness only.
3. *The second sign of the weight.* Both are needed, in G and in G^*. Symmetry of A_t gives both.
4. *Does any step read a path across sectors?* (INT) no. The hybrid lives on a class path from V_1 inside one sector, and its other side is compared by exact equality on a ball. Yes, that is all.
5. *The designated-bond spike.* A hybrid made by cutting xi directly has a designated bond of size L^3 times the residual, out of the class. Hence the bump in the construction of P_h. Then xi_h is defined by P_h, not the reverse.
6. *x in the far gradient.* d_b S_a(xi) = x^{1/2} d_b (A_k o Phi_0)(g xi) + ... has a factor x^{1/2} term by term, but criticality at 0 removes it: it equals int_0^1 Hess(s xi)[e_b, xi] ds, with no x. On K the sup is poly(x), and only the slow tier reads the sup.
7. *Is U really this generous?* U is about C_I(L) x^{1/2}, while the true size of I x is C(L) Ebar, far smaller. RC asks no more than U, and the crude bounds suffice. This does not bear on (K1) or on the sharper h.
8. *Amplitude compounding in Lemma CL.* D_k feeds E_k only through a power 2/L, because the tail of g is at rate delta_# L / 2 per box, against a kernel at rate delta_#. Written with D_k linearly it would compound by C(L)^2 per level. I found this by writing it the first way.
9. *Lemma O2's own use of S_t for the gas:* kept at mu_c(L), as amplitude z pays.
10. *What I would attack first:* Prop LF's second tier at r < r_s, and whether (H1) along the segment of Lemma CL holds when the relative field is C L T_2 and the transition has width C_0 boxes. Also (F3) with the cut radius now depending on C_W(L).

## 7. Numerics

`checks/rc_far/`, criteria first in each script, abelian, trivial background, d = 2, one level, Gaussian, artificial far parts. These test the elementary Lemma W on the real chart matrix, and nothing on the non-Gaussian law, on SU(2) or on sectors. **All three runs read FAIL by their registered criteria**, and the first result was not re-graded.

- `two_rate_weight.py`: FAIL on T3 at L = 7, rate 0.445 against 0.5 on n = 1..4. T1, T2 pass. Its control C1 showed N_s tracking N_2, so T1 was close to vacuous.
- `two_rate_weight2.py`: Part A PASS: slope of a(n) on n = 5, 6, 7 is 0.994, 0.973, 0.928 at L = 3, 5, 7, ratio 0.934. This is the registered tail rate 1 of E, so T3 above was saturation at the gap scale, not a rate falling with L. Part B: N_2 bounded, ratio 1.19, but control B2 FAIL, as the far part made no slow region.
- `two_rate_weight3.py`: C1 PASS, N_2 ratio 1.02, 1.19, 1.19. C3 PASS: a(n) falls at 3.12, 2.82, 2.76 per box, ratio 0.885, about two propagators with no fall in L. C2 FAIL, N_s(1)/N_2(1) = 1.04, 1.28, 1.04. Cause, seen after the run: gamma_0 = 0.02 gives a rate about 0.14 L per box, which is not slow at L = 5, 7, and the norm is held at 1/gamma_0 by the zero mode. A real control needs a far larger torus. I stopped here, since the lemma has a two-line proof and the control could only say whether the weight is necessary.

What they establish: on these matrices the far effect on the local inverse decays at a rate per box that does not fall with L, and the two-rate norm stays bounded in n. What they do not establish: that the two-rate weight is needed.
