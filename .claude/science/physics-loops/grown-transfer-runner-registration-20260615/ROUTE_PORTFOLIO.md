# Route Portfolio

1. Source registration route: add an explicit primary-runner label to the note.
   This is the selected route.
2. Audit-data edit route: manually patch `audit_ledger.json` or
   `citation_graph.json`. Rejected because audit/generated verdict surfaces
   should not be committed in a science repair PR.
3. New runner route: write another wrapper runner. Rejected because the current
   targeted runner and caches are already fresh.
