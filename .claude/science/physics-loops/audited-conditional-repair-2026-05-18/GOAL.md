# Goal — audited_conditional repair campaign 2026-05-18

## Science goal

Repair as many `audited_conditional` source rows toward `audited_clean` as
possible over a 12-hour campaign budget. Positive retained closure is the
preferred outcome (`audited_clean` on a `positive_theorem` or
`bounded_theorem` row). `bounded` settling is accepted only when retained
closure is not reachable from the row's current dependency graph.

## Target status

- `--target retained` (preferred): drive the row's effective status to
  `audited_clean` with `claim_type ∈ {positive_theorem, bounded_theorem}`.
- `--target bounded-support` (fallback): if the cited authority cannot
  promote to retained, settle the row at `bounded_retained` with a narrowed
  scope.

## Scope

- Read the 104 `audited_conditional` rows in `docs/audit/data/audit_ledger.json`.
- Prioritize Tier A repairs (`runner_artifact_issue` and
  `missing_dependency_edge` rows where the cited authority already exists).
- Tier B if Tier A exhausts: `missing_bridge_theorem` rows where the bridge
  is a one-step algebraic identity derivable from retained primitives.
- Skip Tier C (`dependency_not_retained` without queued upstream) and Tier D
  (new physics derivations, scope rewrites) unless the upstream lands during
  the campaign.

## PR policy

- One repair = one PR (1 source-note edit + 1 runner + 1 cache, per
  memory `feedback_review_loop_source_only_policy`).
- Branch per block: `physics-loop/audited-cond-<slug>-2026-05-18`.
- Open PRs against `main`. Do not merge. Do not push to `main`.
- Audit-lane re-audits the rows on next cycle through cascade resolution
  (`docs/audit/data/reaudit_candidates.json`).

## Non-negotiables (from physics-loop skill)

- No new axioms. `A_min` is the minimum stack, not permission to enlarge.
- No bare `retained`/`promoted` in source-note `Status:` lines on this branch.
- No fitted values, hidden imports, or admission inflation.
- Per-block `CLAIM_STATUS_CERTIFICATE.md` before PR open.
- Review-loop on each block unless deferred to bulk review at campaign close.

## Stop conditions

- 12-hour runtime exhausted.
- Refreshed `OPPORTUNITY_QUEUE.md` exhausts viable Tier A/B candidates.
- Worktree corruption or tooling lock conflict requires manual recovery.
