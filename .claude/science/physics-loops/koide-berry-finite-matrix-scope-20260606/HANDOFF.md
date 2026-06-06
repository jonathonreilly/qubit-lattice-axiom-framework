# Handoff

Branch:
`physics-loop/koide-berry-finite-matrix-scope-20260606`

Repair:
The Koide/Berry packet is narrowed to finite matrix algebra. It no longer claims
that native zero Berry selects `Q=1` or that nonzero Berry/chirality selects
`Q=2/3`.

Verification:

- `python3 -m py_compile scripts/frontier_koide_berry_monopole_bridge_reduction_2026_05_31.py`
- `python3 scripts/frontier_koide_berry_monopole_bridge_reduction_2026_05_31.py`
- Runner cache refreshed at
  `logs/runner-cache/frontier_koide_berry_monopole_bridge_reduction_2026_05_31.txt`

Remaining blocker:
A retained bridge theorem is still needed if the repo wants a positive
Berry/chirality-to-`r` weighting selection or a physical `Q` branch assignment.

Audit discipline:
No files under `docs/audit/` were edited.
