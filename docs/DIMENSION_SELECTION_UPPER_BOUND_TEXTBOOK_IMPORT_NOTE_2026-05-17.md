# Dimension Selection Upper-Bound - Native Stable-Orbit Edge with Textbook Cross-References

**Date:** 2026-05-17
**Type:** bounded_theorem
**Status:** bounded source wrapper for the native stable-orbit upper edge
and bounded Coulomb companion that complement the
`d >= 3` lower-bound result in
[DIMENSION_SELECTION_NOTE.md](DIMENSION_SELECTION_NOTE.md).
**Status authority:** independent audit lane only.

## Purpose

This wrapper note registers the current one-hop source dependencies for the
upper-bound side of the
[DIMENSION_SELECTION_NOTE.md](DIMENSION_SELECTION_NOTE.md) lane. For the
current finite lower packet `L_runner = {3,4,5}`, the decisive `d <= 3`
upper edge is no longer a load-bearing textbook import: it is supplied by the
native Green-kernel/effective-potential calculation in
[`BERTRAND_STABLE_ORBIT_UPPER_BOUND_SUPPORT_NOTE_2026-05-20.md`](BERTRAND_STABLE_ORBIT_UPPER_BOUND_SUPPORT_NOTE_2026-05-20.md).
Classical Bertrand references are cited in parallel as context for the
stronger all-bounded-orbits-are-closed theorem, which this packet does not
consume.

## 2026-06-08 dependency-edge source repair

The source-side repair note
[`DIMENSION_UPPER_BOUND_DEPENDENCY_EDGE_REPAIR_NOTE_2026-06-08.md`](DIMENSION_UPPER_BOUND_DEPENDENCY_EDGE_REPAIR_NOTE_2026-06-08.md)
turns the wrapper's textbook/import handle into an auditable dependency edge
without broadening the science. It wires this wrapper to the current one-hop
bounded support packets and composition gate:

| Role | Source packet | Runner/cache |
| --- | --- | --- |
| Native stable-orbit support | [`BERTRAND_STABLE_ORBIT_UPPER_BOUND_SUPPORT_NOTE_2026-05-20.md`](BERTRAND_STABLE_ORBIT_UPPER_BOUND_SUPPORT_NOTE_2026-05-20.md) | [`scripts/bertrand_stable_orbit_green_kernel_bridge.py`](../scripts/bertrand_stable_orbit_green_kernel_bridge.py), [`logs/runner-cache/bertrand_stable_orbit_green_kernel_bridge.txt`](../logs/runner-cache/bertrand_stable_orbit_green_kernel_bridge.txt) |
| Atomic / Coulomb support | [`COULOMB_STABILITY_UPPER_BOUND_SUPPORT_NOTE_2026-05-20.md`](COULOMB_STABILITY_UPPER_BOUND_SUPPORT_NOTE_2026-05-20.md) | [`scripts/frontier_coulomb_stability_scaling_repair.py`](../scripts/frontier_coulomb_stability_scaling_repair.py), [`logs/runner-cache/frontier_coulomb_stability_scaling_repair.txt`](../logs/runner-cache/frontier_coulomb_stability_scaling_repair.txt) |
| Current finite-set composition gate | [`D3_UPPER_BOUND_IMPORT_SCOPE_GATE_NOTE_2026-06-06.md`](D3_UPPER_BOUND_IMPORT_SCOPE_GATE_NOTE_2026-06-06.md) | [`scripts/frontier_d3_upper_bound_import_scope_gate_2026_06_06.py`](../scripts/frontier_d3_upper_bound_import_scope_gate_2026_06_06.py), [`logs/runner-cache/frontier_d3_upper_bound_import_scope_gate_2026_06_06.txt`](../logs/runner-cache/frontier_d3_upper_bound_import_scope_gate_2026_06_06.txt) |

The repair note's paired runner is
[`scripts/dimension_upper_bound_dependency_edge_repair_2026_06_08.py`](../scripts/dimension_upper_bound_dependency_edge_repair_2026_06_08.py),
with cache
[`logs/runner-cache/dimension_upper_bound_dependency_edge_repair_2026_06_08.txt`](../logs/runner-cache/dimension_upper_bound_dependency_edge_repair_2026_06_08.txt).

This dependency repair does not claim a complete framework-internal derivation
of Bertrand's theorem, atomic stability, or a full dimension-selection theorem.
It only makes the bounded support edges and finite-set composition visible for
independent audit.

## 2026-06-10 native stable-orbit import retirement

The current `d = 3` uniqueness composition uses only the finite lower packet
and the native stable-circular-orbit edge:

```text
L_runner = {3,4,5}
U_stable = {d : d <= 3}
L_runner intersect U_stable = {3}.
```

The load-bearing `U_stable` edge is the runner-checked calculation

```text
V(r) = -k/r^(d-2),
d^2 V_eff/dr^2 |_{r_c} = k(d-2)(4-d)/r_c^d,
```

from the support note above. Thus the present wrapper does **not** require the
full Bertrand closed-orbit theorem as an imported premise. The textbook
Bertrand theorem remains a parallel cross-reference for the broader classical
statement, not the source of the current finite-set upper cut.

## Upper-bound routes covered

### 1. Native stable-circular-orbit upper edge (Bertrand context)

Statement: for the attractive Green-kernel potential
`V(r) = -k/r^(d-2)` derived by the support note from the radial continuum
Laplacian, the circular-orbit stability sign is
`k(d-2)(4-d)/r_c^d`. For integer `d >= 3`:

- `d = 3` gives `F ~ 1 / r^2`, the Bertrand-allowed case.
- `d = 4` is marginal for the circular-orbit stability test.
- `d >= 5` is unstable under the same test.

Therefore, against the current lower packet `{3,4,5}`, stable circular
gravitational orbits select only `d = 3`.

Parallel reference: J. Bertrand, "Théorème relatif au mouvement d'un point
attiré vers un centre fixe," *C. R. Acad. Sci. Paris* **77**, 849
(1873). Modern textbook treatment: H. Goldstein, *Classical
Mechanics*, 3rd ed. (Addison-Wesley 2002), §3.6. These references are not
load-bearing for the finite stable-circular-orbit composition above.

### 2. Bounded Coulomb stability companion (Tangherlini/Ehrenfest context)

Statement: hydrogen-like atoms in `d`-dimensional space (with Coulomb
potential `V ~ -1 / r^{d - 2}` for `d >= 3`) admit normalizable bound
ground states only for `d <= 4`, and the standard atomic spectrum
with bound states accumulating at threshold `E -> 0` exists only for
`d = 3`. For `d >= 5` the Coulomb potential is so singular at the
origin that the Schrödinger Hamiltonian is not bounded below and no
stable ground state exists.

Modern textbook references:
- F. R. Tangherlini, "Schwarzschild field in `n` dimensions and the
  dimensionality of space problem," *Nuovo Cimento* **27**, 636 (1963).
- P. Ehrenfest, "In what way does it become manifest in the
  fundamental laws of physics that space has three dimensions?"
  *Proc. Amsterdam Acad.* **20**, 200 (1917).
- M. Bures & P. Siegl, "Hydrogen atom in space with a compactified
  extra dimension and potential defined by Gauss's law," *Annals
  Phys.* **354**, 316 (2015) — discussion of the bound-state existence
  threshold for the higher-dimensional Coulomb potential.

Therefore stable hydrogen-like atoms require `d <= 4`, with the
canonical infinite-bound-state Coulomb spectrum existing only at
`d = 3`.

## Upper-bound conclusion

Combined with the runner-verified `d >= 3` lower bound from
self-consistent propagator + gravitational field in
[DIMENSION_SELECTION_NOTE.md](DIMENSION_SELECTION_NOTE.md), the native
stable-orbit edge gives the matching upper bound `d <= 3`, yielding the
current finite-set conclusion `d = 3`. The bounded Coulomb route gives the
weaker companion upper bound `d <= 4`; it is compatible support, not the
unique selector for this packet.

## What this note does NOT claim

- This is NOT a proof of the full all-bounded-orbits-are-closed Bertrand
  theorem; the current finite composition only consumes the native
  stable-circular-orbit edge.
- This is NOT a complete framework-native derivation of atomic stability.
- This is NOT a framework-level derivation of `d = 3` from `Cl(3)` on
  `Z^3` alone — `Cl(3) ⊗ Z^3` has `d = 3` built into the substrate, so
  the framework does not need a separate dimension-selection theorem.
  The DIMENSION_SELECTION_NOTE lane is a complementary self-consistency
  check, not a framework derivation.
- The bounded scope is the source-side upper-bound composition only.

## Downstream usage

This wrapper is consumed by:

- [DIMENSION_SELECTION_NOTE.md](DIMENSION_SELECTION_NOTE.md) — supplies the upper-bound native stable-orbit edge plus bounded atomic-stability companion complementing the lower-bound (self-consistent gravity / propagator) runner result.

## Boundary

This wrapper note is a bounded source wrapper for the native stable-orbit
upper edge and bounded Coulomb companion. It does not claim:

- a framework derivation of the full Bertrand closed-orbit theorem or full
  atomic stability;
- closure of any downstream dimension-selection theorem.

Its function is to provide a citeable one-hop authority for the current
upper-bound composition, with textbook sources cited in parallel where they
describe broader classical context.
