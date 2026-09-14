"""Package the logarithmic improvement with its explicit provisional dependency."""
from pathlib import Path
import shutil
PACK=Path(__file__).parent
ROOT=Path('/Users/jonreilly/Documents/Codex/toe-direct-clock-wilson-20260914')
NOTE='FINITE_CLOCK_LOGARITHMIC_MAXWELL_SCALING_AND_GLOBAL_DEFECT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-09-14.md'
RUNNER='finite_clock_logarithmic_maxwell_scaling_and_global_defect_boundary_2026_09_14.py'
HEADER='''---
claim_id: finite_clock_logarithmic_maxwell_scaling_and_global_defect_boundary_bounded_theorem_note_2026-09-14
claim_type: bounded_theorem
claim_scope: "For the supplied finite-clock Villain law on equal even four-tori, the explicit logarithmic family beta=ceil(4log(2L^4)), N=8beta has the score-field Gaussian Maxwell limit with all smeared moments, principal-flux distribution limit, and relative separated rectilinear Wilson-loop Coulomb limit, conditional on the direct source's integer geometry and continuum/OS lemmas. Local defect tails and injected integer-current theta sums replace volume-dimensional packing; a bounded line-current potential controls thin Wilson sources. At fixed beta the positive lift's globally exact sector instead has exponentially small probability, and uniform dual theta smallness requires growing sigma. Those are boundaries of global defect/theta removal, not obstructions to a fixed-law infrared phase or to the axioms."
upstream_dependencies:
  - finite_clock_direct_maxwell_scaling_and_coulomb_wilson_interactions_bounded_theorem_note_2026-09-14
runner: scripts/finite_clock_logarithmic_maxwell_scaling_and_global_defect_boundary_2026_09_14.py
---

# Logarithmic finite-clock Maxwell scaling and global defect removal

**Date:** 2026-09-14
**Type:** bounded_theorem
**Status:** proposed_retained

A supplied finite-clock Villain family with coupling and alphabet of order
logarithmic in the volume already has the Maxwell and external Coulomb
limits specified below. The proof uses local defect quantization and
integer-current theta estimates. It also identifies the limitation of this
method: at fixed coupling, a completely defect-free lift has probability
tending to zero. Positive defect density does not rule out a massless phase.

This is a proposed theorem pending independent review and formal audit.
The direct source linked below is also provisional; its appearance in a
PR does not establish its proof. No axioms or primitive registries change.

## Status and dependency map

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: u1_finite_clock_gauge_matter_and_controlled_tame_maxwell_bridge_bounded_theorem_note_2026-09-03
target_blocker_text: "Reduce the supplied Maxwell family's growing microscopic resources and distinguish a fixed-law phase from global defect exclusion."
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Independently review the local-tail and theta derivation, then obtain fixed-law connected-correlation estimates rather than require zero defects everywhere."
conditional_surface_status: "Uses the explicitly provisional direct source's integer geometry, physical field discretization, Green limit and Gaussian OS construction."
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "New analytic finite-volume estimates imply an explicit logarithmic family, with finite checks and narrow method-boundary countercontrols; neither dependency nor conclusion has formal retained status."
```

The sole scientific repository premise is
[the direct finite-clock source](FINITE_CLOCK_DIRECT_MAXWELL_SCALING_AND_COULOMB_WILSON_INTERACTIONS_BOUNDED_THEOREM_NOTE_2026-09-14.md),
originally committed at44faa4d4ce09b8634726cef62a84146f940eb233.
Its precise uses are:

| Imported lemma | Use here | Status |
|---|---|---|
| Positive lifted clock law, constant fibers and saturated integer curl lattice | Defines M and identifies the exact sector | Provisional proof, independent review pending |
| Four-torus Hodge norm, integer periods and minimum dual-vector length | Local defect quantization and source condition(A) | Provisional proof, independent review pending |
| Midpoint cell averages and continuum Hodge limit | Converts source covariance to the Maxwell field | Provisional proof, independent review pending |
| Score conditioning and principal-flux coupling | Transfers to actual bounded clock observables | Provisional proof, independent review pending |
| Heat-kernel estimates and off-diagonal periodic Green limit | Bounds line potentials and separated Wilson pairings | Provisional proof, independent review pending |
| Relative Wilson ratio algebra, subsequent time/return-charge limits and explicit Gaussian OS quotient | External Coulomb interaction and two transverse linear modes | Provisional proof, independent review pending |

This source derives the improved probability bounds, integer-current theta
majorant, potential-source estimate, logarithmic parameter sequence and
global-method lower bounds. It imports no all-affine covariance theorem.
The physical model, varying alphabet, coupling, spacing and probe strengths
are supplied. A fixed-N=3 Hamiltonian phase, native law selection and
dynamical charged matter remain open.

'''
APPENDIX='''

## 9. Finite challenge record and scope

The self-contained executable is
`scripts/finite_clock_logarithmic_maxwell_scaling_and_global_defect_boundary_2026_09_14.py`.
It reads no repository scientific inputs or helper runner. Numerical theta
and image sums are finite challenges, not certifications of infinite tails.
The analytic tail bounds and continuum implications are in the proof.

| Family | Executed domain and distinct check |
|---|---|
| Cochain quantization | Side-four and side-six tori; cube incidence norms, even-sublattice disjoint supports, angle/integer lift, closed flux and nonclosed harmonic control |
| Image atoms and single-cube law | Four beta values and61 shifts each; four gauge-fixed cube laws compared by integer convolution, root-of-unity filtering and direct clock-angle sums |
| Integer-current theta and source bound | Three independently projected plaquettes, all27 small coefficient combinations, five random source pairings, scalar Poisson duality, and a highest-mode equality witness for the source constant |
| Affine characteristic | Three-face shifted integer lattice at four variances; complex direct sums versus dual Poisson sums, with the relative bound invoked only when its hypotheses hold |
| Thin loop potential | Square loops at inverse meshes2,4,6,8 in finite physical boxes; four-torus FFT current energies and scalar Green envelopes, plus a charge-alias countercontrol |
| Logarithmic sequence | Six values of L from4 through1024; explicit theta/defect/wrap rates and the principal-moment exponent boundary |
| Conditional defect count | Two conditional Bernoulli families and their mixture, with a separate control against inferring unconditional independence |

The finite cube probabilities of no defect are approximately0.28944,
0.45765,0.64649 and0.78213 at the disclosed(N,beta) values. The loop
surface norms increase from2 to8 while their potential supremum norms
range from0.17089 to0.23655; these finite boxes do not execute the
infinite-volume continuum limit. The actual proof of the uniform potential
bound is(6.1)–(6.3). A highest-frequency transverse integer edge current
saturates both the operator norm and the source-exponent inequality, so
its numerical equality checks the otherwise easy-to-miss factor32.

## 10. No-Go Discipline Gate

The negative result is restricted to global lift-defect exclusion and
uniform dual-theta smallness. It is not a fixed-law phase no-go, does not
exhaust microscopic routes, and forces no change to the axioms.

### N1 — Materially distinct attempts

| Honesty | Attempt and mathematical mechanism | Disposition |
|---|---|---|
| ATTEMPTED | Keep beta fixed while suppressing every integer image defect | Conditional atom bounds and disjoint cube faces yield(7.2); finite image and mixture checks challenge the mechanism. |
| ATTEMPTED | Remove only magnetic cubes and silently discard global topology | A closed nonzero integer period survives dk=0. Section2 retains six harmonic tests; the cochain family executes that countercontrol. |
| ATTEMPTED | Use the original dimension-packing estimate to demand volume-order couplings | The injective integer-current map replaces it by a scalar theta product and yields the explicit logarithmic family. |
| ATTEMPTED | Control thin-loop relative errors by a bounded surface norm | The surface norm diverges; section6 instead proves a bounded Green-current potential. The Fourier energy also gives a lower bound on the projected norm. |
| ATTEMPTED | Extend that potential bound to arbitrary clock charges | Charge q=N is identically aliased and violates the source-radius hypothesis in the declared plaquette control. |
| ATTEMPTED | Transfer every principal-flux moment through the rare-wrap event at coefficient4 | The Holder bound has positive volume exponent at degree19. The proof retains all score moments, limits the principal claim, and states how to strengthen the chosen family. |
| ATTEMPTED | Treat conditionally independent image labels as unconditionally independent defects | Section7 integrates uniform conditional domination; the finite mixture has strictly positive unconditional covariance. |

These are different mechanisms, not repetitions counted as independent
science. No row is marked ruled out by prior retained authority.

### N2 — Relations and open dependencies

The global defect and dual theta bounds are both obstacles to this
particular proof strategy; neither is shown equivalent to a physical phase
criterion. Their model parameters satisfy sigma=N^2/(4pi^2 beta), so they
are explicitly coupled rather than counted as independent walls. Native
law selection, the fixed-N=3 Hamiltonian phase and dynamical matter remain
open. No implication between those three physical obligations is established
here, and their independence is unknown. The direct source is a provisional
mathematical dependency, not an independently checked authority.

### N3 — Hidden-condition scan

The model is the supplied isotropic Villain law on equal even four-tori,
L>=4, with all integer image labels retained and ordinary cochain norms.
Source conditions(A) or(B), eta_sigma<1 and the displayed logarithmic
sequence are explicit. The physical limit has a->0 and aL->infinity.
Wilson loops have a fixed finite number of straight segments, contractible
integer currents, fixed finite real strengths rounded to integer charges,
and positive physical separation for their cross pairing. Large-time and
return-charge limits follow the continuum limit. A probability about the
auxiliary positive lift is not identified with a physical phase criterion.
The principal-flux all-moment limitation is explicit. No rate of native
record formation, fixed alphabet, continuum covariance or Wick closure is
quietly added to the axioms.

### N4 — Residual matching

| Source or witness | Exact residual | Matching use |
|---|---|---|
| Direct finite-clock source, sections1–3 | Integer lift, saturation and Hodge geometry | Same torus, clock law and source normalization |
| Direct source, physical-field and Green/OS sections | Limit of the Gaussian comparison and relative loop algebra | Same observables and limit order; its proof remains provisional |
| This source, local cube and scalar theta derivation | Replace volume-dimensional packing | Explicit finite-volume analytic inequalities |
| Closed harmonic flux, aliased plaquette and conditional-mixture controls | Specific missing-hypothesis inferences | Narrow countercontrols, never physical-phase counterexamples |
| Driver1987, closed-test current-sector theorem | Comparison with a fixed-coupling literature route | Context only; no full-field or finite-clock theorem is imported |

### N5 — Resolution and rhetoric

The primary runner reports five substantive resolution lines. Scalar
probabilities and phases are per-element checks; cube geometry is per-site;
Fourier current potentials are per-mode; declared finite tori and mixtures
are per-block. The arbitrary-volume and continuum statements are checked
and not executed: the written estimates bear them, subject to review.
Finite agreement and deliberate-fault detection do not constitute an audit
or prove an infinite-volume claim. The global boundary is never described
as excluding a Coulomb phase or forcing an axiom update.

### N6 — Partial paths

The logarithmic family is a constructive partial path using the same
supplied finite-clock law. A local treatment of positive defect density,
renormalized connected correlations, a continuum current identity with a
verified observable scope, or a multiscale argument could support a
fixed-law phase without globally removing defects. These are open routes,
not discharged lemmas. This note makes no claim that approved primitives
cannot help, introduces no primitive and changes no axiom or registry.

### N7 — Steelman

A hostile reviewer should insist that an exponentially unlikely globally
clean configuration says little about long-distance physics: ordinary
phases contain a positive density of local excitations. That criticism is
correct and defeats any broader negative reading. The construction also
still chooses N and beta as functions of volume and supplies the probability
law and external probe strengths; reducing their growth does not select
those quantities natively. Finally, the source depends on unreviewed
integer/continuum lemmas. The stated result keeps every limitation.

### N8 — Cross-cycle comparison

The direct source's beta proportional to volume was a sufficient choice,
not a lower bound; this note replaces it constructively. The earlier
fixed-parameter covariance route does not require zero defects everywhere
and is not contradicted. Bare finite-penalty defects in the earlier quantum
Hamiltonian are a different model and observable; its density result is
not imported as the witness here. No old wall is recounted as a new
independent obstruction.

## 11. Author review and non-claims

All work in this campaign was performed personally, without subagents.
The author rederived the source-potential bound with a saturating
highest-frequency current, compared the three single-cube representations,
and retained the harmonic and conditional-independence countercontrols.
A first draft's potential implication of all principal-flux moments was
restricted after checking the volume exponent. The shifted complex phase,
integer charge alias and actual source conditions remain explicit.
Independent proof review and the formal audit path are pending.

There is no selected native probability law, fixed-N=3 phase, dynamical
charged matter, non-Abelian sector, empirical coupling prediction, gravity,
Born-rule derivation, completed TOE or forced axiom update in this result.
'''
body=(PACK/'BLOCK12_LOGARITHMIC_SCALING_DERIVATION.md').read_text()
body=body[body.index('## 1. Target and leverage'):]
body=body.replace('## 8. Pending checks and primary comparison', '## 8. Primary-source comparison')
body=body[:body.index('Need challenge local cube norms')]+'''Driver's [author-hosted1987 paper](https://mathweb.ucsd.edu/~bdriver/DRIVER/Papers/Drivers_Papers/A1-U%281%29_4-Lattice.pdf),
Commun.Math.Phys.110,479–501, was read in full extracted text (23pages);
page484 was also visually checked because its formula extraction was poor.
Theorems4.2–4.5 concern closed test two-forms, equivalently the current
d*F. Their hypotheses include a continuous U(1) a priori measure and
specified unique or invariant/extreme Gibbs states, or Wilson-like actions
with the further qualifications stated there. They do not supply a
finite-clock full-field theorem. This is a comparison to an established
method, not a claim of novelty for continuum electromagnetism or a theorem
premise here. The present source obtains a different, explicitly varying
finite-clock family using the direct elementary bounds above.
'''
(ROOT/'docs'/NOTE).write_text(HEADER+body+APPENDIX)
shutil.copyfile(PACK/'block12_logarithmic_scaling_check.py',ROOT/'scripts'/RUNNER)
print('note lines',len((HEADER+body+APPENDIX).splitlines()))
