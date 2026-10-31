# The composite adjoint at a background

Own derivation, 2026-10-31; not reviewed. Part: `hard-core--mapped`. The block operators are Balaban's. Consumers: (R3), (SB) at order 1, and so the contraction of Text 5.5, 5.9 and the hypothesis of Theorem F at the actual lift. This replaces the count written in Text 5.5, which it agrees with, including the power of L. This line is not independent of the Sussman-Alpoge account, which supplied the map; this argument does not read it.

**Statement.** d = 4. Level n, units of level n, s_j := L^{j-n}. U a fine field whose chain has every plaquette angle at every level at most T, in a box and its neighbours. Then, for a level-n multiplier lambda,

    || Q^{o,(n)*}_U lambda - (P^{(n)}_U)^* lambda ||_{L^2(box)} <= C L^2 ||F||_{L^4(box+)} |lambda|_{loc},        (AD)
    || (P^{(n)}_U)^* lambda ||_{L^2(box)} <= C |lambda|_{loc},

with C absolute, for a_* = L^2 T <= c L^-2, where P^{(n)}_U is the composite of the path parts, with unitary transports and the positive weights of U = 1, and ||F||_{L^4} is read through the chain, in the sense of Lemma AD0.

**Why it matters.** With (AD) the fixed point of Text 5.5 closes with absolute constants, since L^2 flux' <= C a_*.

**The power is sharp for a comb.** In d = 4 a sheet of flux f on the ladder over the first stage of the comb, L x L plaquettes in one block, has E = L^(1/2) f, and |v_x| about f L^2 for about half of all x, so the residual on the L bonds of the axis gives L^(1/2) f L^2 |lambda| = L^2 E |lambda|. So L^2 cannot be lowered by this method for such data. At the lift such data do not occur, as (R3) bounds ||F||_{L^4}. Averaging over the orders of the axes changes only constants.

## Lemma AD1: one level

Fix a level j, and write in level-j lattice units: block B(y) of side L, comb contours Gamma_{y,x} in a fixed order of axes. An average over orders is an average of bounds in l^2. V a level-j field, theta_p its plaquette angles, geodesic, |theta_p| <= T, so a_* = L^2 T <= c.

*Exact expansion.* For a parent bond c = (y, mu), x in B(y): path_x := Gamma_{y,x} . line_x . (Gamma_{y',x'})^-1, Omega_x its holonomy, Omega_0 that of the centre line, v_x := log(Omega_x Omega_0^-1), A := avg_x v_x, V' := e^A Omega_0. With eps_x the first-order change of Omega_x:

    eps_x = cs_x + Ad(Omega~_x) line_x - Ad(Omega_x) cs'_x,

with cs_x, cs'_x the contour sums at y, y', Omega~_x the contour's holonomy, and line_x the transported sum along the line. Differentiating the log-average,

    Q theta (c) = avg_x (1 + E_x) [ eps_x ] + G_0 [ eps_0 ],
    1 + E_x := Dexp(A) L(v_x),   G_0 := Ad(e^A) - avg_x (1 + E_x) Ad(e^{v_x}),

where L(v) := ad_v/(e^{ad_v} - 1) and Dexp(A) := (e^{ad_A} - 1)/ad_A. *Sizes:* |E_x| <= C (|v_x - A| + |v_x|^2 + |A|^2), since E_x = (1/2) ad_{A - v_x} + O(|v|^2); and |G_0| <= C avg_x |v_x|^2: the first order is ad_A - avg_x (ad_{v_x} + (1/2) ad_{A - v_x}) = ad_A - ad_A = 0.

With Phi := -avg_x cs_x and D' f (c) := Ad(V') f(y') - f(y), Q^o := Q - D' Phi. So the contour sums at y cancel, those at y' cancel up to Ad(V') - Ad(Omega_x), of size C |v_x - A|, and

    Res := Q^o - P_U = avg_x (Ad(V') - Ad(Omega_x)) cs'_x + avg_x E_x [eps_x] + G_0 [eps_0],    P_U theta (c) := avg_x Ad(Omega~_x) line_x.

Hence, for each bond b, |Res^* lambda (b)| <= C |lambda| ( w(b) + W(b) + c_0(b) ), over the boundedly many parents whose paths contain b, with

    w(b) := L^-d sum_{x : b in Gamma_x or Gamma'_x} kappa_x,   W(b) := L^-d sum_{x : b in line_x} kappa_x,   c_0(b) := (avg_x v_x^2) 1(b in path_0),   kappa_x := |v_x| + |A|.

This is checked by (W) of `checks/hard-core--mapped_adjoint_patterns.py`.

*The loop.* Gamma' is the translate of Gamma by L e_mu. So Omega_x Omega_0^-1 is the holonomy of a loop spanned by the ladders e x [0, L e_mu] over the bonds e of Gamma_x not parallel to mu, and over a bond parallel to mu the ladder has no area. The geodesic triangle inequality in SU(2) gives

    |v_x| <= sum_{e in Gamma_x} sigma(e),   sigma(e) := sum_{s < L} |theta_{p(e, s)}|.

*Counts.* Stage i is the part of the comb along the i-th axis: at most L^i bonds. For e in stage i, the set of x using e has N(e) <= L^{d - i + 1} elements, so psi(e) := N(e)/L^d <= L^{1 - i}. Let tau(e)^4 := sum_s theta_{p(e,s)}^4, so sigma(e) <= L^(3/4) tau(e), and E^4 := sum_e tau(e)^4 <= sum over plaquettes in B and its neighbour along mu of theta_p^4, as (e, s) -> p(e, s) is injective.

(a) *Mean.* v-bar := avg_x |v_x| <= sum_e psi(e) sigma(e) <= L^(3/4) (sum_e psi^(4/3))^(3/4) E. Sum_e psi^(4/3) <= sum_i L^i L^{(4/3)(1 - i)} <= C L. So v-bar <= C L^(3/2) E. And |A| <= v-bar.

(b) *Second moment.* v_x^2 <= (d L^2) sum_{p in S_x} theta_p^2. So avg_x v_x^2 <= d L^2 sum_p psi(p) theta_p^2 <= d L^2 (sum_p psi(p)^2)^(1/2) E^2, and sum_p psi(p)^2 <= sum_i L^i L L^{2 - 2 i} <= C L^2. So avg_x v_x^2 <= C L^3 E^2.

(c) *Contours.* For b in stage i', with X_b the x using b: L^-d sum_{x in X_b} |v_x| <= psi(b) sum_{e <= b} sigma(e) + sum_{e > b} psi(e) sigma(e), the stem and the descendants of b.

 Term with |A|: sum_b psi(b)^2 v-bar^2 <= C L v-bar^2 <= C L^4 E^2, as sum_b psi(b)^2 <= sum_i L^{i + 2 - 2 i} <= C L.

 Stem: sum_{e <= b} sigma(e) <= L^(3/4) (d L)^(3/4) E <= C L^(3/2) E. So sum_b psi(b)^2 C L^3 E^2 <= C L^4 E^2.

 Descendants: for b in stage i', with E_sub(b)^4 := sum_{e > b} tau(e)^4: sum_{e > b} psi(e) sigma(e) <= L^(3/4) (sum_{e > b} psi^(4/3))^(3/4) E_sub(b), and sum_{e > b} psi^(4/3) <= sum_{i >= i'} L^{i - i' + 1} L^{(4/3)(1 - i)} <= C L^{7/3 - (4/3) i'}. So the term is at most C L^{5/2 - i'} E_sub(b). Along one segment of stage i' the subtrees are nested, with at most L bonds; distinct segments have disjoint subtrees, and there are at most L^{i' - 1} of them. So sum_b E_sub(b)^2 <= L sum_seg E_seg^2 <= L L^{(i' - 1)/2} E^2. Total: C L^{5 - 2 i'} L L^{(i' - 1)/2} E^2 = C L^{(11 - 3 i')/2} E^2 <= C L^4 E^2.

 So ||w||_{l^2} <= C L^2 E.

(d) *Lines.* A bond is on at most L lines of a block. W(b)^2 <= L^{-2 d} L sum_{x : b in line_x} kappa_x^2. Sum over b, each x on L bonds: ||W||^2 <= L^{2 - 2 d} L^d avg_x kappa_x^2 = L^{2 - d} avg_x kappa_x^2 <= C L^{2 - d} L^3 E^2. So ||W|| <= C L^{1/2} E at d = 4.

(e) *Centre path.* ||c_0||^2 <= C L (avg_x v_x^2)^2, and avg_x v_x^2 <= C a_* v-bar, since |v_x| <= C L^2 T. So ||c_0|| <= C L^(1/2) a_* L^(3/2) E <= C L^2 a_* E.

**Lemma AD1.** ||Res^* lambda||_{l^2(B)} <= C L^2 E(B+) |lambda|_{B+}, C depending on d only. QED

*Pointwise.* |Res^* lambda (b)| <= C a_j psi(b) |lambda| + (lines: C a_j L^{-3} |lambda|) + (centre path: C a_j^2 |lambda|), with a_j := max_x |v_x| at level j. The path part gives |P_U^* lambda (b)| <= L^-3 max |lambda|: a bond lies on lines from at most two parents, with total weight L . L^-4.

## Lemma AD: the composite

Put lambda_n := lambda, lambda_j := Q^{o,[j]*}_U lambda_{j+1} = P_j^* lambda_{j+1} + nu_j, with nu_j := Res_j^* lambda_{j+1}.

*Sup norm.* |lambda_j|_infinity <= (L^-3 + C a_j) |lambda_{j+1}|_infinity. So with s_j^3 := L^{-3 (n - j)}, |lambda_j|_infinity <= s_j^3 |lambda|_infinity prod_{i >= j} (1 + C a_i L^3). In the box, a_i <= C L^2 max theta at level i. With Lemma AD0, sum_i a_i L^3 <= C L^5 sum_i s_i ||F||_{L^4} <= C L^4 ||F||_{L^4}, using s_i <= s_{i+1}/L. At the lift, this is at most C L^4 T_2 = C a_* L^2. So for a_* <= c L^-2 the product is at most 2. Here is the only place a_* must be small in L for this lemma.

*Unitary positivity (no factor per level).* Let P^abs_j be the path part with all transports replaced by the identity, Q^{(j)}_abs := P^abs_{j-1} ... P^abs_0, which is the tri and box operator of Lemma 1 of the energy package. Then |P_j^* mu| <= (P^abs_j)^* |mu| pointwise, as Ad is unitary. Put 𝖤_j(nu) := || (Q^{(j)}_abs)^* |nu| ||_{L^2}. Then

    𝖤_j(lambda_j) <= 𝖤_{j+1}(lambda_{j+1}) + 𝖤_j(nu_j),

with constant 1, as (Q^{(j)}_abs)^* (P^abs_j)^* = (Q^{(j+1)}_abs)^*. *An earlier form had a factor 1 + C(L) theta_j per level for the path part. The relative changes of the weights on lines are now in Res, as term (d), so the path part has none.*

*One level's residual.* 𝖤_j(nu) <= C s_j^-1 ||nu||_{l^2}, in d = 4: the weights have bounded overlap, each ||rho_b||^2_{L^2} = s_j^{-4}, and there is a factor s_j from potential normalisation. By Lemma AD1, over the level-(j+1) blocks in the box,

    ||nu_j||^2_{l^2(box)} <= C L^4 (2 s_{j+1}^3 |lambda|)^2 sum_B E(B+)^2 <= C L^4 s_{j+1}^6 |lambda|^2 (#B)^(1/2) E_box(j)^2 = C L^4 s_{j+1}^4 |lambda|^2 E_box(j)^2.

*Lemma AD0 (angles against F; derived).* Let E_box(j) := (sum over level-j plaquettes in the box of theta_p^4)^(1/4), with E_box(0) = eta ||F||_{L^4}. If L^(5/2) ||F||_{L^4(box+)} <= c, then E_box(j) <= 2 s_j ||F||_{L^4(box+)} for all j <= n.

*Proof.* Take a level-(j+1) plaquette P' with sides c_1, ..., c_4, and for x in a block let W_x be the product of the four holonomies Omega_x^{(i)}, with x translated along the sides. The contours cancel, so W_x is the holonomy of the boundary of the L x L square S_x, and |log W_x| <= sum_{p in S_x} |theta_p| by the triangle inequality. With V'^{(i)} = e^{A_i} Omega_0^{(i)} and Omega_x^{(i)} = e^{v_x^{(i)}} Omega_0^{(i)}, h := W_0: BCH on the four sides gives

    log W_x = sum_i (+-) Ad(.) v_x^{(i)} + log h + O(|v_x|^2 + |v_x| |log h|),
    log hol(P') = sum_i (+-) Ad(.) A_i + log h + O(|A|^2 + |A| |log h|).

Averaging over x and using A_i = avg_x v_x^{(i)}: | log hol(P') - avg_x log W_x | <= C a_j sum_i v-bar^{(i)}, where a_j := max |v_x| at level j, and |log h| <= C a_j. So |theta'(P')| <= avg_x sum_{p in S_x} |theta_p| + C a_j sum_i v-bar^{(i)}. Over a block's plaquettes, in l^4: the first term, by Jensen with weights L^2 rho(p; P') that sum to 1 in each variable, is at most L E(j). The second, by (a) of Lemma AD1, is at most C a_j L^(3/2) E(j). So E_{j+1} <= L (1 + C a_j L^(1/2)) E_j. And a_j <= C L^2 max theta at level j <= C L^2 E_j. With e_j := E_j/s_j: e_{j+1} <= e_j (1 + C L^(5/2) s_j e_j). As long as e_i <= 2 e_0 for i <= j, the product is at most exp(C L^(5/2) e_0 sum_i s_i), and sum_i s_i <= 2 s_j <= 2. So it stays at most 2, for L^(5/2) e_0 <= c. QED

At the lift, ||F||_{L^4} <= C T_2 = C a_*/L^2 gives L^(5/2) ||F||_{L^4} <= C a_* L^(1/2), small. The hypothesis is inside the ball of the fixed point, by continuity.

*Status: derived, each step written; not reviewed. An earlier form of this paragraph read theta' = sum rho Ad theta (1 + O(a_*)) as a count, with a relative error constant per level, which would not have summed. The bootstrap is what makes the error geometric: it reads the size of level-j angles from E_j, not from the class bound T.*

So

    𝖤_j(nu_j) <= C L s_{j+1}^-1 . L^2 s_{j+1}^2 |lambda| . (s_{j+1}/L) ||F||_{L^4} = C L^2 s_{j+1}^2 |lambda| ||F||_{L^4}.

Sum over j: geometric, the top level dominating, at most 2 C L^2 ||F||_{L^4} |lambda|. And 𝖤_n(lambda_n) <= C |lambda|. QED.

## Consequences for (SB)

(i) (AD) closes the fixed point of Text 5.5: Y <= C flux' + C L^2 (flux' + Y) flux' + C a_* Y + C Y^2, with L^2 flux' <= C a_*. So ||F(U)||_{L^4(box)} <= C flux', and ||H'||_{H^2(box)} <= C e^{-delta d}, C absolute. The order of constants asks a_* <= min(a_#(L), c L^-2).

(ii) *The loss L^{4/p} can be lowered.* K(y, x') is s_k times the average of H' over a tile of side 1/L. In d = 4, H^2 misses L^infinity by a logarithm: for f in H^2 on a box and a normalised bump at scale 1/L, |<rho, f>| <= C (log L)^(1/2) ||f||_{H^2}: on the Fourier side, with a cutoff, sum_q |f^(q)| |rho^(q)| <= ||f||_{H^2} (sum_{|q| <= L} |q|^-4)^(1/2). This holds on the lattice, uniformly in eta. So sup_y sum_{x'} |K(y, x')| e^{mu d} <= C L^-1 (log L)^(1/2), and the contraction factor at order n is C^n L^{4 - n} (log L)^{(n-1)/2}, in place of L^{4 - n + 4 (n-1)/p}. At n = 5: C^5 L^-1 (log L)^2.

## Hostile check

(1) *Non-abelian at the expansion.* The expansion of Q is exact for SU(2), since log and Dexp are the usual functions of ad, and the check (W) is on charged components at a Cartan background only. In general ad_v acts on su(2), and the bound |E_x| reads the Taylor expansion uniformly for |v| <= C a_*. Fine.

(2) *|theta_p| <= T is used only for |v_x| small.* In (a) to (d), only L^4 norms enter. In (e), the sup norm and Lemma AD0, the size of a_j enters, and there a_j <= C L^2 E_j, so it is geometric in the level, which a bound by T alone would not be.

(3) *Are the contours really a comb here?* Text 3.1 has avg_Gamma, an average over contours from y to x, and the numerics use axis-ordered combs. If contours are spread radially, the first-stage weight falls and the power falls below 2. Only an upper bound is needed. At a rough cell contours are rerouted (Text 5.2): this is not read at the lift, which is class.

(4) *Is 𝖤_j(nu) <= C s_j^-1 ||nu|| right in the presence of concentration?* It is an l^2 statement with bounded overlap of the weights, so yes.

(5) *What about the second-order term of the chain?* It is not in Q^o, which is first order. It enters bH, and it was bounded in Theorem 7, with C(L).

(6) *Does (AD) need Theorem F?* No. The other way round: Theorem F at the actual lift needs ||F||_{L^4} <= C flux', and the fixed point reads (AD) and Theorem F at the trial field, which has a pointwise bound. So there is no circle: Sad# at U^tr first, then (R2), then (R3) with (AD), then Theorem F at U^*.

(7) *Is the fixed point in the right space?* Eps ball by (R2) in local sup norm, H^2 by (R3) in the local Landau gauge. The term C Y^2 needs ||H||_{L^4(box+)} small, which (R2) gives.

## Numerics on fields that are not constant flux

`checks/hard-core--mapped_adjoint_patterns.py`, criteria written first, d = 2, one level, Cartan background, nc = 4, L = 3, 5, 7, 9, four kinds of field, at largest |v_x| = 0.1 and 0.3. PASS, run once.

- The pointwise bound (W) of the expansion holds on every entry of the residual, with ratio at most 0.999 against the C_w = 3 stated, so with constant 1 as it stands. Without its first-order term the ratio reaches 807, so that term is what carries it. At zero amplitude ||Res|| is at most 2e-16.
- R := ||Res|| / (L^2 max_B E(B)): random 0.025, 0.011, 0.007, 0.004; strip, with flux next to the comb's axis, 0.052, 0.021, 0.012, 0.008; far 0.044, 0.025, 0.015, 0.010; smooth 0.100, 0.084, 0.075, 0.070, at L = 3, 5, 7, 9. All at most 0.1 against the bound 1 stated. The concentrated kinds decay with L in d = 2, as expected, since the case that saturates L^2 needs d = 4. Smooth fields are the largest and nearly level.

Limits: d = 2, one level, Cartan. d = 4 has not been run on this lemma.
