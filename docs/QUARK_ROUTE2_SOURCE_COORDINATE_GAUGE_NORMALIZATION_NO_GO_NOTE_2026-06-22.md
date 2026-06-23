# Quark Route-2 Source-Coordinate Gauge Normalization No-Go

**Date:** 2026-06-22
**Type:** no-go / source-coordinate origin and scale normalization obstruction
**Actual current-surface status:** no-go for formal source coordinates or connected Hessian data alone fixing the raw/disconnected Route-2 product normalization
**Trace class:** negative_route_pruning
**Primary runner:** [`scripts/frontier_quark_route2_source_coordinate_gauge_normalization_no_go_2026_06_22.py`](../scripts/frontier_quark_route2_source_coordinate_gauge_normalization_no_go_2026_06_22.py)
**Cached output:** [`outputs/frontier_quark_route2_source_coordinate_gauge_normalization_no_go_2026_06_22.txt`](../outputs/frontier_quark_route2_source_coordinate_gauge_normalization_no_go_2026_06_22.txt)

This is not an audit verdict. It does not run audit workers and does not apply
audit outcomes.

## Question

Blocks97-100 pruned the shortcuts from finite `P_R` slots to a physical
source-Hessian/product registry. Blocks107-110 then sharpened the remaining
`kappa=0` route to:

```text
same-source variables X,Y
E[XY] = 1
E[X]E[Y] = 1/9
connected = E[XY] - E[X]E[Y] = 8/9.
```

Suppose a future source-action theorem supplies connected-Hessian data. Does
formal source-coordinate or connected-Hessian data by itself fix the raw
moment and disconnected-product normalization needed by that theorem?

## Result

No. The raw/disconnected decomposition is not fixed until the physical source
variables have a fixed origin and scale.

Start from the target signed source model:

```text
P(+1)=2/3, P(-1)=1/3,
X=Y,
E[XY]=1,
E[X]E[Y]=1/9,
connected=8/9.
```

Now shift the source variables by constants:

```text
X' = X + a,
Y' = Y + b.
```

The connected Hessian is unchanged:

```text
E[X'Y'] - E[X']E[Y'] = 8/9.
```

But the raw moment and disconnected product move together:

```text
E[X'Y'] = 1 + (a+b)/3 + ab,
E[X']E[Y'] = 1/9 + (a+b)/3 + ab.
```

For example:

```text
(a,b)=(0,0)  -> raw=1,   product=1/9
(a,b)=(1,0)  -> raw=4/3, product=4/9
(a,b)=(1,1)  -> raw=8/3, product=16/9
```

All three have the same connected Hessian `8/9`. Therefore a connected
Hessian certificate alone can support the selector, but it does not identify
which raw moment is `1` or which one-point product is `1/9`. Those are
source-origin statements.

Multiplicative source rescaling creates a separate scale gate. If

```text
X'' = sX,
Y'' = tY,
```

then raw, disconnected product, and connected Hessian all scale by `st`.
The ratio `connected/raw = 8/9` is invariant on the target model, but the
absolute Route-2 coefficient is not fixed until the source/readout scale is
fixed.

## What This Prunes

This block prunes the shortcut:

```text
formal source coordinates or connected Hessian data
-> raw E[XY]=1 and disconnected product E[X]E[Y]=1/9.
```

It does not rule out a positive source-action theorem. It says that such a
theorem must fix the source variables as physical record variables, not only
up to affine source-coordinate gauge.

## Missing Primitive

The exact missing primitive is:

```text
Route-2 source-coordinate gauge-fixing theorem:

construct the physical same-source Route-2 variables X,Y and source
coordinates; fix their additive origin and multiplicative scale from
framework/source-readout primitives; prove E[XY]=1 and E[X]E[Y]=1/9 in that
fixed gauge; and prove the fixed variables are the same variables used by the
physical P_R/E-T connected Hessian.
```

Equivalently, a future connected-Hessian bridge can bypass the raw/product
normal form only if it directly proves the physical Route-2 readout is
`D_A D_B log Z` with coefficient normalization already fixed. Without one of
those two typed primitives, formal source coordinates and connected covariance
support do not force the endpoint bridge.

No endpoint value is used.

Expected runner result:

```text
TOTAL: PASS=86, FAIL=0
```
