# Assumptions And Imports

## Repo Inputs

- Historical runner paths may be absolute paths from old worktrees.
- Some runner paths live below nested directories such as
  `scripts/corrections/`.
- If an absolute path contains a `scripts/...` suffix and that suffix exists
  in the current checkout, the suffix is the best canonical repo-local path.

## Imports Avoided

- No audit verdicts or claim statuses are changed.
- No ledger rows are hand-edited.
- No claim truth is imported.

## Open Imports

- The canonicalizer copies remain duplicated across three scripts. This block
  keeps the change local and synchronized rather than adding a broader shared
  module refactor inside the audit-unblock stack.
