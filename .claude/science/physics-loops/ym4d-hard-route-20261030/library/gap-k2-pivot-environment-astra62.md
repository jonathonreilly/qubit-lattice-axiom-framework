## Repo search

Row 1475. Research text by Codex at `61bdc768aad4`. The November 8 survey's closest hit is PR 10114, `MASS_GAP_LOCAL_BLOCK_ASTRA.md` 106–149, a lower bound on one loop correlation. I also checked that PR's `checks/review_massgap_block_literature.md` 111–122, 163–170 and main's `research/mass-gap/library/gap-form-exercise.md` 139–145. They describe Tomboulis's flux-mass comparison and the common interpolation parameter questioned by Ito and Seiler. Main's `BETA6_PLAQUETTE_TENSOR_NETWORK_FINITE_IRREP_SUPPORT_AND_RECOUPLING_WALL_NOTE_2026-06-04.md` 10–30 covers SU(3) one-link coefficients and leaves the contraction open. The row name, END-K2 and pivot/environment terms returned no matching file in the YM research and soft-route trees of main and PRs 10114, 10133, 10134, 10141 (respectively `8b11ae2bb9`, `f76f6c649c`, `89faef229f`, `1e70c7211a`, `a2f6a430e2`). The row-specific prior note is absent and the registry names no other owner. [Lead's search](prior/repo-search-2026-11-08.md) · [Open registry](open-registry.md)

Proposition NP uses a direct product with ordered Ising. The Ising film supplies the spin-flip trace and winding-contour idea used below. The pinned Wilson sheet fixes tangential boundary fields at large coupling. Lemma NRM permits arbitrary rescaling on one torus. Row 1474 tests other block representations. Here the spin interacts with the SU(2) link, and one local rule fixes all sixteen masses. [NP, lines 383–419](gap-crux-exercise4-max.md) · [Film, lines 305–307](gap-solve19-astra62.md) · [Pinned sheet, (22)](gap-solve17-astra62.md) · [NRM](gap-blockstep-fable.md) · [1474, §§1–2](gap-k2-t2-representation-fable.md)

## Result

**Proved by hand.** One local member of row 1348 at $\beta=23/10$ has conditional edge-matrix covariance at least $371/432$ at arbitrarily large separation. Its neutral purity is at most $41/81$ on every $m=512v$ family with even $v\ge4$. The end class requires at least $457/625$ at its stipulated sizes. The same pressure obstruction holds for a coefficient law with a density and connected support. The Wilson-only entry remains open.

**Plan saved at the outset.** Identify the input and end classes, test mixing after one pivot, then check the result against the unnormalized mass integral on both time periods.

## 1. The estimate at issue

**Proved in the cited rows.** At time periods $\tau=v,2v$ and spatial side $m$, write $Z^z(\tau)$ for the mass with temporal centre twist $z\in\mathbb Z_2^3$, $Z_+(\tau)=2^{-3}\sum_z Z^z(\tau)$, and $P=Z_+(2v)/Z_+(v)^2$. An exact pivot preserves each mass when implemented on its torus, including its environmental normalization. A common scalar per site cancels from $P$. Row 1471's local end class with wrap error at most $1/100$ gives $P\ge457/625$ at its stipulated sizes. Check 1473 gives $\log(1+1/(42e))$ as the sharp supremum of its sufficient Wilson entry criterion over strengths and free parameters. The certified design-strength example is $\beta=\kappa=1/40000$. [1468, §§3.1 and 4.2](gap-k2-tool-design-fable.md) · [1471, §§4–5](gap-k2-end-class-fable.md) · [1473, lines 28–34 and 82–91](gap-k2-end-class-check-astra62.md)

**Claims tested.** The first is a proposed estimate for row 1348's iterable class. At a side-two pivot, the conditional covariance of any two one-block environmental functions of absolute value at most one is bounded by $C e^{-d/\xi}$ given the retained links, with $d$ the block separation and finite $C,\xi>0$ independent of volume. Impose even a product reference, nearest-neighbour coefficient dependence and the Wilson-size bounds (2) at $B=2$. The second claim is that the full class can reach END-K2 by exact steps. We test it on the masses themselves. The pivot algebra and its closure are inputs from rows 1348, 1350 and 1469. [1348, lines 13–32](gap-blockstep3-astra62.md) · [1350, §7](gap-blockstep3-check-opus.md) · [1469, §5](gap-k2-tool-design-check-astra62.md)

**Source scope.** Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, distinguish mass preservation from identification of a pushed-forward law. They derive the rooted polymer bound assuming the activity inequality of Roland Kotecký and David Preiss. Their complete account uses Tadeusz Bałaban's local gauge-covariant block averages and assumes the earlier-scale density representation in its coupling argument. I checked the source ranges identified by outline chunks 01–03, the obligations and CA-I chunks 01 and 11. Those passages leave the present order-one environmental estimate to be proved. [Outline, 394–416](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L394-L416) · [Activity hypothesis, 1271–1279](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L1271-L1279) · [CA-I, 43013–43028](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L43013-L43028) · [Earlier-level hypothesis, 56439–56458](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L56439-L56458) · [Coupling ceiling, 56530–56547](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L56530-L56547)

## 2. A local member of the pivot class at $\beta=23/10$

**Proved by construction.** Use a four-dimensional periodic lattice, normalized link Haar $dU_e$, and $q(u)=\operatorname{tr}(u)/2=\operatorname{Re}u$. For each twist use exactly the Wilson plaquette tensors $\beta q(U_p)$, with the prescribed centre sign on a seam representative. Quaternion inversion is real linear on unit quaternions, so each is a real four-linear tensor of norm $\beta$. Include the Wilson scalar $e^{-\beta}$ per plaquette. At every site take an independent fair sign $s_x$ and a Haar frame $h_x\in SU(2)$. At every positively oriented edge take two independent Haar frames $l_e,r_e$ and the independent coin specified below. All reference variables are independent of the link Haar. The same rule and the same probability measures are used on every torus.

Let $D=\operatorname{diag}(1,1,-1,-1)$, $D'=\operatorname{diag}(2,0,-1,-1)$, and use probability Haar on $S^3$. Define

$$
A=\int e^{6u^tDu}\,du=\frac{\sinh 6}{6},\qquad
B_t=\int e^{t u^tD'u}\,du,\qquad
p=\frac{A-B_1}{B_6-B_1}.
$$

Indeed $u=(\sqrt{x}\,e^{i\theta},\sqrt{1-x}\,e^{i\phi})$ has uniform $x$ on $[0,1]$ under sphere area. The area element in these coordinates is a constant times $dx\,d\theta\,d\phi$, as follows from the diagonal metric entries $1/[4x(1-x)],x,1-x$. Thus $u^tDu=2x-1$. The first four terms of the positive series for $A$ give $A>1+6+10+9=26$. Also $B_1\le e^2<9$. Interchanging the first two coordinates gives a conjugate $D''$ of $D'$ with $D=(D'+D'')/2$. Strict convexity of the exponential on the positive-area set $u_0^2\ne u_1^2$ gives $A<B_6$. Consequently $0<p<1$. Set $b_e=6$ with probability $p$ and $b_e=1$ otherwise. The coin makes the two ordered signs have precisely the same link integral while allowing an observer to distinguish them from the matrix spectrum.

For $e=xy$ put $\eta_e=s_xs_y$, $\gamma=1/8$, and set $H_e=6D$ for $(s_x,s_y)=(+,+)$, $H_e=b_eD'$ for $(-,-)$ and $H_e=0$ otherwise. The one-edge term in the exponent is

$$
 U_e^t Q_e U_e
 = (l_eU_er_e)^t H_e(l_eU_er_e)
   +\gamma\eta_e\big[q(h_x^{-1}U_eh_y)^2-\tfrac14\big].                 \tag{1}
$$

In homogeneous quadratic notation the last constant is $-|U_e|^2/4$. Left and right quaternion multiplication by fixed units are orthogonal. The second matrix is $\gamma\eta_e$ times a rank-one orthogonal projection minus its scalar part. Both terms are traceless real symmetric matrices. Hence $\|Q_e\|_{\rm op}\le12+3/32<12\beta$ and $\|T_p\|=\beta\le4\beta$, within 1348 (2). Disjoint endpoint sets use independent coefficient variables in the reference. All weights are strictly positive. Under $U_{xy}\mapsto g_x U_{xy}g_y^{-1}$ change $h_x\mapsto g_x h_x$, $l_e\mapsto l_eg_x^{-1}$ and $r_e\mapsto g_y r_e$. Each edge term is invariant. Reversing an edge exchanges its two frames with their inverses, and quaternion conjugation preserves the diagonal form $H_e$. The construction also respects the lattice orientations under reflections.

**Proved, local read of an actual coefficient.** Let $N_e$ be the number of eigenvalues of $Q_e$ above $1/2$. In the three cases $++$, $--$, and opposite signs, $N_e$ is respectively $2,1,0$. For the first two cases the unperturbed positive eigenvalues are $6,6$ or $2b_e\ge2$. Every other unperturbed eigenvalue is nonpositive. The perturbation has norm at most $3/32$, so the min-max bound gives these counts for every realization. Set $f(Q_e)=1,-1,0$ for $N_e=2,1,0$ respectively. Then

$$
                              f(Q_e)=(s_x+s_y)/2.                         \tag{2}
$$

This read is invariant under orthogonal changes of the local quaternion frame. To extend it continuously with $|f|\le1$, replace the eigenvalue count by a sum of continuous ramps from zero at $1/4$ to one at $3/4$, constant outside that interval. Apply the piecewise linear function taking $0,1,2$ to $0,-1,1$ and staying one above $2$. It has the same values on the stated support.

**Proved, exact edge integration.** For every fixed $U,h,s$, integrating the frame term and its coin gives $A$ at a like-sign bond and $1$ at an unlike-sign bond. Indeed $l_eU_er_e$ has Haar law and $pB_6+(1-p)B_1=A$. With $J=(\log A)/2$ the factor is $\sqrt A\,e^{J\eta_e}$. The resulting joint density, besides the Wilson action and $(\sqrt A)^{|E|}$, is

$$
 \exp\!\left(\sum_{e=xy} K_e(U,h)\,s_xs_y\right),\qquad
 K_e=J+\gamma\big[q(h_x^{-1}U_eh_y)^2-\tfrac14\big].                    \tag{3}
$$

The coupling varies with the gauge field. For example, at fixed frames its values at dressed link $1$ and at a purely imaginary unit differ by $1/8$. An SU(2) centre sign on a link preserves $K_e$. Gauge transformations act simultaneously on $U$ and the site frames and preserve (3). All the scalars acquired in this integration are common per site, since $|E|=4|\Lambda|$ and $|\mathcal P|=6|\Lambda|$.

## 3. The first failed estimate is conditional mixing

**Proved, uniformly in $U,h$ and the centre twist.** After the integration in (3), fix all $U,h$. Write $w_e=e^{2K_e}-1$. Then

$$
 e^{2K_e}\ge A e^{-1/16}>26(15/16)>23,\qquad w_e>22.                    \tag{4}
$$

Expand each spin factor as $e^{-K_e}(1+w_e{\bf1}_{s_x=s_y})$. Summing the fair signs assigns an open edge set $S$ weight proportional to $2^{k(S)}\prod_{e\in S}w_e$, where $k(S)$ includes isolated vertices. Given $S$, each component receives one independent fair sign. In particular $\mathbb E[s_xs_y\mid U,h]$ is the probability that $x,y$ are connected. This is the finite Fortuin–Kasteleyn expansion. Conditional on all other edges, the open-to-closed odds at $e$ are $w_e$ if its endpoints are already joined, and $w_e/2$ otherwise. Its conditional probability of being closed is at most $2/(2+w_e)<1/12$. Conditioning successively gives an upper bound $12^{-k}$ for $k$ specified distinct edges all being closed. These probabilities use the full four-dimensional edge law.

**Proved, correlations of the matrices.** Take two sites $x,y$ in the same spatial coordinate plane, a square torus of side $m\ge4$. If they are disconnected within that plane, the boundary of the open component of $x$ is made of closed edges. Its dual has even degree at every vertex and decomposes into edge-disjoint simple cycles. A path from $x$ to $y$ crosses this boundary an odd number of times. Hence either there is a noncontractible dual cycle, or a contractible simple cycle encloses exactly one of $x,y$ in its disk. The case $x=y$ has connection probability one.

A noncontractible simple cycle has length $k\ge m$. At most $4m^2\,3^{k-1}$ oriented walks can start at a vertex and take $k$ nonbacktracking steps. Each candidate simple cycle uses distinct edges, so the probability cost of all such cycles is bounded by

$$
 \frac{4m^2}{3}\sum_{k\ge m}4^{-k}
   =\frac{16}{9}m^2 4^{-m}\le\frac19.                                \tag{5}
$$

The last bound holds at $m=4$ and decreases, since $(m+1)/(2m)<1$. For a contractible cycle enclosing one specified site, lift its disk to the plane around a fixed lift of that site. Its boundary crosses the horizontal ray to the right on one of the first $k$ bonds, since its coordinate width is at most $k/2$. Fixing the crossed edge leaves at most $2\cdot3^{k-1}$ walks. This counts a possible separator about either site at cost at most

$$
  \frac43\sum_{k\ge4} k4^{-k}
  =\frac43\,4^{-4}\left(\frac4{1-1/4}+
                         \frac{1/4}{(1-1/4)^2}\right)=\frac{13}{432}.
$$

Connection in the plane gives connection in the full graph. Thus $\mathbb E[s_xs_y\mid U,h]\ge 1-1/9-13/432=371/432>5/6$, at every separation in that plane. Global spin reversal in (3) gives zero one-site means. By (2), for any two fine edges $e,e'$ contained in that plane,

$$
 \mathbb E[f(Q_e)\mid U,h]=0,\qquad
 \operatorname{Cov}\big(f(Q_e),f(Q_{e'})\mid U,h\big)\ge371/432.        \tag{6}
$$

The covariance is the average of the four endpoint correlations. The marker in (2) is an exact function of the old coefficients even though (3) has integrated their private frames and coins.

**Proved, at the requested step.** Retain the aligned pivot links $V$ of 1348 with $B=2$ and include the full conditional action when integrating the environment. The pivots are functions of $U$. Conditioning (6) down to $V$ preserves the lower bound and the zero means. Equivalently the same inequalities follow by integrating over the remaining fine links at fixed pivots, all densities being positive. Take $e,e'$ internal to two blocks in the plane. Their original matrices are local reads of the enlarged environment on the two blocks. The block separation can grow without bound on the even tori $m=512v$. Thus no finite $C,\xi$ in §1 work even for these bounded reads. The argument is on the weighted environment that determines the pivot density. The independent reference before weighting already has exact factorization at disjoint sites.

## 4. The same environment fails the two-period pressure test

**Proved, one spin twist on each of the eight gauge backgrounds.** For the reduced joint density (3), let $Z_F^z(v)$ insert a global sign flip of the site spins across the last time seam. This is an auxiliary diagnostic. The sixteen requested masses always have periodic site spins. Fix $U,h$ as before. Put $a_e=-1$ on the temporal seam bonds, $+1$ elsewhere. The expansion with $\mathbf 1_{s_xs_y=a_e}$ gives the same weights on $S$ when every open circuit has product of $a_e$ equal to $+1$, and weight zero otherwise. Indeed the constraint on a spanning forest leaves one free sign per component, and consistency on each remaining edge is exactly this circuit test. The antiperiodic-to-periodic conditional partition ratio is the probability of consistency in the periodic open-edge law above.

Restrict a consistent assignment to one spatial-time coordinate plane of size $m\times v$. The edges on which $a_e s_xs_y=-1$ are closed. Their dual is even because each square has product $+1$. A temporal fundamental circle has product $-1$, so it crosses those dual cycles an odd number of times. At least one simple cycle in their decomposition winds oddly around the spatial direction. To see the parity, lift each cycle to the rectangular cover and count its crossings of the fixed temporal circle modulo two. The count equals its net horizontal displacement divided by $m$ modulo two. Its length is therefore at least $m$. Counting as in (5), now with $mv$ starting vertices, gives the bound pointwise in $U,h$. Multiplying by the positive gauge weight and integrating proves

$$
 0\le Z_F^z(v)\le d_{m,v}Z^z(v),\qquad
 d_{m,v}=\frac{16}{9}mv\,4^{-m}\le\frac19
 \quad (4\le v\le m).                                                    \tag{7}
$$

The auxiliary spin twist is distinct from the centre twist $z$. The latter can change the Wilson plaquette action in (7) by any of its prescribed signs. The bound holds on every such background separately.

**Proved, the transfer trace for the coupled model.** The Wilson layer construction is GL8 of Sussman–Alpoge, with Claude and Codex. Here the slice contains the extra frames and signs. Let $X=(u,h,s)$ denote one spatial slice with its product probability measure. Let $D(X)$ be its spatial Wilson weight $e^{\beta\sum_{p\ {\rm spatial}}q(u_p)}$ times the factors $e^{K_e s_xs_y}$ on its spatial links. For a second slice $Y=(u',h',s')$ and temporal links $a_x$, the kernel is given below. [Outline, GL8, 2313–2335](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L2313-L2335)

$$
\begin{aligned}
 L(X,Y;a)=\exp\bigg\{&
 \beta\sum_{e=xy\ {\rm spatial}}q(u_e a_y (u'_e)^{-1}a_x^{-1})\\
 &+\sum_x\left[J+\gamma\left(q(h_x^{-1}a_xh'_x)^2-\tfrac14\right)\right]s_xs'_x
 \bigg\},\\
 T(X,Y)={}&A^{2m^3}e^{-6\beta m^3}\sqrt{D(X)D(Y)}
                  \int L(X,Y;a)\prod_x da_x .
\end{aligned}
$$

Multiplying the slice kernels counts every spatial term once and every temporal term on its own step. The prefactor accounts for four links and six plaquettes per site. Swapping $X,Y$ and replacing $a_x$ by $a_x^{-1}$ preserves each temporal trace by cyclicity and $q(g^{-1})=q(g)$. The site-frame term has the same property. Thus $T$ is self-adjoint and Hilbert–Schmidt, since its kernel is bounded on a finite product of compact spaces. For even $v\ge4$, $T^v$ is positive trace class.

**Proved, positivity already at one time step.** Write $M(h)=hh^t-I/4$ for a unit quaternion column. Then $\operatorname{tr}(M(h)M(k))=(h\cdot k)^2-1/4$. At $a_x=1$, the logarithm of $L(X,Y;1)$ is the inner product of the two vectors made by concatenating $\sqrt\beta\,u_e$ over spatial edges and $(\sqrt J\,s_x,\sqrt\gamma\,s_xM(h_x))$ over sites, using the Hilbert–Schmidt inner product on matrices. This uses $q(uv^{-1})=u\cdot v$. Exponentiating gives a positive kernel operator $K_0$ by the uniformly convergent sum of tensor-power Gram kernels. For general $a$, $L(X,Y;a)=L(X,a\cdot Y;1)$ under the usual vertex gauge action on links and site frames. The kernel at $a=1$ is invariant under the simultaneous action on both arguments, so $K_0$ commutes with the Haar projection $\Pi$ on slice functions. The integrated operator is $K_0\Pi=\Pi K_0\Pi\ge0$. The two factors $\sqrt D$ and the positive scalar preserve this inequality. This extends the Wilson crossing-factor argument of outline AM2 to the coupled site variables. [Outline, 2775–2795](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L2775-L2795)

Let $C_z$ flip the spatial links crossing the selected spatial cut planes on a slice. Let $F$ reverse all its site spins. Their actions on slice functions are commuting unitary involutions. Applying either action to both slices preserves $T$. For $C_z$, the two copies of a spatial link in a temporal plaquette acquire the same sign, every spatial plaquette has even cut parity, and the dressed-link square is centre-even. For $F$, every spin product is preserved. Cyclic integration of the kernels, with the last slice identified with the transformed first one, therefore gives

$$
 Z^z(v)=\operatorname{Tr}(C_z T^v),\qquad
 Z_F^z(v)=\operatorname{Tr}(C_z F T^v).
$$

For instance the trace formula follows by splitting the cycle into two Hilbert–Schmidt half-kernels and integrating their product. The same construction at $2v$ uses the very same $T$. Set $P_{\rm c}=2^{-3}\sum_z C_z$, the projection onto the centre-invariant subspace. Define $A_\pm=P_{\rm c}(I\pm F)T^v/2$. They are positive, trace class, and have orthogonal ranges. Their traces are $(Z_+(v)\pm Z_{+,F}(v))/2$, where $Z_{+,F}=2^{-3}\sum_z Z_F^z$. Moreover $Z_+(2v)=\operatorname{Tr}A_+^2+\operatorname{Tr}A_-^2$. Since the sum of the squares of nonnegative eigenvalues is at most the square of their sum, (7) yields

$$
 \boxed{\quad P\ \le\
  \tfrac12\left[1+\left(\frac{Z_{+,F}(v)}{Z_+(v)}\right)^2\right]
  \le \tfrac12(1+d_{m,v}^2)\le\frac{41}{81}<\frac{457}{625}.\quad}      \tag{8}
$$

Here the spin parities are both present *inside* the centre-invariant subspace. A bound on twisted versus untwisted gauge mass at one period alone would not detect their contribution. Equation (8) holds for all even $v\ge4$ with $m\ge v$. On the required aspect ratio $m=512v$ its upper bound tends to $1/2$.

## 5. Consequence for a pivot step and a chain

**Proved, compatibility with the twists.** Use the last time bonds and the last spatial bonds in each chosen direction for the cuts. Moving a centre cut to this location just changes signs of representative fine links, which preserves Haar and every edge quadratic. In the seam description the negative plaquettes of orientation $0i$ have both their $0$ and $i$ coordinates on the last bond. At any aligned block factor dividing the sides, they cross both cuts. Each group of $B^2$ fine plaquettes forming a twisted coarse plaquette has the same sign. The pivot change of 1348 consequently carries the eight mass labels on each period, with all environmental constants. One can take $v$ divisible by any specified power of two and keep at least three coarse sites per direction throughout.

For the zero-transverse-corner choice the pivots form vertex-disjoint stars. After (3) the $U$ marginal is gauge invariant for every $z$, by changing the integration variables $h_x$ along with $U$. The forest gauge integral already proved in 1345 and checked in 1347 gives product Haar on those pivot links. In this choice the normalized coarse-link density is exactly one, while the unnormalized density equals $Z^z(\tau)$ everywhere. Thus even a vanishing coarse-link Hessian coexists with (8). [Forest integral, 1345 line 188](gap-blockstep2-astra62.md) · [1347, §6](gap-blockstep2-check-opus.md)

In particular, already at this **first pivot**, absorbing the resulting constants into one bulk pressure $c$ with $\big|\log Z^z(\tau)-c\,|\Lambda_\tau|\big|\le\delta$ on every torus would give $\log P\ge-3\delta$. Equation (8) forces $\delta\ge\frac13\log(81/41)>1/6$, since $e<3<(81/41)^2$. A wrap budget of $1/100$ fails for the unnormalized integral itself.

**Proved, a lower bound on the mass error.** On terminal tori where END-K2 applies, let $\widehat Z^z(\tau)$ be any end-class masses. If a common site adjustment $c|\Lambda_\tau|$ brings each of their log masses within $\delta$ of the exact blocked family, positivity puts the log of each twist average within the same $\delta$ after that adjustment. Since $|\Lambda_{2v}|=2|\Lambda_v|$, the log purities then differ by at most $3\delta$. Invariance of the sixteen masses under exact steps and (8) imply

$$
  \delta\ \ge\ \tfrac13\log\!\left(\frac{457\cdot81}{625\cdot41}\right)
          \ >\ \tfrac1{10}.
$$

Indeed the ratio exceeds $10/7$ and $e^{3/10}<1/(1-3/10)=10/7$. For the relaxed set of all positive mass vectors satisfying just $P\ge p_*=457/625$, the log-mass sup distance is exactly $d=(\log p_*-\log P)_+/3$. The preceding inequality proves the lower bound. Multiplying every short-period mass by $e^{-d}$ and every long-period mass by $e^d$ attains it. Thus this distance is strictly positive and identical before and after every exact pivot or centre-sign disintegration. A particular seminorm can still decrease in one step. A class-wide descent guaranteeing entry is ruled out by (8).

**Proved, robustness under a continuous coefficient law.** Add to each $Q_e$ an independent traceless real symmetric matrix $R_e$. In the nine-dimensional space of such matrices use normalized Lebesgue measure on the operator-norm ball of radius $1/32$ with probability $1-\epsilon$ and on the ball of radius $13$ with probability $\epsilon=2^{-64}$. Both laws are invariant under orthogonal conjugation. Hence $\mathbb E_R e^{u^tR_eu}$ is the same constant for every unit $u$. Integrating the $R_e$ multiplies each mass by a common factor per edge and leaves (8) exact. The new bound is $\|Q_e+R_e\|\le25+3/32<12\beta$.

Given any base coefficient array, the new joint law has a Lebesgue density and its support is the product of the translated radius-$13$ balls. Every such product contains zero in its interior because $\|Q_e\|<13$. Their union and its closure are star-shaped about zero. This proves connected support for the reference law of the coefficient array itself, which can be taken as the entire environment. It still has independent restrictions on collections of edges with disjoint endpoint sets. In finite volume positive weighting preserves this support.

At fixed $U$ and all base variables the conditional probability of drawing the large ball is at most $\epsilon e^{13+1/32}/(1-\epsilon)<2^{-11}$, using $e<4$. On the small ball the spectral ramp still reads (2) exactly. If $b=2^{-11}$, replacing each ideal read by the perturbed one changes either first moment by at most $2b$ and the product moment by at most $4b$. After conditioning on the pivots the covariance of the perturbed coefficient reads is therefore at least $371/432-4b-4b^2>5/6$. A reader using only the matrices still sees the failure when their law is absolutely continuous.

**Scope.** The counterexample belongs to the iterable class in 1348 line 30. The pure Wilson input starts with $Q_e=0$. Its canonical blocked matrices come from the single-cut plaquettes and shared open-box links in 1348 lines 13–28. A proof of drift and pressure control on that narrower family remains open. All new inequalities above have written hand proofs. No numerical calculation or Lean verification was used. A second provider has yet to check this proof. This research note grants no status.

## Next two rows and their decisive outcomes

1. **Test transmission between actual Wilson interfaces. Guessed criterion.** At $\beta=23/10$, take one open $2^4$ box and its eight face neighbours. Use the Wilson measure of the union, including every plaquette contained in it. Form the eight $Q_E$ of its internal interfaces by 1348 (1). For each pair $i\ne j$ bound the maximal absolute correlation $\rho_{ij}$ between centred unit-variance functions of $Q_i$ and $Q_j$ in this finite measure. A certified $\max_i\sum_{j\ne i}\rho_{ij}<1$ supplies a finite candidate bound for transmission from an incoming face to the seven exits. Explicit trial functions whose lower bounds have row sum at least one refute this test. It uses no torus masses.
2. **Test gluing with the charged channels present. Sketched, conditional on row 1.** Keep the full boundary variables of those boxes and every four-linear corner tensor. Test whether the finite contraction survives successive joins and yields a common connected expansion of the unnormalized log integral on all sixteen tori. A decisive positive result gives explicit local-rule and winding-tail bounds meeting 1471's norm, $1/100$ wrap budget and size condition, or an intermediate strict decrement with the scalar error carried to the next step. A Wilson boundary mode violating the proposed contraction under a join refutes that extension. An estimate only on the normalized pivot marginal leaves the pressure undetermined.
