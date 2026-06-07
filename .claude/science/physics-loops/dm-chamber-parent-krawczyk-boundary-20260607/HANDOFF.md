# Handoff

## What Changed

This repair demotes the DM PMNS chamber parent from an exact completeness
theorem to a bounded listed-root support packet. The computation still
supports the same three chamber survivors, but the note and runner now admit
that the global no-other-roots side remains unproved.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/frontier_dm_pmns_chamber_spectral_completeness_theorem_2026_04_20.py
```

Result: `PASS=11 FAIL=0`

```bash
PYTHONPATH=scripts python3 scripts/frontier_dm_pmns_chamber_spectral_completeness_krawczyk_certificate_2026_05_16.py
```

Result: `PASS=18 FAIL=0`

```bash
python3 scripts/cached_runner_output.py --refresh scripts/frontier_dm_pmns_chamber_spectral_completeness_theorem_2026_04_20.py
```

Result: cache refreshed cleanly.

## Reviewer Notes

Dependent source notes that consumed the old parent as exact chamber
completeness may need follow-up boundary repairs. This PR intentionally keeps
the change scoped to the parent packet and its runner so the reviewer can
extract the source demotion cleanly.
