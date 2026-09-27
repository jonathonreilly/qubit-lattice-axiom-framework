# PR8069 original source and evidence

archive-manifest.json binds every original path, mode, Git blob and decoded SHA-256. All original manifest hash consumers remain raw in kept/; other original payloads use exact gzip objects. Original internal source paths and receipt hashes describe their historical execution context. Current runtime path keys are mapped separately in the canonical input manifest, without modifying original payloads.

Historical reviews and ACCEPTED statuses are provenance, not current scientific authority. The canonical proof and exact source/arithmetic review determine the bounded claim; the primary executes saved-certificate consistency checks only.


## Stored payloads (moved out of the working tree, 2026-09-27)

The 66 hash-named payloads in `_objects/` are no longer checked out. Git keeps each one byte for byte at tag `archive/work-history-payloads-20260927`, which points at main commit `7d2dc1a8b5`. The manifest in this folder still lists every original path, Git blob id and SHA-256; each payload's file name is the SHA-256 of its decoded content.

Read one payload:

```bash
git show archive/work-history-payloads-20260927:docs/work_history/repo/review_feedback/pr8069-evidence/_objects/<sha256>.gz | gunzip
```

Restore the whole folder:

```bash
git checkout archive/work-history-payloads-20260927 -- docs/work_history/repo/review_feedback/pr8069-evidence/_objects
```
