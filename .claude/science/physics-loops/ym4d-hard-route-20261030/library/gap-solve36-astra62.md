# Repo search

**GUIDE.** FINISH row 1317, source checkout `dde2238e6`. There is no row-specific file at `library/prior/gap-solve36-astra62.md`. The first test is whether a prior result supplies a strictly positive lower edge of the excitation spectrum in physical units on the full vacuum sector. If it does not, the task is to identify and attack the missing Wilson-theory estimate. Labels in this note describe written arguments and confer no project status.

**GUIDE.** The lead's November 8 search covered main and PRs 10114, 10133, 10134 and 10141. I checked the following target-relevant passages against their fetched Git objects. On main at `8b11ae2bb9`, Theorem ZD-c relates a periodic thermal seed to bounds on the cube energy and the free-energy defect under doubling. On PR 10114 at `f76f6c649c`, the one-step plaquette witness holds at finite coupling and the contraction estimate is restricted to \(0<\beta\le1/32\). Grok's PR 10133 at `89faef229f` leaves the crossover and transport of sources open. PR 10134 at `1e70c7211a` distinguishes a nonempty excited space, a lower spectral edge and Yang–Mills identification. PR 10141 at `a2f6a430e2` estimates a constrained classical field at one scale. PR 10144 at `1f20846b80` indexes a second snapshot of local proof notes. [Lead's search](prior/repo-search-2026-11-08.md) · [Source paths and ranges](prior/gap-onebound-read-sol.md)

**GUIDE.** Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, explain the scope of the action-density sector and exhibit a positive spectral measure with polynomial decay and support down to zero. Their complete account explicitly leaves a mass gap open. I used the outline index, chunks 01 and 29 and the obligations list, before checking the source. [Outline 581–599](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L581-L599) · [Outline 31860–31882](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L31860-L31882) · [Complete account I 2704–2712](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L2704-L2712)

**GUIDE.** Row 1218 reports a full thermal-trace criterion of Deep Bhattacharjee, Ushashi Bhattacharya, James Montgomery Lockwood, Tristan Romanov, Ikailo John Sessford and Sanjeevan Singha Roy. The weak-coupling one-scale input remains open in the row 1311 check of their ascent. The coarse straight-path bound in the four-author paper of Bhattacharjee, Bhattacharya, Lockwood and Romanov still needs a comparison to the fine law. Zeng Chunping's tunnelling proposal still needs its microscopic hypotheses. I use the comparisons in the repository. [Published-work reading](prior/gap-onebound-read-sol.md) · [Ascent check](gap-onebound-ascent-check-astra.md)

**GUIDE.** Row 1315, (8), (12), (17) and (20)–(22), treats a rare plaquette, a trace averaged over a linear span, first returns and the fluctuations of the total number of rough plaquettes. Its finite-patch change of variables can cross a threshold at precisely one face. The row 1316 check is listed as started and its file is absent at this pin. Row 1211, (6), controls marked spacetime plaquettes in a Wilson slab between arbitrary physical end vectors. Its antecedents include the positive-transfer estimates of Sussman and Alpoge, with Claude and Codex as authors of their text. A search in the registry and the earlier gap notes located these ingredients. I found no owner for the estimate below on *prescribing simultaneous count residues in the physical transfer*. [Row 1315](gap-solve35-astra62.md) · [Row 1211](gap-solve22-astra62.md) · [Registry](open-registry.md)

## Choice of attack

**GUIDE.** Test whether one can impose exact, spatially extensive constraints on a Wilson time slice while retaining the physical spectral edge to accuracy \(o(a)\), where \(a\) is the lattice spacing. The proposed constraints prescribe the number of rough plaquettes modulo an integer in each of many boxes. The first issue is cancellation for products of plaquette phases between two arbitrary physical states. A variance lower bound for the count gives no cancellation at angle \(\pi\), since a count supported on even numbers can have arbitrarily large variance. The second issue is the normalization after imposing many low-probability constraints. A spectral proof by this route requires a strictly positive lower bound on the first excited energy in physical units, uniform in the required volumes and cutoffs.

## What was already known about the signs

**GUIDE.** Row 1215 reaches further than the variance estimate in row 1315. Its (26)–(29) already prove joint parity mixing for arbitrary disjoint large sets of spatial plaquettes, pointwise in both ends of a two-step bridge. Row 1157 already treats simultaneous bare plane signs. I use those results for signs. The remaining questions here concern larger count moduli, the spectrum and thermal normalization on a prescribed slice, and the continuously valued spatial Wilson action. [Two-step bridge, row 1215](gap-solve23-astra62.md#a-four-link-change-at-physical-bare-coupling) · [Plane signs, row 1157](gap-solve8-astra62.md)

**GUIDE.** Let \(F\) be the positive Wilson time transfer on gauge-invariant \(L^2\) of spatial links with product Haar measure on a periodic three-torus of sides at least four. Use the Wilson weight \(\exp(\beta\sum_p w_p)\), \(w_p=\tfrac12\operatorname{tr}U_p\). Set \(U=F/\lambda_0\), where \(\lambda_0=\|F\|\). One can compute its two-step bridge in temporal gauge before restricting to gauge-invariant functions. The magnetic factors at the two ends cancel from conditional probabilities. In the middle each spatial plaquette contributes \(\beta w_p\), and each link has two linear temporal terms. Gauge averaging at the ends preserves a pointwise inequality with positive majorant. These are the finite-lattice transfer conventions of Osterwalder–Seiler and Lüscher used in rows 1215 and 1298. [Row 1298, three-slice law](gap-solve34-astra62.md)

**PROVED (count moduli, using the four-link construction of row 1215).** Write \(Y_p=1_{\{w_p<0\}}\). For arbitrary real \(t_p\), uniformly in both ends \(x,y\),
\[
 \left|\mathbb E_{x,y}\exp\!\left(i\sum_p t_pY_p\right)\right|
 \le \exp\!\left[-c\,p_\beta\sum_p\sin^2(t_p/2)\right],
 \qquad p_\beta=c_\epsilon e^{-(E_*+\epsilon)\beta},\quad
 E_*=1+20(1-\cos(\pi/8)).                                      \tag{1}
\]
Here and below the spatial plaquettes have one orientation per elementary square. Use row 1215's construction immediately preceding (27). For any fixed exterior of the four edges at \(p\), two disjoint sets of configurations have probability at least \(p_\beta\) each. They have the same indicators on *all* the other spatial plaquettes incident to those edges and opposite indicators at \(p\). This stronger information is in the proof of its (26), which perturbs across the shared zero-trace wall away from every other zero-trace locus and uses compactness of the exterior parameters. Take subprobabilities of mass exactly \(p_\beta\) on the two sets, reducing \(c_\epsilon\) if necessary. Their phases differ by \(t_p\). The triangle inequality gives modulus at most \(1-2p_\beta(1-|\cos(t_p/2)|)\le1-p_\beta\sin^2(t_p/2)\), including the rest of the distribution. Colour the roots by a bounded number of colours so that no action plaquette meets the variable sets of two roots of one colour. A greedy colouring works since the conflict degree is bounded by an absolute constant. Choose the colour carrying the largest sum of \(\sin^2(t_p/2)\). Its integrations are conditionally independent and the phase factors over the chosen sets after fixing their exterior. Multiplication and integration give (1). Taking all nonzero \(t_p=\pi\) recovers the special case already on file. Since the two sets in the cited compactness proof can be chosen as closed balls with strict margins on every trace, the same proof works for \(Y_p=1_{\{w_p<d\}}\) whenever \(|d|\) is sufficiently small depending on \(\epsilon\). Indeed finitely many exterior neighborhoods and positive margins suffice for all their balls. This includes fixed thresholds just below zero used for the rare events of row 1315.

**PROVED.** For disjoint groups \(S_1,\ldots,S_B\) of at least \(k\) plaquettes each, prescribe \(\sum_{p\in S_i}Y_p\bmod q=z_i\) in all groups, with \(q\ge2\). Let \(D=q^B\) and \(M_z\) be multiplication by the joint event. Finite Fourier inversion in (1) gives the pointwise kernel bound
\[
 |D\,U M_z U-U^2|(x,y)\le\delta\,U^2(x,y),\quad
 \delta=\left(1+2\sum_{\ell=1}^{\lfloor q/2\rfloor}
             e^{-4c p_\beta k\ell^2/q^2}\right)^B-1 .             \tag{2}
\]
The term with \(\ell=q/2\) may be overcounted. Each character uses weight \(\sum_i |S_i|\sin^2(\pi\ell_i/q)\), with \(\sin(\pi\ell/q)\ge2\ell/q\) for \(0\le\ell\le q/2\). The zero character gives \(U^2\). At a fixed physical cube of side \(L\), \(a=L/n\), on the *assumed* schedule \(\beta/\log n\to11/(3\pi^2)\), one can take \(p_\beta\ge n^{-\gamma}\) for some \(\gamma<1\). Indeed \(E_*<1+5\pi^2/32<3\pi^2/11\) using \(\pi>3\), and one can then choose \(\epsilon>0\). With \(k=n\), \(B\) polynomial in \(n\) and \(q\le n^{(1-\gamma)/4}\), the error is smaller than every inverse power of \(n\). For example, all \(n^2\) rows of \(12\)-plaquettes parallel to direction 1 may be prescribed at once. The parity case \(q=2\) in (2) is due to row 1215.

## Spectrum and heat trace on a prescribed slice

**PROVED.** Suppose a physical middle-slice event has multiplication projection \(M\), and numbers \(D>0,\ 0\le\delta<1\) satisfy the pointwise inequality (2) with \(M\) in place of \(M_z\). Define
\[
 A=DUMU,\qquad B_M=D M U^2 M\big|_{M\mathcal H}.
\]
Here \(\mathcal H\) is the gauge-invariant space. The two operators are positive and compact. Their positive eigenvalues with multiplicities agree, since they are \(XX^*\) and \(X^*X\) for \(X=\sqrt D\,UM:M\mathcal H\to\mathcal H\). For example \(X^*\) maps an eigenspace of \(XX^*\) of eigenvalue \(s>0\) bijectively to the corresponding eigenspace of \(X^*X\), with inverse \(X/s\). For any \(f,g\), the absolute difference between the matrix elements of \(A\) and \(U^2\) is bounded by \(\delta\langle|f|,U^2|g|\rangle\le\delta\|f\|\|g\|\). The min-max formula therefore bounds the difference between their ordered eigenvalues by \(\delta\). Writing \(u_i\) for the eigenvalues of \(U\), \(u_0=1\), and \(\rho_i\) for the ordered eigenvalues of \(B_M\), this yields
\[
 \left|\rho_i/\rho_0-u_i^2\right|\le 2\delta/(1-\delta).
                                                                    \tag{3}
\]
The same norm comparison on restrictions applies to symmetry sectors preserved by \(M\), with the normalization taken from the full vacuum.

**PROVED.** The trace comparison also controls multiplicities. All kernels in the cycle integral for \(\operatorname{Tr} A^j\) are nonnegative. For any \(j\ge1\), multiplying the two pointwise bounds along the cycle gives
\[
 \left(\frac{1-\delta}{1+\delta}\right)^j
 \le\frac{\operatorname{Tr}(B_M/\rho_0)^j}{\operatorname{Tr} U^{2j}}
 \le\left(\frac{1+\delta}{1-\delta}\right)^j .                      \tag{4}
\]
The finite-grid kernels are bounded on compact spaces, \(U\) is Hilbert–Schmidt and \(A\) is trace class. At \(j=1\) the diagonal integral agrees with the trace by the factorization \(XX^*\) and its Hilbert–Schmidt norm. At \(j\ge2\) kernel composition and that same factorization justify the cycle integral. The top eigenvalue is between \(1-\delta\) and \(1+\delta\). Equation (4) concerns a positive two-step transfer with the event enforced at *every* second slice. The factor \(D\) accounts for its small mass and cancels under vacuum normalization. In particular, an \(o(a)\) relative bridge error is enough for agreement at \(j=O(1/a)\) even when the probability of the prescribed slice tends to zero. Row 1315's first-return comparison (17) concerns a different transfer on a set of large stationary probability.

**GUIDE.** A harder test is to prescribe an interval for the continuously valued *magnetic action* modulo a chosen period in each group. This reading varies even while every plaquette trace stays positive. For this test an adjacent pair of links gives a mixed term that no sum of one-link terms can cancel. The calculations below use this term directly.

## A Fourier estimate for the magnetic action in an arbitrary Wilson bridge

**PROVED (two adjacent links).** Use probability Haar measure on \(S^3=\mathrm{SU}(2)\). Fix an orthogonal \(4\times4\) matrix \(O\), real vectors \(|a|,|b|\le5\), and \(\beta\ge1\). On \(S^3\times S^3\) give \((x,y)\) density proportional to \(e^H\), where
\[
 H=\beta(x\cdot Oy+a\cdot x+b\cdot y).
\]
For real \(t\) and arbitrary measurable real one-variable phases \(f,g\),
\[
 \left|\mathbb E_H e^{\,i(\beta t\,x\cdot Oy+f(x)+g(y))}\right|
 \le h_\beta(t):=\min\!\left(e^{-c\min(t^2,1)},
                 C e^{14\beta}(1+\beta|t|)^{-1/2}\right) .          \tag{5}
\]
Here \(c>0\) and \(C\ge1\) are absolute. In particular the first bound costs no power of the coupling.

**PROVED (a product measure inside the conditional law).** Write \(\mu=e^H\,dx\,dy/Z\). With the nonpositive round Laplacian one has \(-\Delta H\le36\beta\), since each quaternion coordinate has Laplacian \(-3\) times that coordinate and the mixed term has eigenvalue \(-6\). Integration of \(\operatorname{div}(e^H\nabla H)\) gives \(\int|\nabla H|^2\,d\mu=-\int\Delta H\,d\mu\). Thus \(G=\{|\nabla H|\le9\sqrt{1+\beta}\}\) has mass at least \(1/2\). Also \(|\nabla^2 H(v,v)|\le7\beta |v|^2\). Along a product geodesic the two pure second derivatives of \(x\cdot Oy\) cost \(|v|^2\) together, the mixed derivative costs at most \(2|v_x||v_y|\le |v|^2\), and the linear terms cost at most \(5|v|^2\).

**PROVED.** Choose \(r=[8\sqrt{(1+\beta)\max(1,|t|)}]^{-1}\). At every centre \(z\in G\), let \(K_z\) be the product of uniform Haar caps of radius \(r\) about the two spins. On those caps, Taylor's formula along the product geodesic of length at most \(\sqrt2 r\) gives \(|H(w)-H(z)|\le C_0\) with an absolute \(C_0\). Since cap volumes are independent of the centre, \(dz\,K_z(dw)=dw\,K_w(dz)\) for product Haar volume. Consequently \(\int_G \mu(dz)K_z(dw)\le e^{C_0}\mu(dw)\). This supplies a submeasure of \(\mu\) of mass at least \(e^{-C_0}/2\) which is a mixture of these product caps. This use of a distribution of centres gives a uniform mass even when the maximizing fields depend on the exterior.

**PROVED (the mixed phase survives both one-variable phases).** On one product of caps let \(X,X'\) be independent draws from the first cap and \(Y,Y'\) from the second, all independent. Apply Cauchy–Schwarz first to the \(X\) integral of the conditional \(Y\) mean and then to the \(Y,Y'\) integral of the resulting \(X\) mean. The fourth power of the modulus on the caps is at most
\[
 \mathbb E\cos\!\left(\beta t (X-X')\cdot O(Y-Y')\right).
\]
In the first squaring \(f\) disappears, and in the second \(g(Y)-g(Y')\) disappears. Exchanging \(X,X'\) makes the last expectation real. The argument has absolute value at most \(4\beta|t|r^2\le1\). If \(x_0\) is the first cap centre, its covariance \(\Sigma_X\) dominates \(c_1 r^2\Pi_{x_0^\perp}\) in quadratic-form order. Indeed its tangent covariance is \(I\,\mathbb E\sin^2\theta/3\), its mixed radial-tangent covariances vanish by rotations, and \(\theta\in[r/2,r]\) has probability bounded below by a constant from its density proportional to \(\sin^2\theta\). The analogous bound holds at \(y_0\). Thus
\[
 \mathbb E[((X-X')\cdot O(Y-Y'))^2]
 =4\operatorname{tr}(\Sigma_X O\Sigma_Y O^*)\ge c_2 r^4 .
\]
The two tangent projections have product trace \(2+(x_0\cdot Oy_0)^2\). Now \(1-\cos v\ge c_3 v^2\) on \([-1,1]\) and \(1-u^4\le4(1-u)\) for \(0\le u\le1\). The loss in modulus on every product cap is at least \(c_4\beta^2 t^2 r^4\ge c_5\min(t^2,1)\). Use the submeasure just constructed and bound the remainder by its mass. This proves the first part of (5).

**PROVED (summability at high frequencies).** For product Haar and any measurable \(|A|,|B|\le1\),
\[
 \left|\int A(x)B(y)e^{isx\cdot Oy}\,dx\,dy\right|
       \le C(1+|s|)^{-1/2}.
\]
After Cauchy–Schwarz in \(x\) its square is at most the \(dy\,dy'\) integral of \(\big|\int e^{isx\cdot O(y-y')}\,dx\big|\). A coordinate of a uniform point of \(S^3\) has density \((2/\pi)\sqrt{1-u^2}\) on \([-1,1]\). Integrating by parts bounds the inner modulus by \(\min(1,C/(|s||y-y'|))\). The integral of \(|y-y'|^{-1}\) is finite and independent of \(y\), since the polar volume is proportional to \(\sin^2\theta\,d\theta\) and the chord length is \(2\sin(\theta/2)\). To include \(e^H\), expand \(e^{\beta x\cdot Oy}\) in powers and expand each dot product into four coordinates. Each resulting term separates into functions of \(x,y\) of modulus at most one, with sum of absolute coefficients at most \(e^{4\beta}\). The other real factors cost at most \(e^{10\beta}\). The Haar expectation of \(H\) is zero, hence \(Z\ge1\) by Jensen. This gives the second bound in (5).

**PROVED (all spatial plaquettes at once).** Put \(A_p=\beta(1-w_p)\). There is an absolute integer \(J\) such that at every finite grid of the stated size and uniformly in the two ends,
\[
 \left|\mathbb E_{u,v}
           \exp\!\left(i\sum_p t_p A_p\right)\right|
       \le \prod_p h_\beta(t_p)^{1/J}
       \le \exp\!\left[-c J^{-1}\sum_p\min(t_p^2,1)\right].         \tag{6}
\]
Select for every root square \(p\) two adjacent edges. They occur together only in \(p\). With the other links fixed, multiplication by the two known links and quaternion inversion are orthogonal maps of \(\mathbb R^4\), so \(w_p=x\cdot Oy\) for the two selected quaternions. All other incident action terms are linear in one spin, with five unit coefficients per spin, including the temporal neighbours. This gives exactly the law of (5). In the marked phase every other term is constant or a one-variable phase on that pair, regardless of its coefficient. Colour root squares so that no action face or marked face sees chosen edges from distinct roots of one colour, and their edge pairs are disjoint. The conflict graph has absolutely bounded degree, so one fixed \(J\) bounds the number of colours. Take the colour carrying at least \(1/J\) of \(\sum_p-\log h_\beta(t_p)\). Conditional product integration on that colour, using (5) at \(-t_p\), proves (6). The omitted constant in \(A_p\) has unit-modulus phase. The argument with all links of a periodic four-torus works for arbitrary spacetime plaquettes as well, provided all periods are at least four. No continuum or weak-field approximation enters (5) or (6).

## Changing the spatial action at every time

**PROVED (continuous residues).** Take disjoint spatial plaquette sets \(S_b\), \(1\le b\le B\), each of cardinality at least \(k\), and set \(S_b^{\rm act}=\sum_{p\in S_b}A_p\). For \(h\ge1\), write \(R_b=(S_b^{\rm act}/h)\bmod1\). At fixed two-step bridge ends the joint law of \((R_b)\) has a continuous density \(g_{u,v}\) with respect to normalized Lebesgue measure on the \(B\)-torus as soon as \(k/J>4\). If \(k/h^2\) exceeds a fixed constant, then
\[
 \sup_{u,v,z}|g_{u,v}(z)-1|\le(1+\eta)^B-1=:\Delta,\qquad
 \eta=C e^{-c k/h^2}+C(1+h)e^{56\beta-c k}.                       \tag{7}
\]
Constants may change from (5)–(6). Indeed the Fourier coefficient at an integer vector \(\ell\) is bounded by \(\prod_b h_\beta(2\pi\ell_b/h)^{|S_b|/J}\) by (6). For \(d=k/J\), the nonzero frequencies with \(|2\pi\ell/h|\le1\) have sum at most \(C e^{-c k/h^2}\), by summing the Gaussian bound. At higher frequencies use \(h_\beta(t)^d\le e^{-c(d-4)} C^4 e^{56\beta}(1+|t|)^{-2}\). The sum of the last power over this grid is at most \(C(1+h)\) by comparison with its integral. The absolutely convergent series is continuous. Its integral against each trigonometric polynomial equals the bridge expectation. Uniform approximation of continuous functions by those polynomials identifies it as the density. Multiplication of the one-group sums after omitting the zero vector gives (7).

**PROVED (positive reweighting).** Hence for every bounded measurable \(W=W(R_1,\ldots,R_B)\ge0\) with strictly positive uniform mean \(\bar W\), the operator \(U W U/\bar W\) has kernel within \(\Delta U^2(u,v)\) of \(U^2(u,v)\). The bound is relative to the mean and allows both exact interval restrictions and very large ratios of maximum to mean. For sign-count residues use (2) with uniform counting measure, which gives the same conclusion with \(\delta\). In the next two paragraphs let \(\delta\) denote either bridge error, assume \(\delta<1\), and replace \(W\) by \(W/\bar W\). Its uniform mean is now one.

**PROVED (every slice).** The transfer \(V=W^{1/2} U W^{1/2}\) applies the new magnetic weight on every slice. Define \(B'=W^{1/2}U^2 W^{1/2}\). The positive eigenvalues of \(B'\) equal those of \(U W U\) by the \(XX^*,X^*X\) argument. Thus their ordered values differ from those of \(U^2\) by at most \(\delta\), and \(\|B'\|\le1+\delta\). Multiplication of the pointwise bridge bound by \(W^{1/2}\) at both ends gives \(|V^2-B'|(x,y)\le\delta B'(x,y)\), where the absolute value is of the kernel. Testing on \(|f|,|g|\) gives \(\|V^2-B'\|\le\delta(1+\delta)\). It follows that
\[
             |\lambda_i(V)^2-u_i^2|\le (2+\delta)\delta              \tag{8}
\]
for every ordered eigenvalue, uniformly in the height or rarity of the imposed weight. Normalizing \(V\) by its own top eigenvalue changes these squared eigenvalues by at most a further \((2+\delta)\delta\), since the change at any \(i\) is bounded by the change of the top squared eigenvalue from one. A uniform \(o(a)\) error therefore transfers any strictly positive physical lower bound on the first excited energy between the two models, with the same limiting lower bound when finite. This follows by comparing their normalized first squared eigenvalues to \(e^{-2ma}\), with arbitrarily small fixed slack in \(m\).

**PROVED (thermal normalization at all even periods).** Before vacuum normalization one has
\[
 (1-\delta)^{2j}\operatorname{Tr}U^{2j}
 \le \operatorname{Tr}V^{2j}\le
 (1+\delta)^{2j}\operatorname{Tr}U^{2j}\quad(j\ge1).              \tag{9}
\]
Form the cycle of \(j\) kernels \(V^2\), compare pointwise with \(B'\), and use \(\operatorname{Tr}(B')^j=\operatorname{Tr}(UWU)^j\). A second pointwise cycle comparison is with \(U^2\). At \(j=1\) the diagonal formulas follow from the Hilbert–Schmidt factorizations as for (4). Taking \(2j\)-th roots and \(j\to\infty\) gives \(1-\delta\le\lambda_0(V)\le1+\delta\). After vacuum normalization the trace ratio lies between \(((1-\delta)/(1+\delta))^{2j}\) and its reciprocal. For a centre-neutral trace with \(W\) invariant under the spatial centre flips, insert the neutral projector at the closing seam of the cycle. This projector averages the flips. Each resulting kernel trace has a nonnegative path integral. The top eigenfunction on the full space is centre invariant for the positive Wilson kernel, and for the rounded strictly positive kernel used next.

**PROVED (a locally constant magnetic action).** Partition the spatial plaquettes into sets of sizes between \(k\) and \(2k\), with \(k\) of order \((\log n)^2\), and take \(h=(\log n)^{1/4}\). One partition uses nearby plaquettes. Split the array for each orientation into coordinate lines, divide each line into segments of these sizes and distribute the remainder. Here \(n\) is the side in lattice units. On rectangles the same construction works when all sides are comparable to \(n\). Let \(\beta=O(\log n)\), \(\beta\ge1\). Equation (7) gives \(\Delta=o(n^{-A})\) for every fixed \(A\), even after multiplying the one-set errors over all \(O(n^3)\) sets. Use the unnormalized weight \(W=\exp(h\sum_b R_b)\), whose uniform mean is \(((e^h-1)/h)^B\). Then
\[
 e^{-\sum_b S_b^{\rm act}}W
       =\exp\!\left[-h\sum_b\left\lfloor S_b^{\rm act}/h\right\rfloor\right].
                                                                    \tag{10}
\]
Thus replacing each group’s spatial Wilson action by the indicated integer multiple of \(h\) at every time, with all temporal plaquettes at their original Wilson coupling, preserves the squared vacuum-normalized transfer eigenvalues up to \(o(n^{-A})\) for each \(A\). It preserves the full vacuum-normalized periodic thermal trace to relative error \(o(n^{-A})\) at even time periods \(O(n)\). The constant mean per slice cancels under vacuum normalization. The physical size of each group tends to zero when \(a=L/n\) with fixed \(L\). Constants in the bridge estimates are uniform in the end fields. Equation (10) also describes an actual positive transfer with a discontinuous magnetic weight at finite cutoff.

**PROVED (all periods needed by the thermal criterion).** The partition-function comparison in (9) holds at every integer period \(T\ge3\), including odd \(T\). Colour the vertices of the time circle with at most three colours so that adjacent vertices have distinct colours. Under the original periodic path measure, conditional on the slices off one colour, the middle slices of that colour have independent two-end bridge laws. The conditional mean of the product of their normalized \(W\)'s lies in \([(1-\delta)^l,(1+\delta)^l]\) for \(l\) sites. All other weights are nonnegative and measurable in the complement. Remove one colour in this way, then apply the same bound in the original expectation to the product of weights that remain, until none remain. For the periodic trace with a centre flip at the seam, relabel the adjacent endpoint by that flip and apply the bridge bound using the invariance of \(W\). This proves the all-period version for full and neutral traces.

**PROVED (the remaining thermal cost).** Let \(Z_{\rm rd}(s,T)\) use the action (10) before removing its constant mean and let \(Z(s,T)\) use the original action. Write \(\Psi_s(T)=2\log Z(s,T)-\log Z(s,2T)\), with \(\Psi_s^{\rm rd}\) defined likewise. For \(\Delta\le1/2\),
\[
             |\Psi_s^{\rm rd}(T)-\Psi_s(T)|\le8T\Delta .             \tag{11}
\]
The term \(T\log\bar W\) cancels exactly from the doubling defect, and the all-period bound costs at most \(2T\Delta\) in each log of length \(T\). Thus the actual periodic input (B**) of Bhattacharjee and coauthors would follow, with any fixed strict slack, from the corresponding upper bound for (10) on a window \(2T\le s_i<48T\), \(\beta=O(\log T)\), \(T\to\infty\) and \(aT\le t_0\) along the matched cutoffs. For clarity, the desired upper bound is \(y_0 s_1s_2s_3/[2(96T)^3]\), with \(0<y_0\le1/20\), on every required shape. The ratio \(s_1s_2s_3/T^3\) is bounded below by 8 on this window, while the error tends uniformly to zero. If the datum can be proved with the slack just specified, (11) puts it on the original Wilson action, to which the cited propagation theorem applies. The finite-box comparison uses \(\beta=O(\log n)\). [Row 1218, thermal window](prior/gap-onebound-read-sol.md)

## Testing an expansion in the integer magnetic actions

**GUIDE.** In (10) each unit increase of an integer magnetic action has Boltzmann factor \(e^{-h}\), which tends to zero for the stated \(h\). A possible attack on (11) is to expand around a preferred integer value in each group and pay for the groups where that value changes. This requires a probability estimate in the rounded Wilson bridge.

**PROVED (density on the real line).** For a single \(S_b\) of size at least \(k\), the conditional density of its unwrapped \(S_b^{\rm act}\) on \(\mathbb R\) is bounded by
\[
 L_k=C k^{-1/2}+C e^{56\beta-c k},\qquad k/J>4 .                   \tag{12}
\]
Integrate \((2\pi)^{-1} h_\beta(t)^{k/J}\) over \(\mathbb R\), splitting at \(|t|=1\) exactly as in (7). At low frequencies the integral of \(e^{-c k t^2}\) costs \(C/\sqrt{k}\). To identify the inverse transform as the density, multiply the characteristic function by \(e^{-\varepsilon t^2}\) and invert. This gives the density after adding an independent Gaussian. Dominated convergence gives a uniform limit representing the original measure on compactly supported tests.

**PROVED (joint bound with other groups fixed modulo \(h\)).** For any set \(I\) of groups, keep their real, unwrapped actions and keep all other group actions modulo \(h\) in normalized coordinates. The joint density with respect to ordinary \(ds_i\) on \(I\) and probability torus measure on its complement is bounded above by \(L_k^{|I|}(1+\eta)^{B-|I|}\). Apply (6) to the mixed Fourier transforms, integrate the real frequencies on \(I\) using (12), sum the other integer frequencies using (7), and invert as in those proofs. This bound holds pointwise in the two ends.

**PROVED (failure of a dilute expansion about one level).** In a two-step bridge of the fully rounded model, with arbitrary ends, the law of the middle is the original middle law reweighted by \(W=\exp(h\sum R_b)\) and divided by its conditional mean. The endpoint factors cancel. Set \(N_b=\lfloor S_b^{\rm act}/h\rfloor\). For any prescribed integers \(d_b\), possibly chosen from the ends, and any subset \(I\),
\[
  \Pr_{\rm rd}\{N_b=d_b\ (b\in I)\mid u,v\}
  \le\frac{(1+\eta)^{B-|I|}}{1-\Delta}\,(h L_k)^{|I|}.             \tag{13}
\]
On a prescribed real bin the integral of \(\exp(h R_b)\,ds_b\) is \(h(e^h-1)/h=e^h-1\). Each other group contributes \((e^h-1)/h\) after integration on its unit torus. Divide by at least \((1-\Delta)((e^h-1)/h)^B\). This proves (13), even for bins whose actual support is smaller than a full interval. In the logarithmic choice made above \(hL_k\to0\). For any assignment of one baseline per group using the two ends, the conditional expected *fraction of matches* tends to zero uniformly. Even a set of \(o(\sqrt{k}/h)\) candidate levels per group has vanishing match probability, by summing the one-group bound. In particular fixing the baseline to the preceding time slice gives the same failure. No estimate on the excitation energy follows from the small factor \(e^{-h}\) per level in (10).

**PROVED (unwrapped variance).** Directly in the ordinary Wilson bridge,
\[
  \operatorname{Var}_{u,v}\!\left(\sum_p b_p A_p\right)
       \ge c'\sum_p b_p^2
\]
for all real \(b_p\). Substitute \(t_p=\tau b_p\) in (6). Boundedness at fixed grid gives a characteristic-function modulus of \(1-\tau^2\operatorname{Var}_{u,v}/2+o(\tau^2)\) as \(\tau\to0\). Comparison gives the inequality. This concerns a conditional variance within one middle slice. Time correlations of the conditional means still enter the vacuum transfer.

## Dependence of the integer actions on the two ends

**GUIDE.** Equation (13) permits a broad distribution of integer levels with a mean that depends on the end fields. To test this possibility in the actual Wilson integral, take two copies of the same spatial end field, first flat and then with a weak, coherent abelian flux. The following comparison is for the physical kernel with vertex gauge averaging included.

**PROVED (an energy estimate with fixed ends).** Put \(N=n^3\) and \(d(q)=1-\tfrac12\operatorname{tr}q=|1-q|^2/2\) in quaternion chord distance. For an end field \(A\), let \(D(A)=\sum_{p\ {\rm spatial}} d(A_p)\). On a slab of \(T\ge2\) steps with both ends \(A\), let \(\mathcal E\) be the sum of dimensionless deficits on all temporal faces and all *interior* spatial faces. Endpoint magnetic weights are fixed. There is an absolute \(C_0\) such that, for \(\beta\ge1\), \(\log\beta\le NT\),
\[
 \Pr_{A,A}\{\mathcal E>C_0 T(N/\beta+D(A))\}\le e^{-NT}.            \tag{14}
\]
To see the normalization, choose temporal gauge on the first \(T-1\) steps by successive Haar changes of spatial variables at the interior vertices. Gauge invariance of the plaquette weight leaves \(m=3N(T-1)\) free middle spatial links and \(N\) independent Haar vertex frames \(g_x\) for the last end \(A^g\). Each removed gauge integral has mass one. Write \(Z_\beta(A,A)=\int e^{-\beta\mathcal E}\) in these variables. For an upper bound on \(Z_{\beta/2}\), drop the interior magnetic terms and keep only spatial spanning-tree edges on the last temporal step. For fixed previous slice, integration over the last frame leaves, one leaf at a time, a factor \(z_{\beta/2}=\int e^{-(\beta/2)d(q)}dq\) per tree edge, independent of the prescribed parallel transports. The remaining \(T-1\) layers integrate from the top down and give exactly \(z_{\beta/2}^{m}\). Thus \(Z_{\beta/2}\le(C\beta^{-3/2})^{m+N-1}\). The one-link bound follows by polar integration using \(1-\cos\alpha\ge2\alpha^2/\pi^2\) on \([0,\pi]\).

**PROVED.** For a lower bound on \(Z_\beta\), require each middle link to be within angle \(1/\sqrt\beta\) of the corresponding \(A_e\), and each \(g_x\) within that angle of the identity. Each cap costs at most a factor \((c\beta^{-3/2})^{-1}\) in inverse probability. All temporal deficits are then at most \(C/\beta\). For a middle plaquette, replacing its four factors by the end factors changes the chord by at most \(4/\sqrt\beta\), by bi-invariance. Hence \(d(X_p)\le2d(A_p)+C/\beta\). This gives
\[
 Z_\beta\ge(c\beta^{-3/2})^{m+N}
              \exp[-C NT-2\beta T D(A)] .
\]
Consequently \(Z_{\beta/2}/Z_\beta\le \beta^{3/2}\exp[C NT+2\beta T D(A)]\). On \(\{\mathcal E>b\}\) use \(e^{-\beta\mathcal E}\le e^{-\beta b/2}e^{-\beta\mathcal E/2}\). The condition on \(\log\beta\) absorbs the remaining \(\beta^{3/2}\). Choosing \(C_0\) large proves (14) for *every* end field.

**PROVED (a smooth flux detectable through a growing slab).** Fix a sufficiently large \(K>1\) below in the order of choices. Take integers \(R\to\infty\), \(\beta=K R^4\), and spatial side \(n\) a multiple of \(2R^2\). For example one may take \(n=2R^2\lceil e^{\beta/b_*}/(2R^2)\rceil\) with \(b_*=11/(3\pi^2)\). Fix a unit imaginary quaternion \(\mathbf i\) and put
\[
 A_1(x)=A_3(x)=1,\qquad A_2(x)=\exp(\mathbf i\,\pi x_1/R^2).
\]
This is periodic. Its only nonzero plaquette deficits are in the \(12\) plane, each equal to \(1-\cos(\pi/R^2)\le5/R^4=5K/\beta\). Every oriented \(R\times R\) square in that plane has boundary holonomy \(-1\). Let \(D_{12}(X_t)\) denote the sum of its \(N\) elementary \(12\)-plaquette deficits in slice \(t\). For every completion and \(1\le t<T\),
\[
 2\le R^2\sqrt{2D_{12}(X_t)/N}+4R\sqrt{t\,\mathcal E/N}.           \tag{15}
\]
Indeed, bound the chord of the bottom square holonomy by the chords of the elementary faces of the top filling and its four vertical sides. Peeling the disk of faces replaces a boundary product with elementary face products conjugated to one root. Chord distance is invariant under these conjugations and is subadditive for products. Equivalently, first telescope each boundary edge transport along its time ribbon and then fill the top square row by row. Average over all spatial base points. Each top face is counted \(R^2\) times. At each time below the top, each temporal face of orientation 01 or 02 occurs \(2R\) times. Cauchy–Schwarz separately on the top sum and jointly on the two side orientations and \(t\) layers gives (15). The central bottom holonomy makes the left side independent of every frame.

**PROVED.** Let \(T=\lfloor c_0 R\rfloor\), where \(c_0>0\) is chosen with \(4c_0\sqrt{6 C_0}<1\). On the event supplied by (14), \(\mathcal E/N\le 6 C_0 T/R^4\). The second term in (15) is then less than one. Thus at *every* interior time \(\beta D_{12}(X_t)/N\ge K/2\), except on one event of probability at most \(e^{-NT}\). At flat ends, (14) gives instead
\[
 \frac{\beta}{N(T-1)}\sum_{t=1}^{T-1}D_{12}(X_t)\le2 C_0
\]
with the same probability bound. Choose \(K>12 C_0+12\) and then let \(R\) grow. The statistics distinguish the two physical Wilson bridges with probability tending to one, even though their maximum individual end deficits differ by only \(O(1/\beta)\).

**PROVED (after rounding).** Use the orientation-wise partition in (10). Replacing all interior magnetic actions changes the unnormalized middle weight by a factor in \([1,\exp(hB(T-1))]\). Here \(hB=o(N)\), so a failure event of bridge probability at most \(e^{-NT}\) still has probability at most \(e^{-(1-o(1))NT}\). Also \(\big|\beta D_{12}(X_t)-h\sum_{b\ {\rm of\ type}\ 12}N_b(X_t)\big|\le hB=o(N)\). The two experiments therefore have asymptotically disjoint distributions for the *same mean of the rounded integer actions* over the interior. In particular a comparison that replaces these integers by an end-independent law uniformly over all end fields with plaquette deficits at most \(5K/\beta\) fails even at time thickness of order \(\beta^{1/4}\). These prescribed end fields need no positive vacuum probability for this conclusion about a uniform bridge bound. At fixed \(L\), the physical thickness \(aT\) of this test tends to zero.

## Does the Fourier estimate force the one-scale thermal bound?

**PROVED (a test with the actual magnetic energy of a free field).** In the four-dimensional real scalar lattice model take the action
\[
 \frac12\sum_{\langle xy\rangle}(\phi_x-\phi_y)^2
       +\frac{\mu^2}{2}\sum_x\phi_x^2,\qquad 0<\mu\le1 .
\]
Use periods at least four. Its magnetic readings are \(A_{xy}=(\phi_x-\phi_y)^2/2\) on all spatial edges. The positive Fourier multiplier of the temporal Gaussian convolution and the magnetic half-weights give a positive time transfer. In a two-step bridge one has, for an absolute \(J'\),
\[
 \left|\mathbb E_{u,v}\exp\!\left(i\sum_e t_e A_e\right)\right|
 \le \prod_e (1+c t_e^2)^{-1/(4J')}.                              \tag{16}
\]
Indeed, keep the two sites of a spatial edge and condition on the rest, including the two ends. Their joint Gaussian precision has diagonal \(8+\mu^2\) and off-diagonal \(-1\). Thus its covariance \(C\) dominates \(I/10\), irrespective of its mean. The quadratic form in the phase on these two sites has symmetric matrix \(D\) with off-diagonal \(-t_e/2\). The operator norm of \(C^{1/2}DC^{1/2}\) is at least \(|t_e|/20\), by expressing \(D\) through \(C^{-1/2}\). After translating and whitening the two variables, diagonalize this symmetric matrix. For each independent standard Gaussian \(Z\), completion of the square gives
\[
 |\mathbb E e^{i(\lambda Z^2+b Z)}|
 =(1+4\lambda^2)^{-1/4}
   \exp[-b^2/(2(1+4\lambda^2))].
\]
Using the larger absolute eigenvalue bounds the two-site expectation by \((1+c t_e^2)^{-1/4}\). A bounded colouring of edges separates pairs with no common action term between them. Choosing the colour that maximizes the sum of \(\log(1+c t_e^2)\) and integrating conditionally proves (16). This estimate also gives continuous residue densities as in (7) by Fourier inversion. Row 1211 earlier used a free scalar to test a wall-observation bound. The comparison here concerns the joint Fourier transform of the *spatial action itself*. [Earlier free-field test](gap-solve22-astra62.md)

**PROVED (failure of the thermal input in this comparison).** The one-scale doubling defect can diverge in this model. Diagonalize the spatial Laplacian in a real orthonormal basis. If its eigenvalue is \(\lambda\), set \(2\cosh\omega=2+\mu^2+\lambda\). For a temporal period \(T\) the determinant of its precision is
\[
 \prod_{j=0}^{T-1}\big(2\cosh\omega-2\cos(2\pi j/T)\big)
        =e^{T\omega}(1-e^{-T\omega})^2.
\]
This follows by writing each factor as \(e^\omega|1-e^{-\omega}e^{2\pi i j/T}|^2\) and multiplying the roots of unity. The Gaussian integral therefore contributes \(\log[(1+e^{-T\omega})/(1-e^{-T\omega})]\) to \(\Psi_s(T)\), after cancellation of the per-time normalization. Every contribution is positive. Take \(\mu=a^2\) and a physical time \(aT\to t>0\). The spatial zero mode has \(\omega=2\operatorname{arsinh}(\mu/2)\le\mu\), so \(T\omega\to0\) and its contribution alone tends to infinity. This violates the constant window threshold even on \(s=(2T,2T,2T)\).

**PROVED (a local action reading also sees zero mass).** Take infinite spatial volume at each cutoff. At separation \(l>0\) the covariance of two equal-direction spatial differences at the same spatial point is
\[
 \int_{[-\pi,\pi]^3}
 \frac{4\sin^2(k_i/2)}{2\sinh\omega(k)}e^{-l\omega(k)}
       \frac{d^3 k}{(2\pi)^3},\qquad
 2\cosh\omega(k)=2+\mu^2+\sum_j4\sin^2(k_j/2).
\]
The one-dimensional time Green function follows by substituting \(e^{-|l|\omega}/(2\sinh\omega)\) in the second-order difference equation, including its unit jump at \(l=0\). For \(\mu=a^2\), \(l=\lfloor t/a\rfloor\), multiply the covariance by \(a^{-4}\) and put \(k=ap\). Its limit is the strictly positive integral of \(p_i^2 e^{-t|p|}/(2|p|)\,d^3p/(2\pi)^3\), proportional to \(t^{-4}\). For fixed \(t>0\), \(\omega(k)\ge c|k|\) on the Brillouin cube, by \(\sin(|k_j|/2)\ge |k_j|/\pi\) and the bounded argument of \(\operatorname{arsinh}\). The new integrand is dominated by \(C|p|e^{-ct|p|}\) for all sufficiently small \(a\). Gaussian fourth moments give a strictly positive multiple of \(t^{-8}\) for the connected covariance of the corresponding squared differences after rescaling. A positive time padding gives finite norm, and the same polynomial tail at larger times excludes a positive lower edge for that local spectral measure. Thus even the sector read by the nonnegative magnetic energies retains massless propagation despite (16). This spectral calculation is for the comparison field.

**PROVED (what a positive-time scalar test sees in the comparison field).** More explicitly, the limiting measure for the squared spatial difference in (16), after positive time padding, is proportional to the image under \((p,q)\mapsto |p|+|q|\) of
\[
 e^{-t_0(|p|+|q|)}
 \frac{p_i^2 q_i^2}{|p|\,|q|}\,d^3p\,d^3q,\qquad t_0>0.
\]
This follows by multiplying the two limiting Fourier integrals in the fourth-moment calculation. It is finite and gives positive mass in every interval \((0,\varepsilon)\). The test of (6) against a massless theory thus survives removal of the isolated spatial zero mode.

## Local insertions in the finite-volume comparison

**PROVED.** There is also a comparison for correlations before either continuum limit. Work in the raw periodic Wilson path integral on \(n^3\times T\), \(4\le T\le n^C\) for a fixed \(C\). Keep the magnetic partition in (10) at every time. Condition on any prescribed list \(L_0\) of at most \(m\) raw spacetime links. In the four-dimensional proof of (6), omit from the choice of roots every plaquette whose chosen two-edge set meets \(L_0\). At most \(6m\) roots are lost on the whole torus, since a link belongs to at most six plaquettes. The characteristic function still includes *every* member of every group. The omitted roots simply supply no contraction. In each retained pair the rest of the phase is still constant or a one-link term, and all variables in \(L_0\) lie in its exterior. The proof of (6) therefore works conditionally, using at least \(k-6m\) roots per group. This uses the explicit conditional Wilson densities on the finite compact grid.

**PROVED.** Let \(\Delta'=(1+\eta')^{BT}-1\), with the constants from the four-dimensional colouring and the bound in (7) evaluated at \(k-6m\). Write \(\mathbb P,\mathbb P_{\rm rd}\) for the original and rounded periodic laws, respectively. Integrate the product of all the positive rounding weights against the joint residue density, first given \(L_0\) and then unconditionally. Both integrals, divided by the common uniform mean to the power \(T\), are in \([1-\Delta',1+\Delta']\). By the definition of conditional expectation their ratio is the marginal density of the rounded law relative to the ordinary law on the listed links. Consequently, if \(\Delta'<1\),
\[
 \left\|\frac{d(\mathbb P_{\rm rd}|_{L_0})}
                {d(\mathbb P|_{L_0})}-1\right\|_\infty
       \le \frac{2\Delta'}{1-\Delta'}.                              \tag{17}
\]
For \(m\le k/12\), \(\beta=O(\log n)\) and the choices in (10), this is smaller than any inverse power of \(n\). The estimate is uniform in which \(m\) links were listed, including overlapping supports of different insertions. In particular, for a sum of products of a fixed number of local plaquette readings, with the sum of the absolute coefficients times the sup norms of the products bounded by \(n^C\), the two periodic expectations differ by \(o(n^{-A})\) for every fixed \(A\). Apply (17) to each product and sum. This includes polynomial cutoff renormalizations and finite smearing sums with that growth bound. It compares two laws on the same finite physical boxes. It supplies neither convergence of these expectations nor the infinite-volume uniformity needed for a Wightman construction.

## Remaining physical estimate

**OPEN.** Bound the doubling defect itself on the full window along the tuned isotropic Wilson trajectory. In the notation of row 1218 this requires one \(t_0>0\), one \(0<y_0\le1/20\), and for every sufficiently large physical volume index \(p\) and every sufficiently fine cutoff at that \(p\), a common integer \(3\le T\le t_0/a\) for all integer shapes \(2T\le s_i<48T\). For the rounded route it suffices to choose \(T\to\infty\) with \(\beta=O(\log T)\) and to bound \(\Psi_s^{\rm rd}(T)\) by \((1-\varepsilon)y_0 s_1s_2s_3/[2(96T)^3]\) for some fixed \(\varepsilon>0\). Equations (5)–(11) control the error in replacing this quantity by another one. I have no upper estimate of the required size for either quantity. Equation (13) rules out the proposed expansion around a single occupied level. Equations (14)–(15) show how the integer actions can retain boundary information. The comparison in (16) tests explicitly why the short-time estimate alone cannot supply the long-time bound.

**OPEN.** For the Jaffe–Witten conclusion one must also construct a nontrivial continuum theory on \(\mathbb R^4\) with the required local Yang–Mills observables and quantum-field axioms, a vacuum \(\Omega\) with \(\ker H=\mathbb C\Omega\), a nonempty excited space and one \(m>0\) with \(\operatorname{spec}(H|_{\Omega^\perp})\subset[m,\infty)\). The finite-volume comparison of insertions in (17) supplies no such construction. The arguments in this file are author-side hand derivations and have no independent check.

RESULT — OPEN. I did not prove the four-dimensional SU(2) Jaffe–Witten mass gap. PROVED here at finite cutoff, pending independent checking, the magnetic-action Fourier bound (6) and the spectral and thermal comparisons (8)–(11) for rounding that action. The weak-coupling thermal bound itself and the continuum construction remain open.
