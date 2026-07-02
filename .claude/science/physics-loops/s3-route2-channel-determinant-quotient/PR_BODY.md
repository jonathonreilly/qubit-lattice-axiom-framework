# Physics-loop block84: Route-2 channel determinant quotient gate

## Summary

This PR adds a no-go / conditional-support boundary for the Route-2 channel
determinant quotient route. A supplied diagonal determinant model
`S_R=diag(w_E,w_T1)` would give the inverse-square Hessian ratio `9/4` and the
endpoint triple exactly. The current determinant-context machinery does not
supply that Route-2 channel coordinate context, and determinant value alone
does not select the coordinate Hessian ratio.

## Artifacts

- `docs/QUARK_ROUTE2_CHANNEL_DETERMINANT_QUOTIENT_GATE_NOTE_2026-06-21.md`
- `scripts/frontier_quark_route2_channel_determinant_quotient_gate_2026_06_21.py`
- `outputs/frontier_quark_route2_channel_determinant_quotient_gate_2026_06_21.txt`
- `.claude/science/physics-loops/s3-route2-channel-determinant-quotient/`

## Checks

- `python3 -m py_compile scripts/frontier_quark_route2_channel_determinant_quotient_gate_2026_06_21.py`
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_channel_determinant_quotient_gate_2026_06_21.py`
  -> `TOTAL: PASS=24, FAIL=0`
- `PYTHONPATH=scripts python3 scripts/observable_principle_t1d_determinant_context_quotient_bridge_2026_06_18.py`
  -> `TOTAL: PASS=20 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/observable_principle_t1d_positive_diagonal_readout_classifier_2026_06_18.py`
  -> `TOTAL: PASS=33 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_observable_principle_t1d_determinant_readout_independence_2026_06_16.py`
  -> `TOTAL: PASS=20 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_qe_covariance_schur_quadratic_no_go_2026_06_14.py`
  -> `PASS=11 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_exact_readout_map.py`
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
