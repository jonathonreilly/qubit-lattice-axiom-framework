# Audit Landscape Snapshot — 2026-05-17

**Claim type:** meta
**Status:** read-only diagnostic snapshot; not part of the audit citation graph

**Snapshot date:** 2026-05-17
**Diagnostic tool:** `scripts/audit_landscape_snapshot.py`
**Cached output:** `logs/runner-cache/audit_landscape_snapshot.txt`

## Where we stand

### Audit ledger (2135 total claims)

| audit_status | count |
|---|---:|
| (see cached output for full breakdown) | |

### Audit queue (1205 pending)

| criticality | count |
|---|---:|
| critical | 752 |
| high | 35 |
| medium | 150 |
| leaf | 268 |

**Ready (deps cleared):** 4 of 1205 (0.33%)

### Citation cycles (247 total)

- **247 of 247 cycles have explicit informational-co-cycle instructions** — every cycle in the queue includes an audit-pipeline-generated prompt naming the co-cycle members the auditor should treat as informational/non-load-bearing.
- **0 cycles WITHOUT such instructions** — no purely-circular dependencies without a named break target.
- **83 unique primary_break_target notes** — the audit lane has consolidated all 247 cycles into 83 distinct audit-prep tasks.
- Longest cycle: 31 nodes.

### Leverage map (top 10 source notes)

The audit pipeline names these notes as the break targets whose audit verdicts would unlock the most cycles:

| # | source note (primary_break_target) | edges in repair scope |
|---:|---|---:|
| 1 | `axiom_first_microcausality_lieb_robinson_theorem_note_2026-05-01` | 42 |
| 2 | `c3_symmetry_preserved_interpretation_note_2026-05-08` | 41 |
| 3 | `dm_effective_parent_one_clock_transfer_boundary_theorem_note_2026-04-18` | 34 |
| 4 | `dm_leptogenesis_ne_active_column_axiom_boundary_note_2026-04-16` | 33 |
| 5 | `a3_r5_hostile_review_confirms_obstruction_note_2026-05-08_r5hr` | 31 |
| 6 | `a3_route1_higgs_yukawa_c3_breaking_bounded_obstruction_note_2026-05-08_r1` | 29 |
| 7 | `a3_route3_anomaly_inflow_bounded_obstruction_note_2026-05-08_r3` | 29 |
| 8 | `dm_leptogenesis_exact_kernel_closure_note_2026-04-15` | 27 |
| 9 | `angular_kernel_underdetermination_no_go_note` | 23 |
| 10 | `cross_sector_a_squared_koide_vcb_bridge_support_note_2026-04-25` | 22 |

## How cycles actually resolve (5-step workflow)

The audit pipeline ALREADY structures the resolution path. Each cycle has an
`instruction` field that spells out the workflow:

1. **Audit pipeline names** the cycle's `primary_break_target` (node to audit)
   and `co-cycle citations` (other cycle members to treat as informational).

2. **Codex auditor runs** on the break target with the prompt instruction that
   the named co-cycle nodes are non-load-bearing. (The repo uses "current best
   Codex GPT model at maximum reasoning" per `docs/audit/scripts/run_pipeline.sh`.)

3. **If `audited_clean`** (chain closes without the co-cycle deps), the node
   moves to a settled status. The audit ledger records a clean audit status.

4. **Source-graph repair pass strips** the now-confirmed-cite-only markdown
   links from the source note. `effective_status` leaves `retained_pending_chain`.
   This step is currently UNTOOLED — the audit_queue instruction names it as
   needed but no one-command tool exists.

5. **Re-run audit pipeline** (`bash docs/audit/scripts/run_pipeline.sh`)
   regenerates citation graph + cycle inventory. The cycle disappears.

## What's blocking "finish the full audit"

- **Audit verdicts:** 1205 pending, 247 cycles. The Codex auditor handles these
  on a nightly automated pipeline (visible in git log: "audit: nightly repair
  and pipeline refresh (automated)" commits). New audit-prep contributions
  accelerate specific targets.
- **Step 4 tooling absent:** the source-graph repair pass is referenced by
  every cycle's instruction but has no one-command implementation. Currently
  the strip is presumably done manually after each audit verdict.
- **No genuine-circular cycles:** every cycle has an audit-prep path. The
  backlog is throughput-limited, not blocked by unresolvable structural issues.

## Three paths user can authorize

**Option 1 — Build the strip tool (B in the diagnostic's Section 6).**
Mechanical. Makes step 4 a one-command operation. After each `audited_clean`
verdict from the Codex auditor, the strip tool can be run to follow up
without manual editing. ~1-3h of work.

**Option 2 — Author audit-prep contributions (A) for top-N targets.**
Per-target ~3-4h of work (5-agent fan-out + write-up + runner + PR), matching
the [PR #1262 template](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1262) for `anomaly_forces_time_theorem`.
With 83 targets, this is a sustained stream of work — direct but not one-shot.

**Option 3 — Let the automated pipeline (C) crank, monitor with this diagnostic.**
The audit lane already runs nightly. The diagnostic is re-runnable. User
intervenes when specific stuck items need targeted prep.

## Stuck-item monitoring

Re-run the diagnostic any time to refresh:

```bash
python3 scripts/audit_landscape_snapshot.py
```

The `ready_count` is a good thermometer. Going from 4 → 50 → 200 over time
means the pipeline is making progress. Stalled at 4 for weeks means
human/auditor intervention is needed.

## Cross-references (non-load-bearing)

- `docs/audit/AUDIT_QUEUE.md` — canonical audit queue rendering
- `docs/audit/AUDIT_LEDGER.md` — canonical audit ledger
- `docs/audit/scripts/run_pipeline.sh` — audit pipeline orchestrator
- `docs/audit/scripts/build_citation_graph.py` — extracts edges from markdown
- `docs/audit/scripts/compute_audit_queue.py` — generates audit queue + cycles
- `docs/audit/AUDIT_AGENT_PROMPT_TEMPLATE.md` — auditor prompt template
