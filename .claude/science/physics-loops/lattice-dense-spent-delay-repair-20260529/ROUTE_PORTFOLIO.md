# Route Portfolio

## Route A: Dedicated Endpoint Runner

Status: executed.

Add `scripts/lattice_3d_dense_z2_z6_endpoint_check.py`, importing the existing dense 10-property harness and checking z=2..6 directly.

Expected movement: repair the exact missing z=6 endpoint artifact called out by the audit blocker.

## Route B: Mutate Existing Primary Runner

Status: rejected.

Editing `scripts/lattice_3d_dense_10prop.py` would risk invalidating `lattice_gravity_resolution_note`, which is already audited clean with `retained_bounded` effective status.

## Route C: Rewrite Archived Failed Note

Status: rejected.

The old unlanded/archived row should stay historical. This block creates a new auditable packet rather than retagging or rewriting the old audit history.
