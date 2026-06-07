# Handoff

This branch repairs the lensing finite-path source-packet blocker by placing
the long-path source/cache check inside the primary analytical runner output.

Primary runner now prints:

```text
LONG-PATH SOURCE PACKET
  source: scripts/lensing_long_path_test.py
  cache: logs/runner-cache/lensing_long_path_test.txt
  cache SHA/current assertion: PASS
  required short-path facts:
    T_phys = 7.5
    H=0.25 kubo_true slope = -1.4356
    finite-path prediction slope = -1.7336
```

Verification:

```bash
python3 scripts/lensing_analytical_finite_path.py
python3 scripts/lensing_finite_path_centroid_packet_manifest_2026_06_04.py
python3 -m py_compile scripts/lensing_analytical_finite_path.py scripts/lensing_long_path_test.py scripts/lensing_finite_path_centroid_packet_manifest_2026_06_04.py
git diff --check
```

No audit result is changed.
