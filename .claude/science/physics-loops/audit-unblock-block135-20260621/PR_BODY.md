## Summary

Enables the source-graph cycle repair workflow without applying any audit
verdicts or source-note rewrites in this PR.

Stacking note: this PR is based on block134 so follow-up cycle-repair apply
work inherits the current audit-support refresh stack instead of duplicating it.

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
unrelated audit-support churn. The follow-up source repair should be done after
the support-refresh stack settles or on a base that keeps that diff narrow.

## Verification

- `python3 -m unittest docs.audit.scripts.tests.test_audit_pipeline.BuildCitationGraphParserTest docs.audit.scripts.tests.test_audit_pipeline.SourceGraphRepairPassTest docs.audit.scripts.tests.test_audit_pipeline.PrecomputeAuditRunnersTest` -> 11 tests passed
- `python3 -m unittest docs.audit.scripts.tests.test_audit_pipeline` -> 83 tests passed
- `python3 -m py_compile docs/audit/scripts/build_citation_graph.py scripts/source_graph_repair_pass.py docs/audit/scripts/tests/test_audit_pipeline.py` -> OK
- `python3 scripts/source_graph_repair_pass.py` -> dry-run complete; 9 cycles, 9 source notes, 9 live links found
- `python3 scripts/precompute_audit_runners.py --all --check-only --allow-non-main` -> `fresh: 3123`, `stale to refresh: 0`, `missing on disk: 0`
- `git diff --check` -> OK
