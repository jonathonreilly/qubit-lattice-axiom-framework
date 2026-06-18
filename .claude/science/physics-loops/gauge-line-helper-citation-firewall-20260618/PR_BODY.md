# Summary

Source-side repair for
`gauge_vacuum_plaquette_first_sector_minimal_bulk_completion_3plus1_line_helper_note_2026-04-19`.

The audit blocker says downstream citations must use this row only as
helper-interface authority, not as a derivation of the complement-line frame or
selector. This PR makes that boundary executable.

# What changed

- Added a `2026-06-18` citation/use firewall to the helper note.
- Clarified three direct source citations as helper-interface-only uses.
- Added runner checks for helper constants, line normalization/projection,
  live compression smoke behavior, source-note boundary markers, and direct
  citation qualifiers.
- Replaced the empty stdout cache with an executable `PASS=29 FAIL=0` cache.

# Verification

```bash
python3 scripts/frontier_gauge_vacuum_plaquette_first_sector_minimal_bulk_completion_3plus1_line_helper_2026_04_19.py
python3 scripts/cached_runner_output.py --refresh scripts/frontier_gauge_vacuum_plaquette_first_sector_minimal_bulk_completion_3plus1_line_helper_2026_04_19.py
python3 scripts/cached_runner_output.py --check-only scripts/frontier_gauge_vacuum_plaquette_first_sector_minimal_bulk_completion_3plus1_line_helper_2026_04_19.py
python3 -m py_compile scripts/frontier_gauge_vacuum_plaquette_first_sector_minimal_bulk_completion_3plus1_line_helper_2026_04_19.py
git diff --check
```

# Audit discipline

This PR does not audit, retag, or land anything. It does not edit audit result
files, publication effective-status files, front-door status, lane registry, or
the active review queue. Independent audit/review must decide whether this
source-side exact-support repair moves the existing row.
