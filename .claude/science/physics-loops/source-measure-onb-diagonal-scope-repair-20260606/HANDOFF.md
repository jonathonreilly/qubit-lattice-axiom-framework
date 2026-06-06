# Handoff

This PR repairs the conditional ONB source row by narrowing it to the theorem
actually proven by its runner.

Changed source surface:

- The note no longer claims a same-source physical `Y_T` top/`W` response basis.
- The note no longer imports or derives `g_bare`, `F_Htt`, `N_c`, `y_33`, `y_t`,
  or source semantics.
- The load-bearing claim is only the finite `C^6` diagonal matrix-unit theorem.

Changed runner:

- Enforces the narrowed source boundary.
- Proves the `E_ii` Hilbert-Schmidt Gram identity, rank/completeness, identity
  resolution, symbolic reconstruction, democratic unit, fixed-line uniqueness,
  and numpy cross-checks.

Verification:

```text
python3 scripts/audit_companion_source_measure_sharp_record_onb_2026_06_05.py
python3 scripts/cached_runner_output.py scripts/audit_companion_source_measure_sharp_record_onb_2026_06_05.py --refresh
python3 scripts/cached_runner_output.py scripts/audit_companion_source_measure_sharp_record_onb_2026_06_05.py --check-only
```

All passed with `SUMMARY: PASS=37 FAIL=0`; cache is fresh.

No audit data, ledger verdict, queue status, repo-wide registry, or main-branch
status surface was edited.
