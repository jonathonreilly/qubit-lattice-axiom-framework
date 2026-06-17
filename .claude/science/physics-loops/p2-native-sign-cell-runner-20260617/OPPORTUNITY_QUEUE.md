# Opportunity Queue

This block is intentionally scoped to one coherent repair. Broader campaign
selection remains outside this PR.

| Rank | Candidate | Reason | Next action |
|---:|---|---|---|
| 1 | P2 sign-epsilon runner/import repair | Current runner was locally failing against C-Sc wording; textbook imports can be retired by exact finite checks | Complete this PR |
| 2 | Other current-main runner failures | Directly unlocks audit queue without retagging ledger rows | Scan after this PR if campaign continues |
| 3 | Other textbook-import rows with finite native runners | Matches repo policy: prove local finite math, cite external texts only in parallel | Select only where a concrete load-bearing import is named |
| 4 | Hard bridge-science rows | Potentially high impact but more open-ended | Use physics-loop stretch/fan-out only after concrete blocker selection |

Do not spend campaign time keeping existing PRs fresh against main unless a
reviewer asks for a specific branch update.
