## Repo search

**GUIDE.** Row 1321 at `199e7dc32`. The row-specific prior file is absent at this revision. The target is a nontrivial four-dimensional continuum SU(2) Yang–Mills vacuum theory with \(\ker H=\mathbb C\Omega\), \(\Omega^\perp\ne0\), and \(\operatorname{spec}(H|_{\Omega^\perp})\subset[m_*,\infty)\) for some \(m_*>0\) in physical units. A finite-cutoff estimate will need constants that survive the continuum and infinite-volume limits.

**GUIDE.** The lead's November 8 digest covers main and PRs 10114, 10133, 10134 and 10141. The closest hits I checked in the source are the soft-route `MASS_GAP_LOCAL_BLOCK_ASTRA.md`, lines 4–14 and 106–149 (a one-step Wilson plaquette witness, with contraction at small bare coupling), Grok's `MASS_GAP_CROSSOVER_REDUCTION.md`, lines 77–90 (crossover and source transport are premises), and the hard-route `mass-gap-interface.md`, I1–I5 (spectral and identification conditions). Main at `8b11ae2bb9`, `research/mass-gap/library/gap-phys-seed.md`, lines 313–329, gives the conditional Theorem ZD-c relating a periodic thermal seed to finite-size energy and free-energy estimates. On PR 10141 at `a2f6a430e2`, `research/ym4d/library/fp1.md`, lines 299–315, bounds a constrained classical field at one ultraviolet scale. I searched the mass-gap and YM4D paths on the five refs for an entrywise modulus bound on the exterior-square kernel. The closest local result is row 1304 below. The registry search found no owner for this bound. [Lead's search](prior/repo-search-2026-11-08.md)

**GUIDE.** Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, distinguish kernel and operator positivity in their outline, lines 2119–2125. Lines 31860–31882 and CA-I lines 2704–2712, 3213–3222 give the scope of their scalar reconstruction and the separate mass-gap question. Both texts are at `31a47c543775`. Row 1218 records the conditional full-trace ascent of Deep Bhattacharjee, Ushashi Bhattacharya, James Montgomery Lockwood, Tristan Romanov, Ikailo John Sessford and Sanjeevan Singha Roy. Its one-scale thermal hypothesis at the tuned couplings is precisely the missing input on that route. The first four authors' coarse straight-path estimate concerns a restricted marginal. [Row 1218](prior/gap-onebound-read-sol.md)

**GUIDE.** Row 1304, §“Can the neutral slab determinant have one sign?”, treats the genuine neutral transfer on the spatial gauge and centre quotient. Its exchange-path argument rules out orienting all mixed minors to be positive. Row 1283, (29), separates true and independent neutral observations on a long periodic torus at short, growing lattice times. Row 1319, (20), leaves the physical-time Wilson thermal defect open. The file for check 1320 is absent at this pin. I use the first two results at their stated scopes. [Row 1304](gap-positivity-astra62.md) · [Row 1283](gap-solve32-astra62.md) · [Row 1319](gap-solve37-astra62.md)

## Attack on the first neutral excitation

**GUIDE.** The leading eigenvalue of the exterior square of the vacuum-normalized transfer gives the first excited energy. Its mixed kernel is signed. First try bounding the *size* of this operator after taking the absolute value on a slab of several time steps. A quantitative contraction at rate at least a fixed mass times the slab's physical thickness would bound every neutral excitation. The earlier orientation obstruction leaves this possibility open. I will compare the proposed contraction with a test that pairs two independent copies of the actual Wilson vacuum chain, then retain the signs and examine which cancellations can supply a bound.

**GUIDE (finite-volume notation).** On a periodic spatial cube let \(U\) be the Wilson transfer divided by its Perron eigenvalue on the full gauge-invariant slice space. The positive Perron vector \(\Omega\) has norm one and is invariant under all three spatial centre flips, since the flips preserve the transfer and its simple positive eigenvector. Let \(X\) be the slice quotient by vertex gauges and these flips, \(m_X\) the image of probability Haar, and \(K_t\) the kernel on \(X\) of \(U_+^t\), the neutral restriction at integer time \(t\ge1\). The integral over the timelike links and the finite centre average give a strictly positive symmetric kernel. It is also a positive semidefinite operator. Write \(\pi(dx)=\Omega(x)^2m_X(dx)\). The stationary pair law at separation \(t\) is
\[
 \rho_t(dx\,dy)=\Omega(x)K_t(x,y)\Omega(y)m_X(dx)m_X(dy).
 \tag{1}
\]
Both marginals are \(\pi\) by \(U_+^t\Omega=\Omega\). See row 1304 (12) for this symmetric Wilson convention and Sussman–Alpoge, outline 2315–2335, for the gauge-projected transfer trace. All estimates below are finite-volume identities or inequalities until a sequence is specified.

**PROVED (a test for the absolute kernel).** For \(X'=(x_1,x_2),Y'=(y_1,y_2)\) in \(X^2\) and the reference \(m_X^{\otimes2}\), put
\[
 F_t(X',Y')=K_t(x_1,y_1)K_t(x_2,y_2),\qquad
 G_t(X',Y')=K_t(x_1,y_2)K_t(x_2,y_1).
\]
Let \(D_t=(F_t-G_t)/2,\ S_t=(F_t+G_t)/2,\ C_t=|D_t|\), where the last operation takes the absolute value of each kernel entry. If \(u_1\) is the first excited eigenvalue of \(U_+\), then
\[
 u_1^t=\|D_t\|\le\|C_t\|\le1,\qquad D_sD_t=D_{s+t}.
 \tag{2}
\]
Indeed \(D_t=(U_+^t\otimes U_+^t)(1-\mathcal S)/2\), where \(\mathcal S\) exchanges the two replicas. In an orthonormal eigenbasis the antisymmetric tensors have eigenvalues \((u_i u_j)^t\) with \(i<j\), and the symmetric tensors are annihilated. Here \(u_0=1\). Replacing a test function by its absolute value gives the first norm inequality, and \(0\le C_t\le S_t\) pointwise gives the second by the same argument. The operator \(S_t\) has norm one because it is the tensor transfer followed by the orthogonal symmetric projection, and it fixes \(\Phi=\Omega\otimes\Omega\). These arguments use no ordering of the boundary tuples.

**PROVED.** Draw two independent pairs with law (1). Denote the law of all four variables by \(J_t\), and its image on exchanging \(y_1,y_2\) by \(J_t^\times\). Use \(d_{\rm TV}(P,Q)=\sup_A|P(A)-Q(A)|\). Then
\[
 \langle\Phi,C_t\Phi\rangle=d_{\rm TV}(J_t,J_t^\times)
 \ \ge\ 1-\rho_t(A^c)-(\pi\otimes\pi)(A)
 \tag{3}
\]
for every event \(A\subset X\times X\). The two four-variable densities are \(\Phi(X')F_t(X',Y')\Phi(Y')\) and the same expression with \(G_t\). Half their integrated absolute difference gives the equality. Reading just \((x_1,y_1)\) yields \(\rho_t\) in the first experiment and \(\pi\otimes\pi\) in the second. This proves the inequality. A reliable pairing test thus gives a *lower* bound on the norm proposed as an upper bound in (2).

## From a periodic Wilson test to the vacuum

**PROVED (change of boundary law).** For this paragraph use the full gauge-projected transfer \(U\) before averaging the centre. Let \(L_j\) denote its kernel to power \(j\), \(g_j=\log\operatorname{Tr}U^j\), and take an even time period \(N\) and \(1\le t<N/2\). Write \(P_{N,t}\) for the two-slice marginal on the ordinary periodic cylinder and \(Q_N\) for the product of its one-slice marginals. For an event \(E\) on the two neutral slices, lift it to the full slices. Then
\[
 \rho_t(E)^2\le e^{g_N}P_{N,t}(E),\qquad
 (\pi\otimes\pi)(E)\le e^{2g_N}Q_N(E).
 \tag{4}
\]
Indeed let \(B(x,y)=L_t(x,y){\bf1}_E(x,y)\). The lifted stationary expectation is \(\langle\Omega,B\Omega\rangle\). Projecting to neutral orbits gives (1), since independently averaging both end gauges and centre flips on an invariant integrand inserts the neutral projection. Cauchy–Schwarz bounds its square by \(\|B\Omega\|^2\). The positive-operator inequality \(|\Omega\rangle\langle\Omega|\le U^{N-2t}\) bounds this by \(\operatorname{Tr}(B^*B U^{N-2t})\). In that trace the three factors have nonnegative kernels. Dropping one of the two event indicators and integrating over its free variable leaves \(\int {\bf1}_E(x,y)L_t(x,y)L_{N-t}(y,x)\,dm_{\rm full}(x)dm_{\rm full}(y)\), which is the first right-hand side. For the second, \(L_N(x,x)=\int L_{N/2}(x,z)^2\,dm_{\rm full}(z)\ge\Omega(x)^2\), by testing the row against the unit vector \(\Omega\). The ordinary periodic one-slice density is \(e^{-g_N}L_N(x,x)\). Take products, then push forward. This argument uses the full periodic trace, as required for the event supplied by row 1283. The trace estimate with a restricted kernel in (4) is the method of that row's (37).

**PROVED, given rows 1283 (29) and 1153 (4).** Take dyadic ordinary \(N^4\) tori, \(\beta\to\infty,\ \beta\le B_0\log N\) with \(B_0\) fixed, and integers \(k\to\infty,\ k\le \beta^\delta,\ 0<\delta<1/48\). Write \(M=(N/k)^3\). There are \(c,C>0\), uniform along this sequence for all sufficiently large \(\beta\), such that
\[
 1-Ce^{-cM}\ \le\ \langle\Phi,C_k\Phi\rangle\ \le\ 1.
 \tag{5}
\]
Row 1283 (29) gives \(A\) with \(P_{N,k}(A^c)+Q_N(A)\le C_0 e^{-c_0 M}\) on these neutral orbit observations. To pay for (4), row 1153 (4) bounds \(2g_{N/2}-g_N\) by \(C N^3\beta^{-3/16}[\log(2+\beta)]^{9/8}\). Since \(g_j\) decreases, \(g_N\) satisfies the same upper bound. Its ratio to \(M\) tends to zero by \(k^3\le\beta^{3\delta}\). Equation (4) now gives \(\rho_k(A^c)+(\pi\otimes\pi)(A)\le Ce^{-cM}\), and (3) finishes the proof. This only uses the upper estimate on the short-period free energy. The thermal input builds on Sourav Chatterjee's weak-coupling comparison. [Row 1283, (29), (37)](gap-solve32-astra62.md) · [Row 1153, (4)](gap-solve6-astra62.md)

**PROVED (arbitrary subdivisions).** For every integer partition \(s_1+\cdots+s_b=T\) with \(1\le s_i\le k\),
\[
 1-bCe^{-cM}\ \le\
 \langle\Phi,C_{s_1}\cdots C_{s_b}\Phi\rangle\ \le\ 1.
 \tag{6}
\]
The absolute value of a composite integral is at most the integral of the absolute values, so \(C_k\le C_s C_{k-s}\le C_s S_{k-s}\) pointwise for \(s<k\). Applying the two vacuum factors gives \(\langle\Phi,C_s\Phi\rangle\ge\langle\Phi,C_k\Phi\rangle\). Each \(S_s\) fixes \(\Phi\). Telescope the difference of the products of the \(S\)'s and the \(C\)'s by replacing one factor at a time. In each term \(S_s-C_s\) has a nonnegative kernel. Replacing the surrounding \(C\)'s by \(S\)'s only increases its matrix element between the positive \(\Phi\)'s. The enlarged term is exactly \(1-\langle\Phi,C_s\Phi\rangle\). Summing gives (6), including unequal, noncommuting factors. For \(aN=L>0,\ aT\to\tau>0\), the left side tends to one since \(b\le T=O(N)\). Thus taking absolute values afresh on every such short slab cannot yield an upper bound \(e^{-m\tau}<1\) for the neutral excitation. This includes any kernel that pointwise dominates these absolute values on each slab. The signed composition equals \(D_T\). Its norm \(u_1^T\) can be smaller than the bound on the positive comparison.

## A slab of arbitrary finite thickness at fixed cutoff

**GUIDE.** Let the spatial side \(n\) now go to infinity at fixed isotropic \(\beta>0\) and fixed integer \(t\ge1\). No power of \(\beta\) bounds this \(t\). Two source results will be used at fixed coupling. The soft-route plaquette bound (11) in PR 10114 gives a number \(\eta_\beta>0\) independent of \(n\) for the one-step connected correlation of an elementary spatial plaquette. The all-mirror theorem of Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, gives invariance under interchanging axes for every periodic Wilson DLR state on the infinite lattice. Its definition of “periodic” includes every translation-invariant state. The theorem is applied after taking an infinite-volume DLR limit. The source proves it using finite-torus reflection arguments, pressure comparison and separation. Here its axis-interchange conclusion is an imported premise. [Plaquette bound, (7)–(11)](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/f76f6c649c/.claude/science/toe-ruleset-20261021/agents/ym4d-proof/MASS_GAP_LOCAL_BLOCK_ASTRA.md#L106-L178) · [All-mirror theorem, lines 2708–2771](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L2708-L2771)

**PROVED (with these fixed-coupling inputs).** On periodic spatial cubes,
\[
                \lim_{n\to\infty}\|C_{n,t}\|=1
                   \qquad(\beta>0,\quad 1\le t<\infty).
 \tag{7}
\]
Suppose \(\|C_{n,t}\|\le q\) along a subsequence for some \(0<q<1\). By (2) the true normalized neutral transfer on that subsequence has \(u_{1,n}\le u=q^{1/t}<1\). In its stationary vacuum path measure the temporal covariance of two real neutral time-slice functions of absolute value at most one, a distance \(j\) apart, is at most \(u^j\) in absolute value. Indeed it is the matrix element of \(U_+^j\) between their centered vacuum vectors, each of norm at most one.

**PROVED.** Use a real fundamental plaquette \(W=\tfrac12\operatorname{tr}U_p\) parallel to the \(2,3\) plane and let \(W_{i,j}\) be its translate by \(ie_1+je_0\). Put \(\mu_n=\mathbb E_n W\) in the stationary path measure. For every \(n\ge4\) the centered \(W\) vector has spectral measure on \([0,1]\), total mass \(v_n=\operatorname{Var}_n W\le1\), first moment at least \(\eta_\beta\) by the quoted bound. Jensen's inequality applied to \(z^t\) with the measure divided by \(v_n>0\) gives
\[
       \mathbb E_n W_{0,0}W_{0,t}-\mu_n^2
            \ge v_n(\eta_\beta/v_n)^t\ge \eta_\beta^t=:d>0.
 \tag{8}
\]
The local bound used here retains the spatial magnetic multiplier and the Perron vector. Its proof tensors the one-loop rank-one minorant for the kinetic convolution with the positive exterior operator, then cancels the exterior quadratic form by the local Perron comparison. Thus the same \(\eta_\beta\) applies at every spatial size. The lower bound can be extremely small at large \(t\).

**PROVED.** Pass to a further subsequence with a local weak limit \(\nu\) of the stationary full Wilson path measures and write \(\mu=\nu W\). One construction first takes the periodic time length to infinity at each fixed \(n\). The transfer powers converge in trace norm to the simple vacuum projector, since the positive transfer is trace class with all other normalized eigenvalues strictly below one. For a bounded cylinder insertion spanning a fixed number of layers, its transfer kernel is dominated in absolute value by its supremum norm times the unmarked kernel. It is a bounded operator, so trace-norm convergence of the remaining transfer powers gives the stationary boundary factors. Taking a diagonal subsequence on continuous cylinder tests gives the infinite lattice limit by compactness of the countable product of compact link groups. Each finite-region Wilson conditional kernel is continuous in a finite boundary and is eventually the same specification on those tori. Its conditional-integral identity passes to the limit against continuous exterior cylinder functions, then to bounded Borel tests by a monotone class argument. Thus \(\nu\) is Wilson DLR and is translation invariant. The time covariance bound above passes to each continuous local neutral slice function. The axis-interchange theorem therefore applies to the infinite-lattice state \(\nu\).

**PROVED.** In \(\nu\) average \(Z_i=W_{i,0}W_{i,t}\) over \(1\le i\le R\). The mean is at least \(\mu^2+d\) by (8). Interchanging axes \(0,1\) leaves the orientation \(2,3\) of the plaquette alone. It turns \(Z_i\) into the translate in time by \(i\) of the *single-slice* neutral reading \(W_{0,0}W_{t,0}\). Consequently \(|\operatorname{Cov}_\nu(Z_i,Z_{i+j})|\le u^j\). Under the experiment that draws the two end slices from independent copies of \(\nu\), the same average has mean \(\mu^2\). Its covariance at separation \(j\ge1\) is \((\mu^2+c_j)^2-\mu^4\), where \(c_j=\operatorname{Cov}_\nu(W_{0,0},W_{j,0})\). The same exchange of axes gives \(|c_j|\le u^j\), so this covariance has absolute value at most \(3u^j\). In both experiments the variance of the spatial average is at most
\[
            {1\over R}\left(1+6\sum_{j\ge1}u^j\right).
 \tag{9}
\]
This uses temporal clustering only as a consequence of the bound being tested in (7).

**PROVED.** Choose a continuous function valued in \([0,1]\) of this average, zero up to \(\mu^2+d/3\) and one from \(\mu^2+2d/3\). By (9) and Chebyshev its expectations in the two infinite-volume experiments approach one and zero as \(R\to\infty\). For each *fixed* \(R\) this is a bounded continuous function of the two finite sets of neutral spatial plaquettes. Its expectations along the chosen finite cubes converge to the respective expectations, including in the experiment with independent marginals. Inequality (3) applies to this test, by integrating its superlevel events. First choose \(R\) so the limiting difference exceeds \(q\), then take \(n\) large on the subsequence. This contradicts \(\|C_{n,t}\|\le q\), proving (7). In particular for any sequence of finite bare couplings \(\beta_j>0\) and integer slab thicknesses \(t_j\ge1\), the iterated limit with \(n\to\infty\) first is one. The result covers slabs of prescribed physical duration in this order of limits. Equation (7) gives no estimate uniform in \(t/n\) on a single physical cube.

## Reading the sign on one slab

**PROVED, given row 1283 (29).** On the sequence of (5) let \(A_{ij}\) be the short-time curvature test \(A(x_i,y_j)\). Call a pair of slice pairs directly matched when \(A_{11},A_{22}\) hold and \(A_{12},A_{21}\) fail. Call it cross-matched when these four decisions are reversed. Put \(h(X',Y')=1,-1,0\) in the direct, crossed and remaining cases respectively. Swapping either pair of boundary labels reverses \(h\). Row 1283 uses only bounded contractible spatial curvature readings, smeared at the dyadic side \(r\le k<2r\), to form \(A\). It uses a fixed threshold for differences between the paired and independent experiments. Thus \(h\) requires no evaluation of the Wilson transfer kernel. On two independent ordinary periodic \(N^4\) histories the probability of \(h\ne1\) is at most \(2P_{N,k}(A^c)+2Q_N(A)\) by a union bound. A diagonal pair has the genuine joint law and an off-diagonal pair has independent marginals.

**GUIDE (the curvature test).** In row 1283's notation each site reading is \(O_z=\exp(-|A_r(z)|^2)\), with
\[
 A_r(z)=r^{-1}\sum_w\phi(w/r)\operatorname{Ad}(U_{\gamma_{z,w}})
                  \sqrt\beta\,\operatorname{Im}U_{12}(z+w).
\]
Here \(\phi\) is the fixed real, separately even bump of positive integral from that row and \(\gamma_{z,w}\) is the coordinate-ordered spatial path from \(z\) to \(z+w\). Each tile averages \(O_z(x)O_z(y)\) over the prescribed \(L_0^3\) grid sites. Its threshold is strictly between the independent limiting mean and the least paired limiting mean at \(1\le k/r\le2\), whose strict separation is proved in row 1283 after (29). Event \(A\) requires strictly more than half the tiles to reach the threshold. This fixes a measurable test on the two spatial configurations before any comparison of closing conditions. [Spatial smearing](gap-solve26-astra62.md) · [Threshold and tile bound](gap-solve32-astra62.md)

**PROVED.** The sign of the neutral mixed minor can be read with vanishing error in the following measure built from the Wilson kernel. Give the four boundary variables probability proportional to \(\Phi(X')C_k(X',Y')\Phi(Y')\,dm_X^{\otimes2}(X')dm_X^{\otimes2}(Y')\), with normalizer \(b_k=\langle\Phi,C_k\Phi\rangle\), and denote this probability by \(\xi_k\). Write \(\sigma_k=\operatorname{sgn}D_k\) where its density is nonzero. For any bounded test \(H\),
\[
  b_k\,\mathbb E_{\xi_k}[\sigma_k H]
              =\tfrac12\left(\mathbb E_{J_k}H-\mathbb E_{J_k^\times}H\right).
 \tag{10}
\]
This is the signed version of (3). Using (4) for the four decisions, the probability of a wrong or missing direct match under \(J_k\) is at most \(C e^{-cM}\). Under \(J_k^\times\) the corresponding correct reading is \(-1\). Hence \(\mathbb E_{\xi_k}[\sigma_k h]\ge1-C'e^{-c'M}\), using \(b_k\le1\). In particular a wrong or missing sign has probability at most \(C'e^{-c'M}\).

**PROVED (which observations suffice).** Restrict each of the four endpoints to the same single-slice observations. Write \(P\) for conditional expectation on the observed single-slice algebra in \(L^2(\pi)\). Conjugate the transfer by the vacuum, so the vacuum is \(1\), and write \(P U_+^k P\) for the compressed operator in this representation. If its trace excess above one is \(\epsilon\), then for *every* \(|H|\le1\) of the four restricted observations,
\[
       b_k |\mathbb E_{\xi_k}[\sigma_k H]|
                \le \epsilon\sqrt{1+\epsilon^2/2}.
 \tag{11}
\]
Indeed the observed one-pair law has density the kernel of that compression relative to the product of the observed marginals. This follows by testing (1) against products of single-end functions. Pushing the two-replica signed difference forward gives the kernel of its exterior square, with the factor \(1/2\) of (10) built in. Its integrated absolute value is at most its Hilbert–Schmidt norm by Cauchy–Schwarz on probability space. If \(1,\lambda_1,\ldots\) are the eigenvalues of the compression, that squared norm is \(\sum_i\lambda_i^2+\sum_{1\le i<j}\lambda_i^2\lambda_j^2\), with the first sum over \(i\ge1\). Positivity and \(\sum_{i\ge1}\lambda_i=\epsilon\) give (11). Row 1231 (40) and its grid and winding extension give \(\epsilon\to0\) for any fixed finite regular grid of complete fixed-lattice-side patches, also jointly with the neutral readings of all the straight windings specified there. Its proof for fixed grids works at every \(k\to\infty\), and its winding comparison is uniform in \(k\ge2\). Equations (5) and (11) therefore bound the best success probability of even a joint four-end sign decision from these restricted data by \(1/2+o(1)\). The distributed curvature test in (10) has success probability tending to one. The trace input on patches and windings is due to row 1231. [Row 1231, (37)–(40) and the paragraph following (40)](gap-solve26-astra62.md)

## Keeping the signs around a physical time circle

**PROVED (exact finite-volume identity).** Let \(T=bk\), \(b\ge2\), and write \(z_T=\operatorname{Tr}U_+^T\). Use the positive probability on a circle of \(b\) ordered pairs of neutral slices, of density proportional to \(\prod_{j=0}^{b-1}S_k(X'_j,X'_{j+1})\) with \(X'_b=X'_0\). It also defines a law on unordered slice pairs. At each edge draw a temporary label \(\ell_j=+1\) for a direct continuation or \(-1\) for a crossed continuation, conditionally independently with probabilities \(F_k/(F_k+G_k)\) and \(G_k/(F_k+G_k)\). Then
\[
 \mathbb E\prod_j\ell_j
 ={\operatorname{Tr}D_T\over\operatorname{Tr}S_T}
 ={z_T^2-z_{2T}\over z_T^2+z_{2T}}
 =\tanh\!\left({2\log z_T-\log z_{2T}\over2}\right).
 \tag{12}
\]
Conditional expectation inserts \(D_k/S_k\) at each edge. Multiplication around the circle gives the ratio of traces, since both the symmetric and the antisymmetric projection commute with the tensor transfer. The replica-exchange trace \(\operatorname{Tr}[(U_+^T\otimes U_+^T)\mathcal S]=z_{2T}\) follows by summing in an eigenbasis. The same identity holds on the full physical slice space. Changing the ordering at one slice flips its two incident continuation labels and preserves the parity in (12). The purity identity itself is prior work. Row 1155 (10) uses the affinity of *antipodal* slices. Row 1283 (34)–(35) recovers *spatial centre twists* on a time circle. The issue here is whether local curvature readings determine the *replica* parity measuring the ordinary thermal defect. [Replica purity](gap-solve7-astra62.md) · [Reconstruction of centre twists](gap-solve32-astra62.md)

**PROVED, using the tile estimate in row 1283 (29).** The test in (10) may use any prescribed collection of \(m\) of that proof's spatial tiles, by taking its majority over this collection. In each of the two experiments (genuine, independent), its proof bounds the probability that any specified \(j\) tiles give the wrong threshold decision by \(\exp(-cL_0^3 j)\), where each tile has spatial side \(8L_0 r\), \(r\le k<2r\). The proof takes \(L_0\) fixed large enough to absorb the choices in a majority. A union bound on these \(m\) tiles alone gives error at most \(2^m\exp(-cL_0^3m/2)\le e^{-c' m}\). Hence the direct matching fails with probability at most \(4e^{-c'm}\) on two ordinary \(N^4\) tori. All four tests use the very same tiles.

**PROVED (comparison of aspect ratios and closing conditions).** Return to dyadic \(N\) and take \(k\to\infty\) dyadic, \(k\le\beta^\delta\), \(0<\delta<1/48\). Fix \(0<\alpha\le A_0<\infty\) and require \(\alpha N\le T=bk\le A_0 N\). Fix \(\delta<\delta_1<\delta_2<1/16\), \(h_0=\lfloor\beta^{\delta_2}\rfloor\), and take
\[
                   m=\left\lceil (N/\beta^{\delta_1})^3\right\rceil.
\]
There are enough tiles since \(k/\beta^{\delta_1}\to0\). The \(m\) tiles fit in a spatial cube of side \(O(km^{1/3})=o(N)\), including the margins needed for the paths of the contractible readings. In the positive law of (12), the corresponding local sign \(h_j\) disagrees with \(\ell_j\), counting zero as a disagreement, with probability at most \(e^{-c_\alpha m}\) on *each* edge. This holds for both choices of spatial sector in (12).

**PROVED (proof of the comparison).** Work first on the tensor product of two full physical slice spaces. Set \(V=U\otimes U\), let \(B(X',Y')=V^k(X',Y'){\bf1}_{h(X',Y')\ne1}\), and put \(b(s)=\operatorname{Tr}(B^*B V^s)\). The kernel sandwich of (4), with \(V\) in place of \(U\), gives
\[
 b(N-2k)\le 4\exp(2g_N-c'm),\qquad
 b(h_0)\le\operatorname{Tr} V^{2k+h_0}\le \exp(2g_{h_0}).
 \tag{13}
\]
For the second bound drop both event indicators in the integral. Row 1153 (5) yields \(g_{h_0}=O((N/h_0)^3)=o(m)\). Its condition \(h_0^4\beta^{-1/4}[\log(2+\beta)]^{3/2}\to0\) follows from \(\delta_2<1/16\), and the cube-size condition follows from \(\beta\le B_0\log N\). Also \(g_N,g_T\le g_{h_0}\). The spectral expansion of \(b(s)\) has coefficients \(\|Bv_i\|^2\ge0\) in an eigenbasis of \(V\), so it decreases and is log-convex by Hölder. If \(T\le N\), the interpolation coefficient of \(N-2k\) at \(T-2k\) between \(h_0\) and \(N-2k\) is bounded below by a positive constant depending on \(\alpha\). If \(T>N\), use decrease. In either case (13) gives \(b(T-2k)\le e^{-c_\alpha' m}\).

**PROVED.** Let \(P_*\) be the identity on both full replicas or the orthogonal centre-neutral projection on each replica, tensored together. Put \(L=P_*(1+\mathcal S)/2\). A marked edge in the positive symmetric circle has unnormalized disagreement weight
\[
           \operatorname{Tr}(B V^{T-k}L)
       \le b(T-2k)^{1/2}\big(\operatorname{Tr}V^T\big)^{1/2}.
 \tag{14}
\]
For the identity on replicas the two marked summands are the bad direct kernel \(B\) and \(B\mathcal S\), since \(h\) changes sign under an end swap. On the neutral space independent centre averaging of the endpoint variables commutes with the bad-event indicator, which is invariant under every such flip. It therefore gives the compression \(P_* B P_*\) there. The other edges sum to the symmetric tensor transfer, which proves the trace expression. The bound is Hilbert–Schmidt Cauchy–Schwarz on \(BV^{(T-2k)/2}\) and \(V^{T/2}L\). The latter has squared Hilbert–Schmidt norm at most \(\operatorname{Tr}V^T\), since \(L\) is an orthogonal projection commuting with \(V\). The normalizer \(\operatorname{Tr}V^T L\ge1\) contains the two-vacuum state. The last factor in (14) is \(e^{g_T}=e^{o(m)}\). This proves the claimed one-edge error.

**PROVED.** Using only the local curvature data on the selected tube, form \(W_{\rm pair}=\prod_{j=0}^{b-1}h_j\). At each sampled time the observation is an unordered pair of spatial arrays on the tube. The association of sites within each array is part of the observation. Exchanging the two complete arrays at any slice preserves the product. The union bound and (12)–(14) give
\[
 \left|\mathbb E W_{\rm pair}
       -{z_T^2-z_{2T}\over z_T^2+z_{2T}}\right|
          \le 2(T/k)e^{-c_\alpha m}.
 \tag{15}
\]
At \(aN=L_{\rm phys}\) fixed, the spatial side of the observation tube tends to zero in physical units while it wraps the physical time circle. All probabilities are in the stated positive symmetric-circle ensemble. Computing this expectation under two independently labelled periodic histories would change the ensemble and fix the true parity to \(+1\).

## Testing the physical parity bias

**PROVED (the size of the estimate needed).** On the weak-coupling sequence of (5), fix the aspect integer \(K\) from row 1161's neutral criterion and choose a fixed dyadic \(K'\ge K\). On the admissible dyadic grids take \(T=N/K'\), with \(k\mid T\) eventually. Set \(J_+(T)=2\log z_T-\log z_{2T}\). As \(1\le z_{2T}\le z_T\), one has \(\log z_T\le J_+(T)\le2\log z_T\). Consequently a physical side with
\[
             \limsup_{a\downarrow0}\mathbb E W_{\rm pair}<1/5
 \tag{16}
\]
in the *neutral* symmetric circle would give \(z_T-1<1/2\) for all sufficiently fine cutoffs on this grid. Indeed \((1+1/5)/(1-1/5)=3/2\), and (15) has vanishing error. This feeds row 1161 with its other stated hypotheses, including its flux alternatives. In the full ensemble (15) measures the full doubling defect. The One-Bound result has an additional window of spatial shapes. This argument has only used cubes. The continuum limit and its generating observables are separate inputs. [Neutral seed and alternatives](gap-solve9-astra62.md) · [Full thermal window](prior/gap-onebound-read-sol.md)

**PROVED (a test of independent randomization).** In the positive circle each proper subset of the true edge signs \(\ell_j\) consists of independent fair signs *even after conditioning on their total parity*. To see this, independently exchange the two copies at vertices with chosen bits \(v_j\in\{\pm1\}\). Product reference measure and the marked joint density are invariant when \(\ell_j\) is replaced by \(v_j\ell_jv_{j+1}\). Transitivity on the \(2^{b-1}\) strings of a given parity follows by solving successively for \(v_{j+1}\) from \(v_j\). The last equation holds precisely when the two parities agree. For any assignment on a proper subset there are equally many extensions in that parity class. The same argument applies to the observed signs \(h_j\) conditional on their all being nonzero and on their product. Thus exact fair local signs, including on \(b-1\) edges at once, impose no small upper bound in (16).

**PROVED (two ordinary Wilson closing conditions).** Denote by \(P_{\parallel}\) the circle with direct pairings on every edge and by \(P_\times\) the circle with one crossed seam, normalized in each case. In the full space these are two independent period-\(T\) histories and the two halves of a single period-\(2T\) history. For neutral \(U_+\) the same statements use its centre-averaged paths. Their weights in (12) are respectively \(z_T^2/(z_T^2+z_{2T})\) and \(z_{2T}/(z_T^2+z_{2T})\). The first is at least \(1/2\). The second is at least \(1/(2e^{2g_T})=\exp[-o(m)]/2\), since \(z_T\le e^{g_T}\), \(z_{2T}\ge1\). Condition the error probability in (15)'s union bound on either parity. Changing the vertex orderings turns any pattern of that parity into the corresponding canonical pattern, preserving the observed product. Absorbing \(b\) and \(e^{2g_T}\) in the exponent gives
\[
 P_{\parallel}\{W_{\rm pair}\ne 1\}
       +P_\times\{W_{\rm pair}\ne-1\}\le C_\alpha e^{-c_\alpha m}.
 \tag{17}
\]
Thus this single spatial tube distinguishes the two actual closing conditions even if the relative partition weight of one is small. Any mixture of these same two conditional laws keeps their conditional accuracies. The Wilson partition functions specify which mixture occurs in (12).

**PROVED (cost of a direct seam comparison).** On the common space of ordered slice pairs let \(R=G_k(X'_{b-1},X'_0)/F_k(X'_{b-1},X'_0)>0\), with the chosen full or neutral kernels. Write \(J(T)=2\log z_T-\log z_{2T}\) for that choice. Then \(\mathbb E_{\parallel}R=z_{2T}/z_T^2=e^{-J(T)}\) and \(dP_\times/dP_{\parallel}=R/\mathbb E_{\parallel}R\). Both relative entropies between the two closing laws are at least \(c_\alpha' m\) for sufficiently fine cutoffs. In fact if \(p=P_{\parallel}(W_{\rm pair}=1)\), \(q=P_\times(W_{\rm pair}=1)\), integrating the convex function \(x\log x\) on this event and its complement bounds \(D(P_{\parallel}\Vert P_\times)\) below by the binary relative entropy. That is at least \(p\log(1/q)-\log2\). Equation (17) yields the claimed lower bound. Use \(W_{\rm pair}=-1\) for the reverse bound. In particular
\[
 \log\mathbb E_{\parallel}R-\mathbb E_{\parallel}\log R
       =D(P_{\parallel}\Vert P_\times)\ \ge c_\alpha' m,\qquad
              0\le J(T)\le 2g_T=o(m).
 \tag{18}
\]
A Jensen lower bound on the ratio using the undeformed periodic ensemble therefore loses a quantity diverging on the physical cube. This is an estimate in the actual Wilson measures for the seam after an entire \(k\)-step slab has been integrated. One can test whether resampling a tube could change its parity. Place a second disjoint tube of the same size elsewhere. Both observed products equal the same true parity outside an event of probability at most \(2b e^{-c_\alpha m}\) in the symmetric circle. The mean conditional variance of the first product given all observations outside its tube is at most \(8b e^{-c_\alpha m}\), by using the second product as predictor and bounding squared error by four. Neither randomizing a local reading nor the high accuracy of the parity decision supplies the relative weights.

## Can positivity bound the remaining signed coefficient?

**PROVED.** On the neutral cube, assigning a real multiplier \(v_j\) to the signed kernel at each edge gives the polynomial
\[
 \frac{\operatorname{Tr}\prod_{j=0}^{b-1}(S_k+v_jD_k)}
      {\operatorname{Tr}S_T}
       = 1+\eta_T\prod_{j=0}^{b-1}v_j,\qquad
 \eta_T=\frac{z_T^2-z_{2T}}{z_T^2+z_{2T}} .
 \tag{19}
\]
This follows from \(D_k S_k=S_k D_k=0\), since they act on orthogonal exchange sectors. An independently established nonnegative trace for a choice with negative product of modulus greater than five would give \(\eta_T<1/5\). This would suffice at the aspect in (16) with a uniform margin above five.

**PROVED (extent of entrywise positivity).** Let \(\gamma_k=\operatorname*{ess\,sup}|D_k|/S_k\), well defined by the strict positivity of \(S_k\). The entries of \(S_k+v D_k\) are nonnegative almost everywhere exactly for \(|v|\le1/\gamma_k\), with the usual infinite-radius convention at \(\gamma_k=0\). The range of \(D_k/S_k\) is symmetric in essential supremum and infimum by an exchange of the two end labels. Also \(b_k\le\gamma_k\), by integration against \(\Phi(X')\Phi(Y')\) and \(S_k\Phi=\Phi\). Hence on the physical sequence of (5), pointwise positivity of every factor in (19) only permits
\[
          \left|\prod_j v_j\right|
              \le (1-C e^{-cM})^{-b}=1+o(1).
 \tag{20}
\]
Here \(b=O(N)\) and \(M=(N/k)^3\). Positivity as an *operator* permits every \(v_j\ge0\), but then both terms in (19) have the same sign. Achieving the needed negative product requires a signed estimate on the trace after sewing the slabs together. Neither the pointwise extension in (20) nor Jensen's inequality in (18) gives it.

**OPEN.** At a fixed admissible physical side the signed estimate must control the frequency of the crossed closure. For (16) the sufficient margin is a limiting lower probability strictly above \(2/5\), equivalently a limiting upper \(\eta_T\) strictly below \(1/5\). The bounds on \(g_T\) used in (13) permit that probability to tend to zero. Equation (17) controls identification within each ensemble. The comparison of their Wilson partition weights remains open. The construction of a nontrivial continuum Yang–Mills vacuum theory with its full observable algebra also remains open in this argument. All new arguments here are author-side hand arguments with the cited inputs. No numerical run or independent check was used for them.

RESULT — OPEN. The four-dimensional SU(2) Jaffe–Witten mass gap remains unproved. Equations (6) and (7) exclude the entrywise absolute-kernel bound in their stated limits. Equations (15) and (17) recover the replica closing condition from a shrinking spatial tube on a physical cube. The Wilson sector-weight estimate (16) and the nontrivial continuum construction remain open. Research only, with no status granted.
