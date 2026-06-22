# Quark Route-2 Binary Product Normal-Form Support

**Date:** 2026-06-22
**Type:** conditional-support / product-registry normal-form packet
**Actual current-surface status:** conditional-support for a binary normalized product normal form; not current-surface closure
**Trace class:** upstream_support
**Primary runner:** [`scripts/frontier_quark_route2_binary_product_normal_form_support_2026_06_22.py`](../scripts/frontier_quark_route2_binary_product_normal_form_support_2026_06_22.py)
**Cached output:** [`outputs/frontier_quark_route2_binary_product_normal_form_support_2026_06_22.txt`](../outputs/frontier_quark_route2_binary_product_normal_form_support_2026_06_22.txt)

This is not an audit verdict. It does not run audit workers and does not apply
audit outcomes.

## Question

Block101 showed that exact `P_R` slots do not determine the one-point product.
Can a minimal finite-record normal form make the remaining product theorem
sharper?

## Conditional Normal Form

Assume the Route-2 product registry is realized by a normalized binary record
model with one signed record variable:

```text
X = Y in {-1,+1}
E[XY] = 1
E[X] = E[Y] = m.
```

Then the Pcal connected two-point response is:

```text
D^2 log Z = E[XY] - E[X]E[Y] = 1 - m^2.
```

The connected-color target value `8/9` is therefore equivalent, inside this
normal form, to:

```text
1 - m^2 = 8/9
m^2 = 1/9
m = +/- 1/3.
```

Equivalently, the binary record probabilities have a `2:1` bias:

```text
P(+1):P(-1) = 2:1
```

or the sign-reversed `1:2` bias.

## What This Moves

This packet does not derive the Route-2 source/readout theorem. It converts
the product-registry blocker into a smaller exact primitive under a specific
finite-record normal form:

```text
Route-2 binary one-point bias theorem:

prove the physical Route-2 source record is a normalized binary same-record
source with E[XY]=1 and E[X]=+/-1/3.
```

If that theorem is supplied, the existing Pcal/Mobius connected subtraction
gives the `kappa=0` selector without endpoint input. If it is not supplied,
the normal form remains conditional support only.

## Non-Claims

This block does not claim:

- the Route-2 physical readout is already a binary record source;
- the one-point mean `+/-1/3` is derived on the current surface;
- the antisymmetric line is already typed as the connected SU(3) adjoint;
- any endpoint ratio is derived.

No endpoint value is used.

Expected runner result:

```text
TOTAL: PASS=72, FAIL=0
```
