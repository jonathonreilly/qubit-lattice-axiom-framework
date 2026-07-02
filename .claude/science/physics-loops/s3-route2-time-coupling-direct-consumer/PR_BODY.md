# Physics-loop block90: Route-2 time-coupling direct consumer ambiguity gate

## Summary

This PR adds a no-go / exact support boundary for the direct time-coupling
consumer of the Route-2 readout ambiguity. It proves that varying `rho_E`
changes only the E-center source factor in `Xi_P(t ; c)`, while the E-shell,
T-shell, T-center, and shared slice dynamics stay fixed.

## Artifacts

- `docs/QUARK_ROUTE2_TIME_COUPLING_DIRECT_CONSUMER_AMBIGUITY_GATE_NOTE_2026-06-21.md`
- `scripts/frontier_quark_route2_time_coupling_direct_consumer_ambiguity_gate_2026_06_21.py`
- `outputs/frontier_quark_route2_time_coupling_direct_consumer_ambiguity_gate_2026_06_21.txt`
- `.claude/science/physics-loops/s3-route2-time-coupling-direct-consumer/`

## Checks

- `python3 -m py_compile scripts/frontier_quark_route2_time_coupling_direct_consumer_ambiguity_gate_2026_06_21.py`
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_time_coupling_direct_consumer_ambiguity_gate_2026_06_21.py`
  -> `TOTAL: PASS=38, FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_exact_time_coupling.py`
  -> `PASS=8 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_s3_time_theta_to_slice_coupling.py`
  -> `PASS=12 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_exact_readout_map.py`
  -> `PASS=11 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_e_center_blindness_no_go.py`
  -> `TOTAL: PASS=14, FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_e_channel_readout_naturality_no_go.py`
  -> `TOTAL: PASS=28, FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_qe_covariance_schur_quadratic_no_go_2026_06_14.py`
  -> `PASS=11 FAIL=0`

## Boundaries

- No audit verdicts are applied.
- No repo-wide authority surfaces are updated.
- No observed quark endpoint values or fitted selectors are used.
- Existing PRs are not refreshed to `main`.
- PR conflict/mergeability state is not checked.
