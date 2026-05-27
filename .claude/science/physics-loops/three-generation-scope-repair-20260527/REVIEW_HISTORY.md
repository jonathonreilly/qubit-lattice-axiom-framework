# Review History

- Legacy runner check: `python3 scripts/frontier_generation_fermi_point.py` -> `EXACT PASS=7 FAIL=0`, `BOUNDED PASS=1 FAIL=0`.
- Narrow primary runner: `python3 scripts/frontier_three_generation_structure_narrow_spectrum.py` -> `PASS=15 FAIL=0`.
- Audit pipeline: `bash docs/audit/scripts/run_pipeline.sh` -> completed, row reset to `unaudited`, `ready: true`.
- Pending: final local checks and GitHub audit-lane check after PR creation.
