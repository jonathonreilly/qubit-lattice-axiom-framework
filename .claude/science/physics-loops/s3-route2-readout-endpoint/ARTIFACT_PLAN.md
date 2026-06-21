# Artifact Plan

## Delivered In Block21

- Add a note classifying safe and E-center-dependent direct consumers.
- Add a runner that checks parent anchors, exact carrier ranks, subspace
  dependence, and consumer inventory.
- Capture runner output in `outputs/`.
- Package the result for one review PR.

## Verification Plan

Run the new classifier plus focused parent checks:

```bash
PYTHONPATH=scripts python3 scripts/frontier_s3_time_direct_consumer_ecenter_dependency_classification_2026_06_21.py
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_e_center_blindness_no_go.py
PYTHONPATH=scripts python3 scripts/frontier_s3_time_primitive_chain_reaudit.py
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_exact_readout_map.py
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_exact_time_coupling.py
python3 -m py_compile scripts/frontier_s3_time_direct_consumer_ecenter_dependency_classification_2026_06_21.py
git diff --check
```
