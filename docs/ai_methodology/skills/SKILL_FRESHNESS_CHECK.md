# Skill Freshness Check

Before using any repo methodology skill, make a best-effort check for a newer
skill body.

Every repo methodology `SKILL.md` must include a `## Skill Freshness` section
that points to this file before its workflow-specific instructions. This applies
to review-loop, audit-loop, physics-loop, no-go-discipline, reviewer skills,
and any future repo skill. A skill that cannot safely complete this check must
state that freshness could not be verified before continuing.

1. If `origin/main` is reachable, run `git fetch origin main`.
2. If the current worktree is clean and can be safely fast-forwarded, update it
   before continuing.
3. If the worktree is dirty, detached in a way that should not be moved, ahead
   of `origin/main`, or otherwise cannot be fast-forwarded safely, do not modify
   it just to refresh a skill. Read the latest skill text directly with
   `git show origin/main:docs/ai_methodology/skills/<skill>/SKILL.md` and follow
   that version for the current task.
4. If `origin/main` cannot be reached, continue with the local skill and state
   that freshness could not be checked.
5. Never discard user work, overwrite local edits, or force-reset a worktree as
   part of the freshness check.
