## Summary

Repairs `bertrand_stable_orbit_upper_bound_support_note_2026-05-20` by adding
an in-row derivation of the continuum `d`-dimensional radial Green-potential
law and a symbolic runner for the circular-orbit stability calculation.

## Trace Gate

- Trace class: `direct_blocker_closure`
- Audit blocker: missing retained derivation/authority for
  `V(r) = -k/r^(d-2)` across integer `d >= 5`.
- Repair: derive `Delta r^(2-d) = 0` for `r > 0`, then verify
  `d^2 V_eff / dr^2 | rc = k(d-2)(4-d)/r_c^d`.

## Verification

- `python3 scripts/frontier_bertrand_stable_orbit_upper_bound_repair.py`
  - `SUMMARY: PASS=12 FAIL=0`
- `python3 scripts/vocab_lint.py --report-only docs/BERTRAND_STABLE_ORBIT_UPPER_BOUND_SUPPORT_NOTE_2026-05-20.md`
  - clean
- `docs/audit/scripts/run_pipeline.sh`
  - complete
- `git diff --check`
  - clean

## Boundaries

- Does not claim a framework-native universal dimensional-gravity law.
- Does not retire the full Bertrand closed-orbit theorem.
- Does not promote the parent dimension-selection chain.
- No new axioms.
