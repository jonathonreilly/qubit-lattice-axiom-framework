# Artifact Plan

## Source Repair

- Add a `2026-06-16 B-W bridge-chain source graph` section to the kinetic note.
- Link the B-W reduction, Wick-IR cone agreement, and realization-row
  reconciliation rows explicitly.
- Update the B-W premise and no-retirement language to include those rows.
- Extend runner Part H to check the new bridge-chain wiring and no-promotion
  firewall.

## Verification

- `python3 -m py_compile` on the changed runner.
- Run the changed runner and refresh its cache.
- `git diff --check`.
- Protected audit/publication/front-door diff check.
