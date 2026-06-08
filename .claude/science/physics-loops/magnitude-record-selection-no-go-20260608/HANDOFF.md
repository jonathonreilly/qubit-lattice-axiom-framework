## Handoff

This branch repairs `magnitude_reads_minimal_record_block_2026-06-06` by
removing the overstrong Record-selection claim. The repaired source now says:
RP two-step supplies the minimal positive temporal block, but Record does not
select the magnitude readout scale. The positive target is now sharper: supply
a UV/minimal-block readout bridge if we want `8 x 2 = 16` to close beyond
conditional arithmetic.

## Verification

```bash
python3 scripts/magnitude_reads_minimal_record_block_2026_06_06.py
python3 scripts/cached_runner_output.py --refresh scripts/magnitude_reads_minimal_record_block_2026_06_06.py
python3 scripts/cached_runner_output.py --check-only scripts/magnitude_reads_minimal_record_block_2026_06_06.py
python3 -m py_compile scripts/magnitude_reads_minimal_record_block_2026_06_06.py
git diff --name-only -- docs/audit
git diff --check
```

Expected result: `TOTAL: PASS=10 FAIL=0`; no `docs/audit` edits.

