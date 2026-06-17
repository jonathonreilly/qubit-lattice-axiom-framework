# Opportunity Queue

1. Source-cycle false-edge repair, current branch. Directly targets
   `cycles_detected=6` without changing verdicts.
2. Single-clock B-AXIS route. Already covered by open PR #4221 / #4228, so no
   freshness work here.
3. Remaining audited conditionals after graph repair. Re-evaluate after the
   independent audit rebuilds the graph.
