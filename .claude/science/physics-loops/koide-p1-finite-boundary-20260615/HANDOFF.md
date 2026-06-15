# Handoff

This PR narrows `KOIDE_P1_COLLAPSES_FRAME_RESIDUALS_NOTE_2026-06-01.md` to the
finite checks already computed by its runner:

- supplied spin-1/2 input discriminates soft Bose from CAR;
- hard-core boson `sigma_+` remains invisible to the soft-CCR cardinality
  obstruction;
- the scalar/RP witness is only a finite toy kernel check;
- the nearest-neighbour spectrum comparison is finite and bounded.

Verification:

```bash
python3 scripts/frontier_koide_p1_collapses_frame_residuals.py
python3 scripts/precompute_audit_runners.py --runners scripts/frontier_koide_p1_collapses_frame_residuals.py --force --push-mode none
python3 scripts/precompute_audit_runners.py --runners scripts/frontier_koide_p1_collapses_frame_residuals.py --check-only
python3 docs/audit/scripts/audit_lint.py --strict
git diff --check
```

`audit_lint --strict` reports only the expected non-retained note-hash drift
notice for this edited row, with no errors. The audit lane owns reseeding and
verdict handling.
