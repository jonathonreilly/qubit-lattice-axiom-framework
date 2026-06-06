# Summary

Repairs the active `dimension_selection_note` packet-completeness blocker by inlining source-packet checks into the primary parent runner.

The audit blocker was not a physics disproof; it asked for the finite-k bridge source, original dimension runner source/cache, and source-packet verifier/cache to be inspectable from code. The parent runner now verifies those artifacts directly and reports `SUMMARY: PASS=81 FAIL=0`.

# Scope

This is exact support for a source-packet blocker. It does not retag the audit ledger, does not prove full D3 dimension selection, and does not authorize a framework-baseline rewrite.

# Verification

```bash
python3 -m py_compile scripts/frontier_dimension_selection_lower_bound_parent_repair.py scripts/dimension_selection_parent_source_packet_manifest_2026_06_05.py scripts/frontier_d3_lower_bound_source_packet_gate_2026_06_06.py
PYTHONPATH=scripts python3 scripts/cached_runner_output.py --check-only scripts/frontier_dimension_selection_lower_bound_parent_repair.py
PYTHONPATH=scripts python3 scripts/cached_runner_output.py --check-only scripts/dimension_selection_parent_source_packet_manifest_2026_06_05.py
PYTHONPATH=scripts python3 scripts/cached_runner_output.py --check-only scripts/frontier_d3_lower_bound_source_packet_gate_2026_06_06.py
git diff --check
```
