# Summary

Source-side repair for `connectivity_family_v2_elliptical_duplicate_note`.

The audited conditional blocker says the note's row inventory is stale relative
to the current cache: the old `drift = 0.02, seed = 0` row is not run, and the
cache reports `25/45` passes across the 45-row sweep. This PR refreshes the
source note to the current cache and removes the stale targeted-slice narrative.

# What changed

- Replaced missing absolute-path log/script references with current repo links.
- Recorded the current 45-row cached sweep and pass/fail seeds by drift.
- Explicitly retired the stale `drift = 0.02, seed = 0` row from the evidence
  surface.
- Kept the claim narrow: bounded duplicate-boundary diagnostic, not a new
  independent family.

# Verification

```bash
python3 scripts/cached_runner_output.py --check-only scripts/CONNECTIVITY_FAMILY_V2_ELLIPTICAL_SWEEP.py
git diff --check
```

# Audit discipline

This PR does not audit, retag, or land anything. It does not edit audit result
files, publication effective-status files, front-door status, lane registry, or
the active review queue.
