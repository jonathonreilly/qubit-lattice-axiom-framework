## Summary

Adds an exact-support carrier-slot theorem for the critical
`quark_cp_carrier_completion_note_2026-04-18` numerical-match row.

The parent row had a structural blocker: the determinant-neutral complex `1-3`
CP-carrier slot was chosen by ansatz. This PR proves the fixed-Schur-NNI-tree,
Hermitian one-edge version of that statement: tree phases are gauge, the only
off-tree edge is the `1-3` closing edge, its phase is the unique cycle
invariant after tree gauge-fixing, and Hermiticity keeps the determinant phase
real.

## Boundary

This does not derive `xi_u`, `xi_d`, quark comparator targets, CKM magnitudes,
J, or a small-correction interpretation. It partially closes only the
slot-choice sub-blocker. Independent audit remains required for any status
propagation.

No audit verdicts, ledger rows, queue files, generated audit/status outputs, or
publication effective-status files are changed.

## Checks

```bash
python3 scripts/frontier_quark_cp_carrier_slot_minimality_2026_06_17.py
# TOTAL: PASS=29 FAIL=0

python3 scripts/cached_runner_output.py --refresh scripts/frontier_quark_cp_carrier_slot_minimality_2026_06_17.py
python3 scripts/cached_runner_output.py --check-only scripts/frontier_quark_cp_carrier_slot_minimality_2026_06_17.py
python3 scripts/frontier_quark_cp_carrier_completion.py
# TOTAL: PASS=11, FAIL=0

python3 -m py_compile scripts/frontier_quark_cp_carrier_slot_minimality_2026_06_17.py
git diff --check
```

Handoff: `.claude/science/physics-loops/quark-cp-carrier-slot-minimality-20260617/HANDOFF.md`
