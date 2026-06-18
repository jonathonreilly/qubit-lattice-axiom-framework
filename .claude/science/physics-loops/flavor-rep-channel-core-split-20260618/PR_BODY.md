# Summary

This PR splits the retained-native generation-uniform scalar-action core from
the conditional SM sector-representation layer in the flavor gauge-representation
no-go.

It does not derive the SM sector representation assignment or close the parent
row.

# Science Movement

- Adds a bounded support note proving that a scalar action on the shared
  retained generation carrier leaves `r=|b|^2/a^2` invariant.
- Adds a runner/cache checking retained dependency status, uniform-scaling
  invariance, non-uniform controls, conditional colour-class counting, and
  parent firewalls.
- Updates the parent no-go to cite the core split while leaving SM
  representation/readout and electroweak splitter channels open.

# Checks

```bash
python3 -m py_compile scripts/flavor_gauge_representation_generation_uniform_core_2026_06_18.py
python3 scripts/flavor_gauge_representation_generation_uniform_core_2026_06_18.py
python3 scripts/cached_runner_output.py --check-only scripts/flavor_gauge_representation_generation_uniform_core_2026_06_18.py
python3 scripts/frontier_gauge_rep_channel_cannot_source_spread_2026_06_15.py
python3 scripts/cached_runner_output.py --check-only scripts/frontier_gauge_rep_channel_cannot_source_spread_2026_06_15.py
git diff --check
```

All checks passed locally.

# Review

Review-loop not run; user delegated review-loop and landing cleanup to Codex
reviewer.
