# Final-source mathematical review: native formation and cubic centering

Reviewed source, not a new blind reconstruction. The complete 671-line note,
canonical runner and all three declared scientific checkers were read.
Earlier independently derived proofs were reused only after byte verification.
No production, Git, PR, audit, graph or cache changes were made.

The frozen note needs two narrow corrections, listed below. I found no further
unresolved mathematical defect in the stated bounded results. This disposition
is conditional on those corrections and on the note's explicit smooth-interior,
fixed-parameter and coefficient-before-volume hypotheses; it is not a retention
or audit verdict.

## Findings requiring correction

**F1 — inherited Dirichlet-form argument, Part A Eq. (4), lines 112–117.**
The equation writes D_N(sqrt(f_t)), while its following sentence adopts the
checked proof's convention. Both the inherited acoustic note and the sealed
Euler/native reports define

    f_t=dmu_t^N/dpi,
    D_N(f)=sum_e E_pi[(sqrt(f(eta^e))-sqrt(f(eta)))^2].

With that convention Eq. (4) must contain D_N(f_t). The displayed square-root
argument instead takes differences of fourth roots of the density. The proof
controls the former expression and needs that expression for its marginal
Hellinger comparison. The independent check makes the distinction exact on
a two-state uniform space with normalized density (1/41,81/41):
D(f)=64/41, whereas D(sqrt(f))=4/sqrt(41).

Narrow correction: replace D_N(sqrt(f_t)) by D_N(f_t) and explicitly define
f_t and the square-root-density form beside Eq. (4). The entropy constant,
one-block argument and theorem need no change.

**F2 — zero-birth boundary of strict time-response prose, Part A §3,
lines 223–226.** The model explicitly permits beta=0 at line 71. In that case
rho(t)=rho0 and both gains in Eq. (13) are identically one, even for j=1/2
or j<0. Thus the unqualified assertions of strict decrease and damping do
not include the whole declared parameter range.

Narrow correction: scope those strict statements to beta>0, and state that
beta=0 gives constant uniform gains. Eqs. (11)–(15) themselves are correct
also at beta=0. This is an edge-case wording repair, not a counterexample
to the reaction-current theorem.

Both findings were sent to the author before this seal. The author agreed
to preserve the frozen inputs until completion; no correction is assumed
to have occurred in this report.

## Part A: reconstruction and premises

The two exchange choices must remain distinct. Part A imports the fixed
axis-balanced context exchange (including all unequal-label swaps and its
positive floor) from the identity-matched acoustic note. Part B uses constant,
label-independent symmetric stirring. The latter dual-particle calculation
does not automatically extend to the former. The note states this separation
before Part A, in its frontmatter, and again in the limitations.

With microscopic births beta/N, Euler acceleration gives macro birth rate
beta U_a. Under a local product p, the center vacancy is independent of its
six distinct neighbors, so the reaction is exactly

    B_a(p)=beta p0 [p0+sum_b W(a,b)p_b]^6.

This product average is a local-equilibrium coefficient, not an assertion
of exact finite-volume product evolution. No symmetry or row-sum constraint
on the fixed positive matrix W is needed for the general reaction theorem.
The uniform bound uses max(1,W_max), appropriately including the vacancy
weight. With the Dirichlet notation repaired as F1 specifies, the upper
bound R*1<=beta max(1,W_max)^6 V is correct: at an occupied center there is
one incoming channel and at a vacancy only negative outgoing terms. This
explains why the bound does not acquire an extra factor six.

For an inhomogeneous product reference, the exact adjoint contribution at x is

    beta sum_a U_a(x,eta)[1_(eta_x=a)p0_x/p_(a,x)-1_(eta_x=0)].

Its local-product average Vbar(q;p) has Vbar(p;p)=0. Differentiating in q,
the derivative of the neighbor factor vanishes because its prefactor is zero.
The remaining derivative is H(p)B(p), with
H=diag(1/p_a)+(1/p0)11^T. It cancels the reaction part of the reference
log-density derivative only after local-equilibrium replacement. Treating
this as a pointwise cancellation would be wrong; the note explicitly does not.

The inherited finite count-sector comparison remains applicable because
the absolute-entropy dissipation bound is integrated in time and uses only
the exchange floor. Births need not preserve count sectors for this use.
At fixed block size, the marginal Hellinger error vanishes as N grows.
Canonical means differ from product means by O(M^-1), averaged variances
are O(M^-1), and removing anchors whose seven-site footprints cross the
block boundary costs O(ell^-1). The reaction coefficients are bounded on
the stated compact interior reference set. Their remainder is uniformly
quadratic for all block count vectors, including boundary count vectors.
The inherited concentration/entropy estimate and Gronwall then apply,
taking N to infinity before ell. A supplied C2 interior solution, not a
global existence or shock-selection result, is essential.

For the j-family, summing the six species reproduces every term in Eq. (10).
There are three vector fields, one density field and two independent
quadrupoles. Uniform growth gives rho'=6beta(1-rho); the linear vector
reaction is 12beta j(1-rho), density reaction is -6beta and the quadrupole
reaction is zero. The principal transport coefficients in Eq. (12) agree
with the inherited flux. Alpha is the inherited fixed drive amplitude and

    c_s(t)^2=4 alpha^2 rho(t)^2(1-rho(t))/3.

Thus the displayed frozen roots have the correct signs and normalization.
The note imports alpha and c_s through the linked acoustic construction;
their absence as repeated local definitions is not a separate mathematical
defect. Zero alpha gives a degenerate, still isotropic principal symbol.

For complex Fourier amplitudes in coordinates (delta rho,delta g1,
delta g2,delta g3,delta r1,delta r2), with delta r3=-delta r1-delta r2,
the complete entropy metric has quadrupole block
(3/rho)[[2,1],[1,2]]. Direct reconstruction of Hdot+M*H+HM for arbitrary
real K1,K2,K3 verifies Eq. (14), including the two static quadrupoles'
changing weights. Consequently Eq. (15) is a bound for the actual
nonautonomous linear system, not an inference from frozen eigenvalues.
It is uniform over Fourier wave vectors. The positive-part threshold
and j<=1/4 nonincrease statement are correct, with equality allowed.
At beta=0 it reduces to conservation.

The adjacent connected-covariance source 4beta j rho(1-rho)/3 is correct.
At the initial product, context exchange contributes zero by product
stationarity; each birth endpoint contributes 2beta j rho(1-rho)/3.
This is an initial-time witness of nonproduct evolution, not a later-time
factorization. The source and its 1/18 example agree with the sealed
independent result. The note appropriately leaves the interacting native
fluctuation theorem unproved.

## Part B: projection, powers and normalization

At j=0, symmetric stirring and uniform independent births preserve the
evolving homogeneous product. Finite-volume dependence on j is analytic.
For one vector component, the first pair coefficient has source
S(t)=4beta rho(t)v(t)/3 and drift 2kappa N Delta_ref. The factor two counts
the two moving endpoints. An adjacent endpoint exchange reverses their
relative coordinate; it vanishes on the even covariance, so the punctured
walk is the correct restriction here.

The three-feature argument is not a closure assumption. A stirring swap
between a vector-feature position and the vacancy-feature position must be
included. With it, projecting the three-feature chain to the pair gives
H2 exactly. Uniform births kill the vacancy feature at rate lambda=6beta
and have zero vector drift. In the first-order source, a vector multiplied
by a vacancy at the same site is zero, while the other endpoint source
acquires precisely one factor v(t). Hence T=vQ by uniqueness of a finite
linear system.

For diagonal components, the vector pair is unordered. Off-diagonal
components vanish by independent global coordinate sign flips of the
isotropic constant-stirring model; alternatively one can use ordered
component marks. Thus the use of an unordered H2 does not hide an
off-diagonal closure hypothesis in the equations as used here. The new
exact finite checks verify H3 P=P H2 on a four-cycle and a four-site star.
Blocking vector/vacancy-feature exchanges produces a nonzero defect in
both cases, a decisive control for the load-bearing projection rule.

Summing the six birth labels removes odd powers from the instantaneous
total hazard. Its quadratic term is 2beta times the vacancy-weighted
sum of neighbor dot products. The unperturbed pair expectations vanish.
Consequently m1=m2=0, and the first pair response supplies m3, with factor
6beta=2beta times three vector components. Connectivity, positive
beta,kappa,t and interior v0 give strict positivity of m3. These parameters
are explicitly restricted in Part B, unlike the beta>=0 convention in
Part A. The note does not assert the positive coefficient is an all-j
monotonicity theorem.

The unit-rate Laplacian convention is consistent throughout Part B:

    pair motion: 2 kappa N Delta_ref,
    -Delta_ref(6G)=b,
    N C_N(r,t) -> (4beta rho(t)v(t)/kappa)G(r).

My sealed blind report used the Green function g for 2Delta, so G=2g.
Its star constant Gstar=90g(0)-9 equals 3A_star here. Substitution gives
exactly the same cubic density coefficient and the same closed expression
D(t). The author runner's transformed variable exp(-lambda t)C, two
exponential forcing coordinates, and reward 6beta v0 reproduce these
normalizations. No factor of two or three remains unresolved.

## Uniform heat proof and order of limits

The new presentation of the finite-volume proof is sound. Extending across
the missing origin by the mean of its six neighbors gives the exact
variance identity. Each neighbor pair has an origin-avoiding path of
length at most four, including N=4. Therefore the loose factor
E_full<=11 E_punctured is valid uniformly in N. The L1 and L2 comparisons
follow respectively from the triangle inequality and Jensen and hold for
complex functions. The independent controls construct the stated paths
on N=4,5 and verify the extension variance matrix identity exactly.

The finite Fourier cutoff yields the Nash inequality with the N^-2
correction. Both optimizer endpoints are accounted for; constant
functions are not incorrectly subjected to an infinite-volume inequality.
Applied to P_t delta_x, it yields decay until the O(N^-3) threshold and
monotonicity afterward. The semigroup identity and Cauchy-Schwarz extend
the bound to every pair of vertices. Hence the bound on P_t b has constants
independent of N and location.

Compact-time kernel convergence follows by rate-six uniformization and
a Poisson jump-count tail. After u=2kappa N(t-s), the large-u tail is
O(U^-1/2)+O(Nt/N^3). It therefore vanishes in the required sequential
limit at fixed physical t and kappa. The potential identification also
checks: W=6G is bounded, nonnegative, decays at infinity, and solves
-Delta_ref W=b. Dynkin's identity followed by the finite-set/complement
split proves P_t W->0, avoiding an unproved uniqueness claim for an
infinite-volume inverse. Dominated convergence in the density integral
is justified by the same uniform bound.

The result concerns fixed t, positive fixed beta,kappa and Taylor
coefficients taken at j=0 before N grows. It establishes no uniform
Taylor remainder. In particular sqrt(N) growth of the zero-mode cubic
mean coefficient does not disprove a CLT at any fixed nonzero j. The
note states this limitation explicitly, and does not transplant the
symmetric-stirring coefficient to nonzero context drive. No exchange of
kappa->0, t->infinity, boundary density or infinite collection of modes
is supplied or needed for the claimed coefficient limit.

## Code and recorded evidence

The canonical runner and all three scientific sources were fully read.
The Euler checker uses exact rational/symbolic controls, including
nonsymmetric W and a nonproduct-law witness. The centering checker
assembles its 2401-state four-cycle generator separately from the
relative-position response; its finite-dimensional exponentials and
Green integral are numerical. The energy checker checks symbolic
identities and selected exact finite graph identities. The wrapper copies
all three files into a temporary directory, so the energy check's import
of the centering helper resolves within that copy. Its twelve mutations
change only their declared suite's proposed calculation.

Authentication, not rerunning for counts, verified:

- Current identities in AUTHOR_RUNS.json, AUTHOR_VERIFICATION.json and
  every baseline/mutation result match the frozen sources.
- The recorded baseline contains its declared 11+7+6 scientific controls
  plus one source/scope check.
- All twelve executed mutant hashes equal the unique declared textual
  replacement of the authenticated source. Each failed in its selected
  mathematical suite with AssertionError, not a syntax or wrapper failure.
- All seven preserved 3D NPZ hashes, their reported coefficients and the
  finite-cycle quoted tolerances match the underlying arrays.
- The initial bookkeeping failure is preserved. The actual mathematics
  passed 25 controls, but its copied wrapper expected 91 and stopped
  before mutations. No scientific target or source change is inferred.

The original finite-size sequence includes N=4 above the limiting value,
then N=8 below it. The prose accurately avoids claiming global monotone
convergence. The QUADPACK error is identified as an estimate rather than
an interval certificate. No numerical run is presented as a proof of the
uniform heat estimate. The canonical runner's introductory use of
"exact controls" is read together with its explicit mixed symbolic and
numerical scope and the note's precise explanation, not as claiming exact
matrix-exponential evaluation.

The portable verifier authenticated six capsules, 61 sealed artifacts,
27 dependency links and four instruction snapshots. The two relevant
blind reports retain their original identities:

    native Euler REPORT:
    dddec2c24051a77ff46e5c333e4a63c269ddb4b1739f60ba8543b8b0fcde023c
    native Euler PRE_SOURCE_SEAL:
    bcc3bc4ccdefc35df7fd42c8427b2fa7bd8350dab8a7471692ea169acd683c88
    native centering REPORT:
    24b168b662c0e6f72f1b2f95a6efe7fb3440eb5b5d57addf951020335fe05f4e
    native centering PRE_SOURCE_SEAL:
    cb26009a925ecd6861de994e57df67f904f906e5beac33aae6e6ed958b8a5d8e

The new independent checker ran once and completed ten exact selective
groups, including the deliberate blocked-feature negative controls. Full
logs and results are beside this report. There were no failed new review
executions; earlier unsuccessful attempts remain in the authenticated
capsules and author-development directory.

## Source identity, disposition and limits

Frozen note:
2cb9e232400292ef28f75b16ebca67f30a335ed48c03af060180a4f4e7a8bf38

Canonical runner:
fa22aa845d9aef1a1e0d99072ec93c719ec94abfa50e86d674022c0f067f450a

Scientific checkers, respectively Euler, centering and energy:
2e7b6754b68fa78ea987e903253d89401f8a04411509a62ab67b42fcc257ba49
ad960c462bc198e0faffa9060ca8aa84ef9e8bdabace17b7b91fea581dc78bee
4fd9b1947b07a3f13b5470bbabe14f2ad0d0bb28ce9344027c07a0cd1286f633

AUTHENTICATION_RESULTS.json inventories 56 source/evidence files.
SOURCE_REVIEW_SEAL.json binds that inventory, this report and every new
review artifact. Graph/cache integration was outside this review and was
not sealed. No new external literature, primary campaign calculations or
unrelated publication sources were used.

F1 and F2 remain unresolved in these frozen bytes. Once their narrowly
specified edits are applied, only an affected-source acknowledgment is
needed; no unaffected mathematical check requires repetition. The
fixed-j remainder and native interacting fluctuation limit remain named
future obligations, not defects in the bounded claims actually made.
