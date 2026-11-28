# Repo search

**GUIDE — work plan.** (1) Check prior work and identify the probability estimate at the obstruction. (2) Rank candidate attacks and test their hypotheses against the controls. (3) Attempt the first estimate for the leading attack. (4) Compare the attacks with the route registry and its cited results. (5) Record the result and remaining obligation.

**GUIDE.** Row 1131, probability and Gibbs measures, at `8466e1295`. The target-specific prior file was absent. The November 8 digest covered main and PRs 10114, 10133, 10134 and 10141. The soft-route `MASS_GAP_LOCAL_BLOCK_ASTRA.md` gives a positive one-step plaquette correlation at finite bare coupling and reports a physical-time contraction at $\beta\le1/32$. The correlation gives an *upper* bound on the excitation energy. The PR 10141 snapshot retains the terminal covariance in a free ultraviolet decomposition, and the PR 10114 seam review keeps the covariance of conditional means. The required estimate is an upper bound on the full excited transfer weight at fixed physical size. [PR 10114, one-step witness](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/f76f6c649c/.claude/science/toe-ruleset-20261021/agents/ym4d-proof/MASS_GAP_LOCAL_BLOCK_ASTRA.md#L106-L175) · [PR 10114, seam review](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/f76f6c649c/.claude/science/toe-ruleset-20261021/agents/ym4d-proof/CODEX_REVIEW_SEAM.md#L21-L46) · [PR 10141, terminal covariance](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/a2f6a430e2/research/ym4d/library/tp1.md#L71-L88)

**GUIDE.** I checked those passages at the fetched PR revisions, searched the soft-route and `research/ym4d` trees at main `8b11ae2bb9` and PR heads `f76f6c649c`, `89faef229f`, `1e70c7211a`, `a2f6a430e2`, `1f20846b80` (including PR 10144) for replica winding, permutation seams, disagreement percolation and pinned-cell stiffness. The scoped search returned no match. Row 1131 has no separate “Repo prior work” entry. I found no owner for this replica-cover question in `open-registry.md`. The November 8 digest concerns mostly ultraviolet obligations and does not inventory the later gap rows. [Lead's digest](prior/repo-search-2026-11-08.md) · [Council brief, §§2–5](gap-council-brief.md)

## 1. The probability estimate at the obstruction

**PROVED (finite-volume identity, given the transfer representation in the brief).** On a rectangular periodic box $B$, double the direction of length $n$ to obtain $B'$. Write $F(B)=\log Z(B)$, use the transfer operator $T$ normal to that direction, and put $\rho=T^n/\operatorname{Tr}T^n$. Then

```math
d(B)=2F(B)-F(B')=-\log\operatorname{Tr}\rho^2,\qquad
d(B)\ \ge\ -\log p_0\ \ge\ \log(1+e^{-n m}).
```

Here $p_0$ is the largest eigenvalue of $\rho$, $m=-\log(\lambda_1/\lambda_0)$ is in lattice time units, and $\lambda_1$ includes every flux sector. Indeed $\sum p_i^2\le p_0\sum p_i=p_0$, and $1/p_0=\sum_i(\lambda_i/\lambda_0)^n$. The free energy that must shrink measures how much weight survives outside one state. Local relaxation of a chosen plaquette need not see that weight.

**ARGUED (published comparison).** The closest working probability theorem for the geometric attack below is Ding, Huang and Yang, Theorem 1.4. In a free-boundary square of the two-dimensional metric graph with conditioned vertex local times and $2<N\le3$, they bound one-colour connectivity between vertices of its central half exponentially, uniformly for bounded local times. Independent cluster signs and Lupu's isomorphism relate this to the spin estimate in their Theorem 1.1. The step that stops here is the identification of the law to which their connectivity estimate applies. Applying their theorem here would require a Wilson representation with that conditional loop law and a connection event controlling the full transfer trace across flux sectors. Their spin representation supplies neither identification. The attempted four-dimensional port of OpenAI's pinned-cell proof stops at the corresponding all-observables step (L3) in brief §6. [Jian Ding, Fenglin Huang and Peng Yang, Theorems 1.1 and 1.4](https://arxiv.org/abs/2611.04908) · [Council brief, §6](gap-council-brief.md)

**ARGUED (scope of the ultraviolet input).** Tadeusz Bałaban's renormalization-group methods enter through Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. Their outline stops the drift estimate at $K$, with $h<x_K\le h+B$ when $K>0$. Their complete account I, 4.19, assumes the per-step bounds in its two-sided drift lemma. It expressly reserves the infrared spectral question. I used the outline index, neighbouring rows in chunks 18 and 29, its obligations, and the 4.12–4.19 index before checking these passages. [Outline, first passage](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L19849-L19883) · [Outline, infrared scope](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L31871-L31882) · [Complete account I, lines 2702–2711](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L2702-L2711) · [Complete account I, lines 56342–56365](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L56342-L56365)

## 2. Ranked attack

**GUIDE — rank 1, a two-sheet winding test.** Use two independent copies of the actual Wilson field. At a plaquette, reserve the part of their joint Boltzmann weight common to *every* assignment of its four link pairs to the sheets. An unreserved plaquette joins its four link labels and can transmit a sheet permutation. If no joined cycle winds oddly in the direction being doubled, one can relabel the sheets consistently throughout the joined region. This would give a one-sided bound on the *partition function* of the connected double cover using one event in the independent pair. The nearest item in brief §5 is the failed independent-replica swap/pinned-cell criterion. Here there is no imposed swap of a macroscopic interface. The proposed comparison sums over ways of erasing plaquettes and pays only for cycles on which sheets cannot be consistently relabelled. It reads the full transfer trace. The graphical idea comes from joint spin and bond representations of Edwards and Sokal and from disagreement percolation. Section 4 identifies the specific local exchange rule already in the repository.

**GUIDE — first estimate, refuted in §3.** Write $B_k(n)=(2n)^k\times n^{4-k}$ as shorthand for a four-torus with $k$ doubled sides. For $0\le k\le3$ double the next side $\mu=k+1$. Let $P_{B_k,\beta}^{\,0}(W_\mu)$ be the probability that the active plaquette–link incidence graph of the **bare** two-replica law defined in §3 has a cycle of odd $\mu$-winding. The proposed estimate is

```math
\exists L_0,C,c>0\quad \forall r\in\mathbb Z_{\ge0},\ L=2^r L_0,\quad
\forall k\in\{0,1,2,3\},\qquad
\limsup_{j\to\infty}P^0_{B_k(n_j),\beta_j}(W_\mu)\le C e^{-cL}.
\tag{1}
```

Here $L_0$ is an admissible dyadic physical size beyond first passage. The bound is to hold on each compatible sequence of even tori with $a_j n_j=L$ at fine cutoffs of the stated Wilson trajectory. Row 720 assumes the base physical side divided by $4a_j$ is integral at fine cutoffs, so this even-size test is nonvacuous. The constants are in physical units. An exponential estimate is stronger than needed. The next calculation specifies a single rectangle that suffices.

**PROVED (rectangular seed, conditional on the cover bound in §3).** Take $B_3(n)$, time extent $n$ over a spatial cube of side $2n$. Let $p=P^0_{B_3(n),\beta}(W_{\rm time})$. Its entire excited thermal sum $S(n;(2n)^3)=\sum_{i>0}(\lambda_i/\lambda_0)^n$ obeys

```math
 1+S=1/p_0\ \le\ e^d\ \le\ (1-p)^{-1}.
```

Thus $\limsup_j p<1/5042$ at this single shape and one physical size gives $\limsup_j S<1/5041$, the strict PHYS-SEED threshold at spatial size $2L$. This is the existing seed consumer in row 720. It avoids the two meanings of $\Phi_4$ discussed in §5. [Row 720, Theorem ZD-c](gap-phys-seed.md)

**PROVED (control inequality).** For every action with the positive transfer and cover bound, $P^0(W_\mu)\ge1-e^{-d}\ge e^{-n m}/(1+e^{-n m})$. In particular (1) fails if $n m$ stays bounded on a sequence of growing physical cubes and fine cutoffs. The permutation must act on the *whole* field in each sheet.

- **ARGUED — compact $U(1)$ and the free photon.** For the weak-coupling Coulomb comparison in brief §4, (1) would give the full periodic seed that the comparison excludes. The literature input for compact $U(1)$ is the large-$\beta$ Coulomb result of Guth and Fröhlich–Spencer in the respective models. Whenever $n m\le M$ along growing cubes, the explicit lower bound $1/(1+e^M)$ already contradicts (1). This is the box-level failure for a photon with energy of order the inverse side. No numerical photon threshold enters. [Council brief, §§3–4](gap-council-brief.md)
- **PROVED (product law), ARGUED (massless input).** $T=T_1\otimes T_2$ gives $d=d_1+d_2$ and the full first gap is at most the spectator's. A massless spectator with bounded $n m_2$ forces the same failure in (1), however small the first factor's winding cost. More generally a spectator excluded by the brief's seed theorem is excluded by its rectangular seed consequence. Acting only on the first factor would violate the double-cover identity itself.
- **PROVED (exactly frozen finite groups).** With flat plaquette constraints, the cylinder transports flat spatial connections up to gauge equivalence. In temporal gauge a flat time plaquette sets the next spatial link equal to its predecessor. Averaging the remaining temporal gauge gives the projection onto gauge-invariant functions of flat spatial connections, up to a common scalar. Each gauge orbit of commuting holonomy triples supplies one eigenvector with that same eigenvalue. For $Q_8$ and the binary tetrahedral group, $(1,1,1)$ and $(-1,1,1)$ are distinct such orbits. Thus $d\ge\log2$, and the bound in (1) would have to drive a probability at least $1/2$ to zero. **GUIDE.** At finite coupling in a proposed frozen phase, the corresponding input is a tunnelling splitting with bounded $n m$. The transition locations in the brief are numerical guides.
- **ARGUED — positive-character coexistence.** If the periodic transfer retains two states of comparable weight, $p_0$ is bounded away from one and the same obstruction applies. Section 4 gives the quantitative test for the van Enter–Shlosman family at coexistence.

**GUIDE — cheapest decisive test.** Before attempting a continuum estimate, take a single coordinate two-torus inside the four-torus. Test whether the erased faces on this plane can form the dual barrier necessary for *absence* of an odd active cycle. Independent local changes of gauge frame in one replica preserve its Wilson action and change a mixed plaquette. If that makes erased faces sufficiently rare as the bare $\beta$ increases, the proposed representation fails even on its intended trajectory. This can be tested by hand.

## 3. Attempt on the Wilson law

**PROVED — cover comparison.** Fix a finite rectangular torus with each side at least four. Give each positively oriented link $e$ two ordered Haar variables $U_e^0,U_e^1$. Write $w(g)=e^{-\beta A(g)}$, $A(g)=1-\tfrac12\operatorname{tr}g$. Around an oriented plaquette $p=(e_i^{\epsilon_i})_{i=1}^4$, for $s\in\mathbb F_2^4$ put

```math
 b_p^s=\prod_{h=0}^1 w\!\left(\prod_{i=1}^4
                 (U_{e_i}^{\,h+s_i})^{\epsilon_i}\right),\qquad
 b_p^*=\min_s b_p^s,\qquad f_p=b_p^*/b_p^0.
```

Addition in the sheet labels is modulo two. Under two independent Wilson draws, independently erase each face $p$ with conditional probability $f_p$, and call the others active. This is the law $P^0$ in (1).

**PROVED.** Choose one lift of each face and each link in the connected double cover in direction $\mu$. The bits $\tau_{pe}$ say which lift of $e$ the chosen lift of $p$ reads. On a closed walk of the face–link incidence graph their sum is its $\mu$-winding modulo two, by path lifting. In the trivial cover all bits are zero. The corresponding integrals are $Z_\tau=Z(B')$, $Z_0=Z(B)^2$. Expand the factors $b_p^s=b_p^*+(b_p^s-b_p^*)$ in either integral. The terms are nonnegative and indexed by the set $D$ of faces on which the second term was selected. In the trivial cover their normalized masses are exactly the probabilities of the active sets $D$.

**PROVED.** On a set $D$ without an odd cycle there are bits $u_e,v_p$ with $\tau_{pe}=u_e+v_p$ at every active incidence. Obtain them by summing $\tau$ along paths from one vertex per component. Swapping each pair of integration variables by $u_e$ preserves Haar and every $b_p^*$. On an active face the remaining $v_p$ only exchanges the two factors of $b_p^0$. Thus the integral for this $D$ is identical in the two covers. Keeping those terms in $Z_\tau$ gives

```math
             e^{-d(B)}=Z_\tau/Z_0\ \ge\ 1-P^0(W_\mu).                 \tag{2}
```

The argument allows a cycle of even nonzero winding. It is its parity that affects sheet relabelling.

**PROVED — counterexample to (1) on its stated trajectory.** There is a finite $\beta_*$ such that for every $\beta\ge\beta_*$, all even side lengths at least four, and any other coordinate $\nu$,

```math
 P^0(W_\mu^c)\ \le\ N_\mu N_\nu\sum_{r\ge N_\nu}2^{-r}.             \tag{3}
```

In particular if $N_\mu,N_\nu$ have bounded aspect ratio and tend to infinity while $\beta_j\to\infty$, then $P^0(W_\mu)\to1$. The estimate concerns the auxiliary erasure law.

**PROVED (planar erasures).** Work on the $\mu,\nu$ coordinate plane at transverse coordinates zero. For every set $S$ of distinct plaquettes in this plane,

```math
 P^0(S\text{ erased})=\mathbb E\prod_{p\in S}f_p\ \le\ q_\beta^{\,|S|},
                     \qquad q_\beta\longrightarrow0.                 \tag{4}
```

Here and below the expectation is for the two independent Wilson fields. The following is the site-reflection chessboard argument of Fröhlich, Israel, Lieb and Simon, with its dissemination step included. Use the unit four-cubes as blocks. On the block at zero place the test $f$ on its $\mu,\nu$ face at transverse coordinates zero. Extend this placement by reflections in the block faces. Even side lengths make this placement periodic. Reversing a plaquette preserves the real trace, and it permutes the assignments over which the minimum is taken. Thus on the chosen plane the reflected tests are exactly those in (4).

**PROVED.** Reflection in a pair of opposite site planes factorizes the two half-box integrals given the links in the planes. Every Wilson plaquette lies in one closed half or in their common boundary, and reflection preserves both its weight and the two Haar products. For a pattern of block tests, Cauchy–Schwarz on the boundary integral therefore bounds its squared expectation by the product of the expectations obtained by reflecting each half onto the other. Let $Q$ be the maximum, over all nonempty block patterns, of the expectation of their product to the reciprocal of the number of marked blocks. In a maximizing pattern, either reflected nonempty half still maximizes. Indeed the numbers of marks in the two reflected patterns sum to twice the original number, and the empty product is one. Start with a marked block. Reflect a half-box ending at a face of this block, then at the end of the filled interval, to double the length of a filled row. Once it contains a half-period, reflect a filled half to fill the period. Repeat in each coordinate, preserving the filled rectangle in the others. This produces a full maximizing pattern. With $V=\prod_i N_i$, it gives $Q=(\mathbb E\prod_{\text{all blocks}} f)^{1/V}$. Shared edges on block boundaries cause no problem because the reflection inequality conditions on boundary links.

**PROVED (bound on that full-pattern moment).** Reflection selects the $\mu,\nu$ plaquettes with both transverse coordinates even, each with multiplicity four. Put $t=\beta^{-1/2}$, $\beta\ge1$, and call an occurrence good if $A(U^0_p)+A(U^1_p)\le t$. If at least half the $V$ occurrences are bad, the two fields' total action is at least $Vt/8$. A single field's partition function obeys

```math
 Z(B)\ \ge\big(c_0\beta^{-3/2}\big)^{4V}e^{-48V},\qquad
 c_0=8/(3\pi^3).
```

Indeed restrict the four positive links per site to angle at most $\beta^{-1/2}$. The normalized $SU(2)$ radial Haar law is $(2/\pi)\sin^2\theta\,d\theta$, so the ball has at least the indicated mass by $\sin\theta\ge2\theta/\pi$ on $[0,1]$. The product angle is at most the sum of the four angles and $1-\cos x\le x^2/2$. There are $6V$ plaquettes. Since normalized product Haar has mass one, the contribution from the bad-majority event is at most $u_\beta^V$, where

```math
 u_\beta=c_0^{-8}e^{96}\,\beta^{12}e^{-\sqrt\beta/8}\longrightarrow0 .
```

**PROVED (relative gauge rotations).** In the other case there are at least $V/8$ distinct good selected faces. Partition them into four classes by the two in-plane coordinate parities of the lower corner. Faces in each class are vertex-disjoint. Take the largest class, with a deterministic tie rule, and retain only its factors in the product (all others are at most one). At least $V/32$ remain. This choice uses only plaquette actions, which are invariant under independent vertex gauge rotations in either replica.

**PROVED.** On one retained face choose one edge and rotate replica 1 by an independent Haar element at one of its endpoints. Test the candidate assignment in $b_p^*$ that exchanges this edge alone between replicas. The resulting plaquette in replica 0 has Haar holonomy conditional on the original fields, because it contains the fresh Haar variable once, between fixed matrices, possibly inverted. Let $h(x)=\mathrm{Haar}\{A(g)\le x\}$. Except on an event of probability $h(2t)$ its action exceeds $2t$. The other mixed plaquette has nonnegative action and the original sum is at most $t$. Whenever the mixed action exceeds $2t$, it follows that $f_p\le e^{-\beta t}$. Thus the rotation average of $f_p$ is at most $\eta_\beta=h(2t)+e^{-\beta t}\to0$, since Haar has no atom at the identity. The independent rotations on the retained disjoint faces give a product bound. Formally one may average over all site gauges first and condition on the rotations outside the chosen endpoints. The orbit-invariant choice of faces is then fixed and the unconditioned rotations remain independent. Gauge invariance of the Wilson law makes this averaging exact.

**PROVED.** The full-pattern moment is at most $u_\beta^V+\eta_\beta^{V/32}$ for all sufficiently large $\beta$ with $\eta_\beta<1$. Taking $V$-th roots proves (4) with $q_\beta=u_\beta+\eta_\beta^{1/32}$. No independence of actual Wilson plaquettes entered this estimate.

**PROVED (dual barrier).** Draw the square lattice of plaquette centres on the chosen two-torus. Call a bond open when both incident faces are active. An odd $\mu$-cycle of open bonds lifts to an odd cycle of the active incidence graph by inserting the shared link between consecutive faces. If such cycles are absent, the cochain recording crossings of a $\mu$-seam is a coboundary on the open graph. Extend its vertex potential arbitrarily to the other vertices. Adding the coboundary on the whole plane leaves a closed mod-two cochain, supported on closed bonds, whose sum along a $\mu$-row is one. Its crossed dual edges have even degree at every dual vertex, so decompose into simple circuits. An odd intersection with the row requires at least one circuit of odd $\nu$-winding, of length $r\ge N_\nu$. Each of its $r$ crossed bonds has an erased endpoint. There are at most $2^r$ endpoint choices, and each choice contains at least $r/4$ distinct erased faces because a vertex has four incident bonds. There are at most $N_\mu N_\nu 4^r$ possible directed circuits of length $r$. Equation (4) bounds the probability by the sum of $N_\mu N_\nu(8q_\beta^{1/4})^r$ for $r\ge N_\nu$. Choose $\beta_*$ so $8q_\beta^{1/4}\le1/2$ for every $\beta\ge\beta_*$. This proves (3) by hand.

**PROVED (where the attack fails).** At any fixed compatible $L$ the refinement limit on the left of (1) is one. Choose a dyadic $L$ with $Ce^{-cL}<1$. This contradicts (1), already for $k=0$. Equation (2) discards asymptotically all the trivial cover's mass. The connected cover also contains winding terms. **OPEN.** Cancellation between the two winding sums, or an exact expansion after integrating relative gauge frames that makes its own winding event rare, would require a new estimate. Equation (3) gives no estimate of the physical free-energy defect itself.

## 4. Registry comparison

**GUIDE — rank 1 reuses a tried method.** Rows 845/852 and 895/896 distinguish an average under the Gibbs law from a bound that survives conditioning. Rows 1118–1123, method 34, are closer still. Row 1118, §4.2, already takes the minimum of a paired cell weight over partial exchanges, marks the excess, and uses connected marked sets. Its consumer is covariance of separated observables. Row 1121, Proposition J, already uses a single unmatched Haar rotation to bound the mean cost of a junction. Row 1123 confirms the scoped bound and rejects its extrapolation to all ownerships. A lower bound on one mark's mean leaves open whether there is *any* winding cycle. Equations (2)–(4) compare the untwisted and sheet-permuted partition functions and resolve the winding question for bare plaquette marks at sufficiently large bare coupling. I found neither result in those rows. Row 1099, Proposition SW, and check 1100 record an O(4) swap representation and numerical spanning clusters. Its spin law and evidence differ from (3). The cluster rules are due to Kandel and Domany and Niedermayer, the two-replica method to Redner, Machta and Chayes, and the local-exchange covariance argument for finite gauge groups to Adhikari and Cao. [Row 1118, §§4.1–4.3](gap-conv-in-law-astra.md) · [Row 1121, §§8–9](gap-conv-in-law-check-opus.md) · [Row 1099, Proposition SW](gap-pinu-ev.md) · [Adhikari and Cao, §3](https://arxiv.org/abs/2202.10375)

**GUIDE — classification of the input.** This was a two-sample probability under the actual periodic law, with auxiliary independent marks given those samples. Its one-rectangle version is a K-one test for the periodic seed. Formula (1) asks for that type of estimate at multiple sizes without an induction from the stopped coupling. Rows 697/705 already give the directional trace inequalities. Rows 975, 982 and 988 (approach D) already identify the purity with the gluing cost and leave its upper bound open. The sign supplied by reflection positivity in row 988 is respected throughout. In (4) reflection bounds probabilities of erased faces. Row 859's chessboard recursion concerns half-integer spin labels and a flux decoder. Row 1031's thermal entropy drift concerns scale evolution. Neither identifies the sheet-cover event. The registry's routes RA/RC and methods 1–34 contain no supplier for the proposed winding rarity. [Row 705, Theorem D-shape](gap-seed-shape.md) · [Row 988, approach D](gap-unit-max.md) · [Row 859, §4c](gap-brainstorm-max.md) · [Route registry and test table](../parts/gap.md) · [FINISH results](../FINISH.md)

**PROVED (additional controls using the cited results as premises).** Row 884 gives a stronger frozen witness even after projection to the centre-even space. The centre orbits of flat triples $(1,1,1)$ and $(i,1,1)$ remain distinct in both groups since centrality of the first entry is invariant under conjugation and centre flips. For the positive-character test of Proposition V take $w_p(g)=\exp[\beta((1+\operatorname{tr}(g)/2)/2)^p]$, for every sufficiently large integer $p$ to which its stated van Enter–Shlosman input applies. At its coexistence coupling the proposition gives $S(a;(2a)^3)\ge1/5041$ for every $a\ge3$. By §1, $d\ge\log(1+S)$ on this last directional doubling, so (2) forces $P^0(W_\mu)\ge1/5042$. This excludes the fixed-coupling small-probability test there. The K7 endpoint has only guide standing in the registry. Theorem D2 (row 977) and Lemma SHEET (row 996) concern suprema over tilts and coupling fields. The minimum in §3 has only sixteen label assignments at *one fixed plaquette*, with the sampled Wilson fields held fixed. [Row 884, §7](gap-crux-exercise2-check-astra.md) · [Proposition V, §4.1](gap-crux-fp.md) · [Test table](../parts/gap.md)

**ARGUED (nearest same-model theorem).** Hao Shen, Rongchan Zhu and Xiangchan Zhu prove functional inequalities for the lattice Yang–Mills Gibbs measure and decay of spatial correlations under Assumption 1.1. Their certified curvature lower bound must be positive, requiring $|\beta|<1/[16(d-1)]$ for $SU(N)$ in *their* normalization. This is the precise point at which their proof ceases to give an estimate in the band. The two-dimensional OpenAI proof uses a pinned-cell Ward identity with a bracket term and a stiffness inequality uniform in its class of pins. Its variables are site spins with gradient couplings. The gauge rotations in §3 preserve every unmixed plaquette action, including on the overwhelmingly winding configurations. [Shen, Zhu and Zhu, Assumption 1.1 and Corollary 1.6](https://arxiv.org/abs/2204.12737) · [OpenAI, *Sharp mass bounds for the two-dimensional O(4) model*, §3](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Sharp-mass-bounds-for-the-two-dimensional-O4-model-September-23-2026/paper.pdf) · [Fröhlich, Israel, Lieb and Simon, reflection positivity and chessboard estimates](https://doi.org/10.1007/BF01940327)

## 5. Scope and remaining estimate

**PROVED (maximality of the erasure used here).** Suppose a bare-plaquette expansion uses a nonnegative common summand $c_p$ invariant under every exchange of the four link pairs, with $c_p\le b_p^s$ for every $s$, and erases independently given the two fields with probabilities $c_p/b_p^0$. Then $c_p\le b_p^*$. Couple the erasures by one common uniform variable per plaquette. Its active set contains ours, so (3) holds for that scheme as well. This specifies the class ruled out by the counterexample.

**PROVED (what a comparison retaining winding configurations must estimate).** Write $p_{\rm tr}$ and $p_{\rm tw}$ for the winding probabilities under the trivial and connected covers with the same expansion. At finite $\beta$ the empty active set has positive mass. The equal nonwinding sums in §3 give

```math
                 d(B)=\log\frac{1-p_{\rm tw}}{1-p_{\rm tr}} .
```

Equation (3) bounds the denominator $1-p_{\rm tr}$ from above. The numerator is the nonwinding probability under the other measure. **OPEN.** The ratio can still approach one. To turn this identity into an upper bound on $d$ requires control of the *relative* probabilities, for example $p_{\rm tr}-p_{\rm tw}\le\epsilon(1-p_{\rm tr})$ would give $d\le\log(1+\epsilon)$. No estimate of that relative difference was obtained. The proof of (3) gives an existence threshold at large bare coupling. Percolation for a particular numerical coupling in the Wilson window remains unverified here.

**PROVED (notation check affecting the consumer).** The brief calls the side-doubling expression $16F(n^4)-F((2n)^4)$ $\Phi_4(n)$. In row 720, Corollary Z1′ and Theorem ZD-c, $\Phi_4(n)$ instead means $256F(n^4)-F((4n)^4)$. If $D_2(n)$ denotes the former and $D_4(n)$ the latter, then $D_4(n)=16D_2(n)+D_2(2n)$. Row 720, Lemma Z3, already telescopes $D_2$ into four directional defects with weights $8,4,2,1$. Substitution of only the first four doublings into row 720's Z-SEED formula would miss the second scale. The one-rectangle implication in §2 goes directly through PHYS-SEED. [Council brief, §2](gap-council-brief.md) · [Row 720, Corollary Z1′, Lemma Z3 and Theorem ZD-c](gap-phys-seed.md)

**GUIDE.** Row 1131 is a Codex probability-council research note. Its proof is written for hand checking and has had no independent review or formalization. No numerical estimate enters the argument. The labels describe the arguments here and grant no scientific or audit status.

RESULT: PROVED in this note — independent-replica plaquette erasure gives the rectangular double-cover bound (2), but even its maximal common summand has odd winding with probability tending to one along the fine Wilson $SU(2)$ trajectory, by (3)–(4). OPEN — a selective bound on the relative winding weights or on the physical free-energy defect in the order-one band.
