# Quark Route-2 Color-Marginal Product Support/No-Go

**Date:** 2026-06-22
**Type:** support/no-go boundary for same-source color-marginal product transfer
**Actual current-surface status:** conditional-support for a color-marginal one-point product; no-go for current Route-2 transfer
**Trace class:** upstream_support
**Primary runner:** [`scripts/frontier_quark_route2_color_marginal_product_support_no_go_2026_06_22.py`](../scripts/frontier_quark_route2_color_marginal_product_support_no_go_2026_06_22.py)
**Cached output:** [`outputs/frontier_quark_route2_color_marginal_product_support_no_go_2026_06_22.txt`](../outputs/frontier_quark_route2_color_marginal_product_support_no_go_2026_06_22.txt)

This is not an audit verdict. It does not run audit workers and does not apply
audit outcomes.

## Question

Block107 showed that the connected-cumulant route does not require a binary
log-odds selector if a same-source one-point product theorem supplies

```text
E[X]E[Y] = 1/9.
```

Can existing SU(3) color-marginal support supply a narrow `1/9` product route?

## Result

It supplies exact upstream support, but not the Route-2 transfer.

On the uniform normalized trace state of `C^3`, any rank-one color projector
`P_i` has

```text
<P_i> = Tr(P_i) / 3 = 1/3.
```

Therefore two such one-point marginals have disconnected product

```text
<P_i><P_j> = 1/9.
```

This is exactly the product needed by Block107. If Route-2 supplied same-source
record variables `X,Y` whose one-point readouts are such color marginals, and
also supplied the raw moment `E[XY]=1`, then P-cal connected subtraction would
force `kappa=0` without a binary signed record or endpoint input.

The current Route-2 surface does not supply that transfer. Existing color
channel-fraction support proves SU(3) dimension fractions and color projector
algebra. Prior Route-2 color-transfer blocks show that the current `P_R/E-T`
endpoint surface is not already a same-source full color-record ensemble. This
block narrows the possible positive route to a smaller primitive:

```text
Route-2 same-source color-marginal product theorem:

prove that the physical Route-2 source/readout variables have one-point
color-marginal expectations 1/3 and 1/3 on the same source, and raw moment
E[XY]=1, so that their disconnected product is 1/9.
```

No endpoint value is used.

Expected runner result:

```text
TOTAL: PASS=56, FAIL=0
```
