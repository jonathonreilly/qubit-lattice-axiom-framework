# Artifact Plan

Artifacts touched:

- `docs/QCD_LOW_ENERGY_RUNNING_BRIDGE_NOTE_2026-05-01.md`
- `scripts/frontier_qcd_low_energy_running_bridge.py`
- `logs/runner-cache/frontier_qcd_low_energy_running_bridge.txt`
- generated audit data and rendered audit/publication/front-door status files
- `logs/runner-cache/audit_packet_script_deps.txt`

The source change is intentionally narrow: add `Claim type: bounded_theorem`
and require it in the paired runner's manifest-sync section.

