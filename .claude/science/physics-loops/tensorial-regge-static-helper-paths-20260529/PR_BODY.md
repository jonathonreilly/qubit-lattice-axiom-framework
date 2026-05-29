## Summary

Repairs the tensorial Einstein-Regge helper row's audit-packet blocker
without changing science scope.

The primary runner no longer hides helper scripts behind dynamic
`_frontier_loader.load_frontier(...)` calls. It statically imports the same
helper modules, so the audit pipeline now records:

- `scripts/_frontier_loader.py`
- `scripts/frontier_coarse_grained_exterior_law.py`
- `scripts/frontier_microscopic_dirichlet_bridge_principle.py`
- `scripts/frontier_oh_schur_boundary_action.py`
- `scripts/frontier_same_source_metric_ansatz_scan.py`

## Checks

- `python3 -m py_compile scripts/frontier_tensorial_einstein_regge_completion.py`
- `python3 scripts/frontier_tensorial_einstein_regge_completion.py`
  - decisive tests all PASS
- `bash docs/audit/scripts/run_pipeline.sh`
  - target row reset to `unaudited`
  - queue ready: `true`
  - open dependency paths: `[]`
  - helper runner paths include the dynamic helper scripts named by audit

## Status

Branch-local status: bounded-support, re-audit ready.

This PR does not apply an audit verdict and does not claim effective
retained status. Independent audit remains required.
