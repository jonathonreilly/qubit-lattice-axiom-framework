# CI workflows handoff — 2026-07-16

`CI_WORKFLOWS_2026-07-16.patch` carries the two workflow-file changes that the
agent credential (no `workflow` OAuth scope) cannot push:

1. `.github/workflows/audit.yml` — install `requirements-release.txt` (exact
   pins) instead of loose floors. Requires PR #5403 (pyyaml pin) landed first.
2. `.github/workflows/pr-smoke.yml` (new) — per-PR byte-compile of changed
   Python + audit-tooling unit tests when `docs/audit/scripts` changed.
   Read-only permissions, 15-minute cap, no auto-commit.

Apply from any environment with workflow scope:

    git checkout main && git pull
    git am path/to/CI_WORKFLOWS_2026-07-16.patch   # includes the requirements
                                                   # pin; resolve trivially if
                                                   # #5403 already landed
    git push

This branch is a handoff container only; do not merge it.
