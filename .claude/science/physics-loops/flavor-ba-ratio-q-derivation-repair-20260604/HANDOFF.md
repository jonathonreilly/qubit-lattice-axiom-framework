# Handoff

This branch repairs the conditional audit on
`docs/FLAVOR_BA_RATIO_BOUND_HS_EQUIPARTITION_NOTE_2026-05-30.md`.

Main changes:

- Defines `Q` for this finite packet as the spectral Koide readout of
  `Y=aI+b(J-I)`.
- Derives `Q=1/3+(2/3)(b/a)^2` from the eigenvalues `a+2b`, `a-b`, `a-b`.
- Updates the runner to check the symbolic identity instead of hard-coding the
  formula.
- Leaves the physical Hilbert-Schmidt measure selector open.

Verification commands:

```bash
python3 scripts/flavor_ba_ratio_bound_hs_equipartition_2026_05_30.py
python3 scripts/cached_runner_output.py --check-only scripts/flavor_ba_ratio_bound_hs_equipartition_2026_05_30.py
python3 -m py_compile scripts/flavor_ba_ratio_bound_hs_equipartition_2026_05_30.py
git diff --check
```

Expected runner result: `SCORECARD PASS=5 FAIL=0`.
