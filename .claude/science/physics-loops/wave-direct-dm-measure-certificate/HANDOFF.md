# Handoff

This branch repairs the Wave direct-dM Fam2 seed1 source-packet blocker by
adding an independent `measure_dm` source/cache certificate to the
target-specific runner.

Target cache evidence:

```text
MEASURE_DM_SOURCE_PACKET=PASS
MEASURE_DM_SOURCE=scripts/wave_direct_dm_matched_history_probe.py
CONTINUUM_HELPER_SOURCE=scripts/wave_retardation_continuum_limit.py
SUMMARY: WAVE H025 FAM2 SEED1 PASS=33 FAIL=0
```

Manifest evidence:

```text
SUMMARY: WAVE SOURCE PACKET PASS=86 FAIL=0
```

Verification:

```bash
python3 scripts/wave_direct_dm_h025_fam2_seed1_source_packet_manifest_2026_06_06.py
python3 -m py_compile scripts/wave_direct_dm_h025_fam2_seed1_point_runner_2026_06_04.py scripts/wave_direct_dm_h025_fam2_seed1_source_packet_manifest_2026_06_06.py scripts/wave_direct_dm_matched_history_probe.py scripts/wave_retardation_continuum_limit.py
git diff --check
```

No audit result is changed.
