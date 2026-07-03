# Weak-Field Optical Metric Ansatz Diagnostic

**Date:** 2026-06-09
**Claim type:** bounded_theorem (ansatz diagnostic; weak-field support only)
**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome.
**Primary runner:** [`scripts/weak_field_optical_metric_ansatz_diagnostic_2026_06_09.py`](../scripts/weak_field_optical_metric_ansatz_diagnostic_2026_06_09.py)
**Runner cache:** [`logs/runner-cache/weak_field_optical_metric_ansatz_diagnostic_2026_06_09.txt`](../logs/runner-cache/weak_field_optical_metric_ansatz_diagnostic_2026_06_09.txt)

## Summary

This note preserves the runner-backed part of the submitted weak-field metric
work and removes the unsupported closure claims. It studies the standard static
weak-field ansatz

```text
g = diag(-(1 + 2 Phi(x)), 1, 1, 1)
```

as an **optical-metric diagnostic**. Under that supplied ansatz, a spatially
varying scalar potential curves the geometry at linear order, gives the usual
Newtonian geodesic kinematics, and is compatible with a Poisson/`1/r` weak-field
surface.

The note does **not** derive the ansatz from Record, record density, the
kinetic-isotropy primitive, the weak-field Poisson row, or the scalar generator.
It also does not derive the gravity sign, Newton's constant, a source/action
normalization, a tensor graviton, or nonlinear Einstein closure.

## Runner-Verified Result

The runner verifies five support facts:

- **M1 ansatz form:** the supplied metric ansatz has isotropic spatial part and
  a scalar weak-field perturbation in `g_00`.
- **M2 curvature:** linearizing in `Phi` gives `R_00 = d^2 Phi / dx^2` in the
  one-direction model.
- **M3 geodesic kinematics:** the Christoffel symbol is
  `Gamma^x_00 = d Phi / dx`, so nonrelativistic motion follows
  `d^2 x / d tau^2 = -d Phi / dx` for the supplied potential.
- **M4 Poisson compatibility:** `1/r` is harmonic away from the source, and a
  finite lattice resolvent sample has a rough `1/r` falloff trend.
- **M5 boundary:** the runner explicitly flags that the metric/source
  identification, sign, tensor sector, and nonlinear closure are outside this
  check.

`TOTAL: PASS=5 FAIL=0`.

## What This Establishes

Given the static weak-field optical metric ansatz, the local differential
geometry matches the expected Newtonian-form support facts: curvature is
controlled by the Laplacian of the scalar potential, and test-particle
kinematics follows the potential gradient.

This is useful support for later gravity work because it gives a small,
machine-checked target for any future derivation of a record-density or
linear-response metric variable.

## What This Does Not Establish

This note does **not** establish:

- record density as a physical metric degree of freedom;
- the map from a record/readout variable to `Phi`;
- the source equation `Delta Phi = rho` from this ansatz;
- the attraction sign `G > 0`;
- equality with an observed or registered Newton constant;
- any source/action normalization or probability/readout rule;
- TT spin-2 graviton dynamics;
- nonlinear or strong-field Einstein closure;
- that the kinetic-isotropy primitive supplies Lorentz/Poincare covariance or a
  dynamical metric.

## Relation to Existing Rows

- [KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
  supplies only the structural `c_t = c_s` kinetic-form premise. It is not used
  here to derive a metric.
- [EMERGENT_METRIC_CONFORMAL_CLASS_FROM_RECORDS_SCALE_IS_THE_CLOCK_RATE_NO_GO_NARROW_THEOREM_NOTE_2026-06-06.md](EMERGENT_METRIC_CONFORMAL_CLASS_FROM_RECORDS_SCALE_IS_THE_CLOCK_RATE_NO_GO_NARROW_THEOREM_NOTE_2026-06-06.md)
  leaves the conformal-class assembly conditional and the conformal factor at
  the clock-rate boundary.
- [GRAVITY_CLOSURE_FROM_WEAK_FIELD_LINEAR_RESPONSE_BOUNDED_THEOREM_NOTE_2026-06-07.md](GRAVITY_CLOSURE_FROM_WEAK_FIELD_LINEAR_RESPONSE_BOUNDED_THEOREM_NOTE_2026-06-07.md)
  is separate weak-field Poisson/linear-response context; this note does not
  promote or re-audit it.
- [UNIVERSAL_GR_SCALAR_GENERATOR_TT_KERNEL_SHARPENING_BOUNDED_THEOREM_NOTE_2026-06-08.md](UNIVERSAL_GR_SCALAR_GENERATOR_TT_KERNEL_SHARPENING_BOUNDED_THEOREM_NOTE_2026-06-08.md)
  keeps the TT spin-2 sector separate from scalar/longitudinal support.

## Audit Note

The submitted PR claimed that the emergent dynamical metric, weak-field gravity
sign, and Newtonian gravity were derived, leaving only nonlinear Einstein
completion open. Those claims are not landed here. The landed content is only
the bounded optical-metric ansatz diagnostic above.
