## Handoff

This branch repairs the free-Dirac common-core row by adding the Wigner-cocycle
derivative missing from the prior source. The derivative is computed directly
from the canonical boost matrix and matches the expected bounded boost spin
multiplier.

## Verification

```bash
python3 scripts/frontier_wigner_core_coincidence_poincare_generators_2026_06_08.py
python3 scripts/cached_runner_output.py --refresh scripts/frontier_wigner_core_coincidence_poincare_generators_2026_06_08.py
python3 scripts/cached_runner_output.py --check-only scripts/frontier_wigner_core_coincidence_poincare_generators_2026_06_08.py
python3 -m py_compile scripts/frontier_wigner_core_coincidence_poincare_generators_2026_06_08.py
git diff --name-only -- docs/audit
git diff --check
```

Expected result: `TOTAL: 21 PASS / 0 FAIL`; no `docs/audit` edits.

