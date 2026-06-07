# Handoff

This branch repairs
`dm_eta_bounded_prediction_from_supplied_nsites_v_narrow_theorem_note_2026-05-28`.

Changes:

- adds an explicit local `P_DM_ETA` supplied-packet boundary;
- fixes `R(central)` to `(31/9) * 1.59 = 1643/300 = 5.476666...`;
- adds runner checks for both;
- refreshes the runner cache.

Verification:

```bash
PYTHONPATH=scripts python3 scripts/frontier_dm_eta_bounded_prediction_from_supplied_nsites_v.py
python3 scripts/cached_runner_output.py scripts/frontier_dm_eta_bounded_prediction_from_supplied_nsites_v.py --check-only
git diff --check
```

Expected runner result: `TOTAL: PASS=84 FAIL=0`.

No `docs/audit/**` files are changed.

