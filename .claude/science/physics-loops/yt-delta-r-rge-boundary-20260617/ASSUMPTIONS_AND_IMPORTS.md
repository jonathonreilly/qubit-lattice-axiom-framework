# Assumptions And Imports

## Current-Surface Inputs

- The 2026-06-16 P1 correction is authoritative for this block: corrected Delta_R precision is uncontrolled because of the scalar `/N_TASTE` double-count and fermion-channel IR-regulator dependence.
- The runner may still use the old `Delta_R = -3.27%` central as a historical comparator, but not as a current precision-retained input.
- The SM 2-loop RGE coefficients and primary-chain boundary values are inherited from existing YT notes and runners; this block only revalidates the deterministic runner output.

## Imports Not Retired Here

- The Delta_i BZ channel values remain historical/provenance inputs for this cross-check.
- The corrected P1 Delta_R defect remains open and is not repaired by this PR.
- Independent audit remains required before any effective-status movement.
