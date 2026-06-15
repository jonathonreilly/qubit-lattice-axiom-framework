# Handoff

This PR is source hygiene for the complete-chain audit lane.

What changed:

- Bare `frontier_*.py` references in the complete-chain note now use
  `scripts/...` repo paths.

What did not change:

- No runner source changed.
- No runner cache changed.
- No generated audit data or audit verdict files changed.
- No claim status promotion is proposed.

Verification:

```sh
rg --pcre2 -n "(?<!scripts/)frontier_[a-z0-9_]+\\.py" docs/COMPLETE_PREDICTION_CHAIN_2026_04_15.md || true
python3 scripts/cached_runner_output.py --check-only scripts/frontier_complete_prediction_chain.py
python3 scripts/frontier_complete_prediction_chain.py
git diff --check
```
