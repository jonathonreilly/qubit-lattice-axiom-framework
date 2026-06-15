# Review History

- `PYTHONPATH=scripts python3 scripts/precompute_audit_runners.py --runners toy_event_physics.py --check-only`
  passed after refresh.
- `PYTHONPATH=scripts python3 scripts/precompute_audit_runners.py --all --check-only`
  now reports only `scripts/kinetic_isotropy_3d_simultaneous_tick_2026_06_10.py`
  as stale; that runner is already covered by PR #3991.

