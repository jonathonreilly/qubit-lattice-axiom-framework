# No-Go Ledger

## No-Go: Treating Empty `ok` Cache As Sufficient Evidence

An `ok` cache with empty stdout is not a useful audit-unblock artifact for this target because
reviewers cannot inspect the runner's checks, numerical summaries, status boundaries, or final
prediction summary. The block replaces that record with the full generated transcript.

## No-Go: Claiming Readiness From Runner Success Alone

Runner success does not make the target row ready. The audit queue row remains blocked by:

- `gw_echo_null_result_note`
- `work_history.gw_echo_timing_route_note`

## No-Go: Applying Audit Verdicts

Applying or implying an audit verdict in this branch would violate the user's instruction and
the physics-loop claim-status firewall. This block is methodology/tooling support only.
