# Handoff

## What Changed

This branch repairs the hierarchy species-count no-go by making the load-bearing claim abstract:

```text
F(R) = C * alpha^N_species(R)
```

with fixed nonzero `C` and fixed positive `alpha != 1`. If two species-count readouts differ, the bridge is regulator-dependent unless O1/O2/O3 supplies a regulator/substrate-specific target.

The standard regulator table B1/B2 remains as witness/context, not authority. The staggered realization gate is named only as possible O1/O2 context and is not linked as a markdown dependency.

## Verification

- `PYTHONPATH=scripts python3 scripts/frontier_hierarchy_alpha_lm_exponent_species_count_bridge_regulator_dependence_no_go.py`
  - `TOTAL: PASS=15 FAIL=0`
- `python3 scripts/precompute_audit_runners.py --runners scripts/frontier_hierarchy_alpha_lm_exponent_species_count_bridge_regulator_dependence_no_go.py --force --concurrency 1 --push-mode none --allow-non-main`
  - `ok 1`, `nonzero_exit 0`
- `git diff --check`
  - clean

## Boundaries

- No ledger edits.
- No registry edits.
- No audit verdict/status assertion.
- Does not derive B1/B2.
- Does not close the staggered realization gate.

