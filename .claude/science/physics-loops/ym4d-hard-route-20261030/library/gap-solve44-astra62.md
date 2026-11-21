## Repo search

**GUIDE.** Row 1337 is author research at commit `345573e25` and grants no scientific status. The row-specific prior note is absent. The target is a nontrivial continuum SU(2) Yang–Mills theory on four-dimensional spacetime with a strictly positive physical gap above its vacuum.

**GUIDE.** The lead's November 8 search found ultraviolet estimates and earlier soft-route results. I checked the gap passages identified in row 1218 against the repository refs. PR 10114 (`f76f6c649c`, `MASS_GAP_LOCAL_BLOCK_ASTRA.md`, 4–14, 106–149) has a one-step loop witness and contraction at small bare coupling. Grok's PR 10133 (`89faef229f`, `MASS_GAP_CROSSOVER_REDUCTION.md`, 77–90) leaves crossover clustering and source transport open. PR 10134 (`1e70c7211a`, `mass-gap-interface.md`, I1–I5) distinguishes spectral exclusion from nontriviality and identification. PR 10141 (`a2f6a430e2`, `fp1.md`, 299–315) bounds a constrained classical minimizer. The closest thermal estimate on main (`8b11ae2bb9`, `research/mass-gap/library/gap-phys-seed.md`, Theorem ZD-c) propagates a strictly small excited trace at one physical size, conditional on its inputs. I found no owner of this physical estimate in the open registry. A targeted search of the YM4D and mass-gap paths on those refs and PR 10144 for crossed affinity and heat noise on observed slices returned no matches. [Lead's search](prior/repo-search-2026-11-08.md) · [Thermal seed theorem](gap-phys-seed.md) · [Ownership registry](open-registry.md) · [Literature comparison](prior/gap-onebound-read-sol.md)

**GUIDE.** Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, distinguish the action-density sector from the full gauge theory and polynomial decay from spectral exclusion. I checked outline lines 581–599 and 31858–31882 and CA-I lines 2704–2713 and 3213–3224 at `31a47c543775`. Row 1218 records a conditional thermal ascent by Bhattacharjee, Bhattacharya, Lockwood, Romanov, Sessford and Singha Roy, cube dynamics estimates by the first four authors, and conditional spectral criteria by Zeng Chunping. I use the distinction between a thermal seed and a bound on one eigenvalue. Row 1336 checks the two replica periods in row 1334 and specifies the bare-coupling hypotheses needed for its interpolation. Rows 1331 and 1335 leave uniform transport from finite data open. No numerical estimate enters the argument. [Outline, scalar sector and spectral support](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L31858-L31882) · [Complete account I](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L2704-L2713) · [Outline index](sa-index/README.md) · [Row 1336](gap-solve43-check-opus.md) · [Finite-data check](gap-shrink-box-check-astra.md)

## Which part of the two-period weight can be estimated?

**OPEN.** Take lattice spacings \(a_j\downarrow0\) and write \(n=L/a_j\), \(4\mid n\), \(T=n/2\), where \(L=2^i\ell_1\) is fixed, \(i\) is a nonnegative integer and \(\ell_1/(4a_j)\) is an integer at least three for all sufficiently large \(j\). The sufficient target used in row 1334 is \(\limsup_j Z(n,T)^2/Z(n,2T)<1651/1650\) along the trajectory constructing the theory. Spatial and temporal plaquettes have the same Wilson coupling. My approach is to compare the joint law of the two opposite slices of the period-\(T\) torus with the law in which the two end readings from independent samples are exchanged. Convolution of an observed slice with independent SU(2) heat noise gives a continuous family of such comparisons. The estimate in (8) uses time reflection on the periodic Wilson lattice. Equation (16) specifies the part of the unsmoothed ratio that remains open.

**GUIDE.** Rows 1186 and 1211 already relate slice data, information and the transfer spectrum. Row 1321 treats the signed two-replica transfer. Row 1330 factors angular heat flow out of the Wilson electric transfer. Here the heat acts on an observation drawn *after sampling the ordinary Wilson measure*. Its time parameter has no physical units. The physical transfer is that of Osterwalder–Seiler and Lüscher, also developed by Ethan Sussman and Levent Alpoge with Claude and Codex, outline GL3 and GL8. [Slice information](gap-solve19-astra62.md) · [Wall observations](gap-solve22-astra62.md) · [Replica transfer](gap-solve38-astra62.md) · [Electric heat factor](gap-solve42-astra62.md)

## A positive integral for the thermal deficit

**PROVED (finite box).** Set \(t=T/2\), let \(F\) be the physical Wilson transfer in the symmetric magnetic sandwich convention, and write \(K_t(x,y)\) for the strictly positive symmetric kernel of \(F^t\) with respect to product spatial Haar probability \(dx\). Use a common electric normalization at every time. In the ordinary period-\(T\) measure the opposite-slice density is \(p(x,y)=K_t(x,y)^2/Z_T\), with \(Z_u=\operatorname{Tr}F^u\). Write \(z_u=Z_u/\|F\|^u\) for the trace normalized by the vacuum eigenvalue, and \(\operatorname{Re}U=\tfrac12\operatorname{tr}U\) for a unit quaternion. This follows by cutting both time arcs and integrating their disjoint interiors. Vertex gauge integration makes the density invariant under independent vertex gauges at the two ends. This squared-kernel identity is prior work. [Row 1171](gap-solve14-astra62.md)

**PROVED.** Identify SU(2) with the unit round three-sphere. Let \(H_s\) diffuse every link of the first slice independently, with generator \(\frac12\sum_e\Delta_e\). Write \(p_s=H_s^x p\). On two independent samples form the densities
\[
 P_s=p_s(x,y)p_s(x',y'),\qquad Q_s=p_s(x,y')p_s(x',y),\qquad
 A(s)=\int\sqrt{P_sQ_s}.
\]
Here and below the reference for each link is normalized Haar. The four half-cylinder kernels at \(s=0\) close to a single time circle of length \(4t\) in the order \(x,y,x',y'\). Therefore
\[
 A(0)=Z_{2T}/Z_T^2,\qquad A(\infty)=1.                                      \tag{1}
\]
The latter equality follows because at fixed finite box the heat kernel in \(x\) converges uniformly to one. If \(v_e(x,y;s)=\nabla_{x_e}\log p_s(x,y)\), then
\[
 A'(s)=\frac14\sum_e\int\sqrt{P_sQ_s}\,
       |v_e(x,y;s)-v_e(x,y';s)|^2.                                         \tag{2}
\]
Indeed \(P_s,Q_s\) both satisfy the heat equation in \((x,x')\). Differentiate the affinity and integrate by parts on the compact group. Each variable contributes \(\frac18\int\sqrt{P_sQ_s}|\nabla\log(P_s/Q_s)|^2\). The contributions from \(x,x'\) agree by interchanging the two samples. All finite-box densities at zero noise are smooth and strictly positive. Integration of (2), followed by the large-noise limit at that box, gives \(1-Z_{2T}/Z_T^2=\int_0^\infty A'(s)\,ds\). Thus the strict upper bound needed on its cutoff limsup at one physical side is \(1/1651\). No cancellation between different noise times is available.

**PROVED (what the integrand measures at zero noise).** Orient a spatial link \(e\) on slice \(x\). In the Wilson bridge from \(x\) to \(y\), let \(J_e\) be the gradient at \(x_e\) of the normalized real trace of its one inward temporal plaquette. Both gradients being compared live in the same tangent space. Differentiation of the integral for \(K_t\) gives
\[
 v_e(x,y;0)=-\nabla_{x_e}V(x)+2\beta\,\mathbb E[J_e\mid x,y],
\]
where \(V\) includes the spatial coupling. The derivative of the initial half magnetic weight gives the first term after squaring the kernel. Only one time-like plaquette of this half-cylinder contains \(x_e\). The other arc from \(x\) uses the same definition with time reversed. In (2) the magnetic terms cancel. Dividing \(\sqrt{P_0Q_0}\) by \(A(0)\) gives exactly the four equally spaced slice marginals of the ordinary period-\(2T\) Wilson law. Consequently
\[
 \frac{A'(0)}{A(0)}
 =\beta^2\sum_e\mathbb E_{2T}
  \left|\mathbb E[J_e^+\mid X,Y]-\mathbb E[J_e^-\mid X,Y']\right|^2.       \tag{3}
\]
Here \(Y,Y'\) are the endpoints at time \(\pm t\) from \(X\), and the inner expectations are in the indicated single bridges. In the quaternion metric \(|J_e|^2=1-(\operatorname{Re}U_p)^2\le2(1-\operatorname{Re}U_p)\). The singleton case of row 1334 (5) gives \(\mathbb E(1-\operatorname{Re}U_p)\le C/\beta\) by Jensen. Conditional Jensen in (3) yields \(0\le A'(0)/A(0)\le C n^3\beta\). This estimate still grows with the number of links. [Plaquette moment estimate](gap-solve43-astra62.md)

## A volume-uniform conditional density at large observation noise

**PROVED.** Let \(N=n^3\), \(n\ge8\) even. For a fixed spatial connection \(b\), draw independent Haar vertex gauges \(g_v\) and then diffuse each link of \(g.b\) for time \(s\). Write \(k_s^b\) for the output density and \(k_s^{\mathbf1}\) for the density obtained from the identity connection. If \(w_s=1+r_s\) is the one-link heat density, then, for \(s\ge1\),
\[
 \delta=\|r_s\|_\infty\le C_0 e^{-3s/2}.
\]
Indeed the SU(2) character of dimension \(d\) is \(\chi_d(\theta)=\sin(d\theta)/\sin\theta\). The radial Laplacian \(\partial_\theta^2+2\cot\theta\,\partial_\theta\) has eigenvalue \(-(d^2-1)\) on this function. Orthogonality and completeness on central functions follow from the sine basis and radial Haar measure \((2/\pi)\sin^2\theta\,d\theta\). At the identity \(\chi_d=d\), so \(w_s=\sum_{d\ge1}d\,e^{-(d^2-1)s/2}\chi_d\). The bound follows from \(|\chi_d|\le d\) and summing the Gaussian tail.

**PROVED (revealing a link).** Expose the links in any deterministic order. For a set \(S\) of previously exposed edges and the next edge \(e\), let \(b_e^S(z_e\mid z_S)\) denote the one-edge conditional density for input \(b\). For numerical constants \(s_0,C\), every \(s\ge s_0\) satisfies
\[
 b_e^S=1+\sum_{p:\,e\in\partial p,\;\partial p\setminus\{e\}\subset S}
       \sum_{d\ge2}e^{-2(d^2-1)s}\chi_d(b_p)\chi_d(z_p)
       +R_e^S,\qquad |R_e^S|\le C e^{-15s/2}.                              \tag{4}
\]
Here \(b_p,z_p\) are consistently oriented plaquette holonomies. The bound is uniform in the input, exposed values, order and box. Also \(1-\delta\le b_e^S\le1+\delta\) since it is a posterior average of the single-edge heat density.

**PROVED (expansion with a local denominator).** Let \(D_S\) be the observed density on \(S\), the vertex-gauge integral of \(\prod_{j\in S}(1+r_j)\), with \(r_j=r_s(z_j((g.b)_j)^{-1})\). Expand the product. The contribution of a chosen connected set of edges \(B\) is \(h_B=\int\prod_{j\in B}r_j\,dg\), bounded by \(\delta^{|B|}\). Different vertex-disjoint components factor. A component with a leaf has zero integral by Haar integration over its leaf gauge. Group all terms of \(D_{S+e}-D_S\) according to the component \(B\) containing \(e\). Exactly,
\[
 \frac{D_{S+e}}{D_S}-1
 =\sum_{B\ni e}h_B\frac{D_{S\setminus I(B)}}{D_S},
\]
where \(B\) is connected in \(S\cup\{e\}\) and \(I(B)\) consists of the edges incident to its vertices. By positivity of the **unexpanded** products, the quotient is between \((1+\delta)^{-6(|B|+1)}\) and \((1-\delta)^{-6(|B|+1)}\). Doubling the edges of a connected set of size \(k\) containing \(e\) gives a length-\(2k\) traversal from an endpoint of \(e\). Its visited edges specify the set, giving at most \(2\,6^{2k}\) possibilities. Choose \(s_0\) so that \(36\delta(1-\delta)^{-6}<1/2\) and \(\delta<1/2\). Sizes \(k\ge5\) then sum to at most \(C\delta^5\). The only smaller nonzero components are four-edge elementary squares, since the cubic torus has no shorter cycle and \(n\ge8\). For a square the quotient equals \(1+O(\delta)\), with a uniform constant. This costs at most \(C\delta^5\) more in total.

**PROVED (the square coefficient).** On the four edges of a square, every proper nonempty support has a leaf. The full density there is \(1+h_{\partial p}\). It depends only on the conjugacy class of \(z_p\), by fixing a tree of three edges and averaging the remaining root conjugation. The class of the product after four independent central heat increments has the distribution of the class of \(b_p\) diffused for time \(4s\). Conjugating increments or reversing an edge preserves their central heat laws. Thus the expectation of \(\chi_d(z_p)\) is \(e^{-2(d^2-1)s}\chi_d(b_p)\). Under product Haar, \(z_p\) is Haar. Character orthogonality proves the coefficient in (4), including its normalization.

**PROVED (relative entropy estimate).** Write \(a_p(b)=1-\operatorname{Re}b_p\). The normalized noisy orbit satisfies
\[
 D(k_s^b\Vert k_s^{\mathbf1})
 \le C e^{-12s}\sum_p a_p(b)^2 + C N e^{-15s},\qquad s\ge s_0.             \tag{5}
\]
For \(b_p\) of eigenangle \(\theta\), the character is a sum of weights \(e^{im\theta}\) with \(|m|<d\). Since \(1-\cos(m\theta)\le m^2(1-\cos\theta)\), one has \(|\chi_d(b_p)-d|\le d^3a_p(b)\). The difference of the two conditional densities in (4) is bounded by \(C e^{-6s}\sum_{p\ni e}a_p(b)+C e^{-15s/2}\). Conditional relative entropy is at most the integral of the squared difference divided by the reference conditional density, by \(\log u\le u-1\). Its denominator is at least \(1-\delta\). Apply the relative entropy chain rule in the chosen edge order, use the bounded number of squares at any edge and sum, proving (5).

## The part of the positive integral erased by noise

**PROVED (ordinary Wilson measure).** Let \(m(y)\) be the marginal of the unsmoothed opposite slice. Conditional on \(Y\), the Wilson law of \(X\) is vertex-gauge invariant. Thus \(p_s(\cdot,y)/m(y)\) is exactly a mixture of \(k_s^X\) with the conditional Wilson weights. The singleton exponential moment in row 1334 (5) gives \(\mathbb E a_p(X)^2\le C/\beta^2\) on every plaquette, independently of the periods. Convexity of relative entropy in its first argument and (5) yield
\[
 D(p_s\Vert k_s^{\mathbf1}\otimes m)
 \le C N\big(\beta^{-2}e^{-12s}+e^{-15s}\big).                           \tag{6}
\]
In particular, the estimate is on joint data including the entire opposite slice. If \(d\) denotes the entropy on the left, affinity of these two distributions is at least \(e^{-d/2}\) by Jensen. The squared Hellinger distance in the convention \(1-\int\sqrt{fg}\) is therefore at most \(1-e^{-d}\) for their tensor squares. The tensor square of the reference is invariant under swapping \(y,y'\). The triangle inequality for the \(L^2\) distance of square roots gives
\[
 \int_s^\infty A'(r)\,dr=1-A(s)\le4d
 \le C N\big(\beta^{-2}e^{-12s}+e^{-15s}\big).                             \tag{7}
\]
This requires neither a bound on the physical correlation length nor a bound on the number of low-energy states.

**PROVED (a range in which the slice still differs from Haar).** Set \(u=N e^{-12s}\). If \(n,\beta\to\infty\), \(u\to\infty\) and \(u=o(\min(\beta^2,N^{1/5}))\), the right side of (7) tends to zero, since \(Ne^{-15s}=u^{5/4}N^{-1/4}\). In the same range the total variation distance from the *one-slice output marginal* to product Haar tends to one. To see this, select \(N/4\) spatial squares of orientation 12, starting at even first and second coordinates and all third coordinates. Under \(k_s^{\mathbf1}\) their normalized real traces are independent with mean \(e^{-6s}\) and absolute value at most one. Conditional on the flat vertex gauges they depend on disjoint heat increments, and their conditional laws are independent of those gauges by equivariance. Under Haar they are independent with mean zero. Threshold their sum halfway between these expectations. Chebyshev bounds the two errors by \(C/u\). The actual one-slice marginal approaches \(k_s^{\mathbf1}\) in total variation by (6) and the elementary bound \(\|P-Q\|_{\mathrm{TV}}\le\sqrt{2(1-\int\sqrt{PQ})}\). Thus the near-unit crossed affinity in (7) can hold even when the local plaquette signal distinguishes the output from Haar with error tending to zero.

**GUIDE.** For example, on a trajectory with \(\beta\to\infty\) and \(\beta=O(\log n)\), take \(u=\beta\) and \(s=(\log N-\log\beta)/12\). Equations (1)–(7) apply in their stated finite-volume ranges. The logarithmic assumption fixes the scale in this illustration and in the physical-time argument below.

## Using the physical time separation

**PROVED, using row 1151 (24).** Assume now \(\beta\to\infty\), \(\beta\le B\log n\), with fixed \(B\). In (7) write \(h=e^{-6s}\), \(\lambda=Nh^2/\beta^2\). For the noisy slice \(Z\) and the raw opposite slice \(Y\), the quantitative conclusion is
\[
 \lambda\to\infty,\qquad
 \lambda\,[\log(2+\lambda)]^2=o(\log\beta)
 \quad\Longrightarrow\quad
 \|\mathcal L(Z,Y)-\mathcal L(Z)\otimes\mathcal L(Y)\|_{\rm TV}\to0,
 \qquad 1-A(s)\to0 .                                                       \tag{8}
\]
I use the open-box comparison of row 1151 for precisely the \(n^3\times(n/2)\) periodic Wilson law. It builds on Sourav Chatterjee's weak-coupling free-energy comparison. In that result, equation (24) bounds translated joint tests of the **radii** \(R_p=\sqrt{2\beta a_p}\), allowing moving offsets. Its Gaussian comparison variables are independent between the open boxes. They have variance per colour approaching \(1/2\) on average over the position of one face, as established in §12 of the same row. This is a local input at diverging bare coupling. [Moving-mark bound](gap-solve5-astra62.md) · [Check of (24), §9.3](gap-solve5-check-opus.md)

**PROVED (predicting products from the opposite slice).** Fix \(0<2\eta<\gamma<1/12\), \(b=\lceil\beta^\gamma\rceil\), and a clipping level \(M\ge1\). Let \(G\) be a three-component standard normal, \(A_*=|G|^2/4\), \(c_M=\mathbb E\min(A_*,M)\), and
\[
 g_p(x)=\big[\min(\beta a_p(x),M)-c_M\big]/M .
\]
Then \(|g_p|\le1\), and it is \(\sqrt{2/M}\)-Lipschitz in \(R_p\). For \(k\ge1\) plaquettes on the first slice whose base sites have pairwise periodic sup-distance greater than \(4b\), set \(f=\prod_{i=1}^k g_{p_i}\). Uniformly in the positions and \(M\), for all sufficiently large \(n\),
\[
 \mathbb E\big|\mathbb E[f(X)\mid Y]\big|^2\le C k\beta^{-\eta}.          \tag{9}
\]
To prove this, cut the time circle at the slices at \(b\) and \(b+T/2\). Given those slices, their two intervening bridges are independent, one being the reflection of the other in law. The slice \(X\) at zero and \(Y\) at \(T/2\) are on different interiors. Conditional Jensen bounds the left side by the squared norm of the expectation of \(f(X)\) given the cuts. Reflection makes that square exactly \(\mathbb E[f(X_0)f(X_{2b})]\).

**PROVED (size of the reflected product).** In the last expectation there are \(2k\) marks. Their product has bound one and Lipschitz constant at most \(2\sqrt k\) in all radii. Row 1151 (24) therefore costs at most \(Ck\beta^{-\eta}\), since \(\sqrt{(\log\beta)(1/b+b/n)}=O(\beta^{-\eta})\). A common translation leaves the Wilson expectation invariant. In the comparison tiling the marked interior faces lie in distinct cubes by the spatial separations and by the time separation \(2b\). Faces omitted from the tiling have deterministic radius zero. At each translation the expectation factors. Its absolute value is bounded by the absolute one-mark mean of the first factor, since all others have bound one. For an interior mark with per-colour variance \(v\), this mean in absolute value is at most \(\mathbb E|G|^2\,|v-1/2|/(2M)\), by coupling the same \(G\) in the two clipped variables. The squared deviations of the undiluted open-box diagonal entries from \((1-b^{-4})/2\) have position average \(O(1/b)\) by the projection rank estimate in row 1151 §12. Its dilation changes each entry by \(O(1/b)\). Omitted marks have frequency \(O(1/b+b/n)\). The translation average of the one-mark bound is consequently \(O(b^{-1/2}+b/n)\). This proves (9), without treating the full opposite slice as a finite list of local marks.

**PROVED (a normalized approximation to the reading).** Assign each spatial plaquette to its last edge in the revealing order, and let \(\mathcal P_e\) denote the set assigned to \(e\). Define a conditional density at edge \(e\) by
\[
 q_e^x=1+2h\sum_{p\in\mathcal P_e}
          [1-\min(\beta a_p(x),M)/\beta]\chi_2(z_p).
\]
Each nonconstant term integrates to zero in the new link. For \(1\le M\le\beta\) and sufficiently small \(h\), these conditionals are bounded below by \(1/2\) and specify a probability law. In (4) dimensions \(d\ge3\) contribute at most \(Ce^{-16s}\). The dimension-two term uses \(\chi_2(x_p)=2(1-a_p(x))\). By the same conditional entropy bound as in (5), the expected divergence from the exact noisy orbit law to the law with conditionals \(q_e^X\) is at most
\[
 C\big[Ne^{-15s}+\lambda e^{-cM}\big].                                    \tag{10}
\]
The clipping estimate uses \(\mathbb E[(\beta a_p-M)_+^2]\le Ce^{-cM}\), which follows from row 1334 (5). In particular this controls the joint approximation with the latent pair \((X,Y)\) retained, provided an independent vertex gauge is included at the observed end. For the marginal \((Z,Y)\) such a gauge is available from the exact separate invariance.

**PROVED (summing all revealed-edge interactions).** Take the reference law \(R\) with conditionals \(r_e\) given by the same formula as \(q_e^x\) with \(\min(\beta a_p,M)\) replaced by \(c_M\). Set \(d=hM/\beta\) and \(T_{e,p}=-2\chi_2(z_p)/r_e\). Under \(R\), each \(T_{e,p}\) has conditional mean zero given the previous edges and absolute value at most eight. The conditional law for input \(x\) from (10) has likelihood relative to \(R\)
\[
 \prod_e\left(1+d\sum_{p\in\mathcal P_e}g_p(x)T_{e,p}\right).
\]
Given \(Y=y\), average this likelihood over the actual conditional law of \(X\). In its term of order \(k\), the coefficient for a tuple with increasing last edges is \(m_{p_1\ldots p_k}(y)=\mathbb E[\prod_i g_{p_i}(X)\mid Y=y]\). The squared \(L^2(R)\) norm of that term is at most
\[
 (C d^2)^k\sum_{p_1,\ldots,p_k}|m_{p_1\ldots p_k}(y)|^2 .                 \tag{11}
\]
Indeed group the sum by its last edge. Different last edges are orthogonal martingale differences. At one last edge, conditional Cauchy–Schwarz and \(|\mathcal P_e|\le4\) bound its squared norm by a numerical constant times the sum of the squared norms of its preceding coefficients as functions of the revealed values. Repeat on the prefixes. This argument permits the functions \(T_{e,p}\) to depend on every previous link through the conditional density.

**PROVED.** There are at most \((3N)^k/k!\) eligible tuples. Among them, the number having a pair of base sites within \(4b\) is at most \((3N)^k Ck^2 b^3/(Nk!)\). To see this, count all ordered spatial plaquette samples with replacement, choose the nearby pair, then divide by \(k!\) for the subset with distinct last edges. On exceptional tuples use \(|m|\le1\), and on all others use (9). After integrating (11) against \(m(y)dy\) and taking square roots, summing over \(k\ge1\) bounds the distance of the likelihood from one in \(L^2(R\otimes\mathcal L(Y))\) by
\[
 C(\beta^{-\eta}+b^3/N)^{1/2}\exp(C M^2\lambda).                          \tag{12}
\]
For the sum, use \(Nd^2=M^2\lambda\) and \(\sum k v^{k/2}/\sqrt{k!}\le (\sum k^2 2^{-k})^{1/2}e^v\). In (8) choose \(M=K\log(2+\lambda)\) with \(cK>2\) in (10). Then (10) tends to zero, since \(Ne^{-15s}=(\lambda\beta^2)^{5/4}N^{-1/4}\to0\). The exponential in (12) is \(\beta^{o(1)}\), so (12) also tends to zero. Total variation contraction under marginalization and the triangle inequality yield the first conclusion of (8). Applying the swap to two copies and using \(1-\int\sqrt{PQ}\le\|P-Q\|_{\rm TV}\) gives its second conclusion.

**PROVED (the same observation detects its own input).** Under (8), the distance of \(\mathcal L(X,Z)\) to \(\mathcal L(X)\otimes\mathcal L(Z)\) tends to one for the ordinary, unrandomized heat reading of \(X\). Use the disjoint plaquettes \(\mathcal P\) of the one-slice test above, with \(m=|\mathcal P|=N/4\), and put \(A_p(x)=\beta a_p(x)\), \(c_j=\mathbb E A_p(X)\) on this orientation. Fix \(B_1>0\) and \(g(v)=\min(v,B_1)-\mathbb E\min(A_*,B_1)\). In the joint experiment compare the statistic
\[
 \frac{\beta}{mh}\sum_{p\in\mathcal P}g(A_p(X))
       \left[h(1-c_j/\beta)-\operatorname{Re}Z_p\right]                    \tag{13}
\]
with the same statistic using the independent-input experiment. For latent input \(X'\) of \(Z\), the conditional mean given \(X,X'\) is \(m^{-1}\sum_p g(A_p(X))(A_p(X')-c_j)\). The conditional variance is \(O(1/\lambda)\), because the heat increments on the chosen squares are disjoint and \(\mathbb E[\operatorname{Re} Z_p\mid X']=h\operatorname{Re}X'_p\).

**PROVED.** For \(X'=X\) this empirical mean tends in \(L^2\) to \(\operatorname{Cov}(\min(A_*,B_1),A_*)>0\). Positivity follows by taking half the expected product of the increments of the two increasing functions at two independent copies, which is strictly positive on a set of positive probability. For \(X'\) independent of \(X\) the empirical mean tends to zero in \(L^2\). Indeed the one-mark and the two-mark laws at spatial distance greater than \(4b\) tend uniformly to the one- and two-fold independent Gaussian-radius laws by (24) and the open-box diagonal comparison used for (9). This applies to moments here by clipping the unbounded factors at a fixed height and then using the uniform exponential plaquette moment. The proportion of pairs within \(4b\) is \(O(b^3/N)\), with uniformly bounded moments. These facts control the mean and second moment of both averages, and \(c_j\to\mathbb E A_*\). Threshold (13) at half the displayed positive covariance. This also works if an independent gauge is applied before observation, since all the statistics are plaquette traces. Together with (8) this distinguishes information about the raw opposite time slice from information about the time slice actually observed.

## What a fixed amount of noise does to the three spatial centre bits

**GUIDE.** To try to carry (8) back to zero noise I tested the part of a spatial slice that changes under the three noncontractible centre flips. Row 1171 already identifies local loop data determining a connection up to gauge and those flips. In the following decoding experiment one can also retain the input adjoint matrices and the input fundamental plaquette signs. These additional observations make the conditional experiment explicit. The large-noise indistinguishability bound below also applies when they are discarded. [Local loop reconstruction](gap-solve14-astra62.md)

**PROVED (the conditional sign problem).** Let \(D(x)\) be the list of \(\operatorname{Ad}x_e\) and \(\operatorname{sgn}\operatorname{Re}x_p\) on the spatial slice. A vanishing plaquette trace has zero probability, by absolute continuity and integration of one plaquette edge in Haar. Choose one measurable lift \(r(D)\) with these signs. For example lift each adjoint by a Borel section and take the first consistent adjustment of the finite array of signs. Every lift is \(x_e=\sigma_e r_e\), where \(\sigma\) is closed because its sign product on every square is one. Its class modulo vertex signs is determined by its three products on primitive winding paths. Indeed after these products are removed by three seam flips, edge products of the remaining cochain are path independent and furnish the vertex signs. At fixed \(D\), class and opposite slice \(Y\), all vertex-sign lifts are equally likely by the independent gauge invariance of the Wilson density at \(X\).

**PROVED (recovery at small fixed noise).** For some fixed \(s_->0\), observing \((D(X),Z_{s_-})\) recovers the class of \(\sigma\) with error at most \(C N e^{-c n^2}\), uniformly in \(\beta\), the physical time separation, and the actual input. The readings \(\operatorname{sgn}\operatorname{Re}(Z_e r_e^{-1})\) are \(\sigma_e\) times independent signs with error probability \(q=\mathbb P_{w_{s_-}}(\operatorname{Re}g<0)\). Choose the nearest closed sign cochain in Hamming distance. Its difference from the true cochain corresponds on the dual lattice to a union of closed mod-two surfaces. Components joined along dual edges are separately closed by even incidence. An incorrect class has a component with nonzero winding evaluation. It intersects each of the \(n^2\) disjoint parallel representatives of that primitive line oddly, so its size is \(k\ge n^2\). On this component at least half of the measurements have errors, since toggling the whole component is another allowed candidate for the minimization. A dual face has at most 12 edge-neighbours, so there are at most \(3N\,12^{2k}\) connected sets of size \(k\). The probability of at least half errors on a given one is at most \(2^k q^{k/2}\). The heat law tends to a point mass at the identity as \(s_-\downarrow0\). Choose \(2\cdot12^2\sqrt q<1/2\) and sum the geometric series. For two equally likely lifts differing by a single seam, a lower bound at fixed \(s_->0\) follows by pairing the same random vertex signs in both experiments. The heat likelihoods differ on \(n^2\) edges, so each bounds the other below by \((\min w_{s_-}/\max w_{s_-})^{n^2}\). Integration gives the same lower bound on their overlap.

**PROVED (loss at large fixed noise).** At some fixed \(s_+>s_-\) the conditional output laws of any two classes, averaged over the vertex signs, have total variation distance at most \(C N(5q_+)^n\), where \(5q_+<1\). Write the heat kernel as the sum of its centre-even common part \(\min(w_{s_+}(g),w_{s_+}(-g))\) and a nonnegative remainder of integral \(q_+\). Choose the remainder independently on each edge with probability \(q_+\), using the corresponding normalized kernels. On the subgraph of remainder edges a seam flip can be undone by vertex signs whenever it has trivial product on every cycle there. The common part on all other edges is insensitive to these signs. A nontrivial restriction requires a simple winding cycle, with at least \(n\) distinct edges. There are at most \(6N5^{n-1}\) choices of the initial \(n\) nonbacktracking steps and a specified segment of distinct edges is present with probability \(q_+^n\). This gives the stated bound. The uniform convergence \(w_s\to1\) permits the choice of \(s_+\). For different classes on one winding direction the sign product of the noisy readings along one straight winding has conditional means of opposite sign with magnitude \(\rho_{s_+}^n\), \(\rho_s=\mathbb E_{w_s}\operatorname{sgn}\operatorname{Re}g>0\). Thus the distance is at least \(\rho_{s_+}^n\). After the first equatorial hit, reflecting spherical Brownian motion gives zero conditional mean sign. Before that hit the sign is positive, and survival to any finite time has positive probability, proving \(\rho_s>0\).

**PROVED (consequence for the thermal comparison).** Write \(A_D(s)\) for the crossed affinity when the first reading is \((D(X),Z_s)\), and \(A_D(\infty)\) for the one with \(D(X)\) alone. Then
\[
 0\le A_D(s_-)-A(0)\le C\sqrt{N}e^{-c n^2},\qquad
 0\le A_D(\infty)-A_D(s_+)\le C\sqrt{N}(5q_+)^{n/2}.                     \tag{14}
\]
For the first inequality, recover the decoded class and draw uniform vertex signs to reconstruct a raw slice. Conditional on correct class information the target reconstruction kernel is precisely this uniform draw. Coupling to the draw using the true class costs at most the decoding error. For the second inequality, one can simulate the noisy output from \(D\) using its reference class and random vertex signs, within the stated total variation error uniformly in the true class. Each channel may be used separately at the two first-slice endpoints in (1). Affinity increases under a channel by Cauchy–Schwarz, and changing a probability by total variation \(\epsilon\) moves its square root by at most \(\sqrt{2\epsilon}\) in norm. These give (14) in both comparisons. The difference \(A_D(\infty)-A(0)\), which is sensitive to the physical law of the centre classes, still needs an estimate on the matched trajectory.

## Attempt to return to the unsmoothed physical trace

**PROVED (small noise, without the additional observations).** The original affinity satisfies, uniformly for the finite isotropic Wilson boxes under discussion and \(\beta\ge1\),
\[
 0\le A(v)-A(0)\le C\sqrt{N\beta v}.                                      \tag{15}
\]
In the true period-\(T\) law the spatial force \(\nabla_{x_e}V\) is a sum of at most four normalized plaquette gradients times \(\beta\). Each gradient has second moment at most \(C/\beta\) by the plaquette moment estimate. The same bound applies to the one inward temporal force in the derivative of \(K_t\). Conditional Jensen in the bridge and the bound on the sum of finitely many squares give \(\int p|v_e(x,y;0)|^2\le C\beta\). Consequently \(\sum_e\|\nabla_{x_e}\sqrt p\|_2^2\le CN\beta\). The inequality \(\sqrt{H_v p}\ge H_v\sqrt p\) and \(1-e^{-v u}\le v u\) on the spectrum of the nonnegative heat generator bound \(\|\sqrt{p_v}-\sqrt p\|_2^2\) by \(v\sum_e\|\nabla_{x_e}\sqrt p\|_2^2\). Tensoring two unit vectors and taking their inner product with their crossed versions costs at most four times the norm difference. This proves (15).

**PROVED, using the fixed-cube result of row 1227, equation (14).** There are ordinary isotropic Wilson tori on which \(A(0)\to1/8\) and \(A(s_+)\to1\) for the same fixed observation noise as in (14). With the adjoints and plaquette signs retained, \(A_D(s_+) - A_D(s_-)\to7/8\). The periods and couplings of this example have a different order of limits from the physical target. Fix \(n\) first, let \(t=\lfloor e^{\beta^{1/3}}\rfloor\) and \(T=2t\). Row 1227 proves that \((F/\|F\|)^t\) approaches in trace norm the projection onto the eight products of the three fundamental winding signs times the Perron vector \(\psi\). This is the small-volume tunnelling mechanism studied by Lüscher and van Baal. Its kernel is \(8\psi(x)\psi(y)\mathbf1_{\ell(x)=\ell(y)}\), where \(\ell\) is the sign triple. Trace-norm convergence implies Hilbert–Schmidt convergence, and hence \(L^1\) convergence of normalized squared kernels by Cauchy–Schwarz. The joint slice law thus approaches the experiment of choosing a uniform triple and drawing two independent slices from \(\psi^2 dx\) given that triple. Uniformity follows from the three seam flips. In this experiment only coincident triples in the two independent samples contribute to the crossed affinity. The two densities agree there, giving \(1/8\). The side data \(D(X)\) are invariant under the three flips, so are independent of the chosen triple and hence independent of \(Y\). Their crossed affinity is one. Choose \(n\to\infty\) in multiples of four and at each \(n\) choose \(\beta\) large enough that the joint-law error is at most \(1/n\). Equation (14) gives both conclusions with \(D\) retained. Discarding \(D\) can only increase the affinity at \(s_+\). Thus high-noise decorrelation alone cannot be inverted uniformly in Wilson parameters, even at fixed noise. This example uses \(T=2\lfloor e^{\beta^{1/3}}\rfloor\), with no assertion at \(T=n/2\) on the matched trajectory. [Fixed-cube theorem](gap-solve25-astra62.md) · [Check of the eight-state limit](gap-solve25-check-opus.md)

**PROVED (testing the use of the logarithmic schedule).** Even the two opposing conclusions (8) and (13) coexist with \(A(0)\to0\) at \(\beta=\log n\) if the time aspect is shortened. To see this in the original Wilson action, fix a small \(\kappa>0\) and replace the period by \(T'=4\lfloor\kappa\log n\rfloor\), keeping \(n^3\) and every plaquette coupling. The proof of (9) applies with the following rectangular version of its input. In row 1151 (22b), (24), tiling all four circles with open side-\(b\) boxes now leaves a fraction at most \(C b/T'\) of sites uncovered. Crossing edges and boundary tangents occupy at most \(C(1/b+b/T')\) per unit volume. The upper comparison drops their nonnegative actions. The lower comparison restricts the same joining links and boundary tangents to radius \(\beta^{-1}\), at log cost \(C(1/b+b/T')\log\beta\) per unit volume. The internal cube estimates are identical. Thus the density bound used in (24) has \(\Delta_b=(1/b+b/T')\log\beta\) in place of its old value. For the bad-cube estimate, split the faces by their six orientations and apply Hölder and row 1334 (5). The action threshold of row 1151 gives \(C e^{-c\beta/b^8}\) for \(\gamma<1/12\). The Gaussian Lipschitz and translation counts in (24) use total four-volume in both numerator and denominator. These replacements give the bound of (9), since \(T'\asymp\beta\), \(b=\lceil\beta^\gamma\rceil\), \(2\eta<\gamma\), and the two time cuts still separate all reflected marks. Equations (8) and (13) therefore hold in the same noise range on these boxes.

**PROVED.** Row 1161 (19) gives absolute \(c,C>0\) and at least \(c n^3\) excited neutral levels with lattice energy at most \(C\), uniformly in \(\beta\ge1\). Take \(4C\kappa<3\). The normalized trace \(z_{T'}\ge1+c n^3 e^{-CT'}\) diverges. Positivity of the transfer spectrum gives \(A(0)=z_{2T'}/z_{T'}^2\le1/z_{T'}\to0\). Hence the integral below the range of (8) can tend to **one** with the logarithmic bare coupling and the full Wilson action. The time in physical units for these boxes tends to zero. The counterexample concerns the attempt to infer the physical estimate using just the mark comparisons and schedule. [Uniform neutral level count](gap-solve9-astra62.md)

**PROVED (testing the time aspect without the trajectory).** Conversely keep \(T=n/2\) exactly, with \(4\mid n\). At each fixed \(n\), row 1215 (5) proves that every fixed number of the largest neutral eigenvalue ratios tend to one as \(\beta\to\infty\). For that \(n\), choose \(\beta_n\ge n\) so large that the first \(n\) such ratios raised to \(T\) exceed \(1/2\). Then \(A(0)\le 1/z_T\le2/n\). Choosing \(u=N^{1/10}\) in (7) gives \(u/\beta_n^2+u^{5/4}N^{-1/4}\to0\). Thus at this same aspect the general high-noise estimate also coexists with essentially the largest possible thermal deficit. This sequence does not satisfy the logarithmic upper coupling bound. [Fixed-cube neutral spectrum](gap-solve23-astra62.md)

**OPEN (the physical estimate).** On the matched trajectory, suppose \(\beta_j\to\infty\) and \(\beta_j\le B\log n_j\). Applying (8) needs these coupling hypotheses in addition to the premises of Theorem ZD-c. Set \(N_j=n_j^3\), \(T_j=n_j/2\) and, for all sufficiently large \(j\),
\[
 v_j=(N_j\beta_j^2)^{-1},\qquad
 s_j=\frac1{12}\log\!\frac{N_j}{\beta_j^2\sqrt{\log\beta_j}} .
\]
At each fixed permitted side \(L\), (8) with \(\lambda=\sqrt{\log\beta_j}\) and (15) give the hand-proved equality up to vanishing error
\[
 1-\frac{Z(n_j,2T_j)}{Z(n_j,T_j)^2}
   =\int_{v_j}^{s_j} A'_j(r)\,dr+o(1).                                   \tag{16}
\]
Here \(A'_j\) is the integral in (2) of the squared differences of the conditional logarithmic gradients, summed over the spatial links. What I cannot establish is
\[
 \exists L\in\{2^i\ell_1:i\ge0\}\qquad
   \limsup_j\int_{v_j}^{s_j} A'_j(r)\,dr < 1/1651 .
\]
The local force bound (3) grows as \(N_j\beta_j\). The reflected moment estimate (12) loses control when the number of detectable plaquette signals grows beyond its stated range. Neither gives the required upper bound in (16). The ordinary Wilson examples above exhibit the failures at the other time aspect or coupling schedule. A strict bound at the specified aspect on the matched trajectory is still needed for this thermal route. Construction and identification of the full nontrivial continuum theory also remain open here. The new arguments are by hand and have no independent check.

RESULT — OPEN. Row 1337 proves (8) and (13) for noisy Wilson slices on logarithmically bounded coupling trajectories, and identifies in (16) the remaining positive integral for the unsmoothed thermal seed. The strict bound on that integral and the four-dimensional SU(2) Jaffe–Witten mass gap remain unproved.
