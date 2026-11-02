# Independent review of the covariant normalized soft-step background

**Source-only disposition: confirmed with bounded claims.** The reviewed
[COVARIANT_SOFT_BACKGROUND_ASTRA.md](COVARIANT_SOFT_BACKGROUND_ASTRA.md) has
SHA256 `87119008ccf754022b5da0836bb1bea8e0455a5535e589a4207ee49193682b74`.
Its complete 568-line argument and necessary contracts were read. The original
author packet is preserved at coordinator commit
`a63ade893a7f76b9ee1925170545bf7489ad0f18`; its
[receipt](checks/covariant_soft_background_receipt.json), SHA256
`5613420d87a16c573b2848cf43d2385cad7961dac3f0d0379fd5ce975d97e5df`, binds
26 files, all verified. No material source defect or required source repair
was found. This is one scoped scientific review, not whole-PR approval,
retained status, an audit verdict, or confirmation of a full proof.

Full four-dimensional Yang–Mills existence and the physical continuum mass
gap remain **OPEN**. The result is an actual finite-u smooth coordinate-density
critical point and its Gaussian reference for u>=1 on a specified, very small coarse
curvature domain. It does not establish an interacting covariance, an
integrated source logarithm, or fixed-V concentration.

## Review boundary and independence

This is same-family, fresh-context review: Codex reviewing Codex, separated
from authorship. The requested configuration was `gpt-6-astra`, maximum
reasoning; backend identity was not independently observable. I wrote no
author source, shared summary, git change or audit output. The coordinator
owns PR #10114, locks, publication bindings, current-main preservation and
combined integration validation.

The [criteria](checks/review_covariant_background_criteria.md), SHA256
`7a5cbd1e10cd9d02986dd3b209cf1670faef4305a84712d2d59d3cd16823c725`, were
frozen before independent implementation and before reading the target or
its author checkers. The coordinator's source summary and the predecessor
were already exposed; that limit is recorded. The complete target was read
only after the author supplied its frozen source and receipt identities.

The [independent freeze](checks/review_covariant_background_independent_freeze.json),
SHA256 `00090d20ca7255d805996514b97d1992230a50a294b29805678ab60984130aa8`,
binds the independent code, outputs, preserved failures and
[analytical assessment](checks/review_covariant_background_analytic_01.md)
before author-checker inspection. Later author reproduction and mutation
runs are separately identified. The [read manifest](checks/review_covariant_background_read_manifest.json)
records actual coverage; a whole-file hash is not a claim of whole-file reading.

Installed physics-loop/review-loop entry points and the applicable portable
procedures were read at coordinator-supplied current-main revision
`ca2bc7ddf64790da96cd43d42017d000fbfe4808`. The local `origin/main` object
matched at entry; stale local main was not used. The current lane was already
running when [PROCESS_LIGHT.md](PROCESS_LIGHT.md) was adopted and is allowed
to finish its existing format. No external theorem is silently used as the
missing source-return estimate.

## Mathematical assessment

**Exact lift, local quotient and all-V principal gap, CB1–CB6.** Every actual
centered paired contour crosses its designated coarse face exactly once;
both root legs are internal. Its lift transporter therefore equals V_c for
every coarse configuration. A fine plaquette is nontrivial only at a double
face, with the displayed ordered coarse plaquette and L^2 copies. This also
fixes the Wilson vacuum factor without integrating V.

The pinned tree quotient is a triangular product of probability-Haar
translations and inversions. It leaves `(3L^4+1)T^4` free links with no
nonconstant FP determinant. Root and holonomy directions remain among them.
On a lifted two-block brick, the gauge I on its first block and V_c on its
second makes every included link I. The far periodic seam at T=2 is outside
this rectangle and is not generally trivialized. Thus the identity recovery
proof transfers by norm-one adjoint transports without a curvature error on
its actual filling supports.

The internal-edge contribution costs at most `4L^4 b_L^2`; crossing links
cost `2L^3` for each Q term and `2L^3*8 b_L^2` for the curvature allocation.
This gives exactly `C_F=4L^3(L+4)b_L^2`, `C_Q=2L^3` and the stated positive a,
with no volume factor. All other D_V plaquettes contribute nonnegatively.
This proves the principal gap for arbitrary V; the small-curvature condition
enters the actual Wilson Hessian comparison, not this local recovery lemma.

**Actual normalized finite-u Hessian, CB7–CB8.** For one contour family, let
q be the mean transported tangent and v its mean squared spread. The
numerator Hessian is `(t/N)(||q||^2+v)`. Differentiating the actual normalizer,
then using Haar invariance on a single unitary tangent, gives `-(t/N)c_N v`.
After the N/u rescaling the contribution is exactly
`kappa[||q||^2+(1-c_N)v]`. The kernel's first derivative at the lift is zero.
The finite-u spread is therefore present, including in zero-Q directions.
The exponential Jacobian gives `log j_N=-N||a||^2/12+O(||a||^4)`, so its
normalized Hessian is `N^2/(6u)I`.

For the Wilson action, write a plaquette variation as
`exp(B1)...exp(B4)P0`. Its second derivative has `sum Bi^2` and twice the
ordered `Bi Bj` terms. Replacing P0 by I yields `||sum Bi||^2`. A pair of
HS-unit colour directions has error at most `||P0-I||op`; four Hessian
entries per plaquette and six incident plaquettes per edge yield both block
row and column bounds `24 delta_V`. The force per incident plaquette is at
most `sqrt(N)delta_V`. This establishes the exact CB8 identity and force
bound with the stated counting/HS conventions. The nonstationary lift is
not asserted to be a critical point.

**Uniform nonlinear critical point, CB9–CB15.** The single-normalizer input
is the centered bounded analytic logarithm of STEP55 PR/NZ with S5–S7 and
CODEX_REVIEW_STEP R6, for fixed real t>0. The argument does not vary t in a
complex domain and does not use an integrated returned denominator. All
complex derivatives are of explicit local continuations; no complex
conjugation is treated as holomorphic. Local path length and the polar
recentering control its fixed complex chart around each arbitrary unitary V.
The constants count local slots and incident terms, not total volume.

The third-derivative bound is conservative: `48 Mloc/q^3` per scalar
component, at most 15 incident terms, nloc^2 index pairs and D colour rows
give the stated C. Weighted resolvent conjugation gives the inverse point
norm `2/(gamma+t)`. Summing all periodic images and m0 free links gives R.
Its entries are D-dimensional HS operator blocks, so this row sum does not
need an extra D; scalar traces and determinants still count all colours.

The chosen r satisfies `RCr<=1/4` and `Cr<=gamma/4`; the force satisfies
`RG delta_V<=r/8`. These are sufficient for self-mapping and contraction,
for `||a_u||<=r/4`, and independently for the real Hessian gap
`3gamma/4`. The coarse-data and source extensions use those same local
holomorphic estimates. The source perturbation adds inverse-weighted
Hessian norm at most 1/4 and force at most `G delta_V rho`, giving the
stated source contraction and real gap.

The tree/finite-u comparison has the required extra delta_V: the omitted
centered-normalizer and Haar corrections have gradient zero at a=0 and
Hessian bounded by `C_diff/u`. Their force at a_u is consequently bounded
by `(C_diff/u)||a_u||`. The perturbed inverse row norm is at most 2R, giving
`4R^2 G C_diff delta_V/u`. An untracked fixed-volume implicit-function
radius is not substituted for this argument. The explicit admissible
curvature bound is extremely conservative; the finite diagnostic examples
are not represented as satisfying it.

**Localization and exact integral, CB16–CB20.** K_* remains finite-range,
colour-coupled and positive. The resolvent square-root integral gives point
prefactor `2/sqrt(gamma_*)`, and the complete periodic-image sum gives the
weighted row/column factor in CB16. Differentiation of the critical equation
produces an actual coarse-data derivative: its forcing occupies at most
18m0 free-link locations, each bounded by C. The CT inverse bound therefore
gives the CB18 prefactor and distance to that support. No higher connected
activity estimate follows from this first derivative.

The shift is additive in the original Lebesgue chart. With
`sigma^2=N/u`, the quadratic term of L is exactly K_*, as required for the
standard Gaussian change. The prefactor keeps the actual w0(U*,V), one h_N
and j_N(a_u) per free link, the full `D m0 T^4` scaling/mode count and the
single full-colour determinant to power -1/2. No scalar-colour tensor
assumption is made. Local Taylor subtractions contain their individual
linear terms; only their full sum cancels by stationarity. Hard cuts and
the coordinate cutoff remain inside the expectation.

Duhamel's unitary exponential bound gives plaquette displacement at most
`4 sigma p`. Hence `s(U_p)<= (Delta_bg+4 sigma p)^2/2`, which proves CB20
with the stated sufficient constant. The source vacuum, linear and
quadratic orders are respectively `u rho Delta_bg^2`,
`sqrt(u) rho Delta_bg p`, and `rho p^2`. Stationarity of the total density
cannot cancel a separately labelled Wilson source.

**Strong-good interface and complement, CB21–CB24.** The nonabelian combing
argument expresses path differences as ordered products of conjugated
plaquette holonomies, using at most width-sum times word-length plaquettes.
It gives the displayed relative-link bounds on the actual lifted boxes.
The L-by-L fine square and four coarse replacements give
`delta_V<=L^2 delta_f+4eta`. The small principal eigenangles, HS radius and
`r_ch<pi/sqrt(N)` force a traceless logarithm and exclude repeated
exponential preimages. Thus the whole stated strong-good event enters the
relative chart, including large coarse holonomies.

This is a domain implication. The original interior-only cut supplies
neither its all-fine-plaquette hypothesis nor its mismatch hypothesis. The
smooth critical point is not asserted to belong to this hard event; the
proof supplies no fixed-V nonemptiness, typicality or concentration. The
entire complementary integral and all dirty/correlated histories remain.
Sea7/Sea11 are used only on their integrated coarse domain, never as fixed-V
estimates. Arbitrary holes and frozen collars are explicitly outside scope.

## Evidence, controls and failures

The independent [matrix geometry run](checks/review_covariant_background_geometry_01.stdout.json)
passes 16/16 predicates and 5/5 rejection controls. It covers every fine
plaquette on T=2 and T=3, 31,104 actual centered paired words, the lifted
brick trivialization, the far-seam failure, a random pinned gauge quotient,
large flat holonomies and a curved strong-good sample. It also rejects
interior-only substitution and an unguarded SU(3) principal-log convention.
These finite tests do not prove the general-L/all-volume statements.

The independent density implementation uses torch's complex-matrix
exponential/autodifferentiation, separately assembled NumPy transported
variations, direct Haar quadrature, and root-eigenvalue Jacobian checks.
It imports no author code. At a noncommuting background the complete
finite-u Hessian agrees between these routes at about `2e-15`. A zero-Q
vector has nonzero spread. The sampled principal 732-coordinate precision
has minimum about `.02827`; that observation does not replace CB6's much
smaller proven lower bound. The measured Wilson error block-row norm is
about `3.9523`, below its `11.7429` bound.

The [first density run](checks/review_covariant_background_density_01.stdout.txt)
reported 26/30 predicates and 15/16 controls. Four second differences at
step 1e-4 suffered cancellation, missing the declared absolute 2e-5 threshold
by roughly 1.5e-6–6.5e-6, even though autodiff and the independent transported
formula agreed at machine precision. One vacuum omission fixture was
smaller than its declared 1e-6 sensitivity. Both failures remain in their
original source/stdout/stderr; they are not reported as a passing run.

The [affected confirmation](checks/review_covariant_background_density_affected_02.stdout.json)
passes 21/21 predicates and 9/9 controls. It uses differences at .002 and
.001 with the same 2e-5 tolerance, and a larger-u vacuum fixture with the
same 1e-6 detection threshold. Its six second differences agree within
about 1e-6. The successful critical-point/source results were reused rather
than re-executed. This overlapping run is not added to the original counts;
its [failure/repair record](checks/review_covariant_background_density_failure_01.json)
states the exact changes. No tolerance was relaxed.

The original run's full 732-coordinate critical residuals are
`3e-8`–`8e-8`, for the tree phase and u=8,32,128 in the period-one block
sector. Translation symmetry makes sector stationarity full-torus
stationarity at these periodic data; arbitrary inhomogeneous volumes rely
on the written proof. The finite-u/tree difference decreases in this
sequence. At the u=32 critical point, one Wilson plaquette still has source
gradient norm about `.001166`, while the total-density residual is about
`3e-8`. Its measured canonical source vacuum/linear/quadratic scaling is
4/2/1 when u is multiplied by four at the fixed point. Algebraic Gaussian
normalization controls detect omitted Haar, center Jacobian, vacuum, scale
and determinant factors; they are not a full hard-cut quadrature.

Only after the independent freeze did I read both complete author checkers
and inspect the original warning and complete affected code deltas. The
[author replay](checks/review_covariant_background_author_replay.json)
reproduces 49/49 main predicates, 16/16 T=2 geometry and 16/16 T=3 geometry,
all exit zero with empty stderr. These are reproductions, not additional
independent implementations. The preserved LU determinant warnings are
replaced by Cholesky plus an eigenvalue log-sum check; the source/criteria
delta does not loosen a scientific threshold.

Six actual [author-code mutation runs](checks/review_covariant_background_author_mutations_01.json)
all fail for the intended reason: omitted spread, Haar gradient, normalizer
gradient or Wilson error, discarded adjoint transport, and a wrong crossing
assignment. The first five fail their finite-u Hessian assertions; the last
fails the actual contour/plaquette/brick geometry. Their copied mutated
sources and raw outputs remain in the review namespace and are not current
author executables.

## Premises, prior art and final scope

The four-dimensional Wilson law, SU(N), probability Haar, positive compact
kappa range, odd block side, torus, paired arithmetic means, HS metric,
counting adjoints and specified coarse-curvature/chart domain are explicit
model/convention inputs. No empirical or fitted values appear. The current
axiom/primitive registry was read; no dynamics or physical observable was
derived from it. The only non-elementary analytic contract consumed here is
the specifically read local single-normalizer proof from STEP55 and its
corrections, already matched to the predecessor's actual model.

The predecessor supplies the tree quotient, identity finite-u calculation
and Gaussian/resolvent construction. This source adds their covariant
flat-brick extension, the uniform actual coordinate-density shift, its
first coarse-data locality and the strong-good chart interface. The
[Dimock axial-gauge paper](https://arxiv.org/abs/1410.2798v3), §§3.7–3.10,
was checked in its versioned text: its C coordinates solve hard abelian
constraints, including removal of central links. That is not this finite
soft SU(N) precision. The [large-field paper](https://arxiv.org/abs/1212.5562v2),
Appendix F, requires ultralocal probability variables and local small
interactions on their support. Whitening does not establish those hypotheses
for the pulled-back hard cuts. These papers are credited comparisons;
they supply no missing interacting theorem here. External PDFs were read
from verified caches and are not committed.

The scientific proof obligations close at the bounded CB1–CB24 scope just
described, with the stated analytic predecessor input. Code/formulas and
claim boundaries are confirmed at that scope; imports are disclosed; no
retention is claimed. No-go and naming-convention lenses are inapplicable:
there is no route-exhaustion or impossibility claim. Audit and whole-PR
compatibility remain coordinator-owned; this review neither writes verdicts
nor performs a pipeline/landing operation. Focused compile, vocabulary,
relative-link and whitespace checks are recorded in the review receipt.

There are zero unresolved material findings in this source unit. The next
scientific obligation is the convergent, source-labelled local expansion of
the exact weighted Gaussian expectation with its hard cuts, vacuum/source
costs and full determinant counts, joined to the actual complementary
histories. That obligation remains separate from all-depth RG, continuum
existence and the physical Hamiltonian gap. The disposition below applies
only to this frozen bounded producer.

VERDICT: LAND
