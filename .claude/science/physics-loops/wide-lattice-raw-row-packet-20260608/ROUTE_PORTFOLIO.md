# Route Portfolio

## Route A: Full Recompute Artifact

Possible but slower. The frozen log already has a valid SHA and raw rows.

## Route B: Raw-Row Inclusion

Chosen. The audit blocker explicitly allowed raw-row inclusion or equivalent
completed recompute. This branch embeds the raw rows in the source note and
checks them mechanically.
