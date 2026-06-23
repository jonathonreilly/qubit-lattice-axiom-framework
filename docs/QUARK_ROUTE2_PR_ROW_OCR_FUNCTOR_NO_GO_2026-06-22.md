# Quark Route-2 P_R Row to O_CR Functor No-Go

**Date:** 2026-06-22
**Type:** no-go / finite P_R rows to physical O_CR observable functor
**Actual current-surface status:** no-go for current finite P_R rows alone constructing the physical O_CR observable
**Trace class:** negative_route_pruning
**Primary runner:** [`scripts/frontier_quark_route2_pr_row_ocr_functor_no_go_2026_06_22.py`](../scripts/frontier_quark_route2_pr_row_ocr_functor_no_go_2026_06_22.py)
**Cached output:** [`outputs/frontier_quark_route2_pr_row_ocr_functor_no_go_2026_06_22.txt`](../outputs/frontier_quark_route2_pr_row_ocr_functor_no_go_2026_06_22.txt)

This is not an audit verdict. It does not run audit workers and does not apply
audit outcomes.

## Question

Block141's carrier-observable frame failed because finite `P_R` rows are
carrier/readout outputs, not a physical source observable. This block isolates
that frame:

```text
Do the current finite P_R rows canonically define O_CR?
```

## Result

No. The exact readout packet supplies the row form

```text
P_R = [[alpha_E, 0, beta_E, 0],
       [0, alpha_T, 0, beta_T]].
```

This gives two channel rows on the restricted carrier basis. A physical
`O_CR` source observable must instead be a scalar random variable on the same
source space as the RN path and Block121 connected scalar. There is no current
functor

```text
Phi_OCR : P_R/E-T rows -> O_CR
```

that preserves source coordinates, covariance response, Fisher-unit Riesz
typing, and the unit isometry.

## Non-Uniqueness

On the four formal slots, many endpoint-free scalarizations are compatible
with the same row labels:

```text
E-channel indicator      -> covariance 0
T-channel indicator      -> covariance 0
center indicator         -> covariance +1/2
E-center indicator       -> covariance +1/4
center-minus-shell score -> covariance +1
```

Finite `P_R` row labels alone do not choose among these scalar observables.

## Missing Primitive

The exact missing primitive is:

```text
Route-2 P_R-to-O_CR functor theorem:

construct a typed functor Phi_OCR from the finite P_R/E-T row surface to a
scalar source observable O_CR; prove Phi_OCR is defined on the same source
coordinate and RN path used by the center-ratio covariance score; and prove
it preserves the same-source Fisher-unit Riesz line to Block121.
```

No endpoint value is used as an input.

Expected runner result:

```text
TOTAL: PASS=72, FAIL=0
```
