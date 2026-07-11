# Artifact Plan

1. Record the full 12-row default and 24-row strict-lane inventories in the
   source note.
2. Compare both tables exactly to live runner output.
3. Verify that strict-lane retains the eight default required rows in order,
   removes the four default optional hooks, and adds only
   `required-if-present` rows.
4. Refresh the SHA-pinned runner cache and run compile/diff checks.
5. Apply review-loop backpressure, record that current audit policy excludes
   meta rows from ordinary verdict-bearing queues, and leave audit-owned state
   unchanged.
