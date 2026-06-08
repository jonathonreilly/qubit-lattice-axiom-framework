# Dimension Selection Upper-Bound — Named Non-Derivation Imports

**Date:** 2026-05-17
**Claim type:** bounded_theorem
**Status:** bounded named-import wrapper for the two textbook results
that supply the `d <= 3` upper bound complementing the
`d >= 3` lower-bound result in
[DIMENSION_SELECTION_NOTE.md](DIMENSION_SELECTION_NOTE.md).
**Status authority:** independent audit lane only.

## Purpose

This wrapper note documents two classical-physics results as named
non-derivation imports so the
[DIMENSION_SELECTION_NOTE.md](DIMENSION_SELECTION_NOTE.md) lane can
register a one-hop dependency for the `d <= 3` upper-bound argument
rather than carry it as an unattributed textbook reference.

## 2026-06-08 dependency-edge source repair

The source-side repair note
[`DIMENSION_UPPER_BOUND_DEPENDENCY_EDGE_REPAIR_NOTE_2026-06-08.md`](DIMENSION_UPPER_BOUND_DEPENDENCY_EDGE_REPAIR_NOTE_2026-06-08.md)
turns the wrapper's textbook/import handle into an auditable dependency edge
without broadening the science. It wires this wrapper to the current one-hop
bounded support packets and composition gate:

| Role | Source packet | Runner/cache |
| --- | --- | --- |
| Bertrand / stable-orbit support | [`BERTRAND_STABLE_ORBIT_UPPER_BOUND_SUPPORT_NOTE_2026-05-20.md`](BERTRAND_STABLE_ORBIT_UPPER_BOUND_SUPPORT_NOTE_2026-05-20.md) | [`scripts/bertrand_stable_orbit_green_kernel_bridge.py`](../scripts/bertrand_stable_orbit_green_kernel_bridge.py), [`logs/runner-cache/bertrand_stable_orbit_green_kernel_bridge.txt`](../logs/runner-cache/bertrand_stable_orbit_green_kernel_bridge.txt) |
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

## Imports covered

### 1. Bertrand's theorem (1873) — orbital-stability upper bound

Statement: in dimension `d = 3`, the only central force laws producing
closed stable bounded orbits under classical Newtonian dynamics are
the inverse-square law `F ~ 1 / r^2` and the harmonic-oscillator law
`F ~ r`. For an inverse-power gravity law `F ~ 1 / r^{d - 1}` from
the d-dimensional Poisson equation:

- `d = 3` gives `F ~ 1 / r^2`, the Bertrand-allowed case.
- `d >= 4` gives `F ~ 1 / r^{d - 1}` with falloff steeper than
  `1 / r^2`, for which perturbations of closed orbits grow exponentially
  (no bound orbits exist; small radial perturbations cause spiral
  inward or outward).

Therefore stable bounded orbits under gravity require `d <= 3`.

Reference: J. Bertrand, "Théorème relatif au mouvement d'un point
attiré vers un centre fixe," *C. R. Acad. Sci. Paris* **77**, 849
(1873). Modern textbook treatment: H. Goldstein, *Classical
Mechanics*, 3rd ed. (Addison-Wesley 2002), §3.6.

### 2. Atomic stability upper bound (Tangherlini 1963; Ehrenfest 1917)

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
[DIMENSION_SELECTION_NOTE.md](DIMENSION_SELECTION_NOTE.md), the two
textbook imports give the matching upper bound `d <= 3` (from
Bertrand's theorem) and `d <= 4` (from atomic stability), yielding the
joint conclusion `d = 3`.

## What this note does NOT claim

- This is NOT a re-derivation of Bertrand's theorem.
- This is NOT a re-derivation of the atomic-stability upper bound.
- This is NOT a framework-level derivation of `d = 3` from `Cl(3)` on
  `Z^3` alone — `Cl(3) ⊗ Z^3` has `d = 3` built into the substrate, so
  the framework does not need a separate dimension-selection theorem.
  The DIMENSION_SELECTION_NOTE lane is a complementary self-consistency
  check, not a framework derivation.
- The bounded scope is the named non-derivation import only.

## Downstream usage

This wrapper is consumed by:

- [DIMENSION_SELECTION_NOTE.md](DIMENSION_SELECTION_NOTE.md) — supplies the upper-bound (Bertrand's theorem + atomic-stability) authority complementing the lower-bound (self-consistent gravity / propagator) runner result.

## Boundary

This wrapper note is a named-import-only bounded theorem covering two
textbook physics results. It does not claim:

- a framework derivation of either Bertrand's theorem or atomic
  stability;
- closure of any downstream dimension-selection theorem.

Its only function is to provide a citeable one-hop authority for the
two textbook imports so downstream notes register them cleanly
instead of carrying them as accepted-mathematics-and-physics
infrastructure without an audit-lane handle.
