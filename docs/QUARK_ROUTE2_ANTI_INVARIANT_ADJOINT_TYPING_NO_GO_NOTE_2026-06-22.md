# Quark Route-2 Anti-Invariant Adjoint Typing No-Go

**Date:** 2026-06-22
**Type:** no-go / anti-invariant output parity versus adjoint color typing packet
**Actual current-surface status:** no-go for anti-invariant E/T parity alone proving the connected term is the adjoint color bilinear
**Trace class:** negative_route_pruning
**Primary runner:** [`scripts/frontier_quark_route2_anti_invariant_adjoint_typing_no_go_2026_06_22.py`](../scripts/frontier_quark_route2_anti_invariant_adjoint_typing_no_go_2026_06_22.py)
**Cached output:** [`outputs/frontier_quark_route2_anti_invariant_adjoint_typing_no_go_2026_06_22.txt`](../outputs/frontier_quark_route2_anti_invariant_adjoint_typing_no_go_2026_06_22.txt)

This is not an audit verdict. It does not run audit workers and does not apply
audit outcomes.

## Question

Block93 also requires the antisymmetric E/T line to be the connected adjoint
color bilinear. Does anti-invariant E/T output parity alone prove that color
typing?

## Result

No. E/T anti-invariance is an output-channel parity statement. Adjointness is
a color-source representation statement.

An anti-invariant connected response can decompose as:

```text
A_total = a_adj A_ET B_adj + a_0 A_ET C_0
A_ET = (1,-1)
```

where `B_adj` is the `sl_3` adjoint bilinear and `C_0` is a connected
color-scalar or other non-adjoint same-source connected residue. Both terms are
E/T-anti-invariant. An anti-invariant E/T normalization sees the sum
`a_adj + a_0`; it does not identify which part is the adjoint color bilinear.

Thus the Route-2 bridge still needs a representation-typed theorem that the
physical antisymmetric E/T connected Hessian is exactly the adjoint color
bilinear and has no non-adjoint connected residue.

## Missing Primitive

The exact missing primitive is:

```text
Route-2 anti-invariant adjoint-line typing theorem:

for the same-source physical E/T source-Hessian readout, prove the
E/T-anti-invariant connected line is the SU(3) adjoint color bilinear and has
no connected color-scalar or other non-adjoint residue, using framework
primitives rather than endpoint input.
```

No endpoint value is used.

Expected runner result:

```text
TOTAL: PASS=67, FAIL=0
```
