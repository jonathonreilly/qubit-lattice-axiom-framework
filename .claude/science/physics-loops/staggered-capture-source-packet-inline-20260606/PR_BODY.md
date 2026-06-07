# Summary

Repairs the active `staggered_backreaction_live_capture_packet_note_2026-05-29`
restricted-packet blocker by inlining transitive helper source/cache checks
into the primary live capture packet runner.

The audit issue asked for the complete untruncated
`scripts/frontier_staggered_backreaction_prototype.py` helper source and the
transitive helper chain. The primary runner now verifies those artifacts
directly and reports `INLINE SOURCE PACKET: PASS=78 FAIL=0`.

# Scope

This is exact support for a packet-completeness blocker. It does not retag the
audit ledger, does not claim continuum backreaction, and does not claim
physical gravitational closure.

# Verification

```bash
python3 -m py_compile scripts/staggered_backreaction_live_capture_packet_check.py scripts/staggered_backreaction_live_capture_source_packet_manifest_2026_06_06.py
PYTHONPATH=scripts python3 scripts/cached_runner_output.py --check-only scripts/staggered_backreaction_live_capture_packet_check.py
PYTHONPATH=scripts python3 scripts/cached_runner_output.py --check-only scripts/staggered_backreaction_live_capture_source_packet_manifest_2026_06_06.py
git diff --check
```
