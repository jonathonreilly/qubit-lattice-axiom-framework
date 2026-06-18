# Summary

This source-side PR repairs the high-load `audited_renaming` blocker for
`dm_leptogenesis_pmns_minimum_information_source_law_note_2026-04-16`.

The audit found that the row's load-bearing move is an explicit selector
definition plus an imposed `eta_{i_*}/eta_obs = 1` equality constraint. The
runner computes consequences of that convention, but does not derive selector
authority. This PR narrows the source to `open_gate` and hardens the runner to
enforce that boundary.

# Changes

- Change the note type from `bounded_theorem` to `open_gate`.
- Add standard primary runner/cache links.
- Add a re-audit source-repair section.
- Update runner text from theorem wording to open-gate diagnostic wording.
- Add source-boundary checks to the runner.
- Refresh the SHA-pinned cache.
- Add a branch-local physics-loop handoff packet.

# Verification

```bash
python3 scripts/frontier_dm_leptogenesis_pmns_mininfo_source_law.py
python3 scripts/cached_runner_output.py --check-only scripts/frontier_dm_leptogenesis_pmns_mininfo_source_law.py
python3 -m py_compile scripts/frontier_dm_leptogenesis_pmns_mininfo_source_law.py
git diff --check
```

Runner result: `PASS=23 FAIL=0`.

# Boundaries

This PR does not audit, retag, land, or edit ledger/status surfaces. It does
not derive `I_seed`, does not derive the eta equality constraint, and does not
close the PMNS-assisted `N_e` branch.
