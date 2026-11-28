# Repo search

Row 1511 at checkout `c842e1a1bb09`. I searched `origin/main` (8b11ae2bb95e), `pr/10114` (f76f6c649cff), `pr/10133` (89faef229ff6), `pr/10134` (1e70c7211a2c) and `pr/10141` (c73ad7b177d9). `PUR-io`, `M-io-exists`, `457/625`, `neutral purity` and `neutral thermal trace` returned no hits on these refs or outside the lane in the pinned checkout.

- **Boundary transport.** Terms included normal and exterior parallel links, mixed plaquettes, centre flips, Hamming coupling, gauge orbits and layer oscillation. Main's `research/mass-gap/library/gap-ds-gauge.md` gives the directional budget and telescoping for several changed boundary links. Its check confirms the convention. The local row 1122 identifies the unique plaquette of an exterior parallel link and couples a change of a single face-interior normal by a vertex gauge. Rows 1498 and 1501 get $\delta\ge(81/125)u_P$ from the 54 face-interior normals per direction at side four. They suggest the sign probe. Row 1499 with check 1500 rules out contraction for full intersecting face data after a join. Row 1502 found no applicable published in-law criterion. The all-vertex lower bound below did not occur in these hits. [Directional budget](gap-ds-gauge.md) · [Cube geometry](gap-l3-direction-fable.md) · [1498](gap-r8-loop-consumer-fable.md) · [1501](gap-r8-loop-consumer-check-astra62.md) · [1499](gap-k2-interface-join-astra62.md)
- **Closest other estimates.** `MASS_GAP_LOCAL_BLOCK_ASTRA.md` on #10114 and #10133 proves a positive one-step plaquette correlation, with Doob contraction for $0<\beta\le1/32$. Main's `SU2_TWO_REGION_BOUNDARY_RESPONSE_BOUNDED_THEOREM_NOTE_2026-11-08.md` bounds a soft-kernel single-link influence by $\tanh(\lambda^2)$. Row 1497 leaves concentration on a class restriction open. The local interval-resampling estimate contracts a one-dimensional Hamming seminorm. None gives (W) at $23/10$. The task-specific prior file is absent and the registry has no matching owner for the obstruction. [November 8 inventory](prior/repo-search-2026-11-08.md) · [1497](gap-k2-direction-checkpoint-check-astra62.md) · [Interval resampling](gap-solve-fresh-astra62.md) · [Registry](open-registry.md)
- **Thermal comparison and its rate.** Searches included Proposition MIX, plaquette expectations at two periods, physical decay rate and positive separated two-point witness. Main's `research/mass-gap/library/gap-mid-max.md` and its check convert a uniform plaquette discrepancy $\eta$ to a log-mass discrepancy at most $12un^3\beta\eta$. The Dobrushin verification works for $\beta<1/18$. Locally, `gap-os-equiv.md` (5) passes a common physical decay rate to the limit. Row 1462 checks extraction with a positive separated pair from every infinite set of calibrated depths. Below these facts constrain the explicit bound (4). [Proposition MIX](gap-mid-max.md) · [Dobrushin check](gap-dob-astra.md) · [Rate transfer](gap-os-equiv.md) · [Extraction](gap-crux-direction-astra-check-opus.md)
- **Sussman–Alpoge.** I searched the index, obligations, then the supplied TeX for the seed and transport terms. Outline 240–260, 284–293 and 427–440 give the Wilson action, vertex gauges and conditional law. GL3–GL4 at 2197–2239 give the SU(2) Haar integral. At 4638–4641 the outline says a mass gap “requires a separate spectral estimate.” CA-I 2699–2713 gives $H\ge0$ and lists the gap among its omissions. CA-III 381 uses “layer links” for a ladder of indices. The supplied outline and account at `31a47c543775` are by Ethan Sussman and Levent Alpoge with Claude and Codex. Bałaban's small-field estimates, as quoted in the lane, supply no order-one boundary budget used here. [Outline index](sa-index/README.md) · [Obligations](sa-index/obligations.md) · [Bałaban source record](lit-balaban.md)

**Result — REFUTED for two specified families.** At $\beta=23/10$ the side-four Wilson block forces $\delta>392/225$ in (W), whose hypothesis is $\delta<1$. The obstruction covers every integer side through ten and all positive directional Hamming weights. At the calibrated roots, the absolute seam estimate (4) has a divergent right side for every admissible choice of its parameters. Its decay rate in physical units cannot diverge in the presence of the positive two-point witness. (PUR-io), (M-io-exists) and the physical mass gap remain open.

## Plan recorded at the start

1. Read the target and prior results and identify the exact calibration and quantifiers.
2. Search the repository and the Sussman–Alpoge sources for the proposed statement and method.
3. Test a sufficient estimate for the Wilson seed, including its constants and any obstruction.
4. Record the proof or first unproved lemma, the first component needed and two follow-up rows.

## Physical target

Fix the release's odd block factor $b$, one $0<g_0<\delta_{\rm cal}$ and a side $\ell$ that is a positive multiple of 1024. Set $n=\ell b^K$ and $u=n/512$. For the Wilson transfer on the spatial $n^3$ torus at the least-root coupling $\beta_K(g_0)$, let $Z_+(t)$ be the trace of its $t$-th power in the full centre-neutral gauge-invariant sector. The target is $P_K=Z_+(2u)/Z_+(u)^2\ge457/625$ on infinitely many $K$ for one such $\ell,g_0$. Fact PUR then gives $s_K(u)\le4/21$. I test the order-one Wilson boundary criterion left open by row 1501, then trace a modification for gauge-invariant observables to the thermal comparison at the actual calibrated roots. [Exact target and Fact PUR, §3.1](gap-k2-tool-design-fable.md)

## The Wilson cube and the obstruction

Let $S=\{0,\ldots,R\}^{4}$ for an integer $R\ge1$. Let $V$ consist of the unoriented nearest-neighbour links with both endpoints in $S$, choosing one orientation for integration. Its boundary $\partial V$ consists of the links outside $V$ sharing a plaquette with $V$. The same definitions apply in a torus with all periods at least $R+4$. Write $N_R=R(R+1)^3$ and $q(g)=\tfrac12\operatorname{Re}\operatorname{tr}g$.

Here is the family of estimates under test. Fix any constants $h_1,\ldots,h_4>0$, set $h_e=h_{\operatorname{dir}e}$, and use the cost
$$
\rho_h(\sigma,\sigma')=\sum_{e\in V}h_e\,{\bf1}_{\sigma_e\ne\sigma'_e}.
$$
For each $z\in\partial V$, let $k_z\ge0$ bound the mean cost of some coupling for **every** pair of conditional laws whose boundaries agree off $z$. The coupling can depend on both boundaries. Impose $\sum_{z\parallel i}k_z\le\delta h_i N_R$ for each $i$. The Dobrushin–Shlosman block criterion in row 691, (W), takes all $h_i=1$ and requires $\delta<1$.

**Theorem.** Put
$$
m_\beta=\frac{\int_{SU(2)}\operatorname{sgn}(q(g))e^{\beta q(g)}\,dg}
                  {\int_{SU(2)}e^{\beta q(g)}\,dg},
\qquad \operatorname{sgn}(0)=0 .
$$
For every $\beta\ge0$, every $R$ and every choice of the four weights, the Wilson specification requires
$$
\boxed{\displaystyle
\delta\ \ge\ 3\left[1-\left(\frac{R-1}{R+1}\right)^3\right]m_\beta .}
\tag{1}
$$
The bound also holds if the product of the wholly internal plaquette weights is replaced by any positive, Haar-integrable density $A(\sigma)$ invariant under a centre flip at each boundary vertex. The mixed plaquettes retain their Wilson factors. Thus a restriction on the internal action alone cannot evade (1) within this family.

**Geometry and averaging measure.** Call $e\in V$ exposed if it lies in a boundary face. Write $E$ for these links. A mixed plaquette has one inside link $e$, two outward normals at its endpoints and one exterior layer link parallel to $e$. Indeed its two varying coordinates form a rectangle. If three vertices lie in $S$, the fourth does too. Every mixed plaquette is therefore obtained by translating an exposed link by one unit outward in a face containing it. The layer link has both endpoints outside in that one normal coordinate. Its inward translate is unique. In particular, layer links and mixed plaquettes are in bijection, also where several faces contain the same $e$. This uses row 1122's Lemma TILT.

Give the links in $V\cup\partial V$ the joint probability law proportional to
$$
 A(\sigma)\prod_{p\ {\rm mixed}} e^{\beta q(U_p(\sigma,\tau))}
 \,d\sigma\,d\tau ,
\tag{2}
$$
with product Haar as reference. For Wilson, $A=\exp(\beta\sum_{p\ {\rm internal}}q(U_p))$. Its constant action shift cancels. The finite number of bounded mixed factors and the hypothesis on $A$ give a finite positive normalizer. Conditional on $\tau$, (2) gives exactly the cube kernel $\gamma^\tau$. Conditional on $\sigma$ and all the normal links, each mixed holonomy is a fixed left and right translate of its own layer link or its inverse. Those layer links occur in separate factors. Haar invariance therefore makes the mixed holonomies independent with normalized density $e^{\beta q(g)}dg/\int e^{\beta q}$. Every one has sign mean $m_\beta$. In the argument below the boundary is averaged with the **marginal of (2)**. A product-Haar average of the normalized conditional kernels would have different weights.

**Two boundary changes at each vertex.** Choose one incident mixed plaquette $p(e)$ for each $e\in E$, once and for all. Fix a surface vertex $x$. Let $N_x$ contain its outward normal links. Let $L_x$ contain the layer links incident to their exterior endpoints. Write $G_x\sigma$ for the sign change on all links of $V$ incident to $x$. Starting from any $\tau$, either of the following changes pushes $\gamma^\tau$ to the law of $G_x\sigma$ for $\sigma\sim\gamma^\tau$.

1. Flip the centre at $x$ on the full graph. Exactly $N_x$ changes on the boundary.
2. Flip the centre at $x$ and at all its outward neighbours. Each normal in $N_x$ has both endpoints flipped. Each outward neighbour has a unique neighbour in $S$, namely $x$. Two distinct outward neighbours of $x$ have lattice distance two. Hence the changed boundary is precisely $L_x$.

These are changes of variables on the conditional integral. The internal density is invariant, plaquette traces are invariant under a vertex gauge transformation, and multiplication by the centre preserves Haar. Both changes act on the internal links by the same $G_x$.

With the **original** $\tau$ held fixed, use the observable
$$
 F_{x,\tau}(\sigma)=\frac12
 \sum_{\substack{e\in E\\e\ni x}}h_e\,\operatorname{sgn}q(U_{p(e)}(\sigma,\tau)).
$$
Each summand reads one distinct internal link. Its oscillation is at most $h_e$, so $F_{x,\tau}$ is 1-Lipschitz for $\rho_h$. Moreover $F_{x,\tau}(G_x\sigma)=-F_{x,\tau}(\sigma)$. This uses the central sign even for a link traversed backwards. For any fixed 1-Lipschitz $F$, each one-link coupling in the hypothesis gives $|\gamma^\omega F-\gamma^{\omega'}F|\le k_z$. Change a finite set $D$ one link at a time and sum this inequality for the same $F$. This is the expectation form of row 691, Lemma 1. Taking $D=N_x$ and then $D=L_x$ gives, for each choice separately,
$$
 \sum_{z\in D} k_z \ \ge\ 2\gamma^\tau F_{x,\tau}.
$$
Integrate against the boundary marginal of (2). The right side is $m_\beta\sum_{e\in E:e\ni x}h_e$. No choice of an optimal transport plan or of a common maximizing boundary is required.

**Counting.** Sum first over $x$ with $D=N_x$. Every normal has one inside endpoint, while every exposed link has two. Thus $\sum_{\rm normal}k_z\ge2m_\beta\sum_{e\in E}h_e$. Sum next with $D=L_x$. Each layer link is counted at the two endpoints of its unique inward translate, so $\sum_{\rm layer}k_z\ge m_\beta\sum_{e\in E}h_e$. The two boundary sets are disjoint and exhaust $\partial V$.

A link in direction $i$ is unexposed precisely when its three transverse coordinates all lie in $\{1,\ldots,R-1\}$. Thus there are $R[(R+1)^3-(R-1)^3]$ exposed links in each direction. The four directional upper bounds give $\sum_{\partial V}k_z\le\delta N_R\sum_i h_i$. Comparing with the two lower bounds and cancelling the positive common factor proves (1).

## The one-plaquette integral at the specified coupling

**Hand bound.** At $\beta_*=23/10$, $m_{\beta_*}>20/27$. Write $X=q(g)$ under Haar. The SU(2) Weyl formula in outline GL3 gives density $(2/\pi)\sqrt{1-x^2}$ on $[-1,1]$. By symmetry the numerator of $m_\beta$ is $B=\mathbb E\sinh(\beta|X|)$ and the denominator is $D=\mathbb E\cosh(\beta X)$.

GL3 at spin zero, with its displayed Bessel series, gives $D=\sum_{j\ge0}d_j$, $d_j=(\beta^2/4)^j/(j!(j+1)!)$. At $\beta_*$, $d_0=1$, $d_1=529/800<2/3$, and $d_2=\beta_*^4/192<7/48$ since $529^2=279841<280000$. For $j\ge2$ the successive ratio is at most $529/4800<1/9$. Hence
$$
D<1+\frac23+\frac98\frac7{48}<\frac{11}{6},
$$
where $21/128<1/6$ gives the last inequality.

Integrating $x^{1,3,5}\sqrt{1-x^2}$ on $[0,1]$ by $y=1-x^2$ gives $\mathbb E|X|=4/(3\pi)$, $\mathbb E|X|^3=8/(15\pi)$ and $\mathbb E|X|^5=32/(105\pi)$. The first three positive terms of $\sinh$ therefore give
$$
B>\frac4\pi\left(\frac{\beta_*}{3}+
                \frac{\beta_*^3}{45}+\frac{\beta_*^5}{1575}\right)
  >\frac{14}{11}\left(\frac{23}{30}+\frac4{15}+\frac1{25}\right).
$$
Here $\beta_*^3>12$ and $\beta_*^2>21/4$, so $\beta_*^5>63$. The bound $\pi<22/7$ follows by integrating $x^4(1-x)^4/(1+x^2)$ from zero to one. Polynomial division gives integral $22/7-\pi$, which is positive. Consequently
$$
m_{\beta_*}>\frac{14}{11}\frac{161}{150}\frac6{11}
             =\frac{2254}{3025}>\frac{20}{27},
$$
since $60858>60500$. At larger $\beta$, $m_\beta$ increases. Its derivative is $\operatorname{Cov}_\beta(\operatorname{sgn}X,X)\ge0$, as seen by multiplying the differences of these two increasing functions on two independent copies of $X$.

**Consequences.** At side four, (1) forces $\delta>(294/125)(20/27)=392/225$. The normal links alone already force $\delta>(196/125)(20/27)=784/675>1$. Even the trace probe $q$ in place of its sign gives a separate scalar check at this side. Its one-plaquette mean is $I_2/I_1>7/15$ by the GL4 estimate used and checked in rows 1499–1500. With both boundary sums this gives $\delta>686/625>1$.

The geometric coefficient in (1) decreases with $R$. At $R=10$ its product with $20/27$ is $12040/11979>1$. Thus **every** cube with $1\le R\le10$ fails the strict criterion at every $\beta\ge23/10$.

There is also a conclusion on the bare calibrated lattices. Under the one-plaquette tilt, $\Pr_\beta(X\le0)\le e^{-\beta/2}/\Pr_{\rm Haar}(X\ge1/2)$, by restricting the denominator to $X\ge1/2$. Hence $m_\beta\to1$. At $R=14$ the coefficient in (1) is $3534/3375>1$. For every sequence $\beta_K\to\infty$, eventually all $1\le R\le14$ fail (W), even with a different $\delta_K<1$ at each cutoff. This includes the calibrated bare roots by row 1461's $|\beta_K-B_K|\le C_I$, $B_K=sK+O(\log(1+K))$ with $s>0$. The geometry fits the target tori for all sufficiently large $K$. At $R=15$ the coefficient is $507/512$ and it decreases thereafter. A larger-cube estimate needs further information. [Least-root result](gap-crux-direction-astra62.md) · [Check of the width bound](gap-crux-direction-astra-check-opus.md)

## Stability under a change of the boundary action

Multiply the density in (2) by a positive continuous $H(\sigma,\tau)$. Assume $H$ is invariant under centre flips at the vertices of $S$ and at the exterior endpoints of normals, acting on the links of $V\cup\partial V$. Suppose changing **one layer link** with every other link fixed changes $\log H$ by at most $\epsilon$. There is no smallness hypothesis on its total oscillation.

Put $r_\beta=(1-m_\beta)/(1+m_\beta)$. Given every link except the unique layer link of $p$, the event $q(U_p)<0$ has odds at most $e^\epsilon r_\beta$ against $q(U_p)>0$. Indeed, without $H$ the two integrals have ratio $r_\beta$ by Haar translation. With $H$, bound the numerator by its maximum in that layer coordinate and the denominator by its minimum. The equator has Haar measure zero. Thus the conditional sign mean is at least
$$
\frac{1-e^\epsilon r_\beta}{1+e^\epsilon r_\beta}.
$$
This bound survives averaging over all the other links. Gauge covariance still gives the two boundary changes in the proof of (1). Substitution of this lower bound for $m_\beta$ in (1) is therefore valid even when $H$ couples different layer links.

In particular, for $\beta\ge23/10$ and $\epsilon\le\log 2$, the odds are strictly below $14/47$ and the sign mean exceeds $33/61$. At side four the resulting bound is $\delta>9702/7625>1$. This excludes a class of changes to the order-one action with an explicit tolerance in each boundary coordinate. An exact blocked family would have to be tested for this interaction range, invariance and oscillation before this statement could be applied to it.

## A criterion for gauge-invariant correlations

The two boundary changes in the obstruction act on the cube by a vertex gauge. They have identical conditional expectations for every gauge-invariant function supported in $V$. This is why the obstruction does not give an upper bound on the neutral purity. The following modification gives a quantitative test on the boundary data that still affect gauge-invariant observables. Its numerical hypothesis for Wilson remains open.

Work with unit link costs. For exterior values $\tau,\tau'$ differing only at $z$, draw internal arrays $\sigma,\sigma'$ from a coupling of their cube kernels. On the two resulting arrays on $V\cup\partial V$, let $d_S$ be the minimum number of differing links after applying any vertex gauge to the second array supported on $S$. **Count the normal links after this change of gauge.** All links touching a vertex of $S$ are in $V\cup\partial V$. The cost includes a changed layer link even though the gauge cannot change it. The minimum exists and is Borel in the arrays. Hamming cost is lower semicontinuous, the gauge action is continuous, and minimizing a jointly lower semicontinuous function over compact $SU(2)^S$ preserves lower semicontinuity, by a convergent subnet or subsequence of minimizers. Set
$$
 c_z=\sup_{\tau=\tau'\ {\rm off}\ z}\ \inf_{\rm couplings}\mathbb E d_S,\qquad
 C_i=\sum_{z\parallel i}c_z,\qquad b_i=\#\{z\in\partial V:z\parallel i\}.
$$
All exterior values in the supremum are allowed. No quotient of the Gibbs measure is needed.

**A coefficient computed exactly.** If $z$ is the unique outward normal at a face-interior vertex $x$, then $c_z=0$ at every coupling. For any old and new values of $z$, some gauge $g_x$ at its inside endpoint carries the old value to the new one by left or right multiplication. It fixes all other exterior links. Row 1122's coupling draws $\sigma'=g_x\sigma$. Applying $g_x^{-1}$ on the second completed array aligns every link. This gives 54 zero coefficients per direction at side four. Ordinary Hamming cost on the internal links alone detects the same gauge motion.

**Conditional theorem.** If $C_i<N_R+b_i$ for every $i$, gauge-invariant bounded local functions have exponentially decaying connected correlations, with uniform constants on ordinary periodic Wilson tori of periods at least $R+4$, at this coupling. Here is the proof and the rate. Choose $\lambda>0$ so that
$$
 L=\min_i\bigl(N_R+b_i-e^{\lambda(R+2)}C_i\bigr)>0.
$$
Let $M$ be the number of lattice sites. Write $K_a$ for conditional resampling in $V+a$ and $P=M^{-1}\sum_a K_a$. Each resampling preserves the torus Wilson probability $\mu$ and maps gauge-invariant functions to gauge-invariant functions, by conditional integration and gauge covariance.

Use sup distance of the lower endpoints with periodic distances in each coordinate. For a nonempty support $X$, set $w_y=e^{-\lambda d(y,X)}$. Write $\omega_y(f)$ for the supremum of the change in $f$ when only link $y$ changes and $\|f\|_X=\max_y \omega_y(f)/w_y$. All test functions below are real. For $y\in V+a$, $\omega_y(K_af)=0$. For $y$ outside the cube and its boundary, use the same resampled array in both copies to get $\omega_y(K_af)\le\omega_y(f)$. For $y=z+a$ in the boundary, gauge invariance permits the aligning gauge within $S+a$. Outside $(V\cup\partial V)+a$ the two arrays then agree. Telescoping single-link changes within this set bounds the difference of the two $f$ values by $d_{S+a}$ times the largest $\omega_e(f)$ there. Since the set has diameter at most $R+2$, taking the coupling infimum gives
$$
 \omega_y(K_a f)\le c_z\,e^{\lambda(R+2)}w_y\|f\|_X .
$$
This is an inequality for expectations for each fixed pair of boundary values. It needs no measurable choice of an optimal gauge or coupling as those values vary. For $y$ of direction $i$, exactly $N_R$ translates contain it and $b_i$ others have it on their boundary. Each relative boundary link of that direction occurs once. Hence $\|Pf\|_X\le(1-L/M)\|f\|_X$. Here $N_R+b_i\le M$ because the translates counted are distinct. Iterating and telescoping over the finite torus links gives uniform convergence $P^j f\to\mu f$ for gauge-invariant $f$.

For $F,G$ supported on nonempty $X,Y$, respectively, with $F$ gauge invariant, write $\operatorname{Cov}_\mu(F,G)=\sum_{j\ge0}\mu[(P^jF-P^{j+1}F)G]$. For a fixed $a$ the corresponding summand is an integrated conditional covariance of $P^jF$ with $G$. It vanishes if $V+a$ misses $Y$. Its absolute value is at most $\|G\|_\infty\sum_{e\in V+a}\omega_e(P^jF)$, by centering $P^jF$ in its conditional range. At most $N_R|Y|$ translates meet $Y$. For their links $w_e\le e^{\lambda(R+2)}e^{-\lambda d(X,Y)}$. Since $\|F\|_X\le2\|F\|_\infty$, averaging over $a$ and summing the geometric series gives
$$
 |\operatorname{Cov}_\mu(F,G)|
 \le \frac{2N_R |Y|\,|V|e^{\lambda(R+2)}}{L}
       \|F\|_\infty\|G\|_\infty e^{-\lambda d(X,Y)} .
\tag{3}
$$
This argument uses the translated-cube count and bounded-diameter estimate of row 691. The change to its transport argument is the minimization over local gauges with all exterior disagreements retained. Equation (3) concerns Euclidean correlations of the Wilson law.

At $R=4$, $N_R=500$ and $b_i=2(5)^3+6(4)(5)^2=850$ by row 1122. The remaining test is $C_i<1350$ in each direction, with 796 terms left after the 54 zeros. For a single-change comparison the elementary coupling bound $d_S\le |V|+1=2001$ gives no such margin. Nor does (1) bound $C_i$ from below by 1350, because its sign probe depends on the original gauge frames. I have not established that the two aggregate tests have different truth values for Wilson at this coupling. No physical seed is credited to (3).

## The two-period purity bound

Here is a sufficient estimate stated in the variables of the physical target. It uses the two-period plaquette comparison from Proposition MIX and the signed neutral derivative from rows 1461 and 1465. The estimate added here is the effect of changing the time seam under the gauge-aligned resampling bound. [Proposition MIX, checked](gap-dob-astra.md) · [Signed derivative, Step 6](gap-crux-direction-astra-check2-opus.md)

Fix $n=\ell b^K$, $u=n/512$ with $\ell$ a positive multiple of 1024, and $R+4\le u$. Suppose that **throughout** $0\le t\le\beta_K$ the ordinary Wilson cube coefficients at coupling $t$ satisfy
$$
 \min_i\bigl(N_R+b_i-e^{\lambda(R+2)}C_i(t)\bigr)\ge L>0
$$
for a fixed integer $R\ge1$ and fixed $\lambda,L>0$ at this $K$. Put $D=(u/2-R-4)_+$, where $s_+=\max(s,0)$. Then
$$
 -\log P_K\ \le\
 \frac{768\,\beta_K\,u\,n^3\,N_R|V|}{L}\,e^{-\lambda D}.
\tag{4}
$$
At one fixed bare coupling, a common margin on the interval from zero to that coupling gives $P\to1$ as $n=512u\to\infty$. For the physical target one would need the right side at most $\log(625/457)$ on infinitely many cutoffs for one $\ell,g_0$. The calibrated obstruction below addresses this even when $R,\lambda,L$ depend on $K$.

**Proof.** Work on the link array of the ordinary $n^3\times2u$ torus with its untwisted law $\mu$ at $t$. There are two other laws of interest on this same product of Haar spaces. One is a long torus with any temporal twist. The other is the product of two short $n^3\times u$ tori with a prescribed temporal twist on each. For the latter, use the same time-link labels and reconnect the links starting at $u-1$ and $2u-1$ to close their respective halves. Put the twist signs at the closing time bonds. The density ratio of either law $\nu$ to $\mu$ depends only on a set $B$ of at most $16n^3$ links. Take all four directions with lower time coordinate in $\{0,u-1,u,2u-1\}$. Each changed temporal plaquette uses time links at a closing bond and spatial links on its old or new endpoint slices. All purely spatial plaquette factors agree. Normalizers are scalars. Consequently $\nu K_a=\nu$ whenever $(V+a)\cap B$ is empty.

Let $F$ be the average of the $6n^3$ plaquette traces based at time $u/2$, over all spatial sites and all six orientations. Write $X$ for its support. It is gauge invariant in the long torus and agrees with the short-torus observable there. Each link occurs in at most six summands, and each trace has oscillation at most two. Hence $\|F\|_X\le2/n^3$. This spatial average cancels the area of the cuts in the estimate. In the telescoping identity $\nu F-\mu F=\sum_{j\ge0}\nu[(I-P)P^jF]$ only translates meeting $B$ contribute. For each such translate,
$$
 \bigl|(I-K_a)P^jF\bigr|
 \le\sum_{e\in V+a}\omega_e(P^jF)
 \le (2|V|/n^3)(1-L/M)^j e^{-\lambda D}.
$$
Indeed $d(X,B)\ge u/2-2$ and $V+a$ has diameter at most $R+2$. There are at most $N_R|B|$ such translates. The $1/M$ in $P$ cancels the $M/L$ from the geometric series. Thus $|\nu F-\mu F|\le2N_R|B||V|e^{-\lambda D}/(Ln^3)\le32N_R|V|e^{-\lambda D}/L$. Comparing a long twisted law and a short twisted law through $\mu$ costs at most twice this quantity.

The signed plaquette mean for a fixed orientation is constant under translation for each temporal twist. Moving a sign stack back to its original cut multiplies links by centre signs and preserves the signed insertion, as checked in 1499–1500. Thus the mid-slab average represents the signed mean over all six orientations on the corresponding torus. Taking the positive mass-weighted averages over the eight twists at each period preserves the comparison. The already checked derivative of $\log P$ is $12un^3$ times the difference of the six-orientation averages. Since $P(0)=1$, integration gives (4). [Twist translation and seam conventions](gap-k2-interface-join-astra62.md)

**First open inequality on this route.** For $R=4$, decide whether $\sup_{0\le t\le23/10}\max_i C_i(t)<1350$. The 54 zero costs hold on the whole interval. Each remaining cost is at least one. A changed layer link lies outside every allowed gauge. For a changed normal at a multiple-face vertex, an unchanged normal at that vertex would force the aligning gauge there to be the identity if its cost were zero. At $t=0$ common internal Haar samples give cost at most one for every one of these 796 links, so $C_i(0)=796$ exactly. The missing estimate is an upper bound strictly below 554 on the sum of **excess** costs $c_z-1$, uniform on the interval. A pass would prove the fixed-coupling thermal conclusion above. At the calibrated roots there is a further, decisive obstruction to this absolute estimate, proved below.

**First component for testing the excess.** A layer link $z$ has exterior endpoints. Let $W_z$ be the three-link path between them through its mixed plaquette, omitting $z$. Gauges supported on $S$ leave this open transport unchanged. For a genuine change at $z$, any aligned pair already pays one on $z$. If the two $W_z$ values differ, it also pays on the path. Thus $c_z-1$ is at least the total variation distance of the two $W_z$ laws for each such boundary pair. With the plaquette of $z$ deleted, let $\pi$ be the law of $W_z$ at the common remaining boundary. Reinserting the plaquette at $z=g$ gives exactly $e^{t q(W_z g^{-1})}\pi(dW_z)/\int e^{t q(W_z g^{-1})}d\pi$, orienting both paths alike. For $g$ and $-g$ these are different at positive $t$ since $\pi$ has full support by positivity of the finite Wilson density. More generally, sums of total variation distances on edge-disjoint paths with exterior endpoints bound the excess from below when the paths avoid $z$ and use the same boundary pair. Each mismatch requires a distinct differing link after every admissible gauge change. An upper bound must instead couple the joint path and interior data.

## An obstruction at the calibrated roots

**Rate bound.** Fix the release parameters and one $0<g_0<\delta_{\rm cal}$. Consider any infinite set of its least-root depths. Suppose that at each of these depths the ordinary Wilson laws on every sufficiently large periodic cube obey (3), uniformly in its size, with rate $\lambda_K>0$ per lattice spacing. The prefactor may grow arbitrarily with $K$ and with the local tests, provided it is independent of the separation of two translates and of the box size at fixed $K$. Then the physical rates $\lambda_K b^K$ are bounded on this set. There is no upper bound of a specified numerical size in this assertion.

**Proof.** Otherwise choose depths along which $\lambda_K b^K\to\infty$. Apply the first lemma of row 1461, as checked in 1462, to this very set. Along a further sequence $K_j$ it supplies a volume-first limit $S$ in the original units, with a positive separated two-point witness for the centered plaquette-energy field. The dilation for the possible constant lag is already part of that lemma. Write $\nu_j$ for the corresponding periodic-limit state at fixed $j$. The estimate passes to $\nu_j$ on continuous local functions by weak convergence for each pair of translates separately. Arbitrarily large volumes are available **before** taking $j\to\infty$. [Extraction and positive witness](gap-crux-direction-astra-check-opus.md)

Fix a real smooth compact one-field test $f$ strictly in the positive time half-space. Its centered plaquette-energy smear $F_j$ at spacing $b^{-K_j}$ is a bounded continuous gauge-invariant local observable with finite support at fixed $j$. Its support is strictly positive for all sufficiently large $j$. Let $\theta$ reflect through the time-zero site plane, let $\tau_k$ translate by $k$ lattice units and set
$$
 A_m=\nu_j[(\theta F_j)\tau_{4m}F_j],\qquad m\ge0 .
$$
Site reflection positivity for these local observables follows already on an even periodic cube. Condition on the spatial links in the two fixed time slices. Each Wilson plaquette lies in the closure of one of the two halves. Factors supported in the fixed slices are constants under this conditioning. The two open halves are conditionally independent and reflected copies. Their paired expectation is therefore a square. Choosing a cube large enough for any given finite set of shifts and passing to the periodic limit gives the positive reflection form at fixed $j$. Translation invariance passes in the same way. In this form $A_m$ is the squared norm of $\tau_{2m}F_j$. Cauchy–Schwarz on $\tau_{2(m-1)}F_j,\tau_{2(m+1)}F_j$ gives $A_m^2\le A_{m-1}A_{m+1}$ for $m\ge1$. Centering and (3) give $A_m\le H_{j,f} e^{-4\lambda_{K_j}m}$ with $H_{j,f}<\infty$ independent of $m$. The supports are fixed translates at this $j$, and their distance is at least $4m$ minus a fixed support diameter and offset.

Consequently $A_m\le A_0 e^{-4\lambda_{K_j}m}$. Indeed a zero propagates forward by the displayed inequality. On any positive sequence the ratios $A_{m+1}/A_m$ are nondecreasing, and a ratio greater than $e^{-4\lambda_{K_j}}$ would contradict the exponential envelope at arbitrarily large $m$. If the first zero follows a positive term, log convexity forces that positive term to be $A_0$. This is the diagonal reflection-positive rate argument of the existing limit theorem. Its role here is to remove the uncontrolled prefactor $H_{j,f}$. [Diagonal rate transfer, (5)](gap-os-equiv.md)

For each integer $q\ge1$ use the fixed physical time $d=4b^{-q}$. Eventually $d b^{K_j}/4$ is an integer. The barycentre reflection and translation rule and volume-first convergence on the common time grid give
$$
 A_0\longrightarrow S_2(\theta f,f),\qquad
 A_{d b^{K_j}/4}\longrightarrow S_2(\theta f,\tau_d f).
$$
The two smear supports are disjoint even at $d=0$, so only separated moments enter these limits. Since $A_0$ has a finite limit and $d\lambda_{K_j} b^{K_j}\to\infty$, every such $S_2(\theta f,\tau_d f)$ is zero. Continuity on separated Schwartz tests as $d\downarrow0$ gives $S_2(\theta f,f)=0$. Reflection positivity of $S$ and Cauchy–Schwarz then give $S_2(\theta f,h)=0$ for every compact positive-time one-field test $h$. [Common-grid convergence and continuity, rows 1449–1450](sa-ym4-lean-faithful-astra62.md)

This annihilates the separated two-point witness. Indeed any two compact disjoint supports can be partitioned using balls of diameter less than one quarter of the sup-distance between them. Each pair of pieces is separated by a coordinate hyperplane. Coordinate permutation and translation turn that plane into the time-zero plane. Reflecting the negative-time factor gives the preceding form. Bilinearity yields zero on the original pair. Equivalently the two-point distribution vanishes off the diagonal. To see this also for a joint test, partition its compact off-diagonal support into product boxes of this type. On one such box expand the smooth localized test on a slightly larger rectangle by a Fourier series and multiply by product cutoffs equal to one on its support. Its partial sums are finite sums of products with separated supports and converge with every derivative by integration by parts. The distribution therefore vanishes there. Schwartz tails can be cut off by dilation of smooth compact cutoffs with convergence in Schwartz seminorms. This contradicts the positive witness. $\square$

This also sets the precision of any fixed-size transport test at the bare roots. Fix $R$, let $B_R=N_R+b_i$ (independent of $i$ by cube symmetry), and let $C_*=\max_i C_i(\beta_K)$. Then
$$
 (B_R-C_*)_+=O_{R,g_0,b}(b^{-K}).
$$
Indeed $C_*>0$ because every changed exterior layer link costs at least one. If $C_*<B_R$, take $\lambda_K=\log(B_R/C_*)/[2(R+2)]$ in (3), so $L=B_R-\sqrt{B_R C_*}>0$. On any infinite set of such cutoffs the rate bound gives $\lambda_K b^K\le H$ for some finite $H$. Thus $B_R-C_*\le B_R(1-e^{-2(R+2)H b^{-K}})\le 2B_R(R+2)H b^{-K}$. The other cutoffs contribute zero to the positive part, and a finite set is absorbed in the constant. In particular the threshold $1350$ at side four has no uniform strictly positive margin at the calibrated endpoints. This does not decide its margin on $[0,23/10]$.

**Consequence for (4).** For every fixed physical side $\ell$ and level $g_0$, the right side of (4) tends to infinity along any infinite set of calibrated cutoffs at which its hypotheses hold, even if $R,\lambda,L$ are chosen anew at each cutoff. Indeed
$$
 b_i/N_R=2/R+6/(R+1)\le5,\qquad L\le N_R+b_i\le6 N_R,\qquad D\le u/2 .
$$
Thus that side is at least $128\,\beta_K u n^3 e^{-\lambda_K u/2}$. The calibrated roots tend to infinity and $u=\ell b^K/512$. A bounded subsequence of this expression would force $\lambda_K b^K\to\infty$ along it. The endpoint $t=\beta_K$ supplies (3) with that very rate on all sufficiently large periodic cubes, contradicting the rate bound. More generally the contradiction applies to any majorant bounded below by $a_K e^{-c\lambda_K n}$ with $a_K\to\infty$, fixed $c>0$, and $\lambda_K$ an actual uniform periodic local-correlation rate as above. The result concerns this way of bounding the thermal difference. The value of the signed difference and the value of $P_K$ remain open.

A physical comparison could use the scaling of the action insertion, cancellation between the signed seam responses, or rates integrated separately over shrinking coupling intervals. The obstruction identifies the missing feature precisely in a bound that pays a growing absolute prefactor against a single ordinary covariance rate at lattice resolution. For the finite order-one problem, the first quantity that can be built and tested separately is the anchored path law above.

**Verification.** Codex wrote and checked the hand proofs here. Row 1501 checked the earlier face-interior witness, row 1500 checked the quoted Bessel margin, and row 1462 checked the volume-first extraction. The all-vertex count, perturbed boundary bound, relative-gauge comparison and its calibrated obstruction await a separate reader. No Monte Carlo, floating-point or Lean computation enters these new results. This research text grants no status. Row 1510's output was not consulted.

## Next two rows and their decisive outcomes

1. **Check the two obstructions.** Reconstruct both counts from a face, an edge and a corner, and check the sign integral against the side-four threshold. Check the removal of the correlation prefactor by reflection positivity, the fixed-time grid and the use of the positive separated witness. A confirmation rules out (W) for $R\le10$ at $23/10$ and (4) as a calibrated certificate on any fixed physical side. A correction should identify the first failed inequality and state which of the two verdicts survives. The normal-only count also has its own side-four margin.
2. **Decide the gauge-invariant transport test at order-one coupling.** At $R=4$, bound the 796 residual excess costs using local gauge alignment and paths anchored at exterior endpoints. A uniform sum strictly below 554 in each direction for $0\le t\le23/10$ proves fixed-bare-coupling exponential decay and large-box neutral purity by (3)–(4). A direction and coupling with a sum at least 554, or a certified supremum reaching 554, refutes that uniform test. Either outcome decides whether this finite-block test can supply the order-one input. Carrying such input to a calibrated seed still requires a comparison that controls the signed thermal difference on the physical scale.
