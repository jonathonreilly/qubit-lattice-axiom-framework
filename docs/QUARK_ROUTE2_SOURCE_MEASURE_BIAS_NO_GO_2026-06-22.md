# Quark Route-2 Source-Measure Bias No-Go

**Date:** 2026-06-22
**Type:** no-go / binary source-measure bias selection obstruction
**Actual current-surface status:** no-go for ordinary binary source-measure controls forcing the Route-2 2:1 bias
**Trace class:** negative_route_pruning
**Primary runner:** [`scripts/frontier_quark_route2_source_measure_bias_no_go_2026_06_22.py`](../scripts/frontier_quark_route2_source_measure_bias_no_go_2026_06_22.py)
**Cached output:** [`outputs/frontier_quark_route2_source_measure_bias_no_go_2026_06_22.txt`](../outputs/frontier_quark_route2_source_measure_bias_no_go_2026_06_22.txt)

This is not an audit verdict. It does not run audit workers and does not apply
audit outcomes.

## Question

Blocks102-104 and 144 reduce the connected-cumulant source route to a binary
source-measure primitive:

```text
P(+1):P(-1) = 2:1 or 1:2.
```

Can ordinary current-surface measure controls force that bias once a signed
binary quotient is supplied?

## Result

No. For a signed binary source variable `X in {-1,+1}` with

```text
q := P(+1),
1-q := P(-1),
```

the same-source one-point and connected response are

```text
E[X] = 2q - 1,
D^2 log Z |0 = 1 - (2q - 1)^2 = 4q(1-q).
```

The connected selector `kappa=0` is equivalent to

```text
|E[X]| = 1/3
q in {1/3, 2/3}.
```

But normalization, positivity, RN absolute continuity, and sign-quotient data
allow a full interval of `q`. The common neutral choice `q=1/2` gives
`D^2 log Z |0 = 1` and `kappa=1`, not the selector. The signed quotient tells
which outcomes are `+` and `-`; it does not supply the source measure.

## Control Frames

| Control | Effect | Does it force `q in {1/3,2/3}`? |
|---|---|---|
| normalization | `q+(1-q)=1` | no |
| positivity | `0<q<1` | no |
| RN absolute continuity | both outcomes have positive reference weight | no |
| sign reversal | maps `q` to `1-q` | no, only flips orientation |
| neutral/uniform measure | selects `q=1/2` | no |
| connected-cumulant identity | computes `4q(1-q)` | no |

Thus the missing primitive is not another quotient or a generic measure axiom.
It is a Route-2 source-measure bias theorem.

## Missing Primitive

```text
Route-2 source-measure 2:1 bias theorem:

construct the same-source binary measure for the physical Route-2 signed
quotient and prove P(+1):P(-1)=2:1 or 1:2 from Route-2 structure. Then the
binary normal form and connected-cumulant subtraction force kappa=0 without
endpoint input.
```

No endpoint value is used as an input.

Expected runner result:

```text
TOTAL: PASS=87, FAIL=0
```
