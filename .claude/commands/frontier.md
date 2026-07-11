# /frontier — Frontier Map & Gap Analysis

You are the Research Strategist mapping explored vs. unexplored territory for
the qubit-lattice axiom framework.

## Data Collection

1. Ledger statistics — counts by `effective_status` and `claim_type`:
   ```bash
   python3 - <<'PY'
   import json, collections
   rows = json.load(open("docs/audit/data/audit_ledger.json"))["rows"]
   eff = collections.Counter(r.get("effective_status") for r in rows.values())
   ct  = collections.Counter(r.get("claim_type") for r in rows.values())
   print("effective_status:", dict(eff))
   print("claim_type:", dict(ct))
   PY
   ```
2. Audit-lane backlog: `docs/audit/AUDIT_QUEUE.md` depth and
   `docs/audit/data/reaudit_candidates.json`.
3. Lane surfaces: `docs/repo/LANE_REGISTRY.yaml`,
   `docs/work_history/repo/LANE_STATUS_BOARD.md`,
   `docs/repo/ACTIVE_REVIEW_QUEUE.md`.
4. Loop state: `OPPORTUNITY_QUEUE.md`, `NO_GO_LEDGER.md`, and `HANDOFF.md`
   files under `.claude/science/physics-loops/*/` and
   `.claude/science/research-lanes/*/`.
5. In-flight work: `gh pr list --state open` (science and physics-loop
   branches), plus recent landings:
   `git log --oneline --since="2 weeks ago" -- docs/ scripts/ | head -40`.
6. `README.md` current package state.

## Analysis

### 1. Lane Census
- Group active work by lane/domain. For each: retained-grade results,
  bounded results with named conditions, open gates, standing no-gos.
- Present as a table: | Lane | Retained | Bounded | Open gates | No-gos | Status |

### 2. Blocker Fanout (the keystone view)
- Which open gates, unaudited rows, and `audited_conditional` blockers sit
  upstream of the most downstream work? Use the ledger `deps` graph (and
  load-bearing/descendant fields where present) to rank blockers by how much
  they unblock. Closing a high-fanout root beats closing a leaf.

### 3. Premise Coverage
- Which named conditional inputs and imports are still load-bearing, and
  which lanes are queued to derive or eliminate them?
- Which named derivation lanes (dynamics, Born weights, readout bridges,
  species identification, ...) have no active work at all?

### 4. Confirmed vs. Unvalidated
- Landed-and-audited (retained-grade) vs. landed-but-unaudited vs.
  branch-local working results. Only the ledger separates these — list each
  bucket explicitly.

### 5. Dead Ends
- Standing no-go notes and `NO_GO_LEDGER.md` routes. Mark clearly: "do not
  re-attack without a new named premise" — and name what kind of premise
  would qualify, since retired walls do get retired by reframes.

### 6. Highest-Value Gaps
Rank the top 5 unexplored or under-explored targets by:
- expected claim-state movement (could it retire an import, close a gate,
  unblock a high-fanout chain, or prove a useful no-go?);
- feasibility with existing runners vs. new code;
- estimated effort (interactive / unattended block / multi-day campaign).

## Output

Write to `.claude/science/frontier/{date}-frontier-map.md`:

```markdown
# Frontier Map: {date}

## Coverage Summary
{ledger counts, queue depth, open PRs, active loops}

## Lane Census
{table}

## Blocker Fanout
{ranked blockers with what each unblocks}

## Premise Coverage
{load-bearing admissions/imports and their retirement lanes}

## Top 5 Highest-Value Gaps
1. {gap} — {why it matters} — {effort}
...

## Dead Ends (do not revisit without a new named premise)
- {route} — {wall} — {what kind of premise would reopen it}
```

## Rules

- No lock needed — read-only analysis.
- Do not fabricate coverage. If a lane has no artifacts, say so.
- Distinguish "unexplored" (never attacked) from "exhausted" (attacked,
  walled, no-go on record).
- The gap ranking is the most important output — spend the most thought
  there. This skill pairs naturally with `/progress`.
- Mapping only: this skill proposes targets, it does not move claim states.
  Execution belongs to `/physics-loop` or an interactive science session.

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
