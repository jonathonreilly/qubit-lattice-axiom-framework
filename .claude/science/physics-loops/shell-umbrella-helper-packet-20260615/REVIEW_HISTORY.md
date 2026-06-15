# Review History

- Before edit:
  - `extract_runner(...) -> None`.
  - parent runner cache was fresh.
  - helper modules were loaded dynamically through `_frontier_loader`.
- After edit:
  - graph extraction resolves `scripts/frontier_one_parameter_reduced_shell_law.py`.
  - helper paths include `_frontier_loader.py` plus all five umbrella helper modules.
- Full pipeline:
  - `audit_lint` errors: 0.
  - hard invalidations: 0.
  - local ready count: 2.
