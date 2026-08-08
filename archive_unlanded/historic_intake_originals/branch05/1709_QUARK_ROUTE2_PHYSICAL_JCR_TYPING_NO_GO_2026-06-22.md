# Quark Route-2 Physical J_CR Typing No-Go

**Date:** 2026-06-22
**Type:** no-go / formal binary source jet to physical J_CR typing obstruction
**Actual current-surface status:** no-go for the formal binary source-jet model alone typing the physical Route-2 J_CR source
**Trace class:** negative_route_pruning
**Primary runner:** [`scripts/frontier_quark_route2_physical_jcr_typing_no_go_2026_06_22.py`](../scripts/frontier_quark_route2_physical_jcr_typing_no_go_2026_06_22.py)
**Cached output:** [`outputs/frontier_quark_route2_physical_jcr_typing_no_go_2026_06_22.txt`](../outputs/frontier_quark_route2_physical_jcr_typing_no_go_2026_06_22.txt)

This is not an audit verdict. It does not run audit workers and does not apply
audit outcomes.

## Question

Block143 supplied an exact formal source-jet support theorem:

```text
Z_CR[J] = (2/3) exp(J) + (1/3) exp(-J)
```

so that `D^2 log Z_CR |0 = 8/9` and `kappa=0`. Does that formal source model
itself prove the physical Route-2 `J_CR` source typing?

## Result

No. The formal binary exponential family has a one-parameter version:

```text
Z_p[J] = p exp(J) + (1-p) exp(-J).
```

At zero source:

```text
D Z_p |0 = 2p - 1,
D^2 Z_p |0 = 1,
D^2 log Z_p |0 = 4p(1-p).
```

Different exact choices of `p` give different connected selectors:

| `p` | `D Z_p |0` | `D^2 log Z_p |0` | `kappa` |
|---:|---:|---:|---:|
| `1/2` | `0` | `1` | `1` |
| `2/3` | `1/3` | `8/9` | `0` |
| `1/3` | `-1/3` | `8/9` | `0` |
| `3/4` | `1/2` | `3/4` | `-5/4` |
| `5/6` | `2/3` | `5/9` | `-3` |

The support theorem selects `kappa=0` only after the physical source typing
has selected the reference probability and sign/orientation. The current
finite `P_R` row surface, generic Fisher/Riesz support, and the formal binary
family do not supply that physical `J_CR` source coordinate.

## Missing Primitive

The exact missing primitive is:

```text
Route-2 physical J_CR source typing theorem:

construct the physical source sample space Omega_CR, reference measure P0,
source coordinate J_CR, and binary readout variable X_CR for the Route-2
center-ratio line; prove the physical O_CR/readout is the same-source
connected Hessian D^2 log Z_p at p=2/3 with the selected orientation; and
prove this source is the same source consumed by the Riesz/unit-isometry and
orientation steps.
```

No endpoint value is used as an input. This packet only prunes the shortcut

```text
formal binary exponential family => physical J_CR typing.
```

Expected runner result:

```text
TOTAL: PASS=95, FAIL=0
```
