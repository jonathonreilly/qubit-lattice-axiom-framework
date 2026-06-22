# Quark Route-2 Graph-First Spatial/Color Bridge No-Go

**Date:** 2026-06-22
**Claim type:** no_go
**Actual current-surface status:** no-go for graph-first spatial/color bridge closure
**Trace class:** negative_route_pruning
**Runner:** `scripts/frontier_quark_route2_graph_first_spatial_color_bridge_no_go_2026_06_22.py`

Actual current-surface status: no-go for graph-first spatial/color bridge
closure.

## Scope

This block attacks the explicit residual left by the earlier cross-domain
`c_TE = -R_conn` note: perhaps the `GRAPH_FIRST_SU3` construction supplies the
hidden typed spatial/color link.

It tests that escape directly.  The graph-first theorem is allowed as support:

```text
selected graph axis -> weak su(2) + residual swap -> gl(3)+gl(1) -> SU(3)
```

The Route-2 readout target remains:

```text
R_conn -> c_TE = -8/9
```

or equivalently a typed connected-cumulant / disconnected-subtraction readout
theorem that forces the connected selector.

This is not an audit verdict.  It does not resolve the parent
[`S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md`](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md)
row.

## Graph-First Support

The verifier reuses the selected-axis graph-first construction for all three
candidate axes.  On each axis it checks:

```text
dim Comm(weak su(2)) = 16
dim Comm(weak su(2), residual swap) = 10
rank Pi_+ = 6
rank Pi_- = 2
graph-first color rank = 3
```

Thus graph-first SU(3) supplies color rank support and the familiar SU(3)
adjoint fraction support:

```text
F_adj = 8/9.
```

This is real upstream support.  It is not yet the Route-2 center readout.

## Route-2 Readout Surface

The Route-2 center ratio is a cubic tensor-response slot.  The verifier builds
the finite `l=2` symmetric-traceless tensor model and the proper octahedral
group action.  It checks:

```text
|O| = 24
dim l=2 = 5
l=2 has no cubic A1 singlet
l=2 splits into two irreducible cubic summands
E block dimension = 2
T2 block dimension = 3
```

So the center readout lives on the cubic `l=2` `E/T2` split.  The graph-first
commutant theorem lives on the selected-axis taste graph/color surface.  The
two surfaces have different carriers:

```text
graph-first taste space: 8 dimensions
cubic l=2 tensor space: 5 dimensions
```

Dimension mismatch is not by itself a theorem of impossibility.  It is the
typed warning: a bridge theorem must supply an actual map between these
carriers, not just reuse the scalar value `3`.

## Reachability

The generated graph/readout edge set has two separated pieces:

```text
graph_selected_axis -> graph_weak_su2
graph_selected_axis -> graph_residual_swap
graph_weak_su2 + graph_residual_swap -> graph_commutant_gl3_gl1
graph_commutant_gl3_gl1 -> su3_color_rank_3
su3_color_rank_3 -> su3_adjoint_fraction_8_9
```

and

```text
spatial_l2_tensor -> cubic_l2_E_T2_split -> route2_c_TE_readout_slot
route2_c_TE_minus_8_9 -> route2_q_E_15_8 -> route2_rho_E_21_4
```

On this bank:

```text
su3_adjoint_fraction_8_9
```

does not reach:

```text
route2_rho_E_21_4.
```

If the missing bridge is added as a premise, the endpoint path appears
immediately:

```text
su3_adjoint_fraction_8_9 -> route2_c_TE_minus_8_9
  -> route2_q_E_15_8 -> route2_rho_E_21_4.
```

A stronger hypothetical functor

```text
graph_commutant_gl3_gl1 -> route2_c_TE_readout_slot
```

would only reach the readout slot.  It still would not select the signed value
`c_TE = -8/9`.

## Missing Primitive

The precise missing primitive is stronger than graph-first SU(3) rank support:

```text
a typed functor from the selected-axis graph/color commutant to the Route-2
cubic `l=2` `E/T2` center-response readout
```

plus the two bridge switches isolated by the factorization block:

```text
orientation sign `sigma=-1`
connected selector `kappa=0`
```

The graph-first construction can justify the availability of an SU(3) color
surface and the scalar adjoint fraction `8/9`.  It does not by itself provide
the signed Route-2 center ratio, nor the connected/disconnected subtraction
selector.

## Result

The graph-first escape is pruned in its current form:

```text
graph-first SU(3) supplies color rank support, not a typed Route-2 readout map.
```

The remaining positive theorem target is unchanged but now more precise:

```text
derive the typed graph/color -> cubic E/T2 center-readout functor,
derive sigma=-1,
derive kappa=0.
```

Without those primitives, `R_conn = 8/9` remains conditional upstream support
for the bridge target rather than a current-surface derivation of
`c_TE = -8/9`.

## Validation

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_graph_first_spatial_color_bridge_no_go_2026_06_22.py
```

Expected result:

```text
TOTAL: PASS=69, FAIL=0
```
