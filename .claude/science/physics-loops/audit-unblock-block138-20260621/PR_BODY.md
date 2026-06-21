## Summary

Refreshes the generated audit dispatch queue from existing dispatcher sidecars.
This removes the `audit_dispatch_queue_stale` warnings that made live sidecar
targets invisible to audit-loop target selection.

After regeneration:

- live dispatch entries: `3`
- ready dispatch entries: `1`
- resolved post-manifest re-audit entries: `18`
- resolved/invalid entries: `44`
- retired entries: `19`

The ready live target is
`causal_propagating_field_live_packet_note_2026-06-05`. The two other live
targets remain dependency-blocked and are recorded with explicit blockers.

## Boundary

- No audit-loop run.
- No audit verdicts applied.
- No effective-status promotion.
- This is target-selection metadata only; dispatcher sidecars and the generated
  dispatch queue must not be used as audit evidence.

## Artifacts

- `docs/audit/data/audit_dispatch_queue.json`
- `docs/audit/AUDIT_DISPATCH_QUEUE.md`
- `.claude/science/physics-loops/audit-unblock-block138-20260621/HANDOFF.md`
- `.claude/science/physics-loops/audit-unblock-block138-20260621/TRACE_GATE.md`
- `.claude/science/physics-loops/audit-unblock-block138-20260621/CLAIM_STATUS_CERTIFICATE.md`

## Verification

- `python3 docs/audit/scripts/compute_audit_dispatch_queue.py` -> live `3`, ready `1`, resolved `18`, retired `19`
- `python3 docs/audit/scripts/audit_lint.py --strict` -> `audit_dispatch_queue_stale` warnings cleared; still exits 1 on retained note-hash drift errors requiring independent re-audit
- `python3 -m py_compile docs/audit/scripts/compute_audit_dispatch_queue.py docs/audit/scripts/audit_lint.py` -> OK
- `git diff --check` -> OK
