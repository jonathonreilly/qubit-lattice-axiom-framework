# Route Portfolio

1. Targeted cache refresh: run `precompute_audit_runners.py --runners
   toy_event_physics.py --push-mode=none` and commit the generated canonical
   cache.
2. Runner optimization: deferred. The audit blocker here is missing stdout, not
   a proven need to change the runner semantics.
3. Audit action: out of scope for this PR.

