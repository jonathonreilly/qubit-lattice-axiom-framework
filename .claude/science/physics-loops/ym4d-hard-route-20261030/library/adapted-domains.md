# State of attack

**discharged (result of the attack).** On whole-cell regions with generated local patterns, Sections 2--4 construct a critical primitive on a uniformly enlarged chart about every sufficiently small intrinsic graph ball. The box estimate, lattice folding, metric covering/maximal estimate and fixed-dilation Gehring argument have hand proofs below. Large radii are handled by energy monotonicity, and the subset/layer estimate is included. No conclusion rests on a run.

**implication (consumer result).** This gives the Morrey estimate (7.1) provided the abelian minimizer satisfies the two quantitative bounds in (5.1): `||mu||_infty<=C_mu epsilon` and `sup_b sum_c |Q_cb|<=C_Q N^{-3}`, uniformly in region and depth. Those consumer bounds and the global tiling construction are **unchecked** here. Only Step 1 of 7G is used; its needed analytic estimates are proved below, and its other steps are not inputs.

**gap (honest stop).** Literal (AB) on the old adapted `2B` remains open, including for `f^*`. The note supplies a different proof route to Morrey on the stated geometry. Partial-cell patches outside that geometry and the two quantitative consumer bounds remain explicit obligations. The intrinsic sup-ball example only refutes the usual centred-box identification; the possibility of some other box representation is not settled.

**discharged (scope and provenance).** This note starts from the supplied filtered copy, identified by the user as commit `3303e500f`; no history verification is claimed. `GOAL.md` and `FINISH-rules.md` were read first. Only this directory was read and only this file was written. All mathematical arguments are written by hand; no numerical job, search/enumeration computation, web source, commit, post or subagent was used.

**gap (precise target).** Uniformly in cell side, radius, refinement depth and allowed region, every exact two-cochain on each domain `D=2B` used by Lemma 4.5h must admit

\[
 da_D=f,\qquad \|a_D\|_{\ell^2(D)}\le C\|f\|_{\ell^{4/3}(D)}. \tag{AB}
\]

Restricting this assertion to the consumer's `f=f^*` would suffice for that consumer, provided the rest of its reverse Holder and Gehring argument is justified.

## 1. Attempts to kill the three routes

**gap (route 1).** The small-radius definition does not specify the grid offset, rounding when `r/4` is not an integer, or exactly how cubes meeting a ball are cut by the region. Above `N/4` it specifies no actual list. The preceding shelling note supplies no generated-pattern argument for these unions. These observations are failures of specification/proof, not a counterexample to (AB). I do not choose a convenient member of an unspecified list and call it the old domain.

**discharged (obstruction to the centred-box reading of route 2).** Interpret intrinsic sup-norm distance as infimum of sup-norm path length. In the generated local region
\[
 \Omega=\{x_1\le0\ \hbox{or}\ x_2\le0\}\times\mathbb R^2
\]
take `x=(a,-1,0,0)`, `y=(-1,a,0,0)`, `a>2`. Their ambient sup distance is `a+1`. Every path in the region from `x` to `y` must first reach `x_1=0` before entering `x_2>0`. Up to that crossing its length is at least `a`; from that crossing to `y` its length is at least `a`, because its second coordinate at the crossing is nonpositive. Hence the intrinsic distance is at least `2a>a+1`. The two straight segments through `(0,0,0,0)` achieve `2a`. Thus the intrinsic ball of radius `a+1` is not the ambient box of that radius intersected with the region. The example lies in three retained quadrants, a generated partition obtained by a cut in coordinate 1 and a cut in coordinate 2 on just one side. It can be put inside a finite cell region by taking the cell side much larger than `a`. This refutes only the centred-box identity, not a potential estimate on intrinsic balls. The same centred-box obstruction occurs in the link-path metric, in which simultaneous coordinate motion is unavailable.

**gap (what that example does not kill).** The user's broader proposal could allow a different, shifted or shortened box. The example does not refute that assertion. I have not proved such a representation for all generated patterns, or uniform comparable subboxes for it, so do not use it. The replacement below uses enclosing charts and proves its own covering argument instead.

**gap (minimality alone).** Exactness of `f^*` supplies some primitive, without its norm. Minimality supplies an Euler equation, without a local right inverse of `d`. Testing that equation with an uncontrolled primitive does not establish (AB). No counterexample to (AB) restricted to `f^*` is proved here.

**implication (replacement of the proof, route 3).** It suffices instead to construct, for small graph balls `A(x,r)`, domains `D(x,r)` with
\[
 A(x,2r+4)\subset D(x,r)\subset A(x,\Lambda r),\qquad
 da_D=f|_D,\quad \|a_D\|_2\le C\|f\|_{4/3,D}, \tag{C}
\]
where `Lambda,C` are absolute. The cutoff is supported well inside `D`, relative to the region; the estimate of the curvature norm is allowed to read the larger ball. This is an enlargement of the reverse Holder dilation, not an assertion of (AB) on its original domain.

## 2. Precise geometry of the replacement

**discharged (conventions and hypotheses).** A coarse cell has sites `kN+{0,...,N-1}^4`; its walls are at half integers. Retain whole cells, all nearest-neighbour links between their sites, and all elementary squares with their four sites retained. Assume every retained local orthant pattern is generated in the sense proved in `shelling-by-hand.md`. Write `d` for link-path distance, and `A(x,r)={v:d(x,v)<=r}`. Distances between components are infinite. All norms below use counting measure, with one positive orientation per link or plaquette. An unwrapped region is also allowed when it is a cubical covering of such a region, or a whole-cell subregion with the same local generated-pattern property. The arguments are in its intrinsic metric, not in a possibly noninjective global coordinate projection.

**unchecked (application of the hypothesis to the draft).** The local generated-pattern hypothesis is supplied by (T4), or by (T3) and the cut-tree argument in the shelling note. The global tiling construction, nesting and its stated quantitative properties are not proved here. A patch cut into nonuniform partial coarse cells would require its own geometry check; the theorem here concerns the whole-cell geometry specified for Section 3 and 4.5h.

**discharged (a chart containing a small ball).** Let `r>=1`, `s=4 ceil(r)`, and `r<=N/128`. For each coordinate put `c_i=x_i+1/2`. If a coarse wall `w_i` has `|w_i-c_i|<=2s`, set `y_i=w_i`, `h_i=4s`; otherwise set `y_i=c_i`, `h_i=2s`. There is at most one such wall, since `4s<=32r<N`. Set
\[
 D=\Omega\cap\prod_{i=1}^4\{z_i\in\mathbb Z:|z_i-y_i|<h_i\}.
\]
In a snapped coordinate the interval meets exactly its central coarse wall: `4s<N`. In an unsnapped coordinate it meets none. Its distance from `x_i` to either end is at least `2s-1/2`, so it contains every lattice coordinate within `2r+4` of `x_i` (indeed `2s-1/2>=8r-1/2>2r+4`). In particular `A(x,2r+4)` lies in `D` in the base region.

The retained orthants about `y` form the generated pattern at the corresponding coarse face, with free coordinates added for the unsnapped directions. Their side lengths are `h_i`, between `2s` and `4s`. Thus all are rectangular boxes of aspect ratio at most two, and there are at most sixteen. The product closure and the shelling in the supplied note apply. Every nonempty pattern is connected. In each retained orthant choose the site whose coordinates are `y_i+/-1/2`. A point of that orthant joins this site by an axial path of length at most `16s`. Two such sites in face-adjacent orthants are joined by one link. A simple path in the connected graph of at most sixteen orthants uses at most fifteen such links. Consequently
\[
 D\subset A(x,32s+15)\subset A(x,384r)\subset A(x,512r). \tag{2.1}
\]
The cell count, aspect ratios and path bounds are independent of the region and depth. These charts, rather than balls, are the domains on which a primitive will be constructed.

**discharged (why this construction also works in a cover).** The local chart square complex is simply connected by the shelling loop reduction: remove a latest vertex of a loop by a backtrack or a retained square, as proved in the supplied note. To pass from fine links to that orthant graph, move each interface crossing to the crossing between central sites by square strips in the union of the two adjacent orthants, which is a rectangle. Within each rectangular orthant, swaps of consecutive axial steps and backtrack cancellations then replace the intervening paths by paths through its central site. A retained orthant square is filled by the corresponding central fine plaquette. Thus the orthant loop reduction applies to the original fine loop. Every path in the base chart starting at the projection of `x` consequently has a unique lifted endpoint, independent of its path. This constructs one copy of the whole chart through `x`. A path of length at most `2r+4` from `x` projects into the coordinate window just constructed, and lifts into this copy. This proves the asserted inner inclusion in a cover too. No bound on the total number of sheets is used.

**discharged (local volume and doubling, including walls).** For `1<=r<=N/128`, the preceding injection into a coordinate window gives
\[
 4^{-4}r^4\le |A(x,r)|\le(2r+1)^4\le3^4r^4. \tag{2.2}
\]
For the lower bound, in the cell containing `x` choose in each coordinate a direction with at least `(N-1)/2` available steps. The cube of `floor(r/4)` steps in those four directions stays in that cell and in the path ball, and has `(floor(r/4)+1)^4>= (r/4)^4` sites. This construction is valid at a free wall as well as in the interior. If `kr<=N/128`, (2.2) gives `|A(x,kr)|/|A(x,r)|<=12^4 k^4`. There is no thin-intersection assumption in this volume proof.

**discharged (large-radius volume control, if needed).** There is also a uniform constant for volume comparison and doubling at radii up to any fixed multiple `J N`; it need not come from an unspecified list. Here is a finite covering proof. Assume first `N>=2^18`, put `ell=N/2^12`, and take a maximal `ell/8`-separated set of sites in a finite component. Maximality gives an `ell/8` covering. Balls of radius `ell/32` about these sites are disjoint. All centres within `ell/2` of one centre have those balls in its `ell` ball. By (2.2) their number is at most
\[
 D_0=(3^4/4^{-4})32^4.
\]
A path of length `J N` can be divided into at most `ceil(16 J N/ell)+1` pieces of length at most `ell/8`: use integer piece lengths between `ell/16` and `ell/8`, except the last. Associate a net centre to each endpoint. Successive centres are at distance at most `3ell/8<ell/2`. Thus the ball is covered by at most `(D_0+1)^{ceil(16 J 2^{12})+3}` net balls. Each has at most `3^4 ell^4` sites. This proves `|A(x,JN)|<=C_J N^4`. The lower bound at every `r<=JN` is obtained from (2.2) when `r<=N/128`, and from its subball of radius `N/128` otherwise, at a cost depending only on `J`. For `N<2^18`, a radius `JN` ball in a graph of degree at most eight has at most `1+8+...+8^{ceil(J2^{18})}` sites, by counting path words; this is a symbolic bound, not an enumeration. Its nonempty volume is at least one. These observations give the same conclusion with larger constants. This addresses covers as well as embedded regions. Nothing is asserted at radii arbitrarily large compared with `N`: a long one-cell-wide tube would invalidate four-dimensional volume growth there.

**implication (large radii in the consumer).** The proof below will actually need higher integrability only on `A(x,R)` with `R=N/128`, and reverse Holder only at still smaller radii. For `r>=R/2`, the final Morrey estimate follows directly from `E(x,r)<=E(x,N)`. Thus neither a potential nor a domain from the old finite list at `r>N/4` is used.

## 3. Covering, maximal estimates and the box input

**discharged (finite metric covering lemma).** For any finite collection of balls, select a ball of largest radius, discard every ball meeting it, and repeat on those remaining. The selected balls are disjoint. A discarded ball of radius `t` meets a selected ball of radius `r>=t`; the distance of their centres is at most `r+t`, so the discarded ball lies in the concentric `3r` ball. This proves the covering assertion using only the triangle inequality. Applied to balls `A(x,lambda r_x)`, it selects disjoint such balls, and covers all their centres by `A(x_i,2lambda r_i)` (and their entire union by `A(x_i,3lambda r_i)`). The choice is a finite inductive existence proof, not a machine search.

**discharged (maximal estimate).** Suppose all balls allowed in a maximal operator `M` and their triples obey `|3A|<=D|A|`. For nonnegative `u`, the preceding selection applied to one witnessing ball at each site of `{Mu>t}` gives
\[
 |\{Mu>t\}|\le (D/t)\sum u.
\]
On a finite space a supremum exceeding `t` has a witness; on an infinite space first apply the argument to an arbitrary finite subset of the level set. Since `M(u 1_{u<=t/2})<=t/2`, the same estimate gives
\[
 |\{Mu>t\}|\le (2D/t)\sum_{u>t/2}u,
 \qquad \sum(Mu)^2\le8D\sum u^2. \tag{3.1}
\]
The last identity follows by integrating `2t` times the preceding bound and interchanging nonnegative sums and integrals; each summand is integrated over `0<t<2u`. This proves the maximal estimate for our restricted graph-ball family using (2.2), or the large-radius bound when triples reach a fixed multiple of `N`. It also proves it on `Z^4` and on rectangular discrete tori for sup-norm balls: in each coordinate the number of sites is `2 floor(r)+1`, capped at the period on a torus, so tripling a radius changes volume by a bounded factor. No covering lemma is left as a citation.

**discharged (kernel-to-norm estimate).** On `Z^4` or a rectangular four-torus, suppose `|K(v,w)|<=C_K(1+dist_infty(v,w))^{-3}`. Shells of radii `2^j` have at most `C 2^{4j}` sites. Splitting the inner sum into dyadic annuli, bounding the mass in each enclosing ball by its volume times `Mu(v)`, and summing a geometric series gives, for `t>=1`,
\[
 \sum_{dist<t}|K(v,w)|u(w)\le C C_K t Mu(v).
\]
For the exterior, Cauchy--Schwarz and the series `sum_{j>=0}(2^jt)^4(2^jt)^{-6}` give `C C_K t^{-1}||u||_2`. These statements remain valid if `t` exceeds the torus diameter; the exterior is then empty. Since `Mu<=||u||_2`, choose `t=(||u||_2/Mu(v))^{1/2}`, with the zero case separate. By (3.1),
\[
 \|Ku\|_4\le C C_K\|u\|_2.
\]
Finite-sum duality gives `||K^T u||_2<=C C_K||u||_{4/3}`: pair with an arbitrary vector of norm one in `ell^2` and apply Holder. The same pointwise hypothesis holds for the transposed kernel, so both orientations have this critical estimate. This supplies precisely the HLS step needed below.

**discharged (Green kernel, with the low-frequency cutoff specified).** On a rectangular torus of periods `2n_i`, assume `max n_i/min n_i<=8`. Frequencies have steps `h_i=pi/n_i`, put `q(p)=sum_i 4 sin^2(p_i/2)`, and set
\[
 m_\mu(p)=(e^{ip_\mu}-1)/q(p)\quad(p\ne0),\qquad m_\mu(0)=0.
\]
The normalized inverse Fourier transform satisfies
\[
 |\check m_\mu(z)|\le C(1+|z|_\infty)^{-3}, \qquad |z_i|\le n_i. \tag{3.2}
\]
Here are the estimates proving it, rather than an appeal to Lemma 2b. In the principal frequency cube, `q(p)>=4|p|^2/pi^2` and the numerator is at most `|p|`. Differentiating `qm=e^{ip_mu}-1` inductively gives `|partial^alpha m|<=C_alpha |p|^{-1-|alpha|}` for `|alpha|<=5`: derivatives of `q` are bounded by `C_alpha |p|^{2-|alpha|}`, derivatives of the numerator by `C_alpha |p|^{1-|alpha|}`, and every lower-order product in that differentiated identity has the required power. Away from zero these inequalities follow with enlarged constants on the compact frequency cube; derivatives match at its periodic boundary.

Frequency counting in a cube of radius `t>=max h_i` gives at most `C t^4 prod_i h_i^{-1}` points. Dividing by the torus volume, and summing dyadic shells, yields
\[
 |T|^{-1}\sum_{0<|p|\le t}|p|^{-1}\le C t^3,
 \qquad |T|^{-1}\sum_{|p|\ge t}|p|^{-6}\le C t^{-2}. \tag{3.3}
\]
For shells below `max h_i`, there are only a bounded number of dyadic scales down to `min h_i`, since their ratio is at most eight; the same counting bounds with enlarged constants apply there. In particular the normalized sum of `|m|` over the whole frequency cube is bounded absolutely.

Write `r=|z|_infty`, and fix `A=2^{12}pi`. For `r<=4A`, the last absolute bound proves (3.2), with an enlarged fixed constant. Otherwise let `t=A/r<1/4` and choose a smooth cutoff equal to one for `|p|<=t`, zero for `|p|>=2t`, with derivatives of order `j<=5` bounded by `C_j t^{-j}`. Such a cutoff is obtained by rescaling any smooth function constant on the two indicated closed sets; for example smooth the transition using `exp(-1/u)` for `u>0`, zero otherwise. Its first five rescaled derivatives have finite maxima on the compact transition annulus. The inner part is at most `Ct^3` by (3.3). Also
\[
 t\ge A/(\max n_i)\ge512\max h_i.
\]
For the outer multiplier `(1-chi)m`, five differences in coordinate `i` are therefore zero within `|p|<t/2`, and elsewhere bounded by `C h_i^5 |p|^{-6}`. This follows by writing each difference as the integral of its derivative over a step interval, five times, and using the derivative bounds and the cutoff product rule; the frequency shifts total at most `5h_i<t/2`. Choose `i` with `|z_i|=r`. Five summations by parts on the periodic frequency grid divide by `|e^{ih_i z_i}-1|^5`, which is at least `(2h_i r/pi)^5`. The outer part is thus at most `C r^{-5}t^{-2}=C A^{-2}r^{-3}` by (3.3), and the inner part is `C A^3r^{-3}`. This proves (3.2). The constants depend only on the fixed aspect-ratio bound. This proof deliberately keeps the cutoff well above the frequency spacing even when `r` is comparable to a period.

**discharged (critical primitive on a comparable box).** Let a lattice box have edge side lengths `n_i>=1` of ratio at most eight, and let `f=da_0` there. Reflect `a_0` in its endpoint faces onto the torus of periods `2n_i`, carrying link orientations. Pullback commutes with `d`, so its curl is a reflected `f_T`, with at most sixteen copies of each original plaquette. The mean of each link component is zero because reflection in that component reverses its sign. In Fourier variables put `v_i=e^{ip_i}-1`: exterior multiplication by `v` and contraction by its conjugate obey `dd^*+d^*d=q(p)` on forms, by cancelling the cross terms. Since `f_T` is exact,
\[
 a_T=d^*\Delta^{-1} f_T,\qquad da_T=f_T.
\]
The difference from the reflected `a_0` is a gradient: at every nonzero frequency a one-form `b` with `v wedge b=0` is a scalar multiple of `v` (choose a nonzero component of `v`); its zero-frequency component vanishes. The kernels in `d^*Delta^{-1}` are those of (3.2), with conjugations and unit translations, which change the displayed bound only by an absolute factor. The kernel-to-norm estimate and reflection multiplicity give, on restricting to the original box,
\[
 a_Q=a_0+d\lambda_Q,\qquad da_Q=f,\qquad
 \|a_Q\|_2\le C_{\rm box}\|f\|_{4/3}. \tag{3.4}
\]
This proves the box analytic input used here. No eigenvalue estimate or unproved Green-function estimate is imported. The construction is linear in `f`.

## 4. The chart estimate, with the lattice folding proved

**discharged (folding estimate).** Use the shelling proved in `shelling-by-hand.md`, with `I` equal to all earlier-neighbour directions of a new orthant `z`. Reflect coordinates so that its coordinates `q_i`, for `i in I`, are positive half integers. Put `t=min_{i in I}q_i` and
\[
 \Phi_i(q)=q_i-2t\ (i\in I),\qquad \Phi_i(q)=q_i\ (i\notin I).
\]
The image is a lattice site, without rounding. At least one coordinate in `I` is negative. Also `-q_i<=q_i-2t<=q_i`, so the image stays in the rectangular union `O` of the other orthants of the box `B` spanned by `I`. All those orthants are earlier by the shelling predicate.

For an internal link `q -> q+e_k`, if the minimum is unchanged, the images differ by one link; a coordinate attaining the old minimum other than `k` stays negative. If the minimum increases, it increases by exactly one, `k` was its unique old minimizer, and the image displacement is
\[
 e_k-2\sum_{i\in I}e_i.
\]
Join the images by first moving one step negatively in coordinate `k`, and then two steps negatively in each `i in I\{k}`. Coordinate `k` remains negative throughout, and every coordinate stays between its endpoint values. This is a path in `O` of length at most seven. For `k notin I` the image link is unchanged and a negative coordinate in `I` persists. Reversing a link reverses these paths. For a crossing link from an earlier orthant to `z` in direction `k in I`, the new endpoint has `q_k=1/2`; its image and the earlier endpoint have `k` coordinate `-1/2` and differ by minus one in the other `I` coordinates. They are joined inside `O` by at most three links.

The path multiplicity is bounded uniformly. After choosing a minimizing index `j`, the inverse formula is `q_i=Phi_i-2Phi_j` for `i in I` and `q_i=Phi_i` otherwise; there are at most four choices of `j`. If a chosen path uses an old link, its starting image lies in the coordinate cube of radius eight about that link's initial site, containing at most `17^4` sites. At most eight input links start at each preimage. Crossing links add at most eight starts per site. Thus `M=64*17^4` bounds the multiplicity of all these paths. Cauchy--Schwarz along paths of length at most seven proves, for every scalar `zeta` on `O`,
\[
 \sum_{\text{new or crossing links}}|d\zeta_E|^2
 \le7M\sum_{\text{links in }O}|d\zeta|^2, \tag{4.1}
\]
where `zeta_E=zeta` on `O` and `zeta_E=zeta composed with Phi` on `z`. The same argument works componentwise.

**discharged (critical primitive on the chart).** Start from any primitive `a_0` of the exact `f` on `D`. Gauge the first orthant by (3.4). Suppose the earlier union `P` has `a_P=a_0+d lambda_P`. The shelling supplies the rectangular box `B` consisting of `z` and the `I`-orthants; its side lengths in sites are `h_i` or `2h_i`. Their edge lengths have ratio less than eight, since `2s<=h_i<=4s` and `s>=4`. Apply (3.4) on `B`, writing `a_B=a_0+d lambda_B`. On `O=B\z` use `zeta=lambda_P-lambda_B`. Extend it by (4.1), define `lambda=lambda_P` on `P`, `lambda=lambda_B+zeta composed with Phi` on `z`, and set `a=a_0+d lambda` on the enlarged union. Every earlier crossing interface is in `O` because `I` contains all earlier neighbours. Hence (4.1) bounds all new links, not just links internal to `z`:
\[
 \|a\|_{2,P\cup z}\le C\bigl(\|a_P\|_{2,P}+\|a_B\|_{2,B}\bigr).
\]
Both gauges are of the same `a_0`, so this construction also preserves the curl on every crossing plaquette. At most sixteen steps give
\[
 da_D=f,\qquad \|a_D\|_{2,D}\le C_*\|f\|_{4/3,D}. \tag{4.2}
\]
For example `C_*` can be chosen by sixteen iterations of the preceding two-term bound, starting with `C_box`; this is a stated finite order of choice, independent of `N,r` and the region. Together with (2.1), (4.2) proves (C) with `Lambda=512` on the stated whole-cell generated geometry.

**discharged (exact use of 7G).** This proof uses only the shelling of its Step 1 and its strategy of gauging the full box supplied by the earlier-neighbour directions. The critical box input is proved in Section 3, and the needed `ell^2` folding input is proved in (4.1), including crossing links and unequal but comparable side lengths. It uses neither Step 2's partition of unity nor Step 3's overlap constants, Cech correction or nerve inverse. It does not use the `ell^2 -> ell^4` conclusion, the boundedness of `T composed with d`, or Lemma 8's pointwise conclusion.

**unchecked (unused analytic assertions).** Those other conclusions and Steps 2--3 of 7G, the analytic assertions of 8G, and the gauge/period arguments of the other consumers remain unchecked here. In particular no uniform bound on an arbitrary chart nerve is being claimed. The larger chart has at most sixteen orthants and requires no nerve construction.

## 5. Reverse Holder for the minimizer, on graph balls

**implication (the precise consumer assumptions).** In addition to the geometry of Section 2, assume `f=da^*` and a linear coarse constraint `Q` have
\[
 \langle f,de\rangle=\langle\mu,Qe\rangle\quad\hbox{for every link field }e,
 \qquad \|\mu\|_\infty\le C_\mu\varepsilon,
 \qquad \sup_b\sum_c|Q_{cb}|\le C_Q N^{-3}. \tag{5.1}
\]
The constants in the last two inequalities must be uniform in the region and depth. The Euler identity includes variations at the free boundary. No constraint on the periods of `a_D-a^*` is needed, because `e` below is an arbitrary single-valued link field.

**discharged (what minimality itself supplies).** For the finite-dimensional minimum of `||da||_2^2/2` with `Qa` fixed, differentiation along `ker Q` gives `<f,de>=0` on that kernel. Thus `Qe -> <f,de>` is a well-defined linear functional on `range Q`; extend it to the finite coarse space and represent it by an inner product with some `mu`. This proves the Euler identity. It proves neither quantitative inequality in (5.1).

**unchecked (remaining input from 4.5g--h).** The draft asserts the two quantitative bounds in (5.1). Their proofs from the particular averaging operator and the size of the coarse data are not rebuilt here. In particular the bound on the multiplier by `epsilon`, rather than merely by a local fine-energy norm, is retained as an explicit input. The result below has no implicit appeal to minimality for that bound.

**discharged (discrete cutoff calculation under (5.1)).** Anchor each positive plaquette at its lower-coordinate site and define
\[
 g(v)^2=\sum_{i<j:\,(v;i,j)\text{ exists}}|f_{ij}(v)|^2,
 \qquad E(x,r)=\sum_{v\in A(x,r)}g(v)^2.
\]
There are at most six terms at a site. Hence `sum_p |f_p|^{4/3}<=6^{1/3} sum_v g(v)^{4/3}` on any domain (enlarging its anchor set only helps). Use (4.2) on `D(x,r)` and put `chi(v)=min(1,max(0,2-d(x,v)/r))`. For a positive link set `e_i(v)=chi(v)^2 a_{D,i}(v)`, extended by zero. Its support and every plaquette touching that support lie in `A(x,2r+2)`, hence in `D`. For a plaquette based at `v`, direct expansion gives
\[
 (de)_{ij}(v)=\chi(v)^2 f_{ij}(v)
  +[\chi(v+e_i)^2-\chi(v)^2]a_{D,j}(v+e_i)
  -[\chi(v+e_j)^2-\chi(v)^2]a_{D,i}(v+e_j). \tag{5.2}
\]
Along a link `|d chi|<=1/r`, so each coefficient difference is at most `2chi(v)/r+1/r^2`. Put `X^2=sum chi(v)^2 |f_{ij}(v)|^2` and `A_D=||a_D||_2`. The two error sums in (5.2) are bounded by `C r^{-1} X A_D+C r^{-2}||f||_{2,U}A_D`, where `U` consists only of the plaquettes in `D` touching the cutoff. Since `f=da_D` there, the four-link formula and the fact that a link belongs to at most six plaquettes give `||f||_{2,U}^2<=24 A_D^2`. This treats the lattice `r^{-2}` error explicitly.

The last two bounds in (5.1) give
\[
 |\langle\mu,Qe\rangle|\le C\varepsilon N^{-3}\|e\|_1
 \le C\varepsilon N^{-3}r^2 A_D,
\]
using `|D|<= (8s)^4<= (64r)^4` and at most four positive links per site. Insert these bounds in (5.1), absorb `C r^{-1}X A_D` by `X^2/2+C'r^{-2}A_D^2`, and bound the forcing product by `C'r^{-2}A_D^2+C''epsilon^2 N^{-6}r^6`. Since `chi=1` on `A(x,r)`,
\[
 E(x,r)\le C r^{-2}\|f\|_{4/3,D}^{,2}
                  +C\varepsilon^2 N^{-6}r^6. \tag{5.3}
\]
All omitted coefficients in this calculation count at most six plaquettes or four links, or are the constants explicitly specified above.

**discharged (the enlarged reverse Holder inequality).** Take `Lambda=512` and require `r>=1`, `Lambda r<=N/128`. By (2.1), (2.2), (5.3) and the six-component bound,
\[
 \mathop{\rm avg}_{A(x,r)}g^2
 \le b\left(\mathop{\rm avg}_{A(x,\Lambda r)}g^{4/3}\right)^{3/2}
       +C\varepsilon^2N^{-4}(r/N)^2
 \le b\left(\mathop{\rm avg}_{A(x,\Lambda r)}g^{4/3}\right)^{3/2}+H^2,
 \qquad H=C\varepsilon/N^2. \tag{RH}
\]
For clarity, the power cancellation is `r^{-2}/r^4` from (5.3), multiplied by `|A(x,Lambda r)|^{3/2}<=C r^6`. The constants depend only on dimension, `C_*`, `C_mu`, `C_Q` and the fixed dilation. The proof also covers free walls and `r=1`. It imposes no artificial boundary condition on `a_D`.

## 6. Gehring with fixed dilation, including the lattice bottom

**discharged (local metric theorem).** Let `R>=2`, `Q_s=A(x_0,sR)`, and suppose (2.2) holds at radii from one to `R`, with constants `c_0,C_0`. Suppose for all integer radii used below, with their `Lambda`-dilates in `Q_1`,
\[
 \mathop{\rm avg}_{A(x,r)}g^2
 \le b\left(\mathop{\rm avg}_{A(x,\Lambda r)}g^q\right)^{2/q}
       +\mathop{\rm avg}_{A(x,\Lambda r)}h^2,
 \qquad 1\le q<2. \tag{6.1}
\]
It is enough to assume (6.1) for `r<=R/(16Lambda)`. Then there are `eta>0,C` depending only on `b,q,Lambda,c_0,C_0`, such that
\[
 \left(\mathop{\rm avg}_{Q_{1/2}}g^{2+\eta}\right)^{1/(2+\eta)}
 \le C\left(\mathop{\rm avg}_{Q_1}g^2\right)^{1/2}
       +C\left(\mathop{\rm avg}_{Q_1}h^{2+\eta}\right)^{1/(2+\eta)}. \tag{6.2}
\]
Here `Lambda` is the integer 512; the following proof works for any integer dilation at least two.

**discharged (stopping and covering proof).** Put `K=4Lambda`, `c=1/(2C_0)`, and choose
\[
 A=4C_0(4K)^4/(c_0c),\qquad
 \rho=(s'-s)R,\qquad
 t_0^2=A(R/\rho)^4\mathop{\rm avg}_{Q_1}g^2,
 \quad 1/2\le s<s'\le1.
\]
If `rho<=4K`, then `t_0^2>=sum_{Q_1}g^2`, so the level set `Q_s intersect {g>t}` is empty for `t>=t_0`. This is the lattice-bottom case; it requires no nonexistent radius below one. Otherwise, for `x` in that level set, `avg_{A(x,1)}g^2>t^2/C_0>ct^2`. Every integer radius `rho/(4K)<=r<=rho` has average at most `sum_{Q_1}g^2/(c_0 r^4)<ct^2`: these balls are in `Q_{s'}`, and the displayed choice of `A` proves the strict inequality. Therefore a largest integer radius with average at least `ct^2` exists and satisfies
\[
 1\le r_x<\rho/(4K).
\]
Apply the finite metric covering lemma to `A(x,Lambda r_x)`. Its selected balls are disjoint and their `K r_i` balls cover the level set. The latter radii are integers larger than `r_i` and less than `rho`, so maximality gives average below `ct^2` there. Volume comparison yields
\[
 \sum_{Q_s\cap\{g>t\}}g^2
 \le C t^2\sum_i|A(x_i,r_i)|. \tag{6.3}
\]
All `Lambda r_i` balls lie in `Q_{s'}` and have `r_i<R/(16Lambda)`, as required by the stated restricted hypothesis.

For each selected ball, (6.1) and its stopping inequality imply either `avg h^2>=ct^2/2` or `avg g^q>=(c/(2b))^{q/2}t^q` on its `Lambda`-dilate. Choose
\[
 \delta=\tfrac14\min\{1,\sqrt c,\sqrt{c/(2b)}\}.
\]
Deleting respectively the portions `h<=delta t` or `g<=delta t` removes less than half the indicated lower average. Multiply the resulting inequalities by the ball volumes, use `|A(r_i)|<=|A(Lambda r_i)|`, then sum over the disjoint dilates in (6.3). This gives constants `C_g,C_h` with
\[
 \sum_{Q_s\cap\{g>t\}}g^2
 \le C_g t^{2-q}\sum_{Q_{s'}\cap\{g>\delta t\}}g^q
       +C_h\sum_{Q_{s'}\cap\{h>\delta t\}}h^2. \tag{6.4}
\]

**discharged (integration and iteration).** Multiply (6.4) by `eta t^{eta-1}` and integrate from `t_0` to infinity. The left side is at least `Phi(s)-t_0^eta sum_{Q_1}g^2`, where `Phi(s)=sum_{Q_s}g^{2+eta}`. Extending the right integrals down to zero gives coefficients
\[
 C_g\eta\,\delta^{-(2-q+\eta)}/(2-q+\eta)
 \quad\hbox{and}\quad C_h\delta^{-\eta}
\]
in front of `Phi(s')` and `sum_{Q_1}h^{2+eta}`. For `0<eta<=1`, the first coefficient is at most `C_1 eta` for a fixed `C_1`, because `2-q>0`. Choose `eta<=1/4` and `C_1 eta<=1/4`. With
\[
 X=(\mathop{\rm avg}_{Q_1}g^2)^{\eta/2}\sum_{Q_1}g^2,
 \qquad Y=\sum_{Q_1}h^{2+\eta},
\]
we obtain
\[
 \Phi(s)\le\tfrac14\Phi(s')+C(s'-s)^{-2\eta}X+CY. \tag{6.5}
\]
Use `s_j=1-2^{-j-1}`, whose successive differences are `2^{-j-2}`. The series with ratio `2^{2eta}/4<1` bounds the iterated `X` terms, and the `Y` terms form a geometric series. The remainder `4^{-j}Phi(s_j)` tends to zero because the lattice is finite. The empty-level-set case above justifies (6.5) even when these differences fall below one lattice unit. Thus `Phi(1/2)<=C(X+Y)`. Divide by `|Q_{1/2}|`, using (2.2) to compare it with `|Q_1|`, and take the positive root to get (6.2). This rebuilds the stopping argument rather than assuming the old adapted-family proof applies.

## 7. What the replacement delivers

**discharged (conditional Morrey theorem).** Under exactly the whole-cell generated geometry and (5.1), there are uniform `C` and `a>0` such that
\[
 E(x,r)\le C(r/N)^a\bigl(E(x,N)+\varepsilon^2\bigr),
 \qquad 1\le r\le N,\qquad a=\frac{4\eta}{2+\eta}. \tag{7.1}
\]
For `N>=256`, use `R=N/128`, `q=4/3`, and `h=H` in Section 6. All stopping radii are below `R/(16Lambda)`, so (RH) applies and every chart is of Section 2. For `1<=r<=R/2`, Holder and (6.2) give
\[
 E(x,r)\le |A(x,r)|^{\eta/(2+\eta)}
       \left(\sum_{A(x,R/2)}g^{2+\eta}\right)^{2/(2+\eta)}
 \le C(r/R)^a\bigl(E(x,R)+R^4H^2\bigr).
\]
Use `E(x,R)<=E(x,N)`, `R^4H^2<=C epsilon^2`, and `R=N/128`. For `R/2<r<=N`, monotonicity gives the result with the extra absolute factor `256^a`. This includes every radius above `N/4`, without supplying or using the old finite list. For `N<256`, `r/N>=1/256`, so the same monotonicity argument proves (7.1) directly. Thus there is no unexamined small-cell case. In level-k units set `rho=r/N` and `sigma=a/2` to obtain the displayed exponent of 4.5h.

**discharged (subset and layer version).** The same Holder step gives, for every `S subset A(x,R/2)`,
\[
 \sum_S g^2\le C\left(\frac{|S|}{R^4}\right)^{\alpha}
                  (E(x,R)+\varepsilon^2),\qquad \alpha=\eta/(2+\eta). \tag{7.2}
\]
One can also take `S subset A(x,N/2)` and replace `R` by `N` on the right. To verify this without a family citation, for `N>=2^{14}` choose a maximal `R/4`-separated set in `A(x,N/2)`. Its `R/2` balls cover that set, its `R/16` balls are disjoint and contained in `A(x,N)`, and the local lower volume bound and the large-radius upper bound of Section 2 bound the number of centres by an absolute constant. Each radius-`R` ball about a centre is inside `A(x,N)`. Apply (7.2) to the intersection of `S` with each covering ball, bound its cardinality by `|S|` and its outer energy by `E(x,N)`, and sum over the bounded number of centres. The factor `(N/R)^4` is fixed. For `N<2^{14}`, a nonempty `S` has `|S|/N^4>=2^{-56}`, so monotonicity gives the assertion with a fixed larger constant; the empty case is zero.

For a layer of fine thickness `t>=1` adjacent to coarse cell walls, the covering charts have side lengths comparable to `R` and, when `t<R`, meet at most a fixed number of coarse wall planes even after enlargement by `t`. The number of sites within distance `t` of one such plane is at most `C(t+1)R^3`: choose its normal coordinate in at most `2t+2` ways and bound each tangential coordinate interval by `CR`. Sum over four coordinate directions and the bounded covering. When `t>=R`, the total-volume bound gives the same estimate after increasing its constant, since `R=N/128`. Hence
\[
 |\text{layer}\cap A(x,N/2)|\le C(t+1)N^3.
\]
A layer at the free boundary is a subset of these coarse-wall layers. Setting `t=rho N>=1` in the subset estimate gives the fraction `C rho^alpha` of `E(x,N)+epsilon^2`. This proves the layer consequence at resolved lattice thicknesses; thickness below one is not assigned a continuum volume law.

**discharged (metric convention and downstream locality).** Equation (7.1) is for the intrinsic link metric explicitly defined here. For embedded regions, a coordinate sup ball cut by the region at radius `u>=1`, `u<=N/128`, is contained in `D(x,u)` and hence in `A(x,512u)` by Section 2. The same holds for the component in the lifted local star; an intrinsic path whose coordinate displacement stays below `u` remains in that star and lifts there uniquely. Thus an intrinsic sup-length ball of radius `u` has the same inclusion. Conversely a link path is a path of the same or smaller sup length. Apply (7.1) at radius `512u` for small `u`, and monotonicity for the remaining fixed fraction of `N`, to get the corresponding intrinsic sup-length Morrey estimate with unchanged exponent and larger absolute constants. Plaquette conventions that include a plaquette whenever one of its sites is in a ball add at most two link steps; at radii at least one this is another fixed factor. To keep the outer radius exactly `N`, use the small chart `R=N/128`, whose two-step buffer lies inside that outer ball, and handle the remaining radii by monotonicity. This supplies local energy decay for the box/chart balls read by Lemma 8; it does not certify the old rounded-grid domains or their unstated large-radius choices.

**discharged (order and uniformity of constants).** First fix dimension four, the aspect-ratio bound eight, the fixed cutoff constant in (3.2), and the box constant from (3.4). Next fix the folding constant in (4.1), then sixteen chart iterations, `Lambda=512`, and the volume constants. Given uniform `C_mu,C_Q` in (5.1), these fix `b` and the coefficient in `H=C_H epsilon/N^2`. Section 6 then fixes `K,c,A,delta,C_1`, and finally a positive `eta<=min(1/4,1/(4C_1))`. Monotonicity and the finite covering increase constants only by fixed factors. None of these choices reads `N`, `r`, refinement depth, the number of cells, the number of sheets, or a chart nerve. The large-radius counting constants depend on the fixed ratio `J` only, and only a fixed `J` is used. No limit or chosen constant is justified by a numerical run.

**discharged (read/write record).** Read the required two instruction files, `library/shelling-by-hand.md`, `library/lattice_gehring_hls.md`, the relevant box and chart proofs of `library/lattice_sobolev_box_gauge.md`, and the region definitions and relevant consumers around 3.2 and 4.5d--h in `parts/hard-core--independent.md`. Searches in that permitted part file also returned surrounding material; reported computations there supplied no proof input. Only `library/adapted-domains.md` was written. No check script, numerical job, enumeration, other account, external source, commit, post or subagent was used.

## Final status

**discharged.** The box estimate (3.4), the discrete chart estimate (4.2), the enclosing generated charts, the metric covering and maximal estimates, and the fixed-dilation Gehring theorem have hand proofs above. Under the stated geometry and (5.1), they prove (7.1) and the subset/layer consequence. This is a replacement of the analytic route through the original adapted domains, with explicit handling of walls, covers, small radii and large radii. The centred-box identity is false by Section 1; the broader box-representation proposal remains a gap.

**implication.** Application to the draft's actual `f^*` is conditional on its regions satisfying the whole-cell generated hypothesis (the global tiling assertions remain unchecked), and on precisely
\[
 \|\mu\|_\infty\le C_\mu\varepsilon,
 \qquad \sup_b\sum_c|Q_{cb}|\le C_QN^{-3},
\]
with constants uniform in region and depth. The Euler identity follows from the abelian finite-dimensional constrained minimum as proved above. With these inputs the potential required for the replacement proof is supplied on the larger chart for every exact curvature, not just `f^*`. No other analytic assertion of 7G is an input to this replacement; the portions of 7G/8G not used are explicitly unchecked in Section 4. No assertion about nonlinear corrections or the rest of the Yang--Mills chain is made.

**gap.** Literal (AB) for the old adapted `2B`, including its unspecified large-radius list, is still open here; so is (AB) restricted to `f^*` on those old domains. This note avoids that obligation for the precisely stated Morrey theorem; it does not relabel it proved. Patches with partial cells outside the geometry specified in Section 2 still need (C), including its critical norm bound with a constant independent of any sliver width. The two quantitative consumer bounds just displayed require their own verification before claiming 4.5h unconditionally repaired.
