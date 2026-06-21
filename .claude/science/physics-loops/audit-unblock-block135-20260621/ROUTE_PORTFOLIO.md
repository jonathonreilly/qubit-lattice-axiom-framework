# Route Portfolio

1. Implement citation-graph skip logic for a standard non-load-bearing
   cross-reference section.
   - Selected.
   - Reason: without this, moving links into the section would still leave
     cycle edges live.

2. Implement `source_graph_repair_pass.py --apply`.
   - Selected.
   - Reason: the tool already plans repairs but cannot execute them.

3. Apply source-note cycle repairs in the same PR.
   - Deferred.
   - Reason: exploratory pipeline regeneration on bare `origin/main` mixed in a
     broad unrelated support-surface refresh, including 55 hard resets.
