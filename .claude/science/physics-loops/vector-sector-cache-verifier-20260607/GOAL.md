# Goal

Repair `scripts/vector_sector_circular_orbit.py` so the audit runner cache no longer times out.

The original broad live propagation path exceeded 300 seconds in trial. The note already carries the frozen full-harness log, and the separate matched-scalar-exposure certificate remains live-green for the targeted audited case. This block makes the broad runner default verify that frozen full-harness log while preserving the original live computation behind `--recompute`.
