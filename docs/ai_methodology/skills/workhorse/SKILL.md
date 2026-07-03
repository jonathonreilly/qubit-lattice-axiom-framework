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

Use the strongest configured text reasoning worker available through the local
`codex exec` setup for bounded execution. If a named preferred worker profile is
unavailable, do not substitute an image, visual-generation, document-rendering,
or low-reasoning model. Use the strongest available text reasoning profile,
disclose the substitution in the work log, and keep the supervising agent
responsible for the result.

The supervising agent:

- reads current repo context and the relevant command/skill instructions;
- writes the task spec, allowed files, evidence bar, and stopping conditions;
- keeps claim-status, primitive/axiom/Tier-A, no-go, and audit boundaries
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
- add axioms, primitives, or Tier-A admissions;
- decide to land, merge, or close PRs;
- route science work through visual/image-generation tooling.

## Codex Worker Launch & Reliability (REQUIRED)

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
  specific rows only: `git show origin/main:docs/audit/data/audit_ledger.json | grep <claim_id>`.
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
