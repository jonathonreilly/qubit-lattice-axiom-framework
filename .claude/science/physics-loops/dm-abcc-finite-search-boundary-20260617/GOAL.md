# DM A-BCC Finite-Search Boundary Repair

## Goal

Repair the DM A-BCC basin-enumeration executable so it preserves the useful
finite multistart scan while refusing the unsupported jump to theorem-grade
exhaustiveness.

## Scope

- Source-side runner: `scripts/frontier_dm_abcc_basin_enumeration_completeness.py`
- Archived companion note:
  `archive_unlanded/dm-abcc-finite-search-salvage-2026-04-30/DM_ABCC_BASIN_ENUMERATION_COMPLETENESS_THEOREM_NOTE_2026-04-20.md`

## Non-goals

- No audit ledger edits.
- No audit queue edits.
- No claim that the finite scan is an interval-certified completeness theorem.
- No rebase/freshness work for older PRs.
