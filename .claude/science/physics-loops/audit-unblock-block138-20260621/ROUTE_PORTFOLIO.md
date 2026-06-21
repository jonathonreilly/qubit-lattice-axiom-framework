# Route Portfolio

## Selected Route: Dispatch Queue Refresh

Run `compute_audit_dispatch_queue.py` on current `origin/main` so existing
reaudit sidecars are classified into the generated dispatch queue.

Score:

- Audit-unblock value: high, because strict lint reported three stale dispatch
  warnings and audit-loop target selection would otherwise silently miss live
  sidecar targets.
- Science risk: low, because this updates target-selection outputs only.
- Blast radius: low, because the diff is limited to dispatch queue generated
  surfaces and branch-local loop metadata.

## Rejected Route: Rebase Existing PRs

Rejected by user instruction. Existing open PRs should not be refreshed to
fast-moving `main` only for dirty/behind status; the reviewer lane will update
or cherry-pick useful work.

## Deferred Route: Retained Note-Hash Drift

Strict lint still reports 30 retained-grade note-hash drift errors. Those
require independent re-audit or audit-lane reseeding and are outside this
branch because this loop must not run audits or apply verdicts.
