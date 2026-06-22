# Quark Route-2 Normalization Functional Parity No-Go

**Date:** 2026-06-22
**Type:** no-go / same-source normalization parity obstruction packet
**Actual current-surface status:** no-go for neutral same-source scalar normalization fixing the antisymmetric E/T coefficient scale
**Trace class:** negative_route_pruning
**Primary runner:** [`scripts/frontier_quark_route2_normalization_functional_parity_no_go_2026_06_22.py`](../scripts/frontier_quark_route2_normalization_functional_parity_no_go_2026_06_22.py)
**Cached output:** [`outputs/frontier_quark_route2_normalization_functional_parity_no_go_2026_06_22.txt`](../outputs/frontier_quark_route2_normalization_functional_parity_no_go_2026_06_22.txt)

This is not an audit verdict. It does not run audit workers and does not apply
audit outcomes.

## Question

Block91 sharpened the missing primitive to a scale-normalized pure
antisymmetric Hessian coefficient theorem:

```text
(lambda_E, lambda_T) = s(1,-1) + t(1,1).
```

Assume an exact antisymmetric primitive is available. Can a neutral
same-source scalar normalization fix the remaining antisymmetric scale `s`
without adding typed E/T orientation data?

## Result

No. A neutral scalar normalization is E/T-swap invariant. In the coefficient
space

```text
V_ET = C(1,1) + C(1,-1),
```

an invariant linear normalization functional has the form

```text
N_+(lambda_E, lambda_T) = a(lambda_E + lambda_T).
```

It annihilates the antisymmetric line:

```text
N_+(s(1,-1)) = 0.
```

So it cannot set a nonzero finite scale on the pure antisymmetric coefficient
line. To see and normalize `s`, the functional needs an anti-invariant
component:

```text
N_-(lambda_E, lambda_T) = b(lambda_E - lambda_T).
```

But that anti-invariant component is already typed E/T orientation data. It is
not a neutral same-source scalar normalization. If such a functional is
supplied, it may fix scale on an already pure antisymmetric line, but it does
not also prove the required purity statement `t=0` unless a separate
antisymmetric projector or output-typing theorem is present.

Equivalently: one scalar normalization equation in the two-output coefficient
space leaves an affine one-parameter family unless the antisymmetric line is
already supplied; an invariant normalization cannot fix the antisymmetric scale
even after that line is supplied.

## Missing Primitive

The precise missing primitive is now sharper:

```text
Route-2 anti-invariant same-source E/T normalization and purity theorem:

construct a same-source physical E/T readout functional with an exact
anti-invariant component that fixes the antisymmetric Hessian coefficient
scale, prove the symmetric contamination coefficient is zero for the same
connected Hessian, and derive the E/T orientation from framework primitives
rather than an endpoint target.
```

No endpoint value is used.

Expected runner result:

```text
TOTAL: PASS=55, FAIL=0
```
