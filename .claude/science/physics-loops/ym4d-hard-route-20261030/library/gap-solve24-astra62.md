## Repo search

**GUIDE.** Row 1222, research at `6d5dd935d`. The target-specific prior note is absent at this pin. The target is a nontrivial continuum four-dimensional SU(2) Yang–Mills theory in the Jaffe–Witten sense, with the required local fields and axioms, and with an interval above the vacuum free of energy spectrum.

**GUIDE.** The lead's November 8 search covered main and PRs 10114, 10133, 10134 and 10141. Its closest named hit was the one-step Wilson loop witness. I read that argument at `f76f6c649`, lines 4–14 and 106–149 of `.claude/science/toe-ruleset-20261021/agents/ym4d-proof/MASS_GAP_LOCAL_BLOCK_ASTRA.md`. Positivity at one step gives no uniform decay rate. Grok's crossover table on PR 10133 (`89faef229`, lines 77–86) leaves crossover and source transport open. PR 10134's `mass-gap-interface.md` at `1e70c7211` distinguishes an excited space, a gap and identification. PR 10141's `research/ym4d/library/fp1.md`, lines 299–315, controls a classical constrained quadratic form. Main's `research/mass-gap/library/gap-phys-seed.md`, lines 305–329 at `8b11ae2bb`, gives a conditional criterion for the physical transfer trace. I found no registry owner for the Wilson cube-dynamics comparison considered below. [Lead's search](prior/repo-search-2026-11-08.md) · [Registry](open-registry.md)

## Choice of approach

**GUIDE.** Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, distinguish scalar reconstruction from a full observable algebra and polynomial decay from a spectral interval. The outline says “Its support reaches zero” at 31878. I read outline 578–600, 3715–3725 and 31860–31882, and complete account I 2704–2714 and 3213–3222, at `31a47c543775`. Their examples and exclusions are prior work. Rows 1145 and 1215 give a further reason to retain more than long straight transports in this problem. At the physical scaling those readings can lose overlap with low-energy Wilson states. Row 1211 already uses spatial box walls to measure a physical transfer operator. [Outline index](sa-index/chunk-29.md) · [Straight transports](gap-solve2-astra62.md) · [Spatial wall observations](gap-solve22-astra62.md) · [Row 1215](gap-solve23-astra62.md)

**GUIDE.** Row 1218 compares new work by Deep Bhattacharjee, Ushashi Bhattacharya, James Montgomery Lockwood and Tristan Romanov, work with Ikailo John Sessford and Sanjeevan Singha Roy on a thermal seed, and work by Zeng Chunping. I take the four authors' cube heat-bath approach as the starting point. Their finite-volume progress for long straight links leaves the fine-field comparison open. I use the Markov property on complete boundaries of four-dimensional cells to integrate all interior Wilson fluctuations, then estimate what several shifts of the boundaries retain. This uses the full Wilson measure at each step. [Row 1218, including its source and version limitations](prior/gap-onebound-read-sol.md)

## What a complete cell boundary pays for

**PROVED.** Take the four-dimensional periodic Wilson lattice of side \(N\) in fine links. Write \(b\mid N\), \(N\ge4b\). The law \(\mu\) has density proportional to \(\exp(\beta\sum_p\operatorname{Re}\operatorname{tr}U_p/2)\) against independent normalized Haar measures. Work in the gauge-invariant subspace of \(L^2(\mu)\). For a set of links \(D\), let \(P_D f=\mathbb E_\mu[f\mid U_D]\) and \(d_D(f)=\|f-P_Df\|_2^2\). The conditional expectation preserves gauge invariance because \(\mu\) is gauge invariant and the vertex gauge group preserves each link sigma-field.

**PROVED.** For an offset \(s\in(\mathbb Z/b)^4\), tile the torus by closed cells of side \(b\). Let \(W_s\) retain every link tangent to at least one cell wall. A link in direction \(\mu\) with base \(x\) is retained precisely when \(x_\nu=s_\nu\bmod b\) for some \(\nu\ne\mu\). Each remaining link belongs to the private set \(I_C\) of exactly one cell \(C\). A plaquette lies in a closed cell. If several cells contain it, an entire coordinate wall contains it and all its links are retained. Thus each Wilson factor reads private links in at most one cell. Given \(U_{W_s}\), the private fields have independent conditional laws, including for arbitrarily large finite \(\beta\).

**PROVED.** Let \(V_x\) consist of all positively oriented links based in \(x+[0,b)^4\). Set \(\mathcal E_b(f)=b^{-4}\sum_x d_{E\setminus V_x}(f)\), with \(E\) the full link set. Then
\[
  \frac1{b^4}\sum_s d_{W_s}(f)\ \le\ \mathcal E_b(f).                 \tag{1}
\]
Indeed the projections which integrate one \(I_C\) conditional on its complement commute, by the product disintegration. Their product is \(P_{W_s}\). For commuting orthogonal projections \(Q_i\), telescope \(1-\prod_iQ_i\) into the mutually orthogonal differences \((\prod_{j<i}Q_j)(1-Q_i)\). This bounds its quadratic form by \(\sum_i(1-Q_i)\). The base of each private link belongs to the half-open cell of bases with the same lower corner \(x\), so \(I_C\subset V_x\). Integrating all of \(V_x\) has at least as large a squared residual. Summing over offsets counts each lower corner exactly once and proves (1).

**PROVED.** In particular take any \(k\) fixed offsets \(s_i\). If for every mean-zero invariant \(f\),
\[
       \frac1k\sum_{i=1}^k d_{W_{s_i}}(f)\ \ge\ \omega\|f\|^2,       \tag{2}
\]
then the same lower bound holds for \(\mathcal E_b\), with precisely this \(\omega\). Translate (2) by every common offset and average, using translation invariance of the law. This proves an actual Wilson comparison, uniform in volume and coupling. The physical input sought by the cube route is a fixed \(\omega>0\) for some \(a b\le\ell<\infty\) along the continuum sequence. Equation (1) makes the interior comparison at that scale exact. It leaves the estimate (2) on the retained boundaries.

## Four displaced boundaries

**PROVED.** Write \(b=4h\), \(h\ge5\), and take constant offsets \(s_i=((i-1)h,\ldots,(i-1)h)\), \(1\le i\le4\). Write \(W_i=W_{s_i}\), \(S_j=\bigcap_{i=1}^jW_i\). For each link only its three transverse coordinates can decide wall membership. Consequently \(S_4=\varnothing\). The first three walls nevertheless retain a common *contractible* loop. Fix \(x_2=0,\ x_3=h\), and in the other two coordinates take a square with coordinate endpoints \(2h,2h+b\). Each of its links lies on all three walls. Its normalized trace has positive variance at every finite \(\beta\), since the Wilson law has a strictly positive density and the trace is continuous and nonconstant. Its centered trace has \(d_{W_i}=0\) for \(i\le3\). Three such updates cannot give (2), even on local gauge-invariant functions. Four suffice to erase every link at \(\beta=0\), since coordinate conditional expectations of a product law compose by intersecting their retained link sets.

**PROVED.** For the *actual* Wilson law write \(\Pi_0 f=\mu f\). On the invariant subspace the final overlap satisfies
\[
 \big\|P_{W_4}P_{S_3}-\Pi_0\big\|
 \ \le\ \frac{2\delta}{\sqrt{1-\delta}},\qquad
 \delta=(1+\eta)^M-1<1,\qquad
 \eta=\sum_{d=2}^{\infty}d^2
       e^{-(d-1)(h-2)/(1+6\beta)}.                                   \tag{3}
\]
One may take \(M=4(N/h)^4\). To see this, each link in \(S_3\) has the three transverse residues \(0,h,2h\bmod b\) in some order. It belongs to a straight line of such links. Cut every line at the vertices whose remaining coordinate is a multiple of \(h\). This gives a subgraph of the cubic \(h\)-grid with at most \(M\) segments. All its uncut interior vertices have degree two. A gauge-invariant function of its fine links depends only on their ordered segment transports. Indeed independent vertex gauges at the interior vertices can set all but the last link of each segment to the identity. This argument also holds in \(L^2\), by first averaging representatives over the compact vertex group, or by dense invariant continuous functions. The finite-volume positive Wilson density is equivalent to Haar.

**PROVED.** On each segment leave its first and last fine links fixed and expose all links outside the selected interiors. Distinct selected links share no plaquette. Perpendicular segments could have shared a plaquette only within one step of an \(h\)-grid vertex. In particular \(U_{W_4}\) is exposed. Row 1145, (1)–(3), gives conditional independence of the transports and bounds their joint density relative to product Haar \(\nu\) between \(1-\delta\) and \(1+\delta\). This uses Sussman and Alpoge's one-link identity GL3, proved at outline 2197–2231, and row 1145's Bessel-ratio bound. Averaging preserves the same inequalities given \(U_{W_4}\) and unconditionally. If \(g\) is centered under the Wilson law and depends invariantly on \(S_3\), then \(|\nu g|\le\delta\|g\|_{L^1(\nu)}\). Hence \(\|P_{W_4}g\|_\infty\le2\delta\|g\|_{L^1(\nu)}\le 2\delta(1-\delta)^{-1/2}\|g\|_{L^2(\mu)}\). Apply this to \(g=P_{S_3}(f-\mu f)\) to prove (3). [Row 1145, straight transports](gap-solve2-astra62.md) · [Outline index for GL3](sa-index/chunk-02.md)

**PROVED.** The bound in (3) tends to zero if \(h/(1+6\beta)\to\infty\) and \(\log (N/h)=o(h/(1+6\beta))\). Indeed the series for \(\eta\) is bounded by \(C\exp[-(h-2)/(1+6\beta)]\) once its exponent scale exceeds one. Then \(M\eta\to0\). This allows a torus whose physical side tends to infinity along the cutoff sequence, with \(a b\) fixed and \(\beta=O(\log(1/a))\). It does not provide a bound for all \(N\) at a fixed \(\beta,b\).

## Prescribing the transports and keeping the fine observables

**GUIDE.** The primary text of *One Cube Estimate Implies the Yang–Mills Mass Gap*, v7, defines the form in (1) at lines 5850–5918, requires an infinite set of tori at each cutoff at 6106–6120, and leaves the fine-field ascent open at 8243–8267. Corollary 166 at 12137–12144 concerns the straight-path marginal. Row 1161, (23), already gives the simultaneous coloring for every straight *winding* in all four directions. I use it on finite segments to condition Wilson theory at a specified value while retaining its fine-field observables and the absolute partition-function normalization. [Bhattacharjee, Bhattacharya, Lockwood and Romanov, v7](https://hexagonmath.org/2610.00341v7) · [Row 1161](gap-solve9-astra62.md)

**PROVED.** Take a rectangular torus with periods divisible by \(h\in8\mathbb N\). Tile *every* coordinate line into disjoint oriented segments of length \(h\). There are \(M=4|\Lambda|/h\) segments and every fine link occurs in exactly one of them. Any subcollection is also allowed, with \(M\) its own cardinality. Denote their products by \(Y=(Y_\gamma)\). Use \(dH(c)\) for product Haar measure on their values. Pick a set \(D\) of links to be measured. Suppose \(|D\cap\gamma|\le r<h/8\) on each retained segment. Set
\[
   u=(h/8-r)/(1+6\beta),\quad
   \eta_u=\sum_{d\ge2}d^2e^{-(d-1)u},\quad
   \delta_r=(1+\eta_u)^M-1 .
\]
For \(\delta_r<1\), the canonical Wilson law \(\mu^c\) with all \(Y_\gamma=c_\gamma\) satisfies, for every fixed \(c\) and every integrable \(F=F(U_D)\),
\[
 \left|\mu^c F-\mu F\right|
       \le {2\delta_r\over 1-\delta_r}\,\mu |F|,\qquad
 \left|{Z^c\over Z}-1\right|\le\delta_0 .                              \tag{4}
\]
Here \(Z^c\) is the density of the pushforward of the unnormalized Wilson measure against \(dH(c)\). This definition fixes the normalization even when the number of prescribed matrices changes with the torus. There is no small-ball volume in (4).

**PROVED.** Use row 1161's coloring with period eight. Select the link \((x,\mu)\) for \(\sum_\nu x_\nu=2\mu\bmod8\), \(0\le\mu\le3\), in a retained segment unless it is in \(D\). A plaquette uses bases of two consecutive residues. Only one can be even and just one direction belongs to it. Each segment has at least \(h/8-r\) private links. Given the other links \(\mathcal E\), the segment products have conditional joint density \(p_{\mathcal E}(c)\) between \(1-\delta_r\) and \(1+\delta_r\) by the Fourier bound already cited. In particular the marginal density \(p(c)=\mu p_{\mathcal E}(c)>0\) satisfies the same bounds. Bayes' formula gives
\[
      \mu^c F = {\mu[F\,p_{\mathcal E}(c)]\over p(c)} .
\]
This proves the first inequality. With \(D=\varnothing\) it gives the second from \(p(c)=Z^c/Z\). The continuous versions at every \(c\) agree with the direct constrained integral. For that integral eliminate the last fine link in each segment using its ordered product. Haar translation has Jacobian one. The remaining Wilson density is positive and continuous on a compact space. For a bounded measurable \(F(U_D)\) the same pointwise formula follows by integrating a selected link outside \(D\) on each segment. Truncation extends the estimate to the stated integrable functions. On the common graph alone the private links of (3) give the same argument with \(h-2-r\) private links per segment, with no divisibility of \(h\) by eight needed.

**PROVED.** This estimate passes to normalized local insertions without assuming a bound on the full field's pointwise continuum limit. Suppose \(F_j=\sum_\alpha c_{\alpha j}f_{\alpha j}\), with \(|f_{\alpha j}|\le1\), each monomial meeting any segment in at most \(r\) links, and \(\sum_\alpha|c_{\alpha j}|\le B_j\). The error in a one-point expectation is bounded by \(2B_j\delta_r/(1-\delta_r)\). The analogous bound on a product of two insertions uses \(B_j^2\) and \(\delta_{2r}\). It holds at any relative translation and for reflected insertions with the same link bound. For example take \(N_j,a_j^{-1},B_j\) polynomially related, \(\beta_j=O(\log(1/a_j))\), and \(h_j\) divisible by eight with \(h_j/(\log(1/a_j))^2\to\infty\), on commensurate tori. For fixed \(r\) all these errors vanish faster than any power of \(a_j\), even if \(a_j h_j\to0\). This establishes agreement on the stated family of observables. Totality for a proposed continuum theory is a separate requirement.

**PROVED.** In particular the *full* Wilson thermal doubling defect \(2\log Z(s,t)-\log Z(s,2t)\) changes by at most \(3[-\log(1-\delta)]\) if every prescribed segment is set to the identity on each torus. Here \(\delta\) bounds the two errors \(\delta_0\), and the periods are as above. This estimate involves the full partition function, including all flux sectors in its original definition. One may handle incommensurate periods divisible by eight by using segment lengths in \([h,2h)\) divisible by eight when a period is at least \(h\). Divide its length in units of eight into consecutive groups of length \(h/8\) and put the remainder into the last group. The same proof uses the shortest segment length. Each coordinate coloring still closes around the torus. No assertion about a shape outside these hypotheses is needed for the periodic-cube test of the lane.

## A local spin integral for the full periodic defect

**PROVED.** Set each straight *winding* to the identity, taking one segment the length of its circle in (4). Equivalently introduce four \(SU(2)\) variables \(v_\mu(x)\) at each site, with independent Haar reference, and put
\[
       U_\mu(x)=v_\mu(x)^{-1}v_\mu(x+\hat\mu),\qquad
       R_{\mu\nu}(x)=v_\mu(x)v_\nu(x)^{-1}.
\]
On a circle the map from its spins to one base spin and all successive increments except the last preserves product Haar. The last increment is fixed by the identity winding. Integrating out the base spin gives the normalized constrained link integral. Different directional circles use disjoint spin coordinates even at their intersections. A cyclic permutation inside the trace gives the plaquette observable
\[
 w_{\mu\nu}(x)=\tfrac12\operatorname{tr}
 [R_{\mu\nu}(x)^{-1}R_{\mu\nu}(x+\hat\mu)
  R_{\mu\nu}(x+\hat\mu+\hat\nu)^{-1}R_{\mu\nu}(x+\hat\nu)] .             \tag{5}
\]
Thus \(Z^\mathbf1\) is a nearest-plaquette spin integral with the six original Wilson couplings. In this winding version use \(h=\min_\mu N_\mu\) in the error and count the actual circles. The same four-site word occurs in the two-frame frozen-plane model in Lemma A0 of the earlier corner calculation. Formula (5) here uses separate primitives for *all four* directions at finite Wilson coupling. [Earlier corner calculation](gap-mini-solve-b-fable.md)

**PROVED.** On \(\mathbb Z^4\) at fixed finite \(\beta\), the spin formulation also has a local interpretation without a comparison of two limits. Along any one indexed line, fix all spins off that line's *one directional species*. Each incident plaquette contains just one link increment of this line. The conditional Boltzmann weights are thus products of translated one-link densities in the successive increments, with tilt at most \(6\beta\). In an interval with the endpoint spins fixed, their only further constraint is the product joining its endpoints. Integrating a margin of \(k\) increments gives a group transition density between \(1-\eta(k/(1+6\beta))\) and \(1+\eta(k/(1+6\beta))\), by (3)'s single-path estimate. Put such a margin on both sides of a fixed inner interval and send \(k\) to infinity. Uniformly in both endpoints the law inside converges to Haar for its initial spin and independent tilted increments thereafter. This proves uniqueness of the conditional infinite-line law for every exterior background. The endpoint estimate applies under disintegration of any infinite-volume spin Gibbs measure by the finite-interval Gibbs rule.

**PROVED.** It follows that a spin Gibbs measure maps under \(v\mapsto U\) to a Wilson Gibbs measure. Indeed a fine increment given all other increments on its line and all off-line spins has the Wilson single-link density, depending only on its six staples. The staples are functions of the other Wilson links, so taking conditional expectations gives that same law given all other Wilson links. To pass to any finite link set, fix its exterior. Each single-link update has a positive lower density against Haar bounded below by \(e^{-12\beta}\). A sweep over the set therefore minorizes product Haar by \(e^{-12\beta |D|}\). Two laws invariant under that sweep must agree by total variation contraction. Both the conditional law just obtained and the finite Wilson Gibbs kernel are invariant, proving the finite-set assertion.

**PROVED.** Conversely lift a Wilson Gibbs state on \(\mathbb Z^4\) by choosing one independent left Haar frame on every directional line and taking ordered products of the given increments. Re-rooting any finite number of lines, even at origins chosen in advance far from a test, preserves the conditional frame law given the increments. Given the other increments, any finite stretch on one line has the product of the Wilson single-link laws since its links share no plaquette. Take the frame at the left endpoint, independent Haar, and condition on both endpoint spins. The spin conditional density inside is exactly the product of the incident plaquette weights against site Haar. Conditioning on outside spins fixes these endpoints and the other increments, with no further information about the intermediate spins. In particular this gives the single-spin Gibbs kernel. A finite sweep again minorizes product Haar, since a fixed spin occurs in finitely many bounded plaquette terms. This proves the finite-set Gibbs rule. In any spin Gibbs state the line calculation above gives a Haar base spin independent of its entire increment sequence and of all the other spin lines. For the whole sequence this follows first on each finite window by re-rooting, then by the cylinder sigma-field. The base spins are jointly independent given all increments by successive conditioning on finitely many lines. Hence this lift is unique. Translation of the chosen origins has no effect on the law.

**PROVED.** In particular a local observable invariant under the independent left rotations on every line depends only on Wilson links in its enclosing rectangular box. On each line through its support, use the left rotation to set the first used spin to the identity and express later ones by ordered products in the box. Invariance under the further right rotation \(v_\mu(x)\mapsto v_\mu(x)g(x)\) gives the usual vertex gauge invariance of those increments. Conversely every local gauge-invariant Wilson observable lifts to this invariant spin algebra. This identifies the local observables at fixed cutoff. The required continuum limit and its spectral edge still require estimates on their correlations.

## A flat diagonal slice in the isotropic Wilson integral

**PROVED.** There is a choice of the segment origins in (4) for which complete three-dimensional layers of the site variables are fixed. On a four-torus of side \(N\) divisible by \(h\in8\mathbb N\), start a segment on each coordinate line whenever \(l(x)=\sum_\nu x_\nu=0\bmod h\). The coloring proof of (4) is independent of the origins. Set every prescribed transport to the identity. On each segment use independent partial products as its interior \(v_\mu\)'s, fixing both endpoint values to one. Successive Haar translations give product Haar reference on all free spins. Formula (5) holds across segment ends as well. All four spins are now one at *every* site of every selected layer. One may let the spacing \(ah\) of these layers tend to zero under (4)'s hypotheses while retaining the full thermal defect to \(o(1)\).

**PROVED.** Despite this prescription, a plaquette from \(l=s-1\) to \(l=s+1\) across a pinned layer \(l=s\) has action observable
\[
      \tfrac12\operatorname{tr}\!\left[
             R_{\mu\nu}(x)^{-1}R_{\mu\nu}(x+\hat\mu+\hat\nu)^{-1}
                                \right].                               \tag{6}
\]
Here \(s=0\bmod h\) and the levels can be read modulo \(N\). The two intermediate corners are fixed. The two outer corners still interact. This calculation is the reason that imposing all the spin values on these layers has a small normalization cost without cutting time propagation.

**PROVED.** One can remove the two-sided dependence of one quarter of the factors (6) on *every* pinned layer, still changing the full Wilson partition function by a relative \(o(1)\) in (4)'s scaling. Give a lower-layer site \(x\) the color \(\sum_{\mu=0}^3\mu x_\mu\bmod4\). From every color-zero lower site prescribe its four outgoing Wilson links to equal one. Each middle site \(y\) has exactly one chosen predecessor, since the colors of \(y-\hat\mu\) range over all four values. These links form disjoint stars. Stars at different pinned layers are disjoint. Call their union \(A\). In ordinary Wilson theory the joint law on a forest is exactly product Haar, independent of any gauge-invariant measurement. In fact averaging the independent vertex gauges takes the edge labels on a tree to product Haar, starting from any labels, while preserving that measurement. This is the usual gauge-tree integration.

**PROVED.** Each long segment meets \(A\) in at most its terminal link. Thus the conditional density of its full transport array given \(U_A\) lies between \(1-\delta_1\) and \(1+\delta_1\), uniformly in the star values. The normalization after *both* prescriptions has the same bounds relative to \(Z\). Under the Haar reference the long-product and star arrays have independent product Haar laws, by integrating a private link per segment. For a gauge-invariant bounded local measurement \(F\) meeting each segment in at most \(r\) links, apply the same argument while exposing its links in addition to \(A\). Use \(\mu(F\mid U_A)=\mu F\) and the analogous identity for \(|F|\). The relative error bound in the first part of (4) now uses \(\delta_{r+1}\). For continuous measurements these comparisons hold at the specified identity values by continuity of the integrals, or directly by the tree gauge integration. On the lower side the terminal link is \(v_\mu(x)^{-1}\). Thus every selected lower site has all four spins fixed. Its six crossing plaquettes each contribute only a function of their upper site. Four outgoing links per selected star and one incoming selected link per middle site show the selected lower sites form exactly one quarter of that layer.

**PROVED.** A counting obstruction holds for any additional forest \(A\) of nearest-neighbour bonds from either outer layer to one pinned middle layer of \(P=N^3\) sites. Let \(k_x\le4\) be the number of those bonds at outer site \(x\). Up to \(\binom{k_x}{2}\) displayed plaquette factors lose dependence on that site. Both corresponding spin variables must be fixed there, since a free one still ranges over the whole group. For a nonempty forest,
\[
 \sum_{x\ {\rm outer}}(k_x-1)_+
    = \#\{\text{incident middle vertices}\}-\#\{\text{nonempty components}\}
    \le P-1 .
\]
This is the edge count of a forest after subtracting its incident outer vertices. As \(\binom{k}{2}\le2(k-1)_+\) for \(k\le4\), at most \(2(P-1)\) of the \(6P\) crossing factors become single-sided in this way. That leaves at least \(4P+2\) direct two-site factors. This counts factors in (6) before further integrations.

**PROVED.** Prescribing *all* lower-layer outgoing bonds would eliminate every crossing interaction, but has a checkable cost in local measurements. The successive steps \(+\hat0,-\hat1,+\hat2,-\hat0,+\hat1,-\hat2\), starting in the lower layer, form a simple six-link loop \(\gamma\) alternating between that layer and the middle one. Its holonomy would be one. In ordinary Wilson theory, expose all links except one of its edges. The fundamental Fourier multiplier estimate used in (3) gives \(\|\mathbb E[U_e\mid\mathrm{rest}]\|_{\rm op}\le e^{-1/(1+6\beta)}\). The remaining path factors are fixed unitaries. Thus the mean scaled deficit is at least \(\beta(1-e^{-1/(1+6\beta)})\) at each finite coupling, and
\[
  \liminf_{\beta\to\infty}
  \mu\!\left[\beta\!\left(1-\tfrac12\operatorname{tr}U_\gamma\right)\right]
       \ \ge\ \tfrac16 .                                                \tag{7}
\]
The fully fixed lower layer sets this observable to zero. Long-segment and forest prescriptions preserve its expectation to the relative error above. This rules out extending their local-observable comparison to this complete cut. It concerns a microscopic reading and makes no assertion about the continuum spectral weight of that loop.

## How much boundary information must still be controlled

**OPEN.** The following is a single sufficient Wilson estimate on the original, unconstrained law. At each cutoff choose an infinite-volume reflection-positive periodic Gibbs limit \(\nu_j\). Use the four offsets in (3). Choose \(a_jb_j\to\ell>0\), \(b_j=4h_j\), and \(k_j\to\infty\) with \(\log k_j=o(h_j/(1+6\beta_j))\) and \(h_j/(1+6\beta_j)\to\infty\). For a closed box \(D\) with corners on the \(h_j\)-grid write \(G_D=S_3\cap E(D)\), the common segments contained in the box. Seek \(C\ge1\), independent of \(j\), such that on every such box of side at most \(16k_jb_j\),
\[
   \|f-P_{G_D}f\|_2^2
    \ \le\ C\sum_{i=1}^3\|f-P_{W_i}f\|_2^2 .                          \tag{8}
\]
Here \(f\) is any square-integrable gauge-invariant function supported at least \(b_j+2\) inside \(D\). All norms and conditional expectations use \(\nu_j\). The left side retains precisely the common graph. Thus the common contractible loop that defeated three updates is allowed on the left. The estimate asks whether a function well predicted separately by all three walls is already well predicted by their common links.

**PROVED (conditional implication).** Equation (8) yields a positive physical gap under the following matching hypotheses. For each member of a family spanning a dense centered Osterwalder–Schrader space of a continuum theory, suppose its local reflected correlations are limits of those of positive-time Wilson insertions \(F_j\) in boxes of bounded physical side, and \(\log^+\|F_j\|_{L^2(\nu_j)}=o(k_j)\). These hypotheses concern the same selected states \(\nu_j\). For polynomially bounded insertion norms and logarithmic bare coupling one may take \(k_j=\lceil (\log(1/a_j))^2\rceil\) if (8) holds at those sizes. The conclusion is a gap of at least
\[
                  {-\,\log q\over4\ell},\qquad
                 q=\sqrt{1-\frac{1}{20C}} .                            \tag{9}
\]

**PROVED.** First, (3) applies to the finite graph \(G_D\) and the entire fourth wall in \(\nu_j\). The finite set of selected private links has the Wilson conditional law by the finite-set Gibbs rule. The segment count is at most \(4(16k_j b_j/h_j+1)^4\), so the norm bound on centered invariant functions is at most \(1/2\) for all sufficiently large \(j\). If \(P,Q\) are two orthogonal projections with \(\|QP\|\le1/2\) on this space, then \(\|P+Q\|\le3/2\). Indeed the row operator from \(\operatorname{ran}P\oplus\operatorname{ran}Q\) given by \((u,v)\mapsto u+v\) has squared norm at most \(3/2\), by \(|\langle u,v\rangle|\le\|u\|\|v\|/2\). Its product with its adjoint is \(P+Q\). Apply this to \(P_{G_D},P_{W_4}\). Together with (8) it gives \(\sum_{i=1}^4d_{W_i}(f)\ge\|f\|^2/(2C)\) for centered \(f\) in the stated boxes.

**PROVED.** Write \(K=P_{W_4}P_{W_3}P_{W_2}P_{W_1}\). Put \(f_0=f,\ f_i=P_{W_i}f_{i-1}\), \(r_i=f_{i-1}-f_i\). Then \(\sum_i\|r_i\|^2=\|f\|^2-\|Kf\|^2\). Since \(f_i\) belongs to the \(i\)-th range, \(d_{W_i}(f)\le(\sum_{p\le i}\|r_p\|)^2\). Summing and using Cauchy–Schwarz costs at most \(1+2+3+4=10\) times \(\sum_i\|r_i\|^2\). This gives \(\|Kf\|\le q\|f\|\).

**PROVED.** One application of \(P_{W_i}\) grows the support in each coordinate direction by at most \(b_j+2\) on either side. Only the closed cells touching the support enter its conditional integral. Disjoint finite sets of private cells are conditionally independent given the wall. This follows even in \(\nu_j\) by the finite-set Gibbs rule, since their conditional kernels depend only on the wall. Consequently \(\langle f,g\rangle=\langle P_{W_i}f,g\rangle\) if the two supports are at distance greater than \(b_j+2\) in the maximum norm. During \(k_j\) sweeps the support width grows by at most \(8k_j(b_j+2)\). A box with the required margin and \(h_j\)-aligned ends then fits inside the side bound in (8), since the original support has width \(O_F(b_j)\). For the reflected centered autocorrelation at a lattice time \(t_j=4k_j(b_j+2)+O_F(b_j)\), choose the last term large enough that the other insertion stays outside the enlarged cells throughout. Iteration leaves a correlation of \(K^{k_j}f\) with that other insertion. Cauchy–Schwarz bounds its absolute value by \(q^{k_j}\|F_j\|_2^2\).

**PROVED.** For the Wilson physical transfer in the chosen reflection-positive state, the centered reflected time correlation has the form \(C_j(n)=\int_{[0,1]}\lambda^n\,d\sigma_j(\lambda)\) with \(\sigma_j\) positive. This is the spectral theorem on the reconstructed lattice space. For \(n_0<n<n_*\), Hölder bounds \(C_j(n)\) by \(C_j(n_0)^{1-\theta}C_j(n_*)^\theta\), \(\theta=(n-n_0)/(n_*-n_0)\). Take \(n_*=t_j\) and \(a_jn_0\to s_0,\ a_jn\to s>s_0>0\). Since \(a_jt_j/k_j\to4\ell\), the large-time bound and the assumed norm growth imply
\[
                 C(s)\le C(s_0)\exp[(s-s_0)\log q/(4\ell)] .
\]
If \(C(s_0)=0\), monotonicity gives the same conclusion. Positive spectral weight below the rate (9) would violate this inequality at large \(s\), by restricting the Laplace integral to an interval strictly below that rate. The corresponding spectral projection vanishes on the dense centered span and therefore on the whole vacuum orthocomplement. This proves the implication, including exclusion of additional zero-energy vectors in that representation. It supplies neither (8) nor the matching hypotheses. The use of local resampling followed by physical-time decay builds on the cube-dynamics argument of Bhattacharjee, Bhattacharya, Lockwood and Romanov; the finite propagation here is for the four deterministic wall updates. [Their Theorem 66](https://hexagonmath.org/2610.00341v7)

## Comparing complete conditional fields at different graph values

**PROVED.** On the finite graph \(G_D\) of (8), one can compare the laws of *all* remaining links, including the links incident to the graph. Let \(M\ge1\) now be its actual number of segments of length \(h\). Fix the graph links. By a vertex gauge that is the identity at segment endpoints, arrange that each fine link on segment \(\gamma\) equals \(e^{X_\gamma/h}\), where \(e^{X_\gamma}\) is the original oriented segment transport and \(\|X_\gamma\|_{\rm op}\le\pi\). This is possible by successively choosing the gauges at the degree-two interior vertices. Use a fixed choice of logarithm at \(-1\). The same deterministic gauge changes off-graph variables by coordinatewise Haar translations and preserves each wall sigma-field. Write \(\pi_t\) for the conditional law of the off-graph variables at graph values \(e^{tX_\gamma/h}\), \(t\in\mathbb R\), all in the common off-graph coordinates after this choice. In particular \(\pi_0\) fixes just the graph to the identity.

**PROVED.** Let \(\delta\) be the error in (3) for these \(M\) segments, and \(A=24\pi^2\beta M/h\). For \(\delta\le1/2\) and all real \(p\ge1\), the likelihood ratio \(L=d\pi_1/d\pi_0\) satisfies
\[
 \log\mathbb E_{\pi_0} L^p\le \tfrac12 A p(p-1)+4p\delta,\qquad
 \log\mathbb E_{\pi_1} L^{-p}\le \tfrac12 A p(p-1)+4p\delta .           \tag{10}
\]
For the proof, write \(S_t\) for the sum of the action exponents on the plaquettes incident to the fixed graph. The law on the other links has form \(e^{S_t}dQ/Z_t\) with the same \(Q\) for every \(t\). This also holds in a chosen infinite-volume Gibbs state. Its finite-graph conditional Gibbs density given the other links is \(e^{S_t}\) divided by the integral of the exponent over all raw graph links. Absorb that denominator into the off-graph marginal to define \(Q\). Then \(Z_t\) is the density of the raw graph values against product Haar. The raw density is continuous and invariant under every interior vertex gauge, by gauge invariance of the state. Its value is therefore the density of the ordered segment products: under product Haar, the internal tree coordinates integrate to one at fixed products. Hence \(1-\delta\le Z_t\le1+\delta\) for every \(t\), including \(t\) outside \([0,1]\).

**PROVED.** A plaquette with \(m\) graph links has second derivative of its normalized trace bounded by \(m^2\pi^2/h^2\). Differentiate its ordered product twice. Each exponential and every intervening matrix is unitary, and each differentiation costs at most \(\pi/h\). Since \(m^2\le4m\) and each graph edge has six incident plaquettes, \(|S_t''|\le A\) pointwise. The linear interpolation remainder gives \(pS_1+(1-p)S_0\le S_p+A p(p-1)/2\). Integrate against \(Q\) and divide by the normalizers. The bound \(|\log Z_t|\le2\delta\) gives the first part of (10). The path \(t\mapsto1-t\) gives the other part.

**PROVED.** If \(0<A\le(\log2)/4\) and \(\delta\le(\log2)/16\), the exceptional set where \(L\notin[1/2,2]\) has probability at most
\[
                 \epsilon=4\exp[-(\log2)^2/(4A)]                       \tag{11}
\]
under *both* laws. Set \(p=(\log2)/(2A)\ge2\) in (10). The two positive terms there sum to at most \(p\log2/2\). On \(L>2\), the \(\pi_0\) bound follows by Markov's inequality, and the \(\pi_1\) bound by \(L\le L^p/2^{p-1}\) on that event. Reverse the densities on \(L<1/2\). At \(\beta=0\) the laws coincide exactly. In the boxes of (8), with \(a b\to\ell>0,\ k=\lceil\log^2(1/a)\rceil,\ \beta=O(\log(1/a))\), (11) is smaller than \(e^{-c k}\) for every fixed \(c>0\), eventually. This controls the effect of prescribing even atypical common holonomies on the complete remaining field after the stated coordinate change.

**PROVED (one sufficient estimate at the identity).** For bounded \(F\) of the off-graph coordinates, write \(d^\pi_{\mathcal A}(F)=\inf_H\pi|F-H|^2\) over \(\mathcal A\)-measurable \(H\). The infimum is attained by a function bounded by \(\|F\|_\infty\). For every such sigma-field, (11) gives
\[
   d^{\pi_1}_{\mathcal A}(F)\le2d^{\pi_0}_{\mathcal A}(F)
                                  +4\epsilon\|F\|_\infty^2              \tag{12}
\]
and its reverse with the measures interchanged. Use the minimizing \(H\) under the other law, split at the exceptional set, and apply (11). The trivial sigma-field gives the same comparison for the variance. Suppose the following holds in every box of (8), for all bounded off-graph functions \(F\) supported with the indicated margin:
\[
          \operatorname{Var}_{\pi_0}(F)
                \le C_0\sum_{i=1}^3 d^{\pi_0}_{W_i\setminus G_D}(F).
                                                                         \tag{13}
\]
Here (13) is imposed on all such functions. The deterministic gauge used to compare different fibres can change which functions are invariant under the stabilizer of the fixed field. Restricting (13) solely to invariants of the identity fibre would require another argument.

**PROVED.** Apply (12) to the variance and then to the three terms on the right of (13). In each fibre the price is \(4C_0\) in front of the sum, plus at most \((4+24C_0)\epsilon\|F\|_\infty^2\). Undo the deterministic gauge. Integrating the result over the common graph gives (8) with those same two terms, since \(G_D\subset W_i\) for \(i\le3\). Thus (13) at this *one* graph value suffices for the continuum conclusion of (9) on polynomially bounded matched insertions, with a possibly smaller positive rate. In detail take \(C=\max(1,4C_0)\) in the argument for (9). The sweep estimate now reads \(\|Kf\|^2\le q^2\|f\|^2+c_0\epsilon\|f\|_\infty^2\) for a constant depending only on \(C_0\). Conditional expectation contracts the supremum norm, so after \(k_j\) sweeps the extra term in the *squared* norm is at most \(c_0\epsilon\|f\|_\infty^2/(1-q^2)\). With \(k_j=\lceil\log^2(1/a_j)\rceil\) and polynomial \(\|F_j\|_\infty\), its square root times \(\|F_j\|_2\) is negligible compared with \(q^{k_j}\). The same Hölder argument proves the positive bound on the physical spectrum. This uses (13) as a hypothesis, not as a consequence of the high-probability comparison.

## Testing the estimate on one fixed fibre

**PROVED (local Wilson words need less).** Suppose the matched insertions are sums of bounded *gauge-invariant* continuous local words as in (4), with polynomial coefficient sum, fixed \(r\), and supports of bounded physical diameter. In this case it suffices to establish (13) on restrictions of gauge-invariant Wilson functions to the identity graph. One can run the three updates in the pinned model before returning to the original state. This avoids comparing symmetry sectors between different fibres.

**PROVED.** Given \(F_j\), its reflection and a distant translate, choose one \(h_j\)-aligned box \(D\) containing their supports and the cells reached from the first support by \(3k_j\) updates, with margin \(b_j+2\). Take \(t_j=3k_j(b_j+2)+O_F(b_j)\), choosing the last term as in (9). A box of side at most \(16k_jb_j\) suffices. The raw-graph conditional value at the identity agrees, for every gauge-invariant insertion, with the conditional value at identity *segment products*. This follows by averaging the interior vertex gauges at fixed products, as in (10). The proof of (4) applies in \(\nu_j\) on this finite graph using the finite-set Gibbs rule. Consequently the connected correlation of the two words differs in \(\nu_j\) and \(\pi_0\) by \(O(B_j^2\delta_{2r})\), uniform over their positions. The bound applies term by term and to both means. It is smaller than \(e^{-c k_j}\) for every fixed \(c\) with the logarithmic choices following (11).

**PROVED.** Each of the first three walls contains every pinned link. In \(\pi_0\), the private-cell conditional integral is the same local function of the wall as in the original law, evaluated at its fixed graph values. One sees this by integrating the Wilson plaquette factors in the finitely many relevant cells. For continuous cylinder functions this integral gives a continuous version at the identity. Thus successive projections preserve restrictions of gauge-invariant functions. Center the two functions separately under \(\pi_0\), whose selected graph is confined to \(D\). With three projections the telescoping constant is \(1+2+3=6\). If (13) holds in this restricted class, the pinned connected correlation is at most \(q_3^{k_j}(2B_j)^2\), \(q_3=\sqrt{1-1/(6C_0)}\), enlarging \(C_0\) to one if necessary. Private cells supporting the two functions stay disjoint throughout. Return to \(\nu_j\) with the preceding error bound and use its positive transfer and Hölder as in (9). This gives a gap of at least \(-\log(q_3)/(3\ell)\) under the stated matching and totality conditions. The pinned measure itself need not define the continuum vacuum.

**PROVED (a finite bound for (13)).** At fixed cutoff let \(B\) be the free links of the closed support box after the graph is set to one. Write \(m_B\) for the number of fine plaquettes meeting \(B\). Given the other links, their joint law has density in \([e^{-2\beta m_B},e^{2\beta m_B}]\) against product Haar on \(B\). Under product Haar the three conditional projections onto the links of \(W_i\) in \(B\) commute. Their intersection is empty, so the sum of the three squared residuals dominates the Haar variance. For each \(i\), reveal the entire exterior of \(B\) in addition to \(W_i\). This can only decrease the residual in (13). At each fixed exterior, its variational formula and the pointwise lower bound on the density give at least \(e^{-2\beta m_B}\) times that Haar residual. The pinned variance is at most \(e^{2\beta m_B}\) times the Haar variance, by testing its variational formula with the Haar mean. This proves (13) with \(C_0=e^{4\beta m_B}\). The elementary finite-energy comparison also appears for ordinary local cube functions in the four authors' v7 discussion at lines 7357–7369. Here \(m_B\) grows with the fine volume of the support. The bound obtained in this way gives no positive rate in physical units.

**PROVED (which local gauge charges can cause a loss).** Consider the identity fibre and a function with the support margin in (8). Every support vertex that belongs to all three wall complexes also belongs to \(G_D\). Indeed three distinct transverse residues must occur among the four coordinates of the vertex. One can move in a remaining direction while retaining all three residues. This gives an incident common segment in the padded box. Thus at every support vertex off \(G_D\) some wall contains no incident edge. The independent vertex gauge there preserves the pinned measure and each of the three conditional-expectation ranges. A vector of nontrivial gauge type at that vertex is killed by projection to the wall with no incident edge, since the entire range is invariant under that vertex transformation. Decompose under the compact product of gauge groups at the finitely many off-graph support vertices. Each component with any such charge pays at least its squared norm in the sum in (13), and the components remain orthogonal under the projections. This proves a constant-one bound on their direct sum at every finite \(\beta\). The interacting sector still includes all gauge-invariant local Wilson words.

**PROVED (a comparison testing the geometric argument).** On a four-dimensional fine box of side \(R=kb\), use three independent centered real Gaussian fields with precision the nearest-neighbour Dirichlet Laplacian. Set the boundary to zero and also pin the vertices of the common segment graph to zero. Observe the vertices of each full wall. There are absolute \(c,C>0\) such that for \(k,b\) sufficiently large a centered rotation-invariant scalar \(F\), supported in the middle half, obeys
\[
       \frac{\sum_{i=1}^3\mathbb E\operatorname{Var}(F\mid W_i)}
            {\operatorname{Var} F}
                    \ \le\ C(k^{-2}+b^{-1}).                           \tag{14}
\]
This is a free-field comparison with the same wall geometry.

**PROVED.** For one component let \(L\) sum its field on the free sites of the middle half. A tent supported there, equal to one on the middle quarter and with neighbour differences at most \(C/R\), has energy at most \(C R^2\). Set it to zero on the common graph as well. At most \(C R^4/b^3\) sites are lost: there are \(O((R/b)^3)\) occupied coordinate lines per direction and \(O(R)\) sites per line. The new energy is at most \(C(R^2+R^4/b^3)\) and its sum is at least \(cR^4\). The quadratic-form Cauchy–Schwarz inequality for the inverse Dirichlet Laplacian gives
\(v=\operatorname{Var}L\ge cR^8/(R^2+R^4/b^3)\). Given any one wall, the fluctuation field has zero boundary on cells of width at most \(b\), including cells cut by the outer boundary. On each coordinate line telescope to a zero endpoint and apply Cauchy–Schwarz. Summing yields \(\sum u^2\le b^2\sum_{\rm bonds}|\nabla u|^2\). The conditional covariance is therefore at most \(b^2 I\), and \(v_i=\mathbb E\operatorname{Var}(L\mid W_i)\le C b^2R^4\). This variance is deterministic for a Gaussian conditional law. For \(F=\sum_{\alpha=1}^3 (L_\alpha^2-v)\), Wick's formula gives variance \(6v^2\) and residual fraction \(2v_i/v-(v_i/v)^2\) on wall \(i\). The latter also follows by writing \(L_\alpha\) as its conditional mean plus an independent Gaussian of variance \(v_i\). These inequalities give (14). If bounded tests are required, truncate \(F\) and use \(L^2\) convergence and the contraction of each projection. When \(k\) grows and \(b\to\infty\), the geometry, identity graph and scalar rotation symmetry permit arbitrarily small relative losses. A uniform Wilson estimate must control the interacting long-wavelength fluctuations.

## Testing an actual gauge-field mechanism for near equality

**PROVED (linear gauge theory).** In the same boxes there is also a gauge-invariant obstruction with an explicit predictor on each wall. Use the noncompact Abelian potential, zero tangential boundary data, and fine edge potential zero on \(G_D\). Give its curvature \(dA\) the centered standard Gaussian on the image of these potentials under the lattice curl \(d\). Equivalently the action is \(\frac12\|dA\|^2\) on the potentials modulo the kernel of \(d\). Three independent copies allow a rotation-invariant observable. Take \(R=kb\), \(k\to\infty,\ k^2/b\to0\). There is a linear curvature reading \(L\), supported in the middle half, which has relative mean-square prediction error \(O(k^{-2})\) from the oriented boundaries of the \(b\)-by-\(b\) tiles of *each* of the three walls.

**PROVED.** Choose one direction of a trial potential \(A^0\) to be \(R\varphi(x/R)\), with the other components zero. Here \(\varphi\) is a fixed smooth function supported inside the middle half whose derivative in a transverse direction has magnitude bounded below on a subbox. Put \(\omega=dA^0\). Difference quotients give \(\|\omega\|_\infty\le C,\ |\nabla\omega|\le C/R,\ cR^4\le\|\omega\|^2\le CR^4\) for large \(R\). For the lower bound use the subbox on which the derivative has one sign and magnitude bounded below. Set \(A^0\) to zero on the graph edges to obtain an admissible \(A^1\). At most \(C R^4/b^3\) edges change, by at most \(CR\) each, and each occurs in six plaquettes. Hence \(\|dA^1-\omega\|^2\le CR^6/b^3=o(R^4)\). For \(L=\langle\omega,dA\rangle\), the variance is the squared norm of the orthogonal projection of \(\omega\) onto the allowed curl image. Testing against \(dA^1\) gives variance at least \(c'R^4\).

**PROVED.** For offset \(s_i\) and each orientation \(\mu\nu\), tile every \(\mu\nu\)-plane by the \(b\)-squares at that offset, at *every* transverse coordinate. Replace \(\omega\) on each tile by its average to obtain \(\omega_i\). Tiles meeting the support lie inside the box for large \(k\). The derivative bound gives \(\|\omega_i-\omega\|^2\le C R^4(b/R)^2\). Each tile sum of \(dA\) is exactly the circulation along its four sides, by cancellation of oppositely oriented interior edges. All those sides lie on \(W_i\). Therefore \(L_i=\langle\omega_i,dA\rangle\) is a gauge-invariant wall predictor and \(\mathbb E|L-L_i|^2\le\|\omega_i-\omega\|^2\), since the covariance on curvature is a projection. No choice of gauge for individual potentials enters this prediction. The centered scalar \(F=\sum_{\alpha=1}^3(L_\alpha^2-\mathbb E L_\alpha^2)\) has the same \(O(k^{-2})\) relative loss: condition first on all the linear tile fluxes, use the Gaussian residual formula from (14), and then allow the full wall information. This provides a specific way gauge-invariant long-wavelength fluctuations could defeat the three-wall estimate.

**PROVED (what the bare Wilson tile boundaries predict).** Return to the compact \(SU(2)\) Wilson state at logarithmic \(\beta_j\), with \(b_j=4h_j\asymp a_j^{-1}\), \(h_j\in8\mathbb N\) and \(k_j=\lceil\log^2(1/a_j)\rceil\). In a box of side \(O(k_j b_j)\), let \(Y\) contain the \(h_j\)-step segment transports needed by all the square tile boundaries just used, at all transverse sites, for all three offsets and all six orientations. Include the common graph segments also. Partition each coordinate line at multiples of \(h_j\); repeated uses of one segment refer to the same matrix. The number of *distinct* segments is \(O((k_jb_j)^4/h_j)\). For \(O_j=\sum_\alpha c_{\alpha j}f_{\alpha j}\) as in (4), with coefficient sum \(B_j\) and at most \(r\) fine links per term on each segment,
\[
   \big\|\mathbb E_{\nu_j}[O_j\mid Y]-\nu_j O_j\big\|_\infty
          \le {2B_j\delta_r\over 1-\delta_r}.                           \tag{15}
\]
The error tends to zero faster than any power of \(a_j\) for polynomial \(B_j\) and bounded \(r\). The proof is precisely the uniform Bayes estimate (4) for each word. It applies to the finite segment array in the infinite-volume state by the finite-set Gibbs rule. It does not require translation of the transverse sites onto a sparse four-dimensional grid.

**PROVED.** The same estimate, with the error doubled, bounds the covariance in the *identity graph fibre* of \(O_j\) with any unit-\(L^2\), gauge-invariant function of the tile transports. First condition the array \(Y\) on its common-graph segment products being one. Their marginal has a continuous positive density. The bound in (15) holds for every array value, so its mean under this further conditioning is within the same error of \(\nu_j O_j\). The centered conditional mean is within twice the error. Cauchy–Schwarz gives the covariance estimate. For gauge-invariant readings, their products and squared norms, averaging interior vertex gauges identifies these integrals with the ones at the raw identity graph. This also applies to limits of continuous invariant readings in the relevant \(L^2\) space. In particular, for words with variance bounded below by a power of \(a_j\), this entire bare macro-rectangle measurement has vanishing relative predictive power. The Abelian additive circulation argument has no such predictor among these compact Wilson transports. The full walls also carry every *fine* tangential plaquette. Estimate (15) does not bound what those plaquettes can jointly predict.

## A singlet estimate in the identity fibre

**PROVED.** A class of fine-plaquette readings does satisfy (13) with a cutoff-independent constant, even when the number of readings grows. Fix a spatial plaquette \(p\) and use translates \(p_s=p+rs\hat0\) with integer spacing \(r\ge2\) inside the support box. Put \(X_s=\beta(1-\tfrac12\operatorname{tr}U_{p_s})\). For arbitrary complex coefficients and \(2u\) such plaquettes let
\[
            F=\sum_{m=0}^{u-1}z_m(X_{2m}-X_{2m+1}).
\]
On the logarithmic Wilson sequence above there is an absolute \(C_1\) such that, for all sufficiently fine cutoffs, uniformly in \(p,r,u,z\),
\[
       \operatorname{Var}_{\pi_0}F
              \le C_1 \sum_{i=1}^3 d^{\pi_0}_{W_i\setminus G_D}(F).
                                                                         \tag{16}
\]
Variance for complex readings means the mean squared absolute deviation. An individual \(X_s\) also satisfies the same assertion after enlarging \(C_1\).

**PROVED.** The one-link input comes from Bhattacharjee, Bhattacharya, Lockwood and Romanov, v7, proposition labelled \(\mathrm{prop:plaqvar}\), lines 18943–18969. Given all other links, the conditional variance of a normalized plaquette trace with a free edge is at least \(2^{-19}(1+6\beta)^{-2}\). The argument bounds both longitudinal and transverse variances of the tilted quaternion. It applies unchanged after fixing other graph links. The upper input comes from row 1155, (9): the marked-plaquette exponential moment on periodic Wilson tori gives \(\nu_j X_s^2\le C_2\) for an absolute \(C_2\), by passage to the periodic limit at fixed cutoff. Both inputs are hand estimates. [Primary one-link bound](https://hexagonmath.org/2610.00341v7) · [Row 1155, marked plaquettes](gap-solve7-astra62.md)

**PROVED.** The graph \(G_D\) has no elementary plaquette cycle, so mark a free edge of each \(p_s\) and assign it to one of the three walls that omits it. For each fixed wall reveal everything except its assigned marks. The time separation ensures that no action plaquette contains two such marks and no other measured plaquette reads a mark of \(p_s\). The conditional variances add, since the marked links are independent given everything else. This is a finer conditioning than revealing the wall. For coefficients \(c_s\) this gives
\[
       \sum_{i=1}^3 d^{\pi_0}_{W_i\setminus G_D}\Big(\sum_s c_sX_s\Big)
                    \ \ge\ 2^{-19}49^{-1}\sum_s|c_s|^2,\qquad \beta\ge1 .
\]

**PROVED.** In \(\nu_j\) the stationary centered covariance on this time column is \(\int t^{|s-s'|}\,d\sigma(t)\), where \(0\le t\le1\) is the \(r\)-step transfer eigenvalue and \(\sigma([0,1])=\operatorname{Var}_{\nu_j}X_0\le C_2\). This uses positivity of the Wilson time transfer and a spatial plaquette on the reflection slice. For \(t<1\), the Fourier series of \(t^{|s|}\) sums to \((1-t^2)/(1-2t\cos\theta+t^2)\). Multiplication by \(|1-e^{i\theta}|^2\) bounds that kernel by \(4(1-t)/(1+t)\le4\), since its maximum is at \(\cos\theta=-1\). The difference annihilates \(t=1\). Integrate against \(|\sum_m z_m e^{2im\theta}|^2\) and use character orthogonality to get \(\nu_j|F|^2\le4C_2\sum_m|z_m|^2\). Sussman and Alpoge's positive lattice transfer and torus trace identity are at outline 2315–2335, GL8. [Outline transfer index](sa-index/chunk-02.md)

**PROVED.** Each \(X_sX_{s'}\) meets a graph segment in at most eight links. Formula (4) and the raw-graph gauge averaging give
\[
 |\pi_0(X_sX_{s'})-\nu_j(X_sX_{s'})|
                    \le [2\delta_8/(1-\delta_8)] C_2 .
\]
The error for \(F\) is at most this bound times \(4u\sum_m|z_m|^2\), by Cauchy–Schwarz. Here \(u\le16k_j b_j\), so \(u\delta_8\to0\). This proves (16) using the private-edge lower bound. For a single reading, use the same second-moment comparison directly. This proves the desired variance loss for these fine, gauge-invariant observables along the stated sequence. The conditional expectation of such a difference on a wall is an integral over a four-dimensional cell and can depend on its entire fine boundary. The next sweep therefore requires (13) beyond this class.

## A criterion using only functions on a spatial slice

**PROVED.** There is a physical-transfer version which dispenses with proving a bound for the iterates of the wall updates. Take a finite periodic spatial cube of side \(N\), \(b=4h\mid N,\ h\in8\mathbb N\), and take its ordinary Wilson *vacuum* limit in the time direction first. Call this cylinder law \(\nu\). Use the spatial slices at \(t_0=3h,\ t_1=3h+2b\). Fix to one the raw links of the common graph \(G=S_3\) in the time slab \([-2b,5b]\) on that cylinder, including all complete segments in the slab. Write \(\pi\) for the resulting law. There are \(M\le C_3(N/h)^3\) segments for an absolute \(C_3\). No spatial edge of either observed slice belongs to \(G\): a spatial edge in all three walls would need the time coordinate to have one of the first three residues. Thus the two *whole* slices meet the segments in zero links, irrespective of the size or complexity of a slice function.

**PROVED.** Let \(\rho_\mu\) be the supremum of the absolute connected correlation between a gauge-invariant function of the first slice and a gauge-invariant function of the second, each normalized to unit variance in the law \(\mu\). Let \(m_{\rm lat}(N,\beta)\) be the lowest excited physical energy in lattice units on the spatial cube. For \(\delta=(1+\eta((h-2)/(1+6\beta)))^M-1<1\), where \(\eta(x)=\sum_{d\ge2}d^2e^{-(d-1)x}\), and \(\eta_0=2\delta/(1-\delta)\),
\[
       \left|e^{-2b m_{\rm lat}(N,\beta)}-\rho_\pi\right|
                                 \le 2\eta_0+\eta_0^2 .                 \tag{17}
\]
Indeed (3)'s conditional density argument compares the joint gauge-invariant slice law under \(\pi\) and under \(\nu\) by a likelihood ratio in \([(1+\eta_0)^{-1},1+\eta_0]\). Expose both full spatial slices before the private segment links; then condition the segment products to one. The interior gauge integration identifies this conditioning with the raw identity graph for invariant tests. The measure comparison applies to arbitrary measurable slice events in the invariant algebra by approximation or bounded monotone limits. For centered unit functions under \(\nu\), the joint moment changes by at most \(\eta_0\), each mean by at most \(\eta_0\), and each variance under \(\pi\) is at most \(1+\eta_0\). This bounds \(\rho_\nu\) by \((1+\eta_0)\rho_\pi+\eta_0+\eta_0^2\). Interchange the two laws to get the absolute error in (17). Finally in the vacuum cylinder the map \(f\mapsto f\psi\), with \(\psi\) the strictly positive transfer vacuum wave function, is unitary from gauge-invariant slice \(L^2(\psi^2 dU)\) onto the physical transfer space. Its two-slice form is the vacuum-normalized transfer to power \(2b\). The centered operator norm is exactly \(e^{-2b m_{\rm lat}}\). This uses the usual Wilson transfer construction also used in rows 1145 and 1161. [Row 1145](gap-solve2-astra62.md) · [Row 1161](gap-solve9-astra62.md)

**PROVED.** It now suffices on this cylinder to have one cutoff-independent \(c>0\) such that
\[
       \sum_{i=1}^3 d^\pi_{W_i\setminus G}(F)
                  \ge c\,\operatorname{Var}_\pi F
 \qquad\text{for each gauge-invariant }F\text{ on either spatial slice}. \tag{18}
\]
For centered functions on the two slices, conditional covariance given \(W_i\) is zero. The private cells meeting the two slices are disjoint and fixing a subset of \(W_i\) preserves their conditional product law. Thus their connected correlation equals the inner product of their two projected centered functions, for each \(i\). Average the three identities and apply Cauchy–Schwarz to the sum of inner products. Equation (18) bounds the result by \(1-c/3\) times the product of the standard deviations. This proves \(\rho_\pi\le1-c/3\). The conditional integral for a slice function uses only the bounding walls of cells intersecting that slice. The much larger space of general four-dimensional cylinder functions is absent from (18).

**PROVED (continuum implication).** Along \(a_jb_j\to\ell>0\) with \(\log(N_j/h_j)=o(h_j/(1+6\beta_j))\), \(h_j/(1+6\beta_j)\to\infty\), and \(a_jN_j\to\infty\), (17) makes \(\limsup_j\rho_{\pi_j}<1\) equivalent to a strictly positive lower limit of \(m_{\rm lat}(N_j,\beta_j)/a_j\). If (18) holds, that lower limit is at least \(-\log(1-c/3)/(2\ell)\) for \(0<c<3\). To use this on \(\mathbb R^4\) one needs a matching nontrivial continuum theory from these growing spatial cubes with time already in its vacuum limit. For each positive-time word subtract its vacuum mean, apply the finite-cube spectral bound between two positive time paddings, and pass to its matched correlations. The dense-span spectral argument after (9) then gives the continuum gap. This choice of limits and its matching assumption differ from taking infinite spatial volume at each fixed cutoff. The earlier implication from (8) treats the latter choice.

**PROVED (a check on spatial-slice tests in (18)).** Equation (16) also holds for differences along the spatial axis transverse to a spatial plaquette, all on one endpoint slice of (17), with \(r\ge2\) dividing \(N\) and \(2u\le N/r\). The private-edge lower bound is identical because the sampled plaquettes are separated by at least two fine units, also around the period. For the upper bound work first on a finite periodic cylinder and take transfer in that transverse spatial direction. For the real plaquette multiplier the trace in an eigenbasis pairs nonnegative weights \(|X_{vw}|^2\lambda_v^{N-s}\lambda_w^s\) with their reversed pairs. After factoring their total weight at zero separation, each unequal pair gives the kernel \((t^s+t^{N-s})/(1+t^N)\) with \(t=\min(\lambda_v,\lambda_w)/\max(\lambda_v,\lambda_w)\). Equal pairs give constants. On the subcircle sampled every \(r\) steps, replace \(t,N\) by \(t^r,N/r\). At the Fourier frequencies of a circle of length \(n\), the sum of the normalized kernel for \(s=0,\ldots,n-1\) equals \((1-t^n)/(1+t^n)\) times the Poisson kernel used for (16), for \(0\le t<1\). This follows by summing its two geometric series. Thus the paired differences obey the same \(4C_2\) variance bound, by discrete orthogonality. Take the original time period to infinity at fixed spatial size. The second moments remain bounded by the marked-plaquette estimate. The joint full-slice likelihood comparison in (17) transfers the upper variance bound to \(\pi\) directly. This proves (18) with a fixed positive constant for arbitrary such column differences and for single action plaquettes on either slice.

## Nonlinear functions of finitely many fine plaquettes

**PROVED.** On either endpoint slice of (17), (18) holds for every polynomial of degree at most \(d\) in \(n\) scaled plaquette deficits \(X_p=\beta(1-w_p)\), with a positive constant depending only on \(d,n\). Here \(d,n\) are fixed, the plaquettes can have any spatial orientations, and their link sets are at lattice distance at least three from each other. The coefficients can depend on the cutoff. This concerns the full isotropic Wilson law on the identity fibre along the stated weak-coupling sequence.

**PROVED.** Mark one free link \(e_p\) of each plaquette as in (16). Expose the complement of all marks. For each of the six faces \(q\) incident to \(e_p\), write \(w_q=x_p\cdot v_q\) with \(x_p=U_{e_p}\in S^3\) and \(v_q\) its unit target, using the same positive orientation of the marked edge. All targets depend only on the exposed links. The marks are independent under the conditional law, with tilt vectors \(H_p=\beta\sum_{q\ni e_p}v_q\). Fix \(K\) large enough, depending on \(n\), that with probability at least \(1/2\) all \(6n\) incident deficits satisfy \(\beta(1-w_q)\le K\). Such \(K\) exists by the marked-plaquette exponential moment, a union bound, and (4) for a single invariant face event under graph conditioning. This last comparison also follows by bounded approximation, since each such face has a free link. On that event
\[
      |v_q-v_p|\le2\sqrt{2K/\beta}\quad(q\ni e_p).
\]
The event defined just by these target inequalities is exposed and has probability at least \(1/2\). On it, for all sufficiently large \(\beta\), \(|H_p|\ge3\beta\) and the unit tilt direction lies within \(C\sqrt{K/\beta}\) of \(v_p\).

**PROVED.** Conditionally on this exposed event, the law of each \(X_p\) dominates \(c_K\) times Lebesgue measure on \([1,2]\), for a fixed \(c_K>0\). In that interval, \(x_p\) is within \(2/\sqrt\beta\) of \(v_p\). The exponent \(x_p\cdot H_p\) is at least \(|H_p|-C(1+K)\). The integral of \(e^{x\cdot H_p}\) against Haar is at most \(C e^{|H_p|}(1+|H_p|)^{-3/2}\), by integrating \(e^{-|H_p|t}\sqrt{t(2-t)}\) for \(0\le t\le2\). The Haar density of \(\beta(1-x\cdot v_p)\) on \([1,2]\) is \((2/\pi)\beta^{-1}\sqrt{(X/\beta)(2-X/\beta)}\ge c\beta^{-3/2}\) for \(\beta\ge2\). Multiplication gives the assertion, uniformly in the background on that event. The conditional joint law therefore dominates \(c_K^n\) times the uniform law on \([1,2]^n\).

**PROVED.** Assign each mark to one wall omitting it. For each wall, further reveal everything except its assigned marks. At fixed common exterior the independent marks form three independent groups. The sum of the conditional variances for resampling these groups dominates the variance for resampling all of them, by the commuting projection argument of (1). For a polynomial \(P(X)\) the sum on the left of (18) is consequently at least
\[
             \tfrac12 c_K^n\operatorname{Var}_{[1,2]^n} P .
\]
Indeed variance is an infimum over constants, so the joint density lower bound applies to it. In the other direction subtract the mean of \(P\) on \([1,2]^n\). The Euclidean norm of the coefficients of the resulting polynomial is bounded by a constant depending on \(d,n\) times its \(L^2\) norm on that cube. The Gram form of monomials is positive definite, because a polynomial vanishing on an open box vanishes identically; minimize the continuous form on the unit coefficient sphere. All moments through order \(2d\) of the scaled deficits are uniformly bounded in \(\pi\), by (4) and the marked moment for one face, followed by Hölder for products. Expanding the centered polynomial and using Cauchy–Schwarz now bounds \(\operatorname{Var}_{\pi}P\) by \(C_{d,n}\operatorname{Var}_{[1,2]^n}P\). This proves the stated result.

**OPEN.** This last proof uses a joint lower density on a cube of \(n\) readings. Its constant depends on \(n\), both through \(K\) and through \(c_K^n\). The physical transfer norm in (17) takes a supremum over arbitrary functions of a spatial slice, including functions of a number of fine links growing with the cutoff. Even restricting to energy readings would still require controlling their collective fluctuations. The sparse tile estimate (15) and the column and finite-polynomial bounds control different subsets of that supremum.

## Collective plaquette fluctuations on the spatial cube

**PROVED.** Inequality (18) also holds with an absolute positive constant for the following sums over a three-dimensional array, with arbitrary coefficients and a number of terms of order \(N^3\). Fix one elementary spatial plaquette on the endpoint slice and use \(X=\beta(1-w_p)\). Let \(\tau_\alpha\) translate by one fine unit in spatial direction \(\alpha\). Take \(r\ge4\), \(n=N/r\) even, and put
\[
 F_z=\sum_{m\in(\mathbb Z/(n/2))^3} z_m
             \prod_{\alpha=1}^3
             \tau_\alpha^{2r m_\alpha}(1-\tau_\alpha^r)X .
                                                                         \tag{19}
\]
Each coefficient weights the alternating sum of eight sampled action densities. No restriction on their number or on the phases of the coefficients is needed. The free-edge lower bound is the one used in (16) and for one alternating column in row 1204, equation (9). The upper bound requires the reflection estimate in all three spatial directions, including the two directions in the plaquette. [Earlier alternating column](gap-solve21-astra62.md)

**PROVED.** Work first on a four-dimensional periodic cylinder of finite time period. Use any one spatial direction as the transfer direction and denote its Wilson transfer by \(T\). Let \(G_l\), \(0\le l<n\), belong to the complex span of real plaquette readings in the same transverse slice if they have extent \(s=0\) in this direction, or in the same unit slab if they have extent \(s=1\). Each real reading is unchanged by reflection in the middle of that slice or slab. Translation in the chosen direction is \(\tau\). Then
\[
 \left\|\sum_{l=0}^{n-1}\tau^{rl}(1-\tau^r)G_l\right\|_2^2
                         \le 20\sum_{l=0}^{n-1}\|G_l\|_2^2 .             \tag{20}
\]
To prove this, take a finite real spanning list of the readings. Write \(K_l\) for its matrix of two-point moments at displacement \(rl\). \(K_0\) gives its ordinary \(L^2\) form. For \(1\le l<n\) there is a positive matrix-valued measure \(M\) on \([0,1]\) such that
\[
      K_l=\int_{[0,1]}(t^{l-1}+t^{n-l-1})\,dM(t),\qquad
      \int dM\ \le K_1\ \le K_0 .
\]
Indeed use the transfer with half the spatial action on either side of the electric kernel. A real insertion has a real symmetric matrix \(A\) in a real eigenbasis of \(T\). For \(s=0\) it is multiplication by the reading. For \(s=1\) insert the reading in the one-step kernel and integrate the links across that step. Reflection interchanges its arguments and preserves the integrand after the change of bond orientations. The trace for two insertions has powers \(T^{rl-s}\) and \(T^{N-rl-s}\) between them. Pair an eigenvalue pair \(\lambda_a\ge\lambda_b\) with its reverse. Its contribution to \(M\) is the positive outer product of the vector of the entries \(A_{ab}\) for the real list, multiplied by \(\lambda_a^{N-r-s}\lambda_b^{r-s}/\operatorname{Tr}(T^N)\), at \(t=(\lambda_b/\lambda_a)^r\). Use half the weight for a diagonal pair and omit pairs with both eigenvalues zero. This is the displayed formula, with the natural value \(t^0=1\). The trace sums converge by Cauchy–Schwarz for the separated insertions. The first matrix inequality follows at \(l=1\). The second follows by ordinary Cauchy–Schwarz and stationarity for every linear combination. This uses the positive Wilson transfer and periodic trace in GL8 cited above.

**PROVED.** At a Fourier frequency \(\theta=2\pi j/n\), the sum of the two finite geometric series for the off-diagonal kernel has modulus at most \(4/|1-te^{i\theta}|\) if \(\theta\ne0\). Since \(|1-e^{i\theta}|\le2|1-te^{i\theta}|\) and \(|1-e^{i\theta}|\le2\), multiplication by \(|1-e^{i\theta}|^2\) costs at most \(16\) on those two sums together. The diagonal \(K_0\) costs at most \(4K_0\). Thus the Fourier matrix of the covariance of the differences is bounded above by \(20K_0\). At frequency zero the difference vanishes. Discrete Parseval on the coefficient vectors proves (20).

**PROVED.** In (19) set the unused odd positions in (20) to zero. Hold transverse shifts and differences inside the reading \(G_l\), and apply (20) successively in each of the three spatial directions. The transverse operations preserve the required reflection in the direction being considered. This gives \(\nu|F_z|^2\le 20^3 C_2\sum_m|z_m|^2\), first before the time limit and then in the vacuum cylinder. All \(8(n/2)^3\) sampled plaquettes are distinct and their link sets are separated by at least \(r-1\) in the periodic lattice. Their private marked edges therefore give \(\sum_i d^\pi_{W_i\setminus G}(F_z)\ge 8(2^{-19}/49)\sum_m|z_m|^2\) by the conditional variance argument for (16). Equation (17)'s joint-law comparison gives \(\operatorname{Var}_\pi F_z\le (1+\eta_0)\nu|F_z|^2\). This proves (18) on (19) uniformly as \(\eta_0\to0\).

**OPEN.** The three differences annihilate a plaquette mode that is constant along any sampled coordinate. In particular (19) excludes the spatially homogeneous sum of action densities. The estimate establishes loss of conditional variance for an extensive set of collective fluctuations. It leaves open both the slowly varying sums and the other gauge-invariant functions of the slice.

## Relative comparison at arbitrarily small excitation energies

**PROVED.** The diagonal two-slice form improves (17) when the energy tends to zero. Identify the two spatial configurations by time translation and write \(F_s=F(U_{t_s})\) for one and the same gauge-invariant function \(F\), \(s=0,1\). Define
\[
  g_\pi=\inf_{\operatorname{Var}_{\pi} F_0>0}
         {\pi|F_0-F_1|^2\over 2\operatorname{Var}_{\pi}F_0},
  \qquad R=1+\eta_0 .
\]
Then
\[
   R^{-2}g_\pi\ \le\ 1-e^{-2b m_{\rm lat}(N,\beta)}
                     \ \le\ R^2 g_\pi.                                  \tag{21}
\]
In the unpinned vacuum the quotient has infimum exactly \(1-e^{-2b m_{\rm lat}}\), by reversibility and the positive physical transfer used in (17). Both its numerator and its denominator compare within a factor \(R\) in either direction under pinning. For its denominator use \(\operatorname{Var} F=\inf_c\mathbb E|F-c|^2\). For its numerator use the likelihood bound on the entire joint slice algebra. This proves (21) with no additive error, including for eigenfunctions supported mostly on very rare slice configurations.

**PROVED.** Let \(P_i\) condition on \(W_i\setminus G\) in the pinned law. Conditional independence of the two slice interiors gives the exact decomposition
\[
 \pi|F_0-F_1|^2=
 d_i^\pi(F_0)+d_i^\pi(F_1)+\pi|P_iF_0-P_iF_1|^2
 \qquad(i=1,2,3),
\]
where \(d_i^\pi=d^\pi_{W_i\setminus G}\). Thus even (18) on just the first endpoint suffices for \(g_\pi\ge c/6\). There is also an exclusion for trial eigenfunctions. Put \(D(f)=(\sum_i d_i^\pi(f))^{1/2}\) on the first endpoint. If \(f=F_0\) is centered there with unit variance and its quotient in (21) is \(u\), then \(D(f)\le\sqrt{6u}\). For any centered linear space of slice tests \(\mathcal L\) satisfying (18) with constant \(c>0\),
\[
 \operatorname{dist}_{L^2(\pi)}(f,\mathcal L)
 \ \ge\ {(\sqrt c-\sqrt{6u})_+\over\sqrt3+\sqrt c}.
\]
Indeed \(D(g)\le D(f)+\sqrt3\|g-f\|_2\) by the triangle inequality for the three orthogonal residuals, while \(D(g)\ge\sqrt c\,\|g\|_2\) on \(\mathcal L\). Apply these bounds to arbitrary \(g\in\mathcal L\). In particular, if the finite-cube physical gaps tend to zero in physical units, their normalized slow eigenfunctions must stay a positive distance from every uniformly controlled test space above. A bound on each fixed space with its own deteriorating constant does not exclude such eigenfunctions.

**PROVED.** One can test the remaining form on events, including events of arbitrarily small probability. For a gauge-invariant set \(A\) of spatial configurations, write \(A_s=\{U_{t_s}\in A\}\). Define
\[
 \Phi_\pi=\inf_{0<\pi(A_0)<1}
       {\pi(A_0\mathbin{\triangle} A_1)
        \over 2\min(\pi(A_0),\,1-\pi(A_0))}.
\]
The same definition in the unpinned vacuum gives \(\Phi_\nu\), and \(R^{-2}\Phi_\nu\le\Phi_\pi\le R^2\Phi_\nu\) by the joint likelihood bound, also for either complementary marginal. In the vacuum
\[
       \tfrac12\Phi_\nu^2\ \le\ 1-e^{-2b m_{\rm lat}}\ \le\ 2\Phi_\nu.
                                                                         \tag{22}
\]
For the upper bound test the diagonal quotient on each indicator. For the lower bound take a real \(f\) and subtract a median. For its positive part \(g\), every positive superlevel set has mass at most \(1/2\). Integrate the definition of \(\Phi_\nu\) over the superlevel sets of \(g^2\). This gives
\(\Phi_\nu\|g\|_2^2\le\tfrac12\nu|g_0^2-g_1^2|\le \|g\|_2(\nu|g_0-g_1|^2)^{1/2}\)
by stationarity and Cauchy–Schwarz. Apply it also to the negative part. The squared differences of the two parts sum to at most the squared difference of \(f\), and the second moment about its median is at least its variance. Complex functions split into two real ones. This is the conductance inequality for this reversible physical transfer. It gives a necessary and sufficient positive lower bound along the stated sequences for the full finite-cube gaps in physical units.

**OPEN.** The outstanding event estimate asks whether a gauge-invariant property can have almost the same truth value on the two whole slices with disagreement probability negligible compared with the probability of its rarer value. The relative comparison at (21)–(22) preserves precisely that possibility. Independent conditional cell interiors pay for any uncertainty left by a wall. To defeat all three walls the same event must be predictable on both slices and those predictions must agree. The following test treats arbitrary thresholds and more general Borel readings of finitely many plaquettes.

## Arbitrarily rare events of finitely many capped plaquettes

**PROVED.** On either slice let \(X_1,\ldots,X_n\) be the separated scaled action densities used in the finite-polynomial argument. Fix \(n\) and \(B>0\) and put \(Y_p=\min(X_p,B)\). There is \(c(n,B)>0\) independent of the spatial size and of all sufficiently fine cutoffs such that (18) holds for *every* square-integrable Borel function of \((Y_1,\ldots,Y_n)\). In particular the infimum in (22)'s event test restricted to this sigma-field is bounded below in the pinned law, even for cutoffs and thresholds chosen so that the measured event has probability tending to zero.

**PROVED.** Let \(\sigma_B\) be the probability measure on \([0,B]\) proportional to \(\sqrt x\,dx\) on \([0,B)\) plus a unit atom at \(B\). Expose all edges except the separate marks as before. For every tilt \(H\) with \(|H|\le6\beta\), the tilted quaternion density relative to Haar is at most \(C(1+|H|)^{3/2}\). Indeed the spherical cap of chordal radius \((1+|H|)^{-1/2}\) about the tilt direction has volume at least \(c(1+|H|)^{-3/2}\) and exponent at least \(|H|-1\). The Haar density of \(X_p\) at \(x\) is at most \(C\beta^{-3/2}\sqrt{x}\). Therefore the conditional law of \(Y_p\) is bounded above by \(A_B\sigma_B\) uniformly in the exterior. The unit atom before normalizing \(\sigma_B\) absorbs the whole upper tail.

**PROVED.** On the exposed good event of probability at least \(1/2\) from the finite-polynomial argument, the conditional density of \(X_p\) at \(0<x<B+1\) is at least \(a_{K,B}\sqrt{x}\), for \(\beta\ge B+1\) sufficiently large. The tilt direction is within \(C\sqrt{K/\beta}\) of the plaquette target. At value \(x\), the mark is within \(\sqrt{2x/\beta}\) of that target. The exponent is at least \(|H|-C(K+B+1)\). Use the earlier upper bound on the tilt normalizer, \(|H|\ge3\beta\), and the Haar density lower bound \(c\beta^{-3/2}\sqrt{x}\). Integration over \(B<x<B+1\) supplies a positive lower bound for the atom of \(Y_p\). The conditional law of every \(Y_p\) on the good event thus dominates \(a\sigma_B\), with a common \(a=a(n,B)>0\).

**PROVED.** The marks are conditionally independent. Consequently the joint marginal of \(Y\) is bounded above by \(A_B^n\sigma_B^{\otimes n}\), and its conditional law on every good exterior is bounded below by \(a^n\sigma_B^{\otimes n}\). The three-group conditional variance argument above now gives, for every such Borel function \(f\),
\[
 \sum_{i=1}^3 d_i^\pi(f(Y))
 \ \ge\ \tfrac12 a^n\operatorname{Var}_{\sigma_B^{\otimes n}}f
 \ \ge\ \tfrac12(a/A_B)^n\operatorname{Var}_{\pi}f(Y).                 \tag{23}
\]
The lower marginal bound also gives the required integrability under \(\sigma_B^{\otimes n}\). For an event determined by \(Y\), take \(f\) to be its indicator on the first slice. The conditional decomposition after (21) gives \(\pi(A_0\mathbin{\triangle}A_1)\ge c(n,B)\pi(A_0)(1-\pi(A_0))/3\). Dividing by twice the smaller marginal gives the claimed positive lower bound, irrespective of the measure of the event. This does not use a polynomial approximation with constants depending on its degree.

**OPEN.** The cap collapses all large deficits at each marked face into a single value. Formula (23) distinguishes any measurable subset of the remaining range but cannot separate events deep inside that tail. Its constant also deteriorates with the number of faces. A slice event depending on an entire growing spatial region can exploit both freedoms. Neither the marked exponential moment nor (23) bounds its disagreement probability relative to its mass.

## The spatially homogeneous action and its low-energy spectral weight

**PROVED.** There is an unconditional estimate for a homogeneous scalar observable on a set of isotropic weak couplings of positive relative measure. Let \(N\) be the spatial side, let \(M\) be the time period, and put \(V=N^3M\). Use the ordinary Wilson normalization \(Z(\beta)=\int e^{-\beta S}\), \(S=\sum_p(1-w_p)\). Let \(Y_t\) be \(\beta\) times the sum of the unscaled deficits on all electric plaquettes between slices \(t\) and \(t+1\), plus half the sum on the magnetic plaquettes of both endpoint slices, also multiplied by \(\beta\). Thus \(Y_t\) is a reflection-even unit-slab reading and \(\sum_{t=0}^{M-1}Y_t=\beta S\) exactly. Row 1165, (14), gives a fixed-coupling bulk specific-heat estimate conditional on finite-rectangle source bounds. Here coupling averaging and positive physical transfer give a spectral statement on the vacuum cylinder with no such input. [Row 1165, specific heat](gap-solve11-astra62.md)

**PROVED.** There is an absolute \(C\) such that for every \(B\ge1\), uniformly in the periods used here,
\[
 \frac1B\int_B^{2B}\frac{\beta^2}{V}\operatorname{Var}_\beta S\,d\beta
 \ \le\ C .
\]
Indeed \(-\partial_\beta \mathbb E_\beta S=\operatorname{Var}_\beta S\) by differentiation of the finite integral. Row 1155, (9), bounds \(\mathbb E_B S\le C'V/B\) on all these rectangles. Integrate the derivative, use \(S\ge0\), and bound \(\beta^2\) by \(4B^2\).

**PROVED.** Denote the connected covariance of \(Y_0,Y_s\) by \(C_M(s)\). It is nonnegative for every \(1\le s<M\). In the transfer trace use the real symmetric one-step insertion \(A\) for \(Y_0\) from the argument for (20), with the finite-period mean subtracted by replacing \(A\) by \(A-\mathbb E_\beta(Y_0)T\). The numerator for the covariance is a sum of \(|A_{vw}|^2\lambda_v^{s-1}\lambda_w^{M-s-1}\) for this centered insertion. This works also when two unit slabs share their end spatial slice. Their half-weights multiply in the trace. Thus
\[
 \frac{\beta^2}{V}\operatorname{Var}_\beta S
                 =N^{-3}\sum_{s=0}^{M-1} C_M(s).
\]
At fixed \(N,\beta\), take \(M\to\infty\). For each fixed displacement the bounded reading at this cutoff converges to its vacuum-cylinder moment by the simple positive transfer vacuum. In that vacuum \(C(s)=\int_{[0,1]}\lambda^{s-1}d\xi(\lambda)\) at \(s\ge1\), where \(\xi\) is the finite positive spectral measure of the centered one-step insertion applied to the vacuum, divided in squared norm by the square of the vacuum eigenvalue. \(C(0)=\operatorname{Var}_\nu Y_0\). For each fixed \(k\) retain \(s=0,1,\ldots,k,M-k,\ldots,M-1\) in the nonnegative sum. Fatou's lemma in \(\beta\), then monotone convergence in \(k\), proves
\[
 \frac1B\int_B^{2B}\frac1{N^3}\left[
    \operatorname{Var}_\nu Y_0+
    2\int_{[0,1]}\frac{d\xi(\lambda)}{1-\lambda}\right]d\beta\ \le C .
                                                                         \tag{24}
\]
Here \(\nu\) and \(\xi\) in the integrand are evaluated at \(N,\beta\). Thus for each even compatible \(N\) at least half of every such coupling interval, by Lebesgue measure, has the entire bracket at most \(2C N^3\). This selection is at the actual isotropic Wilson action.

**PROVED.** At any selected coupling the homogeneous slab observable has both a positive variance loss on the walls and a small bare low-energy weight. For the first assertion choose either endpoint slab \([t_s,t_s+1]\) of (17), with the same pinned graph and \(h\ge8\). Each spatial layer of the slab misses all common graph spatial edges, and its temporal edges meet each common temporal segment in at most one link. The joint likelihood comparison (4) therefore applies to gauge-invariant tests of the whole slab. For the graph alone one can retain \(h-3\) private links on each segment after exposing the slab. In particular \(\operatorname{Var}_{\pi}Y_{t_s}\le C' N^3\) whenever this comparison has bounded likelihood ratio. Mark the temporal edges of the slab at spatial coordinates all \(1\bmod4\). No such edge belongs to any of the three walls, and no plaquette contains two of them. Given the complement of the marks, all terms in \(Y_{t_s}\) involving a given mark sum to a constant minus \(H\cdot x\), where \(x\) is its unit quaternion and \(H\) its actual six-staple tilt. The earlier good-staple argument for this one edge gives \(\pi(|H|\ge3\beta)\ge1/2\) for large \(\beta\), uniformly in the mark. Row 1165, (7), gives a universal lower bound on the conditional variance of \(H\cdot x\) for \(|H|\ge3\), by its one-dimensional Haar marginal. The conditional variances add. Consequently \(d_i^\pi(Y_{t_s})\ge cN^3\) for each wall. This also lower-bounds the ordinary variance in the pinned law at the same scale.

**PROVED.** For the second assertion, on that same set of couplings, at any proposed lattice spacing \(a>0\) and physical energy cutoff \(E>0\), (24) gives
\[
 N^{-3}\,\xi([e^{-aE},1])\le C(1-e^{-aE})\le CaE .                    \tag{25}
\]
The interval on the left includes every excitation of energy at most \(E\) for this reading. One can take successive \(B\to\infty\) and growing spatial cubes. These conclusions are about the volume-normalized bare observable and the selected couplings. The estimate makes no assertion at a coupling prescribed in advance in each interval, or for a differently renormalized scalar field.

**OPEN.** Even finite \(\int (1-\lambda)^{-1}d\xi\) cannot force a spectral interval free of weight: the positive measure \((1-\lambda)d\lambda\) on \([0,1]\) has finite integral of this kind and gives positive mass to every interval ending at one. The homogeneous observable also does not test all singlet states. The coupling derivative controls its integrated spectral weight, while a mass gap requires absence of low-energy spectrum in every physical channel of the continuum theory.

## Remaining obligation

**OPEN.** For the ordinary isotropic Wilson action at one fixed physical time separation on growing spatial cubes, (21)–(22) reduce the finite-volume spectral question to a relative disagreement bound for every gauge-invariant slice event. The estimates for mixed spatial differences, capped local readings and the homogeneous slab action leave open this infimum. A positive bound on this route would still require construction and identification of a nontrivial continuum Yang–Mills theory with the Jaffe–Witten axioms and a dense local observable space on the same sequence. The sources checked here do not supply that construction.

RESULT — OPEN. Row 1222. Equations (17) and (21)–(22) compare the physical finite-cube gap with correlations and event disagreement on two spatial slices after fixing the common graph. The hand estimates (19)–(20), (23) and (24)–(25) control specific collective and local observables. A uniform bound for all slice events and the matched continuum construction remain open. This attempt did not prove the four-dimensional SU(2) Jaffe–Witten mass gap. Research only, independently unchecked.
