# Artifact Plan

1. Add a source note scoped as `no_go`.
2. Add a verifier that checks source boundaries, registry invariance, exact
   weight-map algebra, determinant-order facts, fork bookkeeping, and no-go
   discipline.
3. Run the verifier and cache its output.
4. Run `py_compile`, audit pipeline, strict audit lint, and `git diff --check`.
5. Run milestone review and record pass/demote/block disposition.
6. Commit and push a stacked PR against block12.
