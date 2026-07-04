# Artifact Plan

## Primary artifact

- [`docs/THETA_G4_THETA_BAR_ASSEMBLY_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md`](../../../../docs/THETA_G4_THETA_BAR_ASSEMBLY_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md)

## Runner

- [`scripts/theta_g4_theta_bar_assembly_current_surface_no_go_2026_07_04.py`](../../../../scripts/theta_g4_theta_bar_assembly_current_surface_no_go_2026_07_04.py)
- Cached output:
  [`logs/runner-cache/theta_g4_theta_bar_assembly_current_surface_no_go_2026_07_04.txt`](../../../../logs/runner-cache/theta_g4_theta_bar_assembly_current_surface_no_go_2026_07_04.txt)

## Audit-generated artifacts

The audit pipeline seeds:

- `theta_g4_theta_bar_assembly_current_surface_no_go_note_2026-07-04`
- `claim_type=no_go`
- `audit_status=unaudited`
- `effective_status=unaudited`
- `criticality=leaf`

## Verification plan

1. Compile the runner.
2. Run the runner before and after audit-pipeline seeding.
3. Run the full audit pipeline.
4. Run strict audit lint.
5. Run `git diff --check`.
6. Run local compact review for overclaim, hidden import, and generated-file freshness.
