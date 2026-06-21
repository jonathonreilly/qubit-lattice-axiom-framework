# Artifact Plan

- Apply `scripts/source_graph_repair_pass.py --apply`.
- Regenerate the audit pipeline with `bash docs/audit/scripts/run_pipeline.sh`.
- Confirm post-apply dry-run reports zero remaining cycle edges.
- Verify strict lint, full runner-cache freshness, tests, py_compile, and
  whitespace.
