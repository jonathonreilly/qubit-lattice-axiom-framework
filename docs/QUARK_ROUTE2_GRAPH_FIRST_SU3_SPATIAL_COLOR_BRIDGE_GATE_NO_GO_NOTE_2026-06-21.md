# Quark Route-2 Graph-First SU(3) Spatial-Color Bridge Gate No-Go Note

**Date:** 2026-06-21
**Claim type:** no_go
**Actual current-surface status: no-go for the graph-first spatial-color escape.**
**Audit boundary:** This source note does not set, predict, estimate, or apply
any audit verdict.
**Primary runner:** [scripts/frontier_quark_route2_graph_first_su3_spatial_color_bridge_gate_no_go_2026_06_21.py](../scripts/frontier_quark_route2_graph_first_su3_spatial_color_bridge_gate_no_go_2026_06_21.py)
**Runner output:** [outputs/frontier_quark_route2_graph_first_su3_spatial_color_bridge_gate_no_go_2026_06_21.txt](../outputs/frontier_quark_route2_graph_first_su3_spatial_color_bridge_gate_no_go_2026_06_21.txt)
**TRACE:** negative_route_pruning

This is not an audit verdict. It is a physics-loop steelman of the named
escape in the Route-2 `c_TE = -R_conn` cross-domain bridge route.

## Scope

The parent S3/Route-2 readout target remains:

```text
rho_E = beta_E/alpha_E = 21/4
<=> q_E = 15/8
<=> c_TE = gamma_T(center)/gamma_E(center) = -8/9.
```

The older color route says:

```text
F_adj = (N_c^2 - 1)/N_c^2 = 8/9
```

and asks whether the graph-first `N_c=3` from `d=3` construction supplies the
missing spatial-color bridge. This block grants that escape its strongest
reasonable form: use the same spatial 3-dimensional axis space and decompose
the full `3 x 3` matrix space.

## Strongest Steelman

Grant the graph-first result that the selected-axis construction gives a
canonical `3 + 1` base split and a compact semisimple `su(3)` on the
3-dimensional block. Then compare it with the spatial tensor decomposition
used by the `c_TE` route.

On the same 3-dimensional spatial axis space:

```text
End(R^3) = scalar A1 (1) + traceless adjoint (8).
```

The traceless part splits under spatial rotations/cubic symmetry as:

```text
traceless adjoint (8) = antisymmetric T1 (3) + symmetric traceless l2 (5)
                      = T1 (3) + E (2) + T2 (3).
```

The Route-2 `c_TE` readout lives inside the spin-2/cubic split:

```text
l2 = E (2) + T2 (3).
```

The color fraction lives at a different level:

```text
F_adj = dim(traceless adjoint) / dim(End(R^3)) = 8/9.
```

## Exact Dimension Routing

The runner checks the exact fractions:

| Quantity | Fraction |
|---|---:|
| traceless adjoint / total `End(R^3)` | `8/9` |
| scalar / total `End(R^3)` | `1/9` |
| spin-2 `l2` / total `End(R^3)` | `5/9` |
| `T2` / total `End(R^3)` | `1/3` |
| `E` / total `End(R^3)` | `2/9` |
| `T2/E` internal split ratio | `3/2` |
| `E/T2` internal split ratio | `2/3` |
| `T2/l2` internal fraction | `3/5` |
| `E/l2` internal fraction | `2/5` |
| `l2/adjoint` fraction | `5/8` |

Only the total traceless-adjoint fraction is `8/9`. None of the E/T2 or
spin-2-internal ratios is `8/9`, and dimension counting supplies no minus
sign.

## Theorem

**Theorem (graph-first spatial-color bridge gate no-go).** Even if the
graph-first `SU(3)` construction is granted as a typed `N_c=3` from `d=3`
spatial-color link, its dimension routing puts

```text
8/9
```

on the total traceless-adjoint fraction of `End(R^3)`, not on the Route-2
`E/T2` spin-2 readout ratio. The Route-2 target `c_TE=-8/9` would still require
an additional typed readout functional or orientation selector mapping that
total adjoint fraction into the signed E-center/T-center response ratio.

Thus the named graph-first escape does not retire the missing bridge.

## Relation To Prior No-Gos

This block sharpens the existing cross-domain no-go rather than merely
repeating it. The earlier note identified the only escape as a typed
`N_c=3`-from-`d=3` spatial-color link. This note grants that link at the
dimension-routing level and still finds that the `8/9` lives in the wrong
slot for `c_TE`.

The remaining bridge would need more than graph-first `SU(3)`:

```text
total traceless adjoint fraction
    -> signed E/T2 Route-2 center response
```

That arrow is a new source/readout theorem, not a consequence of the current
graph-first `SU(3)` integration theorem.

## Boundary

This note does not close the parent S3/Route-2 open gate. It does not derive
the endpoint triple, does not derive `rho_E=21/4`, and does not claim that no
future spatial-color theorem can exist.

It prunes only this route:

```text
graph-first SU(3) already types F_adj=8/9 as c_TE=-8/9.
```

The positive target remains a theorem that supplies a target-free signed
Route-2 E/T2 readout functional or an equivalent typed E-center selector.

## Verification

Run:

```bash
python3 scripts/frontier_quark_route2_graph_first_su3_spatial_color_bridge_gate_no_go_2026_06_21.py
```

Expected final line:

```text
TOTAL: PASS=46, FAIL=0
```
