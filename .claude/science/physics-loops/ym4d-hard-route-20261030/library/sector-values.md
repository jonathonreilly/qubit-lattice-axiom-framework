# Values of R_k across topological sectors

Own derivation, 2026-10-31; not reviewed. Part: `hard-core--mapped`. Answers D4 of `gates/theorem-z-3b7fd4e57.md`. Balaban's objects are kept (block averages, minimal fields, running coupling); the ordered integration below is standard in cluster expansions and is not taken from his text. This line is not independent of the Sussman-Alpoge repository, which supplied the map; this argument does not read it. Nothing here reads the sibling attempt.

Status, by part. Section 1: exact identity, derived. Section 2: derived at the level of each term. Section 3: kept, with the reading corrected by Section 3A. Sections 3A, 3B: the route that replaces a per-level contraction, derived at the level of each term, with (TS) exact. Sections 4 to 6: implications of those. All rest on Theorem F-D, HS-P, HS-T, (R3), (AD), Prop AN3 at their own labels, none gated. So this is a route that has been written out and attacked twice, and not a closed proof.

## 0. The problem and the decision

Item (r) of `library/relative-density-bound.md` said that two class fields equal off J are joined by a path of flux at most C T. *False across sectors* (the gate's D4, which I confirm): an instanton of radius about T^{-1/2} in singular gauge, cut off inside a ball J, has flux at most T and equals 1 off J, and no path of small flux joins it to 1. R_k is known only by derivative norms on D_k, so nothing bounded the difference of its values between sectors. Readers: Step 4 of Theorem Z; (FF_j)(Lo), (FF_j)(U); Lemma 3 of `library/gauge-taylor-contraction.md`, through "a path of class fields"; and also (RP_m[i]) at Steps 2 and the tail clause, so the fallback is hit by the same defect.

*Decision.* The one-function formulation carries it. R_k stays one function in the hypothesis, with no local polymer representation. Two clauses are added: a value clause (VAL_k), with its region form (VAL^𝔡_k), which needs no local form of R_k, and a locality clause (Loc^c_k), in a form with class fields only. Both are outputs of one sum over levels, Sections 3A, 3B. A local decomposition is used only for the *one-step source*, which is computed afresh at each level, so the surface excess of the older recursive density (`parts/hard-core--mapped.md`, routes tried) does not arise.

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

*Read this section with n := k and any lower level, Section 3A (a): it is not to be iterated, and C_0 L^-2 < 1 is not needed.*

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

## 3A. No contraction per level: a direct sum, and a telescoping sum (derived at the level of each term, 2026-10-31)

*Correction to Section 3.* I called (LIFT-I) the hardest inequality, because I read it as a contraction C_0 L^-2 < 1 to be iterated level after level, with room only in L. That reading was wrong, in two ways, and the correction is the main result of this stop.

**(a) Nothing needs iterating.** Steps 1 to 6 of Section 3 apply with n := k, the top level, directly to any lower level j: Step 5 is a convolution from the fine level. So, for the chain of V, with s := L^{j - k}, sum over c in the shadow of a top cell c_k of (|grad F_{V_j}(c)|^2 + |F_{V_j}(c)|^3) <= C_0 s^2 ( I_k(V; w_{c_k}) ), **with C_0 free of j and k, and with no requirement that C_0 L^-2 < 1**, since the sum over levels is then C_0 / (1 - L^-2). The abelian numbers show this: C(4, 3, n) = 16.96, 16.01, 16.00 at n = 1, 2, 3, against 16.96^n L^-2n-type compounding that the iterated form would allow. So only uniformity of (AD), (R3), AN1 in the level is read. Those are composite statements already.

**(b) A second route, with no H^2 at all: the Wilson excess telescopes.**

*Definition.* A_l^W := Wilson action of the level-l field. Y_l := A_l - A_l^W on D_l, so Y_0 = 0. e_j(V') := A_j^W(V^*(V')) - A_{j+1}^W(V'). Then, since A_{j+1}(V') = A_j(V^*(V')),

    Y_{j+1}(V') = Y_j(V^*(V')) + e_j(V'),    so    Y_k(V) = sum_{j<k} e_j(V_{j+1}).        (TS)

Exact, in every sector. So if e_j dominates the gradient energy of its parent, the sum over all levels of the gradient energy is bounded by Y_k(V) at the top, which is a one-level-of-reading statement. For a weight W on top cells, with E_l(V; W) := sum_c W(c) |theta_c|^2, e_j(V'; W) := E_j(V^*(V'); W) - E_{j+1}(V'; W) telescopes in the same way.

**Lemma EX (coercivity of the excess; level of each term).** *For V' in D_{j+1}, f := its largest flux, W with log W Lipschitz at rate nu in cells of level j + 1:*

    e_j(V'; W) >= c_1 I^grad_{j+1}(V'; W) - C(L) (f + nu) E_{j+1}(V'; W) - (toron term),

*with c_1 > 0 and C(L) free of j.*

*Step 1, a local density.* epsilon_{c'}(V') := sum over c in the shadow of c' of |theta_c(V^*(V'))|^2 - |theta_{c'}(V')|^2. It is gauge invariant and, by Prop AN3 and Theorem F-D, local with tree decay, uniformly in j. Taylor at the locally trivial cut field, as in Lemma O3, with D epsilon(1) = 0, gives a quadratic part, order-3 and tail terms at most C(L) times the cubic energy. Averaged over the hypercubic group with reflections, which leaves the sum unchanged, this gives K, translation invariant, reflection even, with K-hat(P) on all six orientations.

*Step 2, the symbol.* K-hat(0) = 0 on all 2-forms: it is a multiple of the identity, by symmetry, and on constant flux the lift is exact (Lemma 3.3 of the producer), so the excess vanishes. By evenness K-hat(P) = O(|P-hat|^2) on all 2-forms. *On closed forms it is coercive, uniformly in j:* the level-j field of the lift lies in the fibre, so its Wilson energy is at least the one-level minimum, whatever A_j is:

    F-hat^* K-hat(P) F-hat >= (g(P) - 1) |F-hat|^2 >= c_e |P-hat|^2 |F-hat|^2,    F-hat = P-hat ^ a,

with g the one-level minimal Wilson energy, an exact finite alias sum. From the main alias, with D the Dirichlet kernel and m equal non-zero components of P, g = D^-(2m + 2) when a points along a zero component, so c_e = (m + 1)/(12 m) (1 - L^-2), least at m = 3 in d = 4: **c_e = (1/9)(1 - L^-2)**. Measured over a grid, including small P: 0.09883, 0.10675, 0.10893, 0.11029, 0.11082 at L = 3, 5, 7, 11, 17 (`checks/hard-core--mapped_excess.py`). (1/9)(8/9) = 0.09877. It is a finite computation for fixed L; I have not written a proof over all P beyond the numerics and the main alias.

*Step 3, all 2-forms.* Closed forms are a subspace. For M large, K-hat_M(P) := K-hat(P) + M (P-hat ^)^* (P-hat ^) >= (c_e/2) |P-hat|^2 on all 2-forms: the closed block is at least c_e |P-hat|^2, the off-diagonal block is at most C |P-hat|^2, the co-closed block gains M |P-hat|^2, so Schur applies with M = M(C^2/c_e). So, by Plancherel on the flat torus, for every 2-form psi with values in su(2), of no closedness,

    Q_flat[psi] + M ||d psi||^2 >= (c_e/2) ||grad psi||^2.

*Step 4, covariance, by IMS at the scale where sectors do not exist.* Partition of unity eta_a at radius r := f^-1/2, in the balls of which an axial gauge has |A| <= f r. Apply Step 3 to psi_a := eta_a F in that gauge. Three errors. (i) IMS: C(L) r^-2 ||F||^2 = C(L) f ||F||^2. (ii) Transport: T_{x -> x + y} - 1 is of size f r |y|. Its first-order part is ad of a small element tau. It pairs psi(x) with psi(x + y) = psi(x) + Delta_y psi. The part with psi(x) cancels, as psi_p . [tau, psi_p'] is antisymmetric in (p, p') and K(y)_{pp'} is symmetric, by evenness. So what remains is f r |psi| |Delta psi| + (f r)^2 |psi|^2, at most epsilon |grad psi|^2 + C(L) f |psi|^2. *This cancellation is what makes r^-2 and (f r)^2 balance at r = f^-1/2, the scale of sectors. So F is treated only locally, and no global gauge or sector enters.* (iii) Bianchi: F is the curvature, so d_{V'} F = O(|F|^2) at each cube, and M ||d_{V'} F||^2 <= C(L) sum |F|^4 <= C(L) f E. Sum over a. With W: apply the same to W^{1/2} F; the commutator with the slowly varying W is at most epsilon |grad F|^2 W + C(L) nu^2 |F|^2 W, and W at the fine level against W at the parent adds nu E_j. QED at this level.

**Lemma TOP (level of each term).** *Uniformly in k, |Y_k(V; W)| <= C(L) ( I^grad_k(V; W^+) + (f + nu) E_k(V; W^+) ), with Y_k(V; W) := E_0(U; W) - E_k(V; W).* The density epsilon^(k)_c := fine Wilson energy of the minimal composite lift on the shadow of c, minus |theta_c|^2, is local with tree decay uniformly in k, by Prop AN3; K-hat(0) = 0 by the exact lift at all levels; so rearrangement as in Section 2 gives this with only an upper bound. So the reading at the top is direct, with no chain.

**Sup flux falls.** f_j <= f_{j+1}/4: non-concentration, Consequence 2 of Prop 10', at threshold f_{j+1} in place of T. Its proof is scale free below T: the trial's energy, Lemma U's smallness, the bump, all scale with the threshold, and L_0 does not change.

**Proposition GS (implication of these three).**

    sum_{j<k} I^grad_{j+1}(V_{j+1}; W) <= B_g(L) ( I^grad_k(V; W^+) + (f_k + nu_k) E_k(V; W^+) ) + (toron term),

*with B_g(L) free of k.* Sum Lemma EX over the chain and use (TS). The errors are C(L) (f_{j+1} + nu_k s_{j+1}) E_{j+1}(V_{j+1}; W), geometric in the level, as E_{j+1}(W) <= E_0(W) + small <= C E_k(V; W^+) by Lemma TOP. **Every constant may depend on L. There is no inequality here that has room only in L^-2.**

*Why (a) and (b) are both kept.* (a) gives each level's term, with s^2. It reads fine-level Weitzenboeck with an L^4 bound on F, and (AD). (b) gives the sum, reading only local Taylor and an exact one-level positivity. (b) is what the value clause reads. The direct sum of Section 3B reads (b) at first variation, and (a) at the field only.

## 3B. Low orders of R_k by one direct sum and an interpolation (level of each term; replaces Sections 5, 6 of the closure for n <= 4)

(CS) has a derivative form. With Lambda_m : D_k -> D_{k-m} the composite lift of m levels, Lambda_0 = id, R_k = sum_{m >= 0} Z_{k-m-1} o Lambda_m. So low orders of R_k need no recursion of their own. They need a bound on one composite, free of m.

**(COMP): what is read of the classical composite, uniformly in the level.** For V in D_k, s := L^-m, theta := plaquette angles of Lambda_m(V), delta_b := derivative along a top bond b, with rate mu in top cells, sums over the cells c of a top cell c_k, constants C(L) free of k, m:

    (i) sum_c |theta_c|^4 <= C s^4 f_loc^4,     sum_c |delta_b theta_c|^2 <= C w_b(c_k),     sum_c |delta^2_{b b'} theta_c|^2 <= C w_{b b'}(c_k);
    (ii) sum_c |grad theta_c|^2 <= C s^2 I_k(V; w_{c_k}).

(i) is (R3) by scale counting, and Prop AN3 in the energy norm. (ii) is Section 3 with n := k, at the field only, where the multiplier is exactly conserved and the comb cancels. *So no H^2 at a variation is read, and no (delta Q^*) lambda.* That is what the attack on this statement found: a first form asked (ii) at first and second variations, and I had named that hardest.

**Lemma EX2 (the sum over levels at first variation; level of each term).** *With b_m(b; W) := sum over level-(k-m) cells of W |grad delta_b theta|^2: sum_m b_m(b; W) <= C(L), for W growing at a rate below the kernel's.* Differentiate (TS) twice along b, with h := Lambda' b, h^2 := D^2 Lambda[b, b]:

    D^2 Y_k(V)[b, b] = sum_j ( D^2 e_j(V_{j+1})[h, h] + D e_j(V_{j+1})[h^2] ).

The left side is at most C(L), by Prop AN3 uniformly in k. In the first term, 2 Q_{V'}[delta F] has delta F nearly closed: d_{V'} delta F = [F, h], at most |F| |delta F| in the gauge at x, so Lemma EX's Steps 3, 4 give at least c_1 b_m - C(L) f ||delta F||^2, and f falls geometrically while ||delta F||_{l^2} is bounded by (i). The second term is <Delta F, K Delta delta_{h^2} F> up to cubic terms, at most C ||grad F||_{l^2} ||delta_{h^2} F||_{l^2} <= C(L) s by (i), (ii). Geometric. So the sum closes, reading no H^2 at a variation. QED at this level.

**Proposition DS.** *Let Z = sum_x zeta(x; .) be gauge invariant on D_{j+1}, with zeta rooted at x in tree-decay norm up to order 4, of size at most 1, zero F^2 coefficient after the rearrangement of Section 2. Then for n = 1, 2, with sum_m read over levels with sources of norm at most 1,*

    sum_m || Z_{k-m-1} o Lambda_m ||_n <= C_n(L).

*Proof.* zeta is the rearranged quadratic part, minus (1/4) sum_y K(y) |Delta_y F|^2, plus c(x; .). In the axial gauge at x a variation of F has link size |delta F|, up to the tree weight, by radial homotopy. So |D c[h]| <= C |F|^2 |delta F|, |D^2 c[h, h']| <= C (|F| |delta F| |delta' F| + |F|^2 |delta^2 F|), by Taylor to order 4 of zeta at x. Sum over a top cell: at order 1, at most (sum |F|^4)^{1/2} ||delta F||_{l^2} <= C s^2 f^2. At order 2, by Hoelder and the lattice Sobolev bound, (sum |delta F|^4)^{1/2} <= C (b_m + s^2): at most C s f (b_m^{1/2} + s) ||delta' F||_{l^2} + C s^2 f^2. Geometric. The quadratic part: at order 1, <Delta F, K Delta delta F>, at most (a_m b_m)^{1/2}, with a_m from (ii), and Cauchy-Schwarz over m with Lemma EX2 and Prop GS. At order 2, <Delta delta F, K Delta delta' F>, at most (b_m b'_m)^{1/2}, the same; and <Delta F, K Delta delta^2 F> at most a_m^{1/2} ||delta^2 F||_{l^2} <= C s. Tree decay: by the weights, with half the rate. QED at this level.

*Orders 3, 4: by interpolation, not by a sum.* For bonds b_1, b_2, b and t := T_2: |D^3 Z[b_1, b_2, b]| <= |D^2 Z(V e^{t b})[b_1, b_2] - D^2 Z(V)[b_1, b_2]|/t + t |D^4 Z[b_1, b_2, b, b]|/2. The difference is at most min( 2 B_2 Phi(d_12/2), C Phi(d(b, {b_1, b_2})/2) ), by (Loc^c) at order 2, which the same sum gives. So D^3 has tree decay at half the rate. Likewise D^4 from D^3 and D^5. So ||R_k||_3, ||R_k||_4 <= C ( T_2^-2 (B_1 + B_2) + T_2 B_5 ), at the rates mu/2, mu/4. Lower rates are enough for these orders, as a lift multiplies a rate by L. **So B_3, B_4 depend on a_*, which is allowed: B's come before x_* and are read only through g^2.**

*The second tier needs no ladder.* A tier of Z_j at rate mu_s in cells of level j + 1 has rate L^m mu_s in top cells, with coefficient zeta_j <= C zeta_k. So it stays inside the profile Phi_k, at every m.

**Consequence: (VAL), (Loc^c) and low orders are one statement.** (VAL_k) is n = 0 of the same count, or Prop GS with SRC. (Loc^c_k) is direct: each term Z_j o Lambda_m is local, in any sector, by Lemma O2 and Theorem F-D, so no recursion is needed for it, and Section 5 below is a second proof. See `library/one-step-closure.md`, Section 10.

## 4. The value clause

**Theorem VAL (implication).** *Given SRC and Prop GS, for all k and V in D_k, in every sector:*

    |R_k(V)| <= B_v(L) ( I^grad_k(V; 1) + f(V) E_k(V) + N_k^4 Phi(e^-8 N_k / 4) ),    f(V) := the largest flux of V.

*Proof: (CS); SRC at each level; Prop GS for the gradient parts; the cubic parts are at most f_{j+1} E_{j+1}, geometric by "sup flux falls". The toron term falls superexponentially going down, as N_j = L^{k-j} N_k. Every constant may depend on L.*

For an instanton of radius rho at level k, this is B_v rho^-2 <= B_v T: the lattice artefact (a/rho)^2 in the instanton's action, as it should be. So there is no constant per unit of charge. (FF_j)(Lo), (FF_j)(U) read this.

**(Jump) is not consumed.** An earlier form of this section proved |R_k(V_1) - R_k(V_2)| <= B_j T_2^2 |J^+| for fields equal off J, by a near and a far zone, and I had put it in H(k). Attacking its far zone found that it needed a telescoping of the difference field, with the difference read at each level. Then I saw that the one consumer, Step 4 of Theorem Z, does not need it: in Step 4 the region is everything inside Sigma, nothing is integrated beyond it, and the crude bound C n is all that is asked. So Step 4 reads (VAL^𝔡) of Section 6, and (Jump) is removed from H(k). It is likely true, and I do not claim it.

## 5. (Loc^c_k): locality back in the hypothesis, class fields only

**(Loc^c_k).** For V, V'' in D_k equal on B(y, r) in a common gauge, and n <= N - 1:

    | D^n R_k(V)[y, b_2, ..., b_n] - D^n R_k(V'')[y, b_2, ..., b_n] | summed over b_i in B(y, r/2), with weight 1/Phi(tree/2), <= D_n(L) Phi(r/2).

*Recursion (level of each term).* R_{k+1} = R_k o V^* + Z_k. For Z_k: O2 and Prop AN3 on the ball, with S_t. For R_k o V^*: chain rule through the lift, which reads D^m R_k at V^*(V'), V^*(V''). Those two agree up to e^{-rho (r' - d')} on the shadow of B(y', r'), by Theorem F-D on the ball with parents equal; interpolate to a field that equals one on an inner ball and the other outside, as in Theorem Jump. The result is C^n L^{4-n} D_n Phi(L r'/2) from the old constant, with the improved distance L r', so a factor e^{-mu (L - 1) r'/2} against C^n L^{4 - n}, for r' >= 1; and from the closeness a source B_{n+1} C(L) e^{-rho r'}. For r' < 1 the bound is trivial if D_n >= 2 e^{mu} B_n. So D_n(L) := max(2 e^mu B_n, 2 C_n(L) B_{n+1}) closes, free of k, for L >= L_0. It reads ||R_k||_{n+1}, available for n <= N - 1.

*Lemma 3 of the Taylor note, corrected.* Its proof read "at s = 0 the field is trivial on a ball of radius r/2, so its derivatives differ from those of the trivial field by C e^{-mu r/2}: this needs only tree decay ... along a path of class fields". Across sectors there is no such path. The step now reads (Loc^c_k), which has no path. Separately, its flux factor 1 + C a r^2 omitted d chi ^ A, which is of order a |x| |grad chi|. With the logarithmic cut-off, the factor is at most 5/4 for a r^2 small, at a fixed loss in r. So its statement needs the formula range to have that room. T_2 is fixed only through a_* small, so H(k) is stated on D_k with T_2 enlarged by a fixed factor 5/4. Nothing else in the closure reads this constant.

## 6. With boundary data: the region clause

Theorem Z's Step 4 reads values only inside a layer family. Define, for class W on the free part R_l^𝔡, with a reference W_ref(𝔡) fixed by the data:

    R_l^𝔡(W) := [F_l^𝔡 - x_l A_l^𝔡](W) - [F_l^𝔡 - x_l A_l^𝔡](W_ref).

**(VAL^𝔡_l).** *|R_l^𝔡(W)| <= B_r(L) n, with n the number of free bonds at level l, uniformly in 𝔡 and l, in every sector.*

*Chain.* V_l := W, and V_j := the region minimiser on the fibre of V_{j+1} between the layers. All class, as the layers are quiet. By the same subtraction as (CS), with the region's own one-step sources, R_{j+1}^𝔡(V') = R_j^𝔡(V^{*,𝔡}(V')) + Z_j^𝔡(V'). So R_l^𝔡(W) = sum_{j<l} Z_j^𝔡(V_{j+1}), and nothing is integrated beyond Sigma, so there is no far zone.

*Interior.* Let W_0 be a top-level cut-off on the free cells, with rate about 1/r_S. Under free level-l cells there are no lower layers, beyond a margin r_S, by clearance. SRC holds there, with the ordered integration in the region, and Prop GS with the weight W_0: the sum over levels is at most C(L) (T_2^2 + nu) n.

*Near a lower layer.* Let Sigma_{j+1} be a layer below the top. It lies under frozen parents, and free parents are at least r_S away. So V_{j+1} near Sigma_{j+1} depends on W only through a kernel across r_S: if delta_{j+2} is the size of the dependence one level up, then delta_{j+1} <= e^{-delta_# r_S} delta_{j+2}. The boxes near that layer have one-step sources bounded by C(L), and their dependence on W is at most C(L) delta_{j+1} per box. Number of cells of the layer at m levels down: L^{3 m} |surface|. So their total is at most sum_m C(L) (C L^3 e^{-delta_# r_S})^m |surface|, and C L^3 e^{-delta_# r_S} <= 1/2 by r_S >= (4 log L + C)/delta_#. So this part is at most C(L) |surface| <= C(L) n. *These surface sources are large in themselves, as data next to a sheet do not scale down; their part that does not depend on W goes into the reference and cancels.*

*At the top face.* Boxes next to Sigma_l: at most C(L) per box, by O1. QED at this level.

Bulk derivative norms are as before: R_l at a class extension plus Delta R_l^𝔡, with contraction by clearance. That split serves derivatives only. Values read the chain above.

## 7. Numerics

Criteria written first, in each script. All under the lock.

`checks/hard-core--mapped_sector_value.py`: d = 2 U(1), block-constrained covariant Laplacian determinant, lift by hand. **PASS, run once.** Gauge invariance exact; power control: a non-gauge change moves G by 1.0. kappa from sectors 1, 2, 3: -0.001032, -0.001033, -0.001033, against -0.001061 from a slowly varying field in sector 0 at p = 2 pi/16 (criterion 3 percent, met). |Z|/I in a patch of charge one, n = 4, 6, 8, 10: 0.0002, 0.0003, 0.0003, 0.0003; in a neutral pair: 0.0002 at all n. |Z| in the charged patch falls like 1/n^3 with I. Two far charged patches: Z(two) = -3.97731e-04, 2 Z(one) = -3.97731e-04. So *no jump, and exact additivity, in the simplest case with sectors.* Limits: U(1), d = 2, one level, one-loop.

`checks/hard-core--mapped_lift_gradient.py`, the abelian (LIFT-I): **FAIL on L2, on caps I had guessed.** L0: comb against line-only, 7e-13, 9e-13 in plaquette angles; the Fourier ratio against a direct solve, all digits printed. L1 passes. L3 passes, R at most 0.85. L2: C(4, L, 1) = 16.96, 30.28, 37.56, 41.57, 43.93 at L = 3 to 11, above the cap of 30, with C(11)/C(7) = 1.17 above 1.15. Composite: 16.96, 16.01, 16.00 at L = 3, n = 1, 2, 3; 30.28, 26.02 at L = 5, n = 1, 2. Follow-up `checks/hard-core--mapped_lift_gradient_limit.py`: **FAIL on M3 only.** C = 45.41, 47.06, 47.90, 48.81 at L = 13, 17, 21, 31, with falling increments; a fit at L = 9, 11 alone gives C_inf = 48.70 and predicts C(31) within 1.5 percent. Symbol g in [1.026, 12.09], above my cap of 10. **So in the abelian sector C_0 is about 50, with no growth in L or in the number of levels: a measurement, on a grid of momenta, with its peak at the zone corner.** With that, C_0 L^-2 <= 1/2 for L >= 10.

`checks/hard-core--mapped_lift_su2.py`: **PASS, run once at these criteria** (smoke runs before it fixed the solver: my first block map had a linear gauge rotation from the jet check, not gauge covariant, which made SQP drift along gauge directions). d = 2, SU(2), one level, the comb, a true constrained minimiser; constraint residual at most 2e-12 and projected gradient at most 4e-6 wherever converged. Commuting parents: R = 2.0014, 2.1434 against the abelian 2.0194, 2.1626, and the difference is the cubic share of the denominator, 0.9 percent. Non-commuting, random low modes: R between 2.7 and 9.4 at L = 3, 5, 7. X(0.05) between -0.0045 and -0.0057, and X(0.1) between -0.011 and -0.014, which is about minus the change in the denominator's cubic share, 1.5 to 2.2 percent, so the true excess is under half a percent at L f^2 = 0.07. One case, L = 3, seed 2, f = 0.1, did not converge and is not used; f = 0.2 failed in a smoke run, as the Gauss-Newton Hessian omits lambda D^2 M. **So no non-abelian excess is seen, and the count (AD) is far from saturated on these parents. This is weak evidence:** d = 2, low modes, random and not adversarial, one level, and the d = 4 count differs.

`checks/hard-core--mapped_excess.py`, on Section 3A: **PASS** (a first run was stopped: its toy and SU(2) parts used the d = 4 normalisation in d = 2, so the excess came out negative; fixed, criteria unchanged). E1: c_e as above. E2: at (L, n) = (3, 2), (3, 3), (5, 2), E_(n) - E_(1) >= 0 as forms, control 6e-15. E3: |Z|/e in the toy with sectors: 0.01036 to 0.01018 for a charged patch at n = 4 to 10, 0.00841 to 0.00837 for a neutral pair; so the source is dominated by the excess, at the same ratio in both sectors. E4: SU(2), d = 2, non-commuting parents, a small random search: smallest e/|grad' F'|^2 = 0.02339, 0.02341, 0.02346 at L = 3, f = 0.02, 0.05, 0.1, and 0.00942, 0.00949, 0.00973 at L = 5, against the abelian 0.02339, 0.00941. So the non-abelian ratio does not go below the abelian bound on these parents. Six solves at f = 0.1 did not converge, and are not used. Weak as a search, as before.

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

(14) *Attack on (TS) and Lemma EX: does e_j have the right sign at level j, when V^* minimises A_j and not A_j^W?* Lemma EX does not use minimality for A_j^W. It uses that the lift lies in the fibre, so it is at least the one-level Wilson minimum, at second order at flat data. E2 checks this for composites. Yes.

(15) *Attack: K-hat(0) = 0 "on all 2-forms" from constant flux.* Constant flux in the Cartan direction has an exact lift, for all orientations of plaquette at once, if the constant 2-form is closed, which any constant is. So F-hat at P = 0 is any 2-form in one colour. Non-commuting constants are not exact, but at second order only one colour at a time is read, by polarisation in colour. Yes.

(16) *Attack: IMS at r = f^-1/2 when f is the global maximum and most of the field is much smaller.* The error is then pessimistic: C(L) f E, with f set by one hot cell. A local scale would be sharper, and nothing reads that.

(17) *Attack on a first form of Prop DS for n <= 4: the term <Delta D^2 F, K Delta D^2 F> at n = 4 read H^2 at second variation, and <Delta delta F, K Delta D^2 F> at n = 3 needed a sum of b_m^{1/2}, which Lemma EX2 does not give.* So the sum stops at n = 2, and orders 3, 4 go by interpolation with order 5, reading (Loc^c) at order 2. The cost is rates mu/2, mu/4, and B_3, B_4 depending on a_*. *Attack on that:* does anything read B_3, B_4 before a_* is fixed? Section 4 of the closure has C_n(L) times lower norms, so B_5 <= (1/4) B_5 + C_5(L) (C T_2^-2 B_2 + C T_2 B_5 + 1): this needs C_5(L) C T_2 <= 1/8, as a_* comes after L. Then B_5 depends on a_*. It is read only through g^2, as x_* comes last. No circle.

(18) *Attack: order loss in Z_j.* The mean term has <R_j o Phi> - R_j o V^* of size g^2 ||R_j||_{n + 2} at order n. So Prop DS, which reads Z_j to order 4, reads ||R_j||_{<= 6}. That is why orders 5, 6 keep the recursion of Section 4 of the closure, with its room L^{4 - n}: they cannot be done this way. So closure reads C_1 absolute at orders 5, 6 still. See Section 10 there.

(12) *What I have not done.* The reflection extension pattern by pattern on the staircase; a proof of c_e > 0 over all P, beyond the main alias and a grid; the fine-level Weitzenboeck in lattice form for (COMP)(ii), whose lattice Bianchi term I bounded by a count; a test of SRC in d = 4 or in SU(2) in any sector; a test of Lemma EX2 in SU(2) at two levels.
