# Artifact Plan

- Add a source note documenting the SU(3) star pairwise-reduction
  obstruction.
- Add a runner that verifies the finite Heisenberg-subgroup witness,
  matrix-level class data, scope guards, and absence of retirement wording.
- Cache the runner output under `logs/runner-cache/`.
- Run py_compile, audit pipeline, strict audit lint, and diff check.
- Commit, push, and open a stacked PR against Block30.
