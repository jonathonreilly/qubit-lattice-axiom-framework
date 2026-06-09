# Dimension Poisson Native Profiles Handoff

## Summary

This branch converts the dimension lower-bound note's standard Poisson Green
profile import into a runner-native proof. The new certificate proves
`Delta_d f_d = 0` away from the source, radius-independent shell flux, and the
derivative sign transition for the exact profile family used by
`frontier_dimension_selection.py`.

## Scope

- Removes textbook authority for the radial identities.
- Keeps textbooks as parallel references only.
- Keeps the finite runner's analytic potential-family choice bounded.
- Does not promote `DIMENSION_SELECTION_NOTE.md` or claim unique D=3 selection.
- Does not edit audit-result files.

## Verification

- `python3 scripts/dimension_selection_poisson_profile_native_proof_2026_06_09.py` -> `SUMMARY: PASS=37 FAIL=0`
- `python3 scripts/cached_runner_output.py --refresh scripts/dimension_selection_poisson_profile_native_proof_2026_06_09.py` -> `status: ok`
- `python3 scripts/cached_runner_output.py --refresh scripts/frontier_dimension_selection.py` -> `status: ok`
- `python3 scripts/cached_runner_output.py --refresh scripts/frontier_dimension_selection_lower_bound_parent_repair.py` -> `SUMMARY: PASS=27 FAIL=0`
- `python3 scripts/cached_runner_output.py --refresh scripts/dimension_selection_parent_source_packet_manifest_2026_06_05.py` -> `SUMMARY: DIMENSION SELECTION SOURCE PACKET PASS=57 FAIL=0`
- `python3 -m py_compile scripts/dimension_selection_poisson_profile_native_proof_2026_06_09.py scripts/frontier_dimension_selection.py scripts/frontier_dimension_selection_lower_bound_parent_repair.py scripts/dimension_selection_parent_source_packet_manifest_2026_06_05.py` -> pass
- `git diff --check` -> clean
- `git diff --name-only -- docs/audit` -> empty
- `rg` stale import phrases in the repaired note and parent runner -> empty

## Residual Observation

Refreshing `scripts/frontier_d3_lower_bound_source_packet_gate_2026_06_06.py`
now fails two ledger-expectation checks on current main because the gate expects
the parent row to remain conditional on a runner-artifact issue. The current
audit state it reads is already different: the finite-k sign bridge and
lower-bound V2 rows are audited clean retained-bounded. That failing generated
cache is not included in this branch.
