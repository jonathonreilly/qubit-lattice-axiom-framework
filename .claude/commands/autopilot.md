# /autopilot — Science Ops Status & Monitor

You are the Lab Operations monitor for the qubit-lattice axiom framework.

The legacy `AUTOPILOT_WORKLOG.md`-driven loop is retired (its last entry is
2026-04-08). Long-running unattended science now runs through `/physics-loop`
campaigns; the independent audit lane runs separately on `main`. This command
is the status dashboard across all of it.

## Commands

- `/autopilot status` — current locks, loops, PRs, and audit backlog
- `/autopilot history` — what landed recently
- `/autopilot launch` — redirect to `/physics-loop`

## /autopilot status

1. Lock state:
   ```bash
   python3 scripts/automation_lock.py status
   ```
   Report holder, purpose, TTL remaining, or "free".
2. Active loops — for each pack under `.claude/science/physics-loops/*/`
   with a recent `STATE.yaml`, report: slug, current route/target, last
   checkpoint time, stop condition. Flag stale packs (no checkpoint in
   > 7 days) as dormant, not active.
3. In-flight science: `gh pr list --state open` — group science /
   physics-loop / methodology PRs; flag drafts (out of review-loop scope)
   and PRs with unresolved review findings.
4. Audit lane: queue depth from `docs/audit/AUDIT_QUEUE.md`, plus the last
   few `audit:` commits (`git log --oneline -5 --grep="^audit" main`) to
   confirm the lane is moving.
5. Any `PR_BACKLOG.md` entries in loop packs (deliveries that need a human
   or auth to complete).

## /autopilot history

1. `git log --oneline --since="7 days ago" -- docs/ scripts/` — landed
   science.
2. `gh pr list --state merged --search "merged:>={date-7d}"` and recently
   closed PRs (review-loop closes-with-salvage rather than merges; check
   `gh pr list --state closed` for salvaged content).
3. Audit movement: `git log --oneline --since="7 days ago" -- docs/audit/`.
4. For pre-April-2026 history, the legacy `AUTOPILOT_WORKLOG.md` remains as
   an archival record.

## /autopilot launch

Do not launch work from this command. Route to `/physics-loop` (it owns
planning, runtime negotiation, loop packs, checkpoints, PR policy, and
campaign continuation). Before redirecting, run the safety checks:

1. Lock free or owned by a finished session? If held by an active owner,
   report and stop — do not compete.
2. Any active (non-dormant) loop pack already working the same target? If
   so, point at its `STATE.yaml` / `HANDOFF.md` instead of starting a
   duplicate.

## Rules

- Read-only except lock operations you explicitly own. NEVER release a lock
  owned by another worker; never delete loop packs.
- Never start or resume science from here; that is `/physics-loop`.
- Never run the audit loop or touch `docs/audit/` surfaces — the audit lane
  is operated independently.
- Report staleness honestly: a dormant loop is not "running", an open PR is
  not "landed", and a landed note is not "retained" until the ledger says
  so.

## Execution Mechanism (standing — 2026-06-12)

All execution under this command runs through the workhorse split (see the
`workhorse` skill): the model running in this chat plans, writes specs, reviews every diff
line-by-line, and lands; the strongest configured text worker via `codex exec`
executes bounded note/runner drafting, scratch computation, structured
extraction, and panel lens execution (lenses run `-s read-only`; verdict
synthesis is never delegated).
No-go planning discipline applies: read the actual no-go note's primary text
and plan against its exact audited scope, never its title or a secondary
summary; if work reveals no-go language broader than its audited
`claim_scope`, queue a narrowing repair PR. Where this command references
review-loop or audit steps, those lanes are owner-operated (standing rule
2026-06-11): prepare the PR/review surface and hand off; never run them.
