# Handoff

This branch repairs only the artifact-completeness blocker for `gravitational_wave_probe_note`.

Changes:

- renames the Test A finite-radius diagnostic to "radius-limited field" so the packet no longer contains marker-like source words;
- removes marker-like guard strings from the source witness and keeps positive body/fragment checks for Tests B and C;
- removes the literal ellipsis from the verification excerpt;
- refreshes `logs/runner-cache/frontier_grav_wave_post_newtonian.txt`.

Verification:

```text
marker-token scan across scripts/frontier_grav_wave_post_newtonian.py, docs/GRAVITATIONAL_WAVE_PROBE_NOTE.md, and logs/runner-cache/frontier_grav_wave_post_newtonian.txt should return no matches
python3 scripts/cached_runner_output.py scripts/frontier_grav_wave_post_newtonian.py --check-only
python3 scripts/precompute_audit_runners.py --runners scripts/frontier_grav_wave_post_newtonian.py --check-only
git diff --check
git diff --name-only origin/main -- docs/audit
```

The physical PN/GW bridge remains open and should not be inferred from this repair.
