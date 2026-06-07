# Handoff

Branch: `physics-loop/fifth-family-radial-packet-manifest-20260607`

Target row:
`fifth_family_radial_repaired_positive_packet_note_2026-05-29`

What changed:

- `scripts/FIFTH_FAMILY_RADIAL_BASIN.py` now statically imports the sweep,
  failure-audit, and F~M transfer companion runners so the audit helper graph
  includes those source files in the restricted packet.
- The basin runner prints a companion packet manifest with SHA-256 hashes for
  each companion source and cache and fails if a companion cache is missing or
  not `status: ok` / `exit_code: 0`.
- `scripts/FIFTH_FAMILY_RADIAL_FAILURE_AUDIT.py` now asserts the expected single
  sign-orientation miss and prints `ASSERTIONS: PASS`.
- The note records the packet-manifest repair without widening the bounded
  finite claim.

Checks:

- Python compile check passed for all four fifth-family radial runners.
- Failure audit runner passed.
- Cache refresh passed for the basin and failure-audit runners.
- Helper graph extraction from the primary runner now includes the FM transfer
  companion.
- No `docs/audit` files were changed.

Remaining blockers:

- Independent audit must decide whether this clears the recorded
  `runner_artifact_issue`.
- The packet remains bounded finite support, not a retained or family-wide
  theorem.
