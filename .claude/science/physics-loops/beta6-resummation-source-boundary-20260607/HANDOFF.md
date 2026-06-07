# Handoff

This branch repairs
`beta6_resummation_radius_growth_rate_bounded_note_2026-05-30`.

It adds a source-boundary manifest and runner checks for:

- `R_tree(g_tree) = 18 / g_tree^(1/4)`;
- `R_tree > 6 iff g_tree < 81`;
- compact `2x2x1` K-built obstruction `k=4, F=16, n=15`;
- the three open growth inputs.

Verification:

```bash
python3 scripts/frontier_beta6_resummation_radius_growth_rate_2026_05_30.py
python3 scripts/cached_runner_output.py scripts/frontier_beta6_resummation_radius_growth_rate_2026_05_30.py --check-only
git diff --check
```

Expected runner result: `SCORECARD: PASS=32 FAIL=0`.

No `docs/audit/**` files are changed.

