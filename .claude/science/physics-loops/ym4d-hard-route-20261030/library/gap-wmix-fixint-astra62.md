## Repo search

At checkout `b317972ca` the target-specific prior note is absent. A bounded search of `origin/main`, `pr/10114`, `pr/10133`, `pr/10134` and `pr/10141` for connected open slabs, cap subtraction, physical-length plaquettes, the plaquette-square coefficient, free-ended Wilson joins, joining strength, plaquette covariance matrices, connected plaquette susceptibilities, spin-network weights and two-slab joining returned no lines. The question is the variation on the fixed joining interval for row 1611. The first test is the contribution of all fundamental squares at physical separation, including their common cap component.

A second pass on the same refs used simple-loop eigenvalues, open-boundary and marked plaquettes, open-cylinder moments, plaquette-block covariance, seam Dobrushin bounds and spin-network truncation. The relevant hits on main were `research/mass-gap/library/gap-fp-astra.md` 539–553 (positive one-bond coefficients and the finite-volume transfer trace) and `research/mass-gap/library/prior/gap-math-lit.md` 15 (the nonvacuum thermal-sum requirement at aspect four). Other hits were the height-five spin-Hamiltonian coefficient in `INDEPENDENT_RECTANGLE_COEFFICIENT.md`, stabilizer paths in `CYCLE703_OPEN_BKSF_STABILIZER_PREPARATION_NOTE`, screened radii in `ag1.md` and `nl1-L.md`, and a seam average in `parts/hard-core--mapped.md`. None estimates this joining variation.

**ON FILE (531, 1149, 1151, 1611).** The November 8 digest leads to `ym4d-proof/MASS_GAP_LOCAL_BLOCK_ASTRA.md` 106–149 on PRs 10114 and 10133. For a simple loop of length $b'$ its normalized character has convolution eigenvalue $(I_2/I_1)^{b'}$ and squared Haar norm $1/4$. Its one-step correlation *lower* bound serves a different consumer. Row 1149 (16) gives monotonicity of $I_d/I_1$ and the marked one-link exponential moment. Row 1151 (4), (6) uses rotation into a spatial transfer direction on an open cylinder with full boundary magnetic weights. Its (2)–(3) analyzes a different anisotropic seam by Poisson products of rectangles. I use the one-plaquette estimate with the half boundary weight below. Row 1611 (8)–(11) supplies the connected covariance, its normalization and the first Taylor coefficient. The registry entries at 1016–1020 concern cube, score and thermal-transport estimates. The specified concurrent assignment aside, I found no owner or prior bound for the normalized spin-pair variation. [November 8 digest](prior/repo-search-2026-11-08.md) · [Row 1149](gap-solve4-astra62.md) · [Row 1151](gap-solve5-astra62.md) · [Row 1611](gap-direction7-astra62.md)

**ON FILE (outline index 244).** Sussman and Alpoge, with Claude and Codex, give the positive Wilson eigenvalues in GL3, the series and ratio bound in GL4, and the product convolution, outline 2195–2257. GL8 gives the rotated transfer trace, 2313–2335. Index locators are chunk 02, 88–93 and 100–103, and obligations 24. The gap is separate at outline 32486–32490 and CA-I 2698–2714. These are the supplied sources at `31a47c543775`. No Balaban estimate is needed here.

## The derivative with the full cap

**PROVED (a decomposition of the actual integrand).** Fix the release witnesses and an allowed $\ell$. Write $V=n^3$, $v=n/1024$, $\beta=\beta_K$, $B=T^v/\langle1,T^v1\rangle$, $\rho=B1$, $C=B-|\rho\rangle\langle\rho|$. In an orthonormal spin-network basis let $\rho_i=\langle i,\rho\rangle$, $C_{ij}=\langle i,Cj\rangle$, and define
\[
 r_i=\prod_e\frac{I_{2j_e(i)+1}(t)}{I_1(t)},\qquad
 s=\sum_i r_i|\rho_i|^2,\qquad h_{ij}=\frac{r_i r_j}{s^2}.
\]
Use the continuous weights at zero. The constant has $r_0=\rho_0=1$, and $C1=0$. Set
\[
 a=\sum_{ij}h_{ij}\operatorname{Re}(\overline{\rho_i}C_{ij}\rho_j),
 \qquad b_c=\sum_{ij}h_{ij}|C_{ij}|^2,\qquad L=1+2a+b_c .
\]
Here $a=\langle J_t\rho,CJ_t\rho\rangle/s^2\ge0$, since $C\ge0$ by Cauchy–Schwarz for $B$. In (11), $a=z_t/s$, $b_c=\|A_t\|_{\rm HS}^2/s^2$. Consequently
\[
 D=\log L-2\log(1+a),\qquad
 D'=\frac{b_c'}{L}-\frac{2(a+b_c)}{L(1+a)}\,a'.                         \tag{1}
\]
Indeed $e^D-1=(b_c-a^2)/(1+a)^2$. This keeps the projection onto the moving cap exactly, including its derivative. The two coefficient magnitudes in (1) are at most $1$ and $2$. For a symmetric set $E$ of ordered pairs define $D'[E]$ by restricting the two *differentiated sums* to $E$, using the full $s,L,a,b_c$ everywhere. Thus $D'=D'[E]+D'[E^c]$. The sign in the second term is essential. Replacing $J_t$ by a finite-rank truncation in the denominator would change this observable.

For rigor at a fixed cutoff, $\rho\in L^2$ and $C$ is Hilbert–Schmidt because the slab has a bounded continuous kernel on a finite product of compact groups. The coefficient absolute sums before weighting are finite for $b_c$ and, by Cauchy–Schwarz on pairs, for $a$. All $r_i$ increase from their values at zero and are at most one, by row 1149 (16) and the convolution contraction. On a compact real $t$ interval the normalized one-link convolution has a continuous derivative in operator norm, by differentiating its bounded kernel. Its finite tensor product and gauge projection inherit this property, so $r_i'$ are bounded uniformly in $i$ at this cutoff. Differentiation of the two sums and of $s$ is legitimate. No bound on that operator derivative uniform in $n$ is used.

## All pairs of fundamental squares

**PROVED (boundary moment for the slab used here, by the method of 1149/1151).** At either free end and for any spatial square $p$, put $d_p=1-w_p$. Uniformly in $n,v$ and $\beta\ge2$,
\[
 \mathbb E e^{\beta d_p/4}\le C_0,\qquad
 \mathbb E d_p\le C_1/\beta,\qquad
 \mathbb E d_p^2\le C_2/\beta^2.                                          \tag{2}
\]
Rotate a periodic spatial axis of $p$ into the transfer direction. The open time boundaries become spatial walls in each of $n$ identical cross-sections. In the symmetric Wilson transfer the spatial plaquettes on the old end had coupling $\kappa=\beta/2$. In the rotated picture $p$ is electric at that coupling. Its tilt in (2) replaces $\kappa$ by $\kappa/2$, at one crossing bond of one layer. All the other couplings and magnetic slice weights in the rotated transfer are the same. Write $z_-(q)=\int e^{-q(1-w)}dU$. With *mass-normalized* electric factors the changed layer is below the original in positive-operator order. Indeed the normalized multipliers are $I_d(q)/I_1(q)$; each factor $I_{h+1}/I_h$ increases because it equals the mean of $x$ under the tilt $e^{qx}(1-x^2)^{h-1/2}dx$ on $[-1,1]$, whose derivative is the variance. The equality follows from the positive Bessel series by integration of even powers, as in row 1149 (16). Tensoring with the unchanged positive convolutions, multiplying on both sides by the same magnetic half weight and restricting to gauge invariants preserve the order. Tracing against the positive $(n-1)$st power of the original layer preserves the inequality. Restoring the scalar at the marked bond gives $\mathbb E e^{\beta d_p/4}\le z_-(\kappa/2)/z_-(\kappa)$. In the Haar angle integral $\sin^2\theta\,d\theta$, $1-\cos\theta\ge2\theta^2/\pi^2$, and on $[0,\min(1,q^{-1/2})]$ one has $\sin\theta\ge2\theta/\pi$ and $1-\cos\theta\le\theta^2/2$. Thus $z_-(q)\asymp(1+q)^{-3/2}$ for $q\ge0$. The last two bounds follow by bounding $x,x^2$ by constants times $e^x$ for $x=\beta d_p/4$. The half weight matters here: row 1151's cut retains a full boundary spatial plaquette.

**PROVED (variation of the entire plaquette matrix in (1)).** Let $\mathcal P$ be all $3V$ unoriented fundamental-square networks, normalized as $\psi_p=2w_p$. For all sufficiently large $\beta$ and every $\tau>0$,
\[
 \int_0^\tau |D'[\mathcal P\times\mathcal P]|\,dt\le C/\beta^2.           \tag{3}
\]
The constant is independent of $v,n,\tau$. More precisely, within (1) the $b_c'$ term from those pairs costs $O(\beta^{-4})$ and the $a'$ term costs $O(\beta^{-2})$. The statement includes all relative displacements in the genuine open slab at $v=n/1024$.

Let $m_p=\mathbb E w_p(X)$ and $C^{w}_{pq}=\mathbb E[w_p(X)w_q(Y)]-m_pm_q$ as in row 1611 (8). The end marginals agree by time reflection. Cauchy–Schwarz and (2) give $|C^w_{pq}|\le C_2/\beta^2$ for every $p,q$. The entries are $C_{pq}=4C^w_{pq}$ and $\rho_p=2m_p$ in the normalized basis. For $r=(I_2/I_1)^4$, the restricted $b_c$ and $a$ are precisely
\[
 \frac{16r^2}{s^2}\sum_{pq}(C^w_{pq})^2,\qquad
 \frac{16r^2}{s^2}\sum_{pq}m_p C^w_{pq}m_q.                               \tag{4}
\]
Termwise smallness alone would leave $9V^2$ pairs.

Choose the $V/4$ vertex-disjoint $12$-squares based at even first and second coordinates, with arbitrary third coordinate. For each unordered pair of them $\psi_p\psi_q=4w_pw_q$ has Haar norm one, and is a spin-network eigenfunction of weight $r^2$. Distinct pairs are orthogonal by integration on an unmatched edge. Since $|w|\le1$, $|1-w_pw_q|\le d_p+d_q$. The coefficient of this product in $\rho$ is at least $4(1-2C_1/\beta)\ge2$ once $\beta\ge4C_1$. It follows on the **full** Hilbert space that
\[
 s=\langle\rho,J_t\rho\rangle\ \ge\ 1+M r^2,\qquad M=4\binom{V/4}{2}.     \tag{5}
\]
No independence of Wilson plaquettes is involved. For any increasing spin-pair weight $w(t)$ with $w(0)=0$, $s$ increases, so the product rule gives
\[
 \int_0^\tau |(w/s^2)'|\,dt
 \le 2\int_0^\tau \frac{w'}{s^2}\,dt-\frac{w(\tau)}{s(\tau)^2}
 \le 2\int_0^\tau \frac{w'}{s^2}\,dt.                                    \tag{6}
\]
For $w=r^2$, (5) bounds this by $2\int_0^\infty (1+M y)^{-2}dy=2/M$. Multiply by the two sums in (4) and use the bounded coefficients in (1). This cancels the full $V^2$ count and proves (3).

**PROVED (coefficient check).** As $t\downarrow0$ at each fixed cutoff, $r=t^4/4^4+O(t^6)$ by GL3. Thus the first expression in (4) has coefficient $16/4^8=1/64^2$ multiplying the unnormalized sum of squares in (9). The linear terms in $a$ cancel between the two logarithms in (1). Estimate (3) bounds the integrated, normalized contribution even when that Taylor coefficient alone has no useful uniform upper bound.

## Bounded total spin, allowing all positions and multiplicities

**PROVED.** For each fixed integer $H\ge4$ let $d(i)=\sum_e 2j_e(i)$ and $E_H=\{(i,j):d(i),d(j)\le H\}$. Choose spin networks on prescribed edge supports with an orthonormal basis of invariant contractions at each vertex. There are constants $K_H,C_H$ such that, along any of the stipulated calibrated sequences, for $K\ge K_H$,
\[
 \sup_{\tau>0}\int_0^\tau |D'[E_H]|\,dt\le C_H\beta_K^{-2}.               \tag{7}
\]
This also holds with the sum of the absolute integrals of the individual real pair contributions on the left. The complementary pairs, including pairs with just one index above $H$, are part of the full cost.

*Control of one network.* For $n>4H+4$ each nonconstant connected support with $d(i)\le H$ lies in a contractible lattice box of bounded size. For a disconnected support use a separate box and a tree gauge on each component. Put each tree link equal to one. Every remaining chord holonomy is a loop in its box, expressible as a product of at most $c_H$ conjugates of unit plaquettes or their inverses. For instance, lift a tree path plus its chord to the cubic lattice, sort its coordinate steps by interchanging perpendicular adjacent steps, and cancel opposite steps within each axis. Each interchange inserts a conjugated elementary square. The sum of the coordinate steps is zero, the path has bounded length, and all interchanged paths stay in a bounded box. The quaternion chord norm obeys the triangle inequality for products and $|U-1|^2=2(1-w(U))$. Thus the sum of squared distances from the identity of all resulting chord holonomies is bounded by $c_H$ times a sum of at most $c_H$ elementary deficits, with multiplicities.

The function of these chord holonomies given by a spin network is smooth, bounded by $c_H$, and invariant under simultaneous conjugation on each component. At the all-identity point, the differential in any single argument is an adjoint-invariant linear functional on $\mathfrak{su}(2)$. It vanishes, since rotations can take each vector to its negative. Taylor's formula in a fixed small product chart bounds deviation from the flat value by $c_H$ times the sum of squared chord distances. Off this chart some chord distance is bounded below, so boundedness gives the same estimate with a larger constant. Uniform constants exist because up to placement there are finitely many connected labelled shapes, representation labels, and chosen contractions for degree $\le H$. Disconnected shapes are tensor products with at most $H$ components. Bounds on (2) and the triangle inequality in $L^2$ now give
\[
 \|\psi_i-\psi_i(\mathbf 1)\|_{L^2(\rho\,dX)}\le c_H/\beta,\qquad
 |\rho_i|\le c_H,\qquad |C_{ij}|\le c_H/\beta^2\quad ((i,j)\in E_H).      \tag{8}
\]
The last estimate uses the two true end marginals and Cauchy–Schwarz on the joint slab law. It places no condition on how far apart the components of the two networks are.

*Counting and normalization.* Let $m$ be the total number of nontrivial connected components in the ordered pair. A component has no degree-one vertex because a nontrivial irreducible has no invariant vector. Hence it contains a cycle of at least four edges on the spatial torus, and $d(i)+d(j)\ge4m$. There are at most $c_H V^m$ such pairs: choose a root vertex for each component, then one of the finitely many shaped, labelled and contracted supports through that root. For $0<t\le1/4$, GL4 bounds $I_{k+1}(t)/I_1(t)$ by a constant times $t^k$, and GL3 gives $I_2(t)/I_1(t)\ge c t$ by the series and compactness. Thus $w=r_i r_j\le c_H r^m$. For $t\ge1/4$ this comparison still holds since $w\le1$ and $r$ has a positive lower bound.

Each product of $m$ distinct squares from the disjoint grid in (5) has Haar norm one and eigenvalue $r^m$. Distinct subsets give orthogonal functions. Its mean in the open-slab end law is at least $2^m(1-m C_1/\beta)$ by telescoping the product of $w_p$'s in $[-1,1]$. For $\beta\ge2m C_1$ these $\binom{V/4}{m}$ contributions give $s\ge1+c_H' V^m r^m\ge1+c_H'' V^m w$, where the two lower-bound constants are positive, for $V\ge8m$. In (6) this gives $\int|(w/s^2)'|\le 2/(c_H'' V^m)$. Both constant-index cases have $C_{ij}=0$. For the rest, multiply by the estimates from (8) and by the two coefficients of (1), then sum over at most $c_H V^m$ pairs for each $m$. This proves (7), including the stated absolute-sum version. All the estimates use the full cap in both normalized sums.

**PROVED (order of the cutoff).** There exists an integer $H(K)\to\infty$ along the full calibrated sequence for which the left side of (7) tends to zero. For each integer $h$ choose increasing $K(h)$ such that (7) is valid and $C_h/\beta_K^2\le1/h$ thereafter. Put $H(K)=h$ for $K(h)\le K<K(h+1)$. This diagonal statement supplies no bound on the complementary sums. At a fixed positive $t$ there can be arbitrarily many mutually disjoint square excitations.

## All nonzero centre characters on the weak joining interval

**ON FILE (785, checked in 790 §5).** For arbitrary pinned $X,Y$ the gauge integral in one join is the partition function of unit quaternion spins $g_x$ with bond readings $g_x\cdot O_e g_y$. Row 785 (14) gives, for a single flat centre flip, $|\log[J_t(X,C_zY)/J_t(X,Y)]|\le4t n^2(3t/2)^{\lfloor n/2\rfloor-1}/(1-3t/2)$, $0<t<2/3$. The one-bond scalar normalization cancels. This already proves exponential suppression of a pinned twist on every compact subinterval below $2/3$. What is needed here is the *absolute variation* of its contribution to (1) after closing the ring with arbitrary ordinary slabs. [Row 785, §3](gap-vmf-lip.md) · [Check 790, §5](gap-vmf-lip-check-opus.md)

**PROVED (all spins in the charged part of (1)).** For every fixed $0<\tau<2/3$ there are $c_\tau,C_\tau>0$ such that at every sufficiently large $n$, every $\beta>0$ and every $v\ge1$,
\[
 \int_0^\tau |D'[\mathrm{ch}]|\,dt+
 \int_0^\tau |(D-D_0)'|\,dt\ \le C_\tau e^{-c_\tau n}.                   \tag{9}
\]
Here $\mathrm{ch}$ consists of ordered spin pairs of the same nontrivial $\mathbb Z_2^3$ character. $D_0$ uses just the centre-neutral ring trace and the original free caps. Distinct characters have $C_{ij}=0$, since $B$ commutes with every flat flip and $\rho$ is neutral. The cap has zero projection on every charged block.

To prove (9) put $R=\operatorname{Tr}(S J_t S J_t)$, $S=T^v$, and $R_0=\operatorname{Tr}(P_0 S J_t S J_t)$. The signed-sector sum $R_0$ is the average of eight **positive path integrals**: in each a single join has $J_t(X,C_zY)$ in place of $J_t(X,Y)$. This follows by commuting the flip and integrating the twisted kernel in the cyclic trace. Telescoping the pinned estimate of row 785 over at most three coordinate flips gives $|\log(R/R_0)|\le \epsilon_n=C_\tau n^2 e^{-m_\tau n}$ throughout $[0,\tau]$. Also $R\ge R_0>0$ since the trace on each character is the trace of the square of $J_t^{1/2}S J_t^{1/2}$ on that character. Write $F=\log(R/R_0)=D-D_0$. This last equality holds because all free ends are neutral.

For both $R$ and $R_0$ remove the same factor $z(t)^{-2|{\cal E}|}$, where $|{\cal E}|=3V$. The logarithmic second derivative of each remaining positive integral is a variance of the sum of its $2|{\cal E}|$ marked bond readings. The formula includes the positive twist mixture. In particular $|F''|\le 8|{\cal E}|^2$. At each $t\in[0,\tau]$ take a one-sided difference of length $h=\sqrt{\epsilon_n}/|{\cal E}|$ within that interval, possible for large $n$. Taylor's inequality gives $|F'|\le2\epsilon_n/h+4|{\cal E}|^2h$. This controls the second integral in (9), including arbitrarily near $t=0$.

In (1) let $L_0=R_0/(\langle1,S1\rangle^2 s^2)$ and let $b_{\rm ch}$ denote the charged terms of $b_c$. Then $L=L_0+b_{\rm ch}$, $a_{\rm ch}=0$, and direct differentiation gives
\[
 D'[\mathrm{ch}]=\frac{b_{\rm ch}'}{L}
 =F'+(1-e^{-F})(\log L_0)' .
\]
Here $|(\log L_0)'|\le C|{\cal E}|$: $R_0$ is a two-join positive integral, $s$ a one-join positive integral, and each log derivative, including its scalar normalizer, is bounded by twice the number of marked bonds. Since $0\le1-e^{-F}\le\epsilon_n$, polynomial factors are absorbed by decreasing $c_\tau$. This proves the first integral in (9). The estimate concerns the signed sum within the full charged block. It holds with no restriction on its total spin degree and requires no assumption about the bulk coupling. In particular it continues from $1/4$ to any fixed $\tau<2/3$.

## A range on which the full absolute variation is controlled

**PROVED (all spins together).** At the calibrated couplings there is a constant $c_*>0$, independent of $K$, such that for all sufficiently late cutoffs
\[
 t_K=(c_*\,\beta_K^{3/2}/V)^{1/4},\qquad
 \int_0^{t_K}|D'_K(t)|\,dt\le\tfrac12\log(16/15).                         \tag{10}
\]
For $Vt_K^4=o(\beta_K^{3/2})$ the integral tends to zero. The endpoint in (10) tends to zero, but is larger than row 1611's $n^{-4}$ range. The proof uses the signed cancellation of the identical cap factors in the two arrangements. It supplies a separate check on the spin-sum calculation near the origin.

**PROVED (uniform remainder for a single join).** For some absolute $\delta>0$, for $0\le t\le\delta$ and all pinned ends,
\[
 \log J_t(X,Y)=\lambda\sum_p w_p(X)w_p(Y)+E_t(X,Y),\qquad
 \lambda=t^4/64,\qquad |E_t|+t|\partial_t E_t|\le C Vt^6.                \tag{11}
\]
Here is the uniformity missing from a fixed-cutoff Taylor expansion. Use the deletion induction of row 1151 §2, here on individual edges with independent Haar vertex spins at strength zero. For a subset $W$ of edges, expand its unnormalized partition function in factors $e^{z y_e}-1$, $|y_e|\le1$. In the graph of edges adjacent at a vertex, of degree at most ten, the integrated weights factor over distinct connected components. Each connected selected set $A$ has weight at most $(e^{|z|}-1)^{|A|}$. To compare with $W\setminus\{e\}$, the term for $A\ni e$ multiplies this weight by the partition function on $W\setminus N[A]$, with $N[A]$ the closed neighbourhood. Inductively assume each previous one-edge deletion ratio (larger set divided by smaller) lies within $1/2$ of one. Then the quotient on deleting $N[A]$ from $W\setminus\{e\}$ has modulus at most $2^{11|A|}$. There are at most $10^{2k}$ connected sets of $k$ edges through $e$, by a doubled spanning-tree walk in the adjacency graph. Choose a fixed disc about zero on which $\sum_{k\ge1}[10^2\,2^{11}(e^{|z|}-1)]^k<1/2$. The induction starts at the empty set and gives an analytic logarithm of each ratio bounded by $\log2$. The logarithm of the full partition function is bounded by $C V$ on that disc. Division by $z(t)^{3V}$ in row 1611 (4) preserves this bound on a smaller disc since the one-link normalizer is analytic and equals one at zero.

The even torus makes the kernel even in $t$ by flipping one vertex sublattice. Row 1611's single-join square integral gives the displayed quartic coefficient and vanishing lower coefficients, also for the logarithm which is zero at $t=0$. Cauchy's coefficient inequality on the fixed disc, summed from degree six, bounds both the remainder and its differentiated series on a smaller half-disc. This proves (11). The statement uses the same plaquette as (4), before the two copies of the join are contracted.

**PROVED (the needed collar probability).** In the six-piece law at $t=0$, with either arrangement of the endpoints, with probability at least $1-Ce^{-cV/\beta^2}$ the sum of the $d_p^2$ over all joined end faces is at most $C V/\beta^2$. For one orientation at one end, repeat the rotated proof of (2) with any subset $A$ marked. Each changed normalized layer $F_i$ satisfies $0\le F_i\le F$, the homogeneous unmarked layer. Schatten Hölder gives $|\operatorname{Tr}\prod_{i=1}^n F_i|\le\prod_i(\operatorname{Tr}F_i^n)^{1/n}\le\operatorname{Tr}F^n$ by eigenvalue monotonicity. Restoring the scalars gives $\mathbb E e^{(\beta/4)\sum_{p\in A} d_p}\le C_0^{|A|}$. On $[0,2]$, $e^{d^2}-1\le C\beta^{-2}e^{\beta d/4}$. Expanding the product of $1+(e^{d_p^2}-1)$ bounds $\mathbb E e^{\sum_p d_p^2}$ by $(1+C/\beta^2)^V$ for that orientation. Exponential Markov and a union bound over three orientations and eight joined ends prove the assertion. This is the multi-mark argument of row 1151 (6) with the boundary convention of (2).

**PROVED (retaining the cap factors in absolute variation).** For either arrangement write $U=\sum_{j,p}(d_p(X_j)+d_p(Y_j))$, $W=\sum_{j,p}d_p(X_j)d_p(Y_j)$, $H_0=U-W=\sum_{j,p}(1-w_p(X_j)w_p(Y_j))\ge0$. With the scalar $e^{4(3V)\lambda}$ removed, the leading partition function from (11) is $Z_H=\mathbb E_0 e^{-\lambda H_0}$. Its cap comparison is $Z_U=\mathbb E_0 e^{-\lambda U}$. In both arrangements there are two slabs with both ends joined and four with one end joined, all independent at zero. Thus $Z_U$ as a *function of* $\lambda$ is exactly the same in A and B. It is the integral with the rank-one join obtained by retaining the two single-end factors of the quartic term. Neither its value nor its derivative needs an absolute volume charge.

Set $G=\log Z_H-\log Z_U\ge0$ separately in A and B. On the good event of the collar bound, $W\le C V/\beta^2$ by $2xy\le x^2+y^2$. On its complement $e^{-\lambda H_0}\le1$. Jensen gives $Z_U\ge e^{-\lambda \mathbb E_0U}\ge e^{-C\lambda V/\beta}$ by (2). For $0\le\lambda\le\Lambda$, $\Lambda V\le\beta^{3/2}$, and $\beta=O(\log n)$, this yields
\[
 0\le G(\lambda)\le C\Lambda V/\beta^2+C e^{-c'V/\beta^2}=:M_\Lambda
\]
for all sufficiently late cutoffs, uniformly in that range. Indeed the extra factor on the bad probability is at most $e^{C\sqrt\beta}$. Both $\log Z_H$ and $\log Z_U$ are convex in $\lambda$ with slopes between $-C V/\beta$ and zero. Their second derivatives are tilted variances, and the total increase of either slope is at most $C V/\beta$. Therefore $|G'|\le C V/\beta$ and $\int_0^\Lambda |G''|\le C V/\beta$. Integration by parts, using $G(0)=0$, gives
\[
 \int_0^\Lambda (G')^2
 =G(\Lambda)G'(\Lambda)-\int_0^\Lambda GG''
 \le C M_\Lambda V/\beta .
\]
Cauchy–Schwarz now gives $\int_0^\Lambda |G'|\le (C\Lambda M_\Lambda V/\beta)^{1/2}$. This is a bound for absolute variation. The subtraction of the common $\log Z_U$ makes it applicable to the difference between the arrangements.

To restore the error in (11), its sum over four joins has size $\le C Vt^6$ and derivative $\le C Vt^5$. For $t\le\tau=(64\Lambda)^{1/4}$, $V\tau^6=o(1)$ uniformly when $\Lambda V\le\beta^{3/2}$. The normalized density ratio to the $e^{-\lambda H_0}$ law is then $1+O(Vt^6)$ uniformly. Under that latter law $\mathbb E_\lambda H_0\le\mathbb E_0 H_0\le C V/\beta$ by differentiating the tilted mean. The resulting error in the log derivative, after integration in $t$, is at most $C V\tau^6(1+\Lambda V/\beta)$ for each arrangement. It tends uniformly to zero since $\beta=O(\log n)$. Combining the two arrangements and using the increasing coordinate $\lambda=t^4/64$ proves
\[
 \int_0^\tau |D_K'|\,dt\le C\Lambda V/\beta^{3/2}+o(1)
 \quad (0\le\Lambda V\le\beta^{3/2}).                                    \tag{12}
\]
All constants precede the cutoff. Choose $c_*>0$ small enough that $c_*\le 1$ and the leading term in (12) with $\Lambda V=c_*\beta^{3/2}/64$ is below $\frac14\log(16/15)$. This leaves room for the vanishing error and proves (10). At fixed $\tau=1/4$, neither the small remainder $V\tau^6$ nor this use of a single positive collar estimate follows.
