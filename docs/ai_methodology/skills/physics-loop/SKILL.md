---
name: physics-loop
description: Use when an LLM agent needs to plan, launch, resume, or package theoretical-physics discovery on a hard open lane/problem, with explicit premises, provisional dependency tracking, decisive checks, durable checkpoints, and review PRs at coherent science milestones.
---

# Physics Loop

## Skill Freshness

Before using this workflow, inspect its applicability and correctness and use
`docs/ai_methodology/skills/SKILL_FRESHNESS_CHECK.md` to select one consistent
source revision, including references. Ordinary operation uses current main;
a user-requested prompt review/test uses the identified candidate under review
without automatically executing the workflow.

## What this is

A claim-state machine for hard physics. A loop exists to make a real lane move:
retire a load-bearing import, close an exact support gate, prove a useful no-go,
add a decisive artifact, or isolate the remaining blocker precisely. It is not
a factory for easy audit artifacts. The evidence rules in
`docs/ai_methodology/SCIENCE_WORKFLOW.md` apply throughout; this skill adds only
loop mechanics.

Original mathematics is authorized. A missing theorem can be the next target.
The loop never adopts new axioms or primitives, never lands science on main
and never writes audit verdicts; its deliverable is a reviewable milestone PR.

## Arguments

| Argument | Meaning |
|---|---|
| goal text | Required unless `status` or `resume` |
| `--mode plan\|run\|resume\|status\|campaign` | Inferred from the request. Overnight, unattended, long or "N-hour" requests imply `campaign` |
| `--runtime DURATION` | Unattended budget, e.g. `6h`, `24h`. If execution is wanted and this is absent, ask; there is no default |
| `--target retained\|exact-support\|bounded-support\|no-go\|best-honest-status` | Default `best-honest-status` |
| `--loop SLUG` | Loop pack slug (`--workstream` is a legacy alias) |
| `--literature` | Allow targeted literature review |
| `--max-cycles N` | Optional cap on major cycles |
| `--checkpoint-interval DURATION` | Default `30m` |
| `--deep-block DURATION` | Planning allocation for one hard problem, default `90m`; evidence may justify an earlier pivot |
| `--delivery milestone\|block` | Default `milestone`; `block` restores per-block PRs |
| `--no-pr`, `--no-commit` | Suppress PRs or commits |
| `--no-review-loop` | Skip optional author milestone review only on request; never waives independent review before landing |

## Required reading by operation

Read only what the current operation needs, from the same source revision. If a
required reference cannot be read, hold the dependent action and say so.

| Operation | Read first |
|---|---|
| Status report | The pack's `STATE.yaml` and `HANDOFF.md` plus the evidence needed to back the report. Separate recorded claims from newly verified ones |
| Select, plan, develop or reassess a route | [Discovery and deep work](references/DISCOVERY.md), [Claim status and premises](references/CLAIM_STATUS.md), then the relevant current source and premises |
| Start/resume execution, create artifacts, commit, prepare a milestone | [Delivery and loop pack](references/DELIVERY.md) |
| Launch/resume unattended work, pivot, declare exhaustion, stop | [Campaign continuation and stopping](references/CAMPAIGN.md) and its `long-running-execution.md` |
| Import, wall, dependency, premise or status judgment | `references/CLAIM_STATUS.md` plus the primitive-registry checks it requires |
| Negative or bounded-with-walls claim | The negative-claim gate in `references/DISCOVERY.md` and the [No-Go Discipline skill](../no-go-discipline/SKILL.md) |
| Third or later PR in one parent-row family | The cluster-cap evaluator in `references/CAMPAIGN.md` (governs PR opening, not truth) |

Paths under `references/` are relative to this skill; backticked `docs/`,
`scripts/` and `.claude/` paths are repository-relative.

## Campaign posture

- Treat `--runtime` as a work budget to spend while a scientifically useful
  route remains, not a ceiling to abandon after the first clean stop. The
  quality-exhaustion conditions in `references/CAMPAIGN.md` may end a campaign
  early; elapsed time, cycle counts and PR counts are never evidence of progress.
- When one route ends (no-go, support-only boundary, human-judgment blocker),
  checkpoint it, pick the next ranked opportunity and continue. Per-route
  blockers, review demotions, dirty PRs, unavailable literature or a failed PR
  creation are not global stop conditions.
- Spend real time on named hard residuals before declaring a route blocked.

## Loop invariants

- Keep the selected model and reasoning effort for hard work.
- No observed target or fitted selector may become a hidden derivation input.
- Preserve counterexamples and failed attempts. A failed search is not a no-go.
- Provisional results may compose on the campaign branch with their open
  obligations explicit. Before heavy downstream reuse of a critical step, get a
  focused independent check by a genuinely different derivation or
  implementation, and disclose limits on that independence.
- The loop pack is the checkpoint; do not write a second summary packet. Keep
  source/input identities, premises, open obligations, failed routes,
  independent-check state and the next decision in it.
- Reuse an earlier read only while its source, premises and scope are unchanged.
  A checkpoint, hash or short tool result cannot stand in for a missing proof.
- Keep full logs in artifacts and return concise findings and paths. Do not fill
  a runtime with status traffic or polished interim reports.
