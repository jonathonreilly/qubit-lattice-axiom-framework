# Review setup and input hygiene

Required at the start of every branch or PR review, including named review-only runs. The [entry point](../SKILL.md) controls mode selection and scope; author pre-flight does not confer review standing.

## Author Pre-Flight (input hygiene)

Authors are expected to run [`PREFLIGHT.md`](../PREFLIGHT.md) before requesting
review. The pre-flight is authoring discipline, not a gate: it grants no
standing, replaces no reviewer lens, and its absence blocks nothing by
itself — but a reviewer may cite a skipped pre-flight item as a finding when
the defect it would have caught is present. Whether such findings are fixed
in place or the branch is rejected follows the existing Fix Policy and
close-with-reason path; the checklist adds no new disposition.

`docs/ai_methodology/REVIEW_LOOP_PR_CONFORMANCE_SPEC.md` is the pre-review
conformance bar the pre-flight serves: authors generate to it, and at review
entry the orchestrator pre-fixes a NARROW set of mechanical subchecks before
a reviewer seat is spent on the PR. The pre-fixable set is exactly:

- link resolution and repository portability (section 8's tracked-regular-file
  / web-URL requirement, and absolute or outside-repository link targets);
- field presence and enum validity in the machine-status and trace blocks
  (section 9), including a value drawn from the wrong enum family;
- removal of forbidden author-written audit outputs and regenerated audit
  surfaces (section 10);
- deterministic command and gate hygiene (section 12): running the focused
  linter, `py_compile`, and diff checks, and restoring identified generated
  residue. Full pipeline/lint/evidence checks follow the shared integrated
  [validation placement](REVIEW_UNITS.md), not an additional pre-review run per PR.

Everything else is scientific or dependency judgment and is NEVER pre-fixed
as mechanical: whether an added, removed, or rewired dependency edge is
INTENDED (section 8); which inputs are underivable, their provenance and role,
and which lane owns an open bridge (section 9); claim scope and the honest
boundary reading of section 3; proof content (section 5); runner logic and
validity (section 6); and sections 1, 2, 4, 7, and 11 entire. Those stay with
the reviewer, who is the only seat that may decide them.

Pre-fix is orchestrator repair of mechanical non-conformance under Fix Policy,
not a review: it confers no PASS, it does not shorten or replace any lens, and
nothing lands without a reviewer PASS on the final state.

## Setup

1. Read the local review/governance surfaces before judging status:
   - `docs/repo/REVIEW_FEEDBACK_WORKFLOW.md`
   - `docs/repo/ACTIVE_REVIEW_QUEUE.md`
   - `docs/repo/DEFERRED_DECISIONS.md` for owner-reserved scope exclusions
   - `docs/repo/CONTROLLED_VOCABULARY.md`
   - `docs/CANONICAL_HARNESS_INDEX.md`
   - `docs/audit/README.md`
   - `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md`
   - `docs/audit/data/axiom_premise_nodes.json` and the source notes named by
     relevant primitive nodes
   - `docs/audit/data/premise_decision_history.json`
   - `docs/KEY_SCIENCE.md` as the current front-of-house router when
     front-facing science changed; it is an index and grants no status
   - the relevant sharded rows under `docs/audit/data/ledger/` when
     quantitative, imported-value, or status-bearing claims changed
2. Determine the base ref:
   - prefer `origin/main` if present;
   - otherwise use `main`;
   - if the current branch is the base branch, use `HEAD~1`.
3. Compute the review base with `git merge-base HEAD <base-ref>`.
4. Build the original changed-file set from committed, staged, unstaged, and
   untracked changes. This is the primary review scope. Read necessary unchanged
   dependencies, callers, schemas, and policy sources from the same snapshot to
   judge those changes; record each contextual path and why it is needed. Context
   inspection does not authorize unrelated edits. If a confirmed fix requires
   another file, record the bounded scope expansion and review its new delta.
5. Record whether the worktree was initially clean. If it was dirty, do not
   auto-commit without explicit user permission unless the slash-command
   invocation clearly requested commit-producing fixes.
6. If the task is to review open/non-landed PRs, include all non-merged,
   non-draft PRs in the requested scope except PRs the user explicitly
   excluded or reserved. Draft PRs are out of scope by default; explicit
   owner-directed draft triage may inspect and close or mark them ready after
   exact-head verification. Mark-ready does not grant review PASS. A still-draft
   PR cannot land; a ready PR must satisfy all ordinary source/landing gates.
   Closed-but-unmerged PR heads can be inspected with `gh pr view` and
   `git fetch origin pull/<N>/head:refs/tmp/pr-<N>`.

Useful commands:

```bash
git diff --name-only <base>...HEAD
git diff --name-only --cached
git diff --name-only
git ls-files --others --exclude-standard
git diff <base>...HEAD -- <files>
git diff --cached -- <files>
git diff -- <files>
```

For untracked files, include their full content or a concise new-file summary
in reviewer prompts.
