# Repo search

At `092edafe2`, I searched `origin/main`, `pr/10114`, `pr/10133`, `pr/10134` and `pr/10141` for two-sample cylinder mixing, H-two-col, H-two-N1, twisted cylinder and calibrated neutral purity. The precise query returned no lines. The broader W-mix/T-mix query matched operational randomization and flavour mixing. Searches for annular score or variance, cutwidth with Poincaré, conditional column contraction and posterior scores on tubes returned no matching theorem. The requested target-specific prior file was absent. A supplementary search at the pinned commit outside this lane was completed in the full clone. The sparse checkout lacked one of its Git objects.

- **ON FILE.** `ym4d-proof/MASS_GAP_LOCAL_BLOCK_ASTRA.md`, (24), bounds its one-step contraction by $18/359$ for $0<\beta\le1/32$. The Nov. 8 digest identifies the same source on PRs 10114 and 10133. This is below the Q2 consumer's band. [Nov. 8 search](prior/repo-search-2026-11-08.md)
- **ON FILE.** The closest lane hit is row 1351, (17) and (21). It bounds the relative endpoint interaction on ordinary conditional Wilson columns and carries their finite-memory normalizers. Row 1211 gives a typical-wall replacement for local Wilson insertions. I use the former's one-dimensional contraction. Neither gives gradient weights for the Q2 score after exterior averaging. [Row 1351](gap-blockstep4-astra62.md) · [Row 1211](gap-solve22-astra62.md)

## Result and consumer

**PROVED below (outcome d).** At $\beta=\kappa\in[2,3]$ the Q2 score has a component satisfying (FL)'s exponential gradient estimate on unrestricted four-dimensional tori. It is the fluctuation that remains when an arbitrarily sparse set of fine links is fixed. The free links form a connected region winding in every direction. Equation (15) bounds its response on arbitrary fine tests. Equations (16)–(17) bound the total-variation cost of changing distant fine data at common sparse wall values. The distribution of the wall values themselves is the outstanding input. The example in (18) shows how sparse pins can carry an order-one signal.

**ON FILE.** Row 1468 §3.1 gives $P_K=Z_+(2u)/Z_+(u)^2$ and Fact PUR. Check 1120, TS3, identifies the one-test two-sample distance within a factor of two with the supremum of its covariance against the outside. Check 1121, JI, gives twice the sum of forward and reverse relative entropies for the mean ring exchange cost. Row 1118 §3.2 proves reverse-martingale convergence to a tail projection even in a mixture. Row 1122 keeps the one-scale-to-all-scales implication distinct. Row 1573 (1)–(3) treats two projected cylinders and separates its entropy majorant from passing purity on positive nonlocal kernels. Rows 1584 (13.4)–(13.6), 1597 (PZ-why and WB1–WB3) and check 1598 retain the physical-length mixing question. Rows 1304/1308 exclude a fixed positive orientation of mixed transfer minors, and row 1321 retains the signs in replica sewing. [Row 1122](gap-l3-direction-fable.md) · [Row 1573](gap-band-neutral-astra62.md) · [Check 1598](gap-direction6-check-astra62.md)

**ON FILE.** The one-step target is (FL), row 1510 §§4.1–4.2. Lemma REV reads covariances in the four-dimensional posterior given the observed coarse field. Registry R10 has no owner. R11 and TWO-PER have different statements and owners. Row 1468 §4.3 also requires a nonlinear flow and control outside the regular set. Row 1553 §3.3 names a one-step in-law input as T-mix. The coarse source, composition and passage to the sixteen masses remain open even given one gradient estimate. Row 1388/check 1389 splits a frozen-layer force covariance by Langevin time. Here the conditioning is on actual fine links and on Q2 observations. [Row 1510](gap-seed-solve-fable.md) · [Check 1513](gap-seed-solve-fable-check-astra62.md) · [Registry](open-registry.md) · [Check 1389](gap-layer-force-cov-check-astra62.md)

**ON FILE.** Sussman and Alpoge, with Claude and Codex, outline at `31a47c543775`, index chunks 01, 02 and 07 and the obligations index. Lines 588–599 give the $E e^{-E}\,dE$ example with polynomial clustering and spectrum down to zero. Lines 2195–2213 and 2313–2335 give the one-bond convolution and finite transfer trace. CA-I 2698–2713 leaves clustering and a mass gap outside its assertion. CA-III 108223–108269 uses a positive gap as one sufficient input for scalar reflected decay. [Outline index](sa-index/README.md)

## The posterior and the part to be estimated

**ON FILE (rows 1468, 1510, check 1513).** Take any periodic fine four-torus of even side lengths at least eight. Write $\nu_V$ for the law of $W$ given the entire coarse observation $V$ in one Q2 step. Its density against product probability Haar is proportional to
\[
 \exp\!\left(\beta\sum_p \tfrac12\operatorname{tr}W_p\right)
 \prod_b \frac{\exp(\kappa\langle M_b(W),V_b\rangle)}
                 {Z(\kappa |M_b(W)|)},\qquad
 Z(t)=\int_{S^3}e^{t v_0}\,dv,\qquad \kappa=\beta\in[2,3].
\]
Here $M_b$ is row 1468's mean of 384 unit-quaternion contour products and $\langle\, ,\,\rangle$ is the real Euclidean inner product. The score at $c$ is the tangent vector $S=\kappa\,\mathrm{proj}_{V_c^\perp} M_c(W)$. The consumer asks for nonnegative weights, the same for all smooth real $f$, satisfying
\[
 \|\operatorname{Cov}_{\nu_V}(f,S)\|^2
 \le \nu_V\!\sum_e\gamma_{ce}(W,V)|\nabla_e f|^2,\qquad
 \mathbb E_{W,V}\gamma_{ce}\le C e^{-m d(c,e)}. \tag{1}
\]
Distances below use fine-link anchors and the base of $c$, with periodic graph distance. Replacing a base by the support of its fixed contour family changes constants only. The outline's block map at 7943–7966 has odd block side and a logarithmic mean. The displayed posterior uses exactly the side-two arithmetic mean of the consumer.

**PROVED below.** Fix a transverse width $w\ge 4$. Take all fine links whose spatial anchors lie within periodic $\ell^\infty$ distance $w$ of the base of $c$, for *all* times. Denote this tube by $U$. For
\[
     S^{\rm out}=\nu_V(S\mid W_{U^c}),\qquad S^{\rm in}=S-S^{\rm out},
\]
(1) holds for $S^{\rm in}$ with deterministic exponential weights supported in $U$, uniformly over $V$, the torus and the specified couplings. The estimate holds for $f$ on the entire fine torus. When $U$ covers the spatial torus it gives full (1) with constants depending on the spatial width. On unrestricted tori the score passed to the exterior has derivatives only in a lateral collar and they decay exponentially in time. Every unit tangent direction loses a volume-independent positive fraction of its actual score variance to $S^{\rm in}$. The quantitative statements and their proofs follow.


## A spatial criterion for the score covariance

**PROVED.** Fix $V$ and nested sets of fine links $\varnothing=D_{-1}\subset D_0\subset\cdots\subset D_J=D$. Put $\mathcal F_i=\sigma(W_{D_i^c})$, $h_{-1}=S$, $h_i=\nu_V(S\mid\mathcal F_i)$ and $b_i=h_{i-1}-h_i$. For a fixed exterior $y$ write $\pi_i$ for the conditional law on $D_i$. Define its cost for this particular vector increment by
\[
 a_i(V,y)=\sup_{g}\frac{\|\pi_i[(g-\pi_i g)b_i]\|^2}
                              {\pi_i\sum_{e\in D_i}|\nabla_e g|^2}. \tag{2}
\]
The tests are smooth real functions in the box with positive denominator. For the smooth score used here the conditional formulas are ratios of integrals of smooth positive densities on compact groups. The supremum may use a countable $C^1$-dense set, for instance rational polynomials in quaternion coordinates restricted to the spheres (polynomial approximation with first derivatives on a box after smooth extension). Thus the cost is measurable. An upper bound is $C_i\,\pi_i\|b_i\|^2$, where $C_i$ is any Poincaré constant in the convention $\operatorname{Var}_{\pi_i}g\le C_i\,\pi_i\sum|\nabla_e g|^2$. This follows by Cauchy–Schwarz. All finite-box costs are finite by the positive density bounds and the Haar inequality proved below.

For positive deterministic $p_i$ with $\sum_i p_i\le1$, set
\[
 \gamma^{D}_{ce}(W,V)=\sum_{\{i:e\in D_i\}}\frac{a_i(V,W_{D_i^c})}{p_i}.
 \tag{3}
\]
These are weights in the first inequality of (1) for $S-h_J$. Indeed $\pi_i b_i=0$ by successive conditioning. For a full-torus test restrict it to each fixed exterior. The norm of $\nu_V[f b_i]$ is at most
$\big(\nu_V[a_i\sum_{e\in D_i}|\nabla_e f|^2]\big)^{1/2}$ by (2), integration over the exterior and Jensen. Sum the bounds, apply weighted Cauchy–Schwarz with the $p_i$, and use $\sum b_i=S-h_J$. The construction furnishes one array of weights for every test simultaneously.

**PROVED consequence.** Take $D_i$ to be the $i$-neighbourhood of the fixed support of $S$, ending when it fills the torus. If, uniformly in the torus, $c$ and the couplings of (1),
\[
             \mathbb E_{V,W} a_i(V,W_{D_i^c})\le A e^{-\alpha i}
             \quad(0\le i\le J),                                      \tag{4}
\]
then full (FL) holds. In fact $h_J$ is constant at fixed $V$. Taking $p_i=(1-e^{-\alpha/2})e^{-\alpha i/2}$ in (3) bounds the mean weight at distance $r$ from the support by
$A(1-e^{-\alpha/2})^{-2}e^{-\alpha r/2}$. In (2) both the increment and its governing conditional law are determined by the fine links and observations in the box and a fixed interaction collar. This follows by cancellation of outside-only factors in both conditional expectations. Their *average* in (4) is in the actual four-dimensional law. This criterion asks for all box sizes and includes the last box. Reverse-martingale convergence alone gives no rate for (4). The following estimates prove summability in one unbounded direction with the lateral exterior retained.


## Uniform bounds along a tube in the four-dimensional posterior

**PROVED (local constants).** A Q2 contour has at most ten links. In fact its anchors in each coordinate lie between the starting fine base and that base plus three on a lift. A Wilson plaquette has range one. Each log plaquette factor has oscillation at most $2\beta$ and each log Q2 factor has oscillation at most $4\kappa$, since $|M_b|\le1$ and $e^{-\kappa}\le Z(\kappa|M_b|)\le e^\kappa$. These bounds hold for every $V$. They bound oscillation when variables are pinned as well.

Partition the time circle into consecutive blocks of length between 8 and 15, putting the whole time support of $S$ in block 0 by shifting the partition. For example divide by 8 and distribute the remainder in one block, placing its first time at the base of $c$. Every allowed time side is at least eight. A block variable consists of the links of $U$ anchored in its time block. Conditional on $W_{U^c}=y$, the density on the resulting circle is
\[
             \mathrm{const}\ \prod_j D_j(x_j)\prod_j K_j(x_j,x_{j+1}).
                                                                    \tag{5}
\]
All factors are positive. Assign each original factor meeting the tube to its single block or to the adjacent pair it meets. Its time range is at most three, so it meets at most two blocks, even across the periodic cut. With a single block put everything in $D_0$. With two blocks keep the two interfaces distinguished by the time cut they cross.

The following loose constants make the width dependence explicit. Per fine base there are at most six plaquette and four coarse-bond factors, counting a coarse base only when it exists. If a factor reads a block link, its base lies in a spatial cube of side at most $2w+9$ and a time interval of at most $15+8$ sites. Hence one may take
\[
     H_w= 12\cdot 10\cdot 23(2w+9)^3,\qquad R_w=e^{H_w},\qquad
     q_w=1-R_w^{-1}.
\]
The factor count also works when a period identifies sites, by overcounting the lift. The log oscillations of *all* factors touching one block sum to at most $H_w$. Each $K_j$ consequently has max/min ratio at most $R_w$. The conditional law of any one block given the others has density between $R_w^{-1}$ and $R_w$ against its product Haar reference. This remains true in a segment conditioned on its exterior and for a one-block marginal of that segment, by averaging its conditional laws.

**PROVED (loss of temporal boundary data).** Let $D_i$ now consist of the blocks at circular block distance at most $i$ from 0, all within $U$. Use $J$ equal to the largest such distance. Write $h_*=h_J=S^{\rm out}$. For $i<J$, fixing the lateral exterior and changing the two bounding block values changes $h_i$ by at most $4\kappa q_w^i$ in norm. To see this, hold the right boundary fixed and compare the two left boundaries. With a fixed future, an oriented step has kernel $K_j(x,z)h(z)\,dz/\int K_j(x,t)h(t)\,dt$, where $h>0$ contains the site and future weights. It dominates $R_w^{-1}h(z)\,dz/\int h$. Removing that common mass contracts total variation (normalized to have maximum one) by $q_w$. Reaching the central block takes at least $i$ such steps. The change of its vector expectation is at most $2\kappa q_w^i$, by testing all unit directions. Reverse time to compare the right boundaries and add. If both ends abut the same outside block, change its two occurrences in succession in the open interval kernel. The intermediate pinned interval is well-defined. Averaging one choice of boundaries gives
\[
             \|h_i-h_*\|\le4\kappa q_w^i,\qquad i<J.                 \tag{6}
\]
This step reuses row 1351's contraction proof with the bounded, finite-range Q2 observation factors included in (5).

**PROVED (the gradient cost in a segment).** On an interval of $N$ blocks in (5), including its full-circle case, every conditional law $\pi$ with its lateral and interval exterior fixed satisfies
\[
 \operatorname{Var}_{\pi} f\le N R_w^7\,\frac{\pi^2_{\rm circ}}2\
                  \pi\sum_{e\ {\rm in\ interval}}|\nabla_e f|^2 .        \tag{7}
\]
Here $\pi_{\rm circ}$ is the diameter of the unit round three-sphere. For one Haar $S^3$, take independent Haar $x,h$ and join $x$ to $xh$ by the path $x\exp(t\log h)$ of length at most $\pi_{\rm circ}$, choosing either shortest arc at an antipode. At each $t$, conditional on $h$, the current point is Haar. Integrating the squared derivative and using $\operatorname{Var} f=\mathbb E|f(x)-f(xh)|^2/2$ gives the stated Haar constant. For product Haar, reveal coordinates successively. The squared martingale increments add, and each conditional-mean derivative is the integral of the corresponding partial derivative. Jensen and the one-coordinate bound give the same constant with the sum of gradients.

For (7) take independent configurations $x,y$ of $\pi$. Move from $x$ to $y$ by installing the blocks of $y$ in order. Square the telescoping sum with Cauchy–Schwarz, at cost $N$. Before updating block $j$, exchange the preceding prefix between the replicas. This change of variables preserves pair Haar measure. Only pair factors crossing one of the at most two cuts can change the product density. Each such cut costs at most $R_w^2$ in the density ratio, so the transformed pair law is dominated by $R_w^4(\pi\otimes\pi)$. Under the latter law the update replaces block $j$ of the first copy by the independent second block. Conditional on the other first-copy blocks, the old and replacement values have respective conditional and marginal densities bounded by $R_w$ against Haar. Their squared difference in $f$ therefore integrates to at most $2R_w^2\operatorname{Var}_{\rm Haar}(f)$ on that block. Apply the product Haar inequality and use the lower density bound $R_w^{-1}$ to return the gradient to its conditional law. The factor two cancels the variance prefactor of the original two-copy difference. Summing over $j$ proves (7). In particular the cost of a long segment grows at most linearly in its length for fixed width.


**PROVED (the tube part of (1)).** For the central increment use $\|b_0\|\le 2\kappa$. For $1\le i\le J$ use (6) and $h_J=h_*$ to get $\|b_i\|\le 8\kappa q_w^{i-1}$. Equation (7) applies in $D_i$ with $N\le 2i+1$. Thus (2) is bounded for every pin and $V$ by
\[
        A_w\kappa^2(2i+1)q_w^{2i}.
\]
For example $A_w=64q_w^{-2}R_w^7\pi_{\rm circ}^2$ covers $i=0$ as well. Take $p_i=(1-\sqrt{q_w})q_w^{i/2}$ in (3). A link at block distance $k$ only enters terms $i\ge k$, and
$\sum_{i\ge k}(2i+1)q_w^{3i/2}\le q_w^k\sum_{i\ge0}(2i+1)q_w^{i/2}$. A link in such a block has temporal distance at most $15(k+1)$ and transverse graph distance at most $3w$ from the base. Consequently there exist $C_w<\infty$ and $m_w=-\log(q_w)/15>0$ such that
\[
 \|\operatorname{Cov}_{\nu_V}(f,S^{\rm in})\|^2
 \le C_w\kappa^2\sum_{e\in U} e^{-m_w d(c,e)}\nu_V|\nabla_e f|^2 .     \tag{8}
\]
One may multiply the preceding geometric-series constant by $q_w^{-1}e^{3wm_w}$ for distance conversion. For a single time block use only $i=0$. The proof also gives (8) *inside each conditioned tube*, for the covariance there with $S$. More generally it applies to any vector reader of norm $L$ supported in the central time block, replacing $\kappa$ by $L$. A shift of the partition contains any reader of time span at most eight. A fixed larger span can instead be contained in a central interval of a fixed number of blocks, changing only the prefactor. This proof uses all fine tests in (1), including tests that read the exterior.

**PROVED (a width that grows with separation).** In (5), two independent draws of the temporal boundary data with a common lateral exterior give conditional central score means differing by at most $4\kappa\exp(-i e^{-H_w})$ across $i$ intervening blocks. The same holds for specified boundary values. For graph distance $T$ in the time direction one can take $i\ge T/15-2$ when a centred interval with that buffer fits. If $H_w\le\frac12\log T$, the bound is at most $4\kappa\exp[-(T/15-2)/\sqrt T]$. Thus the screened region may widen with the separation in the actual posterior at the consumer's fixed band coupling. With spatial diameter fixed, or with all three spatial periods short enough that this tube fills the spatial torus, the entire score is included up to its constant mean. With all spatial sides proportional to $T$, this estimate leaves a lateral exterior.

**PROVED (size of the part removed).** Let $D$ be the union of the fine bonds in the contours of $c$. It has at most $3840$ links. Counting possible bases and orientations bounds the number of original factors reading one link by $L_0=10\cdot9^4$. Put $H_0=12\cdot3840 L_0$. The conditional law on $D$ given $W_{D^c},V$ dominates $e^{-H_0}$ times product Haar on $D$. Under that product Haar, $M_c$ has left-invariant law under quaternion rotations, since a gauge rotation at its initial vertex multiplies every path transport on the left and preserves product Haar. The terminal vertex is different. The mean is zero and the second moment matrix is $(\mathbb E|M_c|^2/4)I$ by transitivity of left rotations on the unit sphere. If every link of $D$ lies within chord distance $1/20$ of the identity then each contour product lies within $10/20$ of it, by the telescoping product bound. Thus $\mathbb E|M_c|^2\ge h^{3840}/4$, where $h>0$ is the Haar mass of that open ball. For every unit $v\perp V_c$ minimize $\nu[(v\cdot S-t)^2]$ over real $t$ to obtain, for every exterior of $D$,
\[
 \operatorname{Var}(v\cdot S\mid W_{D^c},V)\ge
             \delta\,\kappa^2,\qquad \delta=e^{-H_0}h^{3840}/16>0.      \tag{9}
\]
As $D\subset U$, total variance gives the same lower bound after conditioning only on $W_{U^c},V$. Since $\operatorname{Var}_{\nu_V}(v\cdot S)\le\kappa^2$, the exterior mean has variance at most $(1-\delta)\operatorname{Var}_{\nu_V}(v\cdot S)$. The constant is small and independent of volume. In particular (8) controls an actual nonzero part of the score at every $V$.

There is a gauge-invariant way to probe this part in the joint experiment. Take the three-edge detour around a coarse plaquette from the start of $c$ to its end, with transport $A(V)$. Project $A(V)$ onto $V_c^\perp$ and normalize to a unit vector $v(V)$. The exceptional $A(V)=\pm V_c$ set has zero coarse probability by absolute continuity and independent product Haar as reference. Then $v(V)\cdot M_c(W)$ is invariant under simultaneous vertex gauge transformations and under the paired flat centre translations of the fine and coarse fields, since the two transports acquire the same endpoint rotations and centre sign. At fixed $V$ this joint observable is a permitted smooth fine test. Changing only $V_c$ in direction $v(V)$ changes the coarse plaquette trace $\langle V_c,A(V)\rangle$ with positive derivative. The covariance of this test with $v(V)\cdot S^{\rm in}$ is $\kappa^{-1}\nu_V[\operatorname{Var}(v(V)\cdot S\mid W_{U^c},V)]\ge\delta\kappa$. This identifies a directly tested loop response. It gives no lower bound on a transfer energy.


## Integrating a positive density of fine links

**PROVED.** On tori with spatial sides divisible by 32, split each spatial coordinate into cells of length 32. In each three-dimensional cell select the first 16 sites of each coordinate and take all fine links anchored in that cube, at every time. Let $I$ be the union of these tubes and $Y=W_{I^c}$. This integrates exactly one eighth of the fine links. The spacing between different selected cubes exceeds twice the spatial range of any log factor. Conditional on $Y,V$, the laws of the different tubes are independent. In the exterior density keep the product of every outside-only factor and, for each tube, the integral of the product of *all* factors meeting it. This is the full marginal by Fubini. In particular the dependence of each integral on $Y,V$ is retained. For a single tube on any of the original even tori the following conclusions hold with the corresponding width constants.

For every $c$, put $\bar S_c=\nu_V(S_c\mid Y)$. A score reads at most one selected tube. If it reads one only in part, the outside arguments of $M_c$ are fixed in applying (6)–(8). If it reads none, $S_c=\bar S_c$. Thus all scores satisfy the analogue of (8) after subtracting $\bar S_c$, simultaneously, with fixed constants. For a test depending on several interiors, integrate the other independent interiors, or fix them before applying (8) and then use Jensen. For a score supported entirely in a selected tube, (9) holds. The derivative in $V_c$ of the log *unnormalized* exterior density is exactly $\bar S_c$. Differentiation of the normalized exterior density subtracts the constant $\nu_V S_c$. This identifies the score of the next measure, including its normalization.

**PROVED (the transmitted score).** For an exterior link $a$ and unit tangent $u$ at $Y_a$, let $B_{a,u}$ be the $u$ derivative of the log product of the factors that meet the relevant tube. Its norm is bounded by a numerical constant independent of $V$ and the torus. In fact a differentiated plaquette costs at most $\beta$, a derivative of $M_b$ at most 10 by the product rule, and a derivative of $\log Z(\kappa|M_b|)$ at most $\kappa\|D M_b\|$ by differentiation of the defining integral. Thus $L_0(\beta+20\kappa)$ is enough. The interior arguments of $B_{a,u}$ lie within three time steps of $a$. At a fixed exterior the quotient rule gives
\[
   D_{a,u}\bar S_c=\nu_V(D_{a,u}S_c\mid Y)
           +\operatorname{Cov}_{\nu_V(\cdot\mid Y)}(S_c,B_{a,u}).      \tag{10}
\]
Outside-only factors cancel in the covariance. The direct derivative vanishes unless $a$ is in the support of $S_c$. The covariance vanishes unless $a$ is in the fixed-width lateral collar of the tube read by $c$. In that collar condition on the complement of a central segment ending before the time support of $B_{a,u}$. In the conditioned-tube law the covariance equals that of $B_{a,u}$ with $h_i-h_*$, bounded by $4\kappa\|B_{a,u}\|_\infty q_w^i$ by (6). The available $i$ is at least the circular time distance divided by 15 minus a fixed constant, for distant $a$. For closer $a$ use $2\kappa\|B_{a,u}\|_\infty$. Thus $\|D_a\bar S_c\|\le C_w e^{-m_w d(c,a)}$ on the collar (increasing $C_w$ absorbs its bounded transverse diameter and the direct derivative). A score depending only on the exterior has its original finite derivative range. These are derivative bounds for the *actual* exterior score, uniform in every exterior field.

**PROVED (return to the fine tests).** If $F(Y)=\nu_V(f\mid Y)$, differentiation of the same quotient gives $D_{a,u}F=\nu_V(D_{a,u}f\mid Y)+\operatorname{Cov}(f,B_{a,u}\mid Y)$. The conditional law factors over tubes, and an exterior link touches at most one collar in this tiling. Apply the local-reader version of (8) in that tube to $B_{a,u}$ and take the supremum over unit $u$. With a numerical $C$ and $m>0$ fixed by the tile,
\[
 |\nabla_a F|^2\le 2\nu_V(|\nabla_a f|^2\mid Y)
     + C\sum_{e\in I}e^{-m d(a,e)}\,\nu_V(|\nabla_e f|^2\mid Y).       \tag{11}
\]
The second term is needed only in a collar. Now suppose the exterior measure, for the score in (10), has weights $\bar\gamma_{ca}(Y,V)$ in the form of (1). Total covariance gives
\[
 \operatorname{Cov}_{\nu_V}(f,S_c)
 = \nu_V[\operatorname{Cov}(f,S_c\mid Y)]
       +\operatorname{Cov}_{Y\mid V}(F,\bar S_c).
\]
Bound the first term by (8) and the second by the exterior weights and (11), squaring the sum at cost two. The resulting interior weights are bounded by a fixed multiple of
\[
    e^{-m d(c,e)}+\sum_{a\notin I}\bar\gamma_{ca}(Y,V)e^{-m d(a,e)}.
\]
Exterior weights cost at most a fixed multiple of $\bar\gamma_{ce}$. Multiplying (11) by a weight depending on $Y,V$ commutes with conditional expectation under the original joint law. Exponentially decaying mean exterior weights give exponentially decaying mean fine weights. To see the volume uniformity, take half the smaller of the two rates, use the triangle inequality to extract that exponential in $d(c,e)$, and sum the remaining exponential in $d(c,a)$ using the polynomial growth of periodic lattice balls. Conversely, testing a fine bound on functions of $Y$ alone and conditioning the weights on $Y,V$ gives the exterior bound. This equivalence earns no progress by itself. The unconditional estimates (8)–(11) account for the fluctuations removed in the integration, the positive variance removed for interior scores, and the coefficients needed to transfer arbitrary tests back.


## Leaving an arbitrarily small fraction of the fine links conditioned

**PROVED.** At the same order-one couplings, fix any $\varepsilon>0$. For every sufficiently large even torus and every $c$ there is a deterministic set $E$ of at most $\varepsilon$ times the number of fine links, with these properties. The free region $E^c$ is connected in the lattice of anchors and winds around all four periods. It contains the score support. With $Y=W_E$, (1) holds for $S-\nu_V(S\mid Y)$ with deterministic exponential weights supported on $E^c$, uniformly in the four periods, $V$ and all the values on $E$. The rate may depend on $\varepsilon$. In particular (9) still holds for this conditional part. The following construction also bounds the cost as $\varepsilon$ decreases.

**Prior search.** The five-ref search for “subdivided grid/graph/lattice”, “junction/corridor” near “Dobrushin” and “decorated lattice” found an unrelated single-cell valley calculation and a colour-triality note that mentions graph subdivision. Rows 1084/1086 identify a spin marginal on a decorated planar grid. Row 1375, (8), controls sampled spatial coarse holonomies via private links. Their readers use spins or holonomies on the specified grid. Searches of FINISH and the library for chambers with corridors, sparse pinning with posterior mixing, and vanishing-density walls returned no matching statement. The proof below uses the conditional contraction in row 1351 and Dobrushin’s single-site comparison argument used in rows 1566/1568.

**Geometry.** Use corridors of transverse side nine. Write $R=R_4$ and $q=1-1/R$ from (5). Choose once and for all a multiple $L$ of eight, at least 32, so large that
\[
              (R^2-1)q^{\lfloor L/15\rfloor-1}\le 1/32.                \tag{12}
\]
Choose $M\ge 40$ with $4L/(M+L)\le\varepsilon$ and put $P=M+L$. On each coordinate circle of length at least $3P$, take $\lfloor n_i/P\rfloor$ intervals of integer lengths between $P$ and $2P$, assigning the remainder to the last interval. In each interval retain an interval of length $p-L$ followed by a gap of length $L$, where $p$ is its length. Products of four retained intervals form the chambers. Across each face gap connect the two chambers by the straight corridor, whose three other coordinates run through the middle nine sites of their respective retained intervals. Free all fine links anchored in a chamber or corridor, and fix the remaining links $E$. Shift the four partitions so the base of $c$ lies at a chamber centre. Its entire contour support lies inside. The union bound on the four coordinate gaps gives $|E|/|\mathcal E|\le 4L/P$. A path can run from a chamber centre to the next centre in each coordinate direction through the connecting corridor. Every chamber is connected and every corridor attaches at both ends. This proves the claimed topology on the periodic lattice.

**Proof at the junctions.** Keep the chamber variables $z_v$ and condition on the exterior $Y$ and on $V$. Each original log factor has anchor range at most three. Distinct corridor interiors are separated by more than three, including near common chambers, since their openings are in the middle of different faces and $M\ge40$. Nonincident chambers and corridors also have separation greater than three. Thus conditional on the chamber variables the corridor interiors are independent. Integrate them, carrying each normalization. The resulting chamber density has arbitrary single-chamber weights and one positive factor $A_{vu}(z_v,z_u)$ for each nearest-neighbour pair in the four-dimensional grid of chambers.

Each corridor is an open chain of the blocks of (5), with two end factors reading its endpoint chambers. The same $R$ bounds the max/min ratio of each interface factor, including either end, because all factors assigned to an end also read the first or last nine-wide arm block. Given two right chamber values $t,t'$, the ratio $A(s,t)/A(s,t')$ is the expectation, with right endpoint $t'$, of the last factor ratio, which lies in $[1/R,R]$. Changing $s$ changes this expectation by at most $(R-1/R)q^{\lfloor L/15\rfloor-1}$ by the common-mass transitions in (6). Dividing by its lower bound $1/R$ and also interchanging the two left values yields
\[
  \frac{A(s,t)A(s',t')}{A(s,t')A(s',t)}\le1+\eta,\qquad \eta=1/32.    \tag{13}
\]
This holds with all the original exterior data fixed. All factors depending on just one endpoint cancel in (13). In the chamber heat bath, changing a single neighbour reweights the conditional law by a function whose max/min ratio is at most $1+\eta$. Its normalized density ratio lies between $(1+\eta)^{-1}$ and $1+\eta$, so the total variation influence is at most $\eta$. Each chamber has eight neighbours. Its own conditional density has max/min ratio at most $e^{H}$ against its product Haar law, with $H=120(2P+8)^4$. Indeed the ratio for two chamber values is bounded by the total oscillation of all original factors touching that chamber, *before* integration over the corridors. Applying the same bound at every value of the integrated variables preserves it. A chamber Poincaré constant $C_H=(\pi_{\rm circ}^2/2)e^{2H}$ follows from (7)'s product Haar argument and density comparison.

**Proof for arbitrary tests.** Write $\rho$ for this chamber law, $P_v$ for its conditional resampling at chamber $v$, $B$ for the adjacency matrix of the chamber grid, and $\delta_v g$ for the scalar oscillation of $g$ in chamber $v$. For $u\ne v$,
$\delta_u P_v g\le\delta_u g+\eta B_{uv}\delta_v g$, by first changing the argument then the conditional law. Also $\delta_v P_vg=0$. If there are $N$ chambers, put $Q=N^{-1}\sum_v P_v$ and $T_t=e^{-Nt}\sum_{k\ge0}(Nt)^k Q^k/k!$. Summing this oscillation inequality gives, componentwise,
\[
          \delta T_tg\le \exp[-t(I-\eta B)]\,\delta g .
\]
The row and column sums of $\eta B$ are $8\eta<1$. For each finite torus the sum of oscillations therefore tends to zero, so $T_tg$ converges uniformly to $\rho g$ by invariance. Integrate $-d\,\rho(FT_tg)/dt$ from zero to infinity. Conditional expectation is an orthogonal projection and the single-chamber Poincaré bound applies to $F$. Consequently
\[
 |\operatorname{Cov}_\rho(F,g)|
 \le \sum_v b_v\,\big(C_H\,\rho\!\sum_{a\in v}|\nabla_a F|^2\big)^{1/2},
 \qquad b=(I-\eta B)^{-1}\delta g .                                    \tag{14}
\]
Indeed each term under the time integral is
$\rho[((I-P_v)F)((I-P_v)T_tg)]$ and its second factor is bounded by $\delta_v T_tg$. For a unit component $g$ of $S$, only its central chamber $v_0$ has oscillation, at most $2\kappa$. Expanding the inverse in paths gives $\sum b_v\le 2\kappa/(1-8\eta)$ and $b_v\le 2\kappa(8\eta)^{d(v,v_0)}/(1-8\eta)$. Weighted Cauchy–Schwarz in (14) thus gives squared-gradient weights decaying in chamber distance.

To lift (14), set $F=\mathbb E[f\mid z,Y,V]$. For a fine link $a$ of chamber $v$, differentiation as in (11) adds to the mean of $D_af$ a covariance of $f$ with the sum of the incident corridor forces. This force, in any unit direction, is bounded by $L_0(\beta+20\kappa)$ since only original factors reading $a$ are differentiated. Given the chambers, the at most eight incident corridors contain a bounded number $O(L)$ of links. Their joint conditional density has a max/min ratio bounded solely in terms of $L$ by the original oscillation and incidence bounds. Its Poincaré constant is therefore bounded, by comparison with product Haar. Integrating the other independent corridors first and applying Jensen gives
\[
 |\nabla_a F|^2\le C_L\,\mathbb E\!\left[
 |\nabla_a f|^2+\sum_{e\ {\rm in\ corridors\ incident\ to}\ v}|\nabla_e f|^2
 \,\middle|\, z,Y,V\right].
\]
All differentiations concern compact, positive finite integrals. The support of $S$ is inside $v_0$, so conditional on $Y,V$ the covariance of $f$ and $S$ equals $\operatorname{Cov}_\rho(F,S)$. Every link in $v$ or its incident corridors has original distance at most $8P(d(v,v_0)+3)$ from $c$, and each chamber has at most $4(2P)^4$ fine links. Inserting the last estimate into (14), taking the supremum over unit score components, and then averaging over $Y$ proves
\[
 \|\operatorname{Cov}_{\nu_V}(f,S-\nu_V(S\mid Y))\|^2
 \le \sum_{e\notin E}\exp\!\left(A_L P^4-\frac{\log 4}{8P}\,d(c,e)\right)
                         \nu_V|\nabla_e f|^2 .                          \tag{15}
\]
Here $A_L<\infty$ can be chosen independently of $M$ and the periods. Indeed the only $P$-dependent prefactors are $e^{2H}$ and a polynomial of degree at most four from the chamber size. All other factors in (14) and the lift depend only on $L$ and fixed numerical bounds. The rate uses $8\eta=1/4$. The proof gives the corresponding conditional inequality for every $Y$, as well as its displayed full-posterior version.

**PROVED (simultaneous limit).** For a separation $r$ take $M=\max(40,\lceil r^{1/6}\rceil)$ and the same fixed $L$, on tori with shortest side at least $3P$. The conditioned fraction is $O_L(r^{-1/6})$. At distances at least $r$, the individual weights in (15) are at most $\exp(-c_L r^{5/6})$ for sufficiently large $r$, since the positive exponent is $O_L(r^{2/3})$. This is a per-link bound for the score component corresponding to that choice of $E$. It gives a two-sample covariance estimate in a connected four-dimensional free region while the fraction held fixed tends to zero. The choice of $E$ depends on $r$ in this last conclusion.


## Two sampled boundaries and the remaining sparse data

**PROVED.** There is also a total-variation estimate without the chamber Poincaré prefactor in (15). Fix $Y,V$. Prescribe two arbitrary sets of values on the chamber shell at graph distance $k$ from $v_0$. In the ball strictly inside the shell, the possible laws of the *whole* central chamber have total-variation diameter at most
\[
                       d_k=\frac{(8\eta)^k}{1-8\eta}.                    \tag{16}
\]
Here and below a diameter bound can always be truncated at one. For a proof, start with independent draws from the two conditional chamber measures. At each common random choice of an interior chamber, resample by a maximal coupling of the two one-chamber laws. These positive finite-dimensional laws admit the coupling obtained by first taking their common density minimum and then their residual densities. Both marginals stay stationary. Differences in several neighbours cost at most $\eta$ per differing neighbour, by changing them one at a time in (13). If the ball has $N'$ interior sites, the vector of disagreement probabilities at the next update is bounded by
\[
 \big[(1-1/N')I+\eta B_{\rm int}/N'\big]p
       +(\eta/N')B_{\rm int,shell}\mathbf 1 .
\]
The first matrix has row sum at most $1-(1-8\eta)/N'<1$. Iteration and the geometric series bound the limiting upper disagreement at $v_0$ by the sum of the weights $\eta^j$ of walks that first hit the shell, with any overcount from ignoring the first-hit restriction harmless. All such walks have $j\ge k$ and at most $8^j$ choices. Total variation of the stationary central marginals is bounded by the disagreement of each coupling. This proves (16). In particular it bounds the two-sample distance with the supremum over all central tests *inside* the mean.

For the true posterior at fixed $V$, let $B$ denote any observations of fine links beyond the interior region and its incident corridors, disjoint from the interior factors and lying on or beyond its separating chamber shell. Let $Y_0$ be the fine links of $E$ occurring in the factors that meet the interior chambers or their incident corridors. At fixed $Y_0$ and fixed shell chambers, integrating those corridors gives exactly the interior measure used for (16). Other fine observations outside this region can only change the distribution over the shell chambers. Thus for any regular conditional versions on the sampled data, and independent draws $b,b'$ of $B$ under $\nu_V$,
\[
 \mathbb E_{b,b'} d_{\rm TV}\!\left({\cal L}(z_{v_0}\mid b,V),
                                      {\cal L}(z_{v_0}\mid b',V)\right)
 \le d_k+\mathbb E_{b,b'}d_{\rm TV}\!\left({\cal L}(Y_0\mid b,V),
                                            {\cal L}(Y_0\mid b',V)\right). \tag{17}
\]
Indeed maximally couple the two conditional $Y_0$ laws. On common values the two central laws are mixtures of laws of diameter $d_k$, so their distance is at most $d_k$. On differing values use one. The same argument, or direct conditioning, gives the bound $d_k$ when $Y_0$ is fixed first and the two distant observations are then drawn independently. Quantifiers in (17) keep the difference between these experiments.

**PROVED (size of the pinned set).** For a fine separation $r$, take $M=\max(40,\lfloor r/(\log r)^2\rfloor)$ at large $r$, and $k=\lfloor r/(16P)\rfloor-3$. The interior, shell and the finite factor collars needed for $Y_0$ then fit within fine distance $r$ of $c$, with room to spare by the bound $8P(k+3)$ and the fixed factor range. Take fine periods at least $4r$. All readings at distance at least $r$ qualify for $B$, and $B$ is disjoint from $Y_0$. There are $O((k+2)^4)$ cells in the required region including its collar. In any cell at most $O(LP^3)$ anchored sites lie in a coordinate gap, before removing the free corridors. Thus $|Y_0|=O_L(r^3(\log r)^2)$, counting all four link directions. The global fraction pinned is $O_L((\log r)^2/r)$ and the first term of (17) is at most $\exp[-c(\log r)^2]$ for large $r$. These are statements about the conditional experiment at $\beta=\kappa\in[2,3]$. Estimating the second term in (17) requires the distribution of the sparse pins.


## Testing the unconditioning step

**PROVED (a sparse exterior can retain a macroscopic covariance).** This comparison is a Gaussian field with a marked site observable. It tests the inference from screened interiors and small density to full mixing. Use the scalar field on the periodic $N^4$ lattice with precision $m_N^2-\Delta$, where $m_N=N^{-2}$, and mark $s=\phi_0$. Let $f=N^{-4}\sum_x\phi_x$. The constant vector is an eigenvector of the precision with eigenvalue $m_N^2$. Therefore
\[
                         \operatorname{Cov}(f,s)=\frac1{N^4m_N^2}=1.     \tag{18}
\]
A full estimate of form (1) for this marked observable, with uniformly exponentially decaying mean weights, would bound the square of (18) by $C N^{-8}$ since every partial derivative of $f$ is $N^{-4}$.

Use the chamber geometry for sites and centre the mark in a chamber. Given the pinned sites, the covariance on the free sites $D$ is the inverse $G_D$ of the restricted precision, by completing the square. This is the killed-walk representation used in row 836, Proposition GFF. Explicitly, with $A_D$ the adjacency matrix on $D$,
\[
              G_D=(8+m_N^2)^{-1}\sum_{j\ge0}\big(A_D/(8+m_N^2)\big)^j.
\]
From every free site a path of at most $s_0=8P+8$ steps moves all four coordinates into their cell gaps and reaches a pinned site. A simple walk can follow such a specified path until its first hit, with probability at least $8^{-s_0}$. The row sum of the killed walk after $j$ steps is at most $(1-8^{-s_0})^{\lfloor j/s_0\rfloor}$, by conditioning every $s_0$ steps. Consequently $\sum_x G_D(0,x)\le s_0 8^{s_0}/8$. For fixed $P$ the same series started at $j\ge d(0,x)$ gives exponential decay of individual entries, since shorter walks cannot reach $x$. Gaussian integration by parts conditional on the pins expresses the covariance with the centered mark as $\sum_xG_D(0,x)\mathbb E[\partial_x f\mid Y]$. Thus each fixed geometry has the conditional score-type gradient bound, and
\[
       \big|\operatorname{Cov}(f,s-\mathbb E[s\mid Y])\big|
                        \le \frac{s_0 8^{s_0}}{8N^4}.
\]
One can even let $P=L+40+\lceil\sqrt{\log N}\rceil$. The pinned fraction tends to zero while $s_0 8^{s_0}=N^{o(1)}$. By (18) the covariance with $\mathbb E[s\mid Y]$ then tends to **one**. This is a separation for the inference about a marked field. The Gaussian mark is a site field, and the Wilson Q2 mark is the contour score in (1).

**PROVED (bounded separated readings in the same comparison).** Write $G$ for the periodic covariance. Its diagonal is less than 3, uniformly for $N\ge8$. In Fourier variables the zero mode contributes one. In the shell $\max_j|k_j|=h\ge1$ there are at most $(2h+1)^4-(2h-1)^4\le80h^3$ representatives and the precision eigenvalue is at least $16h^2/N^2$ by $\sin(\pi h/N)\ge2h/N$. The nonzero-mode contribution is at most $5N^{-2}\sum_{h\le N/2}h\le5/4$. By (18) the mean over $z$ of $G(0,z)$ is one, and $|G(0,z)|\le G(0,0)$. Fewer than an eighth of the sites have periodic maximum distance less than $N/8$. If all the other covariances were below $1/2$, their total mean would be below $3/8+1/2<1$. At some $z$ of distance at least $N/8$ the two local bounded readings therefore satisfy
\[
        \operatorname{Cov}(\sin\phi_0,\sin\phi_z)
         =e^{-G(0,0)}\sinh G(0,z)\ge e^{-3}\sinh(1/2)>0 .
\]
The equality follows by subtracting the Gaussian cosine characteristic functions of the sum and difference. Conditional on the sparse pins the corresponding covariance is bounded by $|G_D(0,z)|$, or zero at a pinned $z$. Indeed the same cosine formula with the conditional means has derivative of modulus at most one in the cross covariance between zero and its actual value, because the sum of the two variances is at least twice the modulus of that value. At zero cross covariance the conditional covariance vanishes. The killed-walk tail starting at $j\ge N/8$ bounds $|G_D(0,z)|$ by $(s_0 8^{s_0}/8)(1-8^{-s_0})^{\lfloor N/(8s_0)\rfloor}$, which tends to zero for the above $P=O_L(\sqrt{\log N})$. Total covariance then puts a strictly positive separated signal in the conditional means on the sparse exterior. This test uses bounded observables at individual sites.

**PROVED (strength of the last term of (17) on general laws).** Let a core bit be fair and independent of a fair bit $H$ and of all noises. Generate the wall and distant bits by flipping $H$ independently with probability $0<p<1/2$. The core distance in (17) is zero. Direct conditioning on the distant bit gives an averaged wall distance of $(1-2p)^2/2$, since two distant draws differ with probability $1/2$. All eight joint cell probabilities of the three observed bits are positive. A small wall distance is therefore a genuinely stronger demand than a small core distance on general positive probability laws. This example supplies no Wilson comparison.

**ARGUED (where the Wilson attempt stops).** In (17) the comparison of chamber laws uses identical nearby fine wall data. A resampling of the far observations also changes the distribution of those walls. The pinned links retain plaquette holonomies because an entire fine plaquette fits inside the intersection of two gap slabs away from the corridor mouths. Replacing the wall by its density or by a pure gauge frame loses such observations. Applying (2) to isotropic radius-$i$ cubes is one concrete next test. The direct density comparison for a cube costs $\exp[C(1+i)^4]$, since it bounds all touching log factors separately. The trivial increment estimate $\|b_i\|\le2\kappa$ then gives no decay for (4). The two-scale expression to bound is the actual conditional cost (2), or, for the TV route, the second mean in (17) for the true sparse-wall marginal and the consumer's two independent distant data. Equations (9) and (15) control fluctuations on the other side of this decomposition. I have no estimate for these remaining four-dimensional Wilson quantities. The residual in (17) still asks for mixing across a physical separation, so it does not clear WB2. Its selectivity required by WB3 is also open.

**PROVED scope of the component.** The arguments for (5)–(17) use bounded smooth finite-range interactions, compact spins with a one-spin Haar Poincaré inequality, and a fixed bound on the coordination number. They apply as written at every fixed finite coupling after changing the local constants, including the gapped twin at $\beta<2/9$. On $U(1)$ the Haar inequality follows from the same geodesic argument on the circle. In five dimensions each chamber has ten neighbours. Choosing the corridor length so that $\eta\le1/40$ restores the same contraction, with the corresponding five-dimensional factor count and chamber volume. Thus the component does not distinguish weak 4D compact $U(1)$ or weak 5D $SU(2)$. The local-to-global implication (4) is sufficient for (FL) only. I cannot establish that its hypothesis selects 4D Wilson $SU(2)$, or establish an equivalence with the seed on the prescribed trajectory. The exterior transfer proved using (11) is an explicit equivalence for (FL). The estimates in (8), (9), (15) and (16) are unconditional theorems for the stated parts, with the exterior conditioning included. A correlated neutral spectator can still transmit its slow modes through the exterior, as (18) illustrates.

**ON FILE.** Rows 1568 and 1574 give the bare strong-coupling cylinder bounds below $2/9$. Row 1573, with the periodic Villain and positive-mixture inputs of row 1565, bounds the half-turn-projected purity of sufficiently weak compact 4D $U(1)$ by less than $1/2$ at the stated aspect. No such comparison theorem for the interacting weak 5D theory is used here. The constants of the fixed-band proof above also do not supply a uniform estimate with $\beta=\beta_K\to\infty$ on the four-dimensional calibrated tori.

RESULT — **(d), by hand.** For the actual one-step Q2 posterior at $\kappa=\beta\in[2,3]$, (8) and (9) give exponential gradient weights for a nonzero part of every directional score. Equations (15)–(17) extend screening to a connected region winding in all four directions with a conditioned fraction tending to zero. At separation $r$ the two-sample TV error at *common* sparse wall data is at most $\exp[-c(\log r)^2]$. The next component is the wall-law term in (17), or the transverse cost (4) for the gradient route. Full (W-mix), (PUR-io) and the mass gap remain open. The new results have hand proofs by the author. No computation enters the proofs. They have not received a Lean or independent check.
