# Artifact Plan

## Source Artifacts

- `docs/audit/scripts/build_citation_graph.py`
  - Detect literal dynamic helper loads through `load_frontier`.
  - Preserve existing static import parsing.
- `docs/audit/scripts/tests/test_audit_pipeline.py`
  - Add regression coverage for positional and keyword filename forms.

## Generated Artifacts

Pipeline regeneration updates:

- `docs/audit/AUDIT_LEDGER.md`
- `docs/audit/AUDIT_QUEUE.md`
- `docs/audit/AUDIT_DISPATCH_QUEUE.md`
- `docs/audit/data/*.json`
- `docs/publication/ci3_z3/*_EFFECTIVE_STATUS.md`
- `docs/repo/FRONT_DOOR_STATUS.md`
- `logs/runner-cache/audit_packet_script_deps.txt`

Generated current-main stale invalidations are pipeline outputs, not
hand-authored verdict changes.
