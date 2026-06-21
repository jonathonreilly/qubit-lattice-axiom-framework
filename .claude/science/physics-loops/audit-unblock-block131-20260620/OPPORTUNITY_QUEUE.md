# Opportunity Queue

1. Open block131 PR for referenced-cache cleanup safety.
   - status: done locally, PR pending.
   - trace class: methodology.
   - reason: prevents orphan cleanup from creating broken evidence links.

2. Monitor block128, block129, block130, and block131 audit-lane checks.
   - status: pending.
   - reason: stacked PRs need green CI before review.

3. Review the 8 remaining orphan-cache candidates in a later block.
   - status: pending.
   - reason: after header and reference guards, these are narrower cleanup
     candidates.

4. Continue source-side audit unblock work from runner/cache or dispatch
   tooling surfaces.
   - status: pending.
   - reason: user requested an ongoing PR-producing unblock campaign.
