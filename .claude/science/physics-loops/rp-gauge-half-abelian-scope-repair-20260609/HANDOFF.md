# Handoff

This repair addresses the RP gauge-half bridge conditional by choosing the
auditor's abelian restriction path.

Changed files:

- `docs/RP_GAUGE_HALF_WILSON_TEMPORAL_BRIDGE_NARROW_THEOREM_NOTE_2026-06-06.md`
- `scripts/frontier_rp_gauge_half_wilson_temporal_bridge.py`
- `logs/runner-cache/frontier_rp_gauge_half_wilson_temporal_bridge.txt`

Reviewer focus:

- Confirm the theorem now claims W1-W3 only for exact abelian `Z_N`/`U(1)`.
- Confirm SU(2)/SU(3) are diagnostics only and cannot be read as retained
  nonabelian reconstruction.
- Confirm the runner exposes the old SU(2) product-character mismatch.
- Confirm no audit ledger/result files are changed.
