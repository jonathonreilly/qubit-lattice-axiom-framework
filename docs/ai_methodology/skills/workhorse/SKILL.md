---
name: workhorse
description: "Use when a repo science command needs the owner-approved execution split: the supervising agent plans/specifies/reviews/lands, while a high-reasoning text worker executes bounded drafting, computation, extraction, or read-only panel lenses."
---

# Workhorse

## Skill Freshness

Before applying this skill, perform the repo skill freshness check described in
`docs/ai_methodology/skills/SKILL_FRESHNESS_CHECK.md`. If a newer version of
this `SKILL.md` exists on `origin/main`, follow that version for the current
task.

This skill defines the execution mechanism for repo science commands. It is a
coordination protocol, not a physics authority and not an audit lane.

## Execution Split

The supervising agent is the model running the current chat session — whichever
Claude model is driving the conversation (e.g. Fable, or the strongest available
Claude model at the time). It is not a separately pinned or named model; it
follows the in-chat model.

Two worker profiles are first-class (owner directive 2026-08-03).
Operational support — support-only evidence, NOT on `origin/main`: the
2026-08 campaign work-log (`STATE.yaml` and `REVIEW_HISTORY.md` under
`.claude/science/physics-loops/toe-time-expansion-20260802/` on the pack
branch `physics-loop/toe-close-pack-20260729`) records that window's Claude
workers block by block, including a checker refuting a supervisor-authored
primary, a worker catching a verdict-flipping rubric defect in its own
primary, and 3/3 pre-registered checker predictions on never-evaluated
windows. The profiles:

- **Codex text-reasoning worker** — the local `codex exec` setup, preferred
  profile `gpt-5.6-sol` at `model_reasoning_effort=max` (owner directive
  2026-07-08; verify slug and effort live against the local install). Launch
  and reliability rules below.
- **Claude worker** — a subagent of the host session (the Agent tool or
  equivalent), running the strongest available WORKER-TIER Claude model
  (currently Opus 5 — the tier below the supervising frontier model) at
  maximum reasoning effort (farmed work runs at max — owner directive
  2026-06-26; subagents inherit the session's effort, so the session must
  be at max). Launched as background workers, one per block, each in its
  own durable worktree. The codex start-hang/stdin failure modes have not
  been observed with Claude workers (no CLI stdin is involved at launch),
  but context exhaustion from oversized reads or tool output remains
  possible for any bounded-context worker: the bounded-read and
  incremental-delivery discipline applies to this profile too.

  Worker-tier rationale (owner-ratified 2026-08-04): the frontier model is
  NOT the default worker even though it is the strongest available Claude
  model. The default split concentrates the frontier model where its
  capability is load-bearing — spec judgment, line-by-line review, and
  landing — and preserves the shared capacity pool across a long window
  (parallel frontier workers would burn the window's budget on the lane
  where discipline, not raw capability, carries robustness). Per the
  campaign work-log cited above: the defects that were caught in that
  window were caught by the verification structure, including supervisor
  spec errors caught BY workers; that record says nothing about defects
  that went undetected, and no completeness claim is made. The supervising
  agent MAY escalate an individual block's worker or checker to the
  frontier model when that block's difficulty warrants it; escalation is a
  profile fact and is disclosed in the ship note like any other.

Profile selection is the supervising agent's discretion, with one preference:
when both lanes are available, pair them — primary from one family, checker
from the other — because a checker built by a different model family is more
independent than a checker built in a separate context of the same family.
When only one family is available (quota, outage), the same-family setup is
admissible ONLY under the robustness conditions below, and every shipped
block must say plainly in the note, receipt, and PR whether its checker was
built by a different model family or in a separate context of the same
family (and say so if context separation cannot be established). This
describes the checker pairing only; it is not an audit-independence grade —
audit rows use the controlled `independence` vocabulary in
`docs/repo/CONTROLLED_VOCABULARY.md`.

Known residual: the canonical `/workhorse` command surface and its
science-command callers still carry the earlier Codex-first launch default;
they are updated in a separate change, not by this file.

Never substitute an image, visual-generation, document-rendering, or
low-reasoning model for either profile. Disclose any substitution in the work
log and keep the supervising agent responsible for the result.

## Robustness Conditions (mandatory; load-bearing when primary and checker share a model family)

- Every block ships an independent checker spec'd to REFUTE, built on
  machinery disjoint from the primary's (different arithmetic route,
  different enumeration/allocation, no import of the primary — text/AST pins
  behind an import firewall).
- Checker teeth must be demonstrated, not asserted: mutation probes or
  planted defects that the checker provably catches, and tamper tests that
  fail closed.
- The supervising agent reviews every worker diff line-by-line and
  hand-verifies the load-bearing mathematics of at least the central claim
  before accepting a block; cache terminals are verified against emitted
  certificates.
- Integrity gates never encode desired outcomes; findings are generated from
  computed values.
- These conditions are what make same-family worker/checker pairs admissible;
  they are good practice for cross-model pairs too.

The supervising agent:

- reads current repo context and the relevant command/skill instructions;
- writes the task spec, allowed files, evidence bar, and stopping conditions;
- keeps claim-status, foundation/conditional, no-go, and audit boundaries
  current;
- reviews every worker diff line-by-line before accepting it;
- runs the appropriate repo checks;
- lands or rejects the work only through the lane that owns that decision.

The worker may:

- draft notes, runners, tables, or narrow repairs from the supervisor's spec;
- run scratch computations and structured extraction;
- execute panel lenses with read-only filesystem settings;
- report uncertainties, missing premises, and proposed demotions.

The worker must not:

- synthesize final verdicts that the supervising agent merely rubber-stamps;
- apply audit verdicts, effective-status changes, or retained promotions;
- add axioms, primitives, or any unregistered supplied-premise class;
- decide to land, merge, or close PRs;
- route science work through visual/image-generation tooling.

## Claude Worker Launch (when using the Claude profile)

- Spawn one background subagent per block, each pointed at its own durable
  worktree (never a tmp path — reboots purge tmp; the 2026-08-02 campaign
  interruption is the precedent), with the block spec inline in the prompt.
- The spec carries the same bounds as a codex spec: named read caps, exact
  deliverable filenames, commit-incrementally-with-prefix, no docs/ edits
  except deliverable paths the spec names exactly (a note draft assigned
  under the worker contract is such a deliverable), no pushes (the
  supervisor pushes after review), raw final report with a line cap.
- Workers commit locally; the supervisor reviews, then commits any
  supervisor-side artifacts (note, receipt) and pushes. Worker scripts are
  committed BEFORE their first certified run wherever recovery matters.

## Codex Worker Launch & Reliability (REQUIRED when using the codex profile)

`codex exec` workers hang or silently fail to deliver in two confirmed ways. Both
have a fix; apply all of the following every time.

**Launch recipe — close stdin and capture output:**

```bash
codex exec -s workspace-write -C "<repo-abs-path>" \
  -o /tmp/<task>_lastmsg.txt "$(cat /tmp/<task>_spec.md)" \
  < /dev/null > /tmp/<task>_full.log 2>&1 &
```

- `< /dev/null` is MANDATORY. With the prompt passed as an argument, `codex exec`
  still reads stdin to append it as a `<stdin>` block; a backgrounded job's stdin
  never reaches EOF, so the worker can block forever on
  `"Reading additional input from stdin..."` at 0% CPU with zero output. Closing
  stdin gives immediate EOF and prevents the start-hang.
- Pass the prompt as the argument (`"$(cat spec)"`); write the spec to a file first.

**Bound the reads — this is the #1 cause of "ran but never delivered":**

- Name the EXACT files the worker may read (≤ ~5). A worker told to "read the
  closure note + the ledger" dumps the multi-thousand-row `audit_ledger.json` into
  its context, exhausts it, and ends mid-reasoning having written nothing.
- NEVER instruct it to "read the ledger / read everything." For audit status, grep
  specific rows only: `git show "origin/main:docs/audit/data/ledger/<first-2-chars>/<claim_id>.json"` (the ledger is sharded per claim; the monolithic audit_ledger.json is an untracked local cache materialized by the pipeline).
- Tell it to WRITE THE DELIVERABLE INCREMENTALLY (write the output file as it goes,
  not held for a single final message) and to produce ONE focused deliverable plus
  a short stdout summary. Keep the task small and specific.

**Monitor + salvage (supervisor owns the result):**

- Hang signature: process at 0% CPU + log size growing-then-static + empty `-o`
  file. Check `ps -o %cpu=,etime= -p <pid>` and the `_full.log` size after a few
  minutes; do not assume "still working."
- If hung: kill it, salvage the reasoning from `_full.log` (it usually contains the
  analysis), and finish/deliver the result yourself. The supervising agent is
  responsible for the result regardless of worker failure.
- A tight, bounded spec (named files, incremental writes, one deliverable) is what
  makes the worker succeed; an open-ended "go read and figure it out" is what makes
  it hang or over-read.

## No-Go And Narrowing Discipline

When a task touches a no-go, obstruction, impossibility, or negative boundary,
read the actual primary note and its audited `claim_scope`. Plan against that
scope, not the title, reputation, or a secondary summary. If the prose is
broader than the audited support, queue or make a narrowing repair instead of
working around the mismatch silently.

## Lane Hand-Off

Review-loop and audit-loop are owner-operated lanes. A science command may
prepare a PR, review surface, runner cache, or audit targeting metadata for
those lanes, but it must hand off instead of running those lanes itself unless
the user explicitly invokes that lane.
