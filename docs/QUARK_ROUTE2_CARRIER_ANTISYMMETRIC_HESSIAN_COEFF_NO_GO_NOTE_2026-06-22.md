# Quark Route-2 Carrier Antisymmetric Hessian Coefficient No-Go

**Date:** 2026-06-22
**Type:** no-go / carrier E/T coefficient primitive obstruction packet
**Actual current-surface status:** no-go for deriving Hessian E/T coefficient normalization from the current carrier-orbit result
**Trace class:** negative_route_pruning
**Primary runner:** [`scripts/frontier_quark_route2_carrier_antisymmetric_hessian_coeff_no_go_2026_06_22.py`](../scripts/frontier_quark_route2_carrier_antisymmetric_hessian_coeff_no_go_2026_06_22.py)
**Cached output:** [`outputs/frontier_quark_route2_carrier_antisymmetric_hessian_coeff_no_go_2026_06_22.txt`](../outputs/frontier_quark_route2_carrier_antisymmetric_hessian_coeff_no_go_2026_06_22.txt)

This is not an audit verdict. It does not run audit workers, does not perform a
registry audit, and does not apply audit outcomes.

## Question

Block89 showed that a connected color Hessian leaves the two Route-2 `E/T`
output coefficients free:

```text
H_E = lambda_E B,   H_T = lambda_T B.
```

Could the existing carrier-orbit invariance work supply the missing
coefficient-normalization theorem?

## Result

No. The carrier-orbit result is useful support, but it does not provide an
exact antisymmetric `E/T` coefficient primitive for the connected Hessian.

The `E/T` output coefficient space decomposes under the E/T swap into:

```text
C^2 = C(1,1) + C(1,-1).
```

The symmetric line is not enough to distinguish the `E` and `T` coefficient
roles. A theorem that fixes a nontrivial Route-2 `E/T` coefficient vector
needs an exact carrier/output primitive that selects the required coefficient
line and ties it to the same connected Hessian.

The carrier-orbit invariance packet does not supply that primitive. It records
a partial `Z_2` operator classification and a current-registry check:

- current enumerated carrier primitives lie in the swap-symmetric component;
- `Theta_R^(0)` and `Xi_R^(0)` are bounded candidates, not exact coefficient
  normalization theorems;
- an exact antisymmetric carrier primitive remains blocked on registry
  closure or a new constructive operator.

Thus carrier-orbit invariance does not close Block89. It sharpens the next
missing primitive.

## Missing Primitive

The precise missing primitive is:

```text
Route-2 exact antisymmetric E/T Hessian-coefficient primitive:

construct an exact E/T output-space primitive on the Route-2 carrier that
selects the required coefficient vector for the same-source connected Hessian,
or prove a registry-closure theorem that no such primitive exists and choose a
different source/readout route.
```

No endpoint value is used.

Expected runner result:

```text
TOTAL: PASS=48, FAIL=0
```
