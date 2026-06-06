# Assumptions And Imports

## Allowed Inputs

- Existing finite dense-lattice endpoint runner:
  `scripts/lattice_3d_dense_z2_z6_endpoint_check.py`.
- Existing dense helper source:
  `scripts/lattice_3d_dense_10prop.py`.
- Existing runner-cache discipline under `logs/runner-cache/`.
- Existing note scope: finite `z=2..6` endpoint support in the dense
  spent-delay harness.

## Forbidden Inputs

- No observed physical target values.
- No fitted selectors.
- No external theorem import as proof of the finite endpoint result.
- No new axiom.
- No audit-verdict edit.

## Remaining Import Surface

The repair exposes the transitive helper source and verifies that the cached
endpoint/helper outputs are SHA-fresh. Independent audit still decides whether
that packet is sufficient for the row.
