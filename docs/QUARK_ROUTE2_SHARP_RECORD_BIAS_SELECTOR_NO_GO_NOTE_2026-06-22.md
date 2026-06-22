# Quark Route-2 Sharp-Record Bias Selector No-Go

**Date:** 2026-06-22
**Type:** no-go / sharp-record source-measure bias-selector obstruction packet
**Actual current-surface status:** no-go for the generic sharp-record RN/Fisher toolkit selecting the Route-2 binary bias
**Trace class:** negative_route_pruning
**Primary runner:** [`scripts/frontier_quark_route2_sharp_record_bias_selector_no_go_2026_06_22.py`](../scripts/frontier_quark_route2_sharp_record_bias_selector_no_go_2026_06_22.py)
**Cached output:** [`outputs/frontier_quark_route2_sharp_record_bias_selector_no_go_2026_06_22.txt`](../outputs/frontier_quark_route2_sharp_record_bias_selector_no_go_2026_06_22.txt)

This is not an audit verdict. It does not run audit workers and does not apply
audit outcomes.

## Question

Block104 refined the missing primitive to a typed signed quotient plus a
source-measure bias theorem. The repo already has a generic sharp-record
source-measure toolkit: RN cocycles, Fisher unit tangents, and the finite
P-cal connected-response generator. Can that toolkit itself select the
required Route-2 bias?

## Result

No. The generic sharp-record surface supplies the normalized two-outcome
reference

```text
P0(+1) = P0(-1) = 1/2
```

and the RN exponential chart

```text
mu_h(epsilon) = P0(epsilon) exp(h epsilon) / Z(h).
```

Writing

```text
q = exp(2h),
```

the induced source law is

```text
P_h(+1) = q/(1+q),
P_h(-1) = 1/(1+q),
E_h[epsilon] = (q-1)/(q+1).
```

The Block102 one-point bias `|E_h[epsilon]| = 1/3` is therefore equivalent to

```text
q = 2 or q = 1/2,
```

that is

```text
h = +(1/2) log 2 or h = -(1/2) log 2.
```

The generic source-measure theorems construct the chart and its unit tangent.
They do not select this nonzero displacement. At the chart origin `h=0`, the
signed record is unbiased and the connected same-record value is `1`, giving
`kappa=1` in the Block102 normal form, not `kappa=0`.

Thus the remaining primitive is sharper:

```text
Route-2 sharp-record bias-selector theorem:

after constructing the typed same-source signed quotient, prove that the
Route-2 source measure sits at h = +/- (1/2) log 2 in the RN chart, or
equivalently prove the 2:1 / 1:2 signed-outcome source-measure ratio.
```

No endpoint value is used.

Expected runner result:

```text
TOTAL: PASS=67, FAIL=0
```
