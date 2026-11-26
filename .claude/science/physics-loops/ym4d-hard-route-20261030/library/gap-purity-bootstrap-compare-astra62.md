# Repo search

Unreviewed research text, FINISH row 1592 at `674445c45`. The target-specific prior is absent. The lead’s 8 November digest covered main and PRs 10114, 10133, 10134 and 10141. Its nearest soft-route result lower-bounds one loop correlation at one time step. A fresh search on those five refs also found OpenAI’s one-dimensional criterion ported in full on main for a periodic PXP chain and a staggered link ring. I checked the loop argument and the PXP criterion against source. [Lead digest](prior/repo-search-2026-11-08.md) · [PR 10114, one-step witness](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/f76f6c649cff7dffbab664d8976e680e8f287fe9/.claude/science/toe-ruleset-20261021/agents/ym4d-proof/MASS_GAP_LOCAL_BLOCK_ASTRA.md#L106-L149) · [Main, two-purity proof](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/8b11ae2bb95e641494fe75ed83d108ee712fa3a9/docs/PERIODIC_PXP_AND_STAGGERED_LINK_RING_UNIFORM_GAP_BOUNDED_THEOREM_NOTE_2026-10-07.md#L152-L220)

In this lane, row 1577 located the papers and the sector caveat. Row 1468 supplies Fact PUR and check 1527(ii) supplies the lower neutral thresholds. The neighboring registry entry TWO-PER (row 1520) treats transport in the coupling. The comparison below concerns period doubling at fixed coupling. [Row 1577](prior/gap-band-neutral-lit-luna.md) · [Open registry](open-registry.md)

Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, give the positive gauge-averaged periodic transfer in GL8. The outline index (chunk 02, 2315–2335), its neighboring rows and obligations, outline 588–599, and the CA-I 4.12–4.19 index led to the periodic trace and no neutral seed. CA-I 2705–2710 expressly leaves the mass gap open. [Outline, GL8](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L2313-L2335) · [Complete account I](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L2705-L2710)

**Entry plan.** Read the three primary theorems, rotate the Wilson sector projection, and compare the tests first on the same box and then over the admissible sides and cutoffs.

**Finding.** Grover allows a larger four-cube free-energy defect at a fixed volume. For the rotation-invariant Pfaffian trace, the four-purity input and PUR-io imply each other after a fixed change of volume. The missing estimate is still the Wilson seed.

## 1. What the primary results prove

**OpenAI, *The periodic spin-one Haldane gap* (September 24, 2026).** Write $b$ for Euclidean time, reserving the Wilson bare coupling for later. The abstract proposition assumes a nonscalar, finite-dimensional self-adjoint Hamiltonian for each even ring length $L\ge4$. Up to a fixed energy shift $aL$, the positive Gibbs trace at every $b>0$ must equal $\sum_i |\lambda_i(b)|^L$ for *all* such $L$, with the same real list at fixed $b$, multiplicities counted, and $\sum_i |\lambda_i(b)|^4<\infty$. OpenAI constructs a length-independent, self-adjoint Hilbert–Schmidt transfer with exactly these moments. Even powers allow negative spatial eigenvalues. A change in normalization of the common partition function by an extensive energy shift cancels from the ratios. [OpenAI, spatial transfer proposition](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-periodic-spin-one-Haldane-gap-September-24-2026/build/transfer.tex) · [Bootstrap proposition and proof](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-periodic-spin-one-Haldane-gap-September-24-2026/build/bootstrap.tex)

Set $S(L,b)=Z(2L,b)/Z(L,b)^2$ and $T(L,b)=Z(L,2b)/Z(L,b)^2$. The starting bounds are **staggered**, $S(L_0,b_0),T(2L_0,b_0)\ge1-e$, at one even $L_0\ge4$ and one $b_0>0$. With $G(e)=\tfrac12[(1-e)^{-1}+(1-e)^{-2}+(1-e)^{-3}]^2$, the sufficient conditions are $0<e<1/6$, $G(e)\le C$, $r=Ce<1$ and $C(1-3e)>3$. At the pair based at $(2^jL_0,2^jb_0)$ both defects are at most $r^{2^j}/C$. Interpolation of the common spatial moments fills every intermediate even length. Each even $L\ge L_0$ has a simple ground state and gap $>\log(1/r)/b_0$. [OpenAI, uniform-gap proposition](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-periodic-spin-one-Haldane-gap-September-24-2026/build/bootstrap.tex#L123-L158)

The periodic spin-one Heisenberg chain with unit coupling supplies two distinct initializations. $(L_0,b_0,e,C)=(60,105/4,1/8,79/10)$ gives $\gamma_L>(4/105)\log(80/79)$ for all even $L\ge60$. $(2304,784,1/100,5)$ gives $\gamma_L>\log(20)/784$ for all even $L\ge2304$. Twisted spin rings help isolate rotation sectors in the **initialization**. Both final purities use the full periodic spectrum. The thermodynamic statement includes the corresponding local-excitation bound in each subsequential limit of the periodic ground states. [OpenAI, finite seeds](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-periodic-spin-one-Haldane-gap-September-24-2026/build/initialization.tex) · [Theorem and thermodynamic corollary](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-periodic-spin-one-Haldane-gap-September-24-2026/build/assembly.tex)

**Tarun Grover, *Extensions of the Haldane gap proof* (arXiv:2611.07400), §§II–III.** Let $w$ be a finite or countable probability list. Write $P=\sum w_i^2$ and normalize $w_i^2$ by $P$. The new purity $P'$ satisfies

$$
1-P'=2\sum_{i<j}(w_iw_j)^2/P^2
\le (1-P)^2/(2P^2)=f(1-P).
$$

This proves squaring along the direction whose moments produced the weights. Across directions one uses the *same* $Z$. For example $S(L,2b)T(L,b)^2=S(L,b)^2T(2L,b)$. Using $T(L,b)\le1$ gives a lower bound on $S(L,2b)$. The sequence of these operations is what makes staggered seeds sufficient. Grover’s one-dimensional version takes both defects $\le1/100$ and updates their common bound to $5e^2$, giving gap $>\log 20/b_0$ on every even ring of length at least $L_0$. [Grover, §§II–III and Appendix A](https://arxiv.org/html/2611.07400v1#S2)

In $d$ spatial dimensions the hypothesis is a finite positive partition function with a physical Gibbs moment expansion and a convergent Hermitian-transfer moment expansion along **each** spatial direction, for all relevant even rectangular sides $\ge4$ and all positive inverse temperatures. Each list is independent of the length in its own direction at fixed transverse geometry. Define $D_i$ to double side $i$ and $R_i(x)=Z(D_ix)/Z(x)^2$. Beginning at $x=(L,\ldots,L,b)$, double each spatial direction in turn and then time. The $d+1$ input ratios are evaluated at the successive boxes. With $h=2^{d+1}-1$, defects $\le e\le1/(2h^2)$ improve to $h^2e^2$ after simultaneous doubling. In $d=2$ the published values are $1/98$ and $49$. The resulting gap exceeds $\log 2/b$ on every even spatial cube of side at least $L$. One stronger sufficient test is $Q=Z(2x)/Z(x)^{2^{d+1}}\ge1-1/(2h^2)$, because $Q$ is the product of the successive ratios to the powers $2^d,2^{d-1},\ldots,1$. Here $2x$ doubles every side. Conversely, the separate bounds give $Q\ge(1-e)^h$ at that box. [Grover, §III and Appendix A](https://arxiv.org/html/2611.07400v1#S3)

**Grover’s sector caveat (§IV).** In the classical ferromagnetic Ising ring, projecting one untwisted trace gives $(A^L+B^L)/2$ with $A=2\cosh(bJ)>B=2\sinh(bJ)>0$. The supposed spatial purity is $2(A^{2L}+B^{2L})/(A^L+B^L)^2>1$, by $(A^L-B^L)^2>0$. For Ising symmetry $U$, Grover uses $\mathcal Z_k=\sum_{\eta=\pm1}\operatorname{Tr}[(I+kU)e^{-bH^{(\eta)}}/2]$, summing the two spatial boundary conditions at fixed charge $k$. He assumes Hermitian blocks $A_0,A_1$ independent of $L$ at fixed $b$, with convergent moments at every even $L\ge4$ and $b>0$ giving $\mathcal Z_\pm=\operatorname{Tr}A_0^L\pm\operatorname{Tr}A_1^L$, and that the untwisted lowest energy is no higher than the twisted one in each charge. The plus sum is the spatial moment of $A_0\oplus A_1$. The minus sum is generally signed in that frame. Both time ratios remain ordinary purities of the two-boundary-condition Gibbs spectra in their respective charge sectors. Under the staggered $99/100$ plus-sector tests the combined plus spectrum is gapped. The comparison of the two charges and the lowest-energy ordering give a low pair in the original periodic spectrum, splitting $\le[12/(5b_0)]e^{-(\log20)L/(2L_0)}$ and gap above the pair $>\log 8/b_0$. For a general finite Abelian group Grover proves the sector extension in one spatial dimension with character phases and the analogous transfer and energy-ordering hypotheses. A four-dimensional one-form centre requires its own transfer identification. [Grover, §IV and Appendix B](https://arxiv.org/html/2611.07400v1#S4)

**Sirui Lu, *Bridging Gaps with Tensor Networks* (arXiv:2611.11049).** For an even periodic nearest-neighbor ring of finite-dimensional cells, Lu gives a checkable sufficient condition for the spatial estimates. In a real basis let $F=F^T=F^{-1}$, let the on-site term $o=o^T$ be real with $FoF=o$, and write the negative bond term as $-h=\sum_\alpha C_\alpha\otimes FC_\alpha F$ with each $C_\alpha$ real symmetric or antisymmetric. The two-cell Trotter transfer is a Gram matrix $\mathcal F^T\mathcal F$. Taking the Trotter limit at each fixed length and temperature passes the spatial moment inequalities to the Gibbs trace before any doubling. This is a sufficient bond-reflection-positivity condition for these rings. The finite starting bounds are a separate hypothesis. [Lu, main text and supplement](https://arxiv.org/pdf/2611.11049v1)

Lu allows unequal defects $p=1-S(L,b)$ and $q=1-T(2L,b)$. With $f$ above, choose rational bounds in $[0,1)$ and round $p'$ upward from $f(1-(1-p)^2(1-q))$, then $q'$ upward from $f(1-(1-q)^2(1-p'))$. For a target $r>1$ and a finite run through step $J$, the certificate requires $r^{2^j}z_j<1-z_j$ for $0\le j<J$, $z_j=1-(1-p_j)^2(1-q_j)$, and $p_J,q_J\le\varepsilon\le1/100$, $5\varepsilon r^{2^J}\le1$. It gives a gap $>\log r/b_0$ on all even lengths $\ge L_0$. At $(36,49/4)$ the spin-chain starting defect bounds are $47916/10^6$ and $181521/10^6$. These asymmetric inputs enter the $1/100$ defect regime after six rounds. Lu reports a sharpened spin-one bound $>0.0729$ for even $L\ge36$ using additional temperature lifting and interpolation. His Lean 4 formalization checks the general recurrence. Its mixed-field Ising example includes kernel-checked seeds. In the spin-one periodic example the $5$- through $12$-site short-ring trace totals remain external hypotheses of the integer-level Lean theorem. These spin calculations supply no Wilson input here. [Lu, primary manuscript and supplement](https://arxiv.org/pdf/2611.11049) · [Lu’s formalization](https://github.com/LionSR/CertifiedGaps)

## 2. The four-dimensional Wilson comparison

**Which partition function can be doubled?** Write $t$ for the integer number of time steps. All doublings below keep the bare Wilson coupling $\beta_K$ fixed. Let $Z_+=Z_{0,0}$ denote the untwisted magnetic sector with zero electric flux. On the gauge-invariant slice space $P_0=\tfrac18\sum_{z\in\mathbb F_2^3} C_z$ projects onto the centre-neutral states. It commutes with the Wilson transfer $T$. Thus $Z_+(t)=\operatorname{Tr}(P_0T^t)=\tfrac18\sum_z Z^{(z,0)}(t)$. On spatial side $n$ its time purity is $P_+(n,t)=Z_+(2t;n^3)/Z_+(t;n^3)^2$. In another direction the *same* number has the lane’s X16 representation. Holding the other periods fixed and using $a$ as old time and $b$ as new time, it is

$$
 Z_+(a;b,c,d)=\tfrac14\operatorname{Tr} A^b,\qquad
 A=\bigoplus_{(\chi,m)\in X} T_{m}|_{\chi}.
$$

Here the crossed transverse box is $(a,c,d)$, and $X$ consists of the sixteen sectors whose electric and magnetic components along the old time axis both vanish. Of the three old temporal twists, one remains electric and two become magnetic. Summing the remaining electric bit inserts twice its even projector, changing $1/8$ to $1/4$. Consequently the putative spatial purity is

$$
 \frac{Z_+(a;2b,c,d)}{Z_+(a;b,c,d)^2}
   =4\,\frac{\operatorname{Tr} A^{2b}}{(\operatorname{Tr} A^b)^2}.
$$

This identity bounds the spatial ratio by $4$. The published cancellation step requires an upper bound of $1$. Multiplying $Z_+$ by four would divide its **time** purity by four, capping it at $1/4$. At $a=b$ the fifteen additional crossed sectors already have total trace $3Z_{0,0}$ by the lane’s sum rule. The missing upper bound of one is a question about the crossed weights on the actual Wilson trajectory. [X16, sum rule and EVL, §8.5](gap-flux-exercise.md) · [Check of the sector count](gap-flux-exercise-check.md)

The lane already gives three rotation-invariant choices with the requisite counting measure on spectra. In the time frame write $Z_{\chi,m}$ for an electric character $\chi\in\mathbb F_2^3$ and magnetic twist $m\in\mathbb F_2^3$. Then

$$
 W_{\rm per}=\sum_\chi Z_{\chi,0},\qquad
 W_{\rm full}=\sum_m Z_{0,m},\qquad
 W_\kappa=\sum_m Z_{m,m}.
$$

The full choice is $\tfrac18\sum_k Z^k$ over all 64 twists, and the Pfaffian choice inserts $(-1)^{\mathrm{Pf}(k)}$ in that sum. Despite the signs in twist coordinates, each is an ordinary positive direct-sum trace in **every** frame. Each contains the periodic vacuum, and the other blocks have spectral radius at most its eigenvalue. An extra copy of the top is counted as excited until the seed excludes it. These facts use the twisted Wilson transfer construction and Fourier projection on file. [Sector classification, Lemma W and Theorem S-w](gap-flux-exercise.md) · [Twisted kernel and classification check](gap-flux-exercise-check.md)

**Grover’s update for these three choices.** Use $x=(L,L,L,t)$ with even $L,t\ge4$ and one of the $W$ above throughout. Write $R_1,R_2,R_3,R_4$ for the $x$-, $y$-, $z$- and time-purity on, respectively,

$$
 (L,L,L,t),\quad (2L,L,L,t),\quad (2L,2L,L,t),\quad (2L,2L,2L,t).
$$

There are four tests. The successive rectangular geometries differ even when the initial cube is isotropic. A two-direction calculation with two spectator widths held fixed would only control that fixed cross-section. The published $d=3$ constant gives the conditional Wilson test

$$
 \min_i R_i\ge449/450
 \quad\Longrightarrow\quad
 e_{j+1}=225e_j^2,\quad e_j\le 2^{-2^j}/225,
 \qquad \Delta_{W,B}>\log 2/t\quad(B\ge L\text{ even}),
$$

where $e_j$ bounds all four defects at the $j$th dilation. The top eigenvalue is simple and the gap is in lattice units on the cube of spatial side $B$. The alternative input $Q=W(2x)/W(x)^{16}=R_1^8R_2^4R_3^2R_4\ge449/450$ suffices. The exponent $16$ comes from four doubled lengths. [Grover, general dimensions](https://arxiv.org/html/2611.07400v1#S3)

For the port to discrete Wilson time, the weights in each frame are the normalized, summable eigenvalue powers of its compact transfer. Thus $0<R_i\le1$ and the defect after normalized squaring obeys $f$. For the first direction, move its doubling to the end of the four doublings. The product $Q$ is unchanged, and the other three factors in that order are at most one. Its last ratio is therefore at least $Q\ge(1-e)^{15}\ge1-15e$. Doubling that last direction once more gives its next-scale ratio with defect at most $f(15e)\le225e^2$ for $e\le1/450$ since $(1-15e)^2\ge(29/30)^2>1/2$. Cycle the starting box forward by one direction. Its three old remaining ratios and the newly improved one bound its product by the same argument, because $225e^2\le e$. Four cycles give the update for every direction.

For $L_j=2^jL\le B\le2L_j$ apply $\sum x_i^q\le(\sum x_i^p)^{q/p}$, $q\ge p>0$, in each spatial direction at times $t_j=2^jt$ and $2t_j$. The thermal purity is at least $Q_j^{(B/(2L_j))^3}\ge(1-e_j)^{15}\ge1-15e_j$. The largest normalized thermal weight is at least this purity. The ratio of any other weight to the largest is at most $15e_j/(1-15e_j)<2^{-2^j}$. Taking logarithms proves the claimed gap for all the intermediate even cubes as well. Summability of the counting spectra justifies the same argument on the infinite-dimensional Wilson slice spaces.

### What changes in Theorem S

For a true counting trace $W$, write $s_W(t;B)$ for the sum of all excited eigenvalue ratios to power $t$ in spatial box $B$, removing one periodic vacuum. Write $s(N)=s_W(N;(2N)^3)$. Theorem S enlarges the three spatial sides and then squares in time, giving

$$
s(2N)\le\big((1+s(N))^{64}-1\big)^2\le5041s(N)^2
\quad\text{if }s(N)\le1/640.
$$

Thus $s(N)<1/5041$ gives $s(2^jN)\le(5041s(N))^{2^j}/5041$ and gap at least $\log(1/(5041s(N)))/N$ for positive seed. Its corollary covers every integer side $\ge2N$. The Lean theorem `GapChain.Wilson.Assembly.wilson_theoremS` instantiates **periodic** Wilson torus data at $\beta>0$, $N\ge3$. The checked source receipt lists the Lean kernel with `propext`, `Classical.choice`, and `Quot.sound`. The twist-completed versions use the lane’s written Theorem S-w. The comparison here is by hand. I read the Lean declarations and receipt without rerunning Lean. The coefficient $225$ acts on a bound for four purity defects. The coefficient $5041=71^2$ acts on one excited sum. [Lean statement](../lean/gapchain/GapChain/Assembly.lean) · [Recursion and all-side corollary](../lean/gapchain/GapChain/TheoremS.lean) · [Build receipt](../lean/gapchain/RECEIPT-1f.md) · [Theorem S-w](gap-flux-exercise.md)

**Comparison on the same observable.** At $x=(N,N,N,N)$ Grover’s $Q$ is exactly $\exp[-\Phi_W(N)]$, where $\Phi_W(N)=16\log W(N^4)-\log W((2N)^4)$ is already on file. The printed S-w sufficient bound is $\Phi_W\le19/100000$. The shape improvement accepts $s(N)\le1/1650$. Since $1+s(N)\le e^{\Phi_W}$, imposing $\Phi_W\le\log(1+1/1650)$ suffices for that test. Grover admits $\Phi_W\le\log(450/449)=\log(1+1/449)$ on that very cube. This is a looser numerical bound on a specified observable. It is a different observable from the neutral time purity. [Lane’s symmetric defect](gap-crux-restate.md) · [Shape improvement, §§1.5 and 2](gap-seed-shape.md) · [Three sector completions, §8.4](gap-flux-exercise.md)

The two numerical criteria really can differ at a fixed cube in the class of positive counting transfers. Take $W(x)=1+q^{V(x)}$, where $V$ is four-volume and $0<q<1$. In direction $i$ the two eigenvalues are $1,q^{V(x)/x_i}$. Choose $q^{N^4}=y=1/16000$. Then $Q=(1+y^{16})/(1+y)^{16}$. Convexity gives $Q\ge(1+y)^{-16}\ge1-16y=999/1000>449/450$. The binomial lower bound on the denominator gives $Q\le(1+y)/(1+16y)=16001/16016<1650/1651$. This separates Grover’s $Q$ gate from both printed sufficient bounds on $\Phi_W$. It is a moment model for comparing the tests.

**Equivalence when the seed cube can be enlarged.** For any of the three $W$ above, the symmetric four-ratio criterion and the S-w thermal seed imply each other after a bounded change of side. The argument gives the constants and preserves uniformity across cutoffs.

* From the four ratios at $(N,N,N,N)$, three rounds give $e_3\le 1/(225\cdot2^8)=1/57600$. At time $8N$ on $(16N)^3$, the largest weight is at least the time purity, hence $s(8N)\le e_3/(1-e_3)\le1/57599<1/5041$. This direction also applies from $Q\ge449/450$.
* Conversely suppose $s=s(N)<1/5041$, with $N\ge3$. The comparison starts Grover at the even scale $2N$. At the four tests based at $(2N)^4$, view the direction about to be doubled as time. Every transverse side is either $2N$ or $4N$. At time $N$, Proposition B3 with $p=q=1$ bounds $1+s_W(N;B)$ by $(1+s)^{64}$ on each such box (volume multiplier at most $8$, remaining multiplier $2^3$). At time $2N$ its excess is at most $[(1+s)^{64}-1]^2\le(71s)^2<1/5041$. A spectrum of excess $v$ has purity at least $(1+v)^{-2}\ge1-2v$. Thus all four defects are below $2/5041<1/1800$. One further Grover round bounds them by $225/1800^2=1/14400$, so their weighted product there is $\ge1-15/14400>449/450$. This proves the converse even for the single-$Q$ test. [Rectangular enlargement B3](gap-seed-shape.md) · [Theorem S polynomial estimate](../lean/gapchain/GapChain/TheoremS.lean)

For $W_{\rm per}$ the product test needs just two untwisted torus integrals, but it controls every electric-flux sector. For $W_\kappa$ each torus value combines all 64 twists. Over the allowed choice of side the two implications give the same thermal seed for the chosen $W$.

### Comparison with the calibrated neutral seed

**At the identical box and time.** Fix the odd release block factor $b_*$, one calibration level $g_0$ and one $\ell\in1024\mathbb N_{>0}$. At each passing original least-root cutoff $K$, let $n=\ell b_*^K$ and $u=n/512$. PUR-io requires $P_+(n,u)\ge457/625$ at infinitely many such $K$. Take $2L=n$, $t=u$ in Grover’s test for a genuine $W$. Its **time ratio alone** gives $w_0\ge449/450$, hence $s_+(u;n^3)\le s_W(u;n^3)\le1/449$ and

$$
 P_+(n,u)\ge(1+s_+(u;n^3))^{-2}\ge(449/450)^2>457/625.
$$

Here the periodic vacuum belongs to both counting traces. At a single spectrum the reverse numerical implication fails already for neutral relative weights $(1,4/21)$, which have purity exactly $457/625$. Thus the high true-trace condition demands more at the matched input, before bounding any of the three spatial ratios. The separation is between spectral hypotheses. Realization of this spectrum on the calibrated Wilson trajectory is a separate question. [Fact PUR, row 1468, §3.1](gap-k2-tool-design-fable.md)

**Changing the aspect.** Grover’s fixed-coupling theorem allows independent $L,t$. For a continuum handoff the starting physical dimensions and the scale of the resulting bound matter. Here is an explicit transfer between fixed positive aspects. Suppose on an infinite set of original cutoffs the four tests hold for one $W$, with $L_K/b_*^K$ and $t_K/b_*^K$ in a fixed compact subinterval of $(0,\infty)$. Define $x_j=2^j(L_K,L_K,L_K,t_K)$ and let $V(x)$ be the product of the four periods. For even boxes $x_j\le y\le D_i y\le 2^h x_j$ coordinatewise, the moment inequality in each direction bounds

$$
 R_i(y)\ \ge \left[\frac{W(2^h x_j)}{W(x_j)^{16^h}}\right]^{2V(y)/V(2^h x_j)}
 \ \ge\ (1-e_j)^{16^h-1}.
$$

Indeed $W(y)\le W(x_j)^{V(y)/V(x_j)}$ and interpolation downward from $2^h x_j$ bounds $W(D_i y)$ from below. The bracket telescopes as $\prod_{k=0}^{h-1}Q(x_{j+k})^{16^{h-1-k}}$. Each factor $Q$ is at least $(1-e_j)^{15}$, and the outer exponent is at most one.

Choose an integer $c\in1024\mathbb N$ large enough that $y=(n',n',n',n'/512)$, $n'=2^j c b_*^K$, dominates $x_j$. The positive lower bounds on $L_K/b_*^K,t_K/b_*^K$ give one finite $h$ with $D_t y\le2^h x_j$ for all passing $K,j$. Now choose one $j$ making the displayed lower bound $\ge449/450$. The common-vacuum bound $P_+(n',n'/512)\ge R_t(y)^2$ gives **literal PUR-io** at fixed side $\ell'=2^j c$, on the same cutoffs and at their original coupling. The argument also transfers a finite set of directional tests by increasing $h$. Thus an all-direction seed can be posed at another fixed aspect, at the price of supplying the completed-sector purities there. One success at one lattice spacing, or increasing the time without control of its physical size, gives no such uniform conclusion.

**Which completion is equivalent?** The lane supplies the Wilson-specific reverse direction. Fact PUR gives $s_+(u;n^3)\le4/21$. Row 1161, lines 215–227, requires only $s_+\le1/2$, $3\le u\le n/512$, $4\mid n$, and $n\ge2^{70}$, the last condition automatic eventually. At $(n/2;n^3)$ it gives $s_\kappa<2^{-18}$ in both alternatives, and either $s_{\rm per}<2^{-19}$ or $s_{\rm full}<2^{-18}$. Each is below the S-w threshold. The preceding comparison therefore gives the Pfaffian four-purity test on a fixed enlargement at **every** passing sufficiently large $K$. One of the two other completions also passes on an infinite subset, by the finite pigeonhole principle. Conversely, each completion gives PUR-io by the preceding transfer. Over the allowed sides and infinitely many depths, **the Pfaffian test is equivalent to PUR-io, as is the disjunction of periodic and full tests**. Requiring a specified one of the latter two selects a flux alternative. The published bootstrap supplies no Wilson estimate selecting it. [Explicit one-cube alternative and its converse](gap-solve9-astra62.md) · [Check, Step 2](gap-solve9-check-opus.md) · [Calibrated handoff](sa-ym4-lean-faithful-astra62.md)

The extra flux requirement can be seen exactly in the lane’s frozen $\mathbb Z_2$ gauge example. At four-volume $V$ the flat untwisted partition function is $8\,2^{-3V}$, and any nonzero twist has zero flat mass because its plaquette cocycle is not a coboundary. The neutral mass is $2^{-3V}$. Thus every periodic directional purity is $1/8$ while the neutral time purity is one. Conversely at zero Wilson coupling the Haar weights give $Z^k=1$ for every twist, so $W_{\rm full}=8$ and its purities are $1/8$, again with neutral purity one. These are structural counterexamples to a reverse implication for either *specified* completion. At any finite list of boxes the strict separation persists at finite positive couplings by continuity, using the finite-group flat limit in the first example. At each depth one may cover all integer boxes of side at most $K b_*^K$ before choosing the comparison coupling. This preserves the separation at every fixed physical size on such comparison sequences. Selection of a branch on the prescribed SU(2) trajectory remains open. [Existing flat-sector count, equation (29)](gap-solve10-astra62.md) · [Scope of the frozen example](gap-wall-assumptions-opus.md)

**Lower neutral thresholds already on file.** For neutral excited weights $x_i$ at the tested time, put $s=\sum_i x_i$. Then $P=(1+\sum_i x_i^2)/(1+s)^2$ and $\sum_i x_i^2\le\min(s,s^2)$. If $P\ge1/2+\varepsilon$ for a fixed $0<\varepsilon<1/2$, the first bound gives $s<1$, and the second gives

$$
 s\le\frac{1-\sqrt{2\varepsilon}}{1+\sqrt{2\varepsilon}}.
$$

A single excited weight attains equality. Thus $457/625$ gives $4/21$, and $5/9$ gives $1/2$. In particular, **$5/9$ already suffices at the original $u=n/512$** by the $s\le1/2$ hypothesis of row 1161. At equality $P=1/2$, a double top shows why this spectral argument needs a positive margin for a simple vacuum. Nearly equal top weights can also approach that endpoint along a sequence of simple-top operators. [Fact PUR](gap-k2-tool-design-fable.md) · [One-cube theorem](gap-solve9-astra62.md) · [Check 1527(ii)](gap-agy-seed-approaches-neon-check-astra62.md)

Check 1527(ii) also permits the **longer** times $n/34$ for $457/625$ and $n/60$ for $5/9$. For general $1/2+\varepsilon$ it gives the even aspect $A=2\lceil\log(10^6)/\log(1+\sqrt{2\varepsilon})\rceil$, $u=n/A$, with $\ell\in4A\mathbb N$ and one infinite set of passing original cutoffs. Its corrected proof obtains a Pfaffian bound in both flux alternatives, propagates it and recovers the shorter-time neutral **excited-sum** test on an enlarged fixed box. Purity increases with time on a fixed positive spectrum, so a lower bound at the longer time cannot simply be moved to the earlier time. Likewise $s\le4/21$ alone does not invert Fact PUR. For example relative excited weights $(2/21,2/21)$ give $P=449/625$. The existing handoff selects the defining subsequence inside the passing set. For an original PUR-io witness of side $\ell$, its conclusion is an existential calibrated limit in the reconstructed action-density sector with a simple vacuum and $m_{\rm phys}\ge (2/\ell)\log(2^{18}/5041)$. A recovery on another physical side uses that side in the rate. [Corrected thresholds and handoff, 1527(ii)](gap-agy-seed-approaches-neon-check-astra62.md) · [Cutoff choice, row 1461](gap-crux-direction-astra62.md)

## 3. Where the method already occurs

Searching `library/` and `FINISH.md` at the pin, excluding this output, found Grover and the rotated-purity method in the row 1577 literature note and in the queue text (1577, 1592). The two other Haldane hits concern the two-dimensional $O(3)$ model or a list of spin manuscripts. The many doubling hits include the actual shape and spectral results above. Main already has the explicit one-dimensional PXP/link-ring port. In this lane the four-cube free-energy ratio, the loss under crossing of $Z_+$, and the three completed transfers all predate this comparison. I found no earlier lane derivation of Grover’s staggered four-ratio update with $225$ or its $449/450$ Wilson test. [Row 1577 survey](prior/gap-band-neutral-lit-luna.md) · [Theorem S](gap-crux-restate.md) · [Shape estimates](gap-seed-shape.md) · [Sector completions](gap-flux-exercise.md)

The remaining input is a purity bound for the actual Wilson measures on one common physical side at infinitely many least-root cutoffs. The spin-chain initializations bound specific short-ring moments and trial energies. None supplies that Wilson estimate. The same counting argument applies to untwisted compact U(1) in four dimensions and to SU(2) in five dimensions (there $h=31$). A model-selective estimate must enter in the finite-volume input.

RESULT — Grover relaxes the sufficient bound on the existing completed four-cube defect to $\Phi_W\le\log(450/449)$. The Pfaffian version is equivalent to PUR-io over the allowed sides and cutoffs. The neutral trace alone loses the spatial purity under rotation. The Wilson seed remains open.
