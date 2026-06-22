# Quark Route-2 Typed Metric/Source Inverse-Square Boundary

**Date:** 2026-06-22
**Type:** open gate / exact support
**Claim type:** open_gate
**Actual current-surface status:** exact-support
**Status authority:** independent audit lane only. This source note does not
set, predict, or apply an audit verdict.
**Primary runner:** [scripts/frontier_quark_route2_typed_metric_source_inverse_square_boundary_2026_06_22.py](../scripts/frontier_quark_route2_typed_metric_source_inverse_square_boundary_2026_06_22.py)
**Runner output:** [outputs/frontier_quark_route2_typed_metric_source_inverse_square_boundary_2026_06_22.txt](../outputs/frontier_quark_route2_typed_metric_source_inverse_square_boundary_2026_06_22.txt)

## Scope

This block attacks the exact missing primitive for the Route-2/S3 readout
endpoint triple named by
[S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md):

```text
(beta_T/alpha_T, alpha_T/alpha_E, beta_E/alpha_E)
  = (-1, -2, 21/4).
```

The note proves an exact conditional statement:

```text
If the E/T center lifts obey q_X w_X^2 = 5/24
on the seven-site star weights w_E = 1/3 and w_T = 1/2,
and the T-side entries beta_T/alpha_T = -1 and alpha_T/alpha_E = -2
are supplied, then the missing E entry is beta_E/alpha_E = 21/4.
```

This note does not derive the inverse-square primitive on the actual current
surface. It sharpens the remaining target and records the current-surface
negative boundary: existing carrier, equivariant, quadratic, Fierz/color,
registration, and E-center-blind primitives do not supply the law.

## One-Hop Authorities

| Authority | Role used here |
| --- | --- |
| [S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md) | Direct consumer and source of the quoted endpoint-triple blocker. |
| [QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md) | Restricted readout map, endpoint algebra, and missing-map entry. |
| [OH_SEVEN_SITE_STAR_SHELL_LEVERAGE_POSITIVE_THEOREM_NOTE_2026-06-10.md](OH_SEVEN_SITE_STAR_SHELL_LEVERAGE_POSITIVE_THEOREM_NOTE_2026-06-10.md) | Exact same-domain weights `w_E = 1/3`, `w_T = 1/2`, and leverage `3/2`. |
| [QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md](QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md) | Quadratic no-go and exact characterization of the missing inverse-square center-lift law. |
| [S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md](S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md) | Current `K_R` carrier and physical tensor-primitive bridge gap. |
| [QUARK_ROUTE2_RCONN_TYPED_BRIDGE_DERIVATION_BOUNDED_NOTE_2026-06-12.md](QUARK_ROUTE2_RCONN_TYPED_BRIDGE_DERIVATION_BOUNDED_NOTE_2026-06-12.md) | Current Fierz/color typed-bridge boundary. |
| [QUARK_ROUTE2_E_CENTER_BLINDNESS_NO_GO_NOTE_2026-06-17.md](QUARK_ROUTE2_E_CENTER_BLINDNESS_NO_GO_NOTE_2026-06-17.md) | E-center-blind no-go; a positive route must see the E-center column. |
| [ROUTE2_READOUT_RECORD_POSITIVITY_DOES_NOT_FIX_RHO_E_NARROW_NO_GO_NOTE_2026-06-08.md](ROUTE2_READOUT_RECORD_POSITIVITY_DOES_NOT_FIX_RHO_E_NARROW_NO_GO_NOTE_2026-06-08.md) | Registration/positivity leaves the readout direction free. |

## Exact Conditional Theorem

The seven-site star support gives the exact E/T per-arm projector weights:

```text
w_E = 1/3,
w_T = 1/2.
```

Grant the two T-side target entries:

```text
rho_T := beta_T/alpha_T = -1,
s_TE := alpha_T/alpha_E = -2.
```

The endpoint algebra gives:

```text
q_T = 1 + rho_T/6 = 5/6.
```

Now suppose a typed metric/source primitive supplies the inverse-square
center-lift law:

```text
q_X w_X^2 = C.
```

Using the T channel fixes:

```text
C = q_T w_T^2 = (5/6)(1/2)^2 = 5/24.
```

Then the E channel is forced:

```text
q_E = C / w_E^2 = (5/24)/(1/3)^2 = 15/8,
rho_E = 6(q_E - 1) = 21/4.
```

The center ratio then follows:

```text
c_TE = gamma_T(center)/gamma_E(center)
     = s_TE q_T/q_E
     = (-2)(5/6)/(15/8)
     = -8/9.
```

Thus the supplied inverse-square primitive is sufficient to recover the full
endpoint triple:

```text
(-1, -2, 21/4).
```

## Monomial Uniqueness

For a monomial projector-weight lift

```text
q_X proportional to w_X^p,
```

the endpoint covariance is:

```text
q_E/q_T = (w_E/w_T)^p = (2/3)^p.
```

The target covariance is:

```text
q_E/q_T = (15/8)/(5/6) = 9/4.
```

Searching integer exponents `-8 <= p <= 8` gives one hit:

```text
p = -2.
```

Common named structures miss:

| Law | `p` | `q_E/q_T` |
| --- | ---: | ---: |
| constant lift | `0` | `1` |
| direct projector weight | `1` | `2/3` |
| quadratic projector scaling | `2` | `4/9` |
| single inverse leverage | `-1` | `3/2` |
| inverse-square lift | `-2` | `9/4` |

So the missing bridge is now exactly the typed inverse-square lift law, not a
generic nonlinear, quadratic, or dimension-ratio statement.

## Current-Surface Boundary

The current surfaces do not derive the primitive:

- The O_h shell-leverage theorem derives `w_E = 1/3`, `w_T = 1/2`, and
  `kappa = 3/2`, but explicitly does not derive a Route-2 readout entry.
- The Schur/quadratic covariance no-go records that no named functional
  produces an inverse-square-of-projector-weight center lift.
- The bilinear carrier defines `K_R`; it does not prove that this symbol is
  the physical tensor primitive for the readout gate.
- The Fierz/color route can compute the target if a typed signed bridge
  `c_TE = -F_adj` is granted, but `F_adj` is not the same slot as the
  covariance `q_E/q_T = 9/4`, and the typed bridge is not derived.
- Registration/positivity fixes norms or bounds, not the readout direction.
- E-center-blind constraints cannot derive `rho_E`; the target must see the
  E-center column or supply an equivalent source/readout primitive.

Therefore this packet contributes exact support and route sharpening, not
endpoint closure.

## What Would Close The Blocker

A future closure would need one of:

1. a typed metric/source theorem deriving `q_X w_X^2 = 5/24` on the E/T
   Route-2 center-lift channels;
2. an equivalent E-center primitive deriving `q_E = 15/8`;
3. an exact readout-map theorem deriving the endpoint triple directly;
4. a typed source/readout bridge deriving `c_TE = -8/9` without importing it
   from a cross-domain coincidence.

## No-Go Discipline

N1 alternative routes:

| Route | Result |
| --- | --- |
| Constant lift | Gives `q_E/q_T = 1`, not `9/4`. |
| Direct projector-weight lift | Gives `2/3`, not `9/4`. |
| Quadratic projector scaling | Gives `4/9`, not `9/4`; this is also closed by the Schur/quadratic no-go. |
| Single inverse leverage | Gives `3/2`, not `9/4`. |
| Direct Fierz/color slot | Can compute the endpoint after a typed bridge is granted, but the bridge is not derived and the slot is not covariance. |
| Registration/positivity | Leaves `rho_E` as a direction. |
| E-center-blind endpoint constraints | Cannot see the missing E-center column. |

N2 wall independence:

The inverse-square center-lift law is independent from the already named
T-side row selector, shell normalization, Fierz/color bridge, and physical
tensor-primitive identification. Closing any one of those does not by itself
derive `q_X w_X^2 = 5/24`.

N3 hidden-wall scan:

The target rationals are used as comparison targets in exact endpoint algebra.
No observed masses, fitted endpoint values, nearest-rational selector, or
literature value is used.

N4 residual matching:

The residual matches the direct blocker in
[S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md):
the endpoint triple is not derived because the readout map remains unselected.

N5 rhetoric audit:

"Inverse-square primitive" names a future theorem target. It is not asserted as
current framework content.

N6 partial-closure path:

The exact conditional consequence is reusable: any later source note deriving
`q_X w_X^2 = 5/24` can plug directly into the endpoint triple.

N7 steelman:

A genuinely nonlinear tensor/source observable might derive the inverse-square
law. This packet does not rule that out; it isolates it.

N8 cross-cycle echo:

This is consistent with the prior naturality, positivity, covariance,
Rconn/Fierz, and E-center-blind boundaries. It narrows their common positive
target instead of overriding them.

## Validation

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_typed_metric_source_inverse_square_boundary_2026_06_22.py
```

Expected final line:

```text
TOTAL: PASS=30, FAIL=0
```
