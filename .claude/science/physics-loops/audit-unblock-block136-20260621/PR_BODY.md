## Summary

Applies the source-graph repair workflow introduced in block135.

The PR moves audit-queue-named non-load-bearing cycle links from live markdown
dependency positions into `## Cross-references (non-load-bearing)` sections,
then regenerates the deterministic audit graph/queue/status surfaces.

Result:

- cycle inventory: 8 -> 0 on the current block135 base
- ready queue entries: 117
- pending audits: 1694
- first pipeline pass hard resets: 72 stale audit invalidations from current-main hash drift
- second pipeline pass hard resets: 0
- PR-diff runner cache check: 0 stale, 0 missing
- strict lint: OK with 138 notices

## Boundary

This PR does not audit claims, apply verdicts, hand-edit ledger rows, or assert
retained/proposed-retained status. It only applies source-graph hygiene for
cycle links already represented as non-load-bearing by the audit queue and
regenerates support surfaces. The deterministic pipeline invalidates stale audit
rows whose source-note hashes had drifted on current main; it does not author
new clean verdicts.

## Artifacts

- 10 source notes with moved non-load-bearing cross-references
- `docs/audit/data/citation_graph.json`
- `docs/audit/data/cycle_inventory.json`
- `docs/audit/data/audit_queue.json`
- rendered audit/front-door support surfaces
- `.claude/science/physics-loops/audit-unblock-block136-20260621/HANDOFF.md`
- `.claude/science/physics-loops/audit-unblock-block136-20260621/TRACE_GATE.md`

## Verification

- `python3 scripts/source_graph_repair_pass.py --apply` pass 1 -> 2 source notes changed, 2 live markdown links rewritten
- `bash docs/audit/scripts/run_pipeline.sh` pass 1 -> 3474 rows, 1694 pending, 114 ready, 8 cycles, 72 hard resets; lint OK
- `python3 scripts/source_graph_repair_pass.py --apply` pass 2 -> 8 source notes changed, 11 live markdown links rewritten
- `bash docs/audit/scripts/run_pipeline.sh` pass 2 -> 3474 rows, 1694 pending, 117 ready, 0 cycles, 0 hard resets; lint OK with 138 notices
- `python3 scripts/source_graph_repair_pass.py` -> 0 cycles, 0 edges to process
- `python3 scripts/audit_landscape_snapshot.py` -> 117 of 1694 ready, 0 citation cycles
- `python3 scripts/precompute_audit_runners.py --pr-diff origin/physics-loop/audit-unblock-block135-20260621 --check-only --allow-non-main` -> `fresh: 0`, `stale to refresh: 0`, `missing on disk: 0`
- `python3 docs/audit/scripts/audit_lint.py --strict` -> `OK: no errors`, 138 notices
- `python3 -m unittest docs.audit.scripts.tests.test_audit_pipeline` -> 79 tests passed
- `python3 -m py_compile docs/audit/scripts/build_citation_graph.py scripts/source_graph_repair_pass.py docs/audit/scripts/tests/test_audit_pipeline.py` -> OK
- `git diff --check` -> OK

Known baseline caveat: full-ledger runner-cache check still reports 11 unrelated
stale/corrupt caches on this main lineage; this PR does not edit runner sources
or cache files.
