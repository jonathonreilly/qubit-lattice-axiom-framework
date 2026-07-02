# Artifact Plan

## Files

- `docs/QUARK_ROUTE2_QE_BULK_LIMIT_CONSUMER_BOUNDARY_NOTE_2026-06-21.md`
  - consumer-boundary source note
- `scripts/frontier_quark_route2_qe_bulk_limit_consumer_boundary_2026_06_21.py`
  - cache-first verifier and exact algebra checks
- `outputs/frontier_quark_route2_qe_bulk_limit_consumer_boundary_2026_06_21.txt`
  - captured verifier output
- `.claude/science/physics-loops/s3-route2-qe-bulk-limit-consumer-boundary/`
  - branch-local loop pack

## Checks

- compile the new runner;
- run the new runner with `PYTHONPATH=scripts`;
- verify the heavy box-size scan cache is fresh with `cached_runner_output.py --check-only`;
- rerun the S3 primitive-chain and theta-to-slice consumers;
- rerun the measured-calibration, exact readout, and naturality no-go runners;
- run diff/hygiene scans before commit.
