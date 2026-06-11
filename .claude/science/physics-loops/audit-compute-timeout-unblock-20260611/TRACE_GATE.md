# Trace Gate

Verification commands run:

```bash
python3 scripts/frontier_higgs_mass_derived.py
python3 scripts/cached_runner_output.py scripts/frontier_higgs_mass_derived.py --refresh --timeout-sec 60 --tail-chars 2600
python3 scripts/cached_runner_output.py scripts/frontier_higgs_mass_derived.py --check-only

python3 scripts/frontier_dm_full_closure_same_surface_thermal_bounding_theorem.py
python3 scripts/cached_runner_output.py scripts/frontier_dm_full_closure_same_surface_thermal_bounding_theorem.py --refresh --timeout-sec 60 --tail-chars 2600
python3 scripts/cached_runner_output.py scripts/frontier_dm_full_closure_same_surface_thermal_bounding_theorem.py --check-only
```

Observed outcomes:

- Higgs runner: `Global PASS/FAIL: 7 passed, 0 failed`; refreshed cache
  `elapsed_sec: 1.15`, timeout `60`.
- DM thermal runner: `SUMMARY: PASS=25 FAIL=0`; refreshed cache
  `elapsed_sec: 34.83`, timeout `60`.
