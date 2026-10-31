# Independent review of the all-order link-ball traces and Gaussian cutoff component

**VERDICT: LAND**, at the source's stated bounded-support scope. No blocking
mathematical finding remains in this review unit. The actual nonlinear,
full-original-reader connected estimate BF25 is still open. This verdict
does not establish four-dimensional Yang–Mills existence or a positive
physical continuum mass gap, confer an audit status, or authorize integration
of other units.

The sole mathematical target is
[CHART_BOUNDARY_FOREST_ASTRA.md](CHART_BOUNDARY_FOREST_ASTRA.md), lines 1–564,
SHA256 `c74260a3984330c9393f66c9e7b43068ae4d411d35f593d3241378a96fe3abd8`.
It was read completely before the author's checks or receipts were opened.
The [immutable findings freeze](checks/review_chart_boundary_forest_findings_freeze.json)
was written at `2026-10-30T02:09:25.171173+00:00`, SHA256
`f0d4d3131b5ecc2a91822d82c11136994850fe48112dfc4c82c6b7472a429740`.
The final [coverage and identity record](checks/review_chart_boundary_forest_read_manifest.json)
and [receipt](checks/review_chart_boundary_forest_receipt.json) bind the
read sources, author evidence, and this report.

This is fresh-context, same-family Codex review, separated from authorship.
The coordinator requested Astra/max; this runtime identifies generic GPT-6,
so the dispatch request is not an independently attested backend identity.
No earlier review verdict was used as a mathematical premise. Mathematical
checks were analytic; no numerical experiment, numerical runner, or extra
worker was launched. Bałaban and Dimock remain credited for the localization
and small/large-field architecture.

## What was independently checked

**Actual model and producer match (BF1–BF3, lines 45–88).** Starting from the
original Wilson density and the complete compact normalized kernel, the
tree-Haar change of variables integrates each nonroot gauge variable to one.
There are `4L^4-(L^4-1)=3L^4+1` free links per block and `D=N^2-1` scalar
coordinates per free link. The lift has every paired transporter equal to
its original coarse link, while its double-face plaquettes carry the coarse
plaquette. The lifted two-block brick excludes the far seam at `T=2`.

The kernel Hessian was checked by differentiating its numerator and its
compact normalizer. Along a common contour tangent the normalizer is Haar
invariant; its second variation cancels the corresponding common-path
variance. For unequal tangents this leaves exactly
`kappa[Q*Q+(1-c_N(t))B]`, with the complete spread `B` present. The Haar
expansion `log j_N(a)=-N||a||^2/12+O(a^4)` supplies `N^2/(6u)I` after
rescaling. Six incident plaquettes and four Hessian slots give the
`24 delta_V` curvature error; the traceless insertion paired with `P-I`
gives the `6sqrt(N)delta_V` force. Flat-brick edge recovery retains crossing,
root and harmonic directions. Thus the precision used is the finite-u
coordinate-density Hessian, not the u-stripped tree Hessian.

Substituting `a=sigma x` contributes `sigma^(Dn)`, and introducing the
normalized Gaussian contributes `(2pi)^(Dn/2)det(K)^(-1/2)` outside the
integral. This reproduces BF3 with its vacuum, Haar and kernel factors.
No conditional probability under a different law enters this identity.

The local analytic input was also inspected at its producer: CB9 uses joint
fine/coarse scalar polydiscs and the centered single-normalizer estimate.
STEP55's complex Haar translation and local stationary recentering reduce
that estimate to `|R(W)|<=epsilon s(W)`; the exponentially tilted moment
`E_t[ts exp(epsilon ts)]` is uniformly bounded for fixed small epsilon.
The vacuum remains outside this derivative estimate. This is enough for
the actual PS coefficient majorant, not for a returned-component denominator.
CS15's separate compact cap argument is valid even at a degenerate mean;
it is not inserted into a Gaussian marginal or used to cancel a determinant.

**Gaussian jets and every corner (BF4–BF9, lines 90–182).** Accretivity is
preserved by principal compression. For `y=C_A x`,
`Re(y* C_A^-1 y)=Re(x* C_A* x)` gives the lower bound `c/U^2=a`, and
`||C_A^-1||<=1/c=b`. The determinant modulus is bounded by `b^(D|A|/2)`
using singular values, so normality is unnecessary.

For real x and complex w the mixed quadratic term is at most
`2b||x||||w||`; completing this scalar square gives
`Re((x+w)^T K_A(x+w)) >= a||x||^2/2-c_g||w||^2`.
On independent Cauchy circles the logarithm of the order-k factor is
`log(k!)-k log r+c_g r^2`, minimized at `r^2=k/(2c_g)`.
The remaining inequality is exactly `k!<=k^k`; it yields the stated
`sqrt(k!)`, independently in every scalar coordinate. No dimension-dependent
derivative constant has been hidden in BF6.

The exterior indicator has distributional derivative `+n_j dS_R`.
Testing all later derivatives against the Gaussian gives
`(-1)^(r-|B|)` and one sphere per touched link. In particular the second
derivative at one link tests as `-integral n_i partial_j g`, while two
different touched links give a product of two first-order surface measures.
These checks preserve the signs and the corner terms; no pointwise derivative
of a normal vector has been discarded. Splitting Gaussian decay at `a/8`
then gives BF8–BF9, including empty B and the undifferentiated exterior case.

The derivative statements are in the specified scalar components. A general
link direction can be expanded in those components and its absolute coefficient
sum retained; a unit HS direction costs at most `sqrt(D)` per such expansion.
The covariance application already pays its complete scalar colour sum.
No dimension-free bound for arbitrary unnormalized directions is asserted.

**Normalization and parameter derivatives (BF10–BF13, lines 184–258).**
Direct expansion of `(x+C ell)^T Q(x+C ell)` verifies the sign of the mean
`m=-C ell` and the outside factor `exp(ell^T C ell/2)`. Integrating inactive
coordinates in a normalized Gaussian gives covariance `C_A`, not the inverse
of the principal precision. The Schur-complement calculation, followed by
analytic continuation on the accretive domain, fixes both the determinant
branch and the total mass one. This is precisely why BF9 pays only the active
mean and determinant. The same argument is unavailable with the nonlinear
factor present.

As an independent chain-rule check, the Gaussian characteristic function is
`exp(i p.m-p^T C p/2)`. A differentiated parameter block multiplies it by
`i p.partial_B m-p^T(partial_B C)p/2`. Moving these factors to the insertion
gives BF12 with the positive mean derivative. The labelled product rule
partitions the parameter labels among these blocks and the explicit insertion
derivative, giving BF13 with no extra block factorial. At second order it
contains `D_12 H+D_1 D_2 H+D_1 H_2+D_2 H_1+H_12`. Thus an atom
`C_a s_e s_f` contributes the mixed second-derivative operator as stated.
The formula is used where these parameter derivatives exist as distributions;
the fixed-ball analytic insertions in this note meet that condition. It grants
no arbitrary-history differentiability. Independent-pair differentiation
also does not differentiate the BKAR minimum map.

**The two summed Gaussian theorems (BF14–BF19, lines 260–396).** The forest
mask compression is an isometry compression of `C tensor I`, preserving
the same c and U. With mean fixed, block-diagonal covariance factorizes its
normalized Gaussian. Inclusion-exclusion and the finite forest identity
therefore give the exact gas BF15. The monomial-clock derivation of that
identity was checked, including disconnected graphs and zero exponents;
the smooth extension is needed only near the compact forest locus.

For a fixed labelled tree, removing nonroot leaves charges exactly one
scalar covariance row sum per edge. Its degrees contribute
`product sqrt((degree-1)!)`. If the Prüfer multiplicities are `q_i`, their
sum is `n-2`, and the number of words with those multiplicities is
`(n-2)!/product q_i!`. Hence the larger factorial sum is
`(n-2)! binomial(2n-3,n-1)`. Dividing by `(n-1)!` and summing sizes gives
`q_w[1+sum_(k>=1)lambda^k/k]`, exactly BF17. Singletons, the two-vertex tree,
zero off-diagonal covariance, and high-degree star trees are included.
The colour count and nonroot labelling factorial are both paid.

For BF19 the support-overlap components give a different exact gas:
covariances between different components vanish, and its full support is
the connected union of all H_e. A canonical spanning-tree traversal of length
`2n-2` injectively encodes every connected label set rooted at a specified
link, giving the bound `max(1,Delta)^(2n-2)`. Anchoring by at most J labels
and using `|H_A|<=h|A|` gives the displayed geometric series. This remains
valid on a periodic graph and for degrees zero or one.

The rooted incompatibility-tree recursion needs only positive slack alpha:
the sum over objects incompatible with S is at most `alpha|S|`, so
`|a_S|exp((mu+alpha)|S|)` is the stated supersolution. The breadth-first
partition of connected graphs has the claimed optional-edge intervals;
their alternating sums are zero or unit modulus. The resulting absolutely
convergent connected series exponentiates to the finite gas throughout the
activity scaling disc. Thus both logarithm claims are genuinely summed
results under their respective smallness hypotheses. BF19 does not need
RD's particular two-unit weight convention.

BF17 is nevertheless only a field-set theorem. BF19 separately assumes
bounded, connected full original-reader sets, bounded incidence and overlap
degree, vanishing covariances across disjoint readers, and a common analytic
domain for its Gaussian data. None of those finite-range hypotheses follows
for the full inverse from endpoint decay. The source explicitly preserves
this distinction. Its current `sqrt(D)` scalar-row to link-mean conversion
at line 326 is correct. The earlier missing factor was the author's disclosed
self-correction, not a finding of this reviewer.

**Actual nonlinear envelope and translation (BF20–BF24, lines 398–500).**
PS9's AM–GM bound applies to complex scalar coordinates by absolute values.
On the Cauchy polydisc, `sigma|x_i+z_i|<=r_a/2+sigma h_f`, so the coefficient
radius is at most `2r_a`. The first BF20 condition therefore makes the
quadratic-plus-nonlinear coefficient at most `a/64`. Its norm-square price
is `a||x||^2/32+a D|X|h_f^2/32`. Applying the two force Young inequalities
adds exactly the other `a||x||^2/32`, `a D|X|h_f^2/32`, and
`16||ell||^2/a`, proving BF21. These choices must use the actual a from BF4;
the real PS gamma cannot replace it.

For r labelled derivatives, the first product rule has at most `2^r`
assignments. After retaining the first derivative on each touched cutoff,
the remaining distributional derivatives split between the two smooth factors
in at most another `2^r` ways. This proves the `4^r` pattern count. Cauchy on
f and BF6 on the centered Gaussian have total order
`sum_e(k_e-1_(e in B))`; their factorials are bounded by the displayed
product of link factorials. The combined Gaussian exponent is `-3a||x||^2/16`.
Using `(16pi/a)^(D/2)` for each interior and its stated sphere factor gives
exactly E_X and t_R. Empty-sphere terms remain, and the scalar force bound
gives the explicit D in BF23. This is an unnormalized trace bound, with the
entire component determinant and force cost present.

Finally, let `I(t)=integral_B F(y-tm)dy`. Holomorphy and the real divergence
theorem give `I'(t)=-integral_boundary B (m.n)F(y-tm)dS`. Integrating t fixes
BF24's sign for complex m; the product identity keeps all side/corner choices
and unit translation Jacobian. The swept analytic-chart condition and every
side factor `m_e.n_e` remain necessary. This identity does not move a hard
plaquette or history indicator through a complex contour.

## Preserved limits and literature match

The exact source/data contracts remain separate. SA13 is an actual finite-u
critical branch for real admitted V and complex original Wilson coefficients.
IC12 supplies an actual source-free branch on its explicit complex V domain.
USM's displayed phase is u-stripped. None supplies a silently combined joint
domain or replaces BF10's Gaussian mean with a nonlinear critical point.
The concurrent positive-reader covariance and critical-center candidates were
not read or consumed for this verdict.

[Lohmann, arXiv:1411.1107v1](https://arxiv.org/html/1411.1107v1) was checked
directly at Theorem 1, equations (11)–(12), §2.1.3–§2.1.4, Proposition 3,
and Remarks 2/10. Its product-site cutoff, analytic interaction norm and
stability hypotheses matter. Its weak differentiation leaves one sphere per
touched site. These are correctly credited as methodological antecedents;
the paper does not supply the missing Yang–Mills return estimate here.

BF25 asks for exact connected component integrals with their own reference
normalization on one common source/coarse domain and at a rate actually
available for all original readers. The missing sums include higher parameter
blocks of each reader atom, the phase partitions, complete colour contractions,
E_X, and terms with no sphere. Reader-tree vertices need not correspond to
distinct paid failure witnesses. RD R15–R17 uses the same product reference
and supremum-bounded interaction atoms; it cannot accept a different
interacting probability. The source does not make that substitution.

BF25 is comparable to the connected-chart target in this route, rather than
a routine small remaining check. Arbitrary histories, the unchanged G/Omega
boundaries, outside-chart integration, effective-level closure, continuum
existence and a physical Hamiltonian gap are further obligations. This is
positive bounded support; neither the source nor this review rules out a
mathematical route or claims an exhausted search.

## Disposition and evidence

One independent source-review iteration; zero blocking findings, zero source
repairs and zero skipped evidenced findings. The whole 564-line source is
accepted unchanged at its bounded-support scope. Its claimed mathematical
lemmas are conditional on their displayed contracts; the full physical target
is open. Inputs are the explicit supplied Wilson/kernel/cut model, finite
dimensional analytic and combinatorial constructions, and identified local
producer bounds. There is no empirical fit or new framework primitive.

After the findings freeze, the author receipt, read manifest, correction
record and vocabulary report were read. Their identities and the reversible
correction were checked independently. Mechanical hash/link/fence/whitespace
checks are recorded in the review receipt and do not prove the mathematics.
No numerical script was appropriate for the all-order analytic statements.
No source edit, Git/PR mutation, lock, audit/ledger change, or combined pipeline
was performed by this reviewer. Integration and the combined mechanical gate
belong to the coordinator. No audit-derived status is assigned.

The selected methodology is revision
`01589af3faf806b736c42dc2f3bd625e9edead9f`, including the review-loop and
physics-loop references, together with the owner's [PROCESS_LIGHT](PROCESS_LIGHT.md).
The source-only verdict remains bound to the exact source and consumed inputs
identified above; changed hypotheses or interacting source require affected
review in this same session.

**VERDICT: LAND**
