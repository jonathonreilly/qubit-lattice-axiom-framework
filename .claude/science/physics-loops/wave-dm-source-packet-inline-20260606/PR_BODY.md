# Summary

Repairs the active `wave_direct_dm_h025_fam2_seed1_followup_note`
restricted-packet blocker by inlining transitive `measure_dm` and
wave-retardation helper source/cache checks into the target-specific primary
runner.

The audit issue asked for the complete untruncated
`scripts/wave_retardation_continuum_limit.py` helper source, especially
`field_at`, `prop_beam`, and `cz`, or an independent certificate for the
`measure_dm` computation. The primary runner now verifies those artifacts
directly and reports `INLINE SOURCE PACKET: PASS=54 FAIL=0`.

# Scope

This is exact support for a packet-completeness blocker. It does not retag the
audit ledger, does not promote the bounded wave replay, and does not claim a
wave portability or amplitude law.

# Verification

```bash
python3 -m py_compile scripts/wave_direct_dm_h025_fam2_seed1_point_runner_2026_06_04.py scripts/wave_direct_dm_h025_fam2_seed1_source_packet_manifest_2026_06_06.py
PYTHONPATH=scripts python3 scripts/cached_runner_output.py --check-only scripts/wave_direct_dm_h025_fam2_seed1_point_runner_2026_06_04.py
PYTHONPATH=scripts python3 scripts/cached_runner_output.py --check-only scripts/wave_direct_dm_h025_fam2_seed1_source_packet_manifest_2026_06_06.py
git diff --check
```
