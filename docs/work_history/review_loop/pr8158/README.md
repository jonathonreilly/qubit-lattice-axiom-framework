# PR8158 original recovery

Historical source and execution records, not current science or audit authority. The manifest preserves all22 original paths, modes, Git blobs and raw SHA-256 identities from head dd78e677ba6cda496d6de20cfc215ef8bd09374f against original delta df5316ee81d59d573b3837afb80d371d12d890d6. Decompress each content-addressed object to recover the exact original.

Original broad graph claims, the non-lattice triangular diagnostic, source runners, reviewer/refuter controls and outputs remain recoverable. Prior review/status assertions are historical only. Current-main history and scientific parents are preserved separately; this archive does not adopt the original claims.


## Stored payloads (moved out of the working tree, 2026-09-27)

The 22 hash-named payloads in `objects/` are no longer checked out. Git keeps each one byte for byte at tag `archive/work-history-payloads-20260927`, which points at main commit `7d2dc1a8b5`. The manifest in this folder still lists every original path, Git blob id and SHA-256; each payload's file name is the SHA-256 of its decoded content.

Read one payload:

```bash
git show archive/work-history-payloads-20260927:docs/work_history/review_loop/pr8158/objects/<sha256>.gz | gunzip
```

Restore the whole folder:

```bash
git checkout archive/work-history-payloads-20260927 -- docs/work_history/review_loop/pr8158/objects
```
