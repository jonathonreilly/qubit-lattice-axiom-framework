# Repo search

FINISH 1445, Codex, assigned gpt-6.2-astra max, at `b0c2eeda4fd5`. The target-specific prior is absent. The lead’s November 8 search covers thirteen earlier UV targets. I checked main at `8b11ae2bb95e` and PRs 10114, 10133, 10134, 10141 and 10144 at `f76f6c649cff`, `89faef229ff6`, `1e70c7211a2c`, `a2f6a430e251` and `1f20846b8057`. Searches outside this lane for good-cell events, weak centre cuts, crossing ribbons, flux-pin calibration and all-exterior plaquette probes found no textual match among those refs’ Markdown and TeX files. I found no competing (GC) owner. [Lead search, §11](prior/repo-search-2026-11-08.md) · [Registry](open-registry.md)

The closest main-branch result is Theorem ZD-c on periodic seeds. The soft-route plaquette witness on PRs 10114/10133 bounds a one-step correlation from below. Grok’s crossover theorem on 10133 assumes crossover decay and source transport. On 10134, I1–I3 relate a gap and its nonempty excited sector to a dynamical witness. On 10141, H-C prices failures of specified UV tests under its certificate hypotheses. These results have different observables or hypotheses from (GC). [Main, ZD-c](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/8b11ae2bb95e/research/mass-gap/library/gap-phys-seed.md#L311) · [One-step witness](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/f76f6c649cff/.claude/science/toe-ruleset-20261021/agents/ym4d-proof/MASS_GAP_LOCAL_BLOCK_ASTRA.md#L106) · [Crossover theorem](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/89faef229ff6/.claude/science/toe-ruleset-20261021/agents/ym4d-proof/MASS_GAP_CROSSOVER_REDUCTION.md#L141) · [I1–I3](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/1e70c7211a2c/.claude/science/physics-loops/ym4d-hard-route-20261030/library/mass-gap-interface.md#L13) · [H-C](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/a2f6a430e251/research/ym4d/library/in1.md#L161)

Row 1197 proposes three suppliers for the Ding–Huang–Yang good-box mechanism. Checks 1407 and 1443 leave (GC) and row 1131’s local two-sector comparison open. Row 1155 already bounds signed curvature defects for two lifts of shared adjoint data. Row 1262 already bounds the cost of prescribed large rectangle holonomies. Its conditional sheet experiment freezes interior links. The Lüscher–Narayanan–Weisz–Wolff Schrödinger-functional background has periodic spatial directions. Below, only the boundary of a four-cube is pinned in the two-flux test. [1197, §2.6](gap-mini-solve-g-fable.md) · [1407, L107](gap-band-fresh-check-astra62.md) · [1443, §5](gap-mech-direction3-check-astra62.md) · [1131, §§2–3](gap-council-prob-astra.md) · [1155, (9), (32)](gap-solve7-astra62.md) · [1262, (20), (27)–(28)](gap-solve30-astra62.md) · [Schrödinger-functional source reading](prior/gap-fullread-1.md)

## Result

**Scoped negative, proved by hand.** At every dyadic side $\ell\ge8$, a cut that needs a positive density of weak bare centre couplings has probability tending to zero even under the most favourable exterior, as quantified in (1). A cut of finite-thickness Wilson ribbons large enough to separate families of neutral loops has the area bound (3), also in the electric-neutral thermal ensemble. For *every* event of uniformly positive pinned mass, (4) rules out contraction at smaller bare sides using one plaquette. Full (GC) on the first-passage band and (M-neutral) remain open.

The contraction convention for a cell event $G$ uses the law of the specified inner reading conditional on the exterior $y$ and on $G$. Its coefficient is the supremum over two pins of the total variation (TV) distance, equivalently the supremum over tests $0\le F\le1$. For the full inner field take its law on gauge orbits, so the tests are precisely its gauge-invariant functions. The negative probability estimates (1) and (3) apply independently of the contraction metric. In the chessboard alternative the probability is the $M$-th root for the simultaneously reflected cell event on a compatible $M$-cell torus.

## Plan saved at start

1. Check the pinned sources, the prior-work record, the open registry, and the Sussman–Alpoge indexes. Identify the exact quantifiers of (GC) and the required carry to (M-neutral).
2. Test a precise event class and scale range against the finite-volume SU(2) Wilson specification. Track the order of the boundary, event, and observable quantifiers and any dependence on the coupling.
3. Prove the strongest supported statement, check its implications against the recorded tests, and identify the next two decisive rows. Label the status of each mathematical step.

## Source checkpoint

Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, give the action and quaternion trace formula in outline L248–260, 2773–2784 and 32534–32538. Their spectral example in L588–599 and 31871–31882 has polynomial decay. They write, “Its support reaches zero.” CA-I L2698–2711 explicitly excludes a mass gap from the theorem. CA-I L56486–56510 gives first-passage arithmetic under its RG inputs. I use the Wilson law on the original links and distinguish its bare coupling from a coupling after blocking. Both source files were fetched once at `31a47c543775`. [Pinned outline](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L248) · [Pinned complete account](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L2698) · [Outline index](sa-index/README.md) · [Outline obligations](sa-index/obligations.md) · [CA-I index](sa-index/ca-4.12-4.19/README.md)

## 1. A uniform obstruction for weak bare centre couplings

**Proved.** Write $w_p=\tfrac12\operatorname{tr}U_p$, $a_p=1-w_p$, and $J_p=\beta|w_p|$. Use the ordinary four-dimensional isotropic SU(2) Wilson specification. A cell has vertices $\{0,\ldots,\ell\}^4$. Pin its tangential boundary links and its exterior. Call a face testable if it has a free link. Take any fixed $\alpha>0$, $0<\eta\le1$, and any $h_\beta=o(\sqrt\beta)$, $h_\beta\ge0$. Let $E_{\ell,\beta}$ be the following event. A connected set of $k\ge\max(1,\lceil\alpha\ell\rceil)$ distinct cell plaquettes contains at least $\eta k$ testable plaquettes with $J_p\le h_\beta$. Allow any two plaquettes with lower vertices within one lattice unit in the maximum norm to be neighbours. The field may select the set. Then

$$
 \lim_{\beta\to\infty}\ \sup_{\ell\ge8}\ \sup_y
             P_y(E_{\ell,\beta})=0.                                      \tag{1}
$$

This covers every dyadic side in the band, at every late cutoff with diverging bare $\beta$. It also covers sets with holes and allows an arbitrary fraction $1-\eta$ of untested or strong faces. In the centre-sign representation $U_e=z_e\widetilde U_e$, the conditional sign Hamiltonian has plaquette coefficient $\beta w_p(\widetilde U)$. Its absolute value is exactly $J_p$. This identifies the interaction in 1197 §2.3.

**Proved, using a prior estimate.** [1155, L305–315](gap-solve7-astra62.md) proves that a class angle to any fixed axis under tilted quaternion Haar law $e^{H\cdot u}du/Z$ has density at most $C\sqrt{1+|H|}$. [Its check, item 46](gap-solve7-check-opus.md) confirms the bound. Conditional on every other link, each of the six incident Wilson plaquettes gives a linear functional of the free quaternion with unit coefficient norm. Hence $|H|\le6\beta$, including for arbitrary pins. Given the remaining three edges, the trace condition is $|\cos t|\le h_\beta/\beta$ for this angle $t$. For $h_\beta/\beta\le1/2$ its interval has length at most $4h_\beta/\beta$. Thus the conditional probability is at most $p_\beta=\min(1,4C h_\beta\sqrt{1+6\beta}/\beta)$.

**Proved.** Of any $q$ prescribed testable faces select at least $q/21$ with disjoint link sets. Each face shares a link with at most $4(6-1)=20$ others. Choose a free link on each selected face. Conditioning on all links except one of these and iterating bounds the joint probability by $p_\beta^{q/21}$. This argument only needs measurability of the other selected tests. With $\Delta=6\cdot3^4$, a rooted connected $k$-set has at most $\Delta^{2(k-1)}$ possibilities, by a traversal of its spanning tree. There are at most $6(\ell+1)^4$ roots and $2^k$ choices of the weak subset. Put $r_\beta=2\Delta^2 p_\beta^{\eta/21}$. For $r_\beta<1$,

$$
 P_y(E_{\ell,\beta})\le
     6(\ell+1)^4\frac{r_\beta^{\max(1,\lceil\alpha\ell\rceil)}}{1-r_\beta}.
                                                                        \tag{2}
$$

The polynomial times $2^{-\alpha\ell}$ is bounded, and $r_\beta\to0$. This proves (1). For any cell event $G\subset E_{\ell,\beta}$ the same bound holds. On a reflected board, condition on each cell’s complement in turn. The other cell indicators are measurable there. Shared boundary links are pins. The $M$-th root of the simultaneous $M$-cell probability has the same upper bound. No reflection-positivity estimate is needed for this direction.

**Proved scope.** This rules out clause (i) for uniformly weak bare centre cuts. For example, a connected crossing of diameter at least $\alpha\ell$ with bounded mean of $J_p$ on its testable interior faces falls under (1) if a fixed positive fraction are so tested. The estimate is for the Wilson action on the original links. A smooth thick flux can have all its microscopic traces close to one. Its treatment requires a different estimate.

**Proved for frustrated sign couplings.** The weak-face hypothesis follows from a pointwise test on the *whole sign weight*. At fixed adjoint data write the sign weight as $W(z)\propto\exp(\sum_p j_p z_{\partial p})$, with $|j_p|=J_p$ and $z_{\partial p}$ the product of its link signs. Choose any sign change $\tau$ whose set $D=\{p:\tau_{\partial p}=-1\}$ is connected, has size at least $\alpha\ell$, and consists of faces with all four links free. The choice of $D$ may use the field. Suppose its cost satisfies $\inf_z W(\tau z)/W(z)\ge e^{-B_\beta|D|}$ over all lifts, with $B_\beta=o(\sqrt\beta)$. Then the event admitting such a choice obeys (1).

Indeed $\log(W(z)/W(\tau z))=2\sum_{p\in D}j_pz_{\partial p}$. Color $D$ in at most 21 edge-disjoint classes by the degree bound above. Choose a class carrying at least $1/21$ of the total absolute weight. Under uniform free link signs, fix its face products to match the signs of the $j_p$, choosing either sign at zero. Every other face product in $D$ still has mean zero. Expanding the conditioning indicators in sign characters shows that only unions of selected four-edge boundaries can have nonzero mean. A different four-edge boundary is no such union, since the selected boundaries are edge-disjoint. The supremum of the log ratio is therefore at least $2\sum_D J_p/21$. At least half of $D$ must have $J_p\le21B_\beta$, so (2) applies. This accounts for cancellations among the original signed couplings.

## 2. A centre cut tested by contractible Wilson loops

**Proved.** There is also an obstruction for a cut selected under the ordinary Wilson law. It applies to finite-thickness ribbons and to moves whose cost is controlled only after averaging. Fix $0<d\le1$ and $0<\rho\le1$. Use an even ordinary periodic four-torus with a cell embedded without wrapping. All lengths below count fine bonds. Pick integers $s,h,m\ge1$ for the transverse spacing, time height and number of grids, respectively, with $ms,h\le\ell/4$. Fit $m$ parallel square grids of side $ms$ in the concentric inner cube, spaced $s$ apart in the third spatial direction. Use the same two time levels on all grids. For each mesh edge $e$ let $R_e$ be its time extrusion and $W_e$ its boundary’s normalized fundamental trace. Its $A=sh$ elementary faces are disjoint from the fine faces of all other ribbons. Ribbons may share boundary bonds.

In a single field call an edge bad if $1-W_e\ge d$. For a pair $U,V$ call it bad if $(1-W_e(U))+(1-W_e(V))\ge d$. The pair may have **any** coupling of the ordinary Wilson law with itself. In each grid give every good edge capacity one and every bad edge capacity zero. Say that a grid has a cut if some edge separator between its two opposite vertical sides has fewer than $m/2$ good edges. This allows holes in a proposed wall. Denote by $D$ the event that at least $\lceil\rho m\rceil$ grids have such a cut.

There are $b_d>0$, $c_{d,\rho}>0$ and $\beta_{d,\rho}<\infty$ such that on every such torus,

$$
       A^2\le b_d\beta,\quad \beta\ge\beta_{d,\rho}
       \quad\Longrightarrow\quad
       \Pr(D)\le \exp[-c_{d,\rho}(\beta/A)m^2].                          \tag{3}
$$

For any specified $M$ disjoint cells with the same parameters and disjoint ribbon faces the right side acquires a factor $M$ in its exponent. Reflected placements are allowed. Neither estimate depends on the exterior volume. The statement quantifies a class on **every** cell size where the grids fit. One can set $s=h=1,\ m=\ell/4$ on dyadic cells, or take square coarse faces of side $s=h\le(b_d\beta)^{1/4}$. For a mesh edge of width one the permitted height grows as $\sqrt{b_d\beta}$.

**Proved, prior inputs.** For each deterministic set $F$ of distinct fine faces, [1155, (9)](gap-solve7-astra62.md) proves

$$
                 {\mathbb E}\exp(t\beta\textstyle\sum_F a_p)\le C^{|F|},
                 \qquad t=1/8 .
$$

Use $C\ge e$ by enlargement. The [check of (9)](gap-solve7-check-opus.md) verifies the positive-transfer and Hölder comparison for rectangular periodic tori. The disk estimate $1-W_e\le A\sum_{p\subset R_e}a_p$ is [1262, (27)](gap-solve30-astra62.md). Peeling the disk writes its holonomy as a product of conjugated fine holonomies. Squared chordal distance to identity is $2a_p$. The triangle inequality and Cauchy–Schwarz give the factor $A$.

**Proved.** For a fixed set of $k$ bad edges let $F$ be their $Ak$ fine faces. The pair satisfies $\sum_F(a_p(U)+a_p(V))\ge dk/A$. Exponential Markov at $t\beta/2$ and Cauchy–Schwarz on the joint law bound the probability by

$$
        q^k,\qquad q=\exp[A\log C-td\beta/(2A)].
$$

Only the two marginals entered. The one-field bound follows by taking $V=U$, since a one-field bad edge is then pair-bad. Choose $b_d=td/(4\log C)$. Then $q\le\exp[-td\beta/(4A)]$. This bound uses the fine action. The separating sets in the fixed grids may be chosen after sampling.

**Proved.** An edge separator in the square grid contains the crossed edges of a simple dual path from bottom to top. One proof colors vertices reachable from the left after deleting the separator. All left vertices are colored, all right vertices uncolored. The dual interface crosses only deleted edges. At every square it has even degree, since the number of color changes around the square is even. The numbers of interface endpoints on the bottom and on the top are both odd, by their left and right endpoint colors. At least one component connects bottom to top. Erasing loops gives the simple path. Boundary endpoints here are distinct dual leaves. A resulting path has $k\ge m$ edges. If the cut has fewer than $m/2$ good edges, at least $k/2$ crossed edges are bad. With at most $m$ bottom starts and at most four choices per step, the sum over paths and choices of bad edges is at most

$$
                        m\sum_{k\ge m}(8\sqrt q)^k .
$$

For specified planes, take the product of these combinatorial sums. The probability bound for **each union** of marked edges is $q^{\#\text{marked}}$, irrespective of dependence between planes. Choose $\lceil\rho m\rceil$ planes in at most $2^m$ ways. Since $\beta/A\ge\sqrt{\beta/b_d}$, increasing $\beta_{d,\rho}$ absorbs the factor 8, the geometric tail, $m$, and $2^m$ into the exponential in (3), uniformly for $m\ge1$. For example $\log(2m)\le2m$ suffices. Applying exactly the same union estimate across cells proves the $M$-cell bound.

**Proved in the electric-neutral thermal ensemble.** Take the spatially untwisted periodic cube and period $2w$. Insert $P_0=2^{-3}\sum_b R_b$ in the Wilson transfer trace. The positive path law mixes the eight temporal twists with weights $Z_b/\sum_{b'}Z_{b'}$. For twist signs $\tau_p^b$ read $a_p^b=1-\tau_p^b w_p$, and on a ribbon read $(\prod_{p\subset R_e}\tau_p^b)W_e$. These agree with the ordinary readings away from the seam. The disk inequality still follows by peeling because the signs are central. [1155, L414–422](gap-solve7-astra62.md) bounds the marked moment by $C^{|F|}$ for each twist measure *divided by the untwisted partition function*. In the normalized mixture the bound is at most $8C^{|F|}$, since $\sum_b Z_b/Z_0\ge1$. [Check of the mixture normalization](gap-solve7-check-opus.md)

Apply Cauchy–Schwarz to any coupling of two of these mixture marginals as above. For each union of marks there is one factor 8, including on a whole board. With the tilted estimate’s $t>0$, adjusting $b_d,c_{d,\rho},\beta_{d,\rho}$ gives (3) here too, for grids that fit the period. This controls the cut distribution inside the correctly projected trace. Its normalizer cancels throughout the probability estimate.

**Proved consequence for a one-copy event.** If $G$ requires this cut of coarse plaquette curvature in one field, $P(G)$ is bounded by (3). There is some exterior with conditional probability no larger than the periodic average (equivalently its essential infimum is no larger). The simultaneous board bound gives the same upper bound for its chessboard root. Thus neither reading of (i) can hold uniformly along $\beta\to\infty$. This conclusion applies even to a single thick layer of large curvature selected inside the cell if it meets the specified crossing test. An isolated vortex need not satisfy this separator test.

**Proved consequence for an actual centre move.** Suppose a proposed event admits a resampling kernel on the free cell links. For every pin $y$ the kernel preserves the Wilson conditional law $P_y$. On $G$ it achieves the following effect with probability at least a fixed $r>0$. On the grid links (the straight spatial transports at both times and the time columns at the vertices), the new field agrees with the old field up to link signs and vertex gauge transformations. In at least $\lceil\rho m\rceil$ grids, the relative centre sign is negative on the ribbon loop of **every** simple path from left to right. The move, signs, gauges and successful grids can depend on both fields. Each loop follows the path at the bottom, returns at the top and uses the two end columns. The loop bounds a disk inside the inner cube, so its trace is local and electric-neutral.

For a mesh edge let $\varepsilon_e$ be the product of the four relative signs around its ribbon. The sign on a path ribbon is $\prod_{e\in\gamma}\varepsilon_e$, since intermediate column signs occur twice. If $\varepsilon_e=-1$, the two normalized ribbon traces are negatives of each other. Their two deficits sum to 2. Every indicated path must therefore meet a bad edge. Deleting all bad edges disconnects the grid sides, so the pair satisfies $D$. Taking the ordinary first field and one resampled second field gives $rP(G)\le\Pr(D)$. For an entire board, condition on the shared boundary bonds. No fine plaquette contains free bonds from two cells. The cell laws factor with these bonds pinned. Apply the preserving kernels with independent draws in the cells. The second field is again Wilson, and on the simultaneous event the chance of all required moves is at least $r^M$. Equation (3) bounds the chessboard root of $G$ by $r^{-1}\exp[-c_{d,\rho}(\beta/A)m^2]$. This argument also applies directly to moves satisfying the pair-cut criterion with probability $r$, including approximate changes of curvature with the stated deficit threshold. It uses no pointwise comparison over sign backgrounds.

**Proved for partial moves.** It suffices to give, at each pin $y$, a measurable subprobability coupling of mass $u_y\ge rP_y(G)$ supported on successful pairs, with both marginals dominated by $P_y$. To complete it, add the product of the two residual marginals divided by $1-u_y$ when $u_y<1$. This gives a coupling of two Wilson conditionals. Using independent completed couplings over the board proves the same root bound. In particular, an accepted move can be specified just on the fraction of the law on which it succeeds.

**Scope.** A move may change the adjoint data away from the specified grid. A mixture can decorrelate each fixed observable without reversing all crossing loops in one draw. Such a mixture is outside the centre-move conclusion. The bound for coarse ribbons requires $A^2\le b_d\beta$. Smooth flux distributed over an area of order $\ell^2$ at a band scale remains open.

## 3. Every positive-probability event at small bare sides

**Proved.** There is a separate obstruction to clause (ii) which puts **no restriction on the event**. Take $8\mid\ell$, $\beta\ge2$. There are two exterior pins, $y_0,y_\phi$, and one elementary $12$-plaquette $p$ in the concentric side-$\ell/4$ cube. The plaquette is chosen before the event. For every measurable cell event with $P_{y_i}(G)\ge c_0>0$ at both pins, the total variation distance of the two conditioned **single-plaquette class-angle laws** obeys

$$
 d_{\rm TV}\bigl({\cal L}_{y_0}(\theta_p\mid G),
                 {\cal L}_{y_\phi}(\theta_p\mid G)\bigr)
       \ \ge\ 1-\frac{C}{c_0}\frac{\ell^4\log(2\beta)}{\beta}.           \tag{4}
$$

Here $d_{\rm TV}=\sup_B|P(B)-Q(B)|$ and $\theta_p=\arccos w_p$. The same pins preserve asymptotically the *relative contrast of means of the ordinary plaquette action* after conditioning on any such event. In particular any fixed $\theta<1$ fails along every sequence with $\ell^4\log(2\beta)=o(\beta)$. The pins lie on the four-dimensional cube boundary. Every interior link is integrated.

**Proved, calibration.** Fix $\phi=1/8$, $a=\phi/\ell^2$, and $T=\operatorname{diag}(i,-i)$. The trivial pin restricts the identity field. The flux pin restricts $U_2(x)=\exp(a x_1 T)$ with all other positive links equal to one. Extend the pins arbitrarily to the exterior of an embedded cube. Each $12$-plaquette of this filling has angle $a$, and all other plaquettes are flat. In every full $12$-square at fixed $x_3,x_4$, all four perimeter paths are pinned. Their product has angle $\phi$. For *every* filling the group triangle inequality on the peeled square gives $\sum_{p\ \mathrm{in\ square}}\theta_p\ge\phi=\ell^2a$.

Put $f(u)=1-\cos u$. For $0\le a\le1/8,\ 0\le u\le\pi$,

$$
      f(u)-f(a)-\sin a\,(u-a)\ \ge\ (u-a)^2/32 .                       \tag{5}
$$

Indeed for $v=u-a$ the left side is $\cos a(1-\cos v)+\sin a(\sin v-v)$. The first parenthesis is at least $2v^2/\pi^2$. The second is nonnegative for $v\le0$ and at least $-v^2/2$ for $v\ge0$, by integrating $1-\cos x\le x$. Use $\cos a\ge3/4,\ \sin a\le1/8,\ \pi<4$. Let $S$ be the sum of the plaquette deficits in the closed cube, including the constant boundary terms. There are $N_{12}=\ell^2(\ell+1)^2$ faces of the chosen orientation. Sum (5) plane by plane. The linear term has nonnegative sum, and all other orientations have nonnegative action. Therefore

$$
       S-S_* \ \ge\ \tfrac1{32}\sum_{p\parallel12}(\theta_p-a)^2,
       \qquad S_*=N_{12}f(a).                                          \tag{6}
$$

The displayed filling attains the bound at zero excess. For $y_0$ the same argument uses $a=S_*=0$. This proves the minimum and the stated stability for every filling.

**Proved, finite-temperature bound.** There are $P=6\ell^2(\ell+1)^2$ plaquettes and at most $N=4\ell(\ell+1)^3$ free links. In the product of geodesic balls of radius $1/\beta$ about the displayed filling, each plaquette angle changes by at most $4/\beta$. This follows from bi-invariance, the triangle inequality and the distance to identity. The function $f$ is 1-Lipschitz. A ball has normalized Haar mass at least $b\beta^{-3}$, for an absolute $b>0$, by integrating $(2/\pi)\sin^2 t$ radially on $S^3$. For either pin the partition function on the free links satisfies

$$
      Z_y \ge e^{-\beta S_*-4P}(b\beta^{-3})^N,\qquad
      {\mathbb E}_y(S-S_*)\le C_1\ell^4\log(2\beta)/\beta .
$$

For the second inequality use nonnegativity of relative entropy against normalized product Haar, $0\le-\beta{\mathbb E}_y S-\log Z_y$. The cap-and-entropy method for arbitrary raw pins is already in [1262, (5)](gap-solve30-astra62.md). Here it is applied at the two calibrated minima.

**Proved, one neutral observable.** The inner cube has $M=(\ell/4)^2(\ell/4+1)^2$ faces of orientation $12$, so $Ma^2\ge\phi^2/256$. Average (6) for both pins over those faces. Some deterministic $p$ satisfies

$$
 \frac{{\mathbb E}_{y_0}\theta_p^2+
       {\mathbb E}_{y_\phi}(\theta_p-a)^2}{a^2}
       \le \epsilon_{\ell,\beta}:=C_2\,\ell^4\log(2\beta)/\beta .
$$

Markov’s inequality at $a/2$ bounds the sum of the two classification errors by $4\epsilon_{\ell,\beta}$. Conditioning on $G$ multiplies this bound by at most $1/c_0$. The indicator ${\bf1}_{\theta_p>a/2}$ proves (4). For the fixed observable $f(\theta_p)=1-w_p$, use $f(u)\le u^2/2$ at the trivial pin and
$\lvert f(u)-f(a)\rvert\le a|u-a|+(u-a)^2/2$ at the flux pin. Since $f(a)\ge2a^2/\pi^2$, the difference of the two conditional means, flux minus trivial, divided by $f(a)$ is $1+O(\sqrt{\epsilon_{\ell,\beta}/c_0}+\epsilon_{\ell,\beta}/c_0)$. Taking $G$ to be the whole space gives the same limit for the unconditioned contrast. The bounds are uniform in the choice of $G$. Thus a fixed-factor reduction of this pair’s contrast also fails in this range. At finite size the unconditioned error expectations are continuous in the exterior pins, since the positive finite-dimensional Wilson densities vary uniformly. Open pin neighbourhoods retain these bounds with arbitrarily small additive losses, if “every exterior” is interpreted essentially.

**Scope.** Equation (4) uses the lower probability at both pins. A chessboard lower bound alone supplies neither of these two probabilities. Also, (4) concerns sides measured in **bare lattice bonds**. It cannot be placed in the physical band by measuring the same integer in first-passage units.

**Proved limit of this witness.** The particular binary test in (4) loses its distinguishing power when $\ell/\beta^{1/4}\to\infty$. For a tilted link with $|H|\le6\beta$, its Haar density is at most $C(1+\beta)^{3/2}$. Integrating on the ball of radius $(1+|H|)^{-1/2}$ about the maximizing quaternion gives this bound by cancellation of the factor $e^{|H|}$. This is the density estimate in [the capped-plaquette argument](gap-solve24-astra62.md), L383–389. The Haar cap $\theta_p\le a/2$ has mass at most $C a^3$. Thus for **every** exterior, and after every event of conditional mass at least $c_0$,

$$
       P_y(\theta_p\le a/2\mid G)
            \le (C/c_0)\bigl(\sqrt{1+\beta}/\ell^2\bigr)^3.              \tag{7}
$$

This exact upper bound applies to either pin and to every interior plaquette of the chosen orientation. Merely improving the entropy estimate in (4) cannot make this particular indicator work on band-size cubes.

## 4. A restricted good event which does occur

**Proved, for prescribed readings.** Fix $k$ distinct elementary plaquettes in the inner cell. Choose distinct marked links, one on each plaquette, so that no action plaquette contains two marks and all faces incident to a mark lie strictly inside the outer cell. The statement holds at every dyadic side that fits the marks, and throughout the bare weak-coupling regime $\beta\ge2$. There is a gauge-invariant cell event $G$ with chessboard root at least $1/2$. Given $G$, under *any two exterior pins* the joint law of these $k$ plaquette traces has total variation distance at most $1-b_k$, with $b_k>0$ independent of side and coupling. This is the finite-observable application of the prior cap estimates. [Separated marked plaquettes, L291–305, 383–389](gap-solve24-astra62.md) · [Local two-link cap bound, L181–183](gap-solve26-astra62.md)

**Proved.** Expose all links except the marks. A mark passes when some value of that link makes all its six incident deficits at most $K/\beta$. Let $G$ require all marks to pass. The condition is measurable by compact minimization and invariant under changes of vertex gauge. It is independent of the actual marked link values once the other links are fixed. A failure requires the sampled field to have a face with $a_p>K/\beta$ among at most $6k$ faces. Equation (9) of 1155 gives ordinary periodic failure probability at most $6kC e^{-tK}$. Choose $K=K(k)$ large enough that this is at most $1/2$. Finite-torus chessboard domination puts the single-cell probability below the root of the fully reflected event. Apply (AM6) successively in four directions with the other cells filled by 1, using ${\bf1}_G+\varepsilon$ and then $\varepsilon\downarrow0$. The site planes allow shared boundary bonds, and the marks here are strictly inside. This uses Sussman and Alpoge with Claude and Codex, outline L2885–2938 and L23668–23699.

On a passing star write the six deficits as $1-u\cdot v_i$ in the free link quaternion $u$. Each $v_i$ lies within chord $\sqrt{2K/\beta}$ of one witness. On the ball of geodesic radius $\beta^{-1/2}$ about the target of the selected plaquette, all six deficits are at most $C(K+1)/\beta$. The conditional normalizer is at most $C\beta^{-3/2}$, by keeping just the selected plaquette deficit and integrating its radial Haar density. On that ball the unnormalized density is at least $e^{-C'(K+1)}$, and the ball has Haar mass at least $c\beta^{-3/2}$. Therefore the plaquette holonomy dominates a mass $b(K)>0$ times normalized Haar on the identity ball of radius $\beta^{-1/2}$. Multiplication by the fixed links and inversion carry the target ball isometrically to that ball. The free marks are conditionally independent. Passing to traces and integrating the exposed variables on $G$ preserves the common reference component of mass $b_k=b(K)^k$. Every pin permits $G$ with positive probability, by making the interior links around the marks close to identity.

**Proved, an all-exterior version for one averaged probe.** Fix one orientation and pick $p$ uniformly in the central cube’s elementary plaquettes of that orientation, independently of the field. Reveal its location as well as its trace. For every dyadic $\ell\ge\max(16,4\beta)$ the unconditional laws of this pair for any two pins have TV distance at most $1-b$, for one absolute $b>0$. Equivalently this bounds all averages $M^{-1}\sum_p F_p(w_p)$ with $0\le F_p\le1$. Here $G$ is the whole configuration space. To see this, apply [1262, (10)](gap-solve30-astra62.md) inside an even side-$\ell/2$ update containing the central cube and its one-link margin. Condition first on the exterior of that update. For each of the six orientations its sum of internal deficits has mean at most $C\ell^4(\ell^{-1}+\beta^{-1})$. Use the lower link of one fixed direction as each mark. The marks are then distinct and each incident face occurs in at most four stars. The number of probe plaquettes is at least $(\ell/4)^4$. Hence the pin-uniform average of the six-star deficit sum is at most $C'/\beta$. If the star of $p$ cannot pass, its deficit sum exceeds $K/\beta$. Choose $K\ge8C'$. For each pin $y$, its passing probabilities $d_y(p)$ then average at least $7/8$. In the two laws the common reference for $p$ has mass at least $b(K)\min(d_y(p),d_{y'}(p))$. Averaging gives at least $3b(K)/4$, as claimed. The extra randomness selects the location of the probe.

**Scope.** The fixed-probe lower bound uses the chessboard alternative in (i). The averaged bound uses every exterior. Neither controls all functions of the joint inner field. Fixed-size probe sets and the spatially averaged read are distinct from the inner-cell sigma-field in (GC).

## 5. The correlation length and the neutral trace

**Proved scope of the scale comparison.** The band obstruction is (1) or (3) for the specified events. Neither needs a value for the correlation length $\xi$. Equation (4) excludes *all* events of uniformly positive pinned mass on the smaller bare-size range, with a single neutral witness. In the Sussman–Alpoge parametrization $a_{\rm lat}=B^{-K}$, $B>1$ the block factor, the first-passage cell has $B^K$ fine bonds to a side. At a **fixed** target coupling $g_*$, CA-I L56442–56459 gives, under its stated inputs, $K\ge(\beta-g_*^{-2})/B_\sharp-1$ and $g_K\ge(g_*^{-2}+B_\sharp)^{-1/2}$. The range of (4) ends before that first-passage side. Even an effect vanishing as the running coupling tends to zero would require a sequence with that coupling tending to zero *in the claimed band* to contradict fixed $c_0,\theta$. The first-passage arithmetic gives no such sequence at fixed $g_*$.

**Guessed in 1197 and still open.** A general necessity $\ell\gtrsim\xi_{\rm lat}$ for (GC) would require a bound on the effect of every admissible event on the full inner law, or a deduction of a correlation length from such a contraction. The weak-coupling order of an individual deformation supplies neither. Equations (4) and (7) locate the range of a specific all-events test. Section 4 gives actual contractions on smaller families of observables at sides chosen without reference to $\xi$. Smooth collective changes of adjoint data on the cell scale and interscale orientation events with a genuinely collective neutral response remain undecided.

**Open carry to (M-neutral).** On *some* fixed admissible physical side $L_*$, [1367](gap-seed-astra62.md) needs, at every sufficiently late cutoff on its trajectory, $n_j=L_*/a_j$, $4\mid n_j$, $n_j\ge2^{70}$, $\beta_0\le\beta_j\le B_0\log n_j$, and

$$
       \sum_{\nu\ge1}\bigl(\lambda_{\nu,+}/\lambda_0\bigr)^{
                        2\lfloor n_j/1024\rfloor}\le 4/21 .
$$

The zero spatial twist and all eight electric translations enter the projection. The sum counts multiplicities. The pin overlap in §4 controls a prescribed list of readings. Its bound $b(K(k))^k$ deteriorates as the list grows. Equation (3) in the projected ensemble controls a probability normalized by the thermal trace. It gives no upper bound on the trace relative to the vacuum. Thus the results exclude suppliers and give a finite-observable variant, with no carry to (M-neutral). The subsequent gap implication still requires the matched continuum inputs (P1)–(P4), (H2) and totality. [Row 1359](gap-mini-mneutral-check-astra.md)

### Tests of the surviving finite-observable variant

These are the tests of [1386, §4.5](gap-mech-direction2-fable.md), with the [1387 corrections](gap-mech-direction2-check-astra62.md) and the [1443 Villain qualification](gap-mech-direction3-check-astra62.md). The negative bounds require no selectivity to serve as obstructions.

- **(t1) The local gain persists for compact U(1) Wilson (proved).** The unnormalized Fourier coefficients of $e^{-u(1-\cos v)}$ are $e^{-u}I_{|n|}(u)$. The ratios $I_j/I_0$ are increasing for $j\ge1$, by the adjacent-ratio proof in [1149, (16)](gap-solve4-astra62.md) and $(I_1/I_0)'=\operatorname{Var}(\cos v)$ in the circle tilt. Halving the coupling therefore increases each coefficient by at most the ratio of the two zeroth coefficients, bounded uniformly for $\beta\ge2$ by the circle Gaussian integral bounds. Integration of the product Fourier series on an ordinary torus keeps only link-balanced integer assignments, all with nonnegative coefficients. Hence the marked moment $\mathbb E e^{(\beta/2)\sum_F(1-\cos v_p)}\le C^{|F|}$ holds there. The same good-star proof uses circle balls of mass comparable to $\beta^{-1/2}$. There is no abelian zero in the overlap used here.
- **(t2) The local step also holds in five dimensions (proved).** In 5D there are eight staples per link. For the one-face tail used for fixed probes, take an incident direction as transfer time. Replacing that electric factor by the half-coupling factor costs at most $z_{\beta/2}/z_\beta$ in positive-operator order by 1149 (16), independent of the number of transverse directions. The magnetic half-weights preserve order, which persists upon tracing against the remaining homogeneous positive steps. The local cap and union estimates of §4 then hold in 5D as well. They propagate no stiffness with the four-dimensional scale factor and give no estimate of the sixteen electric sectors of the five-dimensional comparison. The weak-coupling massless-phase premise (P5) for five-dimensional SU(2) is conjectural in these tests.
- **(t3) Proved scope for SU(3).** The literal sign $-I$ in §2 belongs to SU(2) and lies outside SU(3). On the positive side $1-\operatorname{Re}\operatorname{tr}(U)/3=\|U-I\|_{\rm HS}^2/6$ gives the same local cap argument near identity in eight dimensions, provided the required typical-star probability is available. No SU(3) sector estimate is used or derived. Check 1387 permits a specifically SU(2) conclusion.
- **(t4) Proved failure as a seed criterion.** At a fixed admissible side and fixed finite probe list the chessboard variant of §4 persists as $\beta\to\infty$. On that very box each fixed-index **neutral** eigenvalue ratio tends to one, so the neutral excited trace at fixed positive integer time diverges. This is [1215, (5)](gap-solve23-astra62.md), as corrected into the filter by 1387. The charged periodic excitations are a separate test. This counterexample tests the fixed-box inference. The physical trajectory has increasing $n_j$.
- **(t5) The estimates admit independent local tests (proved).** A pin, a marked plaquette, or a collection of ribbon deficits tests (1), (3), (4) and the cap bound without a neutral spectrum. The unresolved extensive estimate in 1367 would have to control the sum of losses on the two physical-time faces. Restricting to finitely many of those readings does not bound that sum.
- **(t6) Proved comparison of the local step.** On an ordinary 4D U(1) Villain torus use $v_\beta(u)=\sum_{j\in\mathbb Z}\exp[-\beta(u-2\pi j)^2/2]$ and $r=\operatorname{dist}(u,2\pi\mathbb Z)$. For $\beta\ge2$, $e^{-\beta r^2/2}\le v_\beta(u)\le C e^{-\beta r^2/2}$. With $|u|\le\pi$ and $|j|\ge1$, the excess square is at least $4\pi^2|j|(|j|-1)$. Thus $v_\beta e^{\beta r^2/4}\le C v_{\beta/2}$. Integrating the Gaussian Fourier transform gives $\widehat v_\beta(n)=(2\pi\beta)^{-1/2}e^{-n^2/(2\beta)}$. The half-coupling coefficient is at most $\sqrt2$ times the original one. The positive integer-current sum gives the same uniform marked-moment bound for $\beta r^2/4$. On the passing stars the circle cap provides the same common probability component, by the preceding Gaussian bounds. This matches the periodic state, local observable, weak-coupling normalization and scale of the fixed-probe test. At any fixed large $\beta$ the Villain link conditional also has a positive Haar component for **every** pin, since $\min v_\beta/\max v_\beta>0$. The latter observation applies in the fixed-boundary boxes used for the Fröhlich–Spencer massless state. This last constant depends on $\beta$. The thermodynamic nonsummability input is the one read in [1443, §1(d)](gap-mech-direction3-check-astra62.md). No finite-period projected trace or continuum trajectory is equated with that state. Neither this overlap nor the independent heat factor of (VIL) supplies a mass gap. A later group-dependent estimate on the remaining field would have to be tested on its own hypotheses. [Fröhlich–Spencer source reading](prior/gap-lit-u1.md)

**Proved for the averaged probe in these comparisons.** The same boundary-to-volume argument as in 1262 (10) applies to the circle weights above in 4D and to Wilson SU(2) in 5D. Cutting a periodic side-$s$ box changes at most $C s^{d-1}$ plaquette factors. The normalized density comparison costs $e^{C\beta s^{d-1}}$ for every pin since the log oscillation per face is $O(\beta)$. For 5D SU(2) use the many-mark proof of 1155 (9) with five groups. Within each group mark electric plaquettes in one time direction, use the tensor order on each layer and trace Hölder across the layers, then use ordinary Hölder over the five groups. This gives $\mathbb E_{\rm per}e^{t_d\beta\sum_F a_p}\le C_d^{|F|}$ with $t_d>0$. The circle comparisons in (t1) and (t6) already give this bound, using $r^2$ for Villain. Apply the density comparison and Jensen to the sum over internal faces of one orientation. After division by $\beta s^d$ the mean per face is $O(s^{-1}+\beta^{-1})$. Thus the location-and-trace overlap of §4 holds in the matching local experiments as well. This step requires no assumption on an infinite-volume phase.

**Verification.** The new estimates are hand proofs by Codex, without a second-provider check. The prior estimates and the scope of their checks are identified above. No numerical result, generated Lean proof or compiled evaluator enters the argument. This research note grants no scientific standing.

## Next two rows and their decisive outcomes

1. **T0 first, check the existing CM-O3 row 1444 with its owner.** At the Chapter 5 substitution, match every old-term complex read to the claimed companion and domain. A uniform match at every required read settles that supplier. An admissible read outside the claimed domain sends the first failing case back to the same owner. This follows the current allocation in [1443, final section](gap-mech-direction3-check-astra62.md).
2. **Cross-provider check of 1445.** Check the arbitrary-pin estimate (2), disjoint fine faces and the board and neutral normalizations in (3), and the *single plaquette chosen before the event* in (4). Check the chessboard inequality direction and the fixed-$k$ limit in §4. The decisive outcomes are confirmation on these stated classes or an admissible configuration, coupling, or quantifier showing the first failed bound. The existing R1 literature scan is row 1446. A broader band proof would need a new estimate on collective inner data.
