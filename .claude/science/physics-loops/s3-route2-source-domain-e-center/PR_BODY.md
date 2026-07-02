# Physics-loop block86: Route-2 source-domain E-center primitive gate

## Summary

This PR adds a no-go / source-domain selector boundary for the direct
`delta_A1` route to the missing Route-2 E-center coefficient. The scalar
distinguishes shell from center, but because it is common to E and T in the
current carrier, it does not by itself select `beta_E/alpha_E=21/4`.

## Artifacts

- `docs/QUARK_ROUTE2_SOURCE_DOMAIN_E_CENTER_PRIMITIVE_GATE_NOTE_2026-06-21.md`
- `scripts/frontier_quark_route2_source_domain_e_center_primitive_gate_2026_06_21.py`
- `outputs/frontier_quark_route2_source_domain_e_center_primitive_gate_2026_06_21.txt`
- `.claude/science/physics-loops/s3-route2-source-domain-e-center/`

## Checks

- `python3 -m py_compile scripts/frontier_quark_route2_source_domain_e_center_primitive_gate_2026_06_21.py`
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_source_domain_e_center_primitive_gate_2026_06_21.py`
  -> `TOTAL: PASS=42, FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_source_domain_bridge_no_go.py`
  -> `TOTAL: PASS=103, FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_rconn_typed_bridge_derivation_bounded_2026_06_12.py`
  -> `TOTAL: PASS=62, FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_e_channel_readout_naturality_no_go.py`
  -> `TOTAL: PASS=28, FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_route2_readout_record_positivity_no_go.py`
  -> `TOTAL: PASS=8 FAIL=0`
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
