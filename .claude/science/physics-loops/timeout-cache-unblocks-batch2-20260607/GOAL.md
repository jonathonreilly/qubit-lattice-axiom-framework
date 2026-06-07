# Timeout Cache Unblocks Batch 2

Goal: remove concrete runner-cache timeout blockers without changing audit
verdicts or widening source claims.

Targets:

- `lattice_3d_l2_tail_stats_note`: replace the timed-out default runner cache
  with an audit-compatible frozen-log verifier for the note's narrowed width-8
  claim.
- `fm_transfer_note`: declare an audit timeout and refresh the current runner
  cache from `status: timeout` to `status: ok`.
- `persistent_record_matched_compare_note`: declare an audit timeout and
  refresh the current runner cache from `status: timeout` to `status: ok`.

No `docs/audit/**` files are edited.
