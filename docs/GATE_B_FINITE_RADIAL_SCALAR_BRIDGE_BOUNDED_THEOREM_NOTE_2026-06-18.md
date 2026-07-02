# Gate B Finite Radial Scalar Bridge Bounded Theorem Note

**Date:** 2026-06-18
**Claim type:** bounded_theorem
**Status:** bounded-support source bridge for `GB-S1b-a`; not a Gate B dynamics
closure and not an audit-ratified effective status.
**Status authority:** independent audit lane only. This note does not edit or
predict an audit verdict.
**Primary runner:** [`scripts/gate_b_finite_radial_scalar_bridge_2026_06_18.py`](../scripts/gate_b_finite_radial_scalar_bridge_2026_06_18.py)
**Cached output:** [`logs/runner-cache/gate_b_finite_radial_scalar_bridge_2026_06_18.txt`](../logs/runner-cache/gate_b_finite_radial_scalar_bridge_2026_06_18.txt)

## Purpose

The audited Gate B parent row currently treats `GB-S1b`, the runner scalar and
normalization, as supplied row-local data. This note splits that item.

| ID | Piece | Boundary |
|---|---|---|
| `GB-S1b-a` | finite runner scalar `phi_GB(x)=strength/(r(x,mass)+0.1)` | proved here as exact finite radial algebra matching the current runner helper |
| `GB-S1b-b` | physical Poisson/source equation, finite-core regulator selection, boundary condition, and absolute normalization | still open Gate-B runner/physics data |

This is a source-side bridge, not a physical-gravity theorem. It makes the
runner scalar transparent and checkable, while preserving the real open
physics: deriving why this scalar, regulator, and normalization are selected
from framework primitives.

## The finite scalar statement

On the finite coordinate slab used by `scripts/gate_b_connectivity_tolerance.py`,
let the supplied mass node have coordinate `m`. The runner helper defines

```text
r(x,m) = sqrt((x_1-m_1)^2 + (x_2-m_2)^2 + (x_3-m_3)^2)
phi_GB(x) = strength / (r(x,m) + epsilon)
epsilon = 0.1.
```

The `epsilon` term is a finite-core regulator. It makes the scalar finite at
the mass node, where `r=0` and `phi_GB(m)=strength/0.1`.

## Bounded theorem

The verifier checks these facts on the current Gate B runner surface.

1. **Runner equality.** The current `_field_for_mass` helper exactly matches
   the formula `strength/(r+0.1)` for every site in the tested slab.
2. **Finiteness and positivity.** For positive strength, every scalar value is
   positive and finite, including the mass node.
3. **Radial monotonicity.** On the supplied coordinate embedding, larger
   Euclidean distance from the mass node gives smaller or equal scalar value.
4. **Linear strength normalization.** Scaling `strength` scales the entire
   scalar field linearly.
5. **Action normalization degeneracy.** In the action form `S=L(1-lambda phi)`,
   only the product `lambda*strength` enters the scalar contribution. A
   separate absolute normalization is therefore not derived by this finite
   algebra.

These facts retire only the avoidable opacity of the finite scalar helper.
They do not select the physical Poisson equation, boundary condition,
regulator, source strength, or unit normalization.

## Claim boundary

This note supports only:

```text
GB-S1b-a: the finite Gate B runner scalar is exact positive radial
regularized algebra on the supplied coordinate slab and is linear in source
strength.
```

It does not claim:

- `GB-S1b` is fully derived;
- the scalar is the retained Poisson Green function;
- the `0.1` regulator is derived from framework primitives;
- the source strength or absolute unit normalization is derived;
- `GB-S2` propagation/readout semantics are derived;
- `GB-S3` generated connectivity is derived;
- the parent Gate B dynamics row is closed or promoted;
- a new axiom, Tier-A admission, or audit verdict.

Therefore the parent Gate B dynamics row remains an open gate. A later re-audit
can treat the finite scalar-helper algebra as source-supplied by this theorem
packet while continuing to require the physical source and normalization bridge.

## Verification

Run:

```bash
python3 scripts/gate_b_finite_radial_scalar_bridge_2026_06_18.py
```

Expected result:

```text
TOTAL: PASS=12 FAIL=0
```
