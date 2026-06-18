# Trace Gate

Required local checks:

```text
python3 scripts/frontier_d3_landau_peierls_single_band_normalization_2026_06_18.py
python3 scripts/cached_runner_output.py --refresh scripts/frontier_d3_landau_peierls_single_band_normalization_2026_06_18.py --timeout-sec 120 --tail-chars 4000
python3 scripts/frontier_d3_orbital_response_decomposition_2026_06_13.py
python3 scripts/cached_runner_output.py --refresh scripts/frontier_d3_orbital_response_decomposition_2026_06_13.py --timeout-sec 120 --tail-chars 4000
python3 scripts/cached_runner_output.py --check-only scripts/frontier_d3_landau_peierls_single_band_normalization_2026_06_18.py
python3 scripts/cached_runner_output.py --check-only scripts/frontier_d3_orbital_response_decomposition_2026_06_13.py
```
