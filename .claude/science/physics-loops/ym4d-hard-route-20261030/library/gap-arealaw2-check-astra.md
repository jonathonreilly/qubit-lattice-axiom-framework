# Repo search

The requested `prior/gap-arealaw2-check-astra.md` is absent. The lead's
`prior/repo-search-2026-11-08.md` records searches of main and PRs 10114,
10133, 10134 and 10141, but concerns older RG obligations, not this star
marginal. Row 834 has no target-specific Repo prior work line. Its direct
antecedents are `gap-vmf-lip.md` (Codex, sharp vMF chord bound and comparison),
`gap-arealaw-opus.md` (Claude, slab reduction and the already proved 2/3
range), and `gap-compress-opus.md` with its check (the flat-slab infrared
obstruction). These are reused, not claimed as new. No matching owner was
found in `open-registry.md`, `open-core.md` or `l17c.md` for arealaw2,
decimation, SLAB or ferromagnet. This is the assigned check, not an attack
on the open (SE) supplier.

The existing `gap-vmf-lip.md` and `gap-compress-check-astra.md` search
records supplied these outside-lane hits, checked at source here:

| Source read | Proximity and use |
|---|---|
| main `bb4ec020d5ada57c630dd89acc98a68397ade423`, `docs/ADMISSIBILITY_RULE_RECORDS_THAT_MOVE_WITH_VACANCIES_THE_INFRARED_STIFFNESS_IS_SET_BY_THE_BINDING_SCALE_LONG_RANGE_ORDER_ABOVE_THE_NEUTRAL_SCALE_AND_NO_FULL_BOUND_AT_IT_BOUNDED_THEOREM_NOTE_2026-09-24.md:1–190`, T2/T4 | Same Gaussian-domination and Parseval method in a sphere/vacancy model. Credit its recorded Claude Opus 5.5 attempt and FSS; reuse the argument, not its model identification. |
| main, `docs/ADMISSIBILITY_RULE_SPHERE_STATIC_LAW_ZERO_FIELD_COMPONENT_FOURIER_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-15.md:58–81` | Fixes the same dispersion and bond normalization, for S2 rather than S3. |
| main, `docs/ADMISSIBILITY_RULE_CUBIC_WALK_RETURN_SUM_AND_SPHERE_STATIC_MAGNETIZATION_SUFFICIENT_BOUND_BOUNDED_THEOREM_NOTE_2026-09-15.md:1–180` | Same Green integral. Its 1000-term certificate is not used under the no-computer-proof rule. |
| PR 10133, `89faef229ff6e6bde42baad15ed8270c2f4087d8`, soft-route `MASS_GAP_CW_CROSSOVER_ATTACK.md:115–174` | Same vMF law and transverse-moment identity; the broader chord estimate is not there. Credit the Grok branch's prior formulation. |
| PR 10114, soft-route `TQ55.md:228–239` | Warns that temporal-gauge FSS is only one-dimensional. Different from the present conditional 3D flat slab. |

Here “soft-route” means `.claude/science/toe-ruleset-20261021/agents/ym4d-proof/`.
After fetching the four requested PR heads, the narrow expression
`gap-arealaw2|decimated.{0,30}slab|star.marginal` had no matches within
that directory or `research/ym4d/`. Two broader main scans were cancelled
without completion; no absence claim rests on them. The November 8
record's thirteen RG targets do not cover this check.

**Outline/account lookup.** The README, neighbouring chunk rows and
obligations were consulted first. The named vMF/Dobrushin/decimation/
ferromagnetic/area-law search found no matching supplier in the outline
or CA-I; this is not an exhaustive absence theorem. SA 580–599 supplies
only the gap-scope warning. SA 2195–2240 already supplies the SU(2)
Bessel coefficients and positive series; Section 7 uses that series,
not a new derivation of it. Credit Ethan Sussman and Levent Alpoge, with
Claude and Codex as authors of their text. Both requested files at
`31a47c543775` were downloaded once into
`/tmp/sa-gap-arealaw2-check-astra.woq_3n4k/`; their line counts are
32992 and 166711. No CA-I 4.12–4.19 result or Balaban-paper estimate is
used. The CA subindex was searched, not the whole account read.

Provenance: Codex, row 857; requested runner gpt-6-astra/xhigh; checked source
`a875387e1c32512d38a3b52b6c0ef03f8874545b`, `library/gap-arealaw2-opus.md`
(489 lines), by Claude Opus 5.5. Research text, not an audit; no status grant.
The argument below uses written estimates only. GUIDE runs in the source
were not rerun or treated as proof. External publication and pushing were
not requested.

# Statement checks

Verdicts below concern the printed mathematical statements and their named inputs. No scientific or audit status is granted.

## 1. Exact single-site barrier — HOLDS

Source 3.3, Proposition B(i), lines 148–161. This is for the six-neighbour
periodic slab, beta >= 0 and unit bond strengths (signs can be absorbed
into O). At beta=0 both sides vanish. At beta>0 fix the changed spin w_y.
Of the five other rotated spins choose one equal to -O_xy w_y and two
opposite pairs. Thus the initial field is exactly zero. An arbitrarily
small nonzero change of w_y gives F'=beta O_xy(w'_y-w_y). The linear
unit-direction test in that direction yields

\[
 \frac{d_{\rm Lip}(\mu_0,\mu_{F'})}{|w'_y-w_y|}
 \ge \beta a(\beta|w'_y-w_y|)\longrightarrow\beta/4.
\]

Theorem V and V1 of `gap-vmf-lip.md:59–220` supply the reverse inequality.
Hence C*=(beta/4)A. Summing the putative inequalities C*w <= alpha*w
against the constant left eigenvector gives alpha >= 3 beta/2. This
checks the weighted barrier without any numerical Perron computation.
It excludes this worst-exterior, single-site chord criterion only;
"every single-site method" in the summary must retain that qualification.

## 2. Decimated chart and Lemma F — HOLDS

Source 3.5 and 4.2. Absorb a signed unit J_xz into its orthogonal O_xz.
On the even torus the E sites have no mutual bonds. Their independent
integrals are exactly z(|F_x|). Boundary terms at retained sites give
exp(F0_z.h_z); boundary terms at eliminated sites enter G_x. Thus the
printed odd conditional density is exact. Its dependency graph consists
of two-step paths. Set n_zz=0: the displayed sum over z' means z' != z.
Each of six eliminated neighbours has at most five other retained
neighbours, counting coincident paths separately. This gives 30 also on
side-four tori. It is an upper bound in a free box.

A change of h_z' changes each affected G_x by an isometry times beta
(h_z'-h'_z'). Telescoping the affected messages proves
C^D_zz' <= beta c(beta)n_zz'. The supremum defining c must include the
base values and evaluation points on each field segment; equivalently
it is the derivative at t=0 with arbitrary G_i. The conditional laws
are continuous, positive and defined at every exterior, so DC applies.

For Lemma F, integrate the other leaves first. Under the resulting
joint law Q, h|y has law lambda_(F0+beta y), whereas the y marginal is
exp(G1.y) Zhat(beta y) sigma(dy) after normalization. This gives an exact
mixture with a kernel independent of G1. The derivative of its average
of psi along the straight chord from y to y' is
beta Cov_lambda(psi,(y'-y).h). The chord lies inside the closed unit ball;
this explains precisely why the supremum is over F0+beta B, not only
its boundary. Differentiating the leaf marginal along G1 to G1' gives
the second tau factor. Multiplication and integration give Lemma F with
exactly the printed beta. No convexity or ferromagnetic premise enters.
The zero-field specialization gives c <= beta/16 at that specialization,
not a uniform bound on c(beta).

## 3. In-star Dobrushin calculation — HOLDS AFTER CORRECTION

Source 4.3, Proposition B(ii). Put c0=beta/4. On an n-leaf star the
centre-to-centre Green entry is (1-n c0^2)^(-1); the chosen leaf entry
is 1+c0^2/(1-n c0^2). These follow by summing the alternating walks,
or eliminating the leaves in (I-C)v=e_j. For lambda use five leaves;
for pi use six. The field discrepancy is |dF|/4 by V1. Consequently

\[
 \tau(\lambda)\le\frac1{4(1-5c_0^2)},\qquad
 \tau(\pi)\le\frac{1-5c_0^2}{4(1-6c_0^2)},\qquad
 \alpha_D\le\frac{30c_0^2}{1-6c_0^2}.
\]

The Neumann/comparison argument requires 6c0^2<1. Positive star
weights sqrt(n) at its centre and 1 at leaves give weighted contraction
sqrt(n)c0<1, even when the unweighted centre row sum exceeds one.
Within this domain the last displayed bound is below one exactly when
36c0^2<1, or beta<2/3. This supplies the missing convergence qualifier;
the rational expression is not a valid bound after its denominator
vanishes. The specific two Green-function estimates return 2/3. The
sentence "every bound assembled from single-site Dobrushin steps" is
not proved: it must refer to this calculation, not all refinements of
multi-site comparison.

## 4. Theorem A2 — HOLDS AFTER CORRECTION

Source Step 7. The implication and C_D=48/(1-q_D) hold on the stated
even tori for beta>0, with (SE) a supplied hypothesis. Retain the colour
D containing x and integrate E. Lemma F gives C^D_ij <= beta^2 tau_*^2
n_ij and row sums at most q_D. Each influence step covers two original
edges. Hence G^D_ij <= q_D^ceil(d(i,j)/2)/(1-q_D).

For even R, conditioning on h_y and using the vector version of DC
from `gap-arealaw-opus.md:213–248` gives N(x,y) <= 2G^D_xy. For odd R,
let g_a=(O m(F_y))_a and f_a=(h_x)_a. Both have mean zero by the global
sign. Since |g_a|<=1, the **normalized** probability (1+g_a)mu_D has
the same kernels off N(y). Applying DC to f_a yields

\[
 |\mu_D(f_a g_a)|\le 2\sum_{j\in N(y)}G^D_{xj}.
\]

Summing four components and at most six neighbours gives exactly
48 q_D^((R-1)/2)/(1-q_D). This also bounds the even-R estimate. Thus
Lemma R multiplies T factors as claimed; exchange the directions and
choose the smaller perimeter exponent. The logarithmic area coefficient
is (1/2)log(1/q_D). This checks the normalization omitted from the
source's notation `(g+||g||)mu_D`; one can also normalize that measure
and multiply back by ||g||.

At beta=0 the Wilson-loop expectation is zero for a nonempty rectangle,
by Haar integration of any edge used once. Use this separate case.
The combined expression q_D^(-1/2) and its logarithm are undefined at
q_D=0. In the two separate power bounds take 0^0=1. No constant or
positive-beta range is lost by this correction. The numerical example
tau_*=1/4 is only a counterfactual input; Section 10 below shows it
cannot hold on all of C5 when beta>0.

## 5. Leaves-first reduction and Corollary A2' — HOLDS AFTER CORRECTION

Source 5.2 and Step 7. In the dimer, y|h is mu_(G+beta h), so averaging
any chord-1-Lipschitz test has h-Lipschitz constant beta/4. The h marginal
is an S1 law, whose response to K is at most tau_1. Thus the claimed
one-message sensitivity (beta/4)tau_1 is exact as an upper bound.

For n<=6 leaves set a=beta^2 tau_1/4. The leaves' comparison matrix
has entries a off the diagonal. Its row and column sums are (n-1)a;
the field perturbation at leaf 1 has discrepancy tau_1|dG_1|. The
averaged centre test has coordinate seminorms at most beta/4. The
geometric series therefore gives

\[
 c(\beta)\le\frac{\beta\tau_1}{4(1-5a)},\qquad
 \alpha_D\le\frac{30a}{1-5a}=:q'_D.
\]

The assumption 35a<1 guarantees convergence and is equivalent to
q'_D<1. Apply the proof of A2 with q'_D; no C5 or C1' premise is needed.
At tau_1=1/4 the endpoint is exactly 4/sqrt(35); at beta=2/3 the needed
strict inequality is tau_1<9/35 (approximately 0.25714). The rounded
decimals are illustrations, not endpoint definitions. The sole theorem
correction is the beta=0 convention already given for A2. The weighted
Wasserstein comparison used here follows DC's displayed telescoping
proof by replacing its discrepancy 2 with b_j; no extra factor two
enters this formula.

## 6. Lemma P2 — HOLDS; its claimed uniform value 0.2580 — FAILS

Source Step 5 and 5.2. Put delta_f=mu(u(f-mu f)). Expanding the two
centred factors gives exactly
Cov_lambda(psi,phi)=Cov_mu(psi,phi)+mu(u psi^ phi^)-delta_psi delta_phi.
D1 in `gap-shape-exercise-astra.md:249–339` gives Var_mu(psi)<=1/3
for chord-1-Lipschitz psi; smoothing justifies its use for nonsmooth
psi. Cauchy–Schwarz gives

\[
 |\mu(u\widehat\psi\widehat\phi)|
 \le \|u\widehat\phi\|_2/\sqrt3,\qquad
 |\delta_\psi\delta_\phi|\le\|u\|_2^2/3.
\]

Together with V these prove P2, taking the supremum over e in its
right-hand norm. Since Var_mu(e.h)<=a(|F|)<=1/4 and
exp(-omega)<=w<=exp(omega), its sup-norm corollary is also correct.

The decimal is **correct conditional arithmetic**. If a single message
phi(s) has |phi''(s)|<=53/1000 on [-1,1] and is concave, subtract its
tangent at zero. The resulting R satisfies -53/2000<=R<=0. With
x=53/2000, the displayed Taylor-tail bound

\[
 e^x-1\le x+\frac{x^2}{2(1-x/3)}<\frac{5371}{200000},\qquad
 \sqrt3>\frac{433}{250}
\]

gives, by rational arithmetic,

\[
 \frac14+\frac{125}{433}\frac{5371}{200000}
       +\frac13\left(\frac{5371}{200000}\right)^2
 <\frac{129}{500}=0.2580.
\]

The source supplies no proof of the curvature premise 53/1000. Its
estimate is GUIDE-level, at beta=0.68 with |G|<=5 beta. S1 in the
corollary permits **every** K and every linear field; C1' is a further
Laplace-transform class. An estimate only on [0,6 beta] does not cover
these stated unbounded parameters without an additional reduction.
Thus the summary/FINISH reading "Lemma P2 gives 0.2580" fails as a
proved class bound. P2 is valid, but no uniform tau_1<=0.2580 was
established. No numerical search was used to repair that premise.

## 7. Decimation ceiling beta_D (about 0.7385) — HOLDS AFTER CORRECTION

Source 4.1 and Proposition B(iii). At F0=G_i=0 the centre law is uniform,
m(beta h)=t(beta)h, and its linear test gives exactly t(beta)/4.
Thus the **particular certificate** 30 beta c(beta)<1 cannot pass the
unique positive solution 30 beta_D t(beta_D)=4. The exact equation,
not a rounded decimal, defines the threshold.

Here is a short hand check of the digits. Set u=beta^2/4. Dividing
30 beta I2(beta)-4 I1(beta) by 2 beta gives the same sign as

\[
 D(u)=-1+\sum_{k\ge1}\frac{15k-1}{k!(k+1)!}u^k
 =-1+7u+\frac{29}{12}u^2+\frac{11}{36}u^3
       +\frac{59}{2880}u^4+\cdots.
\]

All positive-degree coefficients are positive. D starts at -1 and
increases to a positive value, so its positive root is unique. At
beta=0.7384, u=0.13630864 and the cubic partial sum is less than
-0.0001638. Here u^4<0.000346 and consecutive tail terms starting
at k=4 have ratio below 0.006; the tail is less than
(59/2880)(0.000346)/(1-0.006)<0.0000072. Hence D<0. At beta=0.7385,
u=0.1363455625 and the cubic partial sum exceeds 0.000119; hence D>0.
All these decimal bounds are terminating rationals with four displayed
polynomial terms. Thus 0.7384<beta_D<0.7385; “about 0.7385” is adequate,
but not an exact cutoff or a proof of a sharp attainable range.

The source's ARGUED all-zero-G environment can be supplied explicitly,
so no numerical solvability argument is needed. In the flat slab,
centre the retained site at 0 and choose orthonormal u,v. Put

\[
 h_{2s e_i}=-u,\qquad
 h_{s e_i+t e_j}=\tfrac14u+st\tfrac{\sqrt{15}}4v
 \quad(i<j,\ s,t\in\{-1,1\}).
\]

At each eliminated neighbour s e_i the other five spins sum to
-u+4(u/4)=0; the transverse terms cancel in pairs. This is consistent
also on side-four tori, where +2e_i and -2e_i coincide. Other spins
are arbitrary. Varying any retained neighbour z' tangentially changes
the n_0z' incident messages. At this environment their derivative score
is beta n_0z' t(beta) Delta.h. A linear test along Delta gives
C^{D,*}_0z' >= beta n_0z' t(beta)/4. By translation the flat slab's
optimal retained single-site matrix dominates (beta t(beta)/4)n,
whose constant row sum is 30 beta t(beta)/4. Summing against positive
weights proves the same ceiling for weighted retained single-site
chord Dobrushin. This repairs the source's unsupported “should exist.”
It excludes neither larger blocks nor other comparison criteria.

## 8. Slab symmetry and the ferromagnetic frame — HOLDS AFTER CORRECTION

Source 3.1–3.2, 6.3, Proposition B(i). The push-forward identity
mu_O -> mu_(O^g), O^g_xy=g_x O_xy g_y^T, is correct. It preserves
chord distances and all optimal influence coefficients. Setting tree
bonds to I is a coordinate change, not deletion of spin variables.
For beta>0, within the stated family of sitewise rotations, the
stabilizer is exactly g_x O_xy g_y^T=O_xy. Distinct edge bilinear
coefficients can be isolated by integrating against coordinate
functions, so equality of the total density forces these identities.

Two qualifications matter. At beta=0 the product law has independent
O(4) symmetry at every site. At beta>0 its stabilizer need not consist
of spatially constant rotations. If O_xy=r_x^T r_y is a nonconstant
pure gauge, every g_x=r_x^T g r_x preserves the law. These g_x need
not be equal. More generally choose a root and a tree: g_root must
commute with all based loop holonomies, and parallel transport then
determines every g_x. There is no **independent** local gauge freedom,
which is the valid conclusion needed here. The unqualified summary
“only global symmetries” is false if it means constant g_x; lattice
automorphisms are also outside the asserted stabilizer description.

For unit nonzero bond strengths (absorb signs into O), a common
ferromagnetic frame exists iff **all cycle holonomies** are identity.
Necessity follows by telescoping g_x O_xy g_y^T along a cycle.
For sufficiency, tree transport fixes g_x so tree bonds become I;
each remaining bond becomes its fundamental-cycle holonomy. Hence it
also becomes I. This is an exact finite-graph argument.

On a torus, plaquette holonomies alone are insufficient. Put a fixed
nonidentity R in SO(4) on every bond crossing one periodic seam and I
elsewhere. Every plaquette has holonomy I, but the winding cycle has
holonomy R. Also arbitrary plaquette values cannot be assigned
independently; they satisfy connection compatibility identities. The
true realizability statement is that any SO(4) **bond assignment** in
one slab lifts bond by bond to a pair of SU(2) face connections.
The associated left/right holonomies, including winding cycles, are
understood modulo the common central kernel and conjugacy.

Section 3.2 is only a diagnosis of the old product estimate: pinning
spins can create nonzero means, so a connected covariance bound alone
does not bound its factors. An actual 4D gauge change also changes the
face data and observables. The claim that it rules out every gauge-fixed
area-law argument does not follow. The narrow diagnosis HOLDS; that
universal reading FAILS.

## 9. Infrared ceiling 4G3 — HOLDS

Source 6.4 and Proposition B(iv), conditional on the stated FSS bound.
The flat slab has weight exp(beta sum_<xy> h_x.h_y), with each unordered
bond once. For the unnormalized Fourier transform the component bound
is E|h-hat^a(p)|^2 <= V/(beta E(p)), E(p)=2 sum_i(1-cos p_i), p!=0.
This is the normalization of Fröhlich, Simon and Spencer, *Infrared
Bounds, Phase Transitions and Continuous Symmetry Breaking*, CMP 50
(1976), Section 2, Theorems 2.2–2.3 ([primary text](https://math.caltech.edu/SimonPapers/65.pdf)).
The finite-torus Gaussian-domination/Parseval argument already appears
in the main-branch vacancy-law note, T2 and T4; see Repo search above.
It is prior machinery, not a new result of row 834.

Parseval and |h_x|=1 give

\[
 V^{-2}E\left|\sum_xh_x\right|^2
 \ge1-\frac{4G_\Lambda}{\beta},\qquad
 G_\Lambda=V^{-1}\sum_{p\ne0}\frac1{E(p)}.
\]

On growing even cubes G_Lambda tends to G3: outside a small ball use
Riemann sums; inside use E(p)>=4|p|^2/pi^2 and integer shells, giving
an omitted contribution bounded by C delta+O(1/L). If
N(0,x)<=C r^d(0,x) with **C finite and 0<=r<1**, uniformly in volume,
its spatial average is O(1/V), since the number of sites at distance
j is bounded by a constant times (j+1)^2. Translation invariance makes
that average dominate the left-hand magnetization square. This
contradicts beta>4G3. The source's phrase “C,r<1” should not restrict
C; its argument works for every finite prefactor.

Use the exact integral G3=(2pi)^(-3) integral_[−pi,pi]^3 1/E(p) dp.
The decimal 1.0109 is approximate and not an exact sufficient cutoff.
The statement excludes a background-uniform slab **two-point decay
bound**, not the 4D area law or every conceivable use of slabs. It
implies nothing about a critical coupling near 0.936, which remains
GUIDE material here. The positive-part defect in the earlier TB2
formula is irrelevant in the present stated domain beta>4G3.

## 10. Remaining assertions and scope

**The tau_*=1/4 illustration — FAILS as an actual C5 bound.** Source
4.4, GUIDE run 1, Step 7. The source itself reports failure numerically;
here is a written check of that mechanism. For r>0, put A(r)=E_r h_1
and a(r)=(1-E_r h_1^2)/3. Folding the h_1 distribution to s=|h_1|,
differentiation gives
(d/dr)E_r s^2=Cov_r(s^2,s tanh(rs))>0, since both functions increase
strictly and the distribution is nondegenerate. Hence a'(r)<0.
For g>0 different from beta, the message
phi(s)=log z(sqrt(beta^2+g^2+2 beta g s)) satisfies
phi''(s)=(beta g)^2 a'(r)/r<0. Take two opposite fields +ge and -ge,
F=0, and the other messages zero. The axial density relative to uniform
is proportional to exp(phi(s)+phi(-s)). It is even and strictly
decreasing for s>0. Therefore E_lambda s^2<1/4 by the elementary
oppositely-monotone covariance identity. Each transverse variance is
(1-E_lambda s^2)/3>1/4. A transverse linear chord test proves
tau(lambda)>1/4. This refutes that proposed uniform constant for
any beta>0. It does not refute (SE) with a larger tau_* or A2's implication.
The source's positive numerical proxies supply no upper bounds on tau
or on c, because they test only linear functions.

**Nuclear norm target — HOLDS AFTER CORRECTION.** Source Step 1, 3.4
and the marks table. For M=E[h_x h_y^T], the O(4) supremum is ||M||_1.
The actual quaternion transfer norm is the SO(4) supremum, as 3.4's
inequality correctly says. Equality with the nuclear norm is not a
general identity: M=diag(1,1,1,-1)/4 has O(4) supremum 1 and SO(4)
absolute supremum 1/2. The nuclear-norm bound is a sufficient target;
operator-norm decay of M is equivalent up to the fixed factor four.
Do not replace the inequality in 3.4 by equality. A2 uses the valid
O(4) upper bound and loses nothing here.

**Free boxes and Gibbs states under (SE) — HOLDS.** The proof can be
completed without new premises. Free boxes have the same bipartition,
row bound and sign symmetry, so A2 applies directly. For a fixed
boundary, remove the external fields to make a sign-symmetric reference
slab. Its decimated kernels and those of the boundary-conditioned slab
coincide outside the retained sites at distance at most one from the
boundary. If both loop endpoints are at boundary distance m>=2, their
pair readout is either h_x.O h_y, of total coordinate seminorm at most
2, or h_x.O m(F_y), of total seminorm at most 1+3 beta/2 by V1.
Its support is at least m-2 original edges from the exceptional set.
DC bounds the change of this slab expectation by

\[
 \epsilon_m=\frac{(4+3\beta)q^{\lceil(m-2)/2\rceil}}{1-q},
\]

where q=q_D, or q=q'_D for A2'. Thus a boundary-conditioned rectangle
is bounded by (C_D q^((R-1)/2)+epsilon_m)^T and the exchanged expression.
This is uniform in the boundary. The DLR equation and m tending to
infinity give A2 in every infinite-volume Gibbs state. A finite
arbitrary boundary needs its error term; the periodic formula alone
is not asserted there. The beta=0 case is separate as above.

**Ferromagnetic comparison, Section 6.2 — HOLDS only as the displayed
conditional arithmetic; FAILS as an established O(4) range claim.** On
a free star, its centre-leaf component correlation is t(beta)/4: the
centre is uniform and the conditional leaf mean is t(beta)h_0. There
are 30 outgoing bonds in the infinite cubic lattice. Thus the printed
Simon–Lieb-type inequality, **if supplied for this O(4) model with the
printed coefficient**, gives exactly 30 beta t(beta)/4<1. The source
explicitly leaves that inequality unchecked. Neither its attribution
nor the assertion that larger sets converge to the true O(4) critical
point is established by its argument. Remove the unqualified statement
in the summary that the ferromagnet already has this star threshold.
The independently checked decimation ceiling in Section 7 survives.

The source check here verified the mean-field attribution more narrowly:
Barry Simon, *Mean Field Upper Bound on the Transition Temperature in
Multicomponent Ferromagnets*, J. Stat. Phys. 22 (1980), 491–493
([primary text](https://math.caltech.edu/SimonPapers/118.pdf)), proves zero
spontaneous magnetization for sum J<D, hence beta<4/6 in this model.
The [publisher's abstract of Aizenman–Simon](https://link.springer.com/article/10.1007/BF01982713)
states exponential decay above the mean-field temperature, but does
not print the finite-set inequality needed in 6.2. Its full text was
not accessible: the author-file request failed, the repository mirror
returned 403, and the publisher offered subscription access. No login
or payment was attempted. Consequently this check does not decide
whether the recalled O(4) finite-set inequality is true; it records
the missing premise and does not substitute an Ising theorem.
Likewise the proposed nonlinear diamagnetic comparison remains OPEN;
nontrivial holonomy prevents a flat frame, but does not itself disprove
such a comparison or prove it is the only way past the ceiling.

## Coverage and source limits

Checked the full 489-line source, including its marks and RESULT, against
the written arguments above. The existing best range beta_W<2/3 is
unchanged; the prior slab theorem and reduction are credited, not
re-proved as new work. (SE) and the S1 improvement remain unsupplied.
No guide optimization, quadrature, certificate, numerical test or audit
was run. The primary FSS and Simon papers were read narrowly online
because the platform requires verification of recalled specialist
literature; this was a limited conflict with the requested repository-only
search boundary. No other filesystem location was searched. The
inaccessible O(4) finite-set source remains unverified, as stated above.
Only this check file was changed; no registry, FINISH row or source note
was edited. No public post or push was authorized or made.

RESULT: HOLDS: exact (beta/4)A single-site barrier, decimated chart, Lemma F, P2 algebra, and the 4G3 two-point obstruction conditional on FSS. HOLDS AFTER CORRECTION: in-star domain and 2/3 calculation, A2 and A2' with their printed constants and a separate beta=0 case, beta_D ceiling with an explicit realizable environment, symmetry and all-cycle holonomy scope. FAILS as a proved bound: tau_1<=0.2580; tau_*=1/4 is false on C5. The recalled O(4) Simon–Lieb star-range claim is unverified. No area-law range beyond beta_W<2/3 is proved; (SE) remains open.
