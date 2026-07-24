---
claim_id: finite_regge_plaquette_scattering_diagnostics_cycle576_bounded_theorem_note_2026-07-22
claim_type_author_hint: bounded_theorem
status_authority: independent_audit_lane_only
direct_effective_status_change_allowed_from_this_note: false
---

# Finite Regge, Plaquette, and Scattering Diagnostics — Cycle 576

**Date:** 2026-07-22
**Claim type:** bounded_theorem
**Authority:** none
**Audit:** unset
**Status authority:** independent audit lane only; effective status is
pipeline-derived.
**Source-note proposal:** this note proposes a bounded execution claim and does
not set an audit verdict or downstream status.

Controlled metadata literals: `authority: none`; `audit: unset`;
`claim type: bounded_theorem`.

**Primary runner:**
[`scripts/physical_dynamical_metric_source_law_bridge_tournament_cycle576_2026_07_22.py`](../scripts/physical_dynamical_metric_source_law_bridge_tournament_cycle576_2026_07_22.py)
**Actual-Regge route support helper:**
[`scripts/physical_dynamical_metric_source_law_bridge_cycle576_regge_support_2026_07_22.py`](../scripts/physical_dynamical_metric_source_law_bridge_cycle576_regge_support_2026_07_22.py)
**Plaquette-route support helper:**
[`scripts/physical_dynamical_metric_source_law_bridge_cycle576_plaquette_support_2026_07_22.py`](../scripts/physical_dynamical_metric_source_law_bridge_cycle576_plaquette_support_2026_07_22.py)
**Receipt:**
[`outputs/physical_dynamical_metric_source_law_bridge_tournament_cycle576_receipt_2026_07_22.json`](../outputs/physical_dynamical_metric_source_law_bridge_tournament_cycle576_receipt_2026_07_22.json)
**Repaired Cycle-572 source note:**
[`finite source-insertion algebra and carrier-label support`](FINITE_SOURCE_INSERTION_ALGEBRA_CARRIER_LABEL_SUPPORT_CYCLE572_BOUNDED_THEOREM_NOTE_2026-07-22.md)
**Linearized Einstein-Hilbert/Regge comparator source:**
[`geometric Regge linearization comparator`](R3_GEOMETRIC_REGGE_LINEARIZATION_GIVES_HEALTHY_LAMBDA1_GRAVITON_NARROW_THEOREM_NOTE_2026-06-08.md)
**Cubic-Coxeter Regge second-variation source:**
[`3+1 cubic-Coxeter Regge second variation`](CUBIC_COXETER_REGGE_3PLUS1_TICK_EXTENSION_SECOND_VARIATION_NARROW_THEOREM_NOTE_2026-06-09.md)
**Campaign provenance (non-source history):**
`docs/work_history/repo/review_feedback/PHYSICAL_DYNAMICAL_METRIC_SOURCE_LAW_BRIDGE_TOURNAMENT_CYCLE576_NOTE_2026-07-22.md`

## Controlled claim

Cycle 576 executes three finite calculations after exact-pinning the repaired
Cycle-572 receipt, runner, and canonical note together with the supplied
linearized Einstein-Hilbert/Regge comparator and cubic-Coxeter Regge
second-variation source surfaces. Their audit status is not asserted here.

1. **Route A — supplied 24-sector Regge model.** A finite
   `1 + 24 * 15 = 361` coordinate model contains one source coordinate and 24
   edge-coordinate sectors. Uniform frame-sector preparation is supplied. The
   actual Regge Hessian, deficit source insertion, action choice, orientations,
   coupling sign and magnitude, update parameter, and readout are supplied.
   The runner checks the actual-edge Bianchi identity, the local-deficit Ward
   identity, all 24 proper-cubic covariance cases, all 576 representation
   products, inverse/norm controls, held `L=3,4` source amplitudes, zero-source,
   source deletion, response deletion, wrong-sign, and anisotropic control.
   The displayed small-momentum R3/EH target-algebra comparison is executed
   only as a comparator after the Regge matrices are fixed. It is not an
   Einstein equation.
2. **Route B — finite plaquette/conjugate model.** The supplied
   31-coordinate Hermitian block has matter, curvature, conjugate, and
   reservoir coordinates. The runner checks its finite exponential,
   reciprocity, source/curvature/conjugate deletions, zero-source and
   wrong-sign controls, all 24 covariance cases, and all 576 products. Its
   momentum-independent six-component block has a nonzero residual against the
   declared R3 comparator. That is a route-specific diagnostic only.
3. **Route C — finite face-scattering model.** The supplied 12-direction
   Grover walk and source profiles are executed on train and blinded held
   fixtures without refit. The runner checks inverse/norm behavior,
   finite-difference tangents, source and transport response deletion,
   zero-source, wrong-sign and anisotropic control, all 24 covariance cases,
   all 576 products, effective-metric reconstruction residuals, and a
   least-squares R3 source comparison. Its mismatch is specific to the
   displayed scattering ansatz.

The strongest result is therefore a finite, supplied, proper-cubic Regge
source-insertion calculation with exact algebraic identities and numerical
target-comparison residuals. The generator is not a rate. The resource is not
physical stress, not physical energy, and not gravity.

## Supplied structure and open work

The calculation supplies the Regge complex and action, edge and metric maps,
24-sector coordinate layout and uniform state preparation, deficit insertion,
coupling constants and signs, finite update parameters, Route-B coordinate
layout, Route-C coin and schedule, periodic domains, source profiles,
tolerances, readouts, and the train/held split.

Audit-packet import inventory: the primary runner ordinary-imports the
cubic-Coxeter Regge second-variation module, the actual-Regge route helper, and
the plaquette-route helper. The plaquette helper ordinary-imports the Regge
helper for the shared frame representation. All three transitive helpers are
bound through `AUDIT_INPUT_PATHS` and the runner's source-dependency closure.
The two new helpers are packaging surfaces only, not independent claims or
authorities.

The complete supplied parameter and control inventory is:

- common numerical policy: `TOL=8e-9`, `FD_TOL=4e-7`,
  `MATCH_TOL=5e-7`, and `SIGNAL=1e-8`;
- Route A: Regge update scale `0.025`, source coupling `+0.17`, update
  parameter `0.035`, one source coordinate plus 24 simultaneously present
  15-edge frame sectors, uniform coherent frame-sector preparation/readout,
  raw deficit-row normalization, comparison magnitude `1e-3` in the five
  displayed directions, and covariance-control momentum
  `(0.17,0.11,0.07,0.13)`;
- Route-A size controls: train `(L=3, amplitude=0.6,
  k=(2*pi/3,0,0,0))`, held-low `(L=4, amplitude=0.37,
  k=(pi/2,pi/2,0,0))`, and held-sign `(L=4, amplitude=-0.81,
  k=(pi/2,0,pi/2,pi/2))`, all without refit;
- Route B: 31-coordinate layout `6 matter + 12 curvature + 12 conjugate + 1
  reservoir`, conjugate frequency `0.31`, reservoir coupling `0.19`, inherited
  curvature coupling `0.23`, update parameter `0.035`, equal matter/reservoir
  initial amplitudes, factor placement, and the displayed anisotropic and
  deletion controls;
- Route C: the normalized 12-direction Grover coin, two coin/stream steps,
  phase amplitude `0.071`, uniform initial face state, centered and normalized
  train profiles `cos(2*pi*x/L)+0.35*cos(2*pi*y/L)` and
  `sin(2*pi*(x+y)/L)+0.27*cos(2*pi*z/L)`, and held profiles
  `sin(2*pi*(x+2*y+z)/L)+0.41*cos(2*pi*z/L)` and a centered point source; and
- Route-C diagnostic choices: tangent step `8e-7`, the declared six-component
  face-metric least-squares design, train-only source calibration, blinded
  `L=4` residual evaluation, and no held-parameter refit.

It does not derive a physical stress tensor, metric observable calibration,
nonlinear or continuum gravitational equation, source preparation law, or
arbitrary-size family. The exact finite exponential does not compile a
bounded-depth local circuit; a bounded-depth finite-time Regge circuit remains
open. There is no physical-site compiler, local code-constraint construction,
leakage test, or executed encoding intertwiner in Cycle 576. There is no
minimum claim, no no-go claim, and no axiom-pressure conclusion.

No physical clock, proper time, Record, realized-history law, or Born rule is
derived.
