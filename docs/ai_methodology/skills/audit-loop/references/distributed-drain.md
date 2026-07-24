# Distributed Audit Drain

Use this operating contract when more than one employee or Codex account is
helping drain the same repository.

## Roles

Designate exactly one **coordinator** for the campaign. It owns:

- targeted dispatch and cascade re-audit sources;
- flagship-lane priority sweeps;
- judicial panels and reseats;
- serial forensic rows;
- the final all-source fixed-point declaration.

During the concurrent development wave, run the coordinator from its own clean
`main` clone with forensic work deferred:

```bash
AUDIT_WORKER_ID=<unique-coordinator-id> \
python3 docs/audit/scripts/orchestrate_audit_loop.py \
  --max-workers 4 --skip-forensic-canary
```

Every other employee is a **development helper**. Give every helper a stable,
globally unique worker id and a separate clean `main` clone:

```bash
AUDIT_WORKER_ID=<unique-employee-account-id> \
python3 docs/audit/scripts/orchestrate_audit_loop.py \
  --development-helper --max-workers 2
```

A helper skips dispatch, cascade, flagship priority passes, panels, and
forensics. It only drains the complete eligible development set in a
worker-specific order. The worker id changes ordering; it does not assign an
exclusive shard. If a helper disappears, every unfinished row remains
eligible to every surviving worker.

## Collision Safety

- Run at most one orchestrator in any clone. The clone-wide lock covers all
  worktrees of that clone.
- Independent clones may run concurrently. Every apply transaction first
  synchronizes to `origin/main` and compares the current ledger provenance,
  exact packet evidence manifest, dependency note bytes, runner/helper inputs,
  computed seat role/independence/passes, and alternate-source selection with
  the state seen by the restricted seat. The cascade source must exactly match
  a pure recomputation from current ledger and runner bytes. If anything
  moved, the stale delivery is discarded as `remote_state_superseded`; it
  mints no verdict and creates no quarantine.
- Different claims still commit one at a time per clone. A push race is
  reconciled against the intended commit and replayed from current
  `origin/main`; never hand-merge generated audit state. If the remote outcome
  cannot be reconciled, preserve the intended local commit and stop instead of
  resetting or replaying an uncertain push.
- Primary and helper runners execute in disposable isolated worktrees. Their
  processes and detached children inherit a per-invocation identity token.
  Cleanup repeatedly enumerates that token, revalidates it immediately before
  every signal, and fails unless no token-bearing process remains; it never
  signals a remembered bare PID. On macOS a kernel sandbox additionally denies
  writes to the canonical checkout. Containment and whole-worktree discard are
  both mandatory on every exit path; cleanup never deletes deltas observed in
  the canonical committer checkout.
- Use unique worker ids. Reusing an id is safe but defeats target dispersion
  and wastes seats.
- Keep the combined repository-wide load near 8-10 active Codex processes,
  including coordinator seats, helper seats, panels, and review-loop
  reviewers. Separate subscriptions do not remove the shared Git/pipeline
  bottleneck.
- Do not run the specialized forensic committer while development helpers are
  still live. The development batch has remote-state replay guards; the
  forensic path is intentionally serial. The concurrent-wave coordinator
  therefore uses `--skip-forensic-canary`.

## Completion Protocol

A helper's zero-progress exit is only a **helper-local development fixed
point**. It never certifies that the audit is finished because another clone
may still have an in-flight seat whose commit does not yet exist.

After every helper is quiescent, run a fresh coordinator-only final sweep
without `--skip-forensic-canary`:

```bash
AUDIT_WORKER_ID=<unique-coordinator-id> \
python3 docs/audit/scripts/orchestrate_audit_loop.py --max-workers 4
```

The coordinator may declare completion only after:

1. every helper is quiescent or has reported its local fixed point;
2. the coordinator performs a fresh final sweep from current `origin/main`;
3. ready dispatch and cascade sources have no actionable non-forensic target;
4. flagship and global development phases land nothing;
5. panels have no resumable handoff;
6. the serial forensic selector has no ready non-excluded target.

The concurrent-wave coordinator is expected to exit at a development fixed
point. Always start the coordinator-only final campaign after helpers
quiesce. Campaign-local quarantines and typed selector skips are not proof
that the entire scientific backlog is empty; report them as governed repair
inventory and route them through `science-fix-loop`.

Schema-invalid, compute-required, and verified claim-transaction failures
exclude only their claim for the current campaign. The coordinator continues
to the next unrelated row. A successfully applied non-clean forensic verdict
that immediately re-enters unchanged is durably excluded from that campaign
so it cannot consume the next forensic seat before source repair. A newly
written exclusion counts as operational progress: the supervisor starts
another bounded batch even when that round landed no Git commit, and declares
a lane fixed point only after both HEAD and the exclusion set remain stable.
