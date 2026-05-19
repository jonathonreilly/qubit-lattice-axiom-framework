# PMNS Graph-First Cycle Frame Support

**Claim type:** bounded_theorem
**Status:** exact support theorem, not a value-selection theorem  
**Script:** [`frontier_pmns_graph_first_cycle_frame_support.py`](../scripts/frontier_pmns_graph_first_cycle_frame_support.py)

## Question

Does graph-first axis selection plus graph-first SU(3) integration canonically
order or frame-fix the oriented-cycle basis strongly enough to support a future
value law?

## Answer

Yes, as a support theorem.

The graph-first selector has exactly three axis minima, each with residual
`Z_2` stabilizer. Once one axis is selected, the graph-first SU(3) integration
on that axis canonically fixes the selected-axis fiber/base split and the
residual swap on the complementary base. Together these data determine the
canonical oriented-cycle frame

`E12, E23, E31`

via forward transport from the diagonal projectors:

`E11 C = E12`, `E22 C = E23`, `E33 C = E31`.

So the oriented-cycle basis is not floating freely. It is frame-fixed by the
graph-first route strongly enough to state future cycle-value laws in an
invariant way.

## Helper-runner code excerpts (load-bearing for restricted packet, inlined 2026-05-18)

The primary runner
[`scripts/frontier_pmns_graph_first_cycle_frame_support.py`](../scripts/frontier_pmns_graph_first_cycle_frame_support.py)
imports four load-bearing functions from two helper modules:

```python
from frontier_graph_first_selector_derivation import build_axis_shifts, selector_from_phi
from frontier_graph_first_su3_integration import make_change_of_basis, residual_swap_op
```

The selector-derivation helper supplies the canonical cube-shift triplet and
the normalized quartic selector (used in PART 1 to check Hermiticity of the
shifts and to enumerate the three axis minima). The SU(3)-integration helper
supplies the selected-axis fiber/base change-of-basis and the residual swap on
the complementary base (used in PART 1 to check unitarity of the graph basis,
and in PART 3 to certify the residual-swap action on the cycle frame). The
load-bearing source bodies are inlined below for restricted-packet visibility.

### From scripts/frontier_graph_first_selector_derivation.py

```python
# scripts/frontier_graph_first_selector_derivation.py
# Canonical cube-shift triplet on the 3-cube taste graph.

I2 = np.eye(2, dtype=complex)
SX = np.array([[0, 1], [1, 0]], dtype=complex)
I8 = np.eye(8, dtype=complex)


def kron3(a: np.ndarray, b: np.ndarray, c: np.ndarray) -> np.ndarray:
    return np.kron(a, np.kron(b, c))


def build_axis_shifts() -> list[np.ndarray]:
    return [
        kron3(SX, I2, I2),
        kron3(I2, SX, I2),
        kron3(I2, I2, SX),
    ]


def selector_from_phi(phi: np.ndarray) -> tuple[float, np.ndarray]:
    r2 = float(np.dot(phi, phi))
    if r2 <= 0:
        raise ValueError("phi must be nonzero")
    p = (phi * phi) / r2
    f = float(sum(p[i] * p[j] for i in range(3) for j in range(i + 1, 3)))
    return f, p
```

`build_axis_shifts` returns the three canonical one-step axis-shift operators
`S_i = I (x) ... (x) sigma_x (x) ... (x) I` on the 3-cube taste graph (where
`sigma_x` lands on the i-th tensor factor). `selector_from_phi` returns the
normalized pairwise-overlap selector `F(p) = sum_{i<j} p_i p_j` with
`p_i = phi_i^2 / sum_j phi_j^2`, which has exactly three axis minima `e_1,
e_2, e_3` with residual `Z_2` stabilizer.

### From scripts/frontier_graph_first_su3_integration.py

```python
# scripts/frontier_graph_first_su3_integration.py
# Graph-first SU(3) integration: selected-axis fiber/base basis + residual swap.

import itertools
import numpy as np


def cube_basis() -> list[tuple[int, int, int]]:
    return list(itertools.product((0, 1), repeat=3))


def cube_index() -> dict[tuple[int, int, int], int]:
    b = cube_basis()
    return {x: i for i, x in enumerate(b)}


def residual_swap_op(axis: int) -> np.ndarray:
    others = [i for i in range(3) if i != axis]
    a, b = others
    idx = cube_index()
    op = np.zeros((8, 8), dtype=complex)
    for x, i in idx.items():
        y = list(x)
        y[a], y[b] = y[b], y[a]
        op[idx[tuple(y)], i] = 1.0
    return op


def make_change_of_basis(axis: int) -> np.ndarray:
    """Graph-native basis: first factor is selected-axis fiber, second is base.

    Basis vector order:
      |fiber_bit> (x) |base_bits>
    where base_bits are the remaining two coordinates in their natural order.
    """
    idx = cube_index()
    basis_cols = []
    others = [i for i in range(3) if i != axis]
    for fiber_bit in (0, 1):
        for b1 in (0, 1):
            for b2 in (0, 1):
                x = [0, 0, 0]
                x[axis] = fiber_bit
                x[others[0]] = b1
                x[others[1]] = b2
                col = np.zeros(8, dtype=complex)
                col[idx[tuple(x)]] = 1.0
                basis_cols.append(col)
    U = np.column_stack(basis_cols)
    return U
```

`make_change_of_basis(axis)` builds the explicit 8x8 unitary that reorders the
cube basis as `|fiber_bit> (x) |base_bits>`, exhibiting the selected-axis
fiber/base split needed to canonically fix the cycle transport order.
`residual_swap_op(axis)` is the permutation operator that swaps the two
complementary base coordinates, used both as the residual symmetry generator
and as the action that exchanges `E12 <-> E31` while fixing `E23` on the
canonical oriented-cycle frame.

The four functions above are exactly the symbols pulled in by the primary
runner's `from ... import` statements. Inlining them here makes the support
theorem self-contained at the source-note tier without enlarging the upstream
authority surface.

## Theorem

**Theorem (graph-first cycle-frame support).**

On the graph-first PMNS `hw=1` route:

1. the normalized cube-shift selector has exactly three axis minima,
2. each selected axis has exact residual `Z_2` stabilizer,
3. graph-first SU(3) integration on a selected axis canonically fixes the
   fiber/base split and the residual swap on the complementary base,
4. the diagonal projectors transported by the canonical forward cycle give the
   unique ordered oriented-cycle frame `E12, E23, E31`,
5. this frame is strong enough to support a future value law, but it does not
   itself select the cycle coefficients.

## What This Gives

This is the exact structural support needed before any future coefficient or
value law on the cycle channel:

- the carrier is fixed,
- the basis ordering is fixed,
- the residual symmetry is explicit,
- the remaining freedom is only in the coefficients.

So the route is a real support theorem for a future value law.

## What It Does Not Yet Give

This route does **not** determine the values `(u, v, w)` on the reduced cycle
channel, and it does **not** provide a positive selector for those values.

The remaining open problem is therefore a value-selection law, not a frame
selection law.

## Upstream authorities

- [GRAPH_FIRST_SELECTOR_DERIVATION_NOTE.md](GRAPH_FIRST_SELECTOR_DERIVATION_NOTE.md) — the graph-first axis-selector derivation supplying the "exactly three axis minima with residual Z_2 stabilizer" structure.
- [GRAPH_FIRST_SU3_INTEGRATION_NOTE.md](GRAPH_FIRST_SU3_INTEGRATION_NOTE.md) — the graph-first SU(3) integration supplying the axis-side fiber/base split and the diagonal-projector forward-transport that frame-fixes the oriented cycle basis.
