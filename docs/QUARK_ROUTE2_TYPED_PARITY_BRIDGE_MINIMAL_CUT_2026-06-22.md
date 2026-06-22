# Quark Route-2 Typed Parity Bridge Minimal Cut

**Date:** 2026-06-22
**Type:** support / minimal-cut synthesis packet
**Actual current-surface status:** exact-support for the typed parity bridge dependency cut; not current-surface closure
**Trace class:** upstream_support
**Primary runner:** [`scripts/frontier_quark_route2_typed_parity_bridge_minimal_cut_2026_06_22.py`](../scripts/frontier_quark_route2_typed_parity_bridge_minimal_cut_2026_06_22.py)
**Cached output:** [`outputs/frontier_quark_route2_typed_parity_bridge_minimal_cut_2026_06_22.txt`](../outputs/frontier_quark_route2_typed_parity_bridge_minimal_cut_2026_06_22.txt)

This is not an audit verdict. It does not run audit workers and does not apply
audit outcomes.

## Result

Blocks 92-95 isolate a minimal typed-parity bridge cut for the
connected-cumulant Route-2 route.

To force `kappa=0` without endpoint input, the bridge needs these three
same-source premises:

1. **Physical source-Hessian premise:** the physical Route-2 E/T readout is a
   same-source E/T source Hessian.
2. **Symmetric purity premise:** the E/T-symmetric singlet line is pure
   factorizable disconnected for that same source/readout.
3. **Antisymmetric adjoint premise:** the E/T-anti-invariant connected line is
   exactly the SU(3) adjoint color bilinear with no non-adjoint connected
   residue.

With these three premises:

```text
D^2 log Z subtracts the symmetric disconnected line
and leaves only the antisymmetric adjoint connected line,
so kappa=0.
```

To additionally fix the scalar E/T coefficient bridge, the route also needs:

4. **Anti-invariant normalization premise:** derive the E/T anti-invariant
   normalization functional from framework primitives.

Block92 shows this normalizer is needed for scale; Block94 shows E/T symmetry
does not prove disconnected purity; Block95 shows E/T anti-invariance does not
prove adjoint color typing; Block93 shows the combined sufficient theorem.

## Exact Missing Primitive

For `kappa=0`, the exact missing primitive is:

```text
Route-2 same-source typed parity source-Hessian theorem:

construct the physical E/T source Hessian, prove the E/T-symmetric line is
pure factorizable disconnected, and prove the E/T-anti-invariant connected
line is the SU(3) adjoint color bilinear, all for the same source/readout and
without endpoint input.
```

For the scalar E/T coefficient bridge, extend it with:

```text
derive the E/T anti-invariant normalization functional from framework
primitives rather than endpoint input.
```

Expected runner result:

```text
TOTAL: PASS=60, FAIL=0
```
