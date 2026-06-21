# Assumptions And Imports

## Repo Inputs

- Cache references appear as text paths such as
  `logs/runner-cache/<name>.txt`.
- The cleanup command must not delete a cache file while another repo file
  still links to it.
- `logs/runner-cache/` itself is excluded from reference scanning so cache
  files do not self-protect through their own headers.

## Imports Avoided

- No claim truth, audit verdict, or retained status is imported.
- No cache files are deleted.
- No ledger rows are hand-edited.

## Open Imports

- The remaining 8 dry-run orphan candidates still need a later focused review
  before destructive cleanup is used.
