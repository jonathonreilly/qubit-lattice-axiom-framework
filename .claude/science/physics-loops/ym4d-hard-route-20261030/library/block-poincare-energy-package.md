# Block Poincaré and the energy package for the hard constraint

Producer: `parts/hard-core--mapped.md`. Status: proved here at real and small complex backgrounds on the single-level determining set, with every constant depending on d and L only; extension to nested determining sets stated as a route. Not reviewed.

Credit: the operators (block averages, constrained covariance) are Balaban's. He obtains the corresponding bounds by random-walk expansions (CMP 95, 96, 99). The proof below does not use walks and is mine. It rests on Lemma 3.1 of the producer file: the contour part of the linearised average is a coarse gradient. Dependence on the Sussman-Alpoge account: none in the proof; the need for M-free constants is taken from its Proposition 2.4:prop-m-freeness.

Consumers: operator bounds in the small-field step; M-freeness of the gap and of the decay rate, which the account's order of constants requires.

## Setting

Fine lattice eta Z^d in level-k units, eta = L^-k, d = 4 (the argument is dimension free). Bond field U with values in SU(2). Fluctuation U -> exp(i eta B) U with B a su(2)-valued bond field. ||B||^2 := eta^4 sum_b |B(b)|^2. For a box R, ||B||_R is the same sum restricted to bonds in R.

Covariant differences: (grad_nu B_mu)(x) := [B_mu(x) - Ad_{U_nu(x)} B_mu(x + eta e_nu)]/eta. Covariant gradient on sites (D omega)(x,nu) := omega(x) - Ad_{U_nu(x)} omega(x + eta e_nu).

K(U) := H(U) + D_U D_U^*, with H(U) the Hessian of A(exp(i eta B) U) in B at 0, A = sum_p (1 - Re tr U(dp)). Write E_U(B) := <B, K(U) B> with the normalisation that at U = 1 it equals ||grad B||^2.

Regularity R(a): |U(dp) - 1| <= a eta^2 for every fine plaquette p.

Q^o_U: the composite block operator with the coarse gradient part removed at every level, as in Lemma 3.9(b) of the producer file, read at a general background: at each level j -> j+1, Q^{o,[j]} = Q^[j] - D_{j+1} Phi^[j], with Phi^[j] the covariant contour average. In potential normalisation, Q^o_U B (c) is the value attached to the level-k bond c.

## Lemma 1 (weights)

At U = 1, Q^o B(c) = eta^4 sum_x rho_c(x) B_mu(x) for c = (y, mu), with rho_c = tri(x_mu - y_mu) prod_{nu != mu} box(x_nu - y_nu), rho_c >= 0, integral 1, sup rho_c <= 1, support in the box R_c := y + [-1/2, 3/2] in direction mu and [-1/2, 1/2] in the others. Over y in Z^d the boxes R_{(y,mu)} cover space with overlap at most 2.

*Proof.* Telescoping of Dirichlet kernels in Lemma 3.1 of the producer file. QED

## Lemma 2 (lattice Poincaré with a bounded weight)

Let R be a box of side at most 3, rho >= 0 on R with eta^4 sum rho = 1 and sup rho <= C_rho, f a function on the fine points of R. Then ||f||_R^2 <= C (||grad f||_R^2 + |<rho, f>|^2), with C depending on d and C_rho, uniformly in eta.

*Proof.* With fbar the uniform average, Poincaré-Wirtinger on the lattice box gives ||f - fbar||_R^2 <= C ||grad f||_R^2, uniformly in eta. |<rho, f> - fbar|^2 = |<rho, f - fbar>|^2 <= <rho, |f - fbar|^2> <= C_rho ||f - fbar||_R^2. Hence ||f||_R^2 <= 2 ||f - fbar||_R^2 + 2 |R| fbar^2 <= C ||grad f||_R^2 + 4 |R| (C_rho ||f - fbar||_R^2 + |<rho,f>|^2). QED

## Lemma 3 (lattice Weitzenböck with holonomy)

Under R(a), with a <= 1: E_U(B) = ||grad_U B||^2 + T, with |T| <= C a (||B||^2 + eta ||B|| ||grad_U B||). Hence E_U(B) >= (1 - C a) ||grad_U B||^2 - C a ||B||^2, and E_U(B) <= 2 ||grad_U B||^2 + C a ||B||^2.

*Proof.* Transport to the base of the plaquette: U(dp) with fluctuations is e^{i H_1} e^{i H_2} e^{i H_3} e^{i H_4} Phi, with Phi = U(dp), H_1 = eta B_mu(x), H_2 = eta Ad_{U_mu(x)} B_nu(x + eta e_mu), H_3 = -eta Ad_{T} B_mu(x + eta e_nu), T = Phi U_nu(x), H_4 = -eta Ad_Phi B_nu(x). The second-order part of 1 - Re tr is (1/2) tr(sum H_i)^2 + O(|Phi - 1|) sum |H_i|^2, because at Phi = 1 the terms combine to the square. Sum over p: the error is at most C a eta^4 sum_b |B|^2 = C a ||B||^2. Next, sum_i H_i = eta^2 (grad_nu B_mu - grad_mu B_nu)(x) + O(a eta^3 |B|), using |Ad_Phi - 1| <= C a eta^2. So the plaquette part is ||d_U B||^2 with an error at most C a eta ||B|| ||grad_U B|| + C a^2 eta^2 ||B||^2. D^* contributes ||grad^- . B||^2, the backward divergence. At U = 1, summation by parts gives ||d B||^2 + ||d^* B||^2 = ||grad B||^2 exactly. At U, the cross terms differ by the commutator of a forward and a backward covariant difference in two directions, which is eta^-2 (Ad_Phi - 1) composed with shifts: at most C a times a product of |B| at neighbouring bonds, and a shift changes B by eta grad_U B. QED

## Lemma 4 (the constraint at a background)

Assume R(a). For a level-k bond c let box(c) be a box of side 3 containing R_c and all supports of Q^o_U at c. In the axial gauge of box(c), U = exp(i eta Atilde) with |Atilde| <= C a, and with Btilde the gauge transform of B, Q^o_U B(c) = <rho_c, Btilde_mu> + Err(c), |Err(c)| <= C(L) a ||Btilde||_{box(c)}.

*Proof.* The axial gauge bound: the angle on a fine bond is the flux through a strip of width at most 3 and height eta, so at most 3 a eta. Now induct on the levels with N_j(theta) := (s_j^4 sum_b |theta(b)/s_j|^2)^{1/2}, restricted to the box, s_j = L^{j-k}. One step of Q^o at level j is a path average with weights changed by a relative C a s_{j+1}, since the transports over a level-(j+1) bond are angles at most C a s_{j+1}, plus a contour sum with coefficient C a s_{j+1}^2, since the loop flux is at most a s_{j+1}^2 and the factor L'(phi-bar) L(phi_loop) - 1 of Lemma 3.9(a) vanishes with the flux. The path average with positive weights summing to 1 satisfies N_{j+1} <= N_j, by Jensen and the count of tubes. The weight change contributes C a s_{j+1} N_j. For the contour sum: with weights w'_b <= 1 and sum w'_b <= C L over at most (C L)^d bonds, Cauchy-Schwarz gives a bound C(L) N_j on the block, and so C(L) a s_{j+1}^2 N_j in all. The sum over j of s_{j+1} is at most 2, so the composite differs from the path composite by at most C(L) a in the operator norm from N_0 to N_k, and the same computation with the box restriction is the local statement. At the level of the bond c this is Err(c). QED

## Theorem 5 (coercivity)

There are a_* and C_P depending on d and L only such that for all U with R(a), a <= a_*, and all B with Q^o_U B = 0: ||B||^2 <= C_P ||grad_U B||^2 and E_U(B) >= gamma ||B||^2 + (1/2) ||grad_U B||^2, with gamma = 1/(4 C_P). No dependence on k, eta, the block size M, or the volume.

*Proof.* In the gauge of box(c), Lemmas 2 and 4 give ||Btilde_mu||_{R_c}^2 <= C ||grad Btilde_mu||_{R_c}^2 + C a^2 ||Btilde||_{box(c)}^2. Since |Atilde| <= C a, grad Btilde differs from the transform of grad_U B by at most C a |Btilde|. The norms are gauge invariant. Sum over c and mu, using the finite overlap: ||B||^2 <= C ||grad_U B||^2 + C a^2 ||B||^2. Absorb. Then Lemma 3. QED

## Theorem 6 (saddle operator and decay)

Let Eps be the completion of bond fields in ||B||_Eps^2 := ||grad_U B||^2 + ||B||^2. The operator Sad(U) := [[K(U), Q^o_U^*], [Q^o_U, 0]] from Eps x l^2(level-k bonds) to its dual is an isomorphism with norm of the inverse at most C(d,L). It is analytic in small complex perturbations U -> exp(i eta A') U with |A'|, |grad_U A'| <= a_1(d,L). Let C_U be the first block of the inverse, the constrained covariance. For f Lipschitz with constant delta, delta <= delta_*(d,L), and boxes X, X' of side 1 in level-k units, ||1_X C_U 1_X'||_{L^2 -> L^2} + ||1_X C_U 1_X'||_{Eps^* -> Eps} <= C e^{-delta_* dist(X, X')}.

*Warning, 2026-10-31.* Theorem 6 is true as stated, but C_U is not the response of the fibre. On ker Q^o only omega with r omega = 0 is gauge, so the term ||D^* H||^2 in K adds real energy on the part r D^* H. For the response use `library/fibre-propagator.md`, Theorem F, whose gauge term sits on ker r. The right inverse by bumps and the method of proof below are used there unchanged.

*Proof.* Babuska-Brezzi: boundedness of K on Eps by Lemma 3; coercivity on the kernel by Theorem 5; inf-sup for Q^o_U from a bounded right inverse. For the right inverse, at U = 1 take B = sum_c Y(c) psi_c with psi_c a fixed lattice bump of bounded gradient, in component mu, with <rho_c', psi_c> = delta_{c c'}: transversally a bump with integral 1 inside the tile, along mu a biorthogonal function to the integer translates of tri. Since the transverse tiles are disjoint this is a one-dimensional problem. By the finite support of the Gram matrix the Riesz bound is uniform in eta. Then ||B||_Eps^2 <= C ||Y||^2. At U, transport psi_c in the gauge of box(c), which is a relative perturbation O(a) in the map Q^o_U on the span. Neumann series. Analyticity: K and Q^o depend analytically on A', with differences bounded on Eps by C(|A'|_inf + |grad_U A'|_inf), and a bounded analytic perturbation preserves invertibility. Decay (Combes-Thomas): conjugate by e^f, f Lipschitz, with coarse values f(y) on l^2. K_f - K is first order with coefficient at most C delta, so bounded on Eps by C delta. Q^o_f - Q^o is bounded from L^2 by C(L) delta, because each row has support of diameter at most 3. So Sad_f is invertible for delta <= delta_*, with the same norm bound. Take f = delta_* min(dist(., X), dist(X, X')). QED

## Theorem 7 (the Lagrange term, off shell)

Let U satisfy R(a), with M^n(U) = V_n and D_U A = Q^(n)* lambda_n, the multiplier equation of the constrained minimum. Suppose Lambda_n := sup_c |lambda_n(c)| < infinity. Let A_n(W) := min{ A(U') : M^n(U') = W } near V_n, and let Y be a level-n bond field. Then

    | D^2 A_n(Y,Y) - min_{Q^{o,(n)} H = Y} D^2 A(U)[H,H] | <= C(L) Lambda_n ||H_Y||^2,

where the derivative is along t -> e^{itY} V_n and H_Y is the minimiser. No factor of n appears. Also Lambda_n <= C sup|F(U)| in level-n units.

*Proof.* **Step 1 (a contour-free chain).** Fix the base point. At each level j let g^[j](V) be a smooth site-valued function near V_j, with g^[j](V_j) = 1 and first derivative -Phi^[j], for instance g_y(e^{i theta} V_j) = exp(-i Phi_y theta) in the log coordinates at the base point. Put N_j(V) := g^[j](V) . M_j(V), N^(n) := N_{n-1} o ... o N_0. Then D N_j = Q^{o,[j]}, by construction, and N^(n)(U') is a coarse gauge transform of M^n(U'), for U' near U.

**Step 2 (same function).** A_n^o(W) := min{ A(U') : N^(n)(U') = W } equals A_n(W) near V_n. Indeed if N^(n)(U') = W then M^n(U') = G . W for a coarse gauge element G, so A_n(W) = A_n(G . W) <= A(U') by gauge invariance of A_n; hence A_n <= A_n^o. Conversely, given U' with M^n(U') = W, the equation N^(n)(G-tilde . U') = W for a fine gauge transform G-tilde extending a coarse element has a solution near 1, by the implicit function theorem, because the coarse-level map is the identity to first order; and A is invariant. Hence A_n^o <= A_n.

**Step 3 (the formula).** Let H be the minimiser of D^2 A[H,H] under Q^{o,(n)} H = Y, and U'(t) a curve with N^(n)(U'(t)) = e^{itY} V_n. By the chain rule with theta^j := Q^{o,[j-1]} ... Q^{o,[0]} (eta H) and zeta^0 = 0, zeta^{j+1} = Q^{o,[j]} zeta^j + b_j[theta^j, theta^j], with b_j the second jet of N_j at the base point, the second derivative of A(U'(t)) at 0 is D^2 A[H,H] - <lambda_n, zeta^n>, using D_U A = Q^(n)* lambda_n = Q^{o,(n)}* lambda_n. The last equality is the Ward identity: gauge invariance of A gives D_n^* lambda_n = 0, and the contour part Phi enters only through D_n. So <lambda_n, zeta^n> = sum_{j<n} <lambda_{j+1}, b_j[theta^j, theta^j]>, with lambda_{j+1} := Q^{o,[j+1]*} ... Q^{o,[n-1]*} lambda_n. For the quantity in the theorem, minimising over H gives the stated lower bound with H_Y, and H_Y itself gives the upper bound.

**Step 4 (the sizes).** Write s_j = L^{j-n}. By Lemma 1 the composite path kernel has weights adding to at most 1 over c for each line, and each level-(j+1) bond lies on a fraction s_{j+1}^3 of the lines of a unit cross section, so at U = 1, sup |lambda_{j+1}| <= s_{j+1}^3 Lambda_n. With the background, the same recursion as in Lemma 4 multiplies this by prod (1 + C(L) a s_i) <= C: the contour residual has coefficient C(L) a s_i^2 and bounded weights, against L^-3 per level for the path part, so it is a relative C(L) a s_i^2 L^3 <= C(L) a s_i, for a <= a_*. Next, N_j is a smooth map on a block with loops close to 1, so |b_j[theta,theta](c)| <= C(L) sum_{b in the block of c} |theta(b)|^2. Hence

    |<lambda_{j+1}, b_j[theta^j,theta^j]>| <= C(L) Lambda_n s_{j+1}^3 sum_b |theta^j(b)|^2 = C(L) Lambda_n s_{j+1}^3 s_j^-2 N_j(theta^j)^2 <= C(L) Lambda_n s_j N_j(theta^j)^2,

with N_j the norm of Lemma 4. By Lemma 4, N_j(theta^j) <= C ||H||, because theta^j is built with Q^o only. The sum of s_j over j < n is at most 2/L. So no power of n appears.

**Step 5 (Lambda_n).** With psi_c the bump of Theorem 6, transported, Q^o psi_c = delta_c + O(a) with exponential tails; a Neumann series gives Psi_c with Q^o Psi_c = delta_c exactly, ||Psi_c||_Eps <= C. Then lambda_n(c) = <lambda_n, Q^o Psi_c> = <D_U A, eta Psi_c>, and D_U A is the divergence of F, so |lambda_n(c)| <= sum over cells of ||F||_{L^2(cell)} ||grad Psi_c||_{L^2(cell)} <= C sup|F|. QED

This replaces item 4 of the list below, for the full constraint. It explains Text 3.4 of the producer: the order-n size of individual diagrams is carried by the gradient parts of the k-fold average, and these are invisible to a gauge-invariant functional.

## What this does not do

1. It gives no pointwise kernel bound at fine scale, and the fine covariance is singular there. For one-step quantities it suffices: the one-step covariance on level-l bonds is C^(l) = Q^(l) C_{U,l+1} Q^(l)*, bounded with exponential decay as an operator on l^2(level-l bonds), since Q^(l) is bounded from L^2 by a local Jensen estimate.
2. It does not give the walk expansion with free decoupling parameters. A parametrix with Dirichlet cubes of side M and a partition of unity with gradient at most C/M yields an error of size C/M in Eps, which gives walks with a geometric factor. Frozen as a separate leaf.
3. It treats the single-level determining set. Route for a nest: use the Poincaré inequality at the local scale s(x), which gives ||B/s||^2 <= C ||grad_U B||^2 when each point has a constraint tube of its own scale, as the admissibility conditions on nests provide. Holes with free boundary: the same on the region, the tubes staying inside.
4. Existence, uniqueness and pointwise regularity of the minimiser (|F(U_k(V))| <= C flux(V), level-k units) are assumed where used. The bounds on the Lagrange term are now Theorem 7.
