# Trace Gate

```yaml
trace_class: direct_blocker_closure
target_claim_id: fifth_family_radial_repaired_positive_packet_note_2026-05-29
target_blocker_text: "runner_artifact_issue: include scripts/FIFTH_FAMILY_RADIAL_FM_TRANSFER.py with its SHA-pinned cache/output, and preferably the sweep and failure-audit companion caches, then re-audit the full bounded packet."
source_of_blocker_text: audit_ledger
reachability_to_target: closes
artifact_role: runner_certificate
next_trace_action: "Independent audit should rebuild helper_runner_paths from the primary basin runner and verify the companion packet manifest in the refreshed cache."
```

The branch does not change the bounded fifth-family science claim. It repairs
the restricted packet surface named by the audit blocker: the primary runner now
imports `FIFTH_FAMILY_RADIAL_SWEEP`, `FIFTH_FAMILY_RADIAL_FAILURE_AUDIT`, and
`FIFTH_FAMILY_RADIAL_FM_TRANSFER`, which makes the audit packet helper resolver
include all three companion sources. The primary cache prints SHA-256 hashes for
the three companion sources and caches and requires `status: ok` / `exit_code: 0`.
