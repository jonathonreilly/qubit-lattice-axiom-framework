# The class and the energy excess

Producer: `parts/hard-core--mapped.md`, Text 5. Status: the Excess Lemma is proved given the five inputs listed. Not reviewed. The closure bound in the producer (Prop R1, Text 5.2) no longer uses this lemma: it uses additivity of the classical energy and Jensen, which removes `Relative chart` and `Shift bound`. This note is kept for the arithmetic of the thresholds T_c, T_f, K_0, the leaf `Cut and Poincare`, and the failure log.

Credit: constrained minimal configurations are Balaban's (CMP 102). The argument below, expansion at the reference on the exterior with the hole's own energy kept separately, is mine. It does not use the account.

Consumers: the rare-cell bound in the real one-step theorem.

## Conventions

Levels k and k+1. theta_p: the angle of a level-k plaquette. flux_c := max |theta_p| over plaquettes p of the level-k cell c. A box is a level-(k+1) cell: L^4 level-k cells. All energies are dimensionless sums over plaquettes, so the L^2 norm of curvature is the same in level-k and level-(k+1) units.

a_* = a_*(d,L) is the threshold of Theorem 5 of `library/block-poincare-energy-package.md`, for R(a) in level-(k+1) units. Shrink it if necessary so that a_* <= varpi/L^2. Absolute constants c_b, c_s, C_r, C_I, C_n appear in the inputs. Put

    K_0^2 := 40 C_n C_I c_s L^{3/2} / c_b,    T_c := a_*/L^2,    T_f := L T_c/(C_r K_0) = a_*/(C_r K_0 L).

For L large, T_c < T_f. Then x_k is taken large.

**Sets.** D_k := { flux_c <= T_f for all c }: where the formula -log rho_k = x_k A_k + vac_k + R_k is claimed. C_k := { flux_c <= T_c for all c }: where the fibre integral is uniformly convex.

**The reference.** For V' in D_{k+1}, U* = U_{k+1}(V') and V* = M^k(U*). By `Regularity`, flux_c(V*) <= C_r L^-1 T_f = T_c/K_0, and the energy of U* per level-k cell is at most c_s (T_c/K_0)^2. (Corrected: this note first used L^-2, which I have not proved. The proved bound is L^-1, from an L^4 estimate, producer Text 5.3, item (R3). It is enough, since T_f = L T_c/(C_r K_0) ~ L^{1/4} T_c.)

**Inputs.**

- `Regularity`: for V in D_k the minimiser U_k(V) exists, is unique among fields with small relative field, and has fine curvature at most C_r flux(V) in level-k units. Also flux_c(M^k(U_{k+1}(V'))) <= C_r L^-1 flux(V').
- `Cut and Poincare`: for a set Y of level-k cells in a box with |Y| < L^3/10, there is Y-hat containing Y with |Y-hat| <= C_I |Y|^{3/2}, such that the box minus Y-hat is simply connected, and a field H on it whose block average restricted to lines avoiding Y-hat is f obeys ||H||^2 <= C_P' (||grad H||^2 + ||f||^2) in level-(k+1) units. Route: fill pockets, and span each 2-cycle of Y by a 3-chain, by the Federer-Fleming isoperimetric inequality; then prune sets of small boundary, using the isoperimetric inequality for the cell graph of Z^4. Frozen leaf. The cut is needed: inside a box the block data do not constrain loops linking an annular Y, so U and U* can differ there by a holonomy.
- `Relative chart`: if U, U* have the same block data at level k+1 and small loops, there is a gauge on the complement of the Y-hat's and of W in which U = e^{i eta H} U*, with D*_{U*} H = 0 and sup |eta H| small. At the box scale no holonomy can appear, because the block data of U and U* coincide; inside a box the cut removes it.
- `Shift bound`: the block average of H over lines meeting Y-hat, paired with lambda, is at most (c_b/32) sum_Y flux_c^2. Reason: a line through Y carries H of size at most C flux_c on one cell, and a line through the membrane carries the jump of H, which is a holonomy alpha around Y with alpha^2 <= w^2 sum_disc flux^2, w^2 the number of plaquettes of Y on a spanning disc. Fractions of lines are L^-3 per cell. For an annulus of size r and thickness w this gives T_f L^-3 r^3 w alpha, against cost f^2 r^2 w^2 with alpha <= f w^2, so a ratio at most (T_f/T_c) r L^-3 <= C L^-3/4 for r <= L. General shapes: frozen with the previous leaf.
- `Block energy`: for a fine field with small loops and level-k data V_k, A_c(U) >= c_b flux_c(V_k)^2. Cauchy-Schwarz with the bounded composite weights of Lemma 1 of the package.

## Excess Lemma

Let V' be in D_{k+1}, V_k in D_k with M(V_k) = V', U = U_k(V_k), and Y the set of cells with flux_c(V_k) > T_c. Then

    A_k(V_k) - A_{k+1}(V') >= (c_b/8) sum_{c in Y} flux_c(V_k)^2 >= (c_b/8) T_c^2 |Y|.

*Proof.* Let W be the set of boxes containing at least L^3/10 cells of Y. Let W^+ be W together with those boxes within distance two of W that have no valid constraint within distance two: a constraint region R_c being valid if it misses W. |W^+| <= C_n |W|. Let Y' := Y minus W, and Y-hat the union of the sets given by `Cut and Poincare` for the boxes off W. Let Ext be the plaquettes off W^+ and off Y-hat^+.

*Dropped boxes.* The energy of U in W is at least c_b sum over the Y-cells in W of flux_c^2. The reference has, in W^+, energy at most C_n |W| L^4 (c_s/K_0^2) T_c^2 = |W| L^{5/2} T_c^2 c_b/(40 C_I), which is at most L^{-1/2} c_b T_c^2 times the number of Y-cells in W. So the net of these boxes is at least (c_b/2) sum over the Y-cells in W of flux_c^2.

*Sparse holes.* For a box off W with m cells of Y', m^{1/2} <= L^{3/2}, so |Y-hat| <= C_I L^{3/2} m. The reference energy on Y-hat^+ is at most C C_I L^{3/2} m (c_s/K_0^2) T_c^2 <= (c_b/40) m T_c^2, after enlarging C_n to contain C. The energy of U on Y' is at least c_b sum_{Y'} flux_c^2. So the net of these holes is at least (c_b/2) sum_{Y'} flux_c^2.

*The exterior.* Work in level-(k+1) units, with H from `Relative chart`. Expand A_Ext at U*. The linear term has two parts.

(i) The constraint part. The multiplier equation and the Ward identity give D_U A(U*) = Q^{o,(k+1)}* lambda, with |lambda| <= C flux(V') by Theorem 7 Step 5. As in Theorem 7, Q^{o,(k+1)} eta H is a coarse gradient, which lambda annihilates, plus the second-order term, bounded by C(L) Lambda ||H||^2_Ext <= C(L) a_* ||H||^2_Ext, plus the part carried by lines through Y-hat, which `Shift bound` controls. Lines through W are not used.

(ii) The boundary part: the first variation of A on the removed plaquettes, at U*, applied to H. It is supported on the plaquettes shared with Ext, with coefficient the curvature of U*. By the trace inequality on cells next to the hole, whose H is controlled by `Cut and Poincare` and the local chain of constraints, it is at most ||F(U*)||_{L^2(layer)} ||H||_{H^1(Ext)} <= (1/16) ||H||^2_{H^1(Ext)} + C (reference energy on the layer). The last term is of the same form as the reference energy above and is absorbed there, enlarging the constant in K_0.

The quadratic term: on Ext the flux is at most T_c, which is R(a_*) in level-(k+1) units. So the proof of Theorem 5, with `Cut and Poincare` in place of Lemma 2 there, gives ||H||^2_Ext <= C ||grad H||^2_Ext, and the quadratic term is at least (1/4) ||grad H||^2_Ext minus C a_* of itself. The cubic and quartic terms are at most C a_* (||grad H||^2_Ext + ||H||^2_Ext). So A_Ext(U) - A_Ext(U*) >= (1/8) ||grad H||^2_Ext - (c_b/16) sum_Y flux_c^2 for a_* small in terms of L.

Add the three parts. QED

## What this delivers, and what it does not

1. x_k times the excess is at least c x_k T_c^2 |Y|, against an entropy of order C(L) |Y| log x_k. So a cell above T_c, under any parent in D_{k+1}, is rare, with no filling of holes and no condition on the topology of the exterior. An annulus of bad cells is priced by its own cells. In the abelian quadratic model the lemma is the orthogonality ||da||^2 = ||da*||^2 + ||d(a-a*)||^2 on the fibre.
2. It is classical energy. Passing to the effective action, with the Gaussian normalisers of the exterior matching, is a separate statement, in the producer: for hole data xi the exterior integral is uniformly convex, and two such integrals differ by at most C times the size of the hole, by `library/convex-laplace-tree-decay.md` applied to S_t = (1-t) S_xi + t S_0 of the centred actions.
3. It concerns V_k in D_k. Outside D_k the formula is unavailable and the upper bound (U_k) takes over. Its induction is an obligation in the producer.

## Route tried and dropped here

Dropping the whole box containing a bad cell, however sparse: the saving is the reference's energy in the box, comparable to the cost of one bad cell at the same threshold. It forces the hole threshold to exceed the parent's by a fixed factor at every level, while the formula range must contain the hole range at the level below: an infinite ladder of thresholds. Keeping the exterior of a sparse box removes it, because the saving is per cell, a factor L^-4 smaller, and the two ranges T_c and T_f suffice.
