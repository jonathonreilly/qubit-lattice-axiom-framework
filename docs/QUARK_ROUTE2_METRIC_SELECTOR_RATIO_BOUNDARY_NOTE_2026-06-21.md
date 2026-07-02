# Quark Route-2 Metric Selector Ratio Boundary

**Date:** 2026-06-21
**Type:** no_go
**Claim type:** no_go
**Status:** no-go / negative route pruning; no endpoint closure
**Primary runner:** `scripts/frontier_quark_route2_metric_selector_ratio_boundary_2026_06_21.py`

## Scope

The preceding campaign block found that a fixed-carrier quadratic source norm
can select the Route-2 target only if a metric/source primitive is supplied.
This branch rederives that load-bearing arithmetic directly and tests whether
the current Fisher/tangent/Hessian selector surfaces already supply that
primitive.

The target remains

```text
rho_E = beta_E / alpha_E = 21/4,
q_E = gamma_E(center) / gamma_E(shell) = 15/8.
```

## Authority Inputs

- [`QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md`](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md)
  supplies the exact restricted Route-2 carrier and missing-map obstruction.
- [`SHARP_RECORD_FISHER_TANGENT_SPACE_NARROW_THEOREM_NOTE_2026-06-06.md`](SHARP_RECORD_FISHER_TANGENT_SPACE_NARROW_THEOREM_NOTE_2026-06-06.md)
  supplies finite sharp-record Fisher tangent geometry.
- [`SOURCE_MEASURE_SHARP_RECORD_TANGENT_SPACE_THEOREM_NOTE_2026-05-30.md`](SOURCE_MEASURE_SHARP_RECORD_TANGENT_SPACE_THEOREM_NOTE_2026-05-30.md)
  supplies the broader source/measure boundary and supplied-basis caveats.
- [`POST_RECORD_SELECTOR_TANGENT_READOUT_WEIGHT_PROTOTYPE_2026-06-06.md`](POST_RECORD_SELECTOR_TANGENT_READOUT_WEIGHT_PROTOTYPE_2026-06-06.md)
  supplies only a conditional diagnostic with supplied metric/Hessian data.
- [`YT_EXACT_HESSIAN_SELECTOR_UNIQUENESS_NOTE.md`](YT_EXACT_HESSIAN_SELECTOR_UNIQUENESS_NOTE.md)
  supplies a domain-specific bounded Hessian selector result, not a Route-2
  E/T metric.
- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md)
  supplies the Record/Quantum non-supply boundary for readout context,
  weighting, tangent metric, Hessian, and source primitives.

## Required Metric Ratio

With the granted T-side values, the fixed source vectors are

```text
S = (1, -2),
C(q_E) = (q_E, -5/3).
```

For a diagonal positive quadratic selector metric

```text
G = diag(a,b),
```

the shell/center equal-norm equation is

```text
a q_E^2 + b (25/9) = a + 4b.
```

Solving this for the target `q_E=15/8` gives the exact required ratio

```text
b/a = 1449/704.
```

For a general symmetric metric

```text
G = [[a,c],[c,b]],
```

target equal-norm selection requires

```text
161 a/64 - 9 c/4 - 11 b/9 = 0.
```

So a metric route can select the target, but only after supplying a metric
tensor satisfying that equation. The equation is not produced by the fixed
carrier itself.

## Current Metric Surfaces

The current metric/tangent/Hessian surfaces do not supply this Route-2 metric:

- The sharp-record Fisher tangent theorem supplies the canonical Fisher pairing
  and a primitive two-outcome signed-record unit. In a two-coordinate E/T
  reading this is the unit/isotropic metric shape, not `b/a=1449/704`.
- The source/measure packet keeps physical source semantics and supplied
  response-basis identification conditional.
- The Post-Record selector/tangent/readout prototype explicitly uses supplied
  carrier, weights, metric/Hessian, and readout data. It is diagnostic
  arithmetic, not Record-derived selector authority.
- The YT exact Hessian selector note is a bounded, domain-specific Schur/Hessian
  selector result. It does not define `gamma_E`, `gamma_T`, `q_E`, or a
  Route-2 E/T metric.
- The minimal axioms do not supply readout weighting, tangent metric, Hessian,
  or source primitive.

## Result

**Theorem (Route-2 metric selector ratio boundary).** On the fixed Route-2
source pair `S=(1,-2)`, `C(q_E)=(q_E,-5/3)`, an equal-quadratic-norm selector
can force `q_E=15/8` only by supplying a metric tensor satisfying

```text
161 a/64 - 9 c/4 - 11 b/9 = 0,
```

with diagonal specialization `b/a=1449/704`. Current Fisher/tangent/Hessian
surfaces do not derive that Route-2 metric. Therefore the metric-selector route
does not close `rho_E=21/4` on the current surface; it sharpens the remaining
positive target to a real Route-2 metric/source primitive rather than a
supplied or domain-mismatched metric.

## What This Prunes

This block prunes the route

```text
fixed Route-2 carrier
+ current Fisher/tangent/Hessian selector surfaces
=> metric ratio b/a = 1449/704
=> q_E = 15/8
=> rho_E = 21/4.
```

It does not prune a future theorem that derives the metric tensor from a typed
Route-2 source/readout primitive.

## Current Status

```yaml
actual_current_surface_status: no-go
trace_class: negative_route_pruning
reachability_to_target: prunes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "The block prunes current metric-selector surfaces; it does not derive the Route-2 metric/source primitive."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_metric_selector_ratio_boundary_2026_06_21.py
```

Expected result:

```text
TOTAL: PASS=45, FAIL=0
VERDICT: current metric-selector surfaces do not derive the Route-2 ratio 1449/704.
```
