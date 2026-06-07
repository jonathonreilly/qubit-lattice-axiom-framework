# Handoff

This PR repairs operational reproducibility for the linear-response heuristic
row.

The default runner now:

- parses all 44 rows in `logs/2026-04-07-linear-response-derivation.txt`;
- recomputes the overall and by-group Pearson correlations;
- recomputes sign agreement, no-fit classification, best in-sample threshold,
  and measured-response ceiling;
- confirms the verdict remains moderate/open.

The live full computation remains available with `--recompute`.

No audit verdicts are changed.
