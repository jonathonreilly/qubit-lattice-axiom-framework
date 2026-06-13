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
