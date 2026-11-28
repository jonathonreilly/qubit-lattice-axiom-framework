## Repo search

Row 1624 at a6216f709. Research text, author only. The proposed Wilson estimate is (15). The finite-volume implication, a finite-period measurement of its signed action, and the four-state comparison are proved below.

**ON FILE (rule 9 search, row 1624).** The literal search for `VIR[- ]down`, `retained SU(2) response`, `thermal virial` returned no matches in Markdown or TeX on `origin/main` (`8b11ae2bb95`), `pr/10114` (`f76f6c649cf`), `pr/10133` (`89faef229ff`), `pr/10134` (`1e70c7211a2`) or `pr/10141` (`c73ad7b177d`). Searching those five refs for diffusion distance/map, slab score, bridge-action excess/score, half-slab comparison/score and thermal Dirichlet form found two adjacent results.

- **ON FILE.** On main, `research/mass-gap/library/prior/gap-fullread-2.md:29–35` records Piazza and Shen's bound $\mathrm{Ent}_\mu(F^2)\le2C_{N,\beta}\sum_e\int|\nabla_eF|^2\,d\mu$ on every periodic square lattice, for all $N\ge2$ and fixed real $\beta$ (statement at lines 19–25). Its independent block interiors use planar tree integration. The estimate concerns configuration-space gradients.
- **ON FILE.** On PRs 10114 and 10133, `REVIEW_MASS_GAP_LOCAL_BLOCK_ASTRA.md:162–188` has half-slab influence row sum $14\beta$ and physical one-step oscillation factor $\beta/[1-12\beta-\beta^2/(1-14\beta)]$ in its small-coupling range. The November 8 digest also identifies `MASS_GAP_LOCAL_BLOCK_ASTRA.md:106–149` on these refs. Its local convolution dominates $c|F\rangle\langle F|$ for a centered simple Wilson loop. This is a one-time-step correlation witness. Neither statement compares two durations as the bare coupling varies. Both files are under `.claude/science/toe-ruleset-20261021/agents/ym4d-proof/`. [November 8 digest](prior/repo-search-2026-11-08.md)

A further search of all five refs for double-centred slab kernels, vacuum-compressed derivatives, buffered scores and outer-endpoint conditional scores returned no matches. These are bounded searches of the named local refs.

## On-file starting point

- **ON FILE (rows 1321, 1553, 1610, 1613, 1617–1623).** Row 1321 (1) gives the stationary neutral two-slice probability used below. Its exterior-square estimate (2) is an operator-norm estimate at one coupling. Row 1553, Lemma ALG, supplies the same-algebra/product test. In row 1617, (10)–(12) approximate the thermal response by finite electric tails and two magnetic means. Check 1621 shows that the remaining inequality costs the whole rate up to arbitrarily small tolerances and $O(1/\beta)$. The high-level obstruction shared by rows 1617–1619 does not apply to a thermal average. Row 1619 §3.3 gives the squared-force excess, and §3.1 explains the missing *size*. Row 1618 Theorem 2 and check 1622 give $0<R<1/\beta$ for the photon times the even electric rotors in the zero-magnetic-flux sector. Row 1623's literature survey found no order-one supplier. Row 1620 checks a different scalar-ring test. The [registry](open-registry.md) lists VIR-DOWN as open, owner none. Its neighbour LEV-FAIL owns the level obstruction.
- **ON FILE (outline, row 244 index).** The chunk-02 entries at 2315–2335 lead to Sussman and Alpoge's GL8, the positive gauge-averaged transfer and the periodic trace. The [index](sa-index/README.md) and [obligations](sa-index/obligations.md) distinguish this construction from the optional Ward input at 32364–32380. CA-I 2706–2710 explicitly excludes a gap from Theorem 0. The local texts are the supplied copies of revision `31a47c543775`, credited to Ethan Sussman and Levent Alpoge with Claude and Codex. No Balaban estimate enters the argument. The task-specific prior file is absent. Local searches for diffusion distance, a coupling derivative of a Dirichlet form, slab scores, crossing/escape and vacuum transport found the pair law above, the conditional one-step scores of row 1298 and the fixed-coupling escape tests of rows 975–976. None of these nearby statements compares the response of a distribution of slice displacements with the cost of removing one time step from a marked central segment.

## The proposed measurement on Wilson slabs

**ON FILE (rows 1321, 1468, 1610 and check 1613).** Fix check 1453's odd block factor and calibration $g_0$, let $1024\mid\ell$, $n=\ell b^K$, $u=n/512$, and keep this spatial lattice fixed as its bare coupling varies above $\beta_K$. Write $\lambda=\lambda_0$, $r_i=\lambda_i/\lambda=e^{-m_i}$, $r_0=1$, $m_0=0$, $Z(t)=\sum_i r_i^t=1+G(t)$, $X=\log Z$ and $\bar E_t=\sum_i m_i r_i^t/Z(t)$. Choose a real positive Perron function $\Omega$ of Haar norm one. On the full spatial link manifold with Haar probability $dx$, use the kernel $K_h$ of the gauge- and centre-averaged $T^h$, for integer $h\ge1$, in the symmetric magnetic placement. Its neutral Doob transition has density
$$
 \pi(dx)=\Omega(x)^2dx,\qquad
 p_h(x,y)=\frac{K_h(x,y)}{\lambda^h\Omega(x)\Omega(y)},\qquad
 q_h(dx\,dy)=p_h(x,y)\pi(dx)\pi(dy).                                    \tag{1}
$$
Both marginals of $q_h$ are $\pi$. This is the joint vacuum law of two slices $h$ steps apart. The gauge and centre averages are included even in $q_1$. The unnormalized trace $Z_+(t)$ and the normalized sum $Z(t)$ have different vacuum factors.

**Definition.** Mark the central two-step Wilson action $A$, including half the spatial weight at each outer end, and the gauge and centre variables of (1). Let $a(x,y)=\mathbb E[A\mid X_0=x,X_2=y]$, $\bar a=\mathbb E A$ and $g(x)=\mathbb E[A-\bar a\mid X_0=x]$. Reversibility gives the same conditional mean at the second end. At fixed coupling and trial rate $\kappa\ge0$, use the signed measure
$$
 \begin{split}
 B(x,y)&=a(x,y)-\bar a-\frac{g(x)+g(y)}{p_2(x,y)},\\
 \sigma&=w q_2,\qquad
 w=B-2\kappa(1-p_1/p_2).                                                    \tag{2}
 \end{split}
$$
Each marginal of $\sigma$ vanishes because integrating $B p_2$ over one end cancels $g$ and $\int g\,d\pi=0$. The second term compares the same endpoints at two steps and at one. Formula (5) below gives an ordinary field measurement of the first term. It uses independent vacuum draws at this one coupling.

**Definition.** For an integer $j\ge1$, let $P^j(x,dz)=p_j(x,z)\pi(dz)$ and put
$$
 \begin{split}
 D_j(x,y)&=\int [p_j(x,z)-p_j(y,z)]^2\,\pi(dz),\\
 L_j(x,y)&=\sum_{C\in\mathcal C,\ \pi(C)>0}
       \frac{[P^j(x,C)-P^j(y,C)]^2}{\pi(C)} .                             \tag{3}
 \end{split}
$$
$D_j$ measures the difference between the two future slice distributions. $L_j$ measures only the differences visible in a specified finite observation of that future. Fix $\mathcal C$ **before** testing the inequality. For a concrete Wilson choice, evolve the spatial slice by $\dot U=-\nabla S_{\rm sp}(U)$ for $(n/128)^2$ units of lattice flow time, using the product unit-sphere metric and the sum of shifted spatial plaquette actions without $\beta$. On the flowed field read the normalized traces of the straight-edged spatial squares of side $n/32$, in all three coordinate planes, based at the grid $(n/32)\mathbb Z^3$ modulo $n$. Bin each trace in intervals of width $1/8$ on $[-1,1]$, assigning internal endpoints to the upper bin and including $1$ in the last bin. Their joint partition is $\mathcal C$. The finite-time flow is a diffeomorphism by completeness and uniqueness of the smooth ODE on a compact manifold. Its equivariance and the contractibility of the squares make these observations neutral. The number of measurements is independent of $K$.

**ON FILE / GUESSED.** Row 1285 explains the perimeter noise in a thin-loop readout, and row 1371 treats related long-path suppression. Row 1547, Theorem 3B, uses Wilson flow for a different constrained-kernel test. Here spatial flow defines the observation at a fixed fraction of the box size. Its adequacy for the thermal response is GUESSED. No continuum limit or effectiveness of the smoothing is assumed in the finite-box lemmas.

**GUESSED (the two-step version of (15)).** Fix the release witnesses and one allowed $\ell$. On an infinite set of late $K$, specify a long window, $\kappa(\beta)\ge0$ and $t=u\exp(\int_{\beta_K}^{\beta}\kappa)$ as in TR-down. At each cold point $G(t;\beta)\le1/2$, set $j=\lfloor(t-2)/2\rfloor$ and $w_\pm=\max(\pm w,0)$. The two-step test is
$$
 \boxed{\quad
    \int w_+\,L_{j+1}\,dq_2\ \ge\ \int w_-\,D_j\,dq_2 .
 \quad}                                                                     \tag{4}
$$
Take $t\ge4$, which holds for all sufficiently late $K$. The desired rate and window budget are fixed independently of $K$. A precise constant-rate version takes $\kappa=8/3$, $\beta_h=\beta_K+(3/8)\log512$, so $t_h=n$. HOT at that endpoint would suffice. The size range $2.3$–$2.7$ in row 1619 and check 1622 is a guide. Formula (15) also accepts a prescribed continuous speed if the band occupies only part of the characteristic and other estimates supply the rest.

**ARGUED (physical content).** The proposed mechanism is an excess of the central Wilson action on histories whose two ends predict different coarse magnetic loops a physical time later. Centering subtracts the excess already explained by seeing either end alone. Its remaining size must pay for the change from two steps to one and for *all* neutral fluctuations on pairs carrying the opposite sign. Equation (15) first averages this signed mark over the interior of a longer slab. Which histories carry the excess is a question about the probability law.

## First component on the actual finite Wilson box

**ON FILE (neighbouring constructions).** Row 1132 §2 transports the vacuum to Haar coordinates for commutator insertions. Row 1215 (24) differentiates a centered plaquette two-point function by a sum of connected three-point insertions. Row 1220 uses projections onto centered functions in a product probability space. Sussman–Alpoge outline 29991–29998 subtracts a vacuum vector in a two-point kernel. Here the two-end centering can be performed on a single marked neutral slab. [Row 1132](gap-council-op-astra.md) · [Row 1215](gap-solve23-astra62.md)

**PROVED (measuring the centered derivative without the derivative of the vacuum).** For any bounded real reading $F(x,y)$, take $X,Y$ from the marked two-step stationary segment and $X',Y'$ independent of it and of one another with law $\pi$. Define $\Delta F=F(X,Y)-F(X,Y')-F(X',Y)+F(X',Y')$. Then
$$
   \int F B\,dq_2=\mathbb E[(A-\bar a)\Delta F].                             \tag{5}
$$
The term with two fresh ends has mean zero after multiplication by the centered mark. Conditioning each of the other two fresh-end terms gives respectively $\int F(x,y)g(x)\,\pi(dx)\pi(dy)$ and its $g(y)$ counterpart. The term with the original ends gives the $a-\bar a$ term in (2). This proves (5). All three conditional means in (2) are at the anchor. A time step carries $3n^3$ temporal plaquettes and the equivalent of $3n^3$ spatial plaquettes. Each shifted action is at most two, giving $0\le A\le B_n=24n^3$.

For the spectral meaning, set $A_b=T_{+,b}/\lambda_b$, with $b$ here a variable coupling, and use the **fixed** isometry $Uf=\Omega_\beta f$ from $L^2(\pi_\beta)$ to Haar space. Then $U^{-1}A_\beta U=P$. Differentiation of the bounded slab integral at fixed endpoints gives $-\partial_b\log K_{2,b}|_\beta=a(x,y)$. Taking the vacuum expectation also gives $\bar a=-\langle\Omega,(T_{+,b}^2)'_\beta\Omega\rangle/\lambda^2=-2\lambda'_\beta/\lambda$, using the simple Perron eigenvalue. Therefore the density kernel of $-U^{-1}(A_b^2)'_\beta U$ is $(a-\bar a)p_2$ relative to $\pi\otimes\pi$. Compress this operator on both sides by $Q=I-|1\rangle\langle1|$. Since the overall mean is zero, compression subtracts just the two one-end means $g(x),g(y)$. The result is precisely the signed kernel $B p_2$. The short proof uses only the vacuum vector at a single coupling. It gives all the excited diagonal matrix elements needed below, even though the full off-diagonal operator changes under compression.

**PROVED (integer slabs suffice for the real-time test).** At every such Wilson box, every real $t\ge4$, every finite partition and every $\kappa\ge0$, (4) implies
$$
             \frac{1}{t}\partial_\beta X(t)\ \ge\ \kappa\bar E_t .           \tag{6}
$$
The two sides of (4) use ordinary positive, integer-step probabilities. The derivative in (6) is at fixed $n,t$.

*Proof.* Use a real orthonormal basis $f_i=\psi_i/\Omega$ of the neutral $L^2(\pi)$, with $P f_i=r_i f_i$, $P=P^1$, $f_0=1$. The nonneutral orthocomplement has eigenvalue zero after averaging. Every positive-eigenvalue function is smooth by its kernel equation. By Parseval, for $\pi\otimes\pi$-almost every pair,
$$
 D_k(x,y)=\sum_{i>0} r_i^{2k}[f_i(x)-f_i(y)]^2,\qquad
 L_k(x,y)\le D_k(x,y).                                                       \tag{7}
$$
Indeed the coefficients of $p_k(x,\cdot)$ are $r_i^k f_i(x)$. The conditional expectation onto the cells is the orthogonal projection in $L^2(\pi)$, with squared difference exactly $L_k$. Integer kernels are smooth and bounded, so $D_j$ is bounded on the fixed box. Define $D_*=\sum_{i>0}r_i^{t-2}(f_i(x)-f_i(y))^2$ at the anchor. Positivity of every summand and $2j\le t-2<2j+2$ give
$$
                      L_{j+1}\le D_{j+1}\le D_*\le D_j .                    \tag{8}
$$
Thus (4) implies $\int D_*\,d\sigma\ge0$, even when $t$ is noninteger. The observable $D_*$ is frozen in this test. No derivative of its eigenvectors or its time is taken.

For normalization and sign, set $d_i=\langle\psi_i,A'_\beta\psi_i\rangle$. On an excited $f_i$ the compression by $Q$ has no effect on its diagonal. Thus the $i$-th diagonal of the kernel $B p_2$ is $-2r_i d_i$. Its marginals vanish, so the two squared one-end terms in $(f_i(x)-f_i(y))^2$ contribute zero. For $q_2-q_1$ the same cancellation holds. It follows that
$$
 \begin{aligned}
 \tfrac12\int D_* B\,dq_2
      &=2\sum_{i>0}r_i^{t-1}d_i=\frac{2Z(t)}t\,\partial_\beta X(t),\\
 \tfrac12\int D_*\,(dq_2-dq_1)
      &=\sum_{i>0}r_i^{t-2}(r_i-r_i^2)
        =\sum_{i>0}r_i^t(e^{m_i}-1).
 \end{aligned}                                                               \tag{9}
$$
The first line uses the real-time trace derivative from check 1613 with $d_0=0$, valid also at eigenvalue coincidences. Both integrations of the series follow by domination by $D_j$ against the total variation of the respective signed measures. Inserting (2) in (9) gives
$$
 \frac14\int D_*\,d\sigma
     =\frac{Z(t)}t\,\partial_\beta X(t)
       -\kappa\sum_{i>0}r_i^t(e^{m_i}-1).                                    \tag{10}
$$

Since $e^m-1\ge m$ and $Z(t)\bar E_t=\sum_{i>0}m_i r_i^t$, (6) follows. This argument needs no bound on $G(t/2)$ and imposes no inequality on each energy level. $\square$

**PROVED (integer-period field check of the sign and factor in (10)).** For integer $t\ge4$, expand the squared difference with weights $r_i^{t-2}$. The mixed term is $p_{t-2}(x,y)-1$, and the one-end terms vanish against $\sigma$. In the remaining integral of $p_{t-2}$ against $Bq_2$, both $g$-terms integrate to zero since $p_{t-2}$ preserves $\pi$. Closing the two-step segment with $p_{t-2}$ leaves $Z(t)(\mathbb E_t A-\bar a)$. Each of the $t$ cyclic placements of one time step contributes equally to the mean total action $A_t$, so $\mathbb E_t A=2A_t/t$. With $a_0=-\lambda'/\lambda=\bar a/2$, this gives the action contribution $Z(t)(a_0-A_t/t)$ to $\int D_*d\sigma/4$. Closing $q_2-q_1$ instead gives $Z(t)-Z(t-1)$. The result is $Z(t)(a_0-A_t/t)-\kappa[Z(t-1)-Z(t)]$, as in (10) and row 1610's D1.

**ON FILE (rows 1610, 1613, 1617).** If (4) holds whenever $G\le1/2$ along the characteristic and the hot end has $G\le4/21$, then the chain rule with $X_t=-\bar E_t$ prevents a last crossing of $1/2$ before the hot end. TR-down gives $G(u;\beta_K)\le4/21$. The passage to (PUR-io) uses the fixed enlargement in check 1613. The same-box implication supplied by Fact PUR in row 1468 §3.1 points from purity to the thermal seed.

## What has to be estimated in (4)

**PROVED (a way to certify the two sides separately).** For any measurable event $A$ of the endpoint pair, the signed mass needed on that event is
$$
 \sigma(A)=q_2(A)\mathbb E_{q_2}[B\mid A]-2\kappa\,[q_2(A)-q_1(A)]          \tag{11}
$$
when $q_2(A)>0$. Suppose there is a union $C$ of the fixed observation cells with $p=\pi(C)\in(0,1)$, and on $A$ the absolute difference between $P^{j+1}(x,C)$ and $P^{j+1}(y,C)$ is at least $a$. For any $M\ge0$, it suffices that
$$
       \sigma(A)\ge M,\qquad
       \int w_-D_j\,dq_2\le \frac{a^2 M}{p(1-p)} .                           \tag{12}
$$
The two-cell observation $C,C^c$ gives $L_{j+1}\ge a^2/[p(1-p)]$ there, by (3) and Cauchy–Schwarz within each union. Also $\int_A w_+dq_2\ge\sigma(A)$. This proves the claim. The negative-side cost itself has the following positive decomposition. Writing $\delta_j(z)=p_j(x,z)-p_j(y,z)$ gives
$$
     D_j=L_j+\sum_C\pi(C)\operatorname{Var}_{\pi(\cdot\mid C)}(\delta_j).
                                                                            \tag{13}
$$
This is the orthogonal projection identity, keeping the within-cell fluctuations. Equivalently the full term can be read from three ordinary return densities,
$D_j=p_{2j}(x,x)+p_{2j}(y,y)-2p_{2j}(x,y)$, by symmetry and composition. A field proof using (11)–(13) would identify a class of two-step histories, bound its *conditional excess action* using the independent-end subtraction (5), and bound the within-cell propagation on negative-weight pairs. All three quantities can be tested on the same fixed box. There is no presumption that a single loop or a single event meets (12).

**PROVED (the negative cost really occurs on Wilson fields).** For every finite Wilson box in this row, every $\beta>0,\ \kappa>0$, and every $j\ge1$, both signs of $w$ have positive $q_2$ measure. Moreover, for the prescribed nontrivial loop partition,
$$
 0<\int w_-L_j\,dq_2<\int w_-D_j\,dq_2,\qquad
 0<\int w_+ L_{j+1}\,dq_2 .                                                 \tag{14}
$$
The inequalities are strict at fixed cutoff. They give no relative size uniform in $K$.

*Proof.* If $\sigma=0$, testing its quadratic form on any one $f_i$ as in (9) gives $2r_i d_i=2\kappa(r_i-r_i^2)$, hence $d_i/r_i=\kappa(e^{m_i}-1)$. Row 1617 (2), checked at 1621 §1.2, gives $(d_i/r_i)/m_i\to0$ as $m_i\to\infty$ on this box. The neutral positive spectrum is infinite. This contradicts the displayed equality. Since $\sigma$ has total mass zero and a bounded density against $q_2$, both signs occur.

The kernel $P$ is injective on neutral $L^2(\pi)$ by the positive Wilson link multipliers and the invertible spatial weight (row 1617, preliminaries). For every bounded neutral nonconstant $g$, $P^k g$ is nonconstant for each $k\ge1$, since a constant value could be subtracted before applying injectivity. It is also real analytic in the slice. The analytic regularity of functions in $T_+L^2(dx)$ follows because the finite Wilson kernel is an integral over compact sets of exponentials of polynomials in the quaternion entries of the ends, with uniformly bounded holomorphic extensions in a neighbourhood of each real chart. This follows by using quaternion conjugates for the inverses on the real group and extending their linear coordinate formulas. Termwise integration on a smaller complex neighbourhood is valid by uniform bounds. Apply the kernel first to $\Omega$ itself and then to $\Omega g$, dividing locally by the positive analytic Perron function. Iteration gives the assertion for all $k$.

On a connected real-analytic manifold a nonconstant analytic function has levels of smooth volume zero. To see this for a fixed level, at every zero some derivative of positive order is nonzero, since otherwise the Taylor series vanishes in a neighbourhood and continuation gives a constant. Taking one predecessor of a nonzero derivative of *minimal* order yields a vanishing derivative whose gradient is nonzero. Thus the level is covered, chart by chart, by countably many regular hypersurface pieces of those predecessor derivatives. This proves the null assertion. Consequently $P^k g(x)\ne P^k g(y)$ almost everywhere for $\pi\otimes\pi$, and also for $q_2$ by (1).

The union of cells where one specified flowed loop has nonnegative trace and its complement both have positive measure. In the output of the spatial flow one can make this loop identity or minus identity by changing one traversed link. Both signs persist on open sets, the flow has a smooth inverse, and $\Omega>0$. For its indicator $g$, (3) and projection onto $g$ minus its mean now give $L_k>0$ almost everywhere. There also exists a bounded, nonzero neutral $g$ orthogonal to all the cell constants. For example subtract from a single fine plaquette trace its conditional expectation given the cells. The trace has an atomless law because its holonomy is Haar under the product reference (integrate any one of its distinct edges) and $\pi$ has a positive density there. It cannot equal a finite-valued function almost everywhere. Normalize the difference to unit $L^2(\pi)$ norm. Orthogonal projection gives $D_k-L_k\ge[P^k g(x)-P^k g(y)]^2>0$ almost everywhere. Integrate against the two nonzero signs to obtain (14). $\square$

**ARGUED (first missing Wilson estimate).** The positive coarse-loop contribution would have to dominate the full negative-side prediction cost in (4), including the strictly positive last term of (13). Short-time persistence of a coarse label alone cannot estimate that cost. The exact subtraction (5) gives no bound on the competing conditional actions at an order-one effective coupling. The dimension enters through the distribution of the full spatial and temporal plaquette histories and the propagation of the chosen large spatial loops. No bound for that dimension dependence has yet been proved.

## Conditioning the score on the ends of a longer slab

**PROVED (sufficiency of the central inequality).** Take an integer $k\ge0$ with $t-2-2k\ge2$. In the stationary process (1) draw the two-step segment $X_0,X_2$ together with endpoints $X_{-k},X_{2+k}$. Define
$$
 \begin{split}
 h&=2k+2,\qquad b_k(x,y)=\mathbb E[w(X_0,X_2)\mid X_{-k}=x,\ X_{2+k}=y],\\
 j_k&=\lfloor(t-h)/2\rfloor .
 \end{split}
$$
For $k=0$, $b_0=w$. The proposed band test compares the positive and negative parts of this conditional mean,
$$
 \boxed{\displaystyle
    \int (b_k)_+\,L_{j_k+1}\,dq_h
          \ \ge\ \int (b_k)_-\,D_{j_k}\,dq_h .}                              \tag{15}
$$
**GUESSED for Wilson.** Use, for definiteness, $k=\lfloor t/8\rfloor$, with $t\ge8$ at all sufficiently late cutoffs. Require (15) on the same cold collar and with the same order-one rate and budget specified for (4). The outer endpoints are drawn from the stationary Wilson law at separation of order $t$. Bounding their negative contribution also requires control of rare pairs with large $D_{j_k}$. In (5) one only inserts the action of the central two steps. The term $1-p_1/p_2$ of (2) becomes $1-p_{h-1}/p_h$ after conditioning, since with $p_1$ in place of $p_2$ the central propagation loses just one ordinary time step. One may use (11)–(13) on these outer endpoint pairs with $b_k,q_h,j_k$ and the conditioned version of (5).

*Proof of sufficiency and of the averaging claim.* Regard a signed measure with density relative to $\pi\otimes\pi$ as an integral kernel, and denote the kernel of $\sigma$ by $S$. At fixed coupling, the Markov property and reversibility give the density of $b_k q_h$ as $S_k=P^k S P^k$, including for $k=0$. Integrating $p_k(x,x')p_2(x',y')w(x',y')p_k(y',y)$ against $\pi(dx')\pi(dy')$ verifies this for $k\ge1$. Dividing by $p_h(x,y)>0$ gives the stated conditional mean. The same multiplication with $p_1$ proves the one-step-shorter term. The marginals still vanish and $\int |b_k|\,dq_h\le\int |w|\,dq_2$ by conditional Jensen. Thus histories of opposite signs can cancel *before* a positive or negative cost is charged.

In (8)–(10) use $D_{*,k}=\sum_{i>0}r_i^{t-h}(f_i(x)-f_i(y))^2$ at the outer endpoints. It lies between $L_{j_k+1}$ and $D_{j_k}$. Zero marginals and $P^k f_i=r_i^kf_i$ give
$$
 \int D_{*,k}\,b_k\,dq_h
    =-2\sum_{i>0}r_i^{t-h}\langle f_i,S_k f_i\rangle
    =-2\sum_{i>0}r_i^{t-2}\langle f_i,S f_i\rangle
    =\int D_*\,d\sigma .                                                     \tag{16}
$$
Thus (15) implies (6) with the *same* one-step secant $e^{m_i}-1$ for every buffer length. All objects in (15) are integer-time field kernels. Neither $k$ nor $j_k$ is differentiated. For every finite $k$, the nonzero high-energy diagonal used in (14) remains nonzero after multiplication by $r_i^{2k}>0$. Hence the strict positive-cost conclusions of (14) hold also for the two signs of $b_k q_h$. $\square$

**PROVED (size of the filtering on a specified energy range).** Let $E_{\ge m}$ be the spectral projection onto positive neutral eigenvalues $r_i\le e^{-m}$. Then $\|E_{\ge m} S_k\|_{\rm HS}\le e^{-km}\|S\|_{\rm HS}$, and the same estimate holds on the right. Indeed $\|E_{\ge m}P^k\|\le e^{-km}$, $\|P^k\|\le1$, and the fixed-box kernel of $S$ is bounded. This bound has a box-dependent prefactor. It locates the fast variations that conditional averaging suppresses. The surviving low-energy part still enters (15). The sparse inserted contractions of Sussman–Alpoge GL9–10 (outline 2337–2381) bound a modified trace from above. Here the central insertion has both signs, and its relative size on the two outer-end laws is the unknown.

## Exact finite test with a hidden neutral mode

**PROVED (order-one rate in a four-state law).** There is a family with a coupling-independent excited level in which (15) with the observation of just one bit proves the rate $8/3$, uniformly in the size parameter throughout a window of width $W=(27/8)\log 2$. Its integrated speed is $\log512$. The argument uses the probabilities of transitions in the specified law.

Let $M_r(x,y)=(1+rxy)/2$ be the transition **probability** on signs $x,y\in\{-1,1\}$, with fair stationary measure. On two independent signs take $P=M_r\otimes M_s$, $s=1/2$, and
$$
 q=e^{-3\beta},\qquad r=\frac{1-q}{1+q}.
$$
The first sign assigns relative Boltzmann weight $q$ to a flip. The second sign is unobserved and has fixed nonzero energy $\log2$. Use the fair vacuum measure, the partition by the first sign, and $\kappa=8/3$. For every sufficiently large integer $n$ divisible by 1024, let $\beta_n=\frac13\log(n/4096)$, $\beta=\beta_n+x$, $0\le x\le W$, and $t=(n/512)e^{\kappa x}$. These couplings define this example only.

*Proof.* The three nonconstant orthonormal characters are the first sign, second sign and their product. Their multipliers $v$ are $r,s,rs$. By (2) and (16) the density of $b_k q_h$ relative to the fair pair reference $\pi\otimes\pi$ is
$$
    c_r r^{2k}\epsilon+c_s s^{2k}\eta+c_{rs}(rs)^{2k}\epsilon\eta,\qquad
    c_v=-2v\,[v'-\kappa(1-v)],                                               \tag{17}
$$
where $\epsilon,\eta$ are the respective products of the two outer signs. In this family the stationary law is fixed, so differentiation of the normalized two-step transition already has zero one-end means. Equivalently (17) follows by expanding the two transition probabilities in the sign basis. Crucially $r'=\tfrac32(1-r^2)$ by the flip weight. Uniformly for $x\in[0,W]$ we have $4096e^{-3W}/n\le q\le4096/n$, so eventually $r\ge8/9$ and
$$
       -c_r=2r(1-r)\,[\,3(1+r)/2-8/3\,]\ \ge\ (1-r)/6\ \ge\ q/6 .
$$
The other two coefficients have absolute value at most $9$ since $0<v<1,\ |v'|\le3/2$. For $q\le1/2$ integration of $2/(1-z^2)$ from $0$ to $q$ gives $2q\le-\log r\le4q$. Since $qt=8e^{-x/3}\le8$, $r^t\ge e^{-32}$. Also $2k\le t$, so the first coefficient in (17) has magnitude at least $4096e^{-3W-32}/(6n)$. The sum of the two other magnitudes is at most $18\,2^{-2\lfloor t/8\rfloor}\le72\,2^{-n/2048}$. This is less than the first magnitude for all sufficiently large $n$, uniformly throughout the window. Thus the signed density is positive exactly when the first sign flips between the outer ends.

On those positive pairs $L_{j_k+1}=4r^{2(j_k+1)}\ge4e^{-32}$, since $2(j_k+1)\le t$. On negative pairs the first signs agree, so only the second and product terms contribute to (7), giving $D_{j_k}\le8\,2^{-2j_k}$. Here $j_k\ge3t/8-2$ tends uniformly to infinity. The positive and negative parts have equal mass. These two bounds prove (15), strictly for all sufficiently large $n$. Coldness holds along this window because $t(-\log r)\ge 16 e^{-W/3}=16\,2^{-9/8}>4$, and $G=r^t+2^{-t}+(r/2)^t\le e^{-4}+2\,2^{-t}<4/21$ for all sufficiently large $n$. In particular the whole long window, including HOT, is nonvacuous. $\square$

**ARGUED (what the finite example establishes).** The local mechanism in this example is the order-one action difference for a transition of the observed sign. The proof controls the unobserved mode by actual propagation through the buffer on *both* sides of that transition. Demanding the same fractional slope of every level would fail already at the second sign. The example supplies no identification of a Wilson loop with a binary mode or a Wilson transition with action cost three.


**PROVED (strict separation with the observation fixed).** Keep exactly the same four states, the same observation of the first sign, and the same window, but interchange the two transition laws, so the observed sign has multiplier $s=1/2$ and the hidden sign carries $r(\beta)$. Every eigenvalue, thermal response and purity is unchanged. In particular the rate $8/3$ and HOT hold on the long window by the preceding proof. On the initial box the purity is at least $1/(1+G)^2$, with $G\le e^{-4}+2\,2^{-u}<1/8$ eventually, so it exceeds $64/81>457/625$.

Nevertheless, (15) fails for **every** $\kappa>0$, every admissible $k$, at every such point. Let $A$ be the event that the *observed* outer sign flips. Its stationary marginal kernel is independent of $\beta$. Integrating (17) over the other sign leaves the density $2\kappa s(1-s)s^{2k}$ times the product of the observed signs relative to their fair pair law. Hence $(b_kq_h)(A)=-\kappa s^{2k+1}(1-s)<0$. Write $\nu_\pm=(b_k)_\pm q_h$. Then $\nu_-(A)>\nu_+(A)$. The observation gives $L_{j_k+1}=4s^{2j_k+2}\mathbf1_A$ and the complete contrast satisfies $D_{j_k}\ge4s^{2j_k}\mathbf1_A$. These facts reverse (15) strictly. This separation works for arbitrarily small positive rates, and pointwise in the real time, so changing the side or taking a small positive rate does not rescue the test. At zero speed the density on $A$ is a nonzero multiple of the product of the hidden signs, because $r r'>0$ and $1-s^{2k+2}>0$ in (17). Thus $\nu_-(A)=\nu_+(A)>0$, which still gives strict reversal. The example separates the *fixed-observation* hypothesis from the seed and from thermal VIR-down in the class of positive transfer families. For the calibrated **pure Wilson** family the converse remains unknown.

## Comparison laws

**PROVED (failure in the marked-slab measurement itself).** For the free photon and the compact Gaussian law of row 1618, the signed mass integrated against $D_{*,k}$ can be evaluated before taking its positive and negative parts. Use the rescaling of each transverse oscillator coordinate by $\sqrt\beta$ to keep its vacuum Gaussian fixed. The normalized transition law of each such oscillator is then independent of $\beta$. For the compact Gaussian family keep the even electric rotors in the unaltered Haar coordinates. By row 1618 Theorem 2 and the projection correction of check 1622 §2.1, a joint character/oscillator state has energy
$$
 m=e_Q+E_{\rm ph},\qquad e_Q=\frac{|Q|^2}{2\beta n},\quad Q\in(2\mathbb Z)^3 ,
$$
with $E_{\rm ph}\ge0$ independent of $\beta$. The model omits monopoles and spatial magnetic flux. The eigenfunctions in these coordinates are fixed, so the two-step transition on this mode has derivative $2e^{-2m}e_Q/\beta$. Testing the conditional bridge measure exactly as in (9), (16) gives
$$
 \frac14\int D_{*,k}\,b_k\,dq_h
       =\sum_{m>0}e^{-tm}\,[\,e_Q/\beta-\kappa(e^m-1)\,] ,                 \tag{18}
$$
counting every mode with multiplicity. For the pure transverse photon set $e_Q=0$. The exchanges of integration and summation are valid here too. Each one-end diagonal $p_{2j_k}(x,x)$ has finite integral $\operatorname{Tr}P^{2j_k}$. The two diagonals bound $D_{j_k}$ since the cross kernel is positive. They are integrable against either stationary pair law. In the rescaled comparison coordinates the vacuum measure is fixed, so the compressed derivative equals the ordinary transition derivative. That derivative is zero in the photon variables, and the rotor factor has bounded logarithmic derivative on its compact torus at each fixed $n,\beta$. Conditional averaging preserves the same integrability bound, using the two outer pair laws and their common marginals.

For the photon, (18) is strictly negative whenever $\kappa>0$. For the compact Gaussian law it is strictly negative whenever $\kappa\ge1/\beta$, since $e_Q\le m<e^m-1$ on every excited state. By (8) and (16) the positive coarse contribution minus the complete negative contribution in (15) is at most (18) multiplied by four. Thus (15) fails for *every* finite observation and every buffer at these rates, also at arbitrarily cold points. The calculation reads the rescalability of the oscillator transition and the diffusion time $h/(\beta n)$ of the holonomy. It uses neither a vanishing Lie bracket nor an assertion that the seed of the comparison law is false. The on-file cold rate $9/(10\beta)<R<1/\beta$ for $\beta\ge4$ is consistent with this stronger test.

**ON FILE and PROVED conditional implication (interacting abelian comparison).** For the weak four-dimensional Wilson cosine law with the specified three half-turns, row 1573 and check 1579, with their periodic Villain comparison input, give $G_{\rm even}(u)>1$. Row 1617 (13) locates a cold point of negative characteristic derivative on any window ending at HOT. At that point (6) is false, so (15) fails by (16). This argument does not evaluate an individual cosine bridge score. Under the full continuous-centre projection the two even-flux witnesses used here are absent.

**ON FILE and ARGUED (five dimensions and the SU(2) factor test).** On a spatial four-torus the same conditional identity uses all four-direction spatial histories, six loop planes and the corresponding neutral projection. No proof in this row bounds the actual weak-coupling five-dimensional Wilson bridge law. If at the starting aspect a neutral level has $um<\log2$, then $G(u)>1/2$ and any HOT endpoint forces an interior cold point with negative characteristic derivative by the last-crossing/mean-value argument of check 1613. Equation (16) then makes (15) fail there, for every observation. Excluding an infinite passing subsequence this way would need such a starting-box estimate eventually at every allowed side and calibration. I cannot prove it for interacting 5D SU(2), or prove the unconditional 4D-versus-5D Wilson distinction. In a product of the 4D Wilson law with the neutral light oscillator of row 1617, the oscillator gives $G(u)>1/2$ on every such box, so the same conclusion holds on any HOT window. The Wilson loops in the observation can retain exactly their original law while the right side of (15) sees the extra mode. The four-state separation demonstrates this sensitivity even with all spectra and dimensions held fixed across the two examples.

## Measuring the signed action on finite periodic Wilson fields

**PROVED (uniform control of the entire signed measure at a cold point).** Write $\mu_k=b_k q_h$. There is an explicit signed measure $\widehat\mu_{k,M}$ using only independently drawn *finite periodic neutral Wilson fields* with periods at most $h+M$, such that for every integer $M\ge t$ and every $G(t)\le1/2$,
$$
 \sup_{|F|\le1}\left|\int F\,d(\widehat\mu_{k,M}-\mu_k)\right|
 \ \le\ (32B_n+8\kappa)G(M)
 \ \le\ (32B_n+8\kappa)\frac{3t}{\log2}\,2^{-M/t}\bar E_t .               \tag{19}
$$
The supremum is over bounded measurable readings of both outer ends. This extends the cold finite-period replacement of a specific mean in row 1617 (10) to the signed measure needed in (15). It gives a finite-torus test of (11) simultaneously for every choice of the event.

*Construction and proof.* In (5), let $X,Y$ now be the outer ends of the stationary $h$-step segment, keep the action $A$ on its central two steps, and take $X',Y'$ independently from $\pi$. Equations (5) and (16), or conditioning on the inner ends, give
$$
   \int F\,d\mu_k=\mathbb E[(A-\mathbb EA)\Delta F]
                  -2\kappa\big(\mathbb E_{q_h} F-\mathbb E_{q_{h-1}} F\big).
                                                                            \tag{20}
$$
Indeed $\mathbb E[A-\bar a\mid X]=P^k g(X)$ and similarly at $Y$. The two independently resampled ends give the two one-end subtractions in $P^k S P^k$. Replace each stationary segment of length $s=h,h-1,0$ by the restriction of a neutral periodic path of length $M+s$, retaining independent rings for independent draws. A length-zero segment means one observed slice. Replace $\mathbb EA$ by the corresponding main ring mean of the central mark. This defines $\widehat\mu_{k,M}$ by (20). Use the positive projected kernels of (1) at the observed cuts. On the quotient by slice gauge transformations and centre flips this is the usual neutral ring. For arbitrary readings of raw representatives, independently average the representatives at the observed slices. Equivalently, insert an independent uniform centre flip at every time cut and sum the temporal gauge links. Changing each slice by the cumulative preceding flips collects the twists at one seam and preserves Haar measure and the marked plaquette action with its seam signs. Each total twist has $8^{M+s-1}$ choices of cut flips. This implements the same eight-twist mixture and specifies the raw-end law used in (19).

Use the marked-segment trace construction of row 667 §8, checked at row 671. For a segment reading $|H|\le1$ with $s\ge1$, its marked vacuum-normalized transfer $J_H$ satisfies $|J_H(x,y)|\le A_\beta^s(x,y)$ on Haar space by the positive path integral. Thus $\|J_H\|\le1$, since $|J_H f|\le A_\beta^s|f|$ and $\|A_\beta^s\|=1$. For $s=0$ use multiplication by $H$. Its stationary expectation is $\operatorname{Tr}(\Pi J_H)$ with $\Pi=|\Omega\rangle\langle\Omega|$. The ring expectation is $\operatorname{Tr}(A_\beta^M J_H)/(1+G(M+s))$. As $\|A_\beta^M-\Pi\|_1=G(M)$, the difference is bounded by $G(M)+G(M+s)\le2G(M)$. Replacing three independent draws therefore costs at most $6G(M)$ times the sup norm of their joint reading, by replacing them one at a time. In the first term of (20) this norm is at most $4B_n$. Replacing the centering mean costs at most $2B_nG(M)\cdot4$. The two remaining expectations cost at most $8\kappa G(M)$. This proves the first inequality in (19).

Each $r_i^t\le G(t)\le1/2$, so $G(M)\le2^{1-M/t}G(t)$ and each excited $m_i\ge(\log2)/t$. Then $\bar E_t\ge 2(\log2)G(t)/(3t)$, which proves the second inequality. For a desired tolerance $\eta\bar E_t$, take
$$
 M=\Big\lceil t\max\!\left\{1,\log_2\!\frac{3t(32B_n+8\kappa)}
                                              {\eta\log2}\right\}\Big\rceil .
$$
For bounded rates this adds $O(t[1+\log(nt/\eta)])$ steps for $0<\eta\le1$. This bound prices any bounded event reading, even if the excited-state occupation is very small. The full $D_{j_k}$ in (15) can have a box-dependent sup norm. Equation (19) alone gives no cutoff-independent relative estimate for that weighted negative part. $\square$

**PROVED (an explicit operator bound at late cutoffs).** The insertion also obeys
$$
 \|E_{\ge m} S_k\|_{\rm op},\quad\|S_k E_{\ge m}\|_{\rm op}
                 \ \le\ (24n^3+\kappa/2)e^{-km}.                            \tag{21}
$$
Indeed, on $L^2(\pi)$ the kernel $(a-\bar a)p_2$ acts in absolute value by at most $B_n P^2$ on absolute values. Its compression by $Q$ has norm at most $B_n$. The duration correction has norm at most $2\kappa\max_{0\le v\le1}v(1-v)=\kappa/2$. Apply the two $P^k$ factors in (16). In particular for $k\ge1,\ p>0$, taking $km\ge(3+p)\log n+\log(24+\kappa/2)$ bounds either error in (21) by $n^{-p}$, independently of coupling and cutoff. This controls normalized matrix elements. The dimension of a high-energy subspace and the pointwise signs still matter when using (21) in a thermal sum.


**PROVED (a finite-period comparison for the full inequality).** There is also a more expensive replacement for the prediction weights in (15). It yields a sign test involving **only finite periodic Wilson laws**, with a prescribed loss in the rate. For $s=j_k,j_k+1$ let $J_s^M$ be the joint law of the two ends of an $s$-step segment in a neutral ring of period $M+s$, and let $\widehat\pi$ be the one-slice law in the ring of period $M$. Form $\widehat p_s=dJ_s^M/d(\widehat\pi\otimes\widehat\pi)$. In (3) replace $p_s,\pi$ by $\widehat p_s,\widehat\pi$, including inside the cell integrals, to obtain $\widehat L_s,\widehat D_s$. The formulas integrate densities and hence do not require $\widehat p_s$ to have constant row sum. Write
$$
 \mathcal M=\int L_{j_k+1}\,d\mu_{k,+}-\int D_{j_k}\,d\mu_{k,-}.
$$
Define $\widehat{\mathcal M}$ by the same expression with all three measures or readings hatted, using the Jordan parts of $\widehat\mu_{k,M}$. Put $C=e^{36\beta n^3}$, $\eta>0$. On the cold collar choose the integer
$$
 M=2+\left\lceil t\max\left\{1,\log_2(32C),
          \log_2\!\frac{30000\,C^3(B_n+\kappa)t}{\eta\log 2}\right\}\right\rceil .
                                                                            \tag{22}
$$
Then $|\widehat{\mathcal M}-\mathcal M|\le\eta\bar E_t$. In particular $\widehat{\mathcal M}\ge0$ implies $\partial_\beta X/t\ge(\kappa-\eta/4)\bar E_t$. To test a prescribed characteristic speed use trial rate equal to that speed plus $\eta/4$ in (2), keeping the times and buffers on the desired characteristic. The longest period used by the complete sign test is $M+\max(h,j_k+1)$. Its measurements and its choice of periods use finite Wilson fields and specified constants.

*Proof.* In the shifted convention $d=e^{-12\beta n^3}\le K_1\le1$, also after gauge and centre averaging. The vacuum equation gives $d\le\lambda\le1$ (or test the constant and bound the norm), and $\min\Omega/\max\Omega\ge d$. Haar normalization then gives $d\le\Omega\le d^{-1}$. Thus $0<p_1\le d^{-3}=C$. The same upper bound holds for every $p_s,\ s\ge1$, by the Markov property. With $r_1$ the largest excited multiplier, set $\delta=C r_1^{M-2}$. Pairing $p_1(x,\cdot)-1$ and $p_1(y,\cdot)-1$ through $P^{M-2}$ on mean-zero functions gives $|p_M(x,y)-1|\le\delta$ because each squared norm, $p_2(x,x)-1$ or $p_2(y,y)-1$, is at most $C$. In particular $G(M)=\int(p_M(x,x)-1)d\pi\le\delta$. Coldness and (22) give $\delta\le1/32$.

Closing the observed segment gives exactly
$$
 \frac{d\widehat\pi}{d\pi}(x)=\frac{p_M(x,x)}{1+G(M)}=:v(x),\qquad
 \frac{\widehat p_s(x,y)}{p_s(x,y)}
     =\frac{p_M(y,x)}{(1+G(M+s))v(x)v(y)} .
$$
This is cancellation of the Perron factors around the ring, as in the segment gluing of row 1173, checked at row 1174. Since $|\log p_M|\le2\delta$ and $0\le\log(1+G(M+s))\le\delta$, $|\log v|\le3\delta$, $|\log(\widehat p_s/p_s)|\le9\delta$. For $|z|\le9/32$, $|e^z-1|\le2|z|$. Hence $\widehat p_s\le2C,\ |\widehat p_s-p_s|\le18C\delta,\ |v-1|\le6\delta$. Within any positive cell the conditional density ratio $v/\mathbb E_\pi[v\mid C_{\rm cell}]$ has absolute log at most $6\delta$. This controls cells of arbitrarily small mass.

The difference of the two row densities in (3) changes by at most $36C\delta$. Its cell mean changes by at most $60C\delta$, including the change of conditional probability at cost $2C\cdot12\delta$. The old and new differences or cell means are bounded by $2C,4C$, respectively. In their squared means, taking the difference of squares costs at most $360C^2\delta$. Reweighting the last integral by $v$ costs at most $96C^2\delta$. Thus each prediction weight changes uniformly by at most $500C^2\delta$.

The variation norm of $\widehat\mu_{k,M}$ is at most $4B_n+4\kappa$ by its defining (20). Replacing either Jordan part by the corresponding part of $\mu_k$ costs at most the variation bound of (19), since the positive-part and negative-part functions on signed densities are each 1-Lipschitz. The old prediction weights are at most $4C^2$. Combining these bounds and $G(M)\le\delta$ gives $|\widehat{\mathcal M}-\mathcal M|\le10000 C^2(B_n+\kappa)\delta$. Finally $r_1^{M-2}\le G(t)2^{1-(M-2)/t}$, which gives the claimed error using (22) and the energy estimate after (20). If the finite sign test passes then (8), (10), (16) give $4Z(t)\partial_\beta X/t\ge4\kappa Z(t)\bar E_t-\eta\bar E_t$. Use $Z(t)\ge1$. $\square$

**ARGUED (cost and remaining test).** At bounded rates and polynomial $t$, (19) uses a complement of order $t\log(nt/\eta)$ for the signed event masses. The sup-norm replacement of all prediction densities in (22) costs order $t[\beta n^3+1+\log(nt/\eta)]$ for $0<\eta\le1$. These are finite-volume integrals on continuous link groups. No numerical quadrature is used as evidence. What remains is a lower bound for the signed surplus on the actual Wilson field law, for example by (12), (13) and (20) on the buffered segment. The truncation controls the accuracy with which the question can be posed and supplies neither sign nor size for that surplus.

RESULT (d) — a first component for thermal VIR-DOWN, proved by hand.
PROVED on finite SU(2) Wilson boxes. The centered two-step action (5), conditioned between longer slabs, gives the real-time implication (15)–(16). Equations (19) and (22) replace its inputs by finite periodic laws with a prescribed error or rate loss.
PROVED that both signed contributions and the within-cell cost are strictly positive on Wilson boxes. In the four-state family the test proves rate $8/3$ uniformly over a window of integrated speed $\log512$ with a hidden zero-slope level.
PROVED that exchanging the observed and hidden modes preserves every purity and defeats the test. The free photon fails it at every positive rate and the compact Gaussian model fails it for $\kappa\ge1/\beta$.
The domination of the complete negative contribution by the positive coarse-loop contribution in (15) is GUESSED on the SU(2) band. Its Wilson sign and size, an unconditional weak-5D failure, HOT, (PUR-io) and the mass gap are open. No Lean or numerical calculation was used.
