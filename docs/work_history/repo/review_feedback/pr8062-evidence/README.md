# PR8062 original historical evidence

The manifest preserves every original path, mode, Git blob and decoded SHA-256. Gzip objects store exact historical bytes; kept files remain raw for the linked handoff and review history. Original review and mutation results are historical reports, not current source verdicts. Current canonical proofs and runner evidence are reviewed separately.

[Historical handoff](kept/pr8062-HANDOFF-9ef67db77ea9ef6f.md)


## Stored payloads (moved out of the working tree, 2026-09-27)

The 40 hash-named payloads in `_objects/` are no longer checked out. Git keeps each one byte for byte at tag `archive/work-history-payloads-20260927`, which points at main commit `7d2dc1a8b5`. The manifest in this folder still lists every original path, Git blob id and SHA-256; each payload's file name is the SHA-256 of its decoded content.

Read one payload:

```bash
git show archive/work-history-payloads-20260927:docs/work_history/repo/review_feedback/pr8062-evidence/_objects/<sha256>.gz | gunzip
```

Restore the whole folder:

```bash
git checkout archive/work-history-payloads-20260927 -- docs/work_history/repo/review_feedback/pr8062-evidence/_objects
```
