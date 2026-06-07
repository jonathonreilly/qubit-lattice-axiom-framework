## Summary

- Demotes the DM PMNS chamber parent from exact compact completeness to
  bounded listed-root support.
- Preserves the eight listed reduced-system roots and the three listed
  chamber survivors.
- Aligns the parent with the May 16 Krawczyk companion: existence/local
  uniqueness and chamber sign are certified for the listed boxes, while the
  upper-bound/no-other-roots side remains open.
- Refreshes the parent runner cache.

## Verification

- `PYTHONPATH=scripts python3 scripts/frontier_dm_pmns_chamber_spectral_completeness_theorem_2026_04_20.py`
- `PYTHONPATH=scripts python3 scripts/frontier_dm_pmns_chamber_spectral_completeness_krawczyk_certificate_2026_05_16.py`
- `python3 scripts/cached_runner_output.py --refresh scripts/frontier_dm_pmns_chamber_spectral_completeness_theorem_2026_04_20.py`
- `git diff -- docs/audit`
