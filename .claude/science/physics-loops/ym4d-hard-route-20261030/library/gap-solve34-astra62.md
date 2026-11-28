# Repo search

**PROVED (checkout observation).** The row-specific prior file `library/prior/gap-solve34-astra62.md` was absent when this note was opened.

**GUIDE.** Row 1298, at `d9936f469`. The lead's November 8 search located soft-route estimates and duplicate hard-route snapshots. I checked the closest primary passages. On PR 10114, `MASS_GAP_LOCAL_BLOCK_ASTRA.md` (4–14, 106–149) gives a finite-coupling plaquette witness and a contraction estimate within its stated coupling range. Grok's PR 10133, `MASS_GAP_CROSSOVER_REDUCTION.md` (77–86), leaves crossover and source transport open. PR 10134, `library/mass-gap-interface.md` (I1–I5), distinguishes a nonempty excited space, its lower edge, and Yang–Mills identification. PR 10141, `research/ym4d/library/fp1.md` (299–315), controls a constrained classical field. On main `8b11ae2bb9`, Theorem ZD-c in `research/mass-gap/library/gap-phys-seed.md` (311–323) requires a physical finite-volume energy estimate and state counting. I found no assignment of the physical mass gap in `library/open-registry.md`. [Lead's search](prior/repo-search-2026-11-08.md)

**GUIDE.** Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, distinguish the scalar cyclic space from the full observable algebra. They exhibit polynomial decay with spectral support reaching zero. The source ranges are indexed in chunks 01 and 29 and in `obligations.md`. The complete account explicitly leaves the mass gap open. [Outline 581–599](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L581-L599) · [Outline 31858–31882](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L31858-L31882) · [Account I 2704–2712](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L2704-L2712)

**GUIDE.** Row 1218 credits Deep Bhattacharjee, Ushashi Bhattacharya, James Montgomery Lockwood, Tristan Romanov, Ikailo John Sessford and Sanjeevan Singha Roy with a conditional propagation theorem for a full thermal trace on a window of shapes. It also describes cube-relaxation criteria and Zeng Chunping's conditional tunnelling proposal. I use the reading to locate the missing weak-coupling input. Row 1290 leaves a signed difference of cut free energies at physical scale and a Poincaré bound on its two-slice midpoint law open. Its results are author-side. [Published-work reading](prior/gap-onebound-read-sol.md) · [Row 1290](gap-solve33-astra62.md)

## Physical question

**OPEN.** Construct a nontrivial quantum Yang–Mills theory with gauge group SU(2) on four-dimensional spacetime with the Jaffe–Witten properties. In its vacuum representation show that the vacuum is unique and that the spectrum of its Hamiltonian on the orthogonal complement of the vacuum is contained in $[m,\infty)$ for one $m>0$.

**PROVED (finite-lattice result).** On an even spatial cube the stationary Wilson measure admits a simultaneous redraw of a positive fraction of the links in one checkerboard colour. For a unit state with frequencies at most \(E\), the mean square change of its reading is at most \(2\tanh(aE)\), where \(a\) is the lattice spacing. The redraw and its probability estimate are given in (29)–(31). The missing physical-scale lower bound is stated in (37).

**GUIDE (choice of attack).** A physical gap would rule out normalized, centered vectors whose energy tends to zero. I work on the corresponding obstruction on the actual time-zero Wilson slice. Row 1236, (11), bounds its relative gradient separately at each link. Summing that bound costs the volume. Row 1290, (3), has a dimension-independent sum on a different variable, the midpoint before Gaussian observation. Row 944, Lemmas TG and EF, identifies the score of the one-step kernel with a conditional electric force. Its supremum over all fixed boundary fields requires a susceptibility estimate. I will keep the middle slice distributed according to the vacuum and expose both of its temporal neighbours. Its conditional action then has only the original Wilson plaquettes, whose second derivatives can be bounded directly. [One-link bound](gap-solve27-astra62.md) · [Midpoint bound](gap-solve33-astra62.md) · [One-step score](gap-sgstep-opus.md)

## A divergence estimate in the physical vacuum measure

**GUIDE (finite-cutoff setting).** Write \(M=(S^3)^m\) for the spatial links on a periodic \(n^3\) cube, \(n\ge3,\ m=3n^3\), with product probability Haar and the unit round metric on each copy of \(\mathrm{SU}(2)\). Write \(w(q)=\tfrac12\operatorname{tr}q\), \(S(x)=-\beta\sum_{p\ {\rm spatial}}w(x_p)\), and \(k(x,y)=\exp(\beta\sum_e x_e\cdot y_e)\), with \(\beta>0\). On the full link space take the integral operator with kernel \(T(x,y)=e^{-S(x)/2}k(x,y)e^{-S(y)/2}\). The Osterwalder–Seiler and Lüscher physical transfer is its restriction to vertex-invariant functions. Using temporal gauge before this restriction keeps the three-slice law particularly simple. The continuous, strictly positive kernel on a compact space has a simple top eigenvalue \(\lambda\) and a smooth positive unit eigenfunction \(\psi\). For example, compact self-adjointness gives a top Rayleigh maximizer, taking its absolute value gives a positive one, and strict kernel positivity precludes a second orthogonal maximizer. Positivity as an operator follows by expanding the exponential of the Euclidean scalar product in tensor powers. Simultaneous gauge transformations and centre flips preserve the top eigenfunction. Put \(\nu(dx)=\psi(x)^2dx\) and \(P(x,dy)=T(x,y)\psi(y)dy/(\lambda\psi(x))\). Thus \(P\) is reversible and positive on \(L^2(\nu)\).

**PROVED.** Let \(U,X,Y\) be three successive slices of the stationary \(P\)-chain. Given \(X\), its neighbours \(U,Y\) are independent with the same law \(P(X,\cdot)\). Given \(U,Y\), the middle slice has density proportional to \(e^{-S_{U,Y}(x)}\), where
\[
 S_{u,y}(x)=S(x)-\beta\sum_e x_e\cdot(u_e+y_e).
\]
Both statements follow by multiplying the two transition densities against \(\nu\). For every tangent vector \(v\), \(|\nabla^2 S_{u,y}(v,v)|\le18\beta |v|^2\), uniformly in both ends and the spatial volume. Along a product geodesic the absolute second derivative of one plaquette trace is at most \((\sum_{e\in p}|v_e|)^2\le4\sum_{e\in p}|v_e|^2\), by differentiating its four quaternion factors including inverses. Each spatial link occurs four times in this sum over plaquettes. Each of the two linear temporal terms contributes at most \(\beta |v_e|^2\).

**PROVED.** For a smooth real vector field \(V\) on the middle slice write \(\delta_\nu V=-\operatorname{div}V-V\log(\psi^2)\) for the adjoint of the gradient. Write \(s_V(X,Y)=V_x\log P(x,y)|_{x=X}\), using the density of \(P\) against Haar. Differentiating its unit integral gives \(\mathbb E[s_V(X,Y)\mid X]=0\). If \(\delta_{u,y}\) is the divergence adjoint for the middle slice with the two neighbours fixed, then
\[
 \delta_{U,Y}V(X)=\delta_\nu V(X)-s_V(X,U)-s_V(X,Y).
\]
Taking the square and using conditional independence gives
\[
 \|\delta_\nu V\|_\nu^2+2\,\mathbb E |s_V(X,Y)|^2
 =\mathbb E|\delta_{U,Y}V(X)|^2
 \le \|\nabla V\|_\nu^2+(2+18\beta)\|V\|_\nu^2.                 \tag{1}
\]
The derivative norm on the right is Hilbert–Schmidt. To see the inequality, integrate twice on the closed product manifold with density \(e^{-A}/Z\). In an orthonormal frame, \(\delta_A V=-\nabla_i V^i+A_iV^i\). In \(\int V^j\nabla_j(\delta_A V)\), commute \(\nabla_j\) past the divergence and integrate the resulting \(-V^j\nabla_i\nabla_j V^i\) in \(i\). The derivative of the density cancels \(V^j A_i\nabla_j V^i\), leaving
\[
 \int |\delta_A V|^2
 =\int \big\{(\nabla_i V^j)(\nabla_j V^i)
            +(\operatorname{Ric}+\nabla^2 A)(V,V)\big\}.
                                                               \tag{2}
\]
Here all integrals use that density. The first contraction is at most \(|\nabla V|^2\). The Ricci tensor of the product of unit three-spheres is \(2g\). Apply (2) with \(A=S_{U,Y}\) and average. The upper Hessian estimate needed here is for the explicit conditional Wilson action.

**PROVED.** If \(f\) belongs to the spectral band \([r,1]\) of \(P\), \(0<r\le1\), then
\[
 2|\langle f,\delta_\nu V\rangle_\nu|^2
 \le (r^{-2}-1)\|f\|_\nu^2
 \big(\|\nabla V\|_\nu^2+(2+18\beta)\|V\|_\nu^2-\|\delta_\nu V\|_\nu^2\big).
                                                               \tag{3}
\]
Indeed \(f=Ph\) with \(\|h\|^2-\|Ph\|^2\le(r^{-2}-1)\|f\|^2\) by spectral calculus. Differentiation gives \(\langle Ph,\delta_\nu V\rangle=\mathbb E[(h(Y)-Ph(X))s_V(X,Y)]\) for real functions. Conditional variance gives exactly \(\|h\|^2-\|Ph\|^2\) for the first squared norm. Cauchy–Schwarz and (1) finish the proof. Real and imaginary parts give the same dual norm estimate on complexification. At fixed cutoff one may first use bounded tests and then \(L^2\) limits, since \(P\) is smooth on a compact space with positive stationary density.

**OPEN.** Inequality (3) tests physical slow states against divergences. Inferring that every centered slow state vanishes would require sufficiently inexpensive vector fields whose divergences detect it. A Poincaré estimate for an auxiliary midpoint distribution does not supply these vector fields on the time-zero vacuum.


## Rotations chosen from already observed links

**PROVED.** Order the \(m\) spatial links arbitrarily and write \(\mathcal F_i=\sigma(X_1,\ldots,X_i)\). Let \(a_i\in\mathbb R^3=\operatorname{Im}\mathbb H\) depend on \(\mathcal F_{i-1}\), and put \(V_i(x)=a_i(x_{<i})x_i\). For every real \(t\) the triangular map
\[
 B_t(x)_i=\exp(t a_i(x_{<i}))x_i
\]
preserves product Haar. One recovers the inputs in order, and at each coordinate the change conditional on the earlier inputs is left multiplication. In particular the assertion applies to bounded measurable choices. With \(b^2(x)=\sum_i|a_i|^2\), each fixed-input curve is a product geodesic of speed \(b(x)\). For \(D=V S_{U,Y}(X)\), changing variables with \(B_{-t}\) in the conditional Wilson integral and applying the second derivative bound gives
\[
 \mathbb E\!\left[\exp\{tD-9\beta t^2 b^2(X)\}\mid U,Y\right]\le1.       \tag{4}
\]
In fact the exponential with exponent \(S_{U,Y}(X)-S_{U,Y}(B_{-t}X)\) has conditional mean one and dominates the displayed integrand. Expanding at zero on the finite cube gives \(\mathbb E[D\mid U,Y]=0\) and \(\mathbb E D^2\le18\beta\,\mathbb E b^2\). This argument takes no derivative of a coefficient in an earlier link.

**PROVED.** For smooth coefficients the Haar divergence of \(V\) vanishes, so \(D=\delta_{U,Y}V\). The two conditional projections of \(D\) onto \(X\) and onto \((X,Y)\) differ by \(s_V(X,Y)\), in that order. Conditional Jensen applied to (4), first averaged in the two neighbours, gives the same unconditional exponential bound for each projection, since \(b\) is determined by \(X\). Cauchy–Schwarz with parameters \(2t,-2t\) gives
\[
     \mathbb E e^{\,t s_V(X,Y)-36\beta t^2 b^2(X)}\le1 .
                                                               \tag{5}
\]
The exact variance splitting in (1) gives the sharper second-moment estimate \(2\mathbb E |s_V|^2+\|\delta_\nu V\|^2\le18\beta\,\mathbb E b^2\). This is an estimate in the joint vacuum law for a direction allowed to depend on the link prefix. Row 944's pointwise sub-Gaussian question keeps the entire initial slice fixed.

**PROVED.** Denote by \(D_i f\) the three components of the derivative in the directions \(a x_i\). Every \(f\) in the \([r,1]\) band satisfies
\[
 \boxed{\quad
 \sum_{i=1}^m\mathbb E_\nu\big|\mathbb E_\nu[D_i f\mid\mathcal F_{i-1}]\big|^2
       \le 9\beta(r^{-2}-1)\|f\|_\nu^2 .\quad}                          \tag{6}
\]
Indeed pair the derivatives with the predictable coefficients and apply the proof of (3) using the sharper variance estimate from (4). Take the supremum over coefficients with \(\mathbb E b^2\le1\). Smooth prefix functions are dense in their marginal \(L^2\) spaces, by positivity of the smooth finite-dimensional density and approximation on a compact manifold. Thus the supremum gives the norm on the left. Complexification follows separately for the two real components. In particular, placing any chosen set of links last and using only functions of the complement tests all their conditional mean gradients at once. For a normalized band of physical energies at most \(E\), put \(r=e^{-aE}\). The full sum is bounded by \(9\beta(e^{2aE}-1)\) on every spatial cube.

**PROVED (what these derivatives miss).** Even at \(\beta=0\), independent Haar, a product of nonconstant zero-mean real class functions, one on each of two links, has all the means on the left of (6) equal to zero in either order. Integrating out the later function gives zero in the first derivative. Haar invariance makes the mean of the derivative of the later function zero as well. This example illustrates a property of the observation of derivatives. It makes no claim about a slow state of Wilson theory. Allowing the coefficient of \(V_i\) to depend on \(x_i\) tests such variations, at a cost only in derivatives on that same link, as follows.

**PROVED.** Suppose more generally that the tangent component \(V_i\) is a smooth function of \(x_{\le i}\). In (2) every mixed trace term for \(i\ne j\) vanishes, since one of \(\nabla_i V_j,\nabla_j V_i\) is zero on the product. Thus (1) and (3) hold with the full derivative cost \(\|\nabla V\|^2\) replaced by \(\sum_i\mathbb E_\nu|\nabla_i V_i|^2\). Derivatives of the feedback with respect to earlier links may be arbitrarily large. In particular this bounds a sum of squared weak derivatives on the actual vacuum in a larger family of directions. A general vector field need not be triangular in any link order.


## What a set of missing spatial links can transmit through the middle slice

**GUIDE.** Row 1167, (11), already bounds the variance lost by hiding \(k\) links by \(\cosh^2(k\beta)\langle f,(1-P^2)f\rangle\). The proof uses the four-point ratio of a *single* temporal step. Row 1169, (15)–(18), permits logarithmically many omissions in a thermal test with an additional shorter-period input. Its reconstruction uses a reweighted line in each fibre of the observation. Here the question is about ordinary conditional expectation in the true vacuum, uniformly on individual states as well as their superpositions. I integrate the missing middle links before bounding the channel between its two neighbours. [Row 1167](gap-solve12-astra62.md) · [Row 1169](gap-solve13-astra62.md)

**PROVED.** Fix a deterministic set \(I\) of \(k\) spatial links, no two belonging to the same spatial plaquette. Write \(Z=X_{I^c}\), \(Qf=\mathbb E_\nu[f(X)\mid Z]\). For \(e\in I\), let \(h_e(z)\) be the **dimensionless** sum of the four unit staples, oriented so that the spatial Wilson exponent involving \(x_e\) is \(\beta h_e(z)\cdot x_e\). Set \(H_e=|h_e|\le4\). Given \(Z=z\), integrating the missing middle links in the three-slice density gives the joint law of \(U,Y\) in the form
\[
 b_z(u)b_z(y)K_z(u,y)\,du\,dy/\mathcal N_z,\qquad
 K_z(u,y)=\prod_{e\in I}\Phi\big(\beta[h_e(z)+u_e+y_e]\big),\qquad
 \Phi(w)=\int_{S^3}e^{w\cdot q}\,dq.                                  \tag{7}
\]
In fact \(b_z(u)=\psi(u)e^{-S(u)/2}\exp(\beta\sum_{e\notin I} z_e\cdot u_e)\) up to a factor depending only on \(z\). No assumption of independence among the \(u_e\) is needed. All endpoints in (7) are in the common temporal gauge of the three-slice law.

**PROVED.** For \(H\in[\sqrt2,4]\), the four-point log diameter of the single factor in (7), i.e. the supremum of \(\log(K(u,y)K(u',y')/[K(u,y')K(u',y)])\), is
\[
                         4\beta/H+O(\log(2+\beta)),                     \tag{8}
\]
uniformly in \(H\). For \(w\) real,
\[
 |w|-C-\tfrac32\log(1+|w|)\le\log\Phi(w)\le |w|.
\]
The lower estimate integrates over an angular cap of radius \((1+|w|)^{-1/2}\) about a maximizer. Its Haar mass is at least \(c(1+|w|)^{-3/2}\), by the \(\sin^2\theta\) volume element, and the exponent drops by at most one. Thus it suffices to compute the diameter with \(\log\Phi(\beta w)\) replaced by \(\beta |w|\). For \(h=Ht\), \(|t|=1\), the support-plane and tangent-quadratic inequalities are
\[
 H+t\cdot v\le |h+v|\le H+t\cdot v+|v|^2/(2H).
\]
The second follows by applying \(\sqrt{1+s}\le1+s/2\) to the squared norm divided by \(H^2\). Apply the upper estimate to the numerator terms and the lower one to the denominator terms. The linear parts cancel and \(|u+y|,|u'+y'|\le2\). This gives \(4/H\). Take \(u=y=-t/H+\sqrt{1-H^{-2}}\,v\) and \(u'=y'=-t/H-\sqrt{1-H^{-2}}\,v\) with \(v\) unit and perpendicular to \(t\). The two upper estimates are equalities since \(|h+2u|=|h+2u'|=H\). The lower estimates are equalities since \(H-2/H\ge0\). The four-point diameter of (7) is the sum of the individual diameters because the endpoint link variables can be chosen independently for this supremum. In particular an arbitrarily large set of these links has diameter of order \(k\beta\) even on a flat complement with \(H_e=4\). This last statement concerns a supremum over endpoints. The probability of the maximizing endpoints has not been estimated.

**PROVED.** Let \(D_z\) denote the diameter of (7). Under the unconditional stationary law, every square-integrable \(f\) satisfies
\[
 \mathbb E\big[(1-\tanh(D_Z/4))\,\operatorname{Var}(f(X)\mid Z)\big]
                     \le \|f\|_\nu^2-\|Pf\|_\nu^2.                      \tag{9}
\]
To prove this, fix \(z\). The conditional neighbour-to-neighbour Markov operator \(L_z\) has rows proportional to \(b_z(y)K_z(u,y)\,dy\). A pair of rows differs by a tilt with maximum-to-minimum ratio at most \(d=e^{D_z}\). Scaling the tilt into \([1,d]\), of mean \(v\), bounds their total variation by \((v-1)(d-v)/(v(d-1))\), by the chord inequality for the positive part of the tilt minus its mean. Its maximum is \(\tanh(D_z/4)\), with zero for identical rows. Thus \(L_z\) contracts oscillations by this factor. It is compact and self-adjoint in its marginal because of (7), compactness of the cube and strict positivity of its continuous densities. Every eigenfunction for a nonzero eigenvalue has a continuous representative. Applying the oscillation estimate to a real centered eigenfunction bounds the centered operator norm by \(\tanh(D_z/4)\).

**PROVED.** More explicitly, put \(A_z f(y)=\mathbb E[f(X)\mid Y=y,Z=z]\) on the centered middle-slice fibre. Conditional on \(X\), the two neighbours are independent draws, even with \(Z\) fixed. Hence \(A_z A_z^*=L_z\) on the centered neighbour space. Conditional variance then gives
\[
 (1-\|L_z\|_0)\operatorname{Var}(f(X)\mid z)
       \le \mathbb E[\operatorname{Var}(f(X)\mid Y,z)\mid z].
\]
Integrate and drop \(z\) from the conditioning on the right. This proves (9) and explains why its contraction factor is for the two outside slices. The argument applies to any physical symmetry sector by restriction.

**PROVED (a uniform statement for individual physical states).** Suppose \(a n=L\) is fixed along a sequence of cubes, \(\beta/\log n\to b>0\), and \(k\) is fixed with \(k b<2\). For every such choice of the \(k\) missing links and any fixed \(E<\infty\),
\[
 \big\|(I-Q)\,\mathbf1_{[e^{-aE},1]}(P)_{\rm phys}\big\|_{2\to2}
                       \longrightarrow0.                                \tag{10}
\]
The subscript restricts the projection to gauge-invariant states. Choose \(s<4\) with \(s>\max(\sqrt2,2kb)\). On \(H_e\ge s\) for all missing links, (8) gives \((1-\tanh(D_z/4))^{-1}\le C(2+\beta)^{Ck}e^{2k\beta/s}\). The contribution of these \(z\)'s to \(\|(I-Q)f\|^2\) is at most this number times \(1-e^{-2aE}\), for unit \(f\) in the stated band. It tends to zero because \(2kb/s<1\).

**PROVED using the lane's marked-plaquette estimate.** A bad \(z\) implies that, for every completion \(x\), one of the \(4k\) incident spatial plaquettes has \(1-w(x_p)>(4-s)/4\). Indeed \(4-h_e\cdot x_e\) is the sum of its four deficits. For a specified spatial plaquette and \(B=\{\beta(1-w_p)>v\}\), the lane's estimate on a rectangular periodic lattice is \(\mathbb E \exp(c\beta\sum_{p\in D}(1-w_p))\le C^{|D|}\) for any prescribed set \(D\). It uses the monotonic normalized one-link spin multipliers, a change of the electric coupling to half its value, and trace Hölder after choosing a common transfer direction for each group of marks. The multipliers are those in Sussman and Alpoge's outline. In magnetic Haar coordinates put \(U_0=T/\lambda\) restricted to the gauge-invariant space. As in row 1290, marking \(B\) on every other slice gives \(\operatorname{Tr}[(1_B U_0^2 1_B)^l]/\operatorname{Tr}U_0^{2l}\le(Ce^{-cv})^l\). At fixed cube the denominator has \(l\)-th root tending to one. Taking roots and using \(U_0^2\succeq r^2\mathbf1_{[r,1]}(U_0)\) bounds the mass of \(B\) in any unit band state by \(r^{-2}Ce^{-cv}\). Transforming to \(\nu\) amounts to dividing the state by \(\psi\). Since the bad-\(z\) indicator is \(Z\)-measurable, its contribution to the conditional variance is bounded by its mass under \(|f|^2\nu\). A union bound therefore finishes (10). [Marked-plaquette estimate, row 1155 (9)](gap-solve7-astra62.md) · [Multiplier monotonicity, row 1149 (16)](gap-solve4-astra62.md) · [Projection argument, row 1290 (11)](gap-solve33-astra62.md) · [Outline 2195–2213](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L2195-L2213)

**PROVED (specialization to a schedule).** For the numerical coefficient \(b=11/(3\pi^2)\) used in row 1215's Wilson normalization, (10) holds for \(k=5\), since \(55<6\pi^2\) (for example \(\pi>31/10\)). This is conditional on the specified cutoff schedule in its physical application. It uses the true one-slice conditional expectation and no heat-trace bound at a shorter period. Row 1169's logarithmic omissions in the thermal experiment have the different inputs and fibre weighting described above. [One-loop schedule](gap-solve23-astra62.md)


## Can the same calculation handle a macroscopic set of links?

**PROVED.** Let \(a_z(u_I)\) be the integral of \(b_z(u)\) in (7) over all the other \(u\)-links. It is a positive smooth density up to normalization. Let \(B_z\) be the infimum, over positive continuous one-link factors \(b_e\), of
\[
     \operatorname{osc}_{u_I}
     \log\!\left(a_z(u_I)\big/\prod_{e\in I}b_e(u_e)\right).
\]
Write \(q_e=\tanh(D_e/4)\) for the individual diameter in (8), using the actual diameter when \(H_e<\sqrt2\). Then
\[
       1-\|L_z\|_0\ \ge\ e^{-2B_z}(1-\max_e q_e).                      \tag{11}
\]
To prove this, first reduce to the hidden coordinates of the neighbours. The remaining coordinates at each neighbour are drawn from \(b_z\) conditional on the hidden ones, independently across the two ends. The Markov operator factors as conditional averaging, the reduced operator, and the isometric inclusion. Its nonzero spectrum is the spectrum of the reduced operator. Replace \(a_z\) at each end by \(\prod b_e\). The normalized joint law then factors into independent pairs. Each coordinate operator is positive semidefinite by its representation as two draws from the same intervening spin. A product of their eigenbases shows that the norm on centered functions is the maximum of their centered norms, bounded by \(\max_e q_e\). For the original pair, write the quotient of the one-sided weights, after constant rescaling, in \([1,e^{B}]\). In the variational quotient for the gap, the numerator is the joint integral of \(|v(u)-v(y)|^2/2\), and the denominator is the infimum over constants \(c\) of the joint integral of \(|v(u)-c|^2\). The common normalization cancels. The numerator is at least its comparison value and the denominator at most \(e^{2B}\) times its comparison value. Taking the infimum in the definition of \(B_z\) proves (11). No product approximation to the Wilson vacuum is assumed in the proof.

**PROVED (the actual one-sided weight).** The vacuum equation implies that for some finite positive measure \(\Lambda_z\),
\[
       a_z(u_I)=\int \exp\!\left(\beta\sum_{e\in I} c_e\cdot u_e\right)
                               d\Lambda_z(c),\qquad |c_e|\le5.           \tag{12}
\]
Substitute the one-step integral for \(\psi(u)\) in \(b_z(u)\). The magnetic half-weights combine to the whole spatial Wilson weight on \(u\). At each hidden link the terms linear in \(u_e\) are its four spatial staples and its one forward temporal staple. The other factors are positive and depend only on the variables being integrated. No plaquette contains two hidden links. Pushing these factors forward by their five-staple sums gives (12). The measure \(\Lambda_z\) may correlate every pair of hidden links.

**PROVED.** The correlations that a product estimate would have to control can be read directly from (12). Tilt \(\Lambda_z\) by the displayed exponential at \(u_I\) and normalize it. For distinct \(e,f\), the mixed derivative of \(\log a_z\) in unit tangent directions \(v_e,v_f\) is \(\beta^2\operatorname{Cov}_{z,u}(c_e\cdot v_e,c_f\cdot v_f)\). If \(J_{ef}\) bounds its absolute value for all \(u_I\) and these directions, then \(B_z\le2\pi^2\sum_{e<f}J_{ef}\). Fix one anchor configuration and interpolate each coordinate by a shortest geodesic from the anchor. Subtract the sum of the single-coordinate log increments at the anchor from the full log increment. Telescoping in coordinate order, then moving each preceding coordinate back to its anchor, bounds the remainder by the sum over pairs of \(J_{ef}\) times the two arc lengths. Taking its oscillation gives the factor two. The bound \(|c_e|\le5\) alone also gives \(\operatorname{osc}\log a_z\le10\beta k\), which still grows with the cardinality.

**OPEN.** For example, on \(H_e\ge s>2\), (9) and (11) would allow simultaneous erasure at an arbitrarily large \(k\) on a region with
\[
              a(2+\beta)^C\exp(2 B_z+2\beta/s)=o(1) .                  \tag{13}
\]
If this is imposed only on part of the exteriors, the complementary contribution to the variance in (9) still needs a bound in the tested state. Even a full erasure estimate at one set would leave the dependence carried by the retained links. The five-staple bound does not determine the collective dependence in (13).


## A comparison with the correct local fluctuation scale

**GUIDE.** In an actual Wilson path, curvature at the cutoff scale fluctuates even under a very low-energy state. Could the five-staple support in (12), small angular fluctuations and agreement of local marginal laws by themselves give a bound in (11) independent of \(k\)? Row 1167 tested two increasingly sharp spatial wells. Row 1169 found an exponential cost in \(k\) for a common minorant of prescribed histories at fluctuation scale. The following comparison tests the **operator norm** of the integrated two-neighbour channel. It keeps the exact middle kernel (7). The one-sided mixing measure is a comparison input. [Two-well test](gap-solve12-astra62.md) · [Common-minorant test](gap-solve13-astra62.md)

**PROVED (comparison).** Set \(h_e=4t\) with \(t=1\) the identity quaternion. There are smooth positive one-sided weights of the form (12), on \(k=4N\) hidden links, for which the conditional neighbour operator has
\[
                         \|L\|_0\ge 1-C e^{-c N}                        \tag{14}
\]
for all sufficiently large \(\beta\), with \(c,C>0\) independent of \(\beta,N\). The two components giving this bound have identical one-coordinate marginals at the middle slice and identical one-coordinate marginals at either neighbour. The middle variable in each component stays within the usual angular scale \(\beta^{-1/2}\) of \(t\) in root mean square. The slow signal can be read from class functions of groups of four links.

**PROVED (construction).** For \(\alpha=2,4\), use the unnormalized factor
\[
 p_\alpha(u)=\frac{\exp(\alpha\beta\,t\cdot u)}{\Phi((\alpha+1)\beta t)},
 \qquad
 F_\alpha(x)=\int p_\alpha(u)e^{\beta u\cdot x}\,du
       =\frac{\Phi(\beta(\alpha t+x))}{\Phi((\alpha+1)\beta t)}.
\]
The normalization makes \(F_\alpha(t)=1\) for both choices. Write \(p=p_2,q=p_4\), \(m(u,v)=p(u)p(v)+q(u)q(v)\). On one block put
\[
 A(u)=m(u_1,u_2)m(u_3,u_4),\qquad B(u)=m(u_1,u_3)m(u_2,u_4).
\]
On \(N\) blocks use the single one-sided weight \(a(u)=\prod_j A(u^j)+\prod_j B(u^j)\) at each end. Its expansion is a positive mixture in (12) with fields \(2t\) or \(4t\). Define \(A_F,B_F\) by replacing \(p,q\) with \(F_2,F_4\) in the same polynomials. Relative to four independent copies of \(e^{4\beta t\cdot x}dx/\Phi(4\beta t)\), put \(s_\beta=\mathbb E A_F^2=\mathbb E B_F^2\) and \(z_\beta=\mathbb E A_F B_F\). Equality of the squares follows by permuting coordinates. The unnormalized masses for the two labels at the ends are \(s_\beta^N\) for each equal pair and \(z_\beta^N\) for each unequal pair, up to a common factor. This follows by integrating the two neighbours conditional on the middle.

**PROVED (strict separation as \(\beta\) grows).** In the chart \(x=\exp(v/\sqrt\beta)\) at \(t=1\), the reference middle law converges after rescaling to the three-dimensional Gaussian of precision \(4\). Moreover \(0<F_\alpha\le1\) and
\[
        F_\alpha(\exp(v/\sqrt\beta))
                \longrightarrow \exp[-\alpha |v|^2/(2(\alpha+1))].
\]
Indeed radial Haar integration with \(\theta=|v|/\sqrt\beta\) has rescaled Jacobian proportional to \((\sin\theta/\theta)^2\) up to the antipode. The inequalities \(1-\cos\theta\ge 2\theta^2/\pi^2\) for \(0\le\theta\le\pi\) and \(\sin\theta/\theta\le1\) give an integrable Gaussian majorant after removing the maximal exponential factor. They likewise give \(\Phi(rt)\sim c\,e^r r^{-3/2}\) by dominated convergence. Expanding \(|\alpha t+x|^2=(\alpha+1)^2-2\alpha(1-t\cdot x)\) then proves the displayed limit. The limiting functions have nonconstant ratio. For arbitrary two-component vectors \(w_i=(F_2(x_i),F_4(x_i))\), one has
\[
 A_F-B_F=\det(w_1,w_4)\det(w_2,w_3).
\]
Consequently the two limiting block functions differ on an open set of positive Gaussian measure. Cauchy–Schwarz is strict there, so \(z_\beta/s_\beta\le r_*<1\) for all sufficiently large \(\beta\). Under a given equal pair, the middle density on each block is proportional to \(A_F^2\) or \(B_F^2\). These are uniformly bounded above and their normalizers stay bounded below. This also gives the claimed angular mean-square bound. Both pairings act transitively on their four positions by their respective symmetries, and the two laws differ by a permutation. Hence their individual middle marginals coincide exactly.

**PROVED (reading the label at a neighbour).** For an equal pair the joint law of the two neighbours in one block has density proportional to \(A(u)A(y)\mathcal K(u,y)\) or \(B(u)B(y)\mathcal K(u,y)\), with the same strictly positive symmetric \(\mathcal K\) from (7). Their single-coordinate marginals coincide by the same permutations. Their full block marginals at a neighbour, however, have affinity bounded strictly below one as \(\beta\to\infty\). Here are details of the strict limit. Rescale the variables at all three slices around \(t\) as above. Up to a common scalar, a term with endpoint factor \(p_\alpha\) converges there to a positive constant proportional to \((\alpha+1)^{3/2}\) times \(e^{-\alpha|u|^2/2}\), now writing \(u\) for the rescaled coordinate. The two electric factors per site converge after removing their maxima to \(e^{-(|u-x|^2+|y-x|^2)/2}\). The endpoint tilts with \(\alpha\ge2\) and the middle tilt of strength four supply a product Gaussian majorant for all coordinates independently, since the normalized electric factors are at most one. The powers of \(\beta\) and fixed exponential factors removed are the same for the two pairings. Thus the normalized rescaled joint densities and their marginals converge in \(L^1\).

**PROVED.** In these limits write \(A_\infty,B_\infty\) for the same polynomials of the two limiting Gaussian endpoint factors. Their ratio is nonconstant, by the determinant calculation above. The limiting integrated neighbour kernel is strictly positive on all Euclidean arguments. If the two limiting joint laws had the same marginal at a neighbour, they would have it at both neighbours by symmetry. Their log likelihood ratio is \(\log(A_\infty/B_\infty)(u)+\log(A_\infty/B_\infty)(y)\), up to a constant. Its integral against the difference of the joint laws would then vanish. That integral is the sum of the two relative entropies, strictly positive for distinct positive densities by \((s-t)(\log s-\log t)>0\) for unequal \(s,t>0\). The integrals are finite by the Gaussian bounds and at-most-quadratic growth of the log ratios. Equality of the joint laws would force \(A_\infty/B_\infty\) constant by strict positivity of the common kernel. This contradiction shows that the limiting endpoint marginals differ. Their affinity is strictly below one. The \(L^1\) convergence gives convergence of affinities by the square-root inequality. All tests can be taken to use only \(t\cdot u_i\) on the original sphere because integrating the other end and the middle leaves each equal-pair marginal invariant under independent rotations fixing \(t\) at each site. These rotations preserve the densities and the same-site dot products when applied simultaneously to all three slices.

**PROVED.** Across the \(N\) blocks of an equal pair the marginals are independent. Test the two product endpoint marginals by their likelihood ratio. Its sum of the two error probabilities is the integral of the smaller density, at most the affinity, bounded by \(r_1^N\) for a fixed \(r_1<1\). The same test works at either end. Unequal pairs together have probability at most \(r_*^N\). Thus the two estimates of the common fair equal-pair label, coded by \(\pm1\), disagree with probability at most \(r_1^N+r_*^N\), and their means have absolute value \(O(r_1^N+r_*^N)\). The Rayleigh quotient of this centered reading for the neighbour transition is at least \(1-C(r_1^N+r_*^N)\), proving (14). The middle label also has an exponentially accurate likelihood test because the two equal-pair middle block laws have affinity \(z_\beta/s_\beta\). The collection of radial observations recovers the label at both ends.

**OPEN.** This comparison specifies \(a\) explicitly. It does not identify the corresponding \(\Lambda_z\) with the one produced by an isotropic Wilson half-cylinder. It shows why a proof using (12) would have to control dependence between links even when all the one-coordinate readings agree. The repeated-pair label and the constants in (14) are features of the comparison only.


## Finite rotations on the vacuum and their low-energy spectral weight

**PROVED.** Let \(B=B_1\) be any of the triangular rotations used in (4), with \(\sum_i|a_i(x_{<i})|^2\le b_0^2\) everywhere. At fixed neighbours \(u,y\) let \(R\) be the density of the image of the middle law under \(B\), relative to that same law. Then
\[
 \mathbb E[R\mid U,Y]=1,\qquad
 \mathbb E[R^p\mid U,Y]\le \exp(9\beta p(p-1)b_0^2),\quad p\ge1.
                                                               \tag{15}
\]
Indeed \(R(Bx)=\exp(S_{u,y}(Bx)-S_{u,y}(x))\) by preservation of Haar. One factor of \(R\) changes variables in the \(p\)-th moment. Taylor along the product geodesic bounds the remaining exponent by \((p-1)D+9\beta(p-1)b_0^2\). Apply (4) with \(t=p-1\). Jensen gives the same bound after mixing the maps with independent randomness. The likelihood of the resulting change of the time-zero vacuum is \(\ell(X)=\mathbb E[R\mid X]\).

**PROVED.** More generally, take any real \(D_0(U,X,Y)\in L^2\) with \(\mathbb E[D_0\mid U,Y]=0\), and put \(d(X)=\mathbb E[D_0\mid X]\). For \(0<r\le1\),
\[
         \|\mathbf1_{[r,1]}(P)d\|_\nu^2
               \le \frac{1-r^2}{1+r^2}\,\mathbb E D_0^2 .                \tag{16}
\]
For a band vector \(f\), pair \(D_0\) with \(f(X)-g(U)-g(Y)\). Choose \(g=P(I+P^2)^{-1}f\). The two cross terms with the middle each use \(P\), and the cross term between \(U,Y\) uses \(P^2\). Expansion gives the squared norm
\(\langle f,(I-P^2)(I+P^2)^{-1}f\rangle\). Subtracting the two neighbour functions leaves the pairing with \(d\) unchanged. Cauchy–Schwarz and the supremum over unit \(f\) in the band give (16). With \(D_0=R-1\), (15) bounds the last factor by \(e^{18\beta b_0^2}-1\). This controls a finite change of the whole vacuum law. Its density ratio can depend on all of the spatial links even when the map acts at a single link.

**PROVED (a simultaneous family in Wilson theory).** Keep the plaquette-separated set \(I\). For each \(e\in I\), draw a uniform unit imaginary quaternion \(a\) and rotate only \(x_e\) on the left by \(\exp(\kappa a/\sqrt\beta)\), with a fixed \(\kappa>0\). Let \(j_e\) be the resulting marginal density relative to \(\nu\), minus one. These are centered, vertex-gauge-invariant, spatial-centre-neutral functions because conjugating the rotation at its base vertex preserves its law and the centre commutes with it. Let \(Jc=\sum_{e\in I}c_e j_e\). For all coefficient vectors, with constants independent of \(I,n,\beta\),
\[
 \|Jc\|_\nu^2\le K_\kappa\sum_e |c_e|^2,\qquad
 \|\mathbf1_{[r,1]}(P)Jc\|_\nu^2
 \le K_\kappa\frac{1-r^2}{1+r^2}\sum_e |c_e|^2,\qquad
 K_\kappa=e^{18\kappa^2}-1 .                                            \tag{17}
\]
Given \(U,Y,Z\), the hidden middle links are independent and have the single-link conditional densities used in (7). The likelihood \(R_e\) of the individual rotation in this conditional experiment depends only on its own hidden coordinate. Each \(R_e-1\) has conditional mean zero and conditional variance at most \(K_\kappa\) by the same one-link proof of (15) with the other links fixed. Indeed the conditional action is linear in that quaternion with tilt of length at most \(6\beta\). Their conditional covariances vanish for distinct \(e\). With \(D_0=\sum c_e(R_e-1)\) this gives \(\mathbb E|D_0|^2\le K_\kappa\sum |c_e|^2\) and \(\mathbb E[D_0\mid U,Y]=0\). Its conditional mean on \(X\) is \(Jc\), as follows by testing changes of variables against any function of \(X\). Contraction of conditional expectation and (16) prove (17). This estimate holds also for random coefficients measurable in \(Z\), with \(\mathbb E\sum |c_e(Z)|^2\) in place of the deterministic sum.

**PROVED (size and normalization of the family).** There are constants \(c_\kappa>0,\beta_0(\kappa)\) such that for \(\beta\ge\beta_0(\kappa)\) and every \(0<\varepsilon<1\) there is a coefficient subspace \(W\) of dimension at least \((1-\varepsilon)|I|\) on which
\[
       \|Jc\|_\nu\ge c_\kappa\sqrt\varepsilon\,\|c\|_{\ell^2}.
                                                                    \tag{18}
\]
For each \(e\) choose an incident plaquette \(p_e\). The \(p_e\) are distinct and no \(p_e\) contains another selected link. Put \(T_e=\beta(1-w_{p_e})-\nu[\beta(1-w_{p_e})]\). The marked-plaquette estimate used above gives \(\mathbb E_\nu T_e^2\le C\) and \(\nu w_{p_e}\ge1-C/\beta\), uniformly. The Laplace moment bounds the second moment by \(v^2\le C' e^{c v}\) for \(v\ge0\). The exact pairing with \(j_f\) vanishes unless \(e=f\). On the diagonal it is
\[
          \langle T_e,j_e\rangle_\nu
             =\beta(1-\cos(\kappa/\sqrt\beta))\,\nu w_{p_e}\ge c'_\kappa .
\]
The mean rotation matrix is \(\cos(\kappa/\sqrt\beta)\) times the identity. The same scalar enters when the changed link occurs inverted inside a plaquette. Since \(1-\cos u\ge u^2/4\) for \(|u|\le1\), the lower bound holds at large \(\beta\). The positive Gram matrix of the \(T_e\)'s has trace at most \(C|I|\). Take \(W\) to be the span of its eigenvectors with eigenvalues at most \(C/\varepsilon\). For \(c\in W\), pair \(Jc\) with \(\sum c_e T_e\), whose norm is at most \(\sqrt{C/\varepsilon}\|c\|\). The exact diagonal formula bounds the pairing below by \(c'_\kappa\|c\|^2\), proving (18). In particular the \(j_e\)'s are linearly independent even before discarding the exceptional coefficient directions.

**PROVED (physical scale of this estimate).** On an even cube one can take all direction-one edges with \(x_2+x_3\) even, numbering \(n^3/2\), as in row 1155. Every unit vector \(v\in JW\) then satisfies
\[
   \|\mathbf1_{[0,E]}(-a^{-1}\log P)v\|^2
       \le \frac{K_\kappa}{c_\kappa^2\varepsilon}\tanh(aE).
                                                                    \tag{19}
\]
This holds simultaneously on the stated subspace and only uses large \(\beta\) for its lower normalization. For example one can choose a fixed \(\delta_{\kappa,\varepsilon}>0\) with the right-hand side at \(E=\delta_{\kappa,\varepsilon}/a\) below one half. Every such vector then has at least half its spectral weight at energies above \(\delta_{\kappa,\varepsilon}/a\). These vectors need not be eigenvectors, and the estimate gives no lower bound on the Hamiltonian acting on their orthogonal complement.


## Random erasure of order the square root of the spatial volume

**PROVED (orthogonality at all orders).** In the conditional product law of the hidden middle links given \(U,Y,Z\), make any independent one-link replacements with densities relative to those conditionals denoted by \(R_e\). A replacement can use the common observed data \(Z\). Write \(K_e=\mathbb E[(R_e-1)^2\mid U,Y,Z]\). Products \(\prod_{e\in A}(R_e-1)\) for distinct subsets \(A\subset I\) are conditionally orthogonal because an index in their symmetric difference has just one centered factor. Their conditional squared norms are \(\prod_{e\in A}K_e\). Consequently if a replacement at \(e\) is activated with probability \(\theta_e(Z)\) independently given \(Z\), the density \(R\) of the altered middle slice with the mask averaged out, given \(U,Y,Z\), obeys
\[
 \mathbb E[R\mid U,Y,Z]=1,\qquad
 \mathbb E[R^2\mid U,Y,Z]=\prod_{e\in I}(1+\theta_e(Z)^2K_e).           \tag{20}
\]
Here \(R=\prod_e(1+\theta_e(R_e-1))\). For the rotations of (17), (16) also bounds every linear combination of the conditional means on \(X\) of the nonempty-subset products. The squared coefficient cost is \(\sum_{A\ne\varnothing}K_\kappa^{|A|}\mathbb E|c_A(Z)|^2\). These identities suggest sampling the mask independently in each coordinate before estimating the cost.

**PROVED (a one-link completion using the retained spatial data).** Take all links of \(I\) parallel, still with no two on one plaquette. In (7), at each \(e\) with \(H=|h|\ge3\), put \(t=h/H\) and replace its middle link by an independent quaternion of density
\[
           \rho_e(x\mid Z)=\exp(12\beta\,t\cdot x)/\Phi(12\beta t).
\]
Keep every link with \(H<3\). This rule uses neither neighbour. For the good links write \(v=u_e+y_e\), \(p=h+v\), \(r_0=|p|\). The actual conditional density is \(q_e(x)=e^{\beta p\cdot x}/\Phi(\beta p)\). The likelihood \(R_e=\rho_e/q_e\) has
\[
  1+K_e=\frac{\Phi(\beta p)\Phi(\beta(24t-p))}{\Phi(12\beta t)^2}
       \ \le C\,\exp\!\left(\tfrac89\beta\sum_{p'\ni e}(1-w_{p'})\right). \tag{21}
\]
The sum is over the four spatial and two temporal plaquettes incident on this middle link in the original Wilson path.

**PROVED.** For \(d=r_0-t\cdot p\), direct squaring gives
\[
 d=\frac{(H+|v|-r_0)(r_0+|v|-H)}{2H}
       \le \frac{2}{H}(6-r_0).
\]
Indeed \(r_0\le H+|v|\), \(|v|\le2\), and \(H\le4\). The component of \(v\) perpendicular to \(t\) has squared norm \(d(r_0+t\cdot p)\le12d\). The excess of \(|24t-p|\) over \(24-t\cdot p\) is thus at most \(12d/36=d/3\), since \(24-t\cdot p\ge18\). The exponential rate in the ratio in (21) is at most \(4d/3\le (8/9)(6-r_0)\). For the actual middle spin \(x_e\), \(6-r_0\le6-p\cdot x_e=\sum_{p'\ni e}(1-w_{p'})\). Finally \(r_0\in[1,6]\), \(|24t-p|\in[18,30]\). The upper and lower bounds \(\Phi(st)\asymp e^s(1+s)^{-3/2}\) for \(s\ge0\) follow by the polar integral as above. Their three prefactors in (21) have bounded ratio uniformly in \(\beta\ge1\). This is why a fixed factor 12 in the proposal suffices.

**PROVED (joint moment in the interacting path).** Set \(K_e'=1_{\{H_e\ge3\}}K_e\), taking it to be zero on the excluded links. For every \(J\subset I\) one has
\[
                    \mathbb E\prod_{e\in J}K_e'\le C_0^{|J|}.           \tag{22}
\]
The six plaquettes per selected link in (21) are distinct and all contain the spatial direction of \(I\). Use that direction as transfer time on the periodic four-torus. Multiplication by \(e^{(8/9)\beta(1-w_{p'})}\) changes each marked coupling from \(\beta\) to \(\beta/9>0\). The normalized convolution at coupling \(s\) has spin multipliers \(I_{2l+1}(s)/I_1(s)\), products of the increasing ratios \(I_{j+1}/I_j\) in row 1149. The smaller coupling therefore gives a smaller positive operator. Congruence by the unchanged positive spatial half-weight, and gauge projection, preserve this order. Each marked factor costs a normalizer ratio \(z_{\beta/9}/z_\beta\le C_1\), where \(z_s=e^{-s}\Phi(st)\). For a transfer circle of length \(L_1\), trace Hölder bounds the trace of the modified layer product by the product of the \(L_1\)-Schatten norms. A positive modified layer bounded in operator order by \(C_1^j\) times the homogeneous layer has \(L_1\)-Schatten norm at most \(C_1^j\) times the homogeneous norm, by min–max. The product of the homogeneous norms is the ordinary partition function. This proves the required moment bound with \(6|J|\) marks on any sufficiently long rectangular periodic time cylinder. Let the original temporal length tend to infinity at fixed spatial box. Away from its seam, setting temporal links to one on the two open steps is a Haar change of frames. The remaining gauge-projected transfer power tends, after normalization, to the vacuum projector by compactness and simplicity of the top eigenvalue. The gauge-invariant plaquette moment therefore has the same bound in the stationary path used here. Keeping the common direction in the argument of row 1155 (9) allows the exponent \(8/9\). [Wilson moment argument](gap-solve7-astra62.md) · [Ordered spin multipliers](gap-solve4-astra62.md)

**PROVED (erasure estimate).** Let \(m_I=|I|\ge1\). Independently activate each link with \(H_e\ge3\) with probability \(\theta\in[0,1]\). Denote the random erased set by \(M_0\), the observation by \(\mathcal O=(M_0,X_{M_0^c})\), and the refilled slice by \(X'\). It can be drawn using only \(\mathcal O\). Equations (20)–(22), expanded over subsets, give \(\mathbb E R^2\le(1+C_0\theta^2)^{m_I}\). For any bounded \(f\), writing \(\mathcal D(f)=\langle f,(1-P)f\rangle_\nu\), one has
\[
 \mathbb E\,\operatorname{Var}(f(X)\mid\mathcal O)
 \ \le\ 4\mathcal D(f)+4\sqrt2\,\|f\|_\infty
              (1+C_0\theta^2)^{m_I/2}\sqrt{\mathcal D(f)}.              \tag{23}
\]
In fact, under the original sampling and independent refilling, \(f(X')\) is a randomized predictor conditionally independent of the missing true links given \(\mathcal O\). The squared prediction error therefore bounds the conditional variance. Split its difference from \(f(X)\) through \(f(U)\), using \(|s+t|^2\le2|s|^2+2|t|^2\). The original difference has second moment \(2\mathcal D(f)\). For the other difference integrate \(|f(X)-f(U)|^2\) against \(R\) in the original joint law. Its original fourth moment is at most \(8\|f\|_\infty^2\mathcal D(f)\). Cauchy–Schwarz proves (23). For the marginal density of the refilled state, (16) gives in addition
\[
 \left\|\mathbf1_{[r,1]}(P)
       \left(\frac{d\mathcal L(X')}{d\nu}-1\right)\right\|_\nu^2
 \le \frac{1-r^2}{1+r^2}\big[(1+C_0\theta^2)^{m_I}-1\big].
                                                                    \tag{24}
\]
Equation (24) tests the averaged density against all normalized band states. Equation (23) requires the displayed supremum norm of the reading.

**PROVED (physical-size consequence).** Take the direction-one checkerboard set \(m_I=n^3/2\) on the even cube, \(\beta\to\infty\), \(an=L\) fixed. The expected fraction with \(H_e<3\) is \(O(e^{-c\beta})\) by the spatial-plaquette bound in the proof of (10), so this fraction tends to zero in probability. Conditional on the retained complement \(Z\), the mask count is binomial on the eligible sites. If \(\theta m_I\to\infty\), its ratio to \(\theta m_I\) tends to one in probability by the binomial variance and the preceding fraction bound. With \(\theta=m_I^{-1/2}\), (23) tends to zero for any uniformly bounded \(f\) with \(\mathcal D(f)=O(1/n)\), while \((1+o_{\mathbb P}(1))\sqrt{m_I}\) links have been erased. One may even take \(\theta=\sqrt{\eta\log n/m_I}\) with \(0<\eta<1/C_0\). The second term in (23) is \(O(n^{-(1-C_0\eta)/2})\) and the count is asymptotic in probability to \(\sqrt{\eta m_I\log n}\). All masks are random and the eligibility test uses retained spatial data. Row 1169, (21), treated prescribed sets of logarithmic size for bounded slow readings. The larger count here comes from the square of the activation probability in (20) and the common-direction estimate (22). [Prescribed-set comparison](gap-solve13-astra62.md)

## A prescribed number of uniformly chosen erasures

**PROVED.** A mask chosen independently of the field can erase exactly a prescribed number of links. The following replacement works even at a vanishing staple sum. For \(H\le9/4\) set \(\rho_e(x)=e^{\beta h\cdot x}/\Phi(\beta h)\), and for \(H>9/4\) set \(\rho_e(x)=e^{60\beta t\cdot x}/\Phi(60\beta t)\). Both use only \(Z\). For every fixed \(J\subset I\), the resulting conditional chi-squared costs obey
\[
              \mathbb E\prod_{e\in J}K_e
                 \le [C_2(1+\beta)^3]^{|J|},\qquad \beta\ge1 .          \tag{25}
\]
Here and below \(I\) is any plaquette-separated set parallel to one coordinate direction.

**PROVED.** In the high-\(H\) case the excess of \(|120t-p|\) over \(120-t\cdot p\) is at most \(12d/228=d/19\), by the perpendicular-component calculation in (21). Its rate is therefore bounded by \((20/19)(2/H)(6-|p|)\le(160/171)(6-|p|)\). The Bessel prefactors are bounded since \(|p|\ge1/4\). The six marks of (22) can again be weakened by a fixed fraction. In the low-\(H\) case the exact second moment is
\[
          1+K_e=
       \frac{\Phi(\beta(h+v))\,\Phi(\beta(h-v))}{\Phi(\beta h)^2}
       \le C(1+\beta)^{-3}\exp\!\left(\beta\sum_{\substack{p'\ni e\\
                     p'\ {\rm spatial}}}(1-w_{p'})\right).               \tag{26}
\]
Indeed the exponential rate is at most \(2\sqrt{H^2+4}-2H\) by Cauchy–Schwarz and \(|v|\le2\). Its distance below \(4-H\) is at least \(cH\), for \(c=(25-2\sqrt{145})/9>0\), by concavity of \(4+H-2\sqrt{H^2+4}\) and its values at 0 and \(9/4\). If \(H\le1/4,\ |v|\ge1\), both numerator arguments before multiplication by \(\beta\) have length at least \(3/4\). Their prefactors supply \((1+\beta)^{-3}\) and the slack \(c\beta H\) absorbs the denominator cost \((1+\beta H)^3\). If \(H\ge1/4\), the positive slack absorbs both polynomial costs. In the remaining case \(H<1/4,\ |v|<1\), the rate is at most \(2\sqrt{1+1/16}\), strictly below \(4-H\ge15/4\). Finally \(4-H\le4-h\cdot x_e\), the spatial deficit in (26).

**PROVED.** To average (26), delete its four marked spatial plaquettes in the common transfer direction. At coupling zero the normalized convolution is the projection onto the constants, below the normalized convolution at \(\beta\) by its nonnegative spin multipliers. Each deletion costs \(z_0/z_\beta\le C(1+\beta)^{3/2}\) in the trace comparison of (22). Multiplied by the prefactor in (26), the four deletions cost only \(C(1+\beta)^3\) per low-\(H\) link. For a mixed product, bound each factor by the sum of the two estimates with their indicators discarded. Expand over the high/low choices and apply the same trace comparison to each fixed pattern. None of their marked plaquettes coincide. The number \(2^{|J|}\) of patterns is absorbed in \(C_2^{|J|}\). This proves (25).

**PROVED.** Independently of the whole Wilson path choose \(M_0\) uniformly among the \(s\)-element subsets of \(I\), \(0\le s\le m_I\). Write \(Q_M f=\mathbb E_\nu[f\mid X_{M^c}]\). With \(R\) the mask-averaged three-slice likelihood, the expansion using (20) now has coefficients \(\mathbb P(A\subset M_0)=(s)_{|A|}/(m_I)_{|A|}\le(s/m_I)^{|A|}\) for each \(A\subset I\), where \((b)_j\) is the descending factorial. Orthogonality and (25) give
\[
 \mathbb E R^2\le \exp\big(C_2(1+\beta)^3s^2/m_I\big),\qquad
 \mathbb E_{M_0}\|(I-Q_{M_0})f\|_\nu^2
 \le4\mathcal D(f)+4\sqrt2\|f\|_\infty
     e^{C_2(1+\beta)^3s^2/(2m_I)}\sqrt{\mathcal D(f)} .                \tag{27}
\]
The second estimate is (23)'s prediction proof with this mask law. The spectral bound (24) uses the new first bound in exactly the same way. If \(m_I=n^3/2,\ \beta\asymp\log n\), choose \(s=\lfloor\sqrt{\eta m_I\log n/(1+\beta)^3}\rfloor\), \(0<\eta<1/C_2\). Then \(s\asymp n^{3/2}/\log n\) and the mean squared error tends to zero for every uniformly bounded sequence of readings with \(\mathcal D(f)=O(n^{-1})\). For each such sequence Markov's inequality also gives convergence in probability over uniform masks. The set has the specified size on every draw, and its selection uses no plaquette tests.

**PROVED (which states can evade the estimate).** Let \(a=L/n\), \(\mathcal D(f)\le C/n\), \(\|f\|_2=1\), and initially take real \(f\). In (27) suppose \(C_2(1+\beta)^3s^2/m_I\le u\log n\) for a constant \(0<u<1\). For any \(0<t<(1-u)/2\), set \(b_n=n^t\) and \(f_b=(-b_n)\vee(f\wedge b_n)\). Clipping is 1-Lipschitz and \(\mathcal D(f)=\tfrac12\mathbb E|f(U)-f(X)|^2\). Thus (27) bounds the mean square error for \(f_b\) by
\[
          \epsilon_n=C'\big(n^{-1}+n^{t-(1-u)/2}\big).
\]
Conditional expectation is a contraction in \(L^p\). On the product of the mask probability and \(\nu\), for \(1\le p<2\) this gives
\[
 \big(\mathbb E_{M_0}\|f-Q_{M_0}f\|_p^p\big)^{1/p}
            \le \sqrt{\epsilon_n}+2b_n^{-(2-p)/p}.                       \tag{28}
\]
Indeed \(|f-f_b|^p\le b_n^{p-2}|f|^2\) on the clipping event. The estimate holds uniformly on the real normalized low band, even for \(p=p_n\uparrow2\) if \((2-p_n)\log n\to\infty\). Real and imaginary parts give the complex version up to an absolute factor. For \(p=2\), the mean square error has square root at most \(\sqrt{\epsilon_n}+(\int_{\{|f|>b_n\}}|f|^2\,d\nu)^{1/2}\), using the orthogonal projection \(I-Q_M\) on the tail. Thus an order-one loss in \(L^2\) forces an order-one share of the state's norm onto amplitudes larger than \(n^t\). Uniform integrability of the squared state densities suffices to recover \(L^2\) convergence. The distinguishing issue is the concentration of normalized states as the cutoff changes.
## Stationary resampling of a positive density of links

**PROVED (a quadratic-form comparison for all states).** In the actual conditional experiment of (7), let \(\rho_e(\cdot\mid Z)\) be a probability density and let \(\epsilon_e=\epsilon_e(U,Y,Z)\in[0,1)\) satisfy \(q_e\ge\epsilon_e\rho_e\) pointwise. Before drawing the hidden links, independently given \(U,Y,Z\) flag each \(e\) with probability \(\epsilon_e\). Draw from \(\rho_e\) at each flagged link and use the residual density at every other link, given by \((q_e-\epsilon_e\rho_e)/(1-\epsilon_e)\). The marginal triple is exactly the original Wilson triple. If \(F\) is the set of flags and \(\mathcal A=(F,X_{F^c})\), the missing spins, given \(\mathcal A,U,Y\), have product law \(\prod_{e\in F}\rho_e(\cdot\mid Z)\). It depends only on \(\mathcal A\). This follows by conditioning the product experiment on its flags and all the unflagged spins. Take an independent second draw of the flagged coordinates with the same law, obtaining \(X''\). The conditional pair \(X,X''\) given \(\mathcal A\) is exchangeable and conditionally independent. Its marginals are both \(\nu\), giving a positive self-adjoint Markov operator \(K_I\) on \(L^2(\nu)\). For every \(f\in L^2(\nu)\),
\[
 \begin{split}
  \langle f,(I-K_I)f\rangle
     &=\mathbb E\operatorname{Var}(f(X)\mid\mathcal A)\\
     &\le \left\langle f,\frac{I-P^2}{I+P^2}f\right\rangle
      \le 2\mathcal D(f).                                                \tag{29}
 \end{split}
\]
Indeed the conditional variance given \(\mathcal A,U,Y\) equals that given \(\mathcal A\). It is bounded on average by the square error of any predictor \(g(U)+g(Y)\). Minimizing as in (16) proves the first inequality. The last follows from \((1-t^2)/(1+t^2)\le2(1-t)\) on \([0,1]\). This construction uses one common minorant per flagged link. Row 1169 estimated the common minorant of a prescribed product of links. Here the flags reveal which trials used the common component, conveying information about the realized field. Equation (29) is an exact stationary resampling form. [Prescribed product minorant](gap-solve13-astra62.md)

**PROVED (local choice of the flags).** There exist constants \(B_1<\infty,\epsilon>0,\beta_1<\infty\), all independent of the grid, for the following choice. When \(H_e\ge3\), put \(t_e=h_e/H_e\). Test whether
\[
       \max\{|u_e-t_e|,|y_e-t_e|\}\le B_1/\sqrt\beta.
\]
On links passing both tests use flag probability \(\epsilon\) and let \(\rho_e\) be uniform on the round cap of radius \(\beta^{-1/2}\) about \(t_e\). Assign zero probability of flagging the remaining links. Norms in the test are Euclidean quaternion norms. For any fixed \(B_1\) and sufficiently large \(\beta\), \(p=h+u_e+y_e\) has length at least three on a passing link, and \(|p/|p|-t_e|\le C B_1/\sqrt\beta\) by subtraction of \((H+2)t_e\) followed by the triangle inequality for normalization. At every \(x\) in the cap, \(\beta(|p|-p\cdot x)=\beta |p|\,|p/|p|-x|^2/2\le C(1+B_1)^2\). The polar integral bound for \(\Phi\) gives \(q_e(x)\ge c\beta^{3/2} e^{-C(1+B_1)^2}\), while the cap mass is at least \(c'\beta^{-3/2}\). Choosing a positive \(\epsilon<1\) below the product of these constants proves the required minorization.

**PROVED (spacetime defects in a normalized slow state).** Write \(m_I=|I|\). There are constants \(B,c,C>0\) independent of \(m_I,n,\beta\ge1\) such that, for every physical \(\|f\|_2=1\), in the original three-slice law,
\[
 \mathbb E\!\left[|f(X)|^2\,\mathbf1_{\{\beta\sum_{e\in I}
            \sum_{p'\ni e}(1-w_{p'})>B m_I\}}\right]
       \le C e^{-c m_I}+C\sqrt{\mathcal D(f)}.                           \tag{30}
\]
All four spatial and both temporal plaquettes are included. For the spatial sum, mark the event \(A\) of exceeding \(B m_I/3\) on each second time slice. Markov's inequality on the product of these indicators and the common-direction change of coupling of (22) give a trace bound \(\operatorname{Tr}[(1_A P^2 1_A)^\ell]\le e^{-c m_I\ell}\operatorname{Tr}P^{2\ell}\) on the physical space once \(B\) is large. The traces refer to the unitary ground-state transform. No marks coincide. Taking roots at fixed grid gives \(\|1_A P\|^2\le e^{-c m_I}\). Since \(\|f-Pf\|\le\sqrt{\mathcal D(f)}\), this controls the spatial-event mass.

**PROVED.** For either one of the two temporal sums mark the symmetric one-step event \(G(x,y)\) that its threshold \(B m_I/3\) is exceeded. Let \(P_G\) be the transfer with that indicator inserted in its kernel. It preserves the gauge-invariant space and is self-adjoint there because the selected temporal plaquette traces are \(x_e\cdot y_e\) in temporal gauge. The trace of \(P_G^{2\ell}\) is the Wilson physical trace with the event on all \(2\ell\) steps. Projection onto the invariant space closes the temporal gauge in that trace, and each event uses the corresponding transport across its step. The selected temporal faces are distinct across steps. The same positive-coupling comparison gives \(\operatorname{Tr}P_G^{2\ell}\le e^{-2c m_I\ell}\operatorname{Tr}P^{2\ell}\). Even powers bound \(\|P_G\|\le e^{-c m_I}\) whether or not \(P_G\) is positive as a Hilbert-space operator. Now
\[
 \mathbb E[|f(X)|^2\mathbf1_G(X,U)]
   \le |\langle f,P_G f\rangle|+\|f\|_2
                                   \|f(X)-f(U)\|_2
   \le e^{-c m_I}+\sqrt{2\mathcal D(f)}.
\]
Time reversal supplies the other step. Union of the three events proves (30). The same conclusion with the weight \(|f(U)|^2\) costs at most another \(2\sqrt{2\mathcal D(f)}\), by Cauchy–Schwarz on the difference of squared moduli. This argument uses only one-step increments and trace bounds for prescribed plaquettes.

**PROVED (number of links actually resampled).** With \(B_1,\epsilon,\beta_1\) chosen as above there are constants \(\delta,c,C>0\) for which
\[
 \mathbb E\big[|f(X)|^2\,\mathbf1_{\{|F|<\delta m_I\}}\big]
       \le C e^{-c m_I}+C\sqrt{\mathcal D(f)},\qquad \beta\ge\beta_1.     \tag{31}
\]
On the complementary event to (30), at least half the links have \(\beta\sum_{p'\ni e}(1-w_{p'})\le2B\). Each such link has \(4-H_e\le2B/\beta\), \(H_e(1-t_e\cdot x_e)\le2B/\beta\), and both \(1-x_e\cdot u_e,\ 1-x_e\cdot y_e\le2B/\beta\). Hence it passes the tests in the local choice for a fixed \(B_1=C\sqrt{1+B}\) and all sufficiently large \(\beta\). The number passing is measurable in \(U,Y,Z\). Conditional on those data, the flags on the passing links are independent Bernoulli variables of parameter \(\epsilon\). The probability of fewer than \(\epsilon m_I/4\) flags when at least half pass is at most \(e^{-c_\epsilon m_I}\), by applying the exponential Markov inequality to the negative of their sum. This conditional bound also holds after weighting by \(|f(U)|^2\). For the bad passing count use (30) with that weight. Moving the weight back to \(X\) costs at most \(2\sqrt{2\mathcal D(f)}\), proving (31). For \(I\) a full checkerboard colour, a positive fraction of \(n^3/2\) actual spins is independently redrawn from the stated caps, with probability tending to one uniformly under normalized physical states with \(\mathcal D(f)\to0\). The stationary expectation of \(|f(X'')-f(X)|^2\) is at most \(4\mathcal D(f)\) by (29). This includes states whose squared amplitudes are not uniformly integrable.
## Testing the lower spectral edge with the resampling operator

**PROVED (a trapped set and its removal).** Using only the cap flags of (31) would leave an open set fixed by every colour on cubes with \(4\mid n\). For coordinates \(x_j\) modulo \(n\) and a fixed imaginary unit \(i\), take abelian links
\[
 U_1(x)=1,\qquad U_2(x)=\exp(i\pi x_1/2),\qquad
 U_3(x)=\exp(i\pi(x_1+x_2)/2).
\]
The oriented plaquette in each positive coordinate plane is \(\exp(i\pi/2)\). In each transverse plane the two staples at an edge sum to the edge times \(2\cos(\pi/2)=0\). Thus all \(H_e=0\). Continuity and strict positivity of the finite-volume vacuum density give positive measure to an open neighbourhood where all \(H_e<3\). This set is gauge invariant when defined by the \(H_e\) inequalities, and has probability strictly less than one by the corresponding open neighbourhood of the flat field. Its indicator is an exact nonconstant fixed function for the cap-only resampling operator, by reversibility. A high-probability count of flags leaves this obstruction undetected.

**PROVED.** Use a second kind of flag on every link, of constant probability \(p_0=e^{-4\beta}/2\) given \(U,Y,Z\), with density \(\rho_e^0=e^{\beta h_e\cdot x}/\Phi(\beta h_e)\). Use half the earlier cap probability where eligible. The ratio \(q_e/\rho_e^0\) lies in \([e^{-4\beta},e^{4\beta}]\), since \(|u_e+y_e|\le2\) and the ratio of the two normalizers lies in \([e^{-2\beta},e^{2\beta}]\). The sum of the two specified subdensities lies below \(q_e\) by taking half of each individual minorant. Reveal the kind of each flag. The proof of (29) is unchanged and (31) holds with a smaller \(\delta\). The rules are gauge covariant because all the local quaternion fields transform by the same left and right actions as the deleted link.

**PROVED (finite-grid coercivity).** On the even cube use the six colours obtained by choosing an orientation and the parity of the sum of the other two coordinates. Let \(K\) be the uniform average of the six corrected operators, and let \(m=3n^3\). Then, writing \(\operatorname{gap}\) for the infimum of the centered Dirichlet quotient,
\[
      \operatorname{gap}(P_{\rm phys})\ge\tfrac12\operatorname{gap}(K_{\rm phys})
      \ge \frac{6^{-6}}{24}\big(\tfrac12 e^{-16\beta}\big)^m .           \tag{32}
\]
For a fixed starting field and fixed temporal neighbours, the posterior probability of a base flag at \(e\) is \(p_0\rho_e^0(x_e)/q_e(x_e)\ge e^{-8\beta}/2\). The posteriors are independent within the colour. The new values at such flags have density at least \(e^{-8\beta}\) against Haar since \(|h_e|\le4\). Consequently a sweep taking the six colours in a fixed order has transition density at least \((e^{-16\beta}/2)^m\) against product Haar, uniformly in the start, by successive application of the one-colour bound to coordinates drawn just once in this sweep. The specified order occurs with probability \(6^{-6}\) under \(K^6\). For a centered \(f\), the integral of \(|f(x)-f(y)|^2\) against \(\nu(dx)\,dy\) is at least \(\|f\|_\nu^2\). The Dirichlet form of \(K^6\) contains half this integral times the lower density. Finally \(I-K^6\preceq6(I-K)\), and (29) gives \(I-K\preceq2(I-P)\). This proves (32). Its right side divided by \(a\) tends to zero on the proposed continuum schedule.

**PROVED (action-density test).** Choose one distinct incident spatial plaquette \(p_e\) per \(e\in I\). For \(T_e=\beta(1-w_{p_e})-\nu[\beta(1-w_{p_e})]\) there is a constant \(c_0>0\), independent of the cube and all sufficiently large \(\beta\), such that
\[
      \left\langle \sum_e b_e T_e,\frac{I-P^2}{I+P^2}
                                \sum_e b_e T_e\right\rangle_\nu
                          \ge c_0\sum_e|b_e|^2 .                          \tag{33}
\]
For each \(e\) the six-plaquette moment used in (22) bounds the vacuum probability that its scaled deficit exceeds a large fixed threshold. The probability of passing the cap test therefore has a uniform positive lower bound. Given the retained values and the flags, each marked plaquette is either fixed or is a function just of its own independent redraw, of the form \(v_e(Z)\cdot x_e\) with \(|v_e|=1\). Under the uniform cap around \(t\), the covariance has one axial and three equal transverse eigenvalues by rotations about \(t\). Its axial eigenvalue times \(\beta^2\) tends to the strictly positive variance of \(|V|^2/2\), and a transverse eigenvalue times \(\beta\) tends to the positive variance of one component of \(V\), for \(V\) uniform on the three-dimensional unit ball. In the chart \(x=\exp_t(V/\sqrt\beta)\), the density of the rescaled \(V\) converges uniformly on the ball to the uniform law by the round volume element. Taylor expansion of the coordinates is uniform on that compact ball. Thus every direction \(v_e\) has \(\operatorname{Var}(\beta v_e\cdot x_e)\ge c'>0\) on a cap flag. Average the independent conditional variances and apply (29) to obtain (33).

**PROVED.** For any \(0<\eta<1\), on a coefficient space of dimension at least \((1-\eta)|I|\) the variance of \(T_b=\sum b_eT_e\) is at most \(C\|b\|_2^2/\eta\), by the trace argument preceding (18). Since \((I-P^2)/(I+P^2)=\tanh(aH_{\rm lat})\), \(H_{\rm lat}=-a^{-1}\log P\), (33) gives
\[
   \|\mathbf1_{(\delta_0/a,\infty)}(H_{\rm lat})T_b\|^2
        \ge \big(c_0-(C/\eta)\tanh\delta_0\big)\|b\|_2^2 .
\]
A fixed positive \(\delta_0\) makes the bracket positive. These are the actual plaquette readings, in addition to the density perturbations tested in (19). For the centered sum of **all** spatial action densities the same variance argument gives a lower bound \(c m_I\) for its \(\tanh(aH_{\rm lat})\) form because the dependence at a cap flag is \(-\beta h_e\cdot x_e\), with \(H_e\ge3\). A normalized low-frequency contribution to the scalar channel could still coexist with these high-frequency fluctuations.
## An inverse covariance test on the time-zero vacuum

**PROVED.** There is a static sufficient estimate on the original gauge-invariant state space that avoids the six-colour sweep. Define the positive tangent tensor \(A_x\) by
\[
 A_x(v,v)=\beta^2\operatorname{Var}_{P(x,dy)}
                               \left(\sum_e v_e\cdot y_e\right).
\]
For \(v\ne0\) the linear reading is nonconstant under the strictly positive conditional density. Thus \(A_x\) is invertible, and is smooth and uniformly positive at each fixed grid by compactness. Define \(C_A\) to be the least constant in
\[
 \operatorname{Var}_\nu(g)\le C_A
      \int\langle\nabla g,A_x^{-1}\nabla g\rangle\,d\nu
 \quad\hbox{for smooth gauge-invariant }g .
\]
Then on the entire physical excited space
\[
       \inf \operatorname{Spec}\!\left(H_{\rm lat}\big|_{\mathcal H_{\rm phys}\ominus\mathbb C1}\right)
                      \ge \frac{1}{2a}\log(1+C_A^{-1}).                  \tag{34}
\]
Indeed, in a tangent direction the conditional score is \(\beta\sum v_e\cdot(y_e-\mathbb E[Y_e\mid x])\), by differentiating the normalized one-step density. Its covariance tensor is \(A_x\). The squared length of the orthogonal projection of \(h(Y)-Ph(x)\) onto the span of these scores, conditionally on \(x\), is exactly \(\langle\nabla Ph,A_x^{-1}\nabla Ph\rangle\), since the normal equations for linear projection have Gram matrix \(A_x\) and right side \(\nabla Ph\). Integration bounds this length by \(\|h\|^2-\|Ph\|^2\). Apply the defining inequality to \(g=Ph\) for any centered physical \(h\). This gives \((1+C_A)\|Ph\|^2\le C_A\|h\|^2\) and proves (34). The score identity is row 944's temporal-gauge force formula. Here its full covariance stays inside the Dirichlet form. [Temporal-gauge score](gap-sgstep-opus.md)

**PROVED (size of the elementary estimate).** At fixed grid \(A_x\preceq\beta^2 m I\) by \(|\sum v_e\cdot y_e|\le\sqrt m\,|v|\). In the vacuum eigenfunction equation the spatial half-action ranges over an interval of width \(\beta m\), and the electric log kernel changes by at most \(2\beta m\) with its first argument. Thus \(\operatorname{osc}\log\psi\le 3\beta m\). The unit three-sphere has first nonconstant Laplace eigenvalue \(3\), from its spherical harmonics, and separation of variables gives the same Haar Poincaré constant \(1/3\) on the product. Comparing variances by minimization over constants and comparing the two gradient integrals yields \(C_A\le \beta^2 m e^{6\beta m}/3\). Substitution in (34) is a finite-grid lower bound. A bound \(C_A\le C/a\) uniform also in physical box size would have the needed physical scale. In a scalar Gaussian mode of stationary variance \(\sigma^2\) with transition \(Y=rX+\sqrt{1-r^2}\,\sigma Z\), \(Z\) standard independent Gaussian, the score variance is \(A=r^2/((1-r^2)\sigma^2)\). The Gaussian Poincaré constant is \(\sigma^2\) with equality on the linear reading, giving \(C_A=r^2/(1-r^2)\). Formula (34) recovers the exact energy \(-a^{-1}\log r\) there. The mode calculation diagnoses which physical scale the static estimate must detect.

**PROVED (a pointwise curvature attempt).** Write \(V=-\log\psi^2\). For tangent \(v\), differentiating the vacuum eigenfunction equation along a product geodesic gives the exact identity
\[
 (\operatorname{Ric}+\nabla^2 V)_x(v,v)
   =2|v|^2+\nabla^2S_x(v,v)
        +2\beta\sum_e |v_e|^2\, x_e\cdot\mathbb E[Y_e\mid x]
        -2 A_x(v,v).                                                     \tag{35}
\]
A pointwise bound \(\operatorname{Ric}+\nabla^2V\succeq c a A\) on the full tangent bundle would give \(C_A\le1/(ca)\). To see this, solve \(\delta_\nu\nabla u=g\) for a smooth centered \(g\) on the compact connected grid (the weighted scalar Laplacian is elliptic with only constants in its kernel). Equation (2) gives \(\|g\|^2\ge ca\int\langle\nabla u,A\nabla u\rangle\,d\nu\), since the Hessian-square term is nonnegative. Pairing \(g\) with \(\delta_\nu\nabla u\) and applying weighted Cauchy–Schwarz gives the criterion. Earlier work tested curvature on an auxiliary bridge. Equation (35) evaluates the curvature on the physical vacuum slice. [Auxiliary bridge curvature](gap-avgcurv-max.md)

**PROVED.** The proposed pointwise curvature is negative in some physical directions at weak bare coupling. On an odd periodic cube set the three constant link fields to the quaternion units \(i,j,k\). Every spatial plaquette is \(-1\), hence the magnetic gradient vanishes. Varying one link in a unit tangent direction \(v\) along a round geodesic makes the four incident traces \(-\cos t\), giving \(\nabla^2S(v,v)=-4\beta\). At this critical point differentiation of \(W S=0\), with \(W\) the generating vector field of a gauge transformation, shows that \(\nabla^2 S\) annihilates gauge-orbit directions in both slots. The horizontal projection \(v_\perp\) therefore has the same Hessian value and is nonzero. Since the remaining mean scalar products in (35) are at most one, its right side at \(v_\perp\) is at most \((2-2\beta)|v_\perp|^2\). The odd windings in the first two directions are \(\pm i,\pm j\), whose common centralizer is the centre, so this orbit is regular. Local transverse coordinates on the quotient thus realize the horizontal direction, and strict negativity persists on an open set when \(\beta>1\). This prevents the pointwise criterion on unrestricted boxes. It neither gives an upper bound on the physical gap nor precludes an integrated estimate for \(C_A\).
## Localizing the remaining spatial mixing estimate

**PROVED.** The global gap of the resampling operator in (32) is stronger than necessary. For an integer \(d\le n/2\), put \(G_d\) equal to the spatial fields for which each translated cube of side \(d\), in each of the three plaquette orientations, has
\(\beta\sum_{p\ {\rm in\ that\ cube,\ orientation}}(1-w_p)\le B d^3\).
For a sufficiently large absolute \(B\), all physical band projections obey
\[
     \|\mathbf1_{G_d^c}\mathbf1_{[r,1]}(P)_{\rm phys}\|^2
               \le 3r^{-2}n^3 e^{-c d^3}.                                \tag{36}
\]
To see this, mark one bad cube and orientation on every second time slice as in (30). There are at most \(C d^3\) marked plaquettes per slice, all containing a common direction. Weakening their couplings by a fixed fraction bounds their exponential moment by a constant to the power \(C d^3\) per slice. The threshold pays \(e^{-c' B d^3}\) per slice. Taking transfer-power roots gives \(\|1_{\rm bad}P\|^2\le e^{-c d^3}\). Represent a band vector as \(Ph\) with \(\|h\|\le r^{-1}\|Ph\|\) and sum the squared bad-set masses over the \(3n^3\) choices. This proves (36), also giving the vacuum bound by taking \(f=1\).

**PROVED (a sufficient lower bound confined to \(G_d\)).** For any of the six-colour averages \(K\) satisfying (29), restrict its stationary chain to \(G_d\) by replacing a proposal to leave \(G_d\) with a holding step. Its stationary law is \(\nu(\cdot\mid G_d)\) by reversibility. Let \(\gamma_d\) be its gap for gauge-invariant functions in that law. For every centered physical \(f\),
\[
 \langle f,(I-K)f\rangle\ge
 \gamma_d\left(\|f\|_\nu^2-\frac{\|\mathbf1_{G_d^c}f\|_\nu^2}{\nu(G_d)}\right).
                                                                            \tag{37}
\]
The transitions with both ends in \(G_d\) give its conditioned Dirichlet form times \(\nu(G_d)\). The centered mean on \(G_d\) costs at most \(\nu(G_d^c)\|\mathbf1_{G_d^c}f\|^2/\nu(G_d)\) by \(\nu f=0\) and Cauchy–Schwarz. Take \(d=\lceil(K_0\log n)^{1/3}\rceil\) with sufficiently large \(K_0\). If \(\gamma_d\ge ca\) uniformly over the spatial boxes and cutoffs in the physical limit, then (29), (36) and (37) exclude all centered band states for \(r=e^{-a\Delta}\) and any fixed \(0<\Delta<c\) at sufficiently small cutoff. Indeed their upper Dirichlet bound is \(\tanh(a\Delta)\), while the lower one is at least \(ca(1-o(1))\). This argument discards the cap-only trapped set by its true spectral weight. It needs mixing only on fields satisfying the local energy tests.

**OPEN.** I cannot establish \(\gamma_d\ge ca\) on those fields. The tests control an average on every specified cube. Even zero plaquette deficit allows the fields \(U_1=\exp(i\alpha/n),\ U_2=U_3=1\) with different spatial winding trace \(2\cos\alpha\). Thus no inequality on the plaquette deficits alone estimates the relaxation time of all collective readings. The true measure and the movement between such readings enter (37). Straight coarse transports were already tested against the temporal transfer in row 1145, so that special case supplies no missing all-observable estimate here. [Straight coarse transports](gap-solve2-astra62.md)
**PROVED (what a uniform bound would pass to the limit).** Suppose a nontrivial reflection-positive Yang–Mills limit has been constructed, with lattice representatives of a dense set of vacuum vectors whose inner products, vacuum means and time-translated inner products converge. A uniform centered lattice energy bound \(m_*>0\) would then give, for each physical time \(t>0\), a bound \(e^{-m_*t}\|v\|\,\|w\|\) on the corresponding centered continuum matrix elements. Apply the lattice spectral theorem at \(\lfloor t/a\rfloor\) steps and pass to the limit on the dense set, then use continuity. On \(v=w\), the positive spectral measure of \(v\) could have no mass in \([0,m_*-\varepsilon]\) for any \(0<\varepsilon<m_*\), since such mass would give a lower bound proportional to \(e^{-(m_*-\varepsilon)t}\) at arbitrarily large \(t\). This identifies the precise transfer statement for which the physical-volume uniformity is required.

**OPEN.** Neither the restricted spatial bound (37) nor the inverse covariance bound \(C_A=O(a^{-1})\) is established at that scale. The finite-grid coercivity, the positive density of resampled links, and the action-density spectral weight leave open states changing collectively across the slice. The nontrivial continuum construction and all-observable Yang–Mills identification required in the preceding implication are also outstanding here. All derivations in this note are analytic research arguments. The note grants no scientific status.

RESULT — OPEN. The four-dimensional SU(2) Jaffe–Witten mass gap remains unproved. Equations (29)–(31) give stationary resampling of a positive density of links with uniform control on every normalized physical slow state. Equations (34) and (37) isolate physical-scale estimates that would exclude the remaining collective states.
