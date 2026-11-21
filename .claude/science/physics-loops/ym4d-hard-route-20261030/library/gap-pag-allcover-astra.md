# Repo search

**ARGUED / provenance.** FINISH row 777. Author: Codex gpt-6-astra max,
2026-11-12. Source checkout `8adccdfdd33131ac3f44e2201f803b40911bbf2b`.
Research text, not an audit; no scientific status is granted.
PROVED below means a written hand proof by this author, awaiting a separate
check. ARGUED, GUIDE and OPEN retain their ordinary weaker meanings.

**ARGUED / prior record.** `prior/gap-pag-allcover-astra.md` is absent.
The lead's `prior/repo-search-2026-11-08.md` concerns earlier RG targets.
Its closest hit is the transfer-kernel plaquette correlation in
`pr/10114:.claude/science/toe-ruleset-20261021/agents/ym4d-proof/MASS_GAP_LOCAL_BLOCK_ASTRA.md:106–149`.
That is a different conditional law. The current task names no additional
"Repo prior work" hit. Current main was fetched at
`a527a6fdaeb22ef8a0d1224cc2ba7bc42c48d3bc`; its workflow, rules,
settings and research procedure were read. The planning branch supplies
no science. Targeted searches of `open-registry.md`, `open-core.md` and
`l17c.md` found no other owner of this corner-angle extension.

**PROVED / imported, with the existing check.**
`gap-pag-grow-astra.md`, checked in `gap-pag-grow-check-opus.md` by
Claude Opus 5.5, supplies the symmetric-pair bound and Lemma V.
The check corrects "fixed twelve functions": their regularization depends
on beta, though not on block size. The face geometry is from
`gap-pag-corner-astra.md` sections 1–3. The cover and PA_g are from
`gap-crux-exercise-astra.md` sections 8.1 and 8.4. Those results are
credited to their earlier Codex/Astra authors and are not new here.

## Contract and checkpoint

**ARGUED / target.** Extend the obstruction to unequal-interval covers
without assuming a reflection exchanging their blocks. Keep the exact
Wilson law, the interior-gauge invariant space, and the exterior quantifier.
The new method uses a gauge rotation on the *exclusive* links at a boundary
vertex. This is a differentiation variable, not a symmetry of the conditional
Wilson law: its ten changed plaquette factors are retained.

**PROVED / result below, author only.** For every section-8.1
cover, including those with no symmetric pair, a pair has invariant angle
at least

\[
 c(\beta)=\frac{2\beta}{(4+6\beta)\sqrt{9+30\beta}}.
\]

In particular the angle exceeds `1/160` for `1/16 <= beta <= 64`,
independently of all block sizes. At beta = 1 it exceeds `1/35`.
The proof uses a marginal integration-by-parts operator and the transverse
conditional variance already calculated in Lemma V.

**OPEN / retained limit.** The displayed bound tends to zero as beta
tends to infinity. It does not settle arbitrarily large beta for asymmetric
covers. The theorem decides every cover in the stated class on the
displayed interval; its coupling range must not be silently enlarged.

## 1. Source comparison and exact new claim

**ARGUED / sources checked.** The PR #10114 hit above was fetched at
`f76f6c649cff7dffbab664d8976e680e8f287fe9` and read at lines 92–164.
It proves a positive one-step transfer correlation using a convolution
kernel and local density comparison. Neither its probability law nor its
operator is the conditional block pair here. Main's targeted searches for
`PA_g`, projection/corner angles, boundary stars and marginal Fisher
information found only unrelated geometry, code-star and Wilson–Fisher
usages. These are bounded searches, not an absence theorem. The lead's
five-ref search remains credited for the earlier PR inventory. A targeted
search of this lane for the new score/star argument found only unrelated
boundary-action derivatives and integration-by-parts passages, not another
owner or proof of (6)–(12).

**ARGUED / outline comparison.** Both requested sources were fetched
once at `31a47c543775`. The SA-index README, chunk-01 rows 653–790,
chunk-03 rows 2760–2883, and their obligation/cross-reference neighbours
were consulted before reading SA 766–779 and 2773–2883. The scalar block
gap is proved there for its stated operator. AM2 and AM5 prove the
reflection Gram construction used by the predecessor. They do not remove
its reflection hypothesis. In the CA 4.12–4.19 index, the neighbouring
rows for 46064–46075 and 49495–49516 led to those source ranges.
They concern a quadratic conditional fluctuation integral and explicitly
separate its application conditions. These passages supply no full Wilson
block-angle estimate. No claim about the unread remainder of CA-I is made.

**ARGUED / credit.** Credit Ethan Sussman and Levent Alpoge, with Claude
and Codex as authors of their text, for the quaternion/reflection
construction and the stated scope distinctions. Credit Tadeusz Balaban
for the fluctuation construction named in their account. No Balaban
estimate is imported here. The new proof replaces the predecessor's use
of reflection positivity with marginal integration by parts. Its one-link
input is the existing, checked Lemma V, not a new derivation of that lemma.

**PROVED / theorem A, precise scope.** Let beta be positive and finite.
Use any nonwrapping product-box cover of section 8.1, with arbitrary
allowed interval lengths and scale `ell >= 12`. Assign positive links
by their base. On every admitted torus there is an interacting pair B,C
such that, at identity exterior,

\[
 k_g(B,C)\ \ge\ c(\beta)
 =\frac{\beta}{(2+3\beta)\sqrt{9+30\beta}}.                 \tag{1}
\]

The essential supremum over exterior configurations has the same lower
bound. In particular both versions of PA_g fail throughout

\[
                    1/16\le\beta\le64.                     \tag{2}
\]

At beta = 1, `k_g > 1/35 > 1/160`. No interval equality, reflection
symmetry, upper volume bound, or upper block-size bound enters (1). Section 6 extends
the geometry and states exactly which changes remain undecided.

## 2. The exclusive boundary star

**PROVED / geometric lemma.** Use the predecessor's face corner and
write

\[
 v=(0,0,a_3,t),\quad z=v-e_1,\quad w=v-e_2,\quad o=v-e_1-e_2,
 \qquad U=(z,1),\quad V=(w,2).
\]

The first two lower overlap endpoints are zero; `a_3` is the common
third interval's lower endpoint. The fourth coordinate is an interior
site. Put `X=B\setminus C`, `Y=C\setminus B`, `Z=B\cap C` for the
three free link sets. These letters also denote their configurations.

The already established face geometry gives `U in X`, `V in Y`, and
the plaquette p based at o has precisely U,V free. At identity exterior
its trace is `u dot v'`, where `u=s(U)` and `v'=s(V)` are unit
quaternions. Below the prime distinguishes the quaternion from the site v.
All endpoints of U,V are boundary vertices of the union S.

The new geometric fact is this: **all free links incident to z lie in X**.
Exactly two incident links are exterior: the incoming links in directions
2 and 3. The remaining six are X links. Thus a vertex gauge transformation
at z, applied only to those six links, acts on X alone. It sends U to kU
and leaves Y,Z fixed.

Here is the complete plaquette check. A plaquette at z is unchanged if
both its incident links there are free, by cancellation of the vertex
gauge. It is unchanged if both are exterior. Each of the two exterior
incident links belongs to six plaquettes. Their unique common plaquette
has both links exterior. Exactly `6+6-2=10` plaquettes therefore change.
Of these ten, only p reads Y or Z; it reads V and no Z link.

For the incoming direction-2 link, the transverse choices are `+1,-1`,
`+3,-3`, and `+4,-4`. The `+1` choice is p. The `-3` choice has both
incident links exterior. In every remaining choice, all free bases have
first coordinate -1 or -2, so are B-only; the other bases have second
coordinate -1 and first coordinate negative, so are exterior. For the
incoming direction-3 link the `-2` choice is the same excluded plaquette.
For its other five choices, the opposite layer has third coordinate
`a_3-1` and is exterior. The free edge at height `a_3` is B-only,
including U in the `+1` choice. This accounts for all ten.

No hidden endpoint assumption is needed. For adjacent intervals of
lengths `s_i`, set `q_i=floor(2s_i/3)`. The distance between successive
lower endpoints is `s_i+q_(i-1)-q_i >= ell-1`; the overlap extends
`2q_i-s_i >= ell/3-2 >= 2` beyond its lower endpoint. Thus the sites
at offsets -2 and +1 used above are available. The common third and
fourth intervals contain the required one-step neighbours.

Let `D_1,D_2,D_3` be the derivatives of this X-only gauge action, with
generators `i sigma_i`. They are skew-adjoint for product Haar on X.
On U they form the unit left-invariant frame of the unit three-sphere.
Consequently, with `Delta=sum_i D_i^2`,

\[
 \Delta u=-3u,\qquad
 \sum_i(D_i u)(D_i u)^T=P_u:=I_4-uu^T,\qquad
 u\cdot D_i u=0.                                           \tag{3}
\]

The vectors `D_i u` are an orthonormal tangent frame: multiplication by
a unit quaternion preserves the Euclidean norm, and `i sigma_i` are
orthonormal at the identity. Differentiating twice along each subgroup
gives `D_i^2 u=-u`, proving the first identity and its normalization.

**PROVED / action identity.** Write rho for the full conditional Wilson
density on X,Y,Z, relative to product Haar. There is a smooth real
function F(X), the sum of beta times the other nine changing plaquette
traces, such that

\[
 D_i\log\rho=D_iF+\beta(D_i u)\cdot v'.                    \tag{4}
\]

Every unlisted plaquette is invariant under this action. The action is
not a symmetry of rho. Equation (4) retains exactly its failure to be
a symmetry. For each of the ten changing plaquette traces `x_q`,
`Delta x_q=-3x_q`: the transformed plaquette has exactly one factor k
or its inverse, and its normalized trace is a linear quaternion function.

## 3. Marginal integration by parts

**PROVED / lemma B.** Let `m_X` be the marginal density on X, and set

\[
 a(X)=\mathbb E[v'\mid X],\qquad
 s_i(X)=D_i\log m_X=D_iF+\beta(D_i u)\cdot a(X),
 \qquad
 T_j(X)=\Delta u_j+\sum_i s_i D_i u_j\quad(0\le j\le3).
                                                               \tag{5}
\]

All functions are smooth and bounded at each finite beta and finite
patch. Their definitions use exact compact integrals, not computed
approximations. The joint density is smooth and strictly positive.
Differentiation under the finite compact integral gives the middle
identity in (5) from (4).

For a smooth function f on X, define
`L_X f = Delta f + sum_i s_i D_i f`. Product-Haar integration by
parts gives

\[
 \int L_X f\,m_X\,dX=0.
\]

Thus every T_j has mean zero. Integrating by parts instead in the full
joint law, and using that `D_i v'_j=0`, gives

\[
 \begin{split}
 \mathbb E[T_jv'_j]
 &=-\beta\,\mathbb E\sum_{i,k}
       (D_i u_j)(D_i u_k)(v'_k-a_k(X))v'_j,\\
 -\sum_{j=0}^3\mathbb E[T_jv'_j]
 &=\beta\,\mathbb E\operatorname{tr}
       \big(P_u\operatorname{Cov}(v'\mid X)\big).
 \end{split}                                                   \tag{6}
\]

For the first line, the joint divergence
`Delta u_j + sum_i (D_i log rho)D_i u_j` has zero integral against
`v'_j`. Subtract its score from the marginal score in (5). Conditioning
on X then turns `(v'-a)v'^T` into the conditional covariance, proving
the second line. No assumption on the sign of a two-link kernel is used.

**PROVED / lemma C, size-free norm.** The same four witnesses obey

\[
                   \sum_j\mathbb E T_j^2\le9+30\beta.       \tag{7}
\]

Let `H_i=D_i log rho`. Since `s_i=E[H_i|X]`, conditional
Cauchy–Schwarz bounds `E sum_i s_i^2` by `E sum_i H_i^2`.
Integration of `D_i(H_i rho)` over product Haar gives

\[
 \mathbb E\sum_i H_i^2
  =-\mathbb E\Delta\log\rho
  =3\beta\sum_{q\text{ changing}}\mathbb E x_q
  \le30\beta.                                               \tag{8}
\]

There are ten terms and each `x_q <= 1`. Their individual expectations
need not be nonnegative; (8) only uses the displayed upper bound.
Equation (3) gives the pointwise identity

\[
 \sum_j T_j^2=
       \left|-3u+\sum_i s_iD_i u\right|^2
       =9+\sum_i s_i^2.
\]

Combine this identity with (8) to prove (7). The number of links away
from the star never enters. In particular this is not a small-field
estimate or a volume-dependent comparison of densities.

## 4. The one-link variance forces a pair angle

**PROVED / lemma D, using the checked Lemma V.** One has

\[
 \mathbb E\operatorname{tr}
       \big(P_u\operatorname{Cov}(v'\mid X)\big)
       \ge\frac{2}{4+6\beta}.                               \tag{9}
\]

Let H denote all free links except V. It includes X. Conditional on H,
the V density is `Z_kappa^{-1} exp(kappa h dot v')` on the unit
three-sphere, with `0 <= kappa <= 6 beta`. Lemma V already proves
that its transverse second moment is at least `1/(4+kappa)`.
Each transverse mean is zero by rotational symmetry around h. Therefore
its *covariance* matrix obeys

\[
 \operatorname{Cov}(v'\mid H)
       \succeq\frac{I_4-hh^T}{4+6\beta}.                    \tag{10}
\]

The longitudinal variance is nonnegative, so it can be discarded. At
kappa = 0 any unit h works. Conditional total covariance gives
`Cov(v'|X) >= E[Cov(v'|H)|X]` as quadratic forms. Since U is in X,
P_u is X-measurable. Finally

\[
 \operatorname{tr}(P_u(I_4-hh^T))
      =2+(u\cdot h)^2\ge2.
\]

This proves (9). The transverse argument is essential: Lemma V does
not give the same lower bound for every *centered* one-link coordinate.
No such false strengthening is used here.

**PROVED / invariant test space.** Both endpoints of U,V are boundary
vertices of S. Hence u and v' are invariant under every interior vertex
gauge of S. The X marginal is invariant under the induced action of
these gauges on X: apply the full gauge and change variables in Y,Z.
Every such vertex differs from z, so its action commutes with D_i.
It follows that s_i and T_j are also interior-gauge invariant.

T_j depends only on X and lies in `ran E_C`; v'_j depends only on Y
and lies in `ran E_B`. Thus the invariant pair angle k_g bounds their
centered correlations. Using (6), (7), and (9),

\[
 \begin{split}
 \frac{2\beta}{4+6\beta}
 &\le\left|\sum_j\operatorname{Cov}(T_j,v'_j)\right|\\
 &\le k_g
       \left(\sum_j\mathbb E T_j^2\right)^{1/2}
       \left(\sum_j\operatorname{Var}v'_j\right)^{1/2}\\
 &\le k_g\sqrt{9+30\beta}.
 \end{split}                                                  \tag{11}
\]

The last step uses `sum Var v'_j=1-|E v'|^2 <= 1`.
For completeness, if centered f lies in `ran E_C` and centered g
lies in `ran E_B`, then
`<g,(E_B E_C-E_S)f>=<g,f>` in this fibre. Both tests belong to the
invariant space, so its operator norm gives exactly the inequality used.
Zero-variance components can be omitted. The positive left side ensures
that at least one of the four pairs `(-T_j,v'_j)` has positive variances
and correlation at least (1). This proves the identity-exterior bound.

**PROVED / arithmetic range.** The factor `beta/(2+3 beta)` increases
with beta. The following rational lower bounds prove (2):

| beta interval | Lower bound for (1) |
|---|---|
| `[1/16,1/4]` | `c > (1/35)/(9/2) = 2/315 > 1/160` |
| `[1/4,1]` | `c > (1/11)/7 = 1/77 > 1/160` |
| `[1,4]` | `c > (1/5)/12 = 1/60 > 1/160` |
| `[4,64]` | `c > (2/7)/44 = 1/154 > 1/160` |

The square-root bounds use respectively `33/2 < 81/4`, `39 < 49`,
`129 < 144`, and `1929 < 1936`. At beta = 1, (1) equals
`1/(5 sqrt(39)) > 1/35`. These displayed inequalities are hand arithmetic.

## 5. Exterior quantifiers and full gauge-invariant realizations

**PROVED / positive-measure exteriors.** At identity exterior select one
of the four pairs furnished by (11). Freeze those two functions there.
They are bounded, smooth, depend only on X or Y, and remain invariant
under the same interior gauge group when the exterior changes. Their
moments in the finite conditional Wilson integral vary continuously with
the exterior links in the touching plaquettes. Their positive variances
do also. Every strict lower bound on their correlation therefore persists
on an open exterior neighbourhood. Its product-Haar measure is positive;
the Wilson exterior marginal has a positive density, so its measure is
positive too. The neighbourhood need not be uniform in beta or block size.

For every `c' < c(beta)`, such a neighbourhood has angle greater than c'.
Taking the supremum over these c' proves the essential-supremum version
of (1). Throughout (2) choose c' above `1/160`. Thus the obstruction is
not confined to a null exterior fibre.

**PROVED / stronger, globally invariant tests when exterior loops are
allowed.** The predecessor's external-frame construction also applies to
the present four T_j, although they read more than U. Place its three
disjoint exterior loops below the common face, with holonomies
`-i sigma_1,-i sigma_2,-i sigma_3`. Keep all touching exterior links
equal to I. The changed links meet no touching plaquette, so the conditional
law and (11) are unchanged.

Here is the extension for a general T_j. The exterior graph connects all
boundary vertices, as proved in the face-corner predecessor. Choose a
root and exterior paths to each boundary vertex. Their transports identify
the boundary frames. The three exterior loop holonomies at the root give
an ordered frame in the three-dimensional space of traceless anti-Hermitian
matrices. In an invariant open neighbourhood where these vectors stay
independent and positively oriented, Gram–Schmidt makes it orthonormal.
Gauge transformations conjugate this frame and transport the boundary
paths in the usual way.

Use that frame and those paths to express the boundary gauges in the fixed
coordinate frame used above. Evaluate T_j on the resulting X links; do the
same for v'_j on Y. The choice of a lift of a three-dimensional rotation
to SU(2) has only the common central sign ambiguity. Changing that sign
at every boundary vertex is equivalent, on the links, to changing it at
all interior vertices. The latter leaves T_j invariant. Arbitrary gauges
at interior vertices likewise do not change its value. The two resulting
functions are therefore invariant under *all* vertex gauges of the full
configuration. They retain X-only or Y-only free dependence.

At the specified exterior they equal the four original functions. They
are continuous locally; multiply by an exterior-only continuous invariant
cutoff equal to one near that exterior and supported where the frames
exist. Extending by zero gives bounded continuous globally invariant
functions. Their correlations have the same positive-measure extension.
Thus requiring restrictions of globally invariant functions, while allowing
them to read the fixed exterior, does not evade the theorem.

**OPEN / different boundary algebra.** Restricting to closed loops entirely
inside each exclusive region, or averaging arbitrary boundary rotations
while holding the exterior matrices fixed, is a different test algebra.
The present witnesses need not belong to it. The latter operation is not
a symmetry of the conditional Wilson law: (4) shows its nonzero score.
Any proposed replacement must prove that its projections preserve its
algebra and that it still contains the physical tests used in A1–A4.

## 6. The broad local class, assignments, and larger groups

**PROVED / theorem E, local version.** On an ordinary four-dimensional
Wilson torus with no short-period plaquette identifications, the proof
works for any finite pair of link regions satisfying these conditions
at one exterior:

1. A boundary vertex z has every free incident link in X. A chosen
   outgoing U there has both endpoints on the boundary of S.
2. Another link V has both endpoints on that boundary and lies in Y.
   One plaquette has U,V as its only free links, with trace `u dot v'`
   after fixed orientation and exterior transport choices.
3. Among the plaquettes changed by the X-only gauge at z, only that
   plaquette reads a variable outside X. Let n count the changed plaquettes.
   Every other changed term is X-only, and every unchanged term is
   invariant under the action.

For such a pair the conclusion is

\[
 k_g\ge\frac{2\beta}{(4+6\beta)\sqrt{9+3n\beta}}.           \tag{12}
\]

There are only 24 elementary plaquettes at a vertex in four dimensions:
six unordered direction pairs and four choices of signs. Thus `n <= 24`.
At beta = 1, every pair in this local class satisfies
`k_g >= 1/45 > 1/160`. Only replace 10 by n in (8); all other
steps are unchanged. Strict threshold violations extend to positive-measure
exteriors as before. This theorem imposes actual local incidence conditions,
not a symmetry condition on the pair's full shape.

**PROVED / unequal intervals.** Every section-8.1 cover contains the
pair in section 2, with n = 10. This remains true when it deliberately
avoids every theta-symmetric pair. Hence all such covers fail PA_g at
order-one beta, with the stronger range (2). Block sides can be unequal
in every coordinate. Outside the displayed local neighbourhood their
lengths do not enter the proof.

**PROVED / two other assignments.** First, assign a link to a product
box only when *both* endpoints belong to that box. The section-8.1
vertex boxes still cover all links: in the varying coordinate an adjacent
site pair lies in one interval, since neighbouring intervals overlap by
at least two sites. Choose covering intervals in the other coordinates.
At the corner, the same six links incident to z have both endpoints in
B; the incoming direction-2 and direction-3 links do not. None of those
six belongs to C. The plaquette enumeration in section 2 still has p as
its only Y-read. U,V still have exterior incoming direction-3 links at
their endpoints. Thus n = 10 and (1)–(2) hold. The interaction degree
cannot increase, since these link blocks are subsets of the base-assigned
blocks.

Second, assigning positive links by their terminal endpoint is the image
of base assignment under inversion of all lattice coordinates, with each
link matrix inverted when its orientation reverses. Haar measure, Wilson
traces, conditional projections and the interior gauge space are carried
unitarily by this bijection. Reflecting the interval partitions gives the
same local geometry at upper rather than lower faces. Thus (1)–(2) hold
for terminal assignment as well. These are actual assignments covered by
the proof, not a claim about every possible link convention.

**PROVED / changes and groups preserving the star.** Altering regions
away from the plaquettes incident to z and from the endpoint boundary
links of U,V preserves (12), provided U remains X-only and V Y-only.
In particular update regions can each be unions of more than two original
blocks. If the added blocks leave this local incidence pattern unchanged,
their two union projections still violate the pair bound at beta = 1.
Their size and number of components do not enter (12). A grouping changes
the degree and locality constants separately; no original constants are
automatically assigned to the new cover.

**OPEN / groups changing the test.** A group that updates U and V together
removes this pair of exclusive tests. A certificate based directly on the
gap of `sum_(B in group)(I-E_B)`, rather than the angle of two union
updates, is also a different operator statement. Neither is refuted by
(12). The predecessor already explains why a bad pair angle does not
force a small gap of the whole block sum. No numerical or qualitative
argument here decides those grouped criteria.

## 7. Disposition and the remaining PA_g obligation

**PROVED / what moved.** Reflection asymmetry and unequal intervals do
not rescue this pair criterion at beta = 1, beta = 2, or anywhere in (2).
The extension covers every section-8.1 cover, two additional link
assignments, and every pair or grouped union with the local conditions
of theorem E. The witness uses four marginal-score functions on one
exclusive region and four link coordinates on the other. It does not
assert a lower bound for the elementary plaquette traces alone.

**OPEN / large beta.** For nonsymmetric covers at arbitrary growth rates,
(1) alone does not prove a violation when beta tends to infinity. The
factor `sqrt(9+30 beta)` remains after replacing the marginal variance
of V by one. Neither a uniform `Var(v') <= C/beta` estimate nor a
different normalized witness eliminating that loss is proved here. The
predecessor already handles symmetric pairs at every beta above `2/47`
and all covers in its explicitly slow-growth regime. Those domains are
not reopened or counted again. A beta-dependent construction that avoids
all symmetric pairs only beyond (2), and grows outside that slow regime,
remains undecided by the combined results.

**ARGUED / failed route retained.** Applying the earlier positive-kernel
argument to asymmetric halves would assume that two different half
integrals form a square. They need not. The current method avoids that
step but pays the explicit Fisher-information factor in (12). No Wilson
association, monotonicity in beta, or small-field approximation fills this
remaining loss. In particular failure at beta = 1 is not extrapolated
to an asymptotically free trajectory.

**OPEN / what an escaping PA_g proposal still needs.** Specify its actual
cover, link assignment and invariant fibre algebra. Establish the required
uniform norm for every interacting pair and essentially every exterior,
on that cover's coupling trajectory. Verify its degree, coloring and
physical locality constants before using A1–A4. If it changes the operator
to a grouped certificate, supply that certificate's inequality and the
locality argument anew. An absent corner witness proves none of these
upper bounds. No successful cover below `1/160` is constructed here.

**ARGUED / check request and recovery.** A separate reader should check
the ten-plaquette enumeration, the sign and conditioning in (6), the
centered transverse variance in (10), the invariant status of T_j, and
the boundary-frame extension. This is one author proof, not an independent
check. No numerical run, machine enumeration, audit, registry edit, or
public post was used. No mass-gap conclusion follows. The next new proof
target is precisely the arbitrary-large-beta nonsymmetric case stated
above, or a different grouped operator supplied with its own contract.

RESULT: PROVED by hand, awaiting a separate check: every section-8.1 product-box cover, including unequal intervals and covers with no symmetric pair, has invariant pair angle at least beta/((2+3 beta)sqrt(9+30 beta)); PA_g fails for 1/16 <= beta <= 64, uniformly in block size and torus, on positive-measure exterior sets. The same range covers terminal and both-endpoint assignments; a local boundary-star theorem also covers star-preserving grouped unions at beta = 1. OPEN: arbitrary-large-beta nonsymmetric growth, assignments or boundary algebras lacking this star, and genuinely different multi-block certificates.
