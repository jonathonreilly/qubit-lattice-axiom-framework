# MIXGFF hostile mathematical review

**Disposition:** no blocking mathematical finding in the reviewed final
manuscript. The conditional separation theorems and the explicit counterexample
are supported at their printed scope. This accepts a research note, not a
Yang–Mills existence, mass-gap, full-WGF-exclusion or retained-status claim.

**Independence:** fresh-context, same-family Codex review from a bounded brief.
I did not author the manuscript. I rebuilt the decisive finite algebra,
spectral limit, flat-test estimate and invariant-mixture argument below.
Shared inputs are the named covariance convention and local reconstruction
library. This is not cross-family review, and the full REC_CONT/REC_LIB proof
was not re-audited. No earlier review verdict was used as mathematical evidence.

**Execution:** no mathematical computational script was run. The author reports
that `nice -n 10 /usr/bin/true` failed with `setpriority: Operation not permitted`;
the supplied guard record says NOT RUN. I honored that block. The checker was
read as source only. No arithmetic PASS count, successful resource preflight,
or actual YM estimate is certified by this review.

## 1. Source binding and coverage

Working folder: `.claude/science/toe-ruleset-20261021/agents/ym4d-proof`.
The local worktree HEAD was
`7329ec3d0bd57a8b07f90221839fca2900242bbe`; the observed local `origin/main`
reference was `01589af3faf806b736c42dc2f3bd625e9edead9f`. No remote fetch,
checkout, commit, audit, ledger or manuscript mutation was performed. Remote
freshness was not established; this review binds the identified local sources.

The complete original 702-line manuscript was read, followed in this same
review session by the author's one-line expansion explicitly setting S0=1,
S1=0 and restricting the nearest-pair distance to n>=2 (final lines 355–359).
The final manuscript has 703 lines. The initial manuscript hash in
`mixgff_review_freeze.sha256` was
`dcfa5540d907e0730c60b4cc4bde5e2c809616e80f9630d79cdb71f7c33578c5`.
The verdict below applies to the final hash in this table.

| Source | Final SHA-256 |
|---|---|
| MIXGFF.md | `6978578119322af1c1161f3282c81055815e5f3cce098d5be78261cfe8e328d3` |
| PROCESS_LIGHT.md | `b61be8245d68af0952d123ed3c1ce602ba948cbe3c5d22c951848f1805e619ab` |
| briefs_q/MIXGFF/AUTHOR.md | `5d2552ad2043bfd21b694a74d03bd8a57db910f71d96984ecdf825d0f58cf959` |
| COMBO.md | `194a32f0547189aa195e2047090026603d5119208b3cac2a0f0c9fb123fdf276` |
| CUMUL.md | `50f337bffacc0e49b7e3bc737609190bd106d8b9210c2ab8f1059745cc1bcfd8` |
| WITNESS.md | `f545b2b544234e9e2a133fb0957bee18cf2c290912897d5a5028ccadc484ecb8` |
| REC_CONT.md | `ac7ac0854fb320f183779f67be136063dfb750ee3f13b869acad10a7ac12a278` |
| REC_LIB.md | `47dd75c7ca3c4f9f1af43139292d1fcfa6774b10f8e6ea2babc05ad67a48e29a` |
| checks/mixgff_criteria.md | `96e37b7c7920785bbbd14d65483404d3434551cd93af6d76b2392b14bb1d72c6` |
| checks/mixgff_exact.py | `1f5bd6818a79aadc2436a393cd8891dfbecc220ceb7fe03f92ae7019faba4049` |
| checks/mixgff_guard_status.txt | `28a26895777ec32587f397888aac02314d9235da8a742142c1ba3fc97c8a9c8d` |
| checks/mixgff_review_freeze.sha256 | `4a4daf46e8e48147c561bf1f221dd6798653dff4646202917d10e1f1eae08e4b` |

The initial freeze's criteria hash was
`ccfd571750e762a23e07a7fac65f1faae913e399822d8dc185bcd863ffcb7ef7`.
The author subsequently specified the two covariance vectors, weights and
common means in item 1 and reports doing so before creating the checker. Both
criteria revisions were read. The freeze remains historical; it must not be
misrepresented as the current criteria identity or as a run receipt.

Exact dependency passages inspected were COMBO §§1–2 and §§3–4 (lines 28–198,
239–427); WITNESS §§1–2 (47–206); CUMUL §§1–3 (20–285); REC_CONT §§1,11
(17–70,982–1018); and REC_LIB §§1–3,18 (112–263,1080–1121). These provide
the field/test/normalization contract, canonical comparator, free curvature
normalization, ordered-domain determination, spatial OS unitaries and exact
conditional reconstruction interface. These are explicit premises, not blanket
endorsement of every claim in those longer files.

Repository AGENTS.md and SCIENCE_WORKFLOW.md were read, with hashes
`febf3a1aaabd4bd13f87b052ab5eacb75f46be535985425bae4d400f509bc7d0` and
`71cab17ea2d5ec892b5d9dbefd608c0d51e77ea398a62f33679736510d9f63d3`.
I applied the local physics-claim-reviewer skill and its focused-review/proof
obligation instructions at this local snapshot. The explicit assignment's
no-commit/no-ledger and same-family review limits control this deliverable.

## 2. Independently rebuilt load-bearing steps

### A. Gaussian mixtures and the actual domain of a sign test

With a common component mean, subtract that deterministic mean first. At four
distinct slots, conditional Wick expansion gives
`E_nu[C12 C34+C13 C24+C14 C23]`. The mixture's disconnected subtraction is
`E[C12]E[C34]+E[C13]E[C24]+E[C14]E[C23]`. Their difference is precisely (3).
It is not a sum of variances at a general four-test tuple. For a covariance
scale V, each term factors and the result is Var(V) times the three pairing
products. This needs no repeated-e product in the flat algebra.

The proposed two-point law for V has E[V]=1 and E[V²]=1+v, so its fourth
cumulant ratio varies through all positive values at a fixed positive tuple
while its covariance stays fixed. For the random constant T=±1,
`kappa4(T)=E[T^4]-3E[T^2]^2=1-3=-2`; independence adds this to the Gaussian's
zero fourth cumulant. Its extra covariance contributes only lambda^8 to V_m.
Thus both examples genuinely evade the stated sign/single-ratio proposals.
The single-coordinate formulas are correctly labelled algebra controls,
not admissible repeated-field moment tests (MIXGFF 86–134).

The high-mass density s²/log²(e+s) has the required positive atomic
approximation. The heat integral without the log is
`integral_0^infinity s² G_s(r) ds = 192/(pi² r^8)`:
first integrate s to obtain 2/t³, then substitute r²/(4t).
Gaussian n-point terms contain at most n/2 such edges and thus at most
delta^(-4n). The flat-test argument in part D therefore also covers the
bounded shifts and scales used here. These are admissible hierarchy examples,
not only finite random-coordinate examples.

### B. Scalar quadratic rigidity and the Maxwell geometry gap

For `e=:psi^T A psi:` with covariance delta_ab H, normal ordering removes
self-loops. At n=2 there are two contractions, giving
`Cij=2 tr(A²) H_ij²`. A connected graph at n>=3 has degree two at each vertex,
hence is a single cycle. For a fixed undirected cycle each vertex independently
assigns its labelled two legs to the two neighbors, giving 2^n pairings.
The species sum is tr(A^n). There are three undirected four-cycles, each
with 16 pairings. This reconstructs (5) without using its expected constants.

Because H_ij>0, each square-root product in D equals
`4 tr(A²)^2 product_cycle H_ij`. Dividing gives
`R=4 tr(A^4)/tr(A²)^2` for every configuration. The hypotheses that H is one
common scalar kernel and that the polynomial is a finite, derivative-free
quadratic form are essential. Unequal kernels, tensor numerators, mixed
degrees and derivatives are not covered. The manuscript retains all these
restrictions explicitly (69–72,136–165,220–233).

Independently differentiating D(z)=1/(4pi²|z|²) gives
`pi² d_mu d_rho D=-delta_mu,rho/(2r^4)+2z_mu z_rho/r^6`.
Taking the four curvature terms with the derivative at the second insertion
of opposite sign gives `G=(Lambda² H_z)/(pi²r^4)`, where
`H_z=I-2zz^T/r²`. The fourth-order z terms in the minors cancel. On a time
axis this matrix has three negative and three positive eigenvalues, verifying
both the sign convention and tr(J²)=6. With the CUMUL clover convention the
field is q_u=u^-1 sum_(a,I):F_I^a F_I^a:, so
`C=12d/(pi^4u²r^8)` and `K4=16d/(pi^8u^4) sum_c tr(J_c) w_c`.
The quotient is therefore the w-weighted trace average divided by 9d.

Here is a separate two-dimensional multiplication for geometry B. In cycle
order 1234,1243,1324 the products of the ordinary plane reflections are

```text
[[ 4/5, -3/5], [ 3/5, 4/5]],
[[   0,   -1], [   1,   0]],
[[ 3/5,  4/5], [-4/5, 3/5]].
```

The action on R4 is this plane rotation plus identity on the perpendicular
plane. Its exterior square contains two fixed area forms and two rotation
copies, so its trace is 2+4cos(phi). This yields 26/5, 2 and 22/5.
The squared edge-length products are respectively 40, 8 and 20, so the
r^-4 weights are 1/1600,1/64,1/400. Their sum is 3/160 and their
trace-weighted sum is 91/2000. Thus the average is 182/75. Geometry A has
average 6. Dividing their difference by 9d gives 268/(675d), as printed.
This calculation is a written exact derivation; it is not a checker run.

Point values are not substituted for arbitrary smeared values. The manuscript
uses the ordered analytic representative furnished by ALG/REC, takes the
continuum limit at each fixed bump/scale, then shrinks the separated bumps.
Products of separately smeared H values would fail the claimed identity;
the note explicitly excludes that operation. The two geometries have strictly
ordered positive times after the given rotation/translation. GEO is a new
actual-hierarchy convergence requirement and is not inferred from CUMUL's
one collinear smeared coefficient. Positive limiting denominators justify
division, and the stated half-gap error bound is sufficient (225–252).

### C. The logarithmic, clustering comparator and all collinear cumulants

The heat-kernel scaling is
`G_s(lambda r)=lambda^-2 G_(lambda²s)(r)`. After sigma=lambda²s, the
rescaled spectral integrand is
`[ell_lambda/log(e+sigma/lambda²)] G_sigma(r)` on sigma>=lambda².
On [lambda²,lambda] its integral is at most
`lambda ell_lambda G_0(r_min)`, which vanishes. On [lambda,infinity) the
bracket is at most 2, tends to 1 at fixed sigma>0, and is dominated by
`2G_sigma(r_min)`, integrable over sigma. Taking the supremum over a compact
radial interval gives the same bound. Integrating sigma in the heat formula
then gives `integral G_sigma(r)d sigma=1/(pi²r^4)`. This proves (13),
including uniformity needed for the fixed separated smears. The alpha>0
variant uses the same argument with ell_lambda^alpha and bound 2^alpha.

For one pair e=2psi chi, direct independent-species contraction gives
`C=4H²` and `K4=32 sum_c product_c H`. Summing p independent pairs multiplies
connected functions by p. For p=3d, the covariance has a strictly positive
lambda^-8 ell_lambda^-2 leading term on the COMBO reflected smears, and
every term of the fixed fourth cumulant is positive. Hence both AF clauses
and nonzero K4 hold.

The same quadratic form has p blocks with eigenvalues +1,-1. Its even power
traces are 2p=6d, and its odd traces are zero. On any collinear configuration
every Maxwell J is the same involution, so its color-summed cycle traces are
exactly the same. The already counted cycle multiplicities therefore match
each connected n-point leading kernel (n>=2); the one-point mean is zero.
Moment matching follows by partitions. This matches the free reference with
u=ell_lambda. It does not identify that parameter with the actual YM running
coupling, nor assert equality at finite scale, on noncollinear data, or for
fixed-width smear integrals. The explicit normalization and chosen p are
counterexample parameters, not derived YM data (279–286,330–342).

For clustering, integrating s>=1 first bounds H by
`(16pi²)^-1 integral t^-3 exp[-r²/(4t)-t]dt`.
Split the exponent into two copies of `r²/(8t)+t/2`. One copy is at least
r/2 by AM–GM, and integration of the remaining r²/(8t) term gives
`4e^(-r/2)/(pi²r^4)`. Every Wick term joining two compact separated blocks
contains a cross-block edge, which then vanishes uniformly when the spatial
separation grows. Terms without such edges factor exactly. This proves the
ordinary block clustering used to obtain CL2. Thus even adding clustering
does not remove this arbitrary-spectral composite.

### D. Flat-test growth, positivity and composite realization

The atomic approximation uses right-endpoint masses, so monotonicity of G_s
gives H_L<=H and pointwise convergence at nonzero separation. The constants
in the upper bound H_L<=1/(pi²r^4) are independent of the increasing number
of mass atoms. All composite Wick kernels have at most n edges, and
`(2n-1)!!=(2n)!/(2^n n!)<=2^n n!`. Finite species/field coefficients add
only a constant to the n. This gives (15), uniformly in L.

For delta<1, project a nearest pair onto its coincidence plane, a displacement
of O(delta) involving only two slots. All Taylor jets of F vanish there.
Taylor order 4n supplies delta^(4n)/(4n)! and at most a constant^n from
directional derivatives and weight comparison. The 9n seminorm controls
these derivatives with more than the needed decay. Moreover

```text
(1+sum_i |x_i|²)^(-5n/2)
    <= product_i (1+|x_i|²)^(-5/2),
```

since each factor 1+|x_i|² is at most 1+sum_i|x_i|². The right-hand side
is integrable over R^(4n) with an integral of the form constant^n. For
delta>=1 the zeroth derivative suffices. Hence
`|S_n,L(F)|<=D^n n! ||F||_(9n),1<=exp(D)(n!)² ||F||_(9n),1`.
The last inequality follows from D^n/n!<=exp(D). This checks the exact
single-triple ALG bound, not a separate estimate at each n. The final
S0/S1 clarification avoids invoking a nearest pair where none exists.

Each atomic scalar reflected covariance has the explicitly positive Laplace
square in (383–384). Gaussian symmetric tensor Gram forms and restriction
to polynomial vectors preserve positivity. An admitted OS quadratic form
contains only finitely many separated moments, so the dominated limits above
preserve it. Covariance, symmetry, reality and normalization pass as well.
There is no assumption that the unsubtracted Euclidean spectral integral at
coincidence is a random distribution covariance.

For the realization claim, retain the Gaussian labels and the composite label
jointly. Mixed words still have at most two legs per insertion, so the same
estimate applies with a larger constant. Split psi and chi within each
composite insertion at a positive-time displacement smaller than the fixed
inter-insertion gaps. Unlike-species self-contractions vanish; all remaining
contractions within norms and mixed inner products stay separated, including
the reflected pairs. Their limits make the squared difference of split and
composite OS vectors tend to zero. Ordered compact-test density then gives
the claimed composite cyclic subspace of the joint Gaussian space. This
establishes the relevant realization rather than merely its two-point kernel.
The use of REC for continuation/reconstruction remains an explicit local
dependency with its full hypotheses.

### E. CL2, arbitrary admissible mixtures and the finite Q extension

For each invariant component, spatial translation preserves the OS form,
commutes with reflection and has an inverse, so it acts unitarily. Continuity
on test vectors and density give strong continuity. Cube averages M_R are
contractions. On `(I-U(b))w` the norm is bounded by the relative measure of
the cube's symmetric difference with its translate, times ||w||, hence tends
to zero. The orthogonal complement of the span of such differences is exactly
the invariant subspace. This proves M_R tends strongly to its projection E,
without assuming unique vacuum or clustering in the component.

For v=[P], Omega is invariant and normalized, so
`||Ev||²=|S_t(P)|²+||Ev-S_t(P)Omega||²`.
The prescribed integrability of S_t(Theta P P)=||v||² dominates the averaged
matrix elements, permits the component integral to pass through the limit,
and also bounds |S_t(P)|². The elementary variance decomposition of
`integral |S_t(P)|²-|integral S_t(P)|²` then gives exactly (18). Both residual
terms are nonnegative. CL2 forces the component expectation of P to agree
with the barycenter's almost surely.

A countable determining family is essential: intersecting its full-measure
sets produces one set valid for every selected degree-one/two test. Individual
continuity extends agreement to all compact ordered tests. At an arbitrary
off-diagonal pair choose a rotation making its time difference nonzero,
translate to positive times, and use a local partition of unity; compact
off-diagonal tests are dense in E2 by the flat cutoff argument. Thus the
components have the same first moment and full separated covariance. No
uniform component spectral envelope, full extremality or hidden removal of
zero modes is needed. Degree-one clustering alone would not fix varying
component covariances; the four-point degree-two OS tests are necessary to
this argument.

A Gaussian hierarchy is fixed by these first two moments, so a barycenter
entirely in G is itself Gaussian and has K4=0. For an F1 component, the radial
finite propagator/Wick expansion has a first nonzero term
`c r^-gamma |log r|^j` with integer gamma, j>=0 and c>0. The displayed ODE
recurrence follows by applying `z²d²-zd-z²` to z^(2n)(a_n+b_n log z);
its coefficients are 4n(n-1) and 4n-2. Its convergent power/log structure
and finite differentiation/product operations cannot produce inverse logs.
RP fixes the leading sign. Positive reflected smearing gives either failure
of V_m->0 when gamma>=8, or lambda_m^-1/2 V_m->0 when gamma<=7. The null
case fails the AF lower clause. Equality of each component covariance with
S's therefore rules out every F1 component on the common full-measure set.
The remaining G components cannot have nonzero K4. This proves (19),(20)
at the printed arbitrary-admissible-barycenter quantifier.

For a finite F1/G/Q mixture, CL2 again fixes the component means/covariance
and AF removes F1. After the common deterministic centering, the fourth
cumulant is affine in the mixture because the disconnected second-moment
subtractions are common. Finite summation also commutes with the point limits.
Each Q component contributes r_t D(C;Z), with configuration-independent r_t;
each Gaussian contributes zero. The mixture ratio is constant. GEO's
nonzero A–B gap contradicts it. The restriction to finite mixtures here
avoids an unproved exchange with unbounded component point limits (519–531).

## 3. Findings, limits and brief coverage

No material correction is required in the final manuscript. The author's
n=0,1 clarification was inspected in this same session and is sound.
The following limits are binding, and the manuscript states them:

1. The exclusion is on the same named scalar e hierarchy with fixed Z(a)=1,
   vacuum and spacetime action. It is not a classification of unmarked free
   nets or non-invariant mixture decompositions.
2. CL2 is a family of spatial Cesaro two-/four-point block conditions on one
   continuum hierarchy. It is not two-point clustering alone or automatic
   vacuum extremality. The original-law producer must take the continuum
   limit at fixed R, then R to infinity; a torus plateau or R(j) diagonal
   limit is insufficient (533–559).
3. GEO concerns the same actual field and common running normalization at
   noncollinear configurations. The free curvature coefficient alone proves
   neither GEO nor its normalization relative to the Wilson observable.
   No actual YM CL2/GEO/existence estimate is supplied.
4. The logarithmic example is genuinely in the restricted common-kernel
   quadratic class and defeats W plus clustering and all collinear leading
   diagnostics. Geometry B distinguishes it, but does not classify WGF with
   arbitrary spectra, tensors, derivatives or mixed degrees.
5. The recommendation is an obligation-count judgment, explicitly not a
   theorem of optimality or a claim that infrared clustering is easy. CL2
   is strictly weaker than a positive quantitative gap requirement: the
   massless canonical scalar already has the necessary decaying block
   contractions, without a mass gap.

The author brief's three candidate directions are all addressed: (a) valid
mixture identities, sign/single-ratio counterexamples and a restricted working
geometric ratio; (b) a positive-spectrum logarithmic composite counterexample,
including admissibility and clustering; (c) a proven invariant-mixture
variance lemma with the exact extra YM condition. Full arbitrary-WGF
separation is honestly OPEN. The N1–N8 discussion preserves live routes and
does not upgrade these counterexamples into a universal impossibility claim.
Balaban/Dimock credit is present. Literature links are attribution; no
literature theorem or remembered assertion was needed in the derivations
verified here.

## 4. Prospective checker: source review only

The full checker source was read, then its revised dropped-cycle control was
inspected. The revision removes one connected numerator term while retaining
the denominator from all two-point data, which is the appropriate mutation.

Its Gaussian moment recursion and full set-partition cumulant calculation
provide a distinct finite-algebra route to (3); the two curvature routines
use Hessians and exterior-square minors separately; its pairing enumeration
builds connected graphs from labelled legs. The code uses exact Fraction
arithmetic, and the geometry/ratio targets have the independent written
derivations above. The registered controls address a numerator replacement,
an omitted cycle and an incorrect cycle multiplicity. None is evidence for
an infinite-dimensional limit or a YM matching estimate.

By source inspection, numerical work is behind niceness/thread checks, an
800 MiB address-space limit, an exclusive lock and load/native-memory checks,
with checks between groups. Existing result/receipt files are not implicitly
overwritten. I did not validate runtime behavior, resource reporting or any
check output. Source inspection is not a successful execution receipt; all
numerical checks remain NOT RUN. The written proofs carry the present verdict
and do not rely on an imagined prospective PASS.

Only this reviewer file was created by this reviewer. No editable prompt,
manuscript, existing source, audit or ledger file was changed.

VERDICT: LAND
