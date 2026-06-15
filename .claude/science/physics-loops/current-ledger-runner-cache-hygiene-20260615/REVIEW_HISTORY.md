# Review History

- 2026-06-15: Initial ledger-wide check found 15 corrupt caches and one missing
  `toy_event_physics.py` runner path.
- 2026-06-15: Root guide wording was changed so the meta guide no longer
  presents the top-level legacy Python artifact as a runner.
- 2026-06-15: Repaired status drift in the observable-principle and p-flux
  source packets after recent audit landings. No status promotion or audit
  ledger edit was made.
- 2026-06-15: Bounded the kinetic-isotropy optimizer search with
  `AUDIT_TIMEOUT_SEC = 300`; direct runner result is `PASS=20 FAIL=0`.
- 2026-06-15: Targeted cache refresh cleared the four stale/corrupt current
  runners (`ok=4`, `timeout=0`, `nonzero_exit=0`); post-pipeline full-ledger
  check reports 2888 fresh, 0 stale, 0 missing.
- 2026-06-15: Rebased onto `origin/main@fc08b0519`. Reviewer landings had
  already absorbed or superseded the runner/script/cache pieces, so conflict
  resolution preserved current main for those files. The refreshed branch now
  contains only the observable-principle source-boundary wording, root-guide
  hygiene, and this loop pack.
