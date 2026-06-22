# Quark Route-2 Non-Binary Product Normal-Form Support

**Date:** 2026-06-22
**Type:** conditional-support / non-binary one-point product normal form
**Actual current-surface status:** conditional-support for a same-source one-point product normal form
**Trace class:** upstream_support
**Primary runner:** [`scripts/frontier_quark_route2_nonbinary_product_normal_form_support_2026_06_22.py`](../scripts/frontier_quark_route2_nonbinary_product_normal_form_support_2026_06_22.py)
**Cached output:** [`outputs/frontier_quark_route2_nonbinary_product_normal_form_support_2026_06_22.txt`](../outputs/frontier_quark_route2_nonbinary_product_normal_form_support_2026_06_22.txt)

This is not an audit verdict. It does not run audit workers and does not apply
audit outcomes.

## Question

Blocks102-106 pursued the binary same-record route. That route reduces
`kappa=0` to a sharp-record bias selector. Is the binary/log-odds selector
actually necessary for the connected-cumulant route?

## Result

No. The connected-cumulant product theorem has a broader non-binary normal
form. Let `X` and `Y` be same-source Route-2 record readouts with raw moment

```text
E[XY] = 1.
```

Then the P-cal connected readout is

```text
E[XY] - E[X]E[Y] = 1 - uv,
```

where

```text
u = E[X],  v = E[Y].
```

Inside this normal form,

```text
kappa = 9 * ((1 - uv) - 8/9) = 1 - 9uv.
```

Therefore

```text
kappa = 0  <=>  E[X]E[Y] = uv = 1/9.
```

The binary same-record case `u=v=+/-1/3` is one subcase of this product
theorem, not the only possible route. Other same-source product examples such
as `(u,v)=(1,1/9)` or `(2/3,1/6)` also give the same connected selector if a
Route-2 theorem supplies those one-point readouts.

## What This Moves

This packet converts the remaining bridge into a broader primitive:

```text
Route-2 same-source one-point product theorem:

construct the physical Route-2 source/readout variables X and Y; prove the
raw moment E[XY]=1 on that same source; and prove E[X]E[Y]=1/9 without using
endpoint values or fitted source weights.
```

If that theorem is supplied, the existing P-cal/Mobius connected subtraction
forces `kappa=0` without requiring a binary signed record or log-odds selector.
If it is not supplied, this remains conditional support only.

No endpoint value is used.

Expected runner result:

```text
TOTAL: PASS=70, FAIL=0
```
