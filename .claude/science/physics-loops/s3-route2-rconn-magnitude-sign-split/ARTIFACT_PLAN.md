# Artifact Plan

Block52 deliverables:

- theorem note:
  `docs/QUARK_ROUTE2_RCONN_MAGNITUDE_SIGN_SPLIT_EXACT_SUPPORT_NOTE_2026-06-21.md`
- runner:
  `scripts/frontier_quark_route2_rconn_magnitude_sign_split_2026_06_21.py`
- output:
  `outputs/frontier_quark_route2_rconn_magnitude_sign_split_2026_06_21.txt`
- loop pack:
  `.claude/science/physics-loops/s3-route2-rconn-magnitude-sign-split/`

Verification plan:

```text
python3 scripts/frontier_quark_route2_rconn_magnitude_sign_split_2026_06_21.py
python3 -m py_compile scripts/frontier_quark_route2_rconn_magnitude_sign_split_2026_06_21.py
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_source_domain_bridge_no_go.py
PYTHONPATH=scripts python3 scripts/frontier_route2_readout_record_positivity_no_go.py
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_exact_readout_map.py
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_e_center_lift_derivation_attempt_bounded_2026_06_12.py
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_e_channel_readout_naturality_no_go.py
git diff --check
```
