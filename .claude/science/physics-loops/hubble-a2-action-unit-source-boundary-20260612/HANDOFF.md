# Handoff

This branch repairs the Hubble Lane 5 C1 A2 action-unit metrology source.

Science result:

- preserve the A2 no-go: supplied dimensionless inputs do not select
  dimensional `kappa`;
- remove stale retained-authority wording for `g_bare = 1`;
- route the staggered-carrier dependency through registered target
  `AC_phi_lambda`;
- leave the real missing bridge explicit: a physical clock/source/action
  metrology theorem.

Verification:

```text
PYTHONPATH=scripts python3 scripts/frontier_hubble_lane5_c1_a2_action_unit_metrology_obstruction.py
# TOTAL: PASS=16, FAIL=0

python3 scripts/precompute_audit_runners.py --runners scripts/frontier_hubble_lane5_c1_a2_action_unit_metrology_obstruction.py --allow-non-main
# ok 1, nonzero_exit 0
```

No audit ledger/result files were edited.
