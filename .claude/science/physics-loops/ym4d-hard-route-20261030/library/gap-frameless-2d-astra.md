## Repo search

**GUIDE — Prior work.** At lane commit `f45a63d76`, the closest hit is Claude Fable’s G8 in row 876. It proposed that equal curved faces could select the two centre spins and stabilize Ising order. Row 1011, Lemma EMB(b) and lines 432, 599–602, identifies the conditional layer and explicitly leaves the positive-temperature proof open. Row 1013 treats a three-dimensional ordered slab and the C7–C9 frame proposals. The corrected results of rows 1016/1018 and 1128 leave field-dependent transport open. Rows 1072–1078 concern an anisotropic face and a shrinking finite-cylinder perturbative interval. Durhuus and Fröhlich had already questioned the normalized comparison and exhibited the warning in a Gaussian limit (§§3, 7 of their original manuscript). The proofs below concern the compact spin measure itself. [Row 876, G8](gap-brainstorm2-max.md) · [Row 1011, Lemma EMB](gap-pinned-cell-gauge-max.md)

**GUIDE — Search scope.** The lead’s November 8 digest covers thirteen earlier existence-chain topics. There is no row-specific prior file. A fresh search of the YM4D proof, research and hard-route library paths on main `8b11ae2bb` and PRs 10114 `f76f6c649`, 10133 `89faef229`, 10134 `1e70c7211` and 10141 `a2f6a430e` found MATCHA’s pinned-cell density jets on 10114/10133. MATCHA_LOG lines 34–45 and FINITE_COUPLING_KERNEL_ASTRA lines 12–34 concern fine-link kernels. The other three refs gave no hit for the searched pinned-cell, two-sided background, Durhuus, frustration and easy-axis terms in those paths. Row 1011 §8 also records Balaban background-field hits on main. The open registry’s T-step layer and two-sided stratum boundary concern other objects.

<details>
<summary>Outline and account checks, and the saved work plan</summary>

**GUIDE — Source scope.** I checked outline index chunks 01 and 08 with neighbouring rows, the obligations, and the CA-I 4.12–4.19 index. Outline Theorem 0 concerns the curvature-squared sector (66–73, 118–131). Lines 588–599 distinguish clustering from spectral interval exclusion. Lines 8735–8748 and 8762–8770 concern a constrained classical precision with flat holonomies. CA-I 2699–2712 gives the narrower Hamiltonian assertion. CA-I 49495–49504 concerns admission of backgrounds for a free-current theorem. None supplies a nonlinear two-sided spin estimate. Credit for both texts at `31a47c543775` belongs to Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. Balaban is the source of their background-field method.

GUIDE — Plan for FINISH row 1139.

1. Check the recorded repository search, source revisions and ownership.
2. Trace the target, the frame obstruction and the published hypotheses to their sources.
3. Test a background that leaves a discrete spin symmetry and seek a proof of long-range dependence.
4. Check the rotation and diamagnetic arguments against the model and a finite graph.
5. Determine the layer-comparison and four-dimensional consequences.
6. Verify the proof, scope and credits, and record the result.

</details>

## Target, model and published input

**OPEN — Target and wall.** Arthur Jaffe and Edward Witten’s target for pure SU(2) is a nontrivial quantum Yang–Mills theory on four-dimensional Euclidean space, satisfying the Wightman axioms, or Euclidean axioms sufficient for their reconstruction, with $\operatorname{spec}H\cap(0,\Delta)=\varnothing$ for some physical $\Delta>0$. The lane's wall (W) asks for one physical box, along the cutoff trajectory, where the box size times its lowest transfer gap, in the cutoff limit, exceeds a fixed multiple of the excess free energy plus a safety margin. This would supply the finite-box seed for decay on larger boxes. In the repaired notation of `parts/gap.md` lines 14–43, there must be a bound $(L_0,D_0)$ for (BDD-Delta) and an admissible $L\ge4L_0$ with $z^-(L)>256D_0+30$. The weak-coupling argument loses control before that box. A two-dimensional spin proof can still distinguish a noncommuting group there because its common left rotations generate a current bracket. In the gauge problem the local colour axes must themselves be transported through the intervening fields. Testing that missing step on a single layer is the purpose of this row.

**GUIDE — Conventions.** Use probability Haar measure on $S^3=\mathrm{SU}(2)$, with $u\cdot v=\operatorname{Re}(u\bar v)$ and real unit quaternion $1$. Orient each unoriented edge once, put $R_{yx}=R_{xy}^{-1}$, and give a spin configuration density proportional to

$$
 \exp\!\left(b\sum_{xy}s_x\cdot R_{xy}s_y+\sum_x h_x\cdot s_x\right).
$$

Pins specify boundary spins. A uniform mixing estimate must, in particular, control the covariances of one-site unit linear functions. At zero field on a free or periodic graph, simultaneous negation makes the one-point functions vanish.

**GUIDE — OpenAI's hypothesis.** In *Sharp mass bounds for the two-dimensional O(4) model*, pp. 12–14, 25 (commit `4eaee8754`), the pinned cell permits fixed **right** twists in $q_y U_e q_x^{-1}$. A common left rotation conjugates this entire quaternion. Its real part is unchanged, and differentiating the imaginary part gives the bracket in (3.7)–(3.8). The short step (3.52) gains a positive constant times the minimum of the response parameter and one. The full covariance bound of Theorem 3.1 is stated for nonnegative untwisted bonds on unpinned free subgraphs and sufficiently large tori, with length $\exp(\pi b+C\sqrt{(1+b)\log(2+b)})$. The earlier OpenAI and Ding–Huang–Yang untwisted results and the local/global distinction are recorded in rows 1007 and 1009. I use none of these mass estimates to prove the counterexample. [OpenAI paper, §3](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Sharp-mass-bounds-for-the-two-dimensional-O4-model-September-23-2026/paper.pdf)

**PROVED — Admissibility for the gauge layer.** With horizontal links fixed to $u_{xy},v_{xy}$ on the two faces, the mixed plaquette contributes $\operatorname{Re}(\bar q_x u_{xy} q_y v_{xy}^{-1})$, up to the orientation convention. Thus $R_{xy}q=u_{xy}qv_{xy}^{-1}$. In particular, equal faces give quaternion conjugations. All examples below have equal faces and zero imposed site fields. This is the specialization of row 1011, Lemma EMB(b), and of the Durhuus–Fröhlich slab law that the proof uses.

## A curved background with order at positive temperature

**PROVED — Counterexample (C).** The period-four background of quaternion conjugations constructed below has a finite $b_*$ such that both statements hold at zero field for every fixed $b\ge b_*$.

- On all sufficiently large square tori of side $2M$, with $M$ a power of two, both the connected real-component correlation and the full spin dot correlation exceed $1/2$ at **every** pair of even-coordinate sites. Their separation can grow proportionally to $M$.
- On ordinary squares with boundary pins, changing only the boundary can change the mean real component at the centre by at least one, uniformly in the radius. For some fixed pins on each square of radius $r\ge2$, two one-site linear tests at distance $r-1$ have connected correlation of magnitude at least $1/[4\pi b(2r-1)]$.

**PROVED — Tile and ground states.** In the tile $Q=\{0,1,2\}^2$, put $A=\operatorname{Ad}_{(1+i)/\sqrt2}$ and $B=\operatorname{Ad}_{(1+j)/\sqrt2}$ on the two consecutive top horizontal bonds, respectively. On imaginary quaternions these are quarter turns about $i$ and $j$. In particular $AB(i)=j$ and $BA(i)=-k$. All other bonds are the identity. Extend by reflecting the tile in its sides. Equivalently, fold each integer coordinate modulo four by the list $0,1,2,1$ and pull back the template transport on the resulting oriented bond. The reverses are the inverses. This defines every edge, including shared sides, and admits reflection through every line of even lattice coordinate. Use one such tile per coarse square. Its energy is

$$
 E_Q=\sum_{e=xy\subset Q}w_e(1-s_x\cdot R_{xy}s_y)
     =\tfrac12\sum_{e=xy\subset Q}w_e|s_x-R_{xy}s_y|^2 ,
$$

where $w_e=1/2$ on the perimeter and $1$ elsewhere. These energies sum to the ordinary unit-bond energy on a tiled torus. The identity bonds connect all nine sites. Zero tile energy therefore means a common spin fixed by $A$ and $B$. Their fixed planes are $\operatorname{span}(1,i)$ and $\operatorname{span}(1,j)$. The only zero-energy tile configurations are the constants $+1,-1$. Every bond is satisfied in either one. More generally, any fixed angle $0<\theta<\pi$ about each of these two axes gives the same two zeros. The contour and pin estimates below then apply with their own $b_*(\theta)$.

**PROVED — Local cost.** Write $U_\pm=\{q:|q\mp1|<1/4\}$. A tile is bad if its nine spins do not all belong to the same one of these caps. This closed set is compact and misses both energy zeros, so its minimum energy $\delta$ is strictly positive. The same $\delta$ applies to each reflected tile. Set

$$
 \rho=\min\{1/8,\sqrt{\delta/32}\},\qquad
 a=\sigma\{|q-1|<\rho\},\qquad
 b_*=\frac{2}{\delta}\big(4\log(1/a)+20\log 2\big).
$$

Here $\sigma$ is Haar probability and $a>0$ because the cap is open. All constants are fixed on a single tile. There are $M^2$ tiles, $4M^2$ sites and $8M^2$ edges on the torus. Restricting every spin to the $\rho$-cap about $1$ costs Haar probability $a^{4M^2}$. On that event each edge has energy at most $2\rho^2$ since its rotation fixes $1$. Thus the partition function in the energy convention is at least $a^{4M^2}\exp(-16b\rho^2M^2)$. The all-bad integral is at most $\exp(-b\delta M^2)$. Dividing and using $16\rho^2\le\delta/2$ gives

$$
 \mathbb P(\text{all tiles bad})^{1/M^2}
 \le a^{-4}\exp(-b\delta/2)=:p.
$$

In particular $p\le2^{-20}$ for the asserted range. The bound is independent of $M$.

**PROVED — Reflections and arbitrary sets of bad tiles.** We use a chessboard estimate in the sense of Fröhlich, Israel, Lieb and Simon. For any set $S$ of coarse squares,

$$
             \mathbb P(\text{all tiles in }S\text{ bad})\le p^{|S|}. \qquad(1)
$$

Denote the probability on the left by $P(S)$, and the set of all tiles by $V$. A reflection through a tile side and the parallel opposite seam divides the torus into halves. Given the seam spins, the two interiors are independent and have reflected laws. Each half's event uses only its interior and the seams. Thus Cauchy–Schwarz for the two conditional probabilities on the seams gives $P(S)^2\le P(S_+)P(S_-)$, where $S_\pm$ copies the corresponding marked half into the other half by reflection. The two sizes sum to $2|S|$. This uses site reflections and permits the boundary spins shared between tiles.

All $P(S)$ are positive, since all spins in a small cap near $i$ make every tile bad. Maximize

$$
 D(S)=\log P(S)-\frac{|S|}{|V|}\log P(V).
$$

If its maximum were positive, a maximizer would contain a marked tile. Both reflected copies of a maximizer also maximize $D$, by the preceding inequality and the size identity. Keep the half containing the marked tile, reflecting in an end of its marked interval of columns. An interval of length $k\le M/2$ then supplies $2k$ consecutive marked tiles in that row. Doubling to a full row and doing the same with rows gives $V$, since $M$ is dyadic. But $D(V)=0$. This proves (1).

**PROVED — Peierls contours.** Put $\tau_x=\operatorname{sign}\operatorname{Re}s_x$ at the coarse vertices (even coordinates). A tie has probability zero by absolute continuity. Draw a dual edge across each coarse edge where the signs differ. Every dual vertex has even degree, by going once around the four signs of its tile. The dual edges thus decompose into edge-disjoint simple cycles, by removing a simple cycle until no edges remain. Every vertex on one of these cycles is a distinct bad tile of that cycle, since two of its corner signs differ. A specified simple cycle of length $n$ therefore has probability at most $p^n$ of occurring by (1).

There are at most $M^2 4^n$ possible rooted walks of length $n$. The probability of any simple contour of length at least $M/2$ is at most $M^2(4p)^{\lceil M/2\rceil}/(1-4p)$. Shorter simple cycles lift to simple plane polygons contained in a box of span less than $M/2$. Their bounded interiors project to disks. If the signs of $x,y$ differ, a coarse path between them crosses an odd number of drawn dual edges. If all cycles are short, at least one of these disks contains exactly one of $x,y$, by crossing parity for a simple polygon. For a short $n$-cycle enclosing a specified site, a lift of a starting dual vertex lies within coordinate distance $n+1$ of that site, by the polygon's bounding rectangle. This gives at most $(2n+3)^2 4^n$ choices. The counts use (1) for each specified cycle and a union bound over possible cycles.

For either endpoint, failure to lie in either cap makes any incident tile bad, with probability at most $p$. Hence the probability that $x,y$ fail to be in the same cap is at most

$$
 2p+2\sum_{n\ge4}(2n+3)^2(4p)^n
       +\frac{M^2(4p)^{\lceil M/2\rceil}}{1-4p}. \qquad(2)
$$

For $n\ge4$, $(2n+3)^2\le4^{n+1}$, so the middle term is at most $8(16p)^4/(1-16p)$. With $p\le2^{-20}$ the first two terms sum to less than $1/16$, and the last term tends to zero. On the same-cap event both $(\operatorname{Re}s_x)(\operatorname{Re}s_y)$ and $s_x\cdot s_y$ exceed $7/8$ (use $|s_x-s_y|<1/2$ and $|\operatorname{Re}s_x|>31/32$). Elsewhere they are at least $-1$. Once (2) is below $1/8$, both expectations are at least $(7/8)^2-1/8=41/64>1/2$. Simultaneous negation centers every coordinate. The same dot bound holds with parallel transport inserted along any path of this background, since every transport preserves each cap.

**PROVED — Infinite-volume form.** Extend the torus configurations periodically to the plane and take a weakly convergent subsequence. Such a subsequence exists by compactness of the countable product of spin spheres and compactness of its probability measures. Local continuous tests keep their limiting means. For any fixed square its conditional Gibbs kernel is continuous in the boundary spins by the finite-integral formula. For fixed local tests the conditioning identity agrees with that on the torus once the square and test supports fit without wrapping. Passing this integrated identity against exterior cylinder tests gives a Gibbs state on the plane. In this spin-flip-symmetric state the lower bound $1/2$ holds simultaneously for all pairs of even-coordinate sites. Decay within an individual extremal phase is a separate question.

**PROVED — Ordinary boxes and fixed pins.** In such a torus take $x=0$, the boundary ring of $[-r,r]^2$, and an even-coordinate $y$ strictly outside it. Choose the torus much larger than $r$. Conditional on ring spins $\eta$, interior spins are independent of the exterior by factorization of nearest-neighbour weights. Write $m(\eta)=\mathbb E_\eta\operatorname{Re}s_0$. The torus correlation bound and $|\operatorname{Re}s_y|\le1$ give $\max_\eta |m(\eta)|\ge1/2$. The maximum exists by continuity of the finite integrals. Since $m(-\eta)=-m(\eta)$, these two pins differ in centre mean by at least one.

Join each boundary value to its negative by a length-$\pi$, constant-speed great semicircle on $0\le t\le1$. Differentiate $m$ under the finite integral. Bonds between pins cancel in the normalized derivative. Each of the $4(2r-1)$ bonds $zw$ from a free site $z$ to a pinned site $w$ contributes

$$
 b\,\operatorname{Cov}_{\eta(t)}
       (\operatorname{Re}s_0,\ s_z\cdot R_{zw}\dot\eta_w(t)).
$$

Every such $z$ has distance at least $r-1$ from the centre (exactly $r-1$ in the maximum norm). Each transported velocity has length $\pi$. Integrating and bounding the sum by its largest absolute term proves the claimed covariance lower bound for some fixed pins, site and unit linear test. Thus even on ordinary squares a positive background- and pin-uniform exponential rate is impossible. The torus statement already gives a nondecaying normalized scalar correlation with zero fields and no fixed pins.

## Two tests of proposed replacements for the common rotation

**PROVED — Cost of a moving left axis.** For the oriented bond $T_e=u_{xy}q_yv_{xy}^{-1}q_x^{-1}$, a left change $q_z\mapsto e^{t f_z n_z}q_z$ sends it to

$$
 e^{t f_y\operatorname{Ad}_{u_{xy}}n_y}\,T_e\,e^{-t f_x n_x}.
$$

For a nonzero constant $f$, the two generators agree only when the axis is parallel across that bond. This is where using the ordinary gradient in OpenAI (3.6) loses its justification. Consider the two upper plaquettes of the template, both based at the common top vertex $z=(1,2)$. Orient each loop so its holonomy on imaginary quaternions is $A$ or $B$, respectively. A unit imaginary direction $n_z=n_i i+n_j j+n_k k$ obeys

$$
 |(1-A)n_z|^2+|(1-B)n_z|^2=2(n_i^2+n_j^2+2n_k^2)\ge2 .
$$

For any assignment of imaginary unit velocities $n_x$, telescope around each plaquette, transporting each bond difference $D_e n=n_x-R_{xy}n_y$ to its base. Cauchy–Schwarz on its four sides and the fact that an edge occurs at most twice give

$$
 2\le 8\sum_{e\subset Q}|D_e n|^2,\qquad
 \sum_{e\subset Q}w_e|D_e n|^2\ge1/8. \qquad(3)
$$

At the aligned ground configuration $q_x=1$, a differentiable spin deformation with velocities $n_x$ has second derivative of $bE_Q$ equal to $b\sum w_e|D_e n|^2$. This follows by differentiating the squared bond differences at zero. The velocities may be chosen from the entire spin configuration. Stationarity at the minimum makes this Hessian depend only on the velocities. A unit plateau therefore costs at least $b/8$ per interior tile in the direct energy, even for a frame chosen from the spins. In OpenAI (3.6) the interior of a constant profile costs zero. This is the local content of FR/HOL on this example.

**PROVED — Scope of (3).** Equation (3) concerns the direct energy at the indicated configuration. A spin-dependent change of variables can contribute a Jacobian, and the free-energy Hessian also contains a current covariance. The fixed-temperature correlation lower bound following (2) rules out any control of these terms by the bracket gain *sufficient to imply uniform mixing over this class*. The balance after averaging over dynamical faces remains OPEN. Here curvature penalizes all three transverse directions while leaving both real poles bondwise satisfied. Its effect is to stabilize a discrete order parameter.

**PROVED — Finite-graph failure of diamagnetic domination.** The proposed O(4) extension of the Ising and planar Ginibre comparisons fails even at zero field. Take the two unit squares with vertex sets $\{0,1\}^2$ and $\{2,3\}\times\{1,2\}$, joined by the single edge from $x=(1,1)$ to $y=(2,1)$. On each square choose one edge incident to its bridge endpoint and put $Hq=iqi^{-1}$ on it. Set all other transports, including the bridge, to $I$. All spins are free and all fields zero. For this graph, at every uniform $0<b\le\sqrt{8}$,

$$
 \mathbb E_R[s_x\cdot s_y]>\mathbb E_I[s_x\cdot s_y]>0. \qquad(4)
$$

The comparison is of normalized Gibbs expectations of the **full dot product**, transported along the identity bridge. Negation symmetry gives the same statement for the connected function. It also disproves the corresponding bound with an absolute value on the left.

**PROVED — Endpoint weights.** Write $K_b(u,v)=\exp(bu\cdot v)$, with kernel powers composed using Haar probability. Integrating the three nonroot spins of a square gives $K_b^4(u,Hu)$ at its root. Normalize this function to have integral one and call it $f$. It is even. For the flat square the normalized function is $1$ by rotation invariance. To see the twisted one is nonconstant, observe that $K_b^2(u,z)=\int\exp(b(u+z)\cdot w)\,d\sigma(w)$ increases strictly with $|u+z|$ for $b>0$, by pairing $w,-w$ and using strict increase of cosh. Rotation invariance gives

$$
 K_b^4(u,u)-K_b^4(u,-u)
 =\tfrac12\int[K_b^2(u,z)-K_b^2(-u,z)]^2\,d\sigma(z)>0 .
$$

Since $H1=1$ and $Hj=-j$, this distinguishes the root weights at $1$ and $j$.

**PROVED — Normalization on the bridge.** Temporarily vary just the bridge coupling $t$, holding $b$ and the decorations fixed. Set $Z_f(t)=\iint f(u)f(v)e^{tu\cdot v}\,d\sigma(u)d\sigma(v)$ and $C_0(t)=Z'_1(t)/Z_1(t)$. The bridge expectation is $Z'_f/Z_f$. With $g=f-1$, the terms linear in $g$ vanish by rotation invariance and $\int g=0$. The absolutely convergent exponential series gives

$$
 Z_f(t)-Z_1(t)=\sum_{\substack{k\ge2\\ k\ {\rm even}}}\frac{t^k}{k!}a_k,
 \qquad a_k=\left\|\int g(u)u^{\otimes k}\,d\sigma(u)\right\|^2 .
$$

At least one $a_k>0$. Otherwise $g$ integrates to zero against every polynomial. The square integral defining $f$ is a uniform limit of polynomials in the root, since its two incident bonds enter as $\exp(bu\cdot v')$ with $|v'|\le2$, whose Taylor series is uniform. Thus $\int g^2=0$, contradicting the two different root values and continuity.

The flat relative coordinate $z=u\cdot v$ has density proportional to $\sqrt{1-z^2}$ on $(-1,1)$, by spherical coordinates on $S^3$. Integrating the derivative of $e^{tz}(1-z^2)^{3/2}$ gives $3C_0(t)=t(1-\mathbb E_t z^2)$. At $t>0$, $\mathbb E_t z^2>1/4$. Indeed the untilted second moment is $1/4$ by symmetry, and tilting an even observable reweights $|z|$ by the strictly increasing $\cosh(t|z|)$. Its covariance with $z^2$ is positive by taking two independent copies and multiplying their differences. Thus $0<C_0(t)<t/4$, with positivity also following by pairing $z,-z$. For $0<t\le\sqrt8$, each nonzero term in the following identity is strictly positive.

$$
 Z'_f(t)-C_0(t)Z_f(t)
 =\sum_{\substack{k\ge2\\ k\ {\rm even}}}
   \frac{t^k}{k!}a_k\big(k/t-C_0(t)\big)>0.
$$

Set $t=b$ and divide by $Z_f(b)>0$. This proves (4), including for $23/10\le b\le26/10$. A single enhanced correlation in that interval settles the comparison inequality there. Long-distance mixing over the two-sided class at those couplings remains OPEN.

## What the layer comparison actually consumes

**GUIDE — Original hypotheses.** Bergfinn Durhuus and Jürg Fröhlich, *A connection between $\nu$-dimensional Yang–Mills theory and $(\nu-1)$-dimensional, non-linear $\sigma$-models*, CMP **75** (1980), 103–151. In their IHÉS manuscript, printed pp. 16–18, (1.35) bounds the absolute expectation of a product of one inverse and one direct representation-matrix entry at separation $j$ by $e^{-V(j)}$, where $V(j)\to\infty$ with $|j|$, uniformly over both external face fields in the thermodynamic limit. Theorem 1.2 requires boundary conditions with nonnegative slab partition-function ratios. Free and periodic conditions occur in Theorem 1.1, and the real Wilson Boltzmann weights here are strictly positive. Linear growth of $V(j)$ gives a linearly confining static potential. Theorem 1.3 uses a faithful action character and a representation nontrivial on the centre for universal one-point vanishing. Here the fundamental SU(2) character is faithful, and changing all spins by the central $-1$ centers every entry in a finite unpinned, zero-field layer and its periodic limits. Their Theorem 1.1(1) bounds a **partition-function ratio** by one. Their separate discussion on printed p. 39 asks about normalized character two-point functions and points to a Gaussian example on printed p. 72. Equation (4) tests that character comparison on the compact model, since $\tfrac12\operatorname{ReTr}(q_xq_y^{-1})=s_x\cdot s_y$. [Original IHÉS manuscript, pp. 12, 16–18, 39, 72](https://repo-archives.ihes.fr/FONDS_IHES/I_Prepublications/FROHLICH/1978-1980/P_79_302/P_79_302_web.pdf) · [Journal article](https://doi.org/10.1007/BF01222514)

**GUIDE — Finite-volume formulation.** Cao, Nissim and Sheffield, §2, Definition 2.1, Remark 2.2 and Theorem 2.3, formulate the sufficient condition as exponential covariance decay of these matrix entries on periodic slices with constants independent of size and of both backgrounds. Their larger class of $\mathrm U(N)$-valued face fields serves an extension to $\mathrm U(N)$. Group-valued face fields suffice for pure $\mathrm{SU}(N)$ by their Remark 2.2. The Wilson coefficient of $\operatorname{ReTr} U_p/2$ equals the $b$ of its layer, or $4\beta$ in their $N\beta\operatorname{ReTr} U_p$ convention. [Cao–Nissim–Sheffield, pp. 3–4](https://arxiv.org/pdf/2509.04688v2#page=3)

**PROVED — Conditional area rate.** Use the SU(2) quaternion slab inequality of the lane’s area-law note, §4.2, Lemma R. Condition the three-dimensional Wilson law on all horizontal bonds. Distinct height-one slabs are then independent. A rectangle of width $R$ and height $T$ uses $T$ distinct slabs if it does not wrap in height. In a periodic cube take $R,T$ at most half the side, so within each horizontal slice the two vertical lines are distance $R$ apart. The two horizontal edge products are fixed unit quaternions. Between them the conditional mean loop is the matrix element of the product, in slab order, of the mean maps $S_k:X\mapsto\bar q_{x,k}Xq_{y,k}$. For unit quaternions $X,Y$,

$$
 \langle Y,S_k X\rangle=\langle q_{x,k}Y,Xq_{y,k}\rangle
       =q_{x,k}\cdot O_{X,Y}q_{y,k},\qquad O_{X,Y}\in\mathrm{SO}(4).
$$

Thus if every unit real linear two-point covariance is bounded by $C e^{-mR}$ on the actual zero-field, unpinned two-sided layers, the four coordinate terms and center symmetry give $\|\mathbb E S_k\|\le4C e^{-mR}$. Taking norms of the product and interchanging the coordinate directions yields

$$
 |\langle W(R,T)\rangle|\le K^{\min(R,T)}e^{-mRT},
 \qquad K=\max(1,4C),\quad W=\tfrac12\operatorname{ReTr} U_{\rm loop}. \qquad(5)
$$

If $\max(R,T)\ge 2\log K/m$, this is at most $e^{-mRT/2}$. For both sides smaller, the trivial bound $1$ is absorbed in a $b$-dependent prefactor. This is an area law uniform in the volume at the covered coupling, and hence in periodic thermodynamic limits. It also applies directly to free boxes if the input holds on free rectangular layers. The entry hypothesis controls the contractions with both horizontal end products. [Lane proof of Lemma R](gap-arealaw-opus.md) · [Research check of the matrix order](gap-arealaw-check-astra.md)

**PROVED — If (P) is supplied only with Dirichlet pins.** On an unpinned square torus of side $L$, take the periodic maximum-norm separation $2\le R\le L/2$ and surround $x$ by the square ring of radius $r=R-1$. Its interior does not meet $y$ and, given the ring, has the ordinary pinned-box law. Under a hypothesized pin-uniform bound $Ce^{-md}$ for pairs of unit linear tests, the same interpolation from $\eta$ to $-\eta$ as above bounds the absolute one-site mean of every unit linear test by $\tfrac12\pi b\,4(2r-1) C e^{-m(r-1)}$. Integrate against the exterior test at $y$, of absolute value at most one. This gives the periodic layer hypothesis with exponent, for example, $m/2$, after changing $C$. Bounded separations are covered by increasing $C$. This checks the boundary-condition change needed in using (5).

**PROVED — The counterexample hits the charged hypothesis.** Here $\operatorname{Re}s_x=\operatorname{Tr}q_x/2$ and $\operatorname{Re}s_y=\operatorname{Tr}q_y^{-1}/2$. Their torus covariance is the average of four diagonal-entry cross-covariances of exactly the kind the slab comparison reads. At least one has magnitude above $1/2$ at arbitrarily large separation. The strict finite-torus inequality persists on a neighbourhood of the two prescribed faces by continuity of normalized compact integrals. Such neighbourhoods have positive finite-volume Wilson probability because the density is positive. Thus a uniform exponential estimate also fails if the supremum over the faces is an essential supremum. The probabilities of the neighbourhoods as the volume grows are uncontrolled by this estimate.

**OPEN — Four dimensions.** At a coupling where (P) held, (5) would concern the fundamental rectangular Wilson loop in *three* dimensions. A fourth direction introduces interlayer influences, and (W) concerns the lowest transfer excitation and a physical-scale finite-size bound. The large-$b$ counterexample rules out the proposed extension of OpenAI’s common-rotation gain at HOL whenever its conclusion is mixing for every conditioning. A cancellation or transport estimate averaged in the actual Wilson measure, or an argument confined to a narrower coupling interval, is still open. The location of the ordering threshold relative to $2.3$–$2.6$ remains open. The three-dimensional area law for the dynamical average and the four-dimensional mass gap are compatible with this counterexample.

**GUIDE — Verification and standing.** The low-temperature estimate uses a single compact tile, reflection Cauchy–Schwarz, contour counting and conditioning. The finite-graph comparison uses positive tensor squares in a normalized bridge integral. Both arguments are analytic. The labels describe the arguments given here. This research row grants no audit status and awaits independent review.

RESULT: PROVED (C) for all $b\ge b_*$ with zero fields and equal curved faces. Normalized O(4) diamagnetic domination fails on eight sites for $0<b\le\sqrt8$. The physical-window mixing bound and four-dimensional (W) remain OPEN.
