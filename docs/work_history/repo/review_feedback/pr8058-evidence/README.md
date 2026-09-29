# Historical evidence

The manifest maps every frozen original path and mode to its exact payload. Gzip objects decompress to the recorded raw SHA-256. Selected current targets remain plain files; all consumer updates require review. Original links inside historical copies retain their original layout. Equal bytes permit one payload read, not reuse of a scientific conclusion across different premises.


## Stored payloads (moved out of the working tree, 2026-09-27)

The 74 hash-named payloads in `_objects/` are no longer checked out. Git keeps each one byte for byte at tag `archive/work-history-payloads-20260927`, which points at main commit `7d2dc1a8b5`. The manifest in this folder still lists every original path, Git blob id and SHA-256; each payload's file name is the SHA-256 of its decoded content.

Read one payload:

```bash
git show archive/work-history-payloads-20260927:docs/work_history/repo/review_feedback/pr8058-evidence/_objects/<sha256>.gz | gunzip
```

Restore the whole folder:

```bash
git checkout archive/work-history-payloads-20260927 -- docs/work_history/repo/review_feedback/pr8058-evidence/_objects
```
