# Handoff

Branch: `physics-loop/plaquette-beta6-native-beta-import-20260617`

This source-side PR retires the W2 beta=6 Wilson-normalization import from the
old plaquette perturbative diagnostic by routing it through the landed native
beta relationship note. It does not promote the old diagnostic or derive the
plaquette value.

Reviewer extraction guidance:

- W2 can route through this repair and the native beta relationship note.
- W1, W3, W4, and the actual non-perturbative beta=6 plaquette surface remain
  conditional/open.
- Audit/review owns any status propagation.

Verification to run:

```bash
python3 scripts/cached_runner_output.py --refresh scripts/frontier_plaquette_beta6_wilson_normalization_native_import_repair_2026_06_17.py
python3 scripts/cached_runner_output.py --check-only scripts/frontier_plaquette_beta6_wilson_normalization_native_import_repair_2026_06_17.py
python3 scripts/frontier_plaquette_beta6_perturbative_derivation_2026_05_27.py
python3 scripts/cached_runner_output.py --check-only scripts/frontier_plaquette_beta6_perturbative_derivation_2026_05_27.py
python3 -m py_compile scripts/frontier_plaquette_beta6_wilson_normalization_native_import_repair_2026_06_17.py scripts/frontier_plaquette_beta6_perturbative_derivation_2026_05_27.py
git diff --check
```

Local result before PR: all commands passed; new verifier reports
`TOTAL: PASS=15 FAIL=0`, and the old plaquette diagnostic reports
`TOTAL: PASS=32 FAIL=0`.
