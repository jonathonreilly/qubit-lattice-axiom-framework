# Handoff

This PR repairs the RALA timeout without narrowing the finite grid.

Main change: the dense pair Bell-projector check remains for `n <= 32`; for `dim=3, side=4`, the runner first verifies the single-register RALA factorization of `Z_axis` and `X_axis`, then checks the Bell projector and teleportation identities in the exact logical factor. The source note now documents that split.

Verification:

```bash
python3 scripts/frontier_teleportation_retained_axis_operator_algebra_closure.py
python3 scripts/cached_runner_output.py --check-only scripts/frontier_teleportation_retained_axis_operator_algebra_closure.py
python3 scripts/precompute_audit_runners.py --runners scripts/frontier_teleportation_retained_axis_operator_algebra_closure.py --check-only --allow-non-main
```

Expected runner summary:

```text
PASS=96 FAIL=0
status: ok
elapsed_sec: 0.14
```

No audit-result files are included.
