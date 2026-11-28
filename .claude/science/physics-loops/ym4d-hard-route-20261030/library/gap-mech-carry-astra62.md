# Repo search

Row 1536, checkout `37430da89`. I searched Markdown and TeX on `origin/main` (`8b11ae2bb9`), `pr/10114` (`f76f6c649c`), `pr/10133` (`89faef229f`), `pr/10134` (`1e70c7211a`) and `pr/10141` (`c73ad7b177`). The search for `PUR-io`, `Gaussian spin response`, `transported plaquette axes`, `signed midpoint` and `covariant Laplacian` near `mass gap` returned no lines. I also searched for straight-product decimation, conditional Haar laws, perimeter bounds, first-layer and endpoint scores, and the covariant Laplacian of a block field.

- Main's `su2-gauge-aligned-response-20261108/parts/compact-energy-coercivity.md`, (6), bounds one coarse face deficit by four edge discrepancies plus a constant times the fine square's action. I use its square-filling argument. In the same directory, `marginal-regional-moments-and-ratios.md`, lines 417–425, assumes two-plaquette coercivity for a radial-profile comparison. `original-source-four-response.md`, lines 35–48, splits a two-step fourth cumulant into a fourth cumulant of conditional means and a third cumulant with conditional covariance. Those scores differentiate two terminal links.
- On PRs 10114 and 10133, `ym4d-proof/FLOW.md`, lines 3742–3748, identifies a block covariant Laplacian determinant at critical backgrounds. `MASS_GAP_LOCAL_BLOCK_ASTRA.md`, §7, and `MGX.md`, lines 39–55, give physical-time contraction $r(\beta)\le18/359$ for $0<\beta\le1/32$. Grok's PR 10133, `MASS_GAP_CROSSOVER_REDUCTION.md`, §3.1, requires uniform exponential clustering past crossover and transport of the original sources. These statements leave the spin trace on typical calibrated fields and its midpoint overlap open. The broad perimeter search also found the free smoothed-loop example in `WLOOP.md`, lines 485–492. The targeted search pairing bridge or replica exchange with score or regression, plus the literal one-sided-score and swap-parity variants, returned no lines on the five refs.
- In this checkout, row 1141 pins an arbitrary adjoint direction with two plaquettes. Row 1145 bounds the conditional density of an entire straight grid between $(1-\eta)^M$ and $(1+\eta)^M$, with $\eta\le C\exp[-(h-2)/(1+6\beta)]$ for long edges of length $h$. Its (4) bounds spectral weight seen by one spatial board. The later fine-field argument bounds overlap with slow vectors by a private-link Dirichlet form. Row 1434 rules out an independent positive heat-time floor on a straight coarse square. I use the conditional density estimate. [Row 1145, (1)–(4)](gap-solve2-astra62.md) · [Fine-field estimates (20)–(22)](gap-solve-fresh-astra62.md) · [Heat-factor obstruction](gap-mech-candidate-astra62.md)
- Row 1161 gives $\operatorname{Var}(a\cdot U_e\mid U_{\ne e})\ge c(1+6\beta)^{-2}$ for every unit quaternion vector $a$. The later wall-variance note credits the plaquette version to Bhattacharjee, Bhattacharya, Lockwood and Romanov. The half-slab comparison in `gap-seed5-astra62.md` bounds the change of the first temporal layer by $\beta\sqrt{3n^3}$ times the endpoint distance. These are inputs to the question about **residual** score variance. [One-link proof before (18)](gap-solve9-astra62.md) · [Plaquette-variance source attribution](gap-solve24-astra62.md) · [Half-slab comparison after (7)](gap-seed5-astra62.md)
- Row 1530 treats the spin of the bare connection and tests an auxiliary Gaussian against the score. Row 1373 gives the neutral two-arc identity. The odd-sector note's (I5) gives the gradient of a twist-label ratio as a first-layer force covariance with that label. Check 1527 distinguishes path energy from purity. The register assigns R11 and TWO-PER to their coupling-transport rows. The first-layer regression and blocked spin shell have no matching entry in `open-registry.md`, `open-core.md` or `l17c.md`. The target-specific prior file is absent at the pin. The November 8 digest treats UV and local-block work. [Prior digest](prior/repo-search-2026-11-08.md) · [Odd-sector force identity](gap-oddgap-max.md) · [Row 1530](gap-mech-attack-astra62.md) · [Midpoint identity](gap-seed3-astra62.md) · [Check 1527, (i) and (vi)](gap-agy-seed-approaches-neon-check-astra62.md)

## Plan saved at entry

1. Read the target-specific prior map, the goal, the finish rules, and the open registry. Search the five named repository refs for the mechanism and its consumer.
2. Check the outline index against its cited source ranges. Re-derive the statements needed from row 1530 and verify the consumer's direction and normalization.
3. Test an explicit blocking or propagation of the signed spin response. Track its scale, the group and dimension dependence, and the implications for Wilson variables.
4. Record the proved bounds, any obstruction and its quantifiers, and the exact remaining estimate. Check the result against the seed and the two comparison models.

## Source conventions and decision

Sussman and Alpoge's outline, authored with Claude and Codex, defines Wilson path products and the Wilson law at lines 238–272. GL8, lines 2313–2336, integrates the time links to obtain the vertex-projected transfer trace. PX42–43, lines 10744–10754, bound a comb-gauge link by a strip of plaquettes. Lines 7063–7073 distinguish Bałaban's symmetric block average from a straight edge. CA-I, lines 2704–2712, leaves a mass gap outside Theorem 0. Source text is the supplied copy at revision `31a47c543775`. The arguments below use exact straight products and the original Wilson weights. [Outline index](sa-index/README.md) · [Obligations](sa-index/obligations.md)

Fix the released odd $b>1$, $g_0$ in its calibration interval and $\ell\in1024\mathbb N_{>0}$. Put $n=\ell b^K$, $u=n/512$ and $\beta=\beta_K\asymp\log n$. For $v=u,2u$ the Wilson transfer $T$ on the spatial $n^3$ torus gives $Z^z(v)=\operatorname{Tr}(C_zT^v)$ and $Z_+(v)=\tfrac18\sum_{z\in\mathbb Z_2^3} Z^z(v)=\operatorname{Tr}(P_0T^v)$. The seed asks for $P_K=Z_+(2u)/Z_+(u)^2\ge457/625$ at infinitely many $K$ for one choice of witnesses. [Check 1453](sa-ym4-lean-trajectory-check-astra62.md) · [Consumer, §3.1](gap-k2-tool-design-fable.md)

Straight blocking carries the selective response through a growing range of radii in lattice units. At the seed radius it loses the response on every increasingly fine coarse grid. Even on a last grid of fixed size the retained data leave an extensive residual in the signed test. A separate bound applies to reflection-symmetric tests of both full Wilson bridges.

## A lower bound on the signed test in (11)

Write $w=u/2$, $B=P_0T^w$, $b_A(C)=B(A,C)$, $k_A=\int b_A^2$, $p_A=b_A^2/k_A$ and $\pi(A)=k_A/Z_+(u)$. Use the Wilson transfer with half the spatial action on each side. Include the vertex projector and the centre projector on **each** arc. Take $K$ large enough that $w\ge2$. In a half-slab, keep the spatial links at times $1,\ldots,w-1$, all temporal links, and the endpoint projection variables. Put the relative endpoint transformation at $C$ by simultaneous gauge and centre invariance. Moving it there uses a Haar change of interior variables independent of the path parameter. Let $Q=Q_{A,C}$ be the conditional half-slab law, and let $S$ be the derivative of its **unnormalized** log weight along $A(s)$. Draw the second half independently given $A,C$ if the test needs it. In that case the conditional expectations involving $Y$ use both draws.

Fix a deterministic set $H$ of spatial edge labels. Hide their copies on time slice 1 of the scored half-slab. Allow the test to read every other variable, including $A,C$, the path and its tangent, every temporal link, and the whole return slab. Additional randomization from these readings and independent coins is allowed. The path and its endpoints are chosen before drawing $C$ and the interiors at that path point. Let $m(H)$ count elementary spatial plaquettes with all four edge labels in $H$. The cost in (11) is
\[
 \mathcal I(Y)=\mathbb E_{\pi\otimes\pi}\int_0^1
 \left[\operatorname{Var}_{p_A Q}(S)
 -\mathbb E_{p_A}\!\left(\frac{(\mathbb E_Q[SY])^2}{\mathbb E_Q[Y^2]}\right)\right]ds ,
\]
with zero for the quotient when its denominator vanishes. Constants in Theorem 1 are independent of $H,n,\beta$ and the path.

**Theorem 1.** For every measurable choice of piecewise smooth paths between independent $\pi$ endpoints, allowing endpoint gauge and centre representatives, and every square-integrable test in this family with $\mathbb E_QY=0$, the left side of row 1530 (11) satisfies
\[
  \mathcal I(Y)\ \ge\ c\, m(H)\frac{\beta^2}{(1+6\beta)^4}.                 \tag{1}
\]
The same bound holds after optimal regression on the entire allowed observation. On the calibrated trajectory a bounded cost requires $m(H)=O(\beta_K^2)$.

**Normalization and sign.** At a fixed $A,C$, write $g=\mathbb E_Q S$. Differentiating the positive finite integral for $b_A$ gives $g=\partial_s\log b_A(C)$. With $C\sim p_A$, the squared speed of the unit row $b_A/\sqrt{k_A}$ is $J=\operatorname{Var}_{p_A}g$. The integrand in (11) is exactly
\[
 J+\mathbb E_{p_A}\inf_{a\in\mathbb R}\mathbb E_Q[(S-g-aY)^2].             \tag{2}
\]
Expanding the square gives the stated negative regression term, including the zero-denominator convention. The same decomposition with the best centred function of all allowed observations replaces the second term by their conditional residual variance.

For completeness, multiplication of $B$'s kernels gives $B^2(A,A')=\sqrt{k_Ak_{A'}}\langle\sqrt{p_A},\sqrt{p_{A'}}\rangle$. Its trace is $Z_+(u)$ and its squared Hilbert–Schmidt norm is $Z_+(2u)$. Thus $P_K=\mathbb E_{\pi\otimes\pi}\langle\sqrt{p_{A_1}},\sqrt{p_{A_2}}\rangle^2$. The squared chord of the two unit rows is at most $\int_0^1 J\,ds$ by Cauchy–Schwarz. The rows are invariant under the endpoint transformations. Hence $\mathcal I(Y)\le2(1-\sqrt{457}/25)$ gives a mean inner product at least $\sqrt{457}/25$, and Jensen gives the seed at this cutoff. This checks precisely the direction in which (1) obstructs the consumer. [Neutral consumer, §3.1](gap-k2-tool-design-fable.md)

**The missing first-layer variance.** Identify $SU(2)$ with the unit quaternions. Holding the first temporal links fixed sends $X_{1,e}$, the spatial link over $e$ on slice 1, to $L_eX_{1,e}R_e$ with fixed unit factors. The first temporal plaquette contributes $\beta\langle A_e,L_eX_{1,e}R_e\rangle$ to the log weight, up to an additive constant. Inversion and centre signs act orthogonally on quaternion coordinates. Differentiating therefore gives
\[
 S=s_0(A,\dot A)+\beta\sum_e t_e\cdot X_{1,e},
 \qquad |t_e|=|\dot A_e|.                                              \tag{3}
\]
Here $s_0$ comes from the spatial half-action on $A$. The $t_e$ are fixed when the temporal and projection variables are fixed. This derivation keeps the Wilson score prior to any integration over slice 1.

Use the one-link variance estimate credited above. Its short proof fixes the needed uniformity. A free link on $S^3$ has density proportional to $e^{k\cdot x}$ with $\kappa=|k|\le6\beta$. Each incident plaquette contributes a linear form of norm $\beta$. Along $k$, $t=x\cdot k/\kappa$ has density proportional to $e^{\kappa t}\sqrt{1-t^2}$. For $\kappa\ge8$, $y=\kappa(1-t)$ has density proportional to $e^{-y}\sqrt{y(2-y/\kappa)}$ on $[0,2\kappa]$. Its normalizer is at most $\int_0^\infty e^{-y}\sqrt{2y}\,dy$. Each of $[1,2]$ and $[3,4]$ therefore has probability at least an absolute positive constant. Two independent draws give $\operatorname{Var}t\ge c/\kappa^2$. Conditional uniformity on the transverse two-sphere gives each transverse coordinate variance $\mathbb E(1-t^2)/3\ge c/\kappa$ and zero mixed covariances. For $\kappa\le8$, the density dominates $e^{-16}$ times Haar, whose coordinate covariance is $I/4$. Minimizing squared deviations over the constant mean proves
\[
 \operatorname{Var}(a\cdot x)\ge c|a|^2/(1+6\beta)^2.
\]

Colour the hidden edges so that no two in a colour belong to one action plaquette. A link has at most 18 neighbours in the plaquette conflict graph, so 19 colours suffice by greedy colouring. Condition on all variables except the first-layer links of one colour. Under $Q$ these links are independent tilted quaternions. Conditioning on the return bridge preserves this fact. The allowed predictor is fixed under this conditioning. Equations (2)–(3) bound the residual below by $c\beta^2(1+6\beta)^{-2}\sum_{e\text{ in colour}}|\dot A_e|^2$. The largest such sum is at least $1/19$ of the sum over $H$. This argument allows an arbitrary predictor of $S$ from the retained data and $C$.

For $f_p(A)=\operatorname{Re}\operatorname{tr}A_p/2$, multiplication by unit quaternions gives $|\dot f_p|\le\sum_{e\in p}|\dot A_e|$. Each spatial link occurs in at most four spatial plaquettes. Integrating and applying Cauchy–Schwarz gives
\[
 16\int_0^1\sum_{e\in H}|\dot A_e|^2 ds
 \ \ge\ \sum_{p\subset H}|f_p(A_1)-f_p(A_2)|^2.
\]
These plaquette traces are invariant under all allowed endpoint identifications. The marginal $\pi$ is the time-zero slice of the neutral $u$-circle. This follows by gluing the two projected arcs, or by cyclicity against a multiplication operator on the diagonal. In the mixture of twisted Wilson tori, expose the twist and all links except one edge of $p$. The other three edges turn $f_p$ into a unit linear functional of that link. The same one-link bound gives $\operatorname{Var}_{\pi} f_p\ge c/(1+6\beta)^2$ by total variance. Independence of the two endpoints gives twice this variance in the last display. Summing proves (1). No independence between different $p$ is required.

**Application to actual block maps.** Let $h=b^j$ with $1\le j\le K$. Keep the ordered products along straight edges on the grid of spacing $h$ in all four directions. Composing these maps is exactly the map at the product of their spacings. For a grid through time zero, no spatial coarse edge reads slice 1. Even for a translated grid through time 1, every $12$ plaquette at third spatial coordinate $x_3$ off its grid planes has all four edges hidden there. Thus $m(H)\ge (1-1/h)n^3$. Any subsequent measurable blocking of these data, any collection of nested levels on this grid, and any postprocessing of their Wilson variables obey (1). This includes a centred Wilson spin test, conditional regression on arbitrarily many such tests, and a test from both projected halves. For example, form a shell trace on the glued Wilson field and subtract its conditional mean given $A,C$. The centring depends only on these endpoints. For every predetermined translation, the best cost diverges at least as $c n^3/(1+\beta_K)^2$ for $\beta_K\ge1$. This bound uses the conditional law at every path point. It does not require the intermediate endpoint to have the stationary marginal.

## The spin response on actual blocked Wilson links

For each $v,z$ use a periodic link representative with $\sigma_p=-1$ on the prescribed twist stacks and $+1$ elsewhere. Put $A=\sum_p(1-\sigma_p\operatorname{Re}\operatorname{tr}U_p/2)$. In this section $A$ denotes the total action. Let $V$ be the straight products at spacing $h=b^j$, including $h=1$. The coarse side is $N=n/h$, the time period is $v/h$, and $V_c=N^{d-1}v/h$ is the site count. The law of $V$ is the exact pushforward from each fine torus.

On coarse vertex colours define $(D_V f)_{x,i}=\operatorname{Ad}(V_{x,i})f_{x+i}-f_x$, $L=D_V^*D_V$ and
\[
 D_r=(L+r^{-2})^{-1}-(L+4r^{-2})^{-1},\qquad
 X_r(V,\xi)=\frac1{2V_c}\operatorname{Tr}(\mathcal D_r M_\xi\mathcal D_r M_\xi).       \tag{4}
\]
Here $\mathcal D_r=I_2\otimes D_r$, $M_\xi=-2J_2\otimes[\xi,\cdot]$, $J_2$ is a quarter-turn, and the colour bracket is the cross product in row 1530's normalization. $M_\xi$ is symmetric and $\|M_\xi\|\le2$ for $|\xi_x|\le1$. The trace is a function of Wilson variables. For $a\sim N(0,\mathcal D_r)$ the quadratic spin $a^t M_\xi a/2$ has variance $V_c X_r$ by the two cross pairings.

**Theorem 2.** Put $q=\lfloor\beta^{1/32}\rfloor$. Tile each coarse coordinate by consecutive intervals of $q$ sites and drop the incomplete intervals. At the root $\rho$ of each cube take $z_\rho=\sqrt{1+\beta}\operatorname{Im}(\sigma_{\square} V_{\square})$ on its $12$ plaquette, with $\sigma_{\square}$ the product of the fine signs in this face. Transport $z_\rho/\max(1,|z_\rho|)$ down the coordinate comb, and put $\xi=0$ off the cubes. There exist $c,C,r_0>0$ such that on each of the sixteen Wilson tori, with probability tending to one,
\[
 c\le X_r(V,\xi)\le C
 \quad\text{at every } h=b^j\le\beta^{1/8}
 \quad\text{and every dyadic }r_0\le r\le q/8.                          \tag{5}
\]
A gauge change rotates the root axis and conjugates the transported operators. A change of centre-seam representative multiplies the coarse face and its fine sign product by the same boundary sign, and leaves each adjoint link fixed. Thus the response is a Wilson observable. One field of axes at each blocking level works for all its shells. In fine links the largest tested radius is comparable to $\beta^{5/32}$. In compact $U(1)$ (4) is zero. In five dimensions (4) is at most $C/r$ for every blocked configuration, bounded axes and each twist at the same aspect. Thus a lower bound uniform in **growing coarse radii** distinguishes both comparison models.

**Deterministic upper estimate.** Hilbert–Schmidt Cauchy–Schwarz bounds (4) by $C\operatorname{Tr}D_r^2/V_c$. Put $a=r^{-2}$. Scalar calculus gives $D_r^2\preceq9a^2(L+a)^{-4}$. Write $L=2dI-\mathcal A_V$. Expanding the heat kernel in powers of the nearest-neighbour adjacency $\mathcal A_V$ counts closed walks. Each transport has trace at most three. Integrating the resulting heat-trace bound against $t^3e^{-at}/6$ bounds the last resolvent trace by three times the free scalar one. The free symbol at momentum $p$ is $4\sum_i\sin^2(p_i/2)\ge4|p|^2/\pi^2$ on the principal cube. At these fixed aspects the number of momenta of norm at most $t$, divided by $V_c$, is at most $C(t+N^{-1})^d$ by coordinate counting. For $1\le r\le N$, the ball of radius $1/r$ contributes at most $Cr^{8-d}$ to the normalized fourth resolvent trace. The annulus of radii $2^k/r$ and $2^{k+1}/r$ contributes at most $C(2^k/r)^{d-8}$. The sum is at most $Cr^{8-d}$ for $d=4,5$. Multiplication by $a^2$ gives $Cr^{4-d}$, including the zero mode. In $U(1)$ the Lie bracket itself vanishes.

**Curvature at nested scales.** Put $V_f=n^3v$ and $a_\beta=\log(2+\beta)/\beta+n^{-2}$ for $\beta\ge1$. The action estimate $\mathbb EA/V_f\le C a_\beta$ suffices. To prove it, restrict every fine link to a Haar ball of chord radius $\beta^{-1/2}$ about the identity. Its mass is at least $c\beta^{-3/2}$ by the $\sin^2\theta$ radial density. Every positive face costs at most $8/\beta$ there. The at most $3n^2$ negative faces cost at most two each. This bounds $F(\beta)=-\log\int e^{-\beta A}$ from above by $C V_f\log(2+\beta)+C\beta n^2$. Since $F(0)=0$, $F'=\mathbb EA$ and $F''=-\operatorname{Var} A$, concavity proves the estimate. The cap argument is the weak-coupling free-energy comparison used in row 1530, with a logarithmic loss allowed here. [Chatterjee attribution and Wilson comparison](gap-solve-astra62.md)

Let $d_f=\|I-\operatorname{Ad}U_f\|$ on a fine face. Then $d_f^2=4(1-(\operatorname{Re}\operatorname{tr}U_f/2)^2)\le8(1-\sigma_f\operatorname{Re}\operatorname{tr}U_f/2)$. The quantity $\mathbb E(d_f^2)$ is translation invariant within each orientation. Indeed a $0i$ stack at fixed $t,x_i$ can be moved by one time step by flipping the $i$-links on the intervening cut. A shift in $x_i$ uses the temporal links on the intervening cut. Only the old and new stacks change sign. The changes preserve Haar measure and all adjoint transports. Products of these flips move several stacks. Summation over translates now gives $\mathbb E d_f^2\le C a_\beta$ individually. A coarse face is tiled by $h^2$ fine faces. Peeling successive rows, cancelling the common edge on each attachment, writes its boundary as a product of conjugated fine boundaries. The norm error of a product of rotations is at most the sum of their norm errors. Cauchy–Schwarz gives
\[
 \mathbb E\|I-\operatorname{Ad}V_\square\|^2\le C h^4 a_\beta.          \tag{6}
\]
A $q$-cube is good if all its internal coarse faces have adjoint error at most $q^{-3}$. A union bound and (6) bound its failure probability by $C q^{10}h^4 a_\beta$. This also bounds the expected volume fraction in failing cubes. Summing over $h=b^j\le\beta^{1/8}$ costs at most $C_b q^{10}\beta^{1/2} a_\beta=o(1)$ by the geometric series. Discarded strips occupy at most $C qh/v=o(1)$ at each level.

A root must also carry enough curvature for the bounded probe. The one-link tilt of concentration $\kappa$ has Haar density at most $C(1+\kappa)^{3/2}$. Integration on a chordal ball of radius $(1+\kappa)^{-1/2}$ about its mode bounds the normalizer below by $c e^\kappa(1+\kappa)^{-3/2}$. Haar mass on $\{|\operatorname{Im}g|\le t\}$ is at most $Ct^3$ for $t\le1/2$, by the same radial density at both poles. Expose one fine link used once in a root loop. All other factors and any inversion preserve the density bound. Uniformly, $\Pr(|z_\rho|<\tau\mid\text{other fine links})\le C'\tau^3$ for $0<\tau\le1/2$. Choose $\tau$ so the right side is at most $1/8$. The root loops are disjoint at each level. For $M$ roots, successive conditioning bounds $\mathbb E2^{\#\mathrm{failures}}\le(9/8)^M$. The probability at least half fail is at most $(9/(8\sqrt2))^M$. At the levels in (5), $M\ge c(n/(hq))^4$, so summing these probabilities over the levels still gives $o(1)$. Markov's inequality on the preceding total bad volume shows that, simultaneously, at least a quarter of all coarse sites belong to good cubes with $|\xi_{\rm root}|\ge\tau$.

**Lower estimate.** In each such cube, use the root-comb gauge. Moving one step of a path past the later coordinate segments traverses at most $dq$ internal faces. The product inequality bounds each internal adjoint link error by $Cq^{-2}$. The axes are constant in this gauge. Pack disjoint subcubes of $r$ sites per side inside each cube. In each use a normalized scalar bump sampled from a fixed nonnegative, nonzero smooth function supported in the middle third, extended by zero. Sampling at mesh $1/r$ in the rescaled cube, a positive lower bound on a smaller box gives an unnormalised norm at least $cr^{d/2}$ for $r\ge r_0$. Bounded second differences then give $\|L_0\phi\|_2\le Cr^{-2}$ for the normalized bump and free Laplacian. One-bond enlargements of the supports are disjoint. The link-error term in $L-L_0$ is a sum of $2d$ shifted multiplications, each bounded there by $Cq^{-2}$. Hence $\|L\psi\|_2\le Cr^{-2}\|\psi\|_2$ on the span of all bumps with all three colours. Write $P$ for the orthogonal projection onto that span. There are at least $cV_c/r^4$ bumps, since $r\le q/8$.

The quadratic form of $D_r^{-1}=(L^2+5a L+4a^2 I)/(3a)$ on this span is at most $CaI$. Restricting the variational maximum of $2\langle f,g\rangle-\langle g,D_r^{-1}g\rangle$ to the span gives $D_r\succeq c r^2 P$. For positive $B,C$ and symmetric $M$, $\operatorname{Tr}(B M C M)=\|C^{1/2}M B^{1/2}\|_{\rm HS}^2$. Expanding in the positive remainder allows the projection bound in both slots of (4). On each bump $M_\xi$ preserves the colour and polarization space, and $\operatorname{Tr}(M_\xi^2)$ there equals $16|\xi_{\rm root}|^2$. Thus (4) is at least $c r^4 \tau^2(V_c/r^4)/V_c$. This proves (5). The same proof at $h=1$, with $q=\lfloor\beta^{1/16}\rfloor$, recovers the short-shell input from row 1530 since $q^{10}a_\beta\to0$.

## What happens at the seed radius

**Theorem 3.** On a grid with $N=n/h\ge4096$, set $r_N=2^{\lfloor\log_2(N/4096)\rfloor}$. Its fine radius $h r_N$ lies in $(u/16,u/8]$. For any predetermined nested straight grids, in four dimensions,
\[
 \lim_{M\to\infty}\limsup_{K\to\infty}\max_{v,z}\,
 \mathbb E^{z,v}_{\beta_K}
 \sup_{\substack{0\le j\le K\\N=n/b^j\ge M}}
 \sup_{|\xi_x|\le1} X_{r_N}(V,\xi)=0.                                \tag{7}
\]
An empty supremum of these nonnegative responses is taken as zero. The axis and the retained level inside this supremum may both read the whole sample. This tests a covariant Laplacian rebuilt from the actual blocked Wilson links at each level.

**A coarse pin.** The following weaker form of the two-plaquette argument of row 1141 suffices. Centre a pair of opposite $12$ plaquettes in a coarse cube of three sites per side. They meet only at the base vertex. Let their holonomies be $g_i=t_i+u_i$ in unit quaternions. For a unit colour $a$,
$|(I-\operatorname{Ad}g_i)a|^2=4|u_i\times a|^2$. The minimum over $a$ of the sum is four times the smaller eigenvalue of the $2\times2$ Gram matrix of $u_1,u_2$. This follows by subtracting the largest eigenvalue of $u_1u_1^t+u_2u_2^t$ from its trace. On $|u_1|\ge |u_2|$ this smaller eigenvalue is at least $|u_2\times\widehat u_1|^2/2$, by determinant over trace. The zero-vector ties have probability zero under the laws used here.

Expose a fine link traversed once by the second coarse boundary and absent from the first. Given every other fine link, $g_2$ has Haar density at most $C(1+6\beta)^{3/2}$, by the one-link density bound above. For Haar $g=t+u$ and fixed unit $a$, $\Pr(|u\times a|\le s)=s^2$ for $0\le s\le1$. Indeed the squared radius in a fixed coordinate two-plane of $S^3$ is uniform on $[0,1]$, by the parametrization $(r e^{i\theta},\sqrt{1-r^2}e^{i\varphi})$ with radial law $2r\,dr$. Use this estimate with the first axis fixed, and interchange the roles for the opposite ordering of lengths. For $\delta=c(1+6\beta)^{-3/2}$, with a sufficiently small absolute $c$, the minimum sum is at least $\delta$ with conditional probability at least $1/2$ given the pin events of any previously tested disjoint coarse cells. Previous events read neither private link. This argument samples the fine Wilson law and uses no Wilson ansatz on the coarse grid. Under independent coarse Haar links the same proof gives a fixed $\delta=c$. [Earlier bare pin, (3)–(7)](gap-crux2-astra62.md)

**Uniformity in block depth.** If $h\le\sqrt n$, one has $\beta\le C(1+\log N)$ and the preceding fine-link estimate suffices. If $h>\sqrt n$, apply the conditional straight-path estimate of row 1145, (1)–(3), to the entire coarse grid. Each edge has $h-2$ private fine links, after dropping its first and last. No elementary face meets two selected links. At fixed complement their tilts have concentration at most $6\beta$, also for a negative seam. The representation multiplier bound in that row gives one edge density at most $1+\eta$, with $\eta\le C e^{-(h-2)/(1+6\beta)}$ when the exponent ratio is at least one. Given the complement, distinct coarse edge products are independent. The joint density is therefore at most $(1+\eta)^{4V_c}\le2$ relative to independent coarse Haar for all sufficiently large $K$, uniformly here, since $V_c\le n^4$. We can transfer a probability bound for failure from independent coarse Haar in this case. This use of row 1145 retains the correct fine coupling and all twist signs.

In each coordinate partition the coarse circle into intervals of lengths in $[k,2k]$, where $k=\lceil (D\log(2+N))^{1/4}\rceil$. For large $N$ the shortest period $v/h$ exceeds $2k$. Such a partition is obtained by absorbing a remainder into the last interval. Each rectangular box contains at least $c k^4$ vertex-disjoint three-site cells. The conditional pin estimate gives probability at most $2^{-c k^4}$ of no pin in that box. There are at most $N^4$ boxes. Fix $D$ large enough that the total probability is at most $C N^{-8}$, including the density factor two in the coarse Haar case.

On the complementary event take one pinned site $x$ in each box. For a colour section $f$ let $E_B$ be its covariant difference energy on internal bonds of the box. Telescoping along the four bonds of each pin loop gives $\delta |f_x|^2\le 4 E_B$ by Cauchy–Schwarz and disjointness of the two loop edge sets. For every $y$ in the box an internal path of length at most $8k$ gives $|f_y|^2\le 2|f_x|^2+16k E_B$. Summing within boxes and then over boxes yields
\[
 L\succeq \big[C k^4(\delta^{-1}+k)\big]^{-1}I
       \succeq c(1+\log N)^{-5/2} I.                                   \tag{8}
\]
In the coarse Haar case it is the deterministic event of having these pins with fixed $\delta$ that transfers to the Wilson law. All constants are uniform in the retained level.

It follows that $\|D_{r_N}\|\le C r_N^{-2}(1+\log N)^5$. On the bad event (4) still obeys the deterministic four-dimensional bound proved above. Thus at one level
\[
 \mathbb E\sup_\xi X_{r_N}(V,\xi)
   \le C (1+\log N)^{10}N^{-4}+C N^{-8},                              \tag{9}
\]
where the supremum has the same unit bound as (7). The possible $N=\ell b^{K-j}$ are geometrically spaced. Summing (9) over the tail $N\ge M$ gives (7), without probabilistic independence across levels.

**A last grid of bounded size.** Here there need be no vanishing. For fixed $r\ge1$, $L\preceq4dI$ implies $D_r\succeq d_r I$, where $d_r=3r^{-2}/[(4d+r^{-2})(4d+4r^{-2})]>0$. Choosing the unit imaginary axis of the $12$ plaquette at every site gives $X_r\ge8d_r^2$ almost surely on a nondegenerate grid. The zero axis event has probability zero by exposing one fine link. This works in five dimensions as well for a fixed $r$. If $N<4096$, the radius $u/8$ is shorter than one coarse edge. For every $h\ge b$, both cases are still subject to Theorem 1 when their retained fields are used to predict the raw score. An order-one finite-grid value, or an unbounded rescaling of a centred test on that grid, cannot remove the conditional variance in (1).

## A restriction even when the blocking reads the entire first layer

The same extensive variance also tests observables of **any** blocking on the glued circle, including a dense smearing. At fixed $A,C$, express the return arc in reverse time, as another bridge from $A$ to $C$. The Wilson half-action is symmetric, vertex Haar is inversion invariant, and the inverse centre element equals itself. Equivalently one may draw two independent copies of the *same* representation of $b_A(C)$, since their product is exactly the weight $b_A(C)^2$. Include all projection variables in both draws. Thus $W_1,W_2$ are iid under $Q_{A,C}^{\otimes2}$. The score in (11) is $S_1=S(W_1)$, a derivative on the first copy. Define $S_2=S(W_2)$ using the same tangent. Write $v_S=\operatorname{Var}_Q S$ and $g=\mathbb E_Q S$.

**Theorem 4.** Let $\mathcal R$ exchange the two oriented bridges. For any conditionally centred $Y$ of both bridges, put $Y_\pm=(Y\pm Y\circ\mathcal R)/2$ and $p=\|Y_+\|_2^2/\|Y\|_2^2$, with $p=0$ at $Y=0$. Norms here use $Q_{A,C}^{\otimes2}$. The conditional regression residual in (2) is at least
\[
 v_S\big(\tfrac12-\sqrt{p(1-p)}\big)\ \ge\ v_S(p-\tfrac12)^2.          \tag{10}
\]
Consequently no family with $|p-1/2|\ge\epsilon>0$ at every point of positive $v_S$ can meet (11) at late cutoffs. The result allows arbitrary nonlinear blockings, any number of levels, and access to both full Wilson interiors. In particular any single test of definite reflection parity fails the budget in (11). The parity condition applies to the final predictor. A conditionally centred observable of unordered bridges always has even parity.

Indeed $S_1-g$ has even part $(S_1+S_2-2g)/2$ and odd part $(S_1-S_2)/2$. Each has squared norm $v_S/2$ by independence. The two parity spaces are orthogonal since exchange preserves the measure. Cauchy–Schwarz in each space bounds the squared correlation numerator divided by $\|Y\|_2^2$ by $v_S(\sqrt p+\sqrt{1-p})^2/2$. Subtracting gives (10). The last inequality follows by rationalizing the difference of square roots. For a parity-pure test the sharper first bound leaves $v_S/2$. This fraction is attained by the explicit Wilson test $Y=S_1-S_2$, which has conditional mean zero and subtracts exactly $v_S/2$.

The proof of (1), taking all spatial labels hidden and using the conditional colour estimates *before* adding $J$, gives
\[
 W_K:=\mathbb E_{A_1,A_2}\int_0^1\mathbb E_{p_A} v_S\,ds
       \ \ge\ c\,n^3\beta_K^2/(1+6\beta_K)^4 .
\]
If (11) holds and $W_K$ is finite, the mean of $(p-1/2)^2$ for the measure with density $v_S/W_K$ relative to the endpoint, path-time and midpoint law must therefore be $O((1+\beta_K)^2/n^3)$. The divergence conclusion for a fixed imbalance follows directly from (10) even if $W_K$ is infinite. For instance, take any Wilson spin statistic computed after any smoothing, average its two bridge-exchanged values, then centre it given $A,C$. The resulting test pays at least $W_K/2$, even if its shell response survives the smoothing. A predictor which uses both parity spaces can evade (10) by balancing their norms. Scoring *both* arcs symmetrically changes the regression problem.

## Separation from purity and stopping statement

There is a separation within pure Wilson theory at the **same aspect**, away from the calibrated trajectory. Fix $\beta_*=1/25600$, take the same $n,u$, and put $t_0=\lceil\log_2 n\rceil$. The strong-coupling entrance in row 708 gives
\[
 \log\bigl(\operatorname{Tr}T^{t_0}/\lambda_0^{t_0}\bigr)\le 0.0101\,t_0/n
\]
on every sufficiently large even spatial side. This is the entrance estimate in the proof of TR1, before its coupling-transport hypothesis is used. The strictly positive finite-volume Wilson kernel has a simple positive top eigenfunction. Gauge and centre transformations preserve it by uniqueness, so its eigenvalue $\lambda_0$ is neutral. Each eigenvalue ratio lies in $[0,1]$. Since $u\ge t_0$ eventually, $1\le Z_+(u)/\lambda_0^u\le\exp(0.0101\,t_0/n)$ and $Z_+(2u)/\lambda_0^{2u}\ge1$. Hence $P_K\to1$. At this same fixed positive coupling (1) with a straight grid and (10) with a parity-pure test still cost at least $c(\beta_*)n^3$. Thus the purity threshold can hold in the original Wilson measure while both proposed regressions fail. This comparison makes no assertion about changing the release coupling. [Strong-coupling entrance, proof of TR1](gap-mid-max.md) · [Arithmetic and hypotheses, §3](gap-mid-check.md) · [Wilson top eigenfunction, §4](gap-transfer.md)

In the other direction, (5) measures a normalized spin response. To see what information it contains, tensor $T$ with the neutral matrix having diagonals $1$ and off-diagonals $n^{-2}$. Every normalized Wilson-field measurement in (5) is unchanged on each twist and period. The two extra eigenvalues have ratio $r=(1-n^{-2})/(1+n^{-2})$. Since $1-r^u\le u(1-r)\to0$, this multiplies the purity by $(1+r^{2u})/(1+r^u)^2\to1/2$. The original purity is at most one by positivity of its eigenvalues. This is a transfer comparison with an extra degree of freedom. It explains why a positive spin response alone cannot supply the signed estimate. [Spectator test, check 1527](gap-agy-seed-approaches-neon-check-astra62.md)

The physical carry tested here asks for a fixed positive lower bound on $\min_{v,z}\mathbb E^{z,v} X_{r_N}$ with bounded axes and $N\to\infty$, together with (11) on the same infinite subsequence for a test of those retained Wilson fields. The positive shell requirement is selective. For four-dimensional $U(1)$ the spin response vanishes identically. For five-dimensional $SU(2)$ it is at most $C/r_N\to0$, in every centre sector. Equation (5) realizes that distinction on growing blocked shells. Equation (7) rules out its physical-radius extension for every nested straight-product grid. Theorem 1 rules out the raw-score estimate even when the final coarse radius stays bounded. Theorem 4 separately rules out tests of fixed bridge-exchange parity for any blocking.

For a blocking with directed boundary data, write $\mathcal O$ for its observations and allow the predictor to use $A,C$. The precise remaining signed estimate for the optimal Wilson predictor is
\[
 \mathbb E_{A_1,A_2}\int_0^1\!\left[
   \operatorname{Var}_{p_A}(\mathbb E_Q S_1)
   +\mathbb E_{p_A}\mathbb E_{Q^{\otimes2}}
         \operatorname{Var}(S_1\mid A,C,\mathcal O)
 \right]ds\ \le\ 2(1-\sqrt{457}/25) .                               \tag{R}
\]
All conditional variances hold the chosen path point and tangent fixed. Here $\mathbb E_Q S_1$ uses the scored bridge. Conditional projection attains the residual with $Y=\mathbb E[S_1\mid A,C,\mathcal O]-\mathbb E_Q S_1$. This projection gives exactly the left side of (R) upon optimizing (11). The inequality at the displayed threshold remains open. To carry the spin by this route outside the excluded families still requires the positive physical-radius shell and (R) for one such blocking, with the same $\ell,g_0$ and infinitely many $K$. The shell supplies the group and dimension test. I have no selectivity proof for (R) alone. Its cutoff-independent budget, including the path energy after exact elimination of the first layer, remains unproved. The negative bounds concern the raw score (3). Integrating that layer before differentiating changes the score to its conditional mean.

The proofs are by hand. They have no separate reader or Lean verification. No computation is used to discharge a step. This note grants no scientific status.

RESULT Row 1536. Straight blocking carries a selective spin response to radii of order $\beta_K^{5/32}$ in fine links. Its mean response vanishes uniformly on increasingly resolved seed-radius grids. Straight-grid tests and tests of definite bridge-exchange parity cannot meet the raw signed midpoint bound. PUR-io and the four-dimensional SU(2) mass gap remain open.
