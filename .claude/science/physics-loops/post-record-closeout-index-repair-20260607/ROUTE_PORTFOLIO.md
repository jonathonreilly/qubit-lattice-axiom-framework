# Route Portfolio

## Route A: direct source packet repair

Use the existing runner's dependency stack as the source of truth, correct the
stale PASS counts in the note, add explicit authority references, regenerate
the packet, and leave audit judgment to the auditor.

Disposition: executed.

## Route B: runner rewrite

Rewrite the runner dependency expectations from scratch.

Disposition: rejected as unnecessary; the existing runner already encodes the
correct PASS=64/PASS=52 expectations and passed after note repair.

## Route C: audit ledger retag

Directly update the audit ledger row.

Disposition: forbidden for this PR; the science branch must queue re-audit by
repairing source artifacts only.
