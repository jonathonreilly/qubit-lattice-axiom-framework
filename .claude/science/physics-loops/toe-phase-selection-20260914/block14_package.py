from pathlib import Path
PACK=Path(__file__).parent
ROOT=Path('/Users/jonreilly/Documents/Codex/toe-clock-ward-quadrature-20260914')
NOTE='FINITE_CLOCK_CONDITIONAL_GAUSSIAN_MIXTURE_WARD_RESIDUAL_AND_HAAR_QUADRATURE_BOUNDED_THEOREM_NOTE_2026-09-14.md'
RUNNER='finite_clock_conditional_gaussian_mixture_ward_residual_and_haar_quadrature_2026_09_14.py'
HEADER='''---
claim_id: finite_clock_conditional_gaussian_mixture_ward_residual_and_haar_quadrature_bounded_theorem_note_2026-09-14
claim_type: bounded_theorem
claim_scope: "For finite Villain plaquette complexes with each incident link appearing once per plaquette and positive possibly anisotropic couplings, the one-link conditional weight is an exact positive mixture of translates of a wrapped Gaussian with precision equal to the incident-coupling sum. Its Fourier bound gives uniform conditional finite-clock quadrature and Ward-residual estimates. A hybrid-measure argument compares bounded-frequency integer Wilson characters with the U(1) model with an absolute error linear in link count. Growing clock order can make this error vanish; no fixed-order infrared phase or relative small-Wilson estimate is inferred."
upstream_dependencies: []
runner: scripts/finite_clock_conditional_gaussian_mixture_ward_residual_and_haar_quadrature_2026_09_14.py
---

# Uniform finite-clock Ward and Haar comparison

**Date:** 2026-09-14
**Type:** bounded_theorem
**Status:** proposed_retained

The finite-clock replacement for continuous Haar integration by parts is
an explicit Fourier-alias residual. A positive Gaussian-mixture identity
bounds it uniformly over all neighboring link values, even frustrated ones.
The same identity gives a lattice-wide absolute comparison for integer
Wilson characters with controlled link frequencies.

These are proposed analytic results, pending independent review and formal
audit. The estimates supply a bridge when clock order grows; they do not
prove that the residual is irrelevant at fixed order. No axiom, primitive,
native law or principal-flux Hamiltonian is changed.

## Status and proof obligations

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: u1_finite_clock_gauge_matter_and_controlled_tame_maxwell_bridge_bounded_theorem_note_2026-09-03
target_blocker_text: "Replace continuous Haar integration by parts by an exact finite-clock identity, and identify the error needed to transfer a controlled observable theorem."
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Independently review the mixture and hybrid comparison, then prove an infrared estimate for the fixed-clock residual and physical-score connected correlations."
conditional_surface_status: "Supplied finite Villain measure with positive couplings, incidence coefficient plus or minus one, integer bounded-frequency observables and the stated Gaussian-tail inequalities."
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "Self-contained positive-mixture, Fourier-alias and hybrid-ratio derivations with finite direct-sum challenges."
```

| Obligation | Status |
|---|---|
| Conditional Gaussian mixture | Exact completion of squares in section1 |
| Uniform Fourier and quadrature estimate | Positive mixing and explicit Gaussian alias sums in section2 |
| Discrete Ward replacement | Exact sampled derivative and explicit residual in section3 |
| Whole-lattice Wilson comparison | Positive hybrid measures and a one-step normalized ratio bound in section4 |
| High-frequency alias control | Explicit charge-N counterexample in section5 |
| Fixed-order phase and physical-score limit | Open; the displayed sufficient growing-order family is not a fixed-order theorem |

The proof has no repository theorem premises. Its finite geometry, Villain
weight and observable frequencies are supplied data. Primary literature
is context for selecting the proof obligation, not an imported phase result.

'''
APPENDIX='''

## 7. Evidence and negative-claim discipline

The self-contained executable tests five finite families: four conditional
mixtures (one,two,three and six incident factors), fifteen Ward/alias cases,
three sharp one-factor alias controls, nine two-square Wilson comparisons,
and four growing-order scales. The largest direct clock sum has7^7=823543
states. Gaussian image sums and fine-grid Fourier sums are finite numerical
checks; the written Gaussian-tail argument carries the infinite-sum claim.
No thermodynamic or continuum limit is executed by the runner.

### N1 — Distinct attempted inference routes

| Honesty | Inference attempted | Finding |
|---|---|---|
| ATTEMPTED | Replace the product by one Gaussian centered at the average background | Completion of squares retains a positive mixture over relative image integers; deleting this mixture generally changes the weight. |
| ATTEMPTED | Carry over Haar integration by parts exactly | Generic shifted one-link examples have a nonzero clock mean force; equation4 is the exact replacement. |
| ATTEMPTED | Use only the zero-mode quadrature error for all Wilson frequencies | Charge N is exactly aliased to the constant on the clock and can have a tiny Haar expectation; the shifted tail is required. |
| ATTEMPTED | Turn an absolute Wilson comparison into a relative ratio estimate | Division requires a separate nonvanishing scale or an error below the denominator; this is left explicit. |
| ATTEMPTED | Infer small total variation between the two angle measures | Clock and Haar measures are atomic and continuous respectively; only the stated observable comparison is obtained. |
| ATTEMPTED | Replace a fixed-order infrared estimate by a volume-dependent clock family | The sufficient family changes clock order and is labeled accordingly; the fixed-order phase remains open. |

No route is marked ruled out by prior retained authority. These are tests
of different inference steps, not independently established physical walls.

### N2 — Dependence

The mixture identity underlies both Fourier bounds and the hybrid argument;
they are not independent proofs of a phase. The growing-order estimate is
sufficient for specific absolute observable errors. The relationships among
fixed-order irrelevance, actual-Hamiltonian phase and native-law selection
remain unknown. No failed comparison is promoted to an axiom obstruction.

### N3 — Hidden assumptions

Every plaquette containing the link uses coefficient plus or minus one;
repeated-incidence self-wrapping complexes are excluded. Couplings are
positive, and fixed or integrated boundary links are treated consistently.
The simple Ward bound assumes a Fourier polynomial with the stated degree.
An exponential of a nonlinear score has no such automatic frequency bound.
The hybrid estimate uses the same plaquette law and normalized a priori
measures at every step. It gives absolute errors, not relative Wilson ratios.

### N4 — Matching residuals

The single-link positive mixture matches the actual Villain conditional
weight, including arbitrary neighboring angles. The nonzero force controls
match the finite-clock sampling operator. The two-square gauge complex
checks actual integer boundary characters by direct link enumeration and
separate plaquette sums. It is not a simulated four-dimensional phase.
Driver's continuous-angle argument is contextual; the exact alias formula
shows which step changes. Dario-Wu's rotator theorem is not imported as a
finite-clock gauge theorem.

### N5 — Resolution

Substantive per-element, per-site, per-mode, per-block and lattice-wide
lines are printed. The finite sums execute those domains. Uniform infinite
image tails, all-background estimates and the general E-link telescoping
argument are checked and not executed; their proofs remain subject to
independent review. Finite PASS lines do not establish universal validity.

### N6 — Partial progress

The estimate can transfer a separately proved continuous-angle conclusion
when its observable degree and absolute accuracy fit the stated bound.
Fixed-order renormalization, a direct score-cumulant estimate, and exact
finite-group identities remain alternatives. The small conditional residual
has not been proved irrelevant in an infrared limit.

### N7 — Steelman

A reviewer should object that the clock order grows with the volume and
that an absolute Wilson error can be useless when its expectation is very
small. Both objections are correct and restrict the conclusion. The result
still supplies the exact finite-clock derivative residual and a uniform
comparison on its stated observable class. It does not manufacture a phase.

### N8 — Cross-cycle comparison

The earlier growing-coupling Maxwell construction used direct lattice
Gaussian estimates; this result instead bounds the finite-angle quadrature
step. The fixed-coupling image-noise distinction remains relevant to any
full-field continuum theorem. A Gaussian current-sector limit still does
not by itself identify all physical photon observables. These results are
compatible and none forces an axiom change.

## 8. Personal review status

All work and checks were performed personally without subagents. Distinct
product/mixture, derivative/Fourier, and direct-link/plaquette calculations
challenge the derivation. Independent proof review, formal audit and main
landing remain pending. The next scientific obligation is fixed-law control
of the physical score or a carrier-preserving connected-defect expansion.
'''
body=(PACK/'BLOCK14_CLOCK_WARD_QUADRATURE_DERIVATION.md').read_text();body=body[body.index('## 1. Positive conditional mixture'):]
(ROOT/'docs'/NOTE).write_text(HEADER+body+APPENDIX)
r=(PACK/'block14_clock_ward_check.py').read_text().replace('import itertools,json,math','import itertools,json,math\nAUDIT_TIMEOUT_SEC = 180')
r=r[:r.index("if __name__=='__main__':")]+'''if __name__=='__main__':
 rows=run()
 print('per_element: executed positive relative-image Gaussian mixtures match direct products in one,two,three and six factor cases; infinite tails are checked and not executed.')
 print('per_site: executed fifteen conditional finite-clock derivative identities match Fourier aliases; generic mean forces are nonzero and obey the uniform bound.')
 print('per_mode: executed charge-N clock characters alias to one while their Haar expectations can be tiny; bounded-frequency tails are checked explicitly.')
 print('per_block: executed nine two-square gauge Wilson expectations match independent plaquette sums, with direct clock sums up to823543states.')
 print('lattice_wide: checked and not executed as an infinite-volume theorem; four growing-clock scales evaluate the uniform E-link comparison; arbitrary lattices and infinite-volume convergence are checked and not executed.')
 print(json.dumps(rows,indent=2))
'''
(ROOT/'scripts'/RUNNER).write_text(r)
print('source',len((HEADER+body+APPENDIX).splitlines()),'runner',len(r.splitlines()))
