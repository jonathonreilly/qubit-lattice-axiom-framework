# Independent review of the uniform dilute Gauss-loop proof

The proposed periodic E/B theorem checks out in the supplied domain
max(zA,zB)<=1/(400e^2), for nonnegative real fugacities, odd N>=7 and
the full constrained grand ensemble. I reconstructed the component mapping,
counting, rooted cluster estimate, source differentiation, spatial bound,
periodic limit and analytic tensor conclusion. No load-bearing gap remains
in that theorem. Two broader extensions need the explicit conventions
below. This is mathematical scrutiny, not an audit verdict.

The complete proposed note was read first. Independent calculations and
provisional findings were then sealed before access to the author polymer
checker or its results. After that seal, both were read completely and
authenticated without rerunning for counts. PROVISIONAL_REVIEW.md preserves
the longer reconstruction and the exact pre-checker boundary.

## Clarifications to the broader extension language

**F1 — general bounded observables.** For one-slot functions f,g, define

    A_f=max_occupied |f(label)-f(vacancy)|,
    A_g=max_occupied |g(label)-g(vacancy)|.

The same proof gives
|Cov(f_x,g_y)|<=(2/e) A_f A_g exp[-d_1(x,y)/4].
The displayed E/B bound has A_f=A_g=1. Saying that the same argument
applies to any bounded observable is correct with these factors; the
same numerical prefactor without a normalization is false under arbitrary
finite rescaling of a nonconstant observable. Add the factors or a stated
normalization to that extension.

**F2 — vacant-exterior boxes.** The proof supplies the claimed box
comparison when allowed record midpoints lie in the box, outside
records are fixed vacant, and Gauss is still imposed at every charge
vertex incident to any allowed edge, including boundary/exterior
vertices. State this convention. Dropping those boundary constraints
permits open currents and is a different specification; it is not
covered by the component restriction argument as written.

These are extension-scope clarifications. Neither changes the explicit
E/B covariance estimate, the odd-periodic limit, or its quadratic
infrared consequence. No production source was repaired in this review.

## 1. Imported result and exact polymer mapping

The actual external input read was Ueltschi's
[arXiv v3, Section 2, Theorem 1 and bound (5)](https://arxiv.org/pdf/math-ph/0304003v3),
including its complete proof through page 4. Its 1/m! convention and
marked-root normalization were checked directly. The downloaded v3 PDF
and read boundary are recorded in EXTERNAL_SOURCE.json. No result from
its later correlation section is assumed.

A polymer is a connected component of one species' occupied charge-edge
support, retaining orientations and satisfying internal midpoint capacity.
Balance restricts componentwise because different same-species components
share no charge vertex. This gives a unique polymer collection. Cycle
decomposition is unnecessary and can be nonunique.

Conversely, incompatible midpoint occupation excludes all cross-axis and
cross-species capacity violations, while same-species shared-vertex
exclusion forces the proposed components to remain distinct. A compatible
collection gives exactly one original configuration with the same product
activity. Different species may share a charge vertex; they may not share
a record midpoint.

The independent control includes a ten-record branched component with
two distinct simple-cycle decompositions, a pair of vertex-disjoint
components sharing a forbidden midpoint, and a valid two-species pair
sharing a charge vertex. These distinguish all parts of the mapping.

## 2. Counting, enlarged activities and the site root

The odd-torus charge graph is simple of degree six. Its line graph has
degree ten. A deterministically chosen spanning-tree depth-first walk,
starting at a prescribed edge, has 2(n-1) steps and visits exactly the
connected n-edge set. Recovering that visited set proves injectivity;
there is no omitted tree multiplicity. The resulting bound is
10^(2n-2), multiplied by 2^n for signs. Balance and internal capacity
only reduce it. Every valid component has at least four records.

For each record in a fixed polymer, incompatibilities are covered by
eleven same-species endpoint edges and six typed midpoint choices.
Their union has sixteen elements in this geometry; seventeen is a safe
overcount. Thus 17n anchor families suffice.

With |w|exp(n), a=n and q=200e^2 max|z_s|, each typed-edge family has
enlarged weighted sum at most

    S(q)=q^4/[100(1-q)].

At the proposed radius, q<=1/2 and S<=1/800. The ordinary-polymer budget
is at most (17/800)n<a. The finite hard-core measure and its weighted
total variation are finite, and |1+zeta|<=1 holds including self-
incompatibility. Thus the cited theorem's actual finite-volume hypotheses
are met uniformly in N. No infinite total-variation measure is inserted
directly into that theorem.

A zero-activity auxiliary root at x, incompatible with every polymer
occupying x, has budget at most 6/800 and can take a=1. Its zero mass
does not affect the ordinary conditions. The rooted estimate is exactly

    sum_clusters |C| exp(M) R_x <= 1,

where M sums record sizes with occurrence multiplicity and R_x counts
polymer occurrences occupying x. Repeated polymers and the 1/m!
normalization are essential. A separate connected-graph enumeration
through five repeated copies gives coefficient (-1)^(m-1)/m and verifies
the one-root and two-source multiplicities.

## 3. Source derivatives and spatial decay

A local field source factors correctly over compatible polymers. Its
cluster derivative is the sum of the corresponding marks, bounded by
R_x. Two derivatives give an insertion bounded by R_xR_y<=R_xM.
Choosing a complex neighborhood with total source modulus below one
uses only part of the exp(M) margin; this justifies differentiation
uniformly. No convergence for arbitrarily large source strengths is needed.

Within a component, charge-edge adjacency connects record midpoints
at physical distance at most two. Every incompatibility supplies either
the same connection or a common midpoint. A connected cluster hitting
x,y therefore has d_1(x,y)<=2(M-1). Hence

    M exp(-M)<=(2/e)exp[-d_1(x,y)/4],

and the rooted sum proves the stated component covariance bound. For
general f,g the marks first subtract the vacancy values and introduce
the factors in F1. This reconstruction uses actual sources of the
original constrained configurations, not a covariance of an assumed
independent loop gas.

## 4. Thermodynamic passage and winding

A cluster with M smaller than a fixed small multiple of N lifts uniquely
near a fixed root; its activity and incompatibilities agree with the
infinite model. A failure of that lift requires mass growing linearly
in N. Rooted tails decay exponentially in M, even after any fixed number
of source derivatives.

For a finite support of small sources, log Z(h)-log Z(0) uses only
clusters meeting that support. Summing the corresponding site roots
gives a uniform majorant. Its limit and derivatives determine all finite
joint laws. This supplies the periodic thermodynamic passage explicitly;
it does not invoke dynamical mixing. Restricting the infinite polymer
family to boxes gives the same local limit under the convention in F2.

For positive activities, the probability of a given polymer is at most
its activity, since the compatible partition-function ratio is at most
one. A noncontractible winding polymer needs at least N edges. Summing
the anchored exponential bounds therefore suppresses winding by an
exponential in N, up to a polynomial volume factor. This is consistent
with the previously checked finite zero-mode term 2N z_s^N I. The
finite grand ensemble has not silently excluded winding or count sectors.

## 5. Analytic Gauss and cubic tensor

The exponential covariance bound makes the infinite Fourier covariance
analytic in a complex strip. The local constraint passes to the limit
and gives S(k)s(k)=s(k)^T S(k)=0. At any zero k0 of the centered symbol,
its derivative is diag(cos k0), an invertible sign matrix. Approaching
k0 in arbitrary directions therefore forces S(k0)=0.

Inversion makes S even. Together with covariance exchange symmetry this
makes the real-momentum matrix real symmetric. Its linear Taylor term
vanishes. The general signed-cubic quadratic tensor has diagonal
a|k|^2+b k_i^2 and off-diagonal c k_i k_j. Transversality yields
b=c=-a, giving a(|k|^2I-kk^T). Positive real fugacities imply a>=0.

Uniform complex-fugacity bounds justify analytic thermodynamic passage
of the coefficient expansion. The leading coefficient along a fixed
ray is 8a0^4 epsilon^4, or 8b0^4 epsilon^4, with O(epsilon^6).
Its claimed strict positivity is properly limited to sufficiently
small positive epsilon with nonzero species amplitude. Higher-order
cubic anisotropy is not excluded.

## 6. Scope counterchecks

This theorem concerns the specified grand ensemble and its periodic/
vacant-boundary limit. It does not establish mixing or state selection
under the irreversible formation dynamics. The latter adds four records
per birth, preserves zero total feature from empty, and does not leave
the grand law invariant. Conditioning on other count or winding sectors
is not part of the proof.

A sharp countercheck to broader uniqueness or stationarity claims is
the equal mixture of fully occupied uniform +A1 and -A1 configurations.
It is Gauss-free and stationary for the physical conservative moves,
yet its E1 covariance is one at every separation. Indeed each uniform
state is frozen even against arbitrary finite constraint-preserving
changes: for compactly supported delta E, summation by parts gives

    sum_x x_j D2(delta E)(x)=-2 sum_x delta E_j(x).

A balanced finite change must have zero total feature. Starting with
E1=1 everywhere, every delta E1 is nonpositive by capacity, so all must
vanish. Thus these fixed-boundary states cannot be replaced by the
vacuum-polymer state merely from Gauss admissibility. The note correctly
does not claim uniqueness for all Gibbs boundary conditions.

Outside the sufficient radius, failure of this majorant proves neither
existence nor absence of a high-density phase. No Coulomb phase, phase
transition, dynamics, quantum interpretation or formation-selected law
is supplied by the present argument.

## 7. Checker comparison, preserved attempts and identities

The primary checker exhaustively enumerates configurations on three
restricted finite charge-edge geometries. Its coverage is not all
thirteen-label assignments on a full torus. Within those stated
geometries its component construction, capacity rule, self-consistent
enumeration and deliberate omission controls are sound. Its anchor,
convergence and tensor checks agree with the independent ones. The
recorded ten primary groups were authenticated, not rerun as proof.

The independent checker completed eleven groups. Its first run stopped
on SymPy structural equality between equivalent forms -(M-2)/2 and
1-M/2. The first script and complete log are preserved; a receipt records
the zero simplified difference. The corrected run changes the comparison,
not the identity or constants.

Reviewed proposal:
3e37fcfa4a946934e09eb2af516e95d3902151ea1085afdabfcea36f03d1c6d3

Identity-matched model:
684f10acda3ebf659ed4b1b47e3fbe35a29c92dfbe1fee77e9cd9469b27f0c30

Primary checker and recorded results:
493542d38c4489a6245eff38846d7de80207c899b05833fcbfc38f8807912eec
6eb5b86df4a756e014306cecfd6088504f462ab7a43e05b6578b13153a77fb3b

Ueltschi v3 PDF:
2cc3e036af5b2a46afe95acf0b5863fe5c7d31554debb10a2a5cade4122bdbfc

Pre-checker seal:
771a65053783c39cb5865e922c4211cb0e234e682613af98c735b3f159342045

SOURCE_COMPARISON.json records the complete source inventory.
FINAL_SEAL.json binds the report, checker, raw successful and unsuccessful
logs, external source/version receipt and all earlier seals. The closing
Henley/Hermele literature comparisons are not used or independently
verified here. No production files, Git/PR state or audit status changed.
