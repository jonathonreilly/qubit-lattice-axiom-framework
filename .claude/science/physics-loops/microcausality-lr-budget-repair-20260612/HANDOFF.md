# Handoff

This PR targets
`axiom_first_microcausality_lieb_robinson_theorem_note_2026-05-01`.

## What Changed

- Replaced the stale `2β/N_c` / `|m| + 30` budget display with the repaired
  `2β` / `|m| + 78` formula.
- Added branch/envelope budgets `|m| + 78 <= |m| + 78.5 <= |m| + 80`.
- Added overlap weights `|m| + 296`, `|m| + 298`, `|m| + 300`.
- Added a primary-runner source guard for these formulas.

## Boundaries

- No audit files edited.
- No retained promotion claimed.
- Gauged/interacting exact-log locality remains open.

## Verification

- `PYTHONPATH=scripts python3 scripts/axiom_first_microcausality_check.py`
- `PYTHONPATH=scripts python3 scripts/microcausality_finite_range_h_bridge_2026_05_09.py`
