## Summary

Enables the source-graph cycle repair workflow without applying any audit
verdicts or source-note rewrites in this PR.

Base note: this PR is now rebased directly on `main` at `678b38ce7`.

Changes:

- `build_citation_graph.py` skips links under
  `## Cross-references (non-load-bearing)`.
- `source_graph_repair_pass.py --apply` is implemented: it replaces live cycle
  links inline with backticked non-live references and copies the original
  links into the skipped cross-reference section.
- regression tests cover graph skipping and apply behavior.

## Boundary

This is tooling-only. It does not audit claims, apply verdicts, edit ledger
rows by hand, or assert retained/proposed-retained status.

I did not keep source-note apply output in this branch because an exploratory
apply plus full pipeline regeneration mixed the tooling change with broad
unrelated audit-support churn. The follow-up source repair should be done as a
separate PR on top of this tooling branch so reviewers can isolate the
source-note and generated-surface diff.

## Verification

- `python3 -m unittest docs.audit.scripts.tests.test_audit_pipeline.BuildCitationGraphParserTest docs.audit.scripts.tests.test_audit_pipeline.SourceGraphRepairPassTest` -> 7 tests passed
- `python3 -m unittest docs.audit.scripts.tests.test_audit_pipeline` -> 79 tests passed
- `python3 -m py_compile docs/audit/scripts/build_citation_graph.py scripts/source_graph_repair_pass.py docs/audit/scripts/tests/test_audit_pipeline.py` -> OK
- `python3 scripts/source_graph_repair_pass.py` -> dry-run complete; 8 cycles, 4 source notes, 2 live links found, 10 planned links already absent
- `python3 scripts/precompute_audit_runners.py --pr-diff origin/main --check-only --allow-non-main` -> `fresh: 0`, `stale to refresh: 0`, `missing on disk: 0`
- `git diff --check` -> OK
