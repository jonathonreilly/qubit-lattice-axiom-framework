# Handoff

This PR turns the broad vector-sector circular-orbit runner into a fast verifier for the frozen full-harness log already cited by the note. The original slow propagation harness remains available with `--recompute`.

Verification:

```bash
python3 scripts/vector_sector_circular_orbit.py
python3 scripts/cached_runner_output.py --check-only scripts/vector_sector_circular_orbit.py
python3 scripts/precompute_audit_runners.py --runners scripts/vector_sector_circular_orbit.py --check-only --allow-non-main
```

Observed:

```text
SCORECARD PASS=21 FAIL=0
fresh logs/runner-cache/vector_sector_circular_orbit.txt
All relevant caches are fresh.
```

No `docs/audit/**` files are touched, and no retained promotion is claimed.
