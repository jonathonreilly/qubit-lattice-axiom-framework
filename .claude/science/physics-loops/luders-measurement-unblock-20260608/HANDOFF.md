# Lueders Measurement-Semantics Unblock Handoff

## Repair

Updated `docs/LUDERS_RULE_FROM_COMPOSITION_CONSISTENCY_NOTE_2026-05-20.md`
to make the 2026-06-08 audit-target split explicit. The parent now names four
exact finite-support blocks:

- finite `PEP` compression algebra;
- canonical finite projective Kraus selection `K_r=P_r`;
- finite pointer-record write to projective Kraus isometry;
- supplied-instrument record-kernel interface.

The note also states the remaining blocker plainly: those finite subclaims do
not derive physical trace/effect probability semantics, a physical measurement
instrument/readout context, or framework-native selective record conditioning.

## Verification

- `python3 scripts/luders_parent_boundary_guard_2026_06_07.py`
- `python3 scripts/luders_measurement_semantics_audit_split_guard_2026_06_08.py`
- `python3 scripts/cached_runner_output.py --refresh scripts/luders_parent_boundary_guard_2026_06_07.py`
- `python3 scripts/cached_runner_output.py --refresh scripts/luders_measurement_semantics_audit_split_guard_2026_06_08.py`

## Remaining Science

The next real science target is a retained measurement-side bridge. This PR
does not close that bridge; it makes the exact support and the open gate
auditable without laundering finite matrix algebra into Born/measurement
semantics.
