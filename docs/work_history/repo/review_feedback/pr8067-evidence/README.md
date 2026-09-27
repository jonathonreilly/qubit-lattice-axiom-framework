# PR8067 original historical evidence

archive-manifest.json preserves all original paths, modes, Git blobs and decoded SHA-256 values. Objects are exact historical bytes; retained handoff/review reports are provenance only.

[Original handoff](kept/pr8067-HANDOFF-9ef67db77ea9ef6f.md)


## Stored payloads (moved out of the working tree, 2026-09-27)

The 60 hash-named payloads in `_objects/` are no longer checked out. Git keeps each one byte for byte at tag `archive/work-history-payloads-20260927`, which points at main commit `7d2dc1a8b5`. The manifest in this folder still lists every original path, Git blob id and SHA-256; each payload's file name is the SHA-256 of its decoded content.

Read one payload:

```bash
git show archive/work-history-payloads-20260927:docs/work_history/repo/review_feedback/pr8067-evidence/_objects/<sha256>.gz | gunzip
```

Restore the whole folder:

```bash
git checkout archive/work-history-payloads-20260927 -- docs/work_history/repo/review_feedback/pr8067-evidence/_objects
```
