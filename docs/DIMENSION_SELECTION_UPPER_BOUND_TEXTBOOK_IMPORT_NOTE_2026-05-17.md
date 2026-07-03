# Dimension Selection Upper-Bound - Native Stable-Orbit Edge with Textbook Cross-References

**Date:** 2026-05-17
**Type:** bounded_theorem
**Status:** bounded source wrapper for the native stable-orbit upper edge
and bounded Coulomb Green-kernel scaling companion that complement the
`d >= 3` lower-bound result in
[DIMENSION_SELECTION_NOTE.md](DIMENSION_SELECTION_NOTE.md).
**Primary runner:** [`scripts/dimension_selection_upper_bound_textbook_import_scope_certificate_2026_06_12.py`](../scripts/dimension_selection_upper_bound_textbook_import_scope_certificate_2026_06_12.py)
**Cached source-packet output:** [`logs/runner-cache/dimension_selection_upper_bound_textbook_import_scope_certificate_2026_06_12.txt`](../logs/runner-cache/dimension_selection_upper_bound_textbook_import_scope_certificate_2026_06_12.txt)
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
| Coulomb Green-kernel scaling support | [`COULOMB_STABILITY_UPPER_BOUND_SUPPORT_NOTE_2026-05-20.md`](COULOMB_STABILITY_UPPER_BOUND_SUPPORT_NOTE_2026-05-20.md) | [`scripts/frontier_coulomb_stability_scaling_repair.py`](../scripts/frontier_coulomb_stability_scaling_repair.py), [`logs/runner-cache/frontier_coulomb_stability_scaling_repair.txt`](../logs/runner-cache/frontier_coulomb_stability_scaling_repair.txt) |
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

## 2026-06-12 Coulomb companion scope narrowing

The Coulomb companion previously carried broader textbook/spectral breadth.
This source packet therefore narrows the Coulomb side to the runner-checked
Green-kernel support lemma in
[`COULOMB_STABILITY_UPPER_BOUND_SUPPORT_NOTE_2026-05-20.md`](COULOMB_STABILITY_UPPER_BOUND_SUPPORT_NOTE_2026-05-20.md):

```text
Q_d[psi_lambda] = lambda^2 T - lambda^(d-2) U
```

for the attractive Green-kernel form `G_d(r) = r^(2-d)` on compactly supported
test functions away from the origin. The lemma shows ultraviolet collapse of
this form for integer `d >= 5` and identifies `d = 4` as the marginal
inverse-square exponent. It does **not** prove a framework-native
electromagnetic sector, a hydrogenic spectrum, bound-state threshold
accumulation, or atomic stability.

Thus the Coulomb companion is only compatible support:

```text
L_runner = {3,4,5}
U_Coulomb_scaling = {d : d <= 4}   (weak scaling upper edge)
L_runner intersect U_Coulomb_scaling = {3,4}.
```

It is not the selector in this wrapper. The decisive upper edge remains the
native stable-circular-orbit route:

```text
L_runner intersect U_stable = {3}.
```

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

### 2. Bounded Coulomb Green-kernel scaling companion

Statement: the runner-checked support note proves only the framework-local
scaling sublemma for the admitted attractive Green-kernel quadratic form

```text
Q_d[psi] = kappa int |grad psi|^2 dx
           - alpha int |x|^(2-d) |psi|^2 dx,
```

the dilation `psi_lambda(x) = lambda^(d/2) psi(lambda x)` preserves
the `L^2` norm and gives

```text
Q_d[psi_lambda] = lambda^2 T - lambda^(d-2) U.
```

Therefore the scaling test sends `Q_d[psi_lambda] -> -infinity` for
integer `d >= 5`, while `d = 4` is marginal and `d = 3` is not ruled
out by this ultraviolet collapse test. This is the whole load-bearing
Coulomb companion in this wrapper.

Equivalently, the attractive Green-kernel form is unbounded below on this test-function family
for every integer `d >= 5`.

Textbook references are cited only in parallel for the broader historical
hydrogenic/atomic-stability context:
- F. R. Tangherlini, "Schwarzschild field in `n` dimensions and the
  dimensionality of space problem," *Nuovo Cimento* **27**, 636 (1963).
- P. Ehrenfest, "In what way does it become manifest in the
  fundamental laws of physics that space has three dimensions?"
  *Proc. Amsterdam Acad.* **20**, 200 (1917).
- M. Bures & P. Siegl, "Hydrogen atom in space with a compactified
  extra dimension and potential defined by Gauss's law," *Annals
  Phys.* **354**, 316 (2015) — discussion of the bound-state existence
  threshold for the higher-dimensional Coulomb potential.

These references are parallel context for the broader physical hydrogenic
story. They are not load-bearing authority in this wrapper, which consumes
only the Green-kernel scaling lemma above. This wrapper does **not** consume a textbook hydrogen spectrum,
threshold-accumulation theorem, self-adjoint-extension classification, or complete
atomic-stability theorem as a load-bearing input.

## Upper-bound conclusion

Combined with the runner-verified `d >= 3` lower bound from
self-consistent propagator + gravitational field in
[DIMENSION_SELECTION_NOTE.md](DIMENSION_SELECTION_NOTE.md), the native
stable-orbit edge gives the matching upper bound `d <= 3`, yielding the
current finite-set conclusion `d = 3`. The bounded Coulomb Green-kernel
scaling companion gives only the weaker exclusion of `d >= 5` by this
ultraviolet-collapse test; against `L_runner = {3,4,5}`, it leaves `{3,4}`
and is therefore compatible support, not the selector for this packet.

## What this note does NOT claim

- This is NOT a proof of the full all-bounded-orbits-are-closed Bertrand
  theorem; the current finite composition only consumes the native
  stable-circular-orbit edge.
- This is NOT a complete framework-native derivation of atomic stability.
- This is NOT a hydrogenic spectral theorem: no normalizable-ground-state,
  threshold-accumulation, or canonical Rydberg-series claim is load-bearing.
- This is NOT a framework-level derivation of `d = 3` from `Cl(3)` on
  `Z^3` alone — `Cl(3) ⊗ Z^3` has `d = 3` built into the substrate, so
  the framework does not need a separate dimension-selection theorem.
  The DIMENSION_SELECTION_NOTE lane is a complementary self-consistency
  check, not a framework derivation.
- The bounded scope is the source-side upper-bound composition only.

## Downstream usage

This wrapper is consumed by:

- [DIMENSION_SELECTION_NOTE.md](DIMENSION_SELECTION_NOTE.md) — supplies the upper-bound native stable-orbit edge plus bounded Coulomb Green-kernel scaling companion complementing the lower-bound (self-consistent gravity / propagator) runner result.

## Boundary

This wrapper note is a bounded source wrapper for the native stable-orbit
upper edge and bounded Coulomb Green-kernel scaling companion. It does not
claim:

- a framework derivation of the full Bertrand closed-orbit theorem or full
  atomic stability / hydrogenic spectrum;
- closure of any downstream dimension-selection theorem.

Its function is to provide a citeable one-hop authority for the current
upper-bound composition, with textbook sources cited in parallel where they
describe broader classical context.
