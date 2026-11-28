# Repo search

Check 1387 corrects Proposition NEG's inventory. Row 1141 already controls every adjoint section on a growing box. Row 1283 bounds the expected spectral count on a three-dimensional time slice and the annealed off-diagonal Dirichlet Green function in four dimensions. I use their two-plaquette test, Neumann block inequality and rare Dirichlet trial cubes. The new estimate is for a signed loop average in a typical single field on the full spacetime torus. [Row 1141, (2)–(7)](gap-crux2-astra62.md) · [Row 1283, (1)–(5), (8)](gap-solve32-astra62.md) · [Check 1387, §2](gap-mech-direction2-check-astra62.md)

At `27ac80562` there is no task-specific prior. The lead’s 8 November digest found a one-step transfer correlation (PR 10114, `MASS_GAP_LOCAL_BLOCK_ASTRA.md`, 106–161) and a flat constrained minimum (PR 10141, `research/ym4d/library/fp1.md`, 142–168). I checked both and searched main and PRs 10114, 10133, 10134 and 10141 for the adjoint spectral and walk estimates. The main hit was a numerical diluted-graph example (`POSITIVE_PATH.md`, 14007–14019). PRs 10114 and 10133 share a Cartan plane-wave calculation (`REVIEW_FLOW_S10.md`, 354–365) and a fixed-background heat-trace test (`checks/f9_criteria.md`, 50–64). The registry's `O-holonomy` asks for uniform closeness to the centre on admitted renormalization backgrounds. I found no matching result or registry assignment for this probability law. [Lead’s digest](prior/repo-search-2026-11-08.md) · [Registry](open-registry.md) · [CA-I, 107073–107120](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L107073-L107120)

I used the indexed Wilson law and the unitarity estimate of Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, at `31a47c543775`. Their layered random walks in CA-I are at a prescribed background. The estimates below concern a typical field drawn from the ordinary periodic Wilson measure. [Outline, 240–293](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L240-L293) · [Outline, 10978–10982](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L10978-L10982) · [CA-I, 53482–53491](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L53482-L53491)

## Proof plan

Use the two cell estimates to bound the smallest eigenvalue on a typical full torus from both sides. Express a signed average of adjoint Wilson loops through this eigenvalue, then remove every loop of small diameter after its retracings have been erased. Use the same walk and diameter cutoff in both comparison models.

## A signed average of long adjoint Wilson loops

Take the unit-mesh periodic torus $\Lambda_N=(\mathbb Z/N\mathbb Z)^d$. Sample the links $U$ with Wilson density proportional to $\exp(\beta\sum_p \tfrac12\operatorname{Re}\operatorname{tr}U_p)$ relative to product probability Haar. Independently, start a walk $X$ at a uniform vertex. It holds with probability $1/2$ and steps to each nearest neighbour with probability $1/(4d)$. Put

$$
m=N^2,\qquad \rho_N=\lfloor(\log N)^{1/6}\rfloor,\qquad B=\{X_m=X_0\}.
$$

On a closed path erase holds and adjacent inverse steps, then erase inverse first and last steps as long as possible. Let $E$ mean that the remaining cyclically reduced loop has diameter at least $\rho_N$ in the periodic $\ell^\infty$ distance. Give an empty loop diameter zero. Write $H_U(X)$ for the ordered link product, with identity on holds, and $\tau(g)=\operatorname{tr}(\operatorname{Ad}g)/\dim\mathfrak g$. The erasures preserve this character, including a change of root by conjugation. For fixed $U$ the observable is

$$
W_N(U)=\mathbb E_X[\tau(H_U(X))\mid B\cap E].
$$

**Theorem.** For each $p>0$ there are $c,C>0$ and $N_0$ such that for every $N\ge N_0$ and every $\beta\in[2,3]$, with Wilson probability at least $1-N^{-p}$ in four-dimensional SU(2),

$$
\exp[-C N^2 h_4(N)]\ \le\ W_N(U)\ \le\ \exp[-c N^2 h_4(N)],
\qquad h_d(N)=\left(\frac{\log\log N}{\log N}\right)^{2/d}.
\tag{1}
$$

In five-dimensional SU(2) the same construction satisfies (1) with $h_5$. In four-dimensional compact U(1) with its Wilson weight $\exp(\beta\sum_p\cos\theta_p)$, $W_N=1$ for every field. Each comparison violates the four-dimensional SU(2) bounds for large $N$, in probability for SU(2) and identically for U(1). All logs are natural.

## The lowest adjoint eigenvalue on the full torus

Identify $\mathfrak{su}(2)$ with the imaginary quaternions. Define $L_U$ on site fields $s:\Lambda_N\to\mathbb R^3$ by

$$
Q_U(s)=\langle s,L_Us\rangle
=\sum_{x\in\Lambda_N}\sum_{i=1}^d
 |s_x-\operatorname{Ad}(U_{x,i})s_{x+e_i}|^2,
\qquad \lambda(U)=\min_{s\ne0}Q_U(s)/\|s\|_2^2.
$$

Gauge transformations conjugate $L_U$ by a sitewise orthogonal change of basis and conjugate each closed holonomy at its root. Both $\lambda$ and $W_N$ are therefore gauge invariant. Put $F_d(t)=t^{-d/2}\log(1/t)$. For $d\in\{4,5\}$ there are positive $c,C,t_0$ depending only on $d$ such that for $0<t<t_0$ and $N\ge C t^{-1/2}$,

$$
\begin{aligned}
\mathbb P(\lambda\le t)&\le N^d \exp[-cF_d(t)],\\
\mathbb P(\lambda>t)&\le
 \exp\!\left[-cN^d t^{d/2}\exp(-CF_d(t))\right].
\end{aligned}\tag{2}
$$

**Excluding a low mode.** Use the cell construction of rows 1141 and 1283 in all $d$ directions. For any specified $j$ links, their conditional joint density given the other links lies between $e^{-K_d j}$ and $e^{K_d j}$ relative to product Haar, where $K_d=12(d-1)$. At most $2(d-1)j$ plaquette terms change, each trace term has range of length two, and $\beta\le3$. This bounds the ratio of the maximum to the minimum of the weight, hence also the normalized density. [Row 1141, proof of (2)](gap-crux2-astra62.md) · [Row 1283, proof of (1)](gap-solve32-astra62.md) · [Check 1289, step 5](gap-solve32-check-opus.md)

At the centre $x$ of a $3^d$ cell take the northeast and southwest plaquettes in the $12$-plane. Write their based holonomies as $q_1,q_2$ and put $D_x=\min_{|v|=1}\sum_{i=1}^2|v-\operatorname{Ad}(q_i)v|^2$. The row 1283 small-ball estimate here reads

$$
\mathbb P(D_x<u\mid\text{links outside the cell})\le H_d u
\qquad(0<u<1),\qquad H_d=e^{2K_d}.
\tag{3}
$$

Leave one private link of each loop unexposed and fix all the rest. Under their product Haar law the two $q_i$ are independent Haar by left and right invariance and inversion. If $a_i=\operatorname{Im}q_i$, then $|v-\operatorname{Ad}(q_i)v|^2=4|a_i\times v|^2$. Thus $D_x/4$ is the smaller eigenvalue of the $2$-by-$2$ Gram matrix of $a_1,a_2$. On $|a_1|\ge|a_2|$ this gives $D_x\ge 2|a_2\times\widehat a_1|^2$ by determinant over trace, ignoring the Haar-null case $a_1=0$. For a fixed axis the squared length of the two perpendicular components of a uniform unit quaternion is uniform on $[0,1]$. Indeed the surface element of $(\sqrt{s}e^{i\theta},\sqrt{1-s}e^{i\phi})\in S^3$ is $\tfrac12\,ds\,d\theta\,d\phi$. Each ordering contributes at most $u/2$ to the Haar probability. The two-link density bound proves (3), also after averaging any of the exposed links.

Partition each coordinate interval into lengths in $[r,2r]$ by merging its final short remainder, where $r\ge6$. In every resulting rectangle $A$ pack $M\ge |A|/6^d$ disjoint $3^d$ cells. Call the rectangle good if at least $M/2$ of their roots have $D_x\ge u$. On a good rectangle the internal-bond form satisfies

$$
\|s\|_{2,A}^2\le (A_d r^2+B_d/u)\,Q_{U,A}(s).
\tag{4}
$$

Write $\nabla_U s(xy)=s_x-\operatorname{Ad}(U_{xy})s_y$. Telescoping its transports around the two four-edge loops and applying Cauchy–Schwarz gives $u|s_x|^2\le4\sum_{e\text{ in the two loops}}|\nabla_U s(e)|^2$ at each good root. These edges are disjoint between cells. For $f=|s|$ the scalar squared bond differences are bounded by the covariant ones. Its variance sum about its mean $\bar f$ on $A$ is at most $2d r^2 Q_{U,A}(s)$, by replacing one coordinate at a time between two uniform points and applying Cauchy–Schwarz on each interval of length at most $2r$. Average $\bar f^{\,2}\le2(f_x-\bar f)^2+2 f_x^2$ over the good roots. They occupy at least $1/(2\cdot6^d)$ of the sites. Adding back the variance gives (4).

Choose $r=\lfloor a t^{-1/2}\rfloor$ and $u=k t$, first taking $a$ small and $k$ large so that $A_d a^2+B_d/k<1/2$. Then decrease $t_0$ to ensure $r\ge6$ and $4H_d k t<1$. For any specified $j$ cells, successive conditioning in (3) gives probability at most $(H_d kt)^j$ that all $j$ roots have $D_x<kt$. The earlier cell indicators are measurable outside the next cell. Hence a rectangle fails with probability at most

$$
2^M(H_d kt)^{M/2}\le \exp[-c\,t^{-d/2}\log(1/t)]
$$

after a further decrease of $t_0$. We used $M\ge r^d/6^d$. If all rectangles are good, sum (4) and add the nonnegative crossing bonds to obtain $\lambda>t$. A union bound over at most $N^d$ rectangles proves the first line of (2).

**Finding a low mode in a typical sample.** Use row 1283's Dirichlet sine trial function on a spacetime cube of side $s=\lceil 2\pi\sqrt{d/t}\rceil$. Ask that every internal link be within quaternion chord distance $\delta=\sqrt{t}/(4\sqrt d)$ of the identity. A Haar cap has mass at least $c\delta^3$ for $0<\delta<1/2$, by taking the positive real branch above imaginary coordinates of norm at most $\delta/2$ in $S^3$. There are at most $d s^d$ internal links. The conditional probability of this cube event, for every exterior, is at least

$$
(e^{-K_d}c\delta^3)^{ds^d}\ \ge\ \exp[-C F_d(t)]=q.
\tag{5}
$$

The event uses fixed link coordinates. It witnesses a gauge-invariant eigenvalue bound. Let $\phi$ be the product of the positive one-dimensional Dirichlet sines on the cube, extended by zero. For any fixed unit colour vector $v$, the quotient of $\phi v$ is at most

$$
2d[1-\cos(\pi/(s+1))]+4d\delta^2 \ \le\ t/2.
$$

Indeed the scalar quotient follows by the sine addition formula. The extra term on one internal edge $xy$ is $\phi_x\phi_y|v-\operatorname{Ad}(U_{xy})v|^2$. Its sum is bounded by $4d\delta^2\|\phi\|^2$, using $|v-\operatorname{Ad}(U)v|\le2|1-U|$ and $2\phi_x\phi_y\le\phi_x^2+\phi_y^2$. Crossing bonds contribute only the scalar Dirichlet energy.

Pack $J\ge c(N/s)^d$ such cubes by spacing their starts $s+1$ sites apart with a periodic gap, taking $N\ge4(s+1)$. Conditional on any previous failures, (5) still applies because those failures use disjoint internal link sets. The probability that all cubes fail is at most $(1-q)^J\le e^{-Jq}$. A single success gives $\lambda\le t/2$. This proves the second line of (2) and upgrades the rare-cube lower construction from an expectation to an existence statement in the sampled field.

**The volume exponent.** For each fixed $\xi>0$,

$$
\frac{F_d(\xi h_d(N))}{\log N}
= \xi^{-d/2}\,
\frac{\frac{2}{d}(\log\log N-\log\log\log N)-\log \xi}
     {\log\log N}
\ \longrightarrow\ \frac{2}{d}\xi^{-d/2}.
\tag{6}
$$

Take $t=\xi_-h_d(N)$ with $\xi_->0$ small enough that the first line of (2) is at most $N^{-p-1}$ for large $N$. In the second line take $t=\xi_+h_d(N)$ with fixed $\xi_+$ large enough that $C F_d(t)\le(d/2)\log N$ eventually. Its failure probability is then at most $\exp[-c N^{d/2}t^{d/2}]\le N^{-p-1}$. The size and smallness conditions in (2) hold for both choices for all sufficiently large $N$. Thus, uniformly for $\beta\in[2,3]$,

$$
\mathbb P\{\xi_- h_d(N)\le\lambda(U)\le \xi_+ h_d(N)\}\ge1-N^{-p}.
\tag{7}
$$

Dimension enters through the $t^{-d/2}$ cells or links in a cube of side proportional to $t^{-1/2}$. Their probability cost is exponential in that volume times $\log(1/t)$. Balancing this cost against the number of places to find one such cube gives (6). The power is $1/2$ in four spacetime dimensions and $2/5$ in five.

## Passing to Wilson loops of growing diameter

For $K_U=I-L_U/(4d)$, the diagonal block of one step is $I/2$ and each neighbour block is the corresponding adjoint transport divided by $4d$. The inequality $0\le L_U\le4d I$ follows by bounding each squared edge difference by twice the sum of its two squared endpoint norms. Thus $0\le K_U\le I$. Expanding the power in paths gives the unconditioned return contribution

$$
J_U=\mathbb E_X[{\bf1}_B\,\tau(H_U(X))]
=\frac{\operatorname{Tr}K_U^m}{3N^d}.
\tag{8}
$$

On SU(2), the character in (8) can be negative. Positivity of the operator gives both bounds

$$
\frac{(1-\lambda/(4d))^m}{3N^d}\ \le\ J_U\ \le\ (1-\lambda/(4d))^m.
$$

On the event (7), $\lambda/(4d)\le1/2$ eventually and $m h_d(N)/\log N\to\infty$. Using $-2x\le\log(1-x)\le-x$ on $[0,1/2]$ and absorbing $3N^d$ gives

$$
e^{-C_1m h_d(N)}\le J_U\le e^{-c_1m h_d(N)}.
\tag{9}
$$

It remains to control the discarded contribution on the small scale of (9). We prove for the walk alone that

$$
R_N:=\mathbb P_X(B\cap E^c)\ \le\ C(m+1)\exp[-c m/\rho_N^2].
\tag{10}
$$

**Reduction of the walk.** Before conditioning on a return, the directions are independent letters with holds. Free reduction of the letters lifts the walk to the $2d$-regular tree of reduced words. Its distance $k$ from the root at time $m$ is its reduced length. Away from the root, a length increment $Y$ is respectively $+1,0,-1$ with probabilities $(2d-1)/(4d),1/2,1/(4d)$. At the root a proposed decrement becomes an increment. Coupling with independent copies $Y_j$ therefore gives $k\ge\sum_{j=1}^mY_j$. For $\eta=\mathbb E Y/2>0$ and small $\theta>0$, $e^{\theta\eta}\mathbb E e^{-\theta Y}<1$ by differentiation at zero. Markov's inequality yields $\mathbb P(k<\eta m)\le e^{-c m}$.

By the symmetries of the rooted tree, conditional on $k$ the reduced word is uniform among nonbacktracking words of length $k$. Its first letter is uniform, and each subsequent letter is uniform among the $2d-1$ choices other than the inverse of the last. With $k\ge\eta m$, the probability of at least $\lfloor k/4\rfloor$ cyclic cancellations is at most $(2d-1)^{-\lfloor k/4\rfloor}$, since that many terminal letters are prescribed by the initial letters. In every remaining closed word, the cyclic reduction contains a contiguous segment of at least $\lfloor k/2\rfloor$ letters. If its diameter is less than $\rho_N$, that segment stays within distance $\rho_N$ of its own start. There are at most $m+1$ possible starts. This upper bound can be taken before imposing the return.

**Exit estimate for that segment.** For a nonbacktracking walk let $z_i$ be its lifted first coordinate and $v_i$ the first component of its incoming unit step. With the entire past given, $\mathbb E_i v_{i+1}=v_i/(2d-1)$. If the incoming step is parallel to the first axis exactly one of its two signs is allowed, and otherwise both are allowed. Thus the conditional variance of $v_{i+1}$ is at least $(2d-2)/(2d-1)^2$. It follows that

$$
M_i=z_i+\frac{v_i}{2d-2}
$$

is a martingale whose increments have conditional variance at least some $\nu_d>0$. Indeed $M_{i+1}-M_i=(1+1/(2d-2))v_{i+1}-v_i/(2d-2)$. Let $\sigma$ be the exit time from a first-coordinate interval with centre $z_*$ and radius $\rho_N$. Up to and including $\sigma$, $|M-z_*|\le\rho_N+2$. Summing the conditional squared increments gives $\nu_d\mathbb E(\sigma\wedge j)\le\mathbb E[(M_{\sigma\wedge j}-z_*)^2]-(M_0-z_*)^2\le(\rho_N+2)^2$. Letting $j\to\infty$ bounds $\mathbb E\sigma\le C_d\rho_N^2$ uniformly over starting points and incoming directions in the interval. For a first step with no predecessor one may condition on that step and add one. Markov's inequality and the Markov property over successive intervals of $\lceil2C_d\rho_N^2\rceil$ steps bound survival for $h$ steps by $C e^{-c h/\rho_N^2}$. Until exit the coordinate interval lifts without wrapping for $2\rho_N+2<N$. A segment confined to the torus ball is among these survivors. Applying this estimate at each possible start, together with the two exponentially small word-length and cancellation probabilities, proves (10).

For the scalar lazy walk, write $K_{\rm sc}$ for its transition matrix. The same quadratic form bound gives $K_{\rm sc}\ge0$, and the constant vector has eigenvalue one. Consequently $\mathbb P_X(B)=N^{-d}\operatorname{Tr}K_{\rm sc}^m\ge N^{-d}$. Since $|\tau|\le1$, (10) also bounds the absolute signed contribution discarded from (8). In both dimensions $\rho_N^{-2}/h_d(N)\to\infty$. For large $N$, (9) and (10) imply $R_N\le J_U/2$ on (7), and $R_N\le N^{-d}/2$. In the conditional average

$$
W_N(U)=
\frac{J_U-\mathbb E_X[{\bf1}_{B\cap E^c}\tau(H_U(X))]}
     {\mathbb P_X(B)-R_N}
$$

the numerator is between $J_U/2$ and $3J_U/2$, and the denominator is between $N^{-d}/2$ and one. Equation (9) absorbs the remaining polynomial factor and proves (1).

## Selectivity and scope

The non-abelian step is (3). Two SU(2) adjoint rotations can have distinct fixed axes. Inequality (3) bounds the Wilson probability that they nearly fix a common axis, even when that axis is chosen after seeing the whole field. In compact U(1) every adjoint transport fixes the entire Lie algebra. Here $D_x=0$ and the long-loop character is exactly one. For the dimension comparison, (6) gives $h_5/h_4=(\log N/\log\log N)^{1/10}\to\infty$. The five-dimensional upper bound in (1) is eventually below the four-dimensional lower bound, for any fixed constants in those bounds. More explicitly, $h_4=o((\log N)^{-4/9})$ and $(\log N)^{-4/9}=o(h_5)$. The single test

$$
\exp[-N^2(\log N)^{-4/9}]<W_N(U)<1
$$

has probability tending to one for four-dimensional SU(2), zero for compact U(1), and tending to zero for five-dimensional SU(2). Both limits are uniform on the stated coupling interval.

Every contributing loop has growing diameter even after erasing retracings. Two flat fields also witness nonlocality directly. Take identity links, then put a fixed noncentral $g$ on all positive links crossing one periodic seam in its normal direction. Both fields are gauge equivalent to identity on each contractible box. For the first field $W_N=1$. For the second, a path winding once straight across that period, with holds to fill the $N^2$ steps, has positive walk probability, survives the diameter test and has $\tau(g)<1$. All other characters are at most one, so the second $W_N$ is strictly smaller.

The adjoint probe is insensitive to multiplying any individual link by a centre sign. Such a flip at the identity field changes the Wilson action on every incident plaquette. The seed uses the neutral Wilson transfer and compares the centre averages of eight twisted partition functions at each of two periods along the calibrated trajectory. The fixed-bare-coupling estimate (1) supplies no bound for that ratio. [Seed consumer, §3.1](gap-k2-tool-design-fable.md)

RESULT — Uniformly for $\beta\in[2,3]$, the typical attenuation $-N^{-2}\log W_N$ of adjoint loops of growing reduced diameter has order $(\log\log N/\log N)^{1/2}$ in four-dimensional SU(2), order $(\log\log N/\log N)^{2/5}$ in five-dimensional SU(2), and is zero in compact U(1). Row 1532 is an author’s hand proof without independent or Lean verification. The seed and the Yang–Mills mass gap remain open.
