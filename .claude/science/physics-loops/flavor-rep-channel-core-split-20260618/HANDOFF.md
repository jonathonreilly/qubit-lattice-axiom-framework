# Handoff

## Claim-State Movement

This branch splits the retained-native generation-uniform scalar-action core
from the conditional SM sector-representation layer in the flavor
gauge-representation no-go.

The branch does not derive the SM sector representation assignment,
hypercharge/T3, right-handed representation data, physical sector readout, or
within-sector measure.

## Checks

```bash
python3 -m py_compile scripts/flavor_gauge_representation_generation_uniform_core_2026_06_18.py
python3 scripts/flavor_gauge_representation_generation_uniform_core_2026_06_18.py
python3 scripts/cached_runner_output.py --check-only scripts/flavor_gauge_representation_generation_uniform_core_2026_06_18.py
python3 scripts/frontier_gauge_rep_channel_cannot_source_spread_2026_06_15.py
python3 scripts/cached_runner_output.py --check-only scripts/frontier_gauge_rep_channel_cannot_source_spread_2026_06_15.py
git diff --check
```

## Review

Review-loop was not run here because the user delegated review-loop and
landing cleanup to the Codex reviewer.

## PR

Pending.
