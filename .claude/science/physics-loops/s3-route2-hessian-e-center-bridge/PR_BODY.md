# Physics-loop block85: Route-2 Hessian-to-E-center bridge gate

## Summary

This PR adds a no-go / conditional-support boundary for the bridge from
inverse-square Hessian coefficients to the Route-2 E-center lift. The
q-proportional map gives the endpoint exactly, but the current bank does not
select that map; other T-calibrated maps using the same Hessian coefficients
miss the target.

## Artifacts

- `docs/QUARK_ROUTE2_HESSIAN_E_CENTER_BRIDGE_GATE_NOTE_2026-06-21.md`
- `scripts/frontier_quark_route2_hessian_e_center_bridge_gate_2026_06_21.py`
- `outputs/frontier_quark_route2_hessian_e_center_bridge_gate_2026_06_21.txt`
- `.claude/science/physics-loops/s3-route2-hessian-e-center-bridge/`

## Checks

- `python3 -m py_compile scripts/frontier_quark_route2_hessian_e_center_bridge_gate_2026_06_21.py`
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_hessian_e_center_bridge_gate_2026_06_21.py`
  -> `TOTAL: PASS=26, FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_e_center_lift_derivation_attempt_bounded_2026_06_12.py`
  -> `TOTAL: PASS=46, FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_e_center_lift_measured_calibration_2026_06_10.py`
  -> `TOTAL: PASS=6 FAIL=0`
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
