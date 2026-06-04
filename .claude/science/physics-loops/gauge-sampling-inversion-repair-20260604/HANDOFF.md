# Handoff

## Summary

This branch repairs the sampling-inversion runner's stale support assertion
against the repaired scalar-value insufficiency note.

The runner previously searched for the old phrase:

```text
one scalar framework-point value does not determine the class-sector vector
```

The repaired scalar no-go note now states the narrower formal lemma. The runner
now checks the current stable phrases:

```text
one scalar constraint does not determine
a scalar plaquette value alone cannot be treated as full class-sector data
```

## Verification

```bash
PYTHONPATH=scripts python3 scripts/frontier_gauge_vacuum_plaquette_retained_class_sampling_inversion_2026_04_17.py
python3 scripts/cached_runner_output.py --refresh scripts/frontier_gauge_vacuum_plaquette_retained_class_sampling_inversion_2026_04_17.py
python3 scripts/cached_runner_output.py --check-only scripts/frontier_gauge_vacuum_plaquette_retained_class_sampling_inversion_2026_04_17.py
python3 -m py_compile scripts/frontier_gauge_vacuum_plaquette_retained_class_sampling_inversion_2026_04_17.py
git diff --check
```

Expected summary:

```text
THEOREM PASS=6 SUPPORT=3 FAIL=0
```

## Remaining Open Gates

- Independent audit must re-audit the same finite-inversion row.
- Beta=6 PF selector closure remains separate.
