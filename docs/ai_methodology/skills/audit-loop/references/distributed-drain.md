# Coordinatorless Audit Drain

Use this contract when more than one employee or Codex account is helping
drain the same repository.

## One command, separate clones

Every participant uses a separate clean clone and runs the same command:

```bash
python3 docs/audit/scripts/orchestrate_audit_loop.py --max-workers 4
```

Run at most one orchestrator in a clone. The clone-wide lock covers every
worktree that shares that clone's Git common directory. Separate employees
must not share one mutable checkout.

The drainer generates a unique session id when `AUDIT_WORKER_ID` and
`--worker-id` are both omitted. The id only rotates target ordering so
independent workers usually start on different claims. It is not a lock,
lease, shard assignment, or scientific authority.

## Deliberately optimistic

There is no coordinator, leader election, heartbeat, campaign ref, shared
checkout ledger, or global completion record. A Markdown checkout ledger
would create a new contended source of truth and could strand work after a
crash, so the canonical workflow does not use one.

Two workers may compute the same claim. That is safe and occasionally
wasteful:

1. each restricted seat binds its delivery to the source, ledger provenance,
   dependencies, runner/helper inputs, evidence manifest, role, independence,
   passes, and selecting dispatch/cascade entry it observed;
2. immediately before apply, the committer fetches current `origin/main` and
   rechecks that complete selection fingerprint;
3. remote movement returns `remote_state_superseded`; the stale delivery mints
   no verdict and creates no quarantine;
4. accepted claims still pass the normal apply, full pipeline, strict lint,
   one-claim commit, and fast-forward push transaction;
5. a push race is reconciled from fresh `origin/main`; generated audit state is
   regenerated, never hand-merged.

These existing claim-transaction checks are the safety boundary. Worker ids
and target rotation only reduce duplicated compute.

## Panels, forensics, and failures

Every worker runs the complete panel-aware loop. Panels and forensic rows are
serial inside one worker but may overlap optimistically across independent
clones. The same current-main precondition and push reconciliation decide
which current transaction can land; stale duplicates are discarded.

Schema-invalid, compute-required, verified claim-transaction failures, and
post-verdict blocked-row reentries remain claim-local campaign exclusions.
The worker records the exact repair artifact and continues every unrelated
eligible row. Unknown execution failures and unreconciled apply, propagation,
or push failures still stop that worker fail-closed; they do not authorize
another worker to reinterpret the failed scientific packet.

Keep repository-wide load near 8-10 active Codex processes when practical,
including audit seats, panels, and review-loop reviewers. This is a throughput
guideline, not a correctness lock. If capacity is exhausted, lower
`--max-workers` or restart later.

## Completion is observational

A worker exits after a fresh synchronized pass lands nothing and no ready
non-excluded forensic target remains. That is a worker-local fixed-point
observation, not a global certificate: another clone may still have an
in-flight delivery.

After visible workers quiesce, refresh `main` and read the canonical audit
queue, lane certification, and campaign exclusion reports. If new work is
visible, run the same command again. A worker that landed the last in-flight
verdict naturally loops back through development and drains anything it
unblocked. A crash after landing may leave newly unblocked work for the next
ordinary invocation; it never creates a false terminal campaign state.

Route quarantined and typed selector-skip repair inventory through
`science-fix-loop`. No operational checkout note, worker exit, or local
campaign artifact may certify retained grade or backlog completion.
