# Route Portfolio

1. Register the existing DM selector branch verifier.
   - Action: add `Runner:` metadata to the source note and regenerate audit surfaces.
   - Outcome: selected and completed.

2. Rewrite or strengthen the verifier.
   - Action: broaden assertions in `scripts/frontier_dm_selector_branch_conclusion.py`.
   - Outcome: rejected for this block. The existing verifier already checks the note's load-bearing obstruction spine and exits `PASS=17 FAIL=0`.

3. Attempt a status promotion.
   - Outcome: rejected. This block is not an audit and does not change `audit_status` or `effective_status`.

