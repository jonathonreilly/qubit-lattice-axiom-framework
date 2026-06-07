# Handoff

Branch: `physics-loop/koide-aps-local-density-boundary-20260607`

Target: `koide_aps_block_by_block_forcing_note_2026-04-21`

This block converts the source from a conditional global APS row into a bounded
local-density manifest. The runner now checks that:

- the note carries the 2026-06-07 local-density retargeting;
- the global PL/ABSS route is explicitly not load-bearing;
- the fixed-locus dependency has ledger `effective_status: retained_bounded`;
- exact C3 fixed-locus and root-of-unity arithmetic gives local density `2/9`;
- ABSS/global topology and physical readout remain outside the direct target.

Verification:

```text
python3 scripts/frontier_koide_aps_block_by_block_forcing.py
Total: 35 PASS, 0 FAIL

python3 scripts/cached_runner_output.py --refresh scripts/frontier_koide_aps_block_by_block_forcing.py
status: ok
```

Reviewer extraction target: keep the bounded local-density packet if accepted;
do not extract it as global APS closure.
