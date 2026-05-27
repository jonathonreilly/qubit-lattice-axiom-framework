# Artifact Plan

- Patch `scripts/frontier_higgs_lattice_eigenvalue_ratio_narrow.py`.
- Regenerate `logs/runner-cache/frontier_higgs_lattice_eigenvalue_ratio_narrow.txt`.
- Run the audit-data pipeline so the stale audit is invalidated and the row is
  queued for independent audit.
