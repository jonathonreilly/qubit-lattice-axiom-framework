# /progress — Research Retrospective

You are the Research Manager reviewing recent progress on the qubit-lattice
axiom framework.

## Data Collection

1. Landed work: `git log --oneline --since="1 week ago" -- docs/ scripts/`
   (science) and `git log --oneline --since="1 week ago" -- docs/audit/`
   (audit lane).
2. PR flow: `gh pr list --state merged --search "merged:>={date-7d}"` and
   `gh pr list --state open` — note science PRs opened, landed, closed with
   salvage, or rejected.
3. Audit-lane movement: new `audit:` commits; current queue depth from
   `docs/audit/AUDIT_QUEUE.md`; any newly retained-grade rows.
4. Loop state: latest `HANDOFF.md` / `STATE.yaml` under
   `.claude/science/physics-loops/*/` touched this period.
5. Working docs: new files under `.claude/science/` (hypotheses, analyses,
   validations, derivations, investigations) this period.

## Report Sections

### Summary (3 sentences max)
- Main thrust of the period, strongest new result, current frontier.

### Claim-State Movement
| Item | Movement | Evidence |
|------|----------|----------|
| {claim/lane} | proposed / landed / audited_clean / retained-grade / demoted / no-go | {PR, commit, ledger row} |

Be precise about the propose/ratify split: "landed on main" is not
"retained" — only the audit ledger grants retained-grade status.

### Key Findings
- Numbered quantitative results from this period, each with its source
  (note + runner + cache, or ledger row).

### Failed / Dead Ends
- What was tried and didn't work? Bug, artifact, wrong regime, genuine
  wall? Honest no-gos and named walls are valuable output — list them with
  their `NO_GO_LEDGER.md` or note references.

### Pipeline Health
- Review backpressure: findings from recent `/review-loop` runs, demotions,
  salvages.
- Audit lane: queue depth trend, conditional backlog, any blocked rows.
- Hygiene: stale branches, unlanded coherent blocks, `PR_BACKLOG.md` entries.

### Recommended Next Steps
Prioritized by expected claim-state movement (defer to `/frontier` for the
full gap analysis):
1. {highest value}
2. {second}
3. {third}

For each: one sentence on why, and estimated effort (interactive /
unattended block / campaign).

## Output

Write to `.claude/science/progress/{date}-retrospective.md`. Create the
directory if it does not exist.

## Rules

- No lock needed — read-only analysis.
- Be honest about dead ends; they are information.
- Do not pad. If it was a slow week, say so.
- Quantify: N PRs, N landed notes, N audit verdicts, N retained-grade
  promotions.
- Never blur author-side status with audit-ratified status.

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
