# Handoff

Branch-local metadata repair for the Koide A1 physical-bridge no-go row.

Review focus:

- Confirm the existing no-go runner is appropriate as the primary runner.
- Confirm the note still says the physical source-law bridge is open.
- Confirm no audit/result/control-plane file is included.

Verification to rerun:

```bash
python3 scripts/cached_runner_output.py --check-only scripts/frontier_koide_a1_physical_bridge_attempt_nogo_2026_04_22.py
python3 scripts/precompute_audit_runners.py --runners scripts/frontier_koide_a1_physical_bridge_attempt_nogo_2026_04_22.py --check-only
```
