# Quark Route-2 Color-Matrix Lift Sufficient Theorem

**Date:** 2026-06-22
**Type:** conditional-support / sufficient same-source color-matrix lift theorem
**Actual current-surface status:** conditional-support; the same-source lift premises are not current-surface theorems
**Trace class:** upstream_support
**Primary runner:** [`scripts/frontier_quark_route2_color_matrix_lift_sufficient_2026_06_22.py`](../scripts/frontier_quark_route2_color_matrix_lift_sufficient_2026_06_22.py)
**Cached output:** [`outputs/frontier_quark_route2_color_matrix_lift_sufficient_2026_06_22.txt`](../outputs/frontier_quark_route2_color_matrix_lift_sufficient_2026_06_22.txt)

This is not an audit verdict. It does not run audit workers and does not apply
audit outcomes.

## Question

Block113 gives exact support on the normalized color-source surface:

```text
trace-one color records + J in End(C^3)
-> connected tangent sl_3
-> connected fraction 8/9
-> kappa=0 on that source surface.
```

What exact Route-2 theorem would be sufficient to transfer that support to the
S3/Route-2 bridge without importing the endpoint value?

## Sufficient Theorem

Assume a Route-2 same-source color-matrix lift theorem with these clauses:

1. **Same-source lift:** the physical Route-2 `P_R/E-T` readout is a readout on
   the same source surface as a trace-one color-record ensemble.
2. **Full color source:** the source varies through Hermitian
   `J in End(C^3)`, not only a finite endpoint pullback or diagonal support
   family.
3. **Connected readout typing:** the physical connected Route-2 readout is the
   coefficient-normalized source Hessian `D_A D_B log Z` for that source.
4. **Singlet typing:** the identity color line is pure normalization /
   disconnected singlet for that same source.
5. **Output normalization:** the E/T coefficient map and source-coordinate
   normalization are fixed by framework primitives.

Then the identity source has zero centered score on trace-one records, so the
connected tangent is:

```text
End(C^3) / C I = sl_3.
```

Therefore:

```text
dim(sl_3) / dim(End(C^3)) = 8/9,
kappa = 0.
```

With the already separated endpoint-orientation sign support `sigma=-1`, the
oriented bridge gives:

```text
c_TE = -8/9.
```

The last line is a consequence of the assumed same-source theorem plus sign
orientation. It is not used as an input.

## Current-Surface Boundary

The clauses above are not all supplied on the current surface. Prior Route-2
blocks show that current `P_R/E-T` is not already a trace-one color-record
surface, finite endpoint lifts have centered rank at most three, and generic
source-measure/color support does not instantiate the Route-2 same-source full
color ensemble.

Thus this packet is a target theorem specification and exact implication
check. It does not close the bridge by itself.

No endpoint value is used.

Expected runner result:

```text
TOTAL: PASS=53, FAIL=0
```
