# Independent review of the normalized soft-step Gaussian producer

**Source-only disposition: confirmed with bounded claims after one chart-domain
repair.** The final source is
[SOFT_FLUCTUATION_COVARIANCE_ASTRA.md](SOFT_FLUCTUATION_COVARIANCE_ASTRA.md),
SHA256 `327d033b22281f5f727c018ccb9b1d23d8f7d131bd3633602d6655a9b3de2403`.
This confirms its identity-background Gaussian reference and restricted
integral on the repaired domain. It is not whole-PR approval, an audit verdict,
retained status, a statement about the interacting conditional covariance, or
an existence or physical-gap theorem. Full four-dimensional Yang–Mills
existence and the physical continuum mass gap both remain **OPEN**.

The original source SHA256 was
`7b579f43ff7c04dd922f652c76cb3a1b9a4add3d64d0bf29d6abf0e04f038296`, preserved
at coordinator commit `86400dbc2ad09b0cf9c6bd9453a8e788a20f46cd` and in the
[original-source recovery copy](checks/review_soft_fluctuation_original_source.md).
The original author receipt remains bound to that original source; it has not
been restamped as evidence for the repaired source. The coordinator's
[repair receipt](checks/full_proof_soft_chart_fix.json) and this review supply
the explicit before/after relationship.

## Review contract and independence

The [criteria](checks/review_soft_fluctuation_criteria.md), SHA256
`c5d22fe40d51ac8baf0e15b906ac7391a9a0a94b803acc58200a23d4b7c89dce`, were
written before independent mathematical implementation and before reading
an author checker. I read the complete target argument and its actually
consumed mathematical contracts. The [read manifest](checks/review_soft_fluctuation_read_manifest.json)
records exact ranges and limits; full file hashes do not imply full reading
where only ranges are reported. A concurrent coordinator update to the front
status checkpoint of PROOF.md shifted the consumed proof ranges by17 lines;
its entire delta was inspected and those mathematical bytes verified unchanged.

The requested configuration was `gpt-6-astra`, maximum reasoning, with a
fresh context. Independently observable backend model metadata was not
provided. This is separation from authorship with independent derivations
and implementation, not a claim of cross-family review. I did not author
or edit the target source, its mathematical inputs, author checkers, shared
summaries, git state, or audit state. The coordinator authored the repair.
The independent evidence was [frozen](checks/review_soft_fluctuation_independent_freeze.json)
before author-checker inspection. Author reproduction is reported separately.

Methodology uses the installed review-loop and physics-loop skills together
with the portable procedures at the coordinator-fetched immutable current-main
revision `ca2bc7ddf64790da96cd43d42017d000fbfe4808`. Local main was not used as
authority. Main's freshness was coordinator-supplied and the same local
`origin/main` object was verified. This delegated unit supplies scientific
source confirmation; the coordinator owns preservation against actual main,
PR provenance, combined validation, publication bindings, and integration.
No new premise, primitive, physical action, or observed parameter was derived
from the framework registry.

## Material finding and affected confirmation

**Principal-log chart domain — fixed.** Original lines 363–367 required only
an HS radius below the injectivity radius and described the event by small
principal logarithms. Under the ordinary matrix-principal-log convention this
can include a nontraceless logarithm. The exact Gaussian coordinate domain is
in `su(N)`, so the identification in (F20) needed an explicit convention or a
smaller chart.

For `N=3`, `U=exp(2pi i/3) I` and `r=4`, the principal matrix logarithm has
HS norm `2pi/sqrt(3)=3.627598728...<r` and trace `2pi i`. Every traceless
anti-Hermitian logarithm has norm at least
`2pi sqrt(2/3)=5.130199320...>r`, while `r<pi sqrt(2)`, the HS injectivity
radius. The minimum follows from eigenangle lifts
`2pi(1/3+k_j)`, `sum k_j=-1`: their squared norm is
`4pi^2(sum k_j^2-1/3)>=8pi^2/3`. The finite enumeration is only a sanity
check of that integer argument. A crossing link carrying this value, with
internal links I, still passes every original cube-interior cut. Strict
margins give a neighborhood, so this is not cured by discarding a single
measure-zero point. If “principal” was intended to mean only the inverse of
the Lie-group exponential on its stated image, that restriction was the
missing convention. The [witness](checks/review_soft_fluctuation_chart_02.stdout.json)
and [original finding](checks/review_soft_fluctuation_findings_01.json) are preserved.

The coordinator now chooses
`0<r<min{injectivity radius,pi/sqrt(N)}` and defines `Omega_r` as the image of
the traceless HS ball under exp. I inspected the complete sole paragraph
delta and its interactions with (F19)–(F22). For `A` in that ball every
eigenangle is in `(-pi,pi)`, so `Log(exp A)=A`. Conversely, `det W=1` and
`||Log W||HS<r` give `tr Log W in 2pi i Z` and
`|tr Log W|<=sqrt(N)||Log W||HS<pi`, hence trace zero. This proves the exact
domain equivalence. The coordinate cutoff still excludes repeated
exponential preimages. (F21) retains the whole changed complement; no
complement estimate is inferred. The smaller fixed chart is compatible with
(F22) after taking the smaller local radius. No precision, prefactor, or
checker formula changed.

The [affected-only check](checks/review_soft_fluctuation_chart_affected_01.stdout.json)
passes 12/12 predicates for SU(2), SU(3), SU(5), and SU(10), checking the
principal inverse, center exclusion, and repeated-preimage exclusion. The
analytic argument above establishes the general claim. The original reviewer
confirms this correction in the same session. No material finding remains
within this source unit.

## Independent mathematical assessment

**Pinned group quotient and retained modes, (F1)–(F3).** The tree has one edge
for every nonroot vertex. Removing `(L^4-1)T^4` tree links from `4L^4T^4`
positive links leaves `(3L^4+1)T^4` group coordinates. At each leaf, solving
the tree-link equation is a left/right Haar translation, and inversion when
its orientation is reversed preserves Haar. The change is triangular in
depth order. Thus (F2) has probability gauge volume one and no nonconstant
Faddeev–Popov determinant. The linear tree-incidence minor is unimodular;
an orthogonal quotient's Gram determinant is a different measure dictionary.
All roots remain pinned during this operation. Their relative gauge modes
remain link degrees of freedom, as do all four harmonic forms. A face-constant
root gradient has fine squared norm `L^3||d_c lambda||^2` and coarse response
`d_c lambda`, giving the stated `kappa/L^3` tree-coordinate quotient. The
constant fine representative's `kappa/L^2` ratio is in a different metric.
Nothing here identifies either ratio with a Hamiltonian mass.

**Actual finite-u precision, (F4)–(F9).** For one contour family let
`a=average||theta||HS^2`, `q=average theta`, and `b=a-||q||HS^2`.
Differentiating its actual normalizer produces
`-(t/N)c_N a+(t/N)^2 Var(Re tr(W^-1 q))`. Haar invariance of
`Z_t(exp(sq))` sets the latter term to `(t/N)c_N||q||HS^2`.
Adding the numerator Hessian `(t/N)a` gives exactly
`(t/N)(||q||HS^2+(1-c_N)b)`. In particular the spread correction is present
at finite u, including on zero-Q directions. It vanishes in the classical
limit only. No tree-phase formula was substituted for this density Hessian.

The Wilson Hessian is `(u/N)d*d`. In the HS convention,
`Tr_ad(ad A)^2=2N tr A^2=-2N||A||HS^2`, so
`log j_N(A)=-N||A||HS^2/12+O(||A||^4)`. Rescaling by
`sigma=sqrt(N/u)` changes the Haar Hessian to `N^2/(6u) I`.
These derivations give the exact displayed scalar `K_u` on the tree
coordinates and its `N^2-1` identical colour copies. Stationarity at I
removes the linear term; it is not assumed from a classical minimizer at a
nonidentity background.

**Uniform coercivity, (F10)–(F12).** The cubical chain contraction stays in
the lifted rectangular box. At each coordinate contraction its strip cost
is bounded by that width times the chain's l1 norm; projections do not
increase that norm. This proves (F10) for general L. Comparing an edge tree
path and an S4-prime path to the same direct root path gives (F11)'s local
representation, with the stated conservative `b_L=60L^2`.

The internal sum costs at most `4L^4 b_L^2` per relevant plaquette. Crossing
links cost `2L^3` per coarse link for the squared mean, and at most
`2*L^3*8*b_L^2` per plaquette for the filling error. The total is
`4L^3(L+4)b_L^2`; the Q coefficient is `2L^3`.
The eightfold count uses oriented incident coarse-link labels and remains
valid at T=2. Lifting each two-block box before filling avoids a false
zero-winding assumption. Consequently `H>=aI` and the two positive finite-u
corrections imply `K_u>=aI`, independently of T. The numerical spectra
are diagnostics of this proof, not a substitute for it.

**Localization and full density, (F13)–(F18).** The local pair support yields
block-l1 range two. Plaquette incidence gives row bound24; the contour
length and at most eight incident coarse labels bound `Q*Q` by `8P^2`
and B by `16P^2`. Thus the advertised b is conservative. For the stated m,
the conjugation perturbation is at most `a/2`; the resolvent norm is bounded
by `2/(a+t)`. Integrating `t^-1/2/pi` gives `2/sqrt(a)`, not `2/a`, for
the inverse square root. Finite-volume Fourier sampling is the exact
periodization of the infinite periodic-block operator, including functional
calculus. The images must be summed. Unfolding them gives
`coth((m-mu)/2)^4` with `m0=3L^4+1` input coordinates per block.

The curvature output is `d J S_u`, with `6L^4` coordinates per block; the
four-link row and six-plaquette column counts give the stated distinct
bounds. The actual Lie-algebra covariance has the additional `N/u` factor.
For a perturbation supported on S, rank is at most `m0|S|`, preserved by
multiplication with the invertible square root. Summing the logarithms of
the nonzero eigenvalues proves (F18); traces/determinants of independent
colours multiply the bound by D. Operator norm control alone is not a
volume-independent determinant bound.

**Exact restricted integral and local remainder, (F19)–(F22).** With the
corrected chart, (F2) first removes only root-pinned gauge variables. Each
remaining Haar link contributes `h_N sigma^D j_N(sigma z)`. Then
`z=K_u^-1/2 xi` contributes `det(K_u)^(-D/2)` and the normalized Gaussian
conversion contributes `(2pi)^(D m0 T^4/2)`. At I the exact vacuum is
`N_t(I)^(-4T^4)`. These are all the factors in (F20).
The original interior-only cut, source action, bounded gauge-invariant
insertion, and nonlinear remainder remain in the expectation. A general
insertion would need its gauge average. This is a global integral, not an
unproved change of frozen-collar variables in H4. The zero-source restricted
denominator is positive; no uniform complex nonvanishing follows from that.

For (F22), the consumed single-normalizer theorem is STEP55 §§4.1–4.3
with S5–S7 and the convention/domain checks in its R6 review. The centered
logarithm after subtracting its value at I is bounded on a fixed complex
field neighborhood for real t>0. Cauchy estimates, the local polar critical
map, and the analytic Haar Jacobian therefore bound all fixed local third
derivatives. Multiplying by `u sigma^3` or `sigma^3` yields the claimed
`C u^-1/2 p^3`. The constants may depend on N,L,kappa bounds; the estimate
is per local term before whitening. It establishes neither an extensive
small total remainder nor a connected hard-cut/source expansion after
whitening.

## Premises, prior work, and consumer match

The supplied four-dimensional Wilson law, paired arithmetic S4-prime mean,
probability Haar, fixed `V=I`, positive fixed-range kappa, counting adjoints,
HS metric, torus geometry, and repaired chart are explicit model and
normalization/boundary inputs. They are not derived framework dynamics or
physical-observable identifications. The proof invokes elementary compact
group invariance, the exponential Jacobian, local chain contraction,
positive-operator functional calculus, and finite Gaussian integration.
Only the optional (F22) bound consumes the separately identified
single-normalizer analytic theorem. There are no fitted or empirical inputs.

Existing [LINEAR_PACKAGE](LINEAR_PACKAGE.md) §1.3 and §6 already supply the
classical soft-chain, admissible FP fixing, and PG gap mechanism.
[PROOF.md](PROOF.md)'s CT/N5/RW arguments already supply the localization and
square-root mechanisms. [STEP55](STEP55.md) and
[its review](CODEX_REVIEW_STEP.md) distinguish minimized coarse curvature
energy, one-step precision, finite-u normalizers, and actual-integral
identification. The new source's contribution is the actual finite-u
local-tree precision/measure dictionary and exact restricted integral; it
does not re-establish novelty for positivity or Combes–Thomas decay.

The current [soft-minimizer source](UNIFORM_SOFT_MINIMIZER_ASTRA.md) explicitly
concerns the u-stripped tree phase, so it supplies no missing finite-u
Hessian by itself. [H1–H5](SOURCE_LOCAL_HISTORY_RETURN_ASTRA.md) define the
actual fixed-V law and old `Z_cut(V)` used here.
[Sea3/Sea4/Sea15](SOURCE_SEA_CONSTRUCTION_ASTRA.md) keep the stronger
all-plaquette `Z_delta` and integrated coarse reference distinct. The new
producer does not use `int k_t(V;M)dV=1` to integrate fine variables at fixed
V. It meets only the identity-background quadratic/restricted-chart part of
that consumer's need. Arbitrary coarse fields, holonomies outside this chart,
frozen exteriors, full hard histories, connected original-source activities,
and the chart complement still require producers. The separate SOFTHARD
comparison packet was not consumed; this review makes no route switch.

Primary-source comparison was checked against versioned pages and matching
cached text: Dimock [1410.2798v3](https://arxiv.org/abs/1410.2798v3), PDF
pp.16–21 §§3.7–3.10, (100)–(152); Dimock
[1212.5562v2](https://arxiv.org/abs/1212.5562v2), PDF pp.91–92 Appendix F,
(633)–(646); Abdesselam–Rivasseau
[hep-th/9409094v1](https://arxiv.org/abs/hep-th/9409094v1), PDF pp.31–33 §V.E.
The first has hard abelian constraints, the second requires ultralocal
probability fields and local small interactions, and the third keeps fixed
cells and normalized Gaussian measures but requires summable links and a
small large-field price. None supplies the missing SU(N), d=4 interacting
estimates. Their use here is accurately limited to construction comparison.

## Executed evidence and preserved failures

The independent main and additional implementations import no author code.
Their [main output](checks/review_soft_fluctuation_independent_02.stdout.json)
has 21/21 predicates and 16/16 corruption controls; their
[additional output](checks/review_soft_fluctuation_additional_02.stdout.json)
has 24/24 predicates and 7/7 controls. These are separate from the chart
witness and affected confirmation, and from the author's counts.

Concrete results include all 7,776 L=3 actual contours and exact integer
fillings (largest l1 filling39 with the independent corner contraction),
all244 free-edge recovery fillings, 3,904 tree coordinates on T=2, all7,776
periodic Wilson plaquette traces under the random Haar SU(2) gauge quotient,
and actual periodic K versus Bloch action error below `9e-14`.
The sampled scalar H minimum was about `.019826` at kappa`.7`; the certified
analytic lower bound remains the much smaller (F12), not that observation.
The kernel Hessian's independent Haar-quadrature error was about `2.1e-8`,
the square-root bilinear-form error about `1.1e-15`, and the restricted
SU(2) one-link integral with all prefactors agreed to about `3e-17`.
Separate actual matrix-product checks cover Wilson/rescaling and the
adjoint Casimir for N=2,3,4; endpoint-pair charge counts cover T=2,3,4.

The rejected corruptions remove finite-u spread, the normalizer, Haar,
Wilson/HS scaling, endpoint pairing, Gaussian half, determinant colour
power, Haar probability density, vacuum factor, full rank, square-root pi,
and incidence/density factors. Some simple bookkeeping controls are
algebraic sensitivities, not full mutation runs of the author program.
The source's all-volume result rests on the reviewed proof. Floating-point
checks are not interval certificates; exact filling exhaustion is for L=3,
not every L. No numerical test certifies an exact nullity at momentum1e-7.

After freezing those independent results, I read both complete author
checkers and reproduced them once: [replay receipt](checks/review_soft_fluctuation_author_replay.json),
90/90 and9/9, both exit zero with empty stderr. This is reproduction, not
another independent implementation. The author's original38/39 spectral
failure is preserved; the complete code delta only changes the unresolved
near-zero rank claim into a near-zero diagnostic. Positivity thresholds
were not weakened. I separately inspected the failing predicate and code
delta; I did not rerun the known bad version.

My original attempts are also retained: the first main script stopped at an
unmatched parenthesis; the first additional script stopped when an argument
name collided with a metadata keyword; the first chart witness serialized a
NumPy integer count as boolean `true`. Corrected versioned copies repair only
those execution/serialization errors. All original sources/stdout/stderr
remain, and no scientific tolerance was relaxed. One later manifest-assembly
TypeError (hashing a list before joining its bytes) is also preserved in the
[mechanical failure record](checks/review_soft_fluctuation_manifest_attempt01_failure.txt);
it wrote no file and changed no mathematical result. The chart witness remains
a finding against the original interpretation even though the final source
now resolves it.

## Final lens dispositions and limits

| Lens | Disposition |
|---|---|
| Code and runner | Confirmed within the stated finite diagnostic scope; original failures preserved |
| Physics claim boundary | Bounded support in the supplied identity-background model |
| Proof obligations | Closed for (F2), (F7)–(F20) on the repaired chart and (F22)'s stated local bound; broader interacting targets open |
| Imports/support | Explicit model conventions and one named analytic input; primary papers used only as comparisons |
| Nature retention | Open; no retention or physical-gap conclusion |
| No-go discipline | Not applicable: no route-exhaustion or impossibility theorem asserted |
| Labeling convention | Not applicable to this mathematical producer |
| Governance and audit separation | No source/audit/git edits by reviewer; whole-PR and combined validation remain coordinator-owned |

One complete source review and one affected repair confirmation were performed.
There was one material finding, fixed by the coordinator and confirmed here;
none was skipped as an unresolved scientific defect in this unit. No
integration, landing, canonical audit cache, pipeline, or formal audit was
performed by this reviewer. The next substantive task is an actual local
expansion/control of the weighted expectation and its complement on the
consumer's required coarse-field domain, followed by the still-open
multiscale, continuum OS, reconstruction, and physical Hamiltonian-gap work.

Focused artifact checks found no vocabulary violations, broken relative links,
nonportable link targets, or trailing whitespace. Current independent scripts
compile in memory; intentionally failed archival attempts are not treated as
current executables. These checks do not replace the coordinator's combined
repository validation.
