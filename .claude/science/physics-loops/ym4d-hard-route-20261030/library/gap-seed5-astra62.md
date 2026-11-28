## Repo search

**GUIDE.** Row 1377, science checkout `41bb3b4b0`. I searched the Markdown and TeX on `origin/main` (`8b11ae2bb95e`), `pr/10114` (`f76f6c649cff`), `pr/10133` (`89faef229ff6`), `pr/10134` (`1e70c7211a2c`) and `pr/10141` (`c73ad7b177d9`). The precise terms M-neutral, one-box neutral seed, neutral thermal or transfer trace, vacuum-subtracted transfer trace and whole-face likelihood returned no matches. Bare 4/21 has unrelated matches. Searches for link-wise replica exchange, unordered bond pairs and Wilson exchange clusters found the unrelated two-index matrix restriction in `b188_check_findings.md`. Searches on the same refs for replica midpoint or locking, relative vertex gauges, gauge-orbit pinning, plaquette mismatch, electric convolution with two covers, and face heat kernels with purity returned no relevant hits. The row-specific prior packet is absent. The registry's G0-SEED-CAI asks for a gauge with a prescribed link bound on background-field reads. I found no registry owner of the neutral thermal trace.

**GUIDE.** On main, `research/mass-gap/library/gap-phys-seed.md`, Theorem ZD-c, identifies the periodic seed on admissible dyadic sides with bounded large-side Casimir defect and unbounded lower cutoff limit of the side times the periodic gap, given its inputs. The hits in `ROWS.md` and `gap-phys-seed-check.md` refer to that theorem. The neutral seed has a separate consumer in either flux branch. On PRs 10114 and 10133, the soft-route `MASS_GAP_LOCAL_BLOCK_ASTRA.md` (11) gives a one-step centered elementary-plaquette correlation at least $v_N^2 e^{-68\beta}/(1+v_N/r_f(\beta)^4)$. This is a lower bound at one lattice time. The present question needs an upper bound on all neutral excitations at positive physical time. [November 8 digest, §11](prior/repo-search-2026-11-08.md) · [Theorem ZD-c and lead notes](gap-phys-seed.md) · [Matched-limit implication, row 1349](gap-seed-audit-check-astra.md)

**GUIDE.** In the outline by Ethan Sussman and Levent Alpoge, written with Claude and Codex, GL8 at 2313–2335 identifies the periodic partition function with the trace of a positive gauge-projected transfer power. Lines 31871–31882 exhibit a polynomially decaying Laplace transform with spectrum down to zero. CA-I 2699–2713 leaves the mass gap open, and CA-III 108223–108260 uses spectral exclusion as a premise of the reflected-decay implication. Source revision supplied for the four texts is `31a47c543775`. Bałaban's CMP 122b Theorem 1, as quoted in the lane, gives ultraviolet stability under the specified running-coupling ceiling. [Outline index](sa-index/README.md) · [Obligations](sa-index/obligations.md) · [Bałaban quotations, §3](lit-balaban.md)

**GUIDE.** Row 1367 fixed the volume quantifier. Rows 1371 and 1373 treat successive angular observations. Check 1374 identifies the full sum in 1373 (17) with a strict-margin version of the original test. Row 1375 studies dense single-link conditionals and many full-length winding readings. I use its author text only. Row 1330 uses a family of covers. The subsequent comparison of the split and connected double covers observes *unordered pairs* of fine links in `gap-solve43-astra62.md`, §§2–5. That observation can distinguish the covers with small error at weak bare coupling. Row 1290 (25) already sews in the two ways by powers of a relative-gauge kernel. Its (26) proves positivity by projecting tensor powers. [Marked electric kernel](gap-solve33-astra62.md) [Two-cover comparison](gap-solve43-astra62.md) · [Row 1374](gap-seed3-check-opus.md) · [Row 1375](gap-seed4-astra62.md)

## One fixed physical side

**OPEN.** On the prescribed trajectory choose one admissible physical $L$. For all late $j$ write $n=L/a_j$, with $4\mid n$, $n\ge 2^{70}$ and $\beta_0\le\beta_j\le B_0\log n$. At zero magnetic twist, $P_0$ is the projection onto the trivial character of the eight electric centre flips. If $1=r_0>r_1\ge r_2\ge\cdots\ge0$ are the eigenvalues of $P_0T/\lambda_0$ on the neutral space, the desired inequality is $s(t)=\sum_{i>0}r_i^t\le4/21$ at $t=2\lfloor n/1024\rfloor$. Time monotonicity makes this the largest available test time. Row 1161 (19) uses a different order of limits. For the continuum implication I keep the matched reflection-positive datum, (H2) and totality of the selected observables as inputs, as in check 1349. [Volume quantifiers](gap-seed-astra62.md) · [Sharp constant, rows 1356 and 1359](gap-mini-mneutral-check-astra.md)

**GUIDE.** The approach is to couple the two spatial faces through their relative gauge orientations and measure the response to exchanging the time histories. A second use of the same integral as a probability channel measures how much the entire noisy spatial face reveals about the normalized half-slab state.

## Coupling two complete spatial faces

**PROVED (the two endpoints of the interpolation).** Work at finite $n,\beta$ and integer $t=2w$. Use normalized product Haar measure $dx$ on the $E=3n^3$ positive spatial links. Write $K(x,y)=(P_0T)^t(x,y)$ and $Z_u=\operatorname{Tr}(P_0T)^u$. The Wilson integral makes $K$ continuous, strictly positive, symmetric and invariant under independent vertex gauges at its two ends. It is also a Gram kernel by gluing two half-slabs. For a nonnegative symmetric weight $B(x,y)$ define
$$
 D[B]=\int B(x,y)K(x,x)K(y,y)\,dx\,dy,\qquad
 N[B]=\int B(x,y)K(x,y)^2\,dx\,dy .
 \tag{1}
$$
Gram Cauchy–Schwarz gives $N[B]\le D[B]$. At $B=1$ these are $Z_t^2$ and $Z_{2t}$, respectively. This implements the centre projection on each constituent slab, including when the two ends of distinct histories are joined. Set $P=N[1]/D[1]$. If $p_i=r_i^t/(1+s(t))$, then $P=\sum_i p_i^2$. In particular $P\ge457/625$ suffices for $s(t)\le4/21$. Indeed if $p_0\le1/2$ then $P\le1/2$. Otherwise $P\le p_0^2+(1-p_0)^2$, which increases up to one and equals $457/625$ at $p_0=21/25$. This is the two-copy bound in row 1373 (4). The normalization in (1) retains every neutral level. [Finite-copy check](gap-seed3-check-opus.md)

**PROVED (a pin on gauge orbits).** Write $x_e,y_e$ as unit quaternions, $G=\mathrm{SU}(2)^{n^3}$, and $(g y)_e=g_v y_e g_{v'}^{-1}$ for $e=(v,v')$. The inner product is the real Euclidean product on $\mathbb R^4$. For $h\ge0$ put
$$
 A_h(x,y)=\int_G \exp\!\left(h\sum_e x_e\cdot(g y)_e\right)dg,\qquad
 B_h(x,y)=\frac{A_h(x,y)}{\sqrt{A_h(x,x)A_h(y,y)}} .
 \tag{2}
$$
For each summand $x_e\cdot(g y)_e=2|(x_e+(g y)_e)/2|^2-1$. Thus (2) measures the lengths of the quaternion midpoints and integrates the relative vertex orientations. The exponential of the inner product is a positive semidefinite kernel by its tensor-power series. Gauge averaging projects its feature vectors orthogonally onto the invariant vectors, since the gauge action on the ambient real space is orthogonal. Consequently $0<B_h\le1$ and $B_h(x,x)=1$. It has the value one on a pair of gauge-equivalent faces. At $h=0$ it is identically one.

**PROVED (strong pinning at fixed cutoff).** Let $d(x,y)=\min_g(\sum_e|x_e-(g y)_e|^2)^{1/2}$. The maximum of $\sum_e x_e\cdot(g y)_e$ is $E-d(x,y)^2/2$. For fixed $n$, restricting the Haar integral to a neighbourhood of a maximizing gauge and using uniform continuity gives $h^{-1}\log B_h\to-d^2/2$ uniformly in $x,y$. For any $\delta>0$ the part of $D[B_h]$ with $d\ge\delta$ is exponentially smaller than its part with $d<\delta/2$. The latter set has positive Haar mass and $K(x,x)$ has a positive minimum at this fixed cutoff. The continuous ratio $K(x,y)^2/[K(x,x)K(y,y)]$ equals one when $d=0$. Compactness, first $h\to\infty$ then $\delta\downarrow0$, gives $N[B_h]/D[B_h]\to1$. The question is how much this ratio changes on removing the pin.

**GUIDE (existing loop integral).** Row 1151, §10, integrates the relative $S^3$ vertex spins on a Wilson electric seam. Its sphere-moment expansion pairs indices at vertices, leaving normalized traces of the two link holonomies on every closed strand. The same relative gauge integral is $A_h$ in (2), used here on a pair of faces in either law (1). The positive sphere-spin expansion is the random-path method credited in that row. The identification of replica exchange with the outer symmetry of $\mathrm{Spin}(4)$ already appears in `gap-laptop-solve3-fable.md`, §2.4(5). [Relative gauge integral](gap-solve5-astra62.md) · [Earlier replica interpretation](gap-laptop-solve3-fable.md)

## The first interaction that survives on the entire face

**PROVED (uniform expansion).** Write $V=n^3$ and $W_p(x)=\tfrac12\operatorname{tr}x_p$. For even $n\ge8$ and all pairs of spatial configurations there are absolute $h_0,C>0$ such that
$$
 \left|\log B_h(x,y)+\frac{h^4}{128}
       \sum_{p\ {\rm spatial}}(W_p(x)-W_p(y))^2\right|
       \le C V h^6,\qquad 0\le h\le h_0 .                         \tag{3}
$$
In particular the error is absolute on a face whose volume tends to infinity whenever $Vh^6\to0$.

**PROVED.** Put $M(h)=\int_{S^3}e^{h u_1}\,du$ for probability surface measure. The edge variable in (2) is $u_e=g_v\cdot R_e g_{v'}$, with $R_e z=x_e z\bar y_e$. Factor out $M(h)^E$ and expand the product of $1+f_e$, where $f_e=e^{hu_e}/M(h)-1$. For complex $|h|$ in an absolute small disk, $|f_e|\le C_0|h|$ and the integral in either endpoint spin alone is zero. The weight of a connected edge set $H$ is $a_H=\int\prod_{e\in H}f_e\,dg$. The weight vanishes if $H$ has a leaf. Components on disjoint vertex sets factor.

**PROVED (control of the logarithm).** For any induced set of vertices $S$ let $Z(S)$ be the sum over collections of vertex-disjoint nonempty connected edge sets, weighted by the products of $a_H$ inside $S$, including the empty collection. For $v\in S$ split off the unique component containing $v$, if present. The ratio $Z(S)/Z(S\setminus\{v\})$ differs from one by the sum of $a_H Z(S\setminus V(H))/Z(S\setminus\{v\})$ over $H$ containing $v$. There are at most $6^{2k}$ edge sets of size $k$ connected to $v$ and containing it, by traversing their doubled edges in a walk from $v$. Inductively require each deletion ratio to be within $1/2$ of one. Deleting the other vertices of $H$ then costs at most $2^k$ in the inverse ratios. The sum is at most $\sum_{k\ge1}(72 C_0|h|)^k<1/2$ on a fixed disk, proving the induction from $Z(\varnothing)=1$. The branch of $\log Z(S)$ through zero at $h=0$ is bounded there by $C|S|$ by telescoping the deletion ratios. This argument also bounds the complex Taylor remainder of order five by $CV|h|^6$ on a smaller disk.

**PROVED (coefficient).** A surviving edge set with at most four edges must be an elementary square. Its coefficient in degree four is $4^{-4}\operatorname{Tr}_{\mathbb R^4}\prod_{e\in p} R_e^{\pm1}$, by $\int gg^{\mathsf T}dg=I/4$ at each of its four vertices. The real trace of $z\mapsto u z\bar v$ is $4\operatorname{Re}(u)\operatorname{Re}(v)$, by evaluating in the quaternion basis. The coefficient is therefore $W_p(x)W_p(y)/64$. Changing all vertex spins on one bipartite colour by a minus sign proves evenness in $h$. The empty graph is the constant term and $\log Z$ has the same fourth coefficient as $Z$. The single-edge terms $E\log M(h)$ cancel exactly in (2). Subtracting half the two diagonal fourth coefficients proves (3).

## Removing a pin with a nonvanishing effect on both Wilson integrals

**PROVED (whole-face response, given the checked local Wilson estimates).** Assume $\beta\to\infty$ in the stated logarithmic band. Let $\mathbb P_D$ and $\mathbb P_N$ be the normalized laws in (1) at $B=1$. Uniformly for $h\ge0$ such that $\tau=Vh^4/\beta^2\le\tfrac14\log\beta$,
$$
 \mathbb E_i\left|e^{9\tau/512}B_h(X,Y)-1\right|=o(1),
 \qquad i\in\{D,N\}.                                                   \tag{4}
$$
Thus $D[B_h]/D[1]$ and $N[B_h]/N[1]$ both equal $e^{-9\tau/512}(1+o(1))$. The ratio of the two pinning factors tends to one even at strengths where each factor tends to zero. The assertion is about all $3V$ spatial plaquettes on the two faces jointly.

**PROVED (inputs and moments).** Set $A_p(x)=\beta(1-W_p(x))$. Use row 1373 (5), checked in row 1374 S7–S15, with $b=\lceil\beta^{1/16}\rceil$. For one orientation and either one mark or two marks more than $4b+4$ apart, the matrix holonomies on one face, jointly with the opposite face, differ in total variation by at most $C\beta^{-1/32}\sqrt{\log\beta}$ from independent $\exp(G/\sqrt\beta)$ marks independent of that opposite face, with $G\sim N(0,I_3/2)$. For $D$, each face is the marginal on a neutral period-$t$ circle and the two circles are independent. For $N$, use the period-$2t$ circle, then apply the marginal estimate to its other face. In the proof of 1373 (5) the half-period is respectively $w$ and $2w$. The discarded time fraction is $O(b/w)$ and the entropy per spacetime lattice site has the same $O((\log\beta)(1/b+b/n+b/w))$ bound for either half-period. The translated cuts leave both marked faces in opposite arcs. Cubic symmetry gives the other orientations. The hypothesis $\beta\le B_0\log n$ absorbs the finite-side terms. [Local matrix estimate](gap-seed3-astra62.md) · [Check S7–S15](gap-seed3-check-opus.md)

**PROVED.** The ordinary one-plaquette exponential moment and the projection comparison $\mathbb E_+ H\le(8\mathbb E_{\rm ord}H^2)^{1/2}$ for a nonnegative contractible insertion (row 1373, following (6)) bound $\mathbb E_i e^{c A_p}$ by an absolute constant for some $c>0$. One may place the temporal seam off the spatial insertion. The Gaussian reference action $\beta(1-\cos(|G|/\sqrt\beta))$ is bounded by $|G|^2/2$. Its difference from $|G|^2/2$ is at most $|G|^4/(24\beta)$. Consequently the joint comparison just quoted gives every action moment of total degree at most four on the indicated marks at both ends within $O(\beta^{-1/50})$ in absolute value of the moments of independent $|G|^2/2$. To see the rate, truncate each action at $C_1\log\beta$. Hölder with the one-mark exponential moments bounds the expectation of a discarded degree-four product by $O(\beta^{-1})$ for large fixed $C_1$. The bounded-product error is $O(\beta^{-1/32}(\log\beta)^{9/2})$. Gaussian moments absorb the $O(\beta^{-1})$ Taylor error. These estimates need only a bounded number of marks.

**PROVED (spatial average).** For either law write
$$
 H=V^{-1}\sum_{p\ {\rm spatial}}(A_p(X)-A_p(Y))^2 .
$$
The reference action is $\chi_3^2/4$, of variance $3/8$. Two independent reference actions have mean squared difference $3/4$. For one orientation, pairs of bases at distance at most $4b+4$ number $O(V b^3)$, and the fourth-moment bound controls each such term. For all other pairs use the preceding joint estimate with two marks at each end. Their reference squared differences are independent. Expanding the square about $3/4$ gives an expected squared error $O(\beta^{-1/50}+b^3/V)$ for that orientation's average. Add the three errors in $L^2$, obtaining $\mathbb E_i|H-9/4|\le C\beta^{-1/100}$. This estimate for an empirical mean uses no assumption that nearby plaquettes are independent.

**PROVED.** Equation (3) gives $\log B_h=-\tau H/128+O(Vh^6)$. Here $Vh^6=\beta^3\tau^{3/2}/\sqrt V$. On the stated interval this vanishes faster than any negative power of $\beta$. The function $e^{-u}$ is 1-Lipschitz for $u\ge0$. The error on replacing $B_h$ in mean absolute difference by $e^{-9\tau/512}$ is therefore at most $C(\tau\beta^{-1/100}+Vh^6)$. Multiplication by $e^{9\tau/512}\le\beta^{9/2048}$ proves (4). The normalized pinned and unpinned whole-face laws also differ by $o(1)$ in total variation, separately on each cover. The relative normalization in (4) matters for comparing their unnormalized masses.

## A finite-strength pin has small mass on both covers

**PROVED (a pointwise bound).** For $h>0$ and the $m=V/64$ spatial $23$-plaquettes whose bases have all coordinates divisible by four, write $\mathcal P$ for this set. There is a positive $a(h)$, independent of $n$, such that
$$
 B_h(x,y)\le
 \exp\!\left[-a(h)\sum_{p\in\mathcal P}(W_p(x)-W_p(y))^2\right].   \tag{5}
$$
The proof isolates actual plaquette components of the gauge integral even at strengths outside the Taylor disk of (3).

**PROVED (one isolated square).** On one plaquette the normalized kernel in (2) is the cosine of the angle between the real vectors
$$
 v_h(u)=(r_d(h)^2\chi_d(u))_{d\ge1},\qquad r_d(h)=I_d(h)/I_1(h),
$$
evaluated on the two plaquette holonomies. Here $\chi_d$ is the dimension-$d$ character. Indeed integrating the four vertex spins around this cycle is the trace of the fourth power of the central single-bond convolution, composed with $z\mapsto x_p z y_p^{-1}$. In the dimension-$d$ matrix-coefficient space that transformation has trace $\chi_d(x_p)\chi_d(y_p)$. The scalar convolution multiplier cancels on normalizing. This uses GL3 and its absolutely convergent character expansion, outline 2195–2231. Put $D_h=\sum_d d^2 r_d^4<\infty$. The first two coordinates are $1,2r_2^2 W_p$. The squared area from this $2\times2$ minor divided by the product of squared vector norms bounds $1-b_p^2$ from below, where $b_p$ is the isolated normalized kernel. Thus $1-b_p\ge 2r_2^4(W_p(x)-W_p(y))^2/D_h^2$. Positivity of the original integral gives $0<b_p\le1$.

**PROVED (isolating many squares).** For each selected square mark every edge incident to its four vertices other than its own four edges. There are at most $16$ such edges, and the marked sets are disjoint. On just the marked edges expand $e^{h u}=e^{-h}+(e^{h u}-e^{-h})$. Both kernels are pointwise nonnegative and positive semidefinite before projection. The second assertion follows from the tensor-power expansion with nonnegative coefficients, including constant coefficient $1-e^{-h}$. For each choice $F$ of terms this gives a positive semidefinite gauge-averaged kernel $A_F$ with nonnegative entries by tensoring the factors and projecting onto the vertex-gauge invariants. A square whose entire marked set received constant factors is isolated. The integral factors into its square kernels and the remaining positive semidefinite kernel. Therefore
$$
 A_F(x,y)\le\sqrt{A_F(x,x)A_F(y,y)}
                \prod_{p\ {\rm isolated}} b_p .
$$
For the self integral at $x$, the probabilities of the choices $F$ are $A_F(x,x)/A_h(x,x)$. They can be sampled by first drawing the relative vertex gauges in that self integral, then choosing the constant terms independently on marked edges with probabilities $e^{-h-hu_e}\ge e^{-2h}$. Conditional on the gauges, the selected squares are isolated independently with probabilities at least $e^{-32h}$. Consequently the mean of the displayed product of $b_p$ is at most $\prod_{p\in\mathcal P}[1-e^{-32h}(1-b_p)]$. The same estimate holds at $y$. Sum the displayed inequality over $F$ and use Cauchy–Schwarz with these two self laws. This proves (5) with $a(h)=2 e^{-32h}r_2^4/D_h^2$. The positive common-term expansion used to select factors in earlier replica work is credited to Kandel–Domany and the subsequent local-exchange constructions in row 1131. Here both summands must additionally give positive semidefinite kernels on the face. [Earlier replica expansion](gap-council-prob-astra.md)

**PROVED (Wilson estimate at physical time).** For some absolute $c>0$, under each of the two actual unpinned laws,
$$
  \mathbb E_i B_h\le
    \exp\!\left[-\frac{c V\min\{a(h),1\}}{(1+\beta)^2}\right],
       \qquad i\in\{D,N\}.                                           \tag{6}
$$
In particular a pin of any fixed positive strength has vanishing total weight under both laws throughout the logarithmic coupling band.

**PROVED.** Condition on the other face, seam bits, and all spacetime links except one chosen edge of each selected plaquette on this face. No action plaquette contains two chosen edges. The chosen links are conditionally independent. After fixed multiplications and inversion, the holonomy of each chosen plaquette is a unit quaternion of density proportional to $e^{H\cdot q}$, with $k=|H|\le6\beta$. This uses just the six Wilson staples. To bound the density of one real coordinate $s$ uniformly in the direction of $H$, put $r=\sqrt{1-s^2}$ and write that direction as axial component $a$ and transverse length $b$, so $a^2+b^2=1$. For $k>0$ the density is
$$
 \frac{2}{\pi M(k)}r e^{kas}\frac{\sinh(kbr)}{kbr}.
$$
Use the continuous value at $br=0$. The cap of angular radius $k^{-1/2}$ gives $M(k)\ge c e^k k^{-3/2}$ for $k\ge1$. The resulting density is at most $C k^{3/2}\min(r,1/(kb))e^{-k(1-as-br)}$. For $r\le2/\sqrt k$ use the first entry of the minimum. Otherwise if $b\ge r/2$ use the second. For $b<r/2$, $1-as-br\ge(r-b)^2/2\ge r^2/8$. These cases bound the density by $Ck$. For $k\le1$ Haar comparison gives a constant. Therefore, uniformly in the fixed target $W_p(X)$, with conditional probability at least $1/2$ the distance $|W_p(Y)-W_p(X)|$ exceeds $c_0/(1+\beta)$ for an absolute $c_0>0$. Multiply the $m$ one-plaquette conditional bounds on the exponential in (5), then remove the conditioning. This proves (6) for the split law and for the joined law, whose two independently projected Wilson arcs still have positive seam weights.

**ARGUED (what the pin comparison costs).** Equation (6) prevents bounding the split-to-joined ratio by retaining a fixed-strength piece of common mass of this form and discarding the rest. In (4) the two retained fractions both vanish along diverging $\tau$ while their quotient tends to one. To use finite-strength pinning one needs the relative error between those small fractions.

## The opposite end at a strength uniform in the cutoff

**PROVED (approaching the gauge diagonal).** For even $t\ge2$, write $C_t(x,y)=K(x,y)^2/(K(x,x)K(y,y))$. Let $h=n^7$ and $0\le\beta\le B_0\log n$. Uniformly in this band and in $t$,
$$
  1-O_{B_0}\!\left(n^{-1/2}(\log n)^{3/2}\right)
       \le \frac{N[B_{n^7}]}{D[B_{n^7}]}\le1.                    \tag{7}
$$
This gives an endpoint at an explicit strength along the actual sequence of boxes.

**PROVED.** For $h\ge2$, restricting the vertex gauges to individual chordal balls of radius $h^{-1/2}$ about the identity gives $A_h(x,x)\ge\exp(hE-C E(1+\log h))$ uniformly in $x$. Each such ball has Haar mass at least $c h^{-3/2}$, and each transformed link moves a distance at most $2h^{-1/2}$. Also $A_h(x,x)\le e^{hE}$. Thus $B_h(x,y)\le\exp(-h d(x,y)^2/2+C E(1+\log h))$. If $|x_e-y_e|\le h^{-1/2}$ at every link, the same restriction in $A_h(x,y)$ gives $B_h(x,y)\ge\exp(-C E(1+\log h))$.

**PROVED.** Let $\ell_t(x)=K(x,x)/Z_t$. Changing a complete spatial slice in this periodic Wilson integral changes at most $3n^3$ spatial and $2E$ adjacent time plaquettes. Each term in the action changes by at most $2\beta$, uniformly in the integrated fields and the centre seam. Hence $\sup\ell_t/\inf\ell_t\le e^{C\beta E}$ and $\inf\ell_t\ge e^{-C\beta E}$ relative to probability Haar measure. Under the split law, given $X=x$, the preceding coordinate balls for $Y$ have probability at least $\exp[-CE(1+\beta+\log h)]$. Thus $D[B_h]/D[1]\ge\exp[-CE(1+\beta+\log h)]$. Comparing with the uniform upper bound on $B_h$ shows that under the normalized $D[B_h]$ law,
$$
 d(X,Y)^2\le C_1 E(1+\beta+\log h)/h
$$
except on a set of probability at most $\exp[-E(1+\beta+\log h)]$, with $C_1$ an absolute constant.

**PROVED.** In the positive Wilson integral for a half-slab, changing its first spatial face from $x$ to a gauge-minimizing representative of $y$ changes the first layer of temporal plaquettes by at most $a=\beta\sqrt E\,d(x,y)$ in the exponent. Each affected normalized trace is 1-Lipschitz in its one changed unit quaternion. The spatial half-action on the initial face contributes a scalar independent of the far end $z$. Independent gauge and centre projection preserve this comparison under positive integration. Consequently the two rows of $(P_0 T)^{t/2}$ evaluated at $z$ have ratio in $[c(x,y)e^{-a},c(x,y)e^a]$ for every $z$. The squared normalized $L^2(dz)$ inner product of those rows, namely $C_t$, is at least $e^{-4a}$. On the preceding event at $h=n^7$, $a\le C_{B_0} n^{-1/2}(\log n)^{3/2}$. Averaging $C_t$ on the pinned split law proves (7).

## The cost on the interval of small fixed strengths

**PROVED (a bound on the remainder under each Wilson law).** There are absolute $c,C,h_*>0$ such that for the physical periods above, all sufficiently late cutoffs in the logarithmic band and $0<h\le h_*$,
$$
 \mathbb E_i\left|\log B_h+
       \frac{h^4}{128}\sum_{p\ {\rm spatial}}(W_p(X)-W_p(Y))^2\right|
       \le \frac{C V h^6}{(1+\beta)^2},\qquad i=D,N.                \tag{8}
$$
The averaged remainder retains two powers of the inverse coupling even for a strength independent of the cutoff.

**PROVED (local coefficients).** Introduce independent complex strengths $z_e$ in $A$ and expand its logarithm through zero. The coefficient $f_{\mathbf k}(x,y)$ of $\prod_e z_e^{k_e}$, of total degree $m>0$, vanishes unless the support of $\mathbf k$ is connected. Indeed one may set all other strengths to zero before extracting this coefficient, and the gauge integrals over disjoint vertex sets factor. Its magnitude is at most $m C^m$ even when each of the link quaternions on the support is continued to complex coordinates of bounded norm, say at most $4$ in the complex Euclidean norm. Here quaternion conjugation of the real coordinates extends complex linearly. To see the bound, on the support alone repeat the deletion argument preceding (3), with bond terms $\exp(z_e u_e)-1$ bounded by $C_0|z_e|$. That argument needed only the bound and factorization on disjoint vertices for its zero-free disk. It gives $|\log A|\le Cm$ on an absolute polydisk. Multivariate Cauchy gives the stated estimate. There are at most $VC^m$ connected multi-indices of total degree $m$, by an edge traversal followed by the compositions of $m$ on the distinct edges. The coefficients are symmetric in $x,y$ and separately invariant under vertex gauges on real link configurations. These properties hold already with independent bond strengths.

**PROVED (two cancellations from gauge invariance).** If $m<n$, choose a spanning tree of the connected support. In each input make the tree links identity. Denote the other links by $\exp(\xi_e)$ on the first field and $\exp(\eta_e)$ on the second, choosing angles in $[0,\pi]$, and put $u=\max_e|\xi_e|$, $v=\max_e|\eta_e|$, with zero for an empty set. Write $f(s,r)$ for the coefficient evaluated with these angles multiplied by $s,r$. Conjugation of all links of the first field by the same group element leaves the coefficient unchanged, for every second field. The only rotation-invariant linear form on $\mathfrak{su}(2)$ is zero. Applied to each non-tree link at the identity this yields $\partial_s f(0,r)=0$. The same argument gives $\partial_r f(s,0)=0$. For real $s,r\in[0,1]$, Cauchy's derivative estimate on complex disks of radii $c/u,c/v$ gives
$$
 |\partial_s^2\partial_r^2f(s,r)|\le m C^m u^2v^2 .
$$
Indeed each link exponential stays bounded in complex norm on those disks, since its imaginary angle is bounded by $c$. If either maximum vanishes the mixed difference is zero. Integrating twice in each variable shows that $f(1,1)-f(0,1)-f(1,0)+f(0,0)$ has magnitude at most $m C^m u^2v^2$. In $f_{\mathbf k}(x,y)-[f_{\mathbf k}(x,x)+f_{\mathbf k}(y,y)]/2$ all terms depending on just one field cancel by symmetry. Its absolute value is therefore at most $m C^m(u^4+v^4)$.

**PROVED (Wilson expectation).** Each non-tree link so obtained is a closed word of length at most $m$ up to conjugation. It lifts to a closed walk on the cubic cover when $m<n$. Commuting adjacent coordinate steps to sort the three axes takes at most $m^2$ swaps, after which inverse pairs cancel. Each swap inserts a conjugate of an elementary plaquette or its inverse. Thus the chordal distance of the loop from the identity is bounded by a sum of at most $m^2$ chordal plaquette distances, with repetitions allowed. Angle is at most $\pi/2$ times chordal distance. The one-plaquette estimate used for (4) gives $\||1-U_p|\|_4\le C/\sqrt{1+\beta}$ on each face, since $|1-U_p|^2=2(1-W_p)$. Minkowski's inequality on each word and then summation over at most $m$ fourth powers give $\mathbb E_i(u^4+v^4)\le C m^9/(1+\beta)^2$. No independence is used. For $m\ge n$ use the field-uniform bound $m C^m$ instead. The resulting tail is bounded by $CV(Ch)^n$, which is at most $CVh^6/(1+\beta)^2$ after reducing $h_*$ and using the logarithmic band. Degrees below four, degree four and parity were computed in (3). Summing the bounds for $m\ge6$ proves (8).

**PROVED (two-sided cost).** Jensen's inequality, the one-plaquette second action moment and (8) give the lower bound below. The upper bound follows from (6) because $a(h)/h^4$ has a positive limit at zero by the single-bond character expansion. After decreasing $h_*$ both constants are uniform in the bounds
$$
 \exp\!\left[-C\frac{Vh^4}{(1+\beta)^2}\right]\le
       \mathbb E_i B_h\le
 \exp\!\left[-c\frac{Vh^4}{(1+\beta)^2}\right],\qquad i=D,N.       \tag{9}
$$
Furthermore, for every sequence $h>0$ tending to zero with $\beta\to\infty$, even when $Vh^4/\beta^2$ diverges arbitrarily fast, (8) and the spatial average in (4) give
$$
 \frac{\log B_h}{Vh^4/\beta^2}\ \longrightarrow\ -\frac{9}{512}
          \quad\hbox{in }L^1(\mathbb P_i),\qquad i=D,N.              \tag{10}
$$
The logarithm in (10) is taken before integration. An estimate for the ratio in (1) must also control the contribution of atypically large $B_h$ to each integral.

## A test at two different Wilson times

**PROVED (the signed response).** Write $J_t(h)=\log(N[B_h]/D[B_h])$ and let $\mathbb E_{i,h}$ mean expectation on the corresponding normalized pinned law. The finite-dimensional integrals are differentiable in $h$, with positive denominators. Hence for $0\le u<H$,
$$
 J_t(H)-J_t(u)=\int_u^H
  \left(\mathbb E_{N,h}\partial_h\log B_h-
        \mathbb E_{D,h}\partial_h\log B_h\right)dh.                 \tag{11}
$$
At physical time take $H=n^7$ and, if $\beta_j\to\infty$, take $u=(\beta^2\log\beta/(4V))^{1/4}$. One may always use $u=0$. Equations (4) and (7) say that (11) equals $-\log P+o(1)$. A limsup strictly below $\log(625/457)$ at one fixed admissible physical side would give the seed by (1). This is a condition on the same two-copy purity up to a vanishing error. Nothing in this identity reduces the required precision.

**PROVED (a diverging cost past fixed strength at another time).** Keep the same spatial cubes and Wilson couplings with $\beta\to\infty$. Take the comparison period $t'=2\lfloor\beta^\kappa\rfloor$, $0<\kappa<1/16$. For every fixed $u\in(0,h_*]$ the right side of (11), now at time $t'$ with $H=n^7$, equals
$$
 \left[\frac{\pi^2}{8}+o(1)\right]\frac{V}{(t')^3}.                 \tag{12}
$$
Indeed row 1373 (16), at copy order two, gives $-\log P=2G_{m,2}(t')$ with coefficient $2\pi^2(1-2^{-4})/15=\pi^2/8$. Its short-period Wilson comparison holds also for the neutral trace. The proof of (8) and the Jensen lower bound in (9) need only the one-plaquette exponential moment on the two periods. The ordinary half-tilt and neutral insertion bound of row 1373, (6) and the paragraph after it, still apply here, as in that row's short-period test (16) with $0<2\gamma<\kappa$. Thus each $\log\mathbb E_i B_u$ is $O(V/\beta^2)$ at this fixed strength. As $(t')^3/\beta^2\to0$, the entire contribution from $[0,u]$ is lower order. The uniform endpoint (7) gives (12). It is the same Wilson model in a time interval whose physical length tends to zero. The prescribed $t=2\lfloor n/1024\rfloor$ has a positive limiting physical duration. [Short-period trace, row 1373 (16)](gap-seed3-astra62.md) · [Wilson coefficient, row 1153](gap-solve6-astra62.md)

**OPEN.** At positive physical duration (11) is a difference of expectations on two *normalized* pinned Wilson measures. Bounds (8)–(10) estimate the individual pinning costs. Even two-sided estimates of order $Vh^4/(1+\beta)^2$ at every fixed small $h$ leave an error growing with $V$ in their difference. Equation (12) shows that an upper bound independent of the duration on the entire interval beyond a fixed small strength would already fail on these same spatial cutoffs. It does not give the sign or size of (11) at the requested duration.

## A normalized observation of the gauge orbit

**GUIDE.** To avoid dividing tiny pinning fractions, use the auxiliary integral as an actual conditional probability. Given a spatial configuration $x$ let the reported face $z$ have density $q_x^h(z)=A_h(x,z)/M(h)^E$ with respect to product Haar. Equivalently, apply independent electric bond noise and a uniformly random vertex gauge. Every conditional density integrates to one. The question becomes whether a full noisy face can reveal its input and still predict the half-slab state at physical time. Row 1371 used Gaussian observations of two electric cuts and the information and estimation identity of Guo, Shamai and Verdú. Here the observations are on one face modulo its independent vertex gauges. [Earlier Gaussian observation](gap-seed2-astra62.md)

**PROVED (the relative entropy of noisy faces).** Let $S_h(x,y)=D_{\rm KL}(q_x^h\Vert q_y^h)+D_{\rm KL}(q_y^h\Vert q_x^h)$. For $0<h\le h_*$, with $h_*$ reduced by an absolute factor if needed, the following bound holds under either face law in (1).
$$
 \mathbb E_i\left| S_h(X,Y)-
 \frac{h^4 r_2(h)^4}{64}
             \sum_p(W_p(X)-W_p(Y))^2\right|
 \le \frac{C V h^{10}}{(1+\beta)^2}.                               \tag{13}
$$
In particular the input and output of this full-face channel have mutual information at most $CVh^8/(1+\beta)^2$ for the actual input marginal $\ell_t$. The two small parameters in this estimate have different origins. The first nonconstant term in the logarithm of the observation density is a square, and passage through the channel damps the fundamental character on each of its four edges.

**PROVED.** Write $U_u f(a)=\int q_a^u(z)f(z)\,dz$. The symmetrized entropy is $(U_h f)(x)-(U_h f)(y)$ for $f=\log q_x^h-\log q_y^h$. At fourth degree in this logarithm the coefficient from (3), before subtracting diagonal terms, is $\sum_p W_p(x)W_p(z)/64$. The central single-bond convolution acts on the fundamental matrix coefficients by $r_2(u)$, hence $U_u W_p=r_2(u)^4 W_p$. This gives the principal term in (13) exactly.

**PROVED.** For a multi-index of degree $m\ge6$ in $\log q_b^h(z)$ write its coefficient as $f_{\mathbf k}(b,z)$. The independent-bond normalization is a sum of one-bond logarithms independent of $b,z$ and cancels in the entropy. For this coefficient it suffices to integrate $z$ on its connected support $\Gamma$. Introduce a separate channel strength $u$ there. Because $f_{\mathbf k}$ is gauge invariant in $z$, $H_u(a,b)=\big(U_u f_{\mathbf k}(b,\cdot)\big)(a)$ can be evaluated by independent normalized bonds on $\Gamma$ without the final random gauge. The Taylor coefficient of $u^l$ in $H_u$ is bounded by $mC^{m+l}$ on the same complex domains for $a,b$ used in (8). Indeed the product of the normalized bond densities on this absolute $u$ disk has modulus at most $C^m$, and the output variables are integrated over real Haar measure. This coefficient is separately gauge invariant in the two real inputs. In degrees $l<4$ it is independent of $a$. To see this, gauge average the normalized bond product before the output integration. Each nonconstant bond term $e^{u a_e\cdot(gz)_e}/M(u)-1$ averages to zero at a free endpoint. Nonempty surviving supports have at least four distinct edges. This holds on $\Gamma$ as well.

**PROVED.** In the symmetrized entropy the combination of the four coefficients is $H(x,x)+H(y,y)-H(x,y)-H(y,x)$. Its one-input terms cancel even without symmetry of $H$. For $m<n$ apply the two angle expansions and the plaquette word bound in (8) to the remaining mixed term in each of these four evaluations. The expected absolute value is at most $m^{10} C^{m+l}/(1+\beta)^2$. For $m\ge n$ there is the geometric winding tail as in (8). Summing over supports and over $m\ge6$, $l\ge4$ at $u=h$ gives (13). Odd degrees of the logarithm vanish by bipartiteness. For independent $X,Y\sim\ell_t$ convexity of relative entropy in the second density gives $I(X;Z)\le\mathbb E D_{\rm KL}(q_X^h\Vert q_Y^h)=\mathbb E S_h(X,Y)/2$. The second moment from (4) gives the claimed uniform bound. More precisely, if $h\to0$ and $\beta\to\infty$, the ratio $\mathbb E_i S_h/(Vh^8/\beta^2)$ tends to $9/65536$, by $r_2(h)/h\to1/4$ and the mean $9/4$ in (4).

**PROVED (single-square check of the coefficient).** On an isolated square the character formula in (5) gives the output density $\sum_{d\ge1}r_d^4\chi_d(x_p)\chi_d(z_p)$. Under product Haar, $z_p$ is Haar and $\mathbb E W_p(z)^2=1/4$. The first correction to density one is $4r_2^4 W_p(x)W_p(z)$. Expanding the symmetrized relative entropy for two such densities gives leading term $4r_2^8(W_p(x)-W_p(y))^2$. Its coefficient of $h^8$ is $1/16384$, agreeing with (13) by direct character orthogonality.

**PROVED (one response with bounded normalization).** Put $k=(P_0T)^{t/2}$, $\psi_x=k(x,\cdot)/\sqrt{K(x,x)}$ and $Q_x=|\psi_x\rangle\langle\psi_x|$. For $X\sim\ell_t$ and $Z$ drawn from $q_X^h$, let $R_t(h)=\inf_M\mathbb E\|Q_X-M(Z)\|_{\rm HS}^2$, where the infimum is over measurable Hilbert–Schmidt operators depending on the report. The optimizer is the conditional mean. Gluing gives $\mathbb E Q_X=K/Z_t$ and $\|\mathbb E Q_X\|_{\rm HS}^2=P$. Orthogonal projection onto the conditional mean gives
$$
  0\le 1-P-R_t(h)\le 2I(X;Z)
      \le \frac{CVh^8}{(1+\beta)^2}\qquad(0<h\le h_*).             \tag{14}
$$
Indeed every $Q_x$ has Hilbert–Schmidt norm one. The squared distance between its posterior and prior means is at most four times the squared total variation distance between the corresponding laws of $X$, bounded by twice the posterior relative entropy by Pinsker's inequality. Integrate over $Z$. No small probability conditions this estimate.

**PROVED (the resolved face).** For $h\ge1$ and every even $t\ge2$ the same experiment satisfies
$$
       R_t(h)\le C\beta E/h.                                        \tag{15}
$$
To prove it, use $Q_Z$ as a predictor and put $v_x=k(x,\cdot)/\sqrt{Z_t}$. For unit vectors of positive inner product the squared distance of their projectors is at most twice their squared vector distance. Also $\|v_x\|\|\psi_x-\psi_z\|\le2\|v_x-v_z\|$ by the reverse triangle inequality. Since $\ell_t(x)=\|v_x\|^2$, the trial loss is bounded by $8\int dx\,q_x^h(z)dz\,\|v_x-v_z\|^2$. The output gauge can be removed because $v$ is gauge invariant. The independent noise increments have mean-zero principal logs in the Lie algebra, with second moment at most $C/h$. This follows in angular coordinates from $1-\cos\theta\ge 2\theta^2/\pi^2$, the measure factor $\sin^2\theta$ and the lower bound on $M(h)$ in (6). Integrate the derivative of $v$ along the product of the exponential paths from $x$ to the noised configuration. After Cauchy–Schwarz in the path parameter and a Haar change of the base point, independence and centering of the log directions remove the cross terms. This bounds the trial loss by $C h^{-1}\int\|\nabla v_x\|^2 dx$, with the sum over all links and the round metric on each unit $S^3$.

**PROVED.** For fixed far endpoint $z'$, $\Delta_x\log k(x,z')\ge-C\beta E$, where $\Delta$ is the product Laplacian with nonpositive spectrum. In each positive half-slab integral, each initial spatial or temporal plaquette containing a given first-slice link is linear in that unit quaternion. Applying its link Laplacian to the normalized trace multiplies it by $-3$. There are boundedly many such plaquettes per link. Differentiating the logarithm under the integral adds a nonnegative summed variance of the gradients to the mean Laplacian of the exponent. These statements apply also to the centre average. Integration by parts with $k^2$ gives $\int|\nabla_x k|^2 dx=-\tfrac12\int k^2\Delta_x\log k\,dx$. Integrate in $z'$ and divide by $Z_t$ to get $\int\|\nabla v_x\|^2 dx\le C\beta E$. This proves (15). The variation of the normalized direction of $v_x$ has the exact duration-dependent expression
$$
 \int\ell_t(x)\|\nabla Q_x\|_{\rm HS}^2 dx
   =2\,\mathbb E_{\ell_t}\sum_e
       {\rm Var}_{z'\mid X}\!\left(\nabla_e\log k(X,z')\right),       \tag{16}
$$
where the conditional density is $k(X,z')^2/K(X,X)$ and the vector variance is the mean squared Euclidean deviation. Differentiate $k(x,\cdot)/\|k(x,\cdot)\|$ to subtract the conditional mean score. Differentiating its rank-one projector multiplies the squared norm by two. The spatial half-action cancels from this variance. The remaining term measures how the conditional temporal boundary force depends on the far endpoint.

**OPEN (the physical duration).** If $Vh^8/(1+\beta)^2\to0$, (14) identifies the best prediction error with $1-P+o(1)$. A predictor with limsup error strictly below $168/625$ at the prescribed $t$ and one fixed physical $L$ would prove the seed. At that noise level, optimizing over all predictors is equivalent, up to a vanishing error, to the same purity test. The explicit predictor in (15) controls the other end, $h\gg\beta E$. The two ranges are disjoint in the allowed band. At the comparison period of (12) the optimal error at the weak end tends to one because $P\to0$. To reach a different conclusion at physical time requires an estimate that uses how the normalized half-slab state changes with its boundary condition across that duration. The uniform bound on the score used in (15) supplies no such decay.

**GUIDE (scope).** These are analytic finite-lattice arguments. They use the cited Wilson moment and short-period estimates as inputs. No computation supplies a proof step. The new estimates have received no independent check in this row.

RESULT: OPEN. The whole-face pin has the same weak-strength response on the two Wilson covers, and (13) bounds the information in a normalized observation of the entire face. At a fixed admissible physical side the relative mass of the two covers at the required time remains uncontrolled. Neither the one-box neutral seed nor a counterexample to it or to the checked implication has been established.
