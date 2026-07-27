# Artifact plan

1. Add role-scoped live markdown links to the target note.
2. Validate the citation graph against the latest `origin/main`, then require
   its regenerated manifest in the eventual latest-base landing set.  Do not
   land a manifest generated from this 17-commit-old worktree.
3. Run the target harness and repository vocabulary lint.
4. Run a local review-loop pass and record its disposition.
