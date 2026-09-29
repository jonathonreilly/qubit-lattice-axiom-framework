# Ward certificate scientific input recovery

This directory preserves relevant source and arithmetic payloads for the finite-moment, posterior, correlated, Gaussian-jet and quartic constructions. The [manifest](manifest.json) records original absolute paths, SHA-256 identities, Git recovery provenance and storage locations. Storage paths are repository-relative; `.gz` objects decode to the specified original bytes. Existing exact objects are reused from earlier landed recovery archives.

These are current supporting inputs, not autonomous claims or current execution receipts. Historical resource and acceptance records retain their original meaning. Current compact runners do not re-execute the catalog, moment workers or saved-data estimator. Negative certification is deferred as described in the canonical notes; preserving its original evidence does not close that work. Unrelated umbrella freeze members are not asserted to be load-bearing.


## Stored payloads (moved out of the working tree, 2026-09-27)

The 4197 hash-named payloads in `objects/` are no longer checked out. Git keeps each one byte for byte at tag `archive/work-history-payloads-20260927`, which points at main commit `7d2dc1a8b5`. The manifest in this folder still lists every original path, Git blob id and SHA-256; each payload's file name is the SHA-256 of its decoded content.

Read one payload:

```bash
git show archive/work-history-payloads-20260927:docs/work_history/repo/review_feedback/pr8079-8083-scientific-recovery/objects/<sha256>.gz | gunzip
```

Restore the whole folder:

```bash
git checkout archive/work-history-payloads-20260927 -- docs/work_history/repo/review_feedback/pr8079-8083-scientific-recovery/objects
```
