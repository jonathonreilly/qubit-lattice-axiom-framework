# Selective review: quantitative routed Euler bound

2026-09-21. The supplied quantitative refinement is mathematically supported
under its explicit inherited hypotheses. No unresolved mathematical finding
or required source correction was identified. This report is a source-bound
scientific check, not a formal audit, retention decision, new physical field
identification, or independent rerun of production dynamics.

The reviewed conclusion is

    sup_(0<=t<=T) E||Y_N(Q,t)-exp(-i A(Q)t)Y_N(Q,0)||^2 <= C N^-1/6,

for sufficiently large even N, fixed full-support p, fixed k0>|gamma|,
bounded fixed autonomous plaquette rate nu, fixed modes Q and fixed T.
Product colors must initially be independent of the arbitrary full-matching
law. The corresponding norm rate is N^-1/12. The constant is finite but
unspecified and is not a practical finite-size accuracy estimate.

## Independent boundary and evidence

The complete new note and the identity-matched routed, moving and preparation
premises were used before accessing the quantitative author checker or any
of its outputs. The reconstruction and independent controls were sealed in
PRE_COMPARISON_SEAL.json, SHA-256
`aa6077d488a34f77be0d9cc21542e174284ae222d6f006ef593b3d6a63b29ba4`,
binding seven artifacts and thirteen source/dependency files. The complete
proof assessment is in PRE_COMPARISON_DERIVATION.md; it remains unchanged.
The subsequent comparison reauthenticated every preseal row.

I then read the complete final author checker, all RESULTS.json, the full
success log and empty stderr, and the preserved development-failure receipt
and traceback. The complete difference to its preserved earlier checker was
examined and independently recovered in both directions. No quantitative
author module was imported or executed. Reusing authenticated earlier
proofs and checking author logs is not counted as a new independent proof.

## Load-bearing estimates reconstructed

The open-cube path load is exactly 2a(L-a)L^2, including both orientations.
Representative paths remain a subset of that all-site route collection.
Contraction and loop erasure do not create edges, and a simple contracted
edge has at most two physical representatives by bipartiteness. Endpoint
words use an edge at most twice and have length at most 6L. With the
inherited unit-rate convention D=(1/2)sum E[(f^e-f)^2], these facts give

    D_all <= 12L^5 D_C,
    Var <= 48L^2 D_C <= (96L^2/k0) D_actual.

The argument is valid conditional on exterior colors and footprint counts.
It uses actual symmetric swap forms. It does not assume stationarity of an
artificially truncated context-dependent generator.

Conditional Poincare, variational duality and the order-l^3 overlap give a
squared negative norm C l^5 for the normalized centered-current sum. The
previously checked stationary or conditional-history energy bound therefore
gives C T l^5/N for its Euler-time integral. The moving-geometry constant
does not grow with the number of geometry jumps.

The canonical correction is exactly centered for each footprint. Coupling
four samples with and without replacement gives an O(1/m) correction, and
Taylor expansion with the iid empirical fourth moment gives variance
O(m^-2). Its normalized spatial sum has variance O(l^-3). The black-cube
replacement has exact squared coefficient norm

    1/m_B - 1/m_C = O(l^-4),

since only O(l^2) outside black partners are added to a cube containing
order-l^3 black sites. Block overlap and bounded shifts therefore give
O(1/l), as claimed.

Constant mean currents must cancel before the phase expansion. This is an
explicit step in the inherited routed proof: sum_u N[phi(q_delta u)-phi(u)]
is zero for each routing permutation. The new centered-field argument
correctly relies on it. Applying the remainder estimate to uncentered
constants would be an invalid alternative and could create a volume loss.

The phase Taylor remainder is at most 2|Q|^2/N because routing displacement
is at most two. Exchanging block and site sums bounds each ordinary-block
coefficient by the supremum of its input coefficients; for irregular pair
footprints a fixed factor, conservatively two, suffices. Thus phase errors
have squared norm O(N^-2), uniformly in l. Coefficients in this application
are deterministic conditional on geometry; independence is not available
for arbitrary color-dependent weights.

The ordinary Fourier multiplier has distance at most sqrt(3)|Q|l/N from
one. Incoming direction terms cancel after reindexing and using
sum_delta A_delta=0. Their remaining bounded block shifts and phase changes
give O(1/l)+O(N^-2). These estimates do not require regular, equilibrated,
or stationary matching geometry.

The actual joint-process martingale has bracket O(T/N). The moving
extension adds the already checked O(T nu^2|Q|^2/(k0 N)) integrated drift
bound and another O(T/N) bracket. The residual integral equation and
Cauchy--Schwarz/Gronwall give

    C [l^5/N + 1/l + l^2/N^2 + 1/N].

Only fixed-time second moments, uniform over the interval, are required;
there is no claim about the expected path supremum, no derivative bound on
the integrated residual, and no need for A(Q) to be normal. Choosing
l=floor(N^(1/6)) eventually meets the stipulated radius and embedding
conditions and gives the asserted rate.

The optional post-completion preparation error epsilon_N=N^-4 changes the
expectation of the squared residual by at most C K epsilon_N=O(N^-1).
The random formation time is additional. The physical endpoint field has
the inherited sqrt(2) normalization and product-reference squared phase
discrepancy O(N^-2); preparation transfer can add O(N^-1).

## Independent controls and author comparison

The independent script used no author code and passed on its first run,
with full stdout, empty stderr and execution receipt preserved. It checked
all open-cube ordered routes for L=3,5,7; all 2775 and 3003 endpoint words
in separate N16, l2 columnar and irregular footprints; and 6000 preselected
words each in N36, l6 columnar and irregular footprints. The latter radius
satisfies 2l+5<N/2. Their larger inventories are explicitly sampled, not
exhaustive. Local graph connectivity, multiplicity, endpoint permutation,
boundary normalization and exact coefficient norms were checked separately.

It also checked all ordinary and irregular footprint memberships in an
N16 fixture, all six phase directions and a non-axis mode. Exact Fraction
binomial calculations at m=4,7,13,31,64 verify a canonical pair-statistic
remainder and the fourth-moment formula. A nonnormal two-dimensional matrix
with three bounded integrated forcing frequencies tests the Gronwall step;
the integral-equation residual was below 8e-17. These are controls on the
general sampling and propagation sublemmas, not changes to the color model.

The complete author results bind their final checker and inherited lattice
helper correctly. The open-cube inventories and common columnar endpoint
inventory agree exactly with independently computed values. All seven
logged footprint rows exactly equal their result rows. Their integer
coefficient sums were recomputed by a different full-array convolution:
the maxima are 113, 210 and 546 at cardinalities 63, 171 and 1099. All nine
Fourier multipliers were independently recovered from a factorized ordinary
plus parity-alternating coordinate sum, with error below 3.4e-16.

Coverage qualification: the author's N32, l6 example is a valid embedded
current-containing footprint and a sampled geometric control, but it does
not meet the theorem's stronger global inequality 2l+5<N/2. Their l2 and l3
cases likewise test the counting sublemma. The result scope describes
finite path/coefficient controls rather than finite verification of the
all-N theorem; no false all-N inference is used. My N36, l6 controls also
exercise the displayed theorem range. No source correction is required for
this distinction, which must remain explicit in any later coverage claim.

The author checker does not directly test irregular coefficient smoothing,
canonical moments, the nonstationary energy estimate, or the final
propagation inequality. Those rely on the reconstructed proofs and, where
useful, the separate independent controls. Its finite PASS lines are not
treated as evidence for these omitted proof obligations.

The preserved author failure occurred after the open-cube group: the
lattice index helper was used as a dictionary although it is callable.
Exactly two expressions changed to function calls. Forward and inverse
recovery match the preserved and final source hashes, and the successful
log is bound to the final checker by its result manifest. No mathematical
target or comparison constant changed. No independent helper failure
occurred in this review.

## Scope and source identities

This review imports the previously checked routed theorem, conditional
moving-geometry energy estimate and preparation transfer at their unchanged
identities. It does not claim a new proof of every inherited result. All
load-bearing changes in the present refinement were reconstructed.

The bound is for fixed finitely many modes and fixed T, with constants
depending on full-support p and fixed rates. It is not uniform at density
boundaries, for modes or horizons growing with N, for rates growing with N,
or for an arbitrary nonproduct color entrance. It is not an optimal rate,
a fitted exponent, a finite-wavelength diffusion formula, a thermodynamic
phase conclusion, or an identification of propagating colors with the
separate geometric Gauss field. No production aggregates or N256
observables were accessed.

Key SHA-256 identities (complete byte counts and paths are in the manifests):

* Reviewed note: `f3883ac1951ede774121807ab83678fd3622c93ee79f4c0d4aa7e50862564bf1`.
* Final author checker: `f3f7ffd137678cb282a0ae289e7a4c3fbd99a2e5bacdf59032eb36db9a4e2449`.
* Final author results: `5fc91245c51a0db06efc3e728dd6e5bae9d2a6762327214d2cc0d4f3fb16b862`.
* Final author log: `4cc0ee9de5298e30b1901582876786248a557e541d4e111decad8a4d07fc91a5`.
* Inherited lattice checker: `98aa5259d58a5355a2aa9283e19bad869160bd9432882d589db8bbb2e0f15921`.
* Preserved failed checker: `832f89f37b79430b1ea09a90470b182498d2ad772c4a8b13ee59c34a98fadc92`.
* Independent checker: `11e45083a99fd0f650cd6b508d9555da4db81e75bd0d5bc203e3908d5451b866`.
* Post-seal comparison checker: `1f796a5efb63728cb7c03f9bc2b857b93cd5bf09a7e75e1a38862ea6e06ae5cc`.

PRE_COMPARISON_SOURCES.json binds the three exact dependency notes and prior
review seals. AUTHOR_COMPARISON.json binds all ten inspected author and
development files. FINAL_SEAL.json binds this report, every local execution
artifact, the unchanged precomparison packet and all source identities.
The earlier finite-wavelength F1 acknowledgment is a separate sealed packet;
no earlier review artifact or primary source was changed here.
