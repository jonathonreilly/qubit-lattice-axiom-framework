# Artifact Plan

- Add a dedicated endpoint runner: `scripts/lattice_3d_dense_z2_z6_endpoint_check.py`.
- Add a source note: `docs/LATTICE_3D_DENSE_SPENT_DELAY_Z2_Z6_ENDPOINT_NOTE_2026-05-29.md`.
- Regenerate audit surfaces with `bash docs/audit/scripts/run_pipeline.sh`.
- Verify the new row is queued as unaudited and ready.
- Verify the existing `lattice_gravity_resolution_note` row is not reset.
- Open one draft review PR for the science block.
