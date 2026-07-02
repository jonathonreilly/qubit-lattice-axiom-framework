# Artifact Plan

## Produced

- `scripts/frontier_quark_route2_nonlinear_tensor_observable_class_no_go_2026_06_21.py`
- `outputs/frontier_quark_route2_nonlinear_tensor_observable_class_no_go_2026_06_21.txt`
- `docs/QUARK_ROUTE2_NONLINEAR_TENSOR_OBSERVABLE_CLASS_NO_GO_NOTE_2026-06-21.md`
- branch-local loop pack under this directory

## Verification Plan

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_nonlinear_tensor_observable_class_no_go_2026_06_21.py
python3 -m py_compile scripts/frontier_quark_route2_nonlinear_tensor_observable_class_no_go_2026_06_21.py
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_e_center_blindness_no_go.py
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_qe_covariance_schur_quadratic_no_go_2026_06_14.py
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_e_channel_readout_naturality_no_go.py
PYTHONPATH=scripts python3 scripts/frontier_s3_time_theta_to_slice_coupling_factor_rigidity.py
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_exact_readout_map.py
```

Then run diff and overclaim gates before commit.
