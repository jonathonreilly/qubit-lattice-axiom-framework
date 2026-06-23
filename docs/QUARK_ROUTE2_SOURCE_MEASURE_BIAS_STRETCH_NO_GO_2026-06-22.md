# Quark Route-2 Source-Measure Bias Stretch No-Go

**Date:** 2026-06-22
**Type:** no-go / first-principles stretch attempt on Route-2 source-measure 2:1 bias
**Actual current-surface status:** no-go for deriving the Route-2 2:1 source-measure bias from the minimal current premises
**Trace class:** negative_route_pruning
**Primary runner:** [`scripts/frontier_quark_route2_source_measure_bias_stretch_no_go_2026_06_22.py`](../scripts/frontier_quark_route2_source_measure_bias_stretch_no_go_2026_06_22.py)
**Cached output:** [`outputs/frontier_quark_route2_source_measure_bias_stretch_no_go_2026_06_22.txt`](../outputs/frontier_quark_route2_source_measure_bias_stretch_no_go_2026_06_22.txt)

This is not an audit verdict. It does not run audit workers and does not apply
audit outcomes.

## A_min

Allowed premises:

- exact four Route-2 labels `E-shell`, `E-center`, `T-shell`, `T-center`;
- deterministic signed quotient `sigma:L->{-1,+1}`;
- binary source measure `q=P(+1)`;
- normalization and positivity;
- connected-cumulant identity `D^2 log Z = 1 - (2q-1)^2`;
- Block145 source-measure bias boundary.

Forbidden imports:

- endpoint value or endpoint triple;
- fitted scalar calibration;
- observed comparator;
- assertion that physical `J_CR` already has `q=2/3`.

## Fan-Out Attempt

Five independent frames were tested:

| Frame | Attempt | Wall |
|---|---|---|
| label-count | count signs over four labels | uniform means are `-1`, `-1/2`, `0`, `1/2`, `1`, not `+/-1/3` |
| signed quotient | choose a deterministic quotient | quotient supplies signs but not `q` |
| RN positivity | require positive reference weights | admits the interval `0<q<1` |
| neutral measure | maximize the neutral product proxy `q(1-q)` | selects `q=1/2`, giving `kappa=1` |
| sign reversal | use orientation reversal | maps `q` to `1-q` but does not select `|2q-1|=1/3` |

## Synthesis Wall

Every frame hits the same missing primitive:

```text
Route-2 source-measure 2:1 bias theorem:

derive q in {1/3, 2/3} from physical Route-2 source/readout structure.
```

No endpoint value is used as an input.

Expected runner result:

```text
TOTAL: PASS=76, FAIL=0
```
