# Dimension Selection Upper-Bound — Native Stable-Orbit Support Wrapper

**Date:** 2026-05-17
**Claim type:** bounded_theorem
**Status:** bounded support wrapper for the native stable-circular-orbit
upper-bound edge and the bounded Coulomb scaling companion edge that
complement the `d >= 3` lower-bound result in
[DIMENSION_SELECTION_NOTE.md](DIMENSION_SELECTION_NOTE.md). The legacy
filename is retained for citation stability.
**Status authority:** independent audit lane only.

## Purpose

This wrapper note records the source-side upper-bound support edges consumed by
the dimension-selection lane. The decisive edge for the current finite
lower-bound packet is not the full Bertrand closed-orbit theorem: it is the
native stable-circular-orbit calculation in
[`BERTRAND_STABLE_ORBIT_UPPER_BOUND_SUPPORT_NOTE_2026-05-20.md`](BERTRAND_STABLE_ORBIT_UPPER_BOUND_SUPPORT_NOTE_2026-05-20.md).
That note derives the continuum Green-kernel shape
`V(r) = -k/r^(d-2)` for integer `d >= 3` and the effective-potential sign
`k(d-2)(4-d)/r_c^d`, so stable circular orbits occur only at integer `d = 3`
among the current checked set. The full Bertrand theorem remains useful
classical-mechanics context, but it is not load-bearing for the finite-set
upper-bound composition recorded here.

The companion atomic route remains bounded support: the Coulomb scaling note
excludes `d >= 5` for the stated Green-kernel quadratic form, leaves `d = 4`
marginal, and does not by itself select `d = 3` from the current lower-bound
packet.

## 2026-06-09 native stable-orbit wrapper refresh

The source-side repair note
[`DIMENSION_UPPER_BOUND_DEPENDENCY_EDGE_REPAIR_NOTE_2026-06-08.md`](DIMENSION_UPPER_BOUND_DEPENDENCY_EDGE_REPAIR_NOTE_2026-06-08.md)
now records this wrapper as an auditable dependency edge without relying on the
full closed-orbit Bertrand theorem. It wires this wrapper to the current
one-hop bounded support packets and composition gate:

| Role | Source packet | Runner/cache |
| --- | --- | --- |
| Native stable-circular-orbit upper edge | [`BERTRAND_STABLE_ORBIT_UPPER_BOUND_SUPPORT_NOTE_2026-05-20.md`](BERTRAND_STABLE_ORBIT_UPPER_BOUND_SUPPORT_NOTE_2026-05-20.md) | [`scripts/bertrand_stable_orbit_green_kernel_bridge.py`](../scripts/bertrand_stable_orbit_green_kernel_bridge.py), [`logs/runner-cache/bertrand_stable_orbit_green_kernel_bridge.txt`](../logs/runner-cache/bertrand_stable_orbit_green_kernel_bridge.txt) |
| Bounded Coulomb scaling companion edge | [`COULOMB_STABILITY_UPPER_BOUND_SUPPORT_NOTE_2026-05-20.md`](COULOMB_STABILITY_UPPER_BOUND_SUPPORT_NOTE_2026-05-20.md) | [`scripts/frontier_coulomb_stability_scaling_repair.py`](../scripts/frontier_coulomb_stability_scaling_repair.py), [`logs/runner-cache/frontier_coulomb_stability_scaling_repair.txt`](../logs/runner-cache/frontier_coulomb_stability_scaling_repair.txt) |
| Current finite-set composition gate | [`D3_UPPER_BOUND_IMPORT_SCOPE_GATE_NOTE_2026-06-06.md`](D3_UPPER_BOUND_IMPORT_SCOPE_GATE_NOTE_2026-06-06.md) | [`scripts/frontier_d3_upper_bound_import_scope_gate_2026_06_06.py`](../scripts/frontier_d3_upper_bound_import_scope_gate_2026_06_06.py), [`logs/runner-cache/frontier_d3_upper_bound_import_scope_gate_2026_06_06.txt`](../logs/runner-cache/frontier_d3_upper_bound_import_scope_gate_2026_06_06.txt) |

The repair note's paired runner is
[`scripts/dimension_upper_bound_dependency_edge_repair_2026_06_08.py`](../scripts/dimension_upper_bound_dependency_edge_repair_2026_06_08.py),
with cache
[`logs/runner-cache/dimension_upper_bound_dependency_edge_repair_2026_06_08.txt`](../logs/runner-cache/dimension_upper_bound_dependency_edge_repair_2026_06_08.txt).

This dependency repair does not claim a complete framework-internal derivation
of Bertrand's closed-orbit theorem, atomic stability, a physical
electromagnetic sector, or a full dimension-selection theorem. It only makes
the bounded support edges and finite-set composition visible for independent
audit.

## Support Edges Covered

### 1. Native stable-circular-orbit edge

Load-bearing statement: for integer `d >= 3`, the native support note derives
the radial Green-kernel potential shape

```text
V(r) = -k / r^(d-2),     k > 0,
```

and then computes the circular-orbit stability sign

```text
d^2 V_eff / dr^2 |_(r_c) = k(d-2)(4-d) / r_c^d.
```

For integer `d >= 3`, this sign is positive only for `d = 3`, marginal for
`d = 4`, and negative for `d >= 5`. Therefore the stable-circular-orbit
upper edge is `d <= 3` on the current lower-bound candidate set
`{3,4,5}`.

Parallel reference context: Bertrand's theorem says that the inverse-square
and harmonic-oscillator laws are the central-force laws for which all bounded
orbits are closed. That full closed-orbit theorem is not consumed by this
finite-set upper-bound composition and remains a standard classical-mechanics
reference rather than a load-bearing import.

### 2. Bounded Coulomb scaling companion edge

Load-bearing statement: the companion support note proves the Green-kernel
scaling lemma for the stated quadratic form

```text
Q_d[psi_lambda] = lambda^2 T - lambda^(d-2) U.
```

This excludes `d >= 5` by ultraviolet collapse, identifies `d = 4` as
marginal, and leaves `d = 3` not collapsed by this scaling test. Composed with
the current finite lower-bound packet, it gives `{3,4}` and is therefore
compatible companion support rather than the decisive unique-dimension
selector.

Parallel reference context: Tangherlini/Ehrenfest-style dimensional atomic
stability and the stronger hydrogenic `d = 3` spectral statement remain
outside this wrapper unless separately derived or explicitly scoped.

## Upper-Bound Conclusion

Combined with the runner-verified finite lower-bound packet from
self-consistent propagator + gravitational field in
[DIMENSION_SELECTION_NOTE.md](DIMENSION_SELECTION_NOTE.md), the native
stable-circular-orbit edge gives

```text
{3,4,5} intersect {d : d <= 3} = {3}.
```

The bounded Coulomb scaling companion gives

```text
{3,4,5} intersect {d : d <= 4} = {3,4}.
```

Thus the current unique finite-set composition is supplied by the native
stable-circular-orbit edge, while the Coulomb scaling route remains compatible
bounded support.

## What This Note Does NOT Claim

- This is NOT a re-derivation of the full Bertrand closed-orbit theorem.
- This is NOT a re-derivation of the full atomic-stability upper bound,
  a physical electromagnetic sector, or a hydrogenic spectrum theorem.
- This is NOT a framework-level derivation of `d = 3` from `Cl(3)` on
  `Z^3` alone — `Cl(3) ⊗ Z^3` has `d = 3` built into the substrate, so
  the framework does not need a separate dimension-selection theorem.
  The DIMENSION_SELECTION_NOTE lane is a complementary self-consistency
  check, not a framework derivation.
- This is NOT a repo-wide promotion, audit verdict, or ledger edit.

## Downstream usage

This wrapper is consumed by:

- [DIMENSION_SELECTION_NOTE.md](DIMENSION_SELECTION_NOTE.md) — supplies the upper-bound native stable-circular-orbit edge and bounded Coulomb companion edge complementing the lower-bound (self-consistent gravity / propagator) runner result.

## Boundary

This wrapper note is a bounded source-support wrapper. It does not claim:

- a framework derivation of the full Bertrand closed-orbit theorem;
- a framework derivation of full atomic stability or the hydrogenic spectrum;
- closure of any downstream dimension-selection theorem.

Its function is to provide a citeable one-hop authority for the native
stable-circular-orbit upper edge and the bounded Coulomb scaling companion edge
so downstream notes register the exact support they consume instead of carrying
an unnecessary textbook-import dependency.
