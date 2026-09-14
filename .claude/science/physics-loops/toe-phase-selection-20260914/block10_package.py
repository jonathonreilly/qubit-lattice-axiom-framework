"""Assemble the personally reviewed source and self-contained finite runner."""
from pathlib import Path
import shutil

PACK=Path(__file__).parent
ROOT=Path('/Users/jonreilly/Documents/Codex/toe-periodic-clock-phase-20260914')
NOTE='FINITE_CLOCK_SCORE_GAUSSIAN_MAXWELL_SCALING_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-14.md'
RUNNER='finite_clock_score_gaussian_maxwell_scaling_limit_2026_09_14.py'

HEADER='''---
claim_id: finite_clock_score_gaussian_maxwell_scaling_limit_bounded_theorem_note_2026-09-14
claim_type: bounded_theorem
claim_scope: "Conditional on the explicitly stated uniform all-affine integer-curl covariance input supplied in the same reviewed delta, bounded plaquette-score observables of isotropic four-dimensional finite-clock Villain models converge along beta,beta_d tending to infinity, lattice spacing tending to zero and physical torus side tending to infinity to the Gaussian Maxwell curvature distribution. All joint smeared moments converge; the explicit Gaussian OS quotient is a symmetric Fock space with two transverse modes of energy |p|. Clock order and couplings vary and the microscopic law is supplied. No fixed-N=3 phase, native law selection or axiom update is asserted."
upstream_dependencies:
  - periodic_finite_clock_villain_covariance_and_observable_masslessness_bounded_theorem_note_2026-09-14
runner: scripts/finite_clock_score_gaussian_maxwell_scaling_limit_2026_09_14.py
---

# Finite-clock scores converge to a Gaussian Maxwell curvature field

**Date:** 2026-09-14
**Type:** bounded_theorem
**Status:** proposed_retained

For the supplied varying-order finite-clock Villain family, the all-affine
integer-curl covariance input stated below implies joint-law convergence
of bounded physical score observables to a Gaussian Maxwell curvature
distribution, whose explicit positive-time quotient has two transverse
modes with energy |p|. This is a conditional model theorem. Independent
review of both its input and the new implication is pending.

The new ingredient beyond covariance convergence is an all-real-source
MGF squeeze. Conditional independence of the auxiliary lifts then removes
their noise without a volume loss, and cell-average smearing controls the
continuum normalization. Gaussianity is derived for the observables; it
is not assumed from their limiting two-point function.

## Status, inputs and proof obligations

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: periodic_finite_clock_villain_covariance_and_observable_masslessness_bounded_theorem_note_2026-09-14
target_blocker_text: "Upgrade the specified finite-clock massless observable sector to an actual Gaussian Maxwell scaling field, while retaining its supplied-law and varying-clock-order hypotheses."
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Independently review the affine-curl input and the new all-source implication, then investigate charged observables and the fixed-alphabet Hamiltonian phase separately."
conditional_surface_status: conditional-support
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "A conditional analytic joint-law and Gaussian reconstruction theorem for a supplied scaling family, with finite mathematical challenges."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

The sole load-bearing repository dependency is
[the periodic finite-clock covariance source](PERIODIC_FINITE_CLOCK_VILLAIN_COVARIANCE_AND_OBSERVABLE_MASSLESSNESS_BOUNDED_THEOREM_NOTE_2026-09-14.md),
sections 2–8, at revision
`075a47fd49e98bb4c8f4b88ec149dcb78a52b5cd`, source SHA-256
`bfedf452ec4e5b4b19c7099cb4c5e7ebc69aca4198fbdfba1c8788647ddea237`.
Its full proof is carried in this PR's delta. It is provisional, not a
retained authority. The new implication is conditional on the precise
all-real-shift estimate stated in section 1; finite challenges here do
not independently establish that arbitrary-volume input.

| Input | Role | Provenance and status |
|---|---|---|
| Equal even four-tori, finite clock alphabets, isotropic Villain weights | Supplied probability models | Defined in section 1; no native identification |
| Uniform covariance bound on every affine integer-curl coset | Sole substantial mathematical premise | Linked source sections 3–8, provisional and included for joint review |
| Poisson summation and finite character duality | Finite-dimensional machinery | Normalizations and fiber multiplicities derived below, including composite N |
| Joint scaling of beta, beta_d, spacing and physical side | Explicit limit family | Defined in section 5, with a concrete integer sequence in section 6 |
| Bounded score observables and cell-average embedding | Supplied observable identification | Sections 4–5; no empirical normalization |

| Proof obligation | Status in this note | Consequence |
|---|---|---|
| Uniform all-affine curl and coexact covariance lower bound | Explicit provisional input, section 1 | Quantitative control at every real tilt |
| Exact positive lift and complementary covariance identity | Derived in section 2 | Full-rank lattice law and harmonic-aware variance control |
| Centered source maximum and integrated tilted curvature | Derived in section 3 | Gaussian joint laws for exact sources |
| Auxiliary-to-physical observable comparison | Derived in section 4 | Uniform l2 error with no volume factor |
| Cell-average projector convergence | Derived in section 5 | Continuum Maxwell covariance and harmonic removal |
| Distributional tightness and moment passage | Derived in section 6 | Actual Gaussian random-distribution limit |
| Electric–magnetic reflection kernel and dense quotient | Derived explicitly in section 7 | Two transverse modes and the full Gaussian Fock quotient |

The strongest unresolved proof validation is independent review of the
uniform affine input. The strongest unresolved physical identification
is the relation of this varying-clock-order family to a selected native
law and to the fixed N=3 interacting Hamiltonian. These are not renamed
as conclusions of the scaling theorem. No axiom or registered primitive
is introduced or altered.

'''

APPENDIX='''

## 9. Finite mathematical challenges

The primary runner is
`scripts/finite_clock_score_gaussian_maxwell_scaling_limit_2026_09_14.py`.
It reads no external or repository scientific input and has no helper
runners. Its elementary formulas and its own finite configurations are
the executable domain. All lattice sums use explicit finite cutoffs;
their floating-point agreement is a challenge to identities, not a
certification of infinite sums or an arbitrary-volume phase proof.

| Family | Independent comparison and actual finite domain |
|---|---|
| Positive lift, score and duality | Three-face cycle-incidence toy at N=2,4,6: explicit clock fibers, positive image sums, an independent Fourier score and primal/dual lattice moment enumerations |
| Centered theta and affine shift | Nonorthogonal rank-two lattice with 25 seeded real sources; a shifted odd-integer lattice with variance 1 at Gaussian parameter 0.05 |
| Gaussian approach and covariance control | Five explicit three-face exact-plane lattice examples; a Rademacher variable with variance 1 and fourth moment 1 preserves the non-Gaussian alternative |
| Real tilt and coset mixing | Direct global moments, conditional moments and finite differences of source derivatives at three nonzero tilts; conditional means are retained |
| Midpoint Fourier geometry | Even side-six four-torus mode, direct cell quadrature, finite Fourier transform and independently constructed differential symbol; four refinement steps |
| Electric–magnetic OS kernel | Full six-component projector versus block formulas, independent oscillatory integrals, reflected Gram factorization and three spatial momenta |
| Bianchi identity and contacts | Exterior-algebra composition versus polynomial divergence covariance; a shared-noise example distinguishes conditional independence |
| Tail and parameter constants | Numerical tail integrals versus the analytic bound, three affine-input delta values and four members of the explicit scaling family |

For example, the three-face moment enumeration gives covariance duality
errors below 4e-15 for its stated parameters. The five exact-plane
examples have log MGF values approaching 0.32, with the final discrepancy
below 5e-7 and fourth moment approximately 3.00013234. These are toy
checks, not samples of the four-dimensional scaling limit. The reflected
six-by-six Gram matrix has eigenvalues 0,0,0,0,2,2 to rounding in each
checked momentum. Its rank follows analytically from section 7.

## 10. No-Go Discipline Gate

The following gate scopes the conditional theorem and the finite
counterexamples. It asserts no exhaustion of routes to a theory of
everything and no contradiction of the framework axioms.

### N1 — Materially distinct attempted failures of the implication

| Honesty | Object and attempted failure | Disposition and authority |
|---|---|---|
| ATTEMPTED | Probability law: retain the limiting covariance but choose a non-Gaussian joint law | The Rademacher witness in section 9 has the same variance and a different fourth moment. Section 3 supplies the extra all-real-source squeeze needed for the stated model. |
| ATTEMPTED | Conditional measure: use nonzero affine means to spoil source curvature or accumulate auxiliary noise coherently | Sections 2–4 retain total covariance after every real tilt and derive independent conditional plaquette noise. The three-face tilt enumeration and shared-noise witness check these exact distinctions. |
| ATTEMPTED | Topology and limiting geometry: retain a norm-one harmonic mode or a sampling alias | Section 5 keeps the harmonic term until its smeared norm vanishes and uses cell integrals with a dense Fourier proof. A constant normalized source retains harmonic norm one and is outside the vanishing-harmonic source hypothesis. |
| ATTEMPTED | Spectral reconstruction: count three Euclidean exact components or four uncoupled electric/magnetic components as physical photons | Section 7 includes the reflection sign, cross blocks and contact subtraction. Its explicit Gram factorization has rank two, independently checked by oscillatory integrals and eigenvalues. |
| ATTEMPTED | Scaling contract: keep the clock order fixed while sending both electric and dual variances to infinity | Section 1 has beta beta_d=N^2/(4pi^2), so the stated limit necessarily varies N. The physical N=2 score is identically zero, and the displayed integer sequence respects all growing-parameter requirements. |

These attempts differ in the joint probability law, conditional measure,
cohomology and continuum geometry, Hilbert-space reconstruction, or
parameter contract. Their disposition is the written derivation and
finite witnesses in this source, subject to review. None is claimed
ruled out by prior retained authority, and the list is not exhaustive.

### N2 — Dependency and independence accounting

There is one substantial mathematical premise: the uniform all-affine
integer-curl estimate, including its dual Hodge version. The latter is
not counted as an independent wall; it follows from the same estimate
and the integral Hodge identification in the linked source. The model
law, four scaling limits and observable choice are definition-level
hypotheses, not an asserted independent-wall set.

| Pair of outstanding questions | Implication established here | Treatment |
|---|---|---|
| Validation of the affine input / selected native-law identification | Neither implication is established | Keep both open; independence is unknown, not asserted |
| Fixed N=3 Hamiltonian phase / selected native-law identification | Neither implication is established | Keep both open; neither is a premise of the varying-N theorem |
| Validation of the affine input / fixed N=3 Hamiltonian phase | Neither implication is established | Do not transfer this proof or its conservative parameter region to that Hamiltonian |

No headline claims a number of independent framework walls. The new
conditional implication is useful even while those physical questions
remain open; it does not collapse them by terminology.

### N3 — Hidden-condition scan

The full mathematical contract is explicit: dimension four; equal even
periodic side L>=4; canonical positive cell orientations; real sources;
the supplied Villain weights; arbitrary finite integer N at each step;
the all-real-affine covariance input; beta,beta_d tending to infinity;
spacing tending to zero and physical side tending to infinity; cell
averages of L2 tests; and strict positive-time support in the reflection
calculation. The Gaussian upper MGF bound is used only at the centered
law. Tilted lower curvature uses all affine cosets. The cutoff boxes in
the Sobolev argument are auxiliary and local. Gaussian Fock
reconstruction is given explicitly through Wick exponentials; no
general interacting reconstruction theorem, transfer-log locality,
phase uniqueness or native probability rule is silently assumed.

### N4 — Exact residual matching

| Source or witness | Residual addressed | Matching claim and disposition |
|---|---|---|
| Linked covariance source, sections 3–8, pinned revision and hash above | Uniform affine-curl covariance at all shifts and its dual application | Exact model and topology match; explicitly provisional mathematical premise |
| This source sections 2–4 and the primary clock/tilt families | Positive lift normalization, conditional means and physical score noise | Exact algebraic mechanism; finite toy domain is disclosed |
| This source sections 5–7 and the primary Fourier/OS families | Continuum projector and positive-time polarization quotient | Matching normalization and sign convention; arbitrary limits are derived in prose |
| Rademacher, shifted lattice and shared-noise witnesses in section 9 | Missing Gaussianity, false shifted upper bound, or missing conditional independence | Matching narrow inference controls, never witnesses against the supplied model or axioms |

No witness from a different microscopic Hamiltonian is used to infer
that Hamiltonian's phase. No external field-theory phase theorem is
imported. The prior source's complete proof remains in this reviewed
delta rather than being replaced by a bare unreviewed conclusion.

### N5 — Resolution and rhetoric

At per-element resolution the runner checks scalar lifts, sources and
tails. At per-site resolution it checks a disclosed three-face incidence
toy. At per-mode resolution it checks symbols, reflections and rank. At
per-block resolution it checks the named finite clock, lattice and
Fourier blocks. At lattice-wide resolution the scaling and tightness
statements are analytic consequences conditional on the uniform input;
they are checked and not executed. The five substantive resolution lines
in the canonical runner cache state this distinction. Finite agreement
is never used as evidence of a universal theorem or an axiom obstruction.

### N6 — Partial closure and primitive boundary

The successful partial result is a complete conditional field-scaling
construction for a supplied family. It permits further work on charged
observables, alternative fixed-alphabet limits, or identification of the
underlying law. The parameters and isotropic coordinate units remain
supplied. This note makes no primitive-absence claim and requests no
new axiom. No premise registry, approved primitive or framework text is
edited, and no convention is promoted into physical selection.

### N7 — Steelman

A hostile reviewer should challenge the all-affine input before accepting
anything downstream: finite coset checks do not establish a uniform
bound in growing four-tori. Even if that proof is correct, a growing
clock alphabet at weak coupling can yield a free field while the
fixed-alphabet interacting Hamiltonian has an entirely different phase.
The concrete obligations are independent review of the linked affine
estimate and, for the broader target, a separate uniform actual-state
estimate for the selected microscopic law. This objection defeats any
claim that the present scaling limit solves the native TOE target. The
paper instead states the precise conditional construction it establishes.

### N8 — Cross-cycle comparison

The same-delta periodic covariance source, sections 10–11, established a
proposed gapless bounded-score sector and expressly stopped before
Gaussian scaling or dispersion. This source supplies that further
implication under a varying-parameter limit; it does not retroactively
claim dispersion at its predecessor's fixed sufficient parameters.

The current-main source
`FREE_FIELD_LATTICE_TO_CONTINUUM_GAUSSIAN_MEASURE_BOUNDED_NOTE_2026-05-30.md`,
sections 0–2 and 4–5, works inside an already supplied free fermionic
Gaussian/quasi-free category. Its covariance-to-moments mechanism is
Wick rigidity under that input. Here Gaussianity is initially absent
and is obtained through the all-source squeeze before using Wick
reconstruction. That earlier source neither proves nor rules out the
present implication. This is a source-scope comparison at main revision
`5deabeb698a27c2c3f68c5df685af2521ef15307`, not an audit-status claim or
an additional load-bearing dependency.

## 11. Author review and falsifiers

The full new source and runner were reviewed personally. Twenty-six
targeted in-memory faults were detected: clock orientation; dual
temperature; lift fiber; score sign; l1 noise accumulation; omitted
conditional variance; dual covariance sign; completed-square source
scale; removed affine shift; Gaussian source scale; omitted between-coset
covariance; tilted source sign; exterior orientation; projector
normalization; midpoint phase; cell-average factor; cell field scale;
magnetic orientation; electric reflection sign; cross-residue sign;
omitted electric–magnetic cross blocks; electric noncontact sign;
quadratic dispersion; discarded Euclidean contact covariance; tail
factor; and halved supplied clock order. The frozen primary source was
not modified by these injections.

The first tilted-sign challenge was invisible to a variance-only check
because the centered law is even and its Hessian is even in the tilt.
An independent finite-difference first derivative now checks the tilted
mean as well, and detects the fault. Direct cell quadrature separately
checks the sinc factor instead of reusing it on both comparison sides.
These are author-check improvements, not independent-review results.

The theorem is falsified by failure of its stated affine input, an
incorrect lift fiber or dual temperature, loss of the uniform real-source
squeeze, a volume factor in the conditional score error, failure of the
cell-average projection limit or tightness, or an incorrect reflected
Gram factorization. The finite challenges address accessible identities
and distinctions; the quantified analytic steps require proof review.

Run the primary executable through `scripts/runner_cache.py` with its
declared 180-second timeout. There are eight finite families. Mechanical
cache and source readiness is not an audit verdict. Integrated pipeline,
strict lint and exact combined-tree evidence gates remain required
before landing; formal retained status belongs to the independent audit
path. No main merge or audit verdict is performed by this author packet.
'''

body=(PACK/'BLOCK10_GAUSSIAN_MAXWELL_SCALING_DERIVATION.md').read_text()
body=body[body.index('## 1.'):]
(ROOT/'docs'/NOTE).write_text(HEADER+body+APPENDIX)
shutil.copyfile(PACK/'block10_gaussian_maxwell_check.py',ROOT/'scripts'/RUNNER)
print(NOTE,RUNNER)
