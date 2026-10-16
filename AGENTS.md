# Agent instructions — planning branch

This orphan branch holds planning only and never merges into `main`.
`origin/main` is the authority for scientific source and applied audit status.

**The rules are on main:** read
`git show origin/main:docs/ai_methodology/SCIENCE_WORKFLOW.md`. Its evidence
rules, owner-settings table (cadence, PR type, audit deferral, reviewer models,
original mathematics) and stage table apply to all work dispatched from here.
This file adds only what is specific to planning and dispatch. Higher-priority
platform instructions and explicit user constraints control; report concrete
conflicts rather than inventing approval gates.

## Before assigning science

Read, from this branch: `TOE_SCORECARD.md` (as-of target map; check its
revision), `CAMPAIGN_STATUS.md` (assignments and current evidence),
`BACKLOG_STATUS.md` (authorized landing/triage actions) and the relevant
entries of `OPEN_PR_INVENTORY.json`. Search actual open-PR science as well as
main, and verify changed heads before reusing anything. None of these files
grants scientific status.

## Orchestrator and dispatch

- The orchestrator owns goal selection, integration and honest reporting. It
  maintains the shared status files; workers return evidence in assigned
  artifacts and do not rewrite shared status concurrently.
- Delegate concrete independent work when useful, sized to available capacity,
  not a fixed worker quota. Estimate total memory and compute across workers and
  choose sparse or reduced representations where needed.
- Every dispatch names: target, source revision, allowed paths, expected
  output, verification, and external-action permissions. An analysis dispatch is
  read-only outside its assigned output paths, with no implicit commit, push or
  network authority.
- A worker may explore alternatives inside its target and should challenge an
  infeasible spec rather than force the requested answer.
- Independent reviewers get raw artifacts and a neutral task, never the author's
  desired conclusion. They read the complete final source of each frozen unit
  and confirm corrections in the same session. Authors read their own complete
  diff before requesting review.

## Landing coordination

Follow current main's `docs/ai_methodology/skills/review-loop/SKILL.md` for
the executable contract. In short, before landing the coordinator:

- verifies the complete constituent and current-main path/claim disposition
  map, including deleted and inherited content and transitive premises (hashes
  alone do not prove completeness);
- reads every author correction diff, finding disposition and integration
  change relative to the frozen reviewed sources, and checks current main for
  science loss and cross-unit interactions;
- holds affected conclusions for the original reviewer when source bytes, a PR
  head, provenance or interactions change, reopening only the affected closure.

Reviewers do not perform GitHub mutations. Ready is a queue state, not
acceptance; a still-draft PR never lands. Only the independent audit path
writes verdicts.

## Evidence and recovery

- Runner output must be sufficient to inspect every claimed check; use
  `TOTAL: PASS=<n> FAIL=<n>` where the runner contract requires it.
- Use isolated worktrees, stage intended paths only, and preserve dirty or
  unpushed work on failure with recovery paths reported.
- Never import moving-main generated audit state into a stale science branch.
- Planning summaries and local memories are retrieval aids; confirm current
  source before citing them.

## Files on this branch

- `TOE_SCORECARD.md`, `CAMPAIGN_STATUS.md`, `BACKLOG_STATUS.md`: live planning.
- `OPEN_PR_INVENTORY.json`, `MAIN_STATUS_SNAPSHOT.json`: pinned snapshots.
- `BATCH_REVIEW_PLAN.md`, `NEXT_REVIEW_UNITS.json`,
  `BACKLOG_CONSOLIDATIONS.json`, `DRAFT_DISPOSITIONS.json`: backlog review
  records (no scientific PASS).
- `backlog_evidence/`: landing receipts and owner-direction evidence, e.g.
  `released18-20260910/RELEASED_TARGETS.json`.
- `REVIEWER_MODEL_PILOT.md`: the Astra-low vs Sol-xhigh comparison behind the
  current reviewer setting.
- `prompt_profiles/`, `PROMPT_REVIEW_2026-09-07.md`: local prompt profiles.
- `README.md`: branch contract and edit flow. `history/`: superseded material.
