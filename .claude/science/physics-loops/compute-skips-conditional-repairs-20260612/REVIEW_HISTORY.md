# Review History

Self-checks run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_higgs_channel_effective_ntaste_boundary.py
PYTHONPATH=scripts python3 scripts/frontier_wilson_corrected_v_taste_tree_level.py
PYTHONPATH=scripts python3 scripts/frontier_observable_principle_p1_bridge_shannon_khinchin_external_narrow.py
python3 scripts/cached_runner_output.py --refresh --timeout-sec 120 scripts/frontier_higgs_channel_effective_ntaste_boundary.py
python3 scripts/cached_runner_output.py --refresh --timeout-sec 120 scripts/frontier_wilson_corrected_v_taste_tree_level.py
python3 scripts/cached_runner_output.py --refresh --timeout-sec 120 scripts/frontier_observable_principle_p1_bridge_shannon_khinchin_external_narrow.py
```

Results:

- Higgs-channel runner: `PASS=88 FAIL=0`.
- Wilson runner: `PASS=61 FAIL=0`.
- Observable-principle runner: `PASS=20 FAIL=0`.
