# Review History

- Added a restricted transitive source-packet manifest for the Wave direct-dM
  Fam2 seed1 row.
- Planned verification:
  - py-compile manifest
  - run manifest, expecting zero failures
  - precompute check-only for manifest cache
  - `git diff --check`
  - `git diff -- docs/audit` must be empty
