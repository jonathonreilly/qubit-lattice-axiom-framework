State of attack

**Gap — stopped; (15) is not decided.** The stopping input is the conditional normalized-density assertion in (BANACH), step (4), `parts/hard-core--independent.md:1010`. The calculation below uses the actual flat SU(2) chart and linearized saddle, and gives its leading homogeneous one-factor, one-link, one-site term, including normalization. Its small-site coefficient is nonpositive, strictly negative if both response entries are nonzero, and proportional to `g^-4 (D_p T e_c)^2 (D_p T e_s)^2`. It is not a counterexample: the spatial kernels can pay for that power, and the interacting remainder has not been bounded in the required joint limit. No claim of an evaluation of the full coefficient (13a) is made.

**Discharged — scope and procedure.** Read `GOAL.md` and `FINISH-rules.md` first. The user identifies this filtered copy as commit `d0c4b447b`; that provenance is supplied, not independently verified. This is a written mathematical investigation by OpenAI Codex, not an audit. Only this file is being written. No numerical job, machine enumeration, external lookup, git operation, or subagent is used.

**Discharged — actual chart specialization.** Write I for `parts/hard-core--independent.md`. Take a plaquette strictly inside one level-0 block and an old factor depending only on its holonomy. In I:665 the rotation `theta(b)` is a gauge transformation and the second correction changes only crossing links. Thus, after dropping that gauge transformation, the four links of this plaquette are exactly `exp(i b_l) V^#_l`. If the coarse field is flat in the boxes defining these four origins, I:774 gives `V^#_l=1`. Hence on these links the inverse field coordinate is exactly `b_l=v_l`, not a nonlinear scalar dilation. A far site cannot change the near rows of P: I:778. The full interacting density and the normalization still change.

**Discharged — scope of the calculation.** The calculation below uses the level-0 Wilson Hessian and the linearization of the actual block map, with three SU(2) colour components. A leading coefficient at fixed finite geometry alone is insufficient for a uniform estimate: I:770 requires a site distance at least `r_2` cubes, and `r_2` grows with `log(1/g)`.

**Discharged — the quadratic data are fixed by the attempt.** On a finite full torus, write `d` for the scalar lattice gradient, `D` for the oriented plaquette curl, `Q` for the triangular block map of I:458 and I:1081–1082, and `Pi_0` for removal of the mean in each block. Use one colour for these matrices. Put

\[
 B=D^TD+\tau d\Pi_0d^T,\quad
 G=(B+Q^TQ)^{-1},\quad H=QGQ^T,
 \qquad T=GQ^TH^{-1},\qquad C=G-GQ^TH^{-1}QG.                 \tag{A}
\]

Here `tau>0` is the chart's gauge parameter. `T` is the linearized saddle modulo a fine gauge transformation; `C` is the covariance on `ker Q`, extended by zero on its orthogonal complement. These are definitions by finite matrices, not fitted decay parameters. For a plaquette p, put `D_p` for its row in D and

\[
 a=D_pT e_c,\qquad b=D_pT e_s,\qquad v=D_p C D_p^T,\qquad D_0=1+v.       \tag{B}
\]

The coarse links c and s are outside the boxes defining the origin at p; s is contained in the one site whose states will be compared.

**Discharged — verification of (A).** The map Q is onto: one crossing link belonging to a coarse bond appears in no other bond, and its coefficient is nonzero, so these links give a diagonal right inverse. If a field h has `Dh=0`, sums along paths show that it is `d lambda + k`, with k constant in each torus direction: subtract its periods, and interchange adjacent lattice steps using `Dh=0` to make the remaining path integral single valued. Telescoping the gradient along each path in the block average gives `Q d lambda` equal to the coarse gradient of the block averages; also `Q k=L k`. Thus `Qh=0` forces k=0 and the block averages of lambda to be constant. Subtract that constant. If also `Pi_0 d^T h=0`, then
`0=<lambda,Pi_0 d^T d lambda>=||d lambda||^2`. Thus `B+Q^TQ` is positive definite, and H is positive definite because Q is onto. `QT=1`, and directly,
`(B+Q^TQ)T=Q^T H^{-1}`. Its pairing with any vector in `ker Q` vanishes. Consequently T minimizes the quadratic form with specified Q-data. The gauge term can be made zero by adding `d lambda` with zero block averages: solve the positive finite system `Pi_0 d^T d lambda=-Pi_0 d^T h` on that space. This leaves Q and D unchanged. Hence the curvature `DT` is also the curvature of the Wilson minimizer. Finally `QC=0` and `C B h=h` for `h in ker Q`, as follows by multiplying (A), so C is precisely the inverse quadratic form on that space.

**Discharged — SU(2) fixes the colour count and the observable.** Identify a Lie algebra vector with `i x·sigma` and use the quaternion norm of I:139. Explicitly,

\[
 \sigma_1=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
 \sigma_2=\begin{pmatrix}0&-i\\i&0\end{pmatrix},\quad
 \sigma_3=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
\]

Multiplication gives `sigma_a^2=1`, `sigma_1 sigma_2=i sigma_3`, `sigma_2 sigma_3=i sigma_1`, `sigma_3 sigma_1=i sigma_2`, with the opposite sign for reversed products. Hence `(x·sigma)^2=|x|^2 1`, and separating the even and odd terms of the exponential series gives
`exp(i x·sigma)=cos|x|+i (x·sigma) sin|x|/|x|`.
For a small link field A the plaquette logarithm is `D_p A+O(A^2)`, by multiplying the four exponential series. Therefore the Wilson action starts with `||D A||^2/2`, with three identical colour copies of (A). Choose

\[
 e(V)=\varepsilon\left(1-e^{-|V_p-1|^2/(2g^2)}\right),
 \qquad\varepsilon=cc_j\omega_P.                              \tag{C}
\]

It is gauge invariant, bounded by epsilon, and bounded by `epsilon |V_p-1|^2/(2g^2)` since `1-e^{-x}<=x` for `x>=0`. It has no tail coefficients at fixed near links. It is an allowed test factor, not asserted to be an RG-produced activity.

**Discharged — the leading homogeneous density, including its denominator.** Give c the link angle w and s the link angle u, both in colour 3. The site states are u and 0, with all other links flat. Rescale `w=g z`, `u=g t`, and the fine field by g. At degree zero in g, the actual constraint is Q, the actual action is `||D A||^2/2`, and the actual gauge device contributes the second term in B. All Jacobians take their constant value at the flat field. The conditional Gaussian has mean `T(z e_c+t e_s)` and covariance C in each colour. This follows by writing `A=Tq+h`, `Qh=0`: the cross term in the quadratic form vanishes by (A), and the remaining Gaussian on h has inverse C on `ker Q`. The constant Gaussian determinants and constant Jacobians divide out. The exact split at I:703 gives the same C; retaining only `P P^T/2` would give a different answer.

Consequently the leading homogeneous normalized expectation is

\[
 \Gamma^{(0)}(z,t)=\varepsilon\left[1-D_0^{-3/2}
             \exp\left(-\frac{(az+bt)^2}{2D_0}\right)\right].       \tag{D}
\]

To verify the integration, in one colour complete the square in
`-(x-m)^2/(2v)-x^2/2`; the integral divided by the original Gaussian integral is `(1+v)^(-1/2) exp(-m^2/(2(1+v)))`. The three colours give (D), including the exponent `-3/2`. If v=0 the same formula follows by evaluating at x=m. This is the quadratic limit of the specified SU(2) chart, with a, b and v fixed by (A)–(B); they are not the adjustable Gaussian parameters of the preceding report.

**Discharged — its one-link, one-site coefficient and sign.** At this homogeneous order, translating back to w,u gives the following coefficient of w squared in the difference of the two site states:

\[
 \Delta K^{(0)}(u)=\frac{\varepsilon a^2}{2g^2D_0^{5/2}}
 \left[
 e^{-b^2u^2/(2g^2D_0)}
 \left(1-\frac{b^2u^2}{g^2D_0}\right)-1\right].                  \tag{E}
\]

For real u with `ab u != 0` this is strictly negative: writing `x=b^2u^2/(g^2D_0)>0`, one has `e^(-x/2)(1-x)<1`. Its first nonzero term in u is

\[
 \boxed{[u^2]\Delta K^{(0)}
       =-\frac{3\varepsilon}{4g^4D_0^{7/2}}\,
          (D_pTe_c)^2(D_pTe_s)^2.}                              \tag{F}
\]

Indeed the linear term of `e^(-x/2)(1-x)-1` is `-3x/2`. Equivalently the term of degree four in the exponential in (D) has the coefficient `6a^2b^2/8`; the minus sign comes from (C). At this homogeneous full-Gaussian order the normalization subtractions in (13a) are included. A constant old factor gives zero instead. No marginal subtraction is made, since the question here is (15).

**Gap — what has and has not been evaluated by (F).** Formula (F) is the leading homogeneous contribution of the actual SU(2) integrand, not an evaluation of its full interacting coefficient at finite g. To turn it into an asymptotic of (13a), one must control Taylor remainders, the real-coordinate cuts, and the original denominator. On a fixed finite graph their constants can depend on that graph. Such an asymptotic would not justify using it with `dist(S,P)>=r_2(g)`, a growing torus, or arbitrary RG depth. No uniform remainder is established here. In particular I have not proved that the complete coefficient has the sign of (F), or that both displayed response entries are nonzero at a specified pair of distant links. These limitations preclude presenting (F) as an SU(2) counterexample.

**Discharged — exact powers versus a distance estimate.** Define `k_c=L^2 D_pTe_c` and `k_s=L^2 D_pTe_s`. These explicitly defined finite-matrix entries give the exact spatial dependence of this homogeneous term. Formula (F) is exactly

\[
 -\frac{3\varepsilon}{4D_0^{7/2}}\,g^{-4}L^{-8}k_c^2k_s^2.      \tag{G}
\]

Writing `L^-8` this way does not establish an L-uniform bound on k. Nor does specifying only the two distances determine these entries: orientations, block positions, torus size and boundary conditions enter (A). An exact exponential law in distance has not been derived.

**Implication — comparison with the asserted budget, using precisely the existing linear input.** Let `d=dist(p,c)`, `R=dist(p,S)` in coarse units, and suppose the interior curvature-response assertion of I:1398 supplies `|k_c|<=K exp(-delta d)` and `|k_s|<=K exp(-delta R)`. In a collinear placement with `R>=d` and the site reached at s, the tree from the output anchor has length at most R. Write `d_R(c)` for distance to the output rough set. The uncapped radius then makes the weighted term `u^2` times (G) at most

\[
 \frac{3\varepsilon K^4c'^2}{4}\,
 u^2 g^{-2}L^{-8}
 e^{\,2c_1d_R(c)-2\delta d-(2\delta-c_3)R}.                   \tag{H}
\]

If c is scaled by zeta and the site state u is not, multiply this expression by `|zeta|^2`; if both are scaled, by `|zeta|^4`. A capped radius only decreases it. The site threshold is essential: with `R>=A log(1/g)` and `(2 delta-c_3)A>2`, its site-distance factor beats the displayed `g^-2`. Thus even this negative term, which is linear in the old activity, does not by itself exceed (15). Equation (H) is conditional on the stated response estimate and controls only the displayed homogeneous term.

**Discharged — conditioning in this actual chart changes the spectator law already at quadratic order.** This identifies what the remaining density argument has to handle, without choosing a replacement model. Restrict the near field to the four interior links, in one colour, and set

\[
 M=2^{-1/2}P_{Y,d},\qquad U=(G_{1,Y},G_{2,Y}),\qquad
 \Sigma_0=MM^T,\quad\Sigma=\Sigma_0+UU^T.
\]

These are the operators of I:703–709 at the flat saddle. The restriction of `ker Q` to these interior links is onto: extend any prescribed values by zero on other interior links, then cancel their Q-data with the private crossing links outside Y. Since `PR=1` on `ker Q`, M is onto as well and `Sigma_0` is positive definite. At the leading homogeneous order, with `z=v_Y/g`, the coordinate equation is `z=M n+U eta`, where n is the local white noise and eta the spectator. Orthogonally split n into its component in `ker M` and
`M^T Sigma_0^(-1)(z-U eta)`. The squared norm of the latter is `(z-U eta)^T Sigma_0^(-1)(z-U eta)`. Thus the conditional density of eta, after integrating the kernel component, is proportional to

\[
 \exp\left[-\tfrac12\eta^T\eta
 -\tfrac12(z-U\eta)^T\Sigma_0^{-1}(z-U\eta)\right].             \tag{I}
\]

Completing this square gives its covariance and mean:

\[
 C_{\eta\mid z}=I-U^T\Sigma^{-1}U,
 \qquad m_{\eta\mid z}=U^T\Sigma^{-1}z.                       \tag{J}
\]

For direct verification, multiply the proposed covariance by `I+U^T Sigma_0^(-1)U`; the identity
`Sigma_0^(-1)-Sigma^(-1)=Sigma_0^(-1)UU^T Sigma^(-1)` cancels the extra terms. Multiplying the proposed mean by the same precision gives `U^T Sigma_0^(-1)z`. This proves (J). The full three-colour formula has three copies. The spectator is not absent: the G1 part of I:703 has positive covariance on X when `||Delta||<1`, so its restriction detects the nonzero plaquette-curl direction in X. Thus (J) differs from the original standard spectator law. Its quadratic factor contains cross-cube terms wherever the indicated kernel entries are nonzero. It is not legitimate simply to replace it by the original product measure. This observation does not say that suitable conditional estimates are impossible.

**Gap — the named stopping input is (BANACH), step (4), I:1010, in the proof of Lemma 4.7c (MOM).** The exact sentence needed there is:

> “There is no quotient: the ratio to N_good^Z is the exponential of the polymers that meet d, by the library at fixed (v, xi_d^perp), of norm 1 + small.”

The library actually invoked is `library/ultralocal_cluster_expansion.md`: line 9 assumes a product probability measure; line 11 assumes a local activity bound on its support; line 42 uses independence to factor integrals on disjoint supports. Its Banach version at line 76 keeps those hypotheses. The calculation (I)–(J) shows explicitly the conditional Gaussian arising from this attempt's own inverse coordinate. Keeping the old product noise instead is possible, but then `exp(-(z-U eta)^T Sigma_0^(-1)(z-U eta)/2)` from (I) is an additional insertion with spectator tails, and its joint field/site norm must be estimated. The original Gaussian of eta is included only once. Whitening (J) is another possible route, but then the transformed interactions, cuts, and their locality bounds must be supplied. Neither operation is carried out in the cited step. The unconditional good-sector expansion at I:640–654 does not establish these conditional hypotheses.

**Gap — why this input decides whether the calculation can be used for (15).** The missing step is used to control precisely the interacting terms `Psi_1,Psi_2`, the inverse-coordinate Jacobian, and the inverse normalization in (11) and (13a). It must do so after their connected subtractions, on the entire `|zeta|<=c/t_#` disc, including a site at a distance growing with `log(1/g)`. A finite-geometry expansion of the integrand, even one with the explicit negative coefficient (F), supplies no bound for that normalized remainder. An error that is small for fixed links can dominate (F) when its response kernels tend to zero as the site recedes. Likewise the cut ratio theta in (13a) cannot be replaced by one using an unproved uniform cut-error claim. I stop at this existing conditional-normalization assertion; I have neither proved it nor shown that its desired conclusion is false.

**Unchecked — requested full result not obtained.** No actual coefficient exceeding the contraction has been established. No general bound uniform in region, depth and radius has been established. In particular, (G) is not a proved distance asymptotic or a complete leading-term evaluation of (13a) in the admissible joint limit. No change of norm, base, or centre is being offered as a demonstrated repair.

**Discharged — record of work.** Read `GOAL.md`, `FINISH-rules.md`, and `library/mixed-coefficient.md` in full; the located chart, saddle, smoothing, site, and linear-lift passages of I; (35)–(43) and neighbouring passages of `library/tail-two-step.md`; and the hypotheses and proof of the cluster library cited above. Text searches exposed additional passages in I. No gates, other proof account, outside-directory file, git history, numerical job, or subagent was used. The displayed arithmetic and Gaussian integrations are written derivations, not computed evidence. Only this report was edited.

**Gap — verdict: (15) is not decided. The stop is the conditional normalized-density assertion in (BANACH), step (4), `parts/hard-core--independent.md:1010`. The actual flat SU(2) quadratic data yield the nonpositive coefficient (F), with explicit `g^-4` dependence, but its promotion to the complete coefficient (13a), with uniform spatial control, remains unproved.**
