# Quark Route-2 Covariant Multi-Record Cumulant Sufficient Theorem

**Date:** 2026-06-22
**Type:** conditional-support / orientation-free covariant multi-record cumulant theorem
**Actual current-surface status:** conditional-support; the covariant multi-record Route-2 source/readout family is not supplied
**Trace class:** upstream_support
**Primary runner:** [`scripts/frontier_quark_route2_covariant_multirecord_cumulant_sufficient_2026_06_22.py`](../scripts/frontier_quark_route2_covariant_multirecord_cumulant_sufficient_2026_06_22.py)
**Cached output:** [`outputs/frontier_quark_route2_covariant_multirecord_cumulant_sufficient_2026_06_22.txt`](../outputs/frontier_quark_route2_covariant_multirecord_cumulant_sufficient_2026_06_22.txt)

This is not an audit verdict. It does not run audit workers and does not apply
audit outcomes.

## Question

Prior blocks pruned two shortcuts:

```text
invariant scalar output -> first-order sl_3 response
covariant family -> scalar invariant before Route-2 E/T typing
```

Is there a clean conditional theorem that keeps the covariant adjoint record
family through connected subtraction and only then contracts it
orientation-free?

## Sufficient Theorem

Assume Route-2 supplies a same-source covariant adjoint record family

```text
X_A,  A = 1,...,8,
```

with these clauses:

1. the records transform as an orthonormal `sl_3` adjoint family for the same
   Route-2 source;
2. the physical E/T readout is the connected source Hessian
   `D_A D_B log Z` for that family;
3. the scalar identity line is pure disconnected for the same source;
4. the E/T coefficient and source-coordinate normalization are fixed;
5. the final scalar readout is the orientation-free Killing contraction
   `sum_A D_A D_A log Z`, not a chosen adjoint covector.

Then the connected adjoint block has eight normalized directions and the
disconnected identity block has one normalized direction:

```text
adjoint / full = 8 / 9.
```

Therefore the connected selector is:

```text
kappa = 0.
```

The contraction is basis-independent: replacing the orthonormal adjoint basis
by another orthonormal basis preserves `sum_A H_AA`. This avoids importing a
color-orientation selector. It does not avoid the need for the Route-2 theorem
that supplies the covariant family and types it to the physical E/T readout.

No endpoint value is used.

Expected runner result:

```text
TOTAL: PASS=50, FAIL=0
```
