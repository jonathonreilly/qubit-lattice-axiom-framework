# Summary

This source-side PR unblocks
`anomaly_forces_time_fb_note_2026-05-17` by registering its primary
runner/cache and refreshing the verifier against current mainline
source text.

Current main no longer uses the older single-clock Step-4 wording that
the stale runner expected. The parent theorem now uses the sharper local
`B-AXIS` boundary. This PR updates the F-B meta note and runner to
verify that current decomposition:

- Step 3 computes the lower bound: `d_t` is odd, hence `d_t >= 1`.
- Step 4 supplies the declared `B-AXIS` cap: `d_t <= 1`.
- The theorem does not derive `B-AXIS`.
- The single-clock note is provenance context, not a markdown dependency
  edge of the parent row.

# Changes

- Add primary runner and cached output links to
  `docs/ANOMALY_FORCES_TIME_FB_NOTE_2026-05-17.md`.
- Add a current-mainline reconciliation section explaining the `B-AXIS`
  supersession of the older F-B wording.
- Update `scripts/frontier_anomaly_forces_time_fb_framing_fix.py` to
  check the meta-note registration and current parent theorem boundary.
- Refresh
  `logs/runner-cache/frontier_anomaly_forces_time_fb_framing_fix.txt`.
- Add a branch-local physics-loop handoff packet.

# Verification

```bash
python3 scripts/frontier_anomaly_forces_time_fb_framing_fix.py
python3 scripts/cached_runner_output.py --check-only scripts/frontier_anomaly_forces_time_fb_framing_fix.py
python3 -m py_compile scripts/frontier_anomaly_forces_time_fb_framing_fix.py
git diff --check
```

Runner result: `30 PASS / 0 FAIL`.

# Boundaries

This PR does not audit, retag, land, or update any audit/status ledger.
It does not propose retained status. Parent theorem boundaries remain
open: P-ABJ, P-HY, P-COMP, P-REC, and `B-AXIS`.
