# Summary

This PR splits the safe fractional-instanton action algebra core from the
audited-conditional external dilute-gas/condensate parent row.

It does not close the dilute-gas mechanism, condensate formation, framework
substrate, or hierarchy observable bridges.

# Science Movement

- Adds a bounded support note deriving
  `S_frac(k,N) = (8*pi^2/g^2)|k/N|` from the retained-bounded topological
  instanton infrastructure.
- Adds a runner/cache checking retained-bounded dependency status, exact
  fractional action arithmetic, canonical parent-table numerics, and status
  firewalls.
- Updates the parent note to cite the action-core split while preserving the
  open determinant/measure/coupling-scale/convergence blockers.

# Checks

```bash
python3 -m py_compile scripts/fractional_instanton_action_core_split_2026_06_18.py
python3 scripts/fractional_instanton_action_core_split_2026_06_18.py
python3 scripts/cached_runner_output.py --check-only scripts/fractional_instanton_action_core_split_2026_06_18.py
python3 scripts/frontier_fractional_instanton_dilute_gas_condensate_external_narrow.py
python3 scripts/cached_runner_output.py --check-only scripts/frontier_fractional_instanton_dilute_gas_condensate_external_narrow.py
git diff --check
```

All checks passed locally.

# Review

Review-loop not run; user delegated review-loop and landing cleanup to Codex
reviewer.
