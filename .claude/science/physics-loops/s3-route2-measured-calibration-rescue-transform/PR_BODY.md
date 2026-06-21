## Summary

This physics-loop block adds a narrow current-bank no-go for the Route-2 measured-calibration rescue route after the box-size scan.

It asks whether the landed measured-calibration cache can still recover `q_E=15/8`, `q_T=5/6`, or `q_E/q_T=9/4` by a non-fitted bulk/tail transform without selecting the anomalous `N=15` point. The answer is no for the current cache: fixed-radius bulk tails, box-proportional stable tails, bulk convex reuse, and bulk covariance reuse all miss the endpoint chain.

This does not derive the endpoint triple, does not apply an audit verdict, and does not claim future nonlinear observables fail. It leaves the positive route as a new E-center-sensitive source/readout primitive or new physical tensor observable.

## Artifacts

- Note: `docs/QUARK_ROUTE2_MEASURED_CALIBRATION_RESCUE_TRANSFORM_FIREWALL_NOTE_2026-06-21.md`
- Runner: `scripts/frontier_quark_route2_measured_calibration_rescue_transform_firewall_2026_06_21.py`
- Output: `outputs/frontier_quark_route2_measured_calibration_rescue_transform_firewall_2026_06_21.txt`
- Handoff: `.claude/science/physics-loops/s3-route2-measured-calibration-rescue-transform/HANDOFF.md`
- Trace gate: `.claude/science/physics-loops/s3-route2-measured-calibration-rescue-transform/TRACE_GATE.md`
- Status certificate: `.claude/science/physics-loops/s3-route2-measured-calibration-rescue-transform/CLAIM_STATUS_CERTIFICATE.md`

## Verification

- `python3 -m py_compile scripts/frontier_quark_route2_measured_calibration_rescue_transform_firewall_2026_06_21.py`: pass
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_measured_calibration_rescue_transform_firewall_2026_06_21.py`: `TOTAL: PASS=40, FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_qe_box_size_scan_2026_06_10.py`: `TOTAL: PASS=7 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_e_center_lift_measured_calibration_2026_06_10.py`: `TOTAL: PASS=6 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_qe_covariance_schur_quadratic_no_go_2026_06_14.py`: `PASS=11 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_exact_readout_map.py`: `PASS=11 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_s3_time_theta_to_slice_coupling.py`: `PASS=12 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_e_center_blindness_no_go.py`: `TOTAL: PASS=14, FAIL=0`

## Review Notes

- Branch-local self-review disposition: pass.
- No observed masses, fitted endpoint values, CKM/J targets, or nearest-rational proof inputs are consumed.
- `N=15` is treated only as a comparator/anomaly, not as a proof selector.
- No repo-wide authority surfaces are edited.
