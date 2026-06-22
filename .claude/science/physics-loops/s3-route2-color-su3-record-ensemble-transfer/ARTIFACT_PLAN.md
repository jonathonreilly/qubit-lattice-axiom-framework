# Artifact Plan

## Block82

- Add a no-go/support-boundary note under `docs/`.
- Add a runner that verifies the transfer boundary and reachability graph.
- Cache the runner output under `outputs/`.
- Add branch-local loop state and handoff files.
- Run scoped verification only; do not run audits.
- Commit, push the science branch, and open a stacked PR.
