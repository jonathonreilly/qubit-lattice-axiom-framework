# Handoff

PR: https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/4403

Branch: `codex/hierarchy-ew-order-parameter-readout-20260618`

Commit: `4ead0c230910`

This block adds a source-side hierarchy bridge:

- New note:
  `docs/HIERARCHY_EW_ORDER_PARAMETER_D4_DENSITY_READOUT_BRIDGE_BOUNDED_SUPPORT_NOTE_2026-06-18.md`
- New runner:
  `scripts/frontier_hierarchy_ew_order_parameter_d4_density_readout_bridge_2026_06_18.py`
- Parent wiring:
  `docs/HIERARCHY_DIMENSIONAL_COMPRESSION_NOTE.md`
  and
  `scripts/frontier_hierarchy_dimensional_compression_taste_authority_2026_06_15.py`

Verification before PR:

```bash
python3 scripts/frontier_hierarchy_ew_order_parameter_d4_density_readout_bridge_2026_06_18.py
python3 scripts/frontier_hierarchy_dimensional_compression_taste_authority_2026_06_15.py
python3 scripts/cached_runner_output.py --refresh scripts/frontier_hierarchy_ew_order_parameter_d4_density_readout_bridge_2026_06_18.py
python3 scripts/cached_runner_output.py --refresh scripts/frontier_hierarchy_dimensional_compression_taste_authority_2026_06_15.py
```

Review-loop was not run; the user delegated review-loop and landing cleanup to
the Codex reviewer.

No audit ledger/result/status/publication/lane-registry files were edited.
