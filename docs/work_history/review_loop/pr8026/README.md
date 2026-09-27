# PR8026 original recovery

Historical source and execution records, not current science or audit authority. The manifest binds all 87 original paths, modes, blobs and SHA-256 identities from head 08d312cdbb643ff661f2abd8b8489bcf0997ba7f against original delta cf104c1e69c971f37bdca51f775a6165f9f57133. Decompress each content-addressed object to recover its exact original bytes.

The canonical note retains both complete mathematical derivations. The 79 original packet files preserve alternate root and primary proofs, the incorrect Haar-index checker and spuriously passing output, subsequent repairs, prospective plans, raw controls and prior review/validation history. Original caches, generated manifest and stale tool versions are recovery only. Current source maps preserve current-main entries; fresh evidence is captured separately.


## Stored payloads (moved out of the working tree, 2026-09-27)

The 81 hash-named payloads in `objects/` are no longer checked out. Git keeps each one byte for byte at tag `archive/work-history-payloads-20260927`, which points at main commit `7d2dc1a8b5`. The manifest in this folder still lists every original path, Git blob id and SHA-256; each payload's file name is the SHA-256 of its decoded content.

Read one payload:

```bash
git show archive/work-history-payloads-20260927:docs/work_history/review_loop/pr8026/objects/<sha256>.gz | gunzip
```

Restore the whole folder:

```bash
git checkout archive/work-history-payloads-20260927 -- docs/work_history/review_loop/pr8026/objects
```
