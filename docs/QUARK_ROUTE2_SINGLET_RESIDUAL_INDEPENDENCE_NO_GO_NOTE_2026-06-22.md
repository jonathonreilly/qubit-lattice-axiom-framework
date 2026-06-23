# Quark Route-2 Singlet Residual Independence No-Go

**Date:** 2026-06-22
**Type:** no-go / pure-disconnected identity-line obstruction packet
**Actual current-surface status:** no-go for SU(3) invariance plus connected-cumulant algebra forcing the identity-line residual to vanish
**Trace class:** negative_route_pruning
**Primary runner:** [`scripts/frontier_quark_route2_singlet_residual_independence_no_go_2026_06_22.py`](../scripts/frontier_quark_route2_singlet_residual_independence_no_go_2026_06_22.py)
**Cached output:** [`outputs/frontier_quark_route2_singlet_residual_independence_no_go_2026_06_22.txt`](../outputs/frontier_quark_route2_singlet_residual_independence_no_go_2026_06_22.txt)

This is not an audit verdict. It does not run audit workers and does not apply
audit outcomes.

## Question

Blocks116-117 isolate the orientation-free adjoint contraction and its
adjoint/singlet coefficient scale. Another Block115 premise remains:

```text
the scalar identity line is pure disconnected for the same source.
```

Does SU(3) invariance plus connected-cumulant algebra force that premise?

## Result

No. SU(3) invariance splits the source into:

```text
1 + adjoint.
```

It forbids an invariant singlet-adjoint cross term, but it allows an
independent connected singlet residual:

```text
eta = connected residual on the identity line.
```

The connected-cumulant selector family is:

```text
R_cumulant(eta) = 8/9 + eta/9.
```

Therefore:

| Identity-line typing | `eta` | `kappa` |
|---|---:|---:|
| Pure disconnected product | `0` | `0` |
| Half connected residual | `1/2` | `1/2` |
| Pure connected residual | `1` | `1` |

Connected-cumulant algebra subtracts factorizable products exactly. It does not
decide whether the identity-line second derivative is factorizable for the
physical Route-2 source. That is a same-source factorization theorem.

## Missing Primitive

The precise missing primitive is:

```text
Route-2 identity-line pure-disconnected factorization theorem:

for the physical same-source covariant adjoint multi-record source/readout,
prove that the scalar identity-line contribution satisfies
D_0 D_0 Z = (D_0 Z)^2 at the readout point, so D_0 D_0 log Z = 0.
```

This is distinct from:

- the orientation-free adjoint contraction theorem;
- the adjoint/singlet coefficient normalization theorem;
- E/T symmetry of the output line.

No endpoint value is used.

Expected runner result:

```text
TOTAL: PASS=51, FAIL=0
```
