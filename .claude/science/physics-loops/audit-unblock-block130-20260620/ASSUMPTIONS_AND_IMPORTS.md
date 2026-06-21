# Assumptions And Imports

## Repo Inputs

- Runner-cache files are keyed by runner stem: `logs/runner-cache/<stem>.txt`.
- A cache header records the authoritative runner path as `runner: ...`.
- `scripts/runner_cache.py::parse_cache_header` is the existing parser for
  cache metadata.
- `scripts/precompute_audit_runners.py::canonical_runner_path` and
  `runner_file_path` are the existing path normalization helpers.

## Imports Avoided

- No claim truth, audit verdict, or retained status is imported.
- No ledger row is changed by hand.
- No orphan cache file is deleted in this block.

## Open Imports

- The remaining 9 dry-run orphan candidates require later review before any
  destructive cleanup command is used.
