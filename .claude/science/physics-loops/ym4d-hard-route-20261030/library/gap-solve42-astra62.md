## Repo search

**GUIDE.** Research note for FINISH row 1330 at `4ed82544e`. The target-specific prior note is absent. The November 8 search covered main and PRs 10114, 10133, 10134 and 10141. Its scope was chiefly the ultraviolet construction. FINISH row 1329 assigns a check of row 1328. The check file is absent at this pin. [Lead's search](prior/repo-search-2026-11-08.md) · [Row 1328](gap-solve41-astra62.md)

**GUIDE.** I checked the one-step plaquette witness on PR 10114 (contraction at bare coupling at most \(1/32\)), Grok's open crossover and source-transport estimates on PR 10133, the mass-gap interface I1–I5 on PR 10134, and the single-scale classical minimizer estimate on PR 10141. The closest result on main is Theorem ZD-c at `8b11ae2bb9`. It gives a sufficient bound on the full excited trace at half the spatial side. The local estimates address different scales or operators. [One-step witness, lines 4–14 and 106–149](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/f76f6c649c/.claude/science/toe-ruleset-20261021/agents/ym4d-proof/MASS_GAP_LOCAL_BLOCK_ASTRA.md#L106-L149) · [Grok's crossover reduction, lines 77–90](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/89faef229f/.claude/science/toe-ruleset-20261021/agents/ym4d-proof/MASS_GAP_CROSSOVER_REDUCTION.md#L77-L90) · [Interface I1–I5](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/1e70c7211a/.claude/science/physics-loops/ym4d-hard-route-20261030/library/mass-gap-interface.md) · [FP1](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/a2f6a430e2/research/ym4d/library/fp1.md#L299-L315) · [ZD-c](gap-phys-seed.md)

## Sources and choice of attack

**OPEN.** The target is the existence of a nontrivial four-dimensional continuum SU(2) Yang–Mills theory in the sense of Jaffe and Witten, with unique vacuum \(\Omega\), nonempty excited space, and \(\sigma(H|_{\Omega^\perp})\subset[m_*,\infty)\) for one \(m_*>0\) in physical units. The proposed first step is to examine the infrared estimate that would make a full Wilson thermal state nearly pure at one fixed physical size. An estimate must apply along arbitrarily fine cutoffs at that size. The labels describe this author's work and confer no scientific status.

**GUIDE.** Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, supply the one-link convolution and gauge-projected transfer trace in GL3 and GL8. Chunks 01, 02 and 29 of the outline index and its obligations list locate these formulas and the scope of the scalar reconstruction. Outline lines 581–599 and 31860–31882 distinguish it from the full spectral problem. CA-I lines 2704–2712 and 3213–3222 leave the gap open. Both texts were read in bounded excerpts at `31a47c543775`. [GL3](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L2195-L2228) · [GL8](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L2313-L2336) · [CA-I](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L3213-L3222)

**GUIDE.** Row 1218 records the thermal ascent of Deep Bhattacharjee, Ushashi Bhattacharya, James Montgomery Lockwood, Tristan Romanov, Ikailo John Sessford and Sanjeevan Singha Roy. It requires a weak-coupling bound on a window of shapes and a construction hypothesis. The first four authors also give criteria using cube dynamics. Zeng Chunping's approach requires a common infrared rate or a microscopic tunnelling estimate. I use the single-cube test of ZD-c. Row 1328, (12), identifies its thermal purity by conditioning expansion degrees at one or two cuts. Its numerical upper bound on that ratio remains open. [Literature comparison](prior/gap-onebound-read-sol.md) · [Two-period ratio](gap-solve41-astra62.md)

**GUIDE.** Prior B8 credits Philip Hartman and Geoffrey Watson for the spherical heat-kernel mixture. Theorem BR in row 947 uses an ambient Gaussian bridge for each Wilson link. Row 1290 controls gradients on its arithmetic midpoint. Row 1151 uses an exit distribution to compare *two Wilson couplings*. The new question is whether a deterministic amount of spherical heat diffusion can be extracted from **every** temporal link while preserving the full physical thermal trace. The registry search found no overlapping owner for this estimate. [Prior B8](gap-sepinput-max.md) · [Theorem BR](gap-fc-max.md) · [Midpoint estimate](gap-solve33-astra62.md) · [Comparison of couplings](gap-solve5-astra62.md) · [Registry](open-registry.md)

## Angular diffusion on a Wilson link

**GUIDE.** Identify SU(2) with the round unit three-sphere in four-dimensional Euclidean space. Use normalized Haar measure. The one-link Markov convolution \(C_\beta\) has kernel proportional to \(\exp[-\beta|x-y|^2/2]\) for unit quaternions \(x,y\). Write \(H_s\) for spherical heat flow with generator one half of the round Laplacian. The time in this notation is dimensionless. The finite-cutoff physical energies are \(-a^{-1}\log(\lambda_i/\lambda_0)\) for the eigenvalues of the full transfer.

**PROVED (one-link estimate).** For every \(\beta>0\) and \(R>1\) there is a central convolution \(C_{\beta,R}\) with positive kernel and a central nonnegative subprobability measure \(D_{\beta,R}\) such that
\[
 C_{\beta,R}=H_sD_{\beta,R},\qquad s=\frac{1}{\beta R^2},
 \qquad
 0\le k_\beta(x,y)-k_{\beta,R}(x,y)
       \le \epsilon_R k_\beta(x,y),\qquad
 \epsilon_R=8e^{-\beta(R-1)^2/2}.                                      \tag{1}
\]
Both \(D_{\beta,R}\) and \(C_{\beta,R}\) are positive semidefinite as convolutions. The estimate holds for every pair of endpoints, including antipodal quaternions.

**PROVED.** Put \(t=1/\beta\). The Euclidean heat kernel \(p_t(x,y)\) restricted to \(|x|=|y|=1\), divided by \(J=\int_{S^3}p_t(x,z)\,dz\), is \(k_\beta\). Here \(J\) is independent of \(x\). Use the same denominator and the heat kernel killed at the boundary of the radius-\(R\) ball to define \(k_{\beta,R}\). The ratio \(p_t^{R}(x,y)/p_t(x,y)\) is the probability of survival of the Euclidean bridge with those endpoints, by conditioning Brownian motion on its endpoint in the definition of the killed transition density. A bridge is the segment from \(x\) to \(y\) plus a centered Gaussian bridge. The whole segment has norm at most one. Exit therefore requires an absolute displacement of at least \((R-1)/2\) in some coordinate of the centered bridge. For one coordinate the upper crossing probability at height \(b>0\) is \(e^{-2b^2/t}\). Reflect the path after its first hit of \(b\) and take the ratio of the free endpoint densities at \(2b\) and zero. The lower crossing has the same bound. Summing over four coordinates proves the pointwise estimate.

**PROVED.** For clarity, the factorization uses the entire radial path. Let \(r_u\) be the radial part of four-dimensional Brownian motion, started at one and bridged back to radius one at time \(t\), with the final angular position integrated out. Set \(A=\int_0^t r_u^{-2}\,du\). For spherical harmonics of degree \(\ell\), the normalized killed kernel has multiplier
\[
 \mathbb E\!\left[{\bf1}_{\{\max r_u<R\}}
          \exp\{-\ell(\ell+2)A/2\}\right].                               \tag{2}
\]
Indeed the polar-coordinate Laplacian is \(\partial_r^2+3r^{-1}\partial_r+r^{-2}\Delta_{S^3}\). On the degree-\(\ell\) eigenspace the angular term is multiplication by \(-\ell(\ell+2)r^{-2}\). The radial heat equation thus gives the radial diffusion with the indicated exponential weight. One can first work on \(\eta<r<R\). For a bounded potential there, multiplying radial transition kernels by the exponential at successive times gives the weighted semigroup by the Markov property and Riemann sums. Its heat equation follows by differentiation at time zero and the semigroup property, and Dirichlet uniqueness identifies the kernel. Disintegrating in the final radius gives the bridge formula. Passing to \(\eta\downarrow0\) is allowed because \(r^{-2}\) is harmonic away from zero in four dimensions and optional stopping on annuli bounds the free probability of reaching \(\eta\) from one by \(\eta^2\). Absolute continuity of the radial bridge with respect to free radial motion on its first half follows by weighting with the positive remaining radial transition density. Reversibility with respect to \(r^3dr\) gives the same conclusion on the last half. Its continuous path thus has positive minimum almost surely. The radial density at the final radius, with the unit-sphere area convention, is exactly the common factor removed by \(J\).

**PROVED.** On survival \(A\ge t/R^2\). Average the spherical heat probability measures at times \(A-s\) against the radial bridge, retaining the survival indicator. The resulting \(D_{\beta,R}\) is a subprobability measure, and each of its multipliers is nonnegative. Multiplying them by the heat multipliers at \(s\) gives (2) in every spherical harmonic. These harmonics are complete on \(S^3\), and spherical heat flow is central convolution on the quaternion group. This proves (1). It uses the same spherical mixture as B8 and the same ambient Gaussian as BR. The deletion here is chosen on the radial path to give a common angular time and a relative error uniform in the angular endpoints.

## The full periodic cube

**PROVED (error through both periods).** On the periodic spatial cube of even side \(n\ge4\) let \(m=3n^3\) count spatial bonds. Keep the ordinary spatial Wilson plaquette weight \(M^2\), with \(M\) its positive square root, at every layer. On the space invariant under all vertex gauges set
\[
 K=M C_\beta^{\otimes m} M,\qquad
 K_R=M C_{\beta,R}^{\otimes m}M,\qquad
 Z(u)=\operatorname{Tr}K^u,\quad Z_R(u)=\operatorname{Tr}K_R^u .
\]
The full space here contains all electric centre sectors. The same positive vertex-gauge average is understood in both trace integrals. Assume \(\epsilon_R<1\), and put \(b_R=-m\log(1-\epsilon_R)\). For integer \(u\ge1\),
\[
 e^{-u b_R} Z(u)\le Z_R(u)\le Z(u),\qquad
 |\Psi_R(T)-\Psi(T)|\le 2T b_R,\qquad
 \Psi(T)=2\log Z(T)-\log Z(2T).                                        \tag{3}
\]
Multiply the pointwise bounds (1) on each of the \(mu\) temporal plaquettes, then integrate the positive Wilson weight on all links. The error in each log trace lies in \([-u b_R,0]\), which gives the constant \(2T\) in (3). Using the same unnormalized one-link kernel throughout is important for this comparison.

**PROVED (individual levels).** Let \(\lambda_i,\lambda_i^R\) be the ordered eigenvalues on the physical space, beginning with \(i=0\). Both operators are compact, positive semidefinite, and preserve nonnegative functions. They have continuous kernels by the heat construction and gauge averaging. For \(d=1-e^{-b_R}\),
\[
 |\lambda_i^R-\lambda_i|\le d\lambda_0,\qquad
 (1-d)\lambda_0\le\lambda_0^R\le\lambda_0 .
                                                                            \tag{4}
\]
Indeed \(|(K-K_R)f|\le d K|f|\) pointwise, and \(|f|\) remains gauge invariant. This bounds the norm of the difference by \(d\lambda_0\). The min–max inequalities give the first assertion. The ordered pointwise bounds and the nonnegative top eigenfunction of \(K\) give the second. If \(r_i=\lambda_i/\lambda_0\), \(r_i^R=\lambda_i^R/\lambda_0^R\), it follows that \(|r_i^R-r_i|\le2d/(1-d)\). For \(r_i\ge1/2\) and \(d\le1/16\), the mean value bound for \(\log\) gives \(|\log r_i^R-\log r_i|\le 6d\). This also covers every family with bounded physical energy at all sufficiently small spacings.

**PROVED (choice on a physical lattice).** Fix \(p>0\), a physical side \(L>0\), \(4\mid n=L/a\), and \(T=n/2\). Take
\[
 R_n=1+\sqrt{2(4+p)\log n/\beta},\qquad
 s_n=\big(\sqrt\beta+\sqrt{2(4+p)\log n}\big)^{-2}.                    \tag{5}
\]
Then \(\epsilon_{R_n}=8n^{-4-p}\), \(b_{R_n}=O(n^{-1-p})\) and \(|\Psi_{R_n}(T)-\Psi(T)|=O(n^{-p})\). The error in every bounded energy in physical units is \(O_L(n^{-p})\) by (4). The multiplicative trace comparison follows because the log of \(Z_R(u)/(\lambda_0^R)^u\) differs from the log of \(Z(u)/\lambda_0^u\) by at most \(u b_R\). For \(0<\beta\le B\log n\) the common time \(s_n\) is at least \((\sqrt B+\sqrt{2(4+p)})^{-2}/\log n\). There is no lower growth assumption on \(\beta\) in (5).

**PROVED (what free angular evolution would give).** With unit magnetic weight the convolution with \(D_{\beta,R}\) divided by its total mass has all multipliers in \([0,1]\). In that model the vacuum-normalized electric operator to the \(T\)-th power has trace, even before gauge projection, at most
\[
 \left(1+\sum_{\ell\ge1}(\ell+1)^2
                 e^{-\ell(\ell+2)Ts_n/2}\right)^m .                    \tag{6}
\]
The factors are simultaneously diagonal in spherical harmonics. The multiplicity \((\ell+1)^2\) is the difference between the dimensions of homogeneous polynomials in four variables in degrees \(\ell\) and \(\ell-2\), by harmonic decomposition. For \(v=Ts_n\ge1\) the sum is at most \(C e^{-3v/2}\), by factoring out the first exponential and summing the remaining Gaussian series at \(v=1\). With (5), \(\beta\le B\log n\) and \(T=n/2\), \(m e^{-3Ts_n/2}\to0\). Thus the upper bound tends to one. To get the Wilson seed this argument would have to account for \(M^2\) between each consecutive pair of electric convolutions.

**PROVED (test on the gauge-invariant spectrum, using row 1227).** A free-heat bound of the form (6) for the vacuum-normalized *full* \(K_R\) at all box sizes and times fails even with the ordinary Wilson magnetic action. Fix an even spatial side \(n\ge4\), any \(R>1\), and let \(\beta\to\infty\). Take \(u=\lceil\beta^2\rceil\). Row 1227, (10), places one energy in each of the seven nontrivial electric sectors below \(C_n e^{-c_n\sqrt\beta}\). The vacuum and these seven states contribute at least \(1+7\exp[-u C_ne^{-c_n\sqrt\beta}]\) to the full normalized Wilson trace. Its lower limit is at least eight. Equations (1) and (3)–(4) change its log by at most \(u b_R=o(1)\). The right side of (6), with \(T=u\) and \(s=1/(\beta R^2)\), tends to one. The input (10) is the fixed-cube tunnelling bound of row 1227, checked in row 1230, following Lüscher and van Baal's small-volume mechanism. This comparison proves a failure for actual gauge-invariant transfers at fixed spatial lattice side. Its aspect ratios differ from \(T=n/2\), so the physical seed is still undecided. [Tunnelling estimate (10)](gap-solve25-astra62.md) · [Check of (10)](gap-solve25-check-opus.md)

## Can the spatial plaquette interaction be absorbed into the two ends?

**GUIDE.** Take \(0<b\le B<\infty\) and \(b\log n\le\beta\le B\log n\). By (5) one may choose a fixed \(\alpha>0\), as small as needed below, so \(2h\le s_n\) for \(h=\alpha/\beta\). Each electric layer now contains a product heat kernel \(\mathsf H_h=H_h^{\otimes m}\) on either side of the residual convolution. The exact middle factor between residual convolutions is \(\mathsf H_h M^2\mathsf H_h\). On the gauge-invariant space its positive kernel divided by that of \(\mathsf H_{2h}\) is
\[
 F(x,y)=
 \frac{\int dg\,dz\ \mathsf H_h(x,z)e^{-S(z)}
                     \mathsf H_h(z,g y)}
      {\int dg\ \mathsf H_{2h}(x,g y)},\qquad
 S(z)=\beta\sum_{p\ {\rm spatial}}(1-\tfrac12\operatorname{tr}z_p).
                                                                         \tag{7}
\]
Here \((g y)_{uv}=g_u y_{uv}g_v^{-1}\). The commutation of heat flow and \(M^2\) with the gauge action allows the projection to be taken once at the end. In particular \(F(x,y)=F(y,x)>0\). The proposed simplification would give \(F(x,y)\) as a scalar times positive factors of the separate ends, with a controlled log error. A test that cancels arbitrary such factors is
\[
                       \frac{F(x,y)F(y,x)}{F(x,x)F(y,y)} .             \tag{8}
\]
I test it on the flat field \(x_e=1\) and an alternating Abelian field \(y\) with nonzero plaquette curvature, so their vertex-gauge orbits are distinct.

**PROVED (cost of changing frames).** Write \(V=n^3\), choose a unit imaginary quaternion \(I\), let \(\epsilon_v=(-1)^{v_1}\), and set
\[
 o_{v\mu}=1,\qquad y_{v2}=e^{I\epsilon_v\theta},\qquad
 y_{v1}=y_{v3}=1,\qquad \theta=A/\sqrt\beta .                           \tag{9}
\]
The positive number \(A\) will be fixed before \(n\to\infty\). The plaquettes in the \(1,2\) plane have angle \(2\theta\) for small \(\theta\), and all other plaquettes are trivial. Thus \(S(y)=\beta V(1-\cos2\theta)\). For arbitrary vertex frames, using chord distance in \(\mathbb R^4\),
\[
 \sum_{e=uv}|g_u y_e-g_v|^2
 \ge 2V(1-\cos\theta)+(1-C|\theta|)\sum_{e=uv}|g_u-g_v|^2              \tag{10}
\]
when \(|\theta|\le1\), with an absolute constant. To see this, use the skew form \(J(a,b)=\langle aI,b\rangle\) on \(\mathbb R^4\), and set \(j_\mu(v)=J(g_v,g_{v+\hat\mu})\). The direction-2 terms on the left expand to
\[
 2V(1-\cos\theta)+\cos\theta\sum_v |g_v-g_{v+\hat2}|^2
                 -2\sin\theta\sum_v\epsilon_v j_2(v).
\]
The remaining directions have their untwisted costs. Sum the oriented \(12\)-plaquette circulations of \(j\) against \(\epsilon_v\). The result is \(-2\sum_v\epsilon_v j_2(v)\) by periodicity. For successive frames \(a,b,c,d\) on a square the circulation equals \(J(b-a,c-a)+J(c-a,d-a)\). Its absolute value is bounded by a constant times the sum of squared chord lengths on the square, by the triangle inequality and \(2uv\le u^2+v^2\). Each spatial edge belongs to at most two such squares. The signed sum therefore costs at most \(C\sum_e|g_u-g_v|^2\). This proves (10) for the complete gauge average, including large changes of frame.

**PROVED (heat-kernel estimates used below).** Write \(d\) for round geodesic distance, \(0<t<t_0\) for some fixed small \(t_0\), and \(0<\delta<1/2\). With constants independent of the endpoints,
\[
 \begin{split}
  c t^{-3/2}e^{-d^2/(2t)}\le H_t(d)\le C t^{-3/2}e^{-d^2/(2t)}
                      &\quad(d\le\pi/2),\\
  H_t(d)\le C_\delta t^{-3/2}e^{-(1-\delta)d^2/(2t)}
                      &\quad(0\le d\le\pi).
 \end{split}                                                            \tag{11}
\]
For the proof, multiply the heat character series by \(\sin d\). Apart from \(e^{t/2}\) it is \(\sum_{k\ge1} k e^{-k^2t/2}\sin(kd)\). This is minus one half of the derivative of the periodic Gaussian Fourier series. Periodizing the real Gaussian, whose Fourier coefficients are given by its Gaussian integral, writes \(H_t(d)\) as a fixed positive constant times
\[
  \frac{e^{t/2}t^{-3/2}}{\sin d}
                  \sum_{j\in\mathbb Z}(d+2\pi j)e^{-(d+2\pi j)^2/(2t)} .
\]
For \(d\le\pi/2\) group \(j\) and \(-j\) for \(j\ge1\). By the mean value theorem their total absolute contribution is bounded by \(C d(1+t^{-1})e^{-(3\pi/2)^2/(2t)}\), summing the further Gaussian tails. It is smaller than half the \(j=0\) term uniformly for small \(t\), with the ratio at \(d=0\) taken by continuity. For \(\pi/2\le d\le\pi\), put \(u=\pi-d\) and pair the terms at \((2j+1)\pi\pm u\) with opposite signs. The derivative bound for \(v e^{-v^2/(2t)}\) gives a sum bounded by \(C u(1+t^{-1})e^{-d^2/(2t)}\). Now \(\sin d\ge2u/\pi\), and \(C_\delta e^{\delta d^2/(2t)}\) absorbs \(1+t^{-1}\). This proves (11), with endpoint limits included.

**PROVED.** A spherical bridge with two successive steps of time \(h\) and endpoints at distance \(d\le\pi/4\) puts probability at least \(c>0\) in the ball of radius \(\sqrt h\) about their geodesic midpoint. The sum of squared distances to the ends has value \(d^2/2\) and zero gradient there. Its Hessian on that ball is bounded uniformly, since squared distance is smooth at distances below \(\pi/2\) and the sphere is compact. Taylor's formula bounds the sum by \(d^2/2+Ch\). Apply the local lower estimate in (11) on the ball and its local upper estimate to the denominator \(H_{2h}(d)\). The normalized Haar volume of the ball is at least \(c h^{3/2}\), by the radial density proportional to \(\sin^2 d\). This gives the asserted probability.

**PROVED (the equal-end upper bound).** Choose \(0<\alpha\le1/512\), also small enough for \(2h\le s_n\). For every assignment \(y\) of spatial links and all sufficiently small \(h=\alpha/\beta\),
\[
                         F(y,y)\le C^V h^{-3/2}e^{-7S(y)/8}.            \tag{12}
\]
For each plaquette the chord difference of two holonomies is at most the sum of the four chord differences of its links, by telescoping products of unit quaternions. Each spatial link occurs four times. The \(\ell^2\) norm of all the plaquette differences is therefore at most four times the \(\ell^2\) norm of the link differences. The identity \(1-\tfrac12\operatorname{tr}u=|1-u|^2/2\) and Young's inequality give
\[
 S(z)\ge(1-\eta)S(y)-\frac{8\beta}{\eta}\sum_e d(z_e,y_e)^2
 \quad(0<\eta<1).
\]
Take \(\eta=1/8\). In the numerator of (7) absorb the last exponential into the first heat kernel. This works because the upper bound (11) with \(\delta=1/4\) has coefficient \(3/(8h)\), and \(64\beta\le1/(8h)\). For each edge, integration of the two remaining Gaussians is at most
\(C h^{-3/2}\exp[-c\,d(y_e,(g y)_e)^2/h]\). Indeed half of the sum of the two squared distances bounds a positive multiple of the squared endpoint distance, and the remaining Gaussian has Haar integral at most \(C h^{3/2}\). Keep the frame exponentials on a spanning tree, dropping the others to upper bound their product. Integrate leaf frames successively. With the parent fixed the leaf has a Haar Gaussian about one group element and costs at most \(C h^{3/2}\). The numerator is bounded by
\[
 e^{-7S(y)/8}(C h^{-3/2})^m(C h^{3/2})^{V-1}.
\]
In the denominator take every frame within \(\sqrt h\) of the identity. This has volume at least \((c h^{3/2})^V\) and gives \(d(y_e,(g y)_e)\le2\sqrt h\). The product of the local lower bounds in (11) is at least \((c h^{-3/2})^m\). Division proves (12).

**PROVED (the unequal-end lower bound).** For (9), \(h=\alpha/\beta\), fixed \(\alpha,A\), and every \(0<\delta<1/4\),
\[
 \liminf_{n\to\infty}\frac{1}{V}\log F(o,y)
 \ \ge\ -\frac{A^2}{2}-\frac{\delta A^2}{4\alpha}
               -C_\alpha A-C_{\alpha,\delta}.                          \tag{13}
\]
The constants can be chosen independently of \(A\). First use the global bound (11) at time \(2h\) in the denominator of (7). Geodesic distance dominates chord distance. Estimate (10) and \(1-C|\theta|\ge1/2\) for all sufficiently large \(n\) give the upper bound
\[
 (C_\delta h^{-3/2})^m(C h^{3/2})^{V-1}
                  \exp[-(1-\delta)2V(1-\cos\theta)/(4h)] .
\]
The frame integral was bounded on a spanning tree, this time using the chord metric. The Haar Gaussian integral is still \(O(h^{3/2})\) because chord and geodesic distances on the round sphere are comparable.

**PROVED.** In the numerator restrict every frame to the \(\sqrt h\) ball at the identity. Then \((g y)_e\) differs from \(y_e\) by distance at most \(2\sqrt h\). All endpoint distances from \(o_e\) are below \(\pi/4\) eventually. Their squared sum is bounded by \(V(\theta^2+4\theta\sqrt h+12h)\). Given the frames, write the two heat factors as the product of the endpoint kernel at time \(2h\) and the conditional bridge law. The midpoint bound after (11), independently on each link, puts all middle links within \(C\sqrt h\) of \(y_e^{1/2}\) at cost at most \(c^{-m}\) in reciprocal probability. Here the single-link geodesic midpoint from \(1\) is its endpoint's principal square root, Lipschitz in a fixed neighbourhood of \(1\). At the field \(y^{1/2}\) the \(12\)-plaquettes have angle \(\theta\) and the others are trivial. The plaquette chord inequality from (12) now gives
\[
                   S(z)\le V\big[A^2/2+C A\sqrt\alpha+C\alpha\big].
\]
The numerator is at least
\[
 (c h^{3/2})^V(c h^{-3/2})^m
 \exp\!\left[-\frac{V(\theta^2+4\theta\sqrt h+12h)}{4h}
              -V(A^2/2+C A\sqrt\alpha+C\alpha)\right].
\]
After division the leading electric cost cancels up to
\(\{\theta^2-(1-\delta)2(1-\cos\theta)\}/(4h)
=\delta A^2/(4\alpha)+o(1)\) per site. The term \(\theta/\sqrt h=A/\sqrt\alpha\) is linear in \(A\) at fixed \(\alpha\). Finally \(|\log h|/V\to0\) on the stated schedules. This proves (13).

**PROVED (failure of separate boundary factors on physical cubes).** There are \(\alpha>0\), \(A<\infty\) and \(c_*>0\) such that on every sufficiently fine cube in the schedule above,
\[
                  \frac{F(o,y)F(y,o)}{F(o,o)F(y,y)}
                              \ \ge\ \exp(c_* n^3).                    \tag{14}
\]
Indeed \(F(o,o)\le1\), and \(S(y)/V=\beta(1-\cos2\theta)\to2A^2\). By (12) and (13), the lower limit of the log ratio per site is at least
\[
            \left(\tfrac34-\frac{\delta}{2\alpha}\right)A^2
                    -C_\alpha' A-C_{\alpha,\delta}' .
\]
Choose \(\alpha\) first as above, then \(\delta=\alpha/4\), then \(A\) sufficiently large, and take \(c_*\) smaller than the positive lower bound. The four slice pairs are gauge invariant in (7), and all classical plaquette angles of their endpoints tend to zero. For any positive functions \(a(x),b(y)\), the alternating sum of \(\log[a(x)b(y)]\) over these pairs vanishes. Consequently at least one of the four values of \(|\log F(x,y)-\log[a(x)b(y)]|\) is at least \(c_*n^3/4\). A normalization depending on the whole lattice can be included in \(a\). This tests the actual magnetic insertion in the split transfer, before the residual convolutions on either side are integrated.

## Keeping only slices of bounded magnetic action density

**PROVED (a thermal restriction, using the marked-plaquette pressure bound).** For each \(\varepsilon>0\) and \(p>0\), choose \(\alpha>0\) sufficiently small in the split above. There is \(K_\varepsilon(p)<\infty\) with the following property on the physical schedules of (7). At every original slice and at both inserted heat endpoints of every step, retain only fields satisfying
\[
  S_B(z):=\beta\sum_{\substack{v\in B\\1\le i<j\le3}}
              (1-\tfrac12\operatorname{tr}z_{v,ij})
           \le(9/4+\varepsilon)|B|
 \quad\text{for every translated spatial cube }B
          \text{ with } K_\varepsilon(p)\log n\le |B|\le V .              \tag{15}
\]
Cubes are sets of base vertices on the spatial torus, with side at most \(n\). Imposing (15) changes each of the log partition functions of \(K_R\) at \(T,2T\) by \(O(n^{-p})\). Consequently the two-period defect computed on these restricted integrals differs by \(O(n^{-p})\) from the original Wilson defect.

**PROVED.** For original Wilson slices use row 1151, (21), (22a), at a fixed small positive tilt \(u_0\) for one plaquette orientation. In its notation the log moment of \(u_0 S_{B,ij}\) is at most \(|B|[p_V(u_0)-p_V(0)]\), where \(S_{B,ij}\) is the contribution of orientation \(ij\). The slope estimate there is \(3/4+O(u_0+\beta^{-\eta_0})\) throughout the tilt interval, for a fixed sufficiently small \(\eta_0>0\). Select \(u_0\) small depending on \(\varepsilon\), then take \(n\) large. Exponential Markov and a union over the three spatial orientations give
\[
  \Pr_{\rm Wilson}\{S_B(z)>(9/4+\varepsilon/2)|B|\}
             \le 3e^{-c_\varepsilon|B|}.
\]
This uses the estimate on the two homogeneous rectangles at their actual coupling. Chatterjee's open-box method supplies the pressure comparison in row 1151. On the original link fields of the split \(K_R\) integral, probabilities are bounded by \(e^{u b_R}\) times the Wilson probabilities at period \(u\), by pointwise domination and (3). [Marked-plaquette estimate](gap-solve5-astra62.md) · [Check of (21)–(22b)](gap-solve5-check-opus.md)

**PROVED.** On an individual half-step, write \(z\) for the original field and \(x\) for its adjacent inserted endpoint, in the common temporal frame of that heat convolution. For every set \(I\) of spatial edges, in the full split thermal integral,
\[
        \mathbb E_{R,u}\exp\!\left(\sum_{e\in I}
                       \frac{d(x_e,z_e)^2}{16h}\right)\le C_0^{|I|}.
                                                                         \tag{16}
\]
Indeed \(e^{d^2/(16h)}H_h(d)\le C_0 H_{2h}(d)\) pointwise. For the needed global lower estimate at time \(2h\), the periodized formula in (11) suffices. At \(d=\pi-w\ge\pi/2\) the first paired difference with \(f(v)=v e^{-v^2/(2t)}\) is \(f(d)-f(d+2w)\ge f(d)(1-e^{-dw/t})\) for sufficiently small \(t\), since \(1+2w/d\le e^{dw/t}\). Dividing by \(\sin d\le w\) bounds this below by \(c e^{-d^2/(2t)}\), and the subsequent pairs are nonnegative by monotonicity on \([\pi/2,\infty)\). Use (11) on the other half of the range. The upper estimate (11) with \(\delta=1/4\) now proves the claimed comparison. Lengthening the heat step on \(I\) multiplies the electric convolution of that layer by an additional commuting heat semigroup. Its multipliers on every product harmonic lie in \([0,1]\), and those of the original convolution are nonnegative. The changed magnetic sandwich is therefore below \(K_R\) in quadratic-form order. Only one layer has changed, so its trace against \(K_R^{u-1}\) is no larger than \(Z_R(u)\). This last argument is on the full physical space. It proves (16) without estimating a vacuum wavefunction.

**PROVED.** The plaquettes based in \(B\) use an edge set \(I\) of size at most \(12|B|\). With probability at least \(1-e^{-|B|}\), (16) gives \(\sum_{e\in I} d(x_e,z_e)^2\le C_1 h |B|\), taking \(C_1=16(12\log C_0+1)\) with \(C_0\ge1\). On this event the chord inequality of (12) gives
\[
 \sqrt{S_B(x)/|B|}\le \sqrt{S_B(z)/|B|}+\sqrt{8C_1\alpha}.
\]
Choose positive \(\alpha\) so that \(\sqrt{9/4+\varepsilon/2}+\sqrt{8C_1\alpha}\le\sqrt{9/4+\varepsilon}\). The exceptional probability for a specified cube and slice is at most \(3e^{u b_R-c_\varepsilon |B|}+e^{-|B|}\). There are at most \(n^4\) such cubes and at most \(3u\) slice positions. Taking \(K_\varepsilon(p)\) with \(K_\varepsilon(p)\min(1,c_\varepsilon)>6+p\) proves the log estimate at each period. Equivalently let \(Q\) multiply by the indicator in (15), and let \(\mathsf D\) be the residual product convolution after splitting off the two heat factors. The restricted positive transfer is
\[
          K_{\rm res}=Q M\mathsf H_h Q\mathsf D Q\mathsf H_h M Q .
\]
Its \(u\)-th trace integrates exactly the retained paths, since \(Q^2=Q\). This construction preserves the gauge and centre symmetries.

**GUIDE.** The large value of \(A\) in (14) can put \(y\) outside (15). To test the proposed simplification on the retained set itself, one needs the mixed magnetic cost for bounded \(A\). A sharper estimate follows by keeping the same leading electric cost in both frame integrals.

## Testing the estimate after the thermal restriction

**PROVED (a field in the restricted set).** In (7) write \(F_Q\) for the same ratio with \({\bf1}_{(15)}(z)\) inserted in the numerator. Take both ends in (15). This is the magnetic factor in the restricted transfer just constructed. Use \(A=1\) and replace (9) by the following field, which is invariant under every spatial reflection through a site plane.
\[
 \sigma_v=(-1)^{v_1+v_2},\qquad \vartheta=\frac{1}{2\sqrt\beta},\qquad
 y'_{v1}=e^{ I\sigma_v\vartheta},\qquad
 y'_{v2}=e^{-I\sigma_v\vartheta},\qquad y'_{v3}=1.                    \tag{17}
\]
Reversing a marked link reverses its orientation and the sign at its new base vertex. A \(12\)-plaquette has angle \(4\vartheta\), and the \(13\) and \(23\) plaquettes are trivial. For every spatial cube, including one vertex, \(S_B(y')/|B|=\beta(1-\cos4\vartheta)\le2\). For the field \(w_e=(y'_e)^{1/2}\) the same bound is \(1/2\), using \(1-\cos v\le v^2/2\). Thus \(o,y'\) both obey (15) for every \(\varepsilon>0\).

**PROVED (frame fluctuations of the mixed heat bridge).** Give frames density proportional to \(\mathsf H_{2h}(o,g y')\). Put \(E(g)=\sum_{e=uv}|g_u-g_v|^2\), and \(B_\theta=4V(1-\cos\vartheta)\). For some absolute \(k,c,C>0\), at each fixed sufficiently small \(\alpha>0\) and all sufficiently large \(n\),
\[
 \log\mathbb E e^{kE(g)/h}\le CV,\qquad
                      \mathbb E E(g)\le C h V .                         \tag{18}
\]
Both bounds are uniform in the subsequent choice of small \(\alpha\) in the sense that their constants are absolute and their starting \(n\) may depend on \(\alpha\). For (17) the current in (10) is now \(\sum_v\sigma_v[j_1(v)-j_2(v)]\). Twice this sum is the signed sum of the \(12\)-plaquette circulations because translation by one in either direction reverses \(\sigma\). The same area estimate proves *both* chord bounds
\[
 B_\theta+(1-C\vartheta)E(g)\ \le\
     \sum_e |1-(g y')_e|^2\ \le\ B_\theta+(1+C\vartheta)E(g).
                                                                         \tag{19}
\]

**PROVED.** To upper bound the frame density, use the local upper bound of (11) with its exact exponent whenever \(d(1,(g y')_e)\le\pi/2\). On any other edge, \(d(g_u,g_v)\ge\pi/2-\vartheta\), so the loss \(\delta\,d(1,(g y')_e)^2\) from the global bound costs at most \(C\delta |g_u-g_v|^2\). Fix a sufficiently small absolute \(\delta\). The lower bound of (19) and geodesic domination of the chord then give
\[
             \mathsf H_{2h}(o,g y')\le
       (C h^{-3/2})^m\exp[-B_\theta/(4h)-c E(g)/h].
\]
Multiplying by \(e^{kE(g)/h}\) for \(k<c/2\) still allows spanning-tree integration, at cost at most \((C h^{3/2})^{V-1}\). For a lower bound on the normalizer take every \(g_v\) within \(\sqrt h\) of 1. Then \(E(g)\le C hV\), and the endpoint angles are \(O(\vartheta+\sqrt h)\). The difference between squared geodesic and squared chord distance on each edge is \(O((\vartheta+\sqrt h)^4)\). Its ratio to \(h\) tends to zero at fixed \(\alpha\). By the *upper* side of (19), the sum of squared geodesic distances is at most \(B_\theta+ChV\). The original frame normalizer is therefore at least
\[
              (c h^{-3/2})^m(c h^{3/2})^V e^{-B_\theta/(4h)}.
\]
After division only \(e^{CV}h^{-3/2}\) remains. Absorb \(|\log h|=o(V)\) into the constant and use Jensen. This proves (18).

**PROVED (where the middle links lie).** Under the free, gauge-averaged, two-step heat bridge from \(o\) to \(y'\), before the magnetic insertion, let \(z\) be its middle slice. Then
\[
                \sum_e\mathbb E d(z_e,(g w)_e)^2\le C hV.              \tag{20}
\]
For endpoints at distance \(d\le\pi/4\) the spherical bridge has mean squared distance at most \(Ch\) from their geodesic midpoint \(b\). To check its tail, \(d(a,z)^2+d(z,a')^2-d^2/2\ge c\,d(z,b)^2\) uniformly for such endpoints. In the ball of radius \(\pi/4\) about \(b\), the Hessian of squared distance to either endpoint has a uniform positive lower bound. The radial and tangential eigenvalues for one half the squared distance in polar coordinates are \(1\) and \(r\cot r\), and \(r\le3\pi/8\). Outside that ball compactness gives the bound, since equality in the triangle and square inequalities requires the unique midpoint. Use the exact exponents of (11) where both distances are at most \(\pi/2\). Else \(d(z,b)\) is bounded below, so a sufficiently small fixed \(\delta\) in (11) costs at most half the positive excess. Divide by the local lower bound for \(H_{2h}(d)\). The resulting density is at most \(C h^{-3/2}\exp[-c\,d(z,b)^2/h]\), proving the moment bound.

**PROVED.** On edges with \(d(1,(g y')_e)\le\pi/4\), their midpoint is within \(C\,d(g_u,g_v)\) of \(g_u w_e g_u^{-1}\), by the Lipschitz property of the principal square root there. Changing that last frame to \(g_v^{-1}\) costs at most another \(d(g_u,g_v)\). On other edges the trivial distance bound \(\pi\) costs at most \(C|g_u-g_v|\), since \(\vartheta\to0\). Conditioning on \(g\), summing the squared estimates, and using (18) proves (20). By translations of period two in each coordinate, each individual edge expectation in (20) is \(O(h)\). Each edge type has at least \(V/8\) translates with the same expectation.

**PROVED (cost of keeping the intermediate field).** Put \(\zeta=\alpha^{1/4}\). For all sufficiently small fixed \(\alpha>0\), the probability under this mixed free bridge that
\[
                d(z_e,(g w)_e)\le\zeta/\sqrt\beta
                      \quad\hbox{on every edge}                         \tag{21}
\]
is at least \(\exp[-C\sqrt\alpha\, V]\) for all sufficiently large \(n\). A side-two closed cube has a bounded number of edges. Markov's inequality and (20) give probability at least \(1-C\alpha/\zeta^2\) that all its edges pass. To extend this estimate, use the finite reflection argument AM6 of Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. Here the joint law of \(g,z\) before normalization has one factor \(H_h(1,z_e) H_h(z_e,(g y')_e)\) per edge. A site reflection preserves the factors, with reversed links inverted. Condition on all frames and tangential links on two opposite site planes. The remaining weights and Haar integrals factor into reflected halves. A boundary weight is positive and can be divided into its two square roots. Cauchy–Schwarz therefore gives the reflection inequality, including tests on shared boundary variables. The edge test in (21) also reflects into itself because \(w\) has the same reflection symmetries as \(y'\). [Finite chessboard proof, outline lines 2885–2939](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L2885-L2939)

**PROVED.** In one direction use the \(n/2\) slabs of width two. For any filling by the test and by ones, divide its expectation by the product of the corresponding fully repeated expectations to power \(2/n\), one factor per slot. Reflection bounds the square of the normalized value by the product for the two reflected fillings. A maximizing filling with a constant run gives another maximizing filling with this run doubled by reflecting at its start, or a constant filling if the run covers a semicircle. The constant fillings have value one. This proves the one-direction inequality, first for strictly positive tests and then by adding a positive constant to the indicator and taking its limit. Use a single occupied slot and repeat in the other two directions. The fully repeated probability is at least the single-cube probability to power \((n/2)^3\). Closed tiles cover every edge, so the repeated event is (21). This proves the exponential lower bound without assuming independence of the tiles.

**PROVED.** On (21), apply the plaquette chord inequality on any \(B\) to \(z\) and the gauge transform \(g w\). There are at most \(12|B|\) edges and \(S_B(g w)=S_B(w)\). Thus
\[
              \sqrt{S_B(z)/|B|}\le 1/\sqrt2+\sqrt{96}\,\zeta .
\]
Choose \(\alpha\) small so the square of this bound is below \(9/4+\varepsilon\). Every middle field in (21) passes (15), and its total magnetic action per site is at most \(1/2+C\alpha^{1/4}\) for \(\alpha\le1\). Integrating the magnetic weight on this event gives
\[
                     F_Q(o,y')\ge e^{-V(1/2+C\alpha^{1/4})}.           \tag{22}
\]

**PROVED (equal endpoints at bounded action).** In the *free* gauge-averaged bridge from \(y\) to \(y\), the proof of (12) also gives
\[
           \log\mathbb E\exp\!\left[\frac1{16h}
                          \sum_e d(z_e,y_e)^2\right]\le CV             \tag{23}
\]
for every \(y\) and all sufficiently large \(n\) on this schedule. To obtain it, use just the displayed insertion in the numerator of (7) in place of \(e^{-S(z)}\). The first Gaussian still has coefficient at least \(1/(4h)\). The same edge integration, spanning tree and denominator used in (12) give \(C^Vh^{-3/2}\). This proves (23) with an absolute \(C\) after taking logs. With \(\eta=\sqrt\alpha\), choose \(\alpha\) small enough that \(8\alpha/\eta\le1/16\). Convexity of the log moment between zero and the exponent in (23) bounds the cost of the Young inequality in (12) by \(C\sqrt\alpha V\). Dropping the middle restriction for the upper bound gives
\[
           F_Q(y,y)\le \exp[-(1-\sqrt\alpha)S(y)+C\sqrt\alpha V].
                                                                         \tag{24}
\]

**PROVED (obstruction inside the restricted integral).** For every \(\varepsilon,p>0\) one can choose \(\alpha>0\) small and \(K_\varepsilon(p)\) as in (15) such that for all sufficiently large \(n\),
\[
      \log\frac{F_Q(o,y')F_Q(y',o)}{F_Q(o,o)F_Q(y',y')}
                                     \ \ge\ \tfrac12 n^3.               \tag{25}
\]
The two end fields obey (15), and the middle indicator is present. Equation (22) bounds the numerator. For the denominator \(F_Q(o,o)\le1\) and \(S(y')/V\to2\), so (24) gives a lower limit for the log ratio per site of \(1-C\alpha^{1/4}\). Choose \(\alpha\) in the stated order. The conclusion also follows at every smaller fixed \(\alpha\) after adjusting the starting \(n\). Thus even after the action restriction changes the two thermal log integrals by only \(O(n^{-p})\), any description of this middle kernel by the free projected heat kernel times positive separate endpoint factors has log error at least \(n^3/8\) at one of the four pairs. This is a pointwise conclusion about the restricted kernel. It places no lower bound on the thermal probability of those four pairs.

## Fixing the energy window in each orientation

**PROVED (two-sided restriction on both thermal periods).** One may replace (15) by the three simultaneous tests
\[
 \left|S_{B,ij}(z)/|B|-3/4\right|\le\varepsilon,
      \qquad 1\le i<j\le3,\qquad |B|\ge K_\varepsilon(p)\log n,         \tag{26}
\]
on every original and inserted slice, with the same \(O(n^{-p})\) conclusion after choosing \(\alpha\) smaller and \(K_\varepsilon(p)\) larger if needed. For the lower tail on an original slice, use the dissemination proof of row 1151, (21), with a negative tilt. The altered plaquette coupling then increases and remains positive. In each coordinate the layer trace Hölder inequality applies to the same positive operators as for a positive tilt, so the same upper log moment bound holds. Integrate (22a) between this negative tilt and zero, then apply exponential Markov to \(-S_{B,ij}\). This gives both tails at half the tolerance. For each orientation the chord inequality used after (16) in fact bounds the absolute difference of the two square roots. The target \(3/4\) is positive. Choose \(\alpha\) so the resulting square-root error \(\sqrt{8C_1\alpha}\) fits between the inner and outer tolerances. One can decrease \(\varepsilon\) first if it exceeds \(1/4\). The same union bound proves (26).

**PROVED (fields in all three windows).** Write \(Q_\varepsilon\) for (26). The two configurations in (25) violate its lower bounds in some orientations. To test this stronger restriction, use a one-parameter family of fields that has constant plaquette action in all three orientations. Set \(\kappa=\sqrt{3/32}\). For \(i\ne j\) let \(c_{12}=c_{23}=c_{31}=1\), \(c_{ji}=-c_{ij}\), and put
\[
 a_{vi}=\frac{\kappa}{\sqrt\beta}
             \sum_{j\ne i}c_{ij}(-1)^{v_i+v_j},
              \qquad U(t)_{vi}=\exp(I t a_{vi}).                       \tag{27}
\]
Every nonzero \(|a_e|\) equals \(2\kappa/\sqrt\beta\). The phases commute. On an \(ij\)-plaquette only the \(ij\) summand of the phases survives the difference, and it gives absolute angle \(4t\kappa/\sqrt\beta\) for bounded positive \(t\) and large \(\beta\). Thus every single plaquette action tends to \(3t^2/4\), uniformly on the whole cube. Site reflections preserve the field with the usual orientation convention. Choose a fixed \(0<d<1/8\) so small that \(|3(1\pm d)^2/4-3/4|<\varepsilon/2\). Set \(x=U(1-d)\), \(y=U(1+d)\), \(w=U(1)\). Both ends pass (26) for all sufficiently large \(n\).

**PROVED (relative colour frames in the mixed kernel).** Under the free gauge-averaged heat bridge from \(x\) to \(y\) in (27), its middle field satisfies
\[
                          \sum_e\mathbb E d_{\rm geo}(z_e,w_e)^2
                                     \le C h V.                          \tag{28}
\]
Here \(d_{\rm geo}\) denotes the round distance denoted by \(d\) in (11), to distinguish it from the fixed amplitude difference. The constants below are absolute for \(0<d<1/8\). Write each unit frame \(g_v=p_v+q_v J\), with \(p_v,q_v\) complex in the circle plane of \(I\) and \(JI=-IJ\). The squared chord cost on \(e=uv\) is
\[
  |g_u y_e-x_e g_v|^2
     =|e^{2Id a_e}p_u-p_v|^2+|e^{-2I a_e}q_u-q_v|^2 .
\]
For \(k=2d,-2\), expansion of a complex summand gives
\(\cos(k a_e)|b_u-b_v|^2+(1-\cos(k a_e))(|b_u|^2+|b_v|^2)\) plus a signed current term \(2\sin(k a_e)\operatorname{Im}(\overline b_u b_v)\), with the sign fixed by the orientation convention. The sum of the current terms is \(O(\beta^{-1/2}\sum_e|b_u-b_v|^2)\). Indeed \(\sin(k a_e)\) is a scalar multiple of \(a_e\) with multiplier of modulus at most two, since all its nonzero absolute arguments have the same size. For each pair \(ij\) the weighted difference of the \(i,j\) currents equals one half of their signed plaquette circulation sum as in (18). Its area bound uses only differences and also holds for a complex field \(b\) of nonconstant modulus.

**PROVED.** Define
\[
 B_0=2\sum_e(1-\cos(2d a_e)),\qquad
 G(g)=E(g)+\sum_{e=uv} a_e^2(|q_u|^2+|q_v|^2).
\]
After pulling out \(B_0\) using \(|p_v|^2+|q_v|^2=1\), the remaining coefficient of \(|q_u|^2+|q_v|^2\) is \(\cos(2d a_e)-\cos(2a_e)\), bounded between \(c a_e^2\) and \(C a_e^2\) for all large \(n\). The gradient coefficients tend to one. The summed chord cost consequently lies between \(B_0+cG(g)\) and \(B_0+CG(g)\). These two bounds give \(\log\mathbb E e^{k G(g)/h}\le C V\) for a small absolute \(k>0\). In detail, for edges with \(d_{\rm geo}(x_e,(g y)_e)>\pi/2\) the frame-gradient chord is bounded below by an absolute constant, since both end fields are uniformly close to the identity. The loss from the global heat upper bound is absorbed in a fraction of \(E(g)/h\), just as in (18). Take out \(e^{-B_0/(4h)}\) and integrate a remaining spanning-tree Gaussian. For the matching lower normalizer take all frames within \(\sqrt h\) of the identity. There \(G(g)\le C h V\), since \(|q_v|\le C\sqrt h\), and the quartic distance error divided by \(h\) is \(o(1)\) per edge. This cancels the same \(B_0\) and proves the log moment bound. In particular \(\mathbb E G(g)\le C hV\).

**PROVED.** Conjugating \(y_e\) by \(g_u\) changes it by chord distance \(2|\sin((1+d)a_e)|\,|q_u|\), by quaternion multiplication. The change from \(g_u^{-1}\) to \(g_v^{-1}\) costs at most the frame-gradient distance. Thus \(d_{\rm geo}((g y)_e,y_e)\le C(d_{\rm geo}(g_u,g_v)+|a_e|\,|q_u|)\). The geodesic midpoint of \(x_e,y_e\) is exactly \(w_e\). If the bridge endpoints are at distance at most \(\pi/4\), use the midpoint second-moment and Lipschitz estimates from (20). Else the frame-gradient chord is bounded below and pays for the trivial distance bound. Sum and use the estimate on \(\mathbb E G\). This proves (28), including the possible noncommuting frame rotations.

**PROVED (failure even in the three two-sided windows).** Fix \(\varepsilon>0\), \(p>0\), \(b,B\) as in (7), and the amplitude \(d\) just chosen. For sufficiently small fixed \(\alpha>0\), at all sufficiently large \(n\),
\[
   \log\frac{F_{Q_\varepsilon}(x,y)F_{Q_\varepsilon}(y,x)}
                {F_{Q_\varepsilon}(x,x)F_{Q_\varepsilon}(y,y)}
                                     \ \ge d^2 n^3 .                     \tag{29}
\]
It holds also when each \(F_{Q_\varepsilon}\) is defined by dividing the magnetic bridge integral by the *free bridge integral with the same middle restriction*.

**PROVED.** Period-two translations, (28) and Markov's inequality imply that the probability of every edge on a side-two tile lying within \(\zeta/\sqrt\beta\) of \(w_e\) is at least \(1-C\alpha/\zeta^2\), where \(\zeta=\alpha^{1/4}\). The joint law with edge factors \(H_h(x_e,z_e)H_h(z_e,(g y)_e)\) and the new test have precisely the site reflection property used for (21). Dissemination gives probability at least \(e^{-C\sqrt\alpha V}\) of this event on all edges. There, on *each* plaquette, the square root of its action differs from that of \(w\) by at most \(4\zeta/\sqrt2\), by the chord inequality. The reference value tends to \(\sqrt{3/4}\). For small enough \(\alpha\) and large \(n\) every plaquette passes the corresponding energy window, so (26) holds on all its cubes. Moreover \(S(z)/V\le9/4+C\zeta+o(1)\). Hence
\[
 \liminf_n V^{-1}\log F_{Q_\varepsilon}(x,y)\ge-9/4-C\alpha^{1/4}.
\]
The equal-end upper bound (24) applies at either end with any middle restriction. Their two limiting actions per site sum to
\((9/4)[(1-d)^2+(1+d)^2]\). Since the kernel ratio is symmetric, this gives a lower limit for the log ratio per site of at least \(9d^2/2-C\alpha^{1/4}\).

**PROVED.** For the second choice of denominator, dividing by the conditional probability of the free middle restriction can only increase the mixed-end lower bound. At each equal-end bridge, (23) and Jensen give \(\sum_e\mathbb E d_{\rm geo}(z_e,x_e)^2\le C h V\) or the same with \(y_e\). Translate and disseminate the tile test about its own end field as before. Each end has a margin of at least \(\varepsilon/2-o(1)\) in the plaquette windows. For small \(\alpha\) the event again implies (26), with probability at least \(e^{-C\sqrt\alpha V}\). Division therefore increases each equal-end upper bound by a log cost at most \(C\sqrt\alpha V\). First fix the window and \(d>0\), then choose \(\alpha\) so both lower limits exceed \(d^2\). This proves (29). For either normalization, any positive factors depending on the individual end fields have log error at least \(d^2 n^3/4\) at one of these four retained pairs. The nonzero effect uses curvatures with specified relative orientations. Even an accurate bound on every single orientation's average action allows these pairs.

## The remaining physical estimate

**PROVED (conditional implication).** Let \(K_{\varepsilon,n}\) denote the restricted transfer following (16), with \(Q_\varepsilon\) from (26) and the choices above. Use all electric sectors. At \(T=n/2\), the log of
\[
       \frac{(\operatorname{Tr}K_{\varepsilon,n}^{T})^2}
            {\operatorname{Tr}K_{\varepsilon,n}^{2T}}                   \tag{30}
\]
differs from \(\Psi(T)\) of the isotropic Wilson transfer by \(O(n^{-p})\). This follows from (3), (5) and the probability estimates for (26), separately at the two periods. For \(U=K/\lambda_0\), \(\operatorname{Tr}U^{2T}\le\operatorname{Tr}U^T\), so \(\log\operatorname{Tr}U^T\le\Psi(T)\). On the admissible dyadic physical sizes and cutoff sequences of Theorem ZD-c, a limiting upper bound strictly below \(1651/1650\) for (30) at one fixed \(L\) would give its two-stage thermal seed. This implication reuses ZD-c with its stated hypotheses.

**OPEN.** I have no bound at that threshold for (30). In the split integral, the middle kernel (7) is averaged against the adjacent residual convolutions and all the other layers. Estimate (29) rules out a uniform approximation by separate endpoint factors at subextensive log error, even in the three restricted windows. To decide (30) one needs a comparison of the *integrated* weights in the \(T\) and \(2T\) ensembles to order one. The four kernel evaluations in (29) give no estimate of their probability under those ensembles. The nontrivial continuum Yang–Mills construction on the full observable space and the positive physical spectral threshold both remain open in this note. All derivations above are by hand and await independent checking.

RESULT — OPEN. On the stated logarithmic coupling schedules, a common angular diffusion time and the three local plaquette-action windows preserve the full Wilson two-period thermal defect up to \(O(n^{-p})\) for any prescribed \(p>0\). Even within those windows the magnetic kernel fails the separate-endpoint comparison (29). The required bound on the averaged ratio (30), the continuum construction and the four-dimensional SU(2) Jaffe–Witten mass gap remain unproved here.
