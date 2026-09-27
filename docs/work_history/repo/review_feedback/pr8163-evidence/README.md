# Historical source and numerical recovery

This packet preserves all 165 original paths at `f950bab266a2c2c82321b49d94e21f0f8d2bcf61`, including their modes and blob identities. `archive-manifest.json` maps each original separately to an exact raw SHA-256 and stored payload. Compressed payloads are historical recovery only, not current runtime inputs or audit authority.

The three full working derivations and complete numerical history remain readable under `kept/`; their provisional wording is superseded by the canonical notes. Both the initial coarse-refinement failure and initially equivalent orientation mutation, all mutant sources and streams, and the 23 final specified formula-fault outcomes remain in the exact archive. No historical successful output is restamped as current-source evidence.

Canonical complete proofs:

- `docs/TEMPORAL_WILSON_RESUMMATION_PHYSICAL_CURL_BOUNDED_THEOREM_NOTE_2026-09-16.md`
- `docs/OPEN_BOUNDARY_WILSON_FOCK_MODEL_MATCH_BOUNDED_THEOREM_NOTE_2026-09-16.md`
- `docs/OPEN_WILSON_GAUGE_MATTER_FIXED_GRAPH_STATE_JOIN_BOUNDED_THEOREM_NOTE_2026-09-16.md`


## Stored payloads (moved out of the working tree, 2026-09-27)

The 105 hash-named payloads in `_objects/` are no longer checked out. Git keeps each one byte for byte at tag `archive/work-history-payloads-20260927`, which points at main commit `7d2dc1a8b5`. The manifest in this folder still lists every original path, Git blob id and SHA-256; each payload's file name is the SHA-256 of its decoded content.

Read one payload:

```bash
git show archive/work-history-payloads-20260927:docs/work_history/repo/review_feedback/pr8163-evidence/_objects/<sha256>.gz | gunzip
```

Restore the whole folder:

```bash
git checkout archive/work-history-payloads-20260927 -- docs/work_history/repo/review_feedback/pr8163-evidence/_objects
```
