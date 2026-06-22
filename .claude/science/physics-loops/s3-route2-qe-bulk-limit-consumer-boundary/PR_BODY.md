# Summary

This physics-loop block packages a consumer-boundary no-go for the S3/Route-2
endpoint triple.

The already-landed `q_E(N)` box-size scan closes the measured-calibration
bulk-limit route: the finite `N=15` shell-response match near `q_E=15/8` is not
an infinite-volume derivation for the tested stack functional. This branch
connects that result to `S3_TIME_PRIMITIVE_CHAIN_NOTE.md` and records the
remaining fixed-carrier blocker.

## Claim Status

- Actual current-surface status: `no-go`
- Trace class: `negative_route_pruning`
- Reachability: prunes the bulk-limit promotion route only
- Does not derive `rho_E=21/4`, `q_E=15/8`, or the endpoint triple
- Does not update audit verdicts or repo-wide authority surfaces

## Artifacts

- `docs/QUARK_ROUTE2_QE_BULK_LIMIT_CONSUMER_BOUNDARY_NOTE_2026-06-21.md`
- `scripts/frontier_quark_route2_qe_bulk_limit_consumer_boundary_2026_06_21.py`
- `outputs/frontier_quark_route2_qe_bulk_limit_consumer_boundary_2026_06_21.txt`
- `.claude/science/physics-loops/s3-route2-qe-bulk-limit-consumer-boundary/`

## Verification

- `python3 -m py_compile scripts/frontier_quark_route2_qe_bulk_limit_consumer_boundary_2026_06_21.py`
  - pass
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_qe_bulk_limit_consumer_boundary_2026_06_21.py`
  - `TOTAL: PASS=37, FAIL=0`
- `python3 scripts/cached_runner_output.py scripts/frontier_quark_route2_qe_box_size_scan_2026_06_10.py --check-only`
  - fresh
- `PYTHONPATH=scripts python3 scripts/frontier_s3_time_primitive_chain_reaudit.py`
  - `TOTAL: PASS=24, FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_s3_time_theta_to_slice_coupling.py`
  - `PASS=12 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_e_center_lift_measured_calibration_2026_06_10.py`
  - `TOTAL: PASS=6 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_e_channel_readout_naturality_no_go.py`
  - `TOTAL: PASS=28, FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_exact_readout_map.py`
  - `PASS=11 FAIL=0`
- `git diff --check`
  - pass
- changed-files overclaim scan
  - pass
- changed-files ASCII scan
  - pass

## Remaining Blocker

The positive target remains unchanged: derive a fixed-carrier
E-center/source/readout primitive that selects `beta_E/alpha_E=21/4` without
observed targets, fitted selectors, or bulk-limit promotion of the measured
calibration.
