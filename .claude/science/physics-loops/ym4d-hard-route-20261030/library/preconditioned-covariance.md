# A covariance bound whose rate does not see the gap

Own derivation, 2026-10-31; not reviewed. Part: `hard-core--mapped`. The formula for a covariance through a Witten-type operator goes back to Helffer and Sjostrand, and the commutation with a generator is Bakry and Emery's; I re-derive what is used. The idea of changing the metric to a constant one adapted to the Hessian, and the weighted energy estimate below with a cut, I have not looked up.

**Why it is needed.** In tree-gauge coordinates the Hessian on a fibre has gap gamma(L) ~ L^-2/C_tree(L). The standard bound on Cov(f, h) in a log-concave law, by Combes-Thomas with the Euclidean metric, then gives a rate per box that falls with L. The consumer (the upper chain's (MD_j), through its kappa := c'_t/8) needs a rate free of L. The Gaussian rate is in fact free of L: `checks/hard-core--mapped_chart_rate.py` finds about 1.5 per box at L = 3, 5, 7, 9 in d = 2, while the gap falls by a factor of 20. The difficulty is to keep that rate for the non-Gaussian law, with a compact cut.

## Hostile check of Lemma HS-M, before its numerical test (2026-10-31): hypothesis (W) should fail in the chart, and a simpler form replaces it

*The failure I expect.* A parent's constraint has support in two adjacent boxes, and in the chart it is solved on a designated bond, with coefficient 1/w_d about L^{d-1}. A weight Theta that differs between the two boxes moves a low-energy xi off the constraint: Theta M Theta^-1 - M contains the designated bond's spike, of size rho L^{d-1} S_2, with S_2 the partial sum of the line average in the second box. S_2 is about L times a typical bond angle c, and the energy is c^2 L^{d-2}. So eps_1 grows like rho L^{d-1}, not like rho. No choice of a box-wise diagonal weight avoids this, as constraints overlap in every direction. The same holds for a soft constraint with a large penalty. The check W1, W2 of `checks/hard-core--mapped_chart_rate.py` was written before this estimate; it decides. **Result: W1, W2 FAIL**, as predicted in kind, and worse in size: at d = 2, eps_1(0.2) = 0.44, 1.73, 5.28 at L = 3, 5, 7, about L^3, not L; eps_1(0.1) = 0.20, 0.68, 1.74, so it is also not linear in rho at the larger L. The l^1 norm of a designated row of T is 6, 20, 42. So in this chart (W) holds only at a slow rate rho_s = rho_s(L), about 0.1 L^{-5/2} at d = 2. The same run: R1, R2 PASS, with the rate of M^-1 per box 1.52, 1.49, 1.49, 1.50 (S1) and 1.76, 1.57, 1.49, 1.46 (S2) at L = 3, 5, 7, 9, d = 2, while the gap is 0.268, 0.066, 0.025, 0.012; and at d = 3, 2.40, 2.67 at L = 3 and 2.60, 2.53 at L = 5. The run's overall verdict is FAIL, on W1, W2, and, narrowly, on R0: the residual of the iterative solve for S2 at d = 3, L = 5 was 1.2e-8 against the stated 1e-8. So that one rate is at reduced accuracy. *A way to improve rho_s, not used:* solve constraints on a smooth bump instead of a designated bond. Then the spike goes, and what remains in (W) is the tree-gauge constant through partial line sums.

*What survives.* The conclusion does not need (W). M^-1 has the fast rate (numerics R1, R2, and Theorem F of `library/fibre-propagator.md`). Below, the metric enters only through A = M^-1, and the weight acts on plain l^2.

## Lemma HS-P (plain weighted norm, no cut; replaces HS-M in the use on a fibre)

*Setting.* S in C^2(R^n), Hess S(xi) = M + V(xi), M constant and positive definite, A := M^-1. mu proportional to e^{-S}. Theta constant, diagonal, positive. Hypothesis, for all xi:

    (A)  || Theta A V(xi) Theta^-1 ||_{l^2 -> l^2} <= 1/2.

*Conclusion.* |Cov_mu(f, h)| <= 2 ||Theta^-1 D f||_{L^2(mu; l^2)} ||Theta A D h||_{L^2(mu; l^2)}.

*Proof.* As in HS-M, with L_A u = h - mu(h), w := A D u, one has L_A w + w + A V w = A D h, with L_A acting on each component. L_A is non-negative on L^2(mu) for each component, so sum_i int w_i L_A w_i d mu >= 0, and L_A commutes with the constant diagonal Theta. So w-tilde := Theta w solves (L_A + 1 + Theta A V Theta^-1) w-tilde = Theta A D h, and by (A), ||w-tilde|| <= 2 ||Theta A D h||. And Cov(f, h) = int (D f)^T w d mu. QED

So the rate is that of A, and V enters only through the size of (A). Note what this does not ask: any relation of Theta to the constraint. The prefactor is in plain norms, so it can carry C(L), which (MD_j) allows; only the rate must be free of L.

*The cut, by extension and a Mayer expansion (a first form; a count only; Lemma HS-C below is what I can write).* The law on a fibre has a compact cut K, a product over cells, and S is defined on a larger product K_2 where it is convex. A barrier does not fit HS-P, since A B is not accretive in plain l^2. So remove the cut. Let T := S - Q_M, with Q_M quadratic of Hessian M. Hess T = V is small on K_2. Let Pi be the product of cell-wise retractions pi_c of R^{n_c} into the ball of K_{2,c}, the identity on K_c, smooth at scale rho_c, the radius of the cut. Put S-tilde := Q_M + T o Pi. Then Hess S-tilde = M + V-tilde, with V-tilde = D Pi^T (V o Pi) D Pi + sum_c D_c T o Pi . D^2 pi_c. The second term is block diagonal, of size |D_c T|/rho_c, and |D_c T(xi)| <= |D_c T(0)| + (size of V) max|xi|. So it is of the size of V plus the gradient at the reference over rho_c, which is small by (H3). Tree decay of V carries over to the first term. So (A) holds for S-tilde on all of R^n. (An earlier extension of the action, the Huber form, was dropped because it needed a domination between actions, with a signed remainder. Here no comparison of actions is made: T o Pi = T on K, and the difference is handled exactly below.) The true law is mu-tilde conditioned on K. Then Z_K = Z-tilde E_{mu-tilde}[prod_c (1 - eta_c)], with eta_c the indicator of failing the cut at c, or a smooth version. Expand the logarithm by Mayer: log E[prod (1 - eta_c)] is a sum over connected sets of Ursell functions of the eta_c. Under mu-tilde each eta_c has mean at most z_c by Gaussian concentration, since S-tilde is uniformly convex, and the truncated expectations have tree decay at the rate of A, by HS-P applied with the split at the largest edge of `library/convex-laplace-tree-decay.md`, with ||D eta_c||_{L^2} <= poly z_c^{1/2}. So this logarithm converges, with no floor: its dependence on far data decays at the rate of A with a factor z^{1/2}. Status: the Ursell bound is a count, not written with its combinatorics.

## Lemma HS-C (the cut, in two tiers; replaces the Mayer expansion above as the form I can write; proved given its hypotheses)

The Mayer expansion above is a count: its Ursell functions, for a non-product base measure, have a factorial I have not beaten for large sets. Here is a form with no series.

*Setting.* mu on K = product of K_c, with S = S_0 + sum_c psi_c, psi_c a convex barrier, Hess S_0 = M + V, B := Hess of the barrier, block diagonal. Two weights. Theta_s, of rate rho_s, for which (W), (V) of HS-M hold. Theta_f, of rate rho_f, for which (A) of HS-P holds, and its dual, ||Theta_f V A Theta_f^-1|| <= 1/2. Let zeta_c := E_mu[ ||B_c|| ], the barrier's mean curvature at c. For a hard cut this is a boundary integral, at most poly z_c.

*Conclusion.* For f with D f bounded and supported near a set S_f, h with support near S_h, d := their box distance:

    |Cov_mu(f, h)| <= C ( e^{-rho_f d} + (sup_c zeta_c)^{1/2} e^{-rho_s d} ) ||D f||_{L^infinity} ||D h||_{L^2(mu; M^-1)},

with C depending on L and on the sizes of S_f, S_h, through the rate of M^-1 and the number of cells near S_f.

*Proof.* (1) Slow tier, HS-M with Theta_s: Term 4 is kept, not dropped, so besides ||Theta_s w||_{L^2(M)}, also E[ sum_c theta_{s,c}^2 w_c^T B_c w_c ] <= 4 ||Theta_s D h||^2_{L^2(M^-1)}. With Theta_s = exp(rho_s d(., S_h)) this is the barrier energy of w, with decay at rate rho_s away from S_h. (2) Fast tier. Put G := (L_A + 1 + A V)^-1. It is bounded on L^2(mu; l^2), and on L^infinity(mu; l^2), in the norm with weight Theta_f, for both G and G^*: L_A's semigroup is Markov, so |e^{-t L_A} g|_{l^2} <= e^{-t L_A} |g|_{l^2} pointwise, and the rest is small by (A). From L_A w + w + A V w + A B w = A D h: w = G A D h - G A B w. So

    Cov(f, h) = E[D f^T w] = E[D f^T G A D h] - E[ (A G^* D f)^T B w ].

The first term is at most C e^{-rho_f d} ||D f|| ||D h||, by HS-P's weighted bound. In the second, zeta_f := A G^* D f is bounded pointwise, with decay at rate rho_f from S_f, since D f is bounded and supported there. By Cauchy-Schwarz over cells, the second term is at most ( E sum_c zeta_{f,c}^T B_c zeta_{f,c} )^{1/2} ( E sum_{c near S_f} w_c^T B_c w_c )^{1/2}, up to tails. The first factor is at most C (sup zeta_c)^{1/2}. The second is at most C e^{-rho_s d} ||D h||_{L^2(M^-1)}, by (1). QED

*What the two tiers mean.* The fast rate is the propagator's. The slow one is a correction of relative size z^{1/2}: the cut is reached with probability z, and then the constraint's rigidity carries the effect with a weaker bound. It is a bound, not a claim that the slow tail is there. *rho_s:* a negative power of L, from the designated bond's spike (measured above at d = 2). For the consumer, x |A|^C z^{1/2} e^{-rho_s D} is tiny at small D, and it is the larger tier only at D above log(1/z)/rho_f. To sit under a stretched exponential exp(-kappa (n lambda)^{1/2}) for all n: the excess kappa (n lambda)^{1/2} - rho_s n is largest at n = (kappa/(2 rho_s))^2 lambda, with value kappa^2 lambda/(4 rho_s). So one needs log(1/z^{1/2}) >= kappa^2 lambda/(4 rho_s), that is lambda_j <= 4 rho_s log(1/z^{1/2})/kappa^2. The upper chain's C_R must be taken of order 1/rho_s, which is allowed, since l_0, l_1 come after L.

## Lemma HS-M (true as stated; its hypothesis (W) is expected to fail on a fibre; see above)

*Setting.* xi in R^n, partitioned into cells c. Boxes are unions of cells. S := S_0 + sum_c psi_c(xi_c), on K := product of K_c, where K_c is convex and open, and psi_c is convex, C^2, and tends to infinity at the boundary of K_c. Let mu be proportional to exp(-S) on K. Let M be a constant positive definite matrix, A := M^-1, and write Hess S_0 (xi) = M + V(xi). Let Theta be diagonal and positive, *constant on each box*. Norms: ||x||_M^2 := x^T M x, and ||eta||^2_{M^-1} := eta^T A eta. Hypotheses, for this Theta and with eps_1 + eps_2 <= 1/2, for all x, y and all xi in K:

    (W)  | (Theta^2 x)^T M y - (Theta x)^T M (Theta y) | <= eps_1 ||Theta x||_M ||Theta y||_M,
    (V)  | (Theta^2 x)^T V(xi) y | <= eps_2 ||Theta x||_M ||Theta y||_M.

*Conclusion.* For f, h in C^1(K), with the norms finite,

    | Cov_mu(f, h) | <= 2 ( int ||Theta^-1 D f||^2_{M^-1} d mu )^{1/2} ( int ||Theta D h||^2_{M^-1} d mu )^{1/2}.

*Proof.* Let L_A u := -tr(A D^2 u) + (A D S)^T D u, symmetric in L^2(mu), with form int (D u)^T A D v d mu; the barrier keeps the mass off the boundary, so there is no boundary term. Solve L_A u = h - mu(h), and put w := A D u. Then Cov(f, h) = int (f - mu(f)) L_A u d mu = int (D f)^T w d mu.

Differentiating: D_k (L_A u) = L_A (D_k u) + (Hess S A D u)_k. Multiply by A: with L_A acting on each component of w,

    L_A w + A Hess S w = A D h,   and A Hess S = 1 + A V + A B,   B := sum_c Hess psi_c >= 0, block diagonal over cells.

Pair with (Theta^2 w)^T M and integrate:

Term 1: int (Theta^2 w)^T M L_A w d mu = int sum_alpha (d_alpha w)^T Theta^2 M (d_alpha w) d mu, where A = sum_alpha e_alpha e_alpha^T and d_alpha := e_alpha . D. By (W) with x = y = d_alpha w this is at least (1 - eps_1) int sum_alpha ||Theta d_alpha w||_M^2 d mu >= 0.

Term 2: int (Theta^2 w)^T M w d mu >= (1 - eps_1) int ||Theta w||_M^2 d mu, by (W).

Term 3: int (Theta^2 w)^T M A V w d mu = int (Theta^2 w)^T V w d mu >= -eps_2 int ||Theta w||_M^2 d mu, by (V).

Term 4: int (Theta^2 w)^T M A B w d mu = int (Theta^2 w)^T B w d mu = sum_c int theta_c^2 w_c^T (Hess psi_c) w_c d mu >= 0. **This is where Theta must be constant on cells, and it is all that the cut asks.** The Euclidean or M-geometry of the cut plays no other part.

Right side: int (Theta^2 w)^T M A D h d mu = int (Theta w)^T (Theta D h) d mu <= ||Theta w||_{L^2(mu; M)} ||Theta D h||_{L^2(mu; M^-1)}.

So (1 - eps_1 - eps_2) ||Theta w|| <= ||Theta D h||, hence ||Theta w||_{L^2(mu; M)} <= 2 ||Theta D h||_{L^2(mu; M^-1)}. Finally Cov(f, h) = int (Theta^-1 D f)^T (Theta w) d mu, and Cauchy-Schwarz. QED

*Remarks.* (1) No lower bound on M enters except through (V): M may have a tiny gap. (2) A hard cut is the limit of barriers psi_c, with the bound uniform. (3) The law need not be close to Gaussian in total variation; only Hess S_0 is close to M in the form (V). (4) In the bound, D f is measured in the dual norm of M. For f gauge invariant, D f annihilates gauge directions, so ||D f||_{M^-1} equals its value in the Landau form, and it carries no tree-gauge constant: |D f [X]| <= ||D f||_{M^-1} ||X||_M, with ||X||_M the energy norm of the fine extension. So the prefactor is free of C_tree(L) as well. (5) (W) with Theta = exp(rho d(., box_0)) says that conjugating M by a box-wise weight is a small relative perturbation of M, in the form sense. Note that it reads M against itself, not against the identity, which is why the gap does not appear.

## Use on a fibre

Take M := T^T D^2 A_k(V^*) T, in the free variables xi of Text 5.1, in B units. T is local to a box and its neighbours.

*(W), first derivation, now doubted (see the hostile check above): I argued* ||X||_M^2 = D^2 A_k(V^*)[X, X], which by Theorems 5, 7 of the energy package is comparable to the Eps norm of the saddle solution H with Q^{[k]} data X, up to C(L) a_* relative. Theorem 6 says the saddle operator conjugated by exp(rho d), rho below delta_*, is a relative perturbation of size C rho on Eps. M is a Schur complement of it, so Theta M Theta^-1 - M has relative size C rho in the form sense, with C absolute. T enters only through the designated bonds: a weight constant on boxes sees T only where a designated bond's constraint straddles two boxes, and there the factor is exp(rho), so this is the same C rho. Check W1, W2 of `checks/hard-core--mapped_chart_rate.py` tests this at the trivial background.

*(V), and (A) of HS-P, derived.* Hess S_0(xi) - M is x g^2 [D^2 A_k(Phi(xi)) - D^2 A_k(V^*)] in the chart, plus g^2 D^2 R_k o Phi, plus chart terms. Relative to ||.||_M these are at most C(L) tau + C(L) g^2, with tree decay, so eps_2 <= 1/4 for tau small in L and x large. Weights: the terms have tree decay at rate delta_* per box, so conjugation by rho below delta_*/2 costs a bounded factor.

*(V) for a marginal (derived; this is what Prop MD reads; the form sense below gives (A) of HS-P for U, with A_m = [M^-1]_{mm}, which has the fast rate as a block of M^-1).* Let S(y, m) have Hess S = M + V + B on (y, m), and let U(m) := -log integral dy e^{-S(y, m)}. Let M_m := M_mm - M_my M_yy^-1 M_ym. Claim: Hess U is within relative distance C eps of M_m, in the form (V), for M_m. A direct expansion, E[S_mm] - Cov(S_m, S_m), does not show this: E[V_mm] is small against M_mm only, and M_mm can be much larger than M_m, for a direction near the edge of m, where the frozen y of M_mm costs a jump that the relaxed y of M_m does not. *Fix: shift y with m.* For a direction x, let y^*(x) := -M_yy^-1 M_ym x, and z(x) := (y^*(x), x), so ||z(x)||_M = ||x||_{M_m}. Translation invariance of Lebesgue measure in y gives

    Hess U [x, x'] = E[ D^2 S [z(x), z(x')] ] - Cov( D S [z(x)], D S [z(x')] ),

with E the conditional law of y given m. Now D_y (D S [z(x)]) = (M + V)_{y .} z(x) = V_{y .} z(x), since the first order cancels by the choice of y^*. So by Lemma HS-M on y, the covariance is at most 2 ||V_{y .} z(x)||_{M_yy^-1} ||V_{y .} z(x')||_{M_yy^-1}, of second order in eps. And E[D^2 S[z, z']] = <z, M z'> + E[V[z, z']] + E[B[z, z']]. So Hess U = M_m + O(eps) M_m in the form sense. *Kernel.* V_m := Hess U - M_m has kernel E[V[z(e_i), z(e_j)]] plus second-order terms, and y^*(e_i) has the fast rate, so V_m has tree decay, and (A) holds for U. *The barrier.* B enters through E[B[z, z']], and through D psi [y^*] in the covariance, and these live where a cell is near its cut, of conditional probability at most z. With a hard cut they are boundary integrals, at most z^{1/2} ||z(x)||^2 up to polynomial factors in x. Status: derived; the barrier's bound is written at the level of a count, and for a frozen rough cell at distance D_c the Hessian of S is that of (Loc_j).

*The fast rate of M^-1 at a background: now `library/fibre-propagator.md`, Theorem F on the torus and Theorem F-D with a frozen exterior.* An earlier paragraph here argued it from Theorem 6 and the box-local map from Landau to tree gauge. **That argument had a gap:** Theorem 6's K carries the whole gauge term ||D^* H||^2, and on ker Q^o the part r D^* H is not gauge, so K's solution is not the class solution; and in global Landau gauge a local curvature has a power-law potential. The fix is a gauge term on ker r only, which is exact, massive and strictly local. The earlier check RF of `checks/hard-core--mapped_tp_flux.py` stands as numerics: PASS at constant flux in d = 2, one level, rate 1.52 to 1.59 for S1 and 1.66 to 1.69 for S2 at a' <= 0.2, L = 3, 5. Note its form was ||d H||^2 and not the Hessian.

*Use for moments in a large volume (derived; answers (OS_j)(c) of the upper chain).* Let f be local near D, and T := S - Q_M a function with |D_b T| of size C(L) g (1 + |xi|_loc)^3 at every bond of the torus. Interpolating S_t := Q_M + t T, d/dt E_t[f] = -Cov_t(f, T). With Theta := exp(-rho d(., D)), a weight *decaying* away from D, HS-P gives |Cov_t(f, T)| <= 2 ||Theta^-1 D f||_{L^2} ||Theta A D T||_{L^2}, and the second norm is at most C(L) g (sum_b e^{-2 rho d(b, D)})^{1/2}: the sum is free of the volume. So E[f] - E_Gauss[f] is at most C(L) g ||D f||, uniformly in the volume. This is (OS_j)(c), with omega(g) = C(L) g at a field regular everywhere, plus the tier from the cut.

*Consequence, by HS-C.* For a fibre over a parent regular on a region, with fields frozen beyond it, Cov(f, h) <= C(L) (e^{-rho d} + z^{1/2} e^{-rho_s d}) ||D f||_{L^infinity} ||D h||_{L^2(M^-1)}, where d is the box distance between supports, rho is the rate of M^-1, absolute, and rho_s = rho_s(L).

*Hostile.* (1) *Is Theta constant on cells compatible with the chart?* A cell here is a set of free variables with a joint cut, inside one box of Text 5.1. Yes. (2) *The frozen boundary.* Variations vanish on it, so M is the restriction of the torus M at a class fill to a subspace, and (W) on a subspace needs Theta to preserve it: coordinate subspaces are preserved by a diagonal Theta. (3) *Sites inside the region.* For fixed site data, the same holds on their exterior. Polymers are handled outside this lemma. (4) *Non-gauge-invariant f, h.* The prefactor then has ||D f||_{M^-1} <= gamma(L)^{-1/2} ||D f||, which is C(L); the rate is unchanged. Numerics: source S2 has the same rate as S1, with a prefactor growing about like L. (5) *What I have not done:* the statement for higher cumulants. By the split at the largest edge in `library/convex-laplace-tree-decay.md` version 2, they reduce to two-point bounds of the same kind, with derivatives of S in place of f, h. So the same rate should carry over. Not written.
