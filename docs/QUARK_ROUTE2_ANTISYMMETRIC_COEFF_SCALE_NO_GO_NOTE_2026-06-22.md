# Quark Route-2 Antisymmetric Coefficient Scale No-Go

**Date:** 2026-06-22
**Type:** no-go / antisymmetric coefficient scale obstruction packet
**Actual current-surface status:** no-go for an antisymmetric E/T direction alone fixing the connected-Hessian coefficient vector
**Trace class:** negative_route_pruning
**Primary runner:** [`scripts/frontier_quark_route2_antisymmetric_coeff_scale_no_go_2026_06_22.py`](../scripts/frontier_quark_route2_antisymmetric_coeff_scale_no_go_2026_06_22.py)
**Cached output:** [`outputs/frontier_quark_route2_antisymmetric_coeff_scale_no_go_2026_06_22.txt`](../outputs/frontier_quark_route2_antisymmetric_coeff_scale_no_go_2026_06_22.txt)

This is not an audit verdict. It does not run audit workers and does not apply
audit outcomes.

## Question

Block90 sharpened the missing primitive to an exact antisymmetric `E/T`
coefficient primitive. Suppose such a primitive were supplied and selected the
antisymmetric direction:

```text
A_ET = (1,-1).
```

Would that alone fix the Route-2 connected-Hessian coefficient vector?

## Result

No. An antisymmetric direction fixes a line, not a scale-normalized coefficient
vector.

The two-output coefficient vector decomposes as:

```text
(lambda_E, lambda_T) = s(1,-1) + t(1,1).
```

An antisymmetric primitive can at most supply the `(1,-1)` line. To become the
Route-2 connected-Hessian coefficient theorem, it must additionally prove:

1. the symmetric contamination coefficient `t` is zero, or otherwise fixed;
2. the antisymmetric scale `s` is fixed by a source/readout normalization;
3. the resulting vector is tied to the same connected Hessian, not to a
   separate carrier diagnostic.

Without these extra statements, there is a one-parameter scale family even on
the pure antisymmetric line and a two-parameter family if symmetric
contamination is not excluded.

## Missing Primitive

The precise missing primitive is:

```text
Route-2 scale-normalized pure-antisymmetric Hessian coefficient theorem:

construct an exact antisymmetric E/T primitive, prove it has no symmetric
coefficient contamination in the physical connected-Hessian readout, and fix
its scale from same-source normalization rather than an endpoint target.
```

No endpoint value is used.

Expected runner result:

```text
TOTAL: PASS=47, FAIL=0
```
