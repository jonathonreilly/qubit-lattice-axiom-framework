"""Assemble a self-contained direct scaling source and finite checker."""
from pathlib import Path
import shutil

PACK=Path(__file__).parent
ROOT=Path('/Users/jonreilly/Documents/Codex/toe-direct-clock-wilson-20260914')
NOTE='FINITE_CLOCK_DIRECT_MAXWELL_SCALING_AND_COULOMB_WILSON_INTERACTIONS_BOUNDED_THEOREM_NOTE_2026-09-14.md'
RUNNER='finite_clock_direct_maxwell_scaling_and_coulomb_wilson_interactions_2026_09_14.py'

HEADER='''---
claim_id: finite_clock_direct_maxwell_scaling_and_coulomb_wilson_interactions_bounded_theorem_note_2026-09-14
claim_type: bounded_theorem
claim_scope: "For the supplied isotropic four-dimensional finite-clock Villain law on equal even tori, explicit dimension-dependent theta estimates at beta=64L^4 and N=8beta give a Gaussian Maxwell random-distribution limit of bounded score and principal-flux fields as spacing tends to zero and physical side tends to infinity. Integer-charge Wilson-loop ratios for separated contractible rectilinear loops converge with relative error control to the Maxwell line-current functional, whose subsequent temporal-rectangle limit gives Coulomb interactions between external probes. The explicit Gaussian positive-time quotient has two transverse modes with energy |p|. No affine-covariance phase theorem is assumed, and no fixed-N=3 phase, native probability law, charged matter or axiom update is inferred."
upstream_dependencies: []
runner: scripts/finite_clock_direct_maxwell_scaling_and_coulomb_wilson_interactions_2026_09_14.py
---

# Finite-clock Maxwell scaling and Coulomb Wilson-loop interactions

**Date:** 2026-09-14
**Type:** bounded_theorem
**Status:** proposed_retained

The supplied finite-clock Villain family at beta=64L^4 and N=8beta
has a Gaussian Maxwell scaling limit for actual bounded score and
principal-flux observables, with controlled normalized charged Wilson
loops and subsequent Coulomb interactions between external probes.
This note derives that statement directly from finite-dimensional
integer cochain geometry and theta estimates. Independent proof review
and formal audit are pending.

The coupling growth is deliberately conservative. It provides an explicit
construction without assuming a uniform finite-coupling phase theorem.
The microscopic law, varying clock order, field normalization and probe
charges are supplied. This is a result about that family, not a selection
of its law from the framework axioms or a construction of charged matter.

## Status, inputs and proof obligations

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: u1_finite_clock_gauge_matter_and_controlled_tame_maxwell_bridge_bounded_theorem_note_2026-09-03
target_blocker_text: "Construct an actual finite-clock state sequence with a Maxwell field and controlled charged-probe interactions, keeping microscopic law selection distinct."
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Independently review the direct integer/theta proof and relative Wilson limit, then address fixed-alphabet dynamics and native law selection."
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Explicit finite-volume relative error bounds and analytic continuum consequences for a completely supplied scaling family, challenged by finite independent calculation paths."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

There are no imported repository theorem premises. The integer
contraction, shortest-vector bounds, theta estimates, field limit,
off-diagonal Green convergence and Gaussian quotient are derived below.
The contextual target is named only as a consumer of bounded support;
its physical identification and audit status are not inputs.

| Supplied input | Role and qualification |
|---|---|
| Four-dimensional equal even cubic tori | Defines the model geometry and the norm of integral harmonic fluxes |
| Finite clock links with isotropic Villain weights | Defines the full probability law; no native law is selected |
| beta=64L^4, N=8beta, a tending to zero and aL tending to infinity | Defines a sufficient varying-alphabet weak-coupling family, not a fixed-parameter phase |
| Bounded score and principal-flux fields | Defines physical model observables and the a^-2 continuum normalization |
| Fixed real probe strengths g_i and integer q_i nearest g_i sqrt(beta) | Defines the external Wilson probes; no empirical coupling is imported or derived |

| Proof obligation | Disposition | Result used downstream |
|---|---|---|
| Exact positive lift and constant clock fiber | Derived in section 1, including composite N | Centered full-rank lattice Gaussian |
| Saturation of the integer curl lattice | Integral contraction in section 2 | One affine coset for each perpendicular quotient vector |
| Uniform nonzero lattice-vector length | Section 3, integer currents and integral harmonic flux | Dimension-dependent theta packing applies |
| Exact-sector weight and relative source control | Sections 4–5, Poisson and packing | Both absolute and refined relative characteristic estimates |
| Actual physical-field convergence | Section 6, score conditioning, principal-flux coupling, cell averages and tightness | Gaussian Maxwell random distribution and all smeared moments |
| Wilson character and current energy identities | Section 7 | Genuine clock loops with surface-independent Gaussian energy |
| Uniform off-diagonal periodic Green limit | Section 8, heat kernels and zero-mode control | Continuum line-current pairing for separated loops |
| Relative loop ratios and time limit | Section 9, separate limit orders | Coulomb interaction of external probes |
| Positive-time physical mode count | Section 10, explicit Gaussian Gram and Wick construction | Two transverse linear modes and symmetric Fock quotient |

No terminal lemma in this graph is left as an assumed phase conclusion.
The strongest outstanding scientific validation is independent review
of the full derivation. The strongest physical obligations remain a
selected native probability law, a fixed-alphabet Hamiltonian phase and
dynamical charged matter; none is a premise or a conclusion of this
supplied-family theorem.

'''

APPENDIX='''

## 11. Primary-source comparison and finite challenges

The Green-function mechanism is standard lattice potential theory.
Lawler and Limic's [author-hosted Random Walk draft](https://math.uchicago.edu/~lawler/srwbook10.pdf),
section 4.3, Theorem 4.3.1, PDF pages 81–83, gives the familiar
simple-random-walk asymptotic. Its four-dimensional discrete-time
constant is 2/pi^2; the rate-one-per-neighbor heat kernel used here has
total jump rate eight and therefore constant 1/(4pi^2). Section 8
derives the normalization and periodic control directly. The reference
is a primary comparison, not an imported phase theorem or a claim of
novelty for Maxwell scaling or Coulomb interactions.

The primary executable is
`scripts/finite_clock_direct_maxwell_scaling_and_coulomb_wilson_interactions_2026_09_14.py`.
It reads no external or repository scientific inputs and uses no helper
runners. The finite domains are explicit in the executable. Infinite
lattice sums there are truncated numerical challenges, not rigorous
tail certifications or executions of the analytic limiting argument.

| Check family | Actual domain and distinct calculation path |
|---|---|
| Integral contraction and short vectors | Side-four four-torus, arbitrary seeded integer cochains in degrees zero through four, period cocycles and Fourier Hodge projection of six plaquette spikes |
| Dimension-dependent packing | Finite integer lattices in ranks one, two and four versus shell bounds; four members of the explicit clock family |
| Exact source and coset mixture | Three-face cycle-incidence lattices at N=3,8,128, with explicit shifted-coset sums and dual Poisson sources |
| Actual clock Wilson characters | Three-face finite-clock toys at N=128,256,384, direct angle sums versus Gaussian current expressions, plus integer-lift and charge-alias controls |
| Uniform shifted theta source | Nonzero affine three-face shifts at four variances, direct complex characteristics versus dual phase sums |
| Green kernels and disjoint loops | Side-four FFT inverse versus heat integration; finite tori of sides 8,18,32; infinite-kernel and separated-loop refinement through inverse mesh 32 |
| Coulomb time and charge signs | Direct time quadrature and complete rectangle line quadrature versus closed formulas, followed by three large-time dipole checks |
| Positive lift and score | Composite orders 2,4,6 in the disclosed three-face toy, using independent Gaussian-image, Fourier and primal/dual moment computations |
| Midpoint cell averaging | Side-six Fourier block, direct cell quadrature and component phase identities |
| Gaussian physical modes | Full electric–magnetic covariance versus oscillatory integrals and a rank-two Gram factorization at three spatial momenta |

The finite harmonic example has squared period norm 20. The six
side-four spike tests have dual lengths approximately 0.70572436 and
quotient lengths approximately 0.70848650; the analytic lower bound is
1/4. The three finite clock toys' normalized Wilson ratios are
approximately 1.39561243, 1.33865672 and 1.34985881, agreeing with their
separately derived Gaussian expressions. These toys do not constitute
a four-dimensional phase simulation.

For the two unit square loops separated by one unit, the continuum
cross term is approximately 0.0418146955. Finite periodic inverse
meshes 2,3,4 give approximately 0.0602585682, 0.0511627221 and
0.0467371582. A separate infinite-kernel separation sum reaches
0.0418777062 at inverse mesh 32, an error about 6.30e-5. The visible
coarse-mesh errors are retained, not called precise continuum values.
The dipole energy at T=1000 is approximately 0.0466247505 versus the
limit (2-sqrt(2))/(4pi), approximately 0.0466154036.

## 12. No-Go Discipline Gate

This gate scopes a positive model theorem and its finite inference
controls. It supplies no exhaustion claim, no axiom contradiction and
no argument that another microscopic model cannot work.

### N1 — Materially distinct attempted failures

| Honesty | Object and attempted failure | Disposition and authority |
|---|---|---|
| ATTEMPTED | Integral topology: retain hidden torsion or several curl cosets with the same perpendicular image | Section 2 constructs an integer homotopy and proves saturation. The full side-four cochain identities and period cocycles independently check that mechanism. |
| ATTEMPTED | Conditional Gaussian geometry: choose an affine shift whose theta weight invalidates the mixture estimate | Sections 4–5 bound the centered theta maximum and both shifted source tails, including the complex phase and denominator. The shifted-lattice family directly challenges those formulas. |
| ATTEMPTED | Source and finite-character algebra: take arbitrary large or fractional charges while retaining the unaliased Gaussian formula | Sections 5 and 7 keep the source-radius and integer-charge hypotheses. A charge q=N gives an exactly trivial clock character, while a fractional charge changes under a 2pi lift. |
| ATTEMPTED | Observable topology: insert a thin Wilson loop directly into convergence of smeared random distributions | Sections 7–9 instead prove relative characteristic errors and a separated-current Green limit. The finite disjoint-loop sums retain their ultraviolet self terms until the normalized ratio cancels them. |
| ATTEMPTED | Infinite-volume geometry: discard the periodic zero mode or sum infinite Green images without control | Section 8 works with heat kernels, subtracts the zero mode and proves an O(L^-2) comparison before the physical limit. FFT and heat-integral computations check its normalization separately. |
| ATTEMPTED | Spectral interpretation: infer physical polarization count from the Euclidean rank alone | Section 10 includes electric reflection, magnetic orientation, cross blocks and contacts. The explicit Gram matrix and independent Fourier integrals yield rank two. |

These are six different mechanisms, not six implementations of one
route. Each disposition is this source's argument and disclosed finite
check, subject to review. None is marked ruled out by prior retained
authority and the list is not exhaustive.

### N2 — Dependency and independence accounting

The mathematical implication graph above has no open phase premise.
Its geometry, law and scaling are supplied model hypotheses. The
original relative bound (1.1) and refined bound (5.3) are not counted
as separate independent breakthroughs: both use the same shortest-vector
and theta-packing lemmas.

| Outstanding physical pair | Relation established here | Treatment |
|---|---|---|
| Native law selection / fixed-alphabet Hamiltonian phase | Neither implication is established | Both remain open; independence is unknown |
| Native law selection / dynamical charged matter | Neither implication is established | External probe insertion does not identify a matter law |
| Fixed-alphabet Hamiltonian phase / dynamical charged matter | Neither implication is established | Neither follows from this varying-alphabet free-field construction |

There is no headline count of independently closed framework walls.
The simultaneous scaling limit and subsequent probe time limit are
explicitly ordered; an interchange is not an additional hidden claim.

### N3 — Hidden-condition scan

The explicit conditions are equal four-dimensional even tori, L>=4,
canonical positive orientations, integer clock alphabets, the supplied
isotropic Villain law, dimension-dependent coupling inequalities and
source radius, then the particular beta=64L^4 and N=8beta sequence.
Physical spacing shrinks while aL grows. Field tests use cell integrals;
thin loops instead have positive separation, bounded physical length
and controlled integer spanning area. Charges are integers rounded
from supplied g_i sqrt(beta). Temporal rectangles are disjoint and
their closing paths remain separated. Their T limit follows the
continuum/infinite-volume limit, and removing return charges comes
afterward. The Gaussian positive-time construction has strict
positive-time support and keeps the electric contact term. No exact
transfer logarithm, phase uniqueness, native Born rule or fixed-N
universality is assumed.

### N4 — Residual matching

| Source or witness | Residual addressed | Exact matching use |
|---|---|---|
| This source sections 2–3 and the primary cochain family | Integral curl saturation and shortest quotient/dual vectors | Same oriented four-torus and integer modules |
| This source sections 4–5 and shifted-source family | Relative characteristic error after affine coset mixing | Same Gaussian/source conventions, with source-radius hypothesis retained |
| This source sections 7–9 and clock/Green families | True integer Wilson characters, self-term cancellation and Coulomb normalization | Same character and separated-current observable; finite toys are labeled |
| Lawler–Limic section 4.3, Theorem 4.3.1 | Standard infinite-volume Green normalization | Primary comparison only; jump-rate conversion is explicit and the periodic argument is derived here |
| Charge alias, fractional-lift and polarization witnesses | Specific inferences with missing hypotheses | Narrow existence controls, never counterexamples to the framework or a fixed-N phase |

No differently scoped no-go or rejected-branch conclusion is imported.
The executable is self-contained and the entire new analytic proof is
carried in this PR's source delta.

### N5 — Resolution and rhetoric

The executable resolves scalar theta/character identities per element,
integral cochain mechanics per site, Fourier and reflected kernels per
mode, and the named finite tori and toys per block. Lattice-wide theta
bounds, field convergence and relative thin-loop limits are checked
and not executed: they are consequences of the written estimates,
not numerical extrapolations. Its canonical cache has all five
substantive resolution lines. No finite count or error threshold is
presented as universal proof or independent review.

### N6 — Partial closure and primitive boundary

The result supplies a concrete Maxwell field and external Coulomb
functional in a chosen finite-clock sequence. A fixed alphabet, an
identified Hamiltonian, or a native formation law remain possible
future routes with distinct obligations. This note makes no claim
that an existing primitive cannot help, proposes no additional axiom,
and changes no primitive registry or framework text. Supplied probe
strengths and coordinate units remain supplied quantities.

### N7 — Steelman

A hostile reviewer should say that letting N and beta grow rapidly
with volume is a carefully chosen free-field limit, not evidence that
the original fixed-carrier interacting dynamics realizes electromagnetism.
The Wilson calculation inserts external currents and cancels their
self terms by normalization; it does not prove the existence of charged
particle states. Those objections are correct against a native-TOE or
matter claim. The terminal obligations remain a controlled fixed-carrier
state/dynamics identification and a matter construction. Inside this
stated family, the strongest mathematical attacks are failure of
integral saturation, nonuniform shifted theta control or the periodic
Green comparison; sections 2–9 make each step explicit for review.

### N8 — Cross-cycle comparison

The pending periodic-clock covariance and conditional score-scaling
sources on PR8127 at `d46526dc07fc1f4f6530c7b4d98c1d5feb8f6eee` use a
uniform all-affine covariance estimate. They allow less restrictive
scaling, and the fixed-parameter source has a separate observable-gap
conclusion. This note uses dimension-dependent packing on a stronger
sequence and does not import either source as a premise. Its simpler
proof does not validate, replace or refute their uniform phase estimate.

The current-main source
`FREE_FIELD_LATTICE_TO_CONTINUUM_GAUSSIAN_MEASURE_BOUNDED_NOTE_2026-05-30.md`,
sections 0–2 and 4–5, assumes the Gaussian/quasi-free category before
passing moments through covariance. This source derives Gaussianity
from a clock law and proves thin-loop ratios separately from smeared
field convergence. The comparison is at main revision
`5deabeb698a27c2c3f68c5df685af2521ef15307`; it imports no theorem or
audit verdict and claims no earlier physical wall has been retired.

## 13. Author review, falsifiers and verification limits

The full proof and primary executable were reviewed personally. Thirty
targeted in-memory faults were detected: forward coboundary direction;
adjoint sign; circle anchor; period cocycle position; contraction
endpoint; tensor degree sign; harmonic volume factor; short-vector
operator bound; packing dimension; theta exponent; dual temperature;
perpendicular coset energy; Poisson source factor; affine phase sign;
omitted affine denominator; fractional Wilson charge; clock alias;
Green jump rate; periodic zero mode; heat zero-mode subtraction; loop
orientation; current-component contraction; Coulomb normalization;
omitted closing paths; charge-interaction sign; score sign; cell-average
factor; electric reflection; electric–magnetic cross sign; and quadratic
dispersion. The frozen primary runner was not modified by the faults.

Two initial finite precision targets were too tight at coarse spacing:
the axis Green error at distance 16 was about 1.01e-4, and the loop
cross-term error at inverse mesh 4 was about 4.92e-3. Those values are
retained above. Finer checks through distance/inverse mesh 32 and
explicit refinement comparisons replace the premature precision
expectation; the finer loop check uses a separation sum instead of a
large four-dimensional FFT allocation. No finite tolerance supplies
the analytic convergence theorem.

Falsifiers include an integer real-exact cocycle outside d Z^E, a
shorter admitted quotient vector invalidating the stated bound, a
missed coset multiplicity, failure of the uniform affine theta ratio,
loss of relative error at a permitted source, incorrect periodic
zero-mode control, or a failed reflected Gram factorization. All are
scientific proof obligations, not claims settled by bookkeeping.

The primary runner declares a 180-second timeout and has ten finite
families. Its canonical cache is produced by `scripts/runner_cache.py`.
Source/cache/N5 readiness is mechanical evidence only. Independent
proof review, integrated pipeline, strict lint and exact combined-tree
validation remain landing gates. Formal retained status belongs to
the independent audit path; this author packet performs no main merge
and changes no audit verdict, axiom or approved primitive.
'''

body=(PACK/'BLOCK11_DIRECT_GAUSSIAN_AND_WILSON_DERIVATION.md').read_text()
body=body[body.index('## 1.'):]
body=body.replace('This direct theorem has stronger coupling growth and weaker parameter\ngenerality than the preceding affine-input theorem, but eliminates\nthat provisional premise and adds actual thin charged-probe ratios.\n',
                  'The coupling growth is a sufficient condition for this direct proof;\nno volume-uniform affine-covariance theorem is a premise. The result\nalso controls actual thin charged-probe ratios.\n')
(ROOT/'docs'/NOTE).write_text(HEADER+body+APPENDIX)
shutil.copyfile(PACK/'block11_direct_wilson_check.py',ROOT/'scripts'/RUNNER)
print(NOTE,RUNNER)
