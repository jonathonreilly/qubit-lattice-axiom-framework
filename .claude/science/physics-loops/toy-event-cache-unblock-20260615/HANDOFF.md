# Handoff

This PR removes one uncovered compute/cache blocker on current main.

Target:

- Ledger row: `repo.root_file_guide`
- Runner: `toy_event_physics.py`
- Cache: `logs/runner-cache/toy_event_physics.txt`

The cache is a canonical timeout cache. That is intentional: the audit runner
can now see the exact current runner behavior instead of treating the row as
missing cached stdout. This PR does not edit audit verdicts, dispatch queues, or
effective statuses.

Verification:

```bash
PYTHONPATH=scripts python3 scripts/precompute_audit_runners.py --runners toy_event_physics.py --check-only
PYTHONPATH=scripts python3 scripts/precompute_audit_runners.py --all --check-only
```

Expected state after this PR alone:

- `toy_event_physics.py` is fresh.
- The full-ledger check still reports the kinetic-isotropy cache as stale until
  PR #3991 lands.

