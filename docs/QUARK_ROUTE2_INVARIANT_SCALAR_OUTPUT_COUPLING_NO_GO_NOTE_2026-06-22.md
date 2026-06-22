# Quark Route-2 Invariant Scalar-Output Coupling No-Go

**Date:** 2026-06-22
**Type:** no-go / source-readout arity obstruction packet
**Actual current-surface status:** no-go for invariant scalar-output Route-2 color coupling
**Trace class:** negative_route_pruning
**Primary runner:** [`scripts/frontier_quark_route2_invariant_scalar_output_coupling_no_go_2026_06_22.py`](../scripts/frontier_quark_route2_invariant_scalar_output_coupling_no_go_2026_06_22.py)
**Cached output:** [`outputs/frontier_quark_route2_invariant_scalar_output_coupling_no_go_2026_06_22.txt`](../outputs/frontier_quark_route2_invariant_scalar_output_coupling_no_go_2026_06_22.txt)

This is not an audit verdict. It does not run audit workers and does not apply
audit outcomes.

## Question

Block86 pruned the spectator-color attempt:

```text
Route-2 scalar carrier x End(C^3), with color-blind P_R.
```

The next nearby attempt is more subtle. Keep the physical `P_R/E-T` output as
two color-invariant scalars, but allow it to depend on the same color source.
Can such an invariant scalar output have the first-order connected adjoint
response needed for the Route-2 endpoint bridge?

## Result

No. A color-invariant scalar output has zero first-order response on the
`sl_3` tangent unless an extra color orientation is supplied.

At the trace-normalized color source,

```text
rho = I_3 / 3 + epsilon X,   X in sl_3.
```

The differential of a color-invariant scalar readout is a linear map

```text
dP : sl_3 -> C^2
```

whose two components are invariant linear functionals on the SU(3) adjoint
representation. But

```text
Hom_SU3(sl_3, C) = 0,
Hom_SU3(sl_3, C^2) = 0.
```

Equivalently, the only linear trace functional on `End(C^3)` restricts to zero
on `sl_3`. Higher scalar invariants such as `Tr(rho^2)` and `Tr(rho^3)` do not
repair this: their first derivatives at `I_3/3` are proportional to `Tr(X)`,
so they also vanish on the connected adjoint tangent.

Thus an invariant scalar `P_R/E-T` readout can see only disconnected scalar-line
data to first order. It cannot by itself supply the typed bridge

```text
same color source -> connected adjoint tangent -> Route-2 scalar output.
```

## What Would Be Needed

A nonzero first-order color response requires one of these additional
structures:

1. an adjoint-valued or covariant color-readout family, so the output is not
   merely a pair of invariant scalars;
2. an external adjoint covector, which is a color-orientation selector and is
   not present on the current source surface;
3. an orientation-free multi-record connected-cumulant theorem that packages a
   covariant color family and then subtracts the disconnected scalar line.

The first and third items are constructive targets. The second is an imported
selector and does not unblock the endpoint bridge.

## Missing Primitive

The precise missing primitive is:

```text
Route-2 covariant color-readout family or orientation-free multi-record
connected-cumulant source/readout theorem:

construct a same-source Route-2 readout whose data are covariant enough to see
the full sl_3 tangent, then prove that disconnected scalar-line subtraction
reduces that covariant family to the needed scalar endpoint bridge without
importing an endpoint value or color-orientation selector.
```

This block does not derive the endpoint value on the current surface. It prunes
only the route where the physical output remains a color-invariant scalar pair
throughout.

No endpoint value is used.

Expected runner result:

```text
TOTAL: PASS=50, FAIL=0
```
