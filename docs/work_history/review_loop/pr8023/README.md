# Original compact-cube cutoff review history

**Type:** meta

The [manifest](original-manifest.json) preserves every original path, mode, Git blob and decoded SHA-256 from PR #8023 at `4c3b9bd33bfbc2e03b9d91e05849607bc33ec70c`. Payloads are deterministic gzip objects; decode the named object with `gzip -dc` to recover the exact original bytes. Identical bytes share storage while every original path retains its own entry.

This is historical recovery material, including earlier proofs, controls, failed executions, certificates and generated outputs. It grants no scientific or audit status. The two canonical cutoff and spectral-enclosure notes contain the current complete arguments; existing corrected main sources remain authoritative over superseded branch versions. No active proof or runtime input is replaced by a compressed payload.


## Stored payloads (moved out of the working tree, 2026-09-27)

The 384 hash-named payloads in `objects/` are no longer checked out. Git keeps each one byte for byte at tag `archive/work-history-payloads-20260927`, which points at main commit `7d2dc1a8b5`. The manifest in this folder still lists every original path, Git blob id and SHA-256; each payload's file name is the SHA-256 of its decoded content.

Read one payload:

```bash
git show archive/work-history-payloads-20260927:docs/work_history/review_loop/pr8023/objects/<sha256>.gz | gunzip
```

Restore the whole folder:

```bash
git checkout archive/work-history-payloads-20260927 -- docs/work_history/review_loop/pr8023/objects
```
