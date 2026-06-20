# Artifact Plan

Artifacts touched:

- `docs/CAUSAL_IMPACT_PARAMETER_NOTE.md`
- `scripts/causal_impact_parameter_probe.py`
- `logs/runner-cache/causal_impact_parameter_probe.txt`
- generated audit data and rendered audit/publication/front-door status files
- `logs/runner-cache/audit_packet_script_deps.txt`

The runner regenerates the source note, so the source metadata repair is made
in the runner first and then materialized into the markdown note and cache.

