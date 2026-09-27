# Scientific recovery for PR8075

The manifest maps every preserved source/data path to its original commit, Git mode/blob and decoded SHA-256. Objects use deterministic gzip; decode the named object and verify its SHA-256 before use. These exact historical scientific bytes support the current independent source review. Installed/system runtime hashes remain explicitly external historical environment provenance. This recovery does not execute old workers or grant a review/audit verdict.


## Stored payloads (moved out of the working tree, 2026-09-27)

The 4769 hash-named payloads in `objects/` are no longer checked out. Git keeps each one byte for byte at tag `archive/work-history-payloads-20260927`, which points at main commit `7d2dc1a8b5`. The manifest in this folder still lists every original path, Git blob id and SHA-256; each payload's file name is the SHA-256 of its decoded content.

Read one payload:

```bash
git show archive/work-history-payloads-20260927:docs/work_history/repo/review_feedback/pr8075-evidence/scientific-recovery/objects/<sha256>.gz | gunzip
```

Restore the whole folder:

```bash
git checkout archive/work-history-payloads-20260927 -- docs/work_history/repo/review_feedback/pr8075-evidence/scientific-recovery/objects
```
