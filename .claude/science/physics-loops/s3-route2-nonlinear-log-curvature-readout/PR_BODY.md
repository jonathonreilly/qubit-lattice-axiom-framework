# Physics-loop block82: Route-2 nonlinear log-curvature readout candidate

## Summary

This PR adds a conditional-support stretch packet for the pure Route-2
second-dual readout law. It shows that a log-barrier channel curvature

```text
d^2(-log w_X)/dw_X^2 = 1/w_X^2
```

would produce `lambda=9/4` and the endpoint triple exactly. The checked
current bank does not supply the log-barrier variational/readout primitive, so
this remains support for a concrete future theorem target rather than
current-surface closure.

## Artifacts

- `docs/QUARK_ROUTE2_NONLINEAR_LOG_CURVATURE_READOUT_CANDIDATE_NOTE_2026-06-21.md`
- `scripts/frontier_quark_route2_nonlinear_log_curvature_readout_2026_06_21.py`
- `outputs/frontier_quark_route2_nonlinear_log_curvature_readout_2026_06_21.txt`
- `.claude/science/physics-loops/s3-route2-nonlinear-log-curvature-readout/`

## Checks

- `python3 -m py_compile scripts/frontier_quark_route2_nonlinear_log_curvature_readout_2026_06_21.py`
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_nonlinear_log_curvature_readout_2026_06_21.py`
  -> `TOTAL: PASS=18, FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_exact_readout_map.py`
  -> `PASS=11 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_qe_covariance_schur_quadratic_no_go_2026_06_14.py`
  -> `PASS=11 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_s3_time_theta_to_slice_coupling.py`
  -> `PASS=12 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_e_center_blindness_no_go.py`
  -> `TOTAL: PASS=14, FAIL=0`

## Boundaries

- No audit verdicts are applied.
- No repo-wide authority surfaces are updated.
- No observed quark endpoint values or fitted selectors are used.
- Existing PRs are not refreshed to `main`.
- PR conflict/mergeability state is not checked.
