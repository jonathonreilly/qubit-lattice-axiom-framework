# Handoff

## Target

- `s3_anomaly_spacetime_lift_note`
- `universal_gr_tensor_variational_candidate_note`

## What changed

- `S3_ANOMALY_SPACETIME_LIFT_NOTE.md` now registers
  `scripts/frontier_s3_anomaly_spacetime_lift.py` as its primary runner.
- The S3/anomaly runner now checks the current bounded/conditional upstream
  route boundary instead of stale exact/closed wording.
- `UNIVERSAL_GR_TENSOR_VARIATIONAL_CANDIDATE_NOTE.md` now registers
  `scripts/frontier_universal_gr_tensor_variational_candidate.py` as its
  primary runner and states an explicit audit boundary.
- Both runner caches are refreshed.

## Status boundary

This PR does not close GR. It leaves the dynamics / Einstein-Regge
identification bridge open and does not promote any audit status.

## Verification

```bash
python3 scripts/frontier_s3_anomaly_spacetime_lift.py
python3 scripts/frontier_universal_gr_tensor_variational_candidate.py
python3 scripts/cached_runner_output.py --refresh scripts/frontier_s3_anomaly_spacetime_lift.py
python3 scripts/cached_runner_output.py --refresh scripts/frontier_universal_gr_tensor_variational_candidate.py
python3 scripts/cached_runner_output.py --check-only scripts/frontier_s3_anomaly_spacetime_lift.py
python3 scripts/cached_runner_output.py --check-only scripts/frontier_universal_gr_tensor_variational_candidate.py
python3 -m py_compile scripts/frontier_s3_anomaly_spacetime_lift.py scripts/frontier_universal_gr_tensor_variational_candidate.py
git diff --check
```

## Reviewer notes

This is meant to let the audit pipeline rediscover runner paths from source
after review extraction. It intentionally avoids generated audit files.
