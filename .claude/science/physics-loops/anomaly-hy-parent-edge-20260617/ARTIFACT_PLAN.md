# Artifact Plan

1. Update `docs/ANOMALY_FORCES_TIME_THEOREM.md` so HY-surface cites
   `GRAPH_FIRST_SU3_INTEGRATION_NOTE.md` as the load-bearing source.
2. Remove the old split-out abelian-surface slug from the parent theorem text.
3. Remove the old prior single-clock source slug from parent theorem context.
4. Add runner checks to `scripts/frontier_anomaly_forces_time.py` that enforce:
   graph-first HY authority, absence of the split-out slug from the parent
   theorem text, absence of the single-clock slug from the parent theorem text,
   and unchanged P-HY declared-premise status.
5. Refresh `logs/runner-cache/frontier_anomaly_forces_time.txt`.
6. Run focused verification, commit, push, and open a ready PR for reviewer
   extraction.
