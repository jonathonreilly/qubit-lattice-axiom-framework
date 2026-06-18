# Handoff

This branch repairs the uncovered Koide first-order selector conditional row by
adding a bounded-localization certificate and runner.

Claim-state movement: the row now has an explicit bounded-only re-audit target.
The physical L-R coupling/readout bridge remains open and should not be treated
as solved by this branch.

Verification run:

- `PYTHONPATH=scripts python3 scripts/koide_first_order_selector_bounded_localization_certificate_2026_06_18.py`
- `PYTHONPATH=scripts python3 scripts/audit_companion_koide_first_order_selector_is_chiral_lr_coupling_exact.py`
- `python3 -m py_compile scripts/koide_first_order_selector_bounded_localization_certificate_2026_06_18.py scripts/audit_companion_koide_first_order_selector_is_chiral_lr_coupling_exact.py`

Do not edit audit ledgers, publication matrices, front-door status, active
review queue, lane registry, or canonical harness surfaces from this branch.
