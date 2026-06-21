# Handoff

## Summary

Block135 makes the source-graph cycle repair workflow executable:

- `build_citation_graph.py` now ignores markdown links inside
  `## Cross-references (non-load-bearing)`.
- `source_graph_repair_pass.py --apply` now deactivates live cycle links by
  replacing them inline with backticked references and copying the original
  live links into that skipped cross-reference section.
- tests cover both behaviors.

The live dry-run on the current stacked base reports:

- cycles named: 9
- unique source notes: 9
- total cycle edges to process: 10
- live markdown links found: 9
- missing/not-found planned links: 1

## Boundary

No source-note repair is applied in this PR. No audit verdicts, ledger rows, or
publication status surfaces are hand-edited.

An exploratory apply plus full pipeline regeneration before the final rebase was
discarded because it mixed this tooling change with broad unrelated
audit-support churn. The final branch intentionally keeps only tooling/tests.

## Verification

- `python3 -m unittest docs.audit.scripts.tests.test_audit_pipeline.BuildCitationGraphParserTest docs.audit.scripts.tests.test_audit_pipeline.SourceGraphRepairPassTest docs.audit.scripts.tests.test_audit_pipeline.PrecomputeAuditRunnersTest` -> 11 tests passed.
- `python3 -m unittest docs.audit.scripts.tests.test_audit_pipeline` -> 83 tests passed.
- `python3 -m py_compile docs/audit/scripts/build_citation_graph.py scripts/source_graph_repair_pass.py docs/audit/scripts/tests/test_audit_pipeline.py` -> OK.
- `python3 scripts/source_graph_repair_pass.py` -> dry-run complete.
- `python3 scripts/precompute_audit_runners.py --all --check-only --allow-non-main` -> `fresh: 3123`, `stale to refresh: 0`, `missing on disk: 0`.
- `git diff --check` -> OK.

## Next Exact Action

Monitor PR #4505. After the support-refresh stack lands or can be used as a
base, create a follow-up source-note repair PR that runs `--apply` and
regenerates the pipeline with a narrow diff.

## PR

- https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/4505
