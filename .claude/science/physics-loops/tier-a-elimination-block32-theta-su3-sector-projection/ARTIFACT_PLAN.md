# Artifact Plan

- Add an exact-support note for the supplied SU(3) star central-sector
  projection.
- Add a runner that verifies the Heisenberg closure/cocycle law, matrix traces,
  conjugation invariance, scope guards, and absence of retirement wording.
- Cache the runner output under `logs/runner-cache/`.
- Run py_compile, audit pipeline, strict audit lint, and diff check.
- Commit, push, and open a stacked PR against Block31.
