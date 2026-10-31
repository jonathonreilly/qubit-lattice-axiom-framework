# The fibre's inverse Hessian has a rate free of L

Own derivation, 2026-10-31; not reviewed. Part: `hard-core--mapped`. The block operators and the idea of a constrained covariance are Balaban's, and the use of an average with its coarse gradient removed is Lemma 3.1 of the producer file. Consumers: `library/preconditioned-covariance.md` (Lemma HS-P on a fibre, moments in a large volume), Prop MD and (H1) in the producer file. This note does not use the Sussman-Alpoge account; the line as a whole is not independent of it.

**Statement wanted.** In the tree-gauge chart of a fibre over a regular parent, |M^-1(xi_i, xi_j)| <= C(L) e^{-rho d(i, j)}, with d in coarse boxes and rho free of L, though the gap of M falls with L. Also the same with the exterior of a region frozen.

## A gap this fixes

`library/preconditioned-covariance.md` argued the rate "by Theorem 6 and the box-local map from Landau to tree gauge". That argument has a gap. Theorem 6 of `library/block-poincare-energy-package.md` inverts K := Hess + D D^* on ker Q^o. On ker Q^o the gauge freedom is only omega with r omega = 0, since Q^o D = D' r. So the part r D^* H of the gauge term cannot be gauged away, and ||D^* H||^2 adds real energy to the class problem. The solution of Theorem 6's system is not the class solution. Control C0 of `checks/hard-core--mapped_sharp.py` confirms this numerically: r D^* H is about 0.07 to 0.2 of ||H|| in level-1 units on the K solution. Using global Landau gauge instead does not help either: it has a nonlocal constraint, and the Landau potential of a local curvature has a power-law tail (Biot-Savart). So the rate needs a formulation that is local, coercive and exact for the class.

## The idea

Gauge-fix only what is gauge. On ker Q^o the residual gauge parameters are ker r, and on ker r the Laplacian has a gap at the block scale. So the gauge term ||P_r D^* H||^2, with P_r the projector on ker r, is exact for the class, massive and strictly local.

## Setting

Level n := k + 1, units of level n, fine spacing eta = L^-n. U satisfies R(a) on the torus, or U = e^{i eta H} U^tr with U^tr satisfying R(a) and ||F(U)||_{L^4(box)} <= a, which is what (R3) gives at the actual lift: see hostile point (6'). Q^o := Q^{o,(n)}, the composite with coarse gradients removed at each level, as in the energy package. Define r^{[j]} := ev - Phi^{[j]} D_j on level-j site functions, and r := r^{[n-1]} ... r^{[0]}. Then, exactly, with no estimate,

    (Cov)  Q^o D_U = D'_{V'} r,    so    D_U^* Q^{o*} = r^* D'^*.

*Proof.* Q^{[j]} D_j = D_{j+1} ev, by covariance of the block map, so Q^{o,[j]} D_j = D_{j+1} (ev - Phi^{[j]} D_j). Compose. QED

r is the covariant block average: r^{[j]} omega (y) = avg over x in B_j(y) of (contour transport from y to x) omega(x). Its supports over distinct y are disjoint. At U = 1 it is the plain average over a unit cube, and r r^* = 1. In the axial gauge of a block, ||r - r_{U=1}|| <= C a, as the contours have angle at most C a s_{j+1} at level j and the sum over j of s_{j+1} is at most 2. So P_r := 1 - r^* (r r^*)^-1 r is an orthogonal projector, diagonal over blocks, and strictly local.

*The form.* Let lambda_n be the multiplier, D_U A = Q^{o*} lambda_n, and N^{(n)} the contour-free chain of Theorem 7, Step 1. Put

    bH[H, H'] := D^2 A(U)[H, H'] - <lambda_n, D^2 N^{(n)}[H, H']>,

defined for all H, H'. Let chain N^{(n)} be as there, so that N^{(n)}(U') = g(U') . M^n(U'), with g(U') a coarse gauge element smooth in U', and g^{[j]}(V_j) = 1, D g^{[j]} = -Phi^{[j]} at the base point.

**Lemma Inv (proved; no manifold and no assumption on the stabiliser of V').** *For every bond field H', and every omega with r omega = 0: bH[H', D_U omega] = 0.*

*Proof.* Let bA(U') := A(U') - <lambda_n, N^{(n)}(U') - V'>, in log coordinates at the base point. Then D bA(U) = D_U A - Q^{o*} lambda_n = 0, and D^2 bA(U) = bH, intrinsically, as U is a critical point of bA. For a fine gauge parameter omega let W_omega(U') be the gauge direction at U'. Gauge invariance of A gives D A(U')[W_omega(U')] = 0 for all U'. And M^n(e^{t omega} . U') = (e^{t omega}|_centres) . M^n(U'), so N^{(n)}(e^{t omega} . U') = h_t(U') . N^{(n)}(U'), with h_t(U') := g(e^{t omega} . U') (e^{t omega}|_centres) g(U')^-1, a smooth curve of coarse gauge elements with h_0 = 1, *defined explicitly, so no stabiliser enters*. With varpi(U') := d/dt|_0 h_t(U'),

    D N^{(n)}(U')[W_omega(U')] = D'_{N(U')} varpi(U')   for all U'.

At U' = U: varpi(U) = r omega, by the chain rule through the levels, since at each level the derivative of the gauge element is ev - Phi^{[j]} D_j = r^{[j]}. Now D bA(U')[W_omega(U')] = - <lambda_n, D'_{N(U')} varpi(U')>. Differentiate along H' at U. The left side gives bH[H', W_omega(U)] + D bA(U)[...] = bH[H', D_U omega], the second term vanishing at the critical point. The right side gives - <lambda_n, D'_{V'} (d_{H'} varpi)> - <lambda_n, (d_{H'} D'_N) varpi(U)>. The first of these is - <D'^* lambda_n, d_{H'} varpi> = 0 by the Ward identity: D_U A[D_U omega'] = 0 for all omega' gives <lambda_n, D' omega'|_centres> = 0, so D'^*_{V'} lambda_n = 0. The second vanishes since varpi(U) = r omega = 0. QED

*Consequences.* (Inv): bH[D_U omega, H'] = 0, for all H' and omega in ker r; D_U omega is in ker Q^o by (Cov). And bH on ker Q^o equals the Hessian of the true fibre on classes: a class has a representative in ker Q^o and one in ker Q^{(n)}, differing by D_U omega'' for some omega'', and the same computation with D A(U) = Q^{(n)*} lambda_n, on the true map M^n in place of N, shows the form on T_U (fibre of M^n) is the same as bH after that shift, as both are the second derivative of A along curves in the same coarse orbit, up to the multiplier's pairing with a coarse gradient, which the Ward identity kills. No bound on the singular composite contour Phi^{(n)} is needed. (Phi^{(n)} contains ev at a fine point, and is not bounded on L^2 uniformly in n, so a first form with H~ := H - D chi[H] in the proof would have been wrong uniformly in n.) By Lemma 3 and Theorem 7 of the package,

    (Size)  | bH[H, H] - ||d_U H||^2 | <= C(L) a ||H||^2,

with d_U H := eta^-2 (sum of the transported legs), and bH is local at the block scale.

Consumer's form: at a constant-flux background on the torus lambda_n = 0, and bH is the true Hessian bK of `checks/hard-core--mapped_sharp_bg.py`, checked against a finite difference of the SU(2) Wilson action to 2e-8. *A first numerical test, `checks/hard-core--mapped_sharp.py`, used ||d_U H||^2 in its place, and failed its identification at flux by 2 percent to 6 percent (A1, A2; its run reads FAIL), because d_U D_U omega = [F, omega].* With the true Hessian the identification holds to 2e-14, at L = 3, 5, m = 0, 1, 2. So (Inv) is really about the Hessian. It fails for the curl form alone.

## Lemma TP-sharp at U = 1 (proved)

*For a bond field H on the fine torus with Q^o H = 0, with phi := D^* H,*

    ||H||^2 + ||grad H||^2 <= C_# ( ||d H||^2 + ||P_r phi||^2 ),   C_# = C_#(d), uniformly in eta.

*Proof.* Fourier on the torus, p the coarse momentum, q = p + 2 pi n its aliases in the fine zone, hat q the fine lattice symbol, with |hat q| >= (2/pi)|q|. Let c := r phi, and note ||phi||^2 = ||P_r phi||^2 + ||c||^2, as r r^* = 1. Let B(p) := r (-Delta)^-1 r^* (p) = sum_n |hat r(q_n)|^2 / |hat q_n|^2. Then:

(a) B(p) |hat p'|^2 >= c_1 > 0, with |hat p'|^2 := sum 4 sin^2(p_nu/2). Keep n = 0: hat r(p) is a product of Dirichlet ratios, each at least 2/pi on |p_nu| <= pi, and |hat p|_fine <= |p|, and |hat p'|^2 >= (4/pi^2)|p|^2. So c_1 = (2/pi)^{2 d + 2}.

(b) Let G_mu(p) := sum_n |hat rho_mu(q_n)|^2 / |hat q_n|^2. Then |hat p'|^2 G_mu(p) <= c_2. The term n = 0 is at most C |hat p'|^2/|p|^2. For n != 0, each factor of hat rho_mu with n_nu != 0 is at most pi |sin(p_nu/2)|/|q_{n,nu}| <= 1/|n_nu|, and 1/|hat q_n|^2 <= C. The sum over n != 0 of the product over nu with n_nu != 0 of 1/n_nu^2 converges in every d. (Note hat rho_mu = (prod_nu hat b(q_nu)) hat b(q_mu), up to phases, from tri = box * box.)

(c) With S(p) := 1/B(p), put g := (-Delta)^-1 r^* S c. Then r g = c, and ||g||^2 <= c_3 ||c||^2: the term n = 0 is S^2 |hat r|^2/|hat p|^4 <= C by (a), and the others are at most S^2 C <= C.

(d) Let beta_mu(p) := hat p'_mu S(p) c(p) / |hat p'|^2, for p != 0, and beta(0) := 0. Note c(0) = 0, as the mean of D^* H vanishes. Then D'^* beta = S c, and by (a), |beta_mu| <= c_1^-1 |hat p'_mu| |c|. By (Cov) at U = 1, E := D g - Q^{o*} beta has D^* E = (-Delta) g - r^* D'^* beta = r^* S c - r^* S c = 0, and zero mean. So E = d^dagger (-Delta)^-1 d E, and d E = -d Q^{o*} beta.

(e) ||(-Delta)^-1 d Q^{o*} beta||^2 <= sum_p sum_mu G_mu(p) |beta_mu(p)|^2 <= c_1^-2 c_2 ||c||^2, using |q^ wedge v|^2 <= |q^|^2 |v|^2 alias by alias, and (b).

(f) Now, with Q^o H = 0, ||c||^2 = <r g, r phi> = <r^* r g, phi> = <g, phi> - <P_r g, P_r phi> = <D g, H> - <P_r g, P_r phi> = <E, H> + <beta, Q^o H> - <P_r g, P_r phi> = <(-Delta)^-1 d E, d H> - <P_r g, P_r phi>. So ||c|| <= c_4 ||d H|| + c_3^{1/2} ||P_r phi||. Hence ||phi||^2 <= C (||d H||^2 + ||P_r phi||^2), and ||grad H||^2 = ||d H||^2 + ||phi||^2, by the identity at U = 1. Finally Q^o H = 0 and Lemma 2 of the package give ||H||^2 <= C ||grad H||^2. QED

Numerics, `checks/hard-core--mapped_sharp.py`, Part B: at the trivial background the sharp constant in level-1 units, C_#, is 1.38, 1.50, 1.54, 1.56, 1.57 at d = 2, L = 3, 5, 7, 9, 11; 1.41, 1.62, 1.71 at d = 3, L = 3, 5, 7; 1.54, 1.79 at d = 4, L = 3, 5, on a coarse grid of momenta. So it looks like a limit, with no growth in L.

## Lemma TP-sharp at a background (proved given Lemmas 3, 4 of the package)

*There are absolute C_#' and R_0, and a_#(L) > 0, such that for U with R(a), a <= a_#(L), and Q^o_U H = 0:*

    ||H||^2_Eps <= C_#' ( ||d_U H||^2 + ||P_r D_U^* H||^2 ).

*Proof.* IMS at scale R. Let zeta_i be a partition of unity on cubes of side R, sum zeta_i^2 = 1, Lipschitz constant C/R, B_i the R-neighbourhood of supp zeta_i. On B_i take the axial gauge, |A~| <= C a R, and let H_i := zeta_i H in this gauge, on a torus T_i containing B_i, with U = 1 on T_i. Then:

- Q^o H_i = Q^o_U (zeta_i H) + (Q^o - Q^o_U)(zeta_i H) has l^2 norm at most s ||H||_{L^2(B_i)}, s := C/R + C(L) a R: the first part is the commutator with zeta_i, on rows of diameter at most 3, and the second is Lemma 4 with the change of gauge. Let F be the right inverse of Q^o by bumps, ||F|| <= C, and put H^_i := H_i - F Q^o H_i, so that Q^o H^_i = 0.
- By the lemma at U = 1, ||H^_i||^2_Eps <= C_# ( ||d H^_i||^2 + ||P_r D^* H^_i||^2 ).
- ||d H^_i|| <= ||zeta_i d_U H|| + s ||H||_{Eps(B_i)}, from the commutator and |A~|.
- D^* H_i = zeta_i phi + O(s) |H|. And P_{r}(zeta_i phi) = zeta_i P_{r_U} phi + (commutator of P_{r_U} with zeta_i, norm at most C/R) phi + (P_r - P_{r_U})(zeta_i phi), of norm at most C a R ||phi||. So ||P_r D^* H_i|| <= ||zeta_i P_{r_U} phi|| + s ||H||_{Eps(B_i)}, as ||phi||_{L^2(B_i)} <= C ||H||_{Eps(B_i)}.

Sum over i, with bounded overlap, sum ||H_i||^2_Eps >= ||H||^2_Eps - s^2 ||H||^2 up to the same gauge error, and H^_i - H_i has Eps norm at most C s ||H||_{L^2(B_i)}. So ||H||^2_Eps <= C ( ||d_U H||^2 + ||P_r phi||^2 ) + C s^2 ||H||^2_Eps. Choose R = R_0 absolute, then a small in L. QED

Only U = 1 is a global statement; a background is local. So no low mode of size a/L^2 can arise, which was the worry of `checks/hard-core--mapped_tp_flux.py`, and this replaces Lemma TP at a background. Numerics, `checks/hard-core--mapped_sharp_bg.py` Part D', with the true Hessian: at d = 2, lam#t = 0.728, 0.726, 0.729, 0.733, 0.738 at L = 3, a' = 0, 0.044, 0.087, 0.175, 0.349, and 0.684, 0.676, 0.682, 0.685 at L = 5, a' = 0, 0.098, 0.196, 0.393.

*Corollary, (H1).* bH on classes is at least c ||H||^2_Eps for the representative with P_r phi = 0, which exists since P_r (-Delta_U) P_r is positive on ker r by Poincare. With the chart map below this gives (H1) with gamma(L), with no Landau representative and no Lemma TP.

## Theorem F (the torus)

Let K# := bH + D_U P_r D_U^*, and Sad# := [[K#, Q^o*], [Q^o, 0]].

(i) Sad# is an isomorphism from Eps x l^2 to its dual, with norm of the inverse at most C_F absolute: bounded by Lemma 3, coercive on the kernel by the lemma above and (Size), and inf-sup by the bumps of Theorem 6.

(ii) If f is Lipschitz with constant delta in level-n units and delta <= delta_#, absolute, then e^f Sad# e^-f is invertible with the same bound. The change in bH is first order, with coefficient C delta, and in its Lagrange part it is C delta C(L) a. The commutator of P_r with e^f has norm at most C delta on L^2, as P_r is diagonal over blocks. The change in Q^o is at most C delta from L^2. All are bounded on Eps by C delta.

So ||1_X Sad#^-1 1_X'||_{Eps^* -> Eps} <= C e^{-delta_# dist(X, X')}, absolute constants.

(iii) *Exactness.* If J in Eps^* vanishes on D_U omega for all omega in ker r, and (H, lambda) := Sad#^-1 (J, 0), then P_r D_U^* H = 0, and H represents the minimiser of bH/2 - J over classes ker Q^o / D_U(ker r). *Proof.* Test with D_U omega, omega in ker r, which lies in ker Q^o. By (Inv) and J(D_U omega) = 0, <P_r D_U^* H, P_r (-Delta_U) omega> = 0. Take omega := (P_r (-Delta_U) P_r)^-1 P_r D_U^* H, in ker r. So P_r D_U^* H = 0. Then bH[H, H'] = J(H') on ker Q^o. QED

(iv) *The chart.* Let X^o := Q^{o,(k)} H, a^o(y') := Phi^{[k]} X^o(y'), with a one-level contour only, chi_k[a^o] the level-k function with values a^o at level-(k+1) centres, and 0 elsewhere, and X := X^o - D_k chi_k[a^o]. Then Q^{[k]} X = 0. Let xi(H) be the free bonds of the tree-gauge representative of X. Then |xi(H)|_box <= C(L) ||H||_{L^2(box and neighbours)}: Lemma 4 for Q^{o,(k)}, and one level for the rest. And xi(H + D_U omega) = xi(H) for omega in ker r: X^o moves by D_k omega_k, omega_k := r^{(k)} omega, r^{[k]} omega_k = 0, and a^o by ev omega_k. So X moves by D_k(omega_k - chi_k[ev omega_k]), whose parameter vanishes at centres, and the tree gauge removes it.

(v) *The Schur step.* A_k restricted to the level-k fibre is the minimum of A over its inner fibre. So M, the Hessian in the chart at V^*, is the Schur complement of bH on classes with respect to ker xi. Hence M^-1 eta = xi(H_eta), with H_eta the class minimiser for J := eta . xi.

**Conclusion, torus.** With J_i := xi_i, |M^-1(xi_i, xi_j)| = |J_i(H_j)| <= C(L) ||H_j||_{L^2(box i, neighbours)} <= C(L) e^{-delta_# d(i, j)} ||J_j||_{Eps^*} <= C(L)^2 e^{-delta_# d(i, j)}, for a <= a_#(L), with delta_# absolute. QED

Why the gap does not set the rate: the small eigenvalues of M live in ker of the map from the chart to the class form, in the sense that a chart coordinate reads a class through a box-local functional of norm C(L). C(L) enters only as a prefactor.

*Numerics.* `hard-core--mapped_sharp.py`, Part C, at U = 1: rate of H per box 1.50, 1.38, 1.35, 1.33, 1.33 at d = 2, L = 3, 5, 7, 9, 11; 1.90, 1.76 at d = 3, L = 3, 5; 2.53 at d = 4, L = 3. In d = 2 the curvature's rate at L = 11 from distance 2 was 1.331 against a prediction, made before the run, of arccosh 2 = 1.317. That prediction comes from d = 2 having no Bianchi identity: there F = J_2 - Q_2^* mu', mu' = (Q_2 Q_2^*)^-1 Q_2 J_2, so the rate is the pole of the inverse Gram matrix of tri x tri, whose symbol is ((2 + cos p)/3)^2 in each axis direction. It is free of L and it has nothing to do with the gap.

## Theorem F-D (a frozen exterior)

**Why Dirichlet needs its own argument.** For i, j at distance from the frozen set Omega, the Dirichlet principle alone gives, with A := M^-1 on the torus and M_Y the restriction,

    |M_Y^-1(i, j) - A(i, j)| <= C(L) e^{-rho (d(i, Omega) + d(j, Omega))}:

w := M_Y^-1 eta_j - A eta_j is M-harmonic on Y with data -A eta_j on Omega, of energy at most C(L) e^{-2 rho d(j, Omega)}, and <eta_i, w> = -<w_i', w>_M, by harmonicity against M_Y^-1 eta_i. This is enough for pairs in the middle of a shell, and it gives nothing for i next to one wall and j next to the other. That is exactly K of the upper chain's free cross-ratio, so a real argument is needed. It is also why a global H^1 norm has to go: the gauge-fixed field has a jump in its normal component at the wall, in the limit, so ||grad H||^2 is about L |H_n|^2 there.

**Setting.** U on the torus with R(a), or with ||F||_{L^4(box)} <= a as in hostile point (6') (a class fill: Text 5.3, (H1) in the ball). Y a union of level-n boxes, Omega the rest. Free level-k bonds: at least one end in a box of Y, so gauge parameters on all sites of Y-boxes are allowed, and no block centre of Omega moves. Constraints bC H := ( Q^{o,(k)} H on bonds with both ends in Omega ; Q^{o,(n)} H on parents with a free bond ). r_N := ( r^{(k)} on level-k sites of Omega ; r^{(n)} on blocks of Y ). P_N := the projector on ker r_N, diagonal over level-n blocks. Then Q^o-covariance gives { omega : D_U omega in ker bC, with the zero block means } = ker r_N, and K#_N := bH + D_U P_N D_U^*, Sad#_N as before with bC. The norm is the graph norm, not Eps:

    ||H||_G^2 := ||H||^2_{L^2} + ||d_U H||^2 + ||P_N D_U^* H||^2,   ||(Y_n, Y_k)||_Lam^2 := ||Y_n||^2 + L^2 ||Y_k||_{N_k}^2.

**Lemma D-coer (L^2 coercivity, derived; constant through one extension).** For H in ker bC, ||H||_{L^2}^2 <= C ( bH[H, H] + ||P_N D_U^* H||^2 ), with C depending on the extension constant C_ext of Omega at box scale, in the sense below.

*Proof.* (1) H is in ker Q^{o,(n)}. By the torus results write H = H_s + D_U omega, with omega in ker r^{(n)}, P_r D_U^* H_s = 0, ||H_s||^2_Eps <= C bH[H, H]. (2) ||D_U omega||^2 = <omega, D_U^* H - D_U^* H_s> = <omega, phi>, since D_U^* H_s is in the range of r^* and omega is in ker r^{(n)}. (3) Let omega_k := r^{(k)} omega. On bonds with both ends in Omega, D_k omega_k = Q^{o,(k)} D_U omega = -Q^{o,(k)} H_s, which is bounded in density normalisation by C ||H_s||_{L^2}. And r^{[k]} omega_k = r^{(n)} omega = 0 on each block, so by Poincare in the box, omega_k on a box of Omega is bounded by its gradient. (4) *Extension.* Let omega~_k be an extension of omega_k from Omega to all level-k sites, with ||omega~_k||_{N} + ||D_k omega~_k||_{N, density} <= C_ext C ||H_s||_{L^2}, and with zero means on the blocks of Y, by a bump. Let omega^ be the minimal fine function with r^{(k)} omega^ = omega~_k. By (c) of the lemma at U = 1, at level k, ||D_U omega^|| <= C ||D_k omega~_k||_{density}, and ||omega^|| <= C(...) too. (5) Now r_N (omega - omega^) = 0, so <omega - omega^, phi> = <omega - omega^, P_N phi>. And <omega^, phi> = <D_U omega^, H>. Hence

    ||D_U omega||^2 <= (C ||D_U omega|| + ||omega^||) ||P_N phi|| + ||D_U omega^|| ( ||H_s|| + ||D_U omega|| ).

Absorb: ||D_U omega|| <= C (||P_N phi|| + ||H_s||), and ||H|| <= ||H_s|| + ||D_U omega||. QED

No H^1 norm on H is used, and no constraint on Omega beyond (3) and (4), and the proof uses the torus lemma as a black box.

**The extension constant.** For flat walls and cube corners, the geometry of the consumer's shell, reflection gives C_ext absolute, since the extension needs only reflect omega_k by a distance of order one box, with the block mean removed. At a pinch, where two boxes of Omega touch only along a face of codimension at least 2, the traces near the pinch disagree, by up to (log L)^{1/2} times the energy, and I only have C_ext about (log L)^{1/2} there. *Way out:* choose frozen sets as unions of cells of a brick tiling, as follows.

**Lemma BG (`Brick geometry`; derived, 2026-10-31).** Let T_1 be the tiling of the line by intervals of length t_0, and T_d the tiling of R^d by layers of height t_0 in x_d, where layer m carries T_{d-1} shifted by m v_{d-1} in R^{d-1}, with v_{d-1} := t_0 (2^{-(d-1)}, ..., 2^{-2}, 2^{-1}), and t_0 a multiple of 2^{d-1} L, so that all walls lie on block faces. *The order matters.* A first form with (1/2, 1/4, ...) has a pinch at d = 3: walls of T_2 in x_1 lie at (t_0/2) Z, and a shift by t_0/2 maps them onto themselves, so two layers can share a wall segment, with four cells on a line. In the order here, walls of T_{d-1} in coordinate i lie at t_0 2^{-(d-2-i+1)} Z for i <= d-2 and at t_0 Z for i = d - 1, and the shift moves them off that set, in each coordinate. Then (a) at most d + 1 cells meet at any point, and near a point where exactly m + 1 cells meet, the tiling is a product of R^{d-m} with a fan of m + 1 cells, any two of them sharing a facet. (b) For Omega any union of cells and x on its boundary, there is a bi-Lipschitz map, with absolute constant, of the ball about x of radius t_0/8 onto a ball, taking Omega to a half-ball. (c) So the extension of Lemma D-coer, Step (4), exists with C_ext absolute.

*Proof.* (a) By induction on d: at a point with x_d not a multiple of t_0, the pattern is that of T_{d-1} times a line. At a point with x_d = m t_0, it is P_+ on top and P_- below, with P_+, P_- the patterns of T_{d-1} and of its shift at x'. The walls of T_{d-1} and those of its shift by v_{d-1} are disjoint in each coordinate, by the choice of v. So at x' the coordinate sets of the two strata are disjoint. If P_+ has k + 1 cells and P_- has l + 1, then k + l <= d - 1, and the total is k + l + 2 <= d + 1. Any two cells of P_+ share a facet, by induction, and a cell of P_+ meets a cell of P_- along a facet inside x_d = m t_0, as their bases overlap in an open set, by transversality. (b) The pattern at x is a complete fan with m + 1 maximal cones, each pair sharing a facet, so it has the combinatorics of the fan with rays e_1, ..., e_m, -sum e_i, times R^{d-m}. A cone-wise linear map, after subdividing a cone that is not pointed, such as the half-space cell of a T junction, takes one to the other. It is bi-Lipschitz, with a constant depending only on the pattern, and there are finitely many patterns, with no dependence on t_0 after scaling. In the model fan, written as cells C_i := { x_i = max_j x_j } in R^{m+1} modulo the diagonal, a union over i in S is { f >= 0 }, f := max_S x - max_{S^c} x. Since f(x + t 1_S) = f(x) + t and f is Lipschitz, this is a Lipschitz graph in the direction 1_S, so bi-Lipschitz to a half-space. **So there is no pinch, for any S.** The two-brick domain, which is not a graph domain, occurs in T_3, and it is covered: it is only the image of the model under a piecewise linear map. (c) Reflect in the flattened coordinates on each ball, and glue by a partition of unity at scale t_0/8. For a lattice function, interpolate multilinearly, extend, and take block means; t_0 is at least L cells, so the energies are comparable, and the block means on Y are removed by a bump as in Step (4). QED

*Numerics.* `checks/hard-core--mapped_brick.py`, criteria written first: PASS. d = 2, 3, 4: no pinching pair, at most d + 1 cells at a point, and the cells cover. Control: the other order of shifts has 70 pinching pairs in the same window at d = 3, as it should. The check is combinatorics only.

*Against the consumer's faces.* In Prop MD* the frozen sets are unions of bricks inside the thirds of the shell A, as the fronts of `library/quiet-boundary-rarity.md` are made of bricks. So nothing frozen meets a face of I', I'' at a corner of another kind. A pinch can only arise if a consumer freezes a set not made of bricks, and then it may enlarge it, as frozen regions may be enlarged freely in Prop MD.

**Nest coercivity: frozen data at several levels (derived, IMS over one-jump models, each step below; consumer: (I_l^𝔡) of `library/quiet-boundary-rarity.md`, and the upper chain's (MD*_j)).** Let frozen data sit on layers at several levels, each layer made of whole parent blocks, with clearance at least t_0 cells of the coarser level. Let s(x) be the local constraint scale: s_{l+1} on free level-l bonds under frozen parents, s_l on a frozen level-l layer. Let s^#(x) := the larger of the two scales for x within R_0 of the coarser scale from a wall, and s(x) otherwise. So s <= s^# <= L s. Then

    || H/s^# ||^2 <= C ( ||d_U H||^2 + ||P_N D_U^* H||^2 ),   H in ker bC,   with C absolute.                (NC)

*A first form was wrong.* I had s in place of s^#, with C absolute. A hostile estimate kills it. Let H = D omega with omega in ker r_N at U = 1, and psi := P_N X omega at the coarse scale L s on the Y side. Then omega has gradient g about L s |psi| at the wall. Its flux enters the first fine block of Omega, where the block mean forces it to turn. So ||D omega / s||^2 on Omega is about g^2 s / s^2 per unit of wall, against ||psi||^2 about L s: a ratio L. This is the jump in the normal component that I had already noted above, and it is real. `checks/hard-core--mapped_nest_weight.py`, pure gauge modes at U = 1, d = 1, criteria first: with the fine weight, Rho/L = 0.062, 0.070, 0.076, 0.081, 0.086, 0.090, 0.093 at L = 3, 5, 7, 9, 13, 17, 25; with s^#, Rho = 0.102, 0.104, 0.104, 0.104, 0.105, 0.105, 0.105, which is about 1/pi^2. The first run read FAIL on the second, from an error in my ring distance that left one wall at the fine weight; the top mode located it; with the fix, and criteria unchanged, PASS. It covers the pure gauge sector only. So at the fine weight the constant is C L^2 (trivially, by s^# <= L s), per wall, and it does not compound.

*What fails at the top scale:* near a level-j sheet the fine curvature is about T/s_j^2, enormous in level-n units, so the torus lemma cannot be applied at scale s_n. *What holds at the patch scale:* |F| (s^#)^2 is at most C T L^2 = C a_*, in an L^4 sense, on each patch.

*Proof of (NC).* Take chi_i with sum chi_i^2 = 1, patches of size R_i := R_0 s^#_i, |grad chi_i| <= C/R_i, each patch meeting at most one wall, by clearance. In the patch's gauge the background is U = 1 up to C a_* R_0^2. Put H_i := chi_i H - B_i, with B_i the block bump restoring the constraints.

- On a block of scale sigma <= s^#_i: Q^o (chi_i H) = Q^o ((chi_i - chi_i(z)) H), which has density at most C (sigma/R_i) times that of H on the block. So ||B_i||^2 on the block is at most C (sigma/R_i)^2 ||H||^2 there, and ||d B_i||^2, ||D^* B_i||^2 at most C ||H||^2 / R_i^2.
- ||d chi_i ^ H||^2 and ||grad chi_i . H||^2: at most C ||H||^2 / R_i^2.
- P_N (chi_i phi) = chi_i P_N phi + [chi_i, 1 - P_N] phi, with (1 - P_N) phi = sum over blocks z of c_z r_z^*. By the bound on block means below, ||(1 - P_N) phi||_z <= C ( ||H||_{z+} / sigma + ||P_N phi||_{z+} ). The commutator carries chi_i - chi_i(z), of size sigma/R_i. So it is at most C ||H||_{z+} / R_i + C (sigma/R_i) ||P_N phi||_{z+}.

All errors are at most (C/R_0^2) ||H/s^#||^2 + (C/R_0^2) ||P_N phi||^2, and sigma-summation is free as blocks are disjoint. In the patch, H_i is in ker Q^{o} at the coarser scale, since a finer constraint implies a coarser one. So the model is exactly Lemma D-coer at U = 1, with one flat wall, at scale s^#_i: ||H_i||^2 <= C s^#_i^2 ( ||d H_i||^2 + ||P_N D^* H_i||^2 ), and C is absolute. The term of size a_* R_0^2 is absorbed for a_* small. Summing over i and taking R_0 large gives (NC). QED

*What (NC) is used for.* The curvature term of bH: |<F, [H, H]>| <= C(L) T L^2 ||H||_G^2 = C(L) a_* ||H||_G^2, using s^# <= L s, with L^4 of F against G and Eps equivalent up to L at a jump, as in (6') below; small, as a_* comes after L. Commutators with e^f, for f Lipschitz in units of the top level: only ||H||_{L^2} and the block means enter, as in Theorem F-D, and they are smaller on finer blocks.

*A layer must contain whole parent blocks.* A strip inside a block is a hole inside a box: a constant rotation of the strip, compensated inside its blocks so that r^{(l)} omega = 0, keeps its bonds fixed at flat data. Check N of `checks/hard-core--mapped_sharp_two.py`, first run: coercivity 0.000 at flat data, and 0.173 and 0.554 at level-2 flux a' = 0.39, 0.79, against 9.78 with no layer and with a whole-block layer (9.78, 10.41 at a' = 0, 0.39). The growth by 3.2 is near the low end of the factor [3, 5.5] I stated before the second run around a'^2 = 4, so a'^2 is only a rough description. So the mode is a soft one at nearly flat data, and it would make (H1) fail uniformly in the data. With whole blocks r^{(l)} omega = 0 forces omega = 0 on a frozen block, and the mode is gone.

**Theorem F-D.** For a <= a_#(L), and Omega with C_ext absolute, Sad#_N is invertible on G x Lam^* with an absolute bound, stable under e^f, f Lipschitz with constant delta <= delta_#. And for gauge-invariant J, its solution has P_N phi = 0 and it represents the class minimiser. So |M_Y^-1(i, j)| <= C(L) e^{-delta_# d(i, j)} for all i, j in Y, including across a shell and along a wall.

*Proof.* Coercivity on ker bC: Lemma D-coer, and (Size). Inf-sup in Lam: a right inverse on Lam by bumps at scale 1/L on Omega, of G norm at most C L ||Y_k||_{N_k}, and bumps at scale 1 on Y, inside the Y part of a straddling tile. These are biorthogonal in the box, since a box of Y carries two overlapping tile weights and a bump on the box separates them. The norm of bC from G to Lam is about L and it does not enter: the bound on Sad^-1 uses only coercivity, inf-sup and the size of K#.

*The commutators, which is where the graph norm has to work.* With e^f:

- bC: [Q^{o,(k)}, e^f] has norm at most delta/L from L^2 to N_k, as the tile has size 1/L. In Lam that is delta. [Q^{o,(n)}, e^f]: delta.
- d_U, D_U^*: multiplication by grad f, size delta on L^2.
- P_N: (1 - P_N) phi = sum over thin blocks z of c_z r^{(k)*} delta_z, plus sum over blocks y of c_y r^{(n)*} delta_y. Multiplying by a function G, with |G| <= C delta on a block and Lipschitz constant C delta, P_N kills the value of G at the block's centre. So the commutator is at most (C delta / L) ||c_z||_{N} + C delta ||c_y||. And the block means are bounded in the graph norm, trivially: with g a bump at the scale of the block, r_N g = c, ||c||^2 = <g, phi> - <P_N g, P_N phi> = <D_U g, H> - <P_N g, P_N phi>, so ||c_z||_N <= C (L ||H||_{L^2} + ||P_N phi||), and ||c_y|| <= C (||H||_{L^2} + ||P_N phi||). So the commutator is at most C delta ||H||_G, with no L.

So e^f Sad#_N e^-f is a perturbation of size C delta. Exactness: as (iii), with ker r_N in place of ker r. The chart: as (iv), as X^o = 0 on bonds of Omega gives a^o = 0 on blocks of Omega. M_Y is the Schur complement for this class problem. QED

*Numerics at two levels.* `checks/hard-core--mapped_sharp_two.py`, d = 2, L = 3, fine torus 36, criteria written first. Part K: steps (iv), (v) with the composite Q^o and the chart read through it, against a direct problem with the true maps only: agreement to 3e-13 at a' = 0, 0.39, 0.79, and (Cov) to 5e-17. Part N: with level-1 data frozen on Omega and fine data frozen on whole level-1 blocks: identification to 2e-14. One size only, so nothing on the dependence on L.

*Numerics.* `checks/hard-core--mapped_sharp_bg.py`, criteria written first: PASS. Part E, d = 2, strip with a frozen exterior: the identification with the tree-gauge M_Y^-1 holds to 3e-14, at flux too, and P_N phi = 0 to 7e-15. L^2 coercivity cn = 9.0000, 9.5492, 9.7051, 9.7698 at L = 3, 5, 7, 9: this is L^2 4 sin^2(pi/(2L)), the Neumann gap of a block, reached by a pure gauge mode, and it tends to pi^2. So it has no dependence on L to speak of. Rate across the strip from a bond next to one wall: 1.53, 1.43, 1.40, 1.39. Along the wall, from two points only: 2.37, 2.53, 2.25, 2.15. At flux: cn rises slightly, the rate across is unchanged to 1e-3, and the rate along to 1e-2. Part F, Bloch along the wall: cn = 9.00, 9.55, 9.71 at d = 3, L = 3, 5, 7 and 9.00 at d = 4, L = 3; smallest rate across 1.57, 1.44, 1.46 at d = 3 and 1.59 at d = 4. Limits: k = 0; flat walls; constant flux; d = 3, 4 at the trivial background; L = 7 at w = 3.

## Hostile check

(1) *Is r r^* really invertible at all levels with the covariance exact?* A0 tested (Cov) at one level to 2e-16 at flux. At several levels it is a composition. The size of r - r_{U=1} is the same recursion as in Lemma 4, simpler, since there is no contour term.

(2) *(Inv) off-shell, and at a reducible parent.* A first version argued through a manifold of fields over the coarse orbit of V', which is not a manifold of the stated tangent when V' has a stabiliser, as at V' = 1. Lemma Inv above replaces it, by a direct differentiation, with the coarse gauge element defined explicitly. What the proof reads: smoothness of g^{[j]} near the base point, and the Ward identity. *Test at a non-zero multiplier:* `checks/hard-core--mapped_sharp_lam.py`, criteria written first, PASS. Cartan constrained minimiser at non-constant flux, d = 2, one level, L = 3, 5, nc = 8, a' up to 0.42, |lambda| up to 9e-3, with the second-order parent phase derived by hand and checked against the actual SU(2) block map. Gauge directions null on the true fibre to 1e-15, with lambda omitted 2e-4 to 4e-3. Lemma Inv in the strong form, on all bonds, to 1e-15, with the chain's cross term omitted 3e-4 to 5e-3. The identification with the tree-gauge M^-1 to 7e-11, and P_r phi = 0 to 7e-11. lam# within 2 percent of its value at zero field, and the rate unchanged to 1e-2. *What I would still attack:* "the same computation on the true map" in the consequences is one sentence. The test above covers it numerically at one level, and at several levels only by composition.

(3) *Does IMS in the background lemma lose the rate?* No: it enters only the coercivity constant, which is absolute because R_0 is absolute. C(L) a is small by the order of constants, as a <= a_# comes after L, and T_2 L^2 is of the order a_*.

(4) *Does anything in Theorem F read the gap?* No. C(L) enters through ||J_i||, a prefactor, and through a_#.

(5) *Coarse zero modes.* At V' = 1 the constant omega has D_U omega = 0, so nothing is lost. And c(0) = 0 was used in (d). At a background there is no Fourier step.

(6) *Is the solution in Eps?* Yes on the torus. For Theorem F-D, in the graph norm only.

(6') *R(a) at the actual lift.* U^* = e^{i eta H} U^tr has ||F||_{L^4(box)} <= C a by (R3), not a pointwise bound: a pointwise bound fails by a logarithm at nested block centres. Three places read it. (i) Lemma 3's curvature term is at most ||F||_{L^4} ||H||_{L^{8/3}}^2 <= C a ||H||_Eps^2. (ii) Lemma 4, and r - r_{U=1}: a contour's angle at level j is at most C(L) theta_j, and theta_j <= s_j ||F||_{L^4}, summable over a nest. With only an Eps bound on H, the product over a nest would be exp(C sum_j ||H||_{L^4(B_j)}), which is not summable. **So (R3) is on the path of Theorem F, and an Eps ball is not enough.** (iii) Theorem F-D: terms bounded by C(L) a ||H||_Eps^2 are not obviously bounded by the graph norm. They are, up to C(L): ||grad H||^2 is at most ||d_U H||^2 + ||phi||^2 up to small terms, and ||phi||^2 = ||P_N phi||^2 + ||r_N^* c||^2 <= C L^2 ||H||_G^2, by the trivial bound on block means. So G and Eps are equivalent up to a factor L, and C(L) a is small after L.


(7) *The non-Gaussian law.* This note is about M only. The use with V, cut and fields frozen is in `library/preconditioned-covariance.md`, through (A) of HS-P, which reads A = M^-1 at a reference and the size of V. For the frozen exterior, A = M_Y^-1.

(8) *The form in Prop MD.* V^fill is class everywhere, with the local form equal to its Hessian on variations in Y, up to tails, by (H1) in the ball. So M_Y is at V^fill, and the difference belongs to V. The tail x T^2 |A| e^{-2 delta D_c} is small by the choice of D_c.

(9) *Does the second tier of Lemma HS-C go away?* No. The cut lives in the chart, and barrier energy needs a diagonal weight in the chart, which is (W) of HS-M. This note improves M^-1, not (W).
