# Assumptions And Imports

- The generated audit surfaces are derived from current source notes and
  audit scripts on `origin/main`.
- Existing audit scripts own invalidation of stale audit snapshots caused by
  note hash drift.
- Runner paths are imported from source-note metadata extracted by
  `build_citation_graph.py`; no runner path was hand-authored into the
  ledger.
- Independent audit remains the only authority for verdicts and retained
  status.

No physics premise, observed value, literature value, fitted selector, or new
axiom is introduced by this block.
