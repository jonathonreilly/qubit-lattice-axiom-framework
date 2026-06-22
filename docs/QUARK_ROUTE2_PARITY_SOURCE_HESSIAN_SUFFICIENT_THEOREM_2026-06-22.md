# Quark Route-2 Parity Source-Hessian Sufficient Theorem

**Date:** 2026-06-22
**Type:** conditional-support / sufficient typed source-Hessian theorem packet
**Actual current-surface status:** conditional-support for a typed parity source-Hessian theorem forcing kappa=0
**Trace class:** upstream_support
**Primary runner:** [`scripts/frontier_quark_route2_parity_source_hessian_sufficient_2026_06_22.py`](../scripts/frontier_quark_route2_parity_source_hessian_sufficient_2026_06_22.py)
**Cached output:** [`outputs/frontier_quark_route2_parity_source_hessian_sufficient_2026_06_22.txt`](../outputs/frontier_quark_route2_parity_source_hessian_sufficient_2026_06_22.txt)

This is not an audit verdict. It does not run audit workers and does not apply
audit outcomes.

## Question

Blocks 91 and 92 sharpened the coefficient obstruction:

```text
(lambda_E, lambda_T) = s(1,-1) + t(1,1).
```

The remaining bridge needs both purity (`t=0` in the connected readout) and an
anti-invariant same-source normalization for `s`. What exact source-Hessian
premises would be sufficient to force `kappa=0` without importing the endpoint
value?

## Sufficient Theorem

Let the same-source Route-2 E/T output Hessian decompose into E/T parity lines:

```text
H_raw = s A_ET B_adj + t S_ET D_singlet
A_ET = (1,-1)
S_ET = (1,1)
```

where `B_adj` is the connected adjoint color bilinear and `D_singlet` is a
factorizable singlet/disconnected product for the same source. Then the
connected source Hessian

```text
H_conn = D^2 log Z
```

subtracts the factorizable singlet product and leaves

```text
H_conn = s A_ET B_adj.
```

Therefore the connected singlet coefficient is exactly zero:

```text
kappa = 0.
```

If, in addition, a same-source E/T anti-invariant normalization functional
`N_-` is derived from framework primitives and satisfies `N_-(A_ET) != 0`, it
fixes the remaining antisymmetric scale `s`. No endpoint value is used.

## What This Does Not Prove

This packet does not prove that the current Route-2 physical readout satisfies
the theorem premises. In particular, it does not construct:

1. the same-source Route-2 E/T source/readout Hessian;
2. the pure-disconnected typing of the symmetric singlet term;
3. the anti-invariant E/T normalization functional from retained framework
   primitives.

## Missing Primitive

The exact remaining primitive is:

```text
Route-2 typed parity source-Hessian bridge theorem:

construct the same-source physical E/T output Hessian, prove its symmetric
E/T line is pure factorizable disconnected singlet for the same source, prove
its antisymmetric line is the connected adjoint color bilinear, and derive the
anti-invariant E/T normalization from framework primitives rather than an
endpoint target.
```

Expected runner result:

```text
TOTAL: PASS=70, FAIL=0
```
