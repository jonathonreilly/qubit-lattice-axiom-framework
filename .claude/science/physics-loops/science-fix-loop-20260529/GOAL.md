# Goal

Run a science-fix loop against the overnight audit results and repair
conditional rows where the auditor supplied a concrete algebraic scope fix.

This block repairs two leaf conditional rows:

- `pmns_tm2_residual_consequence_bounded_note_2026-05-26`
- `planck_target3_coframe_response_accepted_premise_bridge_bounded_note_2026-05-26`

The branch does not apply audit verdicts. The repaired rows are queued for
independent re-audit.
