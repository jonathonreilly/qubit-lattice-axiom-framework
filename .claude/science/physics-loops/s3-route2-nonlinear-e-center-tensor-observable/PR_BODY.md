## Summary

This physics-loop block adds a first-principles boundary for the nonlinear E-center tensor-observable route in the Route-2 readout endpoint campaign.

The result: pure rank-1 carrier invariants have zero bright-linear endpoint readout, and any common scalar nonlinear dressing of the current carrier forces `q_E=q_T`, hence `q_E/q_T=1`, not the target `9/4`. In affine endpoint form, hitting the target requires separate channel slopes `(rho_E,rho_T)=(21/4,-1)`, which is exactly the missing E/T readout selector rather than a consequence of nonlinearity alone.

This does not derive the endpoint triple, does not apply an audit verdict, and does not claim all future nonlinear observables fail. It leaves open a genuine channel-selecting nonlinear observable or source/readout primitive.

## Artifacts

- Note: `docs/QUARK_ROUTE2_NONLINEAR_E_CENTER_TENSOR_OBSERVABLE_GATE_NOTE_2026-06-21.md`
- Runner: `scripts/frontier_quark_route2_nonlinear_e_center_tensor_observable_gate_2026_06_21.py`
- Output: `outputs/frontier_quark_route2_nonlinear_e_center_tensor_observable_gate_2026_06_21.txt`
- Handoff: `.claude/science/physics-loops/s3-route2-nonlinear-e-center-tensor-observable/HANDOFF.md`
- Trace gate: `.claude/science/physics-loops/s3-route2-nonlinear-e-center-tensor-observable/TRACE_GATE.md`
- Status certificate: `.claude/science/physics-loops/s3-route2-nonlinear-e-center-tensor-observable/CLAIM_STATUS_CERTIFICATE.md`

## Verification

- `python3 -m py_compile scripts/frontier_quark_route2_nonlinear_e_center_tensor_observable_gate_2026_06_21.py`: pass
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_nonlinear_e_center_tensor_observable_gate_2026_06_21.py`: `TOTAL: PASS=53, FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_s3_time_bilinear_tensor_primitive.py`: `PASS=4 FAIL=0 TOTAL=4`
- `PYTHONPATH=scripts python3 scripts/frontier_s3_time_bilinear_tensor_primitive_rank1_factorization.py`: `PASS=11 FAIL=0 TOTAL=11`
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_qe_covariance_schur_quadratic_no_go_2026_06_14.py`: `PASS=11 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_exact_readout_map.py`: `PASS=11 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_s3_time_theta_to_slice_coupling.py`: `PASS=12 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_s3_time_constructed_support_tensor_primitive.py`: `PASS=7 FAIL=0 TOTAL=7`
- `PYTHONPATH=scripts python3 scripts/frontier_tensor_support_center_excess_law.py`: `PASS=5 FAIL=0 TOTAL=5`

## Review Notes

- Branch-local self-review disposition: pass.
- No observed masses, fitted endpoint values, CKM/J targets, nearest-rational proof inputs, or `N=15` proof selection are consumed.
- No repo-wide authority surfaces are edited.
