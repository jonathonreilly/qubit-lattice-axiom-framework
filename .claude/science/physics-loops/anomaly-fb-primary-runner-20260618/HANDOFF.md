# Handoff

This PR repairs the source-boundary unblock for
`anomaly_forces_time_fb_note_2026-05-17`.

The important change is not a new theorem. The F-B meta note now
declares:

- primary runner:
  `scripts/frontier_anomaly_forces_time_fb_framing_fix.py`
- cached output:
  `logs/runner-cache/frontier_anomaly_forces_time_fb_framing_fix.txt`

The runner now verifies the parent theorem as it exists on current main:
Step 3 computes the odd-time lower bound, Step 4 supplies the declared
`B-AXIS` upper bound, the theorem does not derive `B-AXIS`, and the
single-clock source is context only rather than a markdown dependency
edge.

Remaining science blockers stay open: P-ABJ, P-HY, P-COMP, P-REC, and
`B-AXIS`. The next highest-impact science moves are the YT neutral
carrier theorem, registrable readout theorem, and hierarchy `alpha_s`
attachment-observable theorem.
