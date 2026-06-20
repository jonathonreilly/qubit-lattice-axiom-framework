# Summary

Block108 repairs `distance_law_preserving_third_family_note` as a
`bounded_theorem` source packet.

The note reports a direct numerical preservation gate for one grown family
(`drift = 0.50`, `restore = 0.90`). It previously used `proposed_retained`
status prose and entered the audit queue as a migration-hint positive theorem.
This PR narrows the source boundary to bounded support, adds canonical
metadata, and updates the runner so it fails if the claim gates or metadata are
missing.

# Claim Boundary

This branch does not claim a retained result, does not run audit-loop, and does
not apply any audit verdict. It leaves the row `unaudited` and ready for the
independent audit worker as `bounded_theorem`.

# Target Row After Pipeline

```text
claim_type=bounded_theorem
claim_type_author_hint_raw=bounded_theorem
claim_type_provenance=author_hint
audit_status=unaudited
effective_status=unaudited
audit_queue_index=644
audit_queue_ready=true
```

# Verification

```text
bash docs/audit/scripts/run_pipeline.sh
python3 -m py_compile scripts/DISTANCE_LAW_PRESERVING_THIRD_FAMILY.py
python3 scripts/DISTANCE_LAW_PRESERVING_THIRD_FAMILY.py
python3 scripts/precompute_audit_runners.py --runners scripts/DISTANCE_LAW_PRESERVING_THIRD_FAMILY.py --force --push-mode none --allow-non-main
python3 scripts/audit_packet_script_deps.py
python3 docs/audit/scripts/audit_lint.py --strict
git diff --check
```

Results:

- runner: sign gate PASS, tail gate PASS, source boundary PASS;
- precompute: 1 OK;
- strict audit lint: 139 notices, 0 errors.

# Loop Packet

- `.claude/science/physics-loops/audit-unblock-20260619/HANDOFF.md`
- `.claude/science/physics-loops/audit-unblock-20260619/TRACE_GATE.md`
- `.claude/science/physics-loops/audit-unblock-20260619/CLAIM_STATUS_CERTIFICATE.md`
- `.claude/science/physics-loops/audit-unblock-20260619/REVIEW_HISTORY.md`
