---
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: direct_blocker_closure
reachability_to_target: closes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "fixed finite-operator computation with explicit conditions, source-step-free endpoints, and an eleven-point residual bound"
audit_required_before_effective_retained: true
bare_retained_allowed: false
review_loop_disposition: pass
---

# Dependency certificate

| Dependency/input class | Count | Disposition |
|---|---:|---|
| Lattice axiom background | 1 | nearest-neighbor cubic adjacency only |
| approved primitive | 0 | none used |
| explicit non-satisfying finite-operator conditions | 1 package | fully enumerated in `ASSUMPTIONS_AND_IMPORTS.md` |
| fitted/observed/literature input | 0 | forbidden and absent |
| open physical interpolation/tensor bridge | 1 package | excluded from bounded claim |

The intended claim type is `bounded_theorem`. Independent audit is required;
no author/review artifact assigns an audit verdict or effective status.

## No-Go Discipline Gate (post-demotion checklist)

The negative content is deliberately narrow: the two implementations supply a
bounded numerical witness against affinity at stated tolerances for one fixed
operator. Exact algebraic non-affinity and every physical/global no-go are open.

### N1 — Alternative routes

| Attack on the narrow witness | Marker | Result |
|---|---|---|
| Source-amplitude finite-difference truncation created the defect | ATTEMPTED | analytic source differentiation removes that step; an independent central difference preserves sign and scale |
| The max-absolute branch was misidentified | ATTEMPTED | all 27 entries are enumerated on 11 backgrounds; the active gap stays above `1.2e-5` |
| Normalization drift created the defect | ATTEMPTED | shell total and anchor are computed at shell/mid/center and remain constant to replay precision |
| Floating cancellation created the displayed sign | ATTEMPTED | 60/90-digit helper and sparse-double implementations agree; claim narrowed to numerical tolerance, not exact nonzero |
| The secant used the wrong scalar coordinate/factor | ATTEMPTED | exact operator identity gives `delta=x/6`; manual endpoint arithmetic reproduces both residual signs |

No route above defeats the bounded numerical witness. Interval/algebraic
certification remains an unattempted route to a stronger exact claim and is
explicitly left open.

### N2 — Wall independence and collapse

For the bounded theorem itself there is no open premise: the finite conditions
define its domain. For a future physical theorem, the raw list collapses to:

- `W_I`: physically select a support-to-shell interpolation/readout contract;
- `W_P`: identify the resulting support pair with a physical tensor observable.

| Pair | closing first closes second? | closing second closes first? | Independent? |
|---|---|---|---|
| `W_I,W_P` | no | possibly (a physical theorem may jointly select it), not proved | not asserted independent |

Support-to-slice coupling and GR closure are downstream of `W_P`, so they are
not inflated as independent walls.

### N3 — Hidden-wall scan

The phrases “background,” “by construction,” “framework,” and “canonical” were
rechecked. The finite box, boundary, metric, interpolation including
`prefilter=True`, probes, shell functional, active-envelope rule, versions, and
helper padding are explicit non-satisfying conditions. `A_min` is restored to
Lattice+Qubit+Admissibility+Record. No admission class is used.

### N4 — Residual matching

| Witness | Witness residual | Current residual | Match? |
|---|---|---|---|
| historical target review quoted in `TRACE_GATE.md` | unavailable runner/stdout; endpoints, normalization, affine role not independently computable | primary runner/cache computes endpoints, normalization, and residual | yes |
| current midpoint replay | exact-affine endpoint extrapolation on fixed operator | bounded midpoint defect at declared tolerance | yes, after demotion |

No physical-primitive or continuum witness is cited as closed.

### N5 — Rhetoric audit

Tested resolutions are: one fixed box, one fixed scalar segment, 11 backgrounds,
three probes, all 27 trace-free entries, and two tangent channels. Untested are
the continuum segment between grid points, other sizes/boundaries/steps/probes,
other interpolators, and other observables. The note therefore says “bounded
numerical witness on the declared grid,” never lattice-wide or universal no-go.

### N6 — Partial-closure routes

No new axiom or primitive is requested. Live routes are: validated numerical
enclosure for exact nonaffinity; a physical principle selecting the
interpolator/readout; a local/smooth observable that removes the spline tail;
and a physical tensor/GR bridge. Each can strengthen or replace the bounded
result without changing the framework premise registry.

### N7 — Steelman

A hostile reviewer can correctly argue that 60/90-digit stability is not an
interval proof and that both implementations share derivative algebra. A
validated enclosure might make the nonzero exact, while a physically selected
local interpolator or different observable may remove the defect entirely.
This steelman defeats the former exact/global wording. The branch adopts its
demotion; it does not defeat the remaining bounded numerical witness.

### N8 — Cross-cycle echo

`QUARK_ROUTE2_ETA_FLOOR_HF_BOUNDARY_NOTE.md` records a method-only boundary that
was later bypassed by analytic differentiation, demonstrating why this note
must not foreclose new methods. The 2026-07-02 honest-gravity and family-size
notes record size/geometry dependence and smooth-observable escape routes.
Their lesson is applied here: fixed-size/interpolation scope is explicit and
all portability/physical routes remain open.

**No-Go Discipline status:** PASS. Iteration 2 confirmed the N1-N8 checklist
after the exact-to-bounded demotion.
