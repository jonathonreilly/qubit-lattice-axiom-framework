# Quark Route-2 Source-Domain Typecast Scale Normalization No-Go

**Date:** 2026-06-21
**Claim type:** no_go
**Claim scope:** exact negative boundary / normalization no-go
**Status authority:** independent audit lane only. This source note does not set, claim, or predict an audit outcome.
**Primary runner:** [`scripts/frontier_quark_route2_source_domain_typecast_scale_normalization_no_go_2026_06_21.py`](../scripts/frontier_quark_route2_source_domain_typecast_scale_normalization_no_go_2026_06_21.py)
**Runner cache:** [`logs/runner-cache/frontier_quark_route2_source_domain_typecast_scale_normalization_no_go_2026_06_21.txt`](../logs/runner-cache/frontier_quark_route2_source_domain_typecast_scale_normalization_no_go_2026_06_21.txt)
**Primary parents:**
[`RCONN_DERIVED_NOTE.md`](RCONN_DERIVED_NOTE.md),
[`EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md`](EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md),
[`RCONN_KAPPA_EW_REGISTER_NOT_READ_COLOR_TRACE_OPEN_GATE_NOTE_2026-06-08.md`](RCONN_KAPPA_EW_REGISTER_NOT_READ_COLOR_TRACE_OPEN_GATE_NOTE_2026-06-08.md),
[`QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md`](QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md),
[`QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md`](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md),
[`ROUTE2_READOUT_RECORD_POSITIVITY_DOES_NOT_FIX_RHO_E_NARROW_NO_GO_NOTE_2026-06-08.md`](ROUTE2_READOUT_RECORD_POSITIVITY_DOES_NOT_FIX_RHO_E_NARROW_NO_GO_NOTE_2026-06-08.md)

## Scope

This is a first-principles stretch attempt on the typed magnitude theorem.
It asks whether the current source bank can turn the color-domain scalar
`F_adj = 8/9` into the Route-2 magnitude `|c_TE|` without adding a hidden
normalization.

It cannot. The most general scalar-to-Route-2 magnitude typecast has an
undetermined positive scale:

```text
|c_TE| = nu F_adj.
```

The target value corresponds to the unit typecast normalization

```text
nu = 1.
```

The current parent bank supplies `F_adj`, endpoint algebra, sign support, and
the typed-edge inventory, but it does not derive the typed magnitude theorem or
the unit typecast normalization. This note records the resulting normalization
no-go.

## A_min

Allowed minimal premises:

1. exact color-domain support
   ```text
   F_adj = (N_c^2 - 1) / N_c^2 = 8/9
   ```
   at `N_c = 3`;
2. positive-lift Route-2 domain `rho_E > -6`;
3. granted T-side values `q_T = 5/6`, `s_TE = -2`;
4. endpoint algebra
   ```text
   |c_TE| = (5/3) / q_E,
   q_E = 1 + rho_E/6;
   ```
5. exact rational arithmetic;
6. current quote-derived typed-edge inventory.

Forbidden proof inputs:

- observed masses;
- fitted Yukawa or CKM/J targets;
- live endpoint nearest-rational selection;
- physical connected-trace selector;
- a hidden scalar-to-Route-2 unit normalization.

## Scale Family

The scale family is the obstruction isolated here.

For any positive typecast scale `nu`, define

```text
|c_TE| = nu F_adj.
```

Using the endpoint inverse,

```text
rho_E = 10 / |c_TE| - 6,
```

so

```text
rho_E(nu) = 10 / (nu F_adj) - 6.
```

At `F_adj = 8/9`, the runner checks:

| `nu` | selected `rho_E` |
|---:|---:|
| `1/2` | `33/2` |
| `3/4` | `9` |
| `1` | `21/4` |
| `9/8` | `4` |
| `5/4` | `3` |
| `2` | `-3/8` |

All sampled values remain in the positive-lift domain and round-trip through
`|c_TE| = nu F_adj`. Therefore the color scalar plus positivity does not pick
the unit scale.

## Hidden Selector

The statement

```text
nu = 1
```

is not a harmless convention inside this route. The statement "nu = 1 is the hidden selector" is the exact obstruction: it turns color-domain `F_adj` into the Route-2 magnitude:

```text
scalar magnitude 8/9 -> Route-2 |c_TE| = 8/9.
```

With sign support, that is equivalent to the typed landing edge

```text
route2_center_TE_minus_8_9.
```

The existing endpoint algebra then reaches

```text
route2_q_E_15_8
route2_rho_E_21_4.
```

So `nu = 1` is the hidden selector unless a future theorem sources it from
accepted structure.

## Current-Bank Graph Check

The runner reuses the current source-domain typed-edge inventory:

```text
CURRENT_TYPED_EDGES + DERIVED_ADDITIONAL_EDGES.
```

It checks that this bank has no path

```text
su3_R_conn_8_9 -> route2_center_TE_minus_8_9
su3_R_conn_8_9 -> route2_rho_E_21_4.
```

Adding the already-named missing bridge creates the path immediately. The
missing bridge is therefore not hidden in the existing quote-derived bank.

## Handoff

The next positive theorem must supply one of:

```text
unit typecast normalization: nu = 1
scalar magnitude 8/9 -> Route-2 |c_TE| = 8/9
su3_R_conn_8_9 -> route2_center_TE_minus_8_9
su3_R_conn_8_9 -> route2_q_E_15_8
su3_R_conn_8_9 -> route2_rho_E_21_4
```

Anything weaker leaves a free typecast scale.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_source_domain_typecast_scale_normalization_no_go_2026_06_21.py
```

Expected branch result:

```text
TOTAL: PASS=48, FAIL=0
VERDICT: current sources leave a free typecast scale; nu=1 is the missing normalization theorem.
```
