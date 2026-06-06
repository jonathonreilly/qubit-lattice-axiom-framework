# Handoff

Branch-local science block:

- Target: `KOIDE_APS_BLOCK_BY_BLOCK_FORCING_NOTE_2026-04-21`.
- Repair: fixed-locus `p = 3` and `(1,2)` weights are now sourced from the
  fixed-locus bridge rather than carried as unsupported stipulations.
- Remaining blocker: global `PL S^3 x R` / ABSS applicability and physical
  selected-line readout.

Verification:

```bash
python3 scripts/cached_runner_output.py scripts/frontier_koide_aps_block_by_block_forcing.py --refresh --timeout-sec 120
python3 scripts/cached_runner_output.py scripts/frontier_koide_aps_block_by_block_forcing.py --check-only
git diff -- docs/audit --exit-code
git diff --check
```

Expected runner result: `29 PASS / 0 FAIL`.
