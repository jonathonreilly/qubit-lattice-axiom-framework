# Opportunity Queue

1. Runtime runner-breakage staleness guard: done in this branch.
2. Reviewer/auditor can use the guard output to clear stale `timeout` and
   `nonzero_exit` blockers.
3. Missing runner path blockers remain covered by the separate path
   canonicalization PR.
4. Active audited conditionals remain science/review targets already represented
   by open PRs; no branch refresh is attempted here.
5. Remaining hard science work should target conditionals not covered by open
   PRs after the next audit batch lands.
