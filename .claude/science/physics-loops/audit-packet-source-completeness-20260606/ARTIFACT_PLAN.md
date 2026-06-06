# Artifact Plan

- Add explicit source character limits in `scripts/codex_audit_runner.py`.
- Raise primary and helper source limits to `120_000`.
- Add a regression test proving sources above the old limits render without
  truncation markers.
- Keep generated audit data out of the PR.
