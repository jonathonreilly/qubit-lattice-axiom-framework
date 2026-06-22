# Quark Route-2 Scalar-Partition Product Selector No-Go

**Date:** 2026-06-22
**Type:** no-go / normalization-only scalar source-product selector obstruction
**Actual current-surface status:** no-go for normalized scalar partitions alone forcing the Route-2 one-point product `1/9`
**Trace class:** negative_route_pruning
**Primary runner:** [`scripts/frontier_quark_route2_scalar_partition_product_selector_no_go_2026_06_22.py`](../scripts/frontier_quark_route2_scalar_partition_product_selector_no_go_2026_06_22.py)
**Cached output:** [`outputs/frontier_quark_route2_scalar_partition_product_selector_no_go_2026_06_22.txt`](../outputs/frontier_quark_route2_scalar_partition_product_selector_no_go_2026_06_22.txt)

This is not an audit verdict. It does not run audit workers and does not apply
audit outcomes.

## Question

Block107 reduced the connected-cumulant route to the same-source product
primitive:

```text
E[XY] = 1,
E[X]E[Y] = 1/9.
```

Block108 supplied color-marginal support for the `1/9` product, and Block109
showed that the current `P_R/E-T` labels do not transfer that color-marginal
support. This block tests a different shortcut:

```text
normalized scalar source partition
-> same-source one-point product 1/9.
```

Can scalar normalization alone force the needed disconnected product without a
color projector theorem, binary bias theorem, endpoint value, or finite-box
comparator?

## Result

No. Normalization alone does not select the one-point product. Even after
granting a same-source raw moment

```text
E[XY] = 1,
```

there is a normalized scalar counterfamily with `X=Y in {+1,-1}`:

```text
P(+1) = p,
P(-1) = 1-p,
E[XY] = 1,
E[X]E[Y] = (2p - 1)^2.
```

The same normalized source shape and raw moment allow:

```text
p = 1/2  -> E[X]E[Y] = 0    -> connected = 1
p = 2/3  -> E[X]E[Y] = 1/9  -> connected = 8/9
p = 3/4  -> E[X]E[Y] = 1/4  -> connected = 3/4
p = 1    -> E[X]E[Y] = 1    -> connected = 0
```

Thus the desired value is one member of a scalar source family, not a
consequence of normalization. Choosing `p=2/3` is exactly a one-point selector
theorem. This block uses the signed two-state family only as a counterfamily;
it does not reopen the already-pruned binary same-record/log-odds route as a
positive derivation.

There is also an invariant obstruction. On an unlabeled normalized scalar
partition, permutation-invariant linear readouts are constant on the simplex.
Their first derivative on the normalized tangent `sum_i delta p_i = 0`
vanishes. A nonconstant one-point marginal therefore requires a distinguished
subset, label, source covector, or physical readout theorem. Scalar
normalization by itself supplies none of those.

## What This Prunes

This prunes only the shortcut:

```text
normalization of a scalar source partition
-> forced same-source one-point product 1/9.
```

It does not rule out a positive Route-2 theorem that constructs the physical
record variables and proves their one-point product. It also does not repeat
the generic Pcal product-registry no-go. That older packet shows the abstract
cumulant theorem does not instantiate Route-2 record variables. This packet
shows that adding only scalar normalization still does not select the needed
one-point product.

## Missing Primitive

The exact missing primitive is now:

```text
Route-2 scalar source-marginal selector theorem:

construct the physical same-source Route-2 variables X and Y and reference
source measure; prove E[XY]=1 for that same source; and prove, from Route-2
source/readout structure rather than endpoint values, fitted weights, or
finite-box comparators, that E[X]E[Y]=1/9.
```

Equivalently, supply a typed disconnected-subtraction theorem whose source
surface contains the nonconstant scalar marginal selector and the raw moment
registry. Without that primitive, scalar normalization remains support context,
not a bridge theorem forcing `kappa=0`.

No endpoint value is used.

Expected runner result:

```text
TOTAL: PASS=73, FAIL=0
```
