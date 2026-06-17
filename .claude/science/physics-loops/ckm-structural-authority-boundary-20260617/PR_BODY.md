## Summary

Repairs three CKM/EW runner blockers by preserving exact arithmetic while
demoting stale positive-closure claims to bounded-support / authority-boundary
status:

- A2 below W2 source-literal arithmetic;
- SU2 weak beta coefficient structural arithmetic;
- CKM/Koide `N_gen = N_color = 3` source equality.

This PR does not audit, land to main, retag the ledger, or update repo-wide
authority surfaces.

## Artifacts

- `docs/CKM_A_SQUARED_BELOW_W2_Y_QUANTUM_CLOSURE_THEOREM_NOTE_2026-04-25.md`
- `docs/SU2_WEAK_BETA_COEFFICIENT_STRUCTURAL_CLOSED_FORM_THEOREM_NOTE_2026-04-26.md`
- `docs/CKM_KOIDE_CROSS_SECTOR_Z3_CLOSURE_THEOREM_NOTE_2026-04-25.md`
- `scripts/frontier_ckm_a_squared_below_w2_y_quantum_closure.py`
- `scripts/frontier_su2_weak_beta_coefficient_structural_closed_form.py`
- `scripts/frontier_ckm_koide_cross_sector_z3_closure.py`
- refreshed `logs/runner-cache/*` outputs
- loop pack under `.claude/science/physics-loops/ckm-structural-authority-boundary-20260617/`

## Verification

```bash
python3 -m py_compile \
  scripts/frontier_ckm_a_squared_below_w2_y_quantum_closure.py \
  scripts/frontier_su2_weak_beta_coefficient_structural_closed_form.py \
  scripts/frontier_ckm_koide_cross_sector_z3_closure.py

python3 scripts/frontier_ckm_a_squared_below_w2_y_quantum_closure.py
python3 scripts/frontier_su2_weak_beta_coefficient_structural_closed_form.py
python3 scripts/frontier_ckm_koide_cross_sector_z3_closure.py

python3 scripts/cached_runner_output.py --check-only scripts/frontier_ckm_a_squared_below_w2_y_quantum_closure.py
python3 scripts/cached_runner_output.py --check-only scripts/frontier_su2_weak_beta_coefficient_structural_closed_form.py
python3 scripts/cached_runner_output.py --check-only scripts/frontier_ckm_koide_cross_sector_z3_closure.py
```

All three refreshed caches are fresh with `HARD_ISSUES=0`.

## Boundaries

- no new axioms;
- no positive retained/proposed status;
- no audit verdict edits;
- no publication matrix, lane registry, or work-history edits;
- textbook one-loop beta formula remains an explicit import unless a later
  framework-native proof lands.
