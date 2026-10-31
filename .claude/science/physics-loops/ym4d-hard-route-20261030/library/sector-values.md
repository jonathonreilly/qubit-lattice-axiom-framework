# Values of R_k across topological sectors

Own derivation, 2026-10-31; not reviewed. Part: `hard-core--mapped`. Answers D4 of `gates/theorem-z-3b7fd4e57.md`. Balaban's objects are kept (block averages, minimal fields, running coupling); the ordered integration below is standard in cluster expansions and is not taken from his text. This line is not independent of the Sussman-Alpoge repository, which supplied the map; this argument does not read it. Nothing here reads the sibling attempt.

Status, by part. Section 1: exact identity, derived. Sections 2, 3: derived at the level of each term, with the constants named, resting on Theorem F-D, HS-P, HS-T, (R3), (AD), Prop AN3 at their own labels. Sections 4 to 6: implications of those. So this is a route that has been written out and attacked once, and not a closed proof.

## 0. The problem and the decision

Item (r) of `library/relative-density-bound.md` said that two class fields equal off J are joined by a path of flux at most C T. *False across sectors* (the gate's D4, which I confirm): an instanton of radius about T^{-1/2} in singular gauge, cut off inside a ball J, has flux at most T and equals 1 off J, and no path of small flux joins it to 1. R_k is known only by derivative norms on D_k, so nothing bounded the difference of its values between sectors. Readers: Step 4 of Theorem Z; (FF_j)(Lo), (FF_j)(U); Lemma 3 of `library/gauge-taylor-contraction.md`, through "a path of class fields"; and also (RP_m[i]) at Steps 2 and the tail clause, so the fallback is hit by the same defect.

*Decision.* The one-function formulation carries it. R_k stays one function in the hypothesis, with no local polymer representation. Two clauses are added to H(k): a value clause (VAL_k), which is a consequence of the recursion and needs no local form of R_k, and a locality clause (Loc^c_k), which comes back into the hypothesis in a form with class fields only. A local decomposition is used only for the *one-step source*, which is computed afresh at each level, so the surface excess of the older recursive density (`parts/hard-core--mapped.md`, routes tried) does not arise.

*What a jump would be.* A constant per unit of charge would be a local density that vanishes on exact fields and is non-zero on a sector. At zero momentum the only quadratic form on 2-forms that vanishes on every simple e ^ a is the Plucker form F ^ F. So a jump is a theta term, and a single-axis reflection, a symmetry of the model, forbids it. A term in |Q| is not local. This is the reason the bound below can be true, and Section 2 uses it, by averaging the order of integration over the signed axis permutations.

## 1. The chain-sum identity (exact, derived)

Let V^*(V') be the unique class minimiser of A_j on the fibre of V' in D_{j+1}. Its flux is at most C_r L^-1 T_2 and it is unique in the chart, whose fibre over a class parent is connected, in every sector: Theorem F-D and Lemma F do not read the sector. Define, by subtraction alone,

    Ghat_j(V') := F_{j+1}(V') - x_j A_{j+1}(V') - R_j(V^*(V')),    Z_j(V') := Ghat_j(V') - Ghat_j(1) + beta_{j+1} A_{j+1}(V').

Writing F_{j+1} as the integral over the fibre, Ghat_j reads R_j only through R_j(W) - R_j(V^*(V')) along the connected chart, so only through derivatives of R_j. With vac_{j+1} |Lambda_{j+1}| = Ghat_j(1), R(1) = 0, A(1) = 0, x_{j+1} = x_j - beta_{j+1}:

    R_{j+1}(V') = R_j(V^*(V')) + Z_j(V')    for every V' in D_{j+1}, in every sector.

Iterating, with R_0 = 0 and the *minimal chain* V_k := V, V_j := V^*(V_{j+1}):

    R_k(V) = sum_{j < k} Z_j(V_{j+1}),    A_j(V_j) = A_k(V) for all j <= k.        (CS)

No path enters. So values of R_k are read from one-step sources along one chain. What is left is a bound on one source, in every sector, that falls along the chain.

## 2. The source: gauge-invariant ordered integration

*Irrelevant energy.* For V a class field at level l, weight w >= 0:

    I_l(V; w) := sum_x w(x) ( sum_{p at x, e} |F_{p}(x + e)^{transported} - F_p(x)|^2 + sum_{p at x} |F_p(x)|^3 ),

with F_p the plaquette angle. Under scaling the gradient and the cubic parts are both dimension six, so both should fall by L^-2 going down one level. w_x(y) := Phi(d(x, y)/4), the profile of `library/one-step-closure.md` at half its rates. Note I_l(V; 1) <= C T_2 E_l(V) + ... is not assumed: I has a gradient part that a bound by energy would lose.

*The order.* Boxes are the blocks of level j + 1, indexed by level-(j+1) cells i. Fix a lexicographic order O on Z^4, for a choice of axis order and signs and an origin of the seam on the torus. Let Z_{<= i}(V') be the total mass over level-j fields W in the fibre of V', with W = V^*(V') on all boxes after i, and the same integrand e^{-F_j(W)}, gas included. Then

    g_i^O(V') := -log ( Z_{<= i}(V') / Z_{< i}(V') ),    F_{j+1}(V') = sum_i g_i^O(V') + F_j(V^*(V')) - log J_{V'}(0),

with J the chart's Jacobian. *J is local:* the constraint on a parent bond is solved for one designated bond, so at xi = 0 the determinant is triangular, and log J_{V'}(0) is a sum over parent bonds of functions of V^* near that bond, gauge invariant, with tree decay in V'. So Ghat_j(V') = sum_i g_i^O(V') - log J_{V'}(0), and the second sum has the same treatment as the first; I do not write it again. Each g_i^O is gauge invariant under parent gauge transformations: V^* is equivariant, the chart at a block centre rotates its coordinates with the parent's gauge, and Haar is invariant. *Every O gives the same sum.* So average over (O): over all positions of the seam and all signed permutations of the axes. Let g_i be the average of g_i^O over O. It is a local, gauge-invariant function, translation and hypercubic covariant *exactly*, with no seam left and no choice left. The reflection of one axis is in the group.

*No pinch.* The free set {boxes <= i} is a down-set of the product order in signed coordinates, so no four boxes around a vertex have free and frozen diagonally. So it is locally a Lipschitz graph, as for the bricks of Lemma BG. I have checked this also across the seams by cases in d = 2, and d = 4 is the same case split per pair of axes; Theorem F-D is stated for bricks and has to be read on this set (implication below).

**Lemma O1 (norms; level of each term).** Rooted at i: sum_{b_1 ... b_n} |D^n g_i(V')[b_1, ..., b_n]| / Phi(tree(i, b_1, ..., b_n)/2) <= C_n(L), with C_n(L) free of x_j and j, for 1 <= n <= N - 1. *Why.* D_a g_i = E_{<= i}[D_a S] - E_{< i}[D_a S]: the two laws differ by integrating box i or holding it at 0. Interpolate by a pinning weight on xi_i; the derivative is a covariance of D_a S with a function on box i, with x cancelling as in HS-T, and it decays by Theorem F-D on the free set and Lemma HS-P, HS-T. Higher n: the cumulant expansion of HS-T. Gas: w_i := the same ratio for total over base mass, by (A1'), (A2).

**Lemma O2 (locality across sectors; level of each term).** If V', V'' in D_{j+1} are equal on B(i, r), in a common gauge there, then |g_i(V') - g_i(V'')| <= C(L) Phi(r/2), and the same for derivatives rooted in B(i, r/2), with the rate of Phi read as mu_c(L), hostile (13). *Why.* Put both on one coordinate space, box by box. S_t := (1 - t) S_{V'} + t S_{V''}. No path of fields is used: this is an interpolation of *actions*, so sectors do not matter. Its Hessian is a convex combination, so it has the same lower bound against the same box-local form as each of the two, and it has the same decay. So d/dt g_i(S_t) = E_{<= i, t}[S_{V''} - S_{V'}] - E_{< i, t}[S_{V''} - S_{V'}], a covariance across distance r, of order one as x cancels. For gas: activities of polymers at distance below r/2 agree up to the tail, and far polymers contribute by tree graphs with their z.

**Lemma O3 (Taylor at a local trivial field; level of each term).** Let f_i(r) := max over B(i, r) of |F|, and r_*(i) := the largest r <= N_{j+1}/2 with f_i(r) r^2 <= c. A_i := V' in axial gauge at i on B(i, r_*). Cut off with a logarithmic chi, |x| |grad chi| <= 1/8 (a cut-off with |x| |grad chi| of order one raises flux by a factor about 3, which Lemma 3 of the Taylor note overlooked; see Section 5). Then the cut field V'^(i) is equal to V' on B(i, e^-8 r_*), has flux at most (5/4) f_i, and exp(s A_i) is a path in the class from it to 1. So with (O2) and Taylor to order 3, with D g_i(1) = 0 by colour invariance:

    g_i(V') - g_i(1) = (1/2) Q_i[A_i, A_i] + O(C(L) sum_y w_i(y) |F(y)|^3) + tail_i,    Q_i := D^2 g_i(1),    |tail_i| <= C(L) Phi(e^-8 r_*/2).

Sizes: |A_i(y)| <= the sum of |F| along the radial path, so the order-3 term is at most a weighted sum of products |F(a)||F(b)||F(c)|, and by Hoelder at most the weighted cubic energy. *The tail is below the cubic energy, by maximality of r_*.* There is a cell at distance r_* + 1 with |F| >= c/(r_* + 1)^2, so w_i |F|^3 there is at least c^3 (r_* + 1)^-6 Phi((r_*+1)/4)... and tail_i <= C(L) c^-3 (r_* + 1)^6 Phi(e^-8 r_*/2)/Phi((r_*+1)/4) w_i|F|^3 at that cell. For this the rate in w_i must be below the rate in the tail by a fixed factor: replace 1/4 by e^-8/4 in w_i. If r_* = N_{j+1}/2 there is no such cell, and the tail is at most C(L) Phi(e^-8 N_{j+1}/4): a toron term, per box.

*Quadratic part.* Q_i annihilates gradients, as D g_i(1) = 0. On the ball, A_i = H_i(dA_i) with H_i the radial homotopy, centred at i, of polynomial growth. So Q_i[A_i, A_i] = <dA_i, kappa_i dA_i>, kappa_i := H_i^dagger Q_i H_i, with decay in d(y, i) + d(y', i). dA_i = F + O(|A_i|^2), so this equals <F, kappa_i F> transported through i, up to the cubic energy. Transporting directly from y to y' changes it by |F(y)||F(y')| times the flux through the triangle (i, y, y'), again cubic.

*The sum.* K(y' - y) := sum_i kappa_i(y, y'), translation invariant by the average over seams, reflection even and hypercubic by the average over axes, on su(2) by colour and on plaquette orientations. Reflection and symmetry give K(y)_{pp'} = K(-y)_{pp'} = K(y)_{p'p}. So polarisation gives no term with one derivative:

    sum_{x, y} F_p(x) K(y)_{pp'} F_{p'}(x + y) = K-hat(0)_{pp'} sum_x F_p F_{p'}(x) - (1/2) sum_{x, y} K(y)_{pp'} Delta_y F_p Delta_y F_{p'}.

K-hat(0) is invariant under signed permutations, and on the six orientations the only invariant is kappa-bar times the identity: a single reflection removes F_01 F_23 (the theta term) and F_01 F_02. Since K represents D^2 Ghat(1) on exact fields, kappa-bar is its F^2 coefficient, the same number that fixes beta_{j+1}. And |Delta_y F|^2 <= |y|^2 times the gradient along a path.

*The action term.* A_{j+1} needs no order. With e_c(V') := the Wilson energy of V^*(V') on the fine cells of c, a local gauge-invariant function, A_j^W(V^*(V')) = sum_c e_c(V'); the same Taylor and sum, with K-hat(0) = 1 by the exact lift of constant flux (Lemma 3.3 of the producer), give the one-step bound in (Y) below. With Y_l := A_l - A_l^W, Y_{j+1}(V') = Y_j(V^*(V')) + [A_j^W(V^*(V')) - A_{j+1}^W(V')], the same chain as (CS), so (VAL) below also gives |Y_k(V)| <= C(L) I_k(V) in every sector. **(Y)**

**Proposition SRC.** *Z_j = sum_x zeta_j(x; .), with zeta_j(x; .) a gauge-invariant, translation-covariant local function, Z's F^2 term removed, and for V' in D_{j+1} with flux at most (4/5) T_2 (see Section 5 for the factor):*

    |zeta_j(x; V')| <= C(L) ( I_{j+1}(V'; w_x) + Phi(e^-8 N_{j+1}/4) ),
    |D zeta_j(x; V')[delta]| <= C(L) I_{j+1}(V'; w_x)^{1/2} |delta F|_{w_x} + (the same tail) |delta F|_{w_x},

*with delta F the first variation of F and |.|_{w} its l^2 norm with weight w. C(L) is free of x_j and of j.*

*Proof.* Collect the rearranged quadratic parts and the cubic and tail parts of Lemma O3 and of the action term. The first derivative: D g_i(V')[delta] reads delta only through delta F, since D g_i(V') vanishes on infinitesimal gauge transformations; use H_i on delta. The linear term in A_i then gives <F, kappa_i delta F>, which after the same rearrangement is <Delta F, K Delta delta F>, and higher terms give |F|^2 |delta F| <= I^{1/2} |delta F|. QED at this level.

## 3. The lift: (LIFT-I)

**Proposition LIFT-I.** *Let V' be in D_{j+1}, W := V^*(V'), c' a level-(j+1) cell, and sh(c') the level-j cells below it. With rho the absolute rate of Theorem F:*

    sum_{c in sh(c')} ( |grad F_W(c)|^2 + |F_W(c)|^3 ) <= C_0 L^-2 sum_{c''} e^{-rho d(c', c'')} ( |grad' F'(c'')|^2 + |F'(c'')|^3 ) + tails,

*with C_0 absolute, for L >= L_0 and a_* <= a_th(L).*

An energy bound does not give this: the response to a non-constant parent has energy of order |grad' F'|^2, with no gain, and then a per-level constant would accumulate. The gain is an H^2 statement, and it has a clean form.

*Step 1: the comb cancels exactly.* Let n := j + 1, U the fine field of the chain, lambda := D A_n(V'). Stationarity on the fibre gives D^*_U F_U = Q^{(n)*}_U lambda (`library/analytic-lift.md`, D_Y A_n = lambda). A_n is gauge invariant, so D'^*_{V'} lambda = 0. Since Q = Q^o + D' Phi, with Phi the block-centre phase (`library/composite-adjoint.md`), <lambda, D' Phi h> = <D'^* lambda, Phi h> = 0. *So on the true multiplier the contour parts of Q^* vanish identically.* In the abelian case this is exact: the contour only chooses a gauge of the parent. `checks/hard-core--mapped_lift_gradient.py`, L0, finds plaquette angles with the comb and with lines only the same to 7e-13 at L = 3 and 9e-13 at L = 5. So the first-stage bonds, which carry order one of a generic Q^*, carry nothing here at the abelian level.

*Step 2: size of Q^*.* By (AD), for the rest: ||Q^{o,(n)*}_U lambda||_{L^2(box)} <= C (1 + L^2 ||F||_{L^4(box+)}) |lambda|_loc <= C |lambda|_loc, as L^2 flux' <= C a_*, C absolute, in level-n units. The line part has weight L^-3 on a bond in lattice units.

*Step 3: the multiplier is of the order of the parent's gradient.* lambda = D^*F' + D Y_n(V'), and, by Lemma 3 of the Taylor note with n = 1 at the local trivial field: |lambda(b')| <= C_lambda sum_{c''} e^{-rho d} |grad' F'(c'')| + C(L) sum e^{-rho d} |F'(c'')|^2 + tails. C_lambda is absolute, read from the symbol at U = 1, g-hat(P) := the quadratic form of A_n on 2-forms, analytic in a strip of absolute width, uniformly in n and L (abelian composite of side L^n equals one level of side L^n: the line averages compose). Reported by the check.

*Step 4: Weitzenboeck, at the fine level.* With a cut-off eta of parent scale, sum over the fine lattice, in level-n units:

    ||eta grad F_U||^2 <= 2 ||eta D^*_U F_U||^2 + C ||(grad eta)(F_U - F-bar)||^2 + C int eta^2 |F_U|^3 + (lattice Bianchi, O(|F|^2 eta_fine) ).

F-bar := F'(c')/L^2 transported, locally constant: it is here that no energy term remains. The response ||F_U - F-bar||^2_{L^2(box++)} is at most C sum e^{-rho d} |grad' F'|^2 + C(L) |F'|^4: the map F' -> F_U has an analytic symbol on closed forms and F-bar is its value on constants, by Lemma 3.3; the non-abelian remainder is Lemma AN1. So the local form closes, with no commutator of size E.

*Step 5: down to level j.* F_{V_j} is the composite average of F_U up to Lemma AN1. The average is a convolution of mass one on its abelian part, so it does not raise the l^2 norm of the gradient; AN1's remainder gives C_2(L)^2 L^-4 f^4 per parent, below L^-2 f^3 for a_* <= a_th(L). In lattice units of level j, sum_c |Delta theta|^2 = L^-2 ||grad F||^2_{L^2(box)}.

*Step 6: the cubic part.* By (R3), ||F_U||_{L^4(box)} <= C f_loc in level-n units, so sum_c theta^4 <= C L^-4 f_loc^4 and, by Hoelder over L^4 cells, sum_c |theta|^3 <= C L^-2 f_loc^3. QED at this level.

*Scale check by exact numerics, abelian.* C(d, L, n) in the check is exactly the ratio in the gradient part. See Section 7.

## 4. The value clause and the jump

**Theorem VAL (implication).** *Given SRC and LIFT-I, with C_0 L^-2 <= 1/2, for all k and V in D_k, in every sector:*

    |R_k(V)| <= B_v(L) ( I_k(V; 1) + N_k^4 Phi(e^-8 N_k / 4) ),    B_v(L) := 2 C_w(L) C(L),

*where C_w(L) is the constant in sum_x w_x <= C_w. Proof: (CS), SRC, and I_{j+1}(V_{j+1}; 1) <= (C_0 L^-2)^{k-j-1} C I_k(V; 1) by LIFT-I summed over cells. The toron term falls superexponentially going down, as N_j = L^{k-j} N_k.*

For an instanton of radius rho at level k, I_k is about rho^-2, so R_k there is at most B_v rho^-2 <= B_v T. This is the lattice artefact (a/rho)^2 in the instanton's action, as it should be. In particular there is no constant per unit of charge.

**Theorem Jump (implication).** *Let V_1, V_2 in D_k be equal off J, in a common gauge there. Then with r_1 := (2/mu) log(1/T_2) and J^+ the r_1-neighbourhood of J in level-k cells:*

    |R_k(V_1) - R_k(V_2)| <= B_j(L) T_2^2 |J^+|,   B_j(L) free of k and of x.

*Proof.* (CS) along the two chains V_{l, j}. At level j + 1, with m := k - j - 1, split x by its distance d_k(x, J) in level-k cells.

*Near zone, d_k <= r_1.* The absolute bound of SRC for each field. By LIFT-I, sum over those x of I_{j+1}(V_{l, j+1}; w_x) <= (C_0 L^-2)^m C I_k(V_l; 1_{J^+}, smeared), and I_k per cell is at most C T_2^2. So this is at most C(L) (C_0 L^-2)^m T_2^2 |J^+|.

*Far zone, d_k > r_1.* Let r := L^m d_k(x, J)/2 in level-(j+1) cells. On B(x, 2 r) the two fields differ by delta, small by Theorem F-D: a difference of minimisers with parents agreeing off J decays at the rate rho per parent cell at each level. Interpolate: V_3 equal to V_2 on B(x, r) and to V_1 off B(x, 2 r), joined across the annulus, where they are close. By Lemma O2 for V_3, V_2: a term C(L) Phi(r/2); its sum over far x, with L^{4m} cells per level-k cell, is at most C(L) L^{4m} e^{-mu L^m r_1/4} |J^+|, which is summable in m and at most C(L) T_2^2 |J^+| by the choice of r_1, up to a factor. For V_1, V_3 there is a true path, so the derivative bound gives C(L) I(V; w_x)^{1/2} |delta F|_{w_x}, and by Cauchy-Schwarz with the weight w_J := e^{-mu d_k(., J)} and its inverse:

    sum_x C(L) I(x)^{1/2} |delta F|(x) <= C(L) ( I_{j+1}(V; w_J) )^{1/2} ( sum_x w_J^-1 |delta F_{j+1}(x)|^2 )^{1/2}.

The first factor is at most (C_0 L^-2)^{m/2} (C T_2^2 |J^+|)^{1/2}. The second is the weighted energy of the difference. The minimal lift preserves the Hessian of the effective action exactly on the quadratic part: A_j(lift of delta') = A_{j+1}(delta'). The effective action's form is comparable to |F|^2, by g-hat, with absolute constants. The weight varies at rate mu L^-m per level-(j+1) cell, so the commutator costs a factor 1 + C mu^2 L^-2m, and the nonlinear part a factor 1 + C(L) f_j, both summable over levels. So the second factor is at most C (T_2^2 |J^+|)^{1/2}, with no growth in m. The product is at most C(L) L^-m T_2^2 |J^+|.

Sum over m. QED given SRC, LIFT-I, O2, F-D.

## 5. (Loc^c_k): locality back in the hypothesis, class fields only

**(Loc^c_k).** For V, V'' in D_k equal on B(y, r) in a common gauge, and n <= N - 1:

    | D^n R_k(V)[y, b_2, ..., b_n] - D^n R_k(V'')[y, b_2, ..., b_n] | summed over b_i in B(y, r/2), with weight 1/Phi(tree/2), <= D_n(L) Phi(r/2).

*Recursion (level of each term).* R_{k+1} = R_k o V^* + Z_k. For Z_k: O2 and Prop AN3 on the ball, with S_t. For R_k o V^*: chain rule through the lift, which reads D^m R_k at V^*(V'), V^*(V''). Those two agree up to e^{-rho (r' - d')} on the shadow of B(y', r'), by Theorem F-D on the ball with parents equal; interpolate to a field that equals one on an inner ball and the other outside, as in Theorem Jump. The result is C^n L^{4-n} D_n Phi(L r'/2) from the old constant, with the improved distance L r', so a factor e^{-mu (L - 1) r'/2} against C^n L^{4 - n}, for r' >= 1; and from the closeness a source B_{n+1} C(L) e^{-rho r'}. For r' < 1 the bound is trivial if D_n >= 2 e^{mu} B_n. So D_n(L) := max(2 e^mu B_n, 2 C_n(L) B_{n+1}) closes, free of k, for L >= L_0. It reads ||R_k||_{n+1}, available for n <= N - 1.

*Lemma 3 of the Taylor note, corrected.* Its proof read "at s = 0 the field is trivial on a ball of radius r/2, so its derivatives differ from those of the trivial field by C e^{-mu r/2}: this needs only tree decay ... along a path of class fields". Across sectors there is no such path. The step now reads (Loc^c_k), which has no path. Separately, its flux factor 1 + C a r^2 omitted d chi ^ A, which is of order a |x| |grad chi|. With the logarithmic cut-off, the factor is at most 5/4 for a r^2 small, at a fixed loss in r. So its statement needs the formula range to have that room. T_2 is fixed only through a_* small, so H(k) is stated on D_k with T_2 enlarged by a fixed factor 5/4. Nothing else in the closure reads this constant.

## 6. With boundary data

Theorem Z's Step 4 reads R + Delta R^𝔡. For the boundary term a crude value clause suffices:

    (VAL^𝔡_l)  |Delta R_l^𝔡(V_1) - Delta R_l^𝔡(V_2)| <= D_v(L) ( number of cells of the boundary surface within r_1 of J ).

*Recursion.* Delta R_{l+1}^𝔡(V') = Delta R_l^𝔡'(V^*(V')) + (G^𝔡 - G^bulk)(V'), by the same subtraction as (CS). (i) G^𝔡 - G^bulk: order the boxes; only boxes within r_1 of the surface have g_i^𝔡 different from g_i^bulk beyond the tail, and each term is bounded by C(L), by O1 and the convexity in Theorem F-D. (ii) The old term: Sigma_l lies under frozen parents, at distance at least r_S parent cells from free bonds, so the two lifts agree on the old term's support up to e^{-delta_# r_S}, on a connected ball, so derivatives apply. That gives C L^3 e^{-delta_# r_S} D_v <= (1/2) D_v per surface cell, by r_S >= (4 log L + C)/delta_#, as in the count for norms. If J meets the sheet Sigma_l itself: then the old term is bounded by its own clause at the level below, and it is counted in n. So D_v(L) := 2 C(L). QED of the sketch.

## 7. Numerics

Criteria written first, in each script. All under the lock.

`checks/hard-core--mapped_sector_value.py`: d = 2 U(1), block-constrained covariant Laplacian determinant, lift by hand. **PASS, run once.** Gauge invariance exact; power control: a non-gauge change moves G by 1.0. kappa from sectors 1, 2, 3: -0.001032, -0.001033, -0.001033, against -0.001061 from a slowly varying field in sector 0 at p = 2 pi/16 (criterion 3 percent, met). |Z|/I in a patch of charge one, n = 4, 6, 8, 10: 0.0002, 0.0003, 0.0003, 0.0003; in a neutral pair: 0.0002 at all n. |Z| in the charged patch falls like 1/n^3 with I. Two far charged patches: Z(two) = -3.97731e-04, 2 Z(one) = -3.97731e-04. So *no jump, and exact additivity, in the simplest case with sectors.* Limits: U(1), d = 2, one level, one-loop.

`checks/hard-core--mapped_lift_gradient.py`, the abelian (LIFT-I): **FAIL on L2, on caps I had guessed.** L0: comb against line-only, 7e-13, 9e-13 in plaquette angles; the Fourier ratio against a direct solve, all digits printed. L1 passes. L3 passes, R at most 0.85. L2: C(4, L, 1) = 16.96, 30.28, 37.56, 41.57, 43.93 at L = 3 to 11, above the cap of 30, with C(11)/C(7) = 1.17 above 1.15. Composite: 16.96, 16.01, 16.00 at L = 3, n = 1, 2, 3; 30.28, 26.02 at L = 5, n = 1, 2. Follow-up `checks/hard-core--mapped_lift_gradient_limit.py`: **FAIL on M3 only.** C = 45.41, 47.06, 47.90, 48.81 at L = 13, 17, 21, 31, with falling increments; a fit at L = 9, 11 alone gives C_inf = 48.70 and predicts C(31) within 1.5 percent. Symbol g in [1.026, 12.09], above my cap of 10. **So in the abelian sector C_0 is about 50, with no growth in L or in the number of levels: a measurement, on a grid of momenta, with its peak at the zone corner.** With that, C_0 L^-2 <= 1/2 for L >= 10.

`checks/hard-core--mapped_lift_su2.py`: **PASS, run once at these criteria** (smoke runs before it fixed the solver: my first block map had a linear gauge rotation from the jet check, not gauge covariant, which made SQP drift along gauge directions). d = 2, SU(2), one level, the comb, a true constrained minimiser; constraint residual at most 2e-12 and projected gradient at most 4e-6 wherever converged. Commuting parents: R = 2.0014, 2.1434 against the abelian 2.0194, 2.1626, and the difference is the cubic share of the denominator, 0.9 percent. Non-commuting, random low modes: R between 2.7 and 9.4 at L = 3, 5, 7. X(0.05) between -0.0045 and -0.0057, and X(0.1) between -0.011 and -0.014, which is about minus the change in the denominator's cubic share, 1.5 to 2.2 percent, so the true excess is under half a percent at L f^2 = 0.07. One case, L = 3, seed 2, f = 0.1, did not converge and is not used; f = 0.2 failed in a smoke run, as the Gauss-Newton Hessian omits lambda D^2 M. **So no non-abelian excess is seen, and the count (AD) is far from saturated on these parents. This is weak evidence:** d = 2, low modes, random and not adversarial, one level, and the d = 4 count differs.

`checks/hard-core--mapped_staircase.py`: **PASS.** No pinch for any i in d = 2, 3, 4 at N = 4 and d = 2, 3 at N = 6, seams included; in d = 4 at every third i. Control: the checkerboard has 16.

## 8. Hostile check (newest step, attacked as a sceptic)

(1) *Is g_i really gauge invariant, with designated bonds straddling boxes?* A designated bond is a function of the free variables in its two boxes and of V'. With boxes after i frozen at V^*, the chart map is the same map restricted to a coordinate subspace, and it is equivariant, since V^* is. Yes.

(2) *The ordered sum is over the fibre with frozen parts at V^*, but rough W on frozen boxes?* In Z_{<= i} the frozen boxes are at V^*, class. Rough W only occur on boxes <= i. The whole sum telescopes to the total mass, as at i = last nothing is frozen. Yes.

(3) *Does O1 hold when nearly everything is frozen, at the first box, and at the staircase in between?* The law on one box: (H1) holds with the frozen exterior, by the box-local chart. For intermediate i the free set has a large boundary, so F-D is read there. Theorem F-D reads the free set only through its extension constant C_ext (`library/fibre-propagator.md`): reflection gives C_ext absolute at flat walls and cube corners, and it fails at a pinch. The free set of a lexicographic order is a down-set of the product order, up to seams, so it has finitely many local patterns with no pinch. `checks/hard-core--mapped_staircase.py` checks no pinch, including seams. **So the absolute rate holds, given that Theorem F-D, which no gate has read, is right, and given that each pattern has a reflection extension, which I have not written pattern by pattern.** Even if not, a restriction to a coordinate subspace has at least the same lower bound, and Combes-Thomas gives a rate depending on L. Then only constants change, since rates enter only through w_x and r_1. Nothing compounds.

(4) *Lemma O3: the cut field has flux up to (5/4) f, and D_{j+1} stops at T_2.* Handled in Section 5 by the factor in T_2.

(5) *r_* at a field with very small flux.* If f_i(r) r^2 <= c up to N/2, then the toron term. If the holonomy is trivial it is smaller. Fine: it is a value, not a jump, and it is common to V_1, V_2 unless J wraps.

(6) *The tail against the cubic energy, when the far cell lies in a zone where F is large only because of a far instanton.* Then it is a real contribution to the bound, and it is small: it is exponentially weighted. Summing over i: sum_i w_i(y) <= C_w, so at most C_w |F(y)|^3 for that y. Yes.

(7) *K is reflection-even only after the average. Is the average legitimate in Lemma O3, where H_i and the order interact?* Taylor is applied for each O; averaging is the last step. In sectors the sum over O of a local form at each i is still local. Yes.

(8) *Non-commuting F and LIFT-I, Step 1.* D'^* lambda = 0 is covariant, and Q = Q^o + D' Phi is in (AD)'s setting with a background: Phi := -avg_x cs_x, D' f (c) := Ad(V') f(y') - f(y). Conservation of lambda in the covariant form is what gauge invariance of A_n gives, exactly. Yes. The non-abelian residual is in (AD).

(9) *A hidden first-order term of Z in sectors?* D g_i(1) = 0 only at V' = 1; at a sector field the "first order" is at the cut field, in the ball, and the Taylor is at 1. Yes. And at (LIFT-I) Step 3 a first-order term in lambda has the factor grad F. Yes.

(10) *Can C(L) in SRC depend on the sector through the gas?* Theorem Z and (A1') have constants free of the sector, once this note is in place. Circularity: Theorem Z at level j reads (VAL_j) and (Jump) at level j - 1 in Step 4, and SRC at level j reads the gas at level j. The order in the induction is: H(j) with (VAL_j), (Loc^c_j); Theorem Z at level j + 1; gas; SRC at level j; so (VAL_{j+1}). No circle.

(11) *B_n, B_v and constants' order.* B_v(L) comes after C(L) in SRC, with C(L) depending on B_n(L) through g_j^2 B_n <= 1 only. So B_v(L) is fixed before a_*, or, if it needs a_*, as C(L, a_*) it enters only (FF_j)(U) and Step 4, which are absorbed by x. x_* comes last. Fine.

(13) *The rate in Lemma O2.* S_t's Hessian is a convex combination of two operators, each with an absolute rate by Theorem F-D. That does not give an absolute rate for the combination: only Combes-Thomas, from its two-sided bound, so a rate mu_c(L) falling with L. So read Phi in O2, in the tail of O3 and in (Loc^c) at a rate mu_c(L) <= mu, and w_x at a fixed fraction of it. Does anything need the absolute rate? (a) r_* >= (c/T_2)^{1/2} and mu_c(L) r_* is large, as a_* comes after L. (b) r_1 := (2/mu_c) log(1/T_2). (c) LIFT-I smears by e^{-rho d} with rho absolute, and a slower weight is unchanged by this. (d) (Loc^c) recursion: the factor is C^n L^{4 - n} e^{-mu_c (L - 1) r'/2}, which is below 1/2 only for r' >= r_min := C log L/(mu_c L); below r_min, the trivial bound holds if D_n >= 2 B_n e^{mu_c r_min/2}. So D_n changes, not the form, and C_w(L), B_v(L), B_j(L) depend on mu_c(L). Fine: all these come before a_*, except that r_1 reads T_2. So B_j's J^+ is larger by a factor (log 1/T_2)^4, read only through n, with C(L, a_*) n log x already there.

(12) *What I have not done.* The reflection extension pattern by pattern on the staircase; a written estimate for g-hat in the non-abelian background beyond its symbol; the fine-level Weitzenboeck in lattice form, whose lattice Bianchi term I bounded by a count; a test of SRC in d = 4 or in SU(2) in any sector.
