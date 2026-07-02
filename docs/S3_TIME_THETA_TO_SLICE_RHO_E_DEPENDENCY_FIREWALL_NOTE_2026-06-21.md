# S3-Time Theta-to-Slice `rho_E` Dependency Firewall: The Unresolved Route-2 Readout Entry Propagates Only Through the E-Center Source Factor

**Date:** 2026-06-21
**Claim type:** exact_support
**Actual current-surface status:** exact-support
**Trace class:** upstream_support
**Reachability to target:** supports and narrows the `s3_time_theta_to_slice_coupling_note` open gate
**Status authority:** independent audit lane only. This note does not set, predict, or estimate an audit outcome.
**Primary runner:** [`scripts/frontier_s3_time_theta_to_slice_rho_e_dependency_firewall_2026_06_21.py`](../scripts/frontier_s3_time_theta_to_slice_rho_e_dependency_firewall_2026_06_21.py) (`PASS=10 FAIL=0`)
**Runner cache:** [`logs/runner-cache/frontier_s3_time_theta_to_slice_rho_e_dependency_firewall_2026_06_21.txt`](../logs/runner-cache/frontier_s3_time_theta_to_slice_rho_e_dependency_firewall_2026_06_21.txt)

## Target

The parent [`S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md`](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md)
already has the correct open-gate boundary:

```text
Xi_P(t ; c) = (P_R c) tensor V_R(t),
V_R(t) = exp(-t Lambda_R) u_*,
```

once an admissible Route-2 readout map `P_R` is supplied. The unique
`Theta_R -> Lambda_R` theorem is still blocked because the exact readout
triple

```text
(beta_T / alpha_T, alpha_T / alpha_E, beta_E / alpha_E)
= (-1, -2, 21/4)
```

is not derived on the current exact stack.

This note does not try to derive the missing entry. It records the direct
consumer firewall: exactly where the unresolved `rho_E := beta_E/alpha_E`
can and cannot affect the theta-to-slice family.

## Exact Firewall

With the two `T`-side entries granted, the reduced readout family is

```text
P(rho_E) = [[1, 0, rho_E, 0],
            [0,-2, 0,     2]].
```

On the four exact restricted carrier columns,

```text
E-shell  = (1, 0, 0,   0),
E-center = (1, 0, 1/6, 0),
T-shell  = (0, 1, 0,   0),
T-center = (0, 1, 0, 1/6),
```

the source factors are:

| carrier column | `(P(rho_E)c)_E` | `(P(rho_E)c)_T` | depends on `rho_E` |
|---|---:|---:|---|
| `E-shell` | `1` | `0` | no |
| `E-center` | `1 + rho_E/6` | `0` | yes |
| `T-shell` | `0` | `-2` | no |
| `T-center` | `0` | `-5/3` | no |

Therefore the complete theta-to-slice family satisfies:

```text
Xi_P(t ; E-shell)  independent of rho_E,
Xi_P(t ; T-shell)  independent of rho_E,
Xi_P(t ; T-center) independent of rho_E,
Xi_P(t ; E-center) = (1 + rho_E/6) e_E tensor V_R(t).
```

The unresolved readout datum is not a diffuse ambiguity in the time dynamics.
It is a single rank-one source factor multiplying the same exact slice seed
`V_R(t)`.

## Target Comparison

For the target value `rho_E = 21/4`,

```text
q_E = 1 + rho_E/6 = 15/8.
```

Relative to `rho_E = 0`, the E-center tensor difference is exactly

```text
(7/8) e_E tensor V_R(t).
```

The runner verifies this at `t in {0, 0.5, 1, 2}` and checks that the
rho-dependent tensor evolves by the same exact slice semigroup. It also checks
that a nearby non-load-bearing comparison value changes the same E-center
scalar and no other carrier column.

## What This Unblocks For Review

This packet narrows the parent open gate:

- no downstream theta-to-slice statement that uses only `E-shell`, `T-shell`,
  or `T-center` depends on the unresolved `rho_E`;
- any statement using `E-center` inherits exactly the scalar
  `1 + rho_E/6`;
- the slice generator `Lambda_R`, transfer `T_R`, and seed law `V_R(t)` are
  outside the ambiguity;
- a unique `Theta_R -> Lambda_R` theorem still requires the upstream readout
  endpoint triple.

So the parent row remains open, but the remaining ambiguity is localized for
the reviewer.

## No-Go / Support Discipline

- **Scope.** This is an exact-support firewall for a direct consumer, not an
  endpoint derivation.
- **Residual.** The residual is still `rho_E = beta_E/alpha_E`, equivalently
  `q_E = 1 + rho_E/6`.
- **Positive content.** The support result is the exact support-localization
  theorem above.
- **Boundary.** The note does not adopt `rho_E = 21/4`, does not close the
  endpoint triple, and does not change any repo-wide status surface.

## Load-Bearing Inputs

- [`S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md`](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md) -
  parent open-gate theta-to-slice surface.
- [`QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md`](QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md) -
  exact slice backbone and conditional family.
- [`QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md`](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md) -
  restricted readout map and endpoint obstruction.

## Forbidden-Imports Check

No observed quark mass, fitted endpoint, nearest-rational selector, or live
readout fit is used. The target `rho_E = 21/4` appears only as the exact
comparison value already named by the Route-2 readout map.
