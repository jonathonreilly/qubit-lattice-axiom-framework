# Quark Route-2 Hessian Counterterm Exclusion Boundary

**Date:** 2026-06-22
**Type:** exact negative boundary
**Claim type:** no_go
**Actual current-surface status:** no-go
**Status authority:** independent audit lane only. This source note does not
set, predict, or apply an audit verdict.
**Primary runner:** [scripts/frontier_quark_route2_hessian_counterterm_exclusion_boundary_2026_06_22.py](../scripts/frontier_quark_route2_hessian_counterterm_exclusion_boundary_2026_06_22.py)
**Runner output:** [outputs/frontier_quark_route2_hessian_counterterm_exclusion_boundary_2026_06_22.txt](../outputs/frontier_quark_route2_hessian_counterterm_exclusion_boundary_2026_06_22.txt)

## Scope

Block100 proved that a dilation-covariant Hessian source density is exactly
the inverse-square law needed by Block99:

```text
H(a w) = a^-2 H(w)  iff  H(w) = C/w^2.
```

This block tests whether the current weaker premises already exclude positive
Hessian counterterms. They do not.

The exact counterterm family is:

```text
H_epsilon(w) = C/w^2 + epsilon,
```

with `C > 0` and `epsilon >= 0`. It is still positive, separable, and
channel-uniform as a functional form. It only recovers the target endpoint at
`epsilon = 0`. Therefore a future positive theorem must prove a no-scale,
dilation-covariant, quotient, or variational rule that sets the counterterm
to zero. Positivity, separability, and finite Record additivity do not do it.

## One-Hop Authorities

| Authority | Role used here |
| --- | --- |
| [QUARK_ROUTE2_DILATION_COVARIANT_HESSIAN_SOURCE_BOUNDARY_NOTE_2026-06-22.md](QUARK_ROUTE2_DILATION_COVARIANT_HESSIAN_SOURCE_BOUNDARY_NOTE_2026-06-22.md) | Direct parent: dilation-covariant Hessian is equivalent to inverse-square source law. |
| [QUARK_ROUTE2_TYPED_METRIC_SOURCE_INVERSE_SQUARE_BOUNDARY_NOTE_2026-06-22.md](QUARK_ROUTE2_TYPED_METRIC_SOURCE_INVERSE_SQUARE_BOUNDARY_NOTE_2026-06-22.md) | Block99: inverse-square center lift suffices for the endpoint triple. |
| [S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md) | Direct downstream consumer and source of the endpoint-triple blocker. |
| [QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md) | Restricted readout map and missing E-channel map entry. |
| [QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md](QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md) | Current no-go that no named functional supplies the inverse-square center lift. |
| [MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md) | Record axiom boundary: no weighting, normalization, probability, dynamics, or readout context. |

## Exact Counterterm Family

Use the Route-2 E/T weights:

```text
w_E = 1/3,
w_T = 1/2.
```

For `C=1`, the counterterm Hessian ratio is:

```text
R(epsilon) := H_epsilon(w_E)/H_epsilon(w_T)
            = (9 + epsilon)/(4 + epsilon).
```

This family has exact endpoints:

```text
R(0) = 9/4,
lim_{epsilon -> infinity} R(epsilon) = 1.
```

For every `epsilon > 0`, it is below the target:

```text
R(epsilon) < 9/4.
```

The derivative is exact:

```text
dR/depsilon = -5/(4 + epsilon)^2 < 0.
```

So the positive counterterm family continuously deforms the inverse-square
endpoint toward the constant-Hessian endpoint.

## Endpoint Effect

Normalize by the T channel as in Block100:

```text
q_E(epsilon) = q_T R(epsilon),       q_T = 5/6.
```

At `epsilon = 0`:

```text
q_E = 15/8,
rho_E = 21/4.
```

At `epsilon = 1`:

```text
R = 2,
q_E = 5/3,
rho_E = 4.
```

At `epsilon = 5`:

```text
R = 14/9,
q_E = 35/27,
rho_E = 16/9.
```

These are exact admissible positive Hessian readings under the weak premises,
but they miss the endpoint. The target equation itself forces the
counterterm to vanish:

```text
(9 + epsilon)/(4 + epsilon) = 9/4
=> epsilon = 0.
```

That is a theorem target, not a consequence of the current surface.

## Current-Surface Boundary

The current surface does not exclude `epsilon > 0`.

- Minimal Record supplies finite scalar additivity in a supplied context, but
  no weighting, normalization, probability, dynamics, or readout context.
- Positivity and convexity are preserved by `epsilon >= 0`.
- Separability is preserved by the potential
  `Phi_epsilon(w) = -C log(w) + (epsilon/2) w^2`.
- The same functional form can be applied to every channel; no channel label
  is inserted by hand.
- The counterterm breaks dilation covariance, but the current surface does
  not derive dilation covariance.

Therefore a route that says "take the inverse-square/log-barrier Hessian" is
still open unless it supplies the counterterm-exclusion theorem.

## No-Go Discipline

N1 alternative routes:

| Route | Result |
| --- | --- |
| Pure inverse-square Hessian | Hits `rho_E=21/4`, but assumes `epsilon=0`. |
| Positive counterterm family | Preserves positivity and separability while missing target for `epsilon>0`. |
| Constant Hessian limit | Gives `R=1`, not `9/4`. |
| Record finite additivity | Does not set a Hessian counterterm. |
| Convexity | Allows every `epsilon >= 0`. |

N2 wall independence:

Counterterm exclusion is independent of the exact endpoint algebra, the O_h
weights, the Block99 inverse-square reduction, and the Block100 functional
equation. Those tell us what would work, not why `epsilon` must vanish.

N3 hidden-wall scan:

The target rationals are comparison targets in exact algebra. No observed
masses, fitted endpoint values, nearest-rational selector, or literature value
is used.

N4 residual matching:

The residual is exactly the missing source/readout primitive for the
readout-map endpoint triple. Block101 narrows it to a zero-counterterm or
no-scale premise when the Hessian route is used.

N5 rhetoric audit:

"Counterterm exclusion" names a future theorem target. It is not asserted as
current framework content.

N6 partial-closure path:

If a later theorem proves `epsilon=0` by a scale, quotient, variational, or
coordinate-invariance rule, then Block100 and Block99 give a direct route to
the endpoint triple.

## Validation

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_hessian_counterterm_exclusion_boundary_2026_06_22.py
```

Expected final line:

```text
TOTAL: PASS=37, FAIL=0
```
