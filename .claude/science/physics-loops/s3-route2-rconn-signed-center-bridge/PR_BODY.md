## Summary

Block71 adds a current-bank selector firewall for the signed Route-2 `Rconn`
center bridge.

The new note and runner split the collapsed bridge

```text
F_adj = 8/9 -> c_TE = gamma_T(center)/gamma_E(center) = -8/9
```

into the independent selectors a positive proof would need:

- typed domain functor from SU3 color/Fierz scalar to Route-2 center readout;
- negative sign/orientation;
- placement in the `c_TE` center-ratio slot;
- `kappa_EW = 0` if using physical `Rconn` instead of exact `F_adj` support.

Claim movement: exact `8/9` support and endpoint algebra are preserved, but
the current bank does not supply the full selector package. This prunes the
collapsed color shortcut as a derivation of `beta_E/alpha_E = 21/4`; it does
not close the s3-time parent row.

## Artifacts

- Note: `docs/QUARK_ROUTE2_RCONN_SIGNED_CENTER_BRIDGE_SELECTOR_FIREWALL_NOTE_2026-06-21.md`
- Runner: `scripts/frontier_quark_route2_rconn_signed_center_bridge_selector_firewall_2026_06_21.py`
- Output: `outputs/frontier_quark_route2_rconn_signed_center_bridge_selector_firewall_2026_06_21.txt`
- Loop pack: `.claude/science/physics-loops/s3-route2-rconn-signed-center-bridge/`
- Handoff: `.claude/science/physics-loops/s3-route2-rconn-signed-center-bridge/HANDOFF.md`
- Trace gate: `.claude/science/physics-loops/s3-route2-rconn-signed-center-bridge/TRACE_GATE.md`
- Certificate: `.claude/science/physics-loops/s3-route2-rconn-signed-center-bridge/CLAIM_STATUS_CERTIFICATE.md`

## Verification

- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_rconn_signed_center_bridge_selector_firewall_2026_06_21.py`
  - `TOTAL: PASS=78, FAIL=0`
- `python3 -m py_compile scripts/frontier_quark_route2_rconn_signed_center_bridge_selector_firewall_2026_06_21.py`
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_exact_readout_map.py`
  - `PASS=11 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_rconn_typed_bridge_derivation_bounded_2026_06_12.py`
  - `TOTAL: PASS=62, FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_source_domain_bridge_no_go.py`
  - `TOTAL: PASS=103, FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_rconn_center_ratio_bridge_obstruction.py`
  - `TOTAL: PASS=26, FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_cte_rconn_bridge_cross_domain_no_go.py`
  - `TOTAL: PASS=9 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_rconn_kappa_ew_register_not_read.py`
  - `TOTAL: PASS=20 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_s3_time_theta_to_slice_coupling.py`
  - `PASS=12 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_s3_time_theta_to_slice_coupling_factor_rigidity.py`
  - `PASS=64 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_e_center_lift_derivation_attempt_bounded_2026_06_12.py`
  - `TOTAL: PASS=46, FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_qe_covariance_schur_quadratic_no_go_2026_06_14.py`
  - `PASS=11 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_route2_readout_record_positivity_no_go.py`
  - `TOTAL: PASS=8 FAIL=0`

Known skipped runner: `scripts/frontier_s3_time_readout_primitive_bridge_assessment_2026_06_12.py`
is not part of this block because of the pre-existing tolerance issue recorded
in prior handoffs.
