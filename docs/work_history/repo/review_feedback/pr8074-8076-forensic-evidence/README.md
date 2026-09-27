# Recovered original PR8074–8076 scientific evidence

The [recovery manifest](recovery-manifest.json) preserves every selected original commit/path, Git mode/blob, raw SHA-256 and provenance role. Gzip objects are exact byte-preserving recovery storage; repeated content shares an object while every original mapping remains distinct. The selection includes the original declared inputs and required independent saved-stage/checker evidence, and excludes unrelated checkpoint75 consequences listed in the manifest.

These payloads preserve the source and saved numerical evidence reviewed for the fixed-family claims. Historical acceptance text is not a new review or audit verdict. The current compact runners do not rerun the native array calculations or execute these compressed objects; current supporting mathematical derivations and actual compact inputs remain raw and directly linked in their canonical notes.


## Stored payloads (moved out of the working tree, 2026-09-27)

The 19986 hash-named payloads in `_objects/` are no longer checked out. Git keeps each one byte for byte at tag `archive/work-history-payloads-20260927`, which points at main commit `7d2dc1a8b5`. The manifest in this folder still lists every original path, Git blob id and SHA-256; each payload's file name is the SHA-256 of its decoded content.

Read one payload:

```bash
git show archive/work-history-payloads-20260927:docs/work_history/repo/review_feedback/pr8074-8076-forensic-evidence/_objects/<sha256>.gz | gunzip
```

Restore the whole folder:

```bash
git checkout archive/work-history-payloads-20260927 -- docs/work_history/repo/review_feedback/pr8074-8076-forensic-evidence/_objects
```
