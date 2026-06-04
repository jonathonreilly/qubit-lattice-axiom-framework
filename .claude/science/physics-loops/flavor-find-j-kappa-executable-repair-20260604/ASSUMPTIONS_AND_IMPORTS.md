# Assumptions And Imports

## Load-Bearing Inputs

- Real regular representation of `C3`.
- Central projectors onto the trivial and standard real sectors.
- Existing round-4 equipartition and det_C/det_R arithmetic.

## Retired Runner Artifact

- R4-2 Plancherel check now computes central projector ranks `(1,2)` and distinguishes per-DOF `r=1` from equal-block `r=1/2`.
- R4-3 K0/Wedderburn check now computes the two central blocks and verifies that multiple positive `C3`-invariant metrics exist on the same blocks, so K0 count alone does not fix energy weights.

## Still Open

- One-hop authority coverage for rounds 1-3 remains open.
- This branch does not promote the full four-round no-forcing theorem.
