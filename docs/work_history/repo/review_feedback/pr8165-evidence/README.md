# Historical compact rotor source recovery

All 88 original paths at `c228dbcfc0a6b71639316915f460c32dbf479723` retain their separate modes, Git blobs and raw SHA-256 identities in `archive-manifest.json`. Four complete proofs and the historical scope/review records remain readable under `kept/`; deterministic payloads preserve the three calculations and all development sources, streams and eleven mutation histories. This is historical provenance, not current execution evidence or audit authority.

The Fourier32/48 attempt failed its unchanged 1e-10 tolerance; Fourier48/64, further diagnostic cutoffs and finite differences are preserved without turning them into a rigorous tail enclosure. The coarse-current before-timeout source also precedes its independent witness-loss assertion. All stronger provisional wording remains recoverable. Formal negative-packet certification lacks five qualifying routes and remains deferred; the canonical notes state positive conditional results and retain exact finite counterexamples.

Canonical complete proofs:

- `docs/COMPACT_ROTOR_SAMPLED_MAGNETIC_EVENT_BOUNDED_THEOREM_NOTE_2026-09-16.md`
- `docs/COMPACT_ROTOR_MAGNETIC_EXCURSION_BOUNDED_THEOREM_NOTE_2026-09-16.md`
- `docs/COMPACT_ROTOR_SPATIAL_GROUND_PATH_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-16.md`
- `docs/COMPACT_ROTOR_TEMPORAL_OSCILLATION_COARSE_CURRENT_BOUNDED_THEOREM_NOTE_2026-09-16.md`


## Stored payloads (moved out of the working tree, 2026-09-27)

The 57 hash-named payloads in `_objects/` are no longer checked out. Git keeps each one byte for byte at tag `archive/work-history-payloads-20260927`, which points at main commit `7d2dc1a8b5`. The manifest in this folder still lists every original path, Git blob id and SHA-256; each payload's file name is the SHA-256 of its decoded content.

Read one payload:

```bash
git show archive/work-history-payloads-20260927:docs/work_history/repo/review_feedback/pr8165-evidence/_objects/<sha256>.gz | gunzip
```

Restore the whole folder:

```bash
git checkout archive/work-history-payloads-20260927 -- docs/work_history/repo/review_feedback/pr8165-evidence/_objects
```
