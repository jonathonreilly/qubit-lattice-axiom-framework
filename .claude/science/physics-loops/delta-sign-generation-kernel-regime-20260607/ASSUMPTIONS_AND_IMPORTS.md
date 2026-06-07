# Assumptions And Imports

## Consumed Internal Surfaces

- `STAGGERED_SELF_CONSISTENT_TWO_BODY_NOTE_2026-04-11.md`: retained bounded
  attractive two-body mediator surface.
- `GENERATION_PERIODIC_PLANE_WAVE_DENSITY_KERNEL_BRIDGE_NOTE_2026-06-07.md`:
  stacked bridge from PR #3029 deriving periodic plane-wave density-kernel
  normalization.
- `INTERACTION_ASYMMETRY_DELTA_OCCUPATION_CURVATURE_TWO_BODY_STRUCTURE_THEOREM_NOTE_2026-06-06.md`:
  structural context for `delta` as occupation curvature.

## Explicit Branch Condition

The sign propagation into `K_C3` requires:

```text
eps_gap > 0
eps_gap + delta > 0
```

This branch is not silently assumed as a physical closure. The note records it
as the remaining physical IR/gap branch.

## Forbidden Inputs

No PDG values, fitted selectors, lattice-MC values, or new axioms are used.
