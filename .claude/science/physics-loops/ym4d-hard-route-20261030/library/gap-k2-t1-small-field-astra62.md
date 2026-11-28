# Repo search

Row 1472, Codex, checkout `1e98ddff456c`. Research text, author only, with no status assigned. The outline and complete account are the supplied source bundle at `31a47c543775`. The target-specific prior file was absent. The five local refs searched were `origin/main` (8b11ae2bb95e), `pr/10114` (f76f6c649cff), `pr/10133` (89faef229ff6), `pr/10134` (1e70c7211a2c) and `pr/10141` (c73ad7b177d9).

- A full-ref Markdown/TeX search for `Q2[_ -]kappa|K2-STEP|gap-k2-t1-small-field|gap-k2-floor-sizing|corner bases|plaquette Hessian readout|per-block remainder constant` returned no lines. Broader bounded searches used one-loop drift/shift, block-spin coupling, soft-pin Hessian, small-field Taylor remainder, cubic vertex and absolute majorant.
- On PRs 10114 and 10133, `ym4d-proof/FLOW.md` 31–46, 576–594 gives the normalisation $u=2N/g_{\rm std}^2$ and coefficient $11N^2\log L/(12\pi^2)$. Its flow uses a different soft chain. Main's `outputs/scale_ladder_continuations_review_2026_10_18/heat_kernel_saddle_versus_wilson_one_loop_lambda_ratio_2026_10_18_full_argument.md` 24–44 compares the heat-kernel and Wilson lattice actions, including the Wilson quartic tadpole. Lines 107 and 120 give the free plaquette projector calculation used below. The two B12 copies record the same scheme change.
- Main's `research/ym4d/library/ym4-assembly.md` 266–286 locates the hard-route quadratic extraction and polymer estimates. The earlier search record `prior/repo-search-2026-11-08.md` 401–422 distinguishes equality of flat fibre minima in FP1 from identification of the nonlinear maps. In the local registry, H-OL concerns the hard-chain finite part, and H-SF is the hard-route formation bound, with error $C_f\theta^{-1/2}(\log\theta)^{p_0}$ under its presentation hypotheses. No ownership match for Q2/T1 was found.
- Row 1468 §§3.2, 4.2–4.4 defines the 384-contour quaternion mean, strength $\kappa=ax$, the weighted real norm, centre readout and (DR). Row 1469 §3 establishes the flat readout $x'=x$ in four dimensions and already exhibits smooth real-norm perturbations with unbounded Hessian. Row 1470 §§3–5 records Bałaban's existential cuts and an extremely high release-specific floor. Its side-two estimates for $c_1$, $K$ and the cut are guesses. Row 1469 also locates closed classes for different maps in rows 1345 and 1348. [Q2 design](gap-k2-tool-design-fable.md) · [Gaussian and class check](gap-k2-tool-design-check-astra62.md) · [Floor sizing](gap-k2-floor-sizing-opus.md)
- Main's `research/ym4d/library/out-pi.md` 827–842 identifies the Wilson Hessian at the identity with the curl form. The companion `out-gw.md` 1015–1029 gives an $O(\alpha r^3+r^4)\ell^{-4}$ local action estimate under its smooth background and gradient hypotheses. On PRs 10114/10133, `ym4d-proof/BFT_B.md` 352–359 identifies a soft cubic vertex $\kappa\langle r_l,\rho_l^{(2)}\rangle$ carrying the residual of that soft chain. The period-two fields below vary the Wilson action while fixing every Q2 contour.
- The method search also used `period.two`, `staggered`, `singleton`, `Wilson quartic`, `cos^3 ... sin^3` and the two-link identity. PRs 10114/10133, `ym4d-proof/RESIDUAL_FULL_COLOUR_ASTRA.md` 219–235, give FC18, the stationary all-Cartan quartic of their soft chain. The cubic exchange from two commuting external inputs vanishes there. The present test varies fine fluctuations at fixed coarse data. The focused five-ref search found no singleton bound for these fields. The broad staggered-plaquette hits concern central eta signs. Searches of the outline and account indexes for the arithmetic contour mean and side-two drift returned no rows.

The outline index at QC1 (chunk 07), RF9–RF11a (chunk 19) and the B3 entry in `obligations.md` distinguishes the average from its coupling calculation. Outline 7957–7976 defines the nearby mean by the averaged logarithm. Outline 20348–20363 says the value requires “the actual lattice trace calculation.” RF10 allows a bounded cumulative finite part. Outline 3986–4004 states the weaker nonlinear error $Cx^{-1/2}(\log x)^p$ for one component of B3 and requires a separate proof for a stronger error. CA-I 3897–3939 cites Bałaban for the corresponding partial-sum law. CA-I 4031–4045, 4084–4101 marks the unmarked error proof incomplete at its domain comparison. The local source ledger `lit-balaban.md` 139–147 records Bałaban’s regular-orbit estimates and the hypotheses of UV stability. The quotations from CMP 109 p. 259 and CMP 122 pp. 175, 185 in row 1470, lines 85–113, leave the cutoff and coupling ceiling existential. The one-step sign and error for the arithmetic Q2 mean require additional estimates.

## Result for row 1472

**Proved for the pointwise version of row 1470’s estimate.** With a Gaussian subtraction in fine-link logarithms, a one-plaquette Boltzmann bound on hot blocks and the star-connected absolute polymer test, a side-two step already fails a necessary estimate at $x=2{,}560{,}000$. Allowing the remainder to decay as $x^{-1/2}$ still gives this floor. Requiring $c_1/x$ makes every finite uniform $c_1$ impossible. Even the weaker test using only face neighbours fails at $x=20{,}000$. If one permits a cubic counterterm, a separate commuting field still forces $X>12{,}500$ for the star test.

All these tests use the bare SU(2) Wilson rule, inside the small-field region, with every contour of Q2 exactly equal to the identity. The cost comes from taking a supremum before fine-field integration. The bond kernel itself admits the explicit real plaquette cut $1/2$ and a complex link neighbourhood given below. The bounds hold for every fixed strength ratio $a>0$. The integrated return radius and readout error $K$ remain open.

The plan saved at creation was to check prior ownership, identify the map and readout, derive the first binding constant, and record what it decides.

## The block estimate and its singleton condition

**Definition.** Use the side-two map of row 1468 §3.2. From the corner $2y$, an offset path in a chosen axis order is followed by two steps in direction $\mu$ and the inverse of the translated offset path. The 16 offsets and 24 orders have equal weight. Write $M_c$ for the quaternion average of their transporters. At $\kappa=ax$, $a>0$, the bond factor is $\exp(\kappa\operatorname{Re}(M_c V_c^{-1}))/F(\kappa|M_c|)$, where $F(w)=\int_{SU(2)}e^{w\operatorname{Re}q}\,dq$ for normalized Haar measure. The readout in (DR) is the transverse $k^2$ coefficient of the centre’s action Hessian. The test configurations have $M_c(W)=1$ on every coarse bond. The soft kernel equals its flat-input value on this level set, and its fine-field integral includes all other configurations as well.

**Pointwise estimate tested.** Use the absolute star-connected expansion considered in row 1470, Step 5. Assign the six plaquettes with ordered axes $i<j$ based at each of the 16 sites to its block. Write $S_B=x\sum_{p\in B}(1-\operatorname{Re}U_p)$ for their Wilson action. Declare a block hot if some assigned plaquette has chord $|U_p-1|\ge s$, where the cut $s=s(x)$ is free. The following choices specify the estimate.

1. On a cold block bound the Wilson factor relative to a vacuum constant and a quadratic in fine link logarithms by $z_S=\sup|e^{-R_B}-1|$, *before* averaging the fine fluctuations. Here $R_B$ is the block Wilson action minus the chosen polynomial. Its coefficients may depend on $x$ and the coarse background. We test $V=1$. The soft factor can be kept exact on both test fields below. Retaining the full Wilson plaquette term in the reference would change this estimate.
2. For a hot block use the single-block sup of its assigned Boltzmann factor, dropping all other costs. A single hot witness gives

   $$
   z_H=\sup_{B\ {\rm hot}}e^{-S_B}=e^{-xs^2/2},\qquad 0<s\le2.
   $$

   Indeed $1-\operatorname{Re} U_p=|U_p-1|^2/2$. Equality is possible locally. Take $B=\{0,1\}^4$ and one nonidentity $\mu$-bond starting at $2e_i$, $i\ne\mu$, of chord $s$. Only the $(i,\mu)$ plaquette based at $e_i$ is affected among the plaquettes assigned to $B$. Neighbouring blocks can also pay. This is an exact supremum of the *assigned weight*. A posterior hot probability additionally involves the normalization of the fine integral.
3. Feed these homogeneous majorants into the absolute Kotecký–Preiss criterion with touching blocks incompatible, including self-incompatibility. This tests a concrete version of (F1)–(F2). The estimate compares Wilson factors with respect to the same Haar measure at this stage. The weight $1+\theta x E_X(V)$ in row 1468 equals one at $V=1$ on every coarse support. Haar, gauge fixing, and integration may instead be used to change the majorants. The outline proves the combinatorial theorem under its activity hypothesis at 1150–1166, 1271–1279, 1357–1375.

**Singleton constraint, proved.** It suffices to test the periodic sector on arbitrarily large even fine tori. On coarse tori with each side at least four, there are $D=3^4=81$ incompatible translates of a singleton, including itself. Retaining only those terms of one type gives $D z e^u\le u$ for a common KP weight $u$. Even allowing site-dependent weights, use the singleton with least weight on the torus. The derivative of $u e^{-u}$ is $(1-u)e^{-u}$. Thus $u e^{-u}\le1/e$, and both assigned majorants must obey $z_S,z_H\le z_*:=1/(81e)$. The KP weight $u=1$ attains this ceiling for this one-type singleton inequality. Larger polymers, both types together, and range reserves can tighten it. Hence
$$
 xs^2\ge 2\log(81e),\qquad
 \operatorname{osc}_{B\ {\rm cold}}R_B\le L_*:=\log\frac{1+z_*}{1-z_*}.
$$
The second bound follows from $1-z_*\le e^{-R_B}\le1+z_*$ for the real action.

Two bounds used below follow by hand. First, $e>1+1+1/2+1/6+1/24=65/24$, so $81e-1>218$ and
$$
 L_*=\log(1+2/(81e-1))<1/109 .
$$
Second, $\log3=2\int_0^{1/2}(1-u^2)^{-1}du>1+1/12+1/80$ by retaining three terms of the geometric series. Hence $2\log(81e)=2+8\log3>43/4$, and $2\log(9e)=2+4\log3>19/3$.

## The cubic Wilson term at a flat Q2 mean

**Proved.** The Wilson action has a cubic term on a level set of the Q2 means. It survives every quadratic subtraction in fine-link logarithms and the Haar Jacobian in block tree gauge.

Regard fine-site parities as the 16 vertices of the unit four-cube. Label each unoriented edge with a group element in its orientation from bit 0 to bit 1. At a fine site of parity $n$, use that label for a positive link if its longitudinal bit is 0 and the inverse label if the bit is 1. This produces a period-two fine configuration. Every length-two axial line has product 1. The two offset legs of every Q2 contour are translates by two with opposite traversal, so each contour has product 1, including for noncommuting edge labels.

Use the $(3,4)$ squares at the three values $(n_1,n_2)=(1,0),(0,1),(1,1)$. On each, follow the oriented boundary from $(n_3,n_4)=(0,0)$, first in direction 3. Set its four successive oriented labels to $e^{It},e^{Jt},e^{Kt},1$ for quaternion units $IJ=K$. Use identical labels on the three squares. Give every other cube edge the identity. The block tree follows axes in decreasing order from the corner. Its edges have identity labels, since every marked edge has a nonzero lower coordinate.

Each selected face gives four assigned plaquettes per side-two block. Starting at a different corner cyclically permutes or reverses the boundary, preserving its real part because the holonomy is unitary. On each selected face the real part of the ordered product is $\cos^3t-\sin^3t$, since $IJK=-1$ and each product of two distinct units has zero real part. A plane with one transverse direction compares two copies of the same edge label, or a copy with an identity edge. Its real part is 1 or $\cos t$. The remaining planes are flat. Thus precisely the 12 selected plaquettes contribute the odd part
$$
 \tfrac12\big[S_B(t)-S_B(-t)\big]=12x\sin^3t.
$$
The local Haar densities are even in $t$ by the radial formula below, and the soft pin is exactly constant. Every fine logarithm is linear in $t$ for $|t|\le1/2$. For **any** vacuum, linear and quadratic subtraction the odd part of the residual therefore equals $r_o(t)=12x\sin^3t-bt$. If $O$ is the oscillation of the residual on $[-T,T]$, then $|r_o(t)|\le O/2$. Eliminating $b$ at $T,T/2$ gives
$$
 O\ge 8x\big[\sin^3T-2\sin^3(T/2)\big]\ge \tfrac92 xT^3,\qquad 0<T\le1/2.
$$
For the last inequality $\sin T\ge T(1-T^2/6)\ge(15/16)T$, $(15/16)^3>13/16$, and $\sin(T/2)\le T/2$.

The largest squared chord along these fields is at most $(3+2T)T^2$. Indeed $\cos^3t\ge(1-t^2/2)^3\ge1-3t^2/2$ and $|\sin^3t|\le |t|^3$. The other nontrivial plaquettes have chord at most $|t|$.

- **Star incompatibility.** Take $x=1600^2=2{,}560{,}000$ and $T=3/(2\sqrt x)$. Since $T<1/2$, every chord is at most $2T=3/\sqrt x<s$ by the hot singleton constraint $xs^2\ge2\log(81e)>9$. The residual oscillation is at least $243/(16\sqrt x)=243/25{,}600>1/109$, since $243\cdot109=26{,}487$. This contradicts $O\le L_*<1/109$. A uniform floor for this Gaussian pointwise estimate must satisfy **$X>2{,}560{,}000$**. More strongly, the same $T$ for arbitrarily large $x$ gives $z_S\ge\tanh(243/(32\sqrt x))$. Consequently **no finite $c_1$** can make $z_S\le c_1/x$ on this raw small-field region. In a $1/\sqrt x$ estimate its asymptotic prefactor is at least $243/32$.
- **Even if only face neighbours are declared incompatible**, the more permissive singleton test has $D=1+2\cdot4=9$. At $x=20{,}000$ choose $T=1/100$, so $xT^2=2$. Every plaquette satisfies $x|U_p-1|^2\le 2(3+2/100)<19/3$. The hot constraint gives $xs^2\ge2\log(9e)=2+4\log3>19/3$. The height is at least $(9/2)xT^3=9/100$, whereas $\log((9e+1)/(9e-1))<2/(9e-1)<2/23<9/100$, using $e>8/3$. This still forces **$X>20{,}000$**. The true Q2 dependencies may require a larger incompatibility neighbourhood.

## The even remainder after cubic subtraction

**Proved by hand, author only.** A commuting family tests the even part of the Wilson action on the same level set $M_c=1$. Number the axes from 1 to 4. Fix an imaginary quaternion $I$ of unit norm and set
$$
A_\mu(n)=(-1)^{n_\mu}\sum_{i<\mu}\frac{1-(-1)^{n_i}}2,\qquad W_\mu(n;t)=\exp(I t A_\mu(n)).
$$
These links have period two and commute. Opposite legs of every contour cancel by translation by $2e_\mu$, and the two middle links cancel since $A_\mu(n+e_\mu)=-A_\mu(n)$. Thus $M_c=1$ for all $c,t$, and the normalized soft kernel takes exactly its flat-field value at every strength and every coarse field. For $i<\mu$, the plaquette angle is $t(-1)^{n_i+n_\mu}$, by taking the forward difference of $A_\mu$ in $i$ and observing that $A_i$ is independent of $n_\mu$. The axis tree that completes the axes in decreasing order already has identity transport because all lower coordinates are even on its $\mu$-edges. Each side-two block therefore attains $96x(1-\cos t)$ in Wilson action. Every quadratic form in these fine link logarithms restricts to a multiple of $t^2$. The construction works on every even torus down to arbitrarily small plaquette deviations.

**Best pointwise subtraction on this curve, proved.** Write $y=t^2$ and $f(y)=96x(1-\cos\sqrt y)$. After restricting any polynomial of degree at most three in link logs to the displayed curve, average at $t$ and $-t$. This removes its linear and cubic parts and keeps the residual in the same real interval. The remaining subtraction is $b+qy$ for arbitrary $b,q$. For any $0<T\le1$ with $T\le s$, the chord at $|t|\le T$ is $2\sin(|t|/2)\le |t|$, so these values may be tested by continuity. At $y=0,T^2/2,T^2$, every affine subtraction cancels from the middle value minus the mean of the two end values. Therefore the oscillation is at least
$$
 H=96x\left[1-\cos(T/\sqrt2)-\tfrac12(1-\cos T)\right]
 \ \ge\ xT^4(1-T^2/15).
$$
For the inequality use $1-\cos v\ge v^2/2-v^4/24$ at the middle and $1-\cos T\le T^2/2-T^4/24+T^6/720$ at the end. The alternating series proves both for $0\le T\le1$.

The exact optimum of the oscillation on this one-dimensional test is the maximal height of $f$ above its secant on $[0,T^2]$. Indeed $f$ is concave there because for $t=\sqrt y>0$, $f^{\prime\prime}(y)=24x(t\cos t-\sin t)/t^3$ and $\sin t-t\cos t=\int_0^t u\sin u\,du\ge0$. The secant attains that oscillation. Subtracting any other affine function leaves each height unchanged relative to the linear interpolation of the endpoint residuals, so it cannot decrease the maximum below that height. With the constant optimized, an oscillation $H_0$ gives best multiplicative error $\tanh(H_0/2)$. At the optimum the extreme ratios are $1-z$ and $1+z$. Their quotient equals $e^{H_0}$, which determines $z$. The lower bound uses only the middle height and survives optimization of all vacuum and quadratic coefficients, even ones depending on $x$.

**Take $x=12{,}500$.** The hot bound above gives $xs^2>43/4$. Thus $T^2=43/(4x)=43/50{,}000<1/1000$ satisfies $T<s$. Consequently
$$
 H\ge \frac{1849}{16x}(1-T^2/15)>\frac{115}{12{,}500}>\frac1{109}.
$$
Here $(1849/16)(999/1000)>115$ and $115\cdot109=12{,}535$. The two necessary inequalities are incompatible. **Even with an arbitrary cubic subtraction, the uniform star-test floor must satisfy $X>12{,}500$.** The test uses the bare Wilson input at the trivial coarse field for every $a>0$. The obstruction arises before the complex-domain and one-loop estimates.

For the notation of row 1470 this also prices $c_1$. Take $T^2=2\log(81e)/x$ for arbitrarily large $x$. The oscillation bound and $z_S\ge\tanh(H/2)$ force
$$
 \liminf_{x\to\infty} x z_S\ \ge\ 2\log^2(81e).
$$
This is a lower bound on $c_1$ in the specific estimate $z_S\le c_1/x$, even allowing cubic refits. Its exact source is the 96 plaquettes, the Wilson quartic, the optimized vacuum subtraction and the hot threshold. For the actual Taylor quadratic with its flat value fixed, the absolute log discrepancy on the curve is exactly $96x(T^2/2-1+\cos T)$. At $T=h/\sqrt{x}$ its leading value is $4h^4/x$. Both bounds apply before integration.

**The same test includes the local Haar Jacobian, proved.** In exponential coordinates normalized at the identity the one-link density is $(\sin u/u)^2$, with $u$ the length of its logarithm. This follows by writing the unit three-sphere metric in radial coordinates, $du^2+\sin^2u\,d\Omega^2$, and dividing by the Euclidean radial volume element. The descending-axis block tree above is already fixed. Haar invariance removes its tree links by successive changes of variables at the nonbase sites, from parent to child. Its Jacobian with respect to product Haar measure is one. All omitted tree logs on the test curve vanish.

Let $g(u)=-2\log(\sin u/u)$. For $|u|\le1/2$,
$$
 |g(u)-u^2/3|\le u^4/30 .
$$
Indeed $1-u^2/6\le\sin u/u\le1-u^2/6+u^4/120$. For $v=u^2/6\le1/24$ the positive tail of $-2\log(1-v)-2v$ is at most $v^2/(1-v)\le u^4/30$. The upper bound on the sine and $-\log(1-w)\ge w$ for $0\le w<1$ give $g(u)\ge u^2/3-u^4/60$.

For a fixed direction $\mu$, $|A_\mu|$ counts the odd coordinates among $\mu-1$ lower axes. The sums of fourth powers over a block in the four directions are $0$, $8$, $4(2+16)=72$ and $2(3+3\cdot16+81)=264$. Their sum is 344. Also $|A_\mu|\le3$. Write $G(t)=\sum_e g(tA_e)$ for the block Jacobian action. Up to a quadratic in $t$ it has absolute value at most $(344/30)t^4$ for $|t|\le T$ at $x=12{,}500$. Thus the Haar contribution can decrease the three-point height by at most $(344/30)(1/4+1/2)T^4<9T^4$. The exact soft kernel contributes zero height. The combined height still exceeds
$$
 xT^4(1-T^2/15-9/x)>\frac{1849}{16x}\frac{999}{1000}>\frac{115}{x}.
$$
This places the conflict in the actual local logarithms of the Wilson, pin and Haar factors before integration. Fixing the block tree and including the Haar term preserve the numerical obstruction.

## An explicit analytic domain for the Q2 bond factor

**Proved for the kernel.** Choose the real fine-plaquette cut $\sigma_{\rm bond}=1/2$ in chord norm on all plaquettes used by a contour strip. Let $S$ be the straight transporter. Moving the two straight steps across the offset path uses two elementary plaquette swaps for each transverse offset bit. A swap in direction $\mu$ costs zero. Comparing products one swap at a time conjugates the plaquette by unitary transport. The bi-invariant angle distance on the unit three-sphere satisfies the triangle inequality. With $j$ transverse bits set, the angle between the contour and $S$ is therefore at most $2j\alpha$, where $\cos\alpha=1-\sigma_{\rm bond}^2/2=7/8$. Since $7/8>\sqrt3/2$, $6\alpha<\pi$. All orders of the legs have this bound. The multiplicities of $j$ give
$$
 \operatorname{Re}(M_c S^{-1})
 \ge 2^{-3}\sum_{j=0}^3\binom3j\cos(2j\alpha)
 =\cos^3\alpha\cos(3\alpha)=\frac{2401}{65536}>\frac1{32}.
$$
The identity takes the real part of $[(1+e^{2i\alpha})/2]^3$. Hence every real mean here has quaternion norm at least $1/32$.

There is also a numerical complex neighbourhood. Write each fine link as $W_e^0\exp Z_e$ about one of these real backgrounds, with $Z_e$ traceless complex and
$$
 \|Z_e\|_{\rm op}<\epsilon:=\tfrac1{10}\log(129/128).
$$
A contour uses at most ten links. Telescoping the product about its unitary factors bounds its change by $e^{10\epsilon}-1=1/128$, including reversed links. Averaging gives the same bound for $M-M_0$. Since a real quaternion matrix has both singular values equal to its norm, $\|M_0^{-1}(M-M_0)\|<1/4$. For any such $2\times2$ matrix $E$, $|\det(1+E)-1|\le2\|E\|+\|E\|^2<9/16$. Hence $\operatorname{Re}\det M>0$ on the tube.

The normalization is zero-free there at every $\kappa>0$. With normalized sphere measure put $F(w)=\int_{S^3}e^{w q_0}dq$. It is entire by compactness and even by reflection of $q_0$. The average of the plane exponential over rotations solves $\Delta f=w^2 f$ in four Euclidean dimensions, so $f(r)=F(wr)$ satisfies $(r^3f')'=w^2 r^3f$ and $f(0)=1$. If $F(w)=0$, integration against $\bar f$ on $[0,1]$ gives
$$
 w^2=-\frac{\int_0^1 r^3|f'|^2\,dr}{\int_0^1 r^3|f|^2\,dr}<0.
$$
The boundary terms vanish by regularity at zero and $f(1)=0$. The denominator of the Q2 bond is the holomorphic continuation $F(\kappa\sqrt{\det M})$ by the unit-quaternion formula on the real slice. The numerator uses $\tfrac12\operatorname{tr}(M V^{-1})$ there and continues holomorphically as well. This yields the stated cut and tube for one bond. A volume-uniform zero-free domain *after integrating fine fields* remains open.

## What the hot estimate costs

**Proved for the raw large-field majorant.** A set of $m$ hot blocks has assigned Wilson weight at most $e^{-mxs^2/2}$ because their assigned plaquettes are disjoint. The same bound holds for the integral of $\prod_{B}\mathbf 1_{B\ {\rm hot}}e^{-S_B}$ against any probability reference. Marking which fine plaquette is hot adds at most $96^m$ labels.

The same majorants give an explicit bound for a gas of connected hot blocks. The number of star-connected sets of size $m$ containing a fixed block is at most $320^{m-1}$. Choose a deterministic rooted ordered spanning tree. Its parenthesis encoding has length $2(m-1)$, with at most $4^{m-1}$ possibilities. Each tree edge has at most 80 directions. The labelled tree recovers every vertex. A polymer $P$ has at most $81|P|$ blocks in its closed star neighbourhood. Thus for activities bounded by $z^m$, taking KP weight $|P|$ gives the upper bound
$$
 |P|\frac{81 e z}{1-320 e z}\le |P|\qquad\text{if }z\le 1/(401e).
$$
At $s=1/2$ the price is $x\ge8\log(401e)$ without labels, or $x\ge8\log(96\cdot401e)$ with labels. Respectively 64 and 96 suffice. Indeed $e^7>(5/2)^7>401$, and $(8/3)^5>128$ implies $e^{11}>128^2(8/3)>96\cdot401$. This bounds a gas with the stated majorants. Normalization of the coupled fine integral, boundary interactions and mixed hot and cold polymers remain separate estimates. Calling $e^{-xs^2/2}$ a normalized Q2 probability would omit them.

## Which part is structural

**Proved.** For this pointwise Gaussian estimate the cubic is structural. It occurs in the bare SU(2) Wilson action and the normalized Q2 kernel is constant on the exhibited fields for every strength ratio. The numerical floor also uses the choice to spend one block's Boltzmann weight on each hot witness and to test the uniform majorants by the absolute singleton KP inequality.

Write $R=R_e+R_o$ for its even and odd parts at the two antipodal log fields, using an even Gaussian reference. The equal-weight mean of the two Boltzmann factors has logarithm $-R_e+\log\cosh R_o$. For real $u$, $0\le\log\cosh u\le u^2/2$, by integrating $0\le\tanh u\le u$ for $u\ge0$. On the three-face test $R_o=12x\sin^3t$. At $|t|\le h/\sqrt x$ the paired cubic costs at most $72h^6/x$. This explicitly removes the order $x^{-1/2}$ on that test. On the Cartan field the two Wilson weights are identical, so the even quartic persists under this pairing.

There is also a bound for one term after a genuine Gaussian average. Take the centred, linearized three-colour Maxwell model on an even periodic four-cube. Use the counting inner product and $A\in(\ker d)^\perp$ for each colour, which removes the gauge and harmonic zero modes. Write $F=dA$. The covariance of one unpinned colour is $x^{-1}$ times the projection onto exact two-forms (outline 888–897, 1673–1686). Its diagonal is at most $1/(2x)$. Indeed on a torus with $N$ sites the map at every nonzero momentum is exterior multiplication by the nonzero difference covector, of rank three on one-forms. Its rank at zero is zero. Symmetry spreads the trace $3(N-1)$ equally over $6N$ plaquettes. This is the projector calculation used in the repository's heat-kernel/Wilson comparison. Take the linearized Q2 observation $Y$ of $A$ on transverse coarse coordinates, with independent Gaussian noise of variance $1/\kappa$ there. Conditioning at $Y=0$ reduces the covariance. Indeed $F-C_{F,Y}C_{Y,Y}^{-1}Y$ is jointly Gaussian and uncorrelated with $Y$, hence independent. Its covariance is $C_{F,F}-C_{F,Y} C_{Y,Y}^{-1} C_{Y,F}$. The subtracted operator is positive semidefinite. The three colours remain independent and identically distributed. With $v_p$ the conditional variance of one colour, $\mathbb E[|F_p|^4\mid Y=0]=15v_p^2$, since three fourth moments give $3\cdot3v_p^2$ and the three cross terms give $2\cdot3v_p^2$. Therefore
$$
 \mathbb E\left[\frac{x}{24}\sum_{p\in B}|F_p|^4\,\middle|\,Y=0\right]\le\frac{x}{24}\,96\,\frac{15}{4x^2}=\frac{15}{x}.
$$
This is the quartic from $1-\cos|F_p|=|F_p|^2/2-|F_p|^4/24+O(|F_p|^6)$ in the linear curvature, evaluated at zero background. The full logarithm also has the commutator terms, two cubic insertions, the response of the pin and the dependence on the external field. The pointwise obstruction supplies no lower bound on the exact normalized activities obtained after those operations.

**Open.** The cut $1/2$ is established for each bond factor. Joint zero-freeness, a bounded return radius, a full post-integration $c_1$, and the readout error $K$ remain open. Even if the one-step coefficient were exactly $d=11\log2/(3\pi^2)$, using $|x'-x+d|\le K/x$ to prove $\delta_0=d/2$ at $X=100$ would require $K\le50d$. The bounded partial sums in RF10 allow individual increments that differ from $d$. One must control the chosen centre's increment for Q2 or prove a strict lower bound directly. No lower bound on the intrinsic floor of Q2 or its integrated class follows here.

Credit goes to Tadeusz Bałaban for the small-field and large-field renormalization scheme, to Kotecký and Preiss for the activity criterion, and to Ethan Sussman and Levent Alpoge, with Claude and Codex, for the outline, complete account and normalized contour-kernel construction behind Q2. Rows 1468–1470 supplied the map, the Gaussian check and the question about the first surviving remainder. All new proofs above are written arguments by Codex. No Lean computation was used and the arguments await a separate reader.

## Next two rows and their decisive outcomes

1. **Integrated small-field activities for Q2.** Start by checking the two period-two fields against the exact 384-contour definition. Integrate the cubic pair and quartic terms under the pinned fluctuation law before taking absolute values. After extracting vacuum and curvature terms, prove a volume-uniform summable activity bound for $x\ge100$, including normalized hot weights, or give a particular integrated activity that violates the proposed bound. This decides whether the pointwise loss can be removed in a specified norm.
2. **Signed Q2 readout for the returned centres.** For a fixed strength ratio and a specified analytic family of centres containing the Wilson input, enclose the actual one-step transverse Hessian coefficient $b(\Phi)$, including its lattice finite part. A uniform $b(\Phi)\ge b_{\min}>0$ and $|x'-x+b(\Phi)|\le K/x$ with $2K/b_{\min}\le100$ would give (DR) with $\delta_0=b_{\min}/2$. An admissible centre with a nonpositive limiting decrement would rule out uniform strict drift for that family.
