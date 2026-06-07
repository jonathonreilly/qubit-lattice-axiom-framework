# Assumptions And Imports

| Item | Role | Status |
|---|---|---|
| `scripts/lensing_analytical_finite_path.py` | Primary finite-path analytical comparison runner. | Strengthened in this branch |
| `scripts/lensing_long_path_test.py` | Long/short-path falsification runner for the T_phys tests. | Source/cache verified inline |
| `logs/runner-cache/lensing_long_path_test.txt` | Cached long-path output carrying T_phys=7.5 measured slope and prediction. | SHA-fresh and clean-exit |
| `scripts/lensing_finite_path_centroid_packet_manifest_2026_06_04.py` | Restricted source-packet manifest. | Zero-fail cache/JSON verified inline |

Forbidden imports for this block:

- treating the centered surrogate as the literal detector-centroid derivation;
- using audit status as branch-local authority;
- changing `docs/audit/**`;
- importing a new physical lensing law.
