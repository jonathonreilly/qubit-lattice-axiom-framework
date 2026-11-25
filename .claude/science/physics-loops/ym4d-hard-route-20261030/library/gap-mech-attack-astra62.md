# Repo search

Row 1530, checkout `e7c98d99e`. I searched `origin/main` (`8b11ae2bb9`), `pr/10114` (`f76f6c649c`), `pr/10133` (`89faef229f`), `pr/10134` (`1e70c7211a`) and `pr/10141` (`c73ad7b177`) in Markdown and TeX. `PUR-io`, `457/625`, `typical.field stiffness` and `order.one (effective )?coupling` near `mass gap` or `purity` returned no lines. Method searches included `paramagnetic spin`, `spin susceptibility`, `adjoint heat trace`, `covariant shell`, `two-propagator trace`, `two-plaquette coercivity`, `physical-time contraction` and `crossover-window clustering`. The specific covariant-shift commutator/form-bound search returned no lines. Broad searches were capped and followed up on the YM paths.

- PRs 10114 and 10133, `ym4d-proof/MASS_GAP_LOCAL_BLOCK_ASTRA.md`, lines 4–12, 106–149, and `MGX.md`, lines 41–56, give positive one-step plaquette correlation at finite $\beta>0$ and fixed-spacing Doob contraction for $0<\beta\le1/32$. Grok's PR 10133, `MASS_GAP_CROSSOVER_REDUCTION.md`, lines 77–92, requires cutoff- and volume-uniform exponential clustering of gauge-invariant block observables and source transport. PR 10134, `library/mass-gap-interface.md`, I2–I5, requires a common trajectory, blocking and observable sector for that import. None supplies the calibrated trace estimate.
- Main, `research/mass-gap/library/gap-skeleton-max-b.md`, A8, identifies the curvature–bracket term in the nonconvex Hessian. `su2-gauge-aligned-response-20261108/parts/marginal-regional-moments-and-ratios.md`, lines 417–425, takes two-plaquette coercivity as input to a bounded radial-profile comparison. Main and PR 10141, `research/ym4d/library/fp1.md`, Lemma 4, prove $\|da\|^2\le E_k(a)\le256\|da\|^2$ on flat constrained fibres. These are different operators or different laws.
- In this checkout, [row 1141, (2)–(7)](gap-crux2-astra62.md) gives the high-probability Neumann colour gap. [Row 1283, (8)](gap-solve32-astra62.md) bounds the expected norm of the four-dimensional Dirichlet adjoint inverse kernel by $C(1+r)^{-2}e^{-cr/\sqrt{1+\beta}}$. [Row 1244, §3.1](gap-mini-solve-aa-opus.md) proposes applying a cell inverse to a spin source. [Row 1249, §3.4](gap-mini-solve-ac-opus.md) anticipates loss of the bare logarithm. [Rows 1526–1527](gap-agy-seed-approaches-neon-check-astra62.md) establish the flat Gaussian spin logarithm and a Kato upper bound if the torus resolves the shell. The calculation below concerns the signed quadratic spin trace in the actual twisted Wilson ensemble. The target-specific prior is absent. The November 8 digest concerns earlier UV and local-block obligations. Row 1530 has no separate “Repo prior work” entry. The registry assigns R11 and TWO-PER elsewhere. Its only hit for `PUR-io` or the spin-shell terms was TWO-PER.

## Plan saved at entry

1. Read the target-specific prior, the goal and the specified finish rules. Check ownership and the outline index.
2. Search the five requested science refs for the seed, its consumers and the candidate mechanism. Record the exact scope of each relevant result.
3. Follow one uncovered route. Test its mathematical implication, its dependence on the group and dimension, and its fit to the consumer. Record each step here.
4. Check the endpoint against the source and distinguish any proved result from the remaining estimate.

## Source and claim scope

The outline index and its obligations led to Sussman and Alpoge (text authored with Claude and Codex), `YM4_sketch_500.tex` at the supplied revision `31a47c543775`. GL8, lines 2315–2335, represents the untwisted mass as a vertex-projected trace. PX43, lines 10744–10754, supplies the comb strip estimate used below. PX72, lines 10978–10982, gives the scalar subsolution inequality for a unitary connection. Lines 4629–4643 and 31871–31882 require a separate spectral estimate for a gap. CA-I, lines 2704–2712, leaves the gap outside its assertion. The Bałaban results quoted in `lit-balaban.md` concern regular backgrounds and UV propagation. This hand argument imports no order-one Wilson estimate from them. It is research text with no status grant. [Index and chunk map](sa-index/README.md) · [Indexed obligations](sa-index/obligations.md)

## The spin observable on the sixteen Wilson tori

Fix a released odd $b$ and calibration parameter $g_0$ as in check 1453. Fix $\ell\in1024\mathbb N$, put $n=\ell b^K$ and $u=n/512$. For $T$ the Wilson transfer on the spatial $n^3$ torus, $Z^z(v)=\operatorname{Tr}(C_zT^v)$ and $Z_+(v)=\tfrac18\sum_z Z^z(v)=\operatorname{Tr}(P_0T^v)$. The seed asks for $P_K=Z_+(2u)/Z_+(u)^2\ge457/625$ at infinitely many $K$ for one choice of $\ell,g_0$. [Consumer, §3.1](gap-k2-tool-design-fable.md)

Write $d=4$, $v=u$ or $2u$, $\Lambda=(\mathbb Z/n)^{d-1}\times(\mathbb Z/v)$ and $V=|\Lambda|$. Work under each normalized Wilson law with temporal twist $z$. In a periodic representative the action is $\beta A$, with $A=\sum_p(1-\sigma_p\operatorname{tr}U_p/2)$ and $\sigma_p\in\{1,-1\}$ the fixed seam signs. Adjoint transports are periodic. Use $\beta=\beta_K\asymp\log n$ as in the question. Constants may depend on the two fixed aspects and the trajectory constants. The five-dimensional comparison uses the same aspect and number of lattice units per spatial side.

Let $(D_U f)_{x,i}=\operatorname{Ad}(U_{x,i})f_{x+e_i}-f_x$ and $H=D_U^*D_U$ on vertex colours, with each positive-direction bond counted once. Take $m=n^{-1}$, $G=(H+m^2)^{-1}$ and $\Gamma=I_2\otimes G$. The two copies label the polarizations in the 12-plane. Normalize the colour bracket to the cross product. For a field of colour axes $h=(h_x)$ of norm at most one, put $M_h=-2J\otimes\operatorname{ad}h$, where $J$ is the real rotation by $\pi/2$ on the two polarizations and $\operatorname{ad}h$ acts at each site. Both factors are skew, so $M_h$ is symmetric. Define

\[
 X(U,h)=\frac{1}{2V}\operatorname{Tr}(\Gamma M_h\Gamma M_h).
 \tag{1}
\]

At fixed $U,h$ this is the variance per site of $\tfrac12 a^tM_h a$ for a centred Gaussian with covariance $\Gamma$. It is a nonnegative function of the Wilson links and the chosen axes. The calculation uses the two Wick pairings across the two quadratic forms. The Gaussian is a test of the Wilson background. The physical Wilson current has a different law.

For a local choice of $h$, take $q=\lfloor\beta^{1/16}\rfloor$ at sufficiently large $K$. Tile each coordinate by intervals of $q$ sites followed by a one-site gap, discarding the final incomplete interval. At the lower corner $r$ of each cube take the oriented $12$ plaquette $p_r$ and its signed imaginary quaternion part $w_r=\operatorname{Im}(\sigma_{p_r}U_{p_r})\in\mathbb R^3$, in the colour basis just fixed. Choose the bounded curvature vector

\[
 h_r=\frac{\sqrt{1+\beta}\,w_r}{\max\{1,\sqrt{1+\beta}\,|w_r|\}}.
\]

Transport $h_r$ to every site of its cube along the coordinate-ordered tree. Set $h=0$ off the cubes and write $X(U)=X(U,h(U))$. Site gauge transformations conjugate all the operators, and moving a centre seam preserves the signed plaquette and adjoint transports under the corresponding link substitution. Thus this observable uses only the Wilson sample, including for nontrivial twists.

The test is whether this spin response can supply an order-one gain per doubling of the *bare* lattice scale. This would take a contribution of order $\log n$ across the growing range. For the bounded transported plaquette probe, the response has order $\log\beta_K$ with Wilson probability tending to one. Its projection on a Wilson boundary score is tested after (10).

## An upper bound for every choice of axes

**Claim.** In four dimensions, for each fixed $k>0$, outside a set of Wilson probability at most $C_k n^{-k}$,

\[
 \sup_{|h_x|\le1} X(U,h)\le C_k(1+\log(1+\beta)).                 \tag{2}
\]

This also bounds the expectation, with a change of constant. In five dimensions $X(U,h)\le C$ for *every* connection at the stated aspects. In compact $U(1)$ the spin insertion $\operatorname{ad}h$ vanishes identically, while the trace per site of the squared free scalar inverse grows logarithmically.

Use (2) of [row 1141](gap-crux2-astra62.md) on the Neumann cubes of side $v$ that partition $\Lambda$. There are $(n/v)^3$ cubes in four dimensions. Omit also the wrap in a direction where the cube fills the period. The remaining internal bonds give the free-face energy used in that row. Its high-probability lower bound on every cube gives

\[
 H\succeq \frac{c_k}{1+\beta+\sqrt{\log(2+n)}}I\succeq \gamma I,
 \qquad \gamma=\frac{c'_k}{1+\beta}.                              \tag{3}
\]

Here the second inequality uses the lower growth bound on $\beta_K$. The union over cubes costs a fixed factor. The extension to each twist can be made before the union bound. The only law-dependent premise in row 1141, (3)–(7), is the one-link conditional tilt $e^{a\cdot U_e}dU_e$ with $|a|\le6\beta$. Seam signs reverse some of the six staple vectors and preserve that bound. Each test uses two internal plaquettes with distinct private links. Central signs leave their adjoint rotations unchanged. The conditional probability and scalar Neumann inequalities therefore have the same constants. This uses the mass estimate for the colour operator on vertices, with no relation between its eigenvalues and the eigenvalues of $T$ assumed.

For $s>0$ and positive integer $j$, the trace of $(H+sI)^{-j}$ is at most three times the corresponding scalar trace for the ordinary periodic Laplacian $H_0$. Indeed the heat expansion of $H=2dI-\mathcal A_U$ sums nearest-neighbour walks with nonnegative scalar weights, and each closed walk has adjoint trace at most three. Integrate the heat trace against $t^{j-1}e^{-st}/(j-1)!$. If $H\succeq\gamma I$, its spectral calculus gives $\operatorname{Tr}(H+m^2)^{-j}\le 2^j\operatorname{Tr}(H+m^2+\gamma)^{-j}$.

For clarity, define $F_{d,j}(s)=V^{-1}\sum_p(4\sum_i\sin^2(p_i/2)+s)^{-j}$ on the rectangle. For $n^{-2}\le s\le 1$ the number of momenta with $|p|\le r$, divided by $V$, is at most $C(r+n^{-1})^d$. This follows from counting grid points in the coordinate intervals for $-\pi\le p_i<\pi$. The lattice symbol is at least $4|p|^2/\pi^2$. The ball up to $\sqrt{s}$ contributes at most $C s^{d/2-j}$, and each dyadic annulus from $\sqrt{s}$ to order one contributes at most $C r^{d-2j}$. Higher momenta contribute at most a constant. Thus

\[
 F_{4,2}(s)\le C(1+\log(1/s)),\quad F_{4,4}(s)\le Cs^{-2},
 \qquad F_{5,2}(s)\le C.                                           \tag{4}
\]

Finally $\operatorname{Tr}(\Gamma M_h\Gamma M_h)\le\|\Gamma M_h\|_{\rm HS}\|M_h\Gamma\|_{\rm HS}\le \|M_h\|^2\operatorname{Tr}\Gamma^2$, and $\|M_h\|\le2$. Apply (3) and (4). Even on the exceptional event the deterministic four-dimensional bound with $s=m^2$ costs only $C(1+\log n)$. This proves (2) and the expectation bound, uniformly over every field-dependent choice of the axes. The five-dimensional bound uses $s=m^2$ directly.

**Effect on individual long shells.** Replace $G$ in (1) by the actual difference $D_R=(H+R^{-2})^{-1}-(H+4R^{-2})^{-1}$ from row 1526 and call the result $X_R$. On the same event (3), simultaneously for $1\le R\le n$, spectral calculus gives $0\preceq D_R\preceq3R^{-2}(H+R^{-2})^{-2}$. By (4) with $j=4$,

\[
 \sup_h X_R(U,h)\le C_k\frac{(1+\beta)^2}{R^4}.                   \tag{5}
\]

The fourth-power estimate uses $R^{-2}+\gamma\ge n^{-2}$, and a parameter above one is bounded by its value at one. On the exceptional event $D_R\preceq(H+m^2)^{-1}$ gives the same deterministic $C(1+\log n)$ trace majorant. Hence each shell with $R/\sqrt{1+\beta}\to\infty$ has vanishing expected spin response of this form.

The Gaussian trial of row 1526 also reads a trace with only one shell factor. Write $\mathcal D_R=I_2\otimes D_R$. On (3), Hilbert–Schmidt Cauchy–Schwarz applied to $M_h\Gamma$ and $\mathcal D_R M_h$ gives

\[
 0\le \frac{1}{2V}\operatorname{Tr}(\Gamma M_h\mathcal D_R M_h)
 \le \frac{C_k(1+\beta)\sqrt{1+\log(1+\beta)}}{R^2},\qquad |h_x|\le1.
\]

Here the factors are bounded by the square roots of $\operatorname{Tr}\Gamma^2$ and $\operatorname{Tr}\mathcal D_R^2$, times $\|M_h\|$. This mixed trace also tends to zero at $R\asymp n$, even in expectation by the exceptional-event bound. For a single fixed Gaussian spin observable, arbitrary orthogonalized centred trial scores can recover at most its full variance $V X(U,h)$ in total, by Bessel's inequality in the conditional Gaussian $L^2$. This handles rescaling of the trials. Smallness of an unnormalized shell trace alone gives no upper bound on a single rescaling-invariant variational quotient.

## A lower bound on a growing range of Wilson scales

**Claim.** There are constants $c,C,R_0>0$ such that with probability tending to one under each of the sixteen Wilson laws, the *same* transported axes obey

\[
 c\le X_R(U,h)\le C\qquad(R_0\le R\le q/8,\ R\text{ dyadic}).       \tag{6}
\]

The statement holds for the bounded root curvatures just specified. It also holds simultaneously for every choice of unit root axes transported on the same trees. In particular $c\log(1+\beta)\le X(U)\le C\log(1+\beta)$ with probability tending to one and with the same order for its expectation. Thus $X(U)$ itself has order $\log\log n$ along the calibration. In five dimensions the upper bound for an individual shell is $C/R$ for *any* axes and any connection. Indeed $D_R^2\preceq9R^{-4}(H+R^{-2})^{-4}$ by scalar spectral calculus. The same annuli as in (4) give $F_{5,4}(s)\le C s^{-3/2}$. With $F_{4,4}(s)\le Cs^{-2}$ this proves both deterministic shell upper bounds, including the contribution of zero momentum.

**Wilson probability of the cubes used in the lower bound.** In a periodic link representative a temporal twist has at most $d-1$ stacks of negative plaquettes, each of order $n^{d-2}$ plaquettes. For a $0i$ twist place its stack at a fixed time and a fixed $i$ coordinate. For the untwisted homogeneous torus, [row 1153](gap-solve6-astra62.md), immediately before (2), already bounds the mean one-plaquette deficit by $C/\beta$ using a marked positive transfer. Here is the total-action version needed for arbitrary seam signs. It uses the tree-volume comparison behind the weak-coupling free-energy estimates credited in [row 1143](gap-solve-astra62.md) to Sourav Chatterjee.

Let $f(t)=-\log\int e^{-tA}$. Gauge-fix a spanning tree. Conditional on its links, the endpoint changes of the other links preserve product Haar, and gauge invariance allows the tree to be set to one. There are $(d-1)V+1$ remaining links. Restrict each to chord distance $\beta^{-1/2}$ from one. The cap has Haar mass at least $c\beta^{-3/2}$ by the radial density proportional to $\sin^2\theta$. The plaquette product inequality gives deficit at most $8/\beta$ off the stacks. Thus

\[
 f(\beta)\le \tfrac32((d-1)V+1)\log\beta+CV+C\beta n^{d-2}.
\]

For the other bound keep only temporal plaquettes between times $0$ and $v-1$, omitting the wrap. This increases the integrand. Fix the temporal links and integrate the spatial layers from $v-1$ down to $1$. Each spatial link in the last remaining layer appears exactly once. Its integral is $I(t)=\int e^{-t(1-\operatorname{tr}g/2)}dg$, also for a negative seam sign by Haar invariance. The same radial density and $1-\cos\theta\ge2\theta^2/\pi^2$ give $I(t)\le C t^{-3/2}$ for $t\ge1$. Consequently $f(\beta/2)\ge\tfrac32(d-1)(V-n^{d-1})\log\beta-CV$. On the prescribed trajectory $\log\beta/v$ and $\beta/n^2$ are bounded. Subtracting gives $\log\mathbb E e^{\beta A/2}=f(\beta)-f(\beta/2)\le C_0V$. Jensen and exponential Markov give

\[
 \mathbb E\,\frac{\beta A}{V}\le 2C_0,\qquad
 \Pr\!\left(\frac{\beta A}{V}>2(C_0+1)\right)\le e^{-V}.           \tag{7}
\]

Call a $q$-cube good if every internal face satisfies $\|I-\operatorname{Ad}U_p\|\le q^{-3}$. With $w=\operatorname{tr}U_p/2$, the squared norm is $4(1-w^2)\le8(1-\sigma_p w)$. Distinct cubes have disjoint internal faces. The total fraction of sites in bad cubes is consequently at most $8q^{d+6}A/V$. Its expectation tends to zero in $d=4$ by (7) and $q\le\beta^{1/16}$. The discarded strips occupy a fraction tending to zero because $q\to\infty$ and $q/v\to0$. Markov's inequality now gives a fraction of sites at least $3/4$ in good cubes with probability tending to one. This argument only uses an average over the twisted Wilson measure. It imposes no small-field condition on a whole torus.

A small plaquette angle could make a root vector too short to see the spin. Take $\tau=1/16$. Row 1141, (3), applied to a private link of $p_r$, bounds the probability of $|w_r|\le\tau/\sqrt{1+\beta}$ by $4(1+6\beta)\tau^2/(1+\beta)\le1/8$, even conditional on all the other links. Indeed multiplying the exposed link on the two sides by fixed unit quaternions or inverting it preserves the tilt bound, and $|w_r|$ bounds its component perpendicular to any fixed axis. The root plaquettes are disjoint. For $N$ cubes, if $J$ roots fail, conditioning successively on the previous indicators gives $\mathbb E 2^J\le(9/8)^N$. Hence $\Pr(J>N/2)\le(9/(8\sqrt2))^N$. With probability tending to one a fraction at least $1/4$ of the whole volume lies in good cubes whose root vectors have length at least $\tau$. This last conclusion uses both volume bounds and does not condition the cap estimate on the small-curvature event.

**Low-energy test spaces inside good cubes.** Use the comb strip bound of Sussman and Alpoge, outline (PX42)–(PX43), in the adjoint representation. In a good cube the root-tree gauge changes every internal transport to within $C_d q^{-2}$ of the identity. In fact sliding the extra step in a bond's root path through the later coordinate segments traverses at most $(d-1)q$ internal faces. The discrepancy is a product of conjugates of face rotations and its norm difference from identity is bounded by the sum of their deficits in operator norm. In this gauge $h$ is constant throughout the cube.

Fix $R$ as in (6). Inside each good cube with $|h_r|\ge\tau$ place disjoint subcubes of side $R$, including at least $\lfloor q/R\rfloor^d$ of them. In the middle third of each subcube place a real bump obtained by sampling a fixed nonzero smooth function supported in $(-1/6,1/6)^d$ at mesh $1/R$, centred in the subcube. Take $R_0$ large enough that its norm before normalization is between $cR^{d/2}$ and $CR^{d/2}$ (use a smaller open box on which the bump is bounded away from zero). The normalized bump $\phi$ satisfies $\|H_0\phi\|_2\le C R^{-2}$ by the second-difference formula and zero extension. The one-bond enlargements of the supports are mutually disjoint and lie in their respective good cubes. There are at least $cV/R^d$ bumps on the event just proved.

For each bump take all three constant colour vectors in its tree frame. Denote their combined span over all bumps by $S_R$, and its orthogonal projection by $P_R$. On one such supported vector, the difference of the two Laplacians is a sum of at most $2d$ shifted link errors with operator bound $Cq^{-2}$ each. By disjointness of the enlarged supports this yields $\|H\psi\|_2\le C R^{-2}\|\psi\|_2$ on the whole span. This controls the *norm* of $H\psi$ needed for the squared resolvent.

Put $a=R^{-2}$. The inverse of the shell is $D_R^{-1}=(H+a)(H+4a)/(3a)$. On $S_R$ its quadratic form is at most $C R^{-2}I$, using the preceding norm bound in each of the three terms $H^2,5aH,4a^2 I$. For every test $f$, restricting the supremum in $\langle f,D_Rf\rangle=\sup_\psi(2\langle f,\psi\rangle-\langle\psi,D_R^{-1}\psi\rangle)$ to $S_R$ gives

\[
 D_R\succeq cR^2 P_R.                                               \tag{8}
\]

The variational restriction is valid for arbitrary $P_R$. For any positive semidefinite $B,C$ and symmetric $M$, $\operatorname{Tr}(BMC M)=\|C^{1/2}M B^{1/2}\|_{\rm HS}^2\ge0$. Consequently the quadratic trace in (1) is increasing in its positive covariance in the order of quadratic forms. Insert (8). On each bump, multiplication by $M_h$ preserves the two-polarization colour space. The trace of its square there is $16|h_r|^2\ge16\tau^2$, since the cross product with $h_r$ has two singular values $|h_r|$ and one zero. The resulting lower bound is $cR^4 V^{-1}$ times the number of bumps, which proves (6) for $d=4$, on a single event for every indicated $R$.

Finally, differences $D_R$ at consecutive dyadic radii telescope. Their sum over (6) is bounded above by $G$, since $R\le n$. Expand the quadratic trace of the sum. Every cross term is nonnegative by the same trace identity. At least $c\log q$ shells contribute, proving the lower bound for $X$. With (2) this also proves the two-sided expectation estimate. The argument leaves the crossover between $q/8$ and order $\sqrt{1+\beta}$ undetermined.

## Testing the plaquette insertion itself

The upper bound survives use of the **untruncated curvature at every site**. In (1) take $h_x=\sqrt{1+\beta}\operatorname{Im}(\sigma_{p_x}U_{p_x})$ for the $12$ plaquette based at $x$. Indeed $\sum_x|h_x|^2\le 2(1+\beta) A$. In the Hilbert–Schmidt bound keep $\operatorname{Tr}(\Gamma^2 M_h^2)$, bounded by $C\sum_x |h_x|^2\|(G^2)(x,x)\|$. The heat-walk argument also bounds each on-diagonal block by the scalar diagonal, using the norm of each walk transport. On (3) these diagonals are at most $C F_{4,2}(m^2+\gamma)$. For $D_R^2$ they are at most $C R^{-4}F_{4,4}(R^{-2}+\gamma)$, using (3) in scalar spectral calculus *before* heat domination. Thus (2) and (5) hold for this unbounded-in-$\beta$ choice on the intersection with (7)'s good event. For expectations the omitted part costs at most $C(1+\beta)(1+\log n)(C_k n^{-k}+e^{-V})$. The lower bound (6) uses the coherent transport inside cubes. I do not obtain it for the sitewise insertion.

There is a separate signed estimate for the curvature of the **adjoint plaquette**. It illustrates what cancellation survives before taking norms. Put $S_i t(x)=\operatorname{Ad}(U_{x,i})t(x+e_i)$ and $P=S_1S_2S_1^*S_2^*$. This acts at each site by the adjoint plaquette rotation. For $U_p=w+u$ in quaternion coordinates, $(P-P^*)/4=w\operatorname{ad}u$. In particular this insertion is unchanged by a centre sign. For all colour sections $s,t$,

\[
 |\langle s,(P-I)t\rangle|\le 10\|D_U s\|\,\|D_U t\|.             \tag{9}
\]

To see this, expand $P-I=[S_1-I,S_2-I]S_1^*S_2^*$. In each of the two terms one difference moves onto $s$. For $W=S_1^*S_2^*$, $\|(W-I)t\|\le2\|D_Ut\|$, so $\|(S_i-I)Wt\|\le5\|D_Ut\|$. The same form bound holds for $P^*-I$ by adjunction. Hence with $h_x=\sqrt{1+\beta}\,w u$ the symmetric spin matrix factors as $M_h=(I_2\otimes H^{1/2})L(I_2\otimes H^{1/2})$, where $\|L\|\le C\sqrt{1+\beta}$. The form vanishes on the nullspace, so the factorization follows by inverting $H^{1/2}$ on its range. Cyclicity and Hilbert–Schmidt Cauchy–Schwarz now give, for every connection in four dimensions,

\[
 X_R(U,h)\le C(1+\beta)V^{-1}\operatorname{Tr}[(H D_R)^2]
 \le C(1+\beta)R^{-4}(1+\log R).                                   \tag{10}
\]

In the last step $H D_R\preceq 3R^{-2}(H+R^{-2})^{-1}$, with both operators functions of $H$. Equations (9)–(10) apply to $w\operatorname{ad}u$. The fundamental plaquette spin and the ordered link insertions in the Wilson Hessian carry their own coefficients and transports. The preceding probabilistic bound applies to the fundamental sitewise curvature, while (9) alone does not estimate the Wilson Hessian. [Outline, (PX114)–(PX116)](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L11313-L11340)

## Attempt to pass the spin response to the neutral midpoint law

First keep track of all sixteen masses in a deformation where the computed sign is exact. At fixed $U$ and for the bounded transported probe define

\[
 L_U(\theta)=\det(I+\theta\Gamma^{1/2}M_h\Gamma^{1/2})^{-1/2},\qquad
 \widehat Z^z_\theta(v)=Z^z(v)\mathbb E^{z,v} L_U(\theta).
\]

For $|\theta|<m^2/2$ this is the Gaussian expectation of $\exp(-\theta a^tM_ha/2)$. The first derivative of $\log L_U$ at zero vanishes by the off-diagonal polarization matrix. The second derivative equals $V X(U,h)$. Compactness and the uniform spectral bound at fixed cutoff justify averaging both derivatives. Thus the free-energy curvature per site in this particular deformation is $-\mathbb E^{z,v} X$. In the ratio, with $\widehat Z_{+,\theta}=\tfrac18\sum_z\widehat Z^z_\theta$, one gets exactly

\[
 \left.\partial_\theta^2\log\frac{\widehat Z_{+,\theta}(2u)}{\widehat Z_{+,\theta}(u)^2}\right|_0
 =2n^3u\left(\mathbb E^{+,2u}X-\mathbb E^{+,u}X\right).
\]

The expectations use the original twist weights $Z^z(v)/\sum_{z'}Z^{z'}(v)$. The leading volume factors match. The separate curvature signs and orders leave the sign of this difference undetermined. Even for a two-level transfer with eigenvalues $1,r$, $0<r<1$, interchanging the diagonal entries $B,B+1$ of an insertion reverses its thermal-mean difference between $u$ and $2u$, for any $B>0$. At $\theta\ne0$ the determinant changes the Wilson weight. This calculation gives no transport in physical Wilson coupling.

At the seed aspect, $u=n/512$ is even. Take $b_A(C)$ to be the kernel of $P_0T^{u/2}$ with the vertex projection included in the physical transfer. Put $K_A=\int b_A(C)^2dC$, $p_A(C)=b_A(C)^2/K_A$ and $\pi_u(A)=K_A/Z_+(u)$. Both half periods carry the neutral projection. [Row 1373](gap-seed3-astra62.md) and [check 1527, (i), (vi)](gap-agy-seed-approaches-neon-check-astra62.md) give $P_K=\mathbb E_{\pi_u\otimes\pi_u}\operatorname{Aff}(p_{A_1},p_{A_2})^2$ and the following one-way test at the original aspect.

Join $A_1$ to a gauge- and centre-equivalent representative of $A_2$ by a piecewise smooth path $A(s)$, $0\le s\le1$. Write $b_A(C)=\int w_A(C,W)\,dW$ as the Wilson half-slab integral, including the finite centre sum and endpoint gauge averages in $dW$. At fixed $A,C$, let $Q$ denote its normalized interior law. Sample $C\sim p_A$ and then $W\sim Q$. For $S=\partial_s\log w_{A(s)}(C,W)$, differentiation of the finite compact integral gives $\partial_s\log b_A(C)=\mathbb E_Q S$. Thus the squared speed of the normalized midpoint row is $\mathcal J=\operatorname{Var}_{p_A}(\mathbb E_Q S)$.

For any square-integrable test $Y$ with $\mathbb E_Q Y=0$, conditional regression gives the following sufficient estimate for a measurable choice of paths and tests. It is required at each $K$ in one infinite set, for the same $\ell,g_0$.

\[
 \mathbb E_{A_1,A_2}\int_0^1
 \left[\operatorname{Var}_{p_A Q}(S)-
       \mathbb E_{p_A}\frac{(\mathbb E_Q[SY])^2}{\mathbb E_Q[Y^2]}\right]ds
 \ \le\ 2\bigl(1-\sqrt{457}/25\bigr).                              \tag{11}
\]

Use zero for the fraction when its denominator is zero. The subtracted term is bounded above by $\mathbb E_{p_A}\operatorname{Var}_Q S$ by conditional Cauchy–Schwarz. Hence the integrand bounds $\mathcal J$ from above. The path-length inequality (2.3) and Jensen (2.2) of row 1526 then give $P_K\ge457/625$. All geometric and projection hypotheses of this implication hold here. Its numerical premise (11) is open. It is stronger than the purity test in the smooth positive-transfer setting. Check 1527, (vi), gives the kernels $1+\tfrac12\cos(Na)\cos(Nc)$ with purity $257/289$ and minimum mean path energy growing at least as $cN^2$. This already separates the two tests before restricting $Y$.

**The signed overlap is the missing quantity.** To test the torus observable in (11), adjoin the return half-bridge conditional on $A,C$, independently of the first half given these endpoints, with its own neutral projection. The original half and its score $S$ retain their joint law with $C$. Given both halves, including their gauge and twist variables, draw the normalized Gaussian with covariance $\Gamma$ or $\mathcal D_R$ from the glued field and put $Y=\tfrac12 a^t M_{h(U)}a$. Its conditional mean at fixed bridges is zero because $M_h$ is off-diagonal in polarization. Taking the inner expectation over the auxiliary field first gives $\mathbb E[SY\mid A,C]=0$ exactly, including for any multiplier measurable in the bridges. The normalized Gaussian integrates to one on each twist and period. The logarithm in (6) supplies no subtraction in (11). A test formed from the Wilson fluctuations themselves would need a mixed moment with the endpoint score. For instance, with $Y$ the weighted divergence of a smooth interior vector field $V$ at fixed $A,C$, this moment equals $\mathbb E_Q\langle\nabla_W S,V\rangle$ by Haar integration by parts. Neither that moment nor the variance of the divergence is controlled by (1)–(10).

Even matching the two polarization covariances on a fixed background would leave a fourth moment undetermined. Take independent $a,c\sim N(0,G)$, an independent fair sign $\varepsilon$, and use the two polarizations $(a,\varepsilon\sqrt{1-\eta^2}\,a+\eta c)$, $0<\eta<1$. Their joint covariance is exactly $I_2\otimes G$, each marginal is Gaussian, and the joint density is smooth and strictly positive. Since $a^t(\operatorname{ad}h)a=0$ for the sitewise skew matrix, their spin variance is only $\eta^2 V X(U,h)$. The example concerns the information in a covariance match. It makes no assertion about the law of the Wilson link fluctuations.

## Stopping statement

The concrete extension tested was a positive, cutoff-independent spin response at the physical radius $R_K=2^{\lfloor\log_2(u/8)\rfloor}$, namely $\limsup_K\min_{v,z}\mathbb E_{\beta_K}^{z,v}\big[\sup_{|h_x|\le1}X_{R_K}(U,h)\big]>0$. Equations (3)–(5) disprove it on every one of the sixteen tori. They allow the frame to read the whole Wilson sample. The shorter-scale statement (6) is genuinely selective. The colour bracket is zero for compact $U(1)$, and the five-dimensional mode count bounds the very same shell by $C/R$. This calculation does not use a conjecture about the five-dimensional spectrum.

The physical-radius statement is a proposed source of gain, with no necessity theorem for the seed. For example the pure Wilson transfer at $\beta=0$ has rank one and purity one. At that coupling the first inequality of (3) gives $\gamma=c_k/(1+\sqrt{\log(2+n)})$. The proof of (5) with this $\gamma$ gives vanishing physical-radius response there too. This example is off the calibration. In the other direction even the successful bounds on the normalized Wilson backgrounds cannot supply the sixteen mass normalizations. Tensoring the transfer with the neutral two-state kernel having diagonal $1$ and off-diagonal $n^{-2}$ leaves every normalized Wilson measurement unchanged and multiplies the purity by a factor tending to $1/2$, as in check 1527's spectator test. These comparisons separate the information in the estimates at the level of the transfer argument. The law in the question has no spectator.

The remaining physical estimate for this attempt is (11) with a test built from Wilson variables. I have neither a bound giving its required signed subtraction nor a dimension-selectivity proof for that general path criterion. The null overlap above and the bound at $R_K$ apply to the specific unblocked implementation. They do not exclude a matched estimate on successively renormalized fields. The proofs here are hand arguments. They have no separate reader or Lean check and use no computed value as a premise.

RESULT Row 1530. The bare Wilson-background spin response is of order $\log\beta_K$ for the transported plaquette probe in four dimensions and vanishes on a shell at the seed scale. The signed Wilson midpoint estimate (11), PUR-io and the physical mass gap remain open.
