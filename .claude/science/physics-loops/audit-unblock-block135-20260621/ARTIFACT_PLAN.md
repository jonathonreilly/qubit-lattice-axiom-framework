# Artifact Plan

- Update `docs/audit/scripts/build_citation_graph.py` so links under
  `## Cross-references (non-load-bearing)` are excluded from citation edges.
- Implement `scripts/source_graph_repair_pass.py --apply` so live cycle links
  become backticked non-live references in place and original links are copied
  into the non-load-bearing cross-reference section.
- Add focused regression tests.
- Verify with unit tests, dry-run output, py_compile, and diff check.
