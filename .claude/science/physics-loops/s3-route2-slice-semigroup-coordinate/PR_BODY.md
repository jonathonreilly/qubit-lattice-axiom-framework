# Physics-loop block88: Route-2 slice-semigroup coordinate gate

## Summary

This PR adds a no-go / semigroup-coordinate boundary for the raw `q_X`
selector. Raw scaling by `9/4` gives the endpoint, but it is not a semigroup
coordinate law; semigroup-natural generator coordinates miss `q_E=15/8`.

## Artifacts

- `docs/QUARK_ROUTE2_SLICE_SEMIGROUP_COORDINATE_GATE_NOTE_2026-06-21.md`
- `scripts/frontier_quark_route2_slice_semigroup_coordinate_gate_2026_06_21.py`
- `outputs/frontier_quark_route2_slice_semigroup_coordinate_gate_2026_06_21.txt`
- `.claude/science/physics-loops/s3-route2-slice-semigroup-coordinate/`

## Checks

- `python3 -m py_compile scripts/frontier_quark_route2_slice_semigroup_coordinate_gate_2026_06_21.py`
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_slice_semigroup_coordinate_gate_2026_06_21.py`
  -> `TOTAL: PASS=29, FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_s3_time_theta_to_slice_coupling.py`
  -> `PASS=12 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_qe_covariance_schur_quadratic_no_go_2026_06_14.py`
  -> `PASS=11 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_exact_readout_map.py`
  -> `PASS=11 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_e_channel_readout_naturality_no_go.py`
  -> `TOTAL: PASS=28, FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_e_center_blindness_no_go.py`
  -> `TOTAL: PASS=14, FAIL=0`

## Boundaries

- No audit verdicts are applied.
- No repo-wide authority surfaces are updated.
- No observed quark endpoint values or fitted selectors are used.
- Existing PRs are not refreshed to `main`.
- PR conflict/mergeability state is not checked.
