# Repo search

Row 1240, Codex hand check of Claude Opus 5.5 row 1237 at `a65ba7cd9`. The assignment specifies GPT-6.2
Astra, max effort. This is research text and grants no status. Line numbers prefixed W refer to
`library/gap-mini-solve-w-opus.md` at this pin.

The lead's November 8 digest searched main and PRs 10114, 10133, 10134 and 10141 for an earlier set of
obligations. Its nearest hits are a positive one-time-step transfer witness (PR 10114,
`MASS_GAP_LOCAL_BLOCK_ASTRA.md` 106–149, identical lineage on PR 10133) and a noncompact Dirichlet Maxwell
Hessian bound (main,
`MASSIVE_WILSON_LOOP_CURVATURE_NONCOMPACT_COVARIANCE_AND_COMPACT_DEFECT_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-14.md`
120–145). I opened both. Neither supplies a Wilson heat-bath rate or compares two RG depths. A targeted name
search on those five refs found no copy of this check outside the lane. The task-specific prior file is
absent. The open registry has no matching assignment.

The close local precedents are row 1229, Claim A (the qualitative dynamics argument), row 1218 (the published
cube criterion), row 1224 §3.4 (the specialized finite-speed argument), and rows 924–925 (conditional
comparison of two tuned recursions and its additional physical premises). Those results retain their original
credit. The missing work here is to test the generalizations and constants in W, and to identify exactly
which maps its two runs share. In W's literature references, A is *One Bound at One Scale* by Bhattacharjee,
Bhattacharya, Lockwood, Romanov, Sessford and Singha Roy. B is *One Cube Estimate* by the first four
authors. [Row 1218's source record](prior/gap-onebound-read-sol.md)

The outline index locates the dense positive-time test space in chunk 27 (outline 28898–28928) and the limits
of scalar matching in chunk 29 (outline 32317–32324). The later tuning and pointing labels are in a different
manuscript. Source credit throughout is to **Ethan Sussman and Levent Alpoge, with Claude and Codex as
authors of their text**. The outline and CA-I are at `31a47c543775`. Line numbers prefixed Y below refer to
[their expanded account at `2bc0658f91d2`](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2/YM4_1400.tex).

## Plan

1. Check the prior-work record, task ownership, and the indexed source ranges.
2. Check Proposition UNI (a)–(c) directly from the form and the cylinder observables.
3. Check Corollaries UNI-1 through UNI-3, including the constants, rate, and cube geometry.
4. Compare Proposition 3.3 and its class clause with the cited account.
5. Compare Lemmas 3.2 and 3.4 with the account's transport and norm statements.
6. Check the remaining statements, dependencies, and conclusions in row 1237.
7. Verify the statement-by-statement verdicts, source credits, and final result.

## 2. Proposition UNI

**UNI(a), W103–170 — HOLDS.** Let $b$ bound the block diameters in plaquette-graph distance, $\rho=b+2$,
and $\Delta$ be the largest number of listed blocks meeting the closed one-link neighbourhood of a block.
For support distance $d\ge b+\rho$ and form gap $\gamma$ on the invariant subspace containing $g$, the bound is

$$
 |\mathrm{Cov}(f,g)|\le(1+2|S_f||S_g|)\|f\|_\infty\|g\|_\infty
 \exp\!\left[-\frac{d-b}{\rho}\min\!\left(1,\frac{\gamma}{e^2\Delta}\right)\right].
$$

Use real observables, or the Hermitian variance and Dirichlet form. The
conditional projection erases dependencies in its block. The only new dependencies lie on links of plaquettes
touching the block. Suppressing clocks meeting $S_f$ therefore fixes multiplication by $f$ and preserves the
measure, giving (2.1). The centered $L^2$ norm for the full dynamics decays by $e^{-\gamma t}$ by
differentiation. For a nonclosed invariant subspace apply the form inequality on its closure by continuity.
This justifies the semigroup step at W135.

Trace a dependency from $S_g$ toward a suppressed block in decreasing clock time. The first retained ring
touches $S_g$. Each subsequent ring touches the preceding block's one-link neighbourhood. After $l$ such
rings the furthest new link is within $l(b+1)$ of $S_g$. To hit a block meeting $S_f$ requires a prefix of
length $m=\lceil(d-b)/\rho\rceil$. There are at most $|S_g|\Delta^m$ prefixes, each with expected number of
ordered occurrences $s^m/m!$. For repeated labels this counts *distinct* points of the same Poisson clock,
with the same simplex integral. There are at most $|S_f|\Delta$ suppressed blocks. Duhamel thus bounds the
error in evolving $g$ by $2\|g\|_\infty |S_f||S_g|(\Delta t)^{m+1}/(m+1)!$. With $t=(m+1)/(e^2\Delta)$, the factorial bound
and the $L^2$ term give exactly W121–122. This is an estimate for a nonempty family of rate-one heat baths
with its actual $\Delta$. Empty blocks contribute zero. If no nonempty block remains, positive Poincaré
forces every element of the subspace to be constant almost surely, and the covariance vanishes.

Two conventions at W111–125 matter. Gauge transformations and centre twists preserving every plaquette
commute with conditioning since they preserve the exterior sigma-algebra and the measure. An arbitrary sign
change on one link changes the action on its incident plaquettes. The one-link count is 19 on a nondegenerate
four-torus. It is an upper bound if periodic neighbours coincide.

**UNI(b), W172–184 — HOLDS AFTER CORRECTION.** Require a common bound $\Delta_j\le\Delta_*$, or use the
actual ratio $\gamma_j/\Delta_j$ and require it to be bounded below. W107 permits a *list*. Repeating each
block $m$ times keeps its diameter and the measure fixed and multiplies both the form gap and $\Delta$ by
$m$. Thus the printed lower bound on the gap in arbitrary clock units does not give a positive uniform
exponent. A list without repetitions of bounded-diameter sets automatically has bounded overlap on this
bounded-degree graph. With $\Delta_*$, each support contains at most $C_R(1+a_j^{-1})^4$ links, and a
plaquette step moves a midpoint by at most one lattice unit. Use periodic separation on a torus. Inserting
$d\ge r/a_j-1$ in (a) proves W180 for all sufficiently fine cutoffs. Local continuous tests pass through the
torus limit. At fixed coupling and fixed support even bounded measurable tests pass by Haar $L^1$
approximation, since their marginal densities are uniformly bounded by bounding above and below the finitely
many incident Boltzmann factors.

**UNI(c), W216–240 — HOLDS** for $D>0$ and **HOLDS AFTER CORRECTION** of the undefined exponent at $D=0$. Weighted
integration by parts on the compact product gives $-\widehat L=\nabla_\mu^*\nabla$. Commuting the
differential with the scalar generator gives $d(-L)=A\,d$, $A=-\widehat L+\mathrm{Ric}+\nabla^2V\ge\kappa I$.
The kernel of $-L$ consists of constants by its Dirichlet form and connectedness. Solving the centered
Poisson equation gives $\mathrm{Cov}(f,g)=\langle df,A^{-1}dg\rangle_\mu$. This verifies the sign and the
inverse used at W233–234.

Weight component $e$ by $W_e=\exp(\lambda\,\mathrm{dist}(e,S_g))$. The product connection preserves each
component, hence commutes with these constant weights. The block norms of $WMW^{-1}-M$ have **both** row and
column sums at most $(e^\lambda-1)D$, by symmetry of $M$ and the one-plaquette range. The Schur bound is
therefore $\kappa/2$ at W225's $\lambda$. The conjugate is invertible by similarity in finite volume and its
real form is at least $\kappa/2$, giving inverse norm $2/\kappa$. Moving the weights onto the two gradients
gives W224. For $D=0$ every weight commutes and the separated covariance is zero by taking $\lambda\to\infty$
at $d>0$. At $d=0$ use the unweighted bound. Counting six plaquettes times three other link occurrences gives
$D\le18c_H|\beta|$, with the metric fixing the mixed derivative bound. Positive curvature here is a pointwise
bound on the full product manifold.

## 3. The three corollaries

**UNI-1, W186–202 — HOLDS AFTER CORRECTION** with UNI(b)'s clock normalization and matching on a dense
positive-time algebra. For each fixed compact positive-time $F$, all its entries have a common clearance
$t_0>0$. Require polynomially bounded representatives for its finitely many terms, membership of the required
factor in $\mathcal A$, and convergence of the reflected pair and of the one-point functions. Applying (b)
term by term then gives $\|[F]-\sigma(F)\Omega\|^2=0$. Density gives $\mathcal H=\mathbb C\Omega$ **on this
matched sector**. These are precisely the roles of matching and density in the outline's 28919–28928 and
31426–31439.

For a single covariance of magnitude at least $\delta>0$, put $Q_j=\log(C'a_j^{-k-8}/\delta)$, increasing
$C'$ and choosing $k\ge0$ if necessary. Taking logarithms of (a) gives

$$
 \min\{1,\gamma_j/(e^2\Delta_j)\}
 \le \rho a_j Q_j/[r-(b+1)a_j].
$$

The right side tends to zero. Only now may one remove the minimum. This proves W194 for bounded $\Delta_j$,
or $\gamma_j/\Delta_j=O(a_j\log(1/a_j))$ with the clock count explicit. A log-Sobolev inequality implies the
form gap on the relevant algebra by expansion at $1+\epsilon g$. W83–87's general reversible dynamics and
$O(a_j M)$ are **not** the fixed-separation theorem proved by W121 or W194. The former needs locality of the
update *kernel* and a rate normalization. The latter needs information controlling the prefactor, for
instance transfer estimates for all time separations and matching of reflected norms.

**UNI-2, W242–249 — HOLDS AFTER CORRECTION to the proof and scope.** The rate in lattice units supplied by
(c) is at least $\log(1+\kappa_0/(36c_H\beta_j))$ for positive $\beta_j$. It can decrease as $1/\beta_j$. On
the stated logarithmic trajectory its exponential at distance $r/a_j$ dominates every power of $1/a_j$. W245
bounds the observable in the sup norm, whereas W224 reads two gradient norms. Sup bounds alone give no
derivative bound on highly oscillatory functions.

Here the Wilson conditional law supplies the missing step even for bounded measurable tests. For separated
supports $S,T$ at graph distance $d>2$, replace $f$ by $P_S f$ and $g$ by $P_T g$. Conditioning twice
preserves their covariance, since $g$ is exterior to $S$ and $P_S f$ is exterior to $T$. The new supports are
in the exterior one-link boundaries. Differentiating the normalized conditional integral at an exterior link
$e$ gives the negative conditional covariance of $f$ with $\nabla_e V_{\rm inc}$, where $V_{\rm inc}$ sums
the plaquettes meeting $S$. The derivative vanishes off the boundary and has norm at most
$C|\beta_j|\|f\|_\infty$ on it, by the six-face incidence bound. The boundary has at most $18|S|$ links.
Apply (c) to the two smooth conditional expectations at distance at least $d-2$. The resulting prefactor is
bounded by $C\kappa_0^{-1}\beta_j^2\sqrt{|S||T|}\|f\|_\infty\|g\|_\infty$, a polynomial on this trajectory.
The same OS argument now applies. The conclusion covers pointwise Bakry–Émery on the specified product
metric. W246's “every form” cannot include arbitrary quotient metrics, dynamics with accelerated clocks, or
an ordinary Langevin Poincaré inequality substituted for the curvature hypothesis.

**UNI-3, W352–365 — HOLDS**, including the printed constant. Bhattacharjee, Bhattacharya, Lockwood and
Romanov include all four link orientations **based** in the cube. Every link lies in $n^4$ translates.
The source form is $n^{-4}\sum_x\|(I-P_x)f\|_2^2$ on real gauge-invariant $f$, so the rate-one-per-cube
convention gives $\gamma=n^4\varpi$. [One Cube Estimate, v7, Definition 62](https://hexagonmath.org/2610.00341v7)

If two cubes touch through a plaquette their origins
differ by at most $n$ in each periodic coordinate, giving $\Delta\le(2n+1)^4$. To join links with bases in
one cube, translate in the coordinates transverse to the initial link, turn to a perpendicular orientation at
the same base, translate in the remaining coordinate, and turn to the final orientation. Each move is one
plaquette step, so $b\le4(n-1)+2$ and $\rho\le4n$. These bounds give $\kappa\ge c/n$ with
$c=\varpi_0/(625e^2)$ for $n\ge2,\ 0<\varpi_0\le1$, since $4(2+1/n)^4\le4(5/2)^4<625$. They cover the
source's side $n=2$. Even if BP is stated with $\varpi_0>1$, testing one nonconstant plaquette trace gives
$\varpi_0\le4$ because at most $4n^4$ cubes touch its support and each *mean* conditional variance is at most
the total variance. Hence $\varpi_0/[e^2(2+1/n)^4]<1$ and the same constant works.

For $d\ge b+\rho$, solving (a) before taking limits, even with W's looser bound $b\le4n+1$, gives

$$
 n_j a_j\ \ge\ c(r-2a_j)/(Q_j+4c).
$$

For $d<b+\rho$, $r/a_j-1\le d<8n_j+4$ already gives a positive physical lower bound for small $a_j$. This
proves W360 in both cases. W203–205's comparison of rates requires the $n^4$ conversion above. With
unnormalized $\gamma$ fixed the displayed bound there scales as $n^{-5}$.

The logarithm is the price of the single separated covariance and its polynomial prefactor. The cited paper
has a stronger conclusion on its own torus-limit and transfer-matrix interface (source lines 4454–4484,
6077–6127). Along a subsequence with $n_ja_j\to0$, its fixed-cutoff gap gives a vanishing centered matrix
element at each positive physical time, since the reflected norm at time zero converges. A nonzero matched
vector has strictly positive $\langle v,e^{-tH}v\rangle$. Thus that stronger interface excludes even this
subsequence. Theorems 45 and 84 use a boundary-influence and a local spectral hypothesis respectively. UNI-3
directly bounds cubes satisfying BP.

## 4. The tuning proposition

Row 924's (UNIV-K) compares a two-torus free-energy difference at successive cutoffs with a summable error.
Its (MAPCONV) bounds differences between aligned one-step maps. Its (CLASS) asks whether the interpolated
recursions admit a uniform analytic tuning with prescribed end data.

**Observation 3.1, W276–279 — HOLDS.** Choose the same *reference* endpoint $X_0$ as well as the same target
$X=X_0+\zeta$. Y93573–93594, 94071–94089 give $a^A_j-a^B_j=b_N-b_j$, including zero at $j=N$, and
$|b_N-b_j|\le 2B_b\lambda_b^j$. The one-step discrepancy is $b_{j+1}-b_j$. W394 conflates the one-step and
tail differences.

**Proposition 3.3, W263–275, 290–323 — HOLDS AFTER CORRECTION as an abstract tuning lemma. The claimed
application closing (CLASS) FAILS at W295, 307–308.** The account proves tuning for one frozen presentation
(Y94034–94040, 94112–94146). To extend its argument, identify the raw profile spaces, the companion and all
formation domains, and supply a horizon-uniform contracting norm for the *interpolated* transports on them. A
common contracting transport is sufficient. Section 5 tests their claimed equality.
Freeze each endpoint's actual cutoff, fluctuation scaling and map in **its own real presentation**. Use B's
frame only as coordinates for the common box and its estimates. Re-evaluating A's formation integral with B's
cutoff would change the map at $s=1$.

Here is the hand check on those premises. Write $s$ for W's $s'$, $a=a^B$, and retain the affine formulas
W294–295, using $T_j(s)=(1-s)T^B_j+sT^A_j$ when necessary. On a fixed inner box $|x_j-a_j|\le\delta a_j/2$,
both original $x$-discs contain the box with room by Observation 3.1 and $a_j\ge cX_0$. First choose the
enlarged input and profile balls, then the floor. For $w(t)=(\log t)^m/t^p,\ p=1,2$, the logarithmic
derivative is $(m/\log t-p)/t$. Thus the two weights differ by a factor $1+O(1/X_0)$. The sum of the absolute
interpolation coefficients is at most $1+2\epsilon$. Y93620–93656 and 94118–94126 now give the same
derivative estimates, with larger constants. The additional scalar $s(b_{j+1}-b_j)$ has zero $x,h$
derivatives. Its tail is exactly $s(b_N-b_j)$, uniformly bounded for $s$ in the prescribed complex
neighbourhood. Even its absolute sum is bounded by $2(1+\epsilon)B_b/(1-\lambda_b)$. Literal R5's *pointwise*
size estimate for the entire shifted remainder is unnecessary and does not follow from a geometric-in-$j$
estimate at fixed $j$ as $N\to\infty$.

In a uniformly equivalent norm in which $\|T_j(s)\|\le q<1$, the forward induction gives
$qH_*+B'_n+C'e_j\le H_*$. Y93739–93768 give $d_{j+1}\le q_1 d_j+C'k_j\|x-\tilde x\|_\infty$, hence
$d_j\le C''k_j\|x-\tilde x\|_\infty$. The backward map differs from $a_j$ by at most
$|\zeta|+2(1+\epsilon)B_b+C'(1+\log^{m+1}a_j)$. Choose the endpoint radius small, then $X_0$ large, so the
image lies strictly inside the common box. Its Lipschitz bound is $C'''\sum k_j<1/2$ by Y93836–93854,
94083–94095. W313's *numerical* constant need not be unchanged. The additive drift contributes zero to it.
Iterating in the fixed raw spaces converges locally uniformly and gives joint holomorphy in $H,\zeta,s$. Real
input gives a real solution for **real** $s$. On that slice the scalar envelope and
$x_0=X+b_\infty N+O(1+\log^{m+1}(X_0+N))$ follow by the same tail sum. Identification with an actual integral
at intermediate $s$ requires its own identity (Y93925–93934).

For W315–317 the box inclusion is in the wrong direction. A point in A's full box need not be in B's half
box, even for coincident frames. Instead the constructed fixed point at either endpoint belongs to that
endpoint's original box and solves its original equations. Endpoint uniqueness identifies it there. For the
two **specified runs**, interpolate the initial data as well, $H(s)=s h_1^d$, with room for its complex
neighbourhood, and keep $x_N=X$. This is row 924's erratum at lines 244–247. Solving at a single common $H$
would not recover both endpoints.

## 5. The two transports and their norms

**Lemma 3.2, W280–288 — FAILS for the exact transport identity at W284–286.** In final-spacing-one units,
Y57943–57959 define $h=L^{-k}$, $\xi=L^{s-k}$ and

$$
 B_\xi(w)=i^{-1}\log\big(M^s U_k(e^{iw})\big).
$$

The suppressed parameters in $B_\xi$ include the fine mesh and the depth of the critical orbit. Y56048–56071
identify the intermediate field as critical for the *effective classical action* $S_s$ on its next mean
fibre. Y58307–58340 and 93510–93544 give nesting within one original lattice. At the first aligned step the
two fields are $U_1(W)$ and $MU_2(W)$, in the same old units and up to old site gauges. Y59338–59346,
60651–60685 give identical tent weights. The following test distinguishes the pullbacks even after pointing.

**A counterexample inside the account's profile space.** Use a compatible periodic four-torus at the trivial
flat field. Prescribe an infinitesimal final field in one colour in direction 2 with nonconstant periodic
amplitude $w_I$ depending only on coordinate 1. Use per-unit-length potentials at both meshes. The flat
quadratic action is $\tfrac12\|dA\|^2$. Differentiating the constrained stationarity equation at zero makes
the first variation of the background a minimizer of this quadratic form under the linearized mean
(Y42083–42121, 42189–42199). The literal linear mean is the straight block/path sum plus a coarse gradient.
It takes fine gradients to coarse gradients of the node restriction (Y8254–8273). The per-length straight sum
and its composition are Y21358–21381, 22421–22453.

Here this reduces exactly to minimizing $E(y)=\sum_t(y_{t+1}-y_t)^2$ with prescribed arithmetic block
averages. Indeed, take the direction-2 link component along the chosen colour and average over coordinates 2,
3 and 4. The average of $d_2 A_1$ vanishes by periodicity. The squared $12$-curl, by the mean-square
inequality, bounds a fixed positive multiple of $E(y)$. All other curvature terms are nonnegative. Averaging
the straight constraint over the same transverse planes gives the block average of $y$ in coordinate 1. Each
fine transverse site occurs with the same multiplicity in those path sums. Conversely the field with sole
component $A_2(t)=y_t$ in that colour attains the energy bound and the straight constraint. A coarse gradient
can be lifted by extending the gauge parameter at the nodes to fine sites. Any two minimizers have the same
curl by the quadratic energy identity. Their difference is a gradient plus a constant form on the periodic
lattice, as one sees by subtracting its periods and integrating along paths. The partial linear mean takes
both terms to curl-free old fields. Thus the scalar minimizer gives the actual old plaquette curvature.

Let $v_i$ minimize $E$ on the **old** lattice with means $w_I$ on blocks of $L$ sites (run B). For run A,
minimize on the lattice one level finer, with the same means on blocks of $L^2$ sites. Call this minimizer
$y$ and set $u_i=L^{-1}\sum_{s=0}^{L-1}y_{Li+s}$, its old mean. Nested centered odd blocks are consecutive
blocks in this indexing after shifting the origin. Set $(Dz)_t=2z_t-z_{t-1}-z_{t+1}$. Variation of two sites
with opposite signs in any block shows $Dv$ is constant on each old block and $Dy=\ell_I$ on each fine block
of $L^2$ sites. Some adjacent $\ell_{I-1},\ell_I$ differ. Otherwise their common value is zero by periodic
summation, which would make $y$ and $w$ constant.

Telescoping first differences gives

$$
 (Du)_i=\frac1L\sum_{s=0}^{L-1}\sum_{h=1-L}^{L-1}
               (L-|h|)(Dy)_{Li+s+h}.
$$

At the second old site of block $I$ this is $L^2\ell_I$ for $L\ge3$. At its first old site it is
$L^2\ell_I+c_L(\ell_{I-1}-\ell_I)$, where $c_L>0$ since the stencil crosses the left boundary with positive
weight. Thus $Du$ is nonconstant in this block. Both $u$ and $v$ have the prescribed means and the energy is
strictly convex on their differences (its only periodic zero modes are constants). Consequently $E(u)>E(v)$.
The quadratic coefficients of the **old Wilson plaquette action** on the two intermediate fields differ by
this strict inequality, with the same positive normalization. Node gauges cannot change it.

For an admissible test, fix this old torus side $P$. At an anchor sum the site plaquette energies over a
translated window of $P^4$ sites, average over the hypercubic images of the window, then square. Give each
site one quarter of each incident plaquette energy. This is a gauge-invariant, covariant, finite-range
analytic pointing, using $1-\tfrac12\operatorname{tr}U_p$ on the complexified bond ball. Its Taylor expansion
starts in degree four, so its companion curvature coefficient
vanishes (Y58397–58412). Use its periodic evaluation for every period and rescale by a fixed constant if
needed. On the chosen torus every such window covers all sites exactly once. The pointing at every anchor is
the square of the total old Wilson action. The fourth-order coefficients of its two pullbacks are therefore
different. The tent sum multiplies each by the same strictly positive factor. This gives $T^A_0\ne T^B_0$ for
the physical operators. This is a discrepancy at $j=0$. A depth-difference bound $C\lambda_0^j$ allows it.

**Norm clause of (MAPCONV), W286–287, 332–335 — HOLDS for uniform equivalence. The deduction of exact
equality FAILS.** On aligned lattices choose identical old units, localization cubes,
$r,\kappa,\gamma_{\rm per}$, companions and compatible period family. Y59540–59562, 59577–59592 define the
raw norm geometrically, including its finite-period term. Its zero-coefficient condition is the same
affine-curvature Hessian test. For either run Y93546–93565 then give
$\|h\|_{\rm raw}\le\|h\|_{*,A/B}\le C_T\|h\|_{\rm raw}$, which proves the comparison row 924 asks for. Each
supremum uses its own future transports. Different transports alone do not decide equality of the two
suprema. W supplies no identity for them. For example, for horizon one on a scalar space, transports $2q$ and
$0$ obey a common pure transport estimate with $\lambda=q/2,\ C_T=4$, but their adapted norms are $2|\cdot|$
and $|\cdot|$. This last example tests the inference from the estimates only.

**Lemma 3.4, W325–330 — HOLDS for the product bound. The tuning conclusion HOLDS AFTER CORRECTION**
on identified raw spaces, conditional on the stated summable difference. In an ordered product of $n$ factors choose $m$ perturbations
$E_i=(1-s)(T_i^B-T_i^A)$. The $m+1$ intervening unperturbed segments contribute at most
$C_T^{m+1}\lambda^{n-m}$, including empty segments. Summing subsets gives the printed $C'_T\lambda^n$,
$C'_T=C_T\exp((1+\epsilon)C_T\tau/\lambda)$. Use products of the interpolated *one-step maps* in the adapted
supremum. Shifting the product length gives the one-step bound $q$ and raw equivalence constant $C'_T$.
Convert also $B_n$, the initial radius, both formation-domain ceilings and the derivative bounds to these
norms before choosing $X_0$. Although the adapted norm depends on $s$ and need not be holomorphic, the maps
and iterates are holomorphic in fixed raw spaces, with uniform norm equivalence. Section 4's proof applies.

Neither separate pure bounds nor equivalence of adapted norms gives this additional hypothesis. Even with the
one-depth shift, the scalar sequence $T_{2i}=3,\ T_{2i+1}=0$ and its shift each have every product of length
two zero. Their midpoint has length-$n$ product $(3/2)^n$. With zero formation terms this already loses the
uniform profile ceiling for nonzero initial data. This is a counterexample to the abstract inference in
W295–308, alongside the physical counterexample to the exact transport identification. The
summable-difference hypothesis itself has no proof in W. Conversely, the original (MAPCONV) operator estimate
$C\lambda_0^j$ would give $\tau\le C/(1-\lambda_0)$. On uniform common formation domains this proves the
analytic (CLASS) condition as a consequence of full (MAPCONV). The converse implication from summability to
the geometric source bound fails, as the scalar differences $(j+1)^{-2}$ illustrate.

## 6. Remaining statements and scope

**A finite-torus counterexample to the unrestricted reading of UNI(b), W173–179.** The clock issue can
actually change the conclusion. Take even tori of fixed physical side one, $a_j=1/(2j)$, and two time slices
half a period apart. On each slice use the three normalized real traces of two spatial winding holonomies
$A,B$ at a common base point and of $AB$. Every trace has expectation zero by a spatial centre-sheet flip. On
flat configurations the triples on the two slices agree by parallel transport. Their entries are
$\cos\alpha,\cos\beta,\cos(\alpha+\beta)$, since flat holonomies commute. Their squared sum has a strictly
positive minimum $c$ on the angle torus because the three cosines cannot vanish together. The sum of the three
cross-slice products is continuous and exceeds $c/2$ in a neighbourhood of the flat set. For each fixed
lattice the Wilson measure concentrates in any such neighbourhood as its coupling tends to infinity. Indeed,
the nonnegative action has a positive minimum on the compact complement, whereas a smaller sublevel set
around the identity has positive Haar measure. Choose a finite coupling large enough at each $j$. Some
cross-slice covariance is then at least $c/12$, with sup norms one and fixed physical separation.

On **each** finite torus at that coupling let $m\le d\mu/d\nu\le M$, $m>0$, for product Haar $\nu$. The
single-link form is a sum of squared distances to the respective exterior subspaces. Comparison of those
distances gives $\mathcal E_\mu\ge m\mathcal E_\nu\ge m\,\mathrm{Var}_\nu\ge(m/M)\mathrm{Var}_\mu$. The
middle inequality follows by decomposing into the joint eigenspaces of the commuting Haar coordinate
projections. On each nonconstant component at least one $I-P_e$ is the identity. Repeat every singleton
$\lceil M/m\rceil$ times in the list. On every torus this gives a gap at least one on the full $L^2$ space
with $b=0$, while preserving the displayed
nonvanishing covariances intact. This counterexample uses W(b)'s finite-torus option and unrestricted
trajectories and lists. The corrected bounded-overlap result applies to the usual clock conventions.

**W1–46, 50–57.** **HOLDS AFTER CORRECTION.** For the matched scalar sector, rows 1179/1183 and 1225/1232
give a sufficient implication. At the explicit aspect the neutral trace bound gives $q_*=5041\,2^{-18}$, time
$L/2$, and $M_*=(2/L)\log(1/q_*)$. Positivity of the transfer permits the integer time
$\lfloor n_j/512\rfloor$. The temperature description is its physical-scale interpretation. Row 1180 lines
95–119 uses the least passing size **on a common admissible grid**, $\nu'$, and seed propagation on that
grid. An unrestricted least size does not place the seed at one fixed physical $L$. In the trace a level
of energy $m$ and multiplicity $D$ contributes $D\exp(-m u)$. A gap by itself supplies no
such count (row 1232). The claims of necessity in W50–55 **FAIL** as statements about every possible proof.
ONE-K also needs admissible predecessors and a base margin covering the summable tail at every reached base
datum (row 917 lines 247–272). One isolated good coupling is insufficient without that identification.

**W34–41, 59–82, 377–381.** **HOLDS AFTER CORRECTION** as a record of routes tried. The neutral-sign and
twist examples concern specified carriers. Row 1228 P5 is a Gaussian $U(1)$ squeeze. The 2D bracket method
and Ding–Huang–Yang's exchange of loop copies are distinct (row 1007). Compactness in row 1017 leaves its
rigidity hypothesis, and the Tomboulis bracket in rows 1025/1029 concerns the flux part. The dilute-defect
example, the absence of a small parameter in the attempted expansion, and the screening lists establish no
impossibility theorem for all defects, signs, gauges or band estimates. Row 1032 puts frustration-free
thresholds in **B1**, the transfer cone in **B2**. Row 1218 records conditional published criteria. Row
1220's Proposition U is an analogous bounded-torus estimate for Villain $U(1)$ with its own scale range
(lines 131–158), not a transfer of the literal SU(2) constants or an all-volume result.

**W83–101, 196–214, 242–251.** **HOLDS AFTER CORRECTION** for the heat baths and full-product curvature bound
in §§2–3. B Corollary 74 and A Theorem 9.14 supply restricted strong-coupling estimates. A Theorem B and B
Theorem 66 *use* BP for a continuum implication. A's Lemma 6.2, checked in row 1224, already uses a cube
clock-chain argument. The account's basic smeared insertion is a sum of bounded plaquette energies
(Y1647–1656), hence polynomially bounded for each fixed compact test and finite product. Its first-passage
increment upper bound with $a=L^{-K}$ already gives $\beta=O(1+\log(1/a))$, enough for UNI-2 (Y1659–1666). These
observations concern the specified estimates and dense matched sector only. For the W87 rate without the
logarithm, suppose fixed-cutoff torus limits and convergence of centered
reflected norms **and** time translates are given. Then (a) at arbitrarily large integer times bounds each matched
vector's transfer spectral support by $e^{-\kappa_j}$. A positive spectral mass above that number would
eventually violate (a), whose prefactor is fixed at that cutoff. Passing the normalized semigroup bound to
the limit on a dense sector gives $\limsup\kappa_j/a_j\le\inf\sigma(H\vert_{\Omega^\perp})$ on a nontrivial
sector. This extra argument does not follow from one separated pair.

**W253–274, 319–323.** **HOLDS AFTER CORRECTION.** The source explicitly freezes the presentation. Row 924
lines 219–224 prescribe interpolation of **maps on common domains**. They do not prescribe recomputing
cutoffs at complex frames. A constant drift can exceed R5's pointwise size allowance. The upper estimate on
$b_{j+1}-b_j$ alone does not prove it does. The admissible analytic tuning result is §4.

**W332–348, 367–390.** **HOLDS** for the scalar $b$ clause and for leaving the formation comparison open.
Y94534–94545 imply $|b_{j+1}-b_j|\le C(1+\lambda_0)\lambda_0^j$, and likewise for $m$. Y61191–61223 bound the
*anisotropic weight derivative's* zero-readout remainder $q_{j,e}$. It is a different object from the
difference of unmarked pointings $n^A_j-n^B_j$. Those lines supply no such difference estimate. **FAILS** at
W335–345 that (MAPCONV-F) is all that remains or actual (CLASS) is closed. The geometric-in-depth transport
difference and stability of the interpolated products still require estimates. The adapted-norm *equivalence*
clause is supplied. Differentiating the two recursions on an admitted family gives both sources,
$-(\Delta b+\Delta r)$ and $\Delta T\,h_j+\Delta n+\Delta f$, where each difference holds $x,h$ fixed. The
initial source is $h_1^d$ and the endpoint source is zero (Y94196–94213). W346–347 account only for the
scalar source.

**W350–394.** **HOLDS** for UNI-3 with its hypotheses, for the absence of a seed in W and for the absence of
a mass-gap proof. W371's “no attack on file” can only mean no successful seed estimate. **FAILS** for the
status elevations at W372–374 and W394 beyond §§2–5. Row 925 lines 197–229, 298–308 additionally require
first-passage admissibility, common final integration/evaluation and control of vacuum wrapping terms. VAC-ID
and DENS-K B1/B2 retain their premises. The regular recursion in Y93438–93448 excludes complementary
large-field operations. None of these physical identifications follows from the formal interpolation.

The dated reading and scheduling notes in W1–18, 43–46, 251 and 377–392 are provenance or the author's
choices. The cited revision of Y contains the requested source at its root. The checks above concern the
mathematics at the two pinned revisions.

RESULT: UNI(a) and UNI-3 hold. UNI(c) holds with the stated zero-interaction convention. UNI(b), UNI-1 and UNI-2 hold after correction, with $\gamma_j=O(a_j\log(1/a_j))$ for bounded block overlap and a persistent separated covariance. Lemma 3.2's exact transport identity fails on a Wilson observable. The adapted norms are uniformly equivalent. Proposition 3.3 and Lemma 3.4 give conditional analytic tuning. The required cross-depth transport and formation estimates, physical (CLASS), (UNIV-K), (N-phys) and the four-dimensional SU(2) mass gap remain open here.
