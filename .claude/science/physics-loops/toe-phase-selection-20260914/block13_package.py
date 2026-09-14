from pathlib import Path
import shutil
PACK=Path(__file__).parent
ROOT=Path('/Users/jonreilly/Documents/Codex/toe-clock-image-noise-20260914')
NOTE='FINITE_CLOCK_IMAGE_NOISE_CURRENT_SECTOR_AND_POSITIVE_TIME_OS_EQUIVALENCE_BOUNDED_THEOREM_NOTE_2026-09-14.md'
RUNNER='finite_clock_image_noise_current_sector_and_positive_time_os_equivalence_2026_09_14.py'
HEADER='''---
claim_id: finite_clock_image_noise_current_sector_and_positive_time_os_equivalence_bounded_theorem_note_2026-09-14
claim_type: bounded_theorem
claim_scope: "At fixed beta>0 and finite N>=2 in the supplied clock Villain model, the positive image lift has strictly positive uniformly bounded-below conditional variance about the actual bounded score. Under a translation-invariant periodic-limit state, macroscopic image noise has a stable conditional white-noise limit along score-field subsequences, with variance given by translation-invariant sector data and independent noise when that variance is constant. Adding independent reflection-invariant white two-form noise preserves the strict positive-time OS Hilbert space and time generator of an RP limiting field. The auxiliary lift cannot approach a pure closed Maxwell Euclidean field at fixed beta under the stated moment bound; current-sector Gaussianity alone is likewise insufficient to identify the full Maxwell physical space. These are observable/conditional-reconstruction statements, not a fixed-law photon phase theorem or an axiom obstruction."
upstream_dependencies: []
runner: scripts/finite_clock_image_noise_current_sector_and_positive_time_os_equivalence_2026_09_14.py
---

# Clock image noise, current-sector scope and positive-time reconstruction

**Date:** 2026-09-14
**Type:** bounded_theorem
**Status:** proposed_retained

The auxiliary positive lift and the actual bounded clock score differ by
conditionally independent local image noise. At fixed coupling its variance
is strictly positive. Macroscopic smearing makes that residual a white-noise
field, with an invariant-sector variance and ordinary independence when the
variance is constant. Independent white contact noise adds no states or
energies to the strict positive-time OS reconstruction of an RP field.

These are proposed analytic statements, pending independent review and
formal audit. They do not identify a fixed-law Gaussian photon phase.
A full-lift Euclidean Bianchi test and a current-only Gaussian test each
miss a relevant distinction; the explicit controls below show why.
No native probability law, axiom or primitive is selected or changed.

## Status and proof obligations

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: u1_finite_clock_gauge_matter_and_controlled_tame_maxwell_bridge_bounded_theorem_note_2026-09-03
target_blocker_text: "Identify which actual finite-clock observables must satisfy a fixed-law Gaussian photon limit, separating auxiliary image noise and Euclidean contact terms from physical states."
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Independently review the conditional-noise and OS isometry proof, then control connected correlations of the actual score on general two-form tests."
conditional_surface_status: "Fixed supplied Villain law; periodic-limit state for the Gaussian moment bound; translation invariance for invariant-sector averaging; constant sector variance for independent-noise OS equivalence; limiting RP field and its time action for the reconstruction statement."
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "Self-contained conditional-limit and Hilbert-space equivalence proofs, with finite independent-calculation challenges and explicit observable-scope countercontrols."
```

| Obligation | Disposition and precise scope |
|---|---|
| Positive image kernel and finite-periodic Gaussian domination | Derived in section1 by a constant-fiber finite-group map and Poisson summation |
| Strict image variance and uniform fixed-beta moments | Derived in section2 by two adjacent image weights and a summable Gaussian tail |
| Conditional characteristic expansion | Derived with an explicit Taylor/log remainder in section3 |
| Macroscopic conditional variance | Weighted L2 mean-ergodic argument in section3, retaining invariant-sector randomness |
| Existence of score subsequences | Uniform L2 test bounds and local negative-Sobolev tightness; no Gaussianity is inferred |
| Independent white-noise OS equivalence | Conditional expectation isometry with dense exponential-cylinder range in section4 |
| Current-sector inference control | Explicit white/Maxwell same-current construction and a nonzero magnetic OS vector in section5 |
| Actual fixed-law photon covariance and higher connected correlations | Open; the conditional equivalence theorem does not supply them |

There are no repository theorem premises. The finite Villain family,
geometry and state hypotheses are supplied mathematical data. The primary
comparison at the end names Driver's established restricted theorem without
importing a broader result. The finite executable is self-contained.

'''
APPENDIX='''

## 7. Primary comparison and finite evidence

Driver's [author-hosted paper](https://mathweb.ucsd.edu/~bdriver/DRIVER/Papers/Drivers_Papers/A1-U%281%29_4-Lattice.pdf),
*Convergence of the U(1)_4 Lattice Gauge Theory to Its Continuum Limit*,
Commun.Math.Phys.110(1987),479–501, was read in full extracted text,
23pages, with journal page484 also visually checked. Definitions3.3–3.4
specify the score-like field h'(dtheta) and current d*F. Theorems4.2–4.5
use closed test two-forms, with their stated unique/extreme/invariant state
or Wilson-like hypotheses. Lemma5.1 uses integration by parts against
continuous U(1) Haar measure. Section5 here provides a direct observable
scope control, not a criticism of Driver's stated conclusion and not a
novelty claim for Gaussian current-sector limits.

The self-contained primary executable is
`scripts/finite_clock_image_noise_current_sector_and_positive_time_os_equivalence_2026_09_14.py`.
It reads no scientific repository inputs or helper scripts. Its finite
Gaussian-image and Fourier sums are numerical challenges, not certifications
of infinite tails or executions of an infinite-volume theorem.

| Family | Actual domain and comparison |
|---|---|
| Conditional moments and score | Five beta values0.03,0.1,0.4,1,3 and121 plaquette angles each; Gaussian-image moments versus Fourier scores and the explicit variance lower bound |
| N=2 score alias | Both clock plaquette values at four beta values, contrasted with N=3,beta=1,angle2pi/3 |
| Conditional characteristic limit | Three image laws and array sizes2^4,3^4,4^4,5^4,8^4; exact finite-sum characteristic logarithms versus their explicit centered Taylor bound |
| Invariant-sector mixture | A two-angle conditional-noise toy at three array sizes, with a correlated bounded variable and a nonzero fourth-cumulant/central-state control |
| White-noise OS map | Three positive times, finite exponential Gram matrices, time-shift intertwining and a temporally colored-noise countercontrol |
| Current-sector blindness | Three four-momenta in the exterior algebra, two independent temporal Fourier integrals and a differential-contact regularization check |

At beta=3 the conditional variance ranges in these tests from approximately
4.54e-24 near zero angle to29.61 at pi. The latter exceeds one: the
centered global Gaussian bound is not an all-conditional variance bound.
The two-sector toy has fourth cumulant approximately10.57387 and a
squared-noise central OS norm approximately3.52462. This toy is not claimed
to be a Gibbs state or a phase of the clock model; it challenges replacing
a random invariant variance by its average. The colored-noise example
changes the proposed Gram intertwining by approximately0.07498.

## 8. No-Go Discipline Gate

The negative sentences concern specified observables, conditional moments
and the scope of particular inference steps. They do not exclude any
fixed-law phase or force an axiom change.

### N1 — Materially distinct attempted inferences

| Honesty | Inference tested | Exact disposition |
|---|---|---|
| ATTEMPTED | A fixed-beta positive lift becomes a strictly closed pure Maxwell Euclidean field | Adjacent image weights give a positive conditional white variance; the coexact-test second-moment argument rules out that auxiliary-field conclusion under the stated moment bound. |
| ATTEMPTED | The global Gaussian bound makes every image conditional variance at most one | The shifted pi-angle Gaussian has variance approximately29.61 at beta=3; the periodic-state and conditional statements are kept distinct. |
| ATTEMPTED | Conditional independence already means exact Gaussian noise on a finite block | The actual finite characteristics have nonzero remainders; the displayed Taylor estimate is used before the macroscopic limit. |
| ATTEMPTED | Translation invariance permits replacing sector variance by its mean | The stable characteristic identity retains invariant data; an explicit two-sector toy has different joint characteristics and a nonzero fourth cumulant. |
| ATTEMPTED | Any local-looking added noise leaves the OS space unchanged | Temporally colored noise has a nonzero cross-reflection covariance and fails the isometry; independent white noise has a proved dense-range map. |
| ATTEMPTED | A Gaussian current sector identifies full Maxwell photon states | White noise and Maxwell have the same current law; their full positive-time spaces differ, as the magnetic witness shows. |
| ATTEMPTED | Vanishing of the chosen N=2 score means every clock observable is trivial | Evenness and periodicity kill this score only; no inference about the full clock algebra is made. |

These mechanisms are not counted as independent physical walls. No route
is marked ruled out by prior retained authority.

### N2 — Dependency accounting

The moment bound, state invariance, invariant-sector variance and RP/time
reconstruction assumptions have different explicit roles. Translation
ergodicity is sufficient for constant variance but is not necessary;
constant invariant variance is the actual independence condition. No
independence between the remaining native-law, fixed-N=3 Hamiltonian phase
and matter obligations is established. They remain open and their mutual
implications are unknown. The white-noise equivalence cannot be used to
supply a missing Gaussian or RP limit by circular reasoning.

### N3 — Hidden conditions

The image law is the supplied Villain Gaussian kernel at fixed positive
beta and finite integer N. Periodic-limit states are required where the
global MGF is used. The averaging theorem assumes translation invariance
and retains random invariant-sector data. The OS theorem assumes a
reflection-invariant RP limiting law and its time action; the added noise
is independent, white, and has constant covariance compatible with the
tensor reflection. Tests are strictly in positive time. The current-only
comparison uses closed two-form tests. No thin Wilson-loop limit, lattice
Hamiltonian identification, full Lorentz invariance, native Record law or
charged matter is silently inferred.

### N4 — Residual matching

| Witness | Residual addressed | Matching scope |
|---|---|---|
| Adjacent Gaussian images and the exact moment split | Can fixed-beta lift noise be set to zero? | Same supplied conditional image kernel and normalization |
| Weighted conditional characteristic expansion | When does that noise become white and independent? | Macroscopic smooth smearing; invariant variance retained |
| Positive-time conditional expectation map | Does independent white contact noise add states? | Same RP algebra and constant independent noise hypotheses |
| White/Maxwell current equality and magnetic norm | Is the restricted current limit a full-field limit? | Explicit Gaussian fields on the same test spaces |
| Driver1987 | Established continuous U(1) current-sector method | Primary context only; no finite-clock or full-field theorem imported |
| N=2 score and random-variance toy | Observable alias and missing ergodic factorization | Narrow controls; the toy is not a claimed clock Gibbs phase |

### N5 — Resolution

The runner prints substantive per-element, per-site, per-mode, per-block
and lattice-wide lines. The finite image laws and Fourier kernels are
executed on their stated domains. The continuum conditional-noise theorem,
weighted ergodic limit and completed OS isometry are checked and not
executed: their written arguments carry them, pending independent review.
No numerical count is presented as a theorem proof or audit verdict.

### N6 — Partial paths

The result supplies a way to compare two precisely defined observables in
a candidate fixed-law scaling limit. It leaves open actual-score Gaussianity
and its nonlocal covariance, or an alternative observable that identifies
physical modes. The random-sector variant can instead retain its invariant
data explicitly; averaging them away is not required. No statement says
that approved primitives cannot help, and no axiom or registry is changed.

### N7 — Steelman

A hostile reviewer should say that the score's limit has not been identified
and the independent-noise theorem cannot manufacture it. That is correct.
A nonergodic variance mixture can add central states, and a different clock
observable can reveal physics absent from this score. These criticisms
prevent a fixed-law photon claim and are included in the source's scope.
They do not invalidate the conditional characteristic calculation or the
isometry under its explicit independent white-noise hypotheses.

### N8 — Cross-cycle comparison

The growing-beta Maxwell construction removes image noise as beta grows;
it is not contradicted by a fixed-beta variance lower bound. The earlier
global-defect boundary concerns an entire lift configuration; the local
noise/OS relation here is a distinct observable calculation. The existing
fixed-clock covariance route may include contact terms and is not disproved.
No earlier failed candidate is promoted to an axiom wall.

## 9. Personal review and outstanding work

The proof and executable were produced personally without subagents.
The finite image/Fourier, characteristic/Taylor, matrix/conditional-average
and Fourier/Laplace comparisons use distinct calculation paths. They are
author checks, not independent review. Formal audit and independent proof
review remain pending. The next load-bearing problem is a fixed-law bound
on the actual score's higher connected correlations and the identification
of its nonlocal covariance. No TOE completion, forced axiom update,
physical parameter prediction or dynamical matter construction is claimed.
'''
body=(PACK/'BLOCK13_IMAGE_NOISE_AND_OS_DERIVATION.md').read_text();body=body[body.index('## 1. Positive lift'):]
(ROOT/'docs'/NOTE).write_text(HEADER+body+APPENDIX)
shutil.copyfile(PACK/'block13_image_noise_os_check.py',ROOT/'scripts'/RUNNER)
print('source lines',len((HEADER+body+APPENDIX).splitlines()))
