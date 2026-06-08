# Route Portfolio

## Selected Route: Primary Verifier Consumes Recompute Artifact

Keep the default frozen-log regression check, but add SHA/header/row-gate validation of the live recompute cache and update the note table to the exact recompute values.

Outcome: implemented.

## Rejected Route: Replace Default With Live Recompute

The live recompute path takes about 100 seconds. Keeping it as a SHA-fresh dependency gives the auditor completed evidence without making every default run slow.

Outcome: rejected.

## Rejected Route: Claim Wider Basin

The audited row is only the three restore values at seed 0 and drift 0.2.

Outcome: rejected.
