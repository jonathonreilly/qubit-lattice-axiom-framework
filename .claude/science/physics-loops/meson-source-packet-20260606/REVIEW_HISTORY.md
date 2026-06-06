# Review History

- Added a restricted source-packet manifest for the existing meson primary
  runner/cache.
- Planned verification:
  - py-compile manifest
  - run manifest, expecting zero failures
  - precompute check-only for manifest cache
  - `git diff --check`
  - `git diff -- docs/audit` must be empty
