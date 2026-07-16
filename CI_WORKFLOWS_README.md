# CI workflows handoff — 2026-07-16

`CI_WORKFLOWS_2026-07-16.patch` carries EXACTLY TWO files — the workflow
changes that the agent credential (no `workflow` OAuth scope) cannot push:

1. `.github/workflows/audit.yml` — install `requirements-release.txt` (exact
   pins) instead of loose floors. The pyyaml pin and the copy-over template
   (`docs/audit/templates/audit_workflow.yml`) land separately via PR #5403,
   which is a **prerequisite**: apply this patch only after #5403 is on main,
   or the nightly will miss pyyaml (needed by the vocabulary/render tooling
   under `scripts/`, not by the audit pipeline itself).
2. `.github/workflows/pr-smoke.yml` (new) — per-PR byte-compile of changed
   Python + audit-tooling unit tests when `docs/audit/scripts/**` changes
   (trigger includes the shell tooling, e.g. `run_pipeline.sh`). Change
   detectors are captured fail-closed outside conditionals (a failing
   git diff aborts the step rather than selecting the skip branch); the
   multi-command run steps set bash + pipefail; unittest output is never
   piped. Read-only permissions; 15-minute cap; no auto-commit.

The patch does NOT include the requirements pin — that is PR #5403.

Apply from any environment with workflow scope, after #5403 lands:

    git checkout main && git pull
    git show origin/handoff/ci-workflows-20260716:CI_WORKFLOWS_2026-07-16.patch | git am
    git push

This branch is a handoff container only; do not merge it.
