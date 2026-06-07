# Route Portfolio

1. Increase the live-runner timeout.
   - Rejected as the default route: the row is an open-gate heuristic record
     supported by a frozen completed log, and rerunning the whole 44-family
     battery is unnecessary for audit reproducibility.

2. Add a frozen-log verifier.
   - Selected.
   - Verifies 44 rows, group counts, Pearson correlations, sign agreement,
     classification summaries, and the open-gate verdict boundary.
