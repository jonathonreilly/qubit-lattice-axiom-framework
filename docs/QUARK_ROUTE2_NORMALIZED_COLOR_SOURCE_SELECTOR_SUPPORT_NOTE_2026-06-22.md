# Quark Route-2 Normalized Color-Source Selector Support

**Date:** 2026-06-22
**Type:** exact-support / normalized color-matrix source selector
**Actual current-surface status:** exact-support on the normalized color-source surface; no current Route-2 transfer
**Trace class:** upstream_support
**Primary runner:** [`scripts/frontier_quark_route2_normalized_color_source_selector_support_2026_06_22.py`](../scripts/frontier_quark_route2_normalized_color_source_selector_support_2026_06_22.py)
**Cached output:** [`outputs/frontier_quark_route2_normalized_color_source_selector_support_2026_06_22.txt`](../outputs/frontier_quark_route2_normalized_color_source_selector_support_2026_06_22.txt)

This is not an audit verdict. It does not run audit workers and does not apply
audit outcomes.

## Question

Block112 isolated a three-lock physical connected-Hessian bridge. One lock is
already well understood on its own source surface:

```text
normalized trace-one color records
Hermitian color-matrix source J in End(C^3)
connected score score_J(rho) = Tr(J rho) - E[Tr(J rho)].
```

What exact selector does that source surface supply, and what does it still not
transfer to Route-2?

## Exact Support On The Color-Source Surface

On trace-one color records,

```text
Tr(rho) = 1.
```

For the identity source `J = lambda I`,

```text
Tr(J rho) = lambda,
score_J(rho) = lambda - E[lambda] = 0.
```

Therefore the identity color source is pure normalization and the connected
color-source tangent factors through

```text
End(C^3) / C I = sl_3.
```

The exact dimension fraction is:

```text
dim(sl_3) / dim(End(C^3)) = 8 / 9.
```

On this source surface, the singlet/identity line is removed by connected
centering and the connected selector is exactly:

```text
kappa = 0.
```

## Route-2 Transfer Boundary

This is not a Route-2 endpoint derivation. The current `K_R -> P_R` surface has
not been proved to be this normalized color-matrix source. To consume this
support, Route-2 still needs:

```text
same-source normalized color-matrix source lift;
trace-one color records for the physical Route-2 readout;
identification of the Route-2 E/T readout with D_A D_B log Z on that source;
E/T coefficient and source-coordinate normalization.
```

Without those transfer primitives, this packet is exact upstream support only.
It does not close `R_conn -> c_TE=-8/9`, does not derive the endpoint triple,
and does not apply an audit verdict.

No endpoint value is used.

Expected runner result:

```text
TOTAL: PASS=68, FAIL=0
```
