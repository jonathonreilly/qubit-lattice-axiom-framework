# Artifact Plan

## Delivered

- Add a sign-support/typecast-remainder note.
- Add a runner checking parent anchors, sign support over positive-lift
  samples, magnitude non-uniqueness, and inventory wording.
- Capture runner output in `outputs/`.
- Package one review PR.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_source_domain_sign_support_typecast_remainder_2026_06_21.py
PYTHONPATH=scripts python3 scripts/frontier_route2_readout_record_positivity_no_go.py
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_e_channel_readout_naturality_no_go.py
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_exact_readout_map.py
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_source_domain_bridge_no_go.py
python3 -m py_compile scripts/frontier_quark_route2_source_domain_sign_support_typecast_remainder_2026_06_21.py
git diff --check
```
