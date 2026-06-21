# Artifact Plan

## Delivered

- Add a typed-edge cut certificate note.
- Add a runner that checks graph reachability, equivalent discharge edges,
  weak additions, and the two-edge scalarization split.
- Capture runner output in `outputs/`.
- Package one review PR.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_source_domain_typed_edge_cut_certificate_2026_06_21.py
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_source_domain_bridge_no_go.py
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_rconn_typed_bridge_derivation_bounded_2026_06_12.py
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_e_center_lift_derivation_attempt_bounded_2026_06_12.py
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_exact_readout_map.py
python3 -m py_compile scripts/frontier_quark_route2_source_domain_typed_edge_cut_certificate_2026_06_21.py
git diff --check
```
