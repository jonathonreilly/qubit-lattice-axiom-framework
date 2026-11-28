## Repo search

<!-- Work plan
1. Record the pinned sources, the lead's search and the scope of neighbouring work.
2. State the continuum and lattice targets, choose an opening and give its proof tree.
3. Attack the first open leaf from the underlying definitions.
4. Check the tree against the indexed account, the route registry and the cited results. Revisit the attack if a prior obstruction applies.
5. Verify the argument and its limits, classify the leaves and record the result.
-->

**GUIDE.** Row 1141, written by Codex for the requested gpt-6.2-astra/max lane on checkout `8872d4c16`. The target-specific prior file is absent. The lead's 8 November digest covers the UV admission, covariance and witness problems. Its closest hits are the PI-class small-field frame (PR 10141 at the digest's `c73ad7b177`, `research/ym4d/library/out-gw.md`, 54–64), the small-curvature soft Hessian (PR 10114, `RTARGET.md`, 716–725), and the one-time-step Wilson-loop witness (same PR, `MASS_GAP_LOCAL_BLOCK_ASTRA.md`, 106–149). I checked those passages. The first two concern selected backgrounds. The third proves a one-step transfer correlation. None estimates how well a colour direction can follow a typical Wilson connection around two plaquettes.

**GUIDE.** I also searched outside this lane on main at `8b11ae2bb9` and PRs 10114, 10133, 10134 and 10141 for pinned-cell stiffness, field-dependent colour frames, covariantly constant directions, holonomy/frame-defect comparisons, random covariant Laplacians and Lifshitz tails. The only match to that search was the same archive blob on all five refs, about low modes on a diluted graph (`POSITIVE_PATH.md`, 14007–14017). The open registry has no matching frame or pinned-cell row. The council identifies the field-dependent step of row 1018 as open. The closest lane results, located in the Phase 2 comparison, are row 1018’s conditional mean bound and row 1051’s two-chord example with a fixed root colour. The microscopic transport question below strengthens both tests.

**GUIDE.** The source revision for Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, is `31a47c543775`. The outline index points to their scalar Theorem 0 at lines 66–131, to the small-chart estimate for adjoint transport at 12787–12803, to the Wilson measure at 238–269, and to the conditional first-passage statement RF24–25 at 20781–20801. In CA-I 2698–2710 the authors explicitly exclude “a mass gap” from the assertion. CA-I 49495–49513 assigns admission of the UV background to the application of Balaban's operator theorem. These are the UV inputs and limits relevant here.

## Phase 1. Target and proof tree

**OPEN — target.** Jaffe and Witten ask, here for SU(2), for a nontrivial quantum Yang–Mills theory on $\mathbb R^4$ whose gauge-invariant Euclidean correlations satisfy the Osterwalder–Schrader axioms strongly enough to reconstruct a Wightman theory. Its Hamiltonian must satisfy $\operatorname{spec}H\subset\{0\}\cup[\Delta,\infty)$, $\Delta>0$, above its vacuum. The lattice proposal uses periodic four-tori, Haar link measure and density proportional to $\exp\{b\sum_p\frac12\operatorname{tr}U_p\}$. Fine spacings $a_j\downarrow0$ follow an asymptotically free bare trajectory $b=\beta_j$. A seed must hold on boxes approximating **one fixed physical size** along that trajectory. Balaban's renormalization group, through the account of Sussman and Alpoge, supplies the UV framework up to first passage. The ensuing band has order-one effective coupling. Applying a bare Wilson estimate to blocked links requires a comparison of their laws.

**PROVED in the lane, as recorded by the council — seed consumer.** Write $F(n)=\log Z(n^4)$, $\Phi_\rho(n)=\rho^4F(n)-F(\rho n)$. The seed uses $\Phi_4(n)=16\Phi_2(n)+\Phi_2(2n)$. It requires the lowest nonvacuum energy of the periodic spatial cube, including zero electric flux. Choose $\ell_1$ with $\ell_1/(4a_j)$ an integer at least three for all large $j$. At one fixed physical size $L\in\{2^r\ell_1:r=0,1,\ldots\}$, the inequality is $z^-(L)>2\psi^+(L)+30$. Here $n_j=L/a_j$, $z^-(L)=\liminf_j n_jm_j(n_j^3)$ and $\psi^+(L)=\limsup_j\Phi_{4,j}(n_j/4)$. Equivalently the lane seeks bounded excess free energy and unbounded dimensionless lowest gap along dyadic sizes (row 720, with its cutoff limits). A selective estimate must bridge every necessary scale from first passage to that seed.

**ARGUED — choice (b).** A frame that follows microscopic parallel transport has a measurable defect even if its construction reads the entire field. Its best possible defect can therefore be tested in the actual, untilted Wilson law. Both the layer-mixing route and the slab sign route require information about an interacting conditional law over arbitrarily many sites. Two loops on eight links suffice to test the local premise of the frame route. The proposed mechanism is of the lane’s K-flow kind if carried out on blocked variables through the band. Its bare tests here concern one Wilson sample. For one- and two-sample mixing criteria the relevant prior work is rows 845, 852, 895–896 and 1118–1123 (lead rule CL).

| Node | Statement needed for this implementation | Initial standing |
|---|---|---|
| UV | The trajectory and the first-passage data used to start the band. | GUIDE, supplied as UV framework by the account with its stated conditions. |
| P | On a Wilson cell, a field-dependent colour mode can have ordinary diffusive cost when transported on microscopic bonds. In particular its covariant energy divided by its squared norm can be $O(R^{-2})$ on a typical cell of lattice side $R$. | OPEN, first leaf attacked below. |
| H | For a rotation with scalar profile $\eta$ and field-built axis, the defect paid in the signed response is smaller than the bracket gain. The version tested pays the positive covariant Dirichlet defect and budgets at most $K\sum\lvert\nabla\eta\rvert^2$ for a smooth profile, with $K$ independent of $R$. | OPEN. Identifying the full response requires the separate signed test below. |
| M | Retain cancellations between distinct supports before any upper bound, and turn the resulting **signed** pinned response into mixing of every observable in the slab, including centre-neutral ones. | OPEN. |
| S | Carry the quantitative mixing/free-energy estimates across the band to the periodic seed, then use its consumer. | OPEN up to the seed, PROVED in the lane thereafter. |

**ARGUED — why P is necessary for this version of H.** Put $s_x=\eta_x n_x(U)$, $|n_x|=1$, and write $T_{xy}=\operatorname{Ad}U_{xy}$ for transport from $y$ to $x$. For any real $\eta\ge0$ one has the exact identity

$$
 \mathcal E_U(s):=\sum_{xy}|s_x-T_{xy}s_y|^2
 =\sum_{xy}(\eta_x-\eta_y)^2+
    \sum_{xy}\eta_x\eta_y|n_x-T_{xy}n_y|^2.                 \tag{1}
$$

Throughout the note an unoriented bond occurs once. If the second sum can be paid by $K\sum|\nabla\eta|^2$, a bump of height one with a bulk plateau and slopes $O(R^{-1})$ gives P. We test even the weaker P which permits arbitrary vectors $s(U)$, variable length, exceptional sites and arbitrary dependence on the exterior. A signed covariance or an effective connection requires its own defect estimate.

## Phase 1. A typical-field obstruction to P

**PROVED here — theorem.** Take a coordinate $d$-cube $\Lambda_R$ of $R^d$ sites, $2\le d\le4$, in an ordinary four-dimensional periodic Wilson SU(2) lattice of coupling $b\ge0$. Use only the bonds internal to the cube, with Neumann (free) faces. Take all torus periods at least three and embed the cube without identifying distinct sites. For each $k>0$ there are $c_{d,k}>0$ and $R_0(d,k)$ such that, with Wilson probability at least $1-(2+R)^{-k}$, simultaneously for **all** $s:\Lambda_R\to\mathfrak{su}(2)$,

$$
  \mathcal E_U(s)\ \ge\
  \frac{c_{d,k}}{1+b+(\log(2+R))^{2/d}}\sum_{x\in\Lambda_R}|s_x|^2,
  \qquad R\ge R_0(d,k).                                      \tag{2}
$$

The quantifier over $s$ comes after sampling $U$. Every choice of frame, pins, amplitudes or exceptional sites made from that sample is included in (2) if the chosen vector is measured by (1). The proof uses conditional probabilities under the interacting Wilson measure.

**PROVED — one-link estimate.** Identify SU(2) with the unit quaternions $q=q_0+u$, $u\in\mathbb R^3$, and $\mathfrak{su}(2)$ with the imaginary quaternions. Condition on all bonds except one. The six incident normalized plaquette traces are linear forms in its four real coordinates, each with coefficient vector of norm one, including when the link occurs inversely. The conditional law is $e^{h\cdot q}\,dq/Z_\kappa$, $\kappa=|h|\le6b$, with normalized Haar $dq$. The same description holds for a plaquette holonomy when its other three links are fixed, since translations and inversion are orthogonal maps of $S^3$.

Fix a unit $n\in\mathbb R^3$. The map $q\mapsto\operatorname{Ad}q\,n$ sends Haar to uniform area on $S^2$ by rotational invariance. The conditional Haar law on a fibre is uniform on the circle $q\exp(tn)$ by invariance under the stabilizer. The average of $e^{h\cdot q}$ on any such circle is $I_0(v)\le I_0(\kappa)$, where $I_0(v)=\int_0^{2\pi}e^{v\cos t}\,dt/(2\pi)$ and $v$ is the length of the projection of $h$ onto that circle's plane. Monotonicity for $v\ge0$ follows by expanding the integral in even powers. To normalize, write $S^3$ as $(r e^{i\theta},\sqrt{1-r^2}e^{i\varphi})$ and put $h$ along the first real coordinate. The normalized volume element has radial part $2r\,dr$ (the three coordinate lengths are $1/\sqrt{1-r^2},r,\sqrt{1-r^2}$). Thus

$$
 Z_\kappa=\int_0^1 2r I_0(\kappa r)\,dr\ \ge\
 \frac{e^{-1/2}}{2(1+\kappa)} I_0(\kappa).
$$

Indeed integrate over $1-[2(1+\kappa)]^{-1}\le r\le1$, where $2r\ge1$ and $I_0(\kappa r)\ge e^{-1/2} I_0(\kappa)$. The tilted pushforward therefore has density at most $M_b=4(1+6b)$ relative to uniform area. The cap of chord radius $2t$ at $n$ has area fraction $t^2$ for $0\le t\le1$. Quaternion multiplication gives $|n-\operatorname{Ad}q\,n|^2=4|u\times n|^2$. Consequently

$$
 {\mathbb P}\{|u\times n|\le t\mid\hbox{other links}\}\ \le\ M_b t^2.       \tag{3}
$$

The conditioning in (3) is on links of the original action at its given coupling.

**PROVED — two plaquettes pin every axis.** At the central site $x$ of a $3^d$ cell take the north-east and south-west elementary plaquettes in the first coordinate plane, based at $x$. Their eight bonds are distinct. Let $h_i=a_i+u_i$ be their holonomies and $A_i=\operatorname{Ad}h_i$. Set $D=\min_{|v|=1}\sum_{i=1}^2 |v-A_i v|^2$. Then

$$
 {\mathbb P}\{D\ge \delta_b\mid\hbox{outside the cell}\}\ \ge\ \tfrac12,
 \qquad \delta_b=\frac{1}{8(1+6b)}.                           \tag{4}
$$

In fact $D/4$ is the smaller eigenvalue of the two-by-two Gram matrix of $u_1,u_2$, since $\sum |u_i\times v|^2=(\sum |u_i|^2)|v|^2-\sum (u_i\cdot v)^2$ and the two nonzero eigenvalues of the three-dimensional outer-product sum agree with the Gram eigenvalues when its rank is two. The rank-zero and rank-one cases give zero on both sides. On $|u_1|\ge|u_2|$, the smaller eigenvalue is at least the determinant divided by the trace, hence at least $|u_2\times\widehat u_1|^2/2$. If $D<\delta_b$, either this last cross product has square less than $\delta_b/2$, or the same holds with indices reversed. In the first case expose all links except one belonging only to the second loop. With the first axis fixed, (3) bounds the probability of the small cross product by $M_b\delta_b/2$. Reverse the roles for the other case. Vanishing imaginary parts have conditional probability zero. The union bound gives $M_b\delta_b=1/2$, also after conditioning on fewer outside links. The minimum in (4) permits the axis to be chosen *after* observing both holonomies.

**PROVED — cancellation and energy.** For the three transports with supports the empty path and the two distinct plaquette boundaries, put $K=(I+A_1+A_2)/3$. Combining them at their common endpoint gives the identity

$$
 |v|^2-|Kv|^2=\tfrac19\bigl(|v-A_1v|^2+|v-A_2v|^2+|(A_1-A_2)v|^2\bigr).   \tag{5}
$$

This identity retains the cross terms between different geometric supports. Estimating the three transports by their norms first would give no strict loss. On a cell satisfying (4)'s event the left side is at least $\delta_b|v|^2/9$. With $v=s_x$, the three squared differences on the right sum to at most three times the sum of the first two. Around each square, $s_x-A_i s_x$ is the telescoping sum of its four transported bond differences. Cauchy–Schwarz therefore gives

$$
 |s_x|^2\ \le\ (12/\delta_b)\sum_{e\ {\rm on\ the\ two\ squares}}
                   |s_{e^-}-T_e s_{e^+}|^2.                   \tag{6}
$$

Equation (5) concerns the colour transports themselves. The signed cancellations needed for the Wilson free-energy consumer at M are a separate obligation.

**PROVED — density of pinned sites.** In a rectangle $B$ of side lengths in $[m,2m]$, $m\ge6$, use disjoint cells of side three. Their number $N\ge |B|/6^d$ by taking integer parts in each coordinate. Write $G_i$ for the indicator in (4). It has conditional mean at least $1/2$ given the previous indicators, all supported outside its cell. Iteration gives ${\mathbb E}3^{-\sum_iG_i}\le(2/3)^N$. By Markov's inequality,

$$
 {\mathbb P}\{\textstyle\sum_iG_i<N/4\}\le e^{-\gamma N},
 \qquad \gamma=\tfrac14\log(27/16)>0.                         \tag{7}
$$

Let $m=\lceil(A\log(2+R))^{1/d}\rceil$, $A=6^d(k+d+1)/\gamma$. Take $R_0$ so that $6\le m\le R/2$ for $R\ge R_0$. Partition each coordinate interval into pieces of length $m$, merging a final short remainder into its neighbour. The union bound on at most $R^d$ rectangles gives the probability in (2). Every rectangle then has at least $\rho |B|$ distinct good roots, $\rho=(4\,6^d)^{-1}$.

**PROVED — arbitrary field-dependent amplitudes.** On such a rectangle set $f_x=|s_x|$ and let $\bar f$ be its mean. One has $|f_x-f_y|\le|s_x-T_{xy}s_y|$ and

$$
 \sum_B(f-\bar f)^2\le 2d m^2\mathcal E_{U,B}(s).
$$

To see the constant, express the variance as half the mean squared difference at two independent uniform vertices. Replace their coordinates successively. Cauchy–Schwarz costs at most $d$ for this sum. In an interval of length $\ell$ the squared difference is at most $\ell$ times the sum of squared bond differences along that line. Averaging the other coordinates and multiplying by $|B|$ costs at most $\ell^2\le4m^2$ in that direction. At the good roots, $|B|\bar f^2\le(2/\rho)\sum_{\rm roots}[(f_x-\bar f)^2+f_x^2]$. Use (6) on their disjoint bonds. Adding the variance shows

$$
 \sum_B |s|^2\le \left[(1+2/\rho)2dm^2+24/(\rho\delta_b)\right]\mathcal E_{U,B}(s).
$$

Sum over $B$, retaining the extra nonnegative bonds between rectangles on the energy side. This proves (2).

**PROVED — counterexample to P.** For every sequence $b_R=o(R^2)$, the lower bound in (2), multiplied by $R^2$, diverges on events of probability tending to one. For every fixed budget $K$, the probability that **any nonzero choice** of $s(U)$ realizes a Rayleigh quotient $\le K/R^2$ tends to zero. This includes every $b\in[2.3,2.6]$, uniformly, and a fixed physical cube at cutoff $a_j$ when $R_j\asymp L/a_j$ and $\beta_j=O(\log(1/a_j))$. The latter is a conditional scaling consequence, independent of any claim about the law of blocked links.

**PROVED — size of the defect for a frame.** For example, choose a nonnegative cutoff $\eta$ equal to one on the central cube of side $\lfloor R/2\rfloor$, zero at the outer faces, with bond slopes at most $8/R$ for $R\ge16$ (truncate a multiple of distance to the faces). Then $\sum|\nabla\eta|^2\le64dR^{d-2}$. Apply (7) directly to the plateau, using disjoint cells of side three. Except with probability $e^{-c_d R^d}$, (6) gives a lower bound $c'_d R^d/(1+6b)$ for the second sum of (1), simultaneously for all unit axes. Its ratio to the scalar energy grows at least as $c''_d R^2/(1+6b)$. Thus allowing the axis to depend on the Wilson field cannot pay this particular defect from a fixed multiple of the diffusive profile budget. This comparison is in the Wilson law itself.

## Phase 2. What the source check changes

**PROVED in the lane — prior geometry.** Row 1011 Lemma FR, row 1018 Lemma FR+ (lines 249–255) and row 1128 Lemma HOL (lines 320–333) already give the deterministic plaquette mismatch, including FR+ for variable-length fields. Row 1018 Lemma NAB (lines 306–321) uses two different Wilson integrations by parts. On a symmetric four-torus, given $\bar x=\mathbb E\,\tfrac12\operatorname{tr}U_p\ge3/4$, it gives $\mathbb E\lambda_x\ge1/(3924b^2)$ for the sum over the six forward plaquettes, minimized over the common axis. The cross-provider check corrects the common-mean hypothesis on nonsymmetric tori. The geometric telescope and the observation that two axes suffice are prior work. The conditional cap estimate (3), the scale $1/(1+b)$ in (4), and the spatially simultaneous (2) supply the part missing from those results.

**PROVED here — the bare estimate requested at row 1018, line 273.** In (4) take instead the two *forward* squares in planes $12$ and $34$. They have distinct links and the same root, the only two properties used in (3)–(4). With row 1018's normalization $\lambda_x=\min_{|v|=1}\sum_{p\ {\rm forward\ at}\ x}|\operatorname{Im}U_p\times v|^2$, one has $\lambda_x\ge D/4$. Hence on every four-torus with periods at least three,

$$
 \mathbb E\lambda_x\ \ge\ \delta_b/8=\frac1{64(1+6b)}.                     \tag{8}
$$

In particular the bare lower bound is of order at least $1/b$ for $b\ge1$, without a plaquette-mean input. The cell-scale fluctuation bound (FL) and the decrease (DEC) in row 1018 §5.5 are open. Equation (8) concerns the bare quantity.

**PROVED in the lane — constraint forcing a return to Phase 1.** Row 1018 Lemmas FLOW and PROJ and its cross-provider check (`gap-short-step-check-astra.md`, items 7–10) state the actual signed test. For $X(B)=-\sum_e B_e\cdot N_e$, with $X$ the variation of the Wilson exponent and $N_e$ the force at the tail, put $j_e=n_{e^-}\cdot N_e$. For an internal gradient move its action variation is $-\sum_z\lambda_z\operatorname{div}j(z)$. With $\Psi_V=VA+\operatorname{div}_{\rm Haar}V$ for the Wilson exponent $A$, the pinned Hessian is $H_c=-\mathbb E[V\Psi_V]-\operatorname{Var}(\Psi_V)$. For a smooth internal move with zero Haar divergence, the Jensen cost $-\mathbb E[V\Psi_V]$ equals its action-score variance. A boundary estimate must control the direct term and its cancellation with the variance. Large $|D n|$ alone cannot imply a large signed response. The check gives an irreducible odd-torus configuration with all forces zero. Row 1026 Theorem E and its check 1027 give aligned site frames on an open set of non-reducible torus configurations. Row 1034 additionally distinguishes link frames from site frames. These results constrain the inference from (2) to H.

**OPEN — revised first leaf, same opening (b).** Apply the constraint to C8 of row 1013. Transport one unit root axis along a rooted spanning tree of the cell. The field itself supplies all the transports, and even the root axis may read the field. Is it possible for this frame to make the **signed** projected current conserved at every free site? C8's triangular, Haar-preserving version requires the ordering in its cross-provider check, lines 110–111. The general alignment examples above do not impose tree transport. This is a question about the actual PROJ current, after cancellation of the incoming and outgoing plaquette forces.

## Return to Phase 1. Signed divergence for a field-built tree frame

**PROVED here — counterexample to the revised leaf.** Sample the ordinary periodic Wilson law, $23/10\le b\le13/5$. Let $C$ be a four-dimensional cell of $R^4=V$ sites. For each spanning tree $T$ of its nearest-neighbour graph, transport a unit vector $v$ from one root along $T$, and denote the resulting current by $j^{T,v}$. There exist $c>0$ and $R_1$, independent of $b$, the surrounding torus and the choice of tree, such that for $R\ge R_1$

$$
 \mathbb P_b\!\left\{
   \min_{T,\ |v|=1}\ \frac1V
       \sum_{z\ {\rm strictly\ interior}}|\operatorname{div}j^{T,v}(z)|^2
                  \ \ge\ c b^2\right\}\ \ge\ 1-e^{-V}.                      \tag{9}
$$

Both the tree and the axis may be selected after seeing all links. One fixed root suffices, since changing it on the same tree only relabels the unit sphere. The same argument works if $C$ is the whole periodic cube and its trees may use wrap bonds. Equation (9) is averaged over the actual Wilson pins.

**PROVED — cancel the forces before estimating them.** For a fixed candidate tree make its links the identity by gauge transformation, fixing the root gauge to one. If needed extend the cell tree to a tree of the whole torus. Gauge invariance of the Wilson density and the tree Haar factorization give the Wilson density on the remaining chord variables against product Haar. This is the spanning-tree formula of Sussman and Alpoge with Claude and Codex, outline Proposition 1a.3.3, lines 7660–7681. Equivalently, condition on the tree links, carry each chord by its two endpoint transports and use left and right Haar invariance. In this gauge the transported frame is exactly $v$ at every cell site. For the positive-coordinate orientation of the bonds, the free-site Gauss identity from PROJ gives

$$
  \operatorname{div}j^{T,v}(z)=v\cdot B_z,\qquad
  B_z=\sum_{e:\,e^+=z}(\operatorname{Ad}(U_e)^{-1}-I)N_e .                \tag{10}
$$

Here the $N_e$ are computed from the *full* Wilson action in the displayed gauge. Equation (10) combines all incoming and outgoing terms, with their signs. In each $N_e$ all six plaquette forces are also added before taking a modulus. Since $|N_e|\le6b$, $|B_z|\le48b$.

**PROVED — a local nonzero polynomial for every tree pattern that is needed.** We use the two-adjacent-chord test of row 1051, Corollary RM-TREE and its following unit-cell example, with the fixed-axis scope checked by row 1057, lines 48–61 and 151–166. The local commutator is prior. Its role here is to control a positive density of sites simultaneously for field-selected trees and axes. Suppose two distinct positive-coordinate bonds $l=(y,y+\hat\imath)$, $m=(y,y+\hat\jmath)$ are chords and set $z=y+\hat\imath$. The vector $B_z/b$ is a polynomial in quaternion coordinates of the chord links in the plaquettes incident to the four incoming links at $z$. There are at most 96 such links. Hold every link in this support at one except $U_l=u=(3+4\mathbf i)/5$ and $U_m=w=(3+4\mathbf j)/5$. The two chords belong to just one common plaquette. The other incoming links at $z$ contribute zero to (10). Five plaquettes at $l$, oriented to start by traversing $l$, contribute $b\,\operatorname{Im}u$ each to $N_l$, so their total cancels under $\operatorname{Ad}(u)^{-1}-I$. The common plaquette has holonomy $u w^{-1}$, and gives exactly

$$
 B_z/b=\operatorname{Im}(w^{-1}u-u w^{-1})
       =2\,\operatorname{Im}u\times\operatorname{Im}w
       =\tfrac{32}{25}\mathbf k.                                           \tag{11}
$$

A common quaternion conjugation realizes this vector in any direction. Thus $v\cdot B_z/b$ is a nonzero polynomial restricted to the local chord groups for every fixed unit $v$, for **every** assignment of the other local edges to the tree consistent with $l,m$ being chords.

**PROVED — arbitrarily small conditional probability of a near-zero signed force.** Under local product Haar, the zero set of that polynomial has measure zero. In stereographic coordinates on each $S^3$ (omit $-1$) its numerator is a nonzero real polynomial by (11), and the rational expression has a positive denominator. A nonzero polynomial on $\mathbb R^n$ has a null zero set by induction and Fubini, discarding the null set where all coefficients in the last coordinate vanish. The coordinate volume has a smooth density and the omitted points have zero Haar measure. Continuity from above now gives probability tending to zero for $|v\cdot B_z|\le 2\epsilon b$ as $\epsilon\downarrow0$. Conjugation invariance of product Haar makes this probability independent of the direction $v$. There are finitely many local tree/chord masks and choices of the two coordinate directions. The largest of their Haar probabilities, $q_H(\epsilon)$, therefore also tends to zero.

In the tree-fixed Wilson measure the conditional density of at most $s=96$ such local chord variables, given all other chords, is at most $e^{12bs}$ relative to normalized product Haar. Indeed at most $6s$ plaquette terms change, each of oscillation at most $2b$, and division by the integral costs at most the ratio of largest to smallest weight. Hence the conditional small-value probability is at most $q(\epsilon)=e^{12(13/5)96}q_H(\epsilon)$, which can be made as small as desired independently of the torus, $b$ in the window, and the outside links. This conditional density bound transfers the local small-value estimate to the unmodified Wilson law.

**PROVED — enough tests to allow the tree itself to depend on the field.** For large $R$ at least $3V/4$ sites $y$ lie four or more layers inside the cell. Among these interior sites, at most $(V-1)/3$ have fewer than two outgoing chords, because each of them uses at least three of the $V-1$ tree edges as outgoing edges. At least $V/3$ candidates remain. For each choose two outgoing chords. The local variables determining (10) are within coordinate distance three of $y$ in the maximum norm. Greedily keep sites of mutual distance greater than six, removing at most $13^4$ candidates per choice. We obtain $N\ge\alpha V$ disjoint tests, $\alpha=(4\cdot13^4)^{-1}$, each at a free site $z$. The choices in this paragraph depend only on the fixed tree, before reading its chord values.

For fixed $T$ and $v$, the probability of small values on any specified $h$ of these tests is at most $q(\epsilon)^h$ by exposing indicators on their disjoint supports and iterating the conditional bound. The probability that at least half the values are $\le2\epsilon b$ in modulus is at most $(2\sqrt{q(\epsilon)})^N$. Fix $\epsilon>0$ so small that

$$
  2\sqrt{q(\epsilon)}<\exp[-(\log8+2)/\alpha].
$$

This is an existence choice by the proved limit, without a numerical estimate. Cover $S^2$ by a finite $\epsilon/48$-net of size $M$, by compactness. The $48b$ bound in (10) costs at most $\epsilon b$ in replacing a vector by its nearest net point. There are at most $8^{V-1}$ trees, since recording the parent of each non-root site injects rooted trees into lists of at most eight choices per site. The union of the exceptional probabilities is at most $M e^{-2V}\le e^{-V}$ for sufficiently large $R$. Off this union each tree and axis pair has at least $N/2$ sites with $|\operatorname{div}j^{T,v}|\ge\epsilon b$. This proves (9) with $c=\alpha\epsilon^2/2$. The union bound uses the original Wilson measure for every event, pulling back the transported axes from each candidate tree gauge.

**PROVED — exact failure and its cost interpretation.** Already on a sufficiently large *fixed* cell, exact conservation by any tree and any root axis has probability zero for every finite $b>0$. For each fixed tree use three disjoint tests from the preceding packing. The determinant with their three vectors $B_z/b$ as columns is a nonzero polynomial because the three disjoint patterns in (11) can be rotated to give three orthogonal vectors. The same null-set proof applies, followed by the finite union over the trees. This gives exact failure for Wilson-almost-every exterior pin by disintegration.

For a measurable selection of tree and axis, average over independent auxiliary signs $\lambda_z=\pm1$ on free sites strictly inside the cell, zero elsewhere. Equivalently take the finite uniform average over all sign assignments. It gives exactly $\sum_z|\operatorname{div}j(z)|^2$ for the averaged square of $\sum_z\lambda_z\operatorname{div}j(z)$. One may restrict the signs to sites at least two layers from the boundary, since all the tests in (9)'s proof lie there. By (9) at least one **deterministic** interior potential, independent of the Wilson sample, has

$$
 \mathbb E_b\left|\sum_e(d\lambda)_e j_e\right|^2
       \ \ge\ (1-e^{-V})c b^2 V,\qquad d(d\lambda)=0.                    \tag{12}
$$

The choice of test may depend on the frame rule. For a smooth rule whose internal moves have zero Haar divergence, the action score has mean zero by integration by parts, and (12) is an obstruction to a cost bounded by any multiple of $\sum_p |(d\theta)_p|^2$ on **all** internal $\theta$. It applies in particular to C8 when its triangularity and fixed or admissible root data give that zero divergence. For a general adaptive tree or root, (9) and (12) bound the signed action current. The response also includes the Jacobian of the move. The constant $c$ is specified by existence. Equation (12) refutes exact gradient invariance. The comparison with the bracket gain for a prescribed long-wavelength rotation remains open.

**PROVED — necessary distance from all tree transports.** This consequence applies to an arbitrary site frame $n(U)$. Let $d_T(n)=V^{-1/2}\inf_{T,v}\|n-n^{T,v}\|_{\ell^2(C)}$. For two site fields the norm of the difference of their edge currents is at most $12b\|n-n'\|_2$, since there are four outgoing edges per site and $|N_e|\le6b$. The divergence from edges to interior sites has norm at most four, by Cauchy–Schwarz on eight incident edges, each counted at most twice. Consequently on the event (9),

$$
 V^{-1/2}\|\operatorname{div}j(n)\|_2+48b\,d_T(n)\ \ge\ \sqrt c\,b.       \tag{13}
$$

An exactly conserved projected current requires mean square distance per site of at least $c/48^2$ from every tree transport. If $h_e$ is the Jacobian current of a smooth frame, replace the first norm in (13) by the sum of $\|\operatorname{div}(j-h)\|_2$ and $\|\operatorname{div}h\|_2$, with the same normalization. This gives the precise limitation for a frame that uses its Jacobian to cancel the signed action defect.

## Phase 2. Comparison models and final leaf status

**PROVED — comparison lines.**

| Test | Line at which the proposed argument loses its SU(2) input |
|---|---|
| Compact U(1), including the free-photon colour direction | Adjoint transport is the identity. $D=0$ in (4), $B_z=0$ in (10), and the commutator in (11) vanishes. |
| SU(2) times a massless factor | A rotation or bracket confined to SU(2) acts identically on $1\otimes f$ for every observable $f$ of the spectator. Node M's required strict contraction on *all* nonvacuum observables fails on this subspace. For a U(1) spectator even (2) on the whole colour space has a covariantly constant vector. This is the product test of rows 708, 998 and 1025. |
| Frozen $Q_8$ and the binary tetrahedral group $2T$ | A holonomy equal to one has positive conditional mass on a finite group with positive Wilson weights, violating (3) as $t\downarrow0$. For a frozen flat sample all local holonomies equal one. Neither group has the real part $3/5$ prescribed in (11). In $Q_8$ the choices are $0,\pm1$, and $2T=Q_8\cup\{(\pm1\pm\mathbf i\pm\mathbf j\pm\mathbf k)/2\}$ adds only $\pm1/2$. A nonzero polynomial can vanish on the entire finite support, and the finite groups have no infinitesimal link rotations. Row 884's centre-even flat states also bind node M. |

**PROVED — sector and measure.** The minimum in (9) is invariant under site gauge transformations. It is also invariant under every spatial centre-plane flip, since a flip preserves all plaquette holonomies and their left-insertion derivatives and leaves each adjoint link transport unchanged. Thus the obstruction is tested by a centre-neutral observable in the periodic Wilson law. The sums in (10)–(11) retain the cancellations between plaquette supports at the free site before the probability estimate in (9). A physical spectral estimate in the zero-flux sector is still needed at M. D2 (row 977), SHEET (row 996, with its SU(2) correction) and method 36 concern stronger uniformity in altered measures. Here only ordinary constant-coupling Wilson probabilities are estimated.

**GUIDE — comparison with the registry.** I checked the crux, methods 19–36 and lead rules in `parts/gap.md` §§“State of attack” and “Lead rules in force”, methods 1–18 in row 878 §6a, the route registry and the test table. The primary frame precedents are C8 and its ordering correction (row 1013), FR+/PROJ/NAB and their cross-provider corrections (row 1018), the aligned frames of rows 1026–1027, and PRIV/Corollary P in row 1034 §§6.4–6.5. PRIV uses a link omitted from specified frames' read sets. Equations (9)–(13) allow a selection that reads every link, provided the chosen axis is carried on a spanning tree, or has the stated distance from such a transport. Rows 1038–1048 concern pin-dependent boundary extensions, including signs on special pin sets. Row 1051 gives a mean ring identity and a two-chord witness at a fixed outer pin. Its cross-provider check 1057 explicitly leaves selection of the root axis and uniform quantitative failure beyond that witness. The packing and probability estimate in (9) address these issues for the bare current. Equation (9) uses internal gradients sampled in the Wilson law. The council's method 35 (rows 1127, 1131, 1133), the flux limitation (1025, 1129, 1130) and the correction of the threshold in method 36 (1139–1140) give no estimate of the missing signed boundary gain. On the other two openings, row 1140 leaves background-uniform layer mixing in the window open, and rows 1135–1138 leave the slab sign lemma there open. A targeted search for tree-transported frames and conserved projected currents on the YM paths of main and the four PR refs found no further supplier.

| Leaf | Status after comparison | Scope |
|---|---|---|
| UV | GUIDE — supplied by the account within its stated hypotheses. | Balaban's RG, the first-passage formulation and tree Haar factorization. The order-one step lies beyond this input. |
| Bare non-Abelian fluctuation at a site | PROVED here, (3), (4), (8). | Strengthens the mean estimate of row 1018 to $1/[64(1+6b)]$ on rectangular four-tori and supplies a conditional probability bound. |
| P and the positive-defect version of H | PROVED counterexample, (2), (6)–(8). | A microscopic frame with a fixed diffusive budget fails typically for $b=o(R^2)$. |
| H with tree transport and exact internal gradient invariance | PROVED counterexample to PROJ-current conservation, (9)–(12). | Simultaneous for every tree and root axis in the window. The cost assertion uses zero Haar divergence. Equation (13) also constrains nearby frames. |
| H with a general field-dependent frame | OPEN. | The **signed** force and Jacobian can cancel. Neither their scale relative to the bracket gain for the required rotations nor the distribution of blocked connections is supplied by (2) or (9). |
| M | OPEN. | Even a signed stiffness bound would still need a connected-SU(2) singlet-mixing consumer (L3, rows 1122–1123). |
| S | OPEN for the order-one seed. PROVED in the lane downstream of the seed. | Theorem ZD-c of row 720, lines 311–324, uses $z^-(L)=\liminf_j n_j m_j(n_j^3)>2\limsup_j\Phi_{4,j}(n_j/4)+30$, $n_j=L/a_j$ on the admissible dyadic sizes. Theorem S and SH then propagate the seed. |

**GUIDE — verification.** The new estimates are hand proofs by Codex. The quaternion calculation, normalized Haar cap, count of disjoint sites and union bound over all trees are displayed above. The signed cancellation tested in (10) is the one in the action current. They have no independent check. No numerical run or computer-assisted proof step was used. This research note grants no status.

RESULT: PROVED by hand for bare Wilson SU(2). The row-1018 local fluctuation is at least $1/[64(1+6b)]$ in mean, and at $2.3\le b\le2.6$ every spanning-tree colour frame has a positive density of signed projected-current defect with high probability, even when the tree and axis are chosen from the field. The full signed field-dependent bracket inequality, the zero-flux mixing step and the four-dimensional mass gap remain OPEN.
