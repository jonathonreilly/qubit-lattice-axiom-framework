# Quark Route-2 Formal Source-Coordinate Registry Vacuity No-Go

**Date:** 2026-06-22
**Type:** no-go / formal source-coordinate registry obstruction packet
**Actual current-surface status:** no-go for a bare formal source-coordinate registry forcing `kappa=0`
**Trace class:** negative_route_pruning
**Primary runner:** [`scripts/frontier_quark_route2_formal_source_coordinate_registry_vacuity_no_go_2026_06_22.py`](../scripts/frontier_quark_route2_formal_source_coordinate_registry_vacuity_no_go_2026_06_22.py)
**Cached output:** [`outputs/frontier_quark_route2_formal_source_coordinate_registry_vacuity_no_go_2026_06_22.txt`](../outputs/frontier_quark_route2_formal_source_coordinate_registry_vacuity_no_go_2026_06_22.txt)

This is not an audit verdict. It does not run audit workers and does not apply
audit outcomes.

## Question

Block98 named the missing source-Hessian integrability registry:

```text
construct source coordinates, assign physical slots to symmetric source-index
pairs, prove mixed-partial reciprocity, and identify the resulting two-jet
with D_A D_B log Z for the same Route-2 source/readout.
```

Can the next shortcut work if it only supplies formal source coordinates and a
symmetric quadratic potential `W`?

## Result

No. A bare formal source-coordinate registry is vacuous for the Route-2
selector. With three formal source coordinates there are six unordered
source-index pairs, so the four finite Route-2 endpoint slots can always be
placed into a symmetric Hessian matrix. A quadratic formal potential

```text
W[J] = (1/2) sum_AB H_AB J_A J_B
```

then satisfies

```text
D_A D_B W = H_AB = H_BA.
```

This proves only formal embeddability. It does not prove that the source
action is the physical Route-2 source/readout, does not provide the raw
`Z[J]` second moment or one-point product, and does not type the singlet line
as pure disconnected.

The obstruction is sharp because the same formal registry skeleton accepts
all values

```text
R_conn(kappa) = 8/9 + kappa/9.
```

For example, the `kappa=0`, `kappa=1/2`, and `kappa=1` Hessians can all be
made symmetric formal Hessians. Mixed-partial reciprocity therefore does not
force `kappa=0`.

## What Still Works

The positive conditional theorem from the prior source-Hessian packets remains
valid:

```text
same-source physical E/T Hessian
+ symmetric line pure disconnected
+ antisymmetric line connected SU(3) adjoint
=> D^2 log Z removes the disconnected singlet and forces kappa=0.
```

Block99 only prunes the weaker shortcut:

```text
finite slots + formal symmetric source-coordinate registry => kappa=0.
```

## Missing Primitive

The exact missing primitive is now stronger than formal integrability:

```text
Route-2 typed source-action/product registry theorem:

construct the physical Route-2 source action and source coordinates; prove the
physical E/T readout is the connected Hessian D_A D_B log Z for that same
source; provide the raw D_A D_B Z and one-point D_A Z D_B Z product registry;
type the E/T-symmetric singlet line as pure disconnected; and type the
E/T-antisymmetric line as the connected SU(3) adjoint bilinear.
```

No endpoint value is used.

Expected runner result:

```text
TOTAL: PASS=88, FAIL=0
```
