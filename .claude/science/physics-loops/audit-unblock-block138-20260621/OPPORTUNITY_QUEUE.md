# Opportunity Queue

## Current Ranking After Block138

1. Search for source-side runner failures among high-impact ready rows that
   are not already covered by open PRs.
2. Inspect audit tooling warnings that can be fixed by source code or
   generated target-selection refreshes without applying verdicts.
3. Run focused direct runners or unit tests only; avoid full audit-loop and
   avoid updating existing PR branches solely for `main` drift.

## Skip List

Already-open audit-unblock PR targets should be skipped unless the user asks
for a correction to that PR:

- #4493 dynamic helper runner paths
- #4494 one-parameter shell helper firewall
- #4495 Koide Q-delta citation firewall
- #4496 runner-cache evidence
- #4497 frozen-stars runner-cache evidence
- #4498 full-ledger runner-cache freshness
- #4499 runner-breakage inventory guard
- #4500 through #4506 audit support stack

Reviewer/review-loop owns updating or cherry-picking those branches.
