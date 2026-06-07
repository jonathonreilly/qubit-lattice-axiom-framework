# Handoff

Branch-local result:

- The target-specific wave runner now checks that the note links the target
  runner/cache/JSON, generic point runner/cache, matched-history helper/cache,
  continuum helper/cache, source-packet manifest cache, and manifest JSON.
- It verifies the `measure_dm` source calls through `solve_wave`, `prop_beam`,
  and `cz`.
- It verifies the continuum helper source includes `field_at`, `prop_beam`,
  `cz`, `solve_wave`, `grow`, and `S_PHYS = 0.004`.
- It verifies helper caches are SHA-fresh and clean-exit.
- It verifies the manifest cache/JSON report zero failures.

Verification:

```bash
python3 -m py_compile scripts/wave_direct_dm_h025_fam2_seed1_point_runner_2026_06_04.py scripts/wave_direct_dm_h025_fam2_seed1_source_packet_manifest_2026_06_06.py
PYTHONPATH=scripts python3 scripts/cached_runner_output.py --check-only scripts/wave_direct_dm_h025_fam2_seed1_point_runner_2026_06_04.py
PYTHONPATH=scripts python3 scripts/cached_runner_output.py --check-only scripts/wave_direct_dm_h025_fam2_seed1_source_packet_manifest_2026_06_06.py
git diff --check
```

Remaining blocker:

Independent audit must decide whether this repaired restricted packet is
sufficient. This PR does not retag the ledger.

Next campaign action:

Re-scan the latest conditional backlog on `origin/main`; the next easy packet
repair appears exhausted, so prioritize hard bridge candidates.
