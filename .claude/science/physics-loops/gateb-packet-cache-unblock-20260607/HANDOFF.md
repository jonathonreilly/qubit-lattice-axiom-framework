# Handoff

This PR unblocks two stale timeout caches by adding explicit audit timeout declarations and refreshing the pinned cache outputs.

Verification:

```bash
python3 scripts/cached_runner_output.py --check-only scripts/gate_b_grown_trapping_transport_probe.py
python3 scripts/cached_runner_output.py --check-only scripts/packet_memory.py
python3 scripts/precompute_audit_runners.py --runners scripts/gate_b_grown_trapping_transport_probe.py,scripts/packet_memory.py --check-only --allow-non-main
```

Observed:

```text
fresh logs/runner-cache/gate_b_grown_trapping_transport_probe.txt
fresh logs/runner-cache/packet_memory.txt
All relevant caches are fresh.
```

No `docs/audit/**` files are touched.
