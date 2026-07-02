# Physics-loop block81: Route-2 inverse-square channel-law gate

## Summary

This PR adds a pure Route-2 exponent gate for the missing readout law:

```text
C_X proportional to w_X^p.
```

The verifier shows the endpoint requires `p=-2` exactly. Native/simple powers
`p=-1,0,1,2` miss, so the remaining positive target is a real second-dual
inverse-square readout primitive.

## Artifacts

- `docs/QUARK_ROUTE2_INVERSE_SQUARE_CHANNEL_LAW_GATE_NOTE_2026-06-21.md`
- `scripts/frontier_quark_route2_inverse_square_channel_law_gate_2026_06_21.py`
- `outputs/frontier_quark_route2_inverse_square_channel_law_gate_2026_06_21.txt`
- `.claude/science/physics-loops/s3-route2-inverse-square-channel-law/`

## Checks

- `python3 -m py_compile scripts/frontier_quark_route2_inverse_square_channel_law_gate_2026_06_21.py`
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_inverse_square_channel_law_gate_2026_06_21.py`
  -> `TOTAL: PASS=20, FAIL=0`
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
