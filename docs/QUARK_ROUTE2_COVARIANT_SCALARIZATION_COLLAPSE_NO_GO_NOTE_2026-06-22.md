# Quark Route-2 Covariant Scalarization Collapse No-Go

**Date:** 2026-06-22
**Type:** no-go / covariant-family scalarization obstruction packet
**Actual current-surface status:** no-go for invariant scalarization of a covariant color family as the Route-2 bridge
**Trace class:** negative_route_pruning
**Primary runner:** [`scripts/frontier_quark_route2_covariant_scalarization_collapse_no_go_2026_06_22.py`](../scripts/frontier_quark_route2_covariant_scalarization_collapse_no_go_2026_06_22.py)
**Cached output:** [`outputs/frontier_quark_route2_covariant_scalarization_collapse_no_go_2026_06_22.txt`](../outputs/frontier_quark_route2_covariant_scalarization_collapse_no_go_2026_06_22.txt)

This is not an audit verdict. It does not run audit workers and does not apply
audit outcomes.

## Question

Block87 showed that a pair of color-invariant scalar outputs cannot have a
first-order `sl_3` response. The surviving constructive route must therefore
carry a covariant color family before any scalar output is formed.

This block tests the nearest shortcut:

```text
covariant sl_3 color-readout family
  -> invariant scalarization, such as Tr(X^2) or Tr(X^3)
  -> Route-2 scalar E/T bridge.
```

Does orientation-free invariant scalarization of a covariant family already
provide the typed Route-2 connected bridge?

## Result

No. It supplies useful color support, but it collapses the readout before the
Route-2 E/T typing is established.

Let `X in sl_3` be the connected color tangent. The orientation-free invariant
polynomials on an adjoint `sl_3` element begin with:

```text
Q(X) = Tr(X^2),
C(X) = Tr(X^3).
```

They are scalar orbit data. They do not retain the adjoint-valued readout
family as a typed source/readout map into Route-2 `E/T` slots:

- `Q` is even: `Q(X) = Q(-X)`, so it loses orientation of the covariant
  family.
- `C` is nonlinear orbit data and still does not type a Route-2 `E/T` readout.
- every invariant scalar has zero first derivative at the trace-normalized
  identity source on traceless perturbations, as Block87 checked.
- arbitrary scalarizations `a Q + b C` are available unless a physical
  source/readout theorem fixes the coefficients and channel assignment.

Disconnected subtraction can remove the scalar identity line. It does not by
itself identify the post-subtraction covariant family with the physical
Route-2 `E/T` readout.

## Missing Primitive

The precise missing primitive is now:

```text
Route-2 covariant-family connected-Hessian E/T readout theorem:

construct a color/tensor-resolved source J_A and a same-source readout tensor
for Route-2 such that the physical E/T readout is D_A D_B log Z on that source;
prove the scalar identity line is a pure disconnected product; and only then
derive the scalar E/T bridge from the connected adjoint block, without
importing an endpoint value or color-orientation selector.
```

This is stronger than "take the Casimir/norm of the color family." The theorem
must preserve the covariant source/readout typing through the disconnected
subtraction step and only then form the physical scalar Route-2 output.

No endpoint value is used.

Expected runner result:

```text
TOTAL: PASS=50, FAIL=0
```
