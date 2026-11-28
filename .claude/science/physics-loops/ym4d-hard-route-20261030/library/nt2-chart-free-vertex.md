# NT2: the vertex clause without a chart, and what positivity reads

Author: anthropic/claude-opus-5-5/max mac-mini-worker, 2026-11-01, queue item 8f.
Source: `be5e58b30`. Neutral: uses no proof of either hard-core attempt.
Status: Proposition V0, Lemma R4 and Lemma RM' are discharged at the stated scope. The clause (NT2-V) is a proposed requirement: it holds at the lattice scale by Theorem 3.17, which is the part's own same-model result, and it is a gap at a blocked scale. Author work, not a review or an audit. No status.
Credit: the gate `gates/nt2-gate-2285befef.md` D2 for the repair and its Lemma K; `library/nt2-coherence-and-positive-norm.md` for Lemma RM, which RM' extends. The Stieltjes form is Kallen-Lehmann.

## 1. No gauge-invariant observable reads the vertex alone

Work on a finite lattice with no double bonds. U_b = exp(i A_b . sigma / 2). Let f be a smooth gauge-invariant function of the links, with Taylor expansion at A = 0 beginning at order three: f = t_3 + t_4 + O(|A|^5). Every finite linear combination of the T of Text 0 is such an f, at any base points.

**Proposition V0 [discharged].** If t_4 = 0 identically, then t_3 = 0 identically.

Proof. For a gauge function h(x) = exp(i theta(x) . sigma / 2), BCH with exp(i X . sigma / 2) exp(i Y . sigma / 2) = exp(i (X + Y - (1/2) X x Y + ...) . sigma / 2) gives, at first order in theta, on b = (x, y),

    delta A_b = (theta_x - theta_y) - thetabar_b x A_b + O(theta A^2),    thetabar_b = (theta_x + theta_y) / 2.

Invariance of f, graded by degree in A, gives at degree three

    D t_4(A)[d theta] = D t_3(A)[thetabar x A]          for all theta, A.

With t_4 = 0 the right side vanishes. Colour covariance and homogeneity give t_3(A) = sum_(b,c,d) C_bcd A_b . (A_c x A_d), with C totally antisymmetric. Then D t_3(A)[thetabar x A] = 3 sum C_bcd (thetabar_b x A_b) . (A_c x A_d) = 6 sum C_bcd (thetabar_b . A_c)(A_b . A_d), using antisymmetry in c, d. Take theta supported at one site x with value e. Fix distinct bonds b_0, c_0, d_0 and read the coefficient of the monomial (e . A_(c_0)) (A_(b_0) . A_(d_0)) with the colour of the second pair orthogonal to e. It comes only from (b, c, d) = (b_0, c_0, d_0) and (d_0, c_0, b_0), and it is a non-zero multiple of C_(b_0 c_0 d_0) [1(b_0 touches x) - 1(d_0 touches x)]. So if C_bcd != 0, then at every site b and d touch together, and by antisymmetry so do c and d. All three bonds then have the same two endpoints, which on a lattice with no double bonds means they coincide, and then C_bcd = 0. []

Check, W1 (`checks/witness/v0_jets.py`): family with 3010 triples built to contain relations, d = 3 and d = 4: rank of the t_3 map 20, of the t_4 map 125, null space of t_4 of dimension 2885, and t_3 on it below 3e-15 of its top singular value. The jets agree with the exact SU(2) products to 4e-6 relative, not the 1e-6 of the criterion: the limit is the five-point fit, and the check was not tightened further.

**Reading.** K_T(f) = E_0 t_4 - E_0[t_3 F_3]. If K_T(f) != 0 then t_3 != 0 or t_4 != 0, and by V0 t_4 != 0 in either case. So no observable, and no finite linear combination of them, has a Wilson tree value made of the vertex alone. Take a covariance C = u u^T of rank one on links tensor colour, not colour-isotropic: then E_C t_4 = 3 t_4(u), so some Gaussian potential has E_C t_4 != 0 on that observable. (A colour-isotropic rank-one c gives 0, since the links are then aligned in colour.) With Lemma K of the gate, which sets K_vert(tau) to any real value for one tau on a family of linear slices, this settles the form of the clause: a chart-free statement of the vertex cannot be one inequality on one linear functional of K_T. It has to quantify over c.

## 2. The clause

Let P(Gamma, Delta) be the tree flux covariance of (NT2-C) and K_T the tree value of T. For a real symmetric kernel c on the coarse links of a window, tensor 1_3, put, with E_i := c J_i and the formulas of Proposition 2.1 and Lemma 3.1,

    P[c](Gamma, Delta) := <J_Gamma, c J_Delta>,
    K_comp[c](tau) := -12 [ A_1(E_2, E_3) + A_2(E_3, E_1) + A_3(E_1, E_2) ],

the order-h^2 and order-h^4 values of the Gaussian potential of covariance 4 h^2 c. Neither mentions a chart: A_b is the exponential coordinate of the link, and a colour-covariant change of that coordinate on one link starts at cubic order, since A x A = 0.

**(NT2-V) [proposed requirement, fixed before the law].** There are a finite set F of templates and kappa_* > 0 such that for every real symmetric c,

    max{ max_(Gamma, Delta in F) |P[c](Gamma, Delta) - P(Gamma, Delta)|,
         max_(tau in F^3) |K_comp[c](tau) - K_T(tau)| } >= kappa_*.

**Correction to the gate's wording.** The gate's repair and `nt2-coherence-and-positive-norm.md` section 4 quote Theorem 3.16 as saying that no c has K_comp[c] = K_T on every triple. Theorem 3.16 says no c has **both** the P_pq and the K_total, and Theorem 3.17 has a pair defect or a triple defect. The pair clause cannot be dropped from what is proved. It costs nothing in NT2: (NT2-M) matches B, so the pair data of any candidate are already fixed.

**Reading in a chart.** If c is the covariance of a linear colour-diagonal slice of F_2, the pair defects vanish and K_T - K_comp[c] = K_vert(tau; slice). So (NT2-V) gives, for every such slice, a template with |K_vert(tau; slice)| >= kappa_*. The template depends on the slice. That is the content of "the vertex is present", and it is all a chart-free statement can say. The table of the gate, K_vert from 0 to 0.26 at fixed K_T, is the same fact for one triple.

**Status.** At n = 1, the lattice scale: Theorem 3.17 gives (NT2-V) with F the plaquette lassos of its box, side about 150 in the leading count, and kappa_* = eps_0 [derived there, same-model]. Numerics in Text 3.13 suggest one hypercube suffices (relative residual 0.19). At a blocked scale it is a gap, and two things are missing: the blocked K_T, which reads the second jet of M, and a level-j form of 3.16 or 3.17. Theorem 3.19 is withdrawn. For translation-invariant c, Theorem 3.10 is the implication in hand, so a clause restricted to that class is reachable first.

**Consequence for (REG-T).** The gate's D2 stands: (REG-T) can hold for K_T and the Gaussian coefficients, and it cannot hold for the split between a tree chart and periodic Feynman. (NV) of `witness-blocked-tree-limit.md` is a statement in the Feynman prescription, so it is evidence in that chart and no longer a clause.

## 3. What reflection positivity reads

**Lemma R4 (singlets read the reflected kernel) [discharged].** Let A be a centred Gaussian potential on a finite lattice with independent colours and covariance h^2 C, with C invariant under a reflection Theta. Let Gamma_1, ..., Gamma_N be closed paths with one base point in the open half-space, P_kl := <J_k, C J_l>, R_kl := <Theta J_k, C J_l>, a symmetric matrix. For c real symmetric put F := sum c_kl B(Gamma_k, Gamma_l), a gauge-invariant function of the half-space links. As h -> 0 at fixed lattice,

    E[Theta F . F] = (h^4 / 16) [ 9 (Tr c P)^2 + 6 Tr(c R c R) ] + O(h^6).

If R has a negative eigenvalue and at least two positive ones, some c has Tr c P = 0 and Tr(c R c R) < 0, so E[Theta F . F] < 0 for small h: RP fails on gauge-invariant functions.

Proof. v_Gamma = (h / 2) Phi_Gamma + O(h^2), so B = (h^2 / 4) Phi_k . Phi_l + h^3 (cubic) + O(h^4). The order h^5 term of the product is odd in a Gaussian, so it vanishes. Wick with independent colours: E[(x . y)(z . w)] = 9 C_xy C_zw + 3 C_xz C_yw + 3 C_xw C_yz. With P_(Theta k, Theta l) = P_kl this gives the display. Take eigenvectors u_- and u_+, u_+' of R, and c = u_- (a u_+ + b u_+')^T + transpose, with a, b not both zero and Tr c P = 0. Then Tr(c R c R) = 2 r_- (a^2 r_+ + b^2 r_+') < 0. []

So the gate's remark that the argument does not reach RP on gauge-invariant functions is too cautious for a Gaussian potential of fixed profile: a fixed indefinite R is rejected on singlets as the amplitude goes to zero. W4 (`checks/witness/singlet_rp.py`): pairings 9, 3, 3 exact; a toy with R = diag(rho, -rho) gives E[Theta F F] negative at 1200 standard errors, with ratio to the leading term 0.74, 0.87 at h = 0.6, 0.4, tending to 1.

**Limit of this test.** For a law that matches (NT2-M) on a fixed template family, R = g_m^2 (R^tree + o(1)), with R^tree positive semidefinite. A negative direction of a running kernel is then of relative order g_m^2, so the leading term of the singlet test on such a direction is of order g_m^6. That is the order of the next terms of F, in particular the quadratic map of L3, which adds a positive piece to the flux kernel. So this test does not decide RP for mu^TD or L3 at the running profile. No claim either way.

**The abelian top-down law [computed, W5, `checks/witness/abelian_td.py`].** On a 9 x 9 x 18 torus with blocks of side 3, the law with amplitude gamma_c on the coarse closed currents and gamma_f on the P-orthogonal rest has flux kernel gamma_f^2 P + (gamma_c^2 - gamma_f^2) delta. At gamma_c = gamma_f the reflected kernel on half-space plaquettes has smallest eigenvalue -4e-16 relative. At gamma_c^2 / gamma_f^2 = 1.01, 1.1, 2 it is -6.2e-7, -6.2e-6, -7.4e-5 relative, with 4 negative directions. At ratio 0.9 it is -0.05, with 36. So every tested non-constant amplitude breaks RP of the abelian law, in both directions, and the negative value is linear in the amplitude change. This is the abelian analogue, where flux is a gauge-invariant function. It does not decide RP for SU(2).

**Lemma RM' (no O(4) needed for a scalar multiplier) [discharged].** Let a be a Gaussian vector field on R^4, with independent colours, whose covariance on conserved currents is a scalar multiplier D(k) >= 0, symmetric under signed permutations of the k_i and bounded in each k_i at fixed other components. Assume RP on closed currents in each axis. Then rho(k) := |k|^2 D(k) is non-decreasing in each k_i^2, so r -> Var <j_r, a> is non-increasing, with j_r as in Lemma RM.

Proof. Fix axis 4, p the other three components, z = k_4^2. RP on purely spatial transverse currents makes the reflected kernel completely monotone in t, so D(z; p) = c_0 + int dnu_p(s) / (z + s), with nu_p >= 0 and c_0 >= 0 since D >= 0 at large z. A closed current in the half-space is J_t = -div g, J_s = d_t g, with g compactly supported in t > 0. The sign of Theta on the time component gives, with ghat(w) := int exp(-w t) g dt and w^2 = s,

    <Theta J, C J> = int dp int dnu_p(s) (1 / (2 w)) [ s |ghat(w)|^2 - |p . ghat(w)|^2 ].

Laplace transforms are dense enough to localize in s, so with ghat parallel to p, (s - |p|^2) dnu_p >= 0: the support of nu_p lies in [|p|^2, infinity). Now |k|^2 D = (z + |p|^2) D, and each (z + |p|^2) / (z + s) with s >= |p|^2 is non-decreasing in z, as is the term c_0 (z + |p|^2). Repeat on each axis. Dilation k -> lambda k, lambda >= 1, raises each k_i^2 in turn, so rho(lambda k) >= rho(k), and Var <j_r, a> = int dm(q) rho(q / r) as in Lemma RM. []

So the scope of Lemma RM, stated in the gate as O(4), can be replaced by hypercubic invariance for scalar multipliers. The earlier note there, that RP in each axis gives only monotonicity of k_i^2 D, missed the spectral condition supp nu_p in [|p|^2, infinity), which closed currents force. Not covered: tensor multipliers on the transverse space, which hypercubic invariance allows. For a one-link local map of a scalar Gaussian the link covariance stays diagonal in direction, and Schur powers keep the spectral condition, so RM' applies at blocked scales up to the errors of Corollary RM.
