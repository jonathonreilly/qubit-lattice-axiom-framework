# Handoff

This branch repairs the stale runner dependency check for
`higgs_lattice_eigenvalue_ratio_narrow_theorem_note_2026-05-02`.

Key movement:

- Runner now checks the repaired g_bare dependency pair:
  `G_BARE_RESCALING_FREEDOM_REMOVAL_THEOREM_NOTE_2026-05-03.md` and
  `G_BARE_CONSTRAINT_VS_CONVENTION_THEOREM_NOTE_2026-05-03.md`.
- Cache refreshed:
  `logs/runner-cache/frontier_higgs_lattice_eigenvalue_ratio_narrow.txt`
- Result: `TOTAL: PASS=33, FAIL=0`
- Pipeline reset the target row to `audit_status=unaudited`,
  `effective_status=unaudited`, `ready=true`.

The scientific scope is unchanged: bounded lattice-side algebra only, with
physical Higgs matching excluded.
