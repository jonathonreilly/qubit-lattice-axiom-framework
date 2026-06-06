# Handoff

This branch repairs explicit source dependency edges for the cosmology cascade.

Files:

- `docs/COSMOLOGY_FROM_MASS_SPECTRUM_NOTE.md`
- `scripts/frontier_cosmology_from_mass_spectrum.py`
- `logs/runner-cache/frontier_cosmology_from_mass_spectrum.txt`

Check:

```text
python3 scripts/cached_runner_output.py scripts/frontier_cosmology_from_mass_spectrum.py --check-only
```

No audit files are edited. Eta and alpha_GUT/Sommerfeld remain open.

