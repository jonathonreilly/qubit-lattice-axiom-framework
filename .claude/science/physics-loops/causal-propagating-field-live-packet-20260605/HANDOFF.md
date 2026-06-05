# Handoff

## What Changed

- `scripts/causal_propagating_field.py` is now an executable finite replay
  rather than a stub.
- `logs/runner-cache/causal_propagating_field.txt` is fresh and reports
  `ASSERTIONS: PASS`.
- `docs/CAUSAL_PROPAGATING_FIELD_LIVE_PACKET_NOTE_2026-06-05.md` records the
  live bounded packet and stale-table boundary.
- `scripts/causal_propagating_field_source_packet_manifest_2026_06_05.py`
  exposes the primary runner, helper source, primary cache, and helper cache.
- `logs/runner-cache/causal_propagating_field_source_packet_manifest_2026_06_05.txt`
  reports `SUMMARY: CAUSAL PROPAGATING FIELD SOURCE PACKET PASS=30 FAIL=0`.

## Verification

```bash
python3 -m py_compile scripts/causal_propagating_field.py scripts/causal_propagating_field_source_packet_manifest_2026_06_05.py
python3 scripts/precompute_audit_runners.py --runners scripts/causal_propagating_field.py --force --push-mode=none --allow-non-main --concurrency 1
python3 scripts/causal_propagating_field_source_packet_manifest_2026_06_05.py
python3 scripts/precompute_audit_runners.py --runners scripts/causal_propagating_field_source_packet_manifest_2026_06_05.py --force --push-mode=none --allow-non-main --concurrency 1
python3 scripts/precompute_audit_runners.py --runners scripts/causal_propagating_field.py,scripts/causal_propagating_field_source_packet_manifest_2026_06_05.py,scripts/evolving_network_prototype_v6.py --check-only --push-mode=none --allow-non-main --concurrency 1
git diff --check
```

## Audit Boundary

This PR does not edit `docs/audit/**`, does not restore the archived `0.45`
dynamic-ratio claim, and does not assign an effective audit status. It queues
a live bounded packet for review.

PR: https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/2666
