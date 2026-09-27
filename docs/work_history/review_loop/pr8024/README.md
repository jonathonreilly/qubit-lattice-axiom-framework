# PR8024 original recovery

Historical source and execution records, not current science or audit authority. The manifest binds all 75 original paths, modes, blobs and SHA-256 identities from PR8024 head 1c814b95243c5f788f57bab57c67fdc542f1aab4 against its original pre-retarget delta base 4c3b9bd33bfbc2e03b9d91e05849607bc33ec70c. Decompress each content-addressed object to recover its exact original bytes.

The volume-uniform gap note retains the complete canonical argument and both finite-carrier and penalized-register supplements. The 71 original packet files retain prior derivations, controls, corrections, reviews and validation history. Existing main parent notes remain unchanged. Original cache and generated citation manifest are historical only; current evidence is captured separately.


## Stored payloads (moved out of the working tree, 2026-09-27)

The 73 hash-named payloads in `objects/` are no longer checked out. Git keeps each one byte for byte at tag `archive/work-history-payloads-20260927`, which points at main commit `7d2dc1a8b5`. The manifest in this folder still lists every original path, Git blob id and SHA-256; each payload's file name is the SHA-256 of its decoded content.

Read one payload:

```bash
git show archive/work-history-payloads-20260927:docs/work_history/review_loop/pr8024/objects/<sha256>.gz | gunzip
```

Restore the whole folder:

```bash
git checkout archive/work-history-payloads-20260927 -- docs/work_history/review_loop/pr8024/objects
```
