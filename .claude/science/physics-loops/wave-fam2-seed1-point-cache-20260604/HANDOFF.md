# Handoff

This PR repairs the row-specific cache problem for
`wave_direct_dm_h025_fam2_seed1_followup_note`.

The new runner fixes `Fam2`, seed `1`, `H = 0.25`, `S = 0.004`, recomputes the
archived observables, writes a JSON certificate, and checks that the relevant
control/synthesis artifacts are present.

Expected verification:

```bash
python3 -m py_compile scripts/wave_direct_dm_h025_point_runner.py scripts/wave_direct_dm_h025_fam2_seed1_point_runner_2026_06_04.py
python3 scripts/cached_runner_output.py --refresh scripts/wave_direct_dm_h025_fam2_seed1_point_runner_2026_06_04.py
python3 scripts/cached_runner_output.py --check-only scripts/wave_direct_dm_h025_fam2_seed1_point_runner_2026_06_04.py
git diff --check origin/main..HEAD
```

Expected summary:

```text
SUMMARY: WAVE H025 FAM2 SEED1 PASS=27 FAIL=0
```

This branch does not touch `docs/audit/**` and does not retag the ledger.
