# Artifact Plan

- Add a branch-local gate document under `docs/`.
- Add a runner that mechanically checks the gate rows, source coverage, status
  firewalls, and unbounded-family-lift blocker.
- Cache the runner output under `logs/runner-cache/`.
- Keep all authority, audit, and registry surfaces untouched.
