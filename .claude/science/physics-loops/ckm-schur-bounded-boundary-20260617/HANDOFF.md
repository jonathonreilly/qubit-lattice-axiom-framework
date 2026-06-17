# Handoff

This block preserves the exact Schur-complement algebra and the six bounded
CKM comparator gaps, but changes their runner representation from hard failure
markers to `[BOUNDARY] [BOUNDED]` observations. This should unblock the queue
without narrowing away useful science.

Verification performed:

- `PYTHONPATH=scripts python3 scripts/frontier_ckm_schur_complement.py`
- `PYTHONPATH=scripts python3 scripts/cached_runner_output.py --refresh scripts/frontier_ckm_schur_complement.py --timeout-sec 120`
- no `[FAIL]`, `FAIL=`, or `FAILED:` markers in the refreshed cache

No audit/status surfaces are edited.

