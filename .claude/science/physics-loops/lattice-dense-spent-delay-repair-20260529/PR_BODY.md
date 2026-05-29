## Summary

This PR adds a dedicated bounded-support endpoint packet for the 3D dense spent-delay finite card. It does not mutate the existing retained-bounded primary runner `scripts/lattice_3d_dense_10prop.py`.

New artifacts:

- `scripts/lattice_3d_dense_z2_z6_endpoint_check.py`
- `docs/LATTICE_3D_DENSE_SPENT_DELAY_Z2_Z6_ENDPOINT_NOTE_2026-05-29.md`
- `.claude/science/physics-loops/lattice-dense-spent-delay-repair-20260529/`

## Science Boundary

The runner checks z=2,3,4,5,6 on the existing dense `L=12`, `W=6`, `h=1.0`, 49-edge/node spent-delay harness. All five endpoints classify as `ATTRACTIVE`, and z=6 is positive on centroid shift, near-window probability, and side-bias.

Safe read: finite endpoint support only. This does not claim continuum attraction, all-distance attraction, physical Newtonian gravity, or effective retained status before independent audit.

## Audit Queue

`bash docs/audit/scripts/run_pipeline.sh`:

- newly seeded: 1
- stale audit invalidations: 0
- new row: `lattice_3d_dense_spent_delay_z2_z6_endpoint_note_2026-05-29`
- queue rank: 900
- ready: true
- open dependencies: none

The existing `lattice_gravity_resolution_note` row remains `audited_clean` / `retained_bounded`.

## Verification

```text
python3 -m py_compile scripts/lattice_3d_dense_z2_z6_endpoint_check.py
python3 scripts/lattice_3d_dense_z2_z6_endpoint_check.py
bash docs/audit/scripts/run_pipeline.sh
git diff --check
```
