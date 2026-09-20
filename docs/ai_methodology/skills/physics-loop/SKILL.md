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
without automatically executing the workflow or replacing it with old main text.

Run a stateful theoretical-physics loop that can make a major lane move:
retire a load-bearing import, close an exact support gate, prove a useful
no-go, add a decisive artifact, or isolate the remaining Nature-grade blocker.

This skill is not a bigger `/autopilot` and not a factory for easy audit
artifacts. It is a claim-state machine for hard physics. It must spend real
time on named hard residuals before a route can be declared blocked or the
campaign can end. Preserve useful work durably and prepare reviewable PRs at
coherent milestones; unfinished research does not need a forced PR.

When launched for a long unattended run, the default posture is a **campaign**:
keep working until the runtime or max-cycle budget is exhausted. If one route
or lane hits an honest stop, checkpoint it, select the next ranked science
opportunity from the repo, and continue. Do not stop the whole campaign merely
because the first target ends in a no-go, support-only boundary, or
human-judgment blocker.

For a request like "run for 12 hours unattended", treat the runtime as a work
budget, not a maximum that can be abandoned after the first clean stop. The
agent should spend the allotted time while a scientifically useful route remains.
The quality-exhaustion conditions in references/CAMPAIGN.md also permit ending a
campaign; elapsed time, cycle counts, and PR counts are never evidence of
progress. Per-route blockers, review demotions, dirty PRs, missing retained
proof, unavailable optional literature, or failed
PR creation are not global stop conditions; they trigger demotion/backlog,
checkpoint, and pivot.

## Arguments

Parse:

- goal/problem text: required unless running `status` or `resume`;
- `--mode plan|run|resume|status|campaign`: optional, infer from the user
  request;
- `--runtime DURATION`: optional unattended runtime such as `45m`, `2h`, or
  `6h`;
- `--target retained|exact-support|bounded-support|no-go|best-honest-status`:
  optional, default `best-honest-status`;
- `--loop SLUG`: optional existing or new loop slug;
- `--workstream SLUG`: legacy alias for `--loop`;
- `--literature`: allow targeted physics/math literature review;
- `--max-cycles N`: optional cap on major execution cycles;
- `--checkpoint-interval DURATION`: optional, default `30m`;
- `--deep-block DURATION`: optional planning allocation for sustained work on
  a hard problem, default `90m`; evidence may justify an earlier route pivot;
- `--delivery milestone|block`: optional, default `milestone`; `block` preserves
  the earlier per-block delivery cadence when requested;
- `--no-pr`: do not open review PRs;
- `--no-review-loop`: skip optional author milestone review only if the user
  asked; this never waives independent review before landing;
- `--no-commit`: do not create commits.

If `--runtime` is absent and the user wants execution, ask how long to run
before launching unattended work. Do not assume a fixed default. If the user
only asks for planning, produce the plan without asking for runtime.

Infer `--mode campaign` when the user asks for an overnight, unattended,
long-running, or 12-hour run, even if the user says only `run`. A campaign
keeps selecting science blocks until the runtime/max-cycle budget or global
queue exhaustion condition is reached.

## Required reading by operation

The linked procedures remain requirements when their trigger applies. Select
the current operation; do not read every reference for a status check or reload
unchanged instructions at every checkpoint. A plan does not authorize execution,
and reviewing this skill does not launch a science campaign.

| Current operation | Required procedure before acting |
| --- | --- |
| Report status without making a new scientific judgment | Read the existing `STATE.yaml` and `HANDOFF.md`, their source identities, and evidence needed to substantiate the report. Distinguish recorded claims from newly verified results. |
| Select, plan, develop or reassess a scientific route | Read [Discovery and deep work](references/DISCOVERY.md) and [Claim status and premises](references/CLAIM_STATUS.md), then the relevant current source and necessary premises. |
| Start/resume execution, create artifacts, commit or prepare a milestone | Read [Delivery and loop pack](references/DELIVERY.md) before those actions; its generation-time conformance requirements apply while drafting. Also satisfy the scientific-route row for the work actually undertaken. |
| Launch/resume unattended work, pivot, declare exhaustion or stop a campaign | Read [Campaign continuation and stopping](references/CAMPAIGN.md), including its route to `long-running-execution.md` for unattended operation. This is additional to scientific and artifact requirements, not a substitute. |
| Make an import, wall, dependency, premise or status judgment | Read [Claim status and premises](references/CLAIM_STATUS.md) and perform the current primitive-registry/source checks it requires. A summary of supplied content is not authority. |
| Make a negative or bounded-with-walls claim | Apply the negative-claim gate in [Discovery](references/DISCOVERY.md) and the [No-Go Discipline skill](../no-go-discipline/SKILL.md) before shipping any such artifact. |
| Open the third or later PR in a parent-row family | Apply the cluster-cap evaluator in [Campaign](references/CAMPAIGN.md); also apply all delivery gates. Its decision governs PR opening, not scientific truth. |

References under `references/` are relative to this skill. Their links resolve
from the reference file; backticked `docs/`, `scripts/` and `.claude/` paths are
repository-relative. Use references from the same selected source revision.
If a required reference cannot be read, hold the dependent action and report
the missing requirement rather than treating this entry point as a substitute.

## Scientific invariants and context reuse

Preserve the selected model and reasoning effort for hard scientific work.
Distinguish proposed constructions, proof obligations, conditional theorems,
empirical predictions, independent checks and formal audit status. Do not add
axioms or primitives as part of a physics-loop run. State exact domains,
quantifiers and separately supplied conditions; no observed target or fitted
selector may become a hidden derivation input. Preserve counterexamples and
failed attempts. A failed search is not a no-go theorem; route counts, elapsed
time, runner PASS and reviewer agreement do not establish closure.

Continuous discovery may compose provisional results on a coherent branch with
explicit inherited gaps. Before extensive downstream reuse of a critical
provisional step, obtain a focused independent check of that step. Check the
mathematics by a genuinely different derivation or implementation, with the
appropriate proof or computational controls, and disclose limits on independence.
Formal retained status belongs only to independent audit. The author run never
lands science on main or writes audit verdicts; delivery is a reviewable milestone.

Use the existing pack as the current checkpoint, not a second summary packet.
Keep exact source/input identities, premises, open obligations, failed routes,
independent-check state and the next scientific decision accessible. Reuse a
completed instruction or evidence read only while its source, premises, scope
and relevant interactions remain valid. Refresh the affected closure when they
change, an unresolved issue reappears, or coverage is uncertain. Read complete
changed arguments and necessary evidence; a checkpoint, matching hash or short
tool result cannot supply a missing proof or certify review coverage.

Keep full logs in artifacts and return concise findings and paths. Batch
independent mechanical reads and calculations; do not turn checkpoints into
polished reports or fill a runtime with status traffic. Protect sustained
reasoning while the next step can add discriminating evidence. This changes
context handling, not the proof obligations or the triggers in the table.
