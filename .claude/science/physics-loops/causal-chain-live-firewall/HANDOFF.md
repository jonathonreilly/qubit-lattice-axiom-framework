# Handoff

This PR narrows `docs/CAUSAL_FIELD_CANONICAL_CHAIN_NOTE.md` from a
package-retained-style chain to a bounded source-firewall map. It adds the
live causal-packet firewall cache and strengthens the firewall runner so the
old stale causal-propagating-field table and package-retained phrases do not
re-enter this live chain map.

Checks run:

- `python3 scripts/causal_field_live_packet_reference_firewall_2026_06_16.py`
- `python3 scripts/cached_runner_output.py scripts/causal_field_live_packet_reference_firewall_2026_06_16.py --refresh`
- `python3 -m py_compile scripts/causal_field_live_packet_reference_firewall_2026_06_16.py`

No audit loop was run, no audit data was edited, and no main landing was done.
The reviewer should decide whether this source demotion is enough to queue
`causal_field_canonical_chain_note` for re-audit.
