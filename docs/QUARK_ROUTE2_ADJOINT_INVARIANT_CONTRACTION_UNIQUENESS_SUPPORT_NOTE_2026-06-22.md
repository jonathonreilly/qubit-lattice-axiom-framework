# Quark Route-2 Adjoint Invariant Contraction Uniqueness Support

**Date:** 2026-06-22
**Type:** exact-support / orientation-free adjoint-Hessian contraction theorem
**Actual current-surface status:** exact-support for the invariant-contraction clause only; the Route-2 covariant multi-record source/readout family is not supplied
**Trace class:** upstream_support
**Primary runner:** [`scripts/frontier_quark_route2_adjoint_invariant_contraction_uniqueness_support_2026_06_22.py`](../scripts/frontier_quark_route2_adjoint_invariant_contraction_uniqueness_support_2026_06_22.py)
**Cached output:** [`outputs/frontier_quark_route2_adjoint_invariant_contraction_uniqueness_support_2026_06_22.txt`](../outputs/frontier_quark_route2_adjoint_invariant_contraction_uniqueness_support_2026_06_22.txt)

This is not an audit verdict. It does not run audit workers and does not apply
audit outcomes.

## Question

Block115 specified a conditional Route-2 bridge:

```text
same-source covariant adjoint multi-record Hessian
+ pure disconnected identity line
+ coefficient/source normalization
+ Killing contraction
-> kappa = 0.
```

The remaining concern is whether the orientation-free scalar readout could hide
some extra adjoint direction or alternative linear contraction. This block
isolates only that representation-theoretic clause.

## Result

For the `sl_3` adjoint representation:

```text
Hom_SU3(adj, 1) = 0,
Hom_SU3(Sym^2(adj), 1) = 1.
```

Equivalently, there is no nonzero invariant adjoint covector, and the
orientation-free linear scalar readout on a symmetric adjoint Hessian is unique
up to scale. In an orthonormal adjoint frame the contraction is:

```text
sum_A H_AA.
```

In an arbitrary basis it is the inverse-Killing contraction:

```text
K^{AB} H_AB.
```

Thus Block115's use of the Killing trace does not import a color-orientation
selector. Any orientation-free linear scalar readout on the adjoint Hessian is
the same contraction after one overall normalization.

## Boundary

This theorem does not supply the Route-2 covariant multi-record family. It also
does not fix the overall coefficient/source normalization. If the contraction is
multiplied by an unfixed scalar `lambda`, then the normalized `8/9` selector is
not forced until `lambda` is fixed by a Route-2 source/readout theorem.

The precise remaining primitive after this block is:

```text
Route-2 same-source covariant adjoint multi-record source/readout theorem:

construct records X_A for the physical Route-2 E/T source;
prove the physical readout is D_A D_B log Z on that same source;
prove the scalar identity line is pure disconnected;
and fix the coefficient/source normalization of the inverse-Killing contraction.
```

No endpoint value is used.

Expected runner result:

```text
TOTAL: PASS=55, FAIL=0
```
