# Handoff

Branch: `codex/hierarchy-d4-bridge-native-endpoints-20260618`

This source-side PR hardens the hierarchy D4 density-scale bridge by replacing
a live endpoint-note audit-status dependency with local APBC endpoint
coefficient checks. On clean `origin/main`, the old bridge runner failed
because `hierarchy_effective_potential_endpoint_note` was `unaudited`; the new
runner passes while reporting that status as context only.

Checks run:

```bash
python3 scripts/frontier_hierarchy_d4_density_scale_readout_bridge_2026_06_16.py
python3 scripts/frontier_hierarchy_dimensional_compression_taste_authority_2026_06_15.py
python3 scripts/cached_runner_output.py --refresh scripts/frontier_hierarchy_d4_density_scale_readout_bridge_2026_06_16.py
python3 scripts/cached_runner_output.py --refresh scripts/frontier_hierarchy_dimensional_compression_taste_authority_2026_06_15.py
```

Expected reviewer focus:

- confirm no audit ledger/status/publication files are edited;
- confirm endpoint ratios are genuinely computed in the D4 bridge runner;
- confirm no physical VEV/order-parameter closure is claimed.

Remaining blocker:

The physical electroweak order-parameter/VEV identification and endpoint
surface selection are still open frontier science.
