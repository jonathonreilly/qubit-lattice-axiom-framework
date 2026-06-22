# Quark Route-2 Information-Metric Degree Boundary

**Date:** 2026-06-22
**Type:** exact negative boundary / no-go
**Claim type:** no_go
**Actual current-surface status:** no-go
**Status authority:** independent audit lane only. This source note does not
set, predict, or apply an audit verdict.
**Primary runner:** [scripts/frontier_quark_route2_information_metric_degree_boundary_2026_06_22.py](../scripts/frontier_quark_route2_information_metric_degree_boundary_2026_06_22.py)
**Runner output:** [outputs/frontier_quark_route2_information_metric_degree_boundary_2026_06_22.txt](../outputs/frontier_quark_route2_information_metric_degree_boundary_2026_06_22.txt)

## Scope

Block107 showed that a scale-shift-invariant second variation in the positive
Route-2 weight coordinate `w` would force the inverse-square source row

```text
H(w) proportional to 1/w^2,
```

and therefore the endpoint triple. Block108 then ruled out deriving that
nonzero Hessian directly from finite scalar Record additivity.

This block tests the next natural source-action candidate:

```text
standard finite-probability information geometry
  (Fisher/Rao, local KL, or Shannon/entropy Hessian).
```

These structures do produce second-order forms, but their one-coordinate
coefficient is inverse-linear:

```text
G(w) proportional to 1/w,
```

not inverse-square. With the Route-2 weights, inverse-linear degree `-1`
gives the first-variation miss from Block107, not the endpoint. Thus a generic
probability/Fisher/Shannon metric does not supply the Block107 source row.

This is not a no-go against a log-barrier, ray-quotient, or scale-invariant
Hessian source action. It prunes only the route that identifies the Route-2
row with the standard information metric of a supplied probability/intensity
coordinate.

## A_min And Forbidden Imports

Allowed in this block:

- the finite sharp-record Fisher tangent theorem as an information-metric
  candidate;
- the Record/Born boundary that probability laws are supplied, not derived
  from Record alone;
- Block107's second-variation target;
- Block108's Record-additive no-go;
- exact O_h channel weights `w_E=1/3` and `w_T=1/2`;
- exact rational arithmetic.

Forbidden proof inputs:

- observed masses;
- fitted endpoint values;
- nearest-rational selection;
- live endpoint measurements;
- assuming `q_E=15/8`, `rho_E=21/4`, or `c_TE=-8/9`.

The target fractions appear only as exact comparison values or as the
consequence of the already isolated inverse-square premise.

## One-Hop Authorities

| Authority | Role used here |
| --- | --- |
| [SHARP_RECORD_FISHER_TANGENT_SPACE_NARROW_THEOREM_NOTE_2026-06-06.md](SHARP_RECORD_FISHER_TANGENT_SPACE_NARROW_THEOREM_NOTE_2026-06-06.md) | Supplies the finite probability/Fisher tangent candidate `sum_i dp_i^2/p_i`; explicitly excludes physical source semantics. |
| [RECORD_BORN_FREQUENCY_BOUNDARY_2026-06-05.md](RECORD_BORN_FREQUENCY_BOUNDARY_2026-06-05.md) | Record counts do not derive a probability law; probability context is a supplied candidate here. |
| [QUARK_ROUTE2_LOG_WEIGHT_SECOND_VARIATION_ROW_BOUNDARY_NOTE_2026-06-22.md](QUARK_ROUTE2_LOG_WEIGHT_SECOND_VARIATION_ROW_BOUNDARY_NOTE_2026-06-22.md) | Direct parent: inverse-square second variation in `w` would close the source-row degree. |
| [QUARK_ROUTE2_RECORD_ADDITIVE_SECOND_VARIATION_NO_GO_NOTE_2026-06-22.md](QUARK_ROUTE2_RECORD_ADDITIVE_SECOND_VARIATION_NO_GO_NOTE_2026-06-22.md) | Direct parent: finite scalar Record additivity does not supply the nonzero Hessian. |
| [S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md) | Downstream open gate and endpoint-triple blocker. |

## Standard Information Metric Degree

For a supplied positive probability/intensity coordinate `w`, the standard
one-coordinate Fisher/KL quadratic form has coefficient

```text
G_F(w) = C/w.
```

Examples:

1. Fisher/Rao probability-coordinate form:

   ```text
   ||dp||_F^2 = sum_i dp_i^2 / p_i.
   ```

2. Local KL expansion for a positive coordinate:

   ```text
   D(w+dw || w) = (dw)^2/(2w) + higher order.
   ```

3. Shannon/Boltzmann convex generator:

   ```text
   d^2(w log w)/dw^2 = 1/w.
   ```

All three have homogeneous degree `-1` in the positive coordinate. They are
information metrics on a supplied probability/intensity coordinate. They are
not the log-barrier Hessian

```text
d^2(-log w)/dw^2 = 1/w^2.
```

## Endpoint Consequence

Using

```text
w_E = 1/3,
w_T = 1/2,
```

the standard information metric gives

```text
G_F(w_E)/G_F(w_T) = (1/w_E)/(1/w_T) = w_T/w_E = 3/2.
```

With supplied `q_T=5/6`,

```text
q_E = (5/6)(3/2) = 5/4,
rho_E = 6(q_E - 1) = 3/2.
```

With supplied shell ratio `s_TE=-2`,

```text
c_TE = (-2)(5/6)/(5/4) = -4/3.
```

This is exactly the first-variation falsifier from Block107. It is not the
endpoint target.

The inverse-square log-barrier/scale-quotient Hessian gives instead

```text
H(w_E)/H(w_T) = (w_T/w_E)^2 = 9/4,
q_E = 15/8,
rho_E = 21/4,
c_TE = -8/9.
```

So the derivative order and metric type are load-bearing.

## Theorem

**Theorem.** A Route-2 source-row theorem cannot close the Block107
second-variation premise by identifying the source row with the standard
finite-probability Fisher/Rao metric, local KL quadratic form, or Shannon
entropy Hessian on the supplied positive weight coordinate.

Those candidates have inverse-linear degree `-1`; the endpoint route requires
inverse-square degree `-2`.

## Current-Surface Boundary

The endpoint target remains open.

This block prunes one physical source-action candidate and sharpens what a
positive theorem must prove:

```text
not merely "information metric" or "probability Hessian",
but specifically a log-barrier, ray-quotient, scale-invariant Hessian,
or equivalent inverse-square source rule.
```

Minimal Record still supplies no probability law, source-action convention,
metric, normalization, or Hessian semantics. Supplying probability/Fisher
context is already extra structure; even after granting it as a candidate, it
lands on degree `-1`, not degree `-2`.

## No-Go Discipline

N1 alternative routes:

| Route | Result |
| --- | --- |
| Fisher/Rao probability metric | Degree `-1`; misses endpoint. |
| Local KL quadratic form | Degree `-1`; misses endpoint. |
| Shannon/Boltzmann entropy Hessian | Degree `-1`; misses endpoint. |
| Poisson/intensity Fisher coefficient | Degree `-1`; misses endpoint. |
| Log-barrier Hessian `-log w` | Degree `-2`; remains positive target. |
| Ray-quotient scale-invariant Hessian | Degree `-2`; remains positive target. |

N2 wall independence:

This wall is independent of Record additivity and endpoint arithmetic. Even
after a probability/information metric is supplied, the standard metric has
the wrong homogeneous degree.

N3 hidden-wall scan:

No observed masses, fitted endpoint values, nearest-rational selector, live
endpoint measurements, or literature values are used.

N4 residual matching:

The residual matches the parent S3/Route-2 blocker: the endpoint triple is not
derived because the source/readout primitive selecting the E-center row is not
derived.

N5 rhetoric audit:

"Cannot close" means "cannot close by identifying the row with standard
Fisher/KL/Shannon information metrics." It is not a no-go against log-barrier,
ray-quotient, scale-invariant Hessian, or other source-action primitives.

## Validation

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_information_metric_degree_boundary_2026_06_22.py
```

Expected final line:

```text
TOTAL: PASS=40, FAIL=0
```
