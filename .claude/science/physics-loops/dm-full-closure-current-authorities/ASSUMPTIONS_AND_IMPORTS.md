# Assumptions And Imports

## Current One-Hop Authorities

The parent runner now checks these rows directly from
`docs/audit/data/audit_ledger.json`:

- `dm_full_closure_same_surface_thermal_integral_representation_theorem_note_2026-04-16`
  has `audit_status: audited_clean` and `effective_status: retained_bounded`.
- `dm_full_closure_same_surface_thermal_monotonicity_theorem_note_2026-04-17`
  has `audit_status: audited_clean` and `effective_status: retained_bounded`.
- `dm_full_closure_same_surface_thermal_series_tail_support_note_2026-04-17`
  has `audit_status: audited_clean` and `effective_status: retained_bounded`.
- `dm_full_closure_64_to_1_channel_weight_bridge_narrow_theorem_note_2026-06-02`
  has `audit_status: audited_clean` and `effective_status: retained_bounded`.

## Still Imported Or Conditional

- The live-DM plaquette / eta-omega constants are not derived in this parent
  note and are not promoted here.
- The packet-completeness / selector premise is not derived in this parent
  note and is not promoted here.
- The sibling current-bank no_go boundary remains a cited boundary, not a
  closure of the live-DM premise packet.

No new axiom is introduced. No audit ledger rows are edited.
