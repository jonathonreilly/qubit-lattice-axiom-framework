# Opportunity Queue

1. Open block130 PR for header-aware orphan cleanup safety.
   - status: done locally, PR pending.
   - trace class: methodology.
   - reason: prevents valid nested-runner caches from being deleted.

2. Rebase block128 and dependent PRs after latest `origin/main`.
   - status: pending.
   - reason: latest main advanced with SU3 Casimir runner/cache changes.

3. Review the 9 remaining orphan-cache dry-run candidates in a later block.
   - status: pending.
   - reason: cleanup is now safer, but deletion still needs a focused review.

4. Continue source-side audit unblock work from runner/cache or dispatch
   tooling surfaces.
   - status: pending.
   - reason: user requested an ongoing PR-producing unblock campaign.
