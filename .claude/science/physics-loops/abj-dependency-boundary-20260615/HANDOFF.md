# Handoff

This branch repairs the ABJ bridge's source dependencies. It does not edit
audit files and does not claim a retained outcome.

## What Changed

- `NATIVE_GAUGE_CLOSURE_NOTE.md` is demoted to nonabelian/Z3 context for
  this ABJ row.
- The LH and RH hypercharge surfaces are routed to the actual bounded
  supplier rows.
- The spacetime-gamma5 step is explicit and still conditional on the
  separate-factor / adjacency-rank carrier route.
- The runner now guards against the stale native-gauge hypercharge claim.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/anomaly_forces_time_abj_inconsistency_accepted_premise_runner.py
python3 scripts/precompute_audit_runners.py --runners scripts/anomaly_forces_time_abj_inconsistency_accepted_premise_runner.py --force --push-mode none
python3 scripts/precompute_audit_runners.py --runners scripts/anomaly_forces_time_abj_inconsistency_accepted_premise_runner.py --check-only
python3 docs/audit/scripts/audit_lint.py --strict
git diff --check
```

Expected ABJ runner scorecard: `TOTAL: PASS=75 FAIL=0`.

## Remaining Blocker

The hypercharge dependency edge is source-repaired. The remaining
Nature-grade blocker is the full spacetime-gamma5 carrier bridge: the
staggered epsilon sign alone is not enough, and the adjacency-rank route is
still audit-owned.
