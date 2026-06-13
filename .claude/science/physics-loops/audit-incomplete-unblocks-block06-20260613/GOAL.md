# Goal

Continue draining incomplete audit status rows after the audited-conditional
repair campaign.

This block targets source-side gaps that remained uncovered after PR #3825:
five retained-pending-chain rows and one critical open-gate row with no primary
runner. It does not apply audit verdicts.
