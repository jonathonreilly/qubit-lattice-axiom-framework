## Repo search

**ON FILE (row 1650, research draft).** The checkout is `1a3b5d019eb7`. I searched Markdown and TeX on `origin/main`, `pr/10114`, `pr/10133`, `pr/10134` and `pr/10141` in the designated Physics repository. The exact terms `(PUR-io)`, `(VIR-down)`, `(K-II)` and “order-one renormalization / RG step” gave no hits. Searches included potential-moving decimation, plaquette-character expansion, spin-foam blocking, theta graphs, four parallel ribbons, Möbius inversion on plaquettes, and a magnetic disk on winding cylinders. A separate search of this checkout outside the lane found no matching target.

- **ON FILE (repo search, rows 697, 701, 708).** Main's `research/mass-gap/ROWS.md` records the doubling defect and thermal transport. In the corresponding lane note `gap-seed-sc.md`, Proposition 4.4 counts $3n^3$ spatial squares in a fixed time direction, each giving a tube of order $4v$ at period $v$. This is a winding surface and an earlier consumer. It does not estimate an order-one blocking step.
- **ON FILE (repo search, rows 531, 1341).** On the soft PRs, `MASS_GAP_LOCAL_BLOCK_ASTRA.md` keeps the exterior convolution and proves $C_F(a)\ge v_N^2 e^{-4\beta(p_B+b)}/(1+v_N/r_f(\beta)^b)>0$ for a centered local loop, uniformly in spatial volume (its (11)). This concerns a one-step correlation. Main's `gauge-plaquette-spatial-env-character-20260710/ROUTE_PORTFOLIO.md` lists a deferred recoupled tensor calculation. `docs/SU3_WILSON_CLOSED_FORM_FANOUT_THEOREM_NOTE_2026-05-04.md` gives an isolated SU(3) plaquette average. None gives the connected weight of several winding SU(2) cylinders. The November 8 memo concerns PI/GW and history admission. Row 1650 has no additional “Repo prior work” hits. Its target-specific prior file is absent.
- **ON FILE (rows 701, 1025, 1105, 1341, 1390, 1418, 1468).** In the lane, `gap-face-exercise-check-opus.md` already uses three cylinders on a theta graph to exhibit a nonzero integer-spin activity. Row 1341 integrates the eight spokes of a Wilson block and computes its triangular marginal. Rows 1025 and 1390 show why separate potential-moving bounds miss the ratio. Row 1418 contracts spin intertwiners. Row 1468 gives exact twist-wise mass transport and the seed consumer. I use character sewing and the two-period consumer from these rows. The target below is the *connected logarithmic weight* of four winding ribbons after all proper supports have been subtracted, and what becomes of those weights when plaquettes are grouped.
## Prior estimates and the remaining question

**ON FILE (rows 1386, 1553, 1600–1649).** The registry entries VIR-DOWN, WMIX-SLICE and LEV-FAIL respectively record an open band rate, a whole-slice equivalence and a refuted level bound. Row 1641 is a FINISH record without a separate note. Rows 1610/1613 give thermal transport, 1630 requires its rate on the whole cold characteristic, and 1648 identifies the magnetic deficit with the same rate up to the stated anisotropy error. Row 1649's reduction to K-II is a judgement. The literature readings in rows 1545, 1604 and 1645 give, respectively, a weak-coupling RG, mixing outside the requested gauge regime, and identities for action differences without the required sign. None of these supplies a joint winding-weight estimate.

**ON FILE (SA index, rows 244, 1545).** Chunk 01 at 396–413 and 588–599, the neighbouring obligations, and the 4.12–4.19 index, chunk 11 at 56361–56378, 56414–56417 and 56532–56549, point to the relevant source statements. In the outline, preserving mass alone gives no control of a chosen block observable. In CA-I the increment inputs have unfinished steps, no individual step sign is asserted, and the quoted Bałaban theorem assumes all effective couplings at most a small ceiling. Credit Ethan Sussman and Levent Alpoge, with Claude and Codex, for the outline and account. I use no order-one estimate from them.

**PROVED below by hand.** Five four-ribbon supports and one six-ribbon support block to the same set. Their leading SU(2) weights cancel. An exterior of arbitrary volume coupled through one spatial cycle still gives a uniform bound at order-one Wilson coupling. For circle Wilson the ratio of the absolute signed sum to the sum of absolute weights tends to $5/11$. Section “One magnetic attachment, worked out” gives the scope of the exterior bound.

## Proposed block variable

**ARGUED (choice of route).** Keep a partition function for each subset of active blocks, with the same underlying Wilson fields and couplings. Passing to a coarser mesh sums signed connected weights before an absolute value is taken. A tractable first question is whether the connected winding contributions already have a fixed sign on the smallest graph with four parallel paths. The answer determines whether a sign can be discarded in this part of the step. The target remains the eight-twist neutral trace at both periods.

**ON FILE (rows 701 and 1105, check 1105 at lines 708–720).** The single square tube and the three-cylinder spin-one example already use electric character propagation and Haar integration at both ends. Searches on the five refs and in the lane for a four- or six-ribbon connected weight, a Polyakov character sixth cumulant, and Möbius grouping of winding cylinders gave no matching proof. The result developed below uses *both* junctions and subtracts *every proper plaquette subset* at positive coupling. The basic character eigenvalues are SA outline GL3–GL4 at 2197–2239, indexed in chunk 02 at 2210–2239.

### The exact map

**PROVED (block map and grouping rule).** Use probability Haar measure. Divide each Wilson plaquette weight by its one-plaquette Haar integral. This changes the full masses by the same factor per plaquette and cancels exactly between the two periods in the purity. At level zero label a plaquette by its base point and its unordered pair of axes, with positive orientation fixed once. For a subset $D$ of labels on a box $T$, let $Z_T^z(D)$ be the integral with just these plaquettes active and with temporal twist $z$. Define

$$
 f_T^z(D)=\log Z_T^z(D),\qquad
 a_T^z(A)=\sum_{D\subseteq A}(-1)^{|A|-|D|}f_T^z(D).
 \tag{1}
$$

Take $B=b^h\ge32$, with the least fixed $h\ge1$ for which this holds. For a $B$ step let $q$ divide every base-point coordinate by $B$ with integer floor, preserving the pair of axes. The new theory is a family of finite measures on coarse gauge fields indexed by enabled coarse plaquette sources. At mask $D'$ use the fine theory at $q^{-1}D'$ and push it forward by the ordered product of fine links along each straight coarse bond. One may work in the twisted-period covering coordinates with the centre cut aligned at a block boundary. A spatial straight path crossing the cut acquires exactly its prescribed centre sign. Gauge transformations telescope to transformations at coarse vertices. These facts define the map on each twist and rectangle. No Wilson parametrization or truncation of the image is needed. The source family and its normalization are part of the coarse theory. The map is exact for any positive input family, including at order-one coupling.

In particular $f'(D')=f(q^{-1}D')$. Boolean inversion of (1) gives $f(D)=\sum_{A\subseteq D}a(A)$, since the alternating sum over the interval between two unequal subsets vanishes. Substitution and collection by image give
$$
                 a'(H)=\sum_{qA=H}a(A).                                      \tag{2}
$$
This equality is for a fixed twist and volume. The same construction with factor $b$ gives the entry map. Straight paths identify the coarse fields. The estimates below read source-dependent masses and require no long thin Wilson loop to approximate a continuum observable.

### A sufficient estimate and its budget

**GUESSED (the order-one estimate).** Fix $\ell_0$ a multiple of $4096$, and put $m=\ell_0/512\ge8$. For an integer $M\ge1$ take $\ell=\ell_0 B^M$. Apply $K$ entry steps of side $b$, then $M$ steps of side $B$. The last temporal period is $m$ or $2m$. Call a final support long if its time base points do not fit in $\lfloor m/4\rfloor$ consecutive cyclic slices. At each earlier level call a support long if its image on this same final clock is long. Thus long supports are unions of whole fibres of the map on supports. Both periods use the same short-length threshold. Write $V_j(T,z)$ for the sum of $|a_j^z(A)|$ over long supports after $j$ of the $B$ steps, $j=0$ denoting entry.

The proposed input is the following. Fix the release witnesses and $\ell_0$. Choose $C<\infty$, $0<\delta<1$ independent of $M,K$. For each fixed $M$ large enough there is an infinite set of $K$ on which the following hold on both periods and all eight twists.
1. At the chosen order-one entry mesh $V_0(T,z)\le C$.
2. At every active $B$ step and for each long coarse support $H$, form disjoint groups of fine supports in the fibre $qA=H$, leaving unmatched supports as singletons. In a group $g$ put $P_g=\sum_{A\in g}(a_j(A))_+$ and $N_g=\sum_{A\in g}(-a_j(A))_+$. Require the estimate
$$
              2\sum_{H\ {\rm long}}\ \sum_{g\ {\rm over}\ H}\min(P_g,N_g)
                    \ \ge\ \delta\, V_j(T,z).                                \tag{3}
$$
The proposed way to prove (3) is by explicit local replacements of occupied plaquette sets with the same coarse image. Sections below give such groups with mixed spatial and temporal plaquettes. For a proof one needs a fraction of the *weight*, including configurations meeting other active cells, at the actual blocked couplings. Merely counting all available replacements gives no such fraction. Taking one group per fibre gives the strongest possible cancellation for this grouping rule.

**PROVED (consumer, conditional on these two inputs).** The triangle inequality applied only *after* the signed group sums gives $V_{j+1}\le V_j-2\sum_g\min(P_g,N_g)\le(1-\delta)V_j$. Choose $M$ first with $C(1-\delta)^M\le1/12$. Keep this one $\ell$ fixed on its infinite set of cutoffs. At the final mesh the total short-support contribution is independent of $z$ and doubles when the time period doubles. To see this, lift a nonempty short support into its time arc and lift the entire underlying enabled fine plaquette set. That set sees at most one additional fine time slice at its far boundary and fits in a proper cylinder. One can place the twist seam outside it by a centre change on a stack of spatial links between two time cuts. All its subset integrals then agree with their untwisted copies. The short arc has length less than half the shorter circle, so the lift of all its time coordinates is unique up to translation by a period (lift relative to any one coordinate by the unique shortest difference). Each short support at period $m$ has exactly two short lifts at $2m$, including supports with disjoint spatial pieces. Conversely each short support at $2m$ projects to one at $m$. The unused Haar variables have mass one. The same statements hold for (1). The empty coefficient is zero.

Consequently there is a real $s$ such that $\log Z^z(u)\in[s-\epsilon,s+\epsilon]$ and $\log Z^z(2u)\in[2s-\epsilon,2s+\epsilon]$, where $\epsilon=1/12$ is valid for every $z$. Averaging the positive masses preserves both exponential bounds. Hence
$$
 \frac{Z_+(2u)}{Z_+(u)^2}\ge e^{-3\epsilon}\ge1-3\epsilon=\frac34>\frac{457}{625}. \tag{4}
$$
This feeds Fact PUR of row 1468, §3.1, at its original aspect and with its original neutral projection. One may stop requiring (3) on any period and twist as soon as $V_j\le1/12$, since (2) makes the filtered absolute sum nonincreasing. The implication uses neither (HOT) nor a comparison of two bare couplings. No estimate in (3) follows from (2) alone.

**GUESSED (location of the window).** The index $K$ in the entry convention above labels a scale. It does not determine the effective coupling there. An operational version allows a fixed extra $s\ge0$ entry steps, uses $R=b^{K+s}$ fine spacings and replaces $\ell$ by $\ell_0 b^s B^M$. All subsequent periods and (4) are unchanged. For example, use the square-loop Creutz ratio of row 720, Q8, on the ordinary full torus. For $W(i,j)$ the mean normalized trace of a fixed spatial rectangular Wilson loop, use the readout
$$
 -R^2\log\!\left(\frac{W(R+1,R+1)W(R,R)}{W(R+1,R)W(R,R+1)}\right).
$$
An explicit order-one entry test is that the four expectations are positive and this readout lies in $[1/4,4]$ on the subsequence. This is a scheme choice. Its realization, the entry bound, and (3) through the ensuing scales are separate open inputs. A bare $\beta$ between 2 and 3 on an isolated block tests part of the construction. It cannot establish any of these inputs for the calibrated image.

## A signed component of the step

**PROVED (exact ribbon coefficient on the Wilson lattice).** Let $p,q$ be distinct spatial sites. Take $k$ internally disjoint spatial paths between them inside a spatial ball. Multiply each path by the full time circle of length $v$ to obtain a plaquette cylinder. Denote these sheets by $S_i$. One may replace interior faces by embedded cubical disk patches, provided each sheet remains an annulus, sheets meet only at the two boundary circles, and every nonboundary edge of a sheet belongs only to that sheet and to precisely two of its faces. Let $a_i=|S_i|$. For $J\subseteq[k]$ set $A_J=\bigcup_{i\in J}S_i$. Then the coefficient (1) of $A_{[k]}$ on the *full* isotropic Wilson lattice, with any temporal twist, is
$$
 c_k(a_1,\ldots,a_k)=\sum_{J\subseteq[k]}(-1)^{k-|J|}
 \log\int dg\,dh\prod_{i\in J} K_{a_i}(g,h),                               \tag{5}
$$
where
$$
 K_a(g,h)=\sum_{\lambda}r_\lambda^{\,a}\chi_\lambda(g)\overline{\chi_\lambda(h)}.
 \tag{6}
$$
The $r_\lambda$ are the scalar convolution eigenvalues of the *normalized* Wilson plaquette density, including $r_0=1$. These are coefficients of the actual source family. No assertion of independence under the unmasked full measure is made.

**Proof.** In a partially occupied sheet, start at a missing face. Every remaining face reachable from the hole across interior edges can be peeled by integrating the newly free link. Each such integral is one with all the other links fixed. The dual graph of faces across nonboundary edges of each annulus used here is connected. Thus the entire incomplete sheet disappears without pricing the junction holonomies. Group the terms of (1) by their complete sheets. The alternating weight of all proper subsets of a given sheet is $-1$, since the alternating sum over all subsets is zero and the full one has weight one.

For a complete sheet the elementary disk sewing rule integrates across a shared edge with Haar convolution. In irreducible matrices this uses $\int D^\lambda_{ab}(x)\overline{D^\mu_{cd}(x)}\,dx=\mathbf1_{\lambda=\mu}\delta_{ac}\delta_{bd}/d_\lambda$. It follows by averaging a matrix unit over the group, obtaining the intertwiner and fixing its scalar by its trace. On a disk, glue along a dual spanning tree of faces. The result has one boundary word with normalized central convolution power $w^{*a}$, whose character coefficients are $d_\lambda r_\lambda^a$. One can first fix the links complementary to these merges by Haar translations at the interior vertices. After contracting the boundary to a root, the unused interior edges contain no cycle. Such a cycle would separate faces that the dual spanning tree connects without crossing it. The number of unused edges equals the number of interior vertices by Euler's formula, so they form a tree to the root. Fixing their values to one changes no remaining integral. Cutting the annulus open on a path from one boundary to the other leaves the relative parallel transport $x$ along this cut. In the resulting disk formula its boundary word is $gxh^{-1}x^{-1}$ up to conjugacy and orientation. Haar integration of $x$ yields $\chi_\lambda(g)\overline{\chi_\lambda(h)}/d_\lambda$, giving (6). Alternatively, on a straight sheet each time column carries one spin after spatial-link integration and at every interior spatial vertex the two end characters sew by orthogonality. Replacing one face by a disk inserts its convolution power. This is the cylinder sewing of row 1105 with arbitrary spins and areas. The two common boundary circles have independent Haar holonomies before the strip factors are inserted. The centre seam may be placed outside the entire spatial ball. This proves (5).

**PROVED (uniform long-cylinder asymptotic).** Use the nonnegative integer $j$ equal to twice the SU(2) spin. On the circle $r_j$ is the eigenvalue at either charge $\pm j$. With $I_j=I_j(\beta)$,
$$
 r_j=I_{j+1}/I_1\quad\text{for SU(2)},\qquad
 r_j=I_j/I_0\quad\text{for U(1)}.
$$
The first formula is GL3 of the outline. For the second, the Fourier coefficient of $e^{\beta\cos\theta}$ follows by expanding the two exponentials in $e^{\pm i\theta}$. Put $Q=I_1/I_0$ and $a_*=\min_i a_i$. For $k=4,6$ and $Q^{a_*}$ sufficiently small,
$$
 \frac{c_k(a_1,\ldots,a_k)}{r_1^{\sum_i a_i}}=
 \begin{cases}
  1+O(Q^{a_*}),\quad -5+O(Q^{a_*}) &\text{SU(2), respectively},\\
  -6+O(Q^{a_*}),\quad 80+O(Q^{a_*}) &\text{U(1), respectively}.
 \end{cases}                                                               \tag{7}
$$
The constants for each $k$ are absolute. In particular the error tends uniformly to zero for $\beta\in[2,3]$ as $a_*\to\infty$, and also whenever $a_*/(1+\beta)^{3/2}\to\infty$.

**Proof of the error bound.** For $j\ge0$ the adjacent quotient $I_{j+1}/I_j$ is the mean of $t$ in density proportional to $e^{\beta t}(1-t^2)^{j-1/2}$ on $(-1,1)$. For example the integral representation for $I_j$ follows by expanding the exponential, integrating the even powers by the beta integral, and comparing to the GL3 series. Differentiation gives the stated mean using $I'_j=I_{j+1}+jI_j/\beta$, also directly from that series. Conditional on $|t|=s$ the mean is $s\tanh(\beta s)$, increasing in $s$. Passing from $j$ to $j+1$ tilts the $s$-law by $1-s^2$, decreasing in $s$. Pairing two iid draws shows that the covariance of an increasing and a decreasing function is nonpositive. Hence $r_1\le Q<1$ and $r_j/r_1\le Q^{j-1}$ for $j\ge1$. Moreover $1-Q\ge c(1+\beta)^{-3/2}$ with a universal $c>0$. In the circle integral for $1-Q$ use the interval $[(1+\beta)^{-1/2},2(1+\beta)^{-1/2}]$, where $e^{\beta(\cos\theta-1)}\ge e^{-2}$ and $1-\cos\theta\ge2\theta^2/\pi^2$, and bound the denominator by $2\pi$. This proves both uniformity assertions.

Set $x_i=r_1^{a_i}$. With two independent Haar endpoints the $i$th factor in (6) has the form $1+x_iY_i$, where
$$
 Y_i=Y+O(Q^{a_*})\quad\text{in supremum norm},\qquad
 Y=\begin{cases}
 \chi_1(g)\chi_1(h)&\text{SU(2), index 1 means spin }1/2,\\
 2\cos(\theta_g-\theta_h)&\text{U(1)} .
 \end{cases}
$$
Indeed the SU(2) remainder divided by $x_i$ is bounded by $\sum_{j\ge2}(j+1)^2(Q^{a_i})^{j-1}$, and the circle remainder by $2\sum_{j\ge2}(Q^{a_i})^{j-1}$. Both are bounded by a fixed multiple of $Q^{a_*}$ when $Q^{a_*}\le1/2$.

For completeness take $L$ a common bound for $1+\|Y_i\|_\infty$ in this range and $\rho=(100L)^{-1}$. On $|z_i|\le\rho$, $\mathbb E\prod_i(1+z_iY_i)$ differs from one by at most $(1+1/100)^6-1<1/2$. Its logarithm has a convergent series with coefficients bounded by $(\log2)\rho^{-|\alpha|}$ by the power series for $\log$ and Cauchy's integral formula. The alternating sum (5) selects exactly the terms using every index. After dividing by $\prod x_i$, the terms of degree greater than $k$ have total absolute value $O(\max_i x_i)$, by summing the product of $k$ geometric series for $\max_i x_i<\rho/2$. The coefficient using every index once is the joint cumulant
$$
 \sum_{\pi}(-1)^{|\pi|-1}(|\pi|-1)!\prod_{D\in\pi}\mathbb E\prod_{i\in D}Y_i ,
$$
by grouping the logarithm series into set partitions $\pi$. Replacing all $Y_i$ by $Y$ costs $O(Q^{a_*})$ in this finite polynomial. Odd moments of $Y$ vanish. For SU(2) the Haar moments of $2\cos\theta$ in degrees $2,4,6$ follow by integrating against $2\sin^2\theta/\pi$ on $[0,\pi]$, taking the constant Fourier coefficient minus the coefficient at frequency two of $(2\cos\theta)^{2s}$. This gives $\binom{2s}{s}-\binom{2s}{s-1}$, or $1,2,5$. The independent endpoints square these values to $1,4,25$. On the circle the corresponding moments are the constant coefficients $\binom{2s}{s}$, hence $2,6,20$. The fourth cumulant is $m_4-3m_2^2$ and the sixth is $m_6-15m_4m_2+30m_2^3$. Substitution gives (7). This is a hand proof, including the arithmetic.

### An explicit cancellation inside one coarse support

**PROVED (five four-path supports against one six-path support).** Work inside one spatial $B$-cell. Translate the following coordinates into its interior. Write $p=(0,0,0)$ and $q=(4,0,0)$. All configurations include the straight path between them. An offset rail first walks in the transverse plane at $x=0$, then travels four steps parallel to $x$, then reverses the transverse walk at $x=4$.

- In the six-path configuration use the direct path and the four rails at offsets $\pm2e_y,\pm2e_z$. The final path goes from $p$ to $(-1,0,0)$, then to $(-1,1,0)$ and $(-1,1,1)$, crosses to $(5,1,1)$, and returns through $(5,1,0),(5,0,0)$ to $q$. The lengths are $4,8,8,8,8,12$.
- In each four-path configuration use the direct path, the two rails at $\pm2e_y$, and a rail reached by $12-i$ positive $z$ steps followed by $i$ positive $y$ steps, $i=0,1,2,3,4$. The lengths are $4,8,8,28$. These are five distinct supports, each with the same total length 48 as the six-path support.

The path interiors in each individual graph are disjoint. In particular the sixth path passes the other longitudinal rails at a different transverse coordinate. Sweep the graph through the time circle. For *all six* configurations choose the same subset $E$ of the slots $t=0,2,\ldots,2\lfloor v/2\rfloor-2$. At each chosen slot replace the $tx$ plaquette on the direct edge from $(2,0,0)$ to $(3,0,0)$ by the other five faces of its unit $txy$ cube on the positive $y$ side. The displaced edge is at $y=1,z=0$, clear of the remaining paths, and successive disks are separated by at least one unused time step. These are sheets of the kind in (5), with direct area $a_0=4v+4|E|$, total area $48v+4|E|$, and every other area at least $8v$. Thus nonempty $E$ introduces genuine spatial Wilson plaquettes.

Denote the six supports by $\mathcal G(E)$. With coordinates translated as above, every one uses the same coarse spatial cell, all coarse time slices and all three temporal-spatial orientations. The added spatial orientation $xy$ has exactly the same coarse time labels in all six. Therefore $qA$ is *identical* for $A\in\mathcal G(E)$, including after further blocking. The supports in different groups are distinct because the set of removed direct plaquettes recovers $E$. At either consumer period these are long supports. Put $w(E)=r_1^{48v+4|E|}$. Equation (7) proves, uniformly in $E$,
$$
 \begin{array}{c|cc}
 & w(E)^{-1}\sum_{A\in\mathcal G(E)}a(A) &
 w(E)^{-1}\sum_{A\in\mathcal G(E)}|a(A)|\\ \hline
 {\rm SU}(2) & O(Q^{4v}) & 10+O(Q^{4v})\\
 {\rm U}(1)  & 50+O(Q^{4v}) &110+O(Q^{4v}).
 \end{array}                                                               \tag{8}
$$
This is a calculation of terms in the actual map (2). In particular the group removes an asymptotic fraction one of its incoming SU(2) absolute weight. For circle Wilson it removes $6/11$ and leaves $5/11$. A requirement that the signed remainder of this group be at most one quarter of its absolute weight succeeds for SU(2) and fails for weak U(1) at these large periods. The same one-quarter comparison also fails for strong-coupling U(1) at fixed positive $\beta$ and sufficiently large $v$. This limits its use as a phase test.

**PROVED (price of taking absolute values first).** The sum of $w(E)$ over all choices is exactly
$$
          r_1^{48v}(1+r_1^4)^{\lfloor v/2\rfloor}.                         \tag{9}
$$
Along the calibrated raw sequence $\beta_K\asymp\log n$, $v=u$ or $2u$, the limit of its log divided by $v$ is $(\log2)/2$. Indeed $r_1\to1$ because the one-plaquette Wilson probability concentrates at the identity. Outside any fixed identity neighbourhood its cosine exponent is separated from its maximum, and a smaller neighbourhood of positive Haar mass gives the denominator bound. Equation (7) applies uniformly here. Even inside one fixed spatial cell, the sum of absolute long raw coefficients therefore grows exponentially in $v$. This is an obstruction to using the entry bound at the bare mesh with no signed grouping. The entropy test by decorating a surface and the unbranched surface weights have precedents in rows 811/816, 838 and 1418. The branches, the logarithmic subtraction, and the opposite signs in the *same* fibre are essential to (8).

### What survives this cancellation

**PROVED (residual on the calibrated sequence).** For SU(2), uniformly in $E$ as $v\to\infty$, both uniformly on $\beta\in[2,3]$ and along $\beta_K\asymp\log n$,
$$
         \sum_{A\in\mathcal G(E)}a(A)
           =\bigl(30+o(1)\bigr)\,w(E)\,r_1^{2a_0}.                         \tag{10}
$$
Thus the exhibited relative gain is real, but even summing *all these groups with their signs* leaves a contribution whose logarithm divided by $v$ tends to $(\log2)/2$ on the raw calibrated sequence. A further class of supports must participate if the total grouped weight there is to stay bounded.

**Proof.** Write $q_j=I_{j+1}/I_j$. The strict covariance argument above gives $q_2<q_1=r_1$. Along $\beta\to\infty$, $\beta(1-q_j)\to j+1/2$ for $j=1,2$. In the integral for the mean of $t$, set $s=\beta(1-t)$. The expectation of $s$ becomes the ratio of integrals against $s^{j-1/2}(2-s/\beta)^{j-1/2}e^{-s}\mathbf1_{[0,2\beta]}(s)$. Dominated convergence in both integrals gives the gamma mean $j+1/2$ by one integration by parts. In particular $(q_2/q_1)^{4v}\to0$ on the calibrated sequence, since $v/\beta_K\to\infty$. The same convergence is uniform on $[2,3]$ by continuity and strict inequality. Also $r_1^{2v}\to0$ in both cases.

In the logarithm proof replace each edge factor by its analytic family
$$
  1+\sum_{j\ge1}t_i^j\,b_{ij}\chi_j(g)\chi_j(h),\qquad
              b_{ij}=(r_j/r_1^j)^{a_i}.
$$
Here $b_{i1}=1$ and $0<b_{ij}\le1$ by the decreasing adjacent quotients. Evaluation at $t_i=x_i=r_1^{a_i}$ restores (6). There is an absolute polydisc of convergence for the logarithm whenever one takes $\rho>0$ with $(1+\sum_{j\ge1}(j+1)^2\rho^j)^6<3/2$. Haar symmetry under $g\mapsto-g$ makes the integral, and its logarithm at zero, invariant under simultaneous $t_i\mapsto-t_i$. After (5) discards monomials missing an index, division by $\prod x_i$ therefore leaves an even total degree. Its degree-zero term is the cumulant in (7). Each $x_i/x_0$, $i\ne0$, is at most $r_1^{2v}$ because $a_0\le6v$ while $a_i\ge8v$. In degree two only the $x_0^2$ coefficient can survive relative to $x_0^2$. Higher degrees are $O(x_0^4)$ by the same geometric-series bound. The only possible uses of higher characters in the $x_0^2$ coefficient are $j=2,3$ on the direct path. Their $b_{0j}$ tend uniformly to zero, bounded by $(q_2/q_1)^{(j-1)a_0}$.

It remains to compute this coefficient with the direct factor $1+t_0Y$ and all other indices appearing just once. Since $\mathbb E Y=0$, this factor changes the moments of $Y$ to $m_j'=m_j+t_0m_{j+1}$. The coefficient in all other indices is the cumulant of order three or five of these tilted moments. The missing-direct subtraction in (5) just removes the value at $t_0=0$. In the third cumulant the cubic coefficient is $2m_2^3=2$. In the fifth cumulant the only cubic contributions are $20m_3'(m_1')^2$ and $-60m_2'(m_1')^3$, yielding $20m_4m_2^2-60m_2^4=20$. These coefficients follow from the set partitions with block sizes $(3,1,1)$ and $(2,1,1,1)$ respectively. Each type has 10 partitions, with multipliers $2!$ and $-3!$. The other partitions give degrees one or five. Thus the constant terms in the five-plus-one combination cancel and the degree-two terms after division contribute $5\cdot2+20=30$. Every estimate was uniform in the choices of the bulges. Finally the sum of $w(E)r_1^{2a_0}$ is $r_1^{56v}(1+r_1^{12})^{\lfloor v/2\rfloor}$. Its log per slice has the claimed limit. This proves (10). It does not bound the complete sum over any fibre, since supports outside the six described types may enter with either sign.

**PROVED (unconditional gain in the full step).** For the first $B$ step applied to an isotropic Wilson input on these tori, let $V_{\rm in},V_{\rm out}$ use any compatible long-support filter containing the time-winding supports above. Then
$$
 V_{\rm in}-V_{\rm out}\ \ge\
 (10+o(1))r_1^{48v}(1+r_1^4)^{\lfloor v/2\rfloor}
 \qquad\text{for SU(2)}.                                                    \tag{11}
$$
Indeed use all the disjoint groups $\mathcal G(E)$ and leave *every other support in the entire Wilson expansion* as a singleton. Further summation within each fibre can only reduce its absolute value. Equations (8) and (9) give (11). The $o(1)$ is uniform in the two regimes specified in (10). This lower bound is on the numerator of (3). It measures no fraction of the unspecified denominator. On a calibrated bare lattice it can also be used as a lower bound on the cumulative loss up to a coarser level. Count this gain only at a step where the labels are still distinct.

### Dependence on the law, and the limits of the test

**PROVED (a same-group change of sign).** On the same four-dimensional lattice give an oriented face the positive normalized weight
$$
                  1+\tfrac1{36}\chi_1+\tfrac1{12}\chi_2 .
$$
It retains a fundamental term, is invariant under conjugation and distinguishes $g$ from $-g$ in its fundamental term. The character bound makes the weight strictly positive, and its convolution coefficients are nonnegative. The slowest nonconstant strip harmonic is now the adjoint with eigenvalue $1/36$, ahead of the fundamental at $1/72$. Formula (5) still holds. The leading variable is $Y=\chi_2(g)\chi_2(h)$. Its moments have $m_1=0,m_2=1,m_3=1,m_4=9,m_6=225$. Indeed the square of spin one contains spins $0,1,2$ once, and the cube contains $0,1,2,3$ with multiplicities $1,3,2,1$, by multiplication of $\chi_j(\theta)=\sin((j+1)\theta)/\sin\theta$. Integrating the respective characters, or their squares by orthogonality, gives $1,1,3,15$ for the single-end moments of orders $2,3,4,6$. The independent endpoints square them. The fourth and sixth cumulants are now $6$ and $225-15\cdot9-10\cdot1^2+30=110$. The five-plus-one remainder divided by $(1/36)^{48v+4|E|}$ tends to $140$ and all six leading weights have the *same* sign. Thus the cancellation (8) depends on which harmonic the plaquette *law* transmits. Neither the Lie algebra, the dimension nor the centre determines it.

**PROVED (a test with a nontrivial exterior).** Suppose the rest of a masked system couples to these sheets only through the two common end holonomies, inducing one and the same probability $\nu(dg\,dh)$ in all six configurations and all their sheet deletions. Keep that exterior enabled as a background. The alternating sheet-deletion difference of its log mass has (5) with $dg\,dh$ replaced by $\nu$ because the background log mass drops out. The coefficient of $w(E)$ in the five-plus-one sum is then
$$
                      5\kappa_{4,\nu}(Y)+\kappa_{6,\nu}(Y),
               \qquad Y=\chi_1(g)\chi_1(h),                                 \tag{12}
$$
with an $O(Q^{4v})$ error after division by $w(E)$, uniform in $\nu$. The proof of (7) used bounded characters in the logarithm estimate, so it applies verbatim to this probability, without symmetry or independent ends. All moments up to order six in (12) refer to the actual joint end law in this restricted attachment. In particular matching two-point data alone is insufficient for this calculation. For example Haar product gives zero, whereas taking $g=1$ and $\chi_1(h)=\pm1/2$ equiprobably gives $Y=\pm1$, $\kappa_4=-2,\ \kappa_6=16$ and (12) equals $6$. If one wants equal second moments, both examples have $\mathbb E Y=0,\ \mathbb E Y^2=1$. The latter endpoint law is an example for (12), not an asserted Wilson exterior.

**PROVED (the seed does not require this cancellation on positive gauge actions).** On each torus enable only the temporal plaquettes over the four edges of one contractible spatial square for all times. This positive Wilson plaquette model has the same gauge group and centre translations. Its normalized partition on that tube is $1+\sum_{j\ge1}r_j^{4v}$ for SU(2), by sewing (6) on two paths making up the square. Any proper subset peels to mass one. All twists give the same value. Consequently exactly one nonempty coefficient in (1) survives, is strictly positive, and winds through every time slice. Plaquettes with weight one cannot create extra coefficients by inversion. After *any* grouping (2) the single positive coefficient persists as a single positive coefficient. Thus (3) fails for every $\delta>0$ at each step. At fixed $2\le\beta\le3$, or even at bare $\beta_K\asymp\log n$, $P_K\to1$ because the two excess sums tend to zero by the quotient bounds following (6). Even the early-exit version has a separation on this family if one allows other coupling sequences. For each $u$ choose a coupling with $Z(u)=9/8$. Such a value exists by continuity, the limit one at zero and $r_1\to1$ at infinity. Then $V_j=\log(9/8)\ge1/9>1/12$ at the shorter period for every $j$, while $P_K\ge64/81>457/625$ since $Z(2u)\ge1$. This tuned tube is outside the calibrated isotropic family. This separates the numerical seed from (3) in a positive gauge-action class on actual tori. Strictness for the particular isotropic calibrated Wilson trajectory is unknown. Merely writing the full log purity as a sum of signed activities with its target bound would be an equivalence and earns no result here.

**ARGUED (which comparisons the proposed estimate still owes).** The proposed property of the law is a lower bound on the fraction of the long connected source response removed by allowed within-cell replacements, uniformly for the *blocked full Wilson source family*. Equations (8), (10) and (12) identify a term that can contribute to that fraction. The U(1) quarter-remainder test fails at a specified harmonic calculation, including for the weak cosine law. Its failure for the gapped U(1) twin means this calculation alone does not diagnose a gap. Weak five-dimensional SU(2) passes exactly the same local cancellation on the embedded three-spatial-direction graphs. This remains true at strong coupling and if a decoupled massless field is added and left unsourced. For the full source-family criterion the spectator must also be enabled/disabled with its cells and its full mass counted in (4). If it is kept as an untracked volume-dependent normalization, even the empty-mask normalization in the proof of (4) fails. This is the limitation of row 1553, Lemma ALG. No lower bound on the weight fraction in 4D, or failure of that bound for 5D, has been proved. I cannot identify a typical-field inequality yet that distinguishes all three laws.

### One magnetic attachment, worked out

**PROVED (an interior attachment in the same coarse cell).** In every graph use arms 0 and 1 for the direct path and the $+2e_y$ rail. At fine time 2 include the spatial $4$ by $2$ rectangle $D$ filling their loop. For this test take $4\in E$, $2\notin E$ and $v$ large and divisible by $B$. The cap meets the sheets only along the two paths at time 2. Its interior links belong to the disk alone. Its $xy$ label is already present in the same coarse time cell from the bulge at time 4. Consequently $q(A\cup D)=qA$ for every $A\in\mathcal G(E)$.

Write $c_k^D$ for the same alternating difference on the sheets with $D$ enabled throughout. At SU(2) Wilson coupling put $\eta=r_2^8$ (spin one, disk area eight). Uniformly in these $E$, at the large periods of (7),
$$
 \frac{c_4^D}{w(E)}=1-\frac53\eta+O(Q^{4v}),\qquad
 \frac{c_6^D}{w(E)}=-5+\eta+O(Q^{4v}).                                    \tag{13}
$$
For circle Wilson $c_k^D=c_k$ *exactly* for all positive couplings and periods in this construction. For SU(2) at $\beta\in[2,3]$ the five-plus-one group with the cap enabled still passes the one-quarter remainder test uniformly for large $v$. On the raw calibrated sequence all six leading *cap-enabled* weights are negative and its remainder fraction tends to one.

**Proof.** Cut all the sheets on their paths at time 2 and let $V_i$ be the cut-path transports. With $g,h$ fixed the exact sheet factors before integrating $V_i$ are $w^{*a_i}(g V_i h^{-1}V_i^{-1})$ by disk sewing. The path transports use disjoint spatial links and have independent Haar law before the cap is inserted. Its additional normalized factor is $w^{*8}(V_0 V_1^{-1})$. An incomplete sheet still peels because cutting along this path leaves a connected disk of faces, so holes propagate without deleting any path link held by the cap. Likewise an incomplete cap peels across its interior. In particular the *actual* coefficient (1) of the augmented support is $a(A\cup D)=c_k^D-c_k$. Adding these two coefficients inside a fibre realizes $c_k^D$.

The fundamental term of the cut SU(2) strip, after dividing by $x_i$, is
$$
 W_i=2\chi_1(gV_i h^{-1}V_i^{-1})
       =4(g_0h_0+\mathbf g\cdot{\rm Ad}(V_i)\mathbf h)
$$
in scalar and imaginary quaternion coordinates. Its mean over one Haar $V_i$ is $Y$. Under the cap each of $V_0,V_1$ is marginally Haar. Conditional on $V_0$, the adjoint rotation of $V_1$ averages to $\eta\,{\rm Ad}(V_0)$ by the spin-one convolution eigenvalue. A uniform rotation of a vector has covariance $|\mathbf h|^2 I/3$, by rotational invariance and trace. Thus the cap changes the conditional mean of $W_0W_1$ by precisely $\eta D_0$, where
$$
                 D_0=\tfrac{16}{3}(1-g_0^2)(1-h_0^2).
$$
All other cut variables remain independent given $g,h$. For U(1) the $V_i$ drop out of every character before integration, giving the exact statement.

To evaluate the squarefree coefficient of the logarithm for SU(2), introduce one $z_i$ per leading strip as in (7). The change of the integral with leading factors is exactly $\eta z_0z_1\mathbb E[D_0\prod_{i\ge2}(1+z_iY)]$. In the log difference only its first power can enter a squarefree coefficient. Set $z_0=z_1=0$ in the denominator. The resulting correction is $\eta$ times the joint cumulant of $D_0$ and $k-2$ copies of $Y$. This follows also by taking the coefficient linear in an additional source multiplying $D_0$. The higher strip harmonics cost $O(Q^{4v})$ after division by $w(E)$, by the bounded-disk logarithm argument of (7), now using $d_j\chi_j$ in place of the product of end characters. The bound is uniform since the cap is a probability tilt.

Using the three single-end moments from (7) gives $\mathbb E D_0=3$, $\mathbb E D_0Y^2=4/3$, $\mathbb E D_0Y^4=3$. For example these are $(16/3)4^{2s}(\mathbb E[g_0^{2s}(1-g_0^2)])^2$ at $s=0,1,2$. Odd insertions vanish. The two cumulants are therefore $4/3-3=-5/3$ and $3-6(4/3)m_2+3(6m_2^2-m_4)=1$. This gives (13). At $\beta\le3$, GL4 yields $r_2=(I_2/I_1)(I_3/I_2)\le(3/4)(1/2)=3/8$. For $\eta\le(3/8)^8<1/16$ the limiting cap-enabled fraction is $22\eta/(30-28\eta)<1/4$ with a uniform strict margin. On the calibrated bare sequence $\eta\to1$, by concentration or the adjacent quotient limits. The two leading coefficients tend to $-2/3$ and $-4$. In this regime the twelve raw supports $A,A\cup D$, if combined at once, have signed remainder divided by their total absolute weight tending to $11/29$. Their signed sum in units of $w(E)$ tends to $-22/3$, and their absolute sum to $10+5(5/3)+1=58/3$. The distinction between the six already combined cap-enabled weights and these twelve raw coefficients matters.

**PROVED (coupling dependence).** For this disk $\eta=r_2^8$ varies continuously from zero to one as the Wilson coupling runs from zero to infinity. Equation (13) places the sign change of the limiting four-arm coefficient at $\eta=3/5$ within the same SU(2) law family.

**PROVED (all Wilson attachments through one cycle at order one).** Extend the direct path length from 4 to 16, the four short offsets in the six-path graph staying at distance two. Its sixth path goes one $x$ step beyond each endpoint as before. In the four-path graphs replace $12-i$ by $24-i$ transverse $z$ steps. Thus the six-path lengths are $16,20,20,20,20,24$, and the four-path lengths are $16,20,20,64$. Each total is 120, and the box still fits in a $B$-cell. Use the same interior bulges away from slice 2. Let $C$ be the single spatial cycle on arms 0 and 1 at this slice. Enable *any* exterior collection of Wilson plaquettes of coupling at most 3 that meets the sheets in links only on $C$. Use the same exterior for all six replacements. It may occupy an arbitrarily large finite lattice. For this cap-enabled sheet difference the remainder fraction is at most $1/4$ for all sufficiently large $v$, uniformly in the exterior, volume, $E$, and sheet coupling $\beta\in[2,3]$.

**Proof.** Gauge-fixing a spanning path of $C$ reduces any gauge-invariant density on its boundary links to a central density of the single remaining cycle holonomy. This is just a Haar change of vertex frames along an open path, with the root gauge conjugating the remaining holonomy. Thus the previous cut-path argument holds with an arbitrary normalized central factor $d(V_0V_1^{-1})$ in place of $w^{*8}$. Only its adjoint eigenvalue
$$
               \eta=\tfrac13\,\mathbb E_{\rm ext}\chi_2(U_C)
$$
enters the coefficient at order $r_1^{120v+4|E|}$ in (13). The same proof gives the uniform error, since the exterior enters as a positive probability tilt. The reference here is the marginal of the *enabled exterior* on $C$. Treating every exterior plaquette as a separate inversion variable would require further signed sums over those plaquettes.

Use the independent-link conditional Wilson estimate behind row 1460, Lemma SE (check 1463). The 16 collinear direct links on $C$ never occur two at a time in an elementary plaquette. Given all other exterior links, their laws factor, each with quaternion Wilson tilt of strength $t\le6\cdot3=18$ in four dimensions. An inverse link or a fixed twist changes only the orthogonal frame. Its mean adjoint matrix is $r_2(t)$ times a rotation, by the same scalar convolution formula. Bounding the norm of the ordered product hence gives $|\eta|\le(\max_{t\le18}r_2(t))^{16}$. Explicitly the Bessel recurrence gives $r_2(t)=1-4(I_2/I_1)/t$ and $I_2/I_1=1/(4/t+I_3/I_2)\ge t/(4+t)$. The value at zero follows by continuity. Hence $|\eta|\le(9/11)^{16}<1/16$, since $2\cdot9^4<11^4$. The signed sum divided by the absolute one is bounded in modulus by $22|\eta|/(30-28|\eta|)+o(1)<1/4$ with a fixed margin. This proves the uniform result. In five dimensions on the same order-one interval the corresponding bound is $(6/7)^{16}<1/8$ since $2\cdot6^5<7^5$. It too passes the quarter test. In U(1) a central factor on $C$ still has exactly zero effect on all the strip factors.

**PROVED (weight required by the consumer).** If disjoint groups with a remainder fraction at most $1/4$ account for a share $\gamma>0$ of $V_j$, they give (3) with $\delta=3\gamma/4$ by summing their losses.

**ARGUED (next component).** Neither (11) nor the one-cycle attachment theorem supplies this share in the source coefficients of an order-one *image*. The one-cycle theorem prices a full-strength exterior of arbitrary volume across a single spatial interface. The uncovered case includes an exterior reading two cycles at different times. There its marginal is a joint law of cut transports, and the single number $\eta$ no longer gives (13). A concrete next test is two $4$ by $2$ magnetic disks between the same arms at a separation proportional to $v$, allowing a connected Wilson exterior on their boundary cycles. The required estimate is a bound on their joint adjoint transfer under that exterior, including the terms surviving the alternating sheet deletions.

**PROVED (what the source measurements read).** At finite cutoff the source measurements can equally be defined from the joint law of the Wilson plaquette weights on the fully enabled torus. With $\mathcal P$ the full label set and $w_p^z$ its positive normalized factors,
$$
 \frac{Z_T^z(D)}{Z_T^z(\mathcal P)}
       =\mathbb E_{T,z}^{\rm full}\prod_{p\notin D}(w_p^z)^{-1}.
$$
This follows by cancellation inside the Haar integral. The law, including its joint correlations, determines (1) and (3). The reciprocal products can be large. Estimating them from typical full fields on the calibrated images is precisely where the one-cycle bounds cease to apply. I have no proof that weak 5D SU(2) fails (3), or that weak 4D U(1) fails its unrestricted version. What fails for U(1) is the specified one-quarter *supplier*. An obstruction to every order-one RG step would require much more.

**RESULT (d), a first component.** The exact factor-$B$ map (2) gives the original neutral seed under the uniform entry bound and signed estimate (3).
For Wilson winding sheets I proved the four- and six-ribbon connected weights, their cancellation inside one coarse support, and the first surviving SU(2) term (7)–(11).
A magnetic attachment changes the leading term by its adjoint Wilson-loop expectation. At order-one coupling the quarter-remainder bound is uniform for every exterior attached through one spatial cycle.
The corresponding compact U(1) family leaves $5/11$. Five-dimensional SU(2) passes the same local test.
The weight share on calibrated blocked fields, entry to the window, (PUR-io), and the mass gap remain open. All new proofs are hand arguments, without a Lean check or independent review. This research note grants no status.
