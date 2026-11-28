# Repo search

**ARGUED / source record.** FINISH row 763; source checkout
`108455453498c50422f3b31e573fbeefd766c988`, 2026-11-12. Research text by
Codex, not an audit, not independently checked, and granting no status.
Here **PROVED** means a complete hand argument is written in this note,
not an accepted repository status; **ARGUED**, **GUIDE**, and **OPEN** keep
their weaker meanings. No numerical output discharges a statement.
The requested `prior/gap-pag-corner-astra.md` is absent.
The lead's `prior/repo-search-2026-11-08.md` records no supplier for this
later target. Its closest specific hit is
`pr/10114:.claude/science/toe-ruleset-20261021/agents/ym4d-proof/MASS_GAP_LOCAL_BLOCK_ASTRA.md:106–149`:
a positive one-time-step plaquette correlation in the transfer ground-state
law. I read lines 92–164 at the fetched PR head. Its bound (11) is positive
but neither a conditional corner correlation nor a bound above 1/160.
Credit that earlier Codex/Astra note for the transfer-kernel comparison;
it is not used as a corner estimate.

**ARGUED / source record.** The exact immediate predecessors are
`gap-crux-exercise-astra.md:749–984,1194–1354` (Codex/Astra: cover,
two-projection criterion, full-space gauge obstruction, invariant repair),
`gap-gc-check-opus.md`, especially section 9 (Claude Opus: the two invariant
plaquettes and their open correlation), and `prior/gap-lit-block.md`
(Codex: existing literature search). These are credited inputs, not new
results here. Searches of `open-registry.md`, `open-core.md` and `l17c.md`
for PA_g, this lane, projection angles and block corners found no competing
owner. The source statement itself remains OPEN.

**ARGUED / source record.** Main was fetched at
`a527a6fdaeb22ef8a0d1224cc2ba7bc42c48d3bc`; its workflow now points to
`RULES.md`, `SETTINGS.md`, and `procedures/research.md`, which were read.
The checkout remains based on the requested pin. No science status is
imported from planning. The four requested PR heads were fetched for the
target search. Broad substring matches are not evidence of coverage.
The completed search for the delimited name PA_g and for
`gauge.invariant.{0,25}projection.angle` found no outside-lane match on
any of the five refs. Full search log:
`/tmp/gap-pag-corner-astra.30EUl1/repo-search.log`.

**ARGUED / other close hits checked.** Main's
`docs/MASSIVE_WILSON_LOOP_CURVATURE_NONCOMPACT_COVARIANCE_AND_COMPACT_DEFECT_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-14.md:120–145`
is a noncompact determinant-weighted Maxwell covariance comparison, not
the compact Wilson conditional law. The two main notes
`docs/PLAQUETTE_CORNER_SYMBOL_PAIR_COVARIANCE_ONLY_ZERO_BOUNDED_THEOREM_NOTE_2026-10-10.md`
and `docs/PLAQUETTE_CORNER_WEIGHT_COVARIANCE_ONLY_ZERO_BOUNDED_THEOREM_NOTE_2026-10-10.md` (headers and carrier
definitions, lines 1–66 and 1–64) concern transformation covariance of
integer corner weights, not statistical covariance. Finally,
`gap-means-astra.md:338–371` already gives perfect anticorrelation of two
plaquette traces under a one-link conditional law. They depend on the
same free link, so they cannot belong to the two exclusive algebras here;
that counterexample is not a PA_g obstruction. Credit the earlier Codex
note and do not redo its association argument.

## Contract and checkpoint

**OPEN.** Decide the invariant pair angle of the actual conditional 4D
Wilson SU(2) measure, with the exterior fixed, for the product-box covers
of section 8.1. In particular, test the two corner plaquette traces in
the review's section 9. The threshold is 1/160, with the torus and cutoff
quantifiers retained. A calculation in a quadratic model alone does not
decide this contract.

**ARGUED / scope.** Write
`S=B union C`, `X=B\C`, `Y=C\B`, `O=B intersect C`.
In a fibre at exterior tau, `ran E_C` consists of functions of X and
`ran E_B` of functions of Y. On the subspace invariant under interior
vertex gauges, the norm in PA_g is the maximal normalized covariance of
admissible functions of X and Y. A single correlation supplies a lower
bound, never an upper bound on this norm. Thus a trace correlation below
1/160 would leave PA_g open.

**PROVED / current checkpoint.** Sections 1–3 give a different pair of
fully invariant boundary plaquettes in every cover of 8.1. Their quadratic
correlation is at least 1/49, and their actual Wilson correlation is above
1/64 for all sufficiently large beta at each fixed block size, uniformly
in the torus. **OPEN:** a threshold uniform in growing blocks and any
prescribed order-one beta. Section 4 records the attempted extensions;
the next load-bearing decision is its explicit uniform moment estimate,
not another computation of the free covariance.

## 1. The additional face corner

**PROVED (hand argument; author only).** Every cover in 8.1 has the
following pair. This uses the same opposite-sign neighbouring boxes B,C
as GC1. Choose coordinates so that their overlap's lower endpoints in
coordinates 1 and 2 are zero, with

    v=(0,0,a3,t),  z=v-e1,  w=v-e2,  u=v-e1-e2.

Here `a3` is the lower endpoint of their identical third interval and t
is at least one step inside their identical fourth interval. The overlaps
in coordinates 1,2 contain at least two sites. Consequently v is in both
boxes, z only in B, w only in C, and u in neither. Links are assigned by
their positive base, exactly as in 8.1. Put

    U=(z,1),   V=(w,2),   e0=(v-e3,3).

Every link incident to v except e0 lies in S. In particular, v is a
boundary vertex of S: the invariant restriction in PA_g does not rotate
v. Both endpoints of U and V are boundary vertices, because each has an
incoming exterior link in direction 3.

There are three elementary plaquettes:

* p in the (1,2) plane based at u: its only free links are U,V;
* p_U in the (1,3) plane based at z-e3: its only free link is U;
* p_V in the (2,3) plane based at w-e3: its only free link is V.

The other links of p_U,p_V have bases with third coordinate a3-1 and
are exterior. The other two links of p have base u and are exterior.
At the identity exterior, their traces are respectively
`x(U V^-1), x(U), x(V)`, up to inversion or cyclic order, which do not
change an SU(2) trace. Write `x(M)=tr(M)/2`.

Thus `x(p_U)` lies in `ran E_C`, `x(p_V)` in `ran E_B`; both are fully
gauge-invariant plaquette traces, not merely invariant under interior
gauges. Their fibre covariance is an admissible lower test of PA_g.
This moves the review's proposed test to the common outer face; it does
not claim an estimate for its original interior-transverse pair.

**ARGUED / scope of the class.** The argument applies to nonwrapping
product-box covers with positive links assigned by base, containing an
opposite-sign neighbouring pair with identical third intervals, the above
two-site overlaps, and identical fourth intervals with an interior site.
Every cover of 8.1 satisfies these conditions. Other link assignments,
rounded or staggered covers without this geometry, and certificates using
larger groups of blocks are outside this obstruction test.

## 2. A uniform quadratic-model lower bound

**PROVED (hand argument; quadratic model only).** Extend real one-cochains
on S by zero on exterior links. Let C be the ordinary lattice curl on
all plaquettes touching S. Give the quotient by `ker C` the centered
Gaussian law with action `||C A||^2/2`. Its curvature covariance is the
orthogonal projection `P_S` onto `ran C`. This follows directly by
diagonalizing `C*C` on its kernel complement: each nonzero singular
direction of C has curvature variance one.

This is the same exact-cochain covariance construction used by Ethan
Sussman and Levent Alpoge, with Claude and Codex as authors of their text,
SA 1670–1687 (indexed at chunk-02, neighbouring rows 1673–1712). Their
periodic free comparison is not an interacting Wilson theorem. The
restriction to this patch and the estimate below are the present argument.

Let `X=A_U`, `Y=A_V`. These are functions on the quotient: each is, up to
sign, the curl on p_U or p_V. Let

    a=Var X, b=Var Y, c=Cov(X,Y),
    s=Var(X+Y)=a+b+2c,  t=Var(X-Y)=a+b-2c.

**PROVED, upper estimate.** One has `t<=1/2`. Indeed, `X-Y` is, up to
sign, the curvature at p. Embed the nonwrapping patch in a larger cubic
N-torus. Its exact-cochain space is a subspace of the full periodic
exact-cochain space; hence `P_S<=P_full` as quadratic forms. The latter
projection has rank `3(N^4-1)`: at each nonzero Fourier frequency the curl
map is wedge product by a nonzero difference vector, with kernel its
one-dimensional span and rank three; at zero frequency its rank is zero.
There are `6N^4` plaquettes. Translations and coordinate permutations make
all its diagonal entries equal. Thus

    t=P_S(p,p) <= P_full(p,p)
      = (1/2)(1-N^-4) <= 1/2.                    (1)

The auxiliary torus is only a finite-dimensional comparison space, not a
change of the patch's probability law. No infinite-volume limit or machine
count is needed. The wedge-product rank follows by taking a basis whose
first vector is the difference vector: the other three basis vectors have
independent wedges with it.

**PROVED, lower estimate.** One has `s>=2/3`. On the full lattice take
the gradient of the vertex indicator `1_v` and restrict it to S; call the
result h. With the gradient oriented as target minus source,
`h_U=h_V=1`. Its only omitted nonzero edge is e0. Since the full gradient
has zero curl,

    C h = -d_1 1_e0,    ||C h||^2=6.

Exactly two plaquettes in each of the other three directions meet e0;
their coefficients are +1 or -1. All six are touching plaquettes of S.
For a linear functional l annihilating `ker C`, the Gaussian variational
identity is

    Var(l A) = sup_{h: C h != 0} (l h)^2 / ||C h||^2.

To verify it, represent l on `(ker C)^perp`, apply Cauchy–Schwarz in the
`C*C` inner product, and take h proportional to `(C*C)^-1 l`. Apply it
with `l A=X+Y` and the displayed h to get

    s >= 2^2/6 = 2/3.                             (2)

The test h is not an allowed interior gauge zero mode: its omitted link
e0 is fixed by the exterior. Its nonzero energy is exactly why it detects
physical boundary plaquettes after the GC4 restriction.

**PROVED, normalized correlation.** Equations (1),(2) give c>0. Since
`2 sqrt(ab)<=a+b`,

    Corr(X,Y) = (s-t)/(4 sqrt(ab))
              >= (s-t)/(s+t) >= 1/7.              (3)

There is no zero-variance issue: (2), positivity of the covariance matrix,
and `s>t` force a,b>0. This bound is uniform in the patch sizes and in
the ambient torus, throughout the class of section 1.

Take three independent colour copies and let
`Q_U=sum_{j=1}^3 X_j^2`, `Q_V=sum_{j=1}^3 Y_j^2`. For one centered
Gaussian pair, write `Y=(c/a)X+Z` with Z independent of X to obtain
`Cov(X^2,Y^2)=2c^2`, `Var(X^2)=2a^2`. The independent colours then give

    Corr(Q_U,Q_V) = c^2/(ab) >= 1/49 > 1/160.      (4)

This is a hand proof in the quadratic model, including its boundary
conditions. It is not a numerical enclosure and not yet a Wilson bound.

**ARGUED / source limits.** The SA-index obligations at 778–779 and the
source lines 766–779 distinguish the scalar block gap from a physical
Hamiltonian gap. SA 1382–1386 explicitly leaves the interacting comparison
separate. In CA-I, the indexed lines 46064–46075 concern a quadratic
conditional fluctuation integral; 49495–49516 leave application conditions
outside the operator theorem. Those passages were read from the requested
downloads. None supplies the nonlinear passage required below. Credit
Sussman and Alpoge, with Claude and Codex as authors, for those constructions
and scope distinctions. No claim about all 166,711 CA-I lines is made.

## 3. What follows for actual Wilson SU(2)

**PROVED (fixed patch, hand argument; author only).** For a fixed pair in
section 1, take the exterior configuration identically I. Let
`mu_(beta,S)^I` have density proportional to

    exp[-beta sum_{p touching S} (1-x(U_p))]

relative to product Haar on S. Then

    lim_{beta -> infinity}
      Corr_{mu_(beta,S)^I}(x(p_U),x(p_V))
       = c^2/(ab) >= 1/49.                          (5)

Here a,b,c are precisely the single-colour covariances in section 2.
In particular there is a finite `beta_0(S)` such that for all
`beta>=beta_0(S)` the actual invariant pair angle is greater than `1/64`,
and hence exceeds `1/160`.

This statement is about the compact Wilson measure, with no truncation
of its support. The following supplies the finite-dimensional passage;
it does not assert a uniform error in the number of links.

### 3.1 All minima and their gauge quotient

**PROVED.** The action is nonnegative and has minimum zero at the identity.
At any zero, every touching plaquette is I, since an SU(2) matrix of
normalized trace one is I. All other plaquettes are I by the exterior
condition. The resulting field is flat on the full torus.

A flat field on the torus is determined, up to vertex gauges, by its
coordinate-cycle holonomies. This follows by exchanging neighbouring
coordinate steps across a flat plaquette, cancelling reversals, and
reducing a lattice path to its winding numbers. For each coordinate
direction there is a representative cycle wholly outside the bounding
rectangle of S: fix a different coordinate outside that rectangle.
These holonomies are I. Therefore the field is a pure vertex gauge.

The graph made of exterior links has one component containing every
vertex outside the base-site union D and every vertex incident to an
exterior link. For this pair the common third and fourth intervals factor
out of D. If a site fails membership in the two-dimensional union of
the first-two-coordinate rectangles, it can move in coordinate 3 to the
outside of the bounding rectangle without entering D. If it fails a
common third or fourth interval, it can keep that failed coordinate
fixed while moving to the exterior shell. The shell is connected.
Every boundary vertex in D is attached to an outside site by an incoming
exterior link. This proves the stated exterior-graph connectivity.

Consequently all boundary vertex gauges have one common value, which a
global constant gauge removes. The zero-action fields are exactly the
orbit of the identity under gauges at interior vertices (vertices with
all incident links in S). There are no additional flat holonomy modes.

Choose a forest of free links connecting every interior vertex to the
boundary, with one rooted tree per component as needed. Such a forest
exists: a finite connected component of interior vertices has a first
edge on a path to a vertex outside it, and that edge is free. Fix these
forest links to I by interior gauge transformations, starting from their
boundary roots. Haar invariance gives an exact product change of variables
between forest gauge coordinates and the remaining link variables. Its
integral over gauge coordinates is one. No field-dependent determinant
is omitted. In this slice the identity is the unique action minimum.
The links U,V have boundary endpoints and cannot be forest edges, so their
matrices are unchanged by this gauge fixing.

The Hessian at the identity is positive definite in the slice. A null
vector has zero linear curl; the same path-exchange argument makes it a
gradient with zero boundary values, and its forest-edge values then force
the gradient to vanish. This also identifies the Gaussian in the slice
with the quotient Gaussian of section 2 on U,V. Gauge fixing changes its
coordinates, not the covariances of these two quotient functionals.

### 3.2 The finite-dimensional integral, including moments

**PROVED.** On each remaining link write
`U_e=exp(i A_e dot sigma)` near I, using Pauli matrices, so
`x(U_e)=cos |A_e|`. In these coordinates, with M the number of remaining
real coordinates,

    S(A) = (1/2)||C A||^2 + O_S(|A|^3),
    dHaar = J(A) dA,   J(0)>0.

There are three independent colour copies of the scalar quadratic form.
The subscript S on the remainder is intentional. Positive definiteness
gives numbers `epsilon_S,k_S>0` such that
`S(A)>=k_S |A|^2` for `|A|<epsilon_S`. On the compact complement of this
neighbourhood, uniqueness of the minimum gives `S>=m_S>0`.

Change variables `Y=sqrt(beta) A` in the neighbourhood. Pointwise, its
rescaled density tends to
`J(0) exp[-||C Y||^2/2]`. The quadratic lower bound dominates every fixed
polynomial moment by a Gaussian integrable function. Restricting Y to a
fixed ball also shows `Z_beta>=c_S beta^(-M/2)` for large beta. Outside
the neighbourhood, every bounded observable times any fixed power of
beta has normalized contribution at most
`C_S beta^(M/2+k) exp(-beta m_S)`, which tends to zero. These facts prove
convergence of the rescaled moments, not just weak convergence.

For the two plaquettes with one free link,

    beta(1-x(p_U)) -> |X|^2/2,
    beta(1-x(p_V)) -> |Y|^2/2,

with convergence of their first, second and joint second moments.
Within the coordinate neighbourhood this also follows from
`0<=beta(1-cos |A_U|)<=|sqrt(beta) A_U|^2/2`; outside it the preceding
exponential tail estimate applies. Thus

    beta^2 Var(x(p_U)) -> (3/2)a^2 > 0,
    beta^2 Var(x(p_V)) -> (3/2)b^2 > 0,
    beta^2 Cov(x(p_U),x(p_V)) -> (3/2)c^2.

Taking the ratio proves (5). Since `1/49>1/64>1/160`, its definition of
convergence supplies the stated finite `beta_0(S)` by an existence
argument, without numerical evaluation of a partition function.

**PROVED, positive-measure exteriors.** This also refutes an
essential-supremum pair bound for this fixed patch and these beta, not
only a pointwise bound at an exceptional exterior. At finite beta all
these expectations are integrals of continuous bounded functions on a
compact group product with a strictly positive partition function. They
depend continuously on the finitely many exterior links entering the
touching plaquettes. The variances at the identity exterior are positive.
Choose beta_0(S) with the strict margin above 1/64, as (5) permits.
Thus the correlation remains above 1/64 on a neighbourhood of that
exterior. Product Haar, and every finite-volume Wilson exterior marginal,
give that neighbourhood positive measure.

### 3.3 The torus quantifier that is actually obtained

**PROVED.** For every fixed integer `ell>=12`, there is a finite
`beta_0(ell)` such that every cover of 8.1 on every admitted sufficiently
large torus has an interacting pair and an open set of exteriors on which

    ||E_B^tau E_C^tau-E_S^tau||_(invariant) >= 1/64,
    beta >= beta_0(ell).                              (6)

For fixed ell, all interval lengths and endpoint offsets come from finite
integer sets bounded in terms of ell. Up to translation and coordinate
permutation there are finitely many possible union-patch shapes. Their
touching-plaquette actions at identity exterior are independent of the
surrounding torus once embedded without wrap identifications. Take the
maximum of the finitely many thresholds in (5). This proves (6) uniformly
in the torus and in all the interval choices at this fixed ell.

**OPEN, distinct quantifier.** Equation (6) does not prove

    exists beta_*  for all ell>=12  for all beta>=beta_*: (6),

and does not prove (6) along `ell_h=ceil(R/h)`, `beta=beta_h` for a
prescribed cutoff trajectory. It also does not decide beta=1, beta=2 or
an order-one interval. No bound on `beta_0(ell)` is established here.
Calling beta_0(ell) a fixed constant after fixing ell does not answer the
order-one-coupling question.

## 4. Attempts at the missing uniform and order-one bounds

### 4.1 Uniform large-beta passage: exact missing estimate

**PROVED (quadratic model).** The individual variances also satisfy
`1/6<=a,b<=1/2`. For the lower bounds use the same h as in (2), now
with the individual functional X or Y. For the upper bounds use the
projection comparison (1) at p_U,p_V. Consequently their quadratic
trace variances `V_U=3a^2/2`, `V_V=3b^2/2` lie between `1/24` and `3/8`.

**OPEN, a sufficient nonlinear estimate.** Uniformly over the section 1
patches, suppose that for all beta beyond one block-independent number,
each of

    |beta^2 Var_W(x(p_U)) - V_U|,
    |beta^2 Var_W(x(p_V)) - V_V|,
    |beta^2 Cov_W(x(p_U),x(p_V)) - 3c^2/2|

is at most `1/10000`, at the identity exterior. The hand calculation then
gives, writing `D=sqrt(V_U V_V)>=1/24`,

    Corr_W >= (1/49-24/10000)/(1+24/10000)
            = 1103/61397 > 1/64.                    (7)

The last comparison is the integer inequality `70592>61397`.
Thus this particular normalized second/fourth-moment estimate, rather
than a full operator-norm approximation, would be sufficient to close
the weak-coupling obstruction for growing blocks. Equation (7) is a
proved implication; its displayed nonlinear premise is OPEN.

**ARGUED, attempted supply and failure.** The proof in 3.2 does not
give this estimate. Its dimension M, local radius, smallest quadratic
eigenvalue, action gap m_S outside a coordinate neighbourhood, and tail
normalizer all depend on S. Letting M grow inside that proof changes its
dominating function and its tail estimate. No interchange of those limits
has been justified. In particular, convergence of a local law without
control of the rescaled fourth moments does not control a covariance of
size beta^-2. The account's quadratic-fibre theorem is on a different
law, as its passages cited in section 2 specify.

GC2's already available volume-uniform mean-energy bound is also
insufficient for this supply. It controls first moments averaged over
the periodic law, not these conditional centred fourth moments at an
identity exterior. It neither gives a relative variance error nor an
every-boundary estimate. I do not repeat its proof or use it to replace
one of the displayed premises.

### 4.2 Order-one coupling: an exact local reduction, no small remainder

**PROVED (actual Wilson identity).** Keep the identity exterior and
integrate out every free link except U,V. Each link meets six plaquettes.
They share exactly p. Three of the resulting eleven plaquettes give
`x(U)`, `x(V)` and `x(U V^-1)`. The other eight contain U or V and at
least one further free link. The two-link marginal therefore has density

    Z_2^-1 exp{beta[x(U)+x(V)+x(U V^-1)]} R_beta(U,V),
    R_beta(U,V)=E_nu exp[beta T(U,V,Z)],
    |T|<=8,  exp(-8 beta)<=R_beta<=exp(8 beta).       (8)

Here nu is the normalized Haar/Wilson measure using precisely the
plaquettes independent of U,V, and Z denotes its remaining links.
The bound is independent of torus and block size. This is the local
version of the existing density-comparison method in 8.1/A5, not a new
general comparison principle.

**ARGUED, failed supplier.** The oscillation estimate in (8) does not
decide the correlation at beta=1 or any prescribed order-one value.
For example the artificial factor
`R_beta(U,V)=exp[-beta x(U V^-1)]` obeys its displayed bounds but makes
the two-link density a product, with zero correlation. This is a
counterexample to an inference from the bounds on R alone, not the actual
Wilson factor and not a counterexample to PA_g's failure. Dropping R from
the integral would change the model. A correlation monotonicity argument
for retaining the other plaquettes has not been proved here.

**PROVED (actual Wilson derivative, fixed patch).** At beta=0 the links
are independent Haar, `E x(U)=0`, `E x(U)^2=1/4`. Differentiation of the
finite compact integral gives

    d/dbeta Cov_beta(x(U),x(V)) at 0 = 1/16,
    d/dbeta Corr_beta(x(U),x(V)) at 0 = 1/4.         (9)

Only p contributes to the first derivative. Every other plaquette either
misses one of U,V, leaving its centered Haar integral zero, or contains
a remaining link occurring once, whose Haar integral is zero. For p,
matrix-coefficient orthogonality gives
`integral x(V) x(U V^-1) dV=x(U)/4`, and the remaining integral is 1/16.
The derivative of the product of the means vanishes at zero. Finite-volume
analyticity and nonzero variance at zero therefore yield
`Corr_beta=beta/4+O_S(beta^2)`.

**GUIDE / OPEN.** The linear term reaches 1/160 at beta=1/40. No bound on
the remainder at that value or at beta=1 follows from (9), and no such
crossing is claimed. A source asserting general non-Abelian monotonicity
cannot be inserted here: the existing `prior/gap-lit-assoc.md` and
`prior/gap-lit-ineq.md` searches leave the needed Wilson inequality
unsupplied. This note does not take over their separately owned
association problem.

### 4.3 The regime already below the threshold

**PROVED, using existing A5 rather than reproving it.** At beta=0 all
pair angles vanish. For a pair patch with n touching plaquettes, 8.1/A5
and the two-projection relation give the sufficient bound

    ||E_B E_C-E_S|| <= 1-exp(-2 beta n).

It applies also on the invariant subspace and for every exterior. Thus
`beta <= log(160/159)/(2 n_max)` suffices for PA_g on a fixed cover, where
`n_max` is the largest touching-plaquette count among its pairs. Covers
with bounded ell have n_max bounded independently of torus size. This
coupling window shrinks as ell grows; it supplies neither an order-one
physical-scale certificate nor a cutoff-trajectory answer. It is an
existing sufficient bound, not a newly determined transition point.

## 5. Guide calculation and source recovery

**GUIDE, not proof or verification.** A small sparse Gaussian calculation
informed the choice of the face test. Take

    B=[-L,L] x [0,2L] x [-L,L]^2,
    C=[0,2L] x [-L,L] x [-L,L]^2,

assign links by base, fix exterior cochains to zero, and invert
`C*C + D_int D_int*`, where D_int consists of gradients at vertices
whose entire star is free. The selected link functionals annihilate
those gradients. The original review test uses transverse links at
`v=(0,0,0,0)`; the face test uses the two incoming links at
`v=(0,0,-L,0)`. Squaring the computed single-colour correlation gives
the quadratic trace correlation.

| L | Free links | Review's interior-transverse test, GUIDE | Face test, GUIDE |
|---|---:|---:|---:|
| 1 | 504 | 0.003495 | 0.215885 |
| 2 | 4100 | 0.012613 | 0.212202 |
| 3 | 16072 | 0.013447 | 0.212405 |

These small boxes are not the ell>=12 covers of 8.1. Their results neither
bound that class nor decide Wilson correlations. They show why neither
the smallest toy box nor a computation without its boundary geometry is
a decisive test. The actual hand bound (4) uses none of these entries.

The script and complete log are
`/tmp/gap-pag-corner-astra.30EUl1/free_guide.py` and
`/tmp/gap-pag-corner-astra.30EUl1/free_guide.log`. Python ran with `-I`;
the process had a resident-memory guard at 1.5 GiB and reported peak use
below 82 MB. No Wilson Monte Carlo, interval certificate, exhaustive
search, Lean check or independent proof review was performed.

**ARGUED / recovery metadata.** The requested source downloads were made
once each at revision `31a47c543775`, outside the checkout:

* `/tmp/sa_ym4.tex`: 32,992 lines, SHA-256
  `d7f77d4da3eb23038250c52468a341281d9ba86b4af21d3371d208a2537d4b6f`;
* `/tmp/sa_ca_I.tex`: 166,711 lines, SHA-256
  `4cb5cb5e0af8dbddbee207926621300350e018c6cf1d6567a753167ce10e6e93`.

Only the indexed excerpts cited above were read. PR heads used in the
completed repository search were 10114 `f76f6c649c`, 10133 `89faef229f`,
10134 `1e70c7211a`, and 10141 `fb99b4dddc`; the full hashes are in the
search log. No shared registry, FINISH row, status, audit record, or source
proof was edited. This output is the sole repository file written.

## 6. Disposition and next obligation

**PROVED, bounded obstruction.** At every fixed lattice block size of
the stated product-box class, PA_g fails at sufficiently weak coupling,
uniformly in the torus, for fully gauge-invariant plaquettes. Merely
removing the open-link gauge functions of GC1 does not make this fixed-size
criterion valid. An alternative cover that avoids this test must change
the face-corner geometry or the block/link assignment; avoiding it alone
would not prove PA_g.

**OPEN, the requested decisive scope.** This note does not close PA_g
along a prescribed growing-block cutoff trajectory or decide it at
order-one beta. The original review's interior-transverse plaquette pair
has only GUIDE values here; the proved obstruction uses the additional
face pair. No general physical mass-gap route is refuted, and no mass
gap or new scientific status follows.

**OPEN / handoff.** Check the hand argument (1)–(6), then attack the
uniform rescaled-moment estimate preceding (7), or a direct finite-beta
estimate for the actual factor R in (8). Do not repeat the free-model
calculation or treat the fixed-patch Laplace limit as uniform in ell.
The order-one target needs that nonlinear input, not another use of the
already checked implication GC4. The present result is our own restricted
obstruction, not a correction of Sussman–Alpoge's text.

RESULT: PROVED by hand, not independently checked: every fixed-size cover of the stated product-box class has fully gauge-invariant face-corner plaquettes with quadratic correlation at least 1/49 and actual Wilson pair angle above 1/64 for beta>=beta_0(ell), uniformly in the torus; OPEN: a block-size-uniform threshold, the prescribed cutoff trajectory, and order-one beta, so the full requested PA_g decision is not obtained.
