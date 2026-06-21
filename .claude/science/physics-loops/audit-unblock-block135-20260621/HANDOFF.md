# Handoff

## Summary

Block135 makes the source-graph cycle repair workflow executable:

- `build_citation_graph.py` now ignores markdown links inside
  `## Cross-references (non-load-bearing)`.
- `source_graph_repair_pass.py --apply` now deactivates live cycle links by
  replacing them inline with backticked references and copying the original
  live links into that skipped cross-reference section.
- tests cover both behaviors.

The live dry-run after rebasing onto `origin/main` at `dea100014` reports:

- cycles named: 8
- unique source notes: 4
- total cycle edges to process: 12
- live markdown links found: 2
- missing/not-found planned links: 10

## Boundary

No source-note repair is applied in this PR. No audit verdicts, ledger rows, or
publication status surfaces are hand-edited.

An exploratory apply plus full pipeline regeneration before the final rebase was
discarded because it mixed this tooling change with broad unrelated
audit-support churn. The final branch intentionally keeps only tooling/tests.

## Verification

- `python3 -m unittest docs.audit.scripts.tests.test_audit_pipeline.BuildCitationGraphParserTest docs.audit.scripts.tests.test_audit_pipeline.SourceGraphRepairPassTest` -> 7 tests passed.
- `python3 -m unittest docs.audit.scripts.tests.test_audit_pipeline` -> 79 tests passed.
- `python3 -m py_compile docs/audit/scripts/build_citation_graph.py scripts/source_graph_repair_pass.py docs/audit/scripts/tests/test_audit_pipeline.py` -> OK.
- `python3 scripts/source_graph_repair_pass.py` -> dry-run complete.
- `python3 scripts/precompute_audit_runners.py --pr-diff origin/main --check-only --allow-non-main` -> `fresh: 0`, `stale to refresh: 0`, `missing on disk: 0`.
- `git diff --check` -> OK.

## Next Exact Action

Monitor PR #4505 after the current-main rebase. If it stays clean, rebase the
follow-up source-note repair PR on top of this tooling branch.

## PR

- https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/4505
