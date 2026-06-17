# Handoff

## What Changed

- Demoted the EW cos complement bridge from stale retained/proposed-retained
  theorem language to bounded support.
- Changed the runner so current unaudited/meta/decorated dependency statuses
  are explicit `[BOUNDARY]` gates, not hard failures.
- Converted the stale YT_EW bare-coupling literal miss into a boundary gate
  while preserving the historical value-level arithmetic as bounded support.
- Refreshed the cache to `exit_code: 0`, `status: ok`.

## What Did Not Change

- No audit ledger, queue, dispatch queue, or publication/status surface was
  edited.
- No audit verdict was applied.
- No new axiom was introduced.
- The row is not retained by this PR.

## Verification To Reproduce

```bash
python3 -m py_compile scripts/frontier_ew_lattice_cos_sq_theta_w_complement_bridge.py
PYTHONPATH=scripts python3 scripts/frontier_ew_lattice_cos_sq_theta_w_complement_bridge.py
PYTHONPATH=scripts python3 scripts/cached_runner_output.py --check-only scripts/frontier_ew_lattice_cos_sq_theta_w_complement_bridge.py --timeout-sec 120
rg -n 'HARD_ISSUES=[1-9]' logs/runner-cache/frontier_ew_lattice_cos_sq_theta_w_complement_bridge.txt
git diff --check
```

Expected runner closeout:

```text
TOTAL: PASS=33, BOUNDARY=7, HARD_ISSUES=0
```

## Remaining Blockers

- Retained promotion requires dependency gates to close independently.
- YT_EW must not be reused as the old unconditional bare-coupling theorem
  unless a future source repair restores a retained-grade input without hiding
  the kappa-family no-go.
