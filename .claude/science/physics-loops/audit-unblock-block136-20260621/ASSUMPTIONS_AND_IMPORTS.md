# Assumptions And Imports

- The strippable edge list comes from `docs/audit/data/audit_queue.json`.
- Links moved by `scripts/source_graph_repair_pass.py --apply` remain readable
  as non-load-bearing cross-references.
- `docs/audit/scripts/build_citation_graph.py` from block135 ignores links
  under `## Cross-references (non-load-bearing)`.
- No audit verdict is inferred from this source-graph repair.
