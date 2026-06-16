# One-Parameter Shell Helper Packet Goal

Target claim:
`one_parameter_reduced_shell_law_note`

Goal: repair the audit packet artifact blocker by making the five load-bearing
helper sources and caches explicit.

The audit asked for full source/cache coverage or retained helper authorities
for:

- `scripts/frontier_star_shell_projector.py`
- `scripts/frontier_same_source_metric_ansatz_scan.py`
- `scripts/frontier_coarse_grained_exterior_law.py`
- `scripts/frontier_sewing_shell_source.py`
- `scripts/frontier_radial_shell_matching_law.py`

This branch makes those helpers static imports and adds a packet runner/cache
that verifies source presence, required functions, SHA-fresh caches, clean
exits, and passing helper output.
