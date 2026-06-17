# Handoff

Branch: `codex/quark-cp-carrier-slot-minimality-20260617`

This branch adds a narrow exact-support theorem for the critical
`quark_cp_carrier_completion_note_2026-04-18` numerical-match row.

## Claim Movement

The parent row's old gap said the determinant-neutral complex `1-3` carrier was
chosen by ansatz. This branch proves the fixed-tree/Hermitian one-edge version:

- phases on the Schur-NNI tree edges are removable by diagonal rephasing;
- the only off-tree edge on three generations is the `1-3` closing edge;
- after tree gauge-fixing, the `1-3` phase is the unique cycle invariant;
- Hermiticity keeps the determinant real, so the slot itself introduces no
  continuous determinant phase.

This partially closes only the slot-choice sub-blocker. The parent row remains
blocked on deriving `xi_u`, `xi_d`, deriving comparator/readout targets, and
explaining the large fitted carrier magnitudes.

## Artifacts

- `docs/QUARK_CP_CARRIER_SLOT_MINIMALITY_THEOREM_NOTE_2026-06-17.md`
- `scripts/frontier_quark_cp_carrier_slot_minimality_2026_06_17.py`
- `logs/runner-cache/frontier_quark_cp_carrier_slot_minimality_2026_06_17.txt`
- parent note pointer in `docs/QUARK_CP_CARRIER_COMPLETION_NOTE_2026-04-18.md`

## Checks

```bash
python3 scripts/frontier_quark_cp_carrier_slot_minimality_2026_06_17.py
python3 scripts/cached_runner_output.py --refresh scripts/frontier_quark_cp_carrier_slot_minimality_2026_06_17.py
python3 scripts/cached_runner_output.py --check-only scripts/frontier_quark_cp_carrier_slot_minimality_2026_06_17.py
python3 scripts/frontier_quark_cp_carrier_completion.py
python3 -m py_compile scripts/frontier_quark_cp_carrier_slot_minimality_2026_06_17.py
git diff --check
```

Expected new runner summary: `TOTAL: PASS=29 FAIL=0`.
Expected parent runner summary: `TOTAL: PASS=11, FAIL=0`.

## Boundaries

No audit verdicts, audit ledgers, queue files, publication effective-status
tables, lane registry, active review queue, or front-door generated status files
are edited. Review-loop and branch freshness are reviewer-owned.
