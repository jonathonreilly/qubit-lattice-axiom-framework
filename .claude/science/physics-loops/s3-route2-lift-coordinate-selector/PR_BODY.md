# Physics-loop block87: Route-2 lift-coordinate selector gate

## Summary

This PR adds a no-go / coordinate-selector boundary for the inverse-square
Route-2 channel ratio. The value `9/4` gives the endpoint only if it scales
the multiplicative lift `q_X`; applying the same value to the additive slope
`rho_X` or increment `q_X-1` misses the target.

## Artifacts

- `docs/QUARK_ROUTE2_LIFT_COORDINATE_SELECTOR_GATE_NOTE_2026-06-21.md`
- `scripts/frontier_quark_route2_lift_coordinate_selector_gate_2026_06_21.py`
- `outputs/frontier_quark_route2_lift_coordinate_selector_gate_2026_06_21.txt`
- `.claude/science/physics-loops/s3-route2-lift-coordinate-selector/`

## Checks

- `python3 -m py_compile scripts/frontier_quark_route2_lift_coordinate_selector_gate_2026_06_21.py`
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_lift_coordinate_selector_gate_2026_06_21.py`
  -> `TOTAL: PASS=31, FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_qe_covariance_schur_quadratic_no_go_2026_06_14.py`
  -> `PASS=11 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_exact_readout_map.py`
  -> `PASS=11 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_e_channel_readout_naturality_no_go.py`
  -> `TOTAL: PASS=28, FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_route2_readout_record_positivity_no_go.py`
  -> `TOTAL: PASS=8 FAIL=0`
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
