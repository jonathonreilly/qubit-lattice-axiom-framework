## Repo search

**GUIDE.** FINISH row 1325, at `d77e647078275c98155d3f1e66ad9e706e212dde`. The lead's November 8 search covered main and PRs 10114, 10133, 10134 and 10141. It identifies an older one-step plaquette witness and distinguishes the ultraviolet estimates from the physical spectral question. There is no row-specific prior file at this pin. Row 1323 gives two cuts with the same Wilson thermal defect and different Gaussian predictions. Row 1324 assigns a check, but its report is absent here. [Lead's search](prior/repo-search-2026-11-08.md) · [Row 1323](gap-solve39-astra62.md)

**GUIDE.** On main at `8b11ae2bb9`, Theorem ZD-c gives a sufficient physical seed on a cube. On PR 10114, `MASS_GAP_LOCAL_BLOCK_ASTRA.md`, lines 4–14 and 106–149, gives a one-step plaquette witness. It proves contraction for positive bare coupling at most 1/32. Grok's PR 10133 leaves both CW and MG2 open in `MASS_GAP_CROSSOVER_REDUCTION.md`, lines 77–90. PR 10134, `mass-gap-interface.md`, I1–I5, separates a positive threshold from nontriviality and identification. PR 10141, `fp1.md`, lines 299–315, concerns a one-scale classical minimizer. The registry assigns the component-limit input TP1-LIMIT separately. I found no assignment there for the temporal-cut comparison below. [Physical seed](gap-phys-seed.md) · [Part formulation](../parts/gap.md)

## Sources and choice of attack

**GUIDE.** Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, supply the exact-curvature projection and the Wilson transfer formulas. The outline gives these at lines 1735–1762, 2195–2229 and 2315–2335. Its lines 581–599 distinguish scalar reconstruction and polynomial clustering from the required spectral exclusion. At lines 32487–32488 the authors explicitly separate “any mass-gap estimate” from their construction. CA-I lines 2704–2712 and 3213–3222 state the limits of Theorem 0 explicitly. I followed the chunk-01, 02, 29 and obligations entries to the sources at `31a47c543775`. [Outline](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L2315-L2335) · [CA-I](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L2704-L2712)

**GUIDE.** Deep Bhattacharjee, Ushashi Bhattacharya, James Montgomery Lockwood, Tristan Romanov, Ikailo John Sessford and Sanjeevan Singha Roy use a full thermal doubling bound on a window of rectangles. Row 1218 records their shape window, their construction hypothesis and their separate fixed-spacing bounds. It also records the cube-dynamics criteria and Zeng Chunping's conditional spectral criteria. Here I use the one-cube target of ZD-c. A proof on one cube would still have to use that theorem's propagation hypotheses. [Row 1218](prior/gap-onebound-read-sol.md)

**OPEN.** The full target is a nontrivial four-dimensional SU(2) quantum Yang–Mills theory on \(\mathbb R^4\) with the Jaffe–Witten properties. Its physical Hamiltonian must have \(\ker H=\mathbb C\Omega\), \(\Omega^\perp\ne0\) and \(\sigma(H|_{\Omega^\perp})\subset[m_*,\infty)\) for one \(m_*>0\) in physical units. The estimates below address the infrared part of the construction.

**GUIDE.** Write \(K\) for the positive physical Wilson transfer on a spatial cube of side \(n\) in lattice units. Include all electric flux sectors. Put \(\Psi=2\log\operatorname{Tr}K^T-\log\operatorname{Tr}K^{2T}\). The hard estimate is small \(\Psi\) at \(T=n/2\) for one fixed physical side \(L=an\) as \(a\downarrow0\). First try to remove the free long-wavelength contribution to a Wilson cut comparison. Row 1323 retained separate winding rings. Even its denser cut left a transverse polarization at momentum \(2\pi(1,1,1)/n\). Joining long paths into a three-dimensional grid gives a way to carry a closed flow with any low momentum. The test is whether the Wilson comparison still measures \(\Psi\) while the free prediction tends to zero. Then attack the residual with the Wilson interaction in the cut.

## A grid on one temporal cut

**GUIDE.** Use normalized Haar measure on positive spatial edges of the periodic lattice. Write \(w(g)=\operatorname{tr}(g)/2\), \(c_\beta(g)=e^{-\beta(1-w(g))}/z_\beta\), with \(\int c_\beta=1\). A cut is the set of temporal plaquettes between two successive spatial slices. Retain full temporal coupling on the edges of a connected spatial graph \(H\). Replace the other temporal weights by one in the unnormalized action on that cut. All spatial plaquettes and the rest of the time circle keep their original Wilson weights.

**PROVED.** Suppose \(b\mid n\), \(2\le b\le n/4\). Take all three-dimensional cubic grid paths of length \(b\) joining neighboring vertices of \(b\mathbb Z^3\) modulo \(n\). Each path keeps every fine bond along its length. Attach the remaining fine vertices by a forest with exactly one attachment to the grid per tree. Such a forest is obtained by adding a new vertex along one edge from the growing connected set until every vertex belongs. Call the resulting graph \(H_b\). It has \(3(n/b)^3\) coarse edges. Every cycle flow in \(H_b\) vanishes on the attached forest, by removing leaves.

**PROVED.** For \(X,Y\) the spatial fields on the two sides, integrate the temporal vertex gauges with full normalized kernels on \(H_b\) and constant kernels off \(H_b\). Call this function \(k_b(X,Y)\). If
\[
 \zeta_b=\sum_{d\ge2}d^2\left(I_d(\beta)/I_1(\beta)\right)^b<1,\qquad
 m_b=3(n/b)^3,
\]
then
\[
   (1-\zeta_b)^{m_b}\le k_b(X,Y)\le(1+\zeta_b)^{m_b}.                 \tag{1}
\]
Each forest edge integrates to one when its leaf gauge is integrated. Condition next on all coarse vertex gauges. The interiors of the grid paths are disjoint. On each open path, left and right translation of the interior gauges absorbs the two spatial fields, leaving their path holonomies at the ends. Haar convolution then gives a translate of \(c_\beta^{*b}\) evaluated at one group element. The character formula GL3 bounds its distance from one by \(\zeta_b\), since a character of dimension \(d\) has modulus at most \(d\). Multiplication of the bounds before integrating the coarse gauges proves (1). This bound is uniform in the spatial action.

**GUIDE.** Row 1323, proof of (16), gives \(\zeta_b\le C(1+\beta)^{3/2}\exp[-c(b-1)/(1+\beta)]\) for \(\beta\ge1\). Its proof uses \(a_d=I_d/I_1\le a_2\) for \(d\ge2\), \(\sum d^2 a_d=1/z_\beta\), and \(1-a_2\ge c/(1+\beta)\). I use that estimate for paths of length \(b\), including paths with distinct end vertices. [One-link estimate](gap-solve39-astra62.md#retaining-winding-loops-at-an-electric-seam) · [Sussman–Alpoge, GL3](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L2195-L2229)

**PROVED.** Let \(E\) be the positively oriented spatial edges and write \(S=E\setminus H_b\), \(X_S(t)=\beta\sum_{e\in S}(1-w(U_{0e}(t)))\), where \(U_{0e}\) is the temporal plaquette above \(e\). With ordinary periodic Wilson expectations of the indicated periods put
\[
 W_b=\log\mathbb E_{2T} e^{X_S(0)+X_S(T)}
          -2\log\mathbb E_T e^{X_S(0)}.
\]
Then, uniformly in \(T\ge2\),
\[
 |W_b-\Psi|\ \le\ 2m_b\log\frac{1+\zeta_b}{1-\zeta_b}.                \tag{2}
\]
Indeed, erasure in the normalized kernel contributes a constant \(1/z_\beta\) per erased edge. It cancels in this difference. In the two remaining positive numerators replace \(k_b\) by one. The single cut now factors through the constant kernel. Two such cuts give two independent open cylinders and precisely the square of the one-cut numerator. The torus denominators give \(\Psi\) by GL8 and its rectangular time version, obtained by integrating the same \(T\) or \(2T\) successive layers. Inequality (1) on each cut bounds the log error by (2). This extends the winding-ring comparison of row 1323 to a grid carrying contractible loops at every coarse plaquette.

## What the free curvature field sees on the grid

**GUIDE.** The comparison field has three independent colours with covariance the projection onto exact two-forms on the periodic four-torus. Replace \(X_S\) by \(\tfrac12\sum_{e\in S}|G_{0e}|^2\) at each cut in the definition of \(W_b\). Denote the resulting log difference by \(G_b\). Row 1323, (19)–(22), computes it as a determinant. I use those identities, including the harmonic part. [Source of the determinant](gap-solve39-astra62.md#comparing-the-two-wilson-moments-with-the-free-curvature-law)

**PROVED, using those identities.** Give fine spatial edges their counting-measure inner product. Let \(\mathcal C\) be the space of divergence-free flows. Let \(D\subset\mathcal C\) consist of those supported in \(H_b\), and \(F=\mathcal C\ominus D\). Write subscripts \(F\) for compression of quadratic forms. Then
\[
 G_b=\tfrac32\log\det\nolimits_F\!\left(1+A_F^{-1/2}\Delta_F A_F^{-1/2}\right).
                                                                    \tag{3}
\]
Here \(A\) is the antiperiodic cut operator of row 1323 and \(\Delta=A_{\rm P}-A\). Both annihilate gradients. On constant unit flows \(A=0,\ \Delta=1/T\). At each nonzero spatial momentum \(k=2\pi l/n\) both act as scalars on the two transverse polarizations. With \(2\cosh\omega=2+4\sum_i\sin^2(k_i/2)\), the scalars are
\[
 a(k)=\tanh(\omega/2)\tanh(T\omega/2),\qquad
 \delta(k)=2\tanh(\omega/2)/\sinh(T\omega).                              \tag{4}
\]
Indeed restriction of a cycle flow to \(S\) has kernel \(D\) and is onto. Any assigned divergence from \(S\) can be canceled on a spanning tree in \(H_b\) by routing from the leaves. Thus the adjoint of restriction identifies the coordinate space on \(S\) with \(F\), with both determinants transformed by the same factor. The retained windings span all harmonic directions under projection. Hence the only constant flow in \(F\) is zero and \(A_F>0\). The periodic and antiperiodic eigenvalues of row 1323, (21), yield (4) by subtraction.

**PROVED.** Fix \(0<\alpha\le T/n\). If \(h\) is a transverse unit Fourier vector at \(k\ne0\), or a constant unit vector at \(k=0\), set
\[
 Q(h)=\langle P_F h,A_F^{-1}P_F h\rangle.
\]
For any \(d\in D\) with the same harmonic projection as \(h\),
\[
 Q(h)\le
 \sum_{k'\ne0}\frac{|\widehat{h-d}(k')|^2}{a(k')}.                     \tag{5}
\]
In fact \(Q(h)=\sup_{f\in F,\ f\ne0}|\langle h,f\rangle|^2/\langle f,Af\rangle\). Replace \(h\) by \(h-d\) in the numerator and apply weighted Cauchy–Schwarz on the nonzero modes. We may complexify the real flow space for Fourier arithmetic. The determinant and trace in (3) are unchanged. In particular \(Q(h)\le1/a(k)\) for \(k\ne0\).

**PROVED.** For every momentum with \(|k|_\infty<\pi/b\), including zero, each of its unit polarizations satisfies
\[
                              Q(h)\le C_\alpha b^2 .                     \tag{6}
\]
Here is a lift that works also for oblique wave vectors. Write \(h_i(x)=n^{-3/2}v_i e^{ik\cdot x}\), \(\sum_i|v_i|^2=1\) and \(\sum_i(1-e^{-ik_i})v_i=0\). Set \(\phi(t)=b^{-1}\sum_{s=0}^{b-1}e^{-ist}\), which has \(|\phi(t)|\ge2/\pi\) for \(|bt|\le\pi\) by the sine quotient and its limit at zero. Put a constant flow on each grid segment out of \(bx\), of value
\[
 d_i(bx+s e_i)=b^2 n^{-3/2}e^{ik\cdot bx}\,v_i/\phi(k_i),
             \quad 0\le s<b .
\]
Put zero on other edges. At the interior vertices the incoming and outgoing flows agree. At coarse vertices use \(1-e^{-ibk_i}=b(1-e^{-ik_i})\phi(k_i)\). This proves \(d\in D\). Summing over \(x\) and \(s\) gives \(\widehat d(k)=v\). The other nonzero coefficients can occur only at \(k'=k+2\pi m/b\) modulo \(2\pi\), and are \(v_i\phi(k_i')/\phi(k_i)\). Thus \(h-d\) has zero low coefficient, including the constant coefficient if \(k=0\). For a nonzero base frequency its aliases cannot include zero.

**PROVED.** Here are the inverse-form costs of the remaining frequencies. Use nearest-to-zero representatives for momenta. Since \(\omega=2\operatorname{arsinh}((\sum_i\sin^2(k_i'/2))^{1/2})\), one has \(c|k'|_\infty\le\omega\le C|k'|_\infty\). For \(k'\ne0,\ T\ge\alpha n\) this gives \(a(k')^{-1}\le C_\alpha/|k'|_\infty\). Fix \(m_i\) and sum this reciprocal over the other two alias indices, omitting the base alias \(m=0\). With the indices centered modulo \(b\), a perpendicular shell of radius \(j\ge1\) has at most \(8j\) members. On it \(|k'|_\infty\ge \pi j/b\), by the bound on \(|k|_\infty\) and distance modulo \(2\pi\). The perpendicular zero term, when present, has \(m_i\ne0\) and costs at most \(C_\alpha b\). The total at fixed \(m_i\) is at most \(C_\alpha b^2\). Finite Fourier orthogonality gives \(\sum_{m_i}|\phi(k_i+2\pi m_i/b)|^2=1\) because summing over \(m_i\) kills distinct \(s,s'\) in the squared geometric sum. Summing (5) with these weights, using \(|\phi(k_i)|\ge2/\pi\) and \(\sum_i|v_i|^2=1\), proves (6).

**PROVED.** For \(2\le b\le n/4\), \(b\mid n\) and \(T\ge\alpha n\),
\[
 \frac92\log\!\left(1+\frac{b^2-1}{T}\right)
       \ \le\ G_b\ \le\
 C_\alpha\left(\frac{b^2}{n}+e^{-c_\alpha n/b}\right).                  \tag{7}
\]
For the upper bound use \(\log\det(1+B)\le\operatorname{Tr}B\) for \(B\ge0\) in (3). Expand the trace in harmonic and transverse Fourier vectors. Its terms are \(Q(h)/T\) on the three constants and \(\delta(k)Q(h)\) on the two polarizations at every \(k\ne0\). Write \(j=|l|_\infty\) for a centered fine frequency index. Equations (4) and \(T\ge\alpha n\) give \(\delta(k)\le (C_\alpha/n)j e^{-c_\alpha j}\). There are at most \(Cj^2\) indices in shell \(j\). Thus (6) bounds the entire low-frequency sum by \(C_\alpha b^2/n\), including the constants. For \(|k|_\infty\ge\pi/b\) use \(Q(h)\le1/a(k)\). Then \(\delta(k)/a(k)=1/\sinh^2(T\omega/2)\le C_\alpha e^{-c_\alpha j}\). The shells with \(j\ge n/(2b)\) contribute at most \(C_\alpha e^{-c'_\alpha n/b}\).

**PROVED.** For the lower bound use row 1323, (22). In its notation \(h+Rh\) is the minimum-norm cycle in \(D\) with harmonic projection \(h\). For a constant unit flow with coefficients \(v_i n^{-3/2}\), the total in direction \(i\) is \(v_i n^{3/2}\). A cycle uses only the \(n^3/b^2\) grid edges in that direction. Cauchy–Schwarz gives a squared norm of at least \(b^2\sum |v_i|^2=b^2\). The flow constant at \(b^2v_i n^{-3/2}\) on those edges attains it. Hence \(R^*R=(b^2-1)I\). The periodic form compressed to \(Z'\) in (22) is at most \(I\), since it compresses an average of orthogonal projections. Its inverse is at least \(I\), and the transverse determinant ratio is at least one by (4). This gives the lower bound in (7). In particular on \(T/n\) bounded above and away from zero, \(G_b\to0\) precisely when \(b^2/n\to0\) along these grids.

**PROVED.** Let \(n=2^j\), \(T=n/2\), \(1\le\beta\le B\log n\), and \(b=2^{\lfloor j/3\rfloor}\) for large \(j\). Then \(m_b\zeta_b\to0\) while \(b^2/n\to0\). Equations (2) and (7) give
\[
              W_b=\Psi+o(1),\qquad G_b=O(n^{-1/3}),\qquad
              W_b-G_b=\Psi+o(1).                                       \tag{8}
\]
The same holds for \(\alpha n\le T\le A n\) with fixed positive \(\alpha,A\). In contrast, row 1323, (28), gives an order-one lower bound on the free transverse contribution for its disjoint winding rings at \(T=n/2\). Thus its surviving transverse mode depends on the geometry of the retained cut. Equation (8) controls the Gaussian determinant down to zero while keeping the original Wilson observable. The number \(\Psi\) still depends on the interacting measure.

## Restoring the coupling of a whole cut

**GUIDE.** For a second attack, retain the same positive absolute coupling \(u\) on *every* temporal plaquette of the cut. The rest of the cylinder remains isotropic at \(\beta\). Put \(V=n^3\), take even \(n\ge8,\ T\ge2\), and let \(\mathcal P\) be the \(3V\) spatial plaquettes. In the following argument \(B=M K^{T-1}M\) is the open-cylinder operator. Here \(K=M C_\beta P M\), \(M\) is the exponential of minus half the spatial Wilson action, \(P\) averages vertex gauges and \(C_\beta\) is the product of normalized electric convolutions. Write \(C(u)\) for the gauge-projected product on the cut at \(u\), with kernel \(k_u(x,y)\). The two orderings of the half steps give the same torus traces by cyclicity. Define
\[
 J(u)=2\log\operatorname{Tr}(B C(u))
      -\log\operatorname{Tr}\!\left(B C(u)B C(u)\right).
\]
The positive operator \(B^{1/2}C(u)B^{1/2}\) gives \(J(u)\ge0\). At \(u=0\) it has rank one, and \(J(\beta)=\Psi\). Row 1151 used the same open-cylinder comparison with longitudinal bonds retained. Here the first coupling between the ends has order four. [Row 1151, §§2–4](gap-solve5-astra62.md)

**PROVED.** For an absolute \(u_0>0\), uniformly over \(n,x,y\) and \(0\le u\le u_0\),
\[
 \left|\log k_u(x,y)-\frac{u^4}{64}
             \sum_{p\in\mathcal P}w_p(x)w_p(y)\right|
                   \le C V u^5.                                         \tag{9}
\]
To see the uniform remainder, normalize each edge weight to \(1+h_e=e^{u w_e}/\int e^{u w}\,dg\). Its arguments include the two independent endpoint vertex gauges at that edge. On a fixed small complex disk \(|u|\le r\), \(\|h_e\|_\infty\le C_0r\), by the exponential series and the nonzero denominator at zero. Expand the product in subsets of edges. A connected edge subset \(P'\) has weight equal to the integral of \(\prod_{e\in P'} h_e\) over its vertices. Disjoint vertex sets factor. Every subset with a leaf has zero integral because a single normalized weight integrates to one in either end gauge.

**PROVED.** For any set \(A\) of allowed vertices let \(Z(A)\) be this sum over disjoint connected subsets inside \(A\), including the empty collection. When deleting a vertex \(z\), group collections by the unique member \(P'\) containing \(z\), if it exists. There are at most \(6^{2q}\) connected \(q\)-edge subsets containing \(z\), since doubling their edges produces closed walks of length \(2q\) from \(z\) whose visited edges recover the subsets. Induct on \(|A|\). If all smaller deletion ratios lie within \(1/2\) of one, then \(|Z(A\setminus V(P'))/Z(A\setminus\{z\})|\le2^q\), by deleting at most \(q\) more vertices. The sum of all terms in \(Z(A)/Z(A\setminus\{z\})-1\) has modulus at most \(\sum_{q\ge1}(72C_0r)^q\le1/2\) for fixed small \(r\). This starts at \(Z(\varnothing)=1\). Telescoping the analytic logarithms of these ratios gives \(|\log k_u|\le V\log2\) on the disk. Cauchy's coefficient estimate bounds the tail from order five by \(CV|u|^5\) on \(|u|\le r/2\).

**PROVED.** The first surviving connected subsets have four edges and form the elementary squares. The lower coefficients vanish by the leaf rule. Identify \(SU(2)\) with the unit quaternions. The coefficient linear in \(u\) on an edge has the form \(g_z\cdot R_e g_{z'}\), where \(R_e\) is left and right multiplication by the two boundary links with the appropriate inverses. Each of the four vertex averages contracts two indices with \(\delta_{ij}/4\) by rotational symmetry on \(S^3\). The remaining real trace around the square is \(4w_p(x)w_p(y)\). Indeed the real trace of \(g\mapsto ag b^{-1}\) is \(4\operatorname{Re}(a)\operatorname{Re}(b)\), as follows by summing its diagonal on \(1,i,j,k\). This proves the coefficient in (9), independently of plaquette orientation. The quaternion contraction is the one used in row 1151, (25).

**PROVED.** Let \((X,Y)\) be the ends of one open cylinder, with joint probability proportional to the positive position kernel of \(B\). There is an actual Wilson correlation in the first response:
\[
 [u^4]\,J(u)=\frac1{32}\sum_{p\in\mathcal P}
        \operatorname{Cov}_{B}\!\left(w_p(X),w_p(Y)\right)\ \ge0 .       \tag{10}
\]
In one sewing, (9) inserts the product on the two ends of this cylinder. In two sewings at \(u=0\), either insertion joins two independent open cylinders, so its expectation factors into the two means. There are two choices of cut. The means at the two ends agree by reversal. For each term, the form \(\langle f,Bg\rangle/\langle1,B1\rangle\) is positive semidefinite. Cauchy–Schwarz against \(1\) gives the sign in (10). Formula (10) is for finite \(n,T\) and does not need any uniform assertion about a Taylor series for \(J\).

**PROVED, using the open-end estimate of row 1151, (6).** There are numerical positive \(c,C\) such that for \(\beta\ge1,\ 0\le u\le u_0\) and \(V u^4\le cV/\beta^2\),
\[
       0\le J(u)\le C\left(Vu^4/\beta^2+Vu^5+e^{-cV/\beta^2}\right).
                                                                         \tag{11}
\]
The cited estimate at either free temporal end is
\(\Pr(\sum_{p\in\mathcal P}(1-w_p)^2>C V/\beta^2)\le C e^{-c_1V/\beta^2}\). It uses spatial transfer with that free end and full spatial weights, as in \(B\) here. Put \(\gamma=u^4/64\), \(d_p=1-w_p\). The leading kernel in (9) is a scalar times
\[
 f(x)f(y)\exp E(x,y),\qquad
 f(x)=e^{-\gamma\sum_p d_p(x)},\qquad E(x,y)=\gamma\sum_p d_p(x)d_p(y).
\]
With just \(f(x)f(y)\) the two normalized sewing integrals are products of open cylinders tilted at their ends. Their ratio defining \(J\) is one. On good ends \(0\le E\le C\gamma V/\beta^2\) by Cauchy–Schwarz. On all ends \(E\le12\gamma V\) and \(|\log f|\le6\gamma V\). For one or two cylinders, the tilted integral of \(e^{\sum E}\) over exceptional ends is thus at most \(C\exp(C'\gamma V-c_1V/\beta^2)\) by the union bound and division by the tilt normalizer. Its full integral is at least one. Our small absolute choice of \(c\) absorbs \(C'\gamma V\). Taking the log in both sewings and paying the remainder in (9) proves (11). [Open-cylinder tail and its proof](gap-solve5-astra62.md#4-a-one-step-restoration-beyond-the-arbitrary-exterior-scale)

**PROVED.** Take \(\beta\to\infty,\ \beta\le B_0\log n\) and \(u_*=n^{-3/4}\beta^{1/3}\). Then \(\sup_{0\le u\le u_*}J(u)=o(1)\) for the original interacting bulk, uniformly in \(T\ge2\). Indeed \(Vu_*^4/\beta^2=\beta^{-2/3}\) and \(Vu_*^5=n^{-3/4}\beta^{5/3}\). Yet the normalized *isolated* cut has
\[
                   \operatorname{Tr} C(u_*)\ge1+3V a_2(u_*)^4\longrightarrow\infty,
             \qquad a_2(u)=I_2(u)/I_1(u).
\]
The fundamental characters on the \(3V\) simple plaquettes are orthonormal in link Haar measure by integration on an unshared edge and character orthogonality. They belong to the physical space and each has electric eigenvalue \(a_2(u)^4\). The Bessel series gives \(a_2(u)=u/4+O(u^3)\). Thus the vanishing contribution in (11) reaches a coupling for which the isolated-cut trace already diverges.

## Which terms carry the full Wilson cut

**GUIDE.** To reach full coupling, try keeping the positive terms in the cut integral instead of continuing (9) past its disk. Row 1151, (25)–(26), already expands this gauge integral in paired quaternion strands. The term with no strands gives a rare-event expression for the purity. Here I group by the *total degree* before making any pairings. This keeps a nonnegative kernel at each surviving degree and permits estimates under the original full Wilson measure.

**PROVED.** Put \(m=3n^3\), the number of temporal plaquettes on one cut, and \(Y=\sum_{e}w(U_{0e})\) there. Use unnormalized weights \(e^{\beta w}\) on the cut, whose scalar normalizations cancel from \(J\). With \(dg\) denoting the temporal vertex gauges, the kernel at even total degree \(k\) is
\[
                  H_k(x,y)=\frac{1}{k!}\int Y(x,g,y)^k\,dg .
\]
All odd coefficients vanish. Multiplying the temporal links on the black vertices of the even spatial torus by \(-1\) changes the sign of every term of \(Y\). This change acts independently at distinct cuts. Each \(H_k\) for even \(k\) is pointwise nonnegative and positive as an operator. Before gauge averaging, the sum of the fundamental characters divided by two across the edges is a positive-definite function of the link group. It is a sum of normalized traces of unitary representations. Its \(k\)-th pointwise power is positive definite by tensoring these representations. The convolution commutes with vertex gauges because its edge characters are central. The gauge average is its compression to the physical space. Each coefficient has finite rank by the finite tensor product. The series \(\sum_{k\ {\rm even}}\beta^k H_k\) is the full cut kernel, with uniform absolute convergence at each finite box since \(|Y|\le m\).

**PROVED.** In the positive expansion of the one- or two-cut partition integral let \(D_i\) be the even degree chosen on cut \(i\). Its joint law can be sampled mathematically as follows. Read \((|Y_i|)_i\) under the ordinary periodic Wilson law. Conditional on these values draw the \(D_i\) independently, with
\[
        \Pr(D_i=k\mid |Y_i|)=
            \frac{\lambda_i^k}{k!\cosh\lambda_i},\quad
        \lambda_i=\beta|Y_i|,\quad k=0,2,\ldots .                       \tag{12}
\]
At \(\lambda_i=0\) use \(D_i=0\). To prove this, erase the specified cut weights in the measure before the temporal gauge integrations. The remaining measure is invariant under each individual sign change above. Thus integrating any function of the \(|Y_i|\) with weights \(e^{\beta\sum_iY_i}\) gives the same integral with weights \(\prod_i\cosh(\beta Y_i)\). Expanding each cosh gives (12) term by term, also when the two spatial endpoint pairs are dependent.

**PROVED, using row 1151, (21)–(22a).** In the thermal-seed rectangles \(n^3\times T,n^3\times 2T\), \(T=n/2\), with \(\beta\to\infty,\ \beta\le B_0\log n\), set \(X=\beta(m-Y)\) on any one cut. For fixed \(0<\eta<1/24\) and \(r=\beta^{-\eta/2}\), one has
\[
             \Pr\{|X/m-3/4|>r\}\le 2\exp(-c_\eta m r^2).                 \tag{13}
\]
Here (22a) is the pressure slope, proved in the earlier row by an open-box argument based on Sourav Chatterjee's weak-coupling free-energy method. For completeness, split the cut into its three orientations. In one orientation on a set \(S\), the logarithm of the expectation of \(e^{h\sum_S\beta(1-w_p)}\) is bounded by \(|S|[p( h)-p(0)]\). The dissemination proof of (21) uses positive layer operators for either sign of small \(h\) because the perturbed coupling \(\beta(1-h)\) stays positive. Here \(p\) is per four-volume with only this orientation tilted everywhere. By (22a), \(p(h)-p(0)\le 3h/4+C_\eta(h^2+|h|\beta^{-\eta})\). Apply ordinary Hölder with three factors and arguments \(3h\) to obtain
\[
 \log\mathbb E e^{h(X-3m/4)}\le C_\eta m(h^2+|h|\beta^{-\eta})
\]
for both signs of small \(h\). Choosing \(h\) a sufficiently small positive or negative multiple of \(r\) proves (13) for large \(\beta\). [Wilson pressure estimate](gap-solve5-astra62.md#8-a-terminal-interval-of-the-original-spatial-face-bound) · [Sussman–Alpoge, finite chessboard inequality](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L2885-L2912)

**PROVED.** Set \(d_*=m(\beta-3/4)\). At full coupling keep the *same* finite set
\[
       I_n=\{k\ge0:\ k\ {\rm even},\quad |k-d_*|\le 3mr\}              \tag{14}
\]
on every cut. Its one-cut discarded probability and the two-cut probability that either degree is discarded are \(O(\exp[-c_\eta m r^2/\beta])\). On the good event in (13), \(Y>0\) and \(|\lambda-d_*|\le mr\). For a Poisson variable of mean \(\lambda\), its centered exponential moment is \(\exp(\lambda(e^t-1-t))\le e^{\lambda t^2}\) for \(|t|\le1\). Choose \(|t|\) a small multiple of \(r/\beta\). Conditioning this Poisson variable on even parity multiplies a tail bound by at most two. Applying (13) to each cut and taking the union bound proves the claim for their joint law. Here \(mr^2/\beta\to\infty\).

**PROVED.** Let \(C_I=\sum_{k\in I_n}\beta^k H_k\). Replacing the full electric cut by \(C_I\) in \(J(\beta)\) changes its value by \(O(\exp[-c_\eta m r^2/\beta])\). Indeed, the respective one- and two-cut partition function ratios are precisely their probabilities that every degree is retained. Taking logarithms proves the estimate without a lower bound on the thermal purity. The one-period trace-normalized positive operator \(B^{1/2}C_I B^{1/2}/\operatorname{Tr}(BC_I)\) differs in trace norm from its full counterpart by at most twice the one-cut discarded probability, since the full state is a convex mixture of its retained and discarded states. These are statements on the interacting slab of thickness \(T\). The degrees in (14) are extensive, even though the width of the retained interval is \(o(m)\).

**PROVED.** The accuracy needed from the remaining high-degree terms can be quantified. Let \(q=1\) or \(2\), and choose even \(k_i\) satisfying \((k_i-d_*)/m\to x_i\in\mathbb R\). Under the corresponding full Wilson law,
\[
 \lim_{n\to\infty}\frac{\beta}{m}\log\Pr(D_1=k_1,\ldots,D_q=k_q)
                         =-\tfrac12\sum_{i=1}^q x_i^2 .                 \tag{15}
\]
On the common good event of (13), \(\lambda_i/m=\beta-3/4+O(r)\). For even \(k\), \(\log(k!)=k\log k-k+O(\log(k+2))\), obtained by bounding the increasing function \(\log t\) by upper and lower integral sums. Since \(\log\cosh\lambda=\lambda+O(1)\) for \(\lambda\ge1\), (12) gives the log mass as
\[
 -\frac{(k-\lambda)^2}{2\lambda}
       +O\!\left(\frac{|k-\lambda|^3}{\lambda^2}+\log(k+2)\right).
\]
This uses Taylor's theorem for \((1+t)\log(1+t)-t\) on \(|t|\le 1/2\). On the good event the expansion divided by \(m/\beta\) converges uniformly to \(-x_i^2/2\), using \(\beta\log(m\beta)/m\to0\). Multiply the conditional masses. The complement has probability at most \(2q e^{-c_\eta m r^2}\), negligible even on this logarithmic scale since \(\beta r^2\to\infty\). This proves both inequalities for (15). The displayed additive rate for two cuts uses the conditional Poisson variables only. It does not assert that the two Wilson boundaries are independent.

**PROVED.** The small quantity in (11) gives exponentially little control by conditioning on (14). For \(q=1,2\), let \(E_I\) mean that all \(q\) degrees are in \(I_n\). In the sewn Wilson model with cut coupling \(u_*\) and all other couplings at \(\beta\),
\[
  \frac{-\log\Pr_{u_*}(E_I)}{q\,m\beta\log(\beta/u_*)}\longrightarrow1. \tag{16}
\]
Indeed, at a particular degree tuple the two weights differ by \((u_*/\beta)^{\sum k_i}\) times the ratio of unnormalized partition functions. The log of this last ratio has absolute value at most \(qm|\beta-u_*|\) by \(|Y_i|\le m\). On \(E_I\), \(\sum k_i/(qm\beta)\to1\) uniformly. At \(\beta\), \(\Pr_\beta(E_I)\to1\) by (14), and \(\log(\beta/u_*)\to\infty\). Summing the lower and upper weight comparisons proves (16). Thus almost all the full-coupling partition integral comes from degrees that have the displayed rare probability at the weak cut.

**PROVED, using row 1153, (5).** Even the individual degree rates (15) can agree on two sequences of *ordinary Wilson tori* with opposite thermal behavior. Keep the same \(n,\beta\) in both. For one choose an even time period \(t_s\) nearest to \(\beta^{1/32}\). Its defect is asymptotic to \((\pi^2/8)n^3/t_s^3\) by row 1153, since \(t_s^4\beta^{-1/4}[\log(2+\beta)]^{3/2}\to0\). For the other, choose even \(t_v\ge n\) so large that \(\operatorname{Tr}(K/\|K\|)^{t_v}-1\le1/n\) at that cutoff. Such a time exists. At finite cutoff the strictly positive continuous Wilson kernel has a simple leading eigenvalue, and powers of the other eigenvalues normalized by it are dominated by their summable first powers. The resulting defect is at most \(2\log(1+1/n)\). [Short-period Wilson law](gap-solve6-astra62.md#the-thermal-sum-in-the-range-controlled-by-3) · [Row 1154, §3](gap-solve6-check-opus.md)

**PROVED.** To verify (15) on these extra shapes, write \(s=\min(n,t)\) for the shortest side. In the box comparison of row 1151, (22b), a tiling by side \(b_0\) omits a fraction at most \(4b_0/s\) by adding the four leftover strip fractions. There are \(O(V_4/b_0)\) boundary sites in complete boxes, where \(V_4=n^3t\). Its joining-link and restricted-boundary cost per site is therefore \(O((1/b_0+b_0/s)\log\beta)\). The single-box Taylor, determinant, and Gaussian-tail bounds in the cited proof depend only on \(b_0,\beta\) and the orientation weight. This gives (22b) with \(b_0/s\) in the leftover term. The uniform Gaussian slope has error \(O(1/b_0)\) at zero and bounded second derivative. The two convex secants at distance \(\sqrt{(\log\beta)(1/b_0+b_0/s)}\) give (22a) on \(|h|\le1/4\) with that error plus \(O(1/b_0)\), besides \(O(|h|)\). Take \(b_0=\lceil\beta^{1/64}\rceil\). Both shapes and their doubles have \(s\ge c\beta^{1/32}\), so any fixed \(0<\eta<1/128\) suffices. The single-box condition \(b_0^{12}\log\beta=o(\beta)\) holds. The proof of (13)–(15) now applies verbatim with this \(\eta\). Thus both time sequences have the same rate at every fixed \(x_1,x_2\), although one defect diverges and the other tends to zero. Their physical time intervals differ. This comparison tests exactly what information the degree rates retain.

## A physical-scale test of homogeneous weakening

**PROVED.** The grid divisibility is unnecessary for a continuously variable comparison. Let \(0<e=u/\beta<1\). On a homogeneous cut the Wilson log difference of the two exponential deletion moments is exactly \(\Psi-J(u)\), by cancellation of the one- and two-cut partition functions. The Gaussian log difference for this same partial deletion is
\[
 G(e)=\tfrac92\log\left(1+\frac{1-e}{eT}\right)
  +3\sum_{k\ne0}\log
     \frac{e/(1-e)+a(k)+\delta(k)}
          {e/(1-e)+a(k)} .                                               \tag{17}
\]
Indeed \(I-(1-e)\Gamma=eI+(1-e)(I-\Gamma)\) in the one-cut Gaussian integral with covariance \(\Gamma\). The temporal even/odd decomposition in the two-cut integral is the one in row 1323, (20). Gradients have equal factors \(e\). The three harmonic directions and two transverse polarizations give (17) from (4).

**PROVED.** If \(T/n\to\alpha>0\) and \(ne\to c\in(0,\infty)\), then \(G(e)\) tends to
\[
 g_\alpha(c)=\tfrac92\log(1+1/(\alpha c))
 +3\!\sum_{l\in\mathbb Z^3\setminus\{0\}}
  \log\frac{c+\pi |l|\coth(\pi\alpha |l|)}
            {c+\pi |l|\tanh(\pi\alpha |l|)}.                              \tag{18}
\]
For fixed \(l\), \(n\omega(2\pi l/n)\to2\pi|l|\). Each nonzero log term is nonnegative and at most \(\delta(k)/a(k)\), summable uniformly by the shell estimate in (7). Hence dominated convergence applies, including along \(ne\to\infty\), where every term tends to zero. The same summable bound proves continuity of \(g_\alpha\) for \(c>0\). Each summand decreases in \(c\), the harmonic term strictly. The limits at zero and infinity are respectively infinity and zero.

**PROVED.** For each fixed \(c>0\) take \(u=\beta c/n\). Then \(u\le u_*\) eventually under the logarithmic bare-coupling bound. Equations (11) and (18) show that the Wilson deletion difference is \(\Psi+o(1)\) for *every* such \(c\), while the free deletion difference can approach any prescribed positive number. Taking \(u=u_*\) gives the same Wilson comparison and \(G(u_*/\beta)\to0\). Thus a geometry-independent free estimate cannot be justified by the small thickness of the changed layer alone. For the interacting Wilson example at \(t_s\) above, changing one layer per period changes the fraction of temporal plaquettes \(1/t_s\to0\), takes the diverging homogeneous defect to \(J(u_*)=o(1)\), and leaves every other coupling at its original value. This last example is at shrinking physical time. It does not decide the fixed-physical-time inequality.

## Using the interacting ends to retain more bonds

**GUIDE.** Try to continue (2) toward the full temporal cut by decreasing the grid spacing. A bound uniform in the two boundary fields can be too expensive. The open Wilson cylinder supplies additional integrations at both ends. Row 1272 uses conditional convolution on the interiors of straight coarse transports. Row 1151, §5, already combines temporal-path convolution with both free Wilson ends on a ladder. The new estimate uses the shortest closed paths of a three-dimensional grid and compares it to the sharp fixed-boundary threshold. Bhattacharjee, Bhattacharya, Lockwood and Romanov also use straight-path convolution in their block-law work described in row 1218. I apply this mechanism inside the actual two sewing integrals. [Row 1151, ladder integration](gap-solve5-astra62.md#5-full-strength-transverse-links-on-the-original-seam) · [Row 1272, straight transports](gap-solve31-astra62.md#fixing-all-straight-coarse-transports-in-the-finite-label-test) · [Published source comparison](prior/gap-onebound-read-sol.md)

**PROVED.** Write \(a_d(t)=I_d(t)/I_1(t)\) for \(d\ge1\), with its continuous value at zero. Then \(0\le a_d(t)\le a_2(t)^{d-1}\), and \(a_2(t)\) increases with \(t\ge0\). This is the Bessel Turán log-concavity recorded in row 996. For a short verification, \(I_{j+1}(t)/I_j(t)\) is the mean of \(x\) in the density proportional to \(e^{tx}(1-x^2)^{j-1/2}\) on \((-1,1)\). Expand the exponential and integrate the even powers by the beta integral, obtaining a constant times \(t^{-j}I_j(t)\) for the normalizer. Its logarithmic derivative is \(I_{j+1}/I_j\) by the Bessel series. Conditional on \(y=|x|\), the mean is \(y\tanh(ty)\), an increasing function of \(y\). Increasing \(j\) by one reweights the \(y\)-law by the decreasing function \(1-y^2\). This lowers the mean, since their covariance is half the mean product of their differences on independent copies. Multiplying the adjacent ratios proves the bound. The derivative of the \(j=1\) mean in \(t\) is its nonnegative variance. Finally
\[
                    -\log a_2(t)=(3/2+o(1))/t\qquad(t\to\infty).         \tag{19}
\]
Indeed \(a_2(t)\) is the Wilson mean of \(\cos\theta\) on \(S^3\). In the radial Haar integral substitute \(s=\sqrt t\,\theta\). The limiting density is proportional to \(s^2e^{-s^2/2}\), and \(t(1-\cos\theta)\) tends to \(s^2/2\), with mean \(3/2\) by integration by parts. The bounds \(1-\cos\theta\ge2\theta^2/\pi^2\), \(\sin\theta\le\theta\) justify both limits. [Row 996, B9 and its attribution](gap-sepinput-max.md)

**PROVED.** Allow the successive grid intervals in every direction to have lengths \(b\) or \(b+1\) with \(D=\lfloor n/b\rfloor\) intervals in each direction, \(D\ge 8\), \(D\ge b\). Distribute the remainder among the intervals. Use the same attached forest as before and put \(N=D^3\). If \(r_0=a_2(\beta)^b\) is sufficiently small,
\[
        cN a_2(\beta)^{4(b+1)}
              \le \log k_b(\mathbf1,\mathbf1)
              \le \sup_{x,y}|\log k_b(x,y)| \le C N r_0^4 .              \tag{20}
\]
For the upper bound each normalized coarse edge has kernel \(1+h_e\). Its character expansion after the internal temporal gauges gives
\(\|h_e\|_\infty\le\sum_{d\ge2}d^2 r_0^{d-1}\le C r_0\). It integrates to zero as a function \(h_e\) of either end gauge when all other arguments are fixed. Apply the vertex deletion proof of (9) to \(1+z h_e\) on the coarse graph, on \(|z|\le c_0/r_0\). Terms of degree less than four vanish by the leaf rule and the girth of the graph. Cauchy's bound on the log at \(z=1\) gives \(C N r_0^4\).

**PROVED.** For the lower bound keep a collection of at least \(N/16\) edge-disjoint elementary coarse squares in the \(12\)-planes. In each plane take alternate pairs in each of the first two coordinates, omitting the leftover line if needed. Products of the fundamental characters on any subset of these squares form an orthonormal set on coarse link Haar space. Every unshared edge integrates to zero for two different subsets. Character orthogonality gives norm one. Each product on \(j\) squares is a gauge-invariant eigenfunction of the coarse electric kernel with eigenvalue at least \(a_2(\beta)^{4(b+1)j}\). Its value at the trivial field has squared modulus \(4^j\). Subtracting these eigenprojections with their eigenvalues leaves a positive operator with continuous kernel. Its diagonal is nonnegative by testing against approximate point masses. Summing over subsets gives \(k_b(\mathbf1,\mathbf1)\ge(1+4a_2(\beta)^{4(b+1)})^{N/16}\), and hence (20). This lower bound tests the actual gauge-integrated kernel before averaging the spatial boundary fields.

**PROVED.** For the full Wilson sewing, \(T\ge3,\ b\ge4\), put
\[
   r_1=a_2(\beta)^b\,a_2(5\beta)^{2(b-2)}.
\]
For \(r_1\) below an absolute constant one has
\[
                               |W_b-\Psi|\le C N r_1^4.                  \tag{21}
\]
After integrating the cut gauges on the forest and inside the grid paths, represent the rest by independent open cylinders, one or two as in (2). At each free end mark every link strictly between the first and last links of each coarse segment. A segment of length \(l\) provides \(l-2\) marked links. No spatial plaquette contains two marks. Parallel marks on one line are collinear, and different parallel lines are separated by at least \(b\). For two distinct directions, meeting the same unit square would require a segment link incident to a coarse vertex, which was omitted. The two ends of an open cylinder are at least two time steps apart, so each temporal plaquette contains at most one mark. Marks on separate open cylinders are independent before sewing.

**PROVED.** Condition this open-cylinder probability on all unmarked fine links. Each marked link occurs in four spatial plaquettes and just one remaining temporal plaquette. Its conditional density on unit quaternions is proportional to \(e^{\beta S\cdot U}\), where the staple sum \(S\) of five unit quaternions has norm at most five. The marked links are conditionally independent, by the preceding incidence statement. Each density is a translate of the central Wilson density of strength \(t=\beta|S|\le5\beta\), with uniform Haar at \(t=0\). Thus the holonomy along each retained segment on an open end is, conditionally, a product of independent translated central kernels and fixed group elements. Centrality moves the fixed elements to one end. Inversion leaves each central kernel unchanged.

**PROVED.** Fix the remaining temporal gauges at coarse vertices. Each coarse cut factor contains one such spatial holonomy from *each* side and the temporal convolution of length \(l\). Each endpoint segment enters once, including in the two-cut numerator. Integrating its marked links on both sides convolves all three distributions. At spin dimension \(d\), the translated central kernel left on that edge has scalar coefficient before translation
\[
            a_d(\beta)^l\prod_{\text{two ends}}\prod_{\text{marks}} a_d(t)
                    \ \le\ r_1^{d-1}.
\]
All conditional laws used here are normalized. Integrating the marks for one edge does not reweight another conditional factor. We now have coarse kernels \(1+h_e\) with \(\|h_e\|_\infty\le C r_1\), and \(\int h_e=0\) in either coarse vertex gauge. The same girth-four proof as in (20) bounds the log of each remaining coarse-gauge integral in absolute value by \(CNr_1^4\), uniformly over the *unmarked* data. For two sewings the coarse vertex gauges of the two cuts are disjoint. The normalized open-cylinder expectation preserves these multiplicative bounds. Rank-one factorization of the completely open numerators then proves (21).

**PROVED.** For \(\beta\to\infty,\ \beta\le B_0\log n\), take \(b=\lceil (2/5)\beta\log n\rceil\). Then (19) gives, simultaneously,
\[
 \sup_{x,y}|\log k_b(x,y)|=n^{3/5+o(1)},\qquad
                     |W_b-\Psi|\le n^{-9/25+o(1)}.                     \tag{22}
\]
Here \(\log N=(3+o(1))\log n\). The powers subtracted in (20) and (21), in units of \(\log n\), are \(6(2/5)\) and \(6(1+2/5)(2/5)\), respectively. More generally, \(b\sim d\,\beta\log n\) with \(5/14<d<1/2\) makes the interacting replacement error tend to zero while the uniform log error diverges. The optimal interacting threshold remains open.

**PROVED.** Iterating the five-staple calculation through the next set of links encounters a coupling of order one even on fields close to the identity. At a free end integrate a single edge. In two distinct spatial staples keep a parallel neighbor link free, orienting its argument in the staple as \(A\) or \(B\). For example take the neighbors at offsets \(e_2,e_3\) of a direction-one edge. No elementary plaquette contains both neighbors. Set the other local links to the identity. The new joint weight, apart from separate factors of \(A\) and \(B\), is
\[
             F_\beta(A,B)=\int_{S^3}e^{\beta q\cdot(3+A+B)}\,dq .
\]
Put \(A=\exp(is/\sqrt\beta),\ B=\exp(it/\sqrt\beta)\) in a common quaternion circle, with fixed real \(s,t\). Then
\[
 \log\frac{F_\beta(A,B)F_\beta(1,1)}
               {F_\beta(A,1)F_\beta(1,B)}
                               \longrightarrow st/5.                    \tag{23}
\]
For \(A=e^{i\theta}, B=e^{i\phi}\), the norm of \(3+A+B\) equals \(5-(\theta^2+\phi^2)/2+(\theta+\phi)^2/10+O((|\theta|+|\phi|)^4)\). The radial Haar integral at norm \(R\) is \(e^{\beta R}(\beta R)^{-3/2}(C+o(1))\) uniformly near \(R=5\), by the substitution in (19). The separate terms cancel from the cross ratio, leaving \(st/5\). This pointwise example is on the original Wilson lattice. It refutes independent convolution of these new neighbors after the first integration. A joint estimate on the resulting normalizers could still give further damping.

## The remaining physical estimate

**PROVED.** There is a finite positive expression for the unresolved quantity at each cutoff. For \(k\in I_n\) let \(A_k=B^{1/2}H_k B^{1/2}\), \(z_k=\operatorname{Tr}A_k\), and put
\[
 p_k=\frac{\beta^k z_k}{\sum_{l\in I_n}\beta^l z_l},\qquad
 R_{kl}=\frac{\operatorname{Tr}(A_kA_l)}{z_k z_l}.
\]
Omit terms of zero weight. Each \(A_k/z_k\) is a density operator, so \(0\le R_{kl}\le1\) by positivity and the bound one on its operator norm. Equations (12)–(14) give
\[
           e^{-\Psi}=\sum_{k,l\in I_n}p_kp_l R_{kl}
                     +O\!\left(e^{-c_\eta m r^2/\beta}\right).           \tag{24}
\]
In fact the sum is exactly the purity of the retained state. Its log differs from the full log purity by the one- and two-cut probability estimates after (14).

**PROVED.** Fix the admissible spacing and limit hypotheses of Theorem ZD-c. An estimate sufficient for its two-stage physical seed is that, for some fixed physical side \(L\), \(n=L/a\) divisible by four and \(T=n/2\),
\[
          \limsup_{a\downarrow0}
               \sum_{k,l\in I_n}p_kp_l(1-R_{kl}) < 1/1651.              \tag{25}
\]
Indeed (24) would give \(\limsup\Psi<\log(1651/1650)\). For \(U=K/\|K\|\), \(\operatorname{Tr}U^{2T}\le\operatorname{Tr}U^T\) gives \(\log\operatorname{Tr}U^T\le\Psi\). This yields \(\limsup(\operatorname{Tr}U^T-1)<1/1650\) in the *full* physical space with its multiplicities. The construction and matching of a nontrivial continuum Yang–Mills theory and its full observable algebra are additional requirements. [Theorem ZD-c](gap-phys-seed.md)

**PROVED.** One can attempt (25) directly at an individual retained degree. Let \(P_T(k)\) and \(P_{2T}(k,l)\) denote the *untruncated* degree probabilities in (12). Exact cancellation of their degree weights gives
\[
                R_{kl}=e^{-\Psi}\,
                     \frac{P_{2T}(k,l)}{P_T(k)P_T(l)}.                   \tag{26}
\]
For instance take \(k_0\) nearest even to \(d_*\). On the good event in (13), \(|k_0-\lambda|\le mr+2\). The log mass expansion in (15) shows for one or both prescribed central degrees that the probability lies between \(\exp[-C_\eta(mr^2/\beta+\log(m\beta))]\) and one. For the lower bound the good event has probability tending to one. Consequently
\[
        |-\log R_{k_0k_0}-\Psi|
              \le C_\eta\big(m\beta^{-1-\eta}+\log(m\beta)\big).
\]
This controls the error in a *single* central degree when only its leading exponential cost is available. That error bound grows on the physical grid. Equation (25) needs a bound of order one with a specified margin.

**OPEN.** I cannot bound (25) at fixed physical \(L\). The Gaussian comparison can assign any positive limit in (18) to the same Wilson defect. The direct interacting estimate (21) retains a grid of long paths, and (23) exhibits the dependence created in the first attempt to extend it to short paths. The weak-cut estimate (11) controls degrees with exponentially little overlap with (14), as quantified by (16). The probabilities in (15) have the same rates in an actual Wilson example with a diverging defect and one with a vanishing defect. What remains in (24) is the normalized overlap of the *open-cylinder states at full-coupling degrees*. Neither their total statistical weight nor the cost of one link bounds that overlap to the accuracy in (25). All new arguments in this note are author-side hand derivations, pending independent checking. This research grants no scientific status.

RESULT — OPEN. At \(b=\lceil(2/5)\beta\log n\rceil\), the Wilson cut recovers the thermal defect with error at most \(n^{-9/25+o(1)}\), while its worst boundary-field log error grows as \(n^{3/5+o(1)}\). The estimate (25) at fixed physical size and the four-dimensional SU(2) Jaffe–Witten mass gap remain open.
