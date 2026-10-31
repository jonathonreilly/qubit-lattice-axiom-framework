# The lift as an analytic function: all orders, with no product displayed

Status: own derivation, each step written below, not reviewed. Numerics: `checks/hard-core--mapped_composite_jet.py`, criteria written first, on Lemma AN1 in d = 2; result at the end. Consumers: (SB) at order j >= 2 and (LG) at order >= 2 in Text 5.5 of `parts/hard-core--mapped.md`, the order-five norm of the classical functional in Text 5.9, and (CF_j)(d) of the upper chain.

Why it is needed. Up to now, higher derivatives of the lift were "finite uniformly in k, by a partition count, products not displayed". A composite block map has k levels. A generic iterate of quadratic maps has a remainder growing by a factor per level, and the hard part of this whole line is that no such factor may appear. Theorem 7 of the energy package handles the second jet. Its sum over levels is geometric, but the third jet mixes the second jet of lower levels, and I had not written that. The route here is new on this map: no order-by-order calculation. Show that one map is analytic on a ball of a size free of k, and read all orders from it.

## Setting

Level-n units. U_0 is the class lift of a class parent, or a class fill with frozen data, with chain V_j^0. Hypotheses: (i) flux at most T_2 at every level; (ii) ||F(U_0)||_{L^4(box)} <= C T_2, which is (R3); (iii) the saddle operator Sad# of `library/fibre-propagator.md`, or Sad#_N with frozen data, is invertible at U_0 with exponential decay at rate delta_#, Theorem F or F-D; (iv) the multiplier obeys |lambda_0|_inf <= C T_2.

Critical norm. For a level-j bond b, let b^+ be its two level-j blocks, and e_j(b) := ||H||_{L^4(b^+)}, a scale-invariant quantity in d = 4 with H in level-n normalisation. Let eps(H) := sup over top boxes of ||H||_{L^4}, so e_j(b) <= C eps(H) for all j, b. In a block of a parent bond c' there are about L^4 level-j bonds, and, by finite overlap,

    (1)  sum_{b in the block of c'} e_j(b)^4 <= C e_{j+1}(c')^4,   so   avg_b e_j(b)^2 <= C L^-2 e_{j+1}(c')^2.

**That L^-2 is the only source of gain.** It is exactly the statement that L^4 is critical in d = 4.

Complexify: H complex in log coordinates at U_0. N_j, N^(n) are the contour-free maps of Theorem 7 of `library/block-poincare-energy-package.md`, with D N_j = Q^{o,[j]} at V_j^0, analytic on a polydisc of radius rho_b(L) in the angles of a block, since the loops are close to 1 by (i) and the log-average is analytic there.

## Lemma AN1 (the composite map has no factor per level)

For eps(H) <= rho(L), the map H -> N^(n)(U_0 e^H) is analytic, and in log coordinates at V_n^0,

    | log N^(n)(U_0 e^H)(c) - Q^{o,(n)} H (c) | <= C_2(L) e_n(c)^2,

with C_2(L) and rho(L) free of n. The same holds at each intermediate level j.

*Proof.* Let theta^j be the level-j angle of the chain of U_0 e^H, and theta_lin^j := Q^{o,(j)} H, zeta^j := theta^j - theta_lin^j, zeta^0 = 0.

*Linear part.* |theta_lin^j(b)| <= C_1 e_j(b). The path part is a positive kernel rho_b with transports, of density at most C s_j^-3 on b^+, by Lemma 1 of the package, so its L^{4/3} norm is at most C, and Hoelder applies. The residual is at most C L^2 ||F||_{L^4(b^+)} ||H||_{L^2(b^+)} / s_j <= C L^2 ||F||_{L^4} e_j(b), by Lemma AD of `library/composite-adjoint.md` at level j, and ||H||_{L^2(b^+)} <= C s_j e_j(b).

*One level.* theta^{j+1} = Q^{o,[j]} theta^j + b_j(theta^j), with b_j the remainder of N_j, |b_j(theta)(c')| <= C_b(L) sum_{b in the block} |theta(b)|^2 for sup |theta| <= rho_b(L), and |Q^{o,[j]} zeta (c')| <= 2 L avg_b |zeta(b)|: a parent's angle is a sum of L angles along each line, averaged over lines, with transports, and the residual of one level is small by (i). So

    zeta^{j+1} = Q^{o,[j]} zeta^j + b_j(theta_lin^j + zeta^j).

*Induction.* Suppose |zeta^j(b)| <= C_2 e_j(b)^2 on all bonds, with C_2 rho(L) <= C_1. By (1), 2 L avg_b |zeta^j(b)| <= 2 L C_2 C L^-2 e_{j+1}(c')^2 = (2 C C_2 / L) e_{j+1}(c')^2. And |b_j| <= 8 C_b C_1^2 sum_b e_j(b)^2 <= 8 C C_b C_1^2 L^2 e_{j+1}(c')^2. So C_2 at level j + 1 is at most (2 C / L) C_2 + 8 C C_b C_1^2 L^2. For L >= 4 C, the bound C_2 := 16 C C_b C_1^2 L^2 reproduces itself, at every level. Finally sup |theta^j| <= C_1 eps + C_2 eps^2 <= rho_b(L) for eps <= rho(L). So the chain is analytic at each step, on a domain free of the level. QED

*Comment.* The remainder of a level is not small relative to the level's linear part, and it never contracts by itself in a sup norm. What saves the count is that a sup bound by local critical norms averages down by L^-2 per level, against the factor L of a sum along a line. This is the same 1/L as the geometric sum s_j in Theorem 7, Step 4.

## Lemma AN2 (local multilinear bounds)

Let E(H, lambda) := A(U_0 e^H) - <lambda, N^(n)(U_0 e^H) - V'>. For eps(H) <= rho(L) and |lambda|_inf <= 1:

(a) A(U_0 e^H) is a sum over fine plaquettes of an analytic function of four angles. The angles are at most C eps(H), since |eta H_b| <= ||H||_{L^4(b)}. Its Taylor terms of order m >= 3 in H, on a box B, are at most C^m times (||d_U H||_{L^2(B)} + ||F||_{L^4(B)} ||H||_{L^4(B)} + ||H||_{L^4(B)}^2) ||H||_{L^4(B)}^{m-2}, polarised.

(b) By Lemma AN1 and Cauchy's estimate on the polydisc, the terms of order m >= 2 in H of <lambda, N^(n)> on the block of c are at most C(L)^m |lambda(c)| e_n(c)^m, polarised. No sum over levels is left.

By the box Sobolev inequality, `library/lattice_sobolev_box_gauge.md`, ||H||_{L^4(B)} <= C ||H||_{Eps(B)}. So every multilinear term of order m >= 3 of E in H, and of order m >= 2 in H with one lambda, is local at the box scale, with norm at most C(L)^m in Eps(B).

## Prop AN3 (the lift and all its derivatives)

Let Y be a level-n parent field near 1. The system

    D_H E(H, lambda) + (gauge) = 0,   N^(n)(U_0 e^H) = V' e^Y

has a unique solution near (0, lambda_0), analytic in Y on { sup |Y| <= rho_2(L) }, with sup_B ||H||_{Eps(B)} + |lambda - lambda_0|_inf <= C(L) sup |Y|. It is the class lift of V' e^Y, up to gauge, and P_r D_{U_0}^* H = 0. For a tuple of directions Y_i at points y_i, i in S, the Taylor coefficient obeys

    (2)  ||H_S||_{Eps(B)} + |lambda_S|_{(B)} <= C_{|S|}(L) e^{- delta_{|S|} St(B, y_S)} prod_i ||Y_i||,

with St the length of a shortest tree on B and the y_i, in boxes, and delta_m := delta_# (1 - 1/(2 m))-type rates, positive for each fixed m. Constants are free of n, and of the volume.

*Proof.* T(H, lambda) := Sad#^-1 [ (0, Y) - NL(H, lambda; Y) ], with NL the terms of Lemma AN2 of total order at least 2, and the nonlinear part of the constraint from Lemma AN1. By (iii) the box-to-box kernel of Sad#^-1 is at most C e^{-delta_# d}, so Sad#^-1 is bounded on sup_B of the local norm, with no volume. T is a contraction on a ball of radius rho(L)/2, analytic in Y, which gives the solution. *Gauge:* test the first equation against the gauge direction W_omega(H) at U_0 e^H, for omega with varpi(U_0 e^H) omega = 0. Gauge invariance of A and the Ward identity kill all terms but <P_r D^* H, D^* W_omega(H)>, and this form is non-degenerate for small H. So the gauge term vanishes, and (H, lambda) is a true constrained critical point, by Lemma Inv's argument. In the real case it is the unique minimiser in the ball, by convexity.

*Majorant.* Let a_S(B) be the left side of (2). Taylor coefficients of the fixed point obey, by Lemma AN2 and the kernel,

    a_S(B) <= sum_{B'} C e^{-delta_# d(B, B')} [ 1_{S = {i}} |Y_i|_{B'} + sum over partitions of S into m >= 2 blocks S_l of C(L)^m prod_l a_{S_l}(B'^+) ].

At |S| = 1 this is Theorem F. Induct on |S|: trees through B' for the S_l join to a tree for S, and sum_{B'} e^{-delta d(B, B')} e^{-delta' St(B', y_S)} <= C e^{-delta'' St(B, y_S)} for delta'' below both. QED

**So at all orders, with tree decay, and no product across levels is needed.** The price is a constant C(L)^m in place of an absolute one at order at least 2, and this is allowed: the contraction reads an absolute constant only at the partition into singletons, Text 5.5.

## Consequences

1. *(SB), order j >= 2:* (2), with level-k values read through Lemma AN1 at level k: D^S V^*(y) for a level-k bond y is Q^{o,(k)} H_S plus products bounded by the same lemma, so at most C_{|S|}(L) with tree decay. Discharges "products not displayed".
2. *(LG), order >= 2:* not needed. All sizes at order at least 2 are in K#'s gauge, in which the response of a class problem at all orders is exponentially local. The top coefficient of the contraction reads the H^2 bound, so the weighted Landau gauge at order 1. The two are joined by the family g(s) := exp(sum s_i omega_i), with compact omega_i: `library/one-step-closure.md`, Section 4. Mixed derivatives then gain only commutators [omega_i, K_j] with tree decay. (A first form of this item said one gauge at all orders, which is not enough for the top coefficient.)
3. *The classical functional.* D_Y A_n = lambda, so D^{|S|+1} A_n = lambda_S. So A_n has all derivative norms bounded uniformly in n, with tree decay. This is the order-five bound of Text 5.9, and the upper chain's (CF_j)(d).
4. *With frozen data.* The same, with Sad#_N, and H in ker bC. Lemma AN1 is applied per region, since each constraint reads its own level only.
5. *Theorem 7 at a merely L^4 background.* Lemma AN2(b) with m = 2 bounds its Lagrange term by C(L) |lambda| ||H||_{L^4}^2. Its own Step 4 gives the same with L^2, using Lemma 4 of the package, and (6') of the fibre note says what that lemma becomes at L^4 control. So at a class lift there are now two proofs of (Size), and the one here does not read R(a).

## Hostile check

1. *Is it circular with (R3)?* (R3) is proved by the fixed point at order 1, with Lemma AD, from Sad# at the trial. Lemma AN1 reads (ii) only through the residual at the linear step, and rho(L). So the order is: Sad# at the trial, (R2), (R3), Theorem F at the lift, then this note.
2. *Where would a factor per level hide?* In the recursion for C_2. The coefficient 2 C / L is below 1 for L large and absolute C, and the source C_3(L) is free of j. If (1) were false, say in a dimension above the critical one, the coefficient would be at least 1. In d = 4, (1) is Hoelder. In the check's d = 2, the critical norm is L^2, the same recursion has coefficient C/L, from L^-1 in the sum of squares and L for the line.
3. *A single huge fine angle?* It is excluded by eps(H) small. For a Taylor coefficient only small H matters, and the bound is multilinear.
4. *Complexified log-average.* The average of logs of complex group elements near 1 is analytic, and N_j has g^[j] analytic. Base loops are close to 1 only after (i): at a merely class chain, each level's loops are below C(L) T_2, which is small in L by a_*.
5. *Could analyticity in a ball of radius rho(L) be false because a single bond's perturbation at fine level is not small?* No: |eta H_b| <= ||H||_{L^4(b)}, as above.
6. *Tree decay at rate delta_m below delta_#.* Only fixed m enter, up to five. The consumer's rate is reduced by a fixed factor, and Taylor reads tree decay along class paths only qualitatively, with C_n(L).
7. *What is not displayed.* Polarisation constants, and the local form of the gauge step at a frozen boundary. The bound on the composite kernel's density, from Lemma 1 of the package, is at U = 1 with transports.

## Numerics

`checks/hard-core--mapped_composite_jet.py`, criteria written first, on Lemma AN1, d = 2, L = 3, U = 1, SU(2), n = 1, 2, 3, 4, where the critical norm is the L^2 norm of H. PASS, run once. R_n := max | log N^(n) - Q^{o,(n)} theta | / S, over the two blocks: random 0.056, 0.011, 0.0009, 0.0001; line 0.099, 0.036, 0.013, 0.004; bundle 0.116, 0.079, 0.067, 0.062; rotblock 0.073, 0.044, 0.006, 0.0009; nested 0.000, 0.006, 0.0007, 0.0001. So there is no growth with n. The bundle, with all bonds of a block turning slowly in colour, is the extremal family found, and it settles at a constant, which is what a scale-invariant quadratic bound predicts. Controls: the remainder is quadratic to 1 percent, and the first derivative is Q^o to 3e-7. Limits: d = 2, U = 1, a search over structured families, not a supremum.

`checks/hard-core--mapped_composite_jet_d4.py`, criteria written first, on Lemma AN1 in d = 4, where L^4 is the critical norm, L = 3, n = 1, 2, 3, torus of 2 top cells along direction 0 and 1 across. PASS, run once. R_n := max | log N^(n) - Q^{o,(n)} theta | / ||H||^2_{L^4}: random 0.018, 0.00065, 0.00004; bundle 0.116, 0.079, 0.067; subbundle 0.028, 0.018, 0.015; rotblock 0.062, 0.017, 0.00017; comb, made to sit on the contours, 0.0719, 0.0717, 0.0717. So no growth, and the comb is level to 0.3 percent. Controls: the remainder is quadratic, and the first derivative is Q^o to 5e-7. The L^2 ratio of the bundle falls by 11 to 13 per level, 1.3e-2, 9.8e-4, 9.1e-5, so the check sees the difference between the critical norm and another. The largest value, 0.116, is far below the L^2 allowed by the proof at L = 3. Limits: L = 3, n <= 3, U = 1, one contour per point, a search.

## Prop AN4: the composite at the H^2 level, uniformly in the level (2026-10-31; level of each term; not gated)

*Only its first display, at the field, is consumed: (COMP)(ii) of `library/sector-values.md`. Variations are not read, since Lemma EX2 and an interpolation replaced them. The rest is kept as a second route, and it has the weakest step, (delta Q^*) lambda.*

Consumer: Prop DS of that note.

*Statement.* In level-k units, for V in D_k, and H, delta_b H, delta^2_{b b'} H the fine field and its variations in the gauge of Prop AN3, with F := d_U H + [H, H] the fine curvature, and F^{(j)} the flux of the level-j field in the same units:

    ||grad F||_{L^2(box)} <= C ( |lambda|_loc + f_loc^{3/2} + response ),    ||grad d_U delta_b H||_{L^2(box)} <= C(L) w_b(box),    ||grad d_U delta^2_{b b'} H||_{L^2(box)} <= C(L) w_{b b'}(box),

free of k, and the same for F^{(j)} by the convolution of Step 5 of LIFT-I, up to AN1's remainder. *Counting by lattice sum gives (COMP)(ii), with the factor s^2: sum over level-j cells of |Delta theta|^2 = s^2 ||grad F^{(j)}||^2_{L^2(box)}.*

*Field.* Steps 1 to 6 of LIFT-I, with n := k.

*First variation.* Differentiate D_U^* F_U = Q_U^* lambda along b. With G := d_U delta H: D_U^* G = Q^* delta lambda + (delta Q^*) lambda + [delta H, F]-terms. Bianchi: D_U G = [F, delta H]. Weitzenboeck with a cut-off at the top scale: ||eta grad G||^2 <= 2 ||eta D_U^* G||^2 + 2 ||eta D_U G||^2 + C int eta^2 |F| |G|^2 + C ||(grad eta) G||^2. Sizes. (i) Q^* delta lambda: by (AD), its line and residual parts at most C |delta lambda|_loc <= C(L) w_b, as ||A_k||_2 <= C(L). Its contour part is Phi^* (D'^* delta lambda), not zero: conservation of lambda varies to D'^*_V delta lambda = [b, lambda], of size |lambda(b)|, only at b. In L^2(box), Phi^* has norm at most C L^{3/2} per level, in the count of `library/composite-adjoint.md`, against |lambda| <= C T_2: at most C a_* L^-1/2. (ii) (delta Q^*) lambda: the variation of the transports, at most C L^2 |lambda| ||delta H||_{L^4} by (AD)'s count. Small. (iii) [delta H, F] in L^2: at most ||F||_{L^4} ||delta H||_{L^4} <= C f ||delta H||_{H^1}, by the lattice Sobolev bound, `library/lattice_sobolev_box_gauge.md`. (iv) int eta^2 |F| |G|^2 <= ||F||_{L^4} ||eta G||_{L^{8/3}}^2 <= C f ||eta G||_{H^1}^2 by interpolation, so absorbed for f small. (v) ||(grad eta) G||^2 <= C(L) w_b^2, by Theorem F-D. So it closes.

*Second variation.* The same, with sources quadratic in first variations: [delta H, d delta' H] in L^2, at most ||delta H||_{L^4} ||d delta' H||_{L^4} <= C(L) w w', by the first-variation bound and Sobolev; (delta^2 Q^*) lambda and (delta Q^*) delta' lambda similar; conservation now has sources at b, b'.

*Hostile.* (1) The Sobolev step at the critical exponent is uniform in the mesh; that is the content of the lattice Sobolev note, and it reads a box gauge. (2) Is (AD)'s C free of k at a variation? It is an operator bound on Q^{o,(n)*}, so yes. (3) At a nested block centre there is no pointwise bound on F. Only L^4 is read above. (4) What I have not written: (delta Q^*) lambda in the composite, beyond a count of one level, and the composition over levels; AD0's form suggests it has no factor per level, and that is the weakest step here. *Numerics:* abelian only, `checks/hard-core--mapped_lift_gradient.py`: C(4, L, n) stable in n and L at the field level. Nothing in SU(2) at two levels.
