# Handoff

Branch: `physics-loop/dm-neutrino-weak-triplet-live-boundary-20260608`

Target claim:
`dm_neutrino_weak_triplet_coefficient_axiom_boundary_note_2026-04-15`

What changed:

- Added a live source note under `docs/`.
- Updated the runner's boundary source read to use the live note.
- Refreshed the runner cache.
- Left the archived stale note as provenance only.
- Did not edit audit outputs.

Verification:

```text
python3 scripts/cached_runner_output.py --refresh scripts/frontier_dm_neutrino_weak_triplet_coefficient_axiom_boundary.py --tail-chars 2500
python3 scripts/cached_runner_output.py --check-only scripts/frontier_dm_neutrino_weak_triplet_coefficient_axiom_boundary.py
python3 -m py_compile scripts/frontier_dm_neutrino_weak_triplet_coefficient_axiom_boundary.py
```

Result: fresh cache, `SUMMARY: PASS=14 FAIL=0`.

Remaining boundary:

No source-amplitude law, exact benchmark rebuild, or effective retained status
is claimed.
