# Independent review of the Euclidean rotation import unit

Type: meta; scoped scientific review, 2026-10-29.

The mathematical conclusions of [the source](EUCLIDEAN_ROTATION_IMPORT_ASTRA.md)
are confirmed at their stated finite or conditional scope after one explicit
hypothesis repair. The repaired source SHA256 is
`513e44546c5147caa44479c616937994f46aab09764a9808a87f3edddb05e294`.
This is not whole-branch approval, certification of the full external RPM1
theorem, or a formal audit. **Full four-dimensional existence and the physical
continuum mass gap remain OPEN.**

The strongest positive results here are a conditional spectral cone for an
ordinary common probability law, diagonal Wilson reflection positivity on
reflection-matched free boxes, and precise support/normalizer implications.
The exact counterexamples refute particular proposed weakenings or transfers.
They do not exclude a Yang–Mills construction or supply its missing state.

## Review identity, independence, and frozen scope

The coordinator requested `gpt-6-astra`, reasoning effort `max`, with
`fork_turns=none`, and subsequently confirmed those dispatch arguments. Backend
model/effort metadata was not independently available to this reviewer. This
review was performed separately from the author; no reviewer subagents were
used. The reviewer wrote only this report and `checks/review_euclidean_rotation_*`.
The coordinator owns integration, publication, and the active automation lock.

The original source hash was
`71e3ea5e66bc694cee172ab1348594a9645b06df92b3e33b8633cd39c725208e`.
All 17 entries of [the original freeze](checks/euclidean_rotation_import_freeze.json)
matched at initial inspection; its SHA256 is
`bbab37ecfaffbed97ef5077f5aee3242b09c2cd95d3387f89ea6087455ae17c4`.
The [initial inventory](checks/review_euclidean_rotation_initial_inventory.json)
and a byte-identical [original-source copy](checks/review_euclidean_rotation_original_source.md)
preserve that state. The coordinator also preserved it at commit
`119cd2c7bd3129448d4e48d42e402f7a4ca53b71`.

The [review criteria](checks/review_euclidean_rotation_criteria.md), SHA256
`314b21116c26b966545f76f5a287fdb2f480677330f24766bfff2ff65ad1be18`,
were written before the independent implementation and before reading the
author checker or its criteria/output packet. The source note, including its
expected constants, had already been read; this was not a blind numerical
challenge. Initial independent checks preceded author-code inspection. Later
matrix controls and mutation checks are explicitly marked post-inspection.
No threshold or original attempt was overwritten.

Installed review-loop and physics-loop instructions were read and applied.
Portable methodology was checked at the explicit fetched-main revision
`ca2bc7ddf64790da96cd43d42017d000fbfe4808`; stale local `main` was not used as
authority. Initial task HEAD was `cb0135f6600ac1f9397fb798228d7da40dcb403b`.
The coordinator subsequently integrated other workers and reported a fresh
fetch still at that same main revision. This review does not certify those
other workers' changes or the combined landing gates.

## Finding and affected-fix confirmation

**F1 — a proof premise was missing from the original spectral-cone statement;
the narrow repair is confirmed.** Original section 5 required strongly
continuous translations on L2 but explicitly made only reflections
measure-preserving. Strong continuity alone does not supply unitary
translations, a stationary expectation, the geometric support map, or the
reflection–translation relations used in the proof.

The coordinator changed only the theorem's hypothesis paragraph. It now
requires geometric translations and coordinate/diagonal reflections to act
covariantly on the local net, preserve the same law, and obey the usual
reflection–translation relations, with translations strongly continuous on L2.
The [repair receipt](checks/full_proof_rotation_hypothesis_fix.json), SHA256
`abca24308ec5a8e6479331fc96d6032df1e632b70b01ac9960f1e13e4a17f58d`,
contains the exact before/after text. I compared the changed bytes against the
preserved original: every displayed formula and all diagnostic code were
unchanged. The added hypotheses close this omission. This finding was a
missing-hypothesis finding, not an exhibited counterexample to the repaired
lemma.

No further source repair was identified within the stated review boundary.

## Conditional spectral cone: independent reconstruction

The premise is **one ordinary probability law**, with its ordinary L2 space,
covariant local observable net, measure-preserving geometric symmetries,
strongly continuous translations, the specified mirror RP forms, and dense
images of bounded compact positive-half observables in the relevant OS
quotients. These are substantial hypotheses; the present Yang–Mills lane has
not constructed them for its complete target family.

For each mirror, Cauchy–Schwarz in the underlying probability space gives
`||q(A)|| <= ||A||_2`. Reflection covariance gives
`||q(U_t A)||² = <q(A), q(U_(2t) A)>` for positive normal translations.
Iteration of Cauchy–Schwarz and the ordinary L2 bound give contraction and
preservation of the quotient null space. Strong continuity descends to the
quotient. Tangential translations preserve the RP form and act unitarily;
they commute with the positive normal semigroup. The joint spectral theorem
therefore gives a positive measure `rho` in coordinate variables with
nonnegative energy, and finite complex cross measures in the diagonal
quantization. The latter have total variation bounded by the product of the
two OS norms. Neither an unbounded insertion operator nor an exponential
field estimate enters these steps.

Translate the compact support of A sufficiently far forward to put it in
`t>|x|`. Both A and its image under the two-reflection composition then lie
in the diagonal positive half. The two quantizations express the same
stationary expectation. In coordinates `v=t+x`, `u=t-x`, the coordinate
factor is

`exp[-((omega-i p)/2)v - ((omega+i p)/2)u]`.

Integrating against `h(v) conjugate(h(u))` produces
`integral |Lh((omega-i p)/2)|² d rho` on the positive side. On the diagonal
side it is bounded by the fixed total variation times the product of the
supremum of `Lh` on the nonnegative real axis and on the imaginary axis.
Compact truncations justify the identity first; L1 integrability of h and
the finite measures justify the limit.

For the normalized gamma-family test, the Laplace transform is
`(1+z/epsilon)^(-1-i gamma)`. Its modulus is the inverse radius times
`exp(gamma arg(1+z/epsilon))`. The real-axis supremum is at most one; the
imaginary-axis supremum is at most `exp(pi |gamma|/2)`. Positive rho-mass in
a bounded set with `|p|>omega+2 epsilon` would make the squared modulus grow
strictly faster for one sign of gamma. Localizing that set also bounds the
radius factor away from zero. Positivity prevents cancellation. Thus such
mass is absent. Sending epsilon down to zero gives `|p|<=omega`.

The forward translation multiplies the original spectral measure by
`exp(-2b omega)>0`, so it does not hide a forbidden spectral component.
Density then removes the forbidden spectral projection. The same argument
applies to each chosen time–space coordinate plane. This confirms
`H >= |P_j|` for every j under the repaired hypotheses.

In dimension four this gives `H >= max_j |P_j|` without continuous rotation
invariance; it does not by itself give the Euclidean norm bound. It gives
no strictly positive threshold above the vacuum, no vacuum uniqueness, and
no nontrivial excitation. The [mass-gap target](MASS_GAP_TARGET.md) still
requires those separate physical and infrared inputs.

## Wilson geometry, actual observables, and normalizers

**Free-box diagonal RP is confirmed at finite cutoff.** For
`h(x)=x_j+s x_k`, every lattice edge changes h by at most one. A square
meeting both open sides must lie in the j,k plane and has heights
`-1,0,0,1`. Its opposite zero-height vertices are fixed by reflection; its
two-edge positive path P is paired with the reflected negative path Q.
The oriented loop is `P Q*`. The identity

`Re tr(P Q*) = (1/2) sum_ab (P_ab conjugate(Q_ab) + conjugate(P_ab) Q_ab)`

gives a positive feature expansion of the crossing exponential for a
nonnegative Wilson coefficient. Pair the remaining plaquettes, condition
on any shared plane links, and use product Haar measure on the two halves.
Every term is a nonnegative coefficient times an absolute square. Compactness
and the finite number of links justify termwise integration. The proof uses
a reflection-matched free finite geometry and paired boundary data, not the
periodic torus by default. It proves bounded half-observable RP; no gauge
fixing or continuum approximation is needed for this diagonal decomposition.

The actual [ROTDEF clover](ROTDEF.md) has diagonal height radius `2a`.
Its plaquette-source coefficient is half the sum of the four corner values,
so `|c_p(f)|<=2||f||_infinity`. Real centering and a real nonzero paired
normalization preserve covariance. A support buffer at least `2a` places
the clover stencil in the closed positive half; a one-unit diagonal buffer
does not suffice. Passing characteristic RP to a common weak ordinary-law
limit is a finite matrix limit. Passing polynomial RP additionally requires
convergence/uniform integrability for the actual products.

For the actual odd-L centered blocks in [PROOF S4](PROOF.md), a strict
positive coarse center has height at least L. The block offsets reduce
height by at most `L-1`, leaving height at least one. Every prescribed
complete-axial/order-averaged contour stays in the union of its two endpoint
blocks: the two endpoint legs remain inside their blocks, and the length-L
middle leg traverses their adjacent union. This is an actual contour check,
not an inference from signed-permutation covariance alone. Plane-centered
blocks fail the support test: at L=5 the prescribed intermediate point
`(-2,2,0,0)` has height -4 for `h=x_0-x_1`. Such coarse observables must be
excluded or separately buffered. The measurable odd-branch convention
preserves the stated reflection covariance but does not repair this support
failure.

The normalized product soft kernel integrates to one in the full coarse
variables for every fine configuration. Integrating the chain from its last
level therefore restores exactly the zero-source bare Wilson marginal.
For coarse observables with disjoint reflected positive footprints, integrating
their own coarse variables produces a positive-half function `T f` of the
fine links, and the reflected quadratic form reduces to fine RP. The support
and product structure are essential. Conditioning at an arbitrary fixed
coarse field does not perform this integration and need not preserve RP.

An independent two-site probability example makes the latter distinction
explicit. Take independent uniform fine signs and
`k(v|u)=(1+alpha v u)/2`, with `alpha=1/2`. Summing all coarse signs gives
one pointwise and preserves the fine product law. The integrated reflected
form for the sign observable is zero. Conditioning on coarse signs `(1,-1)`
instead makes the reflected fine-sign form `-1/4`. This is a logical
normalization control, not a counterexample for a Wilson conditional law.

The current [HRP source](HRP.md), SHA256
`f1f991dea8062bfc7176a68cc639beacd848d4fb9cdd0bd4917198e39dac51b5`,
and [its R2 review](REVIEW_HRP_R2.md) now resolve the earlier bounded review
hold at their coordinate-RP scope. Their zero-source bare-marginal and
limit-domain qualifications agree with the distinctions above. They do not
supply diagonal RP on the needed common continuum law, rotation restoration,
ordinary all-order moments, or a physical gap. The HRP runner was not executed
here; its machine-specific lock path was not imported.

## Exact negative examples and their boundaries

**Periodic geometry.** Removing the fixed diagonal vertices of the 4-by-4
periodic square leaves all 12 remaining vertices connected. The wrapping
plaquette `(3,0),(0,0),(0,1),(3,1)` has only one fixed vertex and is not mapped
to itself. The free-box two-fixed-corner factorization therefore cannot be
transferred unchanged to this torus. This is not a theorem that periodic
Wilson diagonal RP is impossible.

For the separate massive Gaussian model with covariance `(1-Delta_lat)^(-1)`,
the diagonal reflected Gram at `(1,0),(3,1)` is

`[[2/45, 5/63], [5/63, 8/315]]`, with determinant `-19/3675`.

I obtained these entries by solving six translation/square-orbit Green
equations, independently of the author's 16-by-16 inversion and Fourier
sum. A coordinate-reflection control on time layer one has eigenvalues
`2/15`, `2/105`, `2/105`, `2/315`, all positive. Thus symmetry and coordinate
RP alone do not supply the diagonal statement for this periodic Gaussian
model. No gauge-model conclusion is drawn from it.

**The derivative-Gaussian example satisfies the advertised weakened
hypotheses and has a noncontact rotation defect.** Let phi be the ordinary
massive scalar Gaussian free field on R4, with mass one as a control
normalization, and let `F=(sum_j partial_j^4) phi`, declared to be a scalar.
The differential map is real, continuous on Schwartz space, local, and
translation-covariant. It commutes with each required coordinate and diagonal
reflection, which are signed coordinate permutations. Pulling the scalar
free-field RP forms back through that map proves all those mirror RP
conditions for F, including characteristic RP. This yields an ordinary
real tempered stationary Gaussian law with entire source functionals and
Schwartz moment bounds. Its assigned scalar representation has weight zero.

The covariance multiplier is
`(sum_j p_j^4)^2/(|p|²+1)`. It is not rotationally invariant away from contact.
For a rotation with cosine 5/13 and sine 12/13, evaluation of the numerator
defect at `p=(i,0,0,0)` gives `-359438400/815730721`, while the denominator
vanishes. Therefore the denominator does not divide the numerator; the
rational defect is not a polynomial. A translation-invariant distribution
supported only at coincidence has a polynomial Fourier transform, so
disjoint smooth tests can detect this defect. The isotropic comparator
`F=Delta² phi` has zero defect.

This F does **not** meet RPM1's global bound. Applying that bound to `t f`
and sending real t to infinity would give a uniform L2 covariance bound.
But the multiplier on the first axis is `r^8/(r²+1)`, which is unbounded;
high-frequency localized real test packets violate such a bound. Entire
source dependence and finite Schwartz seminorm estimates do not fix this
failure. Consequently this is a counterexample to the proposed replacement
of the specific global bound, not to RPM1 and not to Yang–Mills.

Two additional logical controls have the claimed narrower roles. The
stationary random constant `G²-1` has every moment and all mirror RP, but
Laplace transform `exp(-t)/sqrt(1-2t)` only for `t<1/2`; hence an ordinary
law plus RP need not give the global bound. Conversely the stationary
Gaussian covariance `exp(-|x-y|²)` has bounded spectral density and the
global Gaussian L2 bound, but its two-positive-time RP determinant is
`exp(-20)-exp(-18)<0`. Supported smooth approximations retain the strict
negative sign. Thus the law plus the bound need not give RP. These establish
the stated nonimplications without claiming a larger independent-wall count.

## Literature import, premise inventory, and proof domains

The pinned primary candidate is
[RPM1 at commit 1b92bd0347e3b8763cd8ecc1f96dc3c2a92dd310](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/1b92bd0347e3b8763cd8ecc1f96dc3c2a92dd310/RP%20O(d)%20trick%20(RP1)/RPM1.tex).
The TeX SHA256 is
`ae201364acf2ea69cc01cc323db925793f26743ca02cbe404ef6086d778a7801`;
the independently recomputed Git blob is
`86d31273743ea0b3dc2b99090058ce3b930fba5a`. The GitHub connector returned the
same blob. Both pinned READMEs were read; their tentative verification status
is preserved. No announcement is counted as mathematical evidence.

Theorem A's actual interface is one real tempered Borel probability law,
translation invariance, the global inequality
`E exp F(chi) <= exp C(||chi||_1+||chi||_2²)` for **every real Schwartz
source**, characteristic RP for all stated coordinate/diagonal mirrors, and
a finite orthogonal O(d) representation whose planar weights lie between
-2 and 2. The conclusion is covariance of moments at pairwise disjoint
supports, allowing contact defects. It is not full-law invariance, a field
construction, or a mass-gap theorem. The source's import table matches this
interface.

I read the scientific TeX body, reductions, spectral argument, insertion
estimates, joining/continuation, angular positivity/degree argument, examples,
and appendices. The proof separates the bounded spectral-cone comparison
from the unbounded slab insertion estimate. The latter consumes the global
bound, so the valid removal of that bound from the former does not remove
it from the full rotation theorem. This report independently confirms the
interface and the bounded cone, not every analytic estimate or gluing step
of the full external theorem.

| Input | Classification and actual use | Derivation boundary |
|---|---|---|
| RPM1 Theorem A | Candidate literature theorem, conditionally reusable interface | No full external-theorem certification or matched Yang–Mills producer here |
| Massive scalar free Gaussian field | Standard mathematical model for an exact counterexample | Mass one fixes a control model; no physical Yang–Mills mass is imported |
| Sokal 1982, pp. 327–330, 374–375 | Primary background and same-state boundary comparison | The scalar construction uses its own state/comparison machinery; it supplies no gauge boundary-independence estimate here |
| Jaffe–Jäkel–Martinez 2013, VI.1–VI.5 | Primary spectral-comparison analogy on a two-dimensional cylinder | Existing P(phi)2 Hamiltonian, ground state, and Feynman–Kac inputs do not construct the present four-dimensional theory |
| RP1O1 historical scalar application | Explicitly conditional supplement | Assumes a normalized scalar sequence and its common continuum probability limit; no new lattice construction |
| Wilson coefficient, free boundary, scalar clover, centered blocks, product normalizer | Explicit mathematical model/observable/normalization premises, checked against actual definitions | No bare-to-renormalized coupling identification, periodic-boundary replacement, or full observable-family identification is inferred |
| Ordinary common law, net covariance, L2 continuity, dense domains, all mirror RP | Non-satisfying conditional inputs of the cone | Their construction in Yang–Mills remains open |
| Global real-source bound and representation matching | Additional non-satisfying inputs of the RPM1 route | Finite source discs, restricted Schwinger bounds, and scalar bookkeeping do not construct them |
| [Minimal framework axioms](../../../../../docs/MINIMAL_AXIOMS_2026-06-29.md) and [approved kinetic isotropy](../../../../../docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md) | Foundation inventory, not analytic inputs to these proofs | They add no ordinary field law, continuum rotation theorem, source estimate, vacuum selection, or gap |

[Sokal's source](https://www.numdam.org/article/AIHPA_1982__37_4_317_0.pdf)
is used to check the same-state and exhaustion warning, not to close the
Yang–Mills import. In particular, p. 329 compares mirror-compatible finite
geometries in one infinite-volume scalar state using model-specific
inequalities. Separate mirror-friendly subsequences are insufficient.
[Jaffe–Jäkel–Martinez](https://arxiv.org/pdf/1302.5935v1) is used as a
spectral comparison analogue, not as a four-dimensional existence or gap
theorem. The [pinned outline](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/1b92bd0347e3b8763cd8ecc1f96dc3c2a92dd310/RP%20O(d)%20trick%20(RP1)/RP1O1.pdf)
is used to verify the conditional historical-application description only.

[OSLEAF55](OSLEAF55.md) supplies a restricted collision-flat test domain.
For a nonzero f, `f tensor f` need not belong to it. Such a hierarchy is not
automatically an ordinary algebra of all smeared-field polynomials or a
probability law on tempered distributions. Its variance obstruction is used
with its actual torus trajectory, bounded normalized variance, nonzero
normalized separated covariance, and raw separated upper-bound hypotheses;
no unconditional no-go for renormalized fields follows.
The underlying SRCCD variance lower-bound proof was not recertified here;
the checked points are its quoted hypotheses and the elementary conditional
implication consumed by this import note.

[The source-local history return](SOURCE_LOCAL_HISTORY_RETURN_ASTRA.md)
keeps the coarse field real and fixed, and uses the original coefficient
sources with the kernel/normalizer held at the real coupling. Its basic
`|epsilon_p|<=lambda/u` domain gives the stated finite source radius through
the exact clover coefficient. I also checked the stronger fixed-relative
corollary H20c/d. Neither assertion is the needed global ordinary-field
moment-generating estimate; increasing an admissible source disc is not a
proof of the bound or of the ordinary common law.

The resulting obligation graph is explicit: finite free-box RP plus support
transport still needs a **same-state ordinary continuum limit** before the
conditional cone applies. Full rotation by RPM1 additionally needs the
global bound and an applicable field representation, as well as complete
verification of that candidate theorem. Full four-dimensional existence
needs the complete target observable family and reconstruction conditions.
A physical positive mass gap needs an additional uniform infrared argument
and nontrivial spectrum. No target-equivalent missing producer is labeled
near closure.

## Independent checks, mutations, and preserved failure

The [initial independent runner](checks/review_euclidean_rotation_independent.py)
ran successfully before author-code inspection. Its [receipt](checks/review_euclidean_rotation_attempt01.receipt.json)
and [output](checks/review_euclidean_rotation_attempt01.stdout.json) record:

- Exact classification of 5,832 plaquette/plane cases, including 270
  straddlers; all twelve diagonal normals are included.
- Enumeration of actual centered-block contours for L=3,5, both canonical
  diagonal signs, all 24 axial orders, all fine starting sites, and all
  admissible positive coarse-link directions: 118,608 paths and 2,002,224
  vertex visits. The general odd-L conclusion follows from the preceding
  support proof, not extrapolation from these cases.
- Clover coefficients and two-unit support radius; the normalized-kernel
  fixed-coarse-field control; periodic topology; the separate-model Gaussian
  Gram via orbit equations and a coordinate positive control.
- A different rational rotation for the derivative-Gaussian defect,
  reflection invariance of its symbol, the isotropic control, and the
  spectral change-of-variable factors.

One independence qualification matters: despite being written before the
author checker was read, the initial quaternion control happened to use the
same familiar rational unit-quaternion fixtures and multiplication formula.
It is not counted as implementation diversity. The subsequent
[explicit complex-matrix check](checks/review_euclidean_rotation_matrix_mutations_attempt02.py)
uses different rational SU(2) matrices and direct matrix multiplication.
Its loop and feature sum both equal `2640120/2683573`; removing the adjoint
gives `-957480/2683573`. The positive and negative crossing-kernel quadratic
forms at the specified coefficient are respectively 3 and -3. These are
kernel controls, not a claim about every negative-coupling gauge measure.

The first supplemental matrix attempt failed because it tried to substitute
the sign of `log(2)` after SymPy had already evaluated the Gram entries to
numbers. That substitution left the positive Gram unchanged. The
[failed script](checks/review_euclidean_rotation_matrix_mutations.py),
[stderr](checks/review_euclidean_rotation_matrix_mutations.stderr.txt), and
[receipt](checks/review_euclidean_rotation_matrix_mutations.receipt.json)
are preserved. The second attempt constructs the negative exponential Gram
directly and passes the **same** `-3` criterion. This was a reviewer
implementation error, not adverse evidence about the source.

The author final runner was then run unchanged. Its
[reproduced stdout](checks/review_euclidean_rotation_author_reproduction.stdout.json)
is byte-identical to the frozen attempt03 output, SHA256
`80d04781f93107f134d2b8625e86cc9567431132240a5a5c344865a6d5bfa6ad`.
The [first eight mutations](checks/review_euclidean_rotation_matrix_mutations_attempt02.stdout.json)
and [eleven additional mutations](checks/review_euclidean_rotation_additional_controls.stdout.json)
were all rejected by assertions. They cover mirror sign, path adjoint,
trace factor, crossing coefficient sign, strict-block buffer, periodic
wrapping, Gaussian mass normalization, rotation coefficient, crossing
heights/fixed corners, clover radius, boundary-block height, fixed-corner
count, Fourier normalization, the exact minor and pole constants, isotropic
power, high-frequency growth, and Gaussian integral normalization.

The additional runner also independently differentiates the Gaussian-square
cumulant generator through order eight, checks divergence at its Laplace
radius, and verifies the stationary Gaussian non-RP determinant. This is
coverage of the listed formula families, not an assertion-mutation test of
every line or a continuum proof. No floating tolerance was used.

## Actual read coverage and remaining review limits

The full original 544-line note was read before the checker. The repaired
paragraph and exact whole-file diff were read after the fix. The final
author checker and criteria were read completely; the two prior checker
versions and all three output versions were compared by complete semantic
diffs/parsed key differences, with all receipts, source manifest, validation,
and vocabulary records inspected. The original 17 hashes were all verified.
The reviewer-owned runners were inspected and executed as described above.

| Source | Actual reviewer coverage |
|---|---|
| RPM1.tex | Scientific body lines 702–2867, including appendices and bibliography; truncated tool ranges were reissued. Macro/preamble lines 1–701 were not scientific review inputs. The companion PDF was hashed, not separately proof-certified. |
| Public READMEs | Both whole files at the pinned commit, through GitHub; no other public manuscripts certified. |
| Sokal 1982 | Extracted text for published pp. 327–330 and 374–375; no whole-paper certification. |
| Jaffe–Jäkel–Martinez 2013 | Extracted PDF pp. 25–26, section VI and equations VI.1–VI.5. |
| RP1O1 | Extracted PDF pp. 1–2 and 31–33, including the historical application; not its full proof-task catalogue or the older 27-page source. |
| PROOF.md | Actual S1–S7 definitions at 1046–1110; Decision 4/D4-norm at 2106–2143; L9a/L9a-prime/L9b at 4984–5055. The full 7,000-plus-line file was not certified. |
| ROTDEF.md | Lines 1–150, including the exact clover definition, coefficients, and normalization. |
| OSLEAF55.md | Lines 124–204 and 267–369, plus errata 767–795; restricted products, RP, common-sequence and closure interfaces. No certification of its entire EXT/trajectory machinery. |
| CODEX_REVIEW_OSLEAF.md | Findings F1–F15 and bankable-scope discussion were read, with the previously truncated F4–F6 passages reissued. The consumed FS hypothesis matching/conditional algebra and domain qualifications were checked; the underlying SRCCD variance proof and that entire review were not recertified. |
| SOURCE_LOCAL_HISTORY_RETURN_ASTRA.md | Lines 100–264, 400–450, and 652–690: actual kernels/fixed real data, source price and relative-source corollary, complex-domain limitations. No recertification of the whole history construction. |
| HRP.md | Sections 3–4 (198–357), section 6 (481–578), and repaired consumer statements (743–797). Only intersecting coordinate/normalizer/domain claims are consumed. |
| REVIEW_HRP_R2.md | Whole file; documentary review evidence, not a substitute for the HRP passages just listed. |
| CODEX_REVIEW_SPHERE2.md | F5–F8 and beginning of F9 (73–118), plus the bankable-scope list (240–250). Used to check conditional route boundaries, not to certify the sphere programme. |
| MASS_GAP_TARGET.md | Whole file; its target and elementary conditional decay criterion, not an infrared producer. |

Full applicable methodology reads included the pinned review-loop and
physics-loop skills, workflow/freshness/setup/unit/lens/fix/audit-compatibility
references, discovery/claim-status/delivery/proof-search/literature-bridge
references, and no-go-discipline instructions. The minimal-axiom memo,
primitive-registry check and registry, and kinetic-isotropy source were read.
The final machine-readable receipt binds the precise source versions and
coverage; it does not turn an excerpt read into whole-source certification.

The no-go discipline result is **partial-narrowing**. The note explicitly
has four live or conditionally handled route families rather than a five-route
exclusion packet; N1 receives no packet PASS. N2's two stated nonimplications
are checked; N3–N4 preserve explicit premises and exact model domains; N5's
resolution certificate is finite; N6 does not demand a new axiom; N7 retains
the direct common-state diagonal-RP route; N8 does not claim an exhaustive
repository or literature search. The exact counterexamples can be reused at
these narrow scopes. A global no-go or general review-loop landing PASS would
need additional work and is not issued here.

The final disposition for proof obligations is **CONDITIONAL** for the
spectral-cone/application chain and **CLOSED at the stated finite or exact
model boundary** for the free-box geometry and logical counterexamples.
The complete RPM1 proof, the ordinary common continuum law, periodic
same-state transfer, full local-field identification, four-dimensional
existence, and physical continuum gap remain outside what this report closes.
