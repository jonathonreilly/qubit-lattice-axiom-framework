# Review History

Local verification before PR:

- `python3 scripts/frontier_plaquette_beta6_perturbative_derivation_2026_05_27.py`
  -> `TOTAL: PASS=28 FAIL=0`
- `python3 scripts/cached_runner_output.py --refresh scripts/frontier_plaquette_beta6_perturbative_derivation_2026_05_27.py`
  -> cache refreshed
- `python3 scripts/cached_runner_output.py scripts/frontier_plaquette_beta6_perturbative_derivation_2026_05_27.py --check-only`
  -> fresh
- `git diff --check`
  -> clean
