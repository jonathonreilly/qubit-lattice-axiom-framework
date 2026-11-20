## Repo search

**GUIDE.** Row 1304 at `e1176ef2d`. The target-specific prior digest is absent. The question is whether a positive object controls propagation of centre-neutral Wilson observables at a fixed physical distance. I test two proposed signs on the actual finite Wilson measure. They concern association of neutral plaquette observables and positivity of mixed slab determinants after ordering the boundary configurations.

**GUIDE.** The lead’s November 8 digest covers thirteen earlier construction obligations. On main at `8b11ae2bb9` I checked its finite-clock Villain example (September 14 note, lines 79–94) and its determinant-weighted Dirichlet Maxwell bound (companion note, lines 120–145). Both use other measures. PR 10114 gives a positive one-step Wilson witness (MASS_GAP_LOCAL_BLOCK_ASTRA, 103–149). Grok’s PRs 10133 and 10134 contain a conditional crossover reduction and a common-trajectory requirement, respectively. PR 10141 identifies its material as a snapshot. [Lead’s source list and ranges](prior/repo-search-2026-11-08.md).

**GUIDE.** Claude Opus’s row 1213 asks for the sign of general adjoint Haar moments. Its three examples were positive in Codex’s check. The fundamental-trace counterexample there uses spin one-half. The adjoint test uses spin one, so it survives independent changes of the lift of every link. The open registry has no matching owner. [Row 1213, §4](gap-mini-solve-n-fable.md) · [Row 1247, §N](gap-solve-batch4-check-astra.md).

**GUIDE.** The geometric input is Codex’s 88-plaquette projective plane in row 1127. Claude Fable constructed an earlier 92-plaquette example in row 737. The earlier surface calculations are due to Jean-Michel Drouffe and Jean-Bernard Zuber, and to Edward Witten. I use the first construction and row 1213’s disk-gluing identity. The new operation is to fill the one-sided core by another plaquette disk. It tests a branched support with integer spin on every face. [Row 1127, step 3](gap-w-astra62.md) · [Row 737, §2.4](gap-means-max.md) · [Literature record](prior/gap-lit-assoc.md).

**GUIDE.** The indexed outline of Ethan Sussman and Levent Alpoge, whose text was authored with Claude and Codex, separates scalar reconstruction from a gap. Its example at lines 588–599 and 31858–31882 has positive spectral density down to zero. Lines 3712–3721 explain the inverse-square loss of the reflection estimate. CA-I 2698–2711 states the scope of the curvature semigroup. Balaban’s ultraviolet construction supplies no infrared premise here. Levent Alpoge’s unrefereed remark with Claude describes Stepanov multiplicity, determinants of periods, theta lifts, and the explicit formula of Guinand and Weil. It motivates testing the sign created by a multiplicity-two boundary. The Wilson proof below uses the squaring map on $SU(2)$. [Outline](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex) · [CA-I](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex) · [Alpoge and Claude, pp. 2–4](https://alpo.ge/remark.pdf).

## The sign at a doubled boundary

**PROVED.** Let $g$ have normalized Haar law on $SU(2)$. Write $\chi_j$ for the spin-$j$ character. Then
$$
\int \chi_1(g^2)\chi_1(g)\,dg=-1.
$$
At eigenvalues $e^{\pm i\theta}$ the spin-one character is $1+2\cos(2\theta)$. The spin-two character adds $2\cos(4\theta)$ to this. Hence $\chi_1(g^2)=\chi_2(g)-\chi_1(g)+1$. Character orthogonality gives the integral. Equivalently, exchanging the factors in the tensor square of the three-dimensional rotation representation acts by minus one on its exterior square, which is the same rotation representation.

**GUIDE.** To realize this sign with each *elementary plaquette used once*, one disk must read $g^2$ and the other $g$. They must have separate interior link variables. An abstract attaching word alone would leave this lattice requirement open.

## A product of distinct elementary adjoint characters

**PROVED.** There is a set $P$ of 104 distinct plaquettes in the ordinary four-dimensional cubical lattice such that
$$
\mathbb E_0\prod_{p\in P}\chi_1(U_p)=-3^{-102}.
\tag{1}
$$
Here $U_p$ is the ordered boundary product and $\mathbb E_0$ uses independent normalized Haar links. Every torus of side lengths at least five contains this example. The observable is invariant under changing the sign of any link.

**PROVED (lattice attachment).** Use the first two pieces of row 1127’s step 3. In the first coordinate plane take $B=[-2,2]^2$, with centre $b$, boundary $C_0$, and midpoints $v_\pm=(0,\pm2)$. In the second plane take $Q=[-1,1]^2$, with centre $o$ and side midpoints $E,N,W,S$. The left half of $C_0$ carries the interval $WE$, the right half the interval $SN$. At $v_+$ join the intervals by the opposite quadrant squares $EN,WS$. At $v_-$ use $NW,SE$. Following the endpoint $E$ around the base takes it through $N$ to $W$. These 36 squares form the Möbius band of the cited construction. Its core is $C=C_0\times\{o\}$. The sectors at a joint connect the two half-fibres in pairs. Cutting the band along $C$ opens it to a cylinder. One rim is the old boundary. The other follows $C$ twice in the same direction, since the two sides exchange after one circuit.

**PROVED (cap and new disk).** The cited cap starts with $\{b\}\times Q$. Each quadrant arc of $\partial Q$ is joined to its joint by the rectangle $[b,v_\pm]\times\text{arc}$. At $E,W$ fill the left half of $B$, and at $N,S$ fill the right half. Each rectangle attaches on one boundary arc. Each half-square then attaches along the diameter through $b$. This is a disk of $4+16+32=52$ faces. Its free boundary is the old rim of the band. Write $A$ for band plus cap. Cutting $A$ along $C$ therefore gives a disk of $a=88$ faces with boundary word $C^2$, up to orientation and cyclic origin.

**PROVED.** Add $D=B\times\{o\}$, tiled with $d=16$ plaquettes. The band meets $D$ along $C$. Of the cap pieces, only $\{b\}\times Q$ meets $D$, at the single vertex $(b,o)$. The rectangles and half-squares have second coordinate on $\partial Q$. Thus all shared **links** of $A$ and $D$ are exactly the links of $C$. The extra common vertex carries no integration variable. Each interior link of the cut disk corresponds to a different lattice link. Only its boundary maps two-to-one on the core links. The two copies of a core edge have the same holonomy on their two boundary traversals. All faces lie in $B\times Q$, whose coordinate spans are $4,4,2,2$. This proves the claimed embedding and its link identifications.

**PROVED (disk integration).** For central inversion-invariant plaquette weights on a cellulated disk, integration over interior links gives their group convolution at the boundary holonomy. To see this, merge faces along a spanning tree of the face adjacency graph. At a common edge the two oriented boundary words contain $u,u^{-1}$. Integrating $f(Xu)h(u^{-1}Y)$ gives $(f*h)(XY)$. Orient each face consistently in the cut disk and start each trace at the common edge. After the merges, unused interior edges form a forest. A cycle of unused edges, or a path of them between two distinct boundary vertices, would separate faces and disconnect the chosen dual tree. Each component has one boundary root. Indeed the disk Euler formula leaves exactly as many unused interior edges as there are interior vertices, after removing one fewer edge than faces. Counting components, including isolated boundary vertices, then gives one root per component. Every remaining interior edge then cancels with its inverse by stripping leaves from the merged word. Its Haar integral is one. Central weights commute under convolution. This proof first fixes the disk boundary links independently and hence permits their later identification along $C$.

**PROVED (evaluation).** Matrix orthogonality gives $\chi_1*\chi_1=\chi_1/3$. In detail, conjugation invariance makes the Haar average of $R(u)XR(u)^{-1}$ scalar for the irreducible three-dimensional representation $R$. Its trace gives $(\operatorname{tr}X)I/3$. Applying this to matrix units gives the convolution identity. Conditional on the core links, the cut disk contributes $3^{1-a}\chi_1(g^2)$ and $D$ contributes $3^{1-d}\chi_1(g)$, where $g=U(C)$. The remaining $g$ is Haar because $C$ is simple and each edge occurs once. The doubled-boundary integral above now gives (1). The projective plane on its own gives $+3^{1-a}$ since $\int\chi_1(g^2)\,dg=1$. The extra disk selects the negative spin-one coefficient.

## Failure of adjoint plaquette association at every finite Wilson coupling

**PROVED.** On any finite periodic four-dimensional cubical lattice containing $P$ without identifications, use the Wilson density proportional to $\exp(\sum_p\beta_p x(U_p))$, where $x(g)=\tfrac12\operatorname{tr}g$ and $|\beta_p|\le b_0<\infty$. Fix one marked face $p_*$ of $D$. Write $Y_p=\chi_1(U_p)=4x(U_p)^2-1$ and put
$$
G=1+Y_{p_*},\qquad F_n=\prod_{p\in P\setminus\{p_*\}} (1+Y_p)^n,\qquad n\ge1.
$$
Let $L$ be the links of $P$ and $s$ the number of ambient plaquettes touching at least one link of $L$. Put $K=\exp(2s b_0)$. One may use $s\le 24\cdot104$. Then
$$
  0\le \frac{\mathbb E_\beta [F_n G]}{\mathbb E_\beta F_n}
       \le \frac{294 K^2}{n+2},
  \qquad \mathbb E_\beta G\ge K^{-1}.
\tag{2}
$$
In particular $n+2>294K^3$ gives $\operatorname{Cov}_\beta(F_n,G)<0$. The two functions are bounded, nonnegative and coordinatewise increasing on $[-1,3]^P$. Their **plaquette** supports are disjoint. They are local gauge-invariant observables and are invariant even under independent link sign changes. Association of the natural adjoint plaquette field would require the opposite inequality. The same $n$ works for every volume and all exterior link values under the stated bound on couplings.

**PROVED (the squared-loop Jacobian).** For any continuous central $q$ on $SU(2)$,
$$
  \int 4x(g)^2 q(g^2)\,dg=\int q(h)\,dh.
\tag{3}
$$
Indeed write $x(g)=\cos\theta$, $0\le\theta\le\pi$. Normalized Haar measure on class functions is $2\sin^2\theta\,d\theta/\pi$, from the unit three-sphere volume form. Multiplication by $4\cos^2\theta$ gives $2\sin^2(2\theta)\,d\theta/\pi$. On the two halves of the interval use $\phi=2\theta$ and $\phi=2\pi-2\theta$. Both have $x(g^2)=\cos\phi$, and their half Jacobians add to one. Write $A(q)=\int q(g^2)\,dg$. If $q\ge0$, $q(-h)=q(h)$ and $\int q=1$, (3) also gives
$$
 A(q)=\int \frac{q(h)}{2(1+x(h))}\,dh
     =\frac12\int\frac{q(h)}{1-x(h)^2}\,dh
     \ \ge\ \frac{1}{2\int(1-x(h)^2)q(h)\,dh}.
\tag{4}
$$
The first equality holds for every nonnegative continuous central $q$, including centre-asymmetric weights. Apply (3) with the denominator $2(1+x(h))+\varepsilon$ under $q$ and let $\varepsilon\downarrow0$. The trace-zero class is Haar null. The second equality averages the two centre lifts. The inequality follows from Cauchy–Schwarz for reciprocal positive functions. Thus projection onto the double boundary increases the weight of core holonomies of small fundamental trace.

**PROVED (one convolution coefficient).** Set $u(g)=4x(g)^2=1+\chi_1(g)$, $c_n=\int u^n\,dg$ and $h_n=u^n/c_n$. It is a nonnegative, central and centre-even probability density. Convolution by $h_n$ multiplies $\chi_1$ by
$$
 \lambda_n=\frac13\int h_n\chi_1\,dg=\frac{n}{n+2}.
\tag{5}
$$
For the convolution identity, the integral of the rotation matrix against $h_n$ commutes with every rotation and is scalar. Its trace fixes the scalar. For the value, $c_n$ is proportional to $4^n\int_0^{\pi/2}\sin^2\theta\cos^{2n}\theta\,d\theta$ with a common constant. The integral of the derivative of $\sin^3\theta\cos^{2n+1}\theta$ is zero on that interval. Expanding the derivative gives the ratio $c_{n+1}/c_n=4(2n+1)/(2n+4)$. Subtract one and divide by three to obtain (5).

**PROVED (the Haar estimate).** In a quotient of expectations with $F_n$ one can replace each $u^n$ by $h_n$. Let $q=h_n^{*a}$, with $a=88$, and $Z=A(q)$. The cut disk has conditional weight $q(g^2)$ by disk integration. The marked disk $D$ has $d-1=15$ weights $h_n$. With weight $1$ on its marked face it integrates to $1$. With weight $G$ there, it integrates to $1+\lambda_n^{15}\chi_1(g)$, by (5). These are functions of the same core holonomy $g$. Identity (3) gives $\int\chi_1(g)q(g^2)\,dg=1-Z$. Therefore
$$
 \frac{\mathbb E_0[F_nG]}{\mathbb E_0F_n}
   =1-\lambda_n^{15}+\frac{\lambda_n^{15}}{Z}.
\tag{6}
$$
The even density $q$ has $\int\chi_1 q=3\lambda_n^{88}$. Since $1-x^2=(3-\chi_1)/4$, (4) yields $Z^{-1}\le\tfrac32(1-\lambda_n^{88})$. For $0\le\lambda\le1$, $1-\lambda^r\le r(1-\lambda)$ by the finite geometric sum. Substitution in (6) gives $(15+3\cdot88/2)\,2/(n+2)=294/(n+2)$. The unweighted $\mathbb E_0 G=1$ by character orthogonality.

**PROVED (comparison to the actual measure).** Condition on all links outside $L$. Only the $s$ incident plaquette factors depend on the remaining links. Their combined exponent lies in $[-s b_0,s b_0]$. After normalization the conditional density lies between $K^{-1}$ and $K$ relative to product Haar on $L$. Each of the at most $4\cdot104$ links belongs to at most six ambient plaquettes. This proves the stated bound on $s$. Both $F_nG$ and $F_n$ are nonnegative and $\mathbb E_0 F_n>0$. The density bounds hence compare their quotient with its Haar value with factor $K^2$. They also give $\mathbb E_\beta G\ge K^{-1}$. The bounds hold conditionally and survive averaging the individual expectations over the exterior, proving (2). The same argument applies to any infinite-volume Wilson Gibbs law with this finite-link conditional specification.

**PROVED (which character inequalities fail).** At the same $n$ as in (2), the mean of $Y_{p_*}$ under the reweighting by $F_n$ is negative. Expand $F_n$ by the binomial theorem. All coefficients are nonnegative. Some product of powers of the elementary adjoint characters therefore has negative Wilson mean. Some pair of such monomials on disjoint plaquette sets has negative Wilson covariance, by expanding $\operatorname{Cov}_\beta(F_n,G)$. Equivalently one may expand each power into irreducible characters, with nonnegative integer multiplicities from the tensor product. All spins in that expansion are integers. At general $\beta$ the powers or spin labels may depend on $\beta$. Equation (1) specifies the much simpler label one on every occupied face at $\beta=0$.

**PROVED (a response to positive adjoint sources).** In (6) one may replace $h_n$ by the probability density proportional to $\exp(tY)$ with $t\ge0$. Its coefficient $\lambda(t)=\int Y h_t/3$ tends to one. Indeed the weight of $Y\le3-\delta$ divided by the weight of $Y>3-\delta/2$ is at most $e^{-t\delta/2}/\Pr_0(Y>3-\delta/2)$, and the latter probability is positive. Thus (4) and (6) again send the reweighted mean of $G$ to zero. Add $tY_p$ to the exponent on all 103 unmarked faces. At $t=0$ the mean of $G$ is positive. At some finite $t>0$ its derivative is negative. Differentiation on this finite lattice expresses the derivative as the sum of $\operatorname{Cov}(Y_{p_*},Y_p)$ over the unmarked faces. At least one elementary pair therefore has negative covariance in this positively sourced measure. At homogeneous coupling (2) itself gives the increasing pair.

## The fundamental Wilson plaquette at weak as well as strong coupling

**GUIDE.** A contractible fundamental plaquette is neutral under a global electric centre symmetry. Its trace also enters the Wilson action itself. The adjoint theorem tests variables that forget every link sign. To reach the fundamental trace at arbitrary finite coupling, the pin on a doubled loop must distinguish the two roots $+I$ and $-I$. A second punctured projective plane supplies exactly the singular density in (4), before averaging the two lifts. The following construction uses ordinary positive fundamental plaquette sources.

**PROVED (two successive double boundaries).** There is a fixed set of 203 elementary plaquettes with one marked face $p_*$ on every periodic four-dimensional lattice with all sides at least eight. For each bound $b_0<\infty$ and each $\eta>0$ there exist finite *positive* source strengths on its unmarked faces such that
$$
   F=\exp\!\left(\sum_{p\ne p_*}t_p x(U_p)\right),
   \qquad
   \frac{\mathbb E_\beta[F(1+x(U_{p_*}))]}{\mathbb E_\beta F}<\eta
\tag{7}
$$
for all Wilson couplings $|\beta_p|\le b_0$. Only the unmarked faces of this set enter the sum. The strengths can take just two values. At every finite homogeneous coupling the fundamental plaquette field thus also has a pair of increasing functions with negative covariance. This extends the small-coupling fundamental example in rows 1213 and 1247.

**PROVED (where the second surface fits).** Take the preceding 104-face set in coordinates $(x_1,x_2,z,w)$. Mark the face $[1,2]\times[0,1]\times\{(0,0)\}$ of $D$. Translate a second copy of the 88-face projective plane by $(3,0,4,0)$. Before translation its cap has the face $[-2,-1]\times[0,1]$ at $W=(-1,0)$ in the $(z,w)$ plane. Remove the interior of that face. Its translated boundary lies directly over $\partial p_*$ at $z=3,w=0$. Join these two square rims with the twelve side faces of the straight tube in $0\le z\le3,w=0$. Call the punctured plane and tube $M$, with $87+12=99$ faces.

**PROVED.** The first projective plane only reaches $z=1$. Over $[1,2]\times[0,1]$ its right strip has $z=0$ and its cap pieces there have $z=0$. The pieces at $E,W$ lie in the left half of $B$, and the radii lie at $x_1=0$. Hence the open tube misses the first set. The second plane has $z\ge3$ and meets the tube only on its top rim. The links common to $M$ and the first set are precisely $\partial p_*$. The second plane’s removed face is disjoint from its core, which lies at $z=4,w=0$. Cutting it on that core yields a disk with one interior square removed. Adding the tube extends this annulus. Filling its bottom rim by a single face makes it a disk again, with doubled core as outer boundary. The full coordinate spans are at most $7,4,6,2$, as required for the torus.

**PROVED (the weight contributed by $M$).** Write $k_t(v)=e^{t x(v)}/\int e^{t x}$ for $t>0$, using normalized Haar measure throughout. Give each of the 99 faces of $M$ this weight. For fixed bottom rim links, integration inside $M$ gives a central function $W_t(h)$ of their holonomy $h$. Boundary gauge changes set three links of the simple rim to the identity by changing variables inside. The remaining common conjugation gives centrality. Haar integration of the continuous weights on a compact space gives continuity. For any continuous central test $f$, fill this rim with the weight $f(h)$. Cutting on the second core and applying disk convolution proves
$$
 \int f(h)W_t(h)\,dh
 =\int (k_t^{*99}*f)(v^2)\,dv
 =\int f(h)(k_t^{*99}*\rho)(h)\,dh,
 \qquad \rho(v)=\frac1{2(1+x(v))}.
\tag{8}
$$
At $-I$ give $\rho$ any value in the integral. It is the Haar density of the square of a Haar element, by (3) and monotone convergence, and has total integral one. Convolution by a real inverse-symmetric kernel is self-adjoint for Haar integration, by substitution and Fubini. This proves the last equality. It also gives $W_t=k_t^{*99}*\rho$ everywhere since both sides are continuous central functions.

**PROVED (behaviour at the two roots).** For any fixed positive integer $m$, $k_t^{*m}$ is a probability density concentrating at $I$ as $t\to\infty$. Its supremum outside every neighbourhood of $I$ tends to zero. For $k_t$ itself the normalized supremum on $x\le u<1$ is bounded by $e^{-t(v-u)}/\Pr_0(x\ge v)$ for any $u<v<1$. For a neighbourhood $V$ choose a neighbourhood $U$ of $I$ such that a product of $m$ elements of $U$ lies in $V$. In the convolution integral outside $V$, at least one factor is outside $U$. The corresponding truncated factor has vanishing supremum. Convolution to its left and right by probability densities preserves a supremum bound. Summing these $m$ bounds proves the assertion. Convolution with a continuous function therefore converges uniformly to that function, by compactness and uniform continuity.

**PROVED.** It follows that
$$
                W_t(I)\longrightarrow \tfrac14,
        \qquad W_t(-I)\longrightarrow+\infty .
\tag{9}
$$
For the first limit, near $I$ the weight $\rho$ is continuous with value $1/4$. Away from $I$ its integral is finite and the kernel supremum tends to zero. For the second limit use $\rho(-v)=1/[2(1-x(v))]$. For any $A_0>0$ it exceeds $A_0$ on a sufficiently small punctured neighbourhood of $I$. The mass of $k_t^{*99}$ there tends to one.

**PROVED (evaluation at the marked face).** On the original 103 unmarked faces use $k_r$ and on $M$ use $k_t$. Constants normalizing the two kernels cancel in (7). After integrating $M$, the weight on the marked face of $D$ is $W_t(h)f(h)$, where $f$ is the marked test. Disk integration on the original two disks gives, up to the same source normalization for all $f$,
$$
 I_{r,t}(f)=\int k_r^{*88}(g^2)\,[k_r^{*15}*(W_t f)](g)\,dg.
\tag{10}
$$
At fixed $t$, the bracket converges uniformly to $W_t f$. The probability measure proportional to $k_r^{*88}(g^2)\,dg$ converges to $(\delta_I+\delta_{-I})/2$. Indeed its normalizer is $\int k_r^{*88}(v)\rho(v)\,dv\ge1/4$. Outside any neighbourhood of the two roots, $g^2$ stays a positive distance from $I$, so the density there tends uniformly to zero. The two masses are equal by $g\mapsto-g$. Taking $f=1+x$ and $f=1$ now gives
$$
 \lim_{r\to\infty}\frac{I_{r,t}(1+x)}{I_{r,t}(1)}
   =\frac{2W_t(I)}{W_t(I)+W_t(-I)}.
\tag{11}
$$
This tends to zero with $t$ by (9). In words, the first constraint gives the marked loop two possible central values. The second surface assigns a divergent relative weight to the negative value.

**PROVED (finite parameters and homogeneous base law).** As in (2), use $K'=\exp(2s'b_0)$ with $s'\le24\cdot203$. The actual quotient in (7) is at most $(K')^2$ times its Haar value because both integrands are nonnegative. First choose finite $t$ so the right side of (11) is below $\eta/(2(K')^2)$. Then choose finite $r$ so the Haar quotient is below $\eta/(K')^2$. This proves (7) uniformly in the exterior. Without added sources, $\mathbb E_\beta(1+x(U_{p_*}))\ge(K')^{-1}$ since its Haar mean is one. Taking $\eta<(K')^{-1}$ proves the claimed negative covariance under the *original* measure.

**PROVED (an ordinary Wilson response).** Start from any homogeneous $\beta\ge0$, fix the strengths just chosen, and multiply all of them by $s\in[0,1]$. This is an ordinary Wilson law with nonnegative, spatially variable plaquette couplings. By (7) the mean of the marked trace decreases between the endpoints. At some interior $s$ its derivative is negative. The derivative equals $\sum_{p\ne p_*}t_p\operatorname{Cov}_s(x(U_{p_*}),x(U_p))$, by differentiating bounded finite-volume integrals. At least one pair of distinct elementary plaquettes has negative trace covariance with those inhomogeneous couplings. The assertion for a homogeneous measure is the increasing-function violation in (7).

## Can the neutral slab determinant have one sign?

**GUIDE.** The preceding tests concern local source monotonicity. For propagation in time there is a direct determinant to test. If $T$ is the positive transfer operator in the neutral sector, $\bigwedge^2 T$ has leading eigenvalue $\lambda_0\lambda_1$ whenever $\lambda_0,\lambda_1$ are its two largest eigenvalues, counted with multiplicity. This follows on the vectors $\phi_i\wedge\phi_j$ in an eigenbasis of $T$. Dividing by $\lambda_0^2$ gives the first neutral excited ratio. Row 1081 uses a Karlin–McGregor determinant with a fixed order of spin labels on a one-dimensional reduced problem. The trace identity in the earlier council note also uses an exterior square. Here the labels are the actual spatial boundary configurations of the Wilson slab. [Row 1081, §5.1](gap-descent-sign.md) · [Council note, V1–V4](gap-council-conf-fable.md).

**PROVED (exchange obstruction).** Let $K$ be a real continuous symmetric kernel on a metric space $X$. For ordered $k$-tuples $P,Q$ of distinct points write $D(P,Q)=\det[K(P_i,Q_j)]$. Suppose $D(P,P)>0$ all along a continuous path of such tuples from $P_0$ to a transposition of $P_0$. No orientation of unordered tuples makes every mixed determinant nonnegative. Indeed such an orientation is a sign $e(P)$ alternating under permutations. Near each path time $s$, continuity gives $D(P_s,P_{s'})>0$ for $s'$ sufficiently close to $s$. Nonnegativity of $e(P_s)D(P_s,P_{s'})e(P_{s'})$ forces equal signs there. A locally constant sign on the interval is constant, which contradicts its reversal at the endpoint.

**PROVED (almost-everywhere version).** Assume the reference probability on $X$ has full support and $D(P,P)>0$ on all distinct tuples. If an alternating measurable sign made the kernel nonnegative almost everywhere, each tuple would have an open neighbourhood $U$ with $D>0$ on $U\times U$. Both signs cannot have positive measure there. The almost-sure sign on $U$ is unique, because every nonempty open subset of the distinct-tuple space has positive product measure. Thus signs on intersecting neighbourhoods agree. They define a locally constant sign, and swapping two entries reverses it because product measure is permutation invariant. The same path gives the contradiction. Allowing different real orientation signs on the incoming and outgoing boundaries also fails. On $U\times U$ positivity forces both signs to be the same constant almost everywhere.

**PROVED (strict Gram matrices on neutral Wilson boundaries).** Fix a spatial three-torus of side $N\ge5$ and a homogeneous $0<\beta<\infty$. Let $B_s=SU(2)^{E_s}$ be its spatial link configurations. Quotient by vertex gauges and by the three electric centre flips on spatial seams. Denote the compact orbit space by $X$ and the pushforward of product Haar by $m$. The group acts by isometries on the tuple of quaternions. The minimum Euclidean distance between two compact orbits therefore defines their quotient metric. The preimage of each nonempty open set is open and nonempty in the product group. Thus $m$ has full support. Functions on $X$ are the gauge-invariant, zero-electric-flux sector. The one-step symmetric kernel of the transfer operator on this space is
$$
 K_1([u],[v])=w(u)w(v)\int_{\mathcal H} C(u,hv)\,dh,
 \qquad C(u,v)=\exp\!\left(\beta\sum_{e\in E_s}u_e\cdot v_e\right),
\tag{12}
$$
up to a positive scalar. Here the links are unit quaternions, $w$ is the exponential of half the spatial Wilson exponent, and $\mathcal H$ is the compact group just quotiented. Temporal plaquettes give the quaternion dot products. Integrating the timelike links gives the vertex average. Averaging over the commuting centre flips inserts the neutral projection. Both $w$ and $C$ are invariant under the required simultaneous transformations, with $w$ strictly positive. This is the symmetric spatial-weight convention of row 667. The one-bond expansion and vertex projection are also in Sussman and Alpoge’s outline, authored with Claude and Codex, lines 2195–2243, 2313–2335 and 2834–2860. [Row 667, N.3–N.7 and §§1–2](gap-transfer.md).

**PROVED.** The quadratic form of $C$ is strictly positive on every nonzero finite real signed measure $\sigma$ on $B_s$. As in row 667, expand the exponential of the Euclidean dot product of the concatenated quaternion coordinates. Its quadratic form is a sum of squares of all coordinate monomial moments. A degree $j$ ordered monomial has positive weight $\beta^j/j!$. The series can be integrated termwise since the configuration space is compact and the measure finite. If the form vanishes, all moments vanish. It then follows by the same expansion that for *every* $r>0$ the kernel with $r$ in place of $\beta$ integrates to zero against $\sigma$ at every $v$. After dividing by its one-slice Haar integral this kernel is a product of the one-link densities $k_r(u_e v_e^{-1})$ in (8). Its convolution sends any continuous function uniformly to that function as $r\to\infty$, by the concentration proof above on finitely many links. Testing against a continuous function and taking this limit forces $\sigma=0$.

**PROVED.** Lift a signed measure $\nu$ on $X$ by the uniform probability on each orbit. Its projection recovers $\nu$, so multiplication of this lift by $w>0$ preserves nonzeroness. The quadratic form of (12) on $\nu$ equals that of $C$ on this weighted lift. Thus it is strictly positive for every nonzero $\nu$. In particular $T\nu$, the continuous function obtained by integrating $K_1$ against $\nu$, is nonzero. It remains a nonzero measure when multiplied by $m$, by full support. For the kernel $K_t$ of any positive integral power $T^t$, strict positivity follows by iteration. At $t=2j$ the form is $\int|T^j\nu|^2\,dm$. At $t=2j+1$ use the one-step form on $(T^j\nu)m$, with the case $j=0$ given by (12). Taking $\nu$ to be any nonzero linear combination of point masses at distinct orbits gives strictly positive definite Gram matrices of every finite size. Continuity of each $K_t$ follows by integration of continuous kernels on a compact space.

**PROVED (exchange within the neutral quotient).** Take two link-disjoint elementary spatial plaquettes. Set one link on each to $\operatorname{diag}(e^{i\alpha_i},e^{-i\alpha_i})$ and all other links to $I$. Vary $(\alpha_1,\alpha_2)$ in a small open rectangle in $(0,\pi/2)^2$. The two adjoint plaquette traces $4\cos^2\alpha_i-1$ distinguish all these orbits, even after quotienting by the centre. Hence a parameter circle gives a circle of distinct neutral boundary configurations. Put two configurations at opposite ends of a diameter. A half-turn exchanges them without collision. For a $k$-tuple with $k>2$ keep the other $k-2$ configurations fixed at distinct parameter points off the circle. This gives the path in the exchange obstruction.

**PROVED (scope of the determinant result).** For every integer thickness $t\ge1$ and integer multiplicity $k\ge2$, no ordering or alternating sign choice on the actual neutral boundary tuples makes the mixed minors of $K_t$ pointwise nonnegative, or nonnegative almost everywhere. In particular one cannot integrate nonnegative auxiliary weights to each such oriented minor, including after summing internal labels with fixed boundary tuples. The actual exterior-power operator does have positive principal Gram determinants. Its mixed determinants enter composition across a slab cut. The obstruction applies precisely when those mixed quantities must themselves have one sign for each pair of boundary tuples. Changing the boundary observables, projecting onto a smaller ordered family, or using cancellations between different boundary tuples would require a different argument.

## Consequences for the neutral inequality

**PROVED (size of the association failure).** At fixed finite coupling, even a positive constant $c$ in
$$
        \mathbb E(FG)\ge c\,\mathbb E F\,\mathbb E G
$$
cannot work for all nonnegative increasing functions of the adjoint plaquette traces. The quotient on these examples is at most $294K^3/(n+2)$. Equation (7) gives infimum zero also for fundamental traces. Thus neither plaquette field can be an increasing coordinatewise image of an associated auxiliary law. Indeed the pullbacks of $F$ and $G$ would both be increasing and would have nonnegative covariance. For example the mixed source determinant $\det\bigl(\begin{smallmatrix}1&\mathbb EG\\ \mathbb EF&\mathbb E(FG)\end{smallmatrix}\bigr)$ is strictly negative for the displayed witnesses. Expressing it as an integral of nonnegative principal Gram determinants would contradict this sign. The local tests on neighbouring plaquettes share boundary links.

**PROVED (straight square Wilson loops).** The same obstructions to association hold for the traces of holonomies of straight square loops of any fixed integer side $l\ge1$ in lattice units, once the torus contains the corresponding enlarged configurations. Scale all coordinates by $l$ and replace each old link by its straight path of $l$ fine links. Distinct old links use disjoint sets of fine links, so their products are independent Haar at zero coupling. This gives exactly the Haar calculations above. Condition on the exterior of the union of the path links as in (2). There are at most $4l$ times the number of old faces in path links. The density comparison remains finite for every fixed $l$ and $\beta$. The powers and source strengths chosen in the two proofs may depend on both.

**PROVED (second evaluation of (1)).** Row 1213’s Lemma PAR gives a local tensor check of the sign and power of three. Split the isolated common vertex $(b,o)$ into its two copies. The link integral uses the same edge variables. The regular links carry two adjoint matrix factors. Their Haar projector is $\delta\otimes\delta/3$. Each of the $c=16$ core links carries three, with projector $\varepsilon\otimes\varepsilon/6$. The second formula follows because the rotation-invariant alternating volume spans the invariant tensors of degree three. For instance, invariance under half-turns about the axes forces each surviving index triple to use all three axes, and signed axis permutations then impose alternation. Averaging is the orthogonal projection, and the squared norm of $\varepsilon$ is six.

**PROVED.** At a smooth vertex the index loop gives three. At a core vertex the three local sheets connect the two core links. Contracting their two alternating tensors gives six times the sign of the permutation of the sheets across that vertex. The product of permutations around $C$ exchanges the two sides of the cut disk and fixes the sheet from $D$. The product of signs is minus one. Write $V,E$ for the vertex and edge counts after splitting $(b,o)$. Gluing two disks on their boundary circles to a single circle preserves $V-E+104=2$, since both removed boundary circles and the common circle have Euler characteristic zero. Multiplying the local factors gives $-3^{(V-c)-(E-c)}=-3^{-102}$. This check uses edge projectors directly, without replacing the support by a single character integral. [Row 1213, Lemma PAR](gap-mini-solve-n-fable.md).

**OPEN.** For the repository’s neutral thermal criterion, let $T_j$ be the periodic Wilson transfer on a spatial cube of side $n_j=L/a_j$ and let $\lambda_{0,j}$ be its vacuum eigenvalue. For the required aspect $K_{\rm asp}$, one needs an admissible physical $L$ such that, at every sufficiently fine cutoff, $4\mid n_j$ and some integer $3\le u_j\le n_j/K_{\rm asp}$ satisfies
$$
        \operatorname{Tr}_{\rm neutral}(T_j/\lambda_{0,j})^{u_j}-1\le\tfrac12 .
$$
The source counterexamples give no upper bound on this trace. The determinant obstruction concerns the sign of mixed minors. The slab criterion (RR) asks for a small *absolute* logarithmic cross-ratio with its specified constants. It remains open. The reflected Gram identity AK33 in the Sussman–Alpoge outline (29467–29482) concerns the inner products of point vectors. It is compatible with both obstructions. A different positive construction could still yield the neutral estimate. The continuum construction and a strictly positive spectral gap above the vacuum in the sense of Arthur Jaffe and Edward Witten remain open here. [Neutral criterion, §1.1](gap-mini-neutral2-fable.md) · [Slab criterion, §6](gap-mini-solve-ag-opus.md) · [Row 1265 check](gap-ws-check-astra.md).

**GUIDE.** Codex research text at the assigned pin. All evaluations and limiting arguments above are by hand. The new arguments await a separate reader’s check. This note grants no science status.

RESULT: PROVED in this research note — the adjoint and fundamental plaquette fields each violate association at every finite homogeneous Wilson coupling on sufficiently large tori, and no boundary orientation makes all mixed neutral slab minors nonnegative at positive coupling. OPEN — the neutral thermal estimate and the four-dimensional SU(2) Yang–Mills mass gap.
