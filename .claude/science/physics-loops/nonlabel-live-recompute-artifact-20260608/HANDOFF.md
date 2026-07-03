# Handoff

## Summary

This block repairs the nonlabel grown basin runner-artifact issue.

The primary verifier now validates the SHA-fresh live recompute artifact and cache, including row values, scorecard, restore grid, and row gates. The source note's table now uses the exact live recompute values and charge exponents instead of stale rounded frozen-log entries.

## Main Artifacts

- `docs/NONLABEL_GROWN_BASIN_NOTE.md`
- `scripts/NONLABEL_GROWN_BASIN_TARGETED.py`
- `logs/runner-cache/NONLABEL_GROWN_BASIN_TARGETED.txt`
- `.claude/science/physics-loops/nonlabel-live-recompute-artifact-20260608/TRACE_GATE.md`
- `.claude/science/physics-loops/nonlabel-live-recompute-artifact-20260608/CLAIM_STATUS_CERTIFICATE.md`

## Verification

```bash
python3 scripts/NONLABEL_GROWN_BASIN_TARGETED.py
python3 scripts/NONLABEL_GROWN_BASIN_TARGETED.py --recompute
git diff --check
git diff --name-only -- docs/audit
```

Expected key results:

- Primary verifier: `SCORECARD PASS=4 FAIL=0`.
- Primary live recompute mode: `passed rows: 3/3`.
- No `docs/audit/**` files in the branch diff.

## Remaining Boundaries

- No widening beyond seed 0, drift 0.2, restore values 0.60, 0.70, 0.80.
- Independent audit must decide any effective status movement.

## Next Action

Send this PR to the Codex reviewer/re-audit path. Do not land audit results from this branch.
