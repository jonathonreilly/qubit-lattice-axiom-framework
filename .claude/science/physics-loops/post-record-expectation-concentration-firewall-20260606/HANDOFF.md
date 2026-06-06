# Handoff

## Summary

This block proves a finite no-go for the route from expected post-record
frequencies to concentration, p-values, or audit calibration.

The two supplied laws on four post-record events have the same expected counts
and the same fair one-time marginals, but different extreme-tail probabilities:

```text
iid fair:        P(|count_A-count_B| = 4) = 1/8
correlated fair: P(|count_A-count_B| = 4) = 1
```

The same observed word `AAAA` therefore receives different p-values under the
two laws.

## Meaning

Post-record states carry realized information/counts. Expected frequencies are
ensemble summaries under a supplied pre-record or null law. They do not replace
the finite law needed for calibrated p-values or audit decisions.

## What it unlocks

- Prevents overclaiming expectation formulas as audit calibration.
- Clears a cleaner interface for exact finite null audits: supply the law,
  statistic, and threshold.
- Clears a separate conditional concentration interface: supply dependence
  hypotheses or an explicit theorem.
- Keeps stable dial language honest: a stable location can be certified under a
  supplied score/rule/law, but the dial is not forced by expected frequency.

## Files

- `docs/POST_RECORD_EXPECTATION_CONCENTRATION_FIREWALL_2026-06-06.md`
- `scripts/frontier_post_record_expectation_concentration_firewall_2026_06_06.py`
- `logs/runner-cache/frontier_post_record_expectation_concentration_firewall_2026_06_06.txt`
- `.claude/science/physics-loops/post-record-expectation-concentration-firewall-20260606/`

## Next exact action

Commit, push, open the PR, record PR status, then pivot to the next independent
dynamics lane.
