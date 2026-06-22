# Quark Route-2 T-Side Row Shape/Shell Scale Independence No-Go

**Date:** 2026-06-22
**Type:** no_go
**Claim type:** no_go
**Actual current-surface status:** no-go
**Trace class:** negative_route_pruning
**Primary runner:** [scripts/frontier_quark_route2_t_side_row_shape_shell_scale_independence_no_go_2026_06_22.py](../scripts/frontier_quark_route2_t_side_row_shape_shell_scale_independence_no_go_2026_06_22.py)

## Scope

This block attacks the first two entries of the Route-2 readout endpoint
triple:

```text
beta_T / alpha_T = -1,
alpha_T / alpha_E = -2.
```

The result is a row-shape/shell-scale independence boundary. On the restricted
Route-2 readout algebra, the T-center ratio

```text
rho_T = beta_T / alpha_T,
q_T = 1 + rho_T / 6
```

is a T-row shape coordinate, while

```text
s_TE = alpha_T / alpha_E
```

is a relative E/T shell scale and orientation coordinate. A selector for one
coordinate does not derive the other.

This note does not set or predict any audit verdict.

## Authorities Used

| Authority | Role |
| --- | --- |
| [QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md) | Restricted readout form and endpoint-ratio algebra. |
| [QUARK_ROUTE2_T_SIDE_ENDPOINT_THEOREM_ATTEMPT_BOUNDED_NOTE_2026-06-12.md](QUARK_ROUTE2_T_SIDE_ENDPOINT_THEOREM_ATTEMPT_BOUNDED_NOTE_2026-06-12.md) | Prior bounded attempt and W1/W2 wall separation. |
| [S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md) | Downstream open gate blocked by the endpoint triple. |
| [QUARK_ROUTE2_DIRECT_E_CENTER_SELECTOR_BOUNDARY_NOTE_2026-06-22.md](QUARK_ROUTE2_DIRECT_E_CENTER_SELECTOR_BOUNDARY_NOTE_2026-06-22.md) | Sibling direct E-center block that grants the T-side pair and then leaves `rho_E=21/4` open. |

## Exact Algebra

The restricted Route-2 readout row has the T-side form

```text
gamma_T = alpha_T u_T + beta_T delta_A1 u_T
```

with the carrier endpoint columns

```text
T-shell  = (0, 1, 0, 0)
T-center = (0, 1, 0, 1/6).
```

Therefore

```text
gamma_T(shell)  = alpha_T,
gamma_T(center) = alpha_T + beta_T / 6,
rho_T           = beta_T / alpha_T,
q_T             = 1 + rho_T / 6.
```

The E shell column is disjoint:

```text
E-shell = (1, 0, 0, 0),
gamma_E(shell) = alpha_E,
s_TE = gamma_T(shell) / gamma_E(shell) = alpha_T / alpha_E.
```

The candidate row

```text
alpha_E = 1,
alpha_T = -2,
beta_T  =  2
```

gives

```text
rho_T = -1,
q_T = 5/6,
s_TE = -2.
```

This is exact conditional reproduction after the row is supplied. It is not a
derivation of the row.

## Independence Witnesses

T-row scaling preserves row shape but moves shell scale. For example,

```text
(alpha_E, alpha_T, beta_T) = (1, -6, 6)
```

has

```text
rho_T = -1,
q_T = 5/6,
s_TE = -6.
```

Changing `beta_T` at fixed shells preserves shell scale but moves row shape:

```text
(alpha_E, alpha_T, beta_T) = (1, -2, 0)
```

has

```text
s_TE = -2,
rho_T = 0,
q_T = 1.
```

Changing only the E shell normalization preserves the T row shape and moves
the E/T shell quotient:

```text
(alpha_E, alpha_T, beta_T) = (2, -2, 2)
```

has

```text
rho_T = -1,
q_T = 5/6,
s_TE = -1.
```

These witnesses all live in the same restricted readout algebra. They show
that a future theorem for `beta_T = -alpha_T` would not, by itself, prove
`alpha_T / alpha_E = -2`, and a future theorem for the shell quotient would
not, by itself, prove `beta_T = -alpha_T`.

## Additional Counter-Witnesses

| Witness | Values preserved | Values broken |
| --- | --- | --- |
| `(alpha_E, alpha_T, beta_T) = (2, -2, 2)` | `rho_T=-1`, `q_T=5/6` | `s_TE=-1` |
| `(alpha_E, alpha_T, beta_T) = (1, 2, -2)` | `rho_T=-1`, `q_T=5/6` | `s_TE=+2` |
| `(alpha_E, alpha_T, beta_T) = (1, -2, 0)` | `s_TE=-2` | `rho_T=0`, `q_T=1` |
| `(alpha_E, alpha_T, beta_T) = (1, -2, -2)` | `s_TE=-2` | `rho_T=1`, `q_T=7/6` |

The two target equations therefore require two independent selectors:

1. A T-row shape law `beta_T = -alpha_T`.
2. An E/T shell scale and orientation law `alpha_T / alpha_E = -2`.

Equivalently, a single future primitive could select the full relative row
`(alpha_E, alpha_T, beta_T) = (1, -2, 2)`, but it must supply both pieces of
information.

## Selector Firewall

Carrier columns do not fix either row ratio. The columns provide the endpoint
evaluation sites, but the coefficients `alpha_E`, `alpha_T`, and `beta_T`
remain row data.

The time factor cancels from these ratios. The conditional family

```text
Xi_P(t ; c) = (P_R c) tensor V_R(t)
```

starts after `P_R` is supplied and multiplies all endpoint readouts by the
same slice factor. It does not select `beta_T / alpha_T` or
`alpha_T / alpha_E`.

Shell normalization alone can choose a unit convention for one shell, but it
does not choose both the relative T-shell scale and the T-center row shape.
Center positivity or boundedness also does not select `beta_T=-alpha_T`; it
permits multiple center lifts on the same shell.

## Boundary

This block sharpens the Route-2 endpoint blocker but does not close it. It
prunes any route that tries to get the full T-side pair from only one of the
two coordinates.

The positive route left open is a physical T-row theorem that supplies either:

- both independent selectors listed above, or
- one primitive selecting the full relative T row `(alpha_E, alpha_T, beta_T) =
  (1, -2, 2)` without importing the endpoint target.

Until such a theorem is supplied, the first two entries of the endpoint triple
remain conditional inputs for downstream blocks such as the direct E-center
selector and the s3-time theta-to-slice coupling row.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_t_side_row_shape_shell_scale_independence_no_go_2026_06_22.py
```

Expected final line:

```text
TOTAL: PASS=44, FAIL=0
```
