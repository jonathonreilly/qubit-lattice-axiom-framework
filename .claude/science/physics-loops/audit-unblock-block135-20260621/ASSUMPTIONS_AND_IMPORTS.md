# Assumptions And Imports

- The audit queue already names cycle-break targets and co-cycle citations.
- Non-load-bearing cross-references may remain readable in source notes, but
  should not count as citation-graph dependency edges.
- `scripts/source_graph_repair_pass.py --apply` must be deterministic and
  branch-local.
- Audit verdicts and effective status movement remain owned by the audit lane.
