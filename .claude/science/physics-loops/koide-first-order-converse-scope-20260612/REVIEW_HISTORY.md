# Review History

## 2026-06-12

Self-checks run:

- `python3 scripts/audit_companion_koide_first_order_selector_is_chiral_lr_coupling_exact.py`
  - Result: `10 PASS, 0 FAIL`.
- `python3 scripts/precompute_audit_runners.py --runners scripts/audit_companion_koide_first_order_selector_is_chiral_lr_coupling_exact.py --force --concurrency 1 --push-mode none --allow-non-main`
  - Result: `ok 1`.

Review-loop handoff:

- This PR is ready for reviewer extraction.
- No audit verdicts were edited.
- Remaining risk is the deliberately open physical coupling bridge, not the false-converse repair.
